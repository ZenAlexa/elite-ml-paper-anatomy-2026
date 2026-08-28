#!/usr/bin/env python3
"""Build an independent Figure/Table inventory from PDF caption lines."""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "data" / "processed" / "papers.csv"
SAMPLE = ROOT / "data" / "processed" / "analysis_sample.csv"
READING_VISUALS = ROOT / "reports" / "tables" / "visual_inventory.csv"
OUTPUT = ROOT / "reports" / "tables" / "visual_inventory_pdf.csv"
DISAGREEMENTS = ROOT / "reports" / "tables" / "visual_inventory_disagreements.csv"
CAPTION_RE = re.compile(
    r"(Figure|Fig\.?|Table)\s*((?:[A-Z]\.)?\d+(?:\.\d+)*|[A-Z]\d*|[IVXLCDM]+)\s*:",
    re.IGNORECASE,
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def clean_label(kind: str, number: str) -> str:
    prefix = "Figure" if kind.lower().startswith("fig") else "Table"
    return f"{prefix} {number.upper()}"


def canonical_label(kind: str, label: str) -> str:
    match = re.search(
        r"(?:Figure|Fig\.?|Table)\s*((?:[A-Z]\.)?\d+(?:\.\d+)*|[A-Z]\d*|[IVXLCDM]+)",
        label,
        re.IGNORECASE,
    )
    if match:
        return clean_label(kind, match.group(1))
    return re.sub(r"\s+", " ", label).strip()


def resolve_pdf_path(paper_id: str, metadata: dict[str, str], reading: dict[str, object]) -> Path:
    candidates = [metadata.get("pdf_path", "")]
    source_files = reading.get("source_files")
    if isinstance(source_files, dict):
        candidates.append(str(source_files.get("pdf", "")))
    candidates.extend((f"corpus/pdfs/{paper_id}.pdf", f"corpus/preprints/{paper_id}.pdf"))
    for candidate in candidates:
        if candidate and (ROOT / candidate).exists():
            return ROOT / candidate
    raise FileNotFoundError(f"no local PDF found for {paper_id}: {candidates}")


def caption_candidates(page: Any) -> list[dict[str, object]]:
    candidates = []
    # Search character geometry directly: two-column extraction can merge a
    # caption with unrelated prose on the same baseline and remove all spaces.
    for match in page.search(CAPTION_RE.pattern, regex=True, case=False):
        groups = match.get("groups") or ()
        if len(groups) < 2:
            continue
        label = clean_label(str(groups[0]), str(groups[1]))
        chars = match.get("chars") or []
        fonts = sorted({re.sub(r"^[A-Z]{6}\+", "", str(char.get("fontname", ""))) for char in chars})
        sizes = [float(char["size"]) for char in chars if char.get("size")]
        baseline_chars = [
            char
            for char in page.chars
            if float(char["x0"]) >= float(match["x0"])
            and abs(float(char["top"]) - float(match["top"])) <= 1.5
        ]
        caption_line = "".join(str(char.get("text", "")) for char in sorted(baseline_chars, key=lambda char: char["x0"]))
        caption_start = re.sub(CAPTION_RE, "", caption_line, count=1).strip()
        candidates.append(
            {
                "kind": "figure" if label.startswith("Figure") else "table",
                "label": label,
                "caption_start": caption_start,
                "x0": round(float(match["x0"]), 3),
                "top": round(float(match["top"]), 3),
                "x1": round(float(match["x1"]), 3),
                "bottom": round(float(match["bottom"]), 3),
                "caption_fonts": "|".join(fonts),
                "caption_size_median": round(sorted(sizes)[len(sizes) // 2], 3) if sizes else "",
            }
        )
    return candidates


def inventory_one_paper(task: tuple[dict[str, str], dict[str, str]]) -> list[dict[str, object]]:
    sample, metadata = task
    paper_id = sample["paper_id"]
    reading = json.loads((ROOT / "readings" / f"{paper_id}.json").read_text(encoding="utf-8"))
    pdf_path = resolve_pdf_path(paper_id, metadata, reading)
    appendix_start = int(reading["page_map"]["main_pages"]) + int(reading["page_map"]["reference_pages"]) + 1
    rows: list[dict[str, object]] = []
    seen: set[tuple[str, str]] = set()
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            candidates = caption_candidates(page)
            for candidate in candidates:
                identity = (str(candidate["kind"]), str(candidate["label"]))
                if identity in seen:
                    continue
                seen.add(identity)
                rows.append(
                    {
                        "paper_id": paper_id,
                        "conference": sample["conference"],
                        "analysis_stratum": sample["analysis_stratum"],
                        "kind": candidate["kind"],
                        "label": candidate["label"],
                        "page": page_number,
                        "placement": "appendix" if page_number >= appendix_start else "main",
                        "caption_start": candidate["caption_start"],
                        "x0": candidate["x0"],
                        "top": candidate["top"],
                        "x1": candidate["x1"],
                        "bottom": candidate["bottom"],
                        "caption_fonts": candidate["caption_fonts"],
                        "caption_size_median": candidate["caption_size_median"],
                    }
                )
            flush_cache = getattr(page, "flush_cache", None)
            if callable(flush_cache):
                flush_cache()
    return rows


def main() -> None:
    paper_meta = {row["paper_id"]: row for row in read_csv(PAPERS)}
    checkpoint = [row for row in read_csv(SAMPLE) if (ROOT / "readings" / f"{row['paper_id']}.json").exists()]
    known = defaultdict(list)
    for row in read_csv(READING_VISUALS):
        if row["kind"] in {"figure", "table"}:
            normalized = dict(row)
            normalized["label"] = canonical_label(row["kind"], row["label"])
            known[row["paper_id"]].append(normalized)

    rows: list[dict[str, object]] = []
    tasks = [(sample, paper_meta[sample["paper_id"]]) for sample in checkpoint]
    # A fresh worker per PDF bounds pdfminer/font cache growth across a heterogeneous
    # corpus while keeping the scan deterministic and easy to resume.
    with ProcessPoolExecutor(max_workers=1, max_tasks_per_child=1) as executor:
        for index, paper_rows in enumerate(executor.map(inventory_one_paper, tasks), start=1):
            rows.extend(paper_rows)
            if index % 25 == 0:
                print(f"inventoried {index}/{len(checkpoint)} papers", flush=True)

    fields = list(rows[0]) if rows else ["paper_id"]
    write_csv(OUTPUT, rows, fields)
    pdf_by_paper = defaultdict(set)
    for row in rows:
        pdf_by_paper[str(row["paper_id"])].add((str(row["kind"]), str(row["label"])))
    disagreement_rows = []
    for sample in checkpoint:
        paper_id = sample["paper_id"]
        reading_set = {(row["kind"], row["label"]) for row in known[paper_id]}
        pdf_set = pdf_by_paper[paper_id]
        missing = sorted(pdf_set - reading_set)
        not_detected = sorted(reading_set - pdf_set)
        disagreement_rows.append(
            {
                "paper_id": paper_id,
                "conference": sample["conference"],
                "reading_objects": len(reading_set),
                "pdf_caption_objects": len(pdf_set),
                "pdf_only_count": len(missing),
                "reading_only_count": len(not_detected),
                "pdf_only": "|".join(f"{kind}:{label}" for kind, label in missing),
                "reading_only": "|".join(f"{kind}:{label}" for kind, label in not_detected),
            }
        )
    write_csv(DISAGREEMENTS, disagreement_rows, list(disagreement_rows[0]))
    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(rows)} caption objects)")
    print(f"wrote {DISAGREEMENTS.relative_to(ROOT)} ({len(disagreement_rows)} papers)")


if __name__ == "__main__":
    main()

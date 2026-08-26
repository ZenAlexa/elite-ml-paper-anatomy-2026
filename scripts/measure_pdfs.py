#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import re
import subprocess
from pathlib import Path

from common import PROCESSED, ROOT, TEXT, read_csv, write_csv, write_json

FIELDS = [
    "paper_id",
    "pdf_pages",
    "main_end_page_provisional",
    "appendix_start_page_provisional",
    "total_words",
    "main_words_provisional",
    "appendix_words_provisional",
    "figure_captions",
    "table_captions",
    "algorithm_captions",
    "numbered_equations_provisional",
    "theorem_items",
    "limitation_mentions_main",
    "status",
    "error",
]

WORD = re.compile(r"\b[A-Za-z][A-Za-z'-]*\b")
REFERENCE_HEADING = re.compile(r"(?im)^\s*(?:\d+[. ]+)?references\s*$")
APPENDIX_HEADING = re.compile(r"(?im)^\s*(?:appendix|supplementary material|[A-Z][.]\s+.+)\s*$")
FIGURE = re.compile(r"(?im)^\s*(?:figure|fig[.])\s+([A-Z]?\d+)\s*[:.]?")
TABLE = re.compile(r"(?im)^\s*table\s+([A-Z]?\d+)\s*[:.]?")
ALGORITHM = re.compile(r"(?im)^\s*algorithm\s+([A-Z]?\d+)\s*[:.]?")
NUMBERED_EQUATION = re.compile(r"(?m)^.{0,180}\((\d{1,3})\)\s*$")
THEOREM = re.compile(r"(?i)\b(theorem|lemma|proposition|corollary)\s+[A-Z]?\d+")


def first_heading_page(pages: list[str], pattern: re.Pattern[str], start: int = 0) -> int | None:
    for index, page in enumerate(pages[start:], start=start):
        if pattern.search(page):
            return index + 1
    return None


def measure(row: dict[str, str], refresh: bool) -> dict[str, str]:
    output = {field: "" for field in FIELDS}
    output.update({"paper_id": row["paper_id"], "status": "failed", "error": ""})
    pdf = ROOT / row["pdf_path"]
    text_path = TEXT / f"{row['paper_id']}.txt"
    try:
        if refresh or not text_path.exists():
            text_path.parent.mkdir(parents=True, exist_ok=True)
            process = subprocess.run(
                ["pdftotext", "-layout", str(pdf), str(text_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=180,
            )
            if process.returncode:
                raise RuntimeError(process.stderr.strip() or f"pdftotext exited {process.returncode}")
        text = text_path.read_text(encoding="utf-8", errors="replace")
        pages = text.split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        reference_page = first_heading_page(pages, REFERENCE_HEADING)
        appendix_page = first_heading_page(pages, APPENDIX_HEADING, start=reference_page or 0)
        main_end = (reference_page - 1) if reference_page else len(pages)
        main_text = "\n".join(pages[:main_end])
        appendix_text = "\n".join(pages[(appendix_page - 1) :]) if appendix_page else ""
        output.update(
            {
                "pdf_pages": str(len(pages)),
                "main_end_page_provisional": str(main_end),
                "appendix_start_page_provisional": str(appendix_page or ""),
                "total_words": str(len(WORD.findall(text))),
                "main_words_provisional": str(len(WORD.findall(main_text))),
                "appendix_words_provisional": str(len(WORD.findall(appendix_text))),
                "figure_captions": str(len(set(FIGURE.findall(text)))),
                "table_captions": str(len(set(TABLE.findall(text)))),
                "algorithm_captions": str(len(set(ALGORITHM.findall(text)))),
                "numbered_equations_provisional": str(len(set(NUMBERED_EQUATION.findall(text)))),
                "theorem_items": str(len(THEOREM.findall(text))),
                "limitation_mentions_main": str(len(re.findall(r"(?i)\blimitations?\b", main_text))),
                "status": "measured",
            }
        )
    except Exception as exc:
        output["error"] = str(exc)
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--paper-id", action="append", default=[])
    args = parser.parse_args()
    rows = [row for row in read_csv(PROCESSED / "papers.csv") if row["pdf_status"] == "verified"]
    if args.paper_id:
        requested = set(args.paper_id)
        rows = [row for row in rows if row["paper_id"] in requested]
    output: list[dict[str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(measure, row, args.refresh) for row in rows]
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            output.append(future.result())
            if index % 50 == 0 or index == len(futures):
                print(f"measured {index}/{len(futures)}", flush=True)
    output.sort(key=lambda row: row["paper_id"])
    write_csv(PROCESSED / "auto_metrics.csv", output, FIELDS)
    failures = {row["paper_id"]: row["error"] for row in output if row["status"] != "measured"}
    write_json(PROCESSED / "measurement_failures.json", failures)
    if failures:
        raise SystemExit(f"{len(failures)} PDFs failed measurement")


if __name__ == "__main__":
    main()

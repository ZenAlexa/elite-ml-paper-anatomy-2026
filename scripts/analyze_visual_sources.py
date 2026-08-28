#!/usr/bin/env python3
"""Aggregate source-exact visual style literals at the paper level."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

from common import ROOT


INPUT = ROOT / "reports" / "tables" / "visual_source_style_metrics.csv"
AUDIT_DIR = ROOT / "visual_audits"
OUTPUT = ROOT / "reports" / "tables" / "visual_source_style_summary.csv"
LIST_FIELDS = (
    "tools",
    "hex_colors",
    "figsizes_inches",
    "font_sizes_pt",
    "line_widths_pt",
    "alpha_values",
    "marker_literals",
    "style_literals",
    "dpi_values",
    "export_formats",
)
FLAG_FIELDS = (
    "uses_grid",
    "uses_legend",
    "uses_errorbar",
    "uses_fill_between",
    "uses_log_axis",
    "uses_booktabs",
    "uses_resizebox",
    "uses_small_font",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-unverified-candidates", action="store_true")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    args = parse_args()
    source_rows = read_csv(INPUT)
    audited_papers = set()
    verified_source_papers = set()
    for path in AUDIT_DIR.glob("*.json"):
        audit = json.loads(path.read_text(encoding="utf-8"))
        paper_id = audit["paper_id"]
        audited_papers.add(paper_id)
        if audit["source_acquisition"]["status"] in {"exact_visual_source", "partial_visual_source"}:
            verified_source_papers.add(paper_id)
    if args.allow_unverified_candidates:
        verified_source_papers = {row["paper_id"] for row in source_rows}
    selected = [row for row in source_rows if row["paper_id"] in verified_source_papers]
    source_style_papers = {row["paper_id"] for row in selected}
    file_counts: dict[tuple[str, str], int] = Counter()
    papers_for: dict[tuple[str, str], set[str]] = defaultdict(set)
    for row in selected:
        for field in LIST_FIELDS:
            for value in {item.strip() for item in row[field].split("|") if item.strip()}:
                key = (field, value)
                file_counts[key] += 1
                papers_for[key].add(row["paper_id"])
        for field in FLAG_FIELDS:
            value = "present" if row[field] == "1" else "absent"
            key = (field, value)
            file_counts[key] += 1
            papers_for[key].add(row["paper_id"])
    output_rows = []
    denominator = len(source_style_papers)
    for (dimension, value), count in sorted(
        file_counts.items(), key=lambda item: (item[0][0], -len(papers_for[item[0]]), -item[1], item[0][1])
    ):
        paper_count = len(papers_for[(dimension, value)])
        output_rows.append(
            {
                "dimension": dimension,
                "value": value,
                "file_count": count,
                "papers_present": paper_count,
                "verified_source_papers_with_style_files": denominator,
                "paper_prevalence_with_verified_source": round(paper_count / denominator, 6) if denominator else 0,
                "audited_papers": len(audited_papers),
                "paper_prevalence_all_audited": round(paper_count / len(audited_papers), 6) if audited_papers else 0,
            }
        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        fields = list(output_rows[0]) if output_rows else ["dimension"]
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)
    print(
        json.dumps(
            {
                "audited_papers": len(audited_papers),
                "verified_source_papers": len(verified_source_papers),
                "verified_source_papers_with_style_files": denominator,
                "source_files": len(selected),
                "summary_rows": len(output_rows),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

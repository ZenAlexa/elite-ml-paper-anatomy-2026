#!/usr/bin/env python3
"""Measure the effective ICLR text and column widths from cohort PDFs."""

from __future__ import annotations

import csv
import json
import statistics
from pathlib import Path

import pdfplumber


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "corpus" / "pdfs"
OUTPUT = ROOT / "reports" / "tables" / "iclr_pdf_layout_measurements.csv"
READING_INDEX = ROOT / "reports" / "tables" / "reading_index.csv"


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def main() -> None:
    with READING_INDEX.open(newline="", encoding="utf-8") as handle:
        target_ids = {
            row["paper_id"]
            for row in csv.DictReader(handle)
            if row["checkpoint_250"] == "yes" and row["conference"] == "ICLR"
        }
    rows: list[dict[str, object]] = []
    for path in sorted(PDF_DIR.glob("iclr-2026-*.pdf")):
        if path.stem not in target_ids:
            continue
        with pdfplumber.open(path) as pdf:
            if len(pdf.pages) < 2:
                continue
            page = pdf.pages[1]
            midpoint = float(page.width) / 2
            words = page.extract_words()
            left = [word for word in words if float(word["x1"]) < midpoint]
            right = [word for word in words if float(word["x0"]) > midpoint]
            if len(left) < 30 or len(right) < 30:
                continue
            # Robust edges suppress centered equations or annotations that enter
            # the gutter while preserving the repeated body-column starts.
            left_min = quantile([float(word["x0"]) for word in left], 0.05)
            left_max = quantile([float(word["x1"]) for word in left], 0.95)
            right_min = quantile([float(word["x0"]) for word in right], 0.025)
            right_max = quantile([float(word["x1"]) for word in right], 0.95)
            text_width = right_max - left_min
            column_gap = right_min - left_max
            rows.append(
                {
                    "paper_id": path.stem,
                    "page": 2,
                    "page_width_pt": round(float(page.width), 3),
                    "text_left_pt": round(left_min, 3),
                    "text_right_pt": round(right_max, 3),
                    "text_width_pt": round(text_width, 3),
                    "left_column_width_pt": round(left_max - left_min, 3),
                    "right_column_width_pt": round(right_max - right_min, 3),
                    "column_gap_pt": round(column_gap, 3),
                    "symmetric_column_width_pt": round((text_width - column_gap) / 2, 3),
                }
            )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    summary = {}
    for field in (
        "text_width_pt", "left_column_width_pt", "right_column_width_pt",
        "column_gap_pt", "symmetric_column_width_pt",
    ):
        values = [float(row[field]) for row in rows]
        summary[field] = {
            "median_pt": round(statistics.median(values), 3),
            "median_in": round(statistics.median(values) / 72, 4),
        }
    print(json.dumps({"papers": len(rows), "summary": summary}, indent=2))


if __name__ == "__main__":
    main()

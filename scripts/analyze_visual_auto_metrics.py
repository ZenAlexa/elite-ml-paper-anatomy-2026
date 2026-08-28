#!/usr/bin/env python3
"""Summarize PDF-measured visual metrics with paper and conference balancing."""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path

from common import PROCESSED, ROOT, load_complete_reading, read_csv


INPUT = ROOT / "reports" / "tables" / "visual_object_auto_metrics.csv"
NUMERIC_OUTPUT = ROOT / "reports" / "tables" / "visual_auto_numeric_summary.csv"
CATEGORICAL_OUTPUT = ROOT / "reports" / "tables" / "visual_auto_categorical_summary.csv"
NUMERIC_FIELDS = (
    "caption_words",
    "caption_sentences",
    "caption_font_size_median",
    "caption_self_contained_score",
    "internal_font_size_min",
    "internal_font_size_median",
    "internal_font_size_max",
    "color_count_auto",
    "chromatic_pixel_share",
    "panels_auto",
    "complexity_auto",
    "table_rows_auto",
    "table_columns_auto",
    "table_header_levels_auto",
)
CATEGORICAL_FIELDS = (
    "width",
    "types_auto",
    "caption_headline_bold",
    "caption_has_setup",
    "caption_has_encoding_key",
    "caption_has_main_finding",
    "caption_has_uncertainty_definition",
    "caption_has_appendix_pointer",
    "color_mode_auto",
)


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        fields = list(rows[0]) if rows else ["scope"]
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def scopes(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    return {
        "all": rows,
        "figure": [row for row in rows if row["kind"] == "figure"],
        "table": [row for row in rows if row["kind"] == "table"],
        "main": [row for row in rows if row["placement"] == "main"],
        "appendix": [row for row in rows if row["placement"] == "appendix"],
        "main_figure": [row for row in rows if row["kind"] == "figure" and row["placement"] == "main"],
        "appendix_figure": [row for row in rows if row["kind"] == "figure" and row["placement"] == "appendix"],
        "main_table": [row for row in rows if row["kind"] == "table" and row["placement"] == "main"],
        "appendix_table": [row for row in rows if row["kind"] == "table" and row["placement"] == "appendix"],
    }


def conference_equal(values: list[tuple[str, float]]) -> float:
    grouped: dict[str, list[float]] = defaultdict(list)
    for conference, value in values:
        grouped[conference].append(value)
    return statistics.fmean(statistics.fmean(items) for items in grouped.values()) if grouped else 0.0


def split_values(row: dict[str, str], field: str) -> list[str]:
    value = row[field]
    if not value:
        return []
    if field == "types_auto":
        return [item for item in value.split("|") if item]
    return [value]


def main() -> None:
    rows = read_csv(INPUT)
    samples = [
        row
        for row in read_csv(PROCESSED / "analysis_sample.csv")
        if load_complete_reading(row["paper_id"]) is not None
    ]
    paper_conference = {row["paper_id"]: row["conference"] for row in samples}
    all_papers = sorted(paper_conference)
    numeric_rows: list[dict[str, object]] = []
    categorical_rows: list[dict[str, object]] = []
    for scope, selected in scopes(rows).items():
        by_paper: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in selected:
            by_paper[row["paper_id"]].append(row)
        for field in NUMERIC_FIELDS:
            values: list[float] = []
            paper_means: list[tuple[str, float]] = []
            for paper_id in all_papers:
                paper_values = []
                for row in by_paper.get(paper_id, []):
                    try:
                        paper_values.append(float(row[field]))
                    except (TypeError, ValueError):
                        pass
                values.extend(paper_values)
                if paper_values:
                    paper_means.append((paper_conference[paper_id], statistics.fmean(paper_values)))
            if not values:
                continue
            numeric_rows.append(
                {
                    "scope": scope,
                    "metric": field,
                    "objects_measured": len(values),
                    "papers_measured": len(paper_means),
                    "object_mean": round(statistics.fmean(values), 6),
                    "object_median": round(statistics.median(values), 6),
                    "object_q1": round(quantile(values, 0.25), 6),
                    "object_q3": round(quantile(values, 0.75), 6),
                    "paper_equal_mean": round(statistics.fmean(value for _, value in paper_means), 6),
                    "conference_equal_paper_mean": round(conference_equal(paper_means), 6),
                }
            )
        for field in CATEGORICAL_FIELDS:
            vocabulary = sorted({value for row in selected for value in split_values(row, field)})
            for value in vocabulary:
                hits = [row for row in selected if value in split_values(row, field)]
                paper_values: list[tuple[str, float]] = []
                present = set()
                for paper_id in all_papers:
                    paper_rows = by_paper.get(paper_id, [])
                    count = sum(value in split_values(row, field) for row in paper_rows)
                    if count:
                        present.add(paper_id)
                    paper_values.append(
                        (paper_conference[paper_id], count / len(paper_rows) if paper_rows else 0.0)
                    )
                categorical_rows.append(
                    {
                        "scope": scope,
                        "dimension": field,
                        "value": value,
                        "objects": len(selected),
                        "object_count": len(hits),
                        "object_share": round(len(hits) / len(selected), 6) if selected else 0,
                        "papers": len(all_papers),
                        "papers_present": len(present),
                        "paper_prevalence": round(len(present) / len(all_papers), 6),
                        "paper_normalized_object_share": round(
                            statistics.fmean(item for _, item in paper_values), 6
                        ),
                        "conference_equal_paper_normalized_share": round(conference_equal(paper_values), 6),
                    }
                )
    write_csv(NUMERIC_OUTPUT, numeric_rows)
    write_csv(CATEGORICAL_OUTPUT, categorical_rows)
    print(
        f"wrote {NUMERIC_OUTPUT.relative_to(ROOT)} ({len(numeric_rows)} rows) and "
        f"{CATEGORICAL_OUTPUT.relative_to(ROOT)} ({len(categorical_rows)} rows)"
    )


if __name__ == "__main__":
    main()

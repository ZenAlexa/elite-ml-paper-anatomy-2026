#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import statistics
from collections import Counter, defaultdict

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv, write_json


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    metrics = {row["paper_id"]: row for row in read_csv(PROCESSED / "auto_metrics.csv")} if (PROCESSED / "auto_metrics.csv").exists() else {}
    readings = {}
    for row in papers:
        reading = load_complete_reading(row["paper_id"])
        if reading is not None:
            readings[row["paper_id"]] = reading
    coverage = []
    for conference in ("ICLR", "ICML", "NeurIPS"):
        eligible = [row for row in papers if row["conference"] == conference]
        coverage.append(
            {
                "conference": conference,
                "eligible_papers": len(eligible),
                "verified_pdfs": sum(row["pdf_status"] == "verified" for row in eligible),
                "automatic_measurements": sum(row["paper_id"] in metrics for row in eligible),
                "completed_independent_readings": sum(row["paper_id"] in readings for row in eligible),
                "status": "not_yet_observed" if conference == "NeurIPS" else "observed",
            }
        )
    write_csv(
        ROOT / "reports" / "tables" / "coverage.csv",
        coverage,
        ["conference", "eligible_papers", "verified_pdfs", "automatic_measurements", "completed_independent_readings", "status"],
    )
    write_json(
        ROOT / "reports" / "analysis_status.json",
        {
            "schema_version": "analysis-status.v1",
            "coverage": coverage,
            "aggregate_ready": all(
                row["completed_independent_readings"] == row["eligible_papers"]
                for row in coverage
                if row["status"] == "observed"
            ),
        },
    )
    print(json.dumps(coverage, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

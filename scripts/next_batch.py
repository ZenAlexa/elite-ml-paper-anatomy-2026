#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import PROCESSED, ROOT, read_csv


STRATUM_ORDER = {"outstanding": 0, "oral": 1, "spotlight": 2}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select the next unclaimed verified papers for independent reading.")
    parser.add_argument("--conference", choices=("ICLR", "ICML", "NeurIPS"), default="ICLR")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--exclude", action="append", default=[], metavar="PAPER_ID")
    return parser.parse_args()


def model_route(metric: dict[str, str]) -> tuple[str, str]:
    pages = int(metric.get("pdf_pages") or 0)
    equations = int(metric.get("numbered_equations_provisional") or 0)
    theorem_items = int(metric.get("theorem_items") or 0)
    if pages >= 35 or equations >= 15 or theorem_items >= 3:
        return "gpt-5.6-terra", "max"
    return "gpt-5.6-luna", "max"


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be positive")
    papers = read_csv(PROCESSED / "papers.csv")
    manifest = {row["paper_id"]: row for row in read_csv(PROCESSED / "pdf_manifest.csv")}
    metrics = {row["paper_id"]: row for row in read_csv(PROCESSED / "auto_metrics.csv")}
    excluded = set(args.exclude)
    candidates = []
    for paper in papers:
        paper_id = paper["paper_id"]
        if paper["conference"] != args.conference or paper_id in excluded:
            continue
        if manifest.get(paper_id, {}).get("status") != "verified":
            continue
        if (ROOT / "readings" / f"{paper_id}.json").exists() or (ROOT / "readings" / f"{paper_id}.md").exists():
            continue
        metric = metrics.get(paper_id, {})
        pages = int(metric.get("pdf_pages") or manifest[paper_id].get("pages") or 0)
        equations = int(metric.get("numbered_equations_provisional") or 0)
        theorem_items = int(metric.get("theorem_items") or 0)
        model, reasoning_effort = model_route(metric)
        candidates.append(
            {
                "paper_id": paper_id,
                "conference": paper["conference"],
                "analysis_stratum": paper["analysis_stratum"],
                "selection_flags": paper["selection_flags"],
                "title": paper["title"],
                "openreview_url": paper["openreview_url"],
                "pdf_path": paper["pdf_path"],
                "pdf_pages": pages,
                "numbered_equations_provisional": equations,
                "theorem_items_provisional": theorem_items,
                "recommended_model": model,
                "reasoning_effort": reasoning_effort,
                "routing_score": round(pages + 0.5 * equations + 2 * theorem_items, 2),
            }
        )
    candidates.sort(
        key=lambda item: (
            STRATUM_ORDER[item["analysis_stratum"]],
            item["routing_score"],
            item["paper_id"],
        )
    )
    print(json.dumps(candidates[: args.limit], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

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
    parser.add_argument(
        "--source",
        choices=("official", "any"),
        default="any",
        help="Use a verified preprint when an official PDF is unavailable.",
    )
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--exclude", action="append", default=[], metavar="PAPER_ID")
    parser.add_argument(
        "--all-eligible",
        action="store_true",
        help="Ignore analysis_sample.csv and dispatch from the full verified corpus.",
    )
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
    preprint_manifest_path = PROCESSED / "preprint_manifest.csv"
    preprint_metrics_path = PROCESSED / "preprint_auto_metrics.csv"
    preprint_manifest = (
        {row["paper_id"]: row for row in read_csv(preprint_manifest_path)}
        if preprint_manifest_path.exists()
        else {}
    )
    preprint_metrics = (
        {row["paper_id"]: row for row in read_csv(preprint_metrics_path)}
        if preprint_metrics_path.exists()
        else {}
    )
    sample_path = PROCESSED / "analysis_sample.csv"
    sample = {row["paper_id"]: row for row in read_csv(sample_path)} if sample_path.exists() else {}
    excluded = set(args.exclude)
    candidates = []
    for paper in papers:
        paper_id = paper["paper_id"]
        if paper["conference"] != args.conference or paper_id in excluded:
            continue
        if sample and not args.all_eligible and paper_id not in sample:
            continue
        official = manifest.get(paper_id, {})
        preprint = preprint_manifest.get(paper_id, {})
        if official.get("status") == "verified":
            source = official
            metric = metrics.get(paper_id, {})
            source_kind = "official_pdf"
        elif args.source == "any" and preprint.get("status") == "verified":
            source = preprint
            metric = preprint_metrics.get(paper_id, {})
            source_kind = "verified_preprint"
        else:
            continue
        if (ROOT / "readings" / f"{paper_id}.json").exists() or (ROOT / "readings" / f"{paper_id}.md").exists():
            continue
        pages = int(metric.get("pdf_pages") or source.get("pages") or 0)
        equations = int(metric.get("numbered_equations_provisional") or 0)
        theorem_items = int(metric.get("theorem_items") or 0)
        model, reasoning_effort = model_route(metric)
        candidates.append(
            {
                "paper_id": paper_id,
                "conference": paper["conference"],
                "analysis_stratum": paper["analysis_stratum"],
                "selection_flags": paper["selection_flags"],
                "selection_role": sample.get(paper_id, {}).get("selection_role", "extended"),
                "title": paper["title"],
                "openreview_url": paper["openreview_url"],
                "pdf_path": source["pdf_path"],
                "pdf_url": source["pdf_url"],
                "source_kind": source_kind,
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

#!/usr/bin/env python3
from __future__ import annotations

import random

from common import PROCESSED, read_csv, write_csv


SEED = "elite-ml-paper-anatomy-2026-primary-v1"
TARGETS = {
    ("ICLR", "outstanding"): "all",
    ("ICLR", "oral"): 98,
    ("ICML", "outstanding"): "all",
    ("ICML", "oral"): 49,
    ("ICML", "spotlight"): 49,
}


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    official = {row["paper_id"]: row for row in read_csv(PROCESSED / "pdf_manifest.csv")}
    preprint = {row["paper_id"]: row for row in read_csv(PROCESSED / "preprint_manifest.csv")}
    rng = random.Random(SEED)
    rows = []
    for (conference, stratum), requested in TARGETS.items():
        eligible = []
        for paper in papers:
            if paper["conference"] != conference or paper["analysis_stratum"] != stratum:
                continue
            paper_id = paper["paper_id"]
            if official.get(paper_id, {}).get("status") == "verified":
                source_kind = "official_pdf"
                source_path = official[paper_id]["pdf_path"]
            elif preprint.get(paper_id, {}).get("status") == "verified":
                source_kind = "verified_preprint"
                source_path = preprint[paper_id]["pdf_path"]
            else:
                continue
            eligible.append((paper, source_kind, source_path))
        eligible.sort(key=lambda item: item[0]["paper_id"])
        target = len(eligible) if requested == "all" else int(requested)
        if len(eligible) < target:
            raise SystemExit(f"insufficient verified papers for {conference}/{stratum}: {len(eligible)} < {target}")
        selected = eligible if requested == "all" else rng.sample(eligible, target)
        probability = target / len(eligible)
        for paper, source_kind, source_path in sorted(selected, key=lambda item: item[0]["paper_id"]):
            rows.append(
                {
                    "paper_id": paper["paper_id"],
                    "conference": conference,
                    "analysis_stratum": stratum,
                    "selection_role": "census_outstanding" if requested == "all" else "stratified_random_sample",
                    "eligible_verified_in_stratum": len(eligible),
                    "target_in_stratum": target,
                    "selection_probability": round(probability, 9),
                    "source_kind": source_kind,
                    "source_path": source_path,
                    "sampling_seed": SEED,
                }
            )
    write_csv(
        PROCESSED / "analysis_sample.csv",
        rows,
        [
            "paper_id",
            "conference",
            "analysis_stratum",
            "selection_role",
            "eligible_verified_in_stratum",
            "target_in_stratum",
            "selection_probability",
            "source_kind",
            "source_path",
            "sampling_seed",
        ],
    )
    print(f"sample={len(rows)} seed={SEED}")


if __name__ == "__main__":
    main()

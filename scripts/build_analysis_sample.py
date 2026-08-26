#!/usr/bin/env python3
from __future__ import annotations

import random
from collections import defaultdict

from common import PROCESSED, read_csv, write_csv


COHORTS = (
    (
        "foundation_200",
        1,
        "elite-ml-paper-anatomy-2026-primary-v1",
        {
            ("ICLR", "outstanding"): "all",
            ("ICLR", "oral"): 98,
            ("ICML", "outstanding"): "all",
            ("ICML", "oral"): 49,
            ("ICML", "spotlight"): 49,
        },
    ),
    (
        "replication_200",
        2,
        "elite-ml-paper-anatomy-2026-replication-v1",
        {
            ("ICLR", "oral"): 100,
            ("ICML", "oral"): 50,
            ("ICML", "spotlight"): 50,
        },
    ),
)


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    official = {row["paper_id"]: row for row in read_csv(PROCESSED / "pdf_manifest.csv")}
    preprint = {row["paper_id"]: row for row in read_csv(PROCESSED / "preprint_manifest.csv")}
    eligible_by_group: dict[tuple[str, str], list[tuple[dict[str, str], str, str]]] = defaultdict(list)
    for paper in papers:
        paper_id = paper["paper_id"]
        if official.get(paper_id, {}).get("status") == "verified":
            source_kind = "official_pdf"
            source_path = official[paper_id]["pdf_path"]
        elif preprint.get(paper_id, {}).get("status") == "verified":
            source_kind = "verified_preprint"
            source_path = preprint[paper_id]["pdf_path"]
        else:
            continue
        eligible_by_group[(paper["conference"], paper["analysis_stratum"])].append(
            (paper, source_kind, source_path)
        )
    for eligible in eligible_by_group.values():
        eligible.sort(key=lambda item: item[0]["paper_id"])

    combined_targets: dict[tuple[str, str], int] = defaultdict(int)
    for _, _, _, targets in COHORTS:
        for group, requested in targets.items():
            combined_targets[group] += (
                len(eligible_by_group[group]) if requested == "all" else int(requested)
            )

    selected_ids: set[str] = set()
    rows = []
    for cohort, cohort_order, seed, targets in COHORTS:
        rng = random.Random(seed)
        for (conference, stratum), requested in targets.items():
            eligible = eligible_by_group[(conference, stratum)]
            remaining = [item for item in eligible if item[0]["paper_id"] not in selected_ids]
            target = len(remaining) if requested == "all" else int(requested)
            if len(remaining) < target:
                raise SystemExit(
                    f"insufficient remaining verified papers for {cohort} {conference}/{stratum}: "
                    f"{len(remaining)} < {target}"
                )
            selected = remaining if requested == "all" else rng.sample(remaining, target)
            cohort_probability = target / len(remaining)
            combined_probability = combined_targets[(conference, stratum)] / len(eligible)
            for paper, source_kind, source_path in sorted(selected, key=lambda item: item[0]["paper_id"]):
                selected_ids.add(paper["paper_id"])
                rows.append(
                    {
                        "paper_id": paper["paper_id"],
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "sample_cohort": cohort,
                        "cohort_order": cohort_order,
                        "selection_role": "census_outstanding" if requested == "all" else "stratified_random_sample",
                        "eligible_verified_in_stratum": len(eligible),
                        "remaining_eligible_at_draw": len(remaining),
                        "target_in_stratum": target,
                        "combined_target_in_stratum": combined_targets[(conference, stratum)],
                        "cohort_selection_probability": round(cohort_probability, 9),
                        "selection_probability": round(combined_probability, 9),
                        "source_kind": source_kind,
                        "source_path": source_path,
                        "sampling_seed": seed,
                    }
                )
    write_csv(
        PROCESSED / "analysis_sample.csv",
        rows,
        [
            "paper_id",
            "conference",
            "analysis_stratum",
            "sample_cohort",
            "cohort_order",
            "selection_role",
            "eligible_verified_in_stratum",
            "remaining_eligible_at_draw",
            "target_in_stratum",
            "combined_target_in_stratum",
            "cohort_selection_probability",
            "selection_probability",
            "source_kind",
            "source_path",
            "sampling_seed",
        ],
    )
    print(
        "sample={} cohorts={}".format(
            len(rows),
            ",".join(f"{cohort}:{sum(row['sample_cohort'] == cohort for row in rows)}" for cohort, *_ in COHORTS),
        )
    )


if __name__ == "__main__":
    main()

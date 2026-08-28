#!/usr/bin/env python3
"""Build the integer-ceiling ICLR paper-planning table from checkpoint 250."""

from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "tables" / "checkpoint_250_module_summary.csv"
OUTPUT = ROOT / "reports" / "tables" / "iclr_full_paper_blueprint.csv"

MAIN_ORDER = [
    "abstract",
    "introduction",
    "related_work",
    "method",
    "theory",
    "experimental_design",
    "results",
    "ablation",
    "conclusion",
    "limitations",
    "other",
]

# The execution budget maps the conference-equal observations onto a nine-page
# ICLR main body: 6 figures, 4 tables, 1 algorithm, and 13 displayed equations. Sparse
# per-module means remain visible in separate observed-ceiling columns.
EXECUTION_BUDGET = {
    "abstract": (0, 0, 0, 0),
    "introduction": (1, 0, 0, 0),
    "related_work": (0, 0, 0, 0),
    "method": (1, 0, 1, 6),
    "theory": (0, 0, 0, 6),
    "experimental_design": (0, 1, 0, 0),
    "results": (3, 2, 0, 1),
    "ablation": (1, 1, 0, 0),
    "conclusion": (0, 0, 0, 0),
    "limitations": (0, 0, 0, 0),
    "other": (0, 0, 0, 0),
    "appendix": (8, 7, 1, 20),
}


def ceiling(value: str | float) -> int:
    return math.ceil(float(value))


def main() -> None:
    with SOURCE.open(newline="", encoding="utf-8") as handle:
        source_rows = {row["module"]: row for row in csv.DictReader(handle)}

    rows: list[dict[str, object]] = []
    for module in [*MAIN_ORDER, "appendix"]:
        source = source_rows[module]
        if module == "appendix":
            share_ceiling = ""
            iclr_share_ceiling = ""
            draft_words = ""
        else:
            share_ceiling = ceiling(
                float(source["conference_equal_normalized_word_share"]) * 100
            )
            iclr_share_ceiling = ceiling(
                float(source["iclr_normalized_word_share"]) * 100
            )
            draft_words = ceiling(5220 * share_ceiling / 100)

        recommended = EXECUTION_BUDGET[module]
        rows.append(
            {
                "module": module,
                "papers_present": source["papers_present"],
                "presence_percent_ceil": ceiling(
                    float(source["conference_equal_presence_share"]) * 100
                ),
                "conference_equal_share_percent_ceil": share_ceiling,
                "iclr_share_percent_ceil": iclr_share_ceiling,
                "draft_words_at_5220_ceil": draft_words,
                "observed_mean_words_ceil": ceiling(source["estimated_words_mean"]),
                "observed_figures_mean_ceil": ceiling(
                    source["conference_equal_figures_mean"]
                ),
                "observed_tables_mean_ceil": ceiling(
                    source["conference_equal_tables_mean"]
                ),
                "observed_algorithms_mean_ceil": ceiling(
                    source["conference_equal_algorithms_mean"]
                ),
                "observed_equations_mean_ceil": ceiling(
                    source["conference_equal_displayed_equations_mean"]
                ),
                "execution_figures": recommended[0],
                "execution_tables": recommended[1],
                "execution_algorithms": recommended[2],
                "execution_equations": recommended[3],
            }
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {OUTPUT.relative_to(ROOT)} ({len(rows)} rows)")


if __name__ == "__main__":
    main()

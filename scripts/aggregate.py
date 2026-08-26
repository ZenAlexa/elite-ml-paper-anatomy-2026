#!/usr/bin/env python3
from __future__ import annotations

import json
import statistics
from collections import Counter, defaultdict

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv, write_json

MODULE_FIELDS = [
    "paper_id",
    "conference",
    "analysis_stratum",
    "module",
    "status",
    "estimated_words",
    "main_word_share",
    "figures",
    "tables",
    "algorithms",
    "displayed_equations",
]


def describe(values: list[float]) -> dict[str, object]:
    if not values:
        return {"n": 0, "mean": "", "median": "", "q1": "", "q3": "", "min": "", "max": ""}
    ordered = sorted(values)
    if len(ordered) == 1:
        q1 = q3 = ordered[0]
    else:
        q1, _, q3 = statistics.quantiles(ordered, n=4, method="inclusive")
    return {
        "n": len(ordered),
        "mean": round(statistics.fmean(ordered), 6),
        "median": round(statistics.median(ordered), 6),
        "q1": round(q1, 6),
        "q3": round(q3, 6),
        "min": round(ordered[0], 6),
        "max": round(ordered[-1], 6),
    }


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    metrics = {row["paper_id"]: row for row in read_csv(PROCESSED / "auto_metrics.csv")} if (PROCESSED / "auto_metrics.csv").exists() else {}
    preprints = (
        {row["paper_id"]: row for row in read_csv(PROCESSED / "preprint_manifest.csv")}
        if (PROCESSED / "preprint_manifest.csv").exists()
        else {}
    )
    readings = {}
    for row in papers:
        reading = load_complete_reading(row["paper_id"])
        if reading is not None:
            readings[row["paper_id"]] = reading
    catalog = {row["paper_id"]: row for row in papers}
    coverage = []
    for conference in ("ICLR", "ICML", "NeurIPS"):
        eligible = [row for row in papers if row["conference"] == conference]
        coverage.append(
            {
                "conference": conference,
                "eligible_papers": len(eligible),
                "verified_pdfs": sum(row["pdf_status"] == "verified" for row in eligible),
                "provisional_preprints": sum(
                    preprints.get(row["paper_id"], {}).get("status") == "verified" for row in eligible
                ),
                "automatic_measurements": sum(row["paper_id"] in metrics for row in eligible),
                "completed_independent_readings": sum(row["paper_id"] in readings for row in eligible),
                "status": "not_yet_observed" if conference == "NeurIPS" else "observed",
            }
        )
    write_csv(
        ROOT / "reports" / "tables" / "coverage.csv",
        coverage,
        [
            "conference",
            "eligible_papers",
            "verified_pdfs",
            "provisional_preprints",
            "automatic_measurements",
            "completed_independent_readings",
            "status",
        ],
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

    paper_metrics: list[dict[str, object]] = []
    module_metrics: list[dict[str, object]] = []
    abstract_functions: list[dict[str, object]] = []
    visuals: list[dict[str, object]] = []
    theory_items: list[dict[str, object]] = []
    appendix_items: list[dict[str, object]] = []
    claim_rows: list[dict[str, object]] = []
    for paper_id, reading in readings.items():
        paper = catalog[paper_id]
        page_map = reading["page_map"]
        main_pages = float(page_map["main_pages"])
        appendix_pages = float(page_map["appendix_pages"])
        module_by_name = {item["module"]: item for item in reading["module_metrics"]}
        main_words = sum(
            int(item["estimated_words"])
            for item in reading["module_metrics"]
            if item["module"] != "appendix" and item.get("main_word_share") is not None
        )
        appendix_words = int(module_by_name.get("appendix", {}).get("estimated_words", 0))
        functions = [function for sentence in reading["abstract_sentences"] for function in sentence["functions"]]
        paper_metrics.append(
            {
                "paper_id": paper_id,
                "conference": paper["conference"],
                "analysis_stratum": paper["analysis_stratum"],
                "selection_flags": paper["selection_flags"],
                "main_pages": page_map["main_pages"],
                "reference_pages": page_map["reference_pages"],
                "appendix_pages": page_map["appendix_pages"],
                "appendix_page_ratio": round(appendix_pages / main_pages, 6) if main_pages else "",
                "main_estimated_words": main_words,
                "appendix_estimated_words": appendix_words,
                "appendix_word_ratio": round(appendix_words / main_words, 6) if main_words else "",
                "abstract_sentences": len(reading["abstract_sentences"]),
                "abstract_has_quantitative_result": "quantitative_result" in functions,
                "abstract_has_qualitative_result": "qualitative_result" in functions,
                "abstract_has_theory": "theory" in functions,
                "abstract_has_limitation": "limitation" in functions,
                "visuals_total": len(reading["visual_inventory"]),
                "theory_items_total": len(reading["equation_theory_inventory"]),
                "claims_closed": sum(item["status"] == "closed" for item in reading["claim_closure"]),
                "claims_total": len(reading["claim_closure"]),
                "limitations_recorded": len(reading["limitations"]),
            }
        )
        for item in reading["module_metrics"]:
            module_metrics.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    **item,
                }
            )
        sentence_count = len(reading["abstract_sentences"])
        function_counts = Counter(functions)
        for function in sorted(function_counts):
            abstract_functions.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "function": function,
                    "sentence_mentions": function_counts[function],
                    "abstract_sentences": sentence_count,
                    "present": True,
                }
            )
        for item in reading["visual_inventory"]:
            visuals.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "kind": item["kind"],
                    "module": item["module"],
                    "label": item["label"],
                    "page": item["page"],
                    "purpose": item["purpose"],
                }
            )
        for item in reading["equation_theory_inventory"]:
            theory_items.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "kind": item["kind"],
                    "module": item["module"],
                    "role": item["role"],
                    "label": item["label"],
                    "page": item["page"],
                }
            )
        for item in reading["appendix_inventory"]:
            appendix_items.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "category": item["category"],
                    "title": item["title"],
                    "start_page": item["start_page"],
                    "end_page": item["end_page"],
                    "pages_spanned": item["end_page"] - item["start_page"] + 1,
                    "main_text_call_count": len(item["main_text_calls"]),
                }
            )
        for item in reading["claim_closure"]:
            claim_rows.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "status": item["status"],
                    "claim": item["claim"],
                    "origin": item["origin"],
                }
            )

    table_dir = ROOT / "reports" / "tables"
    write_csv(
        table_dir / "paper_metrics.csv",
        paper_metrics,
        [
            "paper_id",
            "conference",
            "analysis_stratum",
            "selection_flags",
            "main_pages",
            "reference_pages",
            "appendix_pages",
            "appendix_page_ratio",
            "main_estimated_words",
            "appendix_estimated_words",
            "appendix_word_ratio",
            "abstract_sentences",
            "abstract_has_quantitative_result",
            "abstract_has_qualitative_result",
            "abstract_has_theory",
            "abstract_has_limitation",
            "visuals_total",
            "theory_items_total",
            "claims_closed",
            "claims_total",
            "limitations_recorded",
        ],
    )
    write_csv(table_dir / "module_metrics.csv", module_metrics, MODULE_FIELDS)
    write_csv(
        table_dir / "abstract_functions.csv",
        abstract_functions,
        ["paper_id", "conference", "analysis_stratum", "function", "sentence_mentions", "abstract_sentences", "present"],
    )
    write_csv(
        table_dir / "visual_inventory.csv",
        visuals,
        ["paper_id", "conference", "analysis_stratum", "kind", "module", "label", "page", "purpose"],
    )
    write_csv(
        table_dir / "theory_inventory.csv",
        theory_items,
        ["paper_id", "conference", "analysis_stratum", "kind", "module", "role", "label", "page"],
    )
    write_csv(
        table_dir / "appendix_inventory.csv",
        appendix_items,
        ["paper_id", "conference", "analysis_stratum", "category", "title", "start_page", "end_page", "pages_spanned", "main_text_call_count"],
    )
    write_csv(
        table_dir / "claim_closure.csv",
        claim_rows,
        ["paper_id", "conference", "analysis_stratum", "status", "claim", "origin"],
    )

    distributions: list[dict[str, object]] = []
    numeric_paper_fields = [
        "appendix_page_ratio",
        "appendix_word_ratio",
        "abstract_sentences",
        "visuals_total",
        "theory_items_total",
        "limitations_recorded",
    ]
    groups: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for row in paper_metrics:
        groups[(str(row["conference"]), "all")].append(row)
        groups[(str(row["conference"]), str(row["analysis_stratum"]))].append(row)
    for (conference, stratum), rows in sorted(groups.items()):
        for field in numeric_paper_fields:
            values = [float(row[field]) for row in rows if row[field] != ""]
            distributions.append(
                {"conference": conference, "analysis_stratum": stratum, "metric": field, **describe(values)}
            )
    write_csv(
        table_dir / "interim_distributions.csv",
        distributions,
        ["conference", "analysis_stratum", "metric", "n", "mean", "median", "q1", "q3", "min", "max"],
    )
    print(json.dumps(coverage, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import json
import re
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

MODULES = [
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
    "appendix",
    "other",
]

ABSTRACT_FUNCTIONS = [
    "object_scope",
    "problem_gap",
    "core_idea",
    "method",
    "theory",
    "experimental_setup",
    "quantitative_result",
    "qualitative_result",
    "limitation",
    "impact_claim",
]


def describe(values: list[float]) -> dict[str, object]:
    if not values:
        return {
            "n": 0,
            "mean": "",
            "trimmed_mean_20": "",
            "median": "",
            "q1": "",
            "q3": "",
            "min": "",
            "max": "",
        }
    ordered = sorted(values)
    trim = int(len(ordered) * 0.2)
    trimmed = ordered[trim : len(ordered) - trim] if trim and trim * 2 < len(ordered) else ordered
    if len(ordered) == 1:
        q1 = q3 = ordered[0]
    else:
        q1, _, q3 = statistics.quantiles(ordered, n=4, method="inclusive")
    return {
        "n": len(ordered),
        "mean": round(statistics.fmean(ordered), 6),
        "trimmed_mean_20": round(statistics.fmean(trimmed), 6),
        "median": round(statistics.median(ordered), 6),
        "q1": round(q1, 6),
        "q3": round(q3, 6),
        "min": round(ordered[0], 6),
        "max": round(ordered[-1], 6),
    }


def serialize(value: object) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def evidence_locations(items: list[dict[str, object]]) -> tuple[str, str]:
    pages = "|".join(str(item.get("page", "")) for item in items)
    sections = "|".join(str(item.get("section", "")) for item in items)
    return pages, sections


def is_reported(value: object) -> bool:
    if value is None or value == "" or value == [] or value == {}:
        return False
    if isinstance(value, str):
        normalized = value.strip().lower().replace("-", "_").replace(" ", "_")
        return normalized not in {
            "not_present",
            "not_applicable",
            "unavailable",
            "not_yet_observed",
            "none",
        }
    return True


def main() -> None:
    papers = read_csv(PROCESSED / "papers.csv")
    metrics = {row["paper_id"]: row for row in read_csv(PROCESSED / "auto_metrics.csv")} if (PROCESSED / "auto_metrics.csv").exists() else {}
    preprints = (
        {row["paper_id"]: row for row in read_csv(PROCESSED / "preprint_manifest.csv")}
        if (PROCESSED / "preprint_manifest.csv").exists()
        else {}
    )
    preprint_metrics = (
        {row["paper_id"]: row for row in read_csv(PROCESSED / "preprint_auto_metrics.csv")}
        if (PROCESSED / "preprint_auto_metrics.csv").exists()
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
                "provisional_measurements": sum(row["paper_id"] in preprint_metrics for row in eligible),
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
            "provisional_measurements",
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
    abstract_sequences: list[dict[str, object]] = []
    move_rows: list[dict[str, object]] = []
    move_transitions: list[dict[str, object]] = []
    design_rows: list[dict[str, object]] = []
    result_rows: list[dict[str, object]] = []
    ablation_rows: list[dict[str, object]] = []
    limitation_rows: list[dict[str, object]] = []
    adverse_rows: list[dict[str, object]] = []
    statistical_rows: list[dict[str, object]] = []
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
        abstract_sequences.append(
            {
                "paper_id": paper_id,
                "conference": paper["conference"],
                "analysis_stratum": paper["analysis_stratum"],
                "sentence_count": sentence_count,
                "sequence": " → ".join("+".join(sentence["functions"]) for sentence in reading["abstract_sentences"]),
            }
        )
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
        for inventory_name, target in (
            ("experimental_design", design_rows),
            ("ablation_inventory", ablation_rows),
            ("limitations", limitation_rows),
            ("adverse_presentation_strategies", adverse_rows),
        ):
            for item in reading[inventory_name]:
                pages, sections = evidence_locations(item.get("evidence", []))
                target.append(
                    {
                        "paper_id": paper_id,
                        "conference": paper["conference"],
                        "analysis_stratum": paper["analysis_stratum"],
                        "name": item["name"],
                        "status": item["status"],
                        "description": item["description"],
                        "limitation_type": item.get("limitation_type", ""),
                        "strategy": item.get("strategy", ""),
                        "evidence_pages": pages,
                        "evidence_sections": sections,
                    }
                )
        for item in reading["result_inventory"]:
            pages, sections = evidence_locations(item.get("evidence", []))
            result_rows.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "module": item["module"],
                    "claim": item["claim"],
                    "value": item["value"],
                    "comparison": item["comparison"],
                    "statistical_method": item["statistical_method"],
                    "author_interpretation": item.get("author_interpretation", ""),
                    "adverse_explanation": item.get("adverse_explanation", ""),
                    "evidence_pages": pages,
                    "evidence_sections": sections,
                }
            )
        for field, value in reading.get("statistical_analysis", {}).items():
            if field == "evidence":
                continue
            statistical_rows.append(
                {
                    "paper_id": paper_id,
                    "conference": paper["conference"],
                    "analysis_stratum": paper["analysis_stratum"],
                    "field": field,
                    "reported": is_reported(value),
                    "value": serialize(value),
                }
            )
        for move_module, key in (
            ("introduction", "introduction_moves"),
            ("related_work", "related_work_moves"),
            ("method", "method_moves"),
        ):
            ordered_moves = sorted(reading.get(key, []), key=lambda item: int(item["index"]))
            atoms: list[str] = []
            for item in ordered_moves:
                item_atoms = [atom.strip() for atom in re.split(r"\s*(?:→|\+|->)\s*", item["move"]) if atom.strip()]
                for atom_position, atom in enumerate(item_atoms, 1):
                    atoms.append(atom)
                    move_rows.append(
                        {
                            "paper_id": paper_id,
                            "conference": paper["conference"],
                            "analysis_stratum": paper["analysis_stratum"],
                            "module": move_module,
                            "paragraph_index": item["index"],
                            "atom_position": atom_position,
                            "move": atom,
                            "estimated_words": item["estimated_words"],
                        }
                    )
            for position, (source, target) in enumerate(zip(atoms, atoms[1:]), 1):
                move_transitions.append(
                    {
                        "paper_id": paper_id,
                        "conference": paper["conference"],
                        "analysis_stratum": paper["analysis_stratum"],
                        "module": move_module,
                        "transition_index": position,
                        "source": source,
                        "target": target,
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
    write_csv(
        table_dir / "abstract_sequences.csv",
        abstract_sequences,
        ["paper_id", "conference", "analysis_stratum", "sentence_count", "sequence"],
    )
    write_csv(
        table_dir / "move_inventory.csv",
        move_rows,
        [
            "paper_id",
            "conference",
            "analysis_stratum",
            "module",
            "paragraph_index",
            "atom_position",
            "move",
            "estimated_words",
        ],
    )
    write_csv(
        table_dir / "move_transitions.csv",
        move_transitions,
        ["paper_id", "conference", "analysis_stratum", "module", "transition_index", "source", "target"],
    )
    evidence_inventory_fields = [
        "paper_id",
        "conference",
        "analysis_stratum",
        "name",
        "status",
        "description",
        "limitation_type",
        "strategy",
        "evidence_pages",
        "evidence_sections",
    ]
    write_csv(table_dir / "experimental_design_inventory.csv", design_rows, evidence_inventory_fields)
    write_csv(table_dir / "ablation_inventory.csv", ablation_rows, evidence_inventory_fields)
    write_csv(table_dir / "limitation_inventory.csv", limitation_rows, evidence_inventory_fields)
    write_csv(table_dir / "adverse_strategy_inventory.csv", adverse_rows, evidence_inventory_fields)
    write_csv(
        table_dir / "result_inventory.csv",
        result_rows,
        [
            "paper_id",
            "conference",
            "analysis_stratum",
            "module",
            "claim",
            "value",
            "comparison",
            "statistical_method",
            "author_interpretation",
            "adverse_explanation",
            "evidence_pages",
            "evidence_sections",
        ],
    )
    write_csv(
        table_dir / "statistical_methods.csv",
        statistical_rows,
        ["paper_id", "conference", "analysis_stratum", "field", "reported", "value"],
    )

    reading_groups: dict[tuple[str, str], list[tuple[str, dict[str, object]]]] = defaultdict(list)
    for paper_id, reading in readings.items():
        paper = catalog[paper_id]
        reading_groups[(paper["conference"], "all")].append((paper_id, reading))
        reading_groups[(paper["conference"], paper["analysis_stratum"])].append((paper_id, reading))

    module_distributions: list[dict[str, object]] = []
    for (conference, stratum), group in sorted(reading_groups.items()):
        for module in MODULES:
            records = [
                next(item for item in reading["module_metrics"] if item["module"] == module)
                for _, reading in group
            ]
            derived: dict[str, list[float]] = {
                "present": [float(item["status"] == "observed") for item in records],
                "estimated_words": [float(item["estimated_words"]) for item in records],
                "main_word_share": [
                    float(item["main_word_share"])
                    for item in records
                    if item["main_word_share"] is not None
                ],
                "figures": [float(item["figures"]) for item in records],
                "tables": [float(item["tables"]) for item in records],
                "algorithms": [float(item["algorithms"]) for item in records],
                "displayed_equations": [float(item["displayed_equations"]) for item in records],
                "visual_objects": [
                    float(item["figures"] + item["tables"] + item["algorithms"])
                    for item in records
                ],
                "visual_objects_per_1000_words": [
                    1000.0 * (item["figures"] + item["tables"] + item["algorithms"]) / item["estimated_words"]
                    for item in records
                    if item["estimated_words"]
                ],
                "equations_per_1000_words": [
                    1000.0 * item["displayed_equations"] / item["estimated_words"]
                    for item in records
                    if item["estimated_words"]
                ],
            }
            visual_shares: list[float] = []
            equation_shares: list[float] = []
            for (_, reading), item in zip(group, records):
                main_modules = [entry for entry in reading["module_metrics"] if entry["module"] != "appendix"]
                visual_total = sum(entry["figures"] + entry["tables"] + entry["algorithms"] for entry in main_modules)
                equation_total = sum(entry["displayed_equations"] for entry in main_modules)
                if visual_total:
                    visual_shares.append((item["figures"] + item["tables"] + item["algorithms"]) / visual_total)
                if equation_total:
                    equation_shares.append(item["displayed_equations"] / equation_total)
            derived["visual_share_within_main"] = visual_shares
            derived["equation_share_within_main"] = equation_shares
            for metric, values in derived.items():
                module_distributions.append(
                    {
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "module": module,
                        "metric": metric,
                        **describe(values),
                    }
                )
    write_csv(
        table_dir / "module_distributions.csv",
        module_distributions,
        [
            "conference",
            "analysis_stratum",
            "module",
            "metric",
            "n",
            "mean",
            "trimmed_mean_20",
            "median",
            "q1",
            "q3",
            "min",
            "max",
        ],
    )

    abstract_function_summary: list[dict[str, object]] = []
    for (conference, stratum), group in sorted(reading_groups.items()):
        for function in ABSTRACT_FUNCTIONS:
            mention_counts = []
            sentence_shares = []
            for _, reading in group:
                functions = [item for sentence in reading["abstract_sentences"] for item in sentence["functions"]]
                mention_counts.append(float(functions.count(function)))
                sentence_shares.append(
                    sum(function in sentence["functions"] for sentence in reading["abstract_sentences"])
                    / len(reading["abstract_sentences"])
                )
            abstract_function_summary.append(
                {
                    "conference": conference,
                    "analysis_stratum": stratum,
                    "function": function,
                    "papers": len(group),
                    "papers_present": sum(value > 0 for value in mention_counts),
                    "paper_prevalence": round(sum(value > 0 for value in mention_counts) / len(group), 6),
                    "mean_mentions_per_paper": round(statistics.fmean(mention_counts), 6),
                    "mean_sentence_share": round(statistics.fmean(sentence_shares), 6),
                }
            )
    write_csv(
        table_dir / "abstract_function_summary.csv",
        abstract_function_summary,
        [
            "conference",
            "analysis_stratum",
            "function",
            "papers",
            "papers_present",
            "paper_prevalence",
            "mean_mentions_per_paper",
            "mean_sentence_share",
        ],
    )

    inventory_summaries: list[dict[str, object]] = []
    for (conference, stratum), group in sorted(reading_groups.items()):
        dimensions = {
            "visual_kind": ("visual_inventory", "kind"),
            "visual_module": ("visual_inventory", "module"),
            "theory_kind": ("equation_theory_inventory", "kind"),
            "theory_module": ("equation_theory_inventory", "module"),
            "theory_role": ("equation_theory_inventory", "role"),
            "appendix_category": ("appendix_inventory", "category"),
            "claim_status": ("claim_closure", "status"),
        }
        for dimension, (inventory, field) in dimensions.items():
            values = sorted({str(item[field]) for _, reading in group for item in reading[inventory]})
            for value in values:
                counts = [float(sum(str(item[field]) == value for item in reading[inventory])) for _, reading in group]
                inventory_summaries.append(
                    {
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "dimension": dimension,
                        "value": value,
                        "papers": len(group),
                        "papers_present": sum(count > 0 for count in counts),
                        "paper_prevalence": round(sum(count > 0 for count in counts) / len(group), 6),
                        **{f"count_{key}": result for key, result in describe(counts).items()},
                    }
                )
    write_csv(
        table_dir / "inventory_summaries.csv",
        inventory_summaries,
        [
            "conference",
            "analysis_stratum",
            "dimension",
            "value",
            "papers",
            "papers_present",
            "paper_prevalence",
            "count_n",
            "count_mean",
            "count_trimmed_mean_20",
            "count_median",
            "count_q1",
            "count_q3",
            "count_min",
            "count_max",
        ],
    )

    statistical_method_summary: list[dict[str, object]] = []
    for (conference, stratum), group in sorted(reading_groups.items()):
        fields = sorted({field for _, reading in group for field in reading.get("statistical_analysis", {}) if field != "evidence"})
        for field in fields:
            flags = [is_reported(reading.get("statistical_analysis", {}).get(field)) for _, reading in group]
            statistical_method_summary.append(
                {
                    "conference": conference,
                    "analysis_stratum": stratum,
                    "field": field,
                    "papers": len(group),
                    "papers_reported": sum(flags),
                    "paper_prevalence": round(sum(flags) / len(group), 6),
                }
            )
    write_csv(
        table_dir / "statistical_method_summary.csv",
        statistical_method_summary,
        ["conference", "analysis_stratum", "field", "papers", "papers_reported", "paper_prevalence"],
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
        [
            "conference",
            "analysis_stratum",
            "metric",
            "n",
            "mean",
            "trimmed_mean_20",
            "median",
            "q1",
            "q3",
            "min",
            "max",
        ],
    )

    automatic_distributions: list[dict[str, object]] = []
    for source_version, source_metrics in (
        ("official_pdf_provisional_parser", metrics),
        ("arxiv_preprint_provisional_parser", preprint_metrics),
    ):
        source_groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
        for paper_id, metric in source_metrics.items():
            paper = catalog.get(paper_id)
            if paper is None or metric.get("status") != "measured":
                continue
            source_groups[(paper["conference"], "all")].append(metric)
            source_groups[(paper["conference"], paper["analysis_stratum"])].append(metric)
        for (conference, stratum), rows in sorted(source_groups.items()):
            for field in (
                "pdf_pages",
                "total_words",
                "main_words_provisional",
                "appendix_words_provisional",
                "figure_captions",
                "table_captions",
                "algorithm_captions",
                "numbered_equations_provisional",
                "theorem_items",
                "limitation_mentions_main",
            ):
                values = [float(row[field]) for row in rows if row.get(field, "") != ""]
                automatic_distributions.append(
                    {
                        "source_version": source_version,
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "metric": field,
                        **describe(values),
                    }
                )
    write_csv(
        table_dir / "automatic_metric_distributions.csv",
        automatic_distributions,
        [
            "source_version",
            "conference",
            "analysis_stratum",
            "metric",
            "n",
            "mean",
            "trimmed_mean_20",
            "median",
            "q1",
            "q3",
            "min",
            "max",
        ],
    )
    print(json.dumps(coverage, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

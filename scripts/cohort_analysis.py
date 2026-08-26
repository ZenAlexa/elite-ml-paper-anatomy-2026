#!/usr/bin/env python3
from __future__ import annotations

import statistics
from collections import Counter, defaultdict

from aggregate import ABSTRACT_FUNCTIONS, MODULES, describe, is_reported
from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv


VIEWS = ("foundation_200", "replication_200", "combined_400")


def weight(sample: dict[str, str], view: str) -> float:
    field = "selection_probability" if view == "combined_400" else "cohort_selection_probability"
    return 1.0 / float(sample[field])


def weighted_mean(values: list[tuple[float, float]]) -> float | str:
    if not values:
        return ""
    denominator = sum(item_weight for _, item_weight in values)
    return round(sum(value * item_weight for value, item_weight in values) / denominator, 9)


def reading_views(
    sample: list[dict[str, str]], readings: dict[str, dict[str, object]]
) -> dict[str, list[tuple[dict[str, str], dict[str, object]]]]:
    result = {view: [] for view in VIEWS}
    for row in sample:
        reading = readings.get(row["paper_id"])
        if reading is None:
            continue
        result["combined_400"].append((row, reading))
        result[row["sample_cohort"]].append((row, reading))
    return result


def grouped(
    rows: list[tuple[dict[str, str], dict[str, object]]]
) -> dict[tuple[str, str], list[tuple[dict[str, str], dict[str, object]]]]:
    result: dict[tuple[str, str], list[tuple[dict[str, str], dict[str, object]]]] = defaultdict(list)
    for sample, reading in rows:
        result[(sample["conference"], "all")].append((sample, reading))
        result[(sample["conference"], sample["analysis_stratum"])].append((sample, reading))
    return result


def paper_scalars(reading: dict[str, object]) -> dict[str, float]:
    modules = reading["module_metrics"]
    main = [item for item in modules if item["module"] != "appendix"]
    appendix = next(item for item in modules if item["module"] == "appendix")
    page_map = reading["page_map"]
    functions = {function for sentence in reading["abstract_sentences"] for function in sentence["functions"]}
    claims = reading["claim_closure"]
    main_pages = float(page_map["main_pages"])
    appendix_pages = float(page_map["appendix_pages"])
    return {
        "main_pages": main_pages,
        "appendix_pages": appendix_pages,
        "appendix_page_ratio": appendix_pages / main_pages if main_pages else 0.0,
        "abstract_sentences": float(len(reading["abstract_sentences"])),
        "abstract_has_quantitative_result": float("quantitative_result" in functions),
        "abstract_has_qualitative_result": float("qualitative_result" in functions),
        "abstract_has_theory": float("theory" in functions),
        "abstract_has_limitation": float("limitation" in functions),
        "figures_main": float(sum(item["figures"] for item in main)),
        "tables_main": float(sum(item["tables"] for item in main)),
        "algorithms_main": float(sum(item["algorithms"] for item in main)),
        "displayed_equations_main": float(sum(item["displayed_equations"] for item in main)),
        "figures_appendix": float(appendix["figures"]),
        "tables_appendix": float(appendix["tables"]),
        "algorithms_appendix": float(appendix["algorithms"]),
        "displayed_equations_appendix": float(appendix["displayed_equations"]),
        "claim_closure_rate": (
            sum(item["status"] == "closed" for item in claims) / len(claims) if claims else 0.0
        ),
        "limitations_recorded": float(len(reading["limitations"])),
        "appendix_main_text_calls": float(
            sum(len(item["main_text_calls"]) for item in reading["appendix_inventory"])
        ),
    }


def main() -> None:
    sample = read_csv(PROCESSED / "analysis_sample.csv")
    readings = {
        row["paper_id"]: reading
        for row in sample
        if (reading := load_complete_reading(row["paper_id"])) is not None
    }
    views = reading_views(sample, readings)
    table_dir = ROOT / "reports" / "tables"

    module_rows: list[dict[str, object]] = []
    paper_rows: list[dict[str, object]] = []
    categorical_rows: list[dict[str, object]] = []
    for view, view_rows in views.items():
        for (conference, stratum), group in sorted(grouped(view_rows).items()):
            for module in MODULES:
                records = [
                    (
                        sample_row,
                        next(item for item in reading["module_metrics"] if item["module"] == module),
                        reading,
                    )
                    for sample_row, reading in group
                ]
                metrics: dict[str, list[tuple[float, float]]] = defaultdict(list)
                for sample_row, item, reading in records:
                    item_weight = weight(sample_row, view)
                    visual_objects = item["figures"] + item["tables"] + item["algorithms"]
                    values = {
                        "present": float(item["status"] == "observed"),
                        "estimated_words": float(item["estimated_words"]),
                        "main_word_share": (
                            float(item["main_word_share"]) if item["main_word_share"] is not None else None
                        ),
                        "figures": float(item["figures"]),
                        "tables": float(item["tables"]),
                        "algorithms": float(item["algorithms"]),
                        "displayed_equations": float(item["displayed_equations"]),
                        "visual_objects": float(visual_objects),
                        "visual_objects_per_1000_words": (
                            1000.0 * visual_objects / item["estimated_words"] if item["estimated_words"] else None
                        ),
                        "equations_per_1000_words": (
                            1000.0 * item["displayed_equations"] / item["estimated_words"]
                            if item["estimated_words"]
                            else None
                        ),
                    }
                    main_modules = [entry for entry in reading["module_metrics"] if entry["module"] != "appendix"]
                    visual_total = sum(entry["figures"] + entry["tables"] + entry["algorithms"] for entry in main_modules)
                    equation_total = sum(entry["displayed_equations"] for entry in main_modules)
                    values["visual_share_within_main"] = visual_objects / visual_total if visual_total else None
                    values["equation_share_within_main"] = (
                        item["displayed_equations"] / equation_total if equation_total else None
                    )
                    for metric, value in values.items():
                        if value is not None:
                            metrics[metric].append((value, item_weight))
                for metric, observations in metrics.items():
                    summary = describe([value for value, _ in observations])
                    module_rows.append(
                        {
                            "analysis_view": view,
                            "conference": conference,
                            "analysis_stratum": stratum,
                            "module": module,
                            "metric": metric,
                            **summary,
                            "design_weighted_mean": weighted_mean(observations),
                            "status": "complete" if len(view_rows) in {200, 400} else "interim",
                        }
                    )

            scalar_records = [(sample_row, paper_scalars(reading)) for sample_row, reading in group]
            scalar_names = sorted({name for _, values in scalar_records for name in values})
            for metric in scalar_names:
                observations = [(values[metric], weight(sample_row, view)) for sample_row, values in scalar_records]
                paper_rows.append(
                    {
                        "analysis_view": view,
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "metric": metric,
                        **describe([value for value, _ in observations]),
                        "design_weighted_mean": weighted_mean(observations),
                        "status": "complete" if len(view_rows) in {200, 400} else "interim",
                    }
                )

            categorical_counts: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
            for sample_row, reading in group:
                paper_id = sample_row["paper_id"]
                abstract_functions = {
                    function for sentence in reading["abstract_sentences"] for function in sentence["functions"]
                }
                for function in ABSTRACT_FUNCTIONS:
                    categorical_counts[("abstract_function", function)][paper_id] = int(function in abstract_functions)
                for dimension, inventory, field in (
                    ("visual_kind", "visual_inventory", "kind"),
                    ("visual_module", "visual_inventory", "module"),
                    ("theory_kind", "equation_theory_inventory", "kind"),
                    ("theory_role", "equation_theory_inventory", "role"),
                    ("appendix_category", "appendix_inventory", "category"),
                    ("claim_status", "claim_closure", "status"),
                    ("limitation_type", "limitations", "limitation_type"),
                ):
                    for item in reading[inventory]:
                        categorical_counts[(dimension, str(item.get(field, "unspecified")))][paper_id] += 1
                for field, value in reading.get("statistical_analysis", {}).items():
                    if field != "evidence":
                        categorical_counts[("statistical_field_reported", field)][paper_id] = int(is_reported(value))
            paper_weights = {sample_row["paper_id"]: weight(sample_row, view) for sample_row, _ in group}
            for (dimension, value), counts in sorted(categorical_counts.items()):
                per_paper = [float(counts.get(sample_row["paper_id"], 0)) for sample_row, _ in group]
                presence = [float(item > 0) for item in per_paper]
                weighted_presence = [
                    (float(counts.get(paper_id, 0) > 0), item_weight)
                    for paper_id, item_weight in paper_weights.items()
                ]
                categorical_rows.append(
                    {
                        "analysis_view": view,
                        "conference": conference,
                        "analysis_stratum": stratum,
                        "dimension": dimension,
                        "value": value,
                        "papers": len(group),
                        "papers_present": int(sum(presence)),
                        "paper_prevalence": round(statistics.fmean(presence), 9),
                        "design_weighted_prevalence": weighted_mean(weighted_presence),
                        "mean_count_per_paper": round(statistics.fmean(per_paper), 9),
                        "median_count_per_paper": round(statistics.median(per_paper), 9),
                        "status": "complete" if len(view_rows) in {200, 400} else "interim",
                    }
                )

    write_csv(
        table_dir / "cohort_module_comparison.csv",
        module_rows,
        [
            "analysis_view", "conference", "analysis_stratum", "module", "metric", "n", "mean",
            "trimmed_mean_20", "median", "q1", "q3", "min", "max", "design_weighted_mean", "status",
        ],
    )
    write_csv(
        table_dir / "cohort_paper_comparison.csv",
        paper_rows,
        [
            "analysis_view", "conference", "analysis_stratum", "metric", "n", "mean", "trimmed_mean_20",
            "median", "q1", "q3", "min", "max", "design_weighted_mean", "status",
        ],
    )
    write_csv(
        table_dir / "cohort_categorical_comparison.csv",
        categorical_rows,
        [
            "analysis_view", "conference", "analysis_stratum", "dimension", "value", "papers",
            "papers_present", "paper_prevalence", "design_weighted_prevalence", "mean_count_per_paper",
            "median_count_per_paper", "status",
        ],
    )
    print(
        " ".join(
            [f"completed={len(readings)}"]
            + [f"{view}={len(rows)}" for view, rows in views.items()]
            + [f"module_rows={len(module_rows)}", f"categorical_rows={len(categorical_rows)}"]
        )
    )


if __name__ == "__main__":
    main()

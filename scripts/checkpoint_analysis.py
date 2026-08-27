#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv, write_json


MODULES = (
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
)

ABSTRACT_FUNCTIONS = (
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
)

CANONICAL_MOVES = {
    "introduction": {
        "context",
        "problem",
        "failure_of_prior_work",
        "missing_insight",
        "core_idea",
        "method_preview",
        "theory_preview",
        "result_preview",
        "contribution_list",
        "scope_boundary",
        "roadmap",
    },
    "related_work": {
        "taxonomy",
        "chronology",
        "nearest_neighbor_contrast",
        "gap_creation",
        "credit_or_foundation",
        "limitation_of_prior",
        "positioning_only",
    },
    "method": {
        "setup_notation",
        "state_problem",
        "derive",
        "define_component",
        "explain_mechanism",
        "give_intuition",
        "instantiate_algorithm",
        "state_complexity",
        "connect_to_prediction",
        "connect_to_experiment",
        "contrast_alternative",
        "summarize",
    },
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the exact-N deep-reading checkpoint tables.")
    parser.add_argument("--target", type=int, default=250)
    return parser.parse_args()


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return math.nan
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction


def describe(values: list[float]) -> dict[str, float | int | str]:
    if not values:
        return {"n": 0, "mean": "", "median": "", "q1": "", "q3": "", "min": "", "max": ""}
    return {
        "n": len(values),
        "mean": round(statistics.fmean(values), 9),
        "median": round(statistics.median(values), 9),
        "q1": round(quantile(values, 0.25), 9),
        "q3": round(quantile(values, 0.75), 9),
        "min": round(min(values), 9),
        "max": round(max(values), 9),
    }


def conference_equal(values: list[tuple[str, float]]) -> float | str:
    by_conference: dict[str, list[float]] = defaultdict(list)
    for conference, value in values:
        by_conference[conference].append(value)
    if set(by_conference) != {"ICLR", "ICML"}:
        return ""
    return round(statistics.fmean(statistics.fmean(group) for group in by_conference.values()), 9)


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise RuntimeError(f"refusing to write an empty table: {path}")
    write_csv(path, rows, list(rows[0]))


def module_lookup(reading: dict[str, object]) -> dict[str, dict[str, object]]:
    return {str(item["module"]): item for item in reading["module_metrics"]}


def normalize_text(value: object) -> str:
    return re.sub(r"\s+", " ", json.dumps(value, ensure_ascii=False).lower())


def positive_pattern(text: str, pattern: str) -> bool:
    matches = list(re.finditer(pattern, text, flags=re.IGNORECASE))
    for match in matches:
        before = text[max(0, match.start() - 55) : match.start()]
        after = text[match.end() : match.end() + 35]
        negated_before = re.search(
            r"(?:no|not[_ -]?present|without|absent|未报告|没有|无)(?:.{0,45})$", before
        )
        negated_after = re.match(r"(?:.{0,8})(?:not[_ -]?present|false|none|absent|未报告|没有|无)", after)
        if not negated_before and not negated_after:
            return True
    return False


def statistical_features(reading: dict[str, object]) -> set[str]:
    result_methods = " ".join(str(item.get("statistical_method", "")) for item in reading["result_inventory"])
    analysis = reading.get("statistical_analysis", {})

    def positive_analysis_values(value: object, key: str = "") -> list[str]:
        normalized_key = key.lower()
        if any(token in normalized_key for token in ("not_present", "not_reported", "absent")):
            return []
        if isinstance(value, dict):
            return [
                item
                for child_key, child_value in value.items()
                for item in positive_analysis_values(child_value, str(child_key))
            ]
        if isinstance(value, list):
            return [item for child in value for item in positive_analysis_values(child, key)]
        text_value = str(value).strip().lower()
        if text_value in {"", "false", "none", "not_present", "not present", "unavailable", "not_applicable"}:
            return []
        return [f"{key}: {value}"]

    text = normalize_text(
        {
            "result_methods": result_methods,
            "analysis": positive_analysis_values(analysis),
        }
    )
    features: set[str] = set()
    if re.search(r"\bmean|average|median|aggregate", result_methods, flags=re.IGNORECASE):
        features.add("descriptive_mean_median_or_aggregate")
    patterns = {
        "repeated_runs_or_seeds": r"\b(?:seeds?|runs?|replications?|trials?)\b",
        "dispersion_sd_or_se": r"standard deviation|standard error|mean\s*[±+/-]+\s*(?:sd|std|se)|\b(?:sd|std|sem)\b",
        "intervals_or_error_bars": r"confidence intervals?|credible intervals?|error bars?|uncertainty bands?|quantiles?|boxplots?",
        "hypothesis_test_or_p_value": r"\b(?:t-tests?|anova|wilcoxon|mann[- ]whitney|permutation tests?|f-tests?)\b|p\s*[<=>]",
        "multiple_comparison_control": r"bonferroni|benjamini|holm|false discovery rate|multiple[- ]comparison correction|\bfdr\b",
        "bootstrap": r"bootstrap",
        "bayesian_analysis": r"bayesian|posterior|credible interval",
        "correlation": r"spearman|pearson|kendall|correlation coefficient",
        "regression_or_fitted_model": r"\b(?:regression|ols|mixed[- ]effects?|linear model|logistic model)\b",
        "effect_size": r"cohen['’]?s d|effect size|odds ratio|risk ratio",
    }
    for feature, pattern in patterns.items():
        if positive_pattern(text, pattern):
            features.add(feature)
    if re.search(r"point estimates?|single[- ]run|no uncertainty|without uncertainty|无区间|无误差|未报告 uncertainty", text):
        features.add("point_estimate_without_uncertainty")
    return features


def evidence_placement(item: dict[str, object], reading: dict[str, object]) -> set[str]:
    placements: set[str] = set()
    appendix_start = float(reading["page_map"]["main_pages"]) + float(reading["page_map"]["reference_pages"])
    for evidence in item.get("evidence", []):
        section = str(evidence.get("section", "")).lower()
        page = float(evidence.get("page", 0))
        if "abstract" in section:
            placements.add("abstract")
        elif "intro" in section:
            placements.add("introduction")
        elif any(token in section for token in ("limitation", "discussion", "conclusion", "future work")):
            placements.add("conclusion_or_dedicated_limitations")
        elif appendix_start and page > appendix_start:
            placements.add("appendix")
        else:
            placements.add("main_body_other")
    return placements or {"unlocated"}


def categorical_summary(
    records: list[tuple[dict[str, str], dict[str, object]]],
    dimensions: dict[str, dict[str, Counter[str]]],
) -> list[dict[str, object]]:
    conferences = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    rows: list[dict[str, object]] = []
    for dimension, values in sorted(dimensions.items()):
        for value, counts in sorted(values.items()):
            per_paper = [(conferences[paper_id], float(counts.get(paper_id, 0))) for paper_id in conferences]
            presence = [(conference, float(count > 0)) for conference, count in per_paper]
            count_values = [count for _, count in per_paper]
            rows.append(
                {
                    "dimension": dimension,
                    "value": value,
                    "papers": len(per_paper),
                    "papers_present": int(sum(item for _, item in presence)),
                    "paper_prevalence": round(statistics.fmean(item for _, item in presence), 9),
                    "conference_equal_prevalence": conference_equal(presence),
                    "mean_count_per_paper": round(statistics.fmean(count_values), 9),
                    "conference_equal_mean_count": conference_equal(per_paper),
                    "median_count_per_paper": round(statistics.median(count_values), 9),
                }
            )
    return rows


def main() -> None:
    args = parse_args()
    if args.target < 1:
        raise SystemExit("--target must be positive")

    sample = read_csv(PROCESSED / "analysis_sample.csv")
    records: list[tuple[dict[str, str], dict[str, object]]] = []
    for row in sample:
        reading = load_complete_reading(row["paper_id"])
        if reading is not None:
            records.append((row, reading))
    if len(records) != args.target:
        raise SystemExit(f"checkpoint requires exactly {args.target} complete sample readings; found {len(records)}")

    conferences = Counter(row["conference"] for row, _ in records)
    cohorts = Counter(row["sample_cohort"] for row, _ in records)
    strata = Counter((row["conference"], row["analysis_stratum"]) for row, _ in records)
    table_dir = ROOT / "reports" / "tables"

    module_rows: list[dict[str, object]] = []
    for module in MODULES:
        entries = []
        for sample_row, reading in records:
            modules = module_lookup(reading)
            total_main_words = sum(
                float(modules[name]["estimated_words"]) for name in MODULES if name != "appendix"
            )
            reported_share_total = sum(
                float(modules[name]["main_word_share"] or 0.0) for name in MODULES if name != "appendix"
            )
            entries.append((sample_row, modules[module], total_main_words, reported_share_total))
        words = [(sample["conference"], float(item["estimated_words"])) for sample, item, _, _ in entries]
        present = [
            (sample["conference"], float(item["status"] == "observed")) for sample, item, _, _ in entries
        ]
        shares = [
            (sample["conference"], float(item["main_word_share"]))
            for sample, item, _, _ in entries
            if item["main_word_share"] is not None
        ]
        normalized_shares = [
            (sample["conference"], float(item["main_word_share"] or 0.0) / reported_share_total)
            for sample, item, _, reported_share_total in entries
            if module != "appendix" and reported_share_total
        ]
        metric_values = {
            "figures": [(sample["conference"], float(item["figures"])) for sample, item, _, _ in entries],
            "tables": [(sample["conference"], float(item["tables"])) for sample, item, _, _ in entries],
            "algorithms": [(sample["conference"], float(item["algorithms"])) for sample, item, _, _ in entries],
            "displayed_equations": [
                (sample["conference"], float(item["displayed_equations"])) for sample, item, _, _ in entries
            ],
        }
        visuals = [
            (sample["conference"], float(item["figures"] + item["tables"] + item["algorithms"]))
            for sample, item, _, _ in entries
        ]
        total_words = sum(value for _, value in words)
        module_rows.append(
            {
                "module": module,
                "papers": len(entries),
                "papers_present": int(sum(value for _, value in present)),
                "presence_share": round(statistics.fmean(value for _, value in present), 9),
                "conference_equal_presence_share": conference_equal(present),
                "estimated_words_mean": round(statistics.fmean(value for _, value in words), 9),
                "estimated_words_median": round(statistics.median(value for _, value in words), 9),
                "main_word_share_mean": round(statistics.fmean(value for _, value in shares), 9) if shares else "",
                "main_word_share_median": round(statistics.median(value for _, value in shares), 9) if shares else "",
                "main_word_share_q1": round(quantile([value for _, value in shares], 0.25), 9) if shares else "",
                "main_word_share_q3": round(quantile([value for _, value in shares], 0.75), 9) if shares else "",
                "conference_equal_main_word_share": conference_equal(shares),
                "normalized_word_share_mean": round(
                    statistics.fmean(value for _, value in normalized_shares), 9
                )
                if normalized_shares
                else "",
                "normalized_word_share_median": round(
                    statistics.median(value for _, value in normalized_shares), 9
                )
                if normalized_shares
                else "",
                "normalized_word_share_q1": round(quantile([value for _, value in normalized_shares], 0.25), 9)
                if normalized_shares
                else "",
                "normalized_word_share_q3": round(quantile([value for _, value in normalized_shares], 0.75), 9)
                if normalized_shares
                else "",
                "conference_equal_normalized_word_share": conference_equal(normalized_shares),
                "iclr_normalized_word_share": round(
                    statistics.fmean(value for conference, value in normalized_shares if conference == "ICLR"), 9
                )
                if normalized_shares
                else "",
                "icml_normalized_word_share": round(
                    statistics.fmean(value for conference, value in normalized_shares if conference == "ICML"), 9
                )
                if normalized_shares
                else "",
                "figures_mean": round(statistics.fmean(value for _, value in metric_values["figures"]), 9),
                "conference_equal_figures_mean": conference_equal(metric_values["figures"]),
                "iclr_figures_mean": round(
                    statistics.fmean(
                        value for conference, value in metric_values["figures"] if conference == "ICLR"
                    ),
                    9,
                ),
                "icml_figures_mean": round(
                    statistics.fmean(
                        value for conference, value in metric_values["figures"] if conference == "ICML"
                    ),
                    9,
                ),
                "tables_mean": round(statistics.fmean(value for _, value in metric_values["tables"]), 9),
                "conference_equal_tables_mean": conference_equal(metric_values["tables"]),
                "iclr_tables_mean": round(
                    statistics.fmean(
                        value for conference, value in metric_values["tables"] if conference == "ICLR"
                    ),
                    9,
                ),
                "icml_tables_mean": round(
                    statistics.fmean(
                        value for conference, value in metric_values["tables"] if conference == "ICML"
                    ),
                    9,
                ),
                "algorithms_mean": round(statistics.fmean(value for _, value in metric_values["algorithms"]), 9),
                "conference_equal_algorithms_mean": conference_equal(metric_values["algorithms"]),
                "displayed_equations_mean": round(
                    statistics.fmean(value for _, value in metric_values["displayed_equations"]), 9
                ),
                "conference_equal_displayed_equations_mean": conference_equal(
                    metric_values["displayed_equations"]
                ),
                "iclr_displayed_equations_mean": round(
                    statistics.fmean(
                        value
                        for conference, value in metric_values["displayed_equations"]
                        if conference == "ICLR"
                    ),
                    9,
                ),
                "icml_displayed_equations_mean": round(
                    statistics.fmean(
                        value
                        for conference, value in metric_values["displayed_equations"]
                        if conference == "ICML"
                    ),
                    9,
                ),
                "visual_objects_per_1000_words": round(1000 * sum(value for _, value in visuals) / total_words, 9)
                if total_words
                else "",
                "equations_per_1000_words": round(
                    1000 * sum(value for _, value in metric_values["displayed_equations"]) / total_words, 9
                )
                if total_words
                else "",
            }
        )
    write_rows(table_dir / f"checkpoint_{args.target}_module_summary.csv", module_rows)

    scalar_values: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for sample_row, reading in records:
        modules = module_lookup(reading)
        main_modules = [modules[module] for module in MODULES if module != "appendix"]
        main_words = sum(
            float(item["estimated_words"])
            for item in main_modules
            if item.get("main_word_share") is not None
        )
        appendix_words = float(modules["appendix"]["estimated_words"])
        main_visuals = sum(float(item["figures"] + item["tables"] + item["algorithms"]) for item in main_modules)
        main_equations = sum(float(item["displayed_equations"]) for item in main_modules)
        appendix_pages = float(reading["page_map"]["appendix_pages"])
        main_pages = float(reading["page_map"]["main_pages"])
        functions = {function for sentence in reading["abstract_sentences"] for function in sentence["functions"]}
        scalars = {
            "main_pages": main_pages,
            "appendix_pages": appendix_pages,
            "appendix_to_main_page_ratio": appendix_pages / main_pages if main_pages else 0.0,
            "main_words": main_words,
            "appendix_words": appendix_words,
            "appendix_to_main_word_ratio": appendix_words / main_words if main_words else 0.0,
            "main_figures": sum(float(item["figures"]) for item in main_modules),
            "main_tables": sum(float(item["tables"]) for item in main_modules),
            "main_algorithms": sum(float(item["algorithms"]) for item in main_modules),
            "main_visual_objects": main_visuals,
            "main_displayed_equations": main_equations,
            "appendix_figures": float(modules["appendix"]["figures"]),
            "appendix_tables": float(modules["appendix"]["tables"]),
            "appendix_algorithms": float(modules["appendix"]["algorithms"]),
            "appendix_displayed_equations": float(modules["appendix"]["displayed_equations"]),
            "abstract_sentences": float(len(reading["abstract_sentences"])),
            "abstract_has_any_result": float(
                "quantitative_result" in functions or "qualitative_result" in functions
            ),
            "abstract_has_quantitative_result": float("quantitative_result" in functions),
            "abstract_has_qualitative_result": float("qualitative_result" in functions),
            "abstract_has_limitation": float("limitation" in functions),
            "abstract_has_theory": float("theory" in functions),
            "claim_closure_rate": (
                sum(item["status"] == "closed" for item in reading["claim_closure"])
                / len(reading["claim_closure"])
                if reading["claim_closure"]
                else 0.0
            ),
            "appendix_main_text_calls": float(
                sum(len(item["main_text_calls"]) for item in reading["appendix_inventory"])
            ),
        }
        for metric, value in scalars.items():
            scalar_values[metric].append((sample_row["conference"], value))

    paper_rows = []
    for metric, values in sorted(scalar_values.items()):
        summary = describe([value for _, value in values])
        paper_rows.append(
            {
                "metric": metric,
                **summary,
                "conference_equal_mean": conference_equal(values),
                "iclr_mean": round(statistics.fmean(value for conference, value in values if conference == "ICLR"), 9),
                "icml_mean": round(statistics.fmean(value for conference, value in values if conference == "ICML"), 9),
            }
        )
    write_rows(table_dir / f"checkpoint_{args.target}_paper_summary.csv", paper_rows)

    abstract_rows: list[dict[str, object]] = []
    for function in ABSTRACT_FUNCTIONS:
        presence: list[tuple[str, float]] = []
        first_positions: list[tuple[str, float]] = []
        mention_counts: list[tuple[str, float]] = []
        for sample_row, reading in records:
            sentences = reading["abstract_sentences"]
            indexes = [sentence["index"] for sentence in sentences if function in sentence["functions"]]
            presence.append((sample_row["conference"], float(bool(indexes))))
            mention_counts.append((sample_row["conference"], float(len(indexes))))
            if indexes:
                denominator = max(1, len(sentences) - 1)
                first_positions.append((sample_row["conference"], (min(indexes) - 1) / denominator))
        abstract_rows.append(
            {
                "function": function,
                "papers_present": int(sum(value for _, value in presence)),
                "paper_prevalence": round(statistics.fmean(value for _, value in presence), 9),
                "conference_equal_prevalence": conference_equal(presence),
                "mentions_per_paper": round(statistics.fmean(value for _, value in mention_counts), 9),
                "conference_equal_mentions_per_paper": conference_equal(mention_counts),
                "first_normalized_position_mean": round(
                    statistics.fmean(value for _, value in first_positions), 9
                )
                if first_positions
                else "",
                "first_normalized_position_median": round(
                    statistics.median(value for _, value in first_positions), 9
                )
                if first_positions
                else "",
            }
        )
    write_rows(table_dir / f"checkpoint_{args.target}_abstract_summary.csv", abstract_rows)

    dimensions: dict[str, dict[str, Counter[str]]] = defaultdict(lambda: defaultdict(Counter))
    for sample_row, reading in records:
        paper_id = sample_row["paper_id"]
        for item in reading["visual_inventory"]:
            dimensions["visual_kind"][str(item["kind"])][paper_id] += 1
            dimensions["visual_module"][str(item["module"])][paper_id] += 1
        for item in reading["equation_theory_inventory"]:
            dimensions["theory_kind"][str(item["kind"])][paper_id] += 1
            dimensions["theory_role"][str(item["role"])][paper_id] += 1
        for item in reading["appendix_inventory"]:
            dimensions["appendix_category"][str(item["category"])][paper_id] += 1
        for item in reading["claim_closure"]:
            dimensions["claim_status"][str(item["status"])][paper_id] += 1
        observed_limitations = [item for item in reading["limitations"] if item.get("status") == "observed"]
        for item in observed_limitations:
            for placement in evidence_placement(item, reading):
                dimensions["limitation_placement"][placement][paper_id] += 1
        observed_adverse = [
            item for item in reading["adverse_presentation_strategies"] if item.get("status") == "observed"
        ]
        for item in observed_adverse:
            for placement in evidence_placement(item, reading):
                dimensions["adverse_strategy_placement"][placement][paper_id] += 1
        dimensions["paper_feature"]["has_explicit_limitation"][paper_id] = int(bool(observed_limitations))
        dimensions["paper_feature"]["has_adverse_presentation_strategy"][paper_id] = int(
            bool(observed_adverse)
        )
        dimensions["paper_feature"]["has_ablation_inventory"][paper_id] = int(
            any(item.get("status") == "observed" for item in reading["ablation_inventory"])
        )
        dimensions["paper_feature"]["has_algorithm_object"][paper_id] = int(
            any(item["kind"] == "algorithm" for item in reading["visual_inventory"])
        )
        for feature in statistical_features(reading):
            dimensions["statistical_practice"][feature][paper_id] = 1

    categorical_rows = categorical_summary(records, dimensions)
    write_rows(table_dir / f"checkpoint_{args.target}_categorical_summary.csv", categorical_rows)

    move_counts: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
    transition_counts: dict[tuple[str, str, str], Counter[str]] = defaultdict(Counter)
    for sample_row, reading in records:
        paper_id = sample_row["paper_id"]
        for module, field in (
            ("introduction", "introduction_moves"),
            ("related_work", "related_work_moves"),
            ("method", "method_moves"),
        ):
            moves = [str(item["move"]) for item in reading[field]]
            canonical = [move for move in moves if move in CANONICAL_MOVES[module]]
            for move in canonical:
                move_counts[(module, move)][paper_id] += 1
            for source, target in zip(canonical, canonical[1:]):
                transition_counts[(module, source, target)][paper_id] += 1
    paper_conference = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    move_rows: list[dict[str, object]] = []
    for (module, move), counts in sorted(move_counts.items()):
        per_paper = [(paper_conference[paper_id], float(counts.get(paper_id, 0))) for paper_id in paper_conference]
        presence = [(conference, float(count > 0)) for conference, count in per_paper]
        move_rows.append(
            {
                "module": module,
                "move": move,
                "papers_present": int(sum(value for _, value in presence)),
                "paper_prevalence": round(statistics.fmean(value for _, value in presence), 9),
                "conference_equal_prevalence": conference_equal(presence),
                "count": int(sum(value for _, value in per_paper)),
                "mean_count_per_paper": round(statistics.fmean(value for _, value in per_paper), 9),
            }
        )
    move_rows.sort(key=lambda row: (str(row["module"]), -float(row["paper_prevalence"]), str(row["move"])))
    write_rows(table_dir / f"checkpoint_{args.target}_move_summary.csv", move_rows)

    transition_rows: list[dict[str, object]] = []
    for (module, source, target), counts in sorted(transition_counts.items()):
        per_paper = [(paper_conference[paper_id], float(counts.get(paper_id, 0))) for paper_id in paper_conference]
        presence = [(conference, float(count > 0)) for conference, count in per_paper]
        transition_rows.append(
            {
                "module": module,
                "source": source,
                "target": target,
                "papers_present": int(sum(value for _, value in presence)),
                "paper_prevalence": round(statistics.fmean(value for _, value in presence), 9),
                "conference_equal_prevalence": conference_equal(presence),
                "count": int(sum(value for _, value in per_paper)),
            }
        )
    transition_rows.sort(
        key=lambda row: (str(row["module"]), -float(row["paper_prevalence"]), str(row["source"]), str(row["target"]))
    )
    write_rows(table_dir / f"checkpoint_{args.target}_transition_summary.csv", transition_rows)

    sequence_counts: Counter[tuple[str, ...]] = Counter()
    sequence_examples: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for sample_row, reading in records:
        sequence: list[str] = []
        for sentence in reading["abstract_sentences"]:
            for function in sentence["functions"]:
                if not sequence or sequence[-1] != function:
                    sequence.append(function)
        key = tuple(sequence)
        sequence_counts[key] += 1
        if len(sequence_examples[key]) < 5:
            sequence_examples[key].append(sample_row["paper_id"])
    sequence_rows = [
        {
            "rank": rank,
            "sequence": " -> ".join(sequence),
            "papers": count,
            "paper_share": round(count / len(records), 9),
            "example_paper_ids": "|".join(sequence_examples[sequence]),
        }
        for rank, (sequence, count) in enumerate(sequence_counts.most_common(100), start=1)
    ]
    write_rows(table_dir / f"checkpoint_{args.target}_abstract_sequences.csv", sequence_rows)

    write_json(
        ROOT / "reports" / f"checkpoint_{args.target}_status.json",
        {
            "schema_version": "checkpoint-analysis.v1",
            "target": args.target,
            "completed": len(records),
            "conference_counts": dict(sorted(conferences.items())),
            "cohort_counts": dict(sorted(cohorts.items())),
            "stratum_counts": {f"{conference}:{stratum}": count for (conference, stratum), count in sorted(strata.items())},
            "source_tables": [
                f"reports/tables/checkpoint_{args.target}_module_summary.csv",
                f"reports/tables/checkpoint_{args.target}_paper_summary.csv",
                f"reports/tables/checkpoint_{args.target}_abstract_summary.csv",
                f"reports/tables/checkpoint_{args.target}_categorical_summary.csv",
                f"reports/tables/checkpoint_{args.target}_abstract_sequences.csv",
                f"reports/tables/checkpoint_{args.target}_move_summary.csv",
                f"reports/tables/checkpoint_{args.target}_transition_summary.csv",
                f"reports/tables/checkpoint_{args.target}_experimental_design_summary.csv",
                f"reports/tables/checkpoint_{args.target}_limitation_type_summary.csv",
                f"reports/tables/checkpoint_{args.target}_packaging_strategy_summary.csv",
            ],
        },
    )
    print(
        f"checkpoint={args.target} conferences={dict(conferences)} cohorts={dict(cohorts)} "
        f"module_rows={len(module_rows)} categorical_rows={len(categorical_rows)}"
    )


if __name__ == "__main__":
    main()

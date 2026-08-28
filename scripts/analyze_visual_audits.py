#!/usr/bin/env python3
"""Aggregate schema-valid per-paper visual audits without object-count domination."""

from __future__ import annotations

import argparse
import colorsys
import csv
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable

import jsonschema

from common import PROCESSED, ROOT, load_complete_reading, read_csv


AUDIT_DIR = ROOT / "visual_audits"
TABLE_DIR = ROOT / "reports" / "tables"
CAPTION_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is", "it", "of", "on",
    "or", "our", "that", "the", "their", "these", "this", "to", "using", "we", "where", "with",
    "figure", "fig", "table", "left", "right", "top", "bottom",
}

JUDGMENT_THEMES = {
    "reusable": {
        "method_interface": ("pipeline", "architecture", "method-interface", "method interface", "schematic", "流程", "架构", "方法接口", "机制图"),
        "matched_multi_panel": ("matched", "shared axis", "shared axes", "fixed-facet", "small multiples", "paired", "对照", "共享", "固定.*panel", "双 panel"),
        "trend_plus_exact_table": ("exact value", "exact number", "precise", "trend", "curve.*table", "figure.*table", "精确", "趋势", "图.*表", "表.*图"),
        "grouped_booktabs_table": ("booktabs", "multi-level header", "grouped header", "row group", "best/second", "best and second", "粗体", "下划线", "多级表头", "行组"),
        "cost_quality_pair": ("cost", "latency", "runtime", "memory", "compute", "efficiency", "成本", "延迟", "显存", "效率"),
        "mechanism_ablation_chain": ("ablation", "mechanism", "diagnostic", "component", "机制", "消融", "诊断", "组件"),
        "qualitative_matched_grid": ("qualitative grid", "montage", "reference column", "ground-truth", "sample card", "质性", "定性", "网格", "参考列"),
        "direct_labels_reference_lines": ("direct label", "reference line", "threshold", "直接标", "参考线", "阈值"),
        "failure_aware_display": ("failure", "oom", "censor", "stopping rule", "失败", "停止规则", "截断"),
        "main_appendix_handoff": ("appendix", "main figure", "main table", "正文", "附录"),
    },
    "failure": {
        "missing_uncertainty": ("no uncertainty", "omit.*uncertainty", "point estimate", "without uncertainty", "缺少.*不确定", "没有.*不确定", "未.*误差", "缺少.*seed", "没有.*seed", "未.*seed", "point estimates"),
        "color_only_or_grayscale_unsafe": ("color-only", "grayscale", "colour-only", "颜色.*灰度", "灰度.*安全", "辨色", "color carries"),
        "caption_not_self_contained": ("caption.*short", "caption.*omit", "caption.*not self", "caption.*implicit", "图注.*过短", "caption 过短", "不自包含", "依赖正文"),
        "small_text_or_dense_layout": ("small text", "tiny", "dense", "overcrowd", "narrow plot", "缩小", "小.*pt", "密集", "拥挤", "可读性"),
        "qualitative_sampling_gap": ("qualitative.*without", "qualitative.*omit", "first-seed", "sample selection", "prompt.*link", "质性.*没有", "定性.*缺", "样本选择", "筛选"),
        "missing_denominator_or_protocol": ("denominator", "sample count", "aggregation", "protocol", "unit", "分母", "样本数", "聚合", "协议", "单位"),
        "raster_or_source_gap": ("raster", "jpeg", "no public", "source-level", "plotting.*source", "generator", "源码", "源文件", "公共仓库", "模糊"),
        "inconsistent_visual_semantics": ("inconsistent", "unstable", "switch", "mixed.*precision", "不一致", "混用", "切换"),
        "weak_mechanism_attribution": ("do not identify component", "cannot identify", "no.*isolation", "missing.*ablation", "不能.*归因", "没有.*隔离", "缺少.*消融", "替代解释"),
        "undefined_failure_or_censoring": ("censor", "off-scale", "stopping", "infinite-loop", "oom.*without", "截断", "停止", "失败.*未", "oom"),
    },
}

JUDGMENT_THEME_LABELS_ZH = {
    "method_interface": "方法接口图",
    "matched_multi_panel": "同构多面板对照",
    "trend_plus_exact_table": "趋势图与精确数值表配对",
    "grouped_booktabs_table": "分组 booktabs 表",
    "cost_quality_pair": "效果—成本配对",
    "mechanism_ablation_chain": "机制—消融证据链",
    "qualitative_matched_grid": "匹配式质性网格",
    "direct_labels_reference_lines": "直接标注与参考线",
    "failure_aware_display": "显式失败编码",
    "main_appendix_handoff": "正文—附录交接",
    "missing_uncertainty": "缺少不确定性",
    "color_only_or_grayscale_unsafe": "颜色单通道或灰度失效",
    "caption_not_self_contained": "图注/表注不自包含",
    "small_text_or_dense_layout": "小字或高密度拥挤",
    "qualitative_sampling_gap": "质性样本协议缺口",
    "missing_denominator_or_protocol": "分母、聚合或协议缺口",
    "raster_or_source_gap": "栅格清晰度或视觉源码缺口",
    "inconsistent_visual_semantics": "跨对象视觉语义不一致",
    "weak_mechanism_attribution": "机制归因不足",
    "undefined_failure_or_censoring": "失败/截断定义不足",
}

EVIDENCE_RELATION_THEMES = {
    "equation_theorem_or_proof": r"\b(?:eq(?:uation)?s?|theorem|lemma|corollary|proposition|proof)\b|公式|方程|定理|引理|推论|证明",
    "algorithm_or_execution": r"\b(?:algorithm|pseudocode|procedure|update rule)\b|算法|伪代码|执行流程|更新规则",
    "method_component_or_pipeline": r"\b(?:method|component|module|architecture|pipeline|framework|mechanism)\b|方法|组件|模块|架构|流程|机制",
    "experimental_protocol_or_setup": r"\b(?:protocol|setup|dataset|benchmark|metric|baseline|budget|seed|hardware)\b|协议|设置|数据集|基线|指标|预算|硬件",
    "main_result_or_comparison": r"\b(?:main result|headline|comparison|performance|improvement|outperform)\b|主结果|比较|性能|提升|优于",
    "ablation_or_mechanism_test": r"\b(?:ablation|intervention|diagnostic|component removal|sensitivity)\b|消融|干预|诊断|敏感性",
    "robustness_or_generalization": r"\b(?:robustness|generalization|distribution shift|stress test)\b|鲁棒|泛化|分布偏移|压力测试",
    "efficiency_cost_or_failure": r"\b(?:efficiency|cost|latency|runtime|memory|oom|failure|error case)\b|效率|成本|延迟|运行时间|显存|失败|错误案例",
    "qualitative_evidence": r"\b(?:qualitative|sample|example|visualization|montage|case study)\b|质性|定性|样本|案例|可视化",
    "main_appendix_handoff": r"\b(?:appendix|supplement|supplementary|full results|additional results)\b|附录|补充材料|完整结果|追加结果",
}

EVIDENCE_RELATION_LABELS_ZH = {
    "equation_theorem_or_proof": "公式、定理或证明",
    "algorithm_or_execution": "算法或执行流程",
    "method_component_or_pipeline": "方法组件或流程",
    "experimental_protocol_or_setup": "实验协议或设置",
    "main_result_or_comparison": "主结果或比较",
    "ablation_or_mechanism_test": "消融或机制检验",
    "robustness_or_generalization": "鲁棒性或泛化",
    "efficiency_cost_or_failure": "效率、成本或失败",
    "qualitative_evidence": "质性证据",
    "main_appendix_handoff": "正文—附录交接",
}


def font_family_class(families: Iterable[str]) -> str:
    value = " ".join(families).lower().replace("-", " ")
    if any(token in value for token in ("nimbus roman", "times", "texgyretermes", "liberation serif")):
        return "times_like_serif"
    if any(token in value for token in ("computer modern", "cmr", "cmsy", "cmmi")):
        return "computer_modern"
    if any(token in value for token in ("libertine", "linuxlibertine", "biolinum")):
        return "libertine"
    if any(token in value for token in ("dejavu sans", "arial", "helvetica", "nimbus sans", "liberation sans")):
        return "sans_serif"
    if any(token in value for token in ("dejavu serif", "palatino", "bookman", "charter")):
        return "other_serif"
    return "other_or_unknown"


def table_uncertainty_modes(text: str) -> list[str]:
    """Map free-form table audit notes to stable display categories."""

    value = text.lower()
    modes: list[str] = []

    def positive(pattern: str) -> bool:
        for match in re.finditer(pattern, value):
            before = value[max(0, match.start() - 48) : match.start()]
            after = value[match.end() : match.end() + 32]
            before_clause = re.split(r"[.;。；]", before)[-1]
            after_clause = re.split(r"[.;。；]", after)[0]
            if re.search(r"\b(?:no|not|without|neither|missing|omit(?:s|ted)?)\b|(?:没有|未|无|缺少)", before_clause):
                continue
            if re.match(r"\s*(?:is|are|was|were)?\s*(?:not|absent|missing)|\s*(?:未|无|没有)", after_clause):
                continue
            return True
        return False

    patterns = (
        ("standard_deviation", r"mean\s*±\s*(?:std|sd)|±\s*(?:std|sd)|standard deviation|标准差"),
        ("standard_error", r"mean\s*±\s*se|±\s*se\b|standard error|标准误"),
        ("confidence_interval", r"confidence interval|\b\d{2,3}%\s*ci\b|置信区间"),
        ("quantile_or_range", r"\b(?:quantile|percentile|interquartile|iqr)\b|四分位|百分位"),
        ("significance_marker", r"\bp[- ]?value\b|significance marker|statistically significant|显著性标记"),
        ("distribution_summary", r"\b(?:histogram|boxplot|box plot|violin plot)\b|分布摘要"),
        ("repeat_count_only", r"\b\d+\s*(?:seeds?|trials?|runs?|repetitions?)\b|(?:seed|trial|run)[- ]level|\d+\s*次(?:运行|重复)"),
    )
    for label, pattern in patterns:
        if positive(pattern):
            modes.append(label)
    absence_tokens = (
        "no uncertainty", "without uncertainty", "no error", "point estimate", "point metric",
        "single value", "未给", "无误差", "无区间", "无 seed", "无 seed-level", "点估计",
        "没有 run-level", "没有 uncertainty", "未报告不确定性",
    )
    uncertainty_modes = [mode for mode in modes if mode != "repeat_count_only"]
    if not uncertainty_modes and any(token in value for token in absence_tokens):
        modes.append("point_only_or_undefined")
    return list(dict.fromkeys(modes)) or ["unclassified"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=int, default=250)
    parser.add_argument("--allow-partial", action="store_true")
    return parser.parse_args()


def quantile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    fraction = position - lower
    return ordered[lower] * (1 - fraction) + ordered[upper] * fraction


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def target_papers(target: int) -> list[dict[str, str]]:
    rows = []
    for sample in read_csv(PROCESSED / "analysis_sample.csv"):
        if load_complete_reading(sample["paper_id"]) is not None:
            rows.append(sample)
    if len(rows) != target:
        raise SystemExit(f"expected {target} complete checkpoint readings; found {len(rows)}")
    return rows


def load_audits(samples: list[dict[str, str]]) -> list[tuple[dict[str, str], dict[str, object]]]:
    schema = json.loads((ROOT / "schemas" / "visual-audit.schema.json").read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    records = []
    for sample in samples:
        path = AUDIT_DIR / f"{sample['paper_id']}.json"
        if not path.exists():
            continue
        audit = json.loads(path.read_text(encoding="utf-8"))
        errors = list(validator.iter_errors(audit))
        if errors:
            first = errors[0]
            location = ".".join(str(part) for part in first.absolute_path) or "<root>"
            raise SystemExit(f"schema error {sample['paper_id']} at {location}: {first.message}")
        records.append((sample, audit))
    return records


def flatten_objects(records: list[tuple[dict[str, str], dict[str, object]]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sample, audit in records:
        for kind in ("figures", "tables"):
            for item in audit[kind]:
                base = {
                    "paper_id": sample["paper_id"],
                    "conference": sample["conference"],
                    "analysis_stratum": sample["analysis_stratum"],
                    "kind": kind[:-1],
                    "label": item["label"],
                    "page": item["page"],
                    "module": item["module"],
                    "placement": item["placement"],
                    "width": item["width"],
                    "purpose": "|".join(item["purpose"]),
                    "caption_words": item["caption"]["word_count"],
                    "caption_moves": "|".join(item["caption"]["moves"]),
                    "caption_headline_bold": int(item["caption"]["headline_bold"]),
                    "caption_self_contained": int(item["caption"]["self_contained"]),
                    "caption_main_finding": int(item["caption"]["main_finding_stated"]),
                }
                if kind == "figures":
                    grammar = item["plot_grammar"]
                    rows.append(
                        {
                            **base,
                            "types": "|".join(item["types"]),
                            "panels": item["complexity"]["panels"],
                            "series": item["complexity"]["series"],
                            "legend_items": item["complexity"]["legend_items"],
                            "annotations": item["complexity"]["annotations"],
                            "data_marks_estimate": item["complexity"]["data_marks_estimate"],
                            "complexity": item["complexity"]["score"],
                            "font_family": "|".join(item["typography"]["family"]),
                            "font_family_class": font_family_class(item["typography"]["family"]),
                            "font_size_min": item["typography"]["size_pt"]["minimum"],
                            "font_size_median": item["typography"]["size_pt"]["median"],
                            "font_size_max": item["typography"]["size_pt"]["maximum"],
                            "font_weight": "|".join(item["typography"]["weight"]),
                            "font_style": "|".join(item["typography"]["style"]),
                            "typography_provenance": item["typography"]["provenance"],
                            "typography_confidence": item["typography"]["confidence"],
                            "color_mode": item["color"]["mode"],
                            "color_count": item["color"]["color_count"],
                            "palette_hex": "|".join(item["color"]["hex"]),
                            "color_provenance": item["color"]["provenance"],
                            "redundant_encoding": int(item["color"]["redundant_encoding"]),
                            "grayscale_safe": int(item["color"]["grayscale_safe"]),
                            "rendering": grammar["rendering"],
                            "x_scale": grammar["x_scale"],
                            "y_scale": grammar["y_scale"],
                            "grid": grammar["grid"],
                            "legend_present": int(grammar["legend_present"]),
                            "legend_placement": grammar["legend_placement"],
                            "shared_legend": grammar["shared_legend"],
                            "direct_labels": int(grammar["direct_labels"]),
                            "marker_types": grammar["marker_types"],
                            "line_styles": grammar["line_styles"],
                            "hatching": int(grammar["hatching"]),
                            "reference_lines": grammar["reference_lines"],
                            "uncertainty_display": grammar["uncertainty_display"],
                            "line_width_pt": grammar["line_width_pt"],
                            "table_rows": "",
                            "table_columns": "",
                            "table_header_levels": "",
                            "table_row_groups": "",
                            "decimal_precision": "",
                            "table_rules": "",
                            "highlighting": "",
                            "table_uncertainty": "",
                            "table_uncertainty_modes": "",
                        }
                    )
                else:
                    rows.append(
                        {
                            **base,
                            "types": "table",
                            "panels": 1,
                            "series": "",
                            "legend_items": "",
                            "annotations": "",
                            "data_marks_estimate": "",
                            "complexity": "",
                            "font_family": "|".join(item["typography"]["family"]),
                            "font_family_class": font_family_class(item["typography"]["family"]),
                            "font_size_min": item["typography"]["body_size_pt"],
                            "font_size_median": item["typography"]["body_size_pt"],
                            "font_size_max": item["typography"]["header_size_pt"],
                            "font_weight": item["typography"]["header_weight"],
                            "font_style": "",
                            "typography_provenance": item["typography"]["provenance"],
                            "typography_confidence": item["typography"]["confidence"],
                            "color_mode": "grayscale" if not any(token in item["highlighting"] for token in ("cell_color", "text_color")) else "mixed",
                            "color_count": "",
                            "palette_hex": "",
                            "color_provenance": "",
                            "redundant_encoding": "",
                            "grayscale_safe": "",
                            "rendering": "",
                            "x_scale": "",
                            "y_scale": "",
                            "grid": "",
                            "legend_present": "",
                            "legend_placement": "",
                            "shared_legend": "",
                            "direct_labels": "",
                            "marker_types": "",
                            "line_styles": "",
                            "hatching": "",
                            "reference_lines": "",
                            "uncertainty_display": "",
                            "line_width_pt": "",
                            "table_rows": item["rows"],
                            "table_columns": item["columns"],
                            "table_header_levels": item["header_levels"],
                            "table_row_groups": item["row_groups"],
                            "decimal_precision": item["decimal_precision"],
                            "table_rules": item["rules"],
                            "highlighting": "|".join(item["highlighting"]),
                            "table_uncertainty": item["uncertainty"],
                            "table_uncertainty_modes": "|".join(table_uncertainty_modes(item["uncertainty"])),
                        }
                    )
    return rows


def categorical_values(row: dict[str, object], field: str) -> list[str]:
    value = row.get(field)
    if value is None or value == "":
        return []
    if field in {
        "types", "purpose", "caption_moves", "font_family", "font_weight", "font_style", "highlighting",
        "table_uncertainty_modes",
    }:
        return [part for part in str(value).split("|") if part]
    return [str(value)]


def categorical_summary(
    objects: list[dict[str, object]], paper_conference: dict[str, str]
) -> list[dict[str, object]]:
    fields = (
        "kind", "placement", "module", "width", "purpose", "types", "caption_moves",
        "caption_headline_bold", "caption_self_contained", "caption_main_finding",
        "font_family", "font_family_class", "font_weight", "font_style", "typography_provenance", "typography_confidence",
        "color_mode", "color_provenance", "redundant_encoding", "grayscale_safe", "rendering",
        "x_scale", "y_scale", "grid", "legend_present", "legend_placement", "shared_legend", "direct_labels",
        "hatching", "uncertainty_display", "table_rules", "highlighting", "table_uncertainty_modes",
    )
    papers = sorted(paper_conference)
    conference_of = paper_conference
    by_paper_objects: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in objects:
        by_paper_objects[str(row["paper_id"])].append(row)
    rows: list[dict[str, object]] = []
    for field in fields:
        vocabulary = sorted({value for row in objects for value in categorical_values(row, field)})
        for value in vocabulary:
            paper_presence = []
            paper_share = []
            for paper_id in papers:
                paper_rows = by_paper_objects.get(paper_id, [])
                hits = sum(value in categorical_values(row, field) for row in paper_rows)
                paper_presence.append((conference_of[paper_id], float(hits > 0)))
                paper_share.append((conference_of[paper_id], hits / len(paper_rows) if paper_rows else 0.0))
            object_hits = sum(value in categorical_values(row, field) for row in objects)
            conference_presence = defaultdict(list)
            conference_share = defaultdict(list)
            for conference, item in paper_presence:
                conference_presence[conference].append(item)
            for conference, item in paper_share:
                conference_share[conference].append(item)
            rows.append(
                {
                    "dimension": field,
                    "value": value,
                    "papers": len(papers),
                    "papers_present": int(sum(item for _, item in paper_presence)),
                    "paper_prevalence": round(statistics.fmean(item for _, item in paper_presence), 6),
                    "conference_equal_paper_prevalence": round(
                        statistics.fmean(statistics.fmean(values) for values in conference_presence.values()), 6
                    ),
                    "object_count": object_hits,
                    "object_share": round(object_hits / len(objects), 6),
                    "paper_normalized_object_share": round(statistics.fmean(item for _, item in paper_share), 6),
                    "conference_equal_paper_normalized_share": round(
                        statistics.fmean(statistics.fmean(values) for values in conference_share.values()), 6
                    ),
                }
            )
    return rows


def cross_tab_summary(
    objects: list[dict[str, object]], paper_conference: dict[str, str]
) -> list[dict[str, object]]:
    pairs = (
        ("purpose", "kind"),
        ("purpose", "placement"),
        ("purpose", "types"),
        ("types", "width"),
        ("types", "color_mode"),
        ("types", "x_scale"),
        ("types", "y_scale"),
        ("types", "legend_present"),
        ("types", "legend_placement"),
        ("types", "uncertainty_display"),
        ("purpose", "uncertainty_display"),
        ("kind", "caption_moves"),
        ("placement", "caption_moves"),
        ("purpose", "caption_moves"),
        ("purpose", "width"),
        ("table_rules", "highlighting"),
        ("purpose", "table_rules"),
    )
    papers = sorted(paper_conference)
    by_paper: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in objects:
        by_paper[str(row["paper_id"])].append(row)
    rows: list[dict[str, object]] = []
    for left_field, right_field in pairs:
        left_values = sorted({value for row in objects for value in categorical_values(row, left_field)})
        right_values = sorted({value for row in objects for value in categorical_values(row, right_field)})
        for left_value in left_values:
            for right_value in right_values:
                hits = [
                    row
                    for row in objects
                    if left_value in categorical_values(row, left_field)
                    and right_value in categorical_values(row, right_field)
                ]
                if not hits:
                    continue
                present_papers = {str(row["paper_id"]) for row in hits}
                normalized_shares = []
                conference_shares: dict[str, list[float]] = defaultdict(list)
                for paper_id in papers:
                    paper_rows = by_paper.get(paper_id, [])
                    paper_hits = sum(
                        left_value in categorical_values(row, left_field)
                        and right_value in categorical_values(row, right_field)
                        for row in paper_rows
                    )
                    share = paper_hits / len(paper_rows) if paper_rows else 0.0
                    normalized_shares.append(share)
                    conference_shares[paper_conference[paper_id]].append(share)
                rows.append(
                    {
                        "left_dimension": left_field,
                        "left_value": left_value,
                        "right_dimension": right_field,
                        "right_value": right_value,
                        "papers": len(papers),
                        "papers_present": len(present_papers),
                        "paper_prevalence": round(len(present_papers) / len(papers), 6) if papers else 0,
                        "conference_equal_paper_prevalence": conference_equal_prevalence(
                            present_papers, papers, paper_conference
                        ),
                        "object_count": len(hits),
                        "object_share": round(len(hits) / len(objects), 6) if objects else 0,
                        "paper_normalized_object_share": round(statistics.fmean(normalized_shares), 6)
                        if normalized_shares
                        else 0,
                        "conference_equal_paper_normalized_share": round(
                            statistics.fmean(statistics.fmean(values) for values in conference_shares.values()), 6
                        )
                        if conference_shares
                        else 0,
                    }
                )
    return rows


def numeric_summary(
    objects: list[dict[str, object]], paper_conference: dict[str, str]
) -> list[dict[str, object]]:
    fields = (
        "caption_words", "panels", "series", "legend_items", "annotations", "data_marks_estimate",
        "complexity", "font_size_min", "font_size_median", "font_size_max", "color_count",
        "marker_types", "line_styles", "reference_lines", "line_width_pt", "table_rows",
        "table_columns", "table_header_levels", "table_row_groups", "decimal_precision",
    )
    modules = sorted({str(row["module"]) for row in objects})
    purposes = sorted({value for row in objects for value in categorical_values(row, "purpose")})
    scopes: list[tuple[str, list[dict[str, object]]]] = [("all", objects)]
    scopes.extend((f"kind={kind}", [row for row in objects if row["kind"] == kind]) for kind in ("figure", "table"))
    scopes.extend(
        (f"placement={placement}", [row for row in objects if row["placement"] == placement])
        for placement in ("main", "appendix")
    )
    scopes.extend(
        (
            f"kind={kind}|placement={placement}",
            [row for row in objects if row["kind"] == kind and row["placement"] == placement],
        )
        for kind in ("figure", "table")
        for placement in ("main", "appendix")
    )
    scopes.extend((f"module={module}", [row for row in objects if row["module"] == module]) for module in modules)
    scopes.extend(
        (
            f"purpose={purpose}",
            [row for row in objects if purpose in categorical_values(row, "purpose")],
        )
        for purpose in purposes
    )
    rows: list[dict[str, object]] = []
    for scope, selected in scopes:
        if not selected:
            continue
        for field in fields:
            values = [float(row[field]) for row in selected if row.get(field) not in (None, "")]
            if not values:
                continue
            by_paper: dict[str, list[float]] = defaultdict(list)
            for row in selected:
                if row.get(field) not in (None, ""):
                    by_paper[str(row["paper_id"])].append(float(row[field]))
            per_paper_means = {paper_id: statistics.fmean(items) for paper_id, items in by_paper.items()}
            conference_paper_means: dict[str, list[float]] = defaultdict(list)
            for paper_id, value in per_paper_means.items():
                conference_paper_means[paper_conference[paper_id]].append(value)
            rows.append(
                {
                    "scope": scope,
                    "metric": field,
                    "n": len(values),
                    "eligible_papers": len(per_paper_means),
                    "mean": round(statistics.fmean(values), 6),
                    "median": round(statistics.median(values), 6),
                    "q1": round(quantile(values, 0.25), 6),
                    "q3": round(quantile(values, 0.75), 6),
                    "min": round(min(values), 6),
                    "max": round(max(values), 6),
                    "paper_normalized_mean": round(statistics.fmean(per_paper_means.values()), 6),
                    "paper_normalized_median": round(statistics.median(per_paper_means.values()), 6),
                    "conference_equal_paper_normalized_mean": round(
                        statistics.fmean(statistics.fmean(group) for group in conference_paper_means.values()), 6
                    ),
                }
            )
    return rows


def conditional_summary(
    objects: list[dict[str, object]], paper_conference: dict[str, str]
) -> list[dict[str, object]]:
    """Measure right-value prevalence within a left-value denominator.

    Every paper first contributes one conditional share, then the two conference
    means receive equal weight. This keeps papers with dozens of appendix panels
    from defining the visual grammar for the cohort.
    """

    pairs = (
        ("kind", "placement"),
        ("kind", "width"),
        ("kind", "module"),
        ("kind", "purpose"),
        ("kind", "types"),
        ("kind", "caption_moves"),
        ("kind", "caption_headline_bold"),
        ("kind", "caption_self_contained"),
        ("kind", "caption_main_finding"),
        ("kind", "font_family_class"),
        ("kind", "font_weight"),
        ("kind", "color_mode"),
        ("kind", "rendering"),
        ("kind", "redundant_encoding"),
        ("kind", "grayscale_safe"),
        ("kind", "grid"),
        ("kind", "legend_present"),
        ("kind", "direct_labels"),
        ("kind", "uncertainty_display"),
        ("kind", "table_rules"),
        ("kind", "highlighting"),
        ("kind", "table_uncertainty_modes"),
        ("placement", "kind"),
        ("placement", "width"),
        ("placement", "caption_moves"),
        ("purpose", "kind"),
        ("purpose", "placement"),
        ("purpose", "types"),
        ("purpose", "width"),
        ("purpose", "caption_moves"),
        ("types", "color_mode"),
        ("types", "legend_present"),
        ("types", "shared_legend"),
        ("types", "x_scale"),
        ("types", "y_scale"),
        ("types", "grid"),
        ("types", "uncertainty_display"),
        ("table_rules", "highlighting"),
    )
    by_paper: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in objects:
        by_paper[str(row["paper_id"])].append(row)
    rows: list[dict[str, object]] = []
    for left_field, right_field in pairs:
        left_values = sorted({value for row in objects for value in categorical_values(row, left_field)})
        right_values = sorted({value for row in objects for value in categorical_values(row, right_field)})
        for left_value in left_values:
            denominator_objects = [
                row for row in objects if left_value in categorical_values(row, left_field)
            ]
            if not denominator_objects:
                continue
            eligible_papers = {str(row["paper_id"]) for row in denominator_objects}
            for right_value in right_values:
                numerator_objects = [
                    row
                    for row in denominator_objects
                    if right_value in categorical_values(row, right_field)
                ]
                if not numerator_objects:
                    continue
                papers_present = {str(row["paper_id"]) for row in numerator_objects}
                paper_shares: dict[str, float] = {}
                conference_shares: dict[str, list[float]] = defaultdict(list)
                for paper_id in eligible_papers:
                    paper_denominator = [
                        row
                        for row in by_paper[paper_id]
                        if left_value in categorical_values(row, left_field)
                    ]
                    hits = sum(
                        right_value in categorical_values(row, right_field)
                        for row in paper_denominator
                    )
                    share = hits / len(paper_denominator)
                    paper_shares[paper_id] = share
                    conference_shares[paper_conference[paper_id]].append(share)
                rows.append(
                    {
                        "left_dimension": left_field,
                        "left_value": left_value,
                        "right_dimension": right_field,
                        "right_value": right_value,
                        "eligible_papers": len(eligible_papers),
                        "papers_present": len(papers_present),
                        "paper_prevalence_within_left": round(
                            len(papers_present) / len(eligible_papers), 6
                        ),
                        "denominator_objects": len(denominator_objects),
                        "object_count": len(numerator_objects),
                        "conditional_object_share": round(
                            len(numerator_objects) / len(denominator_objects), 6
                        ),
                        "paper_normalized_conditional_share": round(
                            statistics.fmean(paper_shares.values()), 6
                        ),
                        "conference_equal_paper_normalized_conditional_share": round(
                            statistics.fmean(
                                statistics.fmean(values) for values in conference_shares.values()
                            ),
                            6,
                        ),
                    }
                )
    return rows


def paper_level_numeric_summary(
    papers: list[dict[str, object]], paper_conference: dict[str, str]
) -> list[dict[str, object]]:
    fields = (
        "figures", "tables", "main_figures", "main_tables",
        "appendix_figures", "appendix_tables", "visual_source_files",
    )
    rows: list[dict[str, object]] = []
    for field in fields:
        values = [float(row[field]) for row in papers]
        conference_values: dict[str, list[float]] = defaultdict(list)
        for row in papers:
            conference_values[paper_conference[str(row["paper_id"])]].append(float(row[field]))
        rows.append(
            {
                "metric": field,
                "papers": len(values),
                "mean": round(statistics.fmean(values), 6),
                "median": round(statistics.median(values), 6),
                "q1": round(quantile(values, 0.25), 6),
                "q3": round(quantile(values, 0.75), 6),
                "min": round(min(values), 6),
                "max": round(max(values), 6),
                "conference_equal_mean": round(
                    statistics.fmean(statistics.fmean(group) for group in conference_values.values()), 6
                ),
            }
        )
    return rows


def judgment_theme_summary(
    records: list[tuple[dict[str, str], dict[str, object]]]
) -> list[dict[str, object]]:
    paper_conference = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    all_papers = sorted(paper_conference)
    rows: list[dict[str, object]] = []
    for source, themes in JUDGMENT_THEMES.items():
        text_by_paper = {}
        for sample, audit in records:
            field = "most_reusable_patterns" if source == "reusable" else "failure_patterns"
            text_by_paper[sample["paper_id"]] = " ".join(audit["final_judgment"][field]).lower()
        for theme, patterns in themes.items():
            present = {
                paper_id
                for paper_id, text in text_by_paper.items()
                if any(re.search(pattern, text) for pattern in patterns)
            }
            rows.append(
                {
                    "source": source,
                    "theme": theme,
                    "theme_zh": JUDGMENT_THEME_LABELS_ZH[theme],
                    "papers": len(all_papers),
                    "papers_present": len(present),
                    "paper_prevalence": round(len(present) / len(all_papers), 6),
                    "conference_equal_paper_prevalence": conference_equal_prevalence(
                        present, all_papers, paper_conference
                    ),
                }
            )
    return rows


def evidence_relation_summary(
    records: list[tuple[dict[str, str], dict[str, object]]]
) -> list[dict[str, object]]:
    """Quantify which non-visual evidence each Figure/Table explicitly connects to."""

    paper_conference = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    all_papers = sorted(paper_conference)
    object_texts: dict[str, list[str]] = defaultdict(list)
    for sample, audit in records:
        for collection in (audit["figures"], audit["tables"]):
            for item in collection:
                object_texts[sample["paper_id"]].append(
                    " ".join(
                        (
                            item["evidence_relation"],
                            item["caption"]["text"],
                        )
                    ).lower()
                )
    total_objects = sum(len(items) for items in object_texts.values())
    rows: list[dict[str, object]] = []
    for theme, pattern in EVIDENCE_RELATION_THEMES.items():
        papers_present: set[str] = set()
        object_count = 0
        shares_by_conference: dict[str, list[float]] = defaultdict(list)
        for paper_id in all_papers:
            texts = object_texts.get(paper_id, [])
            hits = sum(bool(re.search(pattern, text, re.I)) for text in texts)
            object_count += hits
            if hits:
                papers_present.add(paper_id)
            shares_by_conference[paper_conference[paper_id]].append(hits / len(texts) if texts else 0.0)
        rows.append(
            {
                "theme": theme,
                "theme_zh": EVIDENCE_RELATION_LABELS_ZH[theme],
                "papers": len(all_papers),
                "papers_present": len(papers_present),
                "paper_prevalence": round(len(papers_present) / len(all_papers), 6) if all_papers else 0,
                "conference_equal_paper_prevalence": conference_equal_prevalence(
                    papers_present, all_papers, paper_conference
                ),
                "objects": total_objects,
                "object_count": object_count,
                "object_share": round(object_count / total_objects, 6) if total_objects else 0,
                "conference_equal_paper_normalized_object_share": round(
                    statistics.fmean(
                        statistics.fmean(shares) for shares in shares_by_conference.values()
                    ),
                    6,
                ) if shares_by_conference else 0,
            }
        )
    return rows


def paper_summary(records: list[tuple[dict[str, str], dict[str, object]]]) -> list[dict[str, object]]:
    rows = []
    for sample, audit in records:
        figures = audit["figures"]
        tables = audit["tables"]
        rows.append(
            {
                "paper_id": sample["paper_id"],
                "conference": sample["conference"],
                "analysis_stratum": sample["analysis_stratum"],
                "figures": len(figures),
                "tables": len(tables),
                "main_figures": sum(item["placement"] == "main" for item in figures),
                "main_tables": sum(item["placement"] == "main" for item in tables),
                "appendix_figures": sum(item["placement"] == "appendix" for item in figures),
                "appendix_tables": sum(item["placement"] == "appendix" for item in tables),
                "source_status": audit["source_acquisition"]["status"],
                "selected_repository": audit["source_acquisition"]["selected_repository"] or "",
                "visual_source_files": len(audit["source_acquisition"]["visual_source_files"]),
            }
        )
    return rows


def cross_object_inventory(
    records: list[tuple[dict[str, str], dict[str, object]]]
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for sample, audit in records:
        rows.append(
            {
                "paper_id": sample["paper_id"],
                "conference": sample["conference"],
                "analysis_stratum": sample["analysis_stratum"],
                **audit["cross_object_system"],
            }
        )
    return rows


def caption_language_summary(records: list[tuple[dict[str, str], dict[str, object]]]) -> list[dict[str, object]]:
    captions: list[dict[str, str]] = []
    paper_conference: dict[str, str] = {}
    for sample, audit in records:
        paper_id = sample["paper_id"]
        paper_conference[paper_id] = sample["conference"]
        for collection, kind in ((audit["figures"], "figure"), (audit["tables"], "table")):
            for item in collection:
                captions.append(
                    {
                        "paper_id": paper_id,
                        "conference": sample["conference"],
                        "kind": kind,
                        "placement": item["placement"],
                        "text": item["caption"]["text"],
                        "moves": ">".join(item["caption"]["moves"]),
                    }
                )
    all_papers = sorted(paper_conference)
    rows: list[dict[str, object]] = []
    scopes = {
        "all": captions,
        "figure": [row for row in captions if row["kind"] == "figure"],
        "table": [row for row in captions if row["kind"] == "table"],
        "main": [row for row in captions if row["placement"] == "main"],
        "appendix": [row for row in captions if row["placement"] == "appendix"],
    }
    for scope, selected in scopes.items():
        sequence_counts = Counter(row["moves"] for row in selected if row["moves"])
        sequence_papers: dict[str, set[str]] = defaultdict(set)
        for row in selected:
            if row["moves"]:
                sequence_papers[row["moves"]].add(row["paper_id"])
        for sequence, count in sequence_counts.items():
            rows.append(
                {
                    "scope": scope,
                    "statistic": "caption_move_sequence",
                    "ngram_order": "",
                    "value": sequence,
                    "object_count": count,
                    "object_share": round(count / len(selected), 6) if selected else 0,
                    "papers_present": len(sequence_papers[sequence]),
                    "paper_prevalence": round(len(sequence_papers[sequence]) / len(all_papers), 6) if all_papers else 0,
                    "conference_equal_paper_prevalence": conference_equal_prevalence(
                        sequence_papers[sequence], all_papers, paper_conference
                    ),
                }
            )
        for order in (1, 2, 3, 4):
            counts: Counter[str] = Counter()
            papers_for: dict[str, set[str]] = defaultdict(set)
            for row in selected:
                tokens = re.findall(r"[a-z]+(?:[-'][a-z]+)?", row["text"].lower())
                for index in range(len(tokens) - order + 1):
                    parts = tokens[index : index + order]
                    if all(part in CAPTION_STOPWORDS for part in parts):
                        continue
                    value = " ".join(parts)
                    counts[value] += 1
                    papers_for[value].add(row["paper_id"])
            minimum_papers = max(2, math.ceil(len(all_papers) * 0.02))
            for value, count in counts.most_common():
                if len(papers_for[value]) < minimum_papers:
                    continue
                rows.append(
                    {
                        "scope": scope,
                        "statistic": "caption_ngram",
                        "ngram_order": order,
                        "value": value,
                        "object_count": count,
                        "object_share": round(count / len(selected), 6) if selected else 0,
                        "papers_present": len(papers_for[value]),
                        "paper_prevalence": round(len(papers_for[value]) / len(all_papers), 6) if all_papers else 0,
                        "conference_equal_paper_prevalence": conference_equal_prevalence(
                            papers_for[value], all_papers, paper_conference
                        ),
                    }
                )
    return rows


def conference_equal_prevalence(
    present: set[str], all_papers: list[str], paper_conference: dict[str, str]
) -> float:
    conference_papers: dict[str, list[str]] = defaultdict(list)
    for paper_id in all_papers:
        conference_papers[paper_conference[paper_id]].append(paper_id)
    shares = [sum(paper_id in present for paper_id in papers) / len(papers) for papers in conference_papers.values()]
    return round(statistics.fmean(shares), 6) if shares else 0.0


def color_family(hex_value: str) -> str:
    red, green, blue = (int(hex_value[index : index + 2], 16) / 255 for index in (1, 3, 5))
    hue, saturation, value = colorsys.rgb_to_hsv(red, green, blue)
    if saturation < 0.12:
        return "neutral_light" if value >= 0.72 else "neutral_dark"
    degrees = hue * 360
    if degrees < 15 or degrees >= 345:
        return "red"
    if degrees < 45:
        return "orange"
    if degrees < 70:
        return "yellow"
    if degrees < 165:
        return "green"
    if degrees < 195:
        return "cyan"
    if degrees < 255:
        return "blue"
    if degrees < 290:
        return "purple"
    if degrees < 345:
        return "magenta"
    return "red"


def palette_summary(records: list[tuple[dict[str, str], dict[str, object]]]) -> list[dict[str, object]]:
    paper_conference = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    all_papers = sorted(paper_conference)
    raw_counts: Counter[str] = Counter()
    family_counts: Counter[str] = Counter()
    raw_papers: dict[str, set[str]] = defaultdict(set)
    family_papers: dict[str, set[str]] = defaultdict(set)
    figure_count = 0
    for sample, audit in records:
        for figure in audit["figures"]:
            figure_count += 1
            for value in {item.upper() for item in figure["color"]["hex"]}:
                raw_counts[value] += 1
                raw_papers[value].add(sample["paper_id"])
                family = color_family(value)
                family_counts[family] += 1
                family_papers[family].add(sample["paper_id"])
    rows: list[dict[str, object]] = []
    for statistic, counts, paper_sets in (
        ("hex", raw_counts, raw_papers),
        ("color_family", family_counts, family_papers),
    ):
        for value, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            papers = paper_sets[value]
            rows.append(
                {
                    "statistic": statistic,
                    "value": value,
                    "figure_count": count,
                    "figure_share": round(count / figure_count, 6) if figure_count else 0,
                    "papers_present": len(papers),
                    "paper_prevalence": round(len(papers) / len(all_papers), 6) if all_papers else 0,
                    "conference_equal_paper_prevalence": conference_equal_prevalence(
                        papers, all_papers, paper_conference
                    ),
                }
            )
    return rows


def main() -> None:
    args = parse_args()
    samples = target_papers(args.target)
    records = load_audits(samples)
    if not args.allow_partial and len(records) != args.target:
        raise SystemExit(f"visual aggregation requires {args.target} audits; found {len(records)}")
    objects = flatten_objects(records)
    paper_conference = {sample["paper_id"]: sample["conference"] for sample, _ in records}
    papers = paper_summary(records)
    write_rows(TABLE_DIR / "visual_audit_object_inventory.csv", objects)
    write_rows(TABLE_DIR / "visual_audit_paper_summary.csv", papers)
    write_rows(TABLE_DIR / "visual_cross_object_system.csv", cross_object_inventory(records))
    write_rows(
        TABLE_DIR / "visual_audit_paper_numeric_summary.csv",
        paper_level_numeric_summary(papers, paper_conference),
    )
    write_rows(
        TABLE_DIR / "visual_design_categorical_summary.csv",
        categorical_summary(objects, paper_conference) if objects else [],
    )
    write_rows(
        TABLE_DIR / "visual_design_cross_tabs.csv",
        cross_tab_summary(objects, paper_conference) if objects else [],
    )
    write_rows(
        TABLE_DIR / "visual_design_conditionals.csv",
        conditional_summary(objects, paper_conference) if objects else [],
    )
    write_rows(
        TABLE_DIR / "visual_design_numeric_summary.csv",
        numeric_summary(objects, paper_conference) if objects else [],
    )
    write_rows(TABLE_DIR / "visual_caption_language_summary.csv", caption_language_summary(records))
    write_rows(TABLE_DIR / "visual_palette_summary.csv", palette_summary(records))
    write_rows(TABLE_DIR / "visual_judgment_theme_summary.csv", judgment_theme_summary(records))
    write_rows(TABLE_DIR / "visual_evidence_relation_summary.csv", evidence_relation_summary(records))
    print(
        json.dumps(
            {
                "papers": len(records),
                "figures": sum(row["kind"] == "figure" for row in objects),
                "tables": sum(row["kind"] == "table" for row in objects),
                "complete": len(records) == args.target,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

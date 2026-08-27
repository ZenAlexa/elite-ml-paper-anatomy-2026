#!/usr/bin/env python3
"""Summarize limitation types and adverse-result presentation at a checkpoint."""

from __future__ import annotations

import argparse
import re
from collections.abc import Iterable
from pathlib import Path

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv


LIMITATION_OUTPUT = ROOT / "reports" / "tables" / "checkpoint_250_limitation_type_summary.csv"
PACKAGING_OUTPUT = ROOT / "reports" / "tables" / "checkpoint_250_packaging_strategy_summary.csv"

LIMITATION_PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "scope",
        r"\b(?:scope|boundary|setting|task|domain|modality|benchmark|evaluation|coverage|scale|horizon|context|protocol|dataset|data[- ]?set|single[- ](?:layer|continuous|case)|synthetic|out[- ]of[- ]scope|outside scope|not (?:tested|evaluated|covered)|only .*?(?:tested|evaluated|covered)|current .*?(?:focus|limit))\b|范围|边界|领域|任务|模态|基准|评估|覆盖|规模",
    ),
    (
        "assumption",
        r"\b(?:assumption|assumes?|presuppos|condition|requires?|requirement|hypothes[ie]s|simplification|approximation|bound(?:ed)?|independent[- ]data|trusted server|oracle|fixed[- ]step|precomputed|causal[- ]?assumption|theoretical condition|dependent|relies)\b|假设|条件|要求|近似|简化|前提|依赖",
    ),
    (
        "compute",
        r"\b(?:compute|computation|cost|latency|runtime|memory|gpu|hardware|inference|resource|speed|a100|flop|token budget|time)\b|计算|成本|延迟|速度|内存|硬件|资源|训练时间|推理时间",
    ),
    (
        "data",
        r"\b(?:data|dataset|data[- ]?set|sample|sampling|seed|label|annotation|corpus|prompt|distribution|preprocess|split|domain[- ]specific|synthetic|real[- ]data|training data|test data|population)\b|数据|样本|采样|种子|标注|语料|提示|分布|预处理|划分|群体",
    ),
    (
        "metric",
        r"\b(?:metric|measure|measurement|score|evaluation|judge|proxy|surrogate|uncertainty|variance|standard deviation|standard error|statistical|point estimate|error bar|confidence|calibration|f1|accuracy|recall|precision|psnr|clap|elo|auc|quality|failure)\b|指标|度量|测量|评分|评估|代理|不确定|方差|标准差|统计|误差|置信|准确率|召回|精确率",
    ),
    (
        "baseline",
        r"\b(?:baseline|comparison|comparability|apples?[- ]to[- ]apples?|prior work|prior[- ]work|external method|reference|benchmark(?:s)?(?: comparison)?|fairness|fair comparison|non[- ]apples?)\b|基线|比较|可比|对照|先前工作|公平比较",
    ),
    (
        "generality",
        r"\b(?:generality|generalize|generalization|transfer|external validity|out[- ]of[- ]distribution|ood|cross[- ]domain|cross[- ]dataset|cross[- ]modal|multimodal|broader|wider|other (?:models?|tasks?|settings?)|scale|scaling)\b|泛化|一般性|外部有效|跨域|跨数据集|跨模态|更广|其他模型|其他任务|规模",
    ),
    (
        "causality",
        r"\b(?:caus(?:al|ality)|cause|causal identification|mechanism|mechanistic|confound|confounding|attribution|intervention|perturbation|explanation|explain(?:s|ed|ing)?|correlation|association|identification|counterfactual|dependent)\b|因果|原因|机制|混杂|归因|干预|扰动|解释|相关|识别|反事实",
    ),
    (
        "deployment",
        r"\b(?:deploy(?:ment|ed)?|production|real[- ]world|physical|operational|serving|service|online|runtime|latency|safety|robustness|reliab(?:ility|le)|monitoring|privacy|security|license|legal|commercial|user|application|device|environment|edge)\b|部署|生产|真实世界|物理|服务|在线|运行|安全|鲁棒|可靠|监控|隐私|安全性|许可|法律|商业|用户|应用|设备|环境",
    ),
    (
        "ethics",
        r"\b(?:ethic(?:s|al)?|societal|social|harm|risk|bias|fair(?:ness)?|stereotype|privacy|misinformation|deepfake|malicious|safety|legal|copyright|license|consent|abuse|impact|responsible|discrimination|harmful|security)\b|伦理|社会|伤害|风险|偏见|公平|隐私|错误信息|深伪|恶意|安全|法律|版权|许可|同意|滥用|影响",
    ),
)

PACKAGING_PATTERNS = {
    "position_delayed": re.compile(
        r"position_delayed|position_delay|delayed_limitations|late_limitations|limitations_delayed|位置延后|延后|后置|后移|推迟|结果后置|results_before_failures|positive result front-loading|strong result frontloading|delayed|before",
        re.IGNORECASE,
    ),
    "future_work_framing": re.compile(
        r"future[- ]work|future direction|future extension|future-work|future_work|未来工作|未来方向|未来扩展",
        re.IGNORECASE,
    ),
    "denominator_choice": re.compile(r"denominator|分母", re.IGNORECASE),
    "representative_case": re.compile(
        r"representative|qualitative case|selected case|selected qualitative|example|visual example|single[- ]case|case study|two cases|代表性|案例|精选|示例|样例|单例|example[- ]driven|failure case|walkthrough",
        re.IGNORECASE,
    ),
    "metric_substitution": re.compile(
        r"metric substitution|metric substitute|metric proxy|proxy metric|proxy outcome|substitut|proxy|代(?:理|替)|指标替代|指标代理",
        re.IGNORECASE,
    ),
    "tone_weakening": re.compile(r"uncertain|on par|appears", re.IGNORECASE),
    "active_positive_discussion": re.compile(r"active|主动|公开", re.IGNORECASE),
}

AGGREGATE_PATTERN = re.compile(r"aggregat|average|mean", re.IGNORECASE)
HETEROGENEITY_PATTERN = re.compile(
    r"heterogen|distribution|task-level|subject|per[- ]?setting|异质|分布|差异|spread|dispersion|outcome|category|per[- ]",
    re.IGNORECASE,
)
INFORMATION_LOSS_PATTERN = re.compile(
    r"mask|hide|compress|loss|omit|without|not represented|hidden|压缩|掩盖|隐藏|省略|不可见|未展示",
    re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=int, default=250)
    parser.add_argument("--limitation-output", type=Path, default=LIMITATION_OUTPUT)
    parser.add_argument("--packaging-output", type=Path, default=PACKAGING_OUTPUT)
    return parser.parse_args()


def normalize(values: Iterable[object]) -> str:
    return re.sub(r"\s+", " ", " ".join(str(value) for value in values)).strip().lower()


def completed_records(target: int) -> list[tuple[dict[str, str], dict[str, object]]]:
    records = []
    for row in read_csv(PROCESSED / "analysis_sample.csv"):
        reading = load_complete_reading(row["paper_id"])
        if reading is not None:
            records.append((row, reading))
    if len(records) != target:
        raise SystemExit(f"checkpoint requires exactly {target} complete sample readings; found {len(records)}")
    paper_ids = [row["paper_id"] for row, _ in records]
    if len(set(paper_ids)) != len(paper_ids):
        raise SystemExit("analysis_sample.csv contains duplicate paper IDs among complete readings")
    return records


def observed_items(reading: dict[str, object], field: str) -> list[dict[str, object]]:
    return [
        item
        for item in reading.get(field, [])
        if str(item.get("status", "")).lower() == "observed"
    ]


def item_text(item: dict[str, object]) -> str:
    return normalize(
        (
            item.get("name", ""),
            item.get("description", ""),
            item.get("limitation_type", ""),
            item.get("strategy", ""),
        )
    )


def name_strategy_text(item: dict[str, object]) -> str:
    return normalize((item.get("name", ""), item.get("strategy", "")))


def has_appendix_evidence(item: dict[str, object], reading: dict[str, object]) -> bool:
    appendix_start = float(reading["page_map"]["main_pages"]) + float(
        reading["page_map"]["reference_pages"]
    )
    for evidence in item.get("evidence", []):
        section = str(evidence.get("section", "")).lower()
        page = float(evidence.get("page", 0))
        if "abstract" in section or "intro" in section:
            continue
        if any(token in section for token in ("limitation", "discussion", "conclusion", "future work")):
            continue
        if appendix_start and page > appendix_start:
            return True
    return False


def limitation_presence(reading: dict[str, object]) -> set[str]:
    texts = [item_text(item) for item in observed_items(reading, "limitations")]
    return {
        category
        for category, pattern in LIMITATION_PATTERNS
        if any(re.search(pattern, text, flags=re.IGNORECASE) for text in texts)
    }


def packaging_presence(reading: dict[str, object]) -> set[str]:
    items = observed_items(reading, "adverse_presentation_strategies")
    full_texts = [item_text(item) for item in items]
    reduced_texts = [name_strategy_text(item) for item in items]
    present: set[str] = set()
    if any(has_appendix_evidence(item, reading) for item in items):
        present.add("appendix_migration")
    if any(PACKAGING_PATTERNS["position_delayed"].search(text) for text in full_texts):
        present.add("position_delayed")
    for category in (
        "future_work_framing",
        "denominator_choice",
        "representative_case",
        "active_positive_discussion",
    ):
        if any(PACKAGING_PATTERNS[category].search(text) for text in reduced_texts):
            present.add(category)
    for category in ("metric_substitution", "tone_weakening"):
        if any(PACKAGING_PATTERNS[category].search(text) for text in full_texts):
            present.add(category)
    if any(
        AGGREGATE_PATTERN.search(text)
        and HETEROGENEITY_PATTERN.search(text)
        and INFORMATION_LOSS_PATTERN.search(text)
        for text in full_texts
    ):
        present.add("aggregation_hides_heterogeneity")
    return present


def summary_rows(
    records: list[tuple[dict[str, str], dict[str, object]]],
    categories: tuple[str, ...],
    presence_by_paper: dict[str, set[str]],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for category in categories:
        for conference in ("ALL", "ICLR", "ICML"):
            subset = [
                row
                for row, _ in records
                if conference == "ALL" or row["conference"] == conference
            ]
            papers_present = sum(
                category in presence_by_paper[row["paper_id"]] for row in subset
            )
            rows.append(
                {
                    "category": category,
                    "conference": conference,
                    "papers": len(subset),
                    "papers_present": papers_present,
                    "prevalence": f"{papers_present / len(subset):.6f}",
                }
            )
    return rows


def main() -> None:
    args = parse_args()
    if args.target < 1:
        raise SystemExit("--target must be positive")
    records = completed_records(args.target)
    limitation_by_paper = {
        row["paper_id"]: limitation_presence(reading) for row, reading in records
    }
    packaging_by_paper = {
        row["paper_id"]: packaging_presence(reading) for row, reading in records
    }
    limitation_rows = summary_rows(
        records,
        tuple(category for category, _ in LIMITATION_PATTERNS),
        limitation_by_paper,
    )
    packaging_rows = summary_rows(
        records,
        (
            "appendix_migration",
            "position_delayed",
            "tone_weakening",
            "representative_case",
            "aggregation_hides_heterogeneity",
            "future_work_framing",
            "denominator_choice",
            "active_positive_discussion",
            "metric_substitution",
        ),
        packaging_by_paper,
    )
    fields = ["category", "conference", "papers", "papers_present", "prevalence"]
    write_csv(args.limitation_output, limitation_rows, fields)
    write_csv(args.packaging_output, packaging_rows, fields)
    print(
        f"completed={len(records)} limitation_rows={len(limitation_rows)} "
        f"packaging_rows={len(packaging_rows)}"
    )


if __name__ == "__main__":
    main()

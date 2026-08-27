#!/usr/bin/env python3
"""Summarize the canonical experimental-design fields for a completed checkpoint.

The taxonomy intentionally matches item *names* only.  Reading agents use
different names for the same design fact, so each regular expression groups
case-, spacing-, and synonym-level variants.  A paper is counted once per
field when at least one matching item has status ``observed``.  Fields overlap
by design, and a field without an observed item is not interpreted as proof
that the paper lacks that fact.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from common import PROCESSED, ROOT, load_complete_reading, read_csv, write_csv


TARGET_OUTPUT = ROOT / "reports" / "tables" / "checkpoint_250_experimental_design_summary.csv"


# Keep this order stable: it is the order used in the checkpoint synthesis.
FIELD_PATTERNS: tuple[tuple[str, str], ...] = (
    (
        "research_questions_or_hypotheses",
        r"research.?question|pre.?listed|pre.?declared|hypothes|preregister|pre.?registration|\brq\b|研究问题|研究目标|研究问题/假设|目标",
    ),
    (
        "data_or_dataset",
        r"dataset|data(?:set)?(?:s)?$|training.?data|evaluation.?data|corpus|split|sampling|prompt|annotation|labels?|benchmark|数据集|数据划分|训练数据|样本",
    ),
    (
        "task_or_environment",
        r"task|benchmark|environment|scenario|evaluation.?target|任务|环境|场景|评测范围|实验范围",
    ),
    (
        "models_or_architecture",
        r"model|backbone|architecture|network|agent|controller|models?|模型|架构|骨干|主干|模型与基线|基模型",
    ),
    (
        "baselines_or_comparators",
        r"baseline|comparator|comparison|reference|基线|比较基线|对照",
    ),
    (
        "metrics_or_evaluation",
        r"metric|evaluation|score|measure|performance|accuracy|aggregation|指标|评测|统计与不确定性|正确性|收益",
    ),
    (
        "seeds_or_repeats",
        r"seed|random|repeat|repl|trial|run|replic|randomness|随机|重复|运行次数|重跑",
    ),
    (
        "budget_or_training_compute",
        r"budget|training|optimization|compute|epoch|step|iteration|token|wall.?clock|duration|runtime|cost|resource|训练|优化|计算|预算|步数|时长|资源",
    ),
    (
        "hyperparameters_or_protocol",
        r"hyperparam|learning.?rate|\blr\b|batch|temperature|schedule|optimizer|config|setting|参数|超参数|配置|优化器",
    ),
    (
        "hardware_or_software_runtime",
        r"hardware|gpu|cpu|accelerator|memory|cuda|hardware|software|runtime|硬件|显卡|软件|实现与硬件|硬件与实现",
    ),
    (
        "implementation_source_or_repro",
        r"implementation|source|code|repo|release|provenance|reproduc|artifact|实现|代码|仓库|复现|来源",
    ),
    (
        "leakage_or_contamination_control",
        r"leak|contamin|held.?out|hold.?out|dedup|de.?dup|data.?split|泄漏|污染|去重|划分",
    ),
    (
        "controls_or_matching",
        r"control|match|same.?setting|fair|confound|isolate|对照|控制|匹配|公平|隔离",
    ),
    (
        "failure_or_stopping_criterion",
        r"failure|criterion|criteria|rule|validity|stop|terminat|fail|失败|判定|停止|终止|有效性",
    ),
    (
        "human_evaluation_or_annotation",
        r"human|annotat|participant|inter.?rater|user.?study|mturk|人类|人工|标注|参与者|用户研究",
    ),
)

COMPILED_PATTERNS = tuple((field, re.compile(pattern, re.IGNORECASE)) for field, pattern in FIELD_PATTERNS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=int, default=250)
    parser.add_argument("--output", type=Path, default=TARGET_OUTPUT)
    return parser.parse_args()


def completed_sample(target: int) -> list[dict[str, str]]:
    sample_rows = read_csv(PROCESSED / "analysis_sample.csv")
    records = [row for row in sample_rows if load_complete_reading(row["paper_id"]) is not None]
    if len(records) != target:
        raise SystemExit(
            f"checkpoint requires exactly {target} complete sample readings; found {len(records)}"
        )
    paper_ids = [row["paper_id"] for row in records]
    if len(set(paper_ids)) != len(paper_ids):
        raise SystemExit("analysis_sample.csv contains duplicate paper IDs among complete readings")
    return records


def observed_field_presence(row: dict[str, str]) -> set[str]:
    reading = load_complete_reading(row["paper_id"])
    if reading is None:  # The caller already checked completeness; retain a defensive guard.
        raise SystemExit(f"complete reading disappeared for {row['paper_id']}")
    observed_names = {
        str(item.get("name", ""))
        for item in reading.get("experimental_design", [])
        if str(item.get("status", "")).lower() == "observed"
    }
    return {
        field
        for field, pattern in COMPILED_PATTERNS
        if any(pattern.search(name) for name in observed_names)
    }


def build_rows(records: list[dict[str, str]]) -> list[dict[str, object]]:
    presence_by_paper = {
        row["paper_id"]: observed_field_presence(row)
        for row in records
    }
    rows: list[dict[str, object]] = []
    for field, _ in FIELD_PATTERNS:
        for conference in ("ALL", "ICLR", "ICML"):
            conference_records = (
                records
                if conference == "ALL"
                else [row for row in records if row["conference"] == conference]
            )
            papers_present = sum(
                field in presence_by_paper[row["paper_id"]] for row in conference_records
            )
            papers = len(conference_records)
            rows.append(
                {
                    "field": field,
                    "conference": conference,
                    "papers": papers,
                    "papers_present": papers_present,
                    "prevalence": f"{papers_present / papers:.6f}",
                }
            )
    return rows


def main() -> None:
    args = parse_args()
    if args.target < 1:
        raise SystemExit("--target must be positive")
    records = completed_sample(args.target)
    rows = build_rows(records)
    write_csv(args.output, rows, ["field", "conference", "papers", "papers_present", "prevalence"])
    print(f"completed={len(records)} output={args.output} rows={len(rows)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
from pathlib import Path

from common import ROOT


MODULE_LABELS = {
    "abstract": "摘要",
    "introduction": "引言",
    "related_work": "相关工作",
    "method": "方法",
    "theory": "理论",
    "experimental_design": "实验设计",
    "results": "结果",
    "ablation": "消融",
    "conclusion": "结论",
    "limitations": "局限",
    "other": "其他正文",
}

ABSTRACT_LABELS = {
    "object_scope": "对象与范围",
    "problem_gap": "问题与缺口",
    "core_idea": "核心洞见",
    "method": "方法",
    "theory": "理论",
    "experimental_setup": "实验设置",
    "quantitative_result": "定量结果",
    "qualitative_result": "定性结果",
    "limitation": "局限",
    "impact_claim": "影响主张",
}

APPENDIX_LABELS = {
    "additional_result": "追加结果",
    "implementation_detail": "实现细节",
    "extended_method": "扩展方法",
    "proof": "证明",
    "robustness": "鲁棒性",
    "dataset_detail": "数据细节",
    "qualitative_example": "定性案例",
    "reproducibility": "复现信息",
    "ablation": "追加消融",
    "hyperparameter": "超参数",
    "failure_case": "失败案例",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render dependency-free SVGs for an exact-N checkpoint.")
    parser.add_argument("--target", type=int, default=250)
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def svg_document(width: int, height: int, title: str, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" fill="#f7f5ef"/>
  <style>
    text {{ font-family: "Source Han Sans SC", "Noto Sans CJK SC", sans-serif; fill: #172026; }}
    .title {{ font-size: 28px; font-weight: 700; }}
    .subtitle {{ font-size: 15px; fill: #566168; }}
    .label {{ font-size: 16px; }}
    .value {{ font-size: 14px; font-variant-numeric: tabular-nums; }}
    .axis {{ stroke: #aeb7b9; stroke-width: 1; }}
    .grid {{ stroke: #dcded9; stroke-width: 1; }}
  </style>
  <text class="title" x="52" y="48">{html.escape(title)}</text>
  {body}
</svg>\n'''


def horizontal_bars(
    path: Path,
    title: str,
    subtitle: str,
    rows: list[tuple[str, float]],
    color: str,
    value_format: str = "{:.1%}",
) -> None:
    width = 1120
    left = 230
    right = 90
    top = 104
    row_height = 48
    height = top + row_height * len(rows) + 60
    maximum = max(value for _, value in rows) or 1.0
    chart_width = width - left - right
    parts = [f'<text class="subtitle" x="52" y="76">{html.escape(subtitle)}</text>']
    for index, (label, value) in enumerate(rows):
        y = top + index * row_height
        bar_width = chart_width * value / maximum
        parts.append(f'<text class="label" x="52" y="{y + 23}">{html.escape(label)}</text>')
        parts.append(f'<rect x="{left}" y="{y + 4}" width="{bar_width:.2f}" height="28" rx="4" fill="{color}"/>')
        parts.append(
            f'<text class="value" x="{min(left + bar_width + 10, width - 65):.2f}" y="{y + 24}">{value_format.format(value)}</text>'
        )
    path.write_text(svg_document(width, height, title, "\n  ".join(parts)), encoding="utf-8")


def grouped_module_objects(path: Path, rows: list[dict[str, str]]) -> None:
    modules = [
        "introduction",
        "related_work",
        "method",
        "theory",
        "experimental_design",
        "results",
        "ablation",
        "conclusion",
        "limitations",
    ]
    by_module = {row["module"]: row for row in rows}
    series = [
        ("图", "conference_equal_figures_mean", "#226f73"),
        ("表", "conference_equal_tables_mean", "#cc6b3d"),
        ("公式", "conference_equal_displayed_equations_mean", "#735d9c"),
    ]
    width = 1240
    height = 720
    left = 180
    right = 70
    top = 120
    bottom = 130
    chart_height = height - top - bottom
    chart_width = width - left - right
    maximum = max(float(by_module[module][field]) for module in modules for _, field, _ in series)
    parts = [
        '<text class="subtitle" x="52" y="76">会议等权均值；每根柱表示每篇论文在对应模块中的对象数</text>'
    ]
    for tick in range(0, int(maximum) + 2):
        y = top + chart_height - chart_height * tick / (int(maximum) + 1)
        parts.append(f'<line class="grid" x1="{left}" y1="{y:.2f}" x2="{width-right}" y2="{y:.2f}"/>')
        parts.append(f'<text class="value" x="{left-18}" y="{y+5:.2f}" text-anchor="end">{tick}</text>')
    group_width = chart_width / len(modules)
    bar_width = group_width * 0.22
    scale_max = int(maximum) + 1
    for module_index, module in enumerate(modules):
        base_x = left + module_index * group_width + group_width * 0.12
        for series_index, (_, field, color) in enumerate(series):
            value = float(by_module[module][field])
            bar_height = chart_height * value / scale_max
            x = base_x + series_index * bar_width
            y = top + chart_height - bar_height
            parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{bar_width-3:.2f}" height="{bar_height:.2f}" fill="{color}" rx="2"/>')
        x_label = left + module_index * group_width + group_width / 2
        parts.append(
            f'<text class="label" x="{x_label:.2f}" y="{top+chart_height+28}" text-anchor="middle" transform="rotate(35 {x_label:.2f} {top+chart_height+28})">{MODULE_LABELS[module]}</text>'
        )
    legend_x = 850
    for index, (name, _, color) in enumerate(series):
        x = legend_x + index * 105
        parts.append(f'<rect x="{x}" y="54" width="18" height="18" fill="{color}" rx="2"/>')
        parts.append(f'<text class="value" x="{x+27}" y="69">{name}</text>')
    path.write_text(svg_document(width, height, "正文各模块的图、表与公式", "\n  ".join(parts)), encoding="utf-8")


def main() -> None:
    args = parse_args()
    table_dir = ROOT / "reports" / "tables"
    figure_dir = ROOT / "reports" / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)
    module_rows = read_csv(table_dir / f"checkpoint_{args.target}_module_summary.csv")
    abstract_rows = read_csv(table_dir / f"checkpoint_{args.target}_abstract_summary.csv")
    categorical_rows = read_csv(table_dir / f"checkpoint_{args.target}_categorical_summary.csv")

    horizontal_bars(
        figure_dir / f"checkpoint_{args.target}_module_shares.svg",
        "正文篇幅的相对分配",
        "250 篇逐篇归一化后再对 ICLR 与 ICML 等权；各模块合计 100%",
        [
            (MODULE_LABELS[row["module"]], float(row["conference_equal_normalized_word_share"]))
            for row in module_rows
            if row["module"] != "appendix"
        ],
        "#226f73",
    )
    grouped_module_objects(
        figure_dir / f"checkpoint_{args.target}_module_objects.svg",
        module_rows,
    )
    horizontal_bars(
        figure_dir / f"checkpoint_{args.target}_abstract_functions.svg",
        "摘要功能的论文覆盖率",
        "同一句可承担多个功能；比例按论文是否至少出现一次计算",
        [
            (ABSTRACT_LABELS[row["function"]], float(row["conference_equal_prevalence"]))
            for row in abstract_rows
        ],
        "#cc6b3d",
    )
    appendix_rows = [
        row
        for row in categorical_rows
        if row["dimension"] == "appendix_category" and row["value"] in APPENDIX_LABELS
    ]
    appendix_rows.sort(key=lambda row: float(row["conference_equal_prevalence"]), reverse=True)
    horizontal_bars(
        figure_dir / f"checkpoint_{args.target}_appendix_categories.svg",
        "附录内容的论文覆盖率",
        "按附录一级模块编码；一篇论文可包含多个类别",
        [
            (APPENDIX_LABELS[row["value"]], float(row["conference_equal_prevalence"]))
            for row in appendix_rows
        ],
        "#735d9c",
    )
    print(f"rendered checkpoint {args.target} figures in {figure_dir}")


if __name__ == "__main__":
    main()

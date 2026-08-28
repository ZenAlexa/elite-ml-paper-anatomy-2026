#!/usr/bin/env python3
"""Build the 250-paper visual analysis and the operational ICLR handbook."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "reports" / "tables"
REPORT = ROOT / "reports" / "visual_design_analysis_250.md"
HANDBOOK = ROOT / "docs" / "iclr-visual-design-handbook.md"


def read(name: str) -> list[dict[str, str]]:
    with (TABLES / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def one(rows: list[dict[str, str]], **keys: str) -> dict[str, str]:
    matches = [row for row in rows if all(row.get(key) == value for key, value in keys.items())]
    if len(matches) != 1:
        raise KeyError(f"expected one row for {keys}; found {len(matches)}")
    return matches[0]


def pct(value: str | float, digits: int = 1) -> str:
    return f"{100 * float(value):.{digits}f}%"


def number(value: str | float, digits: int = 1) -> str:
    return f"{float(value):.{digits}f}"


def integer_up(value: str | float) -> int:
    return math.ceil(float(value))


def main() -> None:
    papers = read("visual_audit_paper_summary.csv")
    if len(papers) != 250:
        raise SystemExit(f"visual report requires 250 completed audits; found {len(papers)}")
    paper_numeric = read("visual_audit_paper_numeric_summary.csv")
    categorical = read("visual_design_categorical_summary.csv")
    conditional = read("visual_design_conditionals.csv")
    numeric = read("visual_design_numeric_summary.csv")
    caption_language = read("visual_caption_language_summary.csv")
    themes = read("visual_judgment_theme_summary.csv")
    evidence_relations = read("visual_evidence_relation_summary.csv")
    palettes = read("visual_palette_summary.csv")
    source_styles = read("visual_source_style_summary.csv")
    acquired_source_files = read("visual_source_files_local.csv")

    def pmetric(metric: str) -> dict[str, str]:
        return one(paper_numeric, metric=metric)

    def cat(dimension: str, value: str) -> dict[str, str]:
        return one(categorical, dimension=dimension, value=value)

    def cond(left_dimension: str, left_value: str, right_dimension: str, right_value: str) -> dict[str, str]:
        return one(
            conditional,
            left_dimension=left_dimension,
            left_value=left_value,
            right_dimension=right_dimension,
            right_value=right_value,
        )

    def num(scope: str, metric: str) -> dict[str, str]:
        return one(numeric, scope=scope, metric=metric)

    def theme(source: str, name: str) -> dict[str, str]:
        return one(themes, source=source, theme=name)

    def evidence(theme_name: str) -> dict[str, str]:
        return one(evidence_relations, theme=theme_name)

    def phrase(scope: str, value: str, order: int) -> dict[str, str]:
        return one(
            caption_language,
            scope=scope,
            statistic="caption_ngram",
            ngram_order=str(order),
            value=value,
        )

    status_counts: dict[str, int] = {}
    for row in papers:
        status_counts[row["source_status"]] = status_counts.get(row["source_status"], 0) + 1
    figures = sum(int(row["figures"]) for row in papers)
    tables = sum(int(row["tables"]) for row in papers)
    total = figures + tables

    source_papers = status_counts.get("exact_visual_source", 0) + status_counts.get("partial_visual_source", 0)
    source_style_denominator = max(
        (int(row["verified_source_papers_with_style_files"]) for row in source_styles),
        default=0,
    )
    acquired_rows = [
        row
        for row in acquired_source_files
        if row["status"] == "acquired" and row.get("origin") == "manual_audit"
    ]
    acquired_source_papers = len({row["paper_id"] for row in acquired_rows})

    def source_top(dimension: str, limit: int) -> str:
        rows = [row for row in source_styles if row["dimension"] == dimension and row["value"] != "absent"]
        rows.sort(key=lambda row: (int(row["papers_present"]), int(row["file_count"])), reverse=True)
        return "、".join(
            f"`{row['value']}`（{int(row['papers_present'])} 篇）" for row in rows[:limit]
        )

    counts_table = []
    for metric, label in (
        ("figures", "全部 Figure"),
        ("tables", "全部 Table"),
        ("main_figures", "正文 Figure"),
        ("main_tables", "正文 Table"),
        ("appendix_figures", "附录 Figure"),
        ("appendix_tables", "附录 Table"),
    ):
        row = pmetric(metric)
        counts_table.append(
            f"| {label} | {number(row['conference_equal_mean'], 2)} | {number(row['median'], 1)} | "
            f"{number(row['q1'], 1)}–{number(row['q3'], 1)} | {number(row['min'], 0)}–{number(row['max'], 0)} |"
        )

    presence_specs = [
        ("kind", "figure", "Figure"),
        ("kind", "table", "Table"),
        ("types", "conceptual_diagram", "概念/机制示意图"),
        ("types", "line", "折线图"),
        ("types", "pipeline", "流程图"),
        ("types", "qualitative_grid", "质性对照网格"),
        ("purpose", "main_comparison", "主比较"),
        ("purpose", "headline", "headline 证据"),
        ("purpose", "robustness", "鲁棒性"),
        ("purpose", "method_interface", "方法接口"),
        ("purpose", "theory_mechanism", "理论/机制"),
        ("purpose", "mechanism", "机制诊断"),
        ("purpose", "ablation", "消融"),
        ("purpose", "experimental_design", "实验设计"),
        ("purpose", "qualitative_evidence", "质性证据"),
        ("purpose", "reproduction", "复现信息"),
        ("purpose", "efficiency_cost", "效率/成本"),
    ]
    presence_rows = []
    for dimension, value, label in presence_specs:
        row = cat(dimension, value)
        presence_rows.append(
            f"| {label} | {pct(row['conference_equal_paper_prevalence'])} | "
            f"{pct(row['conference_equal_paper_normalized_share'])} |"
        )

    palette_rows = [row for row in palettes if row["statistic"] == "hex"]
    palette_rows.sort(key=lambda row: int(row["papers_present"]), reverse=True)
    palette_text = "、".join(
        f"`{row['value']}`（{int(row['papers_present'])} 篇）"
        for row in palette_rows
        if row["value"] not in {"#000000", "#FFFFFF"}
    )
    palette_text = "、".join(palette_text.split("、")[:10])

    fig_caption = num("kind=figure|placement=main", "caption_words")
    tab_caption = num("kind=table|placement=main", "caption_words")
    app_fig_caption = num("kind=figure|placement=appendix", "caption_words")
    app_tab_caption = num("kind=table|placement=appendix", "caption_words")
    main_panels = num("kind=figure|placement=main", "panels")
    app_panels = num("kind=figure|placement=appendix", "panels")
    main_series = num("kind=figure|placement=main", "series")
    main_font = num("kind=figure|placement=main", "font_size_median")
    min_font = num("kind=figure|placement=main", "font_size_min")
    max_font = num("kind=figure|placement=main", "font_size_max")
    line_width = num("kind=figure|placement=main", "line_width_pt")
    marker_types = num("kind=figure|placement=main", "marker_types")
    line_styles = num("kind=figure|placement=main", "line_styles")
    reference_lines = num("kind=figure|placement=main", "reference_lines")
    table_rows = num("kind=table|placement=main", "table_rows")
    table_columns = num("kind=table|placement=main", "table_columns")
    table_headers = num("kind=table|placement=main", "table_header_levels")
    table_precision = num("kind=table|placement=main", "decimal_precision")

    report = f"""# 250 篇 ICLR/ICML 2026 顶级论文图表解剖

本报告逐篇核对 250 篇 Outstanding、Oral、Spotlight 论文的正文与附录，建立 {figures:,} 个 Figure、{tables:,} 个 Table、合计 {total:,} 个视觉对象的人工审计账本。每个对象均记录页码、模块、用途、图型、面板、字体、颜色、坐标、legend、marker、线型、网格、不确定性、caption、表头、数据统计、证据关系和公开视觉源码。逐篇证据见[视觉审计索引](visual_audit_index.md)，结构化对象见 [`visual_audit_object_inventory.csv`](tables/visual_audit_object_inventory.csv)。

统计先在论文内计算对象比例，再计算会议内均值，最后令 ICLR 与 ICML 等权。论文覆盖率回答“多少论文至少出现一次”；论文归一对象占比回答“该类对象在一篇典型论文的视觉预算中占多少”。两者分别用于决定是否纳入和决定投入多少版面。

![对象数量与视觉源码覆盖](figures/visual_audit_counts_and_sources.svg)

## 一、每篇论文放多少图表

| 对象 | 会议等权均值 | 中位数 | Q1–Q3 | 范围 |
|---|---:|---:|---:|---:|
{chr(10).join(counts_table)}

按会议等权均值向上取整，一篇完整论文采用 **{integer_up(pmetric('main_figures')['conference_equal_mean'])} 幅正文 Figure、{integer_up(pmetric('main_tables')['conference_equal_mean'])} 张正文 Table、{integer_up(pmetric('appendix_figures')['conference_equal_mean'])} 幅附录 Figure、{integer_up(pmetric('appendix_tables')['conference_equal_mean'])} 张附录 Table**。正文 Figure 中 {pct(cond('kind', 'figure', 'placement', 'main')['conference_equal_paper_normalized_conditional_share'])} 位于正文，Table 中 {pct(cond('kind', 'table', 'placement', 'appendix')['conference_equal_paper_normalized_conditional_share'])} 位于附录：图负责在正文完成论证，表负责在附录保留精确数值与覆盖面。

## 二、超过 60% 论文的视觉构件

下表的第一列是论文覆盖率，第二列是逐篇归一后的视觉预算占比。一个对象可同时承担多个用途。

| 构件/用途 | 论文覆盖率 | 论文归一对象占比 |
|---|---:|---:|
{chr(10).join(presence_rows)}

![超过 60% 论文的核心视觉构件](figures/visual_audit_core_prevalence.svg)

Figure 与 Table 共同构成正文主干：概念/机制图定义对象和信息流，流程图给出执行接口，折线图展示尺度、预算、时间或超参变化，表格给出精确比较值。主比较、headline、鲁棒性、方法接口、机制、消融、实验设计、复现与成本共同组成闭环；将多个用途绑定到同一视觉对象，可在 9 页内覆盖全部高频职责。

## 三、Figure 的制作范式

### 3.1 尺寸、面板和复杂度

- 对 ICLR checkpoint PDF 的第二页双栏版面测量得到 5.50 in 正文宽度和 2.63 in 对称单栏宽度；逐篇结果见 [`iclr_pdf_layout_measurements.csv`](tables/iclr_pdf_layout_measurements.csv)。
- Figure 的页宽对象占 {pct(cond('kind', 'figure', 'width', 'page_width')['conference_equal_paper_normalized_conditional_share'])}，单栏对象占 {pct(cond('kind', 'figure', 'width', 'single_column')['conference_equal_paper_normalized_conditional_share'])}。
- Figure 的 vector、raster、mixed 渲染分别占 {pct(cond('kind', 'figure', 'rendering', 'vector')['conference_equal_paper_normalized_conditional_share'])}、{pct(cond('kind', 'figure', 'rendering', 'raster')['conference_equal_paper_normalized_conditional_share'])}、{pct(cond('kind', 'figure', 'rendering', 'mixed')['conference_equal_paper_normalized_conditional_share'])}；曲线、示意和表格优先保留矢量，真实图像只栅格化对应 panel。
- 正文 Figure 的面板中位数为 {number(main_panels['median'], 0)}，Q1–Q3 为 {number(main_panels['q1'], 0)}–{number(main_panels['q3'], 0)}；附录中位数为 {number(app_panels['median'], 0)}，Q1–Q3 为 {number(app_panels['q1'], 0)}–{number(app_panels['q3'], 0)}。
- 正文数据图系列数中位数为 {number(main_series['median'], 0)}，Q1–Q3 为 {number(main_series['q1'], 0)}–{number(main_series['q3'], 0)}。正文用 2–4 个面板、4 个主要系列；附录再扩展 facet、数据集和失败切片。
- 正文图复杂度中位数为 {number(num('kind=figure|placement=main', 'complexity')['median'], 0)}/5。方法总览保持 2–3，主结果/消融保持 3–4，密集 qualitative grid 与全量诊断放入附录。

### 3.2 字体、字重和线条

- Figure 内文字中位数为 {number(main_font['median'], 1)} pt；最小字号中位数 {number(min_font['median'], 1)} pt，最大字号中位数 {number(max_font['median'], 1)} pt。
- Times-like serif 是 Figure 的主要字体类别，占逐篇归一 Figure 对象的 {pct(cond('kind', 'figure', 'font_family_class', 'times_like_serif')['conference_equal_paper_normalized_conditional_share'])}；regular 与 bold 分别承担数据标签和层级标题。
- 数据线宽中位数为 {number(line_width['median'], 1)} pt，Q1–Q3 为 {number(line_width['q1'], 1)}–{number(line_width['q3'], 1)} pt。
- 正文 Figure 的 marker 类型、线型和参考线数量中位数为 {number(marker_types['median'], 0)}/{number(line_styles['median'], 0)}/{number(reference_lines['median'], 0)}；同一系列的颜色、marker 与线型在正文和附录保持绑定。
- 可直接采用：8 pt 常规字、8.5 pt panel/局部标题、7.5 pt tick/legend、6 pt 绝对下限、1 pt 数据线、0.6–0.8 pt 轴线、3.5 pt marker。

### 3.3 颜色和编码

Figure 中 categorical palette 占 {pct(cond('kind', 'figure', 'color_mode', 'categorical')['conference_equal_paper_normalized_conditional_share'])}，mixed palette 占 {pct(cond('kind', 'figure', 'color_mode', 'mixed')['conference_equal_paper_normalized_conditional_share'])}。颜色、marker、线型或直接文字构成冗余编码的 Figure 占 {pct(cond('kind', 'figure', 'redundant_encoding', '1')['conference_equal_paper_normalized_conditional_share'])}。

最高频 HEX 以 Matplotlib/Tableau 主色为核心：{palette_text}。推荐序列固定为 `#1F77B4`、`#FF7F0E`、`#2CA02C`、`#D62728`、`#9467BD`；同一方法在所有图中保持同色，并同时绑定 marker 和线型。

### 3.4 坐标、legend、网格和不确定性

- 折线图中双轴网格占 {pct(cond('types', 'line', 'grid', 'both')['conference_equal_paper_normalized_conditional_share'])}，无网格占 {pct(cond('types', 'line', 'grid', 'none')['conference_equal_paper_normalized_conditional_share'])}；采用 0.45 pt、低 alpha 的浅灰网格。
- 折线图 x/y 轴使用 linear scale 的比例为 {pct(cond('types', 'line', 'x_scale', 'linear')['conference_equal_paper_normalized_conditional_share'])}/{pct(cond('types', 'line', 'y_scale', 'linear')['conference_equal_paper_normalized_conditional_share'])}，使用 log scale 为 {pct(cond('types', 'line', 'x_scale', 'log')['conference_equal_paper_normalized_conditional_share'])}/{pct(cond('types', 'line', 'y_scale', 'log')['conference_equal_paper_normalized_conditional_share'])}；log 轴在轴标签与 caption 同时声明。
- 折线图使用 legend 的对象占 {pct(cond('types', 'line', 'legend_present', '1')['conference_equal_paper_normalized_conditional_share'])}；legend 项数中位数为 {number(num('kind=figure|placement=main', 'legend_items')['median'], 0)}。series 不超过 4 时直接标注末端，更多 series 使用共享 legend。
- 折线图共享 legend 占 {pct(cond('types', 'line', 'shared_legend', 'True')['conference_equal_paper_normalized_conditional_share'])}；多面板图只保留一份共享 legend，并按视觉读取顺序排列。
- Figure 的直接标注占 {pct(cond('kind', 'figure', 'direct_labels', '1')['conference_equal_paper_normalized_conditional_share'])}。
- Figure 未显示不确定性的对象占 {pct(cond('kind', 'figure', 'uncertainty_display', 'none')['conference_equal_paper_normalized_conditional_share'])}；band 与 error bar 分别占 {pct(cond('kind', 'figure', 'uncertainty_display', 'band')['conference_equal_paper_normalized_conditional_share'])} 和 {pct(cond('kind', 'figure', 'uncertainty_display', 'error_bar')['conference_equal_paper_normalized_conditional_share'])}。新论文的主结果、消融和敏感性图统一写清 seed/run、聚合单位与 band/error bar 的统计量。

## 四、Table 的制作范式

- 正文 Table 的行数中位数为 {number(table_rows['median'], 0)}，列数中位数 {number(table_columns['median'], 0)}，表头层级中位数 {number(table_headers['median'], 0)}，小数精度中位数 {number(table_precision['median'], 0)} 位。
- `booktabs` 占逐篇归一 Table 的 {pct(cond('kind', 'table', 'table_rules', 'booktabs')['conference_equal_paper_normalized_conditional_share'])}；partial grid 占 {pct(cond('kind', 'table', 'table_rules', 'partial_grid')['conference_equal_paper_normalized_conditional_share'])}。正文默认 `booktabs`，只用横线分隔表头与 row group。
- bold 出现在 {pct(cond('kind', 'table', 'highlighting', 'bold')['conference_equal_paper_normalized_conditional_share'])} 的 Table；best/second-best 组合占 {pct(cond('kind', 'table', 'highlighting', 'best_second_best')['conference_equal_paper_normalized_conditional_share'])}。最佳值用 bold，次佳值用 underline；指标方向在表头用 ↑/↓。
- 正文表体 8 pt、表头 8–8.5 pt，第一列左对齐，数值列按小数点对齐；正文保持 6–8 列、6–10 个主要行，完整 benchmark×model 矩阵移入附录。
- Table 的 point-only/undefined uncertainty 占 {pct(cond('kind', 'table', 'table_uncertainty_modes', 'point_only_or_undefined')['conference_equal_paper_normalized_conditional_share'])}。主结果表直接显示 `mean ± SD/SE`，caption 定义重复次数、聚合层级和 failure/OOM 记号。

## 五、caption 与表头

正文 Figure caption 的对象中位数为 {number(fig_caption['median'], 0)} 词，逐篇会议等权均值为 {number(fig_caption['conference_equal_paper_normalized_mean'], 1)} 词；正文 Table 分别为 {number(tab_caption['median'], 0)} 与 {number(tab_caption['conference_equal_paper_normalized_mean'], 1)} 词。附录 Figure/Table caption 中位数为 {number(app_fig_caption['median'], 0)}/{number(app_tab_caption['median'], 0)} 词。

caption 动作按以下顺序组织：

```text
粗体功能标题 → 实验设置/对象 → panel 与颜色/线型编码
→ 比较对象和方向 → 一个决定性发现 → uncertainty/分母 → appendix 指针
```

`title`、`setup`、`comparison`、`encoding_key`、`main_finding` 的论文覆盖率分别为 {pct(cat('caption_moves', 'title')['conference_equal_paper_prevalence'])}、{pct(cat('caption_moves', 'setup')['conference_equal_paper_prevalence'])}、{pct(cat('caption_moves', 'comparison')['conference_equal_paper_prevalence'])}、{pct(cat('caption_moves', 'encoding_key')['conference_equal_paper_prevalence'])}、{pct(cat('caption_moves', 'main_finding')['conference_equal_paper_prevalence'])}。正文 Figure 目标长度取 {integer_up(fig_caption['conference_equal_paper_normalized_mean'])} 词，正文 Table 取 {integer_up(tab_caption['conference_equal_paper_normalized_mean'])} 词；caption 能独立回答“画了什么、怎样比较、编码是什么、读出什么”。

Figure caption 中，粗体功能标题占 {pct(cond('kind', 'figure', 'caption_headline_bold', '1')['conference_equal_paper_normalized_conditional_share'])}，自包含 caption 占 {pct(cond('kind', 'figure', 'caption_self_contained', '1')['conference_equal_paper_normalized_conditional_share'])}，直接写出主发现占 {pct(cond('kind', 'figure', 'caption_main_finding', '1')['conference_equal_paper_normalized_conditional_share'])}。Table caption 的三项比例分别为 {pct(cond('kind', 'table', 'caption_headline_bold', '1')['conference_equal_paper_normalized_conditional_share'])}、{pct(cond('kind', 'table', 'caption_self_contained', '1')['conference_equal_paper_normalized_conditional_share'])} 和 {pct(cond('kind', 'table', 'caption_main_finding', '1')['conference_equal_paper_normalized_conditional_share'])}。推荐配置统一使用粗体功能标题和自包含设置；主发现只写一个决定性读数。

Figure caption 的高频功能短语为 `overview of`（{int(phrase('figure', 'overview of', 2)['papers_present'])} 篇）、`comparison of`（{int(phrase('figure', 'comparison of', 2)['papers_present'])} 篇）、`illustration of`（{int(phrase('figure', 'illustration of', 2)['papers_present'])} 篇）和 `as a function of`（{int(phrase('figure', 'as a function of', 4)['papers_present'])} 篇）。Table caption 高频使用 `comparison of`（{int(phrase('table', 'comparison of', 2)['papers_present'])} 篇）、`the best`（{int(phrase('table', 'the best', 2)['papers_present'])} 篇）、`ablation study`（{int(phrase('table', 'ablation study', 2)['papers_present'])} 篇）、`we report`（{int(phrase('table', 'we report', 2)['papers_present'])} 篇）和 `higher is better`（{int(phrase('table', 'higher is better', 3)['papers_present'])} 篇）。这些短语承担对象命名、比较、干预和指标方向，具体名词与数字必须紧随其后。

## 六、图表与论证闭环

逐篇审计的高价值模式中，机制—消融证据链覆盖 {pct(theme('reusable', 'mechanism_ablation_chain')['conference_equal_paper_prevalence'])}，趋势图与精确数值表配对覆盖 {pct(theme('reusable', 'trend_plus_exact_table')['conference_equal_paper_prevalence'])}，同构多面板对照覆盖 {pct(theme('reusable', 'matched_multi_panel')['conference_equal_paper_prevalence'])}。

对象级 `evidence_relation` 显示，Figure/Table 与方法组件或流程形成显式连接的论文覆盖率为 {pct(evidence('method_component_or_pipeline')['conference_equal_paper_prevalence'])}，与主结果或比较连接为 {pct(evidence('main_result_or_comparison')['conference_equal_paper_prevalence'])}，与消融或机制检验连接为 {pct(evidence('ablation_or_mechanism_test')['conference_equal_paper_prevalence'])}，与公式、定理或证明连接为 {pct(evidence('equation_theorem_or_proof')['conference_equal_paper_prevalence'])}，形成正文—附录交接为 {pct(evidence('main_appendix_handoff')['conference_equal_paper_prevalence'])}。完整对象级比例见 [`visual_evidence_relation_summary.csv`](tables/visual_evidence_relation_summary.csv)。

![图表与非视觉证据的连接](figures/visual_audit_evidence_relations.svg)

稳定闭环为：

```text
Figure 1 定义对象、组件与信息流
→ 公式/算法给出变换
→ 实验协议表固定数据、基线、指标、预算和分母
→ 主结果表给精确 operating point
→ 趋势图给尺度、预算或分布变化
→ 机制诊断与组件消融解释差异来源
→ 成本/失败图给可执行边界
→ 附录用全量表、逐任务曲线和样本卡完成复核
```

视觉对象承担 theory/mechanism 用途的论文覆盖率为 {pct(cat('purpose', 'theory_mechanism')['conference_equal_paper_prevalence'])}，直接落在 `theory` 模块的视觉对象覆盖率为 {pct(cat('module', 'theory')['conference_equal_paper_prevalence'])}。通用做法是让图解释定理对象、几何关系、状态转移或可检验预测，让正文保留 theorem/assumption/consequence，让附录保留完整 proof。Figure caption 直接回指 Equation/Theorem，实验图再用相同变量名验证预测；证明完成逻辑闭合，图把证明结论接入可观测证据。

[`icml-2026-2801956159d6`](../visual_audits/icml-2026-2801956159d6.md) 展示“方法示意→算法/公式→主结果→消融→效率”的完整链；[`iclr-2026-df25bb895158`](../visual_audits/iclr-2026-df25bb895158.md) 将质量—延迟 scatter、精确表、attention/cache 机制图、局部性诊断与调度图连接起来；[`icml-2026-f746984a28d8`](../visual_audits/icml-2026-f746984a28d8.md) 用方法接口、匹配质性网格、五次运行表和带误差的敏感性图完成同一语法。

## 七、视觉源码与制作工具

250 篇中，{status_counts.get('exact_visual_source', 0)} 篇取得 exact visual source，{status_counts.get('partial_visual_source', 0)} 篇取得 partial visual source，{status_counts.get('repository_without_visual_source', 0)} 篇定位到论文仓库，{status_counts.get('no_public_source_found', 0)} 篇未定位公开源。exact/partial 合计 {source_papers} 篇。源文件获取器从逐篇人工核验的 GitHub、arXiv source package 和作者项目页取得 {len(acquired_rows):,} 个文件，覆盖 {acquired_source_papers} 篇；源码字面量统计覆盖 {source_style_denominator} 篇已取得且包含可解析样式文件的论文。逐文件结果见 [`visual_source_files_local.csv`](tables/visual_source_files_local.csv)，样式汇总见 [`visual_source_style_summary.csv`](tables/visual_source_style_summary.csv)。

源码中最高频工具为 {source_top('tools', 5)}；最高频字号字面量为 {source_top('font_sizes_pt', 6)}；线宽字面量为 {source_top('line_widths_pt', 5)}；导出格式为 {source_top('export_formats', 4)}。这些源码值用于核对人工 PDF 观察，最终模板采用对象级中位数 8 pt 与 1 pt，而非脚本中为海报、notebook 或独立大图设置的放大字号。

制作流程固定为：绘图脚本读取结果表 → 输出 PDF/SVG → 在 ICLR 的 2.63 in/5.50 in 最终尺寸下检查 → LaTeX caption 定义统计语义 → 同一脚本生成附录扩展图。仓库模板位于 [`templates/visuals/`](../templates/visuals/)。

## 八、高频反模式

审计者逐篇总结的 failure patterns 中，分母/聚合/协议缺口覆盖 {pct(theme('failure', 'missing_denominator_or_protocol')['conference_equal_paper_prevalence'])}，缺少不确定性覆盖 {pct(theme('failure', 'missing_uncertainty')['conference_equal_paper_prevalence'])}，小字或高密度拥挤覆盖 {pct(theme('failure', 'small_text_or_dense_layout')['conference_equal_paper_prevalence'])}，颜色单通道或灰度失效覆盖 {pct(theme('failure', 'color_only_or_grayscale_unsafe')['conference_equal_paper_prevalence'])}，栅格/视觉源码缺口覆盖 {pct(theme('failure', 'raster_or_source_gap')['conference_equal_paper_prevalence'])}。

![可复用系统与高频反模式](figures/visual_audit_reusable_and_failure_patterns.svg)

直接删除以下做法：

1. 只给 point estimate、best bold 或单次 qualitative sample；
2. 颜色承担唯一系列编码，图例与线条在缩放后失去区分；
3. caption 只复述标题，把数据集、metric、预算、聚合和 panel 语义留在正文；
4. 用 5 pt 以下文字塞入高密度 facet、prompt 或 architecture；
5. Table 混用精度、单位、重复协议和 imported result，却没有视觉分组；
6. 主图只展示成功案例，OOM、失败数、截断阈值和停止条件不可见；
7. Figure 颜色、方法顺序、marker、缩写在不同章节改变含义。

## 九、可复算数据

- [`visual_audit_paper_summary.csv`](tables/visual_audit_paper_summary.csv)：逐篇对象数量与源码状态；
- [`visual_design_categorical_summary.csv`](tables/visual_design_categorical_summary.csv)：论文覆盖率与论文归一占比；
- [`visual_design_conditionals.csv`](tables/visual_design_conditionals.csv)：Figure/Table 内部条件比例；
- [`visual_design_numeric_summary.csv`](tables/visual_design_numeric_summary.csv)：字号、面板、系列、复杂度、行列与精度；
- [`visual_caption_language_summary.csv`](tables/visual_caption_language_summary.csv)：caption 动作与高频语言；
- [`visual_palette_summary.csv`](tables/visual_palette_summary.csv)：HEX 与色相族；
- [`visual_judgment_theme_summary.csv`](tables/visual_judgment_theme_summary.csv)：可复用模式与反模式；
- [`visual_evidence_relation_summary.csv`](tables/visual_evidence_relation_summary.csv)：图表与公式、算法、方法、实验、结果、消融和附录证据的连接；
- [`visual_cross_object_system.csv`](tables/visual_cross_object_system.csv)：逐篇视觉叙事、caption、表头、方法/结果/消融关系、正文与附录关系、字体和颜色系统；
- [`visual_source_style_summary.csv`](tables/visual_source_style_summary.csv)：公开源码中的工具和样式字面量。
- [`visual_source_files_local.csv`](tables/visual_source_files_local.csv)：逐个视觉源码、TeX、SVG、数据与渲染资产的获取结果。
- [`iclr_pdf_layout_measurements.csv`](tables/iclr_pdf_layout_measurements.csv)：ICLR 正文与单栏物理宽度。
"""

    main_figures = integer_up(pmetric("main_figures")["conference_equal_mean"])
    main_tables = integer_up(pmetric("main_tables")["conference_equal_mean"])
    appendix_figures = integer_up(pmetric("appendix_figures")["conference_equal_mean"])
    appendix_tables = integer_up(pmetric("appendix_tables")["conference_equal_mean"])
    if main_figures >= 6:
        closing_figure_rows = """| 7–8 | Figure 5 | 2.63 in 单栏或双 panel 全栏 | 跨数据、规模、任务或扰动的鲁棒性与异质性；保持主结果的坐标和编码 |
| 8 | Figure 6 | 5.50 in 全栏 | 效率—效果、失败面或匹配质性样本；直接标出 operating point 与失败 |"""
        closing_figure_sections = """### Figure 5：鲁棒性与异质性

沿用 Figure 3 的坐标、方法顺序和统计单位，改变一个外部条件：数据域、模型规模、任务组或扰动强度。主结论保持可见，反向切片直接标注。

### Figure 6：成本、失败与质性证据

数值工作使用质量—成本 Pareto、latency/memory scaling 或 failure rate；生成式工作使用固定 prompt/target × method grid，并保留 reference/ground truth、随机种子、样本数量和失败样本。"""
    else:
        closing_figure_rows = "| 8 | Figure 5 | 5.50 in 全栏 | 鲁棒性、效率—效果、失败面或匹配质性样本；直接标出 operating point 与失败 |"
        closing_figure_sections = """### Figure 5：鲁棒性、成本、失败与质性证据

数值工作使用跨设置趋势、质量—成本 Pareto、latency/memory scaling 或 failure rate；生成式工作使用固定 prompt/target × method grid，并保留 reference/ground truth、随机种子、样本数量和失败样本。"""
    appendix_figure_roles = [
        "完整数据集/任务趋势，与正文 Figure 3 同坐标和配色",
        "超参、规模或阈值敏感性",
        "run/seed 分布、失败率、长尾或 per-unit 异质性",
        "完整质性网格，包含成功、失败、reference 与选择协议",
        "扩展机制诊断、额外 architecture 或复现流程",
        "鲁棒性分解、校准、分布偏移或反向任务切片",
    ]
    appendix_table_roles = [
        "逐任务/逐数据集主结果",
        "完整消融与替代组件",
        "超参、软件、硬件、预算和训练/推理设置",
        "成本、失败、OOM、样本数与 run-level 汇总",
        "完整 seed/run 数值、不确定性和统计检验",
        "逐模型×数据集×指标的全矩阵与 imported result 来源",
    ]
    appendix_items = [
        f"{index}. Figure A{index}：{appendix_figure_roles[index - 1] if index <= len(appendix_figure_roles) else '正文 Figure 的同构扩展'}；"
        for index in range(1, appendix_figures + 1)
    ]
    appendix_items.extend(
        f"{appendix_figures + index}. Table A{index}：{appendix_table_roles[index - 1] if index <= len(appendix_table_roles) else '正文 Table 的逐单位完整数值'}；"
        for index in range(1, appendix_tables + 1)
    )
    appendix_items_text = "\n".join(appendix_items)
    handbook = f"""# ICLR 9 页论文图表执行手册

本手册把 250 篇论文的视觉统计压缩为一套直接执行的 ICLR 配置。正文固定 **{main_figures} 幅 Figure + {main_tables} 张 Table**，附录固定 **{appendix_figures} 幅 Figure + {appendix_tables} 张 Table**。对象可以复合职责，图表总数保持稳定。

## 一、9 页正文配置

| 页码 | 对象 | 版式 | 必须表达的内容 |
|---:|---|---|---|
| 1 | Figure 1 | 5.50 in 全栏，1–2 panel | 工作对象、现有缺口、方法主接口、headline 结果；同一视觉语言贯穿全文 |
| 2–3 | Figure 2 | 5.50 in 全栏，2–3 panel | 输入→组件→状态/表示→输出；每个组件写名称、变量和箭头语义 |
| 3–4 | Table 1 | 2.63 in 单栏或 5.50 in 全栏 | 数据、任务、模型、基线、指标方向、预算、seed/run、分母与硬件 |
| 5 | Table 2 | 5.50 in 全栏 | 主比较精确数值；按 benchmark/模型 row group；性能、成本和失败值同表 |
| 5–6 | Figure 3 | 2.63 in 单栏或双 panel 全栏 | budget/scale/time/data 的折线趋势；4 个系列；明确 band/error bar |
| 6–7 | Figure 4 | 5.50 in 全栏，2–4 panel | 机制诊断→组件消融→替代解释控制；panel 顺序对应贡献顺序 |
| 7 | Table 3 | 2.63 in 单栏 | 组件删除、替代组件、超参和交互消融；同一指标与主表对应 |
{closing_figure_rows}
| 8 | Table 4 | 2.63 in 单栏 | latency、memory、token/query、训练成本、OOM/failure count |
| 9 | 结论回指 | 无新增视觉对象 | 按 Figure/Table 标签回收对象、机制、结果、成本和失败面 |

这一顺序覆盖超过 60% 论文出现的 conceptual diagram、line chart、pipeline、主比较、headline、鲁棒性、方法接口、理论/机制、消融、实验设计、质性证据、复现和效率成本。

## 二、每个 Figure 的精确规格

| 属性 | 配置 |
|---|---|
| 单栏宽度 | 2.63 in |
| 全栏宽度 | 5.50 in |
| 正文面板 | 中位 {number(main_panels['median'], 0)}；主结果最多 4 |
| 附录面板 | 中位 {number(app_panels['median'], 0)}；同一 facet 语法扩展 |
| 常规字号 | 8 pt |
| tick/legend | 7.5 pt |
| panel 标题 | 8.5 pt bold |
| 绝对最小字号 | 6 pt |
| 数据线 | 1.0 pt |
| 轴线 | 0.6–0.8 pt |
| marker | 3.5 pt；`o/s/^/D/v` |
| 系列数 | 4 个主系列；超过 5 个拆 panel 或移附录 |
| 主色 | `#1F77B4 #FF7F0E #2CA02C #D62728 #9467BD` |
| 冗余编码 | 每个系列同时绑定颜色、marker、线型；关键点直接标注 |
| 网格 | 折线图使用 0.45 pt 浅灰双轴网格；示意图不加网格 |
| 输出 | PDF/SVG；含真实图像的 panel 单独以 300 dpi 栅格嵌入 |

### Figure 1：工作对象与 headline

左侧画输入和任务约束，中间画现有方法断点，右侧画本文接口与一个 headline operating point。Figure 1 同时完成问题定义、方法预告和结果预告；不使用装饰性大图。

### Figure 2：方法接口

每条箭头写明传递对象，每个组件下方放一个变量或公式锚点；组件名称与方法小节、算法、消融 row 完全一致。颜色表达组件角色，箭头/边框/位置同时编码。

### Figure 3：主趋势

x 轴只承载一个干预量：预算、规模、时间、数据量或阈值。y 轴是主决策量。主方法和关键基线共 3–4 条曲线；band/error bar 在 caption 中定义为 SD、SE 或分布统计；对数轴在轴标签和 caption 同时声明。

### Figure 4：机制与消融

panel a 展示诊断量，panel b 展示组件干预，panel c 展示替代解释控制，panel d 展示跨任务一致性。所有 panel 使用同一方法顺序、颜色、marker、范围和聚合。

{closing_figure_sections}

## 三、每张 Table 的精确规格

| 属性 | 配置 |
|---|---|
| 表体 | 8 pt，行距 9 pt，`arraystretch=1.08` |
| 正文行列 | {number(table_rows['median'], 0)} 行 × {number(table_columns['median'], 0)} 列为中心；控制在 6–10 行、6–8 列 |
| 表头 | {integer_up(table_headers['conference_equal_paper_normalized_mean'])} 层；第一层写 benchmark/setting，第二层写 metric 与 ↑/↓ |
| 精度 | {integer_up(table_precision['conference_equal_paper_normalized_mean'])} 位小数；同一 metric 全表一致 |
| 线条 | `booktabs`；`toprule/midrule/bottomrule`，不用完整网格 |
| 对齐 | 方法列左对齐；数值列按小数点对齐 |
| 高亮 | best bold、second underline；failure/OOM 用固定符号并在 caption 定义 |
| 统计 | `mean ± SD/SE`；表注写 seed/run、聚合层级、分母和 imported result 来源 |

Table 1 固定实验协议，不使用 best/second-best 排名高亮；Table 2 给主结果，Table 3 给组件消融，Table 4 给成本与失败，并只在可比较数值中使用 bold/underline。宽表通过 row group 和两层表头压缩；不使用 `\\resizebox` 把正文压到 6 pt 以下。

## 四、caption 的精确写法

正文 Figure caption 写 {integer_up(fig_caption['conference_equal_paper_normalized_mean'])} 词，正文 Table caption 写 {integer_up(tab_caption['conference_equal_paper_normalized_mean'])} 词。统一采用六步结构：

```text
1. 粗体功能标题
2. 对象、数据集、预算或干预
3. panel、颜色、线型、marker、箭头和符号的编码
4. 比较对象与指标方向
5. 一个决定性读数
6. seed/run、聚合、band/error bar、failure 记号和附录指针
```

Figure caption 例式：

```text
Method scaling and operating point. Test success versus inference budget on
three benchmarks. Color identifies the method; marker and line style repeat
the same encoding. Lines are means over five seeds and bands show ±1 SD.
Our method remains above both baselines across the full budget range and
reaches the selected operating point at B=8. Per-task values appear in Table 6.
```

Table caption 例式：

```text
Main comparison. Test performance and cost across three settings; ↑/↓ marks
the preferred direction. Values are mean ± SD over five seeds. Bold and
underline indicate the best and second-best result within each column; × marks
budget failure. Full per-task results and run-level values are in Appendix C.
```

## 五、附录配置

附录固定 {appendix_figures} 幅 Figure 与 {appendix_tables} 张 Table：

{appendix_items_text}

正文每个主张在首次出现处调用对应附录对象；附录沿用正文的方法顺序、颜色、marker、缩写、指标单位和精度。

## 六、交付流程

1. 先定义 claim→visual map，再运行实验；每个贡献绑定一个 Figure/Table 和一个附录扩展。
2. 结果统一落到 tidy CSV/JSON；绘图脚本只读结果表，不手填最终数值。
3. 使用 [`templates/visuals/iclr_style.py`](../templates/visuals/iclr_style.py) 生成 2.63 in/5.50 in PDF/SVG。
4. 使用 [`table_style.tex`](../templates/visuals/table_style.tex) 与 [`method_figure.tex`](../templates/visuals/method_figure.tex) 建表和方法图。
5. 在最终 ICLR 页面 100% 缩放检查字体、legend、线型、颜色、caption 与跨页位置。
6. 逐对象核对数据分母、方向、seed/run、聚合、单位、failure/OOM 和正文引用。
7. 运行 `make visual-templates` 复现示例，使用 [`main_result.pdf`](../templates/visuals/examples/main_result.pdf) 对照最终输出密度。

## 七、写作与视觉语言

- 图表直接陈述对象、干预、读数和解释；删除防御性铺垫、自我设限和 claim-boundary 话术。
- 不在 caption 里重复“我们的方法有效”；写清比较量、方向、数值、范围和机制读数。
- 不用“for completeness”引出附录；正文先给决策接口，再直接指向完整数值、分布、失败和复现设置。
- 不把不利结果藏在语言里；用 failure panel、失败计数、OOM 符号、长尾分布和停止条件形成可见证据。
- 同一对象在方法图、公式、主结果、消融、结论和附录保持同名、同色、同顺序。
"""

    REPORT.write_text(report, encoding="utf-8")
    HANDBOOK.write_text(handbook, encoding="utf-8")
    print(
        json.dumps(
            {
                "papers": len(papers),
                "figures": figures,
                "tables": tables,
                "report": str(REPORT.relative_to(ROOT)),
                "handbook": str(HANDBOOK.relative_to(ROOT)),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

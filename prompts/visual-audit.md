# 单篇论文图表深度审计协议

每个视觉审计单元处理且仅处理一篇论文。完整检查正文和附录中的每一幅 Figure 与每一张 Table，并在完成该论文后停止。

## 输入

- `paper_id`
- `data/processed/analysis_sample.csv`
- `readings/<paper_id>.json`
- `readings/<paper_id>.md`
- reading 中记录的本地 PDF
- `schemas/visual-audit.schema.json`

## 输出

1. `visual_audits/<paper_id>.md`
2. `visual_audits/<paper_id>.json`

先写 Markdown，完成视觉复核后原子写入 schema-valid JSON。不得修改其他文件。

## 1. 建立完整对象清单

从 reading 的 `visual_inventory` 开始，逐页核对 PDF。记录正文与附录的每个 Figure 和 Table，包括跨页表、复合图、qualitative grid、截图、示意图和 inset。对象数量、标签、页码或模块发生差异时，以 PDF 为准并在 Markdown 中说明。

## 2. 渲染与视觉检查

将含图表的 PDF 页按至少 180 dpi 渲染。逐个对象检查：

- 单栏、双栏、页宽或 inset；
- 面板数、排列、阅读方向和留白；
- 图型、坐标、facet、legend、marker、线型、网格和标注；
- 矢量/栅格/混合渲染，x/y 轴的 linear、log、categorical、time 或无轴类型；
- legend 的位置与共享方式、direct label、hatch、reference line、line width，以及 error bar、band、ellipse、box 或 distribution 等不确定性编码；
- 表格行列数、表头层级、行分组、横线/竖线、精度和高亮；
- 字体家族、估计字号、字重、斜体、等宽体和数学字体；
- 颜色数量、近似 HEX、调色板类型、语义映射、冗余编码和灰度可读性；
- 数据单位、比较对象、聚合、分母、重复、不确定性和失败值；
- caption 的标题、设置、编码说明、比较、主结论、不确定性定义和附录指针。

视觉估计写 `rendered_estimate`。PDF 字体对象写 `pdf_object`。源文件中的 rcParams、HEX、字号、线宽或 LaTeX 命令写 `source_exact`。

## 3. 图的分类

为每幅图选择一个或多个类型：

```text
line · bar · scatter · heatmap · box · violin · area · histogram
matrix · network · tree · pipeline · architecture · conceptual_diagram
qualitative_grid · image_montage · screenshot · map · pareto · other
```

复杂度按 1–5 编码：

- 1：单面板、1–2 系列、无图例或少量标签；
- 2：单面板、3–5 系列或轻量 annotation；
- 3：2–4 面板、5–8 系列或中等 legend；
- 4：5–8 面板、多编码、多层 annotation；
- 5：超过 8 面板、密集网络/矩阵/qualitative grid 或高信息密度复合图。

每幅图把上述绘图语法写入 JSON 的 `plot_grammar`。从公开绘图源读取的数值标记为 `source_exact`；从 PDF 渲染估计的数值标记为 `rendered_estimate`；两者结合时标记为 `mixed`。

## 4. 表的分类

记录：

- 行数、列数、表头层级和 row group；
- `booktabs`、完整网格、部分网格、极简线或无线；
- bold、underline、italic、arrow、cell color、text color、best/second-best；
- 小数位数和列间精度一致性；
- `mean ± SD/SE`、区间、rank、win rate、count、cost 或 failure；
- 主表是否把性能、成本和失败放在同一决策面。

## 5. 证据关系

每个对象说明它连接的对象：

```text
引言主张 → 方法组件 → 公式/理论 → 实验问题
→ Figure/Table → 消融 → 结论 → 附录扩展
```

判断图表承担 headline、方法接口、主比较、机制、鲁棒性、成本、失败、消融、qualitative evidence 或复现中的哪一项职责。指出正文对象与附录完整表、追加切片或证明之间的调用。

JSON 的 `purpose` 使用以下固定值，可多选：

```text
headline · method_interface · theory_mechanism · experimental_design
main_comparison · mechanism · robustness · efficiency_cost · failure
ablation · qualitative_evidence · reproduction · dataset · other
```

## 6. Caption 与表头

逐字提取 caption，统计词数并编码其动作。重点判断：

- 开头是否为粗体结论标题；
- 是否说明实验设置和比较对象；
- 是否定义颜色、线型、阴影、error bar、缩写和箭头；
- 是否在 caption 中直接写出主发现；
- 脱离正文后是否仍可理解。

表头检查指标名称、方向、单位、模型/任务分组、训练/推理条件和成本列。

## 7. 源码获取

按以下顺序搜索：

1. PDF 首页、脚注、正文和参考文献中的 code/project URL；
2. OpenReview/论文页面中的 code、project、supplementary 和 repository；
3. `reports/tables/visual_source_inventory.csv` 的自动候选与 `corpus/visual_sources/<paper_id>/` 已取得的紧凑源文件；
4. 以完整标题和方法名搜索 GitHub；
5. 使用 GitHub API 查看候选仓库树。

自动候选只用于缩短检索路径。作者链接、仓库元数据、README 标题或论文 ID 必须与论文建立直接关系后，才能把其中的视觉文件记为本文源代码。

记录：

- 论文明确链接的候选仓库；
- 最可信仓库；
- `plot*`、`figure*`、`visual*`、`table*`、`.ipynb`、`.tex`、`.tikz`、`.pgf`、`.svg`、style 文件和数据文件路径；
- matplotlib/seaborn/plotly/TikZ/PGF/Graphviz/Illustrator 等工具；
- 可从源码精确读取的字体、字号、字重、颜色、marker、线宽、尺寸和导出格式。

读取仓库树和紧凑源文件，不克隆模型权重、数据集、checkpoint 或完整训练仓库。仓库存在而没有视觉源文件时记录 `repository_without_visual_source`。

## 8. 完成条件

- Figure 和 Table 数量与 PDF 对齐；
- 每个对象均有页码、标签、类型、视觉属性、caption/header、数据表达、证据关系和评价；
- 源码状态与搜索路径明确；
- JSON 通过 `schemas/visual-audit.schema.json`；
- Markdown 给出最可复用模式、最高价值对象和失败模式；
- 完成该论文后停止。

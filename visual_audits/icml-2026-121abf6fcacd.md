# `icml-2026-121abf6fcacd` 视觉审计

## 审计边界与证据

- **论文**：*How Many Different Outputs Can a Transformer Generate?*，Maxime Meyer、Mario Michelessa、Caroline Chaux、Vincent Y. F. Tan。
- **PDF 事实源**：`corpus/preprints/icml-2026-121abf6fcacd.pdf`，arXiv `2605.22223v2 [cs.LG] 8 Aug 2026`。PDF 为 30 个物理页、Letter、612×792 pt，`pdfinfo` 报告 `Tagged: no`、未加密。正文、参考文献和 Appendix A–H 均在该 PDF 内，没有单独 supplementary 文件。
- **完整读取**：用 `pdftotext` 按页读取 p.1–30，覆盖正文 §§1–7、Impact Statement、References、Appendix A–H；再用 PDF 布局文本核对 caption、表头和章节位置。正文主叙事为 p.1–9，Appendix 从 p.14 开始，参考文献位于 p.10–13。
- **渲染与放大复核**：30 页全部以 200 dpi 渲染为 1700×2200 px；逐页查看 contact sheets，并对含对象的 p.4、7–9、15、22–23、26–30 逐页放大。200 dpi 高于协议要求的 180 dpi。`pdfimages -list` 显示 p.4 的 Figure 1 为 684×684 带 mask 的栅格 XObject，p.22 的 Figure 6 为 213×84 RGB 带 mask 的栅格 XObject；其余图表主要由 PDF 矢量路径和文字组成。
- **PDF 对象清单**：PDF 实际有 Figure 1–11 共 11 幅、Table 1–3 共 3 张；没有未编号 Figure/Table，也没有跨页表。reading 的 `visual_inventory` 与逐页 PDF 清单一致。附录图中 Figure 7、8、11 是多面板复合图，分别按一个 PDF 对象记录，并在面板数中展开。
- **字体事实**：`pdffonts`/`pdftohtml -xml` 显示正文和 caption 以 Nimbus Roman No9 L（regular/medium/italic）与 Computer Modern 数学字体为主；图中还嵌入 MyriadPro、SegoeUIVariable、ArialMT、DejaVuSans/Oblique。图内字号来自 PDF font objects 或 200 dpi 渲染估计；没有把正文 caption 字体误记成图内字体。

## 公开视觉源检索

首先核查 `reports/tables/visual_source_inventory.csv`：该行是 `icml-2026-121abf6fcacd,...,no_public_source_found`；`corpus/visual_sources/icml-2026-121abf6fcacd/` 不存在，因而没有已取得的本地紧凑源文件。PDF 首页脚注给出 `github.com/mario-michelessa/transformers_accessibility`，README 的完整标题为本文的 replication code，且明确列出 Voronoi、cramming、embedding geometry、copying 和 cell-volume/convolution 命令，故该仓库与论文建立了直接关系。

随后仅用只读 `gh repo view mario-michelessa/transformers_accessibility` 和 `gh api repos/mario-michelessa/transformers_accessibility/git/trees/HEAD?recursive=1` 核对仓库元数据与树。`HEAD` 的默认分支是 `master`；树中实际存在 `voronoi_visualizer/qwen_token_plane_visualization.svg`、`cramming/plots_accessibility.ipynb`、`th_bounds_estimation.ipynb`、`cell_volume_tests.ipynb` 以及 `cramming/figures/*_both.pdf`。读取的绘图源明确复现 Figure 1 的 PCA-plane 设置、Figure 2/7/8 的 accessibility 语法、Figure 9 的 Ball/Cone/Ellipsoid 小 multiples、Figure 10 的颜色与 log-log scatter、Figure 11 的卷积直方图样式。仓库没有论文 TeX、Table 1–3 的表格生成器或 Figure 7/8 的最终 composite wrapper；当前 `copying/parent_copy_artifacts.py` 的 `plot_model` 还是单模型、带 accuracy band 的另一种通用图，不能冒充论文 Figure 4 的精确源。因此整体状态为 **`partial_visual_source`**：部分图的源参数可精确读取，其余属性以 PDF 对象/渲染观察为准；没有将自动候选或不匹配的脚本标为 exact。

## PDF 对象清单（最终）

|对象|物理页|模块|版面|PDF 中的实际内容|
|---|---:|---|---|---|
|Figure 1|4|method|正文双栏页宽|PCA plane cut 的 decoder argmax regions 与三个 prompt embedding。|
|Figure 2|7|results|正文双栏页宽|PG19/random 的三面板 accessibility 与 `n50(m)`。|
|Table 1|8|results|正文双栏页宽|五种 enclosure/precision strategy × 七个模型的理论/经验 slope ratio。|
|Figure 3|8|results|正文右栏单栏|`D^1`–`D^4` 的 cell-volume convolution 概念分布。|
|Figure 4|9|results|正文左栏单栏|七个模型的 exact-copying accuracy sigmoid transition。|
|Figure 5|15|Appendix A|附录页宽多面板|七个模型的 maximal radius `R` 随最大 sampled input length。|
|Figure 6|22|Appendix F.2|附录双栏页宽|cone 的 `E_δ`/`F_δ` 几何分解示意。|
|Table 2|23|Appendix G.1|附录双栏页宽|七个模型的 `d`、`|V|`、`r`、`θ` 常数。|
|Table 3|26|Appendix H|附录页宽|七个模型各五个最大 decoder-cell token 及 volume proportion。|
|Figure 7|27|Appendix G.3|附录页宽九面板|Pythia-160M/410M/1B 的 Figure 2 式结果。|
|Figure 8|28|Appendix G.3|附录页宽九面板|Qwen-2.5、Gemma-3、Llama-3.2 的 Figure 2 式结果。|
|Figure 9|29|Appendix G.4|附录页宽七面板|三种 support geometry 的 slope upper bound 随 sampled length 收敛。|
|Figure 10|29|Appendix H|附录单栏居中|七模型 decoder-cell volume 的 ranked log-log profile。|
|Figure 11|30|Appendix H|附录页宽七面板|七模型的 `n`-fold volume-proportion convolution distributions。|

## 全文视觉系统

论文把一条理论—实验链映射到视觉对象：§3 的 embedding-space partition 由 Figure 1 给出几何直觉；Theorem 4.6、Corollary 4.7 的固定 prompt-length threshold 由 Figure 2 的 accessibility 和 `n50(m)` 检验；Table 1 把 support enclosure 与 non-uniform-cell refinement 接到 slope upper bound；Figure 3 说明 cell-volume distribution 如何收紧 bound；Figure 4 将 fixed-transformer accessibility limit 转译为 copying failure。Appendix Figure 5 检查 bounded support 的半径，Figure 6 展开 cone proof，Table 2 提供 Table 1 的 model constants，Table 3 与 Figures 10–11 展开 cell-volume 估计，Figures 7–9 提供跨模型、跨架构和 sampling-length 的附加证据。

正文表格和 caption 采用黑白规则、Nimbus Roman/Computer Modern；图内 plotting text 多为无衬线（MyriadPro、Segoe UI、DejaVu Sans）并使用蓝、红、橙、绿、紫的语义或模型族配色。图表间没有统一的全局 legend 组件：Figure 2、7、8 的 accessibility legend 重复出现，Figure 9/11 使用首个面板承担共享 key，Figure 10 使用单 legend。颜色通常配合面板位置、线型或文字标签，但模型曲线和 token-cell heatmap 仍主要依赖色相，灰度复核能力有限。

## Figure 1 — Plane cut of embedding space（p.4）

- **类型与职责**：`heatmap` + `conceptual_diagram`；`method_interface`、`theory_mechanism`、`qualitative_evidence`。图把 §3.1 的 decoder partition `E_t` 变成可见的二维切面：背景颜色表示每个位置的 argmax next token，三个红色 marker 对应文本 `The quick brown fox`、`https://`、`In a distant future` 的最终 token embedding，并落在 `<jumps>`、`<www>`、`<,>` 区域。
- **几何与布局**：单面板近正方形 PCA plane，横轴 `Component 1`、纵轴 `Component 2`，刻度约为 −200、−100、0、100；背景是邻接的彩色 token regions，区域内以白色圆角标签直接标注 `<es>`、`<www>`、`<leetcode>`、`<_world>`、`<world>`、`<jumps>`、`<,>` 等较大 cell。三个白边红心圆 marker 旁边有白底文本框。图无独立 legend，版面占正文双栏宽度。
- **绘图语法**：PDF 中 plane 是栅格 XObject，caption/版面文字是矢量；`x/y=linear`，无可见网格、无不确定性、无 reference line；`marker_types=1`（红白圆）、`line_styles=0`、`direct_labels=true`、`hatching=false`。源脚本精确给出 200×200 grid、`resolution=200`、`max_colors=50`、`figsize=(15,8)`、红 marker `s=200`、`linewidths=3`、白 edge、annotation `fontsize=10`；论文成品是裁剪后的 plane asset，因此 source 与 PDF 的边界/标签有组合差异。
- **字体与颜色**：PDF 图内可见无衬线约 6–10 pt，白底区域标签与坐标 label 为 regular，数学/轴编号带 italic；使用 `DejaVu Sans/Oblique` 与 Computer Modern math（PDF object 与源设置共同佐证）。可见主色约为 `#1f77b4`、`#ff7f0e`、`#2ca02c`、`#d62728`、`#9467bd`、`#8c564b`、`#e377c2`、`#7f7f7f`、`#bcbd22`、`#17becf`，另有白色标签底和红色 marker；颜色编码 token identity/region，marker 的红色编码 prompt embedding。颜色有文字冗余，但仅色彩区分大量 region，灰度下 token identity 不可完全恢复。
- **Caption**：
  `Figure 1. Plane cut of the embedding space E of Qwen-2 (0.5B) (Yang et al., 2024), passing through the final token embeddings of “The quick brown fox”, “https://”, and “In a distant future” (red markers). Colors encode, for each pixel, the most probable next token via the model’s output projection (decoder readout). This induces regions E_t annotated by < t >. Only tokens whose regions have the largest areas are annotated for readability. The three embeddings fall respectively in E_jumps, E_www, and E_,, i.e. the predicted next tokens are <jumps>, <www>, and <,>.`
  （按空白分词 93 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 说明模型、三种输入、颜色语义和可读性裁剪，脱离正文仍能理解图的主编码。
- **数据与证据关系**：图不是统计估计，而是一个 PCA 视觉切片；每个像素的 token 是 decoder readout 的 argmax，marker 是三个具体 prompt 的 embedding。p.4 §3.1 的 `partition the embedding space` → Figure 1 → §3.2 的 prompt regions `E_t^m` → Theorem 4.6/Corollary 4.7 的可达性论证。图没有把二维面积当作高维概率或性能估计。
- **优点**：用一个切面同时显示 support、decoder cells 和 prompt 落点；直接标签避免 token legend 进一步拥挤；源脚本的红 marker 与颜色表能复现主要视觉参数。
- **缺陷**：二维 PCA 切面不能代表高维 cell 体积或全 support；区域边界受 200×200 采样、plane bounds 和 top-color 截断影响；白底 token 标签与相近色块在缩放/灰度下有识别成本；图中没有说明 PCA 的具体方差解释率。
- **可复用范式**：把抽象的 argmax partition 映射为「颜色区域 + 直接 token label + 具体 prompt marker」，并在 caption 明确该图是切面示意而不是高维统计结果。

## Figure 2 — Accessibility threshold and `n50(m)`（p.7）

- **类型与职责**：`line` + `scatter`；`headline`、`experimental_design`、`main_comparison`、`theory_mechanism`。这是主文对 Corollary 4.7 的核心实证对象，比较自然文本 PG19 与 i.i.d. random target，并把临界长度与 trainable memory vectors `m` 连接。
- **几何与布局**：Figure 2 是一个双栏宽三面板布局：a/b 左侧上下排列，分别为 PG19 和 Random 的 `Acc.` 对 `n (tokens)`；c 位于右侧，横轴为 `m (tokens)`，纵轴为 `n at Accessibility=50%`。a/b 各有五条 `m=1…5` 的 sigmoid solid curve、半透明 dotted raw points 和五条 vertical dashed `n50`；c 有 PG19 蓝圆点、Random 红 `x`、黑 dashed/灰 dotted linear fits。a/b 的 legend 在各自右上角，标题为 `m (tokens)`；c 的 fit legend 在左上角。
- **绘图语法**：PDF 为以矢量路径/文字为主的 mixed chart；x/y 均 `linear`，无 grid，`marker_types=3`（raw dot、blue circle、red x），`line_styles=3`（solid fit、dotted observations、dashed threshold/fit），`reference_lines=10`（a/b 各五条 vertical `n50`），`uncertainty_display=none`。源 notebook 精确给出 `figsize=(12,4)`、GridSpec 2×2、宽度比 `[1.8,1]`、`Blues`/`Reds` 在五个 `m` 值上的连续明度、sigmoid solid width 1、raw scatter `s=8, alpha=.35`、vertical dashed width 1，以及 c 面板的 circle/`x` 和 dashed/dotted linear fit。
- **字体与颜色**：图内字体约 6–11 pt，轴 label 与 panel label 为 MyriadPro/Segoe UI/DejaVu Sans，数学变量使用 Computer Modern；字号、线宽由 notebook 与 PDF object 共同验证。蓝色 `Blues` 明度序列编码 PG19 的 `m=1…5`，红色 `Reds` 序列编码 random 的 `m=1…5`，c 面板用蓝/红区分数据源、黑/灰区分 fit；近似主色包括 `#a9cfe5`、`#74add1`、`#4a98c9`、`#1e78b5`、`#084594` 与 `#fc9272`、`#fb6a4a`、`#ef3b2c`、`#cb181d`、`#99000d`。颜色与 panel/line/marker 有冗余，但纯灰度会弱化五档 `m` 的区分。
- **Caption**：
  `Figure 2. Mean accessibility for a) PG19 and b) random target sequences of length n as a function of the number of trainable memory vectors m. For each m, we fit a sigmoid (solid) and mark n50 where the fit crosses 0.5 (vertical dashed line). (c) n50(m) for PG19 (blue) and random (red), with linear fits (dashed).`
  （按空白分词 57 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 定义了两类 target、sigmoid、n50、颜色和 dashed encoding，但没有在 caption 写出 20-target 聚合或拟合质量。
- **数据与证据关系**：p.7 §5.1 固定模型为 Qwen2.5-1.5B；每个 `(n,m)` 的 accessibility 是 20 个 target strings 的 mean success rate，target 来源为 PG19 contiguous spans 或 vocabulary-uniform random strings，`m∈{1,…,5}`。a/b 的 sigmoid 只作阈值摘要，c 对五个 `n50` 做 linear fit；正文报告 PG19 slope `a=79.56`、random `a=36.38`，fit `R²` 分别为 0.999/0.995。Section 5.1 → Figure 2 → Table 1 第一行的 theoretical slope ratio；附录 Figures 7–8 扩展模型族。没有 error bars、seed-to-seed spread 或 target-level interval。
- **优点**：同一 figure 既保留曲线形状，又给出跨 `m` 的 threshold summary；PG19/random 的颜色和上下位置稳定；`n50` vertical dashed 与 c 的 linear fits 让理论 prediction 的可检验量明确。
- **缺陷**：五档 `m` 依赖颜色明度，灰度/色觉异常下读取成本高；raw dots 很密但没有点级不确定性解释；c 的线性拟合以两个域分别给出，未在图内显示样本数量或 slope units；把 sigmoid `R²` 放在正文旁边而不是 caption，使脱离正文的复核仍需阅读 p.7 文字。
- **可复用范式**：采用「上下条件曲线 + 右侧临界量 summary」的小 multiples，把理论阈值从原始 accessibility 轨迹中显式提取，同时保留原始点以检查 sigmoid 是否掩盖形状。

## Table 1 — Theoretical/empirical slope ratios（p.8）

- **版面与结构**：正文双栏页宽表；5 个 strategy 行、7 个 model 列。表头有两级：第一层为 Pythia、Qwen-2.5、Llama-3.2、Gemma-3 家族，第二层为 160M、410M、1B、0.5B、1.5B、1B、270M。横线为 top/header/bottom 的 `booktabs` 风格，无完整网格；数值正文约 9–10 pt Nimbus Roman/Computer Modern，标题/家族表头 medium。`ε` 等数学字符使用 Computer Modern。
- **Caption**：
  `Table 1. Ratio between the theoretical upper bound on the slope (using the infinity norm) and the empirical one for natural texts (PG19), across various models. Rows correspond to different enclosure strategies, and columns to the evaluated models. The detailed theoretical analysis is provided in Appendix F.`
  （按空白分词 47 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`appendix_pointer`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 说明 ratio 分子、PG19、行列语义和 Appendix F 指针，没有误差定义。
- **数据与统计**：单元格是 theoretical upper-bound slope / empirical natural-text slope 的 ratio，列出 Ball、Cone、Ellipsoid、Ellipsoid + Non-uniform Cells、Ellipsoid + variable `ε` 五种 enclosure/refinement。PDF 可见值为：Ball `9.24, 9.79, 7.77, 14.1, 20.4, 14.3, 11.52`；Cone `9.10, 9.60, 7.70, 14.01, 20.34, 13.98, 11.24`；Ellipsoid `7.92, 8.15, 6.12, 10.96, 15.30, 11.86, 11.12`；Non-uniform Cells 行加粗 `6.66, 5.99, 4.56, 7.92, 10.82, 10.71, 8.79`；variable `ε` 行 `8.65, 9.83, 7.71, 12.32, 18.81, 14.63, 13.42`。没有 mean±SD、区间、重复或失败值；小数位混用，最多两位。
- **证据关系**：Corollary 4.7 的 ball/equal-cell upper bound → §5.2 support refinement 和 §5.3 cell-volume refinement → Table 1；Appendix F 给出几何推导，Appendix G/H 给出 constants 与 volume 估计。表支持 `theory_mechanism`、`main_comparison` 和 `reproduction`，但它不是 component-removal ablation。
- **优点**：固定模型列和 strategy 行形成清晰的单一控制面；第四行粗体直接暴露 non-uniform cell refinement 收紧 ratio；黑白 booktabs 规则适合打印和数值复核。
- **缺陷**：列间 `14.1/14.01/14.3` 的精度不统一；ratio 没有给经验 slope、样本数量或估计误差，读者无法判断 refinement 的变异；摘要的「factor less than 10」与该表中若干全表值（如 20.4、15.30）需要结合行语义解释。
- **可复用范式**：把理论近似逐层放在行，把模型族稳定放在列；使用加粗标出 refinement 的方向，同时在 caption 明确分子、分母、数据来源和推导附录。

## Figure 3 — Cell-volume convolution concept（p.8）

- **类型与职责**：`histogram`；`theory_mechanism`、`method_interface`。单栏概念图把 §5.3 的 empirical one-step cell-volume distribution `D^1` 与乘法 n-fold convolution `D^n` 之间的机制画出来，不承担模型间数值比较。
- **几何与布局**：单面板，x 轴为 `Proportion of volume (|E_t|/|E|)` 的 log scale，刻度约 `10^-28` 至 `10^-3`；y 轴为 `Probability density` 的 linear scale。四条相邻的 step/histogram 曲线从浅到深表示 `D^1`、`D^2`、`D^3`、`D^4`，legend 在右上；可见黑/灰竖向 dashed threshold/reference 约两条。没有 marker、hatching 或 error band。
- **绘图语法**：该图没有栅格 XObject，按 PDF 文字/路径观察为 vector；`x=log`、`y=linear`、`grid=none`、`legend_present=true`、`legend_placement=upper right`、`shared_legend=false`、`direct_labels=false`、`marker_types=0`、`line_styles=2`（step solid 与 dashed threshold）、`reference_lines=2`、`uncertainty_display=none`、线宽约 1 pt。来源仓库没有该概念图的对应绘图脚本，因此这些属性均为 rendered estimate。
- **字体与颜色**：图内轴/legend 约 7–9 pt，DejaVu/无衬线 regular，数学变量为 Computer Modern math。四条分布曲线使用 sequential violet，近似 `#e0b3ff`、`#c77dff`、`#a855f7`、`#7a2cbf`，黑色 threshold 为 `#000000`；四档 `D^n` 有颜色加 legend 的冗余，但灰度下相邻紫色难分。
- **Caption**：
  `Figure 3. Conceptual example of using the cell-volume distribution to tighten the upper bound. Rather than assuming equal-volume cells (Dirac mass), we take the n-fold convolution of the empirical one-step volume distribution D1 (light violet) and track when the median of Dn (violet dashed) drops below the threshold (black dashed).`
  （按空白分词 50 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 定义等体积对照、D1/Dn 的颜色和 threshold，但未给出阈值数值。
- **数据与统计**：概念曲线展示 empirical one-step distribution 的乘法卷积和 median criterion；正文 p.8 §5.3 说明实际 D 来自每个 token 的 `|E_t|/|E|`，最小 n 使 median `D^n` 低于 precision-dependent threshold。此面板使用示意分布，不应解读为某个模型的 sampled density，也没有重复或不确定性。
- **证据关系**：§5.3 的 equal-volume approximation → Figure 3 的 D1→Dn 机制 → Appendix H 的 50M ellipsoid samples、Table 3、Figures 10–11。它解释 Table 1 的 Non-uniform Cells 行为什么会收紧 bound。
- **优点**：log x 轴把极小 volume 的乘法衰减放到同一视觉尺度；四档分布、median dashed 和 threshold dashed 对应正文的三个关键概念。
- **缺陷**：概念曲线没有真实模型、样本量或阈值数值；多个竖线和虚线的具体数学角色只能结合正文判断；y 轴标作 density，而展示的是示意 step profile，不能用来比较面积。
- **可复用范式**：先用一幅低负担的机制图说明「单步分布 → n-fold convolution → threshold」，再把真实分布和模型差异放到附录 Figure 10/11。

## Figure 4 — Copying-length generalization（p.9）

- **类型与职责**：`line`；`headline`、`main_comparison`、`failure`、`theory_mechanism`。图把 Corollary 4.11 的 fixed-transformer accessibility limit 连接到 synthetic exact-copying 的长序列失败。
- **几何与布局**：正文左栏单面板，x 轴 `Evaluation length`，linear 0–1000；y 轴 `Copying Accuracy`，linear 0–1。七条模型曲线均为 solid sigmoid-like lines，legend 位于右上并写模型名与对应 `R²`；一条约在训练最大长度处的 grey dashed vertical line。曲线在短字符串接近 1，跨过模型特定阈值后快速降到 0。
- **绘图语法**：图内线/文字为 vector；`x/y=linear`、`grid=none`、`legend_present=true`、`legend_placement=upper right inside panel`、`shared_legend=false`、`direct_labels=false`、`marker_types=0`、`line_styles=2`（model solid 与 training-limit dashed）、`reference_lines=1`、`uncertainty_display=none`、线宽约 1.2 pt，均来自 PDF 渲染观察。论文仓库的 `copying/run_copy_length_generalization.py` 和 shell runner 可验证合成 copy 实验参数，但仓库当前 `copying/parent_copy_artifacts.py::plot_model` 生成的是单模型、两条 context/train vertical lines 和 mean±std band 的另一张 SVG，并非本 Figure 4；因此 Figure 4 视觉属性标为 rendered estimate。
- **字体与颜色**：图内约 7–10 pt 的 MyriadPro/Segoe UI/DejaVu Sans regular，数学 `R²` 使用 Computer Modern。七条模型线的 PDF 颜色为 `#1f77b4`、`#2c9f2c`、`#ff7e0e`、`#d52728`、`#9367bc`、`#8b554a`、`#e277c2`，训练长度线为灰色 `#808080`；颜色与 legend 文本双重编码，模型线型本身没有额外区分，灰度下曲线仍可追踪但模型身份不稳定。
- **Caption**：
  `Figure 4. Models are trained to copy strings up to a maximum length (grey dashed) and evaluated on generating the exact copy of longer strings. We report exact-match copying accuracy versus string length. For each model, we fit a sigmoid to the accuracy curve (continuous lines) and report the corresponding R2 .`
  （按空白分词 52 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`uncertainty_definition`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 定义训练/评测方向、exact-match、sigmoid 和 line key，但没有写模型列表、seed 或 band。
- **数据与统计**：§5.4 说明随机字符串长度至多 50 的 next-token cross-entropy fine-tuning，训练在 length 50 达到 100% exact-match 或 10K optimization steps 后停止；再在 context window 内评估更长 unseen strings。图显示 7 个模型的 exact-match accuracy 曲线，legend 中 `R²` 为 sigmoid fit 指标（Qwen2.5-1.5B 低至 0.46，median 为 0.95），没有 error bar、重复运行或 seed。
- **证据关系**：Theorem 4.10/Corollary 4.11 的「固定 transformer 的可达序列上限」→ §5.4 copy-length experimental design → Figure 4 的 transition → p.9 对 “every transformer admits an accessibility limitation” 的解释。它是失败模式证据，而不是对训练 loss 或 token-level accuracy 的诊断。
- **优点**：共享 x/y 轴直接对比七个模型的 transition location；灰 dashed training cutoff 让训练分布与外推区间可见；曲线形状与正文的 abrupt decline 叙述一致。
- **缺陷**：没有直接标出每个模型的 transition length 或置信/重复范围；legend 的 `R²` 是拟合质量而非 copying success 的不确定性，且不同模型的拟合质量差异较大；训练上限线没有数字标签，脱离相邻正文难以知道是 50。
- **可复用范式**：将「训练覆盖范围」用 reference line 固定，将多个模型的外推 failure curves 叠加，用一个统一的 sigmoid summary 对齐阈值形状；应另配 threshold table 或重复变异。

## Figure 5 — Bounded internal radius（p.15）

- **类型与职责**：`line`；`theory_mechanism`、`experimental_design`、`robustness`。这是 Appendix A 对 bounded embedding support 的经验检查。
- **几何与布局**：7 个 panel，按 3+3+1 排列，最后一行只显示 Gemma-3 270M，其他位置留白。每 panel 标出模型名；x 轴为 `max sampled input length ℓ_max`，linear，约覆盖 0–4000；y 轴为 `R`，各模型使用自己的窄范围。每 panel 一条蓝色 solid line 和圆 marker，前几个短长度点迅速上升，随后形成平台；无 legend、无 inset、无 error band。
- **绘图语法**：PDF 中线、marker、文字均为 vector；`x/y=linear`、`grid=none`、`legend_present=false`、`shared_legend=null`、`direct_labels=true`（panel title）、`marker_types=1`、`line_styles=1`、`reference_lines=0`、`uncertainty_display=none`、线宽约 1 pt；属性由 200 dpi 渲染估计。图中七个 panel 的数据线约各 8 个 sampled-length marks，合计约 56 个可见 marks。
- **字体与颜色**：panel title、axis text 约 6–8 pt DejaVu Sans regular，数学 `ℓ_max` 为 math italic；蓝线/marker 近似 Matplotlib `#1f77b4`。颜色只编码同一统计量，不编码模型；模型身份由标题冗余标记，灰度安全性较好。
- **Caption**：`Figure 5. Maximal radius R of the internal representations of the transformer for various input lengths.`（按空白分词 16 词）。动作是 `title`、`setup`；`headline_bold=false`、`self_contained=false`、`main_finding_stated=false`。caption 没有列模型、采样次数、轴单位或 uncertainty 定义，需结合 Appendix A/G.4。
- **数据与统计**：每个模型随最大 sampled input length 取 internal representation 的 maximal radius `R`；图体现 radius 在延长 sampling 后基本稳定。它是单个最大值轨迹，没有分位数、重复或 Monte Carlo error；附录 p.14–15 说明 transformer layer 的 bounded support，Table 2 的 `r` 则用更具体模型常数。
- **证据关系**：Appendix A 的 bounded-transformer-layer definitions → Figure 5 的 empirical radius stability → Appendix G.1 Table 2 的 `r` → Figure 9 的 geometry-dependent upper bound。它支撑假设的可用性，但不直接验证 theorem 的 sequence-count conclusion。
- **优点**：小 multiples 让七个模型的 support-radius plateau 结构并列可见；统一蓝线和模型标题使阅读路径简单；x 轴延伸到 4000，能够显示长 sampling 后的稳定段。
- **缺陷**：各 panel y 范围不同，视觉高度不能直接比较模型 radius；只画 maximum，极端点敏感，未显示 mean/quantiles；没有 legend、sample size 或 sampling seed。
- **可复用范式**：对一个假设相关的 support statistic 使用固定 x 轴的小 multiples，直接检查随 sampling budget 的收敛，再把最终常数放入主表。

## Figure 6 — Cone decomposition proof diagram（p.22）

- **类型与职责**：`conceptual_diagram`；`theory_mechanism`、`method_interface`。图服务 Appendix F 的 cone-volume proof，把 cone 分为 conical part `E_δ` 和 spherical-cap part `F_δ`。
- **几何与布局**：单个居中二维示意图。竖直 `x_1` 轴穿过 cone apex；蓝色实线边界是 cone，顶部红色弧形 cap 标为 `E_δ`，下部蓝色区域标为 `F_δ`，两者以水平 dashed chord 分开；apex 有 `δ` 角弧标注。没有数值刻度、网格、legend 或数据 marker，x/y 均为 `none`。
- **绘图语法**：`pdfimages` 显示图本体为带 mask 的 213×84 RGB raster XObject，caption 和正文为 vector；`rendering=raster`（从 PDF figure object 角度）、`x/y=none`、`grid=none`、`legend_present=false`、`shared_legend=null`、`direct_labels=true`、`marker_types=0`、`line_styles=3`（blue/red solid、horizontal dashed、angle arc）、`reference_lines=0`、`uncertainty_display=none`、线宽约 1.2–1.5 pt，为 rendered estimate。
- **字体与颜色**：图内 `x_1`、`E_δ`、`F_δ`、`δ` 使用 Times/Computer Modern math，约 7–12 pt；red `#ff0000` 对应 cap `E_δ`，blue `#0000cc` 对应 cone/`F_δ`，black/gray 对应 axis、chord、angle。颜色、分区标签和边界线型冗余承载 proof role；灰度仍能靠区域文字和边界读懂，但红蓝语义会减弱。
- **Caption**：`Figure 6. Decomposition of the cone in Eδ and Fδ.`（按空白分词 10 词）。动作仅为 `title`；`headline_bold=false`、`self_contained=false`、`main_finding_stated=false`。caption 不解释 cap/cone 的几何条件，需要阅读 Appendix F.2 的 Step 3–4。
- **数据与证据关系**：无数据；图示 Section F.2 的 `E_δ` conical volume 与 `F_δ` spherical-cap volume 的分解，随后分别积分并在 Step 5 合并。它连接 Proposition F.3/Lemma F.4 的证明与 Table 1 Cone row 的 bound。
- **优点**：红/蓝分区直接对应证明中两个积分项；水平 chord、轴和 δ arc 暴露后续公式的几何边界。
- **缺陷**：二维示意不能按比例表示 d 维 cone 或体积；caption 太短，没有定义 `δ`、半径或 spherical cap；图体 raster 尺寸小，放大后文字边缘质量低。
- **可复用范式**：把复杂体积证明拆成带符号的颜色分区图，使每个后续积分项有明确空间对象；caption 至少补一行符号定义可进一步降低复核成本。

## Table 2 — Model constants（p.23）

- **版面与结构**：Appendix G.1 的双栏页宽表，4 个数据行、7 个模型列；两级表头为模型家族和规模，横线为 booktabs top/header/bottom，无竖向完整网格。行名为 `Hidden dimension d`、`Vocabulary Size |V|`、`Radius r`、`Cone angle θ`。正文约 9 pt，表头约 10 pt，Nimbus Roman regular/medium 与 Computer Modern math。
- **Caption**：`Table 2. Model constants used to estimate slope upper-bound ratios in Table 1. The dimensionality d and vocabulary size |V| are determined by the model architecture, while r and θ are estimated in Section 5.2.`（按空白分词 35 词）。动作是 `title`、`setup`、`comparison`、`appendix_pointer`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 明确 architectural constants 与 estimated quantities 的边界。
- **数据与统计**：七列顺序为 Pythia 160M/410M/1B、Qwen-2.5 0.5B/1.5B、Llama-3.2 1B、Gemma-3 270M。`d` 为 `768, 1024, 2048, 896, 1536, 2048, 640`；`|V|` 为 `50304, 50304, 50304, 151936, 151936, 128256, 262144`；`r` 为 `63.62, 54.90, 65.68, 309.00, 153.62, 41.06, 10.74`；`θ` 为 `1.96, 1.87, 2.22, 2.23, 2.34, 1.73, 1.82`。表没有误差、重复、sample count 或 fit quality；前两行是 architecture constants，后两行由 §5.2 sampling estimate。
- **证据关系**：§5.2 的 support geometry → Table 2 constants → Appendix F packing formulas → Table 1 rows Ball/Cone/Ellipsoid。该表是 `reproduction` 和 `theory_mechanism` 的接口，补足主文 Table 1 不能容纳的参数来源。
- **优点**：家族/规模两级表头与 Table 1 完全对齐；将 architecture constants 与 geometry estimates 分成明确行，便于复现 bound。
- **缺陷**：`r` 与 `θ` 没有 sampling error 或 confidence；`θ` 的单位/定义（angle versus cosine-derived quantity）不在表头展开；列顺序虽稳定，但表内没有直接给出 estimate 的 prompt count，需回读 Appendix G.4。
- **可复用范式**：用与主比较表相同的模型列顺序，把公式所需的 constants 集中在 appendix 表，并在 caption 明确哪些值来自 architecture、哪些来自 sampling。

## Table 3 — Largest decoder-cell tokens（p.26）

- **版面与结构**：Appendix H 页宽表，7 个模型行、2 列（`Model`；`Tokens corresponding to largest cells E_t (|E_t|/|E|)`），单级表头，top/header/bottom booktabs 规则，无竖线。第二列内每模型列出五个 token/value pair；正文约 8–9 pt Nimbus Roman，token/code 片段使用等宽或 monospaced glyph，数学比例使用 Computer Modern。
- **Caption**：`Table 3. Tokens with the largest estimated decoder-cell volumes (Section 5.3). Volumes are shown in parentheses. Whitespace/control characters are rendered explicitly (e.g., <space>, \n). For non-ASCII tokens (e.g., Gemma), we show the Unicode code.`（按空白分词 34 词）。动作是 `title`、`setup`、`encoding_key`、`abbreviation_definition`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 定义括号数值、空白/control token 和 Unicode code 的显示规则。
- **数据与统计**：每行是五个最大估计 cell volumes，括号为 `|E_t|/|E|`，不是模型性能均值。PDF 可读内容为：Pythia-160M `<ν> (5.5e−3), <κ> (4.7e−3), < > (4.1e−3), <|endoftext|> (3.9e−3), <well> (2.9e−3)`；Pythia-410M `<\n> (0.21), <,> (0.08), < (> (0.07), <-> (0.06), <.> (0.05)`；Pythia-1B `<\n> (0.25), <,> (0.21), <-> (0.10), <.> (0.054), < (> (0.036)`；Llama-3.2 1B `< > (0.38), <,> (0.19), <\n> (0.094), < (> (0.059), <-> (0.051)`；Qwen-2.5 0.5B `< > (0.70), <,> (0.14), <-> (0.038), <\n> (0.036), <.> (0.021)`；Qwen-2.5 1.5B `< > (0.81), <,> (0.076), <\n> (0.038), <-> (0.033), < (> (0.011)`；Gemma-3 270M `<eos> (1.1e−4), <U+000A U+000A> (1.0e−4), </> (9.6e−5), <U+3054 U+7406 U+89E3> (7.0e−5), <<h2>> (6.7e−5)`。这些是 Appendix H 的 50M-sample cell-volume estimates，没有 error bar、rank uncertainty 或 repeated volume runs。
- **证据关系**：§5.3 的 non-uniform cell hypothesis → Appendix H 的 volume computation → Table 3 的 extreme tokens → Figure 10 的 full ranked profile 和 Figure 11 的 convolution。它为 Table 1 的 Non-uniform Cells row 提供 qualitative/numeric interface。
- **优点**：把「哪些 token 占大 cell」和比例放在同一行，直接暴露 punctuation/whitespace/special-token 的模型差异；显式转义 control/Unicode token，便于复现。
- **缺陷**：长 token 列在页宽内换行，模型间的第五名不易横向扫描；只列 top five，不能从表中得到完整 tail；没有给每个 cell 的 Monte Carlo variance 或 sample denominator（尽管 Appendix H 说明总 samples）。
- **可复用范式**：对长尾分布同时提供 top-k 原子项和规范化比例，配合明确的 token escaping 规则；完整 tail 交给 ranked plot。

## Figure 7 — Pythia accessibility suite（p.27）

- **类型与职责**：`line` + `scatter`；`robustness`、`main_comparison`、`experimental_design`、`reproduction`。图把主文 Figure 2 的单模型证据扩展到 Pythia 160M、410M、1B 三种规模。
- **几何与布局**：页宽纵向 3 个 model blocks，每个 block 有 a/b 左侧上下两个 accessibility panels 和 c 右侧 `n50(m)` panel；总计 9 个可见 panels，底部 block labels 为 `(A) Pythia-160M`、`(B) Pythia-410M`、`(C) Pythia-1B`。每 block 的 a/b 有 PG19/Random、五个 `m=1…5` 曲线、raw dots、五条 vertical dashed `n50`；c 有 blue circle/red x 和 two linear fits。legend 在每个 block 的 accessibility panels 右上，c fit key 在左上。
- **绘图语法**：以 Figure 2 notebook 的 source_exact 参数为基础，最终 composite 的排版由 PDF observation 验证，故 `provenance=mixed`；`rendering=vector`、`x/y=linear`、`grid=none`、`legend_present=true`、`legend_placement=a/b upper right; c upper left per block`、`shared_legend=false`、`direct_labels=false`、`marker_types=3`、`line_styles=3`、`reference_lines=30`（三 blocks × a/b × 五 vertical `n50`）、`uncertainty_display=none`、线宽约 1 pt。复杂度为 5：超过 8 个 panel 且重复 legend/fit。
- **字体与颜色**：panel label/title/axis 约 6–10 pt MyriadPro/Segoe UI/DejaVu Sans；PG19 使用五档 `Blues`、Random 使用五档 `Reds`，近似色阶同 Figure 2（蓝 `#a9cfe5`→`#084594`，红 `#fc9272`→`#99000d`），fit 用 black/gray。颜色与上/下 panel、line styles 和 legend 共同编码；灰度仍能辨认 dataset/random，但五档 `m` 的明度难完全区分。
- **Caption**：
  `Figure 7. Mean accessibility for a) PG19 and b) random target sequences of length n as a function of the number of trainable memory vectors m. For each m, we fit a sigmoid (solid) and mark n50 where the fit crosses 0.5 (vertical dashed line). (c) n50(m) for PG19 (blue) and random (red), with linear fits (dashed). Results shown for the Pythia model suite at different scales A) 160M, B) 410M, C) 1B.`
  （按空白分词 73 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`appendix_pointer`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 完整说明重复 Figure 2 语法和 block model identity。
- **数据与统计**：三个 Pythia scale 使用同一 PG19/random target design、五个 memory lengths 和 20-target mean accessibility，c panel 用 linear fit 汇总 `n50`；不同 block 的 x range/y range 随 model capacity 改变。没有重复运行误差、confidence band 或 threshold uncertainty。
- **证据关系**：p.7 Figure 2 的 Qwen2.5-1.5B → Appendix G.3 的 cross-size check → Figure 7 → 论文对 architecture-size generality 的边界。它支持 robustness/reproduction，而不是一个新的 component ablation。
- **优点**：保持 Figure 2 的三面板 grammar，读者无需学习新图例；规模变化的 threshold slope 可以直接与主文 c panel 对照；每个 block 有独立 model title。
- **缺陷**：9 个 panel 和重复 legend 占据整页，字体小；block 间坐标范围不完全统一，横向比较绝对 threshold 需要读坐标；同一图重复显示 raw dots 但仍没有 uncertainty summary。
- **可复用范式**：先冻结一个主图 grammar，再以 model block 重复，保证跨规模证据可比；当 blocks 超过两行时应考虑 shared axis/legend 以降低视觉负担。

## Figure 8 — Cross-architecture accessibility suite（p.28）

- **类型与职责**：`line` + `scatter`；`robustness`、`main_comparison`、`experimental_design`、`reproduction`。它检验 Qwen-2.5、Gemma-3、Llama-3.2 三架构下的 Figure 2 pattern。
- **几何与布局**：与 Figure 7 相同的 3×(a,b,c) block 结构，block labels 为 `(A) Qwen-2.5`、`(B) Gemma-3`、`(C) Llama-3.2`，总计 9 panels。a/b 分别为 PG19/random accessibility，c 为 `n50(m)`；五个 `m` 值使用蓝/红渐变，vertical dashed lines 标出曲线 crossing，c 的 blue circles/red x 加 dashed/dotted linear fits。legend 逐 block 重复。
- **绘图语法**：`rendering=vector`、`x/y=linear`、`grid=none`、`legend_present=true`、`legend_placement=a/b upper right; c upper left per block`、`shared_legend=false`、`direct_labels=false`、`marker_types=3`、`line_styles=3`、`reference_lines=30`、`uncertainty_display=none`、线宽约 1 pt，source style 与 PDF composite 共同验证，故 `provenance=mixed`。复杂度为 5。
- **字体与颜色**：图内约 6–10 pt 无衬线/Computer Modern math；`Blues`/`Reds` 五档色阶与 Figure 2/7 一致，fit 线为 black/gray。颜色映射的是 target source 和 memory length，而不是 architecture；架构由 block title 直接标注。数据与 panel/line style 有冗余，但灰度下颜色档位仍较弱。
- **Caption**：
  `Figure 8. Mean accessibility for a) PG19 and b) random target sequences of length n as a function of the number of trainable memory vectors m. For each m, we fit a sigmoid (solid) and mark n50 where the fit crosses 0.5 (vertical dashed line). (c) n50(m) for PG19 (blue) and random (red), with linear fits (dashed). Results shown for three architectures A) Qwen-2.5, B) Gemma-3, C) Llama-3.2.`
  （按空白分词 68 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`appendix_pointer`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。
- **数据与统计**：各架构使用 same target sources、five `m`、20-target mean；c 面板的 slope/fit 反映 architecture-specific threshold scale。没有 error bars、seed variability、样本量标签或直接的 architecture interaction test。
- **证据关系**：Figure 2 的 canonical Qwen panel → Appendix G.3 architecture slice → Figure 8 → 论文“可达性 pattern 跨架构保持”的经验边界。Table 1/2 提供相同七模型的 geometric constants，但本图不直接画 geometry。
- **优点**：跨架构结果保持与 Figure 2 相同的 panel semantics，可低成本复用解读；model block label 明确，不把颜色误读为 architecture。
- **缺陷**：整页重复 legend/axis labels，信息密度高；架构间 panel y-range 与 n-range 不完全相同；图把 fitted crossing 当 summary，却没有显示 fit residual 或 uncertainty。
- **可复用范式**：用同一 accessibility grammar 分层展示 architecture generalization，并把架构名称放在 block-level title，不占用额外 color channel。

## Figure 9 — Support geometry upper-bound convergence（p.29）

- **类型与职责**：`line`；`theory_mechanism`、`robustness`、`reproduction`。图检查 Monte Carlo sampled prompt length 增大后，Ball/Cone/Ellipsoid 的 theoretical slope upper bound `C` 是否稳定。
- **几何与布局**：3×3 small-multiple grid 中显示 7 个模型 panel：a Pythia-160M、b Pythia-410M、c Pythia-1B、d Qwen2.5-0.5B、e Qwen2.5-1.5B、f Gemma-3 270M、g Llama-3.2-1B，两个空位关闭。x 轴为 `max sampled input length ℓ (tokens)`，linear，主要刻度 0/500/1000；y 轴为 `upper bound on slope C`，各 panel 范围不同。每 panel 有 Ball blue solid、Ellipsoid orange dotted、Cone green dashed，圆 marker；legend 仅在 a panel 右上，作为共享 key。
- **绘图语法**：`rendering=vector`、`x/y=linear`、`grid=none`、`legend_present=true`、`legend_placement=panel a upper right`、`shared_legend=true`、`direct_labels=false`、`marker_types=1`、`line_styles=3`、`reference_lines=0`、`uncertainty_display=none`、线宽约 1 pt；`th_bounds_estimation.ipynb` cell 7 精确给出 `figsize=(4*ncols,3*nrows)`、`marker='o'`、Ball `'-'`、Ellipsoid `':'`、Cone `'--'`、legend fontsize 10、去除 top/right spine、x/y locator，输出 `theoretical_slopes_archi_big.pdf` dpi 200。
- **字体与颜色**：panel title/axis 约 7–10 pt DejaVu Sans，math `ℓ/C` 使用 Computer Modern；源默认 Matplotlib cycle 与 PDF 观察相符：Ball `#1f77b4`、Ellipsoid `#ff7f0e`、Cone `#2ca02c`。颜色、legend、线型三重编码，灰度下仍可借助 solid/dotted/dashed 区分。
- **Caption**：
  `Figure 9. Upper bound on C for different support geometry —Ball (blue), Cone (green), Ellipsoid (orange)—, estimated using 10K randomly sampled input strings of maximum length ℓ. Sampling prompts longer than ℓ ≈ 500 suffices to estimate the upper bound. Pythia models for different sizes: a) 160M b) 410M, c) 1B and support for different model architectures d–e) Qwen (0.5B, 1.5B) f) Llama 1B, g) Gemma 270M.`
  （按空白分词 67 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 定义 geometry/color、10K samples、length threshold 和 panel model mapping，但没有 uncertainty。
- **数据与统计**：每个 model/geometry 组合用 10K randomly sampled input strings，x 是最大 prompt length，y 是根据 support shape 计算的 C upper bound；长于约 500 的 sampling 被认为足以稳定估计。渲染后的 panel title 显示 `f) Gemma-3-270M`、`g) Llama-3.2-1B`，但 PDF caption 写作 `f) Llama 1B, g) Gemma 270M`；这里按 panel 的实际可见标题记录对象，同时保留 caption 的文字错置。主文 §5.2 的叙述使用 `ℓ≈1000` 作为实践稳定点，与 caption 的 `≈500` 存在措辞/阈值差异，应并列记录而不能强行统一。
- **证据关系**：§5.2 的 support refinement → Appendix G.4 sampling procedure → Figure 9 → Table 1 Cone/Ellipsoid rows 和 Table 2 `r,θ`。图回答的是 bound estimation stability，而不是 sequence accuracy。
- **优点**：共享 x 语义、几何线型和首 panel legend，使七个模型的收敛轨迹可扫读；style source exact，包含 spine/tick/size 细节，复现路径明确。
- **缺陷**：不同 panel y 轴范围不一致，绝对高度容易被误读为跨模型可比；没有 Monte Carlo error band；caption 与正文对“足够长”的经验阈值为 500/1000 两种表述；两个空 panel 形成较多留白。
- **可复用范式**：用一个 shared legend 的 support-geometry small multiples 检查上界随 sampling budget 的收敛，并保留 geometry 的线型冗余编码以保证黑白可读。

## Figure 10 — Ranked decoder-cell volume tail（p.29）

- **类型与职责**：`scatter`；`theory_mechanism`、`robustness`、`reproduction`。图是 Appendix H 对 non-uniform cell-volume hypothesis 的完整 ranked profile。
- **几何与布局**：单个居中 log-log scatter，x 为 `Token rank (sorted by decreasing proportion)`，y 为 `Proportion of samples in token cell`，两轴均 log；七个模型以散点叠加，legend 位于右上，top/right spines 隐藏，网格为 both、alpha 约 0.1。没有 title、line、reference line、marker shape variation 或 uncertainty band。
- **绘图语法**：`rendering=vector`、`x/y=log`、`grid=both`、`legend_present=true`、`legend_placement=upper right`、`shared_legend=false`、`direct_labels=false`、`marker_types=1`（small circle）、`line_styles=0`、`reference_lines=0`、`uncertainty_display=none`、点大小 `s=8`、无 edge，来源 `cell_volume_tests.ipynb` cell 10 与 PDF 结构精确匹配，`provenance=source_exact`（最终字体仍以 PDF object 为准）。
- **字体与颜色**：源 cell 10 明确使用 `figsize=(6,4)`、`s=8`、`alpha=1`、legend fontsize 10/frame off、grid alpha .1、top/right spine hidden、PDF 输出 dpi 150。七模型颜色精确为 Pythia-160M `#87adf0`、Pythia-410M `#45a1e2`、Pythia-1B `#215E8C`、Qwen2.5-0.5B `#4aac7b`、Qwen2.5-1.5B `#177517`、Llama3.2-1B `#ec8333`、Gemma3-270M `#934fd3`；图中文字约 7–10 pt DejaVu/Segoe UI regular。颜色按模型/家族编码并配合 legend，但没有线型或 marker 冗余，灰度下模型曲线易混。
- **Caption**：
  `Figure 10. Relative volumes of decoder cells across tokens (log-log). For each model, tokens are sorted by estimated cell volume (largest on the left). A small set of tokens (typically < 10^2) accounts for a large fraction of the support volume, while most tokens (10^4–10^5) have tiny individual volumes (often 10^−6–10^−8 of the support).`
  （按空白分词 54 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`main_finding`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=true`。caption 直接写 long-tail 主结论，且定义排序和数量级。
- **数据与统计**：Appendix H 以 ellipsoid 内 sampled points 的 greedy decoder token frequency 估计 `|E_t|/|E|`，再按 proportion 降序排列；源 cell 10 对每个模型保留前 100 rank 并以 log-spaced ranks 抽取 tail，用 scatter 叠加七个模型。图呈现极少 token 占较大 volume、长尾 token 的 proportion 约 `10^-6`–`10^-8`；无重复或 sampling interval。
- **证据关系**：§5.3 的 non-uniform cells → Appendix H sampling/volume estimator → Figure 10 ranked tail → Table 3 top-k tokens、Figure 11 n-fold convolution、Table 1 fourth row。它是机制 evidence 而非性能 headline。
- **优点**：log-log rank profile 同时显示头部与长尾，且 source code 明确处理 tail subsampling，避免全量 token 堆叠；去除 top/right spine 与低 alpha grid 保持可读。
- **缺陷**：七条模型曲线只靠颜色和 legend，曲线尾部重叠后难定位；抽样的 tail 点密度不是原始 token count，caption 没有提醒这一可视化抽样；y 轴名称是 sample proportion，仍需结合 Appendix H 才能确认它作为 cell-volume proxy。
- **可复用范式**：对于跨度数十个数量级的长尾，采用排序后的 log-log rank plot，并明确头部全量、尾部 log-spaced subsampling；颜色应再配线型或小 multiples 以增强可复核性。

## Figure 11 — n-fold volume distributions（p.30）

- **类型与职责**：`histogram`；`theory_mechanism`、`robustness`、`reproduction`。图把 Figure 3 的概念 convolution 扩展为七个模型的 empirical distribution。
- **几何与布局**：页宽 3×3 small multiples，7 个模型 panel、2 个空位；panel labels a–g 及模型名分别为 Pythia-160M、Pythia-410M、Pythia-1B、Qwen2.5 0.5B、Qwen2.5 1.5B、Llama3.2 1B、Gemma3 270M。每 panel x 为 `Proportion of volume (|E_t|/|E|)`，log；y 为 `Probability density`，linear；六条 step curves `n=1…6` 用 tab10 前六色，legend 在 panel a 左上作为共享 key，网格 both、alpha 约 .2。
- **绘图语法**：`rendering=vector`、`x_scale=log`、`y_scale=linear`、`grid=both`、`legend_present=true`、`legend_placement=panel a upper left`、`shared_legend=true`、`direct_labels=false`、`marker_types=0`、`line_styles=1`、`reference_lines=0`、`uncertainty_display=distribution`、线宽约 1 pt，最终 composite 与 `cell_volume_tests.ipynb` cell 17 的 style/geometry 混合核对，故 `provenance=mixed`。源 cell 的默认 `max_k=4`，而 PDF 实际显示六条 `n=1…6` 曲线；该参数差异已保留，不能把 cell 17 直接称为成品精确源。
- **字体与颜色**：panel title/axis/legend 约 6–9 pt DejaVu Sans/Segoe UI regular；六条 n curves 使用 Matplotlib tab10 前六色 `#1f77b4`、`#ff7f0e`、`#2ca02c`、`#d62728`、`#9467bd`、`#8c564b`，n 由颜色和 shared legend 编码。网格和 step 形状提供少量冗余；灰度下 n=2/4/6 仍可能混淆。
- **Caption**：
  `Figure 11. Distribution of n-sequences volumes proportions by estimating the n-fold convolution of the empirical one-step volume distribution D for different models: a) Pythia-160M, b) Pythia-410M, c) Pythia-1B, d) Qwen2.5 0.5B, e) Qwen2.5 1.5B, f) Llama3.2 1B, g) Gemma 270M.`
  （按空白分词 40 词）。动作是 `title`、`setup`、`comparison`、`appendix_pointer`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。caption 给出估计对象和七个 panel mapping，但没有显式定义 y 轴是 normalized mass 还是 density。
- **数据与统计**：每个模型先从 Appendix H 的 one-step proportions 构造 empirical `D`，再做 n-fold multiplicative convolution；PDF 实际展示 n=1–6 的 normalized step distributions。源 cell 17 使用 70 log bins、`n=2000` compression、uniform weights；源码 y 计算是每 bin 的 normalized weighted histogram，而 PDF label 为 `Probability density`，因此 density/mass 语义需谨慎区分。无 error bar、seed 或 convolution approximation error。
- **证据关系**：Table 3/Appendix H one-step volumes → Figure 11 的 n-fold distributions → Figure 3 median threshold mechanism → Table 1 non-uniform-cell tightening。它展示不同模型的 long-tail 如何在 n 增大时迁移，而不是直接测试 copying accuracy。
- **优点**：七模型小 multiples 保持同一 x semantics，n=1…6 的 step overlays 使 convolution shift 直接可见；shared legend 避免每 panel 再占空间。
- **缺陷**：六条颜色曲线在小 panel 中密集，两个空位留白明显；caption 与源码对 y-axis density/mass 的定义不完全一致；`n` 的颜色没有 line-style/label 冗余，灰度和打印复核成本高；近似 compression/binning 参数只在源码而不在 caption。
- **可复用范式**：将同一分布变换的多个阶数以统一 log-x 小 multiples 展开，并把模型维度放在 panel、阶数放在颜色；对于 normalized histogram，应在 caption 明确 bin mass、density 与 compression。

## 跨对象评价

1. **方法—理论—结果链**：Figure 1 提供 `E_t`/prompt-region 的几何接口；Figure 2 将 Corollary 4.7 变成 accessibility threshold 与 `n50(m)`；Table 1 把 geometry/cell refinement 与 empirical slope 相连；Figure 3 解释 non-uniform convolution；Figure 4 用 copy failure 体现 arbitrary-length limitation。Figures 5–11 和 Tables 2–3 逐层补充 bounded radius、proof geometry、constants、top-k volume 与完整 tail/convolution。
2. **主文与附录分工**：主文保留 Figure 1–4、Table 1，形成「直觉—阈值—bound refinement—failure」最小论证；附录把跨模型 accessibility（Figures 7–8）、support convergence（Figures 5、9）、cell-volume implementation（Table 3、Figures 10–11）和 cone proof（Figure 6）展开。主文的视觉结论依赖附录中的 model constants 与 sampling details，不能只按主文对象判断 reproducibility。
3. **Caption 系统**：Figure/Table caption 统一为斜体编号 + 描述句；Figure 1/2/7/8/9/11 主要写 setup/encoding，Figure 10 明确写出长尾 main finding，Table 1/2/3 说明行列或 token display。大多数 caption 没有 uncertainty definition；Figure 4 写 `R²` 但它是 fit quality，不是不确定性。Caption 自包含程度以 Figure 1/2/3/7/8/9/10/11 较好，Figure 5/6 需要附录正文。
4. **表头系统**：Table 1/2 使用模型家族→规模两级 header，保证主表和常数表列顺序一致；Table 3 使用 model→token list 的单级 header。Booktabs 规则和无颜色表格提高黑白安全性，但 Table 1 的小数精度、Table 3 的长字符串换行和所有表缺少估计误差限制了横向复核。
5. **颜色与版式一致性**：Figure 2/7/8 的 Blues/Reds 语义稳定，Figure 9 的 geometry 颜色和线型稳定，Figure 10 按模型族使用蓝/绿/橙/紫，Figure 11 按 n 使用 tab10。Figure 1 的 token regions 和 Figure 6 proof diagram 使用独立颜色系统；正文/表格保持黑白。这种局部一致性足以支撑各图内部阅读，但跨图没有统一色值语义（例如蓝色既可代表 PG19、Ball、Pythia，也可代表任意 region）。
6. **未闭合的测量边界**：主文文字把 Figure 2 的 sigmoid/linear fits 作为 threshold evidence，把 Figure 4 的 curve decline 作为 copying limitation evidence；但没有 plot-level error bands、seed replication、confidence intervals 或对 Theorem 4.10 的直接 finite-capacity count。Figure 3 是概念图，Figure 5 只有 max radius，Figure 9 的 500/1000 sampling threshold 也不是独立不确定性估计。

## 最终判断

### 最可复用模式

1. Figure 2/7/8 的「条件曲线 + vertical threshold + 右侧 derived summary」：保留原始 accessibility 轨迹，再把理论关心的 crossing quantity 单独呈现。
2. Table 1/2 的稳定模型族两级表头：把 approximating strategy 与 model constants 分开，列顺序完全复用以降低跨表认知成本。
3. Figure 5/9/11 的 small multiples：将 model/geometry 放入 panel，将唯一变化因子映射到颜色、线型或阶数，避免把所有维度叠到一个 panel。
4. Figure 10 的长尾 log-log rank 语法：头部全量、尾部 log-spaced subsampling，并在 caption 写出数量级语义。
5. Figure 1/6 的符号化分区图：用颜色、直接 label 和边界线型把抽象 proof/partition 对象连到公式符号。

### 信息价值最高的对象

- **Figure 2**：唯一同时显示 PG19/random、memory length、accessibility transition 和 `n50(m)`，是核心理论预测的最短可检验接口。
- **Table 1**：把 theoretical upper bound、support geometry、cell-volume refinement 和七模型 empirical slope 放在同一决策面。
- **Figure 4**：把 abstract accessibility limitation 转译为多模型 copying failure，且对读者最直观。
- **Figure 10 + Figure 11**：把 Table 1 的 non-uniform-cell tightening 展开为完整长尾与 n-fold distribution evidence。

### 失败模式

1. 多数对象没有误差/重复编码；Figure 2/4 的拟合与 Figure 5/9/10/11 的 sampling/convolution 都无法从视觉层判断 run-to-run 或 Monte Carlo variation。
2. 颜色承担过多 identity：Figure 2/7/8 五档 `m`、Figure 10 七模型、Figure 11 六个 `n` 在灰度和小 panel 下缺少足够的线型/标签冗余。
3. Table 1 小数精度混排，Table 3 token 列长且换行；精确复核需要回到 PDF 文本/附录，而不是只扫表格。
4. Figure 3/5/6 的 caption 省略关键数值或符号定义；Figure 9 的 caption 与正文把稳定 sampling length 写成约 500/约 1000 两种尺度；Figure 11 的 PDF `Probability density` 与源码 normalized histogram 的统计语义没有完全闭合。
5. 主文 Figure 4 的公开仓库包含 copy 实验 runner，但现有通用 plotting helper 与论文成品图不同；若把候选脚本直接视为 exact visual source，会错误地把 mean±std band、context line 等未出现在 PDF 的元素归入论文。

### 一句话视觉策略

论文先用 embedding-plane 与 accessibility threshold 建立「decoder geometry → finite accessible sequences」的机制链，再以 slope-ratio 表、copying transition 和附录的 geometry/cell-volume small multiples 逐级收紧理论上界并展示跨模型长尾，但把不确定性和部分复现参数留在图外文本与源码中。

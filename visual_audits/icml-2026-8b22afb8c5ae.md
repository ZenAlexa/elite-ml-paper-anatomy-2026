# 视觉审计：`icml-2026-8b22afb8c5ae`

## 范围与对象清单

- **论文**：*Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels*（Dongming Huang、Zhifan Li、Yicheng Li、Qian Lin）。
- **本地事实源**：`corpus/preprints/icml-2026-8b22afb8c5ae.pdf`；`pdfinfo` 显示 73 个 letter 物理页（612 × 792 pt），标题为 *Effective Span Dimension for Learned Kernels*。正文为 p. 1–9，References 为 p. 9–12，Appendix A–I 为 p. 13–73。
- **阅读与渲染**：用 `pdftotext` 逐页读取 p. 1–73（正文、References、附录和证明），并将全 PDF 以 180 dpi 渲染；含对象的 p. 7–9、18–19、24–27 再以 220 dpi 检查，关键图页另以 600 dpi 裁剪检查。`pdfimages -list` 没有报告栅格 XObject；图内曲线、坐标轴、网格、图例和文字均为 PDF 矢量路径/字体对象。
- **对象对齐**：reading 的 `visual_inventory` 给出 5 幅 Figure、0 张 Table。PDF 实际对象包括 Figure 1（p. 8，主文）、Figure 2（p. 8，主文）、Figure 3（p. 19，Appendix B.4）、Figure 4（p. 25，Appendix C.4）和 Figure 5（p. 27，Appendix D.2）。全文没有 `Table`/`Table n`、跨页表、qualitative table 或 pseudocode 表；最终清单为 **5 figures、0 tables**，与 PDF 对齐。
- **页码说明**：p. 7、18、24、26 是对象前的设置/调用段落；图形和 caption 实际落在下一页。审计页码按 PDF 物理页，不按章节起始页推算。

## 公开源获取

PDF 首页、正文脚注和 References 只提供 `https://openreview.net/forum?id=4HrWo5x7YF` 与 `https://arxiv.org/pdf/2509.20294`，没有 GitHub、project 或 supplementary code URL。按完整标题和方法词执行 `gh search repos`、`gh api /search/repositories`，再以完整标题执行只读 `gh api /search/code`；严格命中的代码关联仓库为 [MachineLearning-Nerd/icml26-spectral-minimax-rates](https://github.com/MachineLearning-Nerd/icml26-spectral-minimax-rates)。

该仓库 `main` 当前 commit 为 `8294730f145f567cf1a103de482026c5d8001765`。其 README、`SOURCE_MANIFEST.md` 明确说明这是 clean-room reproduction，不是作者实现；树中没有论文 `.tex`、`.tikz`、`.pgf` 或原始绘图工程。仓库包含五个生成 PNG 和 `repro/src/experiments.py` 中的 Matplotlib 绘图函数，但源脚本参数/默认颜色与 PDF 图存在可见差异（例如 Figure 1 复现图有总标题，PDF Figure 1 没有；Figure 5 复现图标注 scale-reduced）。因此状态为 **partial_visual_source**：这些文件能支持指标和布局的独立重建，不能作为原作者 PDF 的 source-exact 证明。

可定位的源文件如下；行号为该仓库 `main` 树中 `gh api` 读取的文件范围：

- `repro/src/experiments.py:171–217`：`run_span_profile_experiment`，生成 Figure 1 复现图；Matplotlib，含 2×2 axes、log–log profile、`fig.savefig(..., dpi=170)`。
- `repro/src/experiments.py:268–359`：`run_depth_experiment`，生成 Figure 2 复现图；Matplotlib，三种 `D` 的 `errorbar` 曲线。
- `repro/src/experiments.py:468–496`：`run_linear_experiment`，生成固定设计 Figure 3 复现图；Matplotlib，ESD、oracle risk 和 MC scatter。
- `repro/src/experiments.py:515–578`：`run_rkhs_experiment`，生成 RKHS Figure 4 复现图；Matplotlib，bounds 与 MC risk。
- `repro/src/experiments.py:608–676`：`run_pathwise_experiment`，生成 learned-kernel Figure 5 复现图；Matplotlib，双 y 轴和 marker。
- `repro/src/spectral.py`：ESD、span profile、oracle risk 和 OP-GF 数值原语；用于复现数据，不包含原论文绘图样式。
- `outputs/v4/figures/figure1_span_profiles.png`、`figure2_depth.png`、`figure3_linear.png`、`figure4_rkhs.png`、`figure5_pathwise.png`：上述 clean-room 运行的 rendered assets，均为 PNG，不是论文 PDF 中嵌入的图源。
- `SOURCE_MANIFEST.md`：版本、论文对应关系及 clean-room 归属说明；不是绘图源。

## 论文级视觉系统

- **版式**：主文双栏；Figure 1 和 Figure 2 跨双栏。附录改为宽单栏数学版式；Figure 3 跨附录页宽，Figure 4 和 Figure 5 为居中的单图宽度。所有图下置 caption，图与周围正文留白充足。
- **图内字体**：PDF 对象使用嵌入的 `DejaVuSans`/`DejaVuSans-Oblique` Type 3 字体；Figure 1–2 的刻度/图例约 7–11 pt、面板标题约 13 pt，Figure 3 约 11–13 pt，Figure 4 约 15–17 pt，Figure 5 约 11–12 pt。caption/body 使用 `NimbusRomNo9L` 与 Computer Modern 数学字体，caption 约 9 pt。字号是 `pdftohtml -zoom 1` 的 PDF fontspec 对象值，不是由 220 dpi 像素反推的值。
- **字重与样式**：图内主标签和图例以 regular roman/italic 为主；数学变量使用 italic。Figure 3 caption 的标题 `Oracle PCR risk versus Effective Span Dimension` 使用 `NimbusRomNo9L-Medi`，其余 caption 主要为 italic Figure label + regular caption body。图内没有等宽体或 small caps。
- **颜色**：PDF 矢量对象使用 Okabe–Ito 风格类别色，包括蓝 `#0072B2`、橙 `#D55E00`、绿 `#009E73`、粉 `#CC79A7` 和黄 `#E69F00`；网格约 `#B0B0B0`，坐标/文字为黑色。Figure 1 用五色表示时间，Figure 2/3/5 复用蓝/橙，Figure 4 加入绿色。PDF SVG 路径中对应 RGB 百分比为 `#0072B2`、`#D55E00`、`#009E73`、`#CC79A7`、`#E69F00`，颜色值按 PDF 对象转换；以下对象的 `color.provenance` 仍标为 `rendered_estimate`，因为没有原作者 source file。
- **线与不确定性**：主曲线通常为 1.2 的 PDF stroke-width；网格为浅灰虚线。Figure 2–4 使用 error bar 表示 one standard error/standard errors；Figure 1、5 没有不确定性。只有 Figure 5 使用圆/方 marker，其他图依赖颜色和线型。
- **统计边界**：图表只呈现理论量、合成实验、Monte Carlo 均值和标准误；没有 conventional 95% interval、显著性标记或 Table 汇总。Figure 5 是单轨迹示意，不报告重复数。

## Figure 1（p. 8，主文 §6，`double_column`）

### 结构与绘图语法

Figure 1 是跨双栏的 2×2 line-plot grid，面板按 `q=1`、`q=1.5`、`q=2`、`q=3` 排列。每个面板都绘制五条 `d†(τ)` span-profile 曲线，颜色对应训练时间 `t=0,20,40,60,80`。x 轴为噪声水平 `τ` 的 log scale（约 `10⁻⁷`–`10⁻²`），y 轴为 ESD 的 log scale；底排显示 `τ` x-label，左侧/各面板显示 `d†(τ)` y-label。曲线是无 marker 的实线，图内无 grid、hatch、reference line 或 error bar。每个 panel 有独立图例：前三个大致位于左下，`q=3` 为避免遮挡置于右上。PDF 路径的主曲线 stroke-width 为 1.2。

- **类型/复杂度**：`line`；4 个 panel、每 panel 5 个 series、每 panel 5 个 legend item，复杂度 **3/5**（多 panel 和 log 轴，但编码单一）。
- **视觉颜色**：蓝 `#0072B2`=`t=0`，橙 `#D55E00`=`t=20`，绿 `#009E73`=`t=40`，粉 `#CC79A7`=`t=60`，黄 `#E69F00`=`t=80`。每条时间序列只用颜色区分，因此灰度可读性弱；`q=1` 的五条线几乎重叠，彩色线也难分。
- **PDF 字体对象**：`DejaVu Sans` regular 与 `DejaVu Sans Oblique` italic；fontspec 对象约 7 pt（指数）、9 pt（italic `t`）、11 pt（刻度和 legend）、12 pt（轴标签）、13 pt（panel title `q`）。

### 数据编码与 caption

- **编码**：`x=τ`（log）、`y=d†(τ)`（log）、`color=t`、`shape=null`、`line=五条 solid profiles`、`facet=2×2 q`、`text=q panel title + t legend`。
- **数据与统计**：固定参数为 `n=10000`、`σ₀=1`、`d=5000`、`J=15`、`p=2.5`、`γ=1`；`q` 从 1 到 3，span profile 沿训练时间 0/20/40/60/80 计算。Figure 1 是描述性单次轨迹/曲线，不报告 replication、均值、误差、失败值或聚合分母。正文解释 `q=1` 初始对齐好、几乎没有改进空间，而 `q>1` 的 profile 随训练向下移动。

**Caption（PDF 原文，45 词）**：

> *Figure 1.* Evolution of span profiles during the training of an over-parameterized gradient flow. The misalignment level *q* varies from 1 to 3. Fixed parameters are *n* = 10000, *σ*₀ = 1, *d* = 5000, *J* = 15, *p* = 2.5, and *γ* = 1.

Caption 动作：`title`、`setup`、`comparison`；没有显式编码 key、主发现或不确定性定义。它说明了对象、q 对比和固定参数，脱离正文可以辨识实验设置，但不能单独知道五种颜色对应的时间；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。

### 证据关系、优缺点与可复用范式

- **证据关系**：把 §5 的 OP-GF 学习谱机制连接到 §6 的 synthetic misalignment experiment；Figure 1 的 q/time profile 是 Figure 2 的 depth/ESD/error 结果之前的机制读数。正文 p. 7–9 将 `q=1` 的 negative/no-room-for-improvement panel 与 `q>1` 的 downward shift 直接解释为 alignment refinement；附录 D.2 再把 ESD 扩展成 evolving-kernel 的 pathwise descriptor。
- **优点**：2×2 facet 将错配程度和训练时间分离；log–log 轴适合跨数量级的 ESD/profile；固定参数直接置于 caption，读者可以把曲线变化归因于 q 与 t。
- **缺点**：五个时间点只用颜色编码，q=1 的重叠曲线几乎不可区分；图内 caption 没有说明 line/color key，读者需读取 legend 和正文；没有重复或误差，不能区分单次轨迹与稳定趋势。
- **可复用范式**：对谱/复杂度随噪声阈值变化的机制，使用 `2×2 facet = controlled alignment level`、`color = training checkpoint`、双对数轴，并把固定维度和信号参数压入 caption；若要提升可读性，应再加 marker 或线型冗余。
- **物理证据**：PDF p. 8；主图 bbox 约 `[79, 85, 532, 414]` pt，220 dpi 与 600 dpi render 均检查；对象页 caption bbox 约 `[55, 426, 506, 445]` pt。

## Figure 2（p. 8，主文 §6，`double_column`）

### 结构与绘图语法

Figure 2 是跨双栏的两个并排 line panels：左为 `Oracle PC squared error`，右为 `Effective span dimension`。两个 panel 的 x 轴都是 `Training time` 的 log scale（可见 `10¹`–`10⁴`），y 轴分别为 squared error 和 `d†` 的 linear scale。三条实线按 `D=0,1,3` 着色为蓝/橙/绿；每个点带竖向 error bar，但没有 marker。每个 panel 有独立的右上图例，网格为 x/y 两向的浅灰虚线。PDF 主曲线 stroke-width 为 1.2，error-bar 线较细。

- **类型/复杂度**：`line`；2 个 panel、每 panel 3 个 series、每 panel 3 个 legend item，复杂度 **3/5**。
- **PDF 字体对象**：`DejaVu Sans` regular/italic；fontspec 对象约 7 pt（指数）、9 pt（italic `D`）、11 pt（刻度/legend）、12 pt（轴标签）、13 pt（panel title）。
- **颜色与冗余**：`D=0` 蓝 `#0072B2`，`D=1` 橙 `#D55E00`，`D=3` 绿 `#009E73`；不同深度没有 marker 或线型冗余，灰度下仅靠曲线位置和 legend 区分，`redundant_encoding=false`、`grayscale_safe=false`。

### 数据编码与 caption

- **编码**：`x=training time`（log）、左 `y=oracle-PC squared error`（linear）、右 `y=d†`（linear）、`color=D`、`shape=null`、`line=three solid depth trajectories + error bars`、`facet=error/ESD`、`text=panel title + D legend`。
- **数据与统计**：每个曲线为 20 次 Monte Carlo replication 的平均值；error bar 为 one standard error。Figure 2 比较 `D=0,1,3` 随训练时间的 ESD 与 oracle-tuned PC estimator squared error。正文指出 `D=0` 初期下降更早，而充分训练后 `D=1/3` 可达到更低 ESD；caption 没有写 q、`n`、`d`、signal decay 或 stopping rule。

**Caption（PDF 原文，35 词）**：

> *Figure 2.* Averaged squared error of the oracle–tuned PC estimator and ESD as a function of the training time. Each average is computed based on 20 replications and each error bar represents one standard error.

Caption 动作：`title`、`setup`、`uncertainty_definition`；它定义均值、重复数和 error-bar 语义，但不定义 `D` 图例的含义或固定合成设置；`headline_bold=false`、`self_contained=true`（结合 panel title/legend）、`main_finding_stated=false`。

### 证据关系、优缺点与可复用范式

- **证据关系**：Figure 2 承接 Figure 1 的 OP-GF span-profile 机制，直接把 ESD 作为 oracle-PC truncation level，并将其与 estimation error 同步呈现；正文 p. 8–9 用它支持 depth sensitivity，但明确称一般模型的 comprehensive study 留待未来。没有 component-removal ablation；`D` 是深度敏感性对照，不应标成删除模块的 ablation。
- **优点**：并排的 error/ESD panels 用同一 x 轴形成机制—结果对照；20 次 replication 和 one-SE 使曲线波动可见；log training-time 轴展示了早期与后期下降速度差异。
- **缺点**：三种深度只靠颜色编码，error bars 在曲线密集处相互遮挡；caption 没有给 q 和完整实验参数，脱离正文不能复原比较条件；纵轴量级不同，读者需在两个 panel 间转换。
- **可复用范式**：把“复杂度代理 + 任务误差”按同一训练轴并排，并以同一类别色编码控制变量；caption 至少写出 replication、误差定义和所有改变的实验因素。
- **物理证据**：PDF p. 8；主图 bbox 约 `[79, 490, 532, 668]` pt，220 dpi 与 600 dpi render 均检查；caption bbox 约 `[55, 676, 506, 696]` pt。

## Figure 3（p. 19，Appendix B.4，`page_width`）

### 结构与绘图语法

Figure 3 是附录页宽的两个并排 line panels，分别对应 `(a)` geometric eigen-decay 和 `(b)` logarithmic eigen-decay。x 轴为变换强度 `α` 的 linear scale（左 0–30，右 0–10），但 plot 内没有独立的 `α` x-label，变量由 caption、正文和刻度共同确定；y 轴为 `ESD and risk · n/σ₀²` 的 linear scale。每个 panel 有蓝色实线 `ESD` 与橙色虚线 `Rescaled risk ± SE`；橙色曲线带竖向 error bar，无 marker。网格为双向浅灰虚线，图例位于每个 panel 的右下区域，PDF 主曲线 stroke-width 为 1.2、虚线为 PDF dash array `4.44 1.92`。

- **类型/复杂度**：`line`；2 个 panel、2 个 series、2 个 legend item，复杂度 **2/5**。
- **PDF 字体对象**：`DejaVu Sans` regular/italic；约 9 pt（公式小字号/legend）、11 pt（ticks/legend）、13 pt（轴标签）。caption 为 9 pt Nimbus Roman，标题使用 9 pt medium。
- **颜色与冗余**：ESD 蓝 `#0072B2`，rescaled risk 橙 `#D55E00`；颜色配合 solid/dashed line，`redundant_encoding=true`、`grayscale_safe=true`。

### 数据编码与 caption

- **编码**：`x=α`（linear）、`y={d†(α), nR*(α)/σ₀²}`（linear）、`color=ESD/risk`、`shape=null`、`line=solid ESD + dashed risk`、`facet=geometric/logarithmic decay`、`text=ESD 和 Rescaled risk ± SE legend`。
- **数据与统计**：Appendix B.4 固定 `σ₀²=1`、`n=300`、`p=400`；对 geometric 与 logarithmic 两种 spectrum/signal decay 施加非正交 `A(α)` 变换。蓝线是 `d†(α)`，橙虚线是 `nR*(α)/σ₀²`；risk 使用 20 次 replication，error bars 为 standard errors。图显示二者随错配强度大体同步上升，支持 Proposition B.2 的常数级关系。

**Caption（PDF 原文，44 词）**：

> *Figure 3.* **Oracle PCR risk versus Effective Span Dimension** for (a) geometric eigen-decay and (b) logarithmic eigen-decay. The dashed line plots Risk × *n*/σ₀²; the solid line is *d*†(*α*). The risk is computed based on 20 replications and the error bars represent standard errors.

Caption 动作：`title`、`setup`、`encoding_key`、`comparison`、`uncertainty_definition`；medium 字重标题直接写出比较对象，给出线型语义、重复数和误差定义；没有附录指针；`headline_bold=true`、`self_contained=true`、`main_finding_stated=false`。

### 证据关系、优缺点与可复用范式

- **证据关系**：Figure 3 是 Appendix B 对固定设计线性模型的扩展验证；它把正文 ESD—oracle spectral risk 关系接到 Proposition B.2，并以两种 spectrum/signal decay 做 robustness-style split。它不是新的 baseline 排名或学习算法效果图。
- **优点**：两种 decay case 采用同一 y 量纲与线型，易于比较 ESD 和 rescaled risk；risk 的 error bars 和 20-replication 分母写在 caption；solid/dashed 使灰度阅读仍可辨识。
- **缺点**：图内缺少 `α` x-label，x 变量依赖 caption/正文；两个 panel 的 x 范围不同（0–30 与 0–10），共享视觉宽度可能让斜率比较产生误读；曲线顶部接近饱和，caption 没直接写趋势结论。
- **可复用范式**：在理论扩展中以 side-by-side case panels 固定 y 量纲，用实线表示复杂度、虚线表示重标化风险，并把 replication/SE 定义写进 caption；不同 case 的 x-range 应显式标注。
- **物理证据**：PDF p. 19；图块 bbox 约 `[66, 70, 543, 243]` pt，220 dpi 与 600 dpi render 均检查；caption bbox 约 `[55, 260, 542, 278]` pt。

## Figure 4（p. 25，Appendix C.4，`single_column`）

### 结构与绘图语法

Figure 4 是附录中居中的单面板 line plot。x 轴为 misalignment severity `α` 的 linear scale，刻度 0–30；图内没有独立的 `α` x-label。y 轴是 `Risk and ESD-based bounds` 的 linear scale（0–约 1.2）。三条曲线为蓝色 dashed lower bound `(d†−1)σ₀²/n`、绿色 dotted upper bound `2d†σ_eff²`、橙色 solid empirical `Optimal KPCPE risk ± SE`；橙线带 error bar，无 marker。图例位于左上并直接显示公式，双向浅灰虚线 grid；主曲线 PDF stroke-width 为 1.2。

- **类型/复杂度**：`line`；1 个 panel、3 个 series、3 个 legend item，复杂度 **2/5**（单 panel，但公式图例和 bounds 较密）。
- **PDF 字体对象**：`DejaVu Sans` regular/italic；约 10 pt（公式下标）、13 pt（公式变量）、15 pt（刻度/legend）、17 pt（y-axis label）。caption 为 9 pt Nimbus Roman regular/italic。
- **颜色与冗余**：lower blue `#0072B2`、upper green `#009E73`、empirical orange `#D55E00`；颜色与 dashed/dotted/solid line 联合编码，`redundant_encoding=true`、`grayscale_safe=true`。

### 数据编码与 caption

- **编码**：`x=α`（linear）、`y={risk,bounds}`（linear）、`color=bound type/risk`、`shape=null`、`line=dashed lower + dotted upper + solid risk`、`facet=null`、`text=formula legend + y-axis label`。
- **数据与统计**：Appendix C.4 固定 cosine basis、`x∼Unif[0,1]`、`n=400`、`J=800`、`σ₀²=1`，仅变换前 `D=80` 个 eigenvalues 的 severity `α`。橙线为 oracle-tuned KPCPE risk 的 Monte Carlo 均值，10 次 replication；error bar 为 one standard error。蓝/绿线是 ESD-based lower/upper bounds；风险曲线位于两条 bound 之间并随 α 增大。

**Caption（PDF 原文，64 词）**：

> *Figure 4.* Optimal KPCPE risk and ESD-based bounds. The blue dashed curve plots the lower bound (*d*†(*α*) − 1)σ₀²/*n*. The green dotted curve plots the ESD-based upper curve 2*d*†(*α*)(σ₀² + ‖*f*∗‖∞²)/*n*. The orange curve with error bars plots the Monte Carlo estimate of the risk of the oracle–tuned KPCPE. The risk is averaged over 10 replications, and the error bars represent one standard error.

Caption 动作：`title`、`setup`、`encoding_key`、`comparison`、`uncertainty_definition`；它定义三种颜色/线型、公式、Monte Carlo、replication 和 SE，可脱离正文辨识 bound 关系；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。

### 证据关系、优缺点与可复用范式

- **证据关系**：Figure 4 是 Appendix C.4 对 RKHS/KPCPE extension 的 bound sandwich；它调用 Proposition C.4，并对应正文对 ESD framework 跨到 RKHS 的说明。橙色经验风险、蓝色下界和绿色上界形成“理论界—经验风险”闭环，不承担 learned-kernel 的直接比较。
- **优点**：一张图同时显示上下理论界和经验 risk，线型冗余使关系在灰度下仍清楚；公式写在 legend 中，读者无需反复查正文；error bars、10 次 replication 和 SE 定义完整。
- **缺点**：x 轴缺 `α` 标签，只能从 caption/正文得知；公式 legend 占据左上图内空间，容易与高位绿色曲线和网格竞争；upper bound 的量级明显高于 empirical risk，y 轴的大空区降低下方差异的可读性。
- **可复用范式**：对理论不等式与经验估计，使用同轴的 lower/upper/risk 三线图，给理论线以 line-style、给估计线以 error bar，并在 legend 直接写 bound 公式；同时保留 x 变量和单位标签。
- **物理证据**：PDF p. 25；图块 bbox 约 `[190, 70, 441, 296]` pt，220 dpi 与 600 dpi render 均检查；caption bbox 约 `[55, 322, 543, 352]` pt。

## Figure 5（p. 27，Appendix D.2，`single_column`）

### 结构与绘图语法

Figure 5 是附录单面板的双 y-axis line plot，x 轴为 `Epoch` 的 linear scale（0–500）。左 y 轴蓝色 `ESD`，右 y 轴橙色 `Risk`；蓝线使用圆形 marker，橙线使用方形 marker，二者均为实线。图例位于右上，grid 为双向浅灰虚线；无 error bar、band、reference line 或 distribution。PDF 主曲线 stroke-width 为 1.2；左右 y-label 与相应曲线颜色一致。

- **类型/复杂度**：`line`；1 个 panel、2 个 series、2 个 legend item，复杂度 **2/5**（双 y 轴和 marker 增加解释负担）。
- **PDF 字体对象**：`DejaVu Sans` regular；约 11 pt（ticks/legend）、12 pt（轴标签）；左/右 y-label 为同一字体并分别使用蓝/橙色。caption 为 9 pt Nimbus Roman regular/italic。
- **颜色与冗余**：ESD 蓝 `#0072B2` + circle，Risk 橙 `#D55E00` + square；`redundant_encoding=true`、`grayscale_safe=true`，但双 y 轴的颜色仍是重要导航。

### 数据编码与 caption

- **编码**：`x=epoch`（linear）、左 `y=ESD`（linear）、右 `y=parameter risk`（linear）、`color=ESD/Risk`、`shape=circle/square`、`line=two solid trajectories`、`facet=null`、`text=colored axis labels + legend`。
- **数据与统计**：Appendix D.2 的论文设置为 random-design linear regression，`p=900`、`n=1000`、`β_j*=j^{-1.1}`（`j≤200`）、`σ₀=0.1`、4-layer linear network、full-batch Adam、learning rate `10⁻⁴`。图在一条训练轨迹上同时绘制 pathwise `d†(t)` 和 `‖A(t)^⊤w(t)−β*‖₂²`；没有 replication、均值、error bar 或 uncertainty。曲线从早期到后期都下降，末段约在 ESD 50、risk 0.1 附近平台。

**Caption（PDF 原文，15 词）**：

> *Figure 5.* Pathwise ESD and risk under a learned kernel using a 4-layer linear network.

Caption 动作只有 `title`；没有 setup、编码 key、比较、uncertainty 或 appendix pointer；它能识别对象主题，但不能独立解释双轴 risk 定义、训练设置或单轨迹边界；`headline_bold=false`、`self_contained=false`、`main_finding_stated=false`。

### 证据关系、优缺点与可复用范式

- **证据关系**：Figure 5 连接 Appendix D.2 的 pathwise ESD 定义、deep-linear learned kernel 构造和 evolving-eigenfunction 的开放边界。正文/附录明确把它定位为 illustrative evidence，并用它支持 ESD 追踪 signal–kernel alignment；这不构成 evolving-eigenfunction 的一般定理。
- **优点**：双轴把复杂度与 parameter risk 放在同一训练轨迹，circle/square marker 为颜色提供冗余；单面板和短轨迹容易看到同步下降及平台。
- **缺点**：双 y 轴可能让两条曲线的垂直斜率被误读为可直接比较；没有 replication/error bars，无法判断单条 Adam 轨迹的稳定性；caption 没有说明两个 y 轴的 risk 公式、`p/n/depth` 或 near-identity 初始化。
- **可复用范式**：在 evolving-kernel 机制只具 pathwise 证据时，用双轴轨迹展示 descriptor 与 task risk 的同步变化，并用不同 marker/轴色保持可读性；caption 应显式标记“single trajectory/illustration”及实验规模。
- **物理证据**：PDF p. 27；图块 bbox 约 `[161, 70, 440, 251]` pt，220 dpi 与 600 dpi render 均检查；caption bbox 约 `[55, 260, 454, 270]` pt。

## 表格与附录对象核对

- **Tables**：PDF p. 1–73 没有 `Table`/`Tab.` 标签、表头、booktabs/grid table、cell highlight、跨页表或表格图片；JSON `tables=[]`，`paper_style.main_tables=0`、`appendix_tables=0`。
- **附录对象分布**：Appendix A（p. 13–15）为 related work；B（p. 15–19）含 Figure 3；C（p. 19–25）含 Figure 4；D（p. 25–27）含 Figure 5；E–I（p. 27–73）为证明、应用和 ridge 讨论，没有额外 Figure/Table。逐页 180 dpi render 和全文文本检查未发现隐藏对象。
- **调用边界**：附录 B/C 的图把 ESD—risk 关系扩展到 fixed-design linear/RKHS；附录 D 的图把 pathwise descriptor 扩展到 learned kernel。证明附录 E–G/H/I 没有图形性总结或表格性汇总，读者需要从公式和正文回读对象关系。

## 跨对象系统判断

1. **视觉叙事**：Figure 1 先展示 q/time 下 span profile 如何变化；Figure 2 把同一 OP-GF 过程连接到 depth、ESD 和 oracle-PC error；Figure 3/4 在附录中分别验证 fixed-design PCR 与 RKHS bound；Figure 5 最后给出 evolving learned-kernel 的 pathwise illustration。整体为 `mechanism → main empirical comparison → cross-model bound checks → pathwise extension`。
2. **Caption 系统**：五个 caption 都用 italic `Figure n.` 起头。Figure 1/2/4/5 的标题正文为 regular，Figure 3 用 medium/bold 结论标题。Figure 1 固定参数最完整；Figure 2–4 明确 replication/SE；Figure 5 极短且没有不确定性或规模信息。仅 Figure 3 的 caption 同时把比较对象作为加粗标题，其他 caption 通过正文补主发现。
3. **表头系统**：无表格，因此没有指标方向、单位、模型/任务分组、成本列、失败值、best/second-best，也没有把性能、成本和失败放在同一决策视图。
4. **方法、结果与消融链接**：Figure 1 的 q 是 alignment sensitivity，Figure 2 的 D 是 depth sensitivity。二者都不是 component-removal ablation。Figure 3/4 是理论扩展的 risk/bound validation，Figure 5 是 learned-kernel pathwise mechanism。论文没有组件替换、baseline 排名或成本实验。
5. **正文—附录链接**：主文 Figure 1–2 由 §5–§6 的 OP-GF 条件、ESD 定义和实验段落调用；Appendix B.4 Figure 3、C.4 Figure 4、D.2 Figure 5 由各自扩展段落调用。附录 E–G/H/I 补充证明和条件，但没有追加 visual slices 或完整结果表。
6. **字体与颜色一致性**：所有图内 plot text 均为 DejaVu Sans，主曲线均 1.2 PDF stroke-width；蓝/橙/绿在图间维持 ESD/risk/bound 的大体语义，Figure 1 额外用粉/黄表示时间。附录 Figure 4 字号显著大于其他图，适应单图缩放但削弱跨图字号统一；Figure 5 用橙色 risk 与 Figure 3/4 风格一致，但其右轴导航依赖颜色。

## 最终判断

- **最可复用模式**：
  1. 用 `controlled facet = alignment/depth lever`，把一个机制量（ESD/span profile）与训练时间或错配强度分离，并保持 log/linear 轴与数据量级匹配。
  2. 用并排的 `complexity proxy ↔ estimator risk` 面板或同轴 bounds sandwich，把理论量、经验均值和 SE 放在同一证据链上。
  3. 对 evolving-kernel 只有 pathwise 证据的场景，使用双 y 轴 + marker redundancy 展示 descriptor 与 parameter risk 的同步轨迹，同时在 caption 写清 single-trajectory 边界。
- **最高价值对象**：Figure 1（p. 8）把 alignment、q、training time 和 ESD profile 组织成主机制接口；Figure 2（p. 8）以 20-replication SE 对照 depth、ESD 与 oracle-PC error；Figure 4（p. 25）最直接地把 empirical KPCPE risk 放在 ESD lower/upper bounds 之间。
- **失败模式**：Figure 1/2 只用颜色区分多条系列，灰度和重叠曲线不友好；Figure 1、3、4 的 x 变量 `τ/α` 在部分 panel 中依赖 caption/正文而缺少独立 x-label；Figure 2 caption 缺 q 和固定设置；Figure 5 是无不确定性的单轨迹双轴图且 caption 信息不足；全文没有表格、成本、失败或 baseline 汇总；公开严格匹配仓库是 clean-room reproduction，缺少原作者 plotting/LaTeX source，不能 source-exact 复原 PDF。
- **一句话视觉策略**：先用 q/time span-profile facets 暴露谱—信号对齐机制，再用 depth 对照和 error/ESD 并排读数闭合主文证据，最后以 fixed-design、RKHS bounds 和 learned-kernel pathwise 图扩展同一 ESD 叙事，同时把单轨迹和缺失表格作为明确边界。

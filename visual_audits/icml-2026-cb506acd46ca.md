# DiScoFormer：视觉审计

## 审计边界与事实源

- **paper_id**：`icml-2026-cb506acd46ca`
- **PDF 事实源**：`corpus/preprints/icml-2026-cb506acd46ca.pdf`；`pdfinfo` 显示 21 页、Letter、612×792 pt。PDF 标题为 *DiScoFormer: Plug-In Density and Score Estimation with Transformers*，作者为 Vasily Ilin、Peter Sushko、Ranjay Krishna。
- **读取边界**：逐页检查物理页 1–21，包括正文、参考文献、附录和嵌入附录；没有单独 supplementary PDF。正文视觉对象位于物理页 3–9，附录视觉对象位于物理页 18–21；物理页 10、11–17 没有新的 Figure/Table。
- **渲染检查**：使用 `pdftoppm -r 200 -png` 将全部 21 页渲染为 PNG（200 dpi，满足至少 180 dpi），先检查全页接触表，再逐页检查含对象页面及物理页 21。字体对象用 `pdffonts`、嵌入图像用 `pdfimages -list` 辅助核对；视觉尺寸、颜色、字号和线宽均在没有绘图源时标为 rendered estimate。
- **PDF 清单对齐**：PDF 中共有 **15 幅 Figure、6 张 Table、1 个 Algorithm**。reading 的 `visual_inventory` 与 PDF 的 Figure/Table 标签和页码一致；Algorithm 1（物理页 5）已检查但不进入 schema 的 `figures`/`tables` 数组，并在方法段落中记录。
- **页码语义**：下文 `page` 均为 PDF 物理页码，不是印刷页脚重复计数。

## 源码与视觉源核查

1. 首页、正文、参考文献和 reading：PDF 未给出代码仓库链接；reading 给出 arXiv PDF `https://arxiv.org/pdf/2511.05924` 和 OpenReview `https://openreview.net/forum?id=gyOWJpP8cQ`，没有 supplementary 文件。
2. `reports/tables/visual_source_inventory.csv` 的目标行仍为 `no_public_source_found`，没有 repository 字段；`reports/tables/visual_source_files_local.csv` 没有目标行；`corpus/visual_sources/icml-2026-cb506acd46ca/` 不存在。
3. 使用 `agent-reach doctor --json`：GitHub backend 为 `warn`（检测到认证配置但 doctor 不自动执行会写 device-id 的认证检查）；随后用 `gh` 完整标题/方法名搜索。GitHub 找到直接匹配候选 **`celerychen/discoformer`**：描述明确写明实现该论文，README 直接链接论文题目和 arXiv:2511.05924v2。
4. `unicli scholar code` 用完整标题通过 github-scholar 返回同一仓库，`match_type=title_exact`、`relationship=candidate-implementation`、`confidence=0.98`，并标为非官方代码；`gh api` 核对候选默认分支为 `main`、公开、未归档，树包含 `discoformer.py`、`test_discoformer.py`、`README.md`、`score_comparison_2d.png` 以及模型权重和论文 PDF。按协议未克隆权重、数据或完整仓库；只读取 README、实现/测试脚本的相关片段、树和 PNG 元数据。该仓库只有一个测试生成的 2D 分数场 PNG（Matplotlib 3.10.8、150 dpi），没有 `plot*`/`figure*`/`visual*`/`table*` 脚本、TeX/TikZ/PGF、notebook 或样式文件。PNG 是两个并排的简单分数场，与论文 Figure 3 的单个多色 quiver 图不相同，不能作为论文 Figure 3 的精确重绘源。
5. 因而 `source_acquisition.status` 记为 `partial_visual_source`：仓库与论文的关系直接成立，并有一个相关 rendered asset，但不存在能逐对象重建论文 Figure 1–15/Table 1–6 的视觉源；`score_comparison_2d.png` 作为 `rendered_asset` 记录，不能把论文 PDF 的颜色、字号、线宽或数值误标为 source exact。

## PDF 对象清单

| 对象 | 物理页 | 模块 | PDF 中的构成/职责 |
|---|---:|---|---|
| Table 1 | 3 | method | 变换类型与仿射等变误差 |
| Figure 1 | 3 | method | 平均注意力、KDE 矩阵、相关散点、head 专门化 |
| Figure 2 | 4 | method | 仿射等变 forward-pass 代码框 |
| Algorithm 1 | 5 | method | GMM DataLoader 训练数据生成；已检查，不入 JSON |
| Figure 3 | 6 | results | 2D score field：Scott KDE/Transformer/true |
| Figure 4 | 6 | results | 维度/样本量和 mode 数量的两面板 MSE 曲线 |
| Table 2 | 6 | results | d=2、d=10，n 外推和 OOM |
| Table 3 | 7 | results | 2D Laplace score MSE |
| Table 4 | 7 | results | 2D Student-t、TTT 步数 |
| Figure 5 | 7 | results | Laplace score MSE 与 TTT |
| Table 5 | 7 | results | d=100 score/log-density MSE |
| Table 6 | 7 | ablation | whitening 的 ID/OOD 消融 |
| Figure 6 | 8 | results | relative Fisher information 的 cross-attention 估计 |
| Figure 7 | 9 | results | 五种 2D density heatmap 定性比较 |
| Figure 8 | 9 | results | 1D bimodal GMM density 曲线 |
| Figure 9 | 9 | results | 1D/2D density MSE scaling |
| Figure 10 | 9 | results | entropy/Fisher information 的 2×2 scaling |
| Figure 11 | 9 | results | Landau 方程 covariance 的三面板轨迹 |
| Figure 12 | 18 | appendix | layer-0 八个 head 的完整注意力矩阵 |
| Figure 13 | 19 | appendix | 三组 query 情形下八个 head 的注意力散点 |
| Figure 14 | 20 | appendix | sliced score matching 与 Transformer |
| Figure 15 | 21 | appendix | d=2/d=10 runtime 与 OOM |

## 论文级视觉系统

论文采用 Letter 双栏版式，正文和 caption 以 Nimbus Roman/Times-like serif 为主，数学使用 Computer Modern 系列；代码框使用 Nimbus Mono 等宽体。caption 通常是 8–9 pt 左右的 serif italic label 加 roman 正文，图内 Matplotlib 风格文字约 7–10 pt，具体字号仅可由渲染估计。表格以黑色 booktabs/minimal 横线、无竖线为主，数字右对齐；最佳项以粗体标记。图像对象大多是 RGB 栅格嵌入，方法代码和表格、文字为 PDF 向量，整体为 mixed vector/raster。

颜色策略以 viridis 类连续色标（深紫—蓝绿—黄）表达 attention/density 强度，另用 Matplotlib 的蓝、橙、红、绿、紫、青区分方法或曲线。颜色在热图中语义稳定，但多数曲线未提供线型/marker 的完全冗余编码，许多对象不能仅靠灰度安全解码。正文视觉叙事按“等变接口与 attention–KDE 机制 → score 主比较与外推 → TTT/high-dimensional/whitening → Fisher/SD-KDE/entropy/PDE → 附录机制、score matching 与成本”展开；Figure 1/12/13 是机制链最强的可视证据，Table 2/5/6、Figure 4/5/15 承担数值、鲁棒性和成本边界。

## 逐对象审计

### Table 1（物理页 3，method）

- **几何与表头**：左栏上方的单栏窄表；6 个数据行、2 列（`Transform`、`Rel. MSE`）、单层表头、无 row group。上/表头下/底部三条主要横线，横线极简、无竖线。数据依次为 Permutation、Translation、Isotropic scaling、Anisotropic scaling、Rotation、Full affine；数值为 0、0、0、0、5×10⁻⁴、1×10⁻⁴。
- **设计/排版**：黑色 vector serif，表头与正文同一字号附近，列间距宽松；科学计数法用数学字体。没有颜色、箭头、下划线或不确定性列。
- **数据与统计**：指标是 affine-equivariance error 的 relative MSE，caption 明确是 50 trials 的平均；没有 SD/SE、重复分布或失败值。它把 exact translation/scaling 与 residual rotation/full-affine error 放到同一决策面。
- **caption/header**：原文为 “Table 1. Relative MSE of affine equivariance error, averaged over 50 trials.”（词数 12）。动作：title、setup、uncertainty_definition（仅定义聚合次数，不提供离散度）；不是粗体结论标题，未在 caption 直写结论，脱离正文可理解指标但不知具体变换为何重要。
- **evidence relation**：连接 Proposition 3.1/Remark 3.2 的“白化后平移和尺度精确、旋转近似”主张；与 Figure 2 的 whitening forward pass 对应，作为 Figure 1 attention 机制之前的接口验证，并被 Limitations 的 rotation equivariance 边界调用。
- **优点**：行标签完整、误差尺度直接可比较；极简横线适合窄栏。
- **弱点**：单一均值掩盖试验间变异，`Rel. MSE` 未在表内解释分母；没有 precision/实验维度列，读者需回正文。
- **可复用模式**：用变换类型作行、统一 error metric 作列，并以少量横线呈现等变性检查；若用于最终论文，应补充聚合离散度或在表头/脚注定义分母。

### Figure 1（物理页 3，method）

- **几何与 panel**：右栏的大型单栏复合图，9 个可辨识 panel：顶部 1 个 `Score comparison n=1000` 2D quiver/scatter；中部 2 个注意力矩阵 heatmap；其下 2 个相关散点（标题 `corr=0.930`、`corr=0.841`）；底部 4 个 head scatter（Head 0、1、2、5）。阅读方向由上到下、由左到右；colorbar 大多贴近 panel。PDF 嵌入为多张 RGB 栅格图，文字/框线混合为 vector/raster。
- **plot grammar**：顶部 x/y 为 linear（约 −3–3/−4–3），heatmap 的 query/key 为索引轴，相关图为连续 linear，底部 head 图为 2D linear；heatmap 有网格状像素但无独立网格线，散点/箭头图有轻网格。顶部与底部有 legend；顶部 legend 位于左下，相关散点无 legend，底部以 head 标题直接标识；没有 shared legend、hatching 或 uncertainty band/error bar。顶部约 4 种箭头/点语义，heatmap 2 种，底部每 panel 1 个 attention scalar 映射。
- **编码**：x/y 是二维样本坐标或 query/key 索引；红/蓝/绿箭头区分 true/predicted/KDE score，点的位置是 GMM sample，黑色叉是 means，红色叉是 chosen point；attention scalar 用 viridis 连续色标，热图亮度对应矩阵权重，相关图用点云表达 agreement；panel/facet 表达 average/layer/head。
- **颜色与字体**：约 6 个主要颜色，连续 viridis（估计 `#440154`、`#21918C`、`#FDE725`）叠加红 `#D62728`、蓝 `#1F77B4`、绿 `#2CA02C`；颜色语义跨子图不完全统一，红/蓝/绿没有全套形状冗余，因此灰度安全性为 false。图内无源代码可核对字号；标题和轴标签为 rendered estimate，约 7–9 pt。
- **caption**：原文为 “Figure 1. Attention visualization. Top: average attention in layer 0 from query x; heatmaps show the attention matrix and the normalized KDE matrix Dᵢⱼ ∝ e^(−∥xᵢ−xⱼ∥²/2), and scatter plots show very high agreement. Bottom: individual heads exhibit emergent specialization (close-range, far-range, directional).”（词数 42，公式按一个 token 计）。动作：title、setup、encoding_key、comparison、main_finding；未粗体结论标题；直接写出 agreement 和 specialization，脱离正文可大致理解，但 layer/归一化约定仍依赖 Section 3。
- **数据与统计**：n=1000 GMM sample；top legend 给 Transformer MSE=0.0366，热图比较 layer-0 average attention 与 normalized KDE，散点给两种相关系数；没有误差条或重复聚合，相关系数/MSE 作为 panel 标题或 legend inline statistic。
- **evidence relation**：由 Proposition 3.3–3.6 的 attention-as-reweighted-Gaussian/KDE 结论通向经验验证；Figure 2 是接口实现，Table 1 是等变性前提，Appendix Figure 12/13 扩展 layer-0 全 head 矩阵和 query-conditioned scatter，Conclusion 再引用多尺度 kernel-like behavior。
- **优点**：把矩阵、相关性和空间 head behavior 放在一个可追踪的机制面；chosen point、means、MSE/correlation 让抽象 attention 对象可落到数据。
- **弱点**：9 panel 信息密度高，底部 head 子图尺寸小；两个相关 panel 的轴/层名需放大才能读，热图色标未统一显式标注；不同语义共用相似连续色阶，颜色之外缺少冗余编码。
- **可复用模式**：采用“全局 score field → attention/KDE 矩阵 → agreement statistic → individual-head spatial specialization”的机制复合图；正式版应统一色标范围、显式写出 layer/head 及 query 采样条件，并给 panel 编号。

### Figure 2（物理页 4，method）

- **几何与类型**：左栏上方的单栏代码框/inset，1 个 panel；灰白底、细灰边框、等宽字体，内容是 `forward(self, X, Y)` 的中心化、scatter、逆平方根白化、core、`logdet` 与 score 变换。
- **plot grammar/编码**：无 x/y、legend、grid、marker 或统计轴；这是 code screenshot + conceptual_diagram，颜色是语法高亮（洋红 keyword、青色/蓝色 identifier、灰黑 operator），流程由代码顺序表达。PDF 对代码字符和边框为 vector，属于 mixed。
- **caption**：原文为 “Figure 2. The forward pass implementing affine equivariance.”（词数 8）。动作：title、setup；不粗体结论、不定义颜色、不直接陈述结果；脱离正文仅能知道主题，`self._core`、`matrix_sqrt_inv` 和坐标变换含义由紧随其后的正文解释。
- **数据与证据关系**：没有数据统计；它把 Proposition 3.1 的 permutation/affine equivariance 接到可实现接口，并为 Figure 1 的 attention 机制和 Table 1 的变换误差提供 architectural origin。Algorithm 1 在下一页补训练数据生成。
- **优点**：将数学变换压缩成可复现的 forward-pass 顺序，代码框比纯箭头示意更精确。
- **弱点**：没有输入/输出 shape、分支标识或显式 `density`/`score` 标签；小字号和正文段落并置时，图和解释分离。
- **可复用模式**：对含有关键不变量的模型，使用短代码框展示 normalization、core 和 inverse transform；应在图内补 shape/语义 callout，避免把 caption 之外的解释当成图例。

### Figure 3（物理页 6，results）

- **几何与 panel**：左栏大单栏 2D score-field quiver，1 个 panel，标题 `Score comparison n=1000`；x/y linear，约 x∈[−3,3]、y∈[−3,3]，有方格网。大量短箭头覆盖 GMM sample，legend 在右上；红、蓝、绿三套箭头对应 True、Transformer、KDE，右上 color/attention 不单独使用。
- **plot grammar**：`other` + `scatter`/quiver；linear/linear；grid=both；legend=true，placement=upper right，shared=false；marker 主要是箭头与小点，line style 约 1–2，reference line=0，uncertainty=none。渲染是 mixed（RGB 图嵌入、文字和轴框 vector）。
- **编码与颜色**：箭头方向/长度表达 negated score vector，红/蓝/绿表达 true/Transformer/KDE；半透明点是 sample，黑色/红色特殊点和 legend 解释 context。估计颜色 `#F8766D`、`#619CFF`、`#00BA38`，约 5 色，categorical；颜色有少量语义冗余（legend 文本），但形状/线型冗余不足，灰度安全 false。
- **caption**：原文为 “Figure 3. Score estimation comparison between Scott KDE (Scott, 2015) and our transformer model. The transformer is more accurate, especially in the sparse regions. We plot the negated score for easier viewing.”（词数 32）。动作：title、comparison、main_finding、encoding_key；不粗体结论；明确 Scott KDE、稀疏区域、negated score，脱离正文可理解。
- **数据与统计**：2D unimodal Gaussian，n=1000；legend 显示 Transformer MSE=0.0077、KDE MSE=0.1528，caption 不写 uncertainty。MSE 是单次可视比较，没有重复/分母说明；Table 2 和 Figure 4 承担跨 n/d 的量化扩展。
- **evidence relation**：它是“预训练 operator 比 KDE 更准”主张的第一个直观结果，承接 Figure 1 的 score/attention 机制，连接 Figure 4/​​Table 2 的 scaling 与正文 Section 4.1；附录 Figure 15 则检查成本而非精度。
- **优点**：在一张空间图中同时展示方向、稀疏区域误差和比较 MSE，直观支持 caption 结论。
- **弱点**：箭头密度高，红蓝绿重叠后难以逐点判别；没有误差分布、重复试验或 sparse-region 的明确区域标记；MSE 只在 legend 里出现。
- **可复用模式**：用真实/模型/KDE 三色 score field 作为 qualitative-to-quantitative bridge；更稳健的版本应降低箭头密度、给 error magnitude 或局部 inset，并提供重复统计。

### Figure 4（物理页 6，results）

- **几何与 panel**：左栏下方单栏宽复合图，2 个并排 line-chart panel。左 panel 是 `MSE Loss Comparison (Transformer vs KDE)`，4 条线（Transformer d=1/d=10、KDE d=1/d=10）；右 panel 是 `MSE Loss d=10`，7 条 mode-count 曲线（1、4、7、10、13、16、19 modes）。两 panel 都有标题、图例、marker 与网格。
- **plot grammar**：x 为 `n (log scale)`，y 为 MSE 且视觉上为 log scale；grid=both；每 panel 独立 legend，左下/右上附近；line+marker，约 4/7 series，marker 约 2 种，line style 以实线为主；无 band/error bar/hatching，reference line=0。RGB 图嵌入与 PDF caption/边框混合。
- **编码/颜色**：x 是 sample size，y 是 score MSE；左以颜色区分模型和 dimension，右以 viridis/彩色序列区分 mode count。估计颜色约 `#F8766D`、`#E69F00`、`#56B4E9`、`#0072B2` 和多级 categorical；legend 是唯一语义 key，灰度安全 false。
- **caption**：原文为 “Figure 4. Left: MSE of score estimation in dimensions 1 and 10 on a 3-modal GMM using Transformer and KDE. The Transformer has excellent scaling in both dimension d and the sample size n. Right: MSE of score estimation using the Transformer on GMMs with different numbers of modes. Despite being trained only on GMMs with 1-10 modes, and n = 2048, the model exhibits excellent generalization.”（词数 67）。动作：title、setup、comparison、encoding_key、main_finding；直接写 scaling/generalization；脱离正文大致自洽，但训练范围语义需要 caption 的文字。
- **数据与统计**：左是 3-modal GMM 的 score MSE，d=1/10、多个 n；右是训练 mode 1–10、固定 n=2048、测试到 19 modes；没有不确定性或重复摘要。Table 2 给出更大 n 的精确值，Table 3/4 给非高斯分布。
- **evidence relation**：把 Figure 3 的单点比较升级为 dimension/sample-size/mode-count scaling，支撑 abstract 的 cross-distribution/sample-size claim；右 panel 的 OOD mode 泛化与 Table 4 的 TTT OOD、Table 6 的 whitening OOD 互补。
- **优点**：左右 panel 将效率维度与分布复杂度维度分开，横轴对数化后能看到多数量级趋势。
- **弱点**：左、右 y 轴/训练范围依赖 caption 和正文，曲线较多且颜色近似；没有置信带，`excellent` 是趋势判断而非 uncertainty-aware 结论。
- **可复用模式**：并排放“尺度外推”和“结构复杂度外推”两个 panel；用 caption 明确训练域与测试域边界，并在表格中补关键端点。

### Table 2（物理页 6，results）

- **几何与表头**：右栏上方单栏窄表；6 个数据行（n=2⁸、2¹⁰、2¹²、2¹⁴、2¹⁶、2¹⁷）、5 列。两层表头：第一层把四个数值列按 d=2、d=10 分组，第二层为 `Ours`/`KDE`；`n` 跨层。上、分组下、表头下、底部为极简横线，无竖线。d=2 Ours/KDE 为 14.67/43.8、8.80/33.6、7.24/24.6、6.80/17.2、5.35/OOM、5.41/OOM；d=10 为 7.49/65.6、4.65/61.3、3.32/57.1、2.83/52.9、2.80/OOM、2.74/OOM。
- **数据/统计**：relative score MSE (%)，归一化到 zero predictor=100%（正文定义）；训练 n∈[2⁸,2¹⁴]，最后三行是外推；KDE 在单张 48GB L40S 上超出 2¹⁴ 后 OOM。没有 SD/SE、rank 或重复范围；OOM 是明确 failure value。
- **caption/header**：原文为 “Table 2. Relative MSE (%) of score estimation on GMMs. The Transformer was trained with n ∈ [2⁸, 2¹⁴], so the last three rows probe extrapolation past the training range. KDE encounters OOM past n = 2¹⁴ on a single 48GB L40S.”（词数 42）。动作：title、setup、comparison、uncertainty_definition（无不确定性；定义归一化/失败条件）、abbreviation_definition（OOM）；未直写 Transformer 更优，脱离正文可理解表头但需正文解释 zero predictor。
- **证据关系**：Figure 4 左 panel 的曲线端点和正文 Section 4.1 的外推叙述的精确锚点；同时把 accuracy 与 memory failure 放同一决策面，为 Figure 15 的 runtime/memory 成本铺垫。
- **优点**：d 与 method 交叉分组清晰，外推行和 OOM 直接可读；精度和失败条件并列。
- **弱点**：Ours/KDE 的小数精度不一致（2 位 vs 1 位）；没有平均次数/seed 或离散度；OOM 的硬件条件只在 caption，阅读表格本身不完整。
- **可复用模式**：用双层表头展示 dimension×method，并在同一表中保留 OOM；最好统一精度、增加 eval repetition/硬件脚注。

### Table 3（物理页 7，results）

- **几何与表头**：左栏上方单栏表，4 个数据行（n=512、1024、2048、4096）、3 列（`n`、`KDE`、`Transformer`）、单层表头、无 row group；booktabs/minimal 横线，无竖线。Transformer 列粗体：0.3598、0.2992、0.2756、0.2597；KDE 为 0.3810、0.3305、0.2990、0.2650。
- **数据与统计**：2D Laplace 的 score MSE；每个 n 一个点值，无误差、重复、分母或失败标记。四位小数一致。
- **caption/header**：原文为 “Table 3. MSE of score estimation on the 2D Laplace distribution.”（词数 11）。动作：title、setup、comparison（由列名给出）；不粗体结论，不定义 uncertainty；脱离正文可读但不说明训练域/TTT。
- **证据关系**：正文从 GMM 转向非高斯 Laplace 的第一张精确表，与 Figure 5 的 TTT 曲线和 Table 4 的 Student-t/TTT 对照，支持“仅 GMM 训练仍能估计非高斯 score”的鲁棒性主张。
- **优点**：小表低认知负担，粗体让逐行优胜快速可见，四位精度一致。
- **弱点**：粗体规则未在 caption 声明；没有 TTT/seed/区间，单表不能支持稳定性。
- **可复用模式**：对单一 OOD 分布使用 n×baseline/model 窄表，保持统一小数位并在 caption 说明 best/highlight 规则。

### Table 4（物理页 7，results）

- **几何与表头**：左栏中部单栏表，4 个 n 行、6 列（`n`、`KDE`、`No TTT`、`TTT 4`、`TTT 6`、`TTT 8`）、单层表头、无 row group；横线为 minimal/booktabs，无竖线。每行 best 粗体：n=128 为 TTT 8 0.1450，256 为 TTT 8 0.0897，512 为 TTT 6 0.0485，1024 为 TTT 8 0.0765。
- **数据与统计**：2D Student-t ν=3 的 score MSE；数值均四位小数，无误差或 failure。比较 TTT 步数和 KDE，TTT 的跨 n 最优步数并不固定。
- **caption**：原文为 “Table 4. MSE of score estimation on the 2D Student-t distribution (ν = 3).”（词数 14）。动作：title、setup、abbreviation_definition（TTT 在正文定义但 caption 仅缩写）；未直写 best 结论，脱离正文可理解分布和指标但不知 TTT 学习规则。
- **证据关系**：与 Figure 5 同一 TTT OOD 论证；Table 3 给 Laplace baseline，Table 6 将 whitening 作为另一 OOD 机制因素。它把“少量 TTT 足够”从曲线趋势落实为离散 step choice。
- **优点**：五个方法列在同一面，逐行粗体清楚揭示 step count；表头短，窄栏可读。
- **弱点**：未说明粗体是行最小值；没有 TTT 的计算成本/学习率或重复离散度；方法名 `No TTT` 与 `TTT 4` 的单位需正文补齐。
- **可复用模式**：将 adaptation budget 作为列而不是隐含参数，保留 no-adaptation baseline，并在 caption 定义缩写与选择规则。

### Figure 5（物理页 7，results）

- **几何与 panel**：左栏下方单栏 line chart，1 panel；标题 `Laplace 2D: Score Estimation MSE`，x 为 `n (number of samples)`、对数刻度（10²–10³），y 为 `Score MSE`、对数样式的科学刻度；6 条曲线：KDE、No TTT、TTT 2/4/6/8 steps。legend 在右上，三角/圆/方 marker 与颜色共同编码。
- **plot grammar**：x=log，y=log（按刻度/网格的幂级数显示）；grid=both；legend=true、upper right、无 shared legend；约 6 series、3 marker types、实线为主；无 band/error bars/hatching/reference line；RGB 栅格图与 vector 轴/caption 混合。
- **颜色/编码**：红三角 KDE，黑圆 No TTT，紫/蓝/青/绿方形为 TTT 步数；估计 `#E41A1C`、`#222222`、`#984EA3`、`#377EB8`、`#1B9E77`、`#4DAF4A`，categorical，legend 文本是唯一完整 key，灰度安全 false。图内字体约 7–8 pt rendered estimate。
- **caption**：原文为 “Figure 5. MSE of score estimation on the Laplace distribution. Test-time training (TTT) improves the out-of-distribution generalization.”（词数 17）。动作：title、setup、abbreviation_definition、main_finding；直接说 TTT 改善 OOD；脱离正文可理解但不说明 step/seed/uncertainty。
- **数据与统计**：Laplace 2D 的 score MSE 随 n；每条线为点估计，无 uncertainty；与 Table 4 的 Student-t discrete values 互补。
- **证据关系**：连接 Section 3.5 consistency loss、Table 3/4 的 OOD 结果；将 Table 6 的 normalization benefit 与 TTT benefit 分开，避免把 whitening 和 adaptation 混作同一机制。
- **优点**：step count、n scaling 和 baseline 一图展示；对数 x 使样本量跨度清晰。
- **弱点**：6 条线在小 n 聚集、颜色区分依赖较强；y 轴/聚合规则未给 uncertainty；caption 的 OOD 泛化结论没有限定数据生成或 TTT budget。
- **可复用模式**：用预算序列曲线展示 test-time adaptation 的收益/饱和；增加 line-style/marker 冗余和重复区间可提升可访问性。

### Table 5（物理页 7，results）

- **几何与表头**：右栏上方单栏表，3 个方法行、3 列（`Method`、`Score MSE`、`Log-density MSE`）、单层表头、无 row group；上/表头下/中间分隔/底部横线，书籍式无竖线。行是 Scott KDE、Oracle h KDE、DiScoFormer；DiScoFormer 数值粗体（0.167、20.8）。
- **数据与统计**：d=100、随机 2-component diagonal-covariance GMM，n=2048 context、256 queries；KDE 有 Scott 与 grid-search best fixed bandwidth 两种策略；score MSE 1.155/1.090/0.167，log-density MSE 967/781/20.8；没有 uncertainty 或 failure。
- **caption/header**：原文为 “Table 5. Score and log-density estimation in d = 100 on random 2-component diagonal-covariance GMMs (n = 2048 context, 256 queries). KDE baselines use two bandwidth strategies; “Oracle h” is the best fixed bandwidth found by grid search. DiScoFormer (d_model = 256, 8 heads, 6 layers) is evaluated at 150k training steps.”（词数 52）。动作：title、setup、comparison、encoding_key、abbreviation_definition；未在 caption 直说 DiScoFormer 更低，脱离正文可理解设置和列。
- **证据关系**：Section 4.2 对 Figure 4 中 d≤10 scaling 的高维扩展，直接支撑 curse-of-dimensionality mitigation；与 Table 2 的 OOM/large-n 成本边界、Figure 15 runtime 一起形成高维决策面。
- **优点**：把 score 与 log-density 两个输出目标并列，Oracle h 防止单一 KDE 调参 strawman；模型配置与训练步数写入 caption。
- **弱点**：两列数值精度混合（score 三位、log-density 一位/整数）；没有 query-level aggregation/seed；粗体规则未写。
- **可复用模式**：在高维表中并列任务指标、强/弱 baseline 和调参上界，并把 context/query、训练预算写入 caption。

### Table 6（物理页 7，ablation）

- **几何与表头**：右栏中部单栏表；4 个数据行，左侧两组 `ID`/`OOD`，每组 Whitening/No whitening 两行；4 列（行标签、variant、`Score MSE`、`Log-density MSE`），指标表头在同一顶部层级，视觉上有两层横线及 ID/OOD 组间分隔，极简无竖线。ID Whitening 0.107/0.058、No whitening 0.118/0.066；OOD Whitening 0.020/0.123、No whitening 1.136/1.593；组内较优值粗体。
- **数据与统计**：d=1；ID/OOD 使用不同 log-uniform GMM location/scale meta-distribution，OOD scale 远超训练范围；两个 MSE 输出，无 SD/SE/重复信息，3 位小数一致。
- **caption**：原文为 “Table 6. Ablation: effect of whitening on score and density estimation (d = 1). ID and OOD use different log-uniform meta-distributions over GMM location and scale parameters; OOD scales are well beyond the training range.”（词数 35）。动作：title、setup、comparison、abbreviation_definition；没有 uncertainty 定义或直接结论；脱离正文可理解 ID/OOD 的设置但需正文解释 whitening 的理论作用。
- **证据关系**：是 Figure 2 whitening interface、Proposition 3.1/Remark 3.2 和 Limitations(rotation only approximate) 的直接 ablation；与 Table 1 的 affine error 和 Figure 5 TTT OOD 形成“结构归一化 vs 后适配”的区分。
- **优点**：ID/OOD 分组和两输出指标同时呈现，catastrophic OOD failure 无需额外解释即可看见。
- **弱点**：行组标签较靠左且无显式 multi-level header；粗体规则未说明，ID/OOD 的 meta-distribution 参数范围没有数值。
- **可复用模式**：将结构组件消融放在 ID/OOD 成对 row group，并同时保留核心任务与辅助任务指标；caption 应给出精确 OOD 范围和聚合方式。

### Figure 6（物理页 8，results）

- **几何与 panel**：左栏上方单栏 2D scatter/quiver，1 panel；x/y linear，约 x∈[−1.5,2]、y∈[−1.5,1.5]，轻网格。浅蓝 Distribution A 与浅红 Distribution B 点云，若干 score arrows 在 chosen query 附近；legend 位于左上，列出 Distribution A/B、True Score A/B、Predicted Score A/B。
- **plot grammar**：`scatter` + `other`（quiver）；linear/linear；grid=both；legend=true/upper left/shared=false；marker 是小点和箭头，line style 约 1–2；无 uncertainty/hatching/reference line。渲染 mixed（RGB 图嵌入，轴和文字 vector）。
- **编码/颜色**：点颜色表达两个分布，箭头颜色/方向表达 true/predicted score for A/B；约 6 色，估计浅蓝 `#A6CEE3`、浅红 `#FB9A99`、深绿 `#33A02C`、橙 `#FF7F00`、红 `#E31A1C`、蓝 `#1F78B4`；categorical、legend 直解，但形状冗余弱，灰度安全 false。
- **caption**：原文为 “Figure 6. Computing relative Fisher information. Our model predicts ∇ log g(xᵢ) at query points xᵢ via cross-attention with the samples yᵢ ∼ g.”（词数 24）。动作：title、setup、encoding_key、main_finding（接口能力）；不粗体；说明 query/context 角色，脱离正文可大致理解但 relative Fisher estimator 公式在正文。
- **数据与统计**：X∼f 作 query、Y∼g 作 context；图像是空间直观，不显示 relative Fisher 数值、不确定性或 Monte Carlo 重复。正文公式给 `S(X,X)−S(Y,X)` 的样本估计。
- **证据关系**：承接 cross-attention 的 context/query 设计和 Section 4.4 relative Fisher 公式，说明一个 score oracle 如何比较两个分布；后续 Figure 10 使用 score/log-density 输出作 entropy/Fisher 插件，Figure 11 作 PDE solver。
- **优点**：把抽象的“用 g 的样本估计 g 在 f 查询点的 score”变成可读的点云和箭头；legend 明确四类 score。
- **弱点**：点云与箭头重叠，chosen query/样本索引没有显式标注；没有数值 estimator error 或多次 Monte Carlo variation。
- **可复用模式**：对于 cross-distribution operator，使用 context/query 分色并在同一空间叠加 true/predicted field；应补 query marker 和 estimator 数值摘要。

### Figure 7（物理页 9，results）

- **几何与 panel**：页宽横向 qualitative grid，5 个并排 heatmap：Ground Truth Density、Scott KDE（MISE=0.001241）、SD-KDE (True Score)（0.000617）、EMP SD KDE（0.000981）、SD-KDE (Pred Score)（0.000798）。每 panel 有 x/y linear（约 −4–4）坐标，等比例空间，颜色为紫→绿→黄的 density 强度；无显式共享 colorbar，标题直接写方法和 MISE。
- **plot grammar**：`heatmap`/`qualitative_grid`，linear/linear，轻网格或无独立网格，legend=false、shared legend=false、direct labels=true（panel title）；无 marker/line/uncertainty/hatching/reference line；RGB 栅格嵌入。
- **颜色/编码**：连续 viridis 类 sequential，估计 `#440154`、`#21918C`、`#FDE725`；颜色亮度映射 density，标题内数值映射 MISE；约 3 个主色端点，灰度安全 false（密度强弱仅靠颜色）。
- **caption**：原文为 “Figure 7. Qualitative comparison: True density, Scott KDE, Emp-SD-KDE, and SD-KDE with our learned score. Learned-score SD-KDE is visibly less biased.”（词数 21）。动作：title、setup、comparison、abbreviation_definition、main_finding；直接说 learned-score SD-KDE less biased；脱离正文可识别比较对象，但 MISE/SD-KDE 细节仍靠正文。
- **数据与统计**：2D density map；MISE 作为每 panel 标题内点值，未提供 uncertainty/重复；Ground Truth 与四种 estimate 共用同一空间布局，适合形状/偏差比较。
- **证据关系**：Section 4.5 的 score-debiased KDE 机制 → 视觉密度 recovery；Figure 8/9 将同一方法扩展为 1D 曲线和 n scaling，Figure 6 的 score oracle 是其输入来源。
- **优点**：固定坐标和 panel 顺序使 bias/peak/tail 直接对比，MISE 将定性形状与数值绑定。
- **弱点**：没有共享 colorbar 或统一数值范围声明，颜色差异会被各自自动归一化的可能性不易排除；caption 没有定义 MISE。
- **可复用模式**：将 ground truth、baseline、oracle、learned estimator 放进固定坐标 qualitative grid，并把误差值写入 panel title；正式版应共享 color normalization/colorbar。

### Figure 8（物理页 9，results）

- **几何与 panel**：左栏中部单 panel 1D density plot，标题 `2048 samples from GMM with 2 components`；x/y linear，x 为 x、y 为 Density。灰色 histogram 面积/柱，黑色虚线 ground truth，蓝 KDE、绿 SD-KDE with GT score、红/紫两条 learned/autograd score 线；legend 在左下并写各方法 MSE。
- **plot grammar**：`line` + `area`/`histogram`，linear/linear；轻网格或无明显 grid；legend=true/lower left/shared=false；约 5 条 density series、3 类 line style（solid/dashed/filled bars），无 uncertainty band/error bar/hatching/reference line；mixed raster/vector。
- **颜色/编码**：灰 `#BDBDBD` histogram、黑 `#222222` ground truth、蓝 `#377EB8` KDE、绿 `#4DAF4A` true-score SD-KDE、红 `#E41A1C`/洋红 `#984EA3` learned variants；categorical，legend 文本和虚线/柱形提供冗余，灰度部分安全但曲线仍会混淆。
- **caption**：原文为 “Figure 8. 1D bimodal GMM (n = 2048): SD-KDE with the learned score best approximates the density by MSE.”（词数 19）。动作：title、setup、comparison、main_finding；直接陈述 best-by-MSE；脱离正文可理解 n、分布和结论，但方法缩写需正文。
- **数据与统计**：n=2048、2-component 1D GMM；legend 给 KDE density MSE=0.00049、ours learned density=0.00022、debiased learned score=0.000147、autograd score=0.000157 等点值；无 uncertainty。灰色 histogram 不是独立统计表，而是 sample visualization。
- **证据关系**：为 Figure 7 heatmap 的方法比较提供 one-dimensional concrete slice；与 Figure 9 density scaling 区分“小 n direct density 优势”和“score-based 随 n 更好”的结论。
- **优点**：ground truth、sample histogram、多个 estimator 的峰/谷/尾部可直接对齐，legend 将形状比较绑定到 MSE。
- **弱点**：多条曲线在峰值处重叠；legend 很密，线型/颜色语义需要放大；单一 GMM 没有重复或 uncertainty。
- **可复用模式**：用 histogram+truth+方法曲线同时呈现样本支持、目标密度和估计 bias，并在 legend 中附点误差；建议增加局部尾部 inset。

### Figure 9（物理页 9，results）

- **几何与 panel**：左下单栏复合图，2 个并排 line-chart panel，标题分别为 `GMM d=1, MSE of density estimation vs number of samples n` 与 `GMM d=2, ...`；x/y 均为 log scale、x 是 n、y 是 MSE。每 panel 约 5 条线：KDE、Debiased KDE (EMP-SD-KDE)、Debiased KDE (learned score)、Debiased KDE (autodiff log-density score)、Transformer (learned density)，legend 位于左下。
- **plot grammar**：line，log/log，grid=both/轻网格；legend per panel、shared=false；约 5 series，marker 以圆点为主、实线为主，约 1–2 styles；无 uncertainty/reference/hatching；mixed raster/vector。
- **颜色/编码**：蓝/紫/青/橙/红等 categorical 线，legend 文本完整区分 estimator；颜色约 `#3B4CC0`、`#984EA3`、`#56B4E9`、`#E69F00`、`#D73027`；灰度安全 false，几乎没有 line-style 冗余。
- **caption**：原文为 “Figure 9. MSE of density estimation in 1D (left) and 2D (right). SD-KDE with our learned score and the Transformer model show the best scaling. The Transformer was trained only at n = 2048.”（词数 34）。动作：title、setup、comparison、main_finding、appendix_pointer（训练 n 边界）；直接写 best scaling；脱离正文可理解轴/结论，但缩写和曲线名主要在 legend。
- **数据与统计**：d=1/2、多个 n、density MSE；每条线点估计，无重复区间。训练固定 n=2048，曲线测试多 n，故包含 sample-size OOD。
- **证据关系**：Figure 8 的单个 n density 对比 → Figure 9 的 scaling；与 Figure 4 score scaling 和 Table 2 score 外推对应，说明 score-debiased pipeline 不是只在一张 density 图有效。
- **优点**：左右维度切片保持同一图语法，可直接看 slope/交叉；caption 明确训练 n 与评估 n 的边界。
- **弱点**：五条线颜色接近且 legend 低位占据数据区域；斜率只写在 legend、没有 uncertainty；d=1/d=2 的相同 y normalization 需读者自行确认。
- **可复用模式**：用固定维度并排 log-log small multiples 展示 estimator scaling，caption 明确 training support；应把 slope/CI 或重复范围置于表格/annotation。

### Figure 10（物理页 9，results）

- **几何与 panel**：右栏中部 2×2 小 multiples：d=1 entropy、d=1 Fisher info、d=10 entropy、d=10 Fisher info；每 panel x=n log scale，y 为 absolute error/abs error log-like。每 panel 约 3 series，颜色分别代表 KDE、learned score/model、autodiff log-density/debiased variant；每 panel 有独立 legend，位置随空白区变化。
- **plot grammar**：line，log/log，grid=both/轻网格；legend=true、per-panel、shared=false；约 3×4 series instances，marker 圆点，实线为主；无 uncertainty band/error bars/hatching/reference line；RGB raster + vector axes。
- **编码/颜色**：典型蓝/红/绿/紫 categorical；标题编码 dimension/functional，y 编码 error，line color 编码 method；约 4 色，估计 `#1845FB`、`#E41A1C`、`#2CA02C`、`#984EA3`；灰度安全 false。
- **caption**：原文为 “Figure 10. Comparison between the transformer model (learned) and Scott KDE and score-debiased KDE for estimation of differential entropy H(f) and Fisher Information I(f). Transformer’s MSE is lower than that of the KDE approximation, even in dimension 1.”（词数 38）。动作：title、comparison、encoding_key、main_finding、abbreviation_definition；直接写 d=1 仍更低；脱离正文可理解目标量和结论，但 panel method legend 需放大。
- **数据与统计**：1D 3-mode GMM 的 entropy/Fisher（grid integration）和 d=10 random Gaussian（analytic formulas）；曲线是 absolute error，caption 说 MSE；无 uncertainty/seed。
- **证据关系**：Figure 6 score/log-density plug-in 输出的下游效用证据；Figure 9 的 density scaling 延伸到 functionals，Figure 11 再延伸到 PDE；与 abstract 的 Fisher information plug-in claim 对应。
- **优点**：2×2 layout 将两种 functional 和两种 dimension 正交展开，避免把 d=1 的结论泛化为单一任务。
- **弱点**：小 panel 的 legend/斜率文字压缩严重；caption 的 `MSE` 与 y 轴 `abs error` 可能让统计对象不够清楚；无不确定性。
- **可复用模式**：用 dimension×functional 的 2×2 grid 展示同一 estimator family 的下游效用；在轴/表头显式统一 error definition，减少 legend 负担。

### Figure 11（物理页 9，results）

- **几何与 panel**：右栏下方单栏三面板一行：Maxwell d=3、Maxwell d=10、Coulomb d=3；标题共同为 `Σ11(t) for Maxwell (d=3,10) and Coulomb (d=3)`。x=t linear，y=Σ11 linear；每 panel 有 n=500 KDE、n=500 Transformer 和 analytic/equilibrium dashed reference；legend 通常在上方空白区。
- **plot grammar**：line，linear/linear，grid=both/轻网格；legend per panel/shared=false；约 3 series/panel，实线+虚线两种 line style、无 marker 或少量 marker；无 uncertainty band/error bar/hatching；reference line/curve=1 条 analytic/equilibrium；mixed raster/vector。
- **颜色/编码**：蓝 KDE、橙 Transformer、黑虚线 analytic/equilibrium；约 3 色，实线/虚线提供一定灰度冗余，灰度安全中等而非完全安全。x/y 与 legend 字体约 6–8 pt。
- **caption**：原文为 “Figure 11. Comparison between the trained Transformer model and Scott KDE on the task of numerically solving the homogeneous Landau equation. We plot the first entry of the covariance matrix Σ₁,₁(t) of the numerical solutions and ground truth, when known. The left two panels use Maxwell collisions, while the last panel shows Coulomb collisions. The Transformer outperforms KDE, and is comparable in quality to SBTM in (Ilin et al., 2025).”（词数 70）。动作：title、setup、encoding_key、comparison、main_finding、abbreviation_definition；直接写 outperforms/comparable；脱离正文可理解 quantity、collision split 和结论，但 SBTM 未在 caption 展开。
- **数据与统计**：时间轨迹、covariance first entry；analytic/equilibrium ground truth 仅在 known panel；n=500。没有误差带、ensemble、solver variability 或时间步信息。
- **证据关系**：Section 4.7 将预训练 score oracle 连接 Landau/Fokker–Planck particle solver，证明无需 simulation-time retraining 的应用价值；Figure 15 的 runtime 是成本边界，Figure 6/10 是其他插件。
- **优点**：把 Maxwell/Coulomb 物理情形和 analytic reference 放在同一横向比较，结构清楚；虚线 reference 提供非颜色的校验。
- **弱点**：三 panel 纵轴/时间范围不完全同质，caption 未报告 solver step/error；“comparable to SBTM”缺少 SBTM 曲线，属于跨来源文字结论。
- **可复用模式**：在 PDE/solver 结果中以同一 observable、多个物理 regime 和 reference curve small multiples 组织证据，并显式标出哪些 regime 有 ground truth。

### Figure 12（物理页 18，appendix）

- **几何与 panel**：附录页宽 2×4 heatmap grid，共 8 个 panel，标题 `L0 H0` 至 `L0 H7`；每个矩阵约 90×90，x/key 与 y/query 为索引轴，附近粒子按 ordering 排列；每 panel 有自身竖向 attention colorbar。阅读方向行优先，几乎填满页宽上半部；RGB 栅格嵌入。
- **plot grammar**：`heatmap` + `matrix`，x/y 为 categorical/linear index（不是物理坐标），网格由像素矩阵构成；legend=false、direct_labels=true（head title）、shared_legend=false（每 panel colorbar）；无 marker/line/uncertainty/hatching/reference line。8 panel、8 colorbars，复杂度 4。
- **颜色/编码**：yellow higher attention、blue lower；viridis sequential，估计 `#440154`、`#21918C`、`#FDE725`，每 panel colorbar 刻度范围可能不同；灰度安全 false。标题 serif/图内 colorbar sans-serif 为 rendered estimate，约 7–8 pt。
- **caption**：原文为 “Figure 12. We visualize attention of the eight individual heads of layer 0 as a heatmap. Yellow color denotes higher attention weight and blue is lower. We choose the particle ordering so that nearby particles are close in the ordering. Heads 0, 2, and 5 specialize on nearby points, heads 1 and 6 specialize on far-away points, whereas heads 3, 4, and 7 attend in specific directions.”（词数 67）。动作：title、setup、encoding_key、main_finding、appendix_pointer；直接陈述 head specialization；脱离正文可理解矩阵和 ordering，但 layer-0/nearby 的构造仍靠附录段落。
- **数据与统计**：完整 attention matrix，8 heads；无重复/不确定性，颜色是权重而不是 estimate error。每 colorbar 局部 scale 会影响跨 head 的绝对亮度比较。
- **证据关系**：是 Figure 1 底部 4 个 head panel 的完整附录展开，支持 Section 3.3 的 emergent head specialization；Figure 13 用相同 head 集合改为 query-conditioned spatial scatter。
- **优点**：8 head 全覆盖、同一 ordering 下可比较近对角/远距离/方向模式；caption 解释颜色和 ordering。
- **弱点**：每 panel 独立 colorbar 可能使 head 间强度不可直接比；矩阵索引没有物理坐标，directional pattern 的解释需要附录文字。
- **可复用模式**：将多头机制展示为固定 head grid，caption 同时给颜色 key、排序规则和解释标签；应共享或标注 color normalization。

### Figure 13（物理页 19，appendix）

- **几何与 panel**：近满页的 scatter grid，共 **24 个 panel（3 组 query/样本情形 × 每组 8 个 head，6 行×4 列）**；每组依次 Head 0–7。每 panel 是二维 sample scatter，x/y linear，红色 `x` 标记随机 query，点颜色映射该 query 对各 sample 的 attention；每 panel 有窄竖 colorbar。RGB 栅格嵌入，信息密度为全论文最高。
- **plot grammar**：`scatter` + `qualitative_grid`；连续 linear/linear，轻网格或无网格；没有独立 legend，head title 与 colorbar 是 direct labels；shared_legend=false，每 panel colorbar；约 24 panel、每 panel 一组点云，无 uncertainty/line/hatching/reference line。复杂度 5，data marks 多（每 panel 数百点）。
- **颜色/编码**：yellow high / blue low 的 viridis sequential；红 `#E41A1C` query x，点色约 `#440154`–`#FDE725`，不同 panel colorbar 数值范围不完全相同；灰度安全 false，红 x 是少量冗余。
- **caption**：原文为 “Figure 13. We visualize attention of the eight individual heads of layer 0 as a scatter plot. We choose a random query point, marked with a red x. Yellow color denotes higher attention weight and blue is lower. Heads 0, 2, and 5 specialize on nearby points, head 1 specializes on far-away points, whereas heads 3, 4, 6, and 7 attend in specific directions.”（词数 64）。动作：title、setup、encoding_key、main_finding、appendix_pointer；直接写 specialization；脱离正文能读懂 query/color/head 语义，但三组 query 的分组界线未在 caption 明示。
- **数据与统计**：8 个 layer-0 head 在三组空间样本/query 条件上的 attention weight；没有聚合或 uncertainty，点云是 qualitative attention field。三组 x/y 范围不同（上组约 −3–3，中/下组约 −2–3 或 −4–3），跨组不能直接比较坐标密度。
- **证据关系**：Figure 12 的 matrix ordering 证据 → query-specific directional evidence；与 Figure 1 的 corr/average attention 共同支持“多尺度 learned kernels”机制，附录 C 正文明确 Head 0/2/5 close/mid-range、Head 1 far-range、Head 3/4/6/7 directional。
- **优点**：同一组 head 在多个 query/分布情形复现模式，避免单一 query 的偶然性；红 x 和各自 colorbar 让空间关系可追踪。
- **弱点**：24 panel 极密，标题、colorbar 和点云在印刷尺寸下难读；三组的 color scale/坐标范围不共享，视觉比较存在归一化歧义；caption 未说明三组条件。
- **可复用模式**：用多 query block × head grid 展示 attention 的空间稳定性；应显式给 block labels、统一坐标/color normalization，或把完整 24 panel 放交互补充材料。

### Figure 14（物理页 20，appendix）

- **几何与 panel**：附录页宽 2×3 score-field grid，共 6 个 quiver/scatter panel。上排是 MLP implicit score matching 训练 10/100/1000 steps，下排是 universal Transformer 的三个对应情形；每 panel 有 true/predicted score arrows、浅蓝样本点和 legend。x/y linear、范围约 −6–6 或随数据设定变化；RGB 栅格。
- **plot grammar**：`scatter` + `other`/quiver；linear/linear；轻网格；每 panel 独立 legend，shared=false；2 个主箭头 series（true/predicted），实线/箭头色区分；无 uncertainty/hatching/reference line。复杂度 4，panel=6。
- **颜色/编码**：浅蓝 data sample、橙 true、蓝 predicted；约 3 categorical colors，估计 `#9ECAE1`、`#FF7F0E`、`#1F77B4`；legend 提供语义但箭头形状冗余有限，灰度安全中等偏低。
- **caption**：原文为 “Figure 14. Comparison of sliced score matching and our transformer model. The transformer model can be used without retraining and does not suffer from overfitting. We plot the negated score for ease of visualization.”（词数 34）。动作：title、comparison、main_finding、encoding_key；直接写 no retraining/no overfitting；脱离正文可理解大意，但 10/100/1000 steps 和 sliced loss 细节在附录正文。
- **数据与统计**：不同 score-matching 训练步数与 universal Transformer 的 score field qualitative comparison；没有 numerical MSE/uncertainty，negated score 由 caption 定义。
- **证据关系**：附录 D 直接解释 Hyvärinen score matching loss 与 finite-difference divergence trick；Figure 14 将“每分布重训、易 under/over-fit”对比到主方法的 sequence-to-operator claim，并与 Figure 15 的成本边界互补。
- **优点**：训练步数作为上排 facet 直接暴露 overfitting trajectory，下排保持同一视觉语法。
- **弱点**：没有把每个 panel 的步数/数据条件放成醒目 panel label；qualitative 箭头比较难量化，caption 的 strong claim 没有附 numeric score。
- **可复用模式**：把 baseline 的 optimization budget 作为 facet 维度，并在同坐标下对照 universal model；最好附一个 MSE/early-stop summary table。

### Figure 15（物理页 21，appendix）

- **几何与 panel**：附录页宽两 panel runtime line chart；左标题 `Score inference comparison (d=2)`，右为 `(d=10)`。x 为 n（log scale），y 为 `Runtime (s)`（log scale，10⁻⁴–10¹），每 panel 两条曲线：蓝 KDE、橙 Transformer，圆 marker；另有虚线 fit（KDE/Transformer slope），legend 在左上。KDE 曲线在 n=2¹⁵ 处 OOM/停止，正文说明 naive implementation 在 n=32768 后耗尽 GPU memory。
- **plot grammar**：line，log/log，grid=both；legend per panel、upper left、shared=false；2 series/panel、圆 marker、实线+虚线 fit 两种 line styles；无 uncertainty band/error bar/hatching，fit 线是 2 条 reference/trend lines；mixed raster/vector。
- **颜色/编码**：蓝 `#1F77B4` KDE、橙 `#FF7F0E` Transformer，拟合虚线同色；2 categorical colors，legend+line style 有部分冗余，灰度安全中等。图内轴/legend 约 8–9 pt rendered estimate。
- **caption**：原文为 “Figure 15. Runtime comparison between KDE and the Transformer model in 2 and 10 dimensions. Both are O(n²) asymptotically, but empirically the Transformer scales better and has improved memory efficiency. KDE encounters an OOM error at n = 2¹⁵.”（词数 39）。动作：title、setup、comparison、encoding_key、main_finding、abbreviation_definition；直接写 empirical scaling/memory 与 OOM；脱离正文可理解，硬件（single L40S 48GB）由附录正文给出。
- **数据与统计**：single L40S GPU，n 约 2¹–2¹⁵；y 为 wall-clock seconds，虚线标经验 slope（左 KDE −1.98、Transformer 1.65；右 KDE −2.53、Transformer 1.65，图内 legend）。没有重复运行/误差范围；OOM 是 failure censoring，不应当当成 runtime=∞ 的连续点。
- **证据关系**：Table 2 的 OOM/large-n accuracy 与 Figure 15 成本证据闭合；附录 E 解释两者虽均 O(n²) 但 attention kernels 的实现常数/显存行为不同；Figure 14 说明 score matching 还需 retraining。
- **优点**：d=2/10 并排，log-log 轴和 slope fit 让 crossover/渐近与实际差异同时可读，OOM failure 明确标出。
- **弱点**：没有 error bars、warm-up/repetition 或硬件利用率；KDE OOM 截断曲线会使 slope 比较受 censoring 影响；caption 没报告小 n 的 KDE 优势和 crossover（正文才说明 n≤2048）。
- **可复用模式**：runtime 图同时给 wall-clock、dimension facet、经验 slope 和 OOM failure；应把硬件、重复统计、crossover 与 censored observation 写入 caption/表格。

## Algorithm 1（物理页 5，已检查但不进入 schema）

Algorithm 1 是带边框的 `GMM DataLoader`，输入 `B,d,nx,ny,[kmin,kmax]`，repeat 时采样 k，按 batch 生成两个 k-component GMM，采样 X/Y 并输出 `X,Y,log f_X(Y),∇ log f_X(Y)`。它是训练数据生成/复现接口，不是 Figure/Table，故不占用 JSON 对象数量；其职责由 Figure 2 的 forward interface 和结果对象的训练域说明承接。

## 跨对象判断

- **最可复用视觉模式**：Figure 1 的“field→matrix→correlation→head specialization”机制链；Figure 7/8 的 truth-first qualitative comparison 加 panel/legend MISE；Table 2/5/6 的 dimension×method、OOD/failure 和 ID/OOD row-group；Figure 15 的 log-log runtime 加 slope 与 OOM。
- **最高价值对象**：Figure 1（attention–KDE 构造性机制）、Figure 4+Table 2（score scaling/extrapolation）、Table 5+Table 6（高维和 whitening 边界）、Figure 7–9（SD-KDE 下游证据）、Figure 15（成本/失败边界）。
- **主要失败模式**：大量对象依赖颜色且灰度不安全；caption 常写“excellent/best/outperforms”却没有 uncertainty、seed 或重复定义；Figure 1、13 的 panel 密度压缩了轴和 colorbar；heatmap 常用独立 color normalization；表格粗体规则和聚合分母不总在 caption 说明；runtime 的 OOM/censoring 与 slope fit 需要更明确的统计语义。
- **主文—附录链**：正文 Figure 1 的四个 head panel 在附录 Figure 12/13 全展开；Table 1/6 和 Figure 2 支撑 whitening/等变性，附录 Figure 14 补 score matching failure，Figure 15 补 runtime/memory；Figure 6、10、11 将同一 score/log-density interface 连接到 Fisher、entropy 和 Landau solver。
- **最终视觉策略一句话**：以无位置编码、白化和 attention–KDE 机制为入口，用多尺度 score/density 主比较和 OOD/高维消融建立效果边界，再以插件应用和附录 attention/cost 图补齐机制、失败与复现信息。

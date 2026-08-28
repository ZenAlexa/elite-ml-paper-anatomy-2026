# iclr-2026-a58db1cc65db 视觉审计

## 1. 审计边界、事实源与渲染

- **论文**：Shifeng Xie、Vasilii Feofanov、Jianfeng Zhang、Themis Palpanas、Ievgen Redko，*CauKer – Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data*；ICLR 2026 Oral。
- **PDF 事实源**：`corpus/pdfs/iclr-2026-a58db1cc65db.pdf`，`pdf_verified=true`，29 个物理页，Letter（612 × 792 pt），pdfTeX-1.40.27；source_files 记录 OpenReview `https://openreview.net/forum?id=xBW2FIfswU` 与 proceedings PDF。
- **渲染检查**：全部 29 页以 200 dpi（1700 × 2200 px）PNG 渲染并逐页检查；对象页 p.4、6、8、9、15、18–29 另做原尺寸复核。200 dpi 高于协议要求的 180 dpi。
- **版面事实**：p.1–10 正文为两栏 ICLR layout；p.15–29 的 PDF 渲染几何呈宽单栏附录，附录图表多为 page-width，少数居中的窄图/表为 `single_column`。reading 备忘录称附录仍双栏，本审计以 PDF 几何为准。
- **对象清单**：PDF 对齐 Figure 1–13（13 幅）与 Table 1–13（13 张）；另有 Algorithm 1（p.17），按协议记录在清单说明中但不纳入 schema 的 figures/tables 数组。p.15 是 references 与 Appendix A/B 的混合物。
- **不计入对象**：公式、普通章节标题、Algorithm 1 之外的伪代码行和 Figure 内部的子图不另计；Figure 7 内嵌的结果表属于复合 Figure，不另计 Table。

## 2. 公开视觉源核查

- `reports/tables/visual_source_inventory.csv` 将 `ShifengXIE/CauKer` 标为 `partial_visual_source`，并列 `vfeofanov/mantis` 为次级候选；本地 `corpus/visual_sources/iclr-2026-a58db1cc65db/` 已有 Chronos evaluation CSV/YAML 与一个 SVG。
- `gh repo view` 与 main recursive tree 核对到 `CauKer.ipynb`、`CauKer.py`、`Models/Mantis`、`Models/Chronos`、Chronos assets/config/results。notebook 只有随机 SCM series 的 Matplotlib demo，`CauKer.py` 没有绘图导出；没有 paper TeX、编号 Figure/Table generator、plot/figure/table 目录、TikZ/PGF/SVG figure source 或 style file。
- 本地 `Models/Chronos/figures/zero_shot-agg_scaled_score.svg` 的 Matplotlib metadata 和 CSV/YAML 只支持 forecasting 扩展的相关 evaluation artifact；未将它们误当作 Figures 1–13 的重建源。故 JSON 保留 `partial_visual_source`，所有正文/附录 Figure 仍以 PDF 渲染为视觉事实源。

## 3. PDF 对象清单

| 类型 | 标签 | PDF 物理页 | 模块 | 版面 | 主要职责 |
|---|---|---:|---|---|---|
| Figure | `Figure 1` | 4 | `method` | `page_width` | method_interface；theory_mechanism；experimental_design |
| Figure | `Figure 2` | 6 | `results` | `single_column` | qualitative_evidence；mechanism；dataset |
| Figure | `Figure 3` | 8 | `results` | `page_width` | main_comparison；robustness；experimental_design |
| Figure | `Figure 4` | 8 | `results` | `single_column` | qualitative_evidence；robustness；mechanism |
| Figure | `Figure 5` | 8 | `results` | `single_column` | mechanism；robustness；ablation |
| Figure | `Figure 6` | 9 | `results` | `single_column` | robustness；efficiency_cost；main_comparison |
| Figure | `Figure 7` | 9 | `results` | `page_width` | headline；main_comparison；experimental_design；mechanism |
| Figure | `Figure 8` | 18 | `appendix` | `page_width` | method_interface；reproduction |
| Figure | `Figure 9` | 19 | `ablation` | `page_width` | method_interface；qualitative_evidence；reproduction |
| Figure | `Figure 10` | 23 | `appendix` | `single_column` | ablation；robustness；main_comparison |
| Figure | `Figure 11` | 26 | `appendix` | `page_width` | qualitative_evidence；mechanism；robustness |
| Figure | `Figure 12` | 27 | `appendix` | `page_width` | qualitative_evidence；robustness；main_comparison |
| Figure | `Figure 13` | 28 | `appendix` | `page_width` | qualitative_evidence；mechanism；robustness |
| Table | `Table 1` | 6 | `results` | `page_width` | headline；main_comparison；experimental_design |
| Table | `Table 2` | 6 | `results` | `single_column` | efficiency_cost；experimental_design |
| Table | `Table 3` | 15 | `appendix` | `page_width` | dataset；experimental_design；reproduction |
| Table | `Table 4` | 20 | `ablation` | `page_width` | ablation；mechanism；robustness |
| Table | `Table 5` | 20 | `ablation` | `page_width` | ablation；robustness |
| Table | `Table 6` | 20 | `appendix` | `single_column` | mechanism；robustness；experimental_design |
| Table | `Table 7` | 21 | `appendix` | `page_width` | experimental_design；reproduction；main_comparison |
| Table | `Table 8` | 22 | `appendix` | `page_width` | experimental_design；main_comparison；reproduction |
| Table | `Table 9` | 23 | `appendix` | `single_column` | robustness；main_comparison；dataset |
| Table | `Table 10` | 24 | `appendix` | `single_column` | robustness；main_comparison；dataset |
| Table | `Table 11` | 25 | `appendix` | `single_column` | main_comparison；robustness；efficiency_cost |
| Table | `Table 12` | 29 | `appendix` | `single_column` | main_comparison；experimental_design；robustness |
| Table | `Table 13` | 29 | `appendix` | `single_column` | robustness；main_comparison；experimental_design |

## 4. 全文视觉系统

- **计数**：主文 Figure 1–7（7）、Table 1–2（2）；附录 Figure 8–13（6）、Table 3–13（11）；Algorithm 1 位于 p.17。
- **字体**：`pdffonts` 显示正文/表格主要为 Nimbus Roman No9 L、Nimbus Mono L、Computer Modern 系列；图内包含 DejaVu Sans、Calibri、Ubuntu 等，图内字号约 5.5–12 pt，来源多为嵌入 vector/raster composite。
- **颜色**：Table 1–13 主要黑白、bold 与横线；Figure 2/11 使用连续色条，Figure 3/6/7/10/13 使用蓝/橙或蓝/灰系列，Figure 4/12 使用 CauKer/UEA/UCR 来源色。颜色语义不是跨图固定，需依赖各自 legend/caption。
- **统计表达**：主结果多为 UCR average accuracy、runtime、MASE、AUROC/AUPRC 或 domain average 点估计；Figure 5 与 Table 6 才显式呈现 box/distribution 或 mean ± s.d.。大量图表没有 seed、误差或分母，定性 embedding/attention 图不提供 coverage、cluster 或 faithfulness statistic。

## 5. Figure 逐对象审计

### Figure 1（p.4，method）

- **版面与职责**：`page_width`；类型为 `pipeline, architecture, conceptual_diagram, image_montage`；purpose=`method_interface, theory_mechanism, experimental_design`；complexity=4/5（panels=3，marks≈None）。
- **绘图语法**：rendering=`mixed`；x/y=`none`/`none`；grid=`none`；legend=`False`（none）；direct labels=`True`；marker types=0；line styles=2；hatching=`False`；uncertainty=`none`；线宽≈1.0 pt；provenance=`rendered_estimate`。
- **编码**：x=左到右 Selected kernels → Combined kernels → Generate with selected mean → SCM with selected activation functions → Generated time series。；y=画布层级：kernel/mean 先验、root time series、DAG nodes、最终序列。；color=模块角色和节点/序列类别使用蓝、浅蓝、绿色、米色等颜色。；shape=矩阵缩略图、时间序列曲线、圆形 DAG nodes、箭头和虚线框。；line=实线箭头表示生成/传播，虚线弧线表示可选的节点输出路径。；facet=三块流程区；SCM 区内部还有多节点结构。；text=K、GP、均值函数、activation function、root/child 节点和 generated time series 标签。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Nimbus Roman No9 L, Computer Modern，约 5.5–12.0 pt（中位 8.0），provenance=`mixed`；模式=`mixed`，颜色数≈8，灰度安全=`False`。蓝色箭头/时间序列、浅蓝输入、米色和浅绿色节点分别编码 GP、SCM/activation 和数据流；模块标题与箭头方向提供文字和位置冗余。
- **Caption（112 词）**：Figure 1: An illustration of the proposed CauKer pipeline. Kernels sampled from the kernel bank K are randomly combined and used together with sampled mean functions to form GP priors. Time series sampled from these GP priors act as root nodes in a directed acyclic graph that encodes causal dependencies between nodes. Each edge of this graph applies an activation function from a predefined activation function bank and aggregates over incoming edges using a random linear transformation to propagate transformed time series through the graph. Intermediate node outputs are optionally interpolated to fixed length, forming the final synthetic dataset. This procedure yields rich, diverse, and causally consistent time series for self-supervised pre-training.
  - moves=`title, setup, encoding_key, main_finding`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`True`。
- **数据与统计**：示意图不编码样本分母、聚合或不确定性；它把论文正文的五步生成过程压缩成 kernel composition、GP root sampling、DAG propagation 和 optional interpolation。Algorithm 1 在 p.17 给出可执行细节；Figure 1 本身只有机制接口。
- **证据关系**：§3.2 的三类 bank 与五步 CauKer → Figure 1 的 kernel/mean→GP→SCM→series 机制链 → Table 1 的生成器对照、Figure 2 的 DTW 聚类和 Figure 3–7 的预训练结果；附录 Figure 8–9 展开 bank。
- **设计优点**：五个阶段按阅读方向排列，能把 GP temporal structure 与 SCM dependency 的分工放在同一条链上。；截图、文字标签、箭头和节点形状形成冗余编码，输入、传播和输出无需依赖正文公式。；caption 解释 root nodes、activation、random linear transformation 和 optional interpolation，脱离正文仍能理解流程。。
- **设计弱点**：小型 kernel 矩阵和时间序列缩略图在页面缩放后难以读出具体函数。；颜色和图标较多，灰度下模块区分变弱；没有用数值标注呈现 bank 大小、节点数或生成成本。；图给出“causally consistent”叙述，但没有在对象内区分 DAG 语义与因果识别证据。。
- **可复用模式**：用“先验组件→随机结构→观测输出”的横向 pipeline 同时呈现数据生成的接口和机制；每个阶段保留直接标签，并把不可见的随机操作写进 caption。

### Figure 2（p.6，results）

- **版面与职责**：`single_column`；类型为 `heatmap, matrix`；purpose=`qualitative_evidence, mechanism, dataset`；complexity=5/5（panels=1，marks≈40000）。
- **绘图语法**：rendering=`mixed`；x/y=`linear`/`linear`；grid=`none`；legend=`True`（right colorbar）；direct labels=`False`；marker types=0；line styles=0；hatching=`False`；uncertainty=`none`；线宽≈None pt；provenance=`rendered_estimate`。
- **编码**：x=列索引 0–200，表示排序后的 200 个 time series。；y=行索引 0–200，和列使用同一排序。；color=色条 DTW distance，深紫低、黄高。；shape=200×200 方格矩阵单元。；line=无；facet=单面板；行列按 hierarchical-clustering membership 排序。；text=轴刻度 0/50/100/150/200、标题 Sorted DTW distance、右侧 DTW distance 色条。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`sequential`，颜色数≈4，灰度安全=`False`。viridis-like 色条从低到高编码 DTW distance；颜色是唯一的连续数值编码，排序后的块结构通过位置呈现。
- **Caption（12 词）**：Figure 2: Clustering structure of CauKer generated dataset with 200 time series.
  - moves=`title, setup`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：由 200 条 CauKer 序列计算 pairwise Dynamic Time Warping distance，形成 200×200（约 40,000 cell）矩阵；先对预计算距离做 hierarchical clustering，再按 cluster membership 同时排序行列。没有误差、重复、分母或显著性统计；caption 不说明 DTW 的具体实现参数。
- **证据关系**：§4.1 的“classification 需要 discriminative clustering”主张 → Figure 2 的块状低/高 DTW 结构和异常条带 → Table 1 的 CauKer accuracy 优势；Appendix Table 6 以 SWD/CKNNA 提供全局/局部定量补充。
- **设计优点**：矩阵的对称结构和排序后的块让 cluster membership 具有直接视觉证据。；轴刻度、标题和 colorbar 定义了距离单位，异常和组内相似度可以在同一画布对照。；200-series 规模和 DTW 方法在正文叙述中明确，使定性图有可追溯计算对象。。
- **设计弱点**：40,000 个 cell 没有直接数值标签，色条估读无法复核细微差异。；连续色条对灰度不安全，且没有 cluster 边界线或 dendrogram，块的数量需凭颜色推断。；图展示的是一组随机生成样本，不能单独证明聚类结构在不同 seed 或数据规模下稳定。。
- **可复用模式**：将高维样本的 pairwise distance 按聚类排序后用对称 heatmap 展示；同时报告样本数、排序规则和距离定义，并用边界标出 cluster。

### Figure 3（p.8，results）

- **版面与职责**：`page_width`；类型为 `line`；purpose=`main_comparison, robustness, experimental_design`；complexity=4/5（panels=4，marks≈90）。
- **绘图语法**：rendering=`vector`；x/y=`unknown`/`linear`；grid=`both`；legend=`True`（top, two grouped legends）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.8 pt；provenance=`rendered_estimate`。
- **编码**：x=前两 panel 为 log-like data size（10^4–10^7）；后两 panel 为离散 model-size settings（MOMENT 77/248/783M，Mantis 0.75/2.59/8.10M）。；y=Accuracy，四个 panel 的 y 范围略有不同，均为线性。；color=UEA 与 CauKer 数据来源、以及 UEA/CauKer 的具体规模由颜色和两处 legend 编码。；shape=无 marker；每条曲线是一种数据来源/规模条件。；line=实线连接同一条件在不同数据或模型规模下的 accuracy。；facet=四个 panel：MOMENT data scaling、Mantis data scaling、MOMENT model scaling、Mantis model scaling。；text=Accuracy、Data Size/Model Size、UEA 1%/10%/100%、CauKer 100K/1M/10M。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈8，灰度安全=`False`。左侧数据规模图用 CauKer/UEA 两色；右侧模型规模图用三种 UEA 比例和三种 CauKer 规模的橙/蓝色系。颜色与图例绑定，线型基本相同。
- **Caption（42 词）**：Figure 3: Scaling law of MOMENT and Mantis depending on the dataset size (left, middle left, respectively) model trained on different subsets of UEA and CauK datasets. Scaling law for the same models depending on the model size (middle right, right, respectively)
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：四个 panel 汇总 data-size 与 model-size sweeps。左两图比较 UEA 随机子集和 CauKer 10K–10M；右两图比较 MOMENT 77/248/783M 与 Mantis 0.75/2.59/8.10M。y 为 128 个 UCR 数据集的平均 accuracy point estimate；无误差带、seed dispersion 或置信区间。Table 7 给出 data-scaling 精确值，Table 8 给出 model-scaling 精确值。
- **证据关系**：Q2 的 scaling-law 问题 → Figure 3 同时展示数据和模型容量变化 → Figure 5 的 non-linearity/CKA 解释与 Figure 6 的 training-time curves；Appendix Tables 7–8 负责可复核数字。
- **设计优点**：四 panel 使用相同 Accuracy 语义，能把 data scaling 和 model scaling 放在一个跨对象问题上。；左侧来源 legend 与右侧条件 legend 各自靠近对应 panel，避免把数据来源与规模条件混为一谈。；曲线连接使 UEA 的不规则趋势和 CauKer 的总体上升方向可直接比较。。
- **设计弱点**：同一 figure 同时混用 log-like data-size 轴和离散 model-size 轴，caption 没有明确说明坐标变换。；颜色承担几乎全部系列区分，线型没有冗余，灰度下六条模型规模曲线难以辨认。；y 轴截断/窄范围放大了百分点差异，caption 没有给重复或不确定性。。
- **可复用模式**：把两种 scaling 轴拆成同构小 multiples，并共享来源/规模的 legend；同时提供一张 exact-value appendix table，避免曲线承担精确数字。

### Figure 4（p.8，results）

- **版面与职责**：`single_column`；类型为 `scatter`；purpose=`qualitative_evidence, robustness, mechanism`；complexity=3/5（panels=1，marks≈100000）。
- **绘图语法**：rendering=`raster`；x/y=`linear`/`linear`；grid=`both`；legend=`True`（top right）；direct labels=`False`；marker types=1；line styles=0；hatching=`False`；uncertainty=`none`；线宽≈0.4 pt；provenance=`rendered_estimate`。
- **编码**：x=1st Principal Component。；y=2nd Principal Component。；color=CauKer/UEA/UCR 来源类别用三种颜色。；shape=密集小圆点。；line=无；facet=无；text=右上 legend 和两轴 principal-component 标签。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈3，灰度安全=`False`。CauKer、UEA、UCR 三个数据来源分别用浅蓝、粉、绿散点；legend 用文字补充颜色语义。
- **Caption（16 词）**：Figure 4: Mantis embeddings of 100K time series drawn from UCR, UEA and generated by CauKer.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：在原始 Mantis embedding space 的 PCA 投影中比较 UCR、UEA 和 100K CauKer-generated time series。散点数量高、重叠明显，图呈现覆盖范围而非可检验的 cluster metric；没有 explained-variance、类别中心、置信椭圆或重复实验。
- **证据关系**：Q2 关于数据多样性/域覆盖的解释 → Figure 4 显示 CauKer embedding 覆盖区域包住 UEA/UCR → Figure 3 的 scaling 方向和 Figure 5 的 CKA 结构变化；Appendix Figure 12 用不同 nmax 重复 PCA 视角。
- **设计优点**：三种来源同轴叠加，直接回答 synthetic corpus 是否覆盖真实 embedding region。；legend 与点颜色清楚定义来源，PCA 轴标签避免把坐标误读为原始时间轴。；紧邻 Figure 3/5，覆盖范围、容量 scaling 和内部结构解释形成连续视觉段落。。
- **设计弱点**：大量点重叠且没有透明度/密度编码，覆盖“包住”是视觉判断而非面积或距离统计。；三色类别在灰度下不安全，图中没有形状或边界作为替代编码。；100K 的抽样与各来源分母未在 caption 中说明，不能据图比较类别密度。。
- **可复用模式**：对 representation coverage 用同一 PCA/embedding 空间叠加多来源散点；同时在 caption 给出每类抽样量，并用 density/ellipse 或 coverage statistic 补足重叠问题。

### Figure 5（p.8，results）

- **版面与职责**：`single_column`；类型为 `box`；purpose=`mechanism, robustness, ablation`；complexity=4/5（panels=4，marks≈22）。
- **绘图语法**：rendering=`vector`；x/y=`categorical`/`linear`；grid=`none`；legend=`False`（none）；direct labels=`False`；marker types=1；line styles=0；hatching=`False`；uncertainty=`box`；线宽≈0.8 pt；provenance=`rendered_estimate`。
- **编码**：x=CauKer panel 10K/50K/100K/1M/10M；UEA panel 1%/5%/10%/20%/30%/100%。；y=上排 Linearity、下排 CKA；CauKer 与 UEA 的 y 范围按 panel 单独设置。；color=橙色 median line，黑色 whisker/outline；条件主要由 x tick 和 panel title 编码。；shape=箱体、whisker 和离群圆点。；line=无；facet=2×2 panels：CauKer/UEA × Linearity/CKA。；text=Panel titles CauKer/UEA、y labels Linearity/CKA、x ticks 数据规模。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`mixed`，颜色数≈2，灰度安全=`True`。白色箱体与黑色轮廓承载分布，橙色中位线标出中心；CauKer/UEA 和 Linearity/CKA 由 panel 标题与轴标签编码，不依赖颜色区分条件。
- **Caption（36 词）**：Figure 5: (Top row) Non-linearity statistics of the Mantis models pre-trained on CauKer synthetic datasets of varying size (left) compared to UEA (right); (Bottom row) CKA similarities calculated across the hidden layers of the pre-trained models.
  - moves=`title, setup, comparison, encoding_key`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：四个 panel 包含 5 个 CauKer 数据规模箱体（每个上/下排）和 6 个 UEA 百分比规模箱体；箱体表达 non-linearity statistic 或 CKA 的分布，median、四分位范围、whisker 和 outlier 可见。没有说明每个箱体的样本数或跨 seed 聚合规则，也没有显著性比较。
- **证据关系**：Q2 的“合成数据让内部表征随规模变化”主张 → Figure 5 以 Linearity/CKA 分布解释 Figure 3 的 scaling 曲线 → Appendix Figure 4/5 的文字和 exact values 继续说明 synthetic diversity。
- **设计优点**：箱体而不是单点保留了分布形状、离群值和中位差异。；2×2 结构把 dataset source 与 representation statistic 正交拆开，便于比较 CauKer 和 UEA。；黑白箱体和位置编码使主要语义在灰度下仍可读。。
- **设计弱点**：四个 panel 使用不同的 y 范围，跨 panel 比较绝对变化需要读刻度。；x tick 很密且 UEA/CauKer 的规模单位不同，caption 没有说明箱体样本/重复层级。；CKA 下降被作者解释为更非线性，但图本身不呈现 causal mechanism 或 statistical test。。
- **可复用模式**：对内部统计量使用同一 2×2 source×metric layout，并保留 box/whisker 分布；在 caption 补充分布分母、聚合单位和方向解释。

### Figure 6（p.9，results）

- **版面与职责**：`single_column`；类型为 `line`；purpose=`robustness, efficiency_cost, main_comparison`；complexity=2/5（panels=2，marks≈120）。
- **绘图语法**：rendering=`vector`；x/y=`linear`/`linear`；grid=`both`；legend=`True`（top center）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.8 pt；provenance=`rendered_estimate`。
- **编码**：x=Training Epoch；MOMENT 左 panel 约 1–20，Mantis 右 panel 约 5–100。；y=Test accuracy，两个 panel 使用各自线性范围。；color=CauKer 与 UEA 训练 corpus。；shape=无 marker 的连续折线。；line=实线表示随 epoch 的 accuracy trajectory。；facet=左右 panel 分别为 MOMENT、Mantis。；text=legend、Training Epoch、Accuracy，以及 1/20/40/60/80/100 等 epoch ticks。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈2，灰度安全=`False`。CauKer dataset 蓝线、UEA dataset 橙线；legend 直接定义两条线，未使用线型冗余。
- **Caption（12 词）**：Figure 6: Test accuracy across epochs for MOMENT (left) and Mantis (right).
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：追踪 Mantis 与 MOMENT 在 10% UEA 和 1M CauKer 上随训练 epoch 的 zero-shot UCR accuracy；图中每条线是单一训练轨迹，未给多次训练的均值、误差带、checkpoint 选择或 seed。左/右 panel 的 epoch 范围和 y 刻度不同。
- **证据关系**：§4.3 training-time scaling → Figure 6 对比延长优化在 CauKer 与 UEA 上的收益 → Figure 3 data/model scaling；Figure 7 右侧再以 loss+accuracy 对照补充 sample-efficiency。
- **设计优点**：两种架构共享 legend 和颜色，训练来源差异一眼可见。；epoch 作为连续横轴，能展示“CauKer 持续上升、UEA 平/波动”的趋势，而不是只报告终点。；panel 标题在 caption 中明确，读者不会把 MOMENT 与 Mantis 曲线混合。。
- **设计弱点**：仅用颜色区分两条线，灰度/色弱下辨识度低。；没有 error band 或重复轨迹，无法判断“稳步”是否跨 seed 稳定。；两个 panel 的 y 范围和 epoch 采样不一致，直接比较斜率需要额外换算。。
- **可复用模式**：用 source×architecture small multiple 展示训练时间轨迹；保持共享 legend，同时提供跨重复的均值/分位带而非单轨迹。

### Figure 7（p.9，results）

- **版面与职责**：`page_width`；类型为 `line, other`；purpose=`headline, main_comparison, experimental_design, mechanism`；complexity=4/5（panels=3，marks≈40）。
- **绘图语法**：rendering=`mixed`；x/y=`linear`/`linear`；grid=`both`；legend=`True`（top of right plots）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.8 pt；provenance=`rendered_estimate`。
- **编码**：x=左侧为 table rows；右侧横轴 Epoch Number 1–100。；y=右上 Training Loss、右下 Test Accuracy；两个 y 轴各自线性范围。；color=右侧 CauKer/Real 两条曲线；左表绿色 No、红色 Yes。；shape=左表文本行与右侧两条连续线，未使用 marker。；line=右侧实线随 epoch 变化；左侧 group separator 连接 Mantis/MOMENT rows。；facet=复合布局：左表 + 右侧上下两图（loss/accuracy）。；text=Model、pre-train set、Size、UCR Included?、UCR acc.(%)；CauKer/Real legend。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Nimbus Roman No9 L, Computer Modern，约 5.5–12.0 pt（中位 8.0），provenance=`mixed`；模式=`categorical`，颜色数≈3，灰度安全=`False`。右侧 loss/accuracy 曲线以 CauKer 蓝、Real 橙为主，左侧表格以绿色/红色文字编码 UCR Included? Yes/No；模型和状态文字提供冗余。
- **Caption（102 词）**：Figure 7: Performance comparison of Mantis and MOMENT models on different pre-training datasets. CauKer-generated pre-training data allows to nearly match the performance of the original TSFMs, while being more sample-efficient. Rows with ‘UCR included? = Yes’ correspond to in-distribution zero-shot evaluation, as the pre-training corpus contains UCR train splits (though not test data). Rows with ‘UCR included? = No’ correspond to strictly OOD zero-shot models. Training loss and test accuracy corresponding to the first two rows illustrated in the right figure show that synthetic data is harder to train on, but leads to a smoother increase of the test accuracy across epochs.
  - moves=`title, setup, comparison, encoding_key, main_finding`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`True`。
- **数据与统计**：复合对象左侧列出 Mantis/MOMENT 各四种预训练设置及 UCR accuracy：Mantis CauKer100K 78.55、real 1.89M 78.66、UEA100K 76.73、Forecasting100K 75.81；MOMENT CauKer10M 77.49、Time Series Pile13M 78.85、CauKer100K 74.24、UEA100K 73.55、Forecasting100K 73.93。右侧只画前两行对应的 Training Loss 与 Test Accuracy trajectories；没有重复/不确定性。
- **证据关系**：Q3 sample-efficient pretraining → Figure 7 把 corpus size、UCR inclusion、accuracy 和训练动态放在一个对象 → Table 9/10/12/13 扩展域外、fine-tuning 与 irregular clinical 结果；Figure 6 提供独立 training-time 对照。
- **设计优点**：表格和曲线共享 CauKer/Real 语义，既给终点决策值，又给训练过程机制。；UCR Included? Yes/No 把官方 checkpoint 的 train-split exposure 写入对象，避免把所有分数都称为严格 OOD。；caption 同时解释样本效率、in-distribution/OOD 边界和曲线含义，信息自足度高。。
- **设计弱点**：左表是 figure 内嵌的第二种阅读语法，模型组与 curve panel 的视觉权重不完全一致。；颜色编码 UCR Included? 与 Real/CauKer 叠加，红/绿在灰度下不安全；状态虽有 Yes/No 文字，表格仍需放大。；右侧只展示第一、第二行的训练曲线，不能从图中推断其他配置的训练动态或重复稳定性。。
- **可复用模式**：在 headline figure 中并列“条件表 + 对应训练轨迹”，让终点性能、数据暴露边界和优化动态共存；caption 明确哪些行被曲线选中。

### Figure 8（p.18，appendix）

- **版面与职责**：`page_width`；类型为 `heatmap, line, image_montage`；purpose=`method_interface, reproduction`；complexity=4/5（panels=12，marks≈None）。
- **绘图语法**：rendering=`mixed`；x/y=`linear`/`linear`；grid=`none`；legend=`True`（individual matrix colorbars）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.7 pt；provenance=`rendered_estimate`。
- **编码**：x=上排/下排各子图横轴为 time index；上排矩阵横纵均为时间索引，下排为 Time。；y=上排为 covariance intensity，下排为 sampled signal value；各小图 y 范围不同。；color=每个 kernel 的 covariance colorbar 使用连续强度；sample paths 统一蓝色。；shape=六列×上下两行小图；每列一个 base kernel。；line=下排蓝色曲线，表示从对应 GP prior 抽样的 path。；facet=六列 Kernel 1–6；上 covariance、下 corresponding series。；text=Kernel 1…6、Covariance/Time Series 标题与 Time/Time Index 轴。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`mixed`，颜色数≈6，灰度安全=`False`。上排 covariance matrix 使用各自连续色块/色条；下排 sample path 主要为蓝线。Kernel 1–6 标签和上下位置提供颜色之外的身份编码。
- **Caption（21 词）**：Figure 8: Visualizations of covariance matrices (top) and corresponding sampled time series (bottom) from each base kernel in the kernel bank.
  - moves=`title, setup, encoding_key`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：展示六类代表 kernel 的 1024 evenly spaced time points covariance matrix 与一条 GP sample path：ExpSineSquared、DotProduct、RBF、RationalQuadratic、WhiteKernel、ConstantKernel。它们是 illustrative examples，不是 36-kernel bank 的完整分布；无重复、误差或聚合统计。
- **证据关系**：Appendix C.2 的 kernel bank 解释 → Figure 8 以 covariance→sample path 绑定每个 base kernel 的时间结构 → Figure 1 的 GP root 组件和 Figure 9 mean-function bank；Appendix C prose 明确实际生成使用更大 bank。
- **设计优点**：每列上/下配对，把抽象 covariance 与可见时间轨迹直接连接。；六列同构，便于横向比较周期、趋势、局部波动、噪声和常数信号。；caption 和正文都说明 1024 点、illustrative subset 与 full bank 的边界，避免把示例误当完整 generator。。
- **设计弱点**：六个 colorbar 和小型坐标轴很密，缩放后难以读取具体 covariance 数值。；各 kernel 的 y 轴范围不同，sample-path 振幅不宜直接比较。；没有把 36 个参数化实例或随机抽样频率可视化，仍需依赖文字理解 bank diversity。。
- **可复用模式**：用同列上下配对的“kernel matrix + sampled path”解释生成先验；在 caption 明确示例子集、时间网格和完整 bank 的关系。

### Figure 9（p.19，ablation）

- **版面与职责**：`page_width`；类型为 `line`；purpose=`method_interface, qualitative_evidence, reproduction`；complexity=2/5（panels=4，marks≈4）。
- **绘图语法**：rendering=`vector`；x/y=`linear`/`linear`；grid=`none`；legend=`False`（none）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.7 pt；provenance=`rendered_estimate`。
- **编码**：x=Time 0–1。；y=Mean Value；四个 panel 的 y 范围按样本函数变化。；color=无颜色区分；同一蓝色用于四类函数。；shape=四个同构小折线图。；line=蓝色 sample path。；facet=四个函数类型从左到右排列，但 panel 内没有标题。；text=Time、Mean Value 和 caption 的 four mean function types；具体类型名由附近 Appendix C.2 prose 给出。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈1，灰度安全=`True`。所有 mean-function sample path 使用同一蓝线；函数身份由四个并列 panel 位置和正文列出的 Zero/Linear/Exponential/Sparse Anomalies 定义。
- **Caption（29 词）**：Figure 9: Examples of four mean function types used in the synthetic data pipeline. Each function introduces distinct temporal structure, contributing to the diversity and realism of generated sequences.
  - moves=`title, setup, main_finding`；headline_bold=`False`；self-contained=`False`；main_finding_stated=`True`。
- **数据与统计**：四个 panel 是 Zero Mean、Linear Mean、Exponential Mean、Sparse Anomalies 的随机实例；图展示 mean vector 的时间形状，不报告参数分布、重复数或不确定性。每个 panel 只有一条 illustrative line。
- **证据关系**：Appendix C.2 mean bank → Figure 9 展示均值函数的 temporal motifs → Figure 1 GP prior 与 Table 1 的 Mean+KernelSynth/CauKer 组件增量；Figure 8 展示对应 covariance bank。
- **设计优点**：四个 panel 共享时间范围，简单线形直观看出零、线性、指数和稀疏异常差异。；单色线避免把颜色误认为函数语义，灰度可读性好。；正文说明随机参数和 additive/multiplicative composition，避免把四条线当成固定模板。。
- **设计弱点**：panel 没有直接标出函数名，caption 也不列出四类名称，脱离周围 prose 无法逐一映射。；各 y 轴范围不同，指数/异常的幅度不能直接按纵向高度比较。；仅为各类一个 sample path，不能展示随机参数覆盖或失败行为。。
- **可复用模式**：用相同坐标的小 multiples 展示生成函数类别；必须把函数名写在 panel 标题或 caption，而不是依赖正文段落。

### Figure 10（p.23，appendix）

- **版面与职责**：`single_column`；类型为 `line`；purpose=`ablation, robustness, main_comparison`；complexity=3/5（panels=1，marks≈30）。
- **绘图语法**：rendering=`vector`；x/y=`categorical`/`linear`；grid=`both`；legend=`True`（lower right）；direct labels=`False`；marker types=3；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.8 pt；provenance=`rendered_estimate`。
- **编码**：x=Mantis model size 0.75M、2.59M、8.10M、28.56M、114.14M，按离散位置排列。；y=Classification Accuracy，约 0.72–0.79 的线性 y 轴。；color=UEA 1%/10%/100% 与 CauKer 100K/1M/10M。；shape=圆、方、三角 marker 分别补充系列身份，线段连接 model-size values。；line=六条实线表示各 corpus condition 随 Mantis capacity 的变化。；facet=无；text=legend、UCR accuracy、Model Size (Parameters) 和六条件名称。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈6，灰度安全=`False`。三种 UEA subset 条件用橙色系、三种 CauKer corpus size 用蓝色系；legend 同时给出 marker shape 与条件名。
- **Caption（22 词）**：Figure 10: Accuracy on UCR dataset with varying model sizes for the Mantis model trained on UEA subsets and synthetic CauKer data.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：复现 Figure 3 中 Mantis model-size panel，并扩展到 28.56M 与 114.14M。8.10M→28.56M→114.14M 的 CauKer10M accuracy 为 79.09→78.19→78.81，显示作者所述 saturation/单点反常；UEA 规模曲线也不单调。所有点是 UCR average accuracy，无重复或误差。
- **证据关系**：Q2 model scaling claim → Figure 10 补足 main Figure 3 未显示的大 Mantis capacities → Table 8 的完整 model-size×dataset exact values；为 Figure 3 “28M 后 saturation”叙述提供附录证据。
- **设计优点**：marker shape 与颜色双重编码六条线，较 Figure 3 更容易追踪条件。；扩展模型容量并保持同一 UEA/CauKer 条件集合，能检验有限主图的外推。；legend 放在图内，caption 清楚限定 Mantis、UEA subsets 和 synthetic data。。
- **设计弱点**：模型参数在离散等距 x 位置展示，轴没有说明是 categorical 还是 numeric scale。；六条线在 2.59M–8.10M 区域交叠，颜色在灰度下不安全。；单点平均值没有 seed/数据集 dispersion，饱和与反常仍可能是配置噪声。。
- **可复用模式**：用 marker+palette 的 multi-series line chart 展示容量扩展，并在附录表提供 exact values；对不等距模型规模应使用真实 log/numeric x 轴或明确离散轴。

### Figure 11（p.26，appendix）

- **版面与职责**：`page_width`；类型为 `scatter`；purpose=`qualitative_evidence, mechanism, robustness`；complexity=4/5（panels=4，marks≈1800）。
- **绘图语法**：rendering=`raster`；x/y=`linear`/`linear`；grid=`both`；legend=`True`（right colorbars and combined-panel legend）；direct labels=`False`；marker types=1；line styles=0；hatching=`False`；uncertainty=`none`；线宽≈0.4 pt；provenance=`rendered_estimate`。
- **编码**：x=UMAP first component/embedding horizontal coordinate。；y=UMAP second component/embedding vertical coordinate。；color=Frequency、Slope、Bias panel 的 generating parameter 用连续色条；combined panel 用三类颜色。；shape=密集小散点。；line=无；facet=2×2：Frequency Analysis、Slope Analysis、Bias Analysis、Combined Analysis。；text=各 panel title、parameter colorbar、combined legend（Frequency/Slope/Bias）。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`mixed`，颜色数≈12，灰度安全=`False`。Frequency/Slope/Bias panel 分别用连续 parameter colorbar；Combined panel 用绿色 frequency、蓝色 slope、红色 bias 类别。颜色在各 panel 的语义不同。
- **Caption（30 词）**：Figure 11: UMAP projections of embeddings produced by the CauKer pre-trained encoder. Colour encodes the generating parameter for each synthetic class (green = frequency, blue = slope, red = bias).
  - moves=`title, setup, encoding_key`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：用 Mantis 8M（10M CauKer 预训练）编码三类合成序列：20 个 frequency periods、slope [0.1,10]、bias [-5,5]，每个参数设置实例化 30 次。前三 panel 观察 parameter gradient，第四 panel 观察三类 cluster；图没有 cluster score、UMAP stability 或统计检验。
- **证据关系**：Appendix K 的 known generative-factor test → Figure 11 展示 embedding 是否沿 frequency/slope/bias 有序变化 → Figure 12 的 real-vs-synthetic PCA diversity 和 Figure 13 的 attention localization；这些是 representation mechanism 的定性补充。
- **设计优点**：前三 panel 使用连续 colorbar，第四 panel 使用类别 legend，分别适合 parameter gradient 和 class separation。；四 panel 同页保留相同 embedding 语义，能从 factor-level 到 combined-level 阅读。；caption 定义 green/blue/red 类别，正文给出参数范围与每点重复数，证据边界比单纯散点图清楚。。
- **设计弱点**：各 panel 颜色条的方向和尺度不同，跨 panel 不能直接比较颜色。；散点密度高、轴标签小，且颜色是主要类别编码，灰度下不安全。；“disentangled”来自视觉 cluster 与 gradient，缺少定量 separability、seed stability 或 negative control。。
- **可复用模式**：先用连续 colorbar 检查已知生成因子，再用统一类别 legend 检查联合分离；为每种色彩语义固定尺度，并配一个定量 disentanglement 指标。

### Figure 12（p.27，appendix）

- **版面与职责**：`page_width`；类型为 `scatter`；purpose=`qualitative_evidence, robustness, main_comparison`；complexity=4/5（panels=3，marks≈None）。
- **绘图语法**：rendering=`raster`；x/y=`linear`/`linear`；grid=`none`；legend=`True`（top right of each panel）；direct labels=`False`；marker types=1；line styles=0；hatching=`False`；uncertainty=`none`；线宽≈0.4 pt；provenance=`rendered_estimate`。
- **编码**：x=1st Principal Component。；y=2nd Principal Component。；color=CauKer、UEA、UCR 三种 dataset source。；shape=密集小散点。；line=无；facet=三个 nmax panels：(a) 10K、(b) 100K、(c) 1M。；text=panel labels nmax、source legend、principal-component axes。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈3，灰度安全=`False`。每个 PCA panel 用浅蓝 CauKer、粉 UEA、绿 UCR；同一 legend 位置重复出现，点的来源同时由文字 label 编码。
- **Caption（38 词）**：Figure 12: PCA-visualization of Mantis embeddings for samples from UCR, UEA and CauKer-generated data. For each plot, we randomly select min(nsamples, nmax) samples for each dataset, where nsamples is the dataset size and nmax ∈ {10K, 100K, 1M}.
  - moves=`title, setup, comparison, encoding_key`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：在原始 Mantis embedding space 上对 UCR、UEA 和 CauKer 生成数据做 PCA；每个 panel 对每个来源抽取 min(nsamples,nmax)，nmax 为 10K/100K/1M，比较样本量变化下的覆盖。点数随 nmax 增大，图不提供 explained variance、coverage ratio、密度统计或重复 PCA。
- **证据关系**：Appendix K 的 diversity question → Figure 12 重复 Figure 4 的 real-vs-synthetic embedding 对照并改变 nmax → Table 9 UCR domain breakdown、Table 10 WOODS externality；与 Figure 11 的 known-factor UMAP 形成 representation evidence pair。
- **设计优点**：三个 nmax panel 保持同一来源颜色和坐标语义，读者可观察 CauKer coverage 随规模扩展。；legend 和 panel caption 明确 nmax，避免把三张图误读为三种模型。；用 matched sample count 处理不同数据集规模，比较意图在 caption 中可复核。。
- **设计弱点**：颜色类别没有形状冗余，灰度下难区分 UEA/UCR/CauKer。；点云重叠随 nmax 增大，视觉“更均匀覆盖”缺少数值 coverage/overlap 指标。；三个 panel 的 dense raster 点在论文尺寸下细节较小，legend 还重复占用空间。。
- **可复用模式**：用固定颜色/坐标的 sample-size multiples 检查 representation coverage；同时报告 PCA explained variance 和 coverage/overlap summary，避免仅靠点云外观。

### Figure 13（p.28，appendix）

- **版面与职责**：`page_width`；类型为 `line, image_montage`；purpose=`qualitative_evidence, mechanism, robustness`；complexity=5/5（panels=20，marks≈40）。
- **绘图语法**：rendering=`vector`；x/y=`linear`/`linear`；grid=`none`；legend=`True`（top of each row）；direct labels=`False`；marker types=0；line styles=1；hatching=`False`；uncertainty=`none`；线宽≈0.7 pt；provenance=`rendered_estimate`。
- **编码**：x=Time index 0–500。；y=左轴 Input value；attention rollout 与 input series 使用同一小图中的双尺度/不同刻度语义。；color=蓝 attention、灰 input；颜色仅用于叠加身份。；shape=每个样本为两条连续曲线。；line=两条实线叠加，蓝线峰值表示 attention mass。；facet=四行×五列：ECG CauKer-100K、ECG real-data Mantis、Fish CauKer-100K、Fish real-data Mantis。；text=row captions、Label=0/1/3/5/6、Attention rollout/Input time series legend。。
- **字体与颜色**：字体=DejaVu Sans, Calibri, Ubuntu, Computer Modern，约 5.5–10.0 pt（中位 7.5），provenance=`mixed`；模式=`categorical`，颜色数≈2，灰度安全=`False`。蓝色 Attention rollout 与灰色 Input time series 两条线；四个 row label 和每个 Label=… 文本补充样本/类别语义。
- **Caption（10 词）**：Figure 13: Attention Rollout on UCR ECG and FISH samples.
  - moves=`title, setup`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **数据与统计**：展示 UCR ECG/Fish 各五个随机代表样本，共 20 个小图，比较 CauKer-100K 预训练 Mantis 与 real-data Mantis 的 attention rollout 和 input series。图是 selected cases，没有汇总 attention entropy、peak width、类别平均或重复置信度；不同样本 y 刻度还会变化。
- **证据关系**：Appendix L 的 representation comparison → Figure 13 以 input/attention overlay 支撑“synthetic model 更尖锐、更局部” → Figure 11/12 的 embedding evidence 和 Table 12 fine-tuning；它是机制性 qualitative case，不替代总体 attention statistic。
- **设计优点**：每一行固定 dataset×pretraining source、每一列固定样本位，能直接比较同类案例。；蓝/灰线把模型解释信号和原始输入叠加，attention peak 可定位到具体时间段。；row caption、Label 文本和 legend 形成文字冗余，图无需依赖颜色才能知道案例身份。。
- **设计弱点**：20 个小图信息密度很高，局部峰值和双尺度刻度在页面尺寸下难读。；蓝/灰实线仍是核心系列区分，灰度/打印质量可能混淆。；随机代表案例没有抽样规则、总体分母或 attention faithfulness test，不能据图量化“更局部”。。
- **可复用模式**：用固定行列语义的 small-multiple overlay 绑定输入与解释信号；若要做机制结论，应在旁边提供总体峰宽/熵/定位误差的汇总。

## 6. Table 逐对象审计

### Table 1（p.6，results）

- **版面与结构**：`page_width`；purpose=`headline, main_comparison, experimental_design`；2 个数据行、5 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=2。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`bold`。
- **Caption（19 词）**：Table 1: Average zero-shot accuracy (%) on the UCR benchmark after pre-training on synthetic corpora generated by different methods.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：每个 cell 是 100K synthetic pre-training 后、128 个 UCR dataset 平均 zero-shot accuracy 的点估计；没有误差、重复或分母列。
- **数据与统计**：SCM 73.49/59.23、FPFN 77.52/70.85、KernelSynth 77.70/69.31、Mean-KernelSynth 78.20/72.56、CauKer 78.31/74.24（Mantis/MOMENT）。
- **证据关系**：Q1 生成器对照 → Table 1 的逐级组件比较 → Figure 2 聚类机制与 Table 2 runtime → Appendix Tables 4–6 的敏感性/对齐诊断。
- **设计优点**：5 个生成器列在同一行中，能直接读取 kernel、mean 和 SCM 组件的增量。；Mantis/MOMENT 行对齐不同架构，显示 CauKer 的收益并非只发生在一个模型。；粗体 CauKer 列给出 headline result，表格非常紧凑。。
- **设计弱点**：只有最终平均值，没有数据集级分布、seed 或 task count。；caption 没有说明 100K、univariate length 512 和冻结 encoder，这些条件需回正文。；粗体只突出 CauKer，不标注与最强 baseline 的差值或显著性。。
- **可复用模式**：用“模型行×生成器列”的单层 booktabs 表隔离组件贡献；把生成数据量、序列长度和平均分母写进 caption。

### Table 2（p.6，results）

- **版面与结构**：`single_column`；purpose=`efficiency_cost, experimental_design`；4 个数据行、2 列、1 层表头、2 个 row group；规则=`booktabs`；主精度=2。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（12 词）**：Table 2: Overall wall-clock generation time and internal runtime breakdown for CauKer.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：报告 1,000 条、长度 512 的 univariate series 生成 wall-clock：CauKer 121.64s、KernelSynth 182.25s；CauKer 内部 GP sampling 118.54s、SCM structure+propagation 1.14s。没有硬件/重复误差。
- **数据与统计**：运行时点估计和内部拆分支持“SCM layer <1% cost、CauKer 甚至快于 KernelSynth”的结论。
- **证据关系**：Q1 computational-cost question → Table 2 的总时长/组件时长 → Figure 1 的 root-only GP/SCM propagation 机制；没有独立 runtime plot。
- **设计优点**：总时长与内部 breakdown 分成两组，计算开销问题可快速回答。；秒数保留两位小数，GP 与 SCM 的数量级差异清楚。；与 Figure 1 的“只对 roots 采 GP”机制在空间上相邻。。
- **设计弱点**：只有一次/一种硬件软件设置，缺少跨硬件、并行度和生成吞吐。；表格把总耗时与组件耗时混在同一两列，读者需依赖横线理解组别。；没有标准差或运行次数，121.64 与 182.25 的差异无法量化稳定性。。
- **可复用模式**：把总耗时和可归因组件耗时放在两组相邻行；同时记录 N、L、硬件和重复统计，避免单次 wall-clock 被当作一般成本。

### Table 3（p.15，appendix）

- **版面与结构**：`page_width`；purpose=`dataset, experimental_design, reproduction`；8 个数据行、6 列、1 层表头、0 个 row group；规则=`partial_grid`；主精度=混合/不适用。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（12 词）**：Table 3: Overview of pre-training datasets for Time Series Foundation Models (TSFMs).
  - moves=`title, setup`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：分类/开放状态及 time points、series count 的目录型信息；数值混合 B/M/K/N/A/约数，没有均值或不确定性。
- **数据与统计**：Chronos、ForecastPFN、Mantis、MOMENT、NuTime、TabPFN、TimePFN、UniTS 的 Synthetic/Real/Open 与 corpus scale；它是数据来源背景，不是模型性能表。
- **证据关系**：Appendix A 的 TSFM pre-training data taxonomy → Table 3 统一整理代表模型的 corpus 属性 → Figure 7 的 UCR Included? 和 Table 11 的 Chronos 语境。
- **设计优点**：六列 header 直接把 synthetic/real、time points、series count 和 open status 并列。；按 model name alphabetic 排列，便于查找 baseline。；用 Yes/No/N/A/约数保留源资料异质性，没有伪造精度。。
- **设计弱点**：长引用嵌入模型名使行高不均，窄字号下不易读。；表中没有版本、抓取日期或数据泄漏边界；Mantis count 还受版本脚注影响。；异质单位（84B observations、890K series、N/A）不宜直接横向当作同一尺度。。
- **可复用模式**：对 foundation-model corpus 做目录表时保留来源类型、数量单位和开放状态，并明确版本与 in-distribution exposure。

### Table 4（p.20，ablation）

- **版面与结构**：`page_width`；purpose=`ablation, mechanism, robustness`；5 个数据行、6 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（36 词）**：Table 4: Kernel/Parents co-sweep. Increasing both the number of sampled kernels in the GP composition and the maximum number of parents per node produces steadily higher Entropy/Stability/Lumpiness and a decreasing Hurst, while UCR accuracy stays stable.
  - moves=`title, setup, comparison, main_finding`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`True`。
- **不确定性/统计**：Kernel3/Parent2→Kernel7/Parent6 的 Entropy、Hurst、Stability、Lumpiness 和 UCR accuracy 点估计；Lumpiness 列从两位到八位不一致，没有重复误差。
- **数据与统计**：Entropy 0.4629→0.6225、Hurst 0.7719→0.7519、Stability 0.9821→11.7237、Lumpiness 145.18→10,148,441.78，UCR 0.7848→0.7810；复杂度改变数据统计但 accuracy 近似稳定。
- **证据关系**：Appendix C.3 hyperparameter question → Table 4 kernel/parent co-sweep → Table 5 graph-size sweep → Table 1 的 CauKer component result；为“robust to generative hyperparameters”提供边界。
- **设计优点**：同一行同时给 generator complexity 与 downstream accuracy，机制—结果绑定紧。；Kernel/Parents 标签直接表达 sweep direction，读者无需解码编号。；caption 直接写出统计趋势和 accuracy stability，附录表自足。。
- **设计弱点**：Lumpiness 数值跨多个数量级且精度不一致，缺少 log 变换或单位说明。；只有五个设定、无 seed/置信范围，稳定性判断依赖极小的 sweep。；表头没有注明各指标方向，尤其 Hurst/Stability 的解释需回正文脚注。。
- **可复用模式**：把生成复杂度参数和下游 metric 放在同一 sweep 表；对跨数量级统计使用明确单位/变换，并保留完整精度。

### Table 5（p.20，ablation）

- **版面与结构**：`page_width`；purpose=`ablation, robustness`；5 个数据行、6 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（11 词）**：Table 5: Graph size sweep. CauKer is insensitive to DAG size.
  - moves=`title, setup, main_finding`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`True`。
- **不确定性/统计**：DAG graph size 10/20/30/40/50 下的 Entropy、Hurst、Stability、Lumpiness、UCR accuracy 点估计；无重复或误差。
- **数据与统计**：UCR accuracy 0.7848、0.7811、0.7812、0.7815、0.7785，作者据此称对 graph size 不敏感；数据统计变化幅度较小但 Lumpiness 仍跨量级。
- **证据关系**：Appendix C.3 graph-size sweep → Table 5 检查 DAG 节点数敏感性 → Table 4 kernel/parent sweep；共同限定 Figure 1 SCM graph 的可选规模。
- **设计优点**：单列 Graph Size 与统一五个指标，趋势可按节点数顺序扫描。；与 Table 4 使用相同列语义，两个 sweep 可直接横向比较。；caption 明确结论，表格不需要读正文才能知道作者关注点。。
- **设计弱点**：“insensitive”没有预先阈值，0.7848 到 0.7785 的可接受范围由读者判断。；没有运行重复或置信度，无法把窄 band 与噪声区分。；Lumpiness 的极端值可能受统计定义/样本规模影响，表中无解释列。。
- **可复用模式**：对结构规模敏感性使用与组件 sweep 同构的表格；预先定义稳定范围并报告重复分布，而不是只列单点。

### Table 6（p.20，appendix）

- **版面与结构**：`single_column`；purpose=`mechanism, robustness, experimental_design`；2 个数据行、3 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`bold`。
- **Caption（34 词）**：Table 6: Global and local alignment between UCR and synthetic corpora. Lower is better for SWD; higher is better for CKNNA. Means ± s.d. across five independent synthetic draws, then averaged over UCR datasets.
  - moves=`title, setup, comparison, uncertainty_definition`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：SWD 为 mean ± s.d.（五个 independent synthetic draws 后再跨 UCR average），lower is better；CKNNA 同样 mean ± s.d.，higher is better。
- **数据与统计**：KernelSynth/CauKer：Global SWD2 7.11 (±1.13)/3.1486 (±0.21)；CKNNA 0.014 (±0.03)/0.015 (±0.03)。CauKer 全局更近、局部略高。
- **证据关系**：Appendix D alignment diagnostics → Table 6 以全局 SWD 和局部 CKNNA 支撑 SCM backbone 的 distribution/class geometry 解释 → Figure 2 DTW 与 Table 1 accuracy。
- **设计优点**：caption 定义指标方向、五次 draw 和跨 UCR averaging，统计边界比主表更完整。；两行正交覆盖 global/local alignment，CauKer 的主要优势清晰。；粗体强调更优 CauKer cell，同时保留不确定性。。
- **设计弱点**：CKNNA 两列标准差都为 0.03，均值差 0.001 的解释力有限。；只有两种 generator、没有 dataset-wise distribution 或 paired test。；SWD 与 CKNNA 的数值尺度差异大，表中没有标准化效果量或图示。。
- **可复用模式**：把分布级与邻域级 alignment 并排，并在 caption 写清 lower/higher、重复 draw 和跨数据集聚合。

### Table 7（p.21，appendix）

- **版面与结构**：`page_width`；purpose=`experimental_design, reproduction, main_comparison`；21 个数据行、4 列、1 层表头、4 个 row group；规则=`partial_grid`；主精度=2。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（13 词）**：Table 7: Exact accuracy values used in the scaling law plots (Figure 3).
  - moves=`title, setup, appendix_pointer`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：MOMENT(77M) 与 Mantis(8M) 在 UEA/CauKer data-size sweep 的 exact UCR accuracy；MOMENT 10 rows、Mantis 11 rows，值保留两位小数。
- **数据与统计**：列出 UEA 12.7K–12.67M/633K 等随机子集与 CauKer 10K–10M：MOMENT CauKer 74.24→77.49，Mantis CauKer 76.91→79.09；UEA 序列不单调。
- **证据关系**：Appendix E 的 data-scaling implementation details → Table 7 为 Figure 3 左两 panel 提供 exact values → Table 8 承接 model-size sweep。
- **设计优点**：Model group、Train Set、Data Size、UCR Accuracy 四列直接对应 Figure 3 的条件。；横线分隔 MOMENT/Mantis 及 UEA/CauKer，行顺序保留生成规模。；exact table 可让读者重建主图而不必从像素估读。。
- **设计弱点**：21 行 dense table 依赖跨行 model labels，模型和数据源的嵌套关系需视觉追踪。；UEA data-size 数字顺序并非严格升序（127K、1.27M、633K…），caption 未解释采样排序。；accuracy 仍为单点，没有 seed、UCR dataset count 或 variance。。
- **可复用模式**：为 scaling plot 提供同条件 exact-value companion table；保持 plot 的条件顺序，并在表中按真实数值排序或解释非单调顺序。

### Table 8（p.22，appendix）

- **版面与结构**：`page_width`；purpose=`experimental_design, main_comparison, reproduction`；8 个数据行、7 列、1 层表头、2 个 row group；规则=`partial_grid`；主精度=2。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（18 词）**：Table 8: Exact zero-shot accuracy (%) on the UCR benchmark under different model sizes and pre-training dataset configurations.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：8 个 model-size rows × 6 个 UEA/CauKer dataset conditions 的 zero-shot UCR accuracy point estimates；无误差、重复或显著性。
- **数据与统计**：MOMENT 77/248/783M 和 Mantis 0.75/2.59/8.10/28.56/114.14M；例如 CauKer10M 为 77.49/77.51/77.85（MOMENT）和 76.44/78.30/79.09/78.19/78.81（Mantis）。
- **证据关系**：Appendix F model-capacity details → Table 8 exact matrix → Figure 3 右两 panel 与 Figure 10 Mantis large-capacity extension；它暴露 saturation/outlier。
- **设计优点**：多级 header 把模型容量和训练 corpus 条件放在一个完整矩阵。；MOMENT/Mantis 横线分组，容量值直接写在行标签。；补齐 Figure 3 和 Figure 10 的精确数值，便于复核“单一 outlier”。。
- **设计弱点**：六列数值密集，表头 CauKer 字样较长导致横向扫描成本高。；模型容量和数据规模都是离散 condition，未给参数/数据的 log scale 或趋势摘要。；没有重复/不确定性，严格单调和 saturation 结论仍由少量点估计支撑。。
- **可复用模式**：用 model capacity×dataset regime 的矩阵记录 scaling exact values；在同一表中保留异常点而不是只给拟合曲线。

### Table 9（p.23，appendix）

- **版面与结构**：`single_column`；purpose=`robustness, main_comparison, dataset`；15 个数据行、4 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（16 词）**：Table 9: Domain-wise UCR accuracy (mean across datasets within each Type). Δ = CauKer100K − Official.
  - moves=`title, setup, comparison, abbreviation_definition`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：15 个 UCR Type 的 domain-average accuracy；CauKer100K、Official 与 Δ 均为跨该 Type 数据集的平均点估计，没有 Type 内 dispersion。
- **数据与统计**：Device、ECG、EOG、EPG、HRM、Hemodynamics、Image、Motion、Power、Sensor、Simulated、Spectro、Spectrum、Traffic、Trajectory；Power +0.0611，Spectro −0.0550，8/15 domains 为正。
- **证据关系**：Appendix H domain heterogeneity → Table 9 将总体 UCR average 拆成 Type → Table 10 WOODS/外部域；Spectro deficit 解释为小样本与 official UCR exposure。
- **设计优点**：Δ 列直接给出 CauKer100K − Official，方向一眼可查。；15 行保留正负 domain heterogeneity，不只呈现 overall average。；caption 说明 mean across datasets 和差值定义，表格可独立阅读。。
- **设计弱点**：无每个 Type 的 dataset count，平均值的权重不能由表重建。；−0.0550 等差值未以颜色/粗体突出，发现重要 domain 需扫描。；Official checkpoint 含 UCR train split 的暴露边界只在正文/脚注，caption 未提示。。
- **可复用模式**：把总体性能拆成标准领域行，并显式加入 baseline difference；同时报告每域样本/数据集数和 baseline exposure。

### Table 10（p.24，appendix）

- **版面与结构**：`single_column`；purpose=`robustness, main_comparison, dataset`；6 个数据行、4 列、1 层表头、2 个 row group；规则=`booktabs`；主精度=3。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`bold`，provenance=`pdf_object`；highlighting=`bold, best_second_best`。
- **Caption（36 词）**：Table 10: WOODS summary (domain averages over constituent datasets) and overall statistics. ERM: supervised baseline from Gagnon-Audet et al. (2023). Mantis-2M: original real-data pre-trained encoder (∼1.89M series). CauKer100K: the same architecture pre-trained on 100K CauKer samples.
  - moves=`title, setup, comparison, abbreviation_definition`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：CAP/HAR/MI/SEDFx 四个 WOODS domain averages，以及 win counts 和 average over all 17 datasets；accuracy 是官方 split 平均点估计，未给跨 split dispersion。
- **数据与统计**：ERM、CauKer100K、Mantis-2M 三列；CauKer100K overall 0.820，ERM 0.800，Mantis 0.810；win counts 7/11/4（ties counted）。MI 中 ERM 0.733 高于 CauKer 0.563 和 Mantis 0.543。
- **证据关系**：Appendix I WOODS OOD extension → Table 10 展示 EEG-heavy domain、MI counterexample 与 overall/win summary → Table 9 UCR domains 和 Table 13 irregular clinical extension。
- **设计优点**：domain rows 与 overall summary 分隔，既显示异质性又保留 headline average。；粗体按 sub/domain winner，能看出 CauKer 并非所有 domain 都最好。；caption 定义三个 baseline 名称和训练样本量，比较边界清楚。。
- **设计弱点**：caption 没有说明 17 个 dataset 的具体组成和各 domain 权重。；win count 把 ties 计入 wins，容易与严格胜出数混淆；正文还存在 12 vs 表中 11 的文字冲突。；0.733/0.563 等 domain averages 没有置信范围或每数据集分布。。
- **可复用模式**：用 domain average + win count + overall summary 的三层结构呈现 OOD 异质性；必须定义 tie 计数和 domain 权重。

### Table 11（p.25，appendix）

- **版面与结构**：`single_column`；purpose=`main_comparison, robustness, efficiency_cost`；9 个数据行、4 列、1 层表头、5 个 row group；规则=`booktabs`；主精度=2。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（24 词）**：Table 11: Zero-shot forecasting on the chronos-zero-shot suite (27 non-overlapping subsets). Lower MASE is better. CauKer1M denotes pre-training on 1M sequences of length 512.
  - moves=`title, setup, comparison, uncertainty_definition`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：27 non-overlapping chronos-zero-shot subsets 的平均 MASE 点估计；Chronos rows 为 0.81–0.89、Seasonal Naive 为 1.0000，未给 subset-level dispersion。lower is better。
- **数据与统计**：Chronos Tiny/Mini/Small/Base 的 Official 84B vs CauKer1M 0.5B observations：0.87/0.89、0.84/0.87、0.83/0.86、0.81/0.83；Seasonal Naive 1.0000。
- **证据关系**：Appendix J forecasting transfer → Table 11 对比 official Chronos 与 1M CauKer pretraining → local Chronos CSV/config artifacts provide related benchmark inputs but not a verified paper-table generator。
- **设计优点**：Model Type、Training Data、pre-training Data Size、MASE 四列明确比较对象与单位。；每个 Chronos model 的 Official/CauKer rows 相邻，方向 lower-is-better 在 caption 写明。；Seasonal Naive 放在末行，提供统一 scale baseline。。
- **设计弱点**：表中 MASE 由 27 subset 聚合而来，但没有聚合公式/权重或 subset variance。；Official 84B 与 CauKer 0.5B 数量级不同，表格没有显式 sample-efficiency ratio。；CauKer1M 脚注使用内部 shorthand，caption 与脚注需一起读。。
- **可复用模式**：为跨 model scale 的 forecasting transfer 使用 paired rows；把 baseline、数据观察量和聚合分母写成正式列/脚注。

### Table 12（p.29，appendix）

- **版面与结构**：`single_column`；purpose=`main_comparison, experimental_design, robustness`；3 个数据行、3 列、1 层表头、0 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（28 词）**：Table 12: Downstream fine-tuning accuracy on UCR for Mantis using the default fine-tuning pipeline. All models are pre-trained with the indicated corpus and then fine-tuned under identical settings.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：三种 Mantis pre-training corpus 在相同 default fine-tuning pipeline 下的 UCR test accuracy：0.8496、0.8291、0.8457；没有 dataset-level variance。
- **数据与统计**：Original real-data 1.89M=0.8496，CauKer100K=0.8291，CauKer1M=0.8457；从 100K 到 1M synthetic 缩小与 real model 的 gap。
- **证据关系**：Appendix M downstream adaptation → Table 12 把 zero-shot 表外的 supervised fine-tuning 结果补回 → Table 7 的 zero-shot counterparts 与 Table 13 irregular benchmarks。
- **设计优点**：三行直接对应三种 pre-training initialization，比较面简单。；caption 明确 identical fine-tuning settings，控制条件写在对象内。；Test accuracy 保留四位小数，足以显示 100K→1M 的变化。。
- **设计弱点**：没有列出 fine-tuning dataset count、seed、训练轮次或方差。；仅给 overall UCR accuracy，不能判断改善是否由少数 domains 驱动。；real corpus 与 synthetic corpus 的数据质量/暴露差异没有在表中重复提示。。
- **可复用模式**：用最小的 pretraining×fine-tuning result table 复用同一模型与 pipeline；同时报告 seed/数据集级分布，避免精确小数造成过度确定感。

### Table 13（p.29，appendix）

- **版面与结构**：`single_column`；purpose=`robustness, main_comparison, experimental_design`；6 个数据行、4 列、1 层表头、2 个 row group；规则=`booktabs`；主精度=4。
- **表头/高亮**：header family=Nimbus Roman No9 L, Computer Modern, Nimbus Mono L，body/header≈8.5/8.5 pt，header weight=`mixed`，provenance=`pdf_object`；highlighting=`none`。
- **Caption（22 词）**：Table 13: Zero-shot-style evaluation on irregular, multivariate clinical benchmarks. We compare the original Mantis encoder with Mantis pre-trained on CauKer-100K and CauKer-1M.
  - moves=`title, setup, comparison`；headline_bold=`False`；self-contained=`True`；main_finding_stated=`False`。
- **不确定性/统计**：P12/P19 两个 irregular, multivariate clinical benchmark 的 AUROC/AUPRC 点估计；每个 dataset 三种 Mantis checkpoint，没有置信区间或重复。
- **数据与统计**：P12 real/CauKer100K/CauKer1M AUROC 0.8121/0.7984/0.8189、AUPRC 0.4340/0.4276/0.4592；P19 对应 0.8846/0.8534/0.8709、0.5368/0.4954/0.5005。
- **证据关系**：Appendix N irregular clinical extension → Table 13 检验 regular fixed-length UCR 之外的转移 → Table 10 WOODS 与 Table 12 fine-tuning，限定 synthetic pretraining 的外推范围。
- **设计优点**：Dataset/Model 两层行组让 P12/P19 内的三种 checkpoint 对齐。；AUROC 与 AUPRC 并列，兼顾 imbalance 下 ranking 与 precision-recall。；caption 明确 original real-data baseline 与两个 CauKer 数据规模。。
- **设计弱点**：只有两个 dataset，不能代表 irregular multivariate clinical population。；没有 positive prevalence、split 数、方差或显著性，0.8189 vs 0.8121 不宜作强优越性结论。；表没有标明 higher-is-better，方向需读者凭指标常识判断。。
- **可复用模式**：用同一 dataset block 比较 real/synthetic checkpoints，并把 AUROC/AUPRC 同列；对少量临床任务必须附 prevalence、split 和不确定性。

## 7. 交叉对象判断

- **视觉叙事**：Figure 1 先给 kernel/mean/SCM 生成接口；Table 1/2 和 Figure 2 回答 generator quality、cost、cluster mechanism；Figure 3–7 依次展开 data/model/time scaling 与 sample efficiency；Appendix Figure 8–13、Tables 3–13 补足 bank、敏感性、OOD、forecasting、representation 和 fine-tuning。
- **Caption/header 系统**：caption 多以“Figure/Table n: object noun”开头，正文表格 caption 通常简短，Figure 1/7 和 Table 4/5 写出主发现；Figure 5/7/11/12 定义 top/bottom、来源颜色或 sample-size 条件。少数 caption（Figure 9、Table 7）依赖相邻 prose 才能映射具体函数/条件。 表头以 Model/Train Set/Data Size、dataset/source、metric/unit 为核心；booktabs-like top/mid/bottom rules 占主导，少数宽矩阵用 partial vertical separators。粗体用于 CauKer/best cells，precision 随指标而变，均值±s.d. 只在 Table 6 明确出现。
- **方法—结果—消融链**：Figure 1 的 GP kernel/mean/SCM 链接 Table 1 的 SCM→FPFN→KernelSynth→Mean-KernelSynth→CauKer progression；Figure 2、Table 4–6 验证 cluster、hyperparameter robustness 与 global/local alignment；Figures 3–7 将这些设计映射到 scaling、训练时间和 sample efficiency。
- **正文—附录链**：正文 Figure 1–7 与 Table 1–2 保留主决策链；Appendix Table 3、Algorithm 1、Figures 8–9 解释数据和 generator；Tables 4–8/10–13 与 Figures 10–13 提供 exact scaling、domain/OOD、forecasting、representation、fine-tuning 和 clinical boundary。Algorithm 1 是 PDF 对象清单中的额外算法，schema 只审计 Figure/Table。
- **字体/颜色一致性**：native tables统一 Nimbus Roman/Computer Modern 约 8.5pt，表头多为 bold/mixed；plot labels 多为 DejaVu Sans/Calibri/Ubuntu 约 5.5–10pt。正文与附录的图内字号和 raster/vector 输出质量不完全一致，尤其 Figure 11–13 的小 panel。 蓝/橙常用于 CauKer/UEA 或 CauKer/Real 对照，viridis-like scale 用于 distance/parameter intensity，浅蓝/粉/绿用于 UCR/UEA/CauKer source；表格主要黑白并用 bold。跨图颜色语义并非全局固定（例如 Figure 11 的 blue 同时是 slope 或模型条件），因此 caption/legend 必须随图重定义。

## 8. 最终判断

- **最可复用模式**：
  - Figure 1 的“组件先验→随机结构→观测序列”pipeline，把生成机制和实验接口放在同一空间顺序中。
  - Figure 3/6 的同构 small multiples，把 data/model/time scaling 变成可比较的曲线族，并用 appendix exact tables 兜底。
  - Figure 7 的“条件表+训练轨迹”复合图同时呈现终点性能、数据暴露边界和优化动态。
  - Table 4–6/9–10 的组件 sweep、global/local diagnostics 和 domain breakdown，将 headline average 拆成可证伪的机制/异质性切片。
- **最高价值对象**：
  - Table 1：最直接的生成器/组件主比较，数值和模型行都可扫读。
  - Figure 3：将 synthetic/real data scaling 与 model capacity scaling 统一成主结果视觉。
  - Figure 7：在一个对象中绑定 sample efficiency、UCR inclusion 和 training dynamics。
  - Table 6 与 Table 10：分别提供 global/local alignment 和 WOODS domain/OOD 反例，限定“causal synthetic data”主张。
- **失败模式**：
  - 多系列图大量依赖颜色且缺少线型/marker 冗余，Figure 3/6/10/12/13 在灰度或小尺寸下辨识度下降。
  - 散点/heatmap/UMAP 图以 selected samples 或单次生成作为定性证据，缺少 coverage、cluster、attention 或稳定性统计。
  - 主表和附录表多为平均点估计，常不写分母、重复层级、seed 和误差；精确小数容易造成超出证据的确定感。
  - 附录把 exact scaling、domain/OOD 和版本脚注分散在 p.15–29；Mantis count、WOODS wins、accuracy drop 等叙述/表格存在可定位冲突。
- **一句话视觉策略**：论文用一条“GP kernel/mean temporal prior→SCM causal propagation→synthetic representation→scaling/sample-efficiency/OOD”视觉链，结合少数 headline tables、密集 qualitative plots 和附录 exact values，论证 CauKer 在有限 TSFM 设置中比简单 synthetic baselines 更有用，但尚未把 DAG 语义升级为因果识别保证。

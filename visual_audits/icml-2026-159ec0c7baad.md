# Visual audit - `icml-2026-159ec0c7baad`

## 范围、事实源与对象清单

- **论文**：*Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models*（EcoVLA），Yuting Huang 等，arXiv:2602.00780v1，PDF 日期 2026-01-31。
- **PDF 事实源**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/preprints/icml-2026-159ec0c7baad.pdf`。`pdfinfo` 报告 12 个物理页、letter 页面（612 x 792 pt）、PDF 1.7。正文为物理页 1-8，参考文献为 9-10，附录为 11-12；完整文本、参考文献和附录均已读取。
- **渲染与检查**：完整 PDF 用 `pdftoppm -r 220 -png` 渲染为 1870 x 2420 px/页，超过 180 dpi。逐页检查 1-12 页，并对含视觉对象的 p.1、p.3、p.7、p.8、p.12 以 220 dpi 高分辨率检查；同时用 `pdfimages -list`、`pdffonts` 与 `pdftohtml -xml` 核对栅格对象、字体对象和 caption 位置。
- **PDF 对象清单**：PDF 实际包含 7 幅 Figure（Figure 1-7）和 5 张 Table（Table 1-5）。Figure 1 在 p.1，Figure 2 在 p.3，Table 1-4 与 Figure 3-4 在 p.7，Figure 5 与 Table 5、Figure 6 在 p.8，Figure 7 在附录 p.12。p.9-11 没有未标注的 Figure/Table；页 11 的附录文字承接 p.12 的 Figure 7。Algorithm、公式和普通照片子图不另计为对象。
- `readings/icml-2026-159ec0c7baad.json` 的 visual inventory 与上述 PDF 清单一致；inventory 只作起点，最终数量和页码以 PDF 逐页对象为准。
- 下文 bbox 使用 PDF 点的近似 `[x0, top, x1, bottom]`，由 220 dpi 渲染边界和 `pdftohtml` 的页面坐标换算，目的是定位对象而非替代视觉描述。

| 物理页 | PDF 对象 | 模块 | 版面职责 |
|---:|---|---|---|
| 1 | Figure 1 | introduction / abstract-side | 动态稀疏模式的动机热图 |
| 3 | Figure 2 | methodology | EAP 与 I2O 的方法总览 |
| 7 | Table 1 | main results | OpenVLA-OFT + LIBERO 主比较 |
| 7 | Table 2 | main results | π0.5 + LIBERO 跨模型比较 |
| 7 | Table 3 | main results | CogACT + SIMPLER 跨模型比较 |
| 7 | Table 4 | real-robot results | π0.5 / Kinova Gen3 真实机器人计数 |
| 7 | Figure 3 | real-robot results | 三个真实机器人任务照片 |
| 7 | Figure 4 | more results / ablation | dense/sparse 延迟分解 |
| 8 | Figure 5 | more results / trade-off | pruning ratio - success/speedup 曲线 |
| 8 | Table 5 | more results / overhead | 正常推理与 I2O 延迟 |
| 8 | Figure 6 | more results / hyperparameters | α 与 p 灵敏度曲线 |
| 12 | Figure 7 | appendix A.4 | Kinova Gen3 与 RealSense 硬件设置 |

## 公开视觉源获取

- `reports/tables/visual_source_inventory.csv` 的目标行将该论文标为 `no_public_source_found`，候选列为空；`corpus/visual_sources/icml-2026-159ec0c7baad/` 不存在。PDF 首页、脚注、正文和参考文献没有作者 GitHub、project 或 code URL；正文 p.6 只给出实验/实现描述，附录 p.11-12 也没有代码链接。
- 按协议用 `gh` 只读检索完整标题、方法名 `EcoVLA` 和 `EcoVLA VLA pruning`。严格标题检索无结果；方法名检索得到 `https://github.com/Echo-hyt/Ecovla`。`gh repo view` 显示公开仓库、默认分支 `main`、未归档；README 的项目标题逐字为 **EcoVLA: Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models**，并明确写作 official implementation，因此与论文建立了直接标题关系。
- `gh api repos/Echo-hyt/Ecovla/git/trees/main?recursive=1` 的完整树只有 `README.md`；README 声明实现仍在整理、尚未公开。没有 `plot*`、`figure*`、`visual*`、`table*`、`.ipynb`、`.tex`、`.tikz`、`.pgf`、`.svg`、style 或数据文件。主分支当前 commit 为 `ad59e60f34e19b8fd14c9dea6b0ae1d386b5ae18`，README blob 为 `303a3f5de30b15a47a1d58524096d089a3c06521`。
- 因此源状态为 **`repository_without_visual_source`**：有经标题和 README 严格验证的官方仓库，但没有可登记的公开绘图脚本、表格生成器或可编辑图源；所有 Figure 的颜色/字号/线宽均来自 PDF 对象或渲染估计，不能写成 `source_exact`。

## 全文视觉风格

- **版式**：正文与参考文献采用双栏 letter 模板。Figure 1 是摘要右侧的单栏小图；Figure 2 是跨两栏页宽方法图；p.7 以页宽连续排放 Table 1-3，左栏下方为 Table 4/Figure 3，右栏为 Figure 4；p.8 是 Figure 5/Table 5 左栏与 Figure 6 右栏；附录 p.11-12 为单栏文字和硬件照片。对象顺序遵循“动机 - 方法 - 主结果 - 分解/权衡 - 真实硬件”。
- **字体**：页面 PDF 字体对象包含 Nimbus Roman No9 L、TimesNewRomanPSMT/TimesNewRomanPS-BoldMT、Computer Modern Roman/Math 及少量等宽数学字体。Figure 1、Figure 2、Figure 3、Figure 4、Figure 5-6 和 Figure 7 的图内字号有部分由嵌入栅格图烘焙，按渲染观测估计；表格正文和表头可由 PDF 字体对象核对，约 7.5-10 pt，数学符号使用 Computer Modern。
- **颜色**：Figure 1 使用紫色 attention-head 与橙黄色 MLP channel 两条顺序热图；Figure 2 使用黄/橙、蓝、绿、红的流程阶段色；Figure 4 使用淡紫/淡蓝/浅绿/浅黄区分延迟增量；Figure 5 使用蓝色 success 与橙色 speedup；Figure 6 使用橙色 α 与紫色 p。Table 1-5 为黑白 booktabs。除 Figure 5 的线型/marker 和 Figure 6 的柱+线+数值标签外，颜色仍是主要类别通道，整体灰度安全性有限。
- **矢量/栅格**：`pdfimages -list` 报告 p.1 有 2 个大 JPEG heatmap，p.3 有大量 JPEG 流程片段和图标，p.7 有 3 个机器人照片与 1 个延迟图 JPEG，p.8 有 Figure 5-6 的 3 个图表 JPEG，p.12 有硬件照片/产品图 3 个 JPEG。caption、表格文字、部分框线和箭头仍是 PDF 矢量，因此 Figure 1/3/4/5/6/7 记为 raster 或 mixed，Figure 2 记为 mixed；没有公开源可追溯到作者的绘图参数。
- **一致性**：caption 均置于对象下方、标签斜体，表格均采用横线式表格；主结果表统一使用 success/FLOPs/latency/speedup 的方向箭头。图形子系统之间的配色并不完全统一：Figure 5 的蓝/橙与 Figure 6 的橙/紫来自不同实验问题，Figure 2 的流程色没有在结果图中复用。双栏缩放后 Figure 4-6 的图内小字和 Figure 2 的高密度流程标签是主要可读性瓶颈。

## Figure 1 - 动态重要性热图

- **位置与职责**：p.1，摘要右侧、§1 Introduction 开始处，单栏宽，约 bbox `[330, 205, 532, 330]` pt。类型为 `heatmap`；用途为 `headline`、`mechanism`。上半部为 Attention Head Importance Score，下半部为 MLP Channel Importance Score，纵向箭头为 Inference Time。
- **面板与布局**：两个上下堆叠的规则色块矩阵，共享“随推理时间变化”的纵向阅读方向；没有数值刻度、颜色条或明确横轴。每个矩阵由多列时间片和若干行通道/头的色块组成，矩阵外有细黑边框，两个面板中间直接放置标题。
- **绘图语法**：栅格化热图；`x` 无可读尺度，`y` 为时间方向但未标定；无网格线、无 legend、无 marker、无 line data、无 reference line 和不确定性显示；直接标签为两个矩阵标题和 `Inference Time`；线宽约 0.8-1 pt（渲染估计）。`rendering=raster`，其余完整 grammar 见 JSON。
- **Typography**：图内 serif 字形接近 Times/Computer Modern；约 8-11 pt，regular roman；字号和字体烘焙进两个 JPEG，`provenance=rendered_estimate`、confidence medium。
- **颜色**：上图为淡紫到深紫顺序 ramp（代表色约 `#D8D7E9`, `#8E83BE`, `#3F087D`），下图为淡黄到橙色顺序 ramp（代表色约 `#FFF1D7`, `#FCD27E`, `#D88420`）。颜色深浅看起来编码 importance，但图注未定义色标、数值范围或统一量纲；`mode=mixed` 的两条顺序 ramp，灰度下两种语义容易混淆，颜色没有形状冗余。
- **数据与统计**：这是说明动态稀疏转移的定性热图，不是带可读数值的实验统计。图中未给模型、时间步、通道/头数量、聚合方式、重复次数、分母、失败值或不确定性；正文 p.1 §1 只把它引用为“optimal sparsity patterns vary dynamically”。
- **Caption（PDF 逐字，22 个空白分词）**：
  > Figure 1. During VLA execution, channel importance scores vary dynamically as the environment evolves, causing the optimal sparsity pattern to shift accordingly.

  caption moves=`title, main_finding`；没有粗体结论标题，`headline_bold=false`；直接写出动态变化和稀疏模式转移，`main_finding_stated=true`；由于没有模型、色标、时间/通道定义，`self_contained=false`。
- **证据关系**：p.1 Abstract 的环境变化与静态 pruning 缺口 -> p.1-2 §1 的 dynamic sparsity shifts -> Figure 1 的动机观察 -> p.3-5 Eq. (5)-(11) 的 EAP 触发/时间一致性机制 -> Figure 6 的 α/p sensitivity。它是机制动机而非性能证据。
- **优点**：上下两种内部结构共享时间方向，快速表达“attention head 与 MLP channel 都会变化”；紧邻摘要和正文动机，读者能直接将热图与后续 EAP 连接。
- **缺陷**：没有颜色条、数值轴、来源样本或色标定义，深浅只能作方向性印象；两套顺序色在灰度和投影下不易区分；图注没有说明热图是否来自真实轨迹、哪个模型或如何计算。
- **可复用模式**：用两个同宽热图对齐同一时间轴来表达结构变化；正式结果应补统一色标、模型/样本来源和可比较的横纵刻度，并用纹理或直接标签提高灰度可读性。

## Figure 2 - EcoVLA 方法总览

- **位置与职责**：p.3，§4 Methodology 开头，页宽跨两栏，约 bbox `[68, 55, 545, 420]` pt。类型为 `pipeline`、`architecture`、`conceptual_diagram`；用途为 `method_interface`、`theory_mechanism`。
- **面板与布局**：上半部 `(a) Environment-aware Adaptive Pruning (EAP)` 从 Visual Observation/Instruction 经 Vision Encoder、Sparsity Variations Predictor 和 Temporal Consistency Pruning，经过 Sparse LLM 和 Action Head 生成 Robot Action；上方的 VLA Sequential Execution 画出多个连续 frame 与 sparsity changes，左上还显示 Reuse Sparsity Pattern/no changes。下半部 `(b) Interleaved Inference Orchestration (I2O)` 用三条横向带表现 Inference Stream、Shared Memory Interface、Pruning Stream；VLM Backbone/Action Expert 的 high/low FLOPs 片段与 Sparsity Pattern Compute 对齐，并通过 `Sparse Load & Dense Weight` 和箭头表达共享内存。
- **绘图语法**：混合栅格片段、矢量箭头/边框和文字；无坐标轴与网格；底部为一个跨下半部的共享图例，解释 High FLOPs、Low FLOPs、Lower FLOPs、Dense Inference、Sparse Inference、Compute、Data Transfer、Load Weight；直接标签贯穿所有流程节点；约 3 种线型（实线、虚线、点线/虚线边界），有 hatch 表示 sparse/dense block，箭头线宽约 1 pt；无 reference line、error bar、band 或其他不确定性。
- **Typography**：图内 serif/Computer Modern 与数学符号混排；模块标题、panel 标题约 8-11 pt，细节标签约 5.5-8 pt，regular/bold/italic roman 混合，`rendered_estimate`、confidence medium。图注中 EAP/I2O 组件名加粗，但图内字号来自图形资产，不能视为源精确值。
- **颜色**：约 10 个代表色：`#FFF1C5`、`#F3D06A`（low/high FLOPs 与 action blocks）、`#DCE8F2`、`#9CB4D3`（共享内存与 backbone）、`#72B947`（稀疏节点）、`#E89050`（temporal pruning）、`#F18A86`（Action Head）、`#8A4D2D`（强调标题）、`#8A8987`（箭头/边界）、`#FFFFFF`（留白/图例）。颜色是流程阶段/计算状态的类别编码，文字、箭头和位置提供部分冗余，但整体灰度安全性有限。
- **数据与统计**：概念性算法接口，不提供实验数值、样本量、延迟、FLOPs 分母、重复或不确定性；公式片段在图内只作为 `historical/instantaneous/fusion feature` 的机制提示。p.5 Eq. (13) 才给出串行 `L_synch` 与 I2O `L_I2O` 的延迟关系，图本身不承诺数值比例。
- **Caption（PDF 逐字，72 个空白分词）**：
  > Figure 2. Overall pipeline of EcoVLA. (a) Environment-aware Adaptive Pruning (EAP): EAP is a lightweight, environment-aware method that identifies sparsity variations by perceiving real-time dynamics. Considering the temporal consistency of VLA execution in physical environments, EAP integrates instantaneous features with historical features to jointly compute the sparsity pattern. (b) Interleaved Inference Orchestration (I²O): I²O interleaves sparsity pattern computation into the inherent FLOPs bubbles within the VLA inference using a non-blocking parallel paradigm.

  caption moves=`title, setup, encoding_key`；说明 EAP/I2O 组件、历史/瞬时特征和 FLOPs bubbles，但没有单独粗体标题或数值结论，`headline_bold=false`、`main_finding_stated=false`、`self_contained=true`（方法职责在 caption 中已定义，流程细节由图内标签补充）。
- **证据关系**：p.2 §1 的两个挑战 -> p.3-5 §4.1 EAP 和 §4.2 I2O -> Figure 2 的两段式接口 -> Table 5/ Figure 4 的 overhead 与加速分解 -> Figure 5/ Tables 1-3 的结果。它是整篇视觉叙事的方法锚点。
- **优点**：上半部把环境感知、时间融合和稀疏模型放在因果流中，下半部把计算/内存时间关系转成并行流；图例同时解释计算强度、推理状态和数据传输，方法组件与硬件执行紧密相连。
- **缺陷**：信息密度很高，5-8 pt 标签在双栏投影中偏小；上下部分别使用时序流和资源流，阅读方向切换成本较高；没有显示真实时间比例、触发频率或并行冲突边界，容易把概念箭头误读为定量调度保证。
- **可复用模式**：将“算法触发/状态更新”和“硬件流/共享内存”分为上下同宽面板，并用同一组箭头与计算状态图例连接；可复用版本应再加最小时间轴和阻塞条件。

## Table 1 - OpenVLA-OFT 主结果

- **位置与结构**：p.7，§5.2 Main Results 上半部，页宽，约 bbox `[78, 70, 535, 355]` pt。用途为 `headline`、`main_comparison`、`robustness`。共 11 个数据行、9 列：`Method`；Success Rate (%) 的 5 列（LIBERO-Spatial、LIBERO-Object、LIBERO-Goal、LIBERO-Long、Average）；FLOPs (T) ↓；Latency (ms) ↓；Speedup ↑。两级表头，Success Rate 横跨 5 列；3 个 row group（未剪枝基线、Pruning Ratio 25%、Pruning Ratio 40%）。
- **数据与高亮**：未剪枝组 3 行：Vanilla、FastV、VLA-Cache；25% 和 40% 组各 4 行：Wanda、Ours、FastV + Ours、VLA-Cache + Ours。Success Rate 为一位小数，FLOPs/Latency/Speedup 为两位小数，FLOPs 括号还给相对 dense 百分比。可读的关键值包括 Vanilla `96.7 / 4.05 (100.0%) / 143.56 (162.78) / 1.00x`，25% Ours `96.8 / 3.23 (79.75%) / 113.98 / 1.26x`，25% FastV + Ours `96.2 / 1.96 (48.39%) / 65.85 / 2.18x`，40% Ours `94.0 / 2.74 (67.65%) / 101.58 / 1.41x`，40% FastV + Ours `92.9 / 1.64 (40.49%) / 61.16 / 2.35x`。`Ours` 与组合方法行名加粗；没有误差条、区间或重复统计。
- **版式与字体**：booktabs 式顶/组间/底部横线，Method/Success/FLOPs/Latency/Speedup 间有竖直分隔，row group 标签为斜体。表格正文和表头约 7.5-8.5 pt，Times New Roman/Nimbus Roman 与 Computer Modern math，header weight mixed，`provenance=pdf_object`、confidence high。
- **Caption（PDF 逐字，15 个空白分词）**：
  > Table 1. Performance of EcoVLA on OpenVLA-OFT in LIBERO at 25% and 40% pruning ratio.

  caption moves=`title, setup`；没有粗体结论标题，`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。
- **不确定性与证据关系**：成功率/FLOPs/latency/speedup 都是点估计，表中没有 seed、episode 数、SD/SE、区间或失败计数；Table 1 承接 p.6 的两个 simulator/三模型实验设置，支撑 p.7-8 关于 1.26x、2.18x 和 2.35x 的主比较，Figure 4 分解其 latency，Figure 5 检查 pruning-ratio trade-off。
- **优点**：将成功率、计算量、延迟和 speedup 放在同一决策面；未剪枝、单独 model pruning、FastV/VLA-Cache 组合和两个 pruning ratio 的行组能直接检验正交组合主张；方向箭头减少读者查找成本。
- **缺陷**：页宽表字号偏小，方法行名和多层指标使横向扫描负担较高；括号内 FLOPs 百分比的基准写在 cell 内而非表下注释；没有统计变异、episode 分母或硬件测量重复定义，无法判断小幅成功率差异的稳定性。
- **可复用模式**：用“baseline - own pruning - orthogonal combination”三段 row group，并把性能、FLOPs、latency、speedup 放在同一表；正式版本应在 caption 或脚注明确基准、重复和失败定义。

## Table 2 - π0.5 跨模型结果

- **位置与结构**：p.7，Table 1 下方，页宽，约 bbox `[76, 238, 535, 315]` pt。用途为 `main_comparison`、`robustness`。4 列方法结构列（Method、Sparsity）加 5 个 Success Rate (%) 列（四个 LIBERO suite 与 Average）及 FLOPs (T) ↓、Latency (ms) ↓、Speedup ↑，共 10 列；两级表头；2 个 row group（Vanilla 与 Ours）。
- **数据与统计**：3 个数据行：Vanilla 0%：`98.8, 98.2, 98.0, 92.4, 96.9, 1.99 (100.0%), 81.94, 1.00x`；Ours 25%：`98.2, 98.6, 98.4, 91.6, 96.7, 1.64 (82.41%), 62.66, 1.31x`；Ours 37.5%：`97.8, 98.4, 96.8, 87.0, 95.0, 1.47 (73.87%), 55.98, 1.46x`。成功率一位小数，其余数值两位小数；无误差、区间、重复或失败计数。Ours 方法标签加粗。
- **规则与字体**：booktabs 顶/中/底线，Method/Sparsity 与 Success/FLOPs 等区域有竖线分隔；正文/表头约 7.5-8.5 pt，Times/Nimbus Roman + Computer Modern math，header weight mixed，`provenance=pdf_object`、confidence high；无 cell color、underline 或 arrows 高亮。
- **Caption（PDF 逐字，15 个空白分词）**：
  > Table 2. Performance of EcoVLA on π0.5 in LIBERO at 25% and 37.5% pruning ratio.

  caption moves=`title, setup`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。
- **证据关系与评价**：p.8 §5.2 的 `Results on π0.5` 以此表闭合跨模型泛化和 1.31x/1.46x 加速主张；正文指出 LIBERO-Object 在 37.5% 出现 0.2% 改善，并将其解释为 pruning 的 regularization，但表中没有统计不确定性。优点是以同一 suite/metric 合同复用 Table 1，缺点是表头拥挤且 p.7 小字号下 37.5% 行与基线差异不易追踪；可复用模式是保留一条 dense baseline 和多个 pruning levels，同时把模型特有比例写入 caption。

## Table 3 - CogACT / SIMPLER 结果

- **位置与结构**：p.7，Table 2 下方，页宽，约 bbox `[75, 320, 535, 420]` pt。用途为 `main_comparison`、`robustness`。11 列：SIMPLER suite/group、Method、Sparsity；Pick Coke、Move Near、Open/Close、Open Top、Average 五个 Success Rate (%) 列；FLOPs (T) ↓、Latency (ms) ↓、Speedup ↑。两级表头，2 个 row group（Visual Matching、Variant Aggregation），每组 Vanilla/ours 25%/ours 40% 共 6 行。
- **数据与统计**：Visual Matching：Vanilla `93.3,83.8,74.5,41.7,73.3,1.81 (100%),104.16,1.00x`；ours 25% `95.0,82.1,70.8,38.9,71.7,1.45 (80.11%),72.65,1.44x`；ours 40% `93.0,85.4,73.5,42.6,73.6,1.25 (69.06%),66.43,1.57x`。Variant Aggregation：Vanilla `88.7,76.8,26.7,51.9,61.0,1.81 (100.0%),105.87,1.00x`；ours 25% `85.9,75.3,27.2,46.0,58.6,1.47 (81.22%),73.98,1.43x`；ours 40% `86.1,74.3,33.1,48.7,60.6,1.28 (70.72%),66.25,1.60x`。成功率一位小数，其余数值两位小数；方法标签 `ours` 加粗但没有 best/second-best cell 标记；无误差或分母之外的 trial 信息。
- **规则与字体**：booktabs 横线和组间横线，SIMPLER/Method/Sparsity 与指标区有竖线；约 7-8 pt，Times/Nimbus Roman + Computer Modern，header weight mixed，`provenance=pdf_object`、confidence high。颜色、阴影、下划线均未使用。
- **Caption（PDF 逐字，15 个空白分词）**：
  > Table 3. Performance of EcoVLA on CogACT in SIMPLER at 25% and 40% pruning ratio.

  caption moves=`title, setup`；`headline_bold=false`、`self_contained=true`、`main_finding_stated=false`。
- **证据关系与评价**：p.8 `Results on CogACT` 用此表回答跨架构/跨 SIMPLER 场景泛化，正文引用 1.57x 与 1.60x 以及 0.3%/0.6% 成功率变化；它把 Table 1-2 的 LIBERO 证据扩展到不同模型和任务。优点是两种 SIMPLER 模式并列，能看到 25% 到 40% 的效率-性能变化；缺点是短任务名在 11 列表头中拥挤，组内行名大小写不一致（Vanilla/ours），缺少 episode 数和统计变异；可复用模式是对多环境套件使用相同指标列、把环境子集作为 row group。

## Table 4 - 真实机器人计数

- **位置与结构**：p.7 左栏下部、Figure 3 上方，约 bbox `[75, 432, 405, 505]` pt，单栏宽。用途为 `main_comparison`、`robustness`。2 个数据行、5 列：Method、Task1、Task2、Task3、Latency(ms)；一级表头；无额外 row group。Task1-3 的自然语言名称在紧邻 Figure 3 的三个照片标签中给出，而表头本身没有展开任务名。
- **数据与统计**：baseline：`12/20, 18/20, 16/20, 86.08`；Ours：`12/20, 16/20, 15/20, 68.40`。前三列是 20 次试验中的成功计数，延迟为毫秒点值；没有成功率换算、置信区间、失败原因或每次延迟分布。Appendix B p.12 说明物体位置每次随机化并指出 workspace 边界附近是主要失败位置。
- **规则与字体**：booktabs 顶/中/底横线和列间竖线，正文约 9.5 pt、表头约 10 pt，Times/Nimbus Roman + Computer Modern，header weight regular/bold mixed，`provenance=pdf_object`、confidence high；无颜色、best/highlight 或不确定性。
- **Caption（PDF 逐字，11 个空白分词）**：
  > Table 4. Performance of EcoVLA on π0.5 on a real-world robot.

  caption moves=`title, setup`；`headline_bold=false`、`self_contained=false`（Task1-3 需要 Figure 3/正文恢复语义）、`main_finding_stated=false`。
- **证据关系与评价**：p.6-7 §5.1 的 Kinova Gen3 设置 -> Table 4 的三任务成功计数/latency -> Figure 3 的任务照片 -> Appendix B 的 20 个随机位置与失败边界分析。优点是把成功分子和端到端延迟放在同一行，真实部署结果易于核对；缺点是任务名没有进入表头，baseline/Ours 的性能差异不能只靠 caption 理解，计数也没有说明失败定义或重复测量；可复用模式是将 `/20` 原始计数保留在主表并在表头展开任务名。

## Figure 3 - 真实机器人任务照片

- **位置与职责**：p.7 左栏、Table 4 下方，约 bbox `[75, 505, 405, 600]` pt。类型为 `image_montage`、`qualitative_grid`；用途为 `qualitative_evidence`。三个等宽照片从左到右显示 apple-in-basket、pill-bottle-in-cabinet、banana-in-basket，照片下方直接给出粗体两行任务标签。
- **绘图语法**：三 panel 横向定性 montage，无坐标、网格、legend、marker、line data、hatching、reference line 或不确定性；direct labels=true（任务文字），边框/间隙约 0.5-1 pt；照片 JPEG 与矢量文字混合，`rendering=mixed`。
- **Typography 与颜色**：任务标签为 Times/Nimbus Roman bold，约 8-10 pt，照片本身不承载可测量文字；自然 RGB 摄影没有数据调色板，颜色仅呈现木桌、机械臂和红/黄物体，`mode=not_applicable`、`color_count=0`、`grayscale_safe=false`（灰度仍能识别场景，但不应将物体颜色当作编码）。图内字号来自 PDF text object/渲染共同观察，`provenance=rendered_estimate`、confidence medium。
- **数据与统计**：三张照片是任务实例的定性证据，不是三次独立统计；Table 4 的 Task1-3 `/20` 计数和 p.12 Appendix B 的随机位置/失败分析才提供评测分母和结果。图中没有 success/failure overlay、时间点、轨迹或不确定性。
- **Caption（PDF 逐字，8 个空白分词）**：
  > Figure 3. Robot Manipulation on Kinova Gen3 Platform.

  caption moves=`title, setup`；`headline_bold=false`、`self_contained=true`（平台和三张任务照片可由图内标签识别）、`main_finding_stated=false`。
- **证据关系与评价**：§5.1 真实机器人设置 -> Table 4 计数/latency -> Figure 3 作为视觉确认 -> Appendix B 的边界失败机制。优点是三项任务同构排列，读者可将照片标签与表格任务行直接对应；缺点是照片没有时间、成功状态或操作轨迹，无法独立证明 success rate，图注也没有说明每张图是代表性帧；可复用模式是用固定宽度三 panel 对齐任务名称，并在正式版本用编号/状态标记连接 raw count。

## Figure 4 - Dense/sparse 延迟分解

- **位置与职责**：p.7 右栏下部，约 bbox `[300, 430, 535, 600]` pt。类型为 `bar`；用途为 `ablation`、`efficiency_cost`、`mechanism`。单面板、两根 stacked bar：Dense Inference 与 Sparse Inference。
- **面板与编码**：纵轴 `Time (ms)`，0-300 的线性刻度，水平虚线网格；横轴为两类 inference。Dense bar 从底部 `Final Latency 148.06`，向上依次为 `+ Batched Metric Computation 21.14`、`+ Allocation-Free Caching 10.00`、`+ Parallel Paradigm 36.04`，总 `Original Latency 215.24`。Sparse bar 为 `Final Latency 108.24`、`+ Kernel Fusion 1.76`、`+ Memory coalescing 13.49`、`+ Sparse Linear Transformation Kernel 32.63`，总 `Original Latency 156.12`。每段和总值均直接标注；上方有 Dense 与 Sparse 两个分开的 legend box。
- **绘图语法**：单 panel categorical x、linear y、y grid；legend_present=true，placement=`upper-left and upper-right, two semantic boxes`，shared_legend=false；direct_labels=true；无 marker、line series、hatching、reference line 或 uncertainty；stack outlines 约 0.5 pt，栅格图表主体来自 JPEG，`rendering=raster`、`provenance=rendered_estimate`。
- **Typography 与颜色**：图内粗体 serif 字形约 7-12 pt（轴标题与 legend 较大），regular/bold roman；`provenance=rendered_estimate`、confidence medium。约 8 个数据色：Dense 的淡紫 `#B9ADD1`、浅黄 `#F3E0A8`、浅绿 `#C0EFDB`、浅蓝 `#9BC4FA`，Sparse 的淡紫 `#CDC3E5`、浅黄 `#FBF7B2`、浅绿 `#B7EBD8`、浅蓝 `#BFDAF7`；同一层级通过 legend 文字而不是跨柱统一色值来解释，灰度安全性有限。
- **数据与统计**：延迟 breakdown 是单个测量点/组件增量，没有重复次数、SD/SE、区间或硬件时钟状态。p.8 §5.3 把 Dense 的 36.04/10/21.14 ms 与 Sparse 的 36.04/13.49/1.76 ms 解释为优化项，Table 5 用 143.56 vs 148.06 ms 补 pruning stream overhead。
- **Caption（PDF 逐字，9 个空白分词）**：
  > Figure 4. Acceleration breakdown for dense and sparse inference.

  caption moves=`title`；没有 setup、legend 定义或主发现，`headline_bold=false`、`self_contained=false`、`main_finding_stated=false`。
- **证据关系与评价**：§4.2 的 I2O/FLOPs bubbles 与 §4.3 Triton kernel -> Figure 4 的 dense/sparse 分层优化 -> Table 5 的 end-to-end overhead -> Table 1 的 speedup。优点是段内数值标签让每个优化增量可加总，Dense/Sparse 双 legend 分清语义；缺点是两个 legend 的色值并非完全共享，正文/图注没有说明测量基准和总值关系，stack 段很薄时标签拥挤；可复用模式是以 cumulative stacked bar 展示优化链，但应统一颜色语义并注明 measurement protocol。

## Figure 5 - Pruning ratio 的性能-效率权衡

- **位置与职责**：p.8 左栏上部，约 bbox `[65, 65, 300, 175]` pt。类型为 `line`；用途为 `ablation`、`efficiency_cost`、`robustness`。单 panel 双 y 轴：左轴 `Success Rate (%)`，右轴 `Speedup (X)`，横轴 `Pruning Ratio (%)`。
- **面板与编码**：x 为 0-90、每 10 个百分点一个观测，线性均匀排列；蓝色圆点实线编码 success，橙色方点虚线编码 speedup；左 y 约 0-100，右 y 约 1.0-4.0。40% 处有竖向灰色虚线，图内文字 `Efficiency Plateau`；水平/垂直白色点线网格，legend 位于右上。success 在 40% 以下保持高位、超过 40% 后快速下降，speedup 单调上升；图注未直接写出阈值结论。
- **绘图语法**：栅格图表，`x_scale=linear`、`y_scale=linear`（双 y 轴），`grid=both`；legend upper-right，非共享；direct_labels=true（Efficiency Plateau 文字）；marker_types=2（circle/square），line_styles=2（solid/dashed），hatching=false，reference_lines=1，uncertainty=none，线宽约 1.8 pt；`provenance=rendered_estimate`。
- **Typography 与颜色**：Times/Nimbus-like bold serif，图内约 6.5-10 pt，轴标题与 legend 较粗，`rendered_estimate`、confidence medium。数据色为蓝 `#5B9BD5` 和橙 `#ED7D31`，背景淡紫 `#F0F0FC`、网格白；颜色与线型/marker 有冗余，灰度下仍可区分两条线。
- **数据与统计**：绘制同一模型在 pruning ratio 0-90% sweep 的 success rate 和 speedup 点估计；没有 error bar、band、episode 数、seed 或速度测量重复。p.8 §5.3 将 40% 描述为较优 trade-off，并说 40% 之后 success 快速恶化。
- **Caption（PDF 逐字，8 个空白分词）**：
  > Figure 5. Trade-off between Success Rate and Latency.

  caption moves=`title`；`headline_bold=false`、`self_contained=false`（双 y 轴、线型和 40% reference line 依赖图内元素）、`main_finding_stated=false`。
- **证据关系与评价**：Table 1 的多 ratio 结果 -> Figure 5 的连续 sweep -> p.8 §5.3 的 40% trade-off 结论 -> Appendix A.3 的实际 p/α 设置。优点是双轴叠加直接呈现效率-性能拐点，线型和 marker 对颜色提供冗余；缺点是 caption 把 speedup 称为 latency trade-off 但没有定义基线，双 y 轴可能夸大视觉斜率，所有点无不确定性；可复用模式是将性能和速度放在同一 ratio sweep 中，并明确双轴、基线和停止阈值。

## Table 5 - Pruning stream overhead

- **位置与结构**：p.8 左栏 Figure 5 下方，约 bbox `[90, 188, 300, 245]` pt，单栏窄表。用途为 `efficiency_cost`、`ablation`。2 个数据行、2 列：Execution Method、Latency (ms)；一级表头、无 row group。`Normal VLA Inference=143.56`，`I2O=148.06`，差值为 4.50 ms。
- **规则与字体**：booktabs 顶/中/底横线，Execution Method 与 Latency 间有竖线；body/header 约 9.5/10 pt，Times/Nimbus Roman + Computer Modern，header weight bold，`provenance=pdf_object`、confidence high；无高亮、颜色或不确定性。
- **Caption（PDF 逐字，6 个空白分词）**：
  > Table 5. Overhead of Pruning Stream.

  caption moves=`title`；`headline_bold=false`、`self_contained=true`（列标题给出 execution method 与 ms 单位）、`main_finding_stated=false`。
- **数据与统计、证据关系**：这是两种执行范式的单点 latency 对照，不给重复/seed/硬件状态或误差；p.8 §5.3 由此把 pruning stream overhead `δ` 限定为 4.5 ms，并与 Figure 2 的 non-blocking stream、Figure 4 的 dense final latency 和 Table 1 的 speedup 相连。优点是极简、差值可直接计算；缺点是没有把 baseline、context length、model 或测量次数写进表，不能单独判断 4.5 ms 的适用范围；可复用模式是为系统开销保留两行同单位对照，但必须补 benchmark 条件。

## Figure 6 - α 与 p 的超参数分析

- **位置与职责**：p.8 右栏上部，约 bbox `[325, 65, 535, 220]` pt。类型为 `bar`、`line`；用途为 `ablation`、`mechanism`、`robustness`。两个上下 panel，无 legend：`(a) Temporal Inertia Parameter` 对 α，`(b) Sensitivity Parameter` 对 p。
- **面板与编码**：两个 panel 的 y 都是 `Success Rate (%)`，显示范围约 70-90；每个条件是一个浅色柱并叠加同色圆 marker 折线，数值直接写在 marker 上。上 panel α 为 0.0-1.0、步长 0.1，橙色；可见 success rate 依次为 `79.8,81.2,80.2,82.4,83.4,83.6,80.8,87.0,82.6,80.0,80.6`，峰值在 α=0.7。下 panel p 为 `5,10,20,30,40,50,60,70,75,80,85,90`，紫色；success rate 为 `78.8,78.4,78.4,75.6,80.4,77.4,80.0,80.0,82.0,87.0,81.2,82.8`，峰值在 p=80。两 panel 具有水平/垂直白色点线网格，x 为 categorical 条件而非连续曲线。
- **绘图语法**：`rendering=raster`；`x_scale=categorical`、`y_scale=linear`、`grid=both`；legend=false、shared_legend=false；direct_labels=true（全部数值与 panel title）；marker_types=1（circle），line_styles=1（solid），hatching=false，reference_lines=0，uncertainty=none，线宽约 1.3 pt；`provenance=rendered_estimate`。
- **Typography 与颜色**：图内粗体 serif，约 6.5-10 pt，regular/bold roman，`rendered_estimate`、confidence medium。α panel 代表色约 `#FFCA92`/`#E8A14A`，p panel 约 `#C4B9E1`/`#76689E`；柱、线、marker 和数值标签提供冗余，灰度下结构可读但两 panel 色语义会减弱。
- **数据与统计**：两组 success-rate 点估计在 π0.5 上评估；Appendix C p.12 指明 α 分析对应 LIBERO-Long，p 分析对应环境动态灵敏度，论文没有报告 trial 数、seed、重复或误差。图支持“中等 α、p=80% 峰值”的参数选择，但不提供对峰值差异的显著性判断。
- **Caption（PDF 逐字，8 个空白分词）**：
  > Figure 6. Impact on Hyperparameters α and p.

  caption moves=`title`；`headline_bold=false`、`self_contained=false`（α/p 的任务和评测设置在 Appendix C）、`main_finding_stated=false`。
- **证据关系与评价**：§4.1.1-4.1.2 的 quantile trigger/temporal fusion -> Figure 6 的 α/p sweep -> Appendix A.3 实际参数 -> Appendix C 对峰值和噪声/历史滞后的解释。优点是直接标签和柱+线组合同时暴露数值与趋势；缺点是 y 轴截断到 70-90 会放大差异，caption 没有任务/模型/实验分母，双 panel 颜色体系不与 Figure 5 共享；可复用模式是给关键超参用离散 sweep、数值标签和同尺度 panel，但应显式说明截断轴和不确定性。

## Figure 7 - Kinova Gen3 硬件设置（附录）

- **位置与职责**：p.12，Appendix A.4 Real-Robot Setup 顶部，页宽内居中，约 bbox `[205, 65, 530, 275]` pt。类型为 `image_montage`、`conceptual_diagram`；用途为 `experimental_design`、`qualitative_evidence`。主照片显示 Kinova Gen3 在桌面工作区，右侧为 Kinova Gen3 与 Intel RealSense D435i 的产品图；红/橙色框和连接线把主照片中的机械臂、末端/相机位置映射到右侧标签。
- **绘图语法**：混合栅格照片/产品图与矢量连接框和文字；无坐标、网格、legend、marker、hatching、reference line 或不确定性；direct_labels=true，连接线约 1.2-1.5 pt；`rendering=mixed`，x/y 均为 none。
- **Typography 与颜色**：图内标签为 Times/Nimbus-like regular，约 7-10 pt，`rendered_estimate`、confidence medium。照片为自然 RGB，不存在数据调色板，`mode=not_applicable`、`color_count=0`、`hex=[]`、`grayscale_safe=false`；红/橙框只承担硬件定位，不是数值类别编码。
- **数据与统计**：硬件文档图，不提供成功率、延迟、样本、重复或不确定性；附录 A.4 文字定义两台 RealSense D435i 的 third-person/wrist 角色，Appendix B p.12 给出 20 个随机 object placements，Table 4 给出真实任务计数和 latency。
- **Caption（PDF 逐字，6 个空白分词）**：
  > Figure 7. Kinova Gen3 Robot Setup.

  caption moves=`title`；`headline_bold=false`、`self_contained=false`（摄像机角色和训练/评测条件在附录正文）、`main_finding_stated=false`。
- **证据关系与评价**：Appendix A.4 的硬件说明 -> Figure 7 的设备/相机空间对应 -> Table 4/ Figure 3 的真实机器人结果 -> Appendix B 的边界失败分析。优点是主照片与硬件 cutout 通过连接线建立了明确的部署接口；缺点是相机视野、坐标系、时间同步和控制频率没有图示，产品 cutout 与实拍尺度不一致；可复用模式是用主场景加带标注的设备 inset 记录实验硬件，但应补视野/坐标或在 caption 中说明用途。

## 跨对象系统判断

- **Visual narrative**：Figure 1 先把环境变化转成 attention/MLP 重要性 shift；Figure 2 给出 EAP 的时间融合和 I2O 的并行资源接口；Tables 1-3 用三种 VLA/两种 benchmark 兑现 success-FLOPs-latency-speedup；Table 4 与 Figure 3 把结果移到 Kinova Gen3；Figure 4 分解加速来源，Figure 5 找到约 40% pruning 的效率-性能拐点，Table 5 量化 pruning stream overhead，Figure 6 给出 α/p 选择，Figure 7 补硬件复现边界。主线从动机到部署较完整。
- **Caption system**：所有 caption 采用 `Figure/Table n.` + 描述性标题；Figure 2 唯一承担较长的 setup/encoding key，Figure 1 把方向性主发现写入 caption，其余 Figure 多为短标题。Tables 1-4 的 caption 说明模型/benchmark/剪枝比例，Table 5 仅说明 overhead；大多数 caption 没有样本分母、seed、误差定义或 measurement protocol。
- **Table-header system**：Table 1-3 采用 grouped Success Rate header 和方向箭头，将套件/任务 Average 与 FLOPs、Latency、Speedup 并列；Table 4/5 改为单级简表。表头单位和方向总体明确，但 Table 4 的 Task1-3 未展开，Table 1-3 的括号百分比基准依赖正文/读者推断。
- **Method-result-ablation link**：Figure 2 的 EAP/I2O 接口对应 Figure 4 的 kernel/bubble breakdown 与 Table 5 的 δ；Figure 1 的动态重要性动机对应 Figure 6 的 temporal inertia/sensitivity；Tables 1-3 提供主比较，Figure 5 连续 sweep 检查 ratio trade-off，Table 4/Figure 3/7 构成真实机器人证据。
- **Main-appendix link**：正文 p.6-8 将真实机器人设置和超参数分析指向 Appendix A-C；Figure 7 在 A.4 闭合硬件，Appendix B 解释 Table 4 的边界失败，Appendix C 解释 Figure 6 的 α/p 峰值。附录没有额外 Table，但补足了任务分母、位置随机化和相机角色。
- **Typography consistency**：表格和正文共享 Times/Nimbus Roman/Computer Modern，caption 风格稳定；Figure 1-2 的图内字体与 Figure 4-6 的栅格图字体大小/字重不同，Figure 2 与 Figure 6 的细节字号最容易在双栏缩放下丢失。
- **Color consistency**：颜色在每个对象内部语义明确，但没有跨对象全局 token：Figure 5 蓝/橙是 success/speedup，Figure 6 橙/紫是 α/p，Figure 2 的橙/绿/蓝是流程/资源状态。Figure 5 通过 marker/line style，Figure 6 通过柱/线/数值标签提供冗余；热图和照片没有统一灰度方案。

## 最终判断

- **最可复用模式**：
  1. 用 Figure 1 的双热图建立动态稀疏动机，再用 Figure 2 上下分栏分别表示算法状态流与硬件资源流。
  2. 用 Tables 1-3 的 grouped header 将 success、FLOPs、latency、speedup 置于同一决策面，按模型/环境 row group 展开外推边界。
  3. 用 Figure 4 的 cumulative stacked bar 拆分优化来源，用 Figure 5 的性能-速度双轴 sweep 显示操作点，再用 Table 5 量化并行 stream 的残余开销。
  4. 用 Figure 6 的离散超参 sweep 和 Figure 7 的设备 inset 将机制选择与真实部署接口接上；正式复现需保留 Appendix B 的原始 `/20` 计数和失败位置。
- **最高价值对象**：Table 1（主决策面最完整）、Figure 2（方法与硬件接口最集中）、Figure 4（优化增量可加总）、Figure 5（40% trade-off 的直接证据）、Table 4/Figure 7（真实机器人复现边界）。
- **失败模式**：Figure 1 没有色标/数值尺度；Figure 2 信息密度高且没有时间比例；Figure 4-6 的图注过短；Tables 1-5 和 Figure 5-6 没有误差/seed/episode 分母；Figure 5 双 y 轴和 Figure 6 截断 y 轴可能放大差异；Table 4 的 Task1-3 依赖 Figure 3 才能解码；官方 GitHub 仓库当前只有 README，没有可复用绘图/表格源。
- **一句话视觉策略**：论文用“动态热图建立稀疏动机、双层流程图解释 EAP/I2O、统一性能-成本主表和逐层效率/超参补图推进到真实机器人”的视觉层级承载 EcoVLA 主张，但量化不确定性、轴/图注自洽性和公开视觉源缺口限制了可审计复现。

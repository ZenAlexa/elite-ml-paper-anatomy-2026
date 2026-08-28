# Visual audit — `icml-2026-c65beb96fda3`

## 范围、事实源与完整对象清单

- **论文**：*Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning*（Tung M. Luu、Hwanhee Kim、Younghwan Lee、Chang D. Yoo；KAIST）。
- **PDF 事实源**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/preprints/icml-2026-c65beb96fda3.pdf`；`pdfinfo` 显示 23 个 letter 物理页（612×792 pt，PDF 1.7，arXiv GenPDF）。主文完整页为 1–8，第 9 页下部/左栏收束正文且右栏进入 references；references 跨 9–13；Appendix 从 14 至 23。
- **渲染与视觉检查**：全部 23 页用 `pdftoppm -r 200 -png` 渲染为 1700×2200 px/页（200 dpi，超过 180 dpi）；逐页检查 `/tmp/icml-c65-work/contact.png` 及 `/tmp/icml-c65-pages/` 的高分辨率页，另外对含对象页 4、6–8、14–20、22–23 进行放大核对。字体/对象边界用 `pdffonts`、`pdftotext -layout` 交叉核对；下述颜色、线宽和字号若非 PDF 字体对象或源代码明确值均标为 `rendered_estimate`。
- **PDF 清单**：人工逐页核对得到 19 个 Figure（正文 Figure 1–7；附录 Figure 8–19）和 13 个 Table（正文 Table 1–3；附录 Table 4–13），共 32 个 Figure/Table 对象；Appendix 的 Algorithm 1（p.14）是独立伪代码对象，不计入 figures/tables。`readings/icml-2026-c65beb96fda3.json` 的 visual_inventory 与此标签/页码一致。
- **自动清单差异解释**：`reports/tables/visual_inventory_disagreements.csv` 对本论文写出 `pdf_caption_objects=0`、`reading_only=32`；这是自动 caption parser 未识别该 PDF caption 排版的解析失败，不是 PDF 缺图。人工 PDF 文字流和渲染结果逐一找到 Figure 1–19、Table 1–13，故 PDF 作为最终清单事实源。

## 公开视觉源与获取核查

- PDF 首页/摘要明确给出 `https://github.com/tunglm2203/votp`；OpenReview forum 为 `https://openreview.net/forum?id=G8LVO5easu`，project page 为 `https://votp2026.github.io`。`gh repo view tunglm2203/votp` 返回同名仓库、精确论文标题描述、默认分支 `main`、MIT license 和相同 homepage；README 也明确写出 official implementation、作者和 arXiv。
- 已用 GitHub API 读取递归 tree（1540 entries，未截断）并获取紧凑源文件：`README.md`、`assets/votp-overview.png`、`research/utils/plotter.py`、两个 MetaWorld plotting notebooks，以及 `external_packages/Metaworld/metaworld/envs/mujoco/sawyer_xyz/visual/__init__.py`。本地 acquisition inventory 的四个文件分别为 0、5466、5628、11504 bytes；空的 `__init__.py` 没有视觉逻辑。
- **源状态：`partial_visual_source`**。README 中的 `assets/votp-overview.png`（1573×775）与 PDF Figure 1(a) 的 pipeline 子图视觉匹配，但缺少 PDF Figure 1(b) 的 R/μ* computation；`research/utils/plotter.py` 能确认 serif paper context、multi-panel layout、seaborn SD bands、legend/grid/inset 等通用语法，却没有 paper-specific figure config、结果数据或 Figure 2–19 的生成入口；两个 notebooks 是通用 MetaWorld reward/noise 示例而非本文图表复现。自动 inventory 将该 repo 标成 `exact_visual_source`，经直接资产与 PDF 对照后校正为 partial。未克隆模型、数据集或 checkpoint。
- 可核对的源精确信息：`plotter.py` 使用 `sns.set_context(context="paper", font_scale=0.68)`、`sns.set_style("white", {"font.family": "serif"})`，`plot_run` 用 `sns.lineplot(..., errorbar="sd")`，`plot_from_config` 支持 `(rows, cols)` grid、`legend_pos=bottom` 和可选 inset。这些只用于识别通用来源，不把通用 helper 冒充为本文每幅图的精确生成源。

## 全文视觉风格

- **版式**：letter 双栏；主文 Figure 1 为页宽复合图，Table 1 为窄 inset 宽表，Figure 2–3 横跨双栏，Figure 4 为双栏宽，Figure 5–6 为单栏，Figure 7 页宽；附录保留双栏论文版式，learning curves/aggregate metrics 多为页宽，超参数和小表按栏宽布置。caption 放在对象下方且统一使用 `Figure/Table n.`。
- **字体**：正文/caption 以 Nimbus Roman No9 L 与 Computer Modern 数学字体为主，PDF 还嵌入 Times New Roman、Cambria Math、DejaVu Sans/Arial 等导入图字体；图内可见约 5–14 pt，表格约 6.5 pt，regular/bold 与 roman/italic 混用。字号为 PDF 对象/渲染综合判断，除 `plotter.py` 的 paper context 外没有逐图公开 rcParams。
- **颜色与冗余**：定量图采用橙/绿/紫/蓝/红的 categorical palette，IQL 常用黑虚线；自然图像/流程图使用混合 pastel 与照片原色。方法名、panel 标题、线型和 row position 提供部分冗余，但多数曲线图灰度安全性有限；表格主要是黑白 minimal/booktabs，粗体承担局部最佳值。
- **向量/栅格**：曲线、柱、矩阵、文字和表格主要是 PDF vector；视频帧、环境照片和 rollout/distraction montage 是 raster；Figure 1、7、14、18、19 等为 mixed。

## 逐对象审计

### Figure 1（p.4，main）
- **位置与结构**：`module=method`，`width=page_width`；复合画布分为 (a) 左侧 pipeline 与 (b) 右侧 OT computation。左侧按 labeled segments → Video Foundation Model → Latent Space → Inferred Preference 由左向右，右侧给出 4 个 labeled segments、2 个 unlabeled segments、preference matrix R、transport plan μ* 与 score；有一条顶部说明框。
- **类型与绘图语法**：`types=pipeline, conceptual_diagram, matrix, heatmap`；`rendering=mixed`；x/y=`none/none`；grid=`none`；legend=有（top right，shared=False）；direct labels=有；markers=2；line styles=2；reference lines=0；uncertainty=`none`；line width=0.9 pt；provenance=`mixed`。
- **编码与数据统计**：x=处理阶段与匹配方向；y=无定量轴；latent/inferred 两个状态；color=绿=preferred、橙=non-preferred，灰=unlabeled，蓝/紫=模块与矩阵；shape=圆点/视频帧框/圆角模块；line=实线 GT preference 与虚线 pseudo preference 箭头；facet=(a) pipeline；(b) computation；text=N、R、μ*、Eq. (5) score 与图例；图面把 segment 的视频帧、latent-space 圆点、R 与 μ* 的数值格子和 score=0.18 同时编码；没有重复实验或误差统计。
- **Caption（PDF 逐字，96 词；moves=title, setup, encoding_key, comparison；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 1. Overview of our framework. (a) VOTP embeds visual segments into a latent space using an off-the-shelf video foundation model and uses the optimal transport plan to propagate preferences with relative alignment strengths. Green dots indicate preferred segments over orange ones. (b) Example computation in VOTP with four labeled segments (σ_i) and two unlabeled segments (σ̄_i′). Preference relations among labeled segments are represented by the preference matrix R. Each entry of the optimal transport plan μ* specifies the probability that a labeled segment matches an unlabeled segment, and the unnormalized preference score is computed using Eq. (5).
- **证据关系**：引言的少量 feedback 与 latent-space propagation 主张 → §4.1–4.2 的 representation、R、OT coupling 与 Eq. (5) → Figure 1 方法接口 → Figure 18 的完整伪标注实例 → Table 13 的 pseudo-label accuracy。
- **设计优点**：把数据输入、表示、OT 对齐和最终偏好放在同一阅读方向，方法接口清晰。；矩阵/transport plan 与视频帧之间有显式对应，且图例解释了实线/虚线。
- **设计弱点**：副图信息密度高，矩阵和 score 在单栏缩放后接近可读性下限。；颜色承担偏好与数据状态，灰度下需依赖文字、位置和箭头；caption 未给归一化公式或阈值。
- **可复用模式**：将“输入视频段→表征→耦合→伪标签”的 pipeline 与一个最小数值 worked example 并置，可复用于需要解释算法如何落到数据的论文。

### Figure 2（p.6，main）
- **位置与结构**：`module=ablation`，`width=page_width`；四个并列 learning-curve panel：hopper-medium-replay-v2、walker2d-medium-replay-v2、door-open-v2、drawer-open-v2。每 panel 使用四条方法曲线，底部共享图例。D4RL x 轴到 1.0×10^6，MetaWorld 到 0.4×10^6；纵轴为 Score 或 Success Rate (%)。
- **类型与绘图语法**：`types=line`；`rendering=vector`；x/y=`linear/linear`；grid=`both`；legend=有（bottom center，shared=True）；direct labels=无；markers=0；line styles=1；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=Training Steps (×10^6)；y=Score 或 Success Rate (%)；color=SIM-individual / SIM-mean / SIM-weighted / VOTP；shape=无；line=四条方法线；facet=task panels；text=共享方法图例；x 为训练步数，y 为归一化 D4RL score 或 MetaWorld success rate；方法由颜色区分，均值由线、五次运行的标准差由阴影区分。
- **Caption（PDF 逐字，19 词；moves=title, setup, uncertainty_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 2. The effectiveness of using OT to infer pseudo-labels. Results are averaged over five runs with standard deviation (shaded area).
- **证据关系**：§5.3 的 OT pseudo-labeling 组件问题 → Figure 2 的 SIM-individual/mean/weighted 与 VOTP 反事实 → Table 1 的最终 benchmark → Figure 18 的 coupling 可视化。
- **设计优点**：四任务同一坐标语法，OT 替代方案可快速横向比较。；caption 明确五次运行和阴影含义，曲线与机制问题直接相连。
- **设计弱点**：共享图例在缩放后较小，曲线末端没有直接标签。；D4RL 与 MetaWorld 的 x 范围不同；caption 未说明各 panel 的 y 指标名称和 seed 级聚合细节。
- **可复用模式**：固定任务 panel 和共享方法色，用均值线+SD band 将组件消融压缩成可扫描的四格结果图。

### Figure 3（p.6，main）
- **位置与结构**：`module=ablation`，`width=page_width`；四个任务组 hopper、walker2d、door-open、drawer-open；每组五根柱表示 R3M、CLIP、S3D、VideoCLIP、InternVideo。y 轴为 Performance，柱顶配置误差线，底部共享图例；hopper/walker2d 使用 medium-replay。
- **类型与绘图语法**：`types=bar`；`rendering=vector`；x/y=`categorical/linear`；grid=`y`；legend=有（bottom center，shared=True）；direct labels=无；markers=0；line styles=0；reference lines=0；uncertainty=`error_bar`；line width=0.7 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=task category；y=Performance；color=trajectory encoder；shape=柱高/柱顶 error bar；line=无；facet=四个 task groups；text=encoder legend；x 为四个任务类别，y 为最终 performance；五种 encoder 用柱色，误差线来自五次运行。
- **Caption（PDF 逐字，23 词；moves=title, setup, uncertainty_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 3. Ablation with various trajectory encoders in D4RL and MetaWorld. For hopper and walker2d, we use medium-replay datasets. Results are averaged over five runs.
- **证据关系**：§4.1 对 video foundation model 表示能力的选择 → Figure 3 的 IFM/ViFM encoder 替换 → 选定 S3D 后用于 Figure 2、Figure 4–7 与 Table 1。
- **设计优点**：把 image/video encoder 作为单一干预轴，任务间差异易见。；误差线和五次运行定义比只给点估计更完整。
- **设计弱点**：四组五色柱在窄 panel 中较密；缺少具体 y 轴单位和各 encoder 参数规模。；颜色是主要方法通道，灰度阅读区分度有限。
- **可复用模式**：用任务分组柱状图呈现 representation choice 的反事实，并保持一个共享 encoder legend。

### Figure 4（p.7，main）
- **位置与结构**：`module=results`，`width=double_column`；四个并列 task panel，x 为 preference feedback 数量 5、10、50、100、500、1K，y 为 Score 或 Success Rate。IQL 作为黑色虚线基准，P-IQL、SURF、VOTP 为有色实线并带半透明 band，底部共享图例。
- **类型与绘图语法**：`types=line`；`rendering=vector`；x/y=`categorical/linear`；grid=`both`；legend=有（bottom center，shared=True）；direct labels=无；markers=0；line styles=2；reference lines=1；uncertainty=`band`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=number of preference feedbacks；y=Score 或 Success Rate；color=method；shape=无；line=IQL 虚线基准；其余实线；facet=four task panels；text=共享方法图例；横轴是离散 label budget，纵轴是最终性能；IQL 的 task-reward 水平作为 reference line，其余方法的反馈效率由曲线达到该水平的 budget 体现。
- **Caption（PDF 逐字，12 词；moves=title, setup；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Figure 4. Average performance of each method as the number of preference feedbackts varies.
- **证据关系**：摘要/§5.1 的 feedback-efficient 主张 → Figure 4 的 label-budget response → Figure 5 的 τP quality–quantity trade-off → Table 11 的 pseudo-label 计算成本。
- **设计优点**：把预算响应放在同一四 panel 画布，直接支持‘少量 feedback’叙事。；IQL reference line 使达到 task-reward 水平的 label 数可视化。
- **设计弱点**：caption 有 ‘feedbackts’ 拼写错误，未解释虚线、阴影及各任务 y 指标。；离散 label count 的不等间距/对数感较强，读者需从刻度判断实际位置。
- **可复用模式**：用参考水平线+多方法 budget 曲线同时呈现效果和反馈成本，适合反馈效率问题。

### Figure 5（p.7，main）
- **位置与结构**：`module=ablation`，`width=single_column`；四个任务 panel 展示 VOTP 随 preference threshold τP 改变的性能。x 为任务特定的离散 τP 值，y 为 Score 或 Success Rate；每 panel 一条蓝色均值线和淡色 band，无图例。
- **类型与绘图语法**：`types=line`；`rendering=vector`；x/y=`categorical/linear`；grid=`both`；legend=无（—，shared=False）；direct labels=无；markers=0；line styles=1；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=preference threshold τP；y=Score 或 Success Rate；color=蓝色=VOTP；shape=无；line=单条 VOTP 曲线；facet=four task panels；text=—；τP 是 x 轴干预，性能是 y 轴；线表示五次运行平均，band 表示标准差，反映伪标签质量与数量的折衷。
- **Caption（PDF 逐字，11 词；moves=title, setup；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Figure 5. Performance of VOTP under different values of the preference threshold τP.
- **证据关系**：§4.2 Eq. (7) threshold filtering → Figure 5 超参数敏感性 → Figure 2 的伪标签质量 → Table 13 的标签 accuracy。
- **设计优点**：一条线、同构 panel 使阈值趋势和回落快速可见。；颜色和 band 很克制，不会掩盖干预轴。
- **设计弱点**：caption 没有给出各任务实际 τP grid、seed 数或 band 定义。；x 为离散阈值但未明确标为 categorical，图外无法判断最优值的具体数值。
- **可复用模式**：以同一 y 指标和固定 panel 结构扫描单个质量阈值，并用 band 保留重复运行信息。

### Figure 6（p.7，main）
- **位置与结构**：`module=results`，`width=single_column`；两个并列 scatter panel，标题 P-IQL 和 VOTP。x 为 GT Reward，y 为 Estimated Reward，点为 door-open 的 segment；两 panel 在右下/内部显示 Pearson r=0.57 与 r=0.93，网格横纵均有。
- **类型与绘图语法**：`types=scatter`；`rendering=vector`；x/y=`linear/linear`；grid=`both`；legend=无（—，shared=False）；direct labels=有；markers=1；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=GT Reward；y=Estimated Reward；color=蓝色 segment 点；shape=圆点；line=无；facet=P-IQL/VOTP panels；text=r 数值注释；每点是一个 door-open trajectory segment 的 learned reward/GT reward 配对；r=0.57 与 r=0.93 是 Pearson correlation point estimates，没有误差椭圆或置信区间。
- **Caption（PDF 逐字，16 词；moves=title, setup, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 6. The Pearson correlation (r) between learned rewards and GT rewards for P-IQL and VOTP in door-open.
- **证据关系**：§5.3 的 reward-model alignment 诊断 → Figure 6 的 P-IQL/VOTP 相关性 → Figure 17 扩展到八个任务 → Table 13 的 pseudo-label accuracy。
- **设计优点**：坐标变量和相关系数位置直接可读，P-IQL/VOTP 对照紧凑。；点云比单一平均分更接近 reward-shaping 机制证据。
- **设计弱点**：相关性不能独立证明 reward alignment 导致 policy 提升；没有样本量或分层信息。；单一蓝色点云缺乏冗余编码，密集区域在缩放后会重叠。
- **可复用模式**：用同坐标轴 paired scatter 将 reward quality 诊断与主方法对照相邻呈现，再在附录扩展任务覆盖。

### Figure 7（p.8，main）
- **位置与结构**：`module=results`，`width=page_width`；复合图左侧为 Lift Banana 的成功/失败 trajectory frame grid，帧上给出 t=0、13、15、17、20、26；右侧为 learned reward 随 timestep 的折线。P-IQL/VOTP 各有成功实线和失败虚线，并带 band；共享图例位于右图上方/左上。
- **类型与绘图语法**：`types=qualitative_grid, line`；`rendering=mixed`；x/y=`linear/linear`；grid=`both`；legend=有（upper left of line panel，shared=False）；direct labels=无；markers=0；line styles=2；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=time step；y=learned reward；color=P-IQL/VOTP × success/failure；shape=frame snapshots；line=成功实线、失败虚线；facet=qualitative frames + reward chart；text=四条轨迹图例；左侧是单个 Lift Banana 案例的定性成功/失败帧，右侧是 timestep→learned reward 的四条均值轨迹与 band；不是跨 seed benchmark 汇总。
- **Caption（PDF 逐字，36 词；moves=title, setup, encoding_key, appendix_pointer；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 7. Lift Banana: Examples of successful and failed trajectories at each time step (left) with the corresponding reward outputs over timesteps from VOTP and P-IQL (right). Additional results and detailed experimental setup are provided in the Appendix.
- **证据关系**：§5.5 的真实机器人可用性 → Figure 7 以成功/失败 reward 反事实解释 P-IQL 的 failure mode → Table 3 的 10-episode success rate → Figure 14 的 Drawer Open 对应扩展。
- **设计优点**：把行为证据和 reward 曲线放在同一画布，机制与 failure surface 对齐。；线型与颜色双重区分 success/failure 和 method，图例有明确作用。
- **设计弱点**：左图帧数少且只有一个案例，不能代表真实机器人总体成功率。；caption 未定义 band 的统计量，也未给失败判定阈值。
- **可复用模式**：用同步时间快照+reward trace 对照成功与失败轨迹，适合展示 learned reward 如何误判行为。

### Figure 8（p.14，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；一行六个环境缩略图，依次标为 Hopper、Walker2d、Door open、Drawer open、Plate slide、Sweep into；每个 tile 下有任务标签，无坐标轴或统计图例。
- **类型与绘图语法**：`types=image_montage, qualitative_grid`；`rendering=mixed`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=—；y=—；color=自然环境图像与任务标签；shape=environment thumbnails；line=—；facet=六个环境 tile；text=环境名称；六个 benchmark/environment 视觉样例；没有 performance、样本数、误差或分母。
- **Caption（PDF 逐字，14 词；moves=title, setup, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 8. Overview of environments used in our experiments: Gym Locomotion (a–b) and MetaWorld Manipulation (c–f).
- **证据关系**：Appendix A.1 的任务定义 → Figure 8 固定六个实验环境 → Table 1/2/9–13 与 Figure 2–6 的任务轴 → Figure 19 的 MetaWorld distraction 变体。
- **设计优点**：用同一缩略图尺寸给出实验空间的最小可视上下文。；Gym 与 MetaWorld 分组在 caption 中明确，任务标签直接可读。
- **设计弱点**：缩略图本身没有动作/成功判定或摄像机条件，caption 只说明大类。；自然图像颜色不构成可比较的数据编码，灰度下场景辨识可能下降。
- **可复用模式**：将所有环境以等尺寸 montage 列出，并在 caption 中说明任务族范围，作为后续定量图的任务索引。

### Figure 9（p.15，appendix）
- **位置与结构**：`module=appendix`，`width=single_column`；单张真实机器人 setup 图：Sawyer 机械臂、桌面、Drawer/Banana 对象和 RealSense Camera D435i 等可见标签，属于照片/截图与矢量文字混合。
- **类型与绘图语法**：`types=screenshot, image_montage`；`rendering=mixed`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=—；y=—；color=自然场景与对象标签；shape=robot/camera/object regions；line=—；facet=single setup image；text=Sawyer、Drawer、Banana、camera labels；真实机器人实验 setup 的定性照片；正文/Appendix A.4 另给 7-DoF、480×480、10 Hz 和 521-dimensional policy input 等设置，图自身不含统计量。
- **Caption（PDF 逐字，4 词；moves=title, setup；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 9. Setup in real robot.
- **证据关系**：Appendix A.4 的真实机器人 setup → Figure 9 作为 Table 3 success-rate 的物理环境证据 → Figure 7/14–16 的 rollout 与 reward 案例。
- **设计优点**：对象、相机和机械臂的空间关系在一张照片中可核对。；setup 图与文字参数互补，有利于复现设备边界。
- **设计弱点**：caption 过短，未说明视角、相机分辨率或标注颜色。；照片没有尺寸标尺、坐标系或遮挡/视场说明。
- **可复用模式**：用一张直接标注的 setup photo 固定 embodiment、传感器和任务对象，再把控制/数据参数放在附录表格。

### Figure 10（p.16，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；四个 D4RL task learning-curve panel：hopper-medium-replay-v2、hopper-medium-expert-v2、walker2d-medium-replay-v2、walker2d-medium-expert-v2。五条曲线 IQL、IPL、P-IQL、SURF、VOTP，底部共享图例，线周围为 SD band。
- **类型与绘图语法**：`types=line`；`rendering=vector`；x/y=`linear/linear`；grid=`both`；legend=有（bottom center，shared=True）；direct labels=无；markers=0；line styles=1；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`mixed`。
- **编码与数据统计**：x=Training Steps (×10^6)；y=Score/normalized performance；color=method；shape=无；line=五条方法曲线；facet=four D4RL task panels；text=共享方法图例；训练步数到最终 checkpoint 的 D4RL 曲线；每条线是 5 runs 的均值，SD band；曲线按 window size=3 moving average 平滑。
- **Caption（PDF 逐字，39 词；moves=title, setup, encoding_key, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 10. Learning curves of IQL, IPL, P-IQL, SURF, and VOTP on D4RL (Table 1). Results are means of 5 runs with standard deviation (shaded area). We smooth the learning curves using a moving average with a window size of 3.
- **证据关系**：Table 1 主 D4RL 终点结果 → Figure 10 提供完整训练动力学 → Appendix B 的 aggregate Fig. 12 → Table 10 的 GT/incorrect reward sanity check。
- **设计优点**：把主表的终点比较扩展成全过程，方法颜色和 Table 1 可对齐。；caption 同时给重复、band 和平滑窗口，复现线索较充分。
- **设计弱点**：四 panel 与五条线密度较高，末端缺直接标签。；moving average 会遮蔽短期波动，caption 没有说明 y 轴在不同任务是否完全同尺度。
- **可复用模式**：主表只报终点时，附录用同色的多 panel learning curves 补回训练稳定性和收敛路径。

### Figure 11（p.16，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；四个 MetaWorld task learning-curve panel：door-open-v2、drawer-open-v2、plate-slide-v2、sweep-into-v2；五条 IQL/IPL/P-IQL/SURF/VOTP 曲线，底部共享图例与 SD band。
- **类型与绘图语法**：`types=line`；`rendering=vector`；x/y=`linear/linear`；grid=`both`；legend=有（bottom center，shared=True）；direct labels=无；markers=0；line styles=1；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`mixed`。
- **编码与数据统计**：x=Training Steps (×10^6)；y=Success Rate (%)；color=method；shape=无；line=五条方法曲线；facet=four MetaWorld task panels；text=共享方法图例；MetaWorld success-rate 训练曲线，均值来自 5 runs，SD 以带状区域编码并使用 window=3 平滑。
- **Caption（PDF 逐字，39 词；moves=title, setup, encoding_key, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 11. Learning curves of IQL, IPL, P-IQL, SURF, and VOTP on MetaWorld (Table 1). Results are means of 5 runs with standard deviation (shaded area). We smooth the learning curves using a moving average with a window size of 3.
- **证据关系**：Table 1 的 MetaWorld 终点结果 → Figure 11 的训练轨迹 → Fig. 12/13 aggregate metrics → Table 12 scripted/human teacher slice。
- **设计优点**：与 Figure 10 共用颜色、布局和统计语法，跨 domain 可比。；完整曲线揭示 VOTP 与 baselines 的收敛/波动，而不仅是终点。
- **设计弱点**：不同 task 成功率曲线混在一页，图例与小刻度较细。；caption 未给每个 panel 的具体 episode/evaluation frequency。
- **可复用模式**：将 domain 变化放在 panel 轴、将方法保持在颜色轴，形成可复用的跨 benchmark learning-curve 页面。

### Figure 12（p.17，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；4×4 metric matrix：四个 D4RL task 行，每行 Median、IQM、Mean、Optimality Gap 四个 mini-panel；五个方法的水平区间/点线显示 aggregate metric 与区间，方法名称在左侧直接标注。
- **类型与绘图语法**：`types=line, other`；`rendering=vector`；x/y=`linear/categorical`；grid=`x`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`multiple`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=aggregate score；y=metric row / method；color=method colors；shape=horizontal interval mark；line=区间端点/线段；facet=task × metric matrix；text=Median/IQM/Mean/Optimality Gap labels；跨五 runs 的 Median、IQM、Mean、Optimality Gap aggregate metrics；前三个指标越高越好，Optimality Gap 越低越好，误差编码为 95% percentile-bootstrap CI。
- **Caption（PDF 逐字，37 词；moves=title, setup, encoding_key, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 12. Aggregate metrics on D4RL locomotion tasks with 95% confidence intervals (CIs) across five runs. Higher mean, median and IQM scores and lower optimality gap are better. The CIs are estimated using the percentile bootstrap with stratified sampling.
- **证据关系**：Figure 10 的完整曲线 → Figure 12 的 D4RL aggregate summary → Table 1 的最终均值与 Table 10 的 reward sanity check。
- **设计优点**：把四个 metric 方向固定成同构 matrix，能同时看中心趋势和 aggregate robustness。；caption 明确指标方向、运行数和 bootstrap 方法。
- **设计弱点**：16 个 mini-panel 和多方法区间信息密集，字体/区间重叠会增加扫描成本。；没有独立 legend，直接标签在缩小后容易拥挤；CI 只覆盖五 runs 聚合而非任务实例不确定性。
- **可复用模式**：将多个 aggregate metric 排成 task×metric 矩阵，并用统一区间语法将主结果的终点表扩展为分布稳健性摘要。

### Figure 13（p.17，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；4×4 metric matrix：四个 MetaWorld task 行，每行 Median、IQM、Mean、Optimality Gap mini-panel；五方法 aggregate 区间/点线，方法标签直接放在图面。
- **类型与绘图语法**：`types=line, other`；`rendering=vector`；x/y=`linear/categorical`；grid=`x`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`multiple`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=aggregate score；y=metric row / method；color=method colors；shape=horizontal interval mark；line=区间端点/线段；facet=task × metric matrix；text=Median/IQM/Mean/Optimality Gap labels；MetaWorld 四任务的 Median/IQM/Mean/Optimality Gap aggregate metrics；指标方向、五 runs 与 bootstrap CI 同 Figure 12。
- **Caption（PDF 逐字，37 词；moves=title, setup, encoding_key, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 13. Aggregate metrics on MetaWorld manipulation tasks with 95% confidence intervals (CIs) across five runs. Higher mean, median and IQM scores and lower optimality gap are better. The CIs are estimated using the percentile bootstrap with stratified sampling.
- **证据关系**：Figure 11 的 MetaWorld curves → Figure 13 的 aggregate comparison → Table 1 MetaWorld average → Table 12 teacher-source robustness。
- **设计优点**：与 Figure 12 视觉同构，domain 变化只在 task rows，跨域比较成本低。；把 optimality gap 的反向方向直接写进 caption，避免只看柱/点高低。
- **设计弱点**：高密度 16 panel 仍然需要附录放大查看；没有显式方法 legend。；bootstrap CI 的 stratification 单位和 aggregate 计算细节不在图中。
- **可复用模式**：保持 metric skeleton 不变，仅替换 domain/task rows，以最小改动生成跨域 aggregate evidence。

### Figure 14（p.18，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；Drawer Open 成功/失败 trajectory frames 位于左侧（top success、bottom failure），带有 t=0…58 的时间标签；右侧为 VOTP/P-IQL 成功与失败 learned-reward 曲线，实线/虚线和颜色区分方法/结局，并有 band 与上方图例。
- **类型与绘图语法**：`types=qualitative_grid, line`；`rendering=mixed`；x/y=`linear/linear`；grid=`both`；legend=有（upper left of line panel，shared=False）；direct labels=无；markers=0；line styles=2；reference lines=0；uncertainty=`band`；line width=0.8 pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=timestep；y=learned reward；color=P-IQL/VOTP × success/failure；shape=trajectory frames；line=solid=success, dashed=failure；facet=frames + reward panel；text=时间标签与方法图例；单个 Drawer Open 成功/失败 rollout 的帧序列与对应 learned reward traces；band 表示运行/案例波动，图不是任务级 success-rate 汇总。
- **Caption（PDF 逐字，25 词；moves=title, setup, encoding_key；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 14. Drawer Open: Examples of successful and failed trajectories at each time step (top) with the corresponding reward outputs over timesteps from VOTP and P-IQL (bottom).
- **证据关系**：Figure 7 的 Lift Banana 机制案例 → Figure 14 扩展到 Drawer Open → Figure 15/16 的三方法 rollout snapshots → Table 3 的真实任务 success rate。
- **设计优点**：时间标签把视觉行为和 reward 曲线对齐，成功/失败反事实清楚。；方法和结局由颜色+线型冗余编码，读者可在图例缺失时仍追踪。
- **设计弱点**：帧网格占据大量空间但不提供动作/距离数值；band 统计定义不在 caption。；成功/失败案例数量有限，不能替代 10-episode rate。
- **可复用模式**：把视频帧时间线与 reward trace 做上下/左右对齐，展示 reward model 在 failure trajectory 上的行为差异。

### Figure 15（p.18，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；Lift Banana rollout snapshot：三行方法 BC、P-IQL、VOTP，每行七个时间快照 t=0、5、12、19、26、33、40，末端有 T/时间方向提示；为自然图像栅格，方法名直接标注。
- **类型与绘图语法**：`types=qualitative_grid, image_montage`；`rendering=raster`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=rollout time；y=visual state；color=自然场景色；方法由行位置编码；shape=robot/object pose in frame；line=—；facet=method rows × time snapshots；text=BC/P-IQL/VOTP labels；三种 policy 的单个 Lift Banana rollout 快照；caption 明确 BC/P-IQL failure 与 VOTP success，但无 episode 分母或统计聚合。
- **Caption（PDF 逐字，54 词；moves=title, setup, comparison, main_finding, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=True）**：
  > Figure 15. Snapshot of rollouts on Lift Banana task from BC, P-IQL and VOTP. The BC agent fails to descend to the banana and cannot grasp it. The P-IQL agent grasps the banana but does not lift and just release it. VOTP agent successfully reaches the banana, grasps it, and lifts it to a specified height.
- **证据关系**：Table 3 的 real-robot success-rate → Figure 15 用同一任务给出行为级 qualitative comparison → Figure 7 reward-case 与 Figure 16 Drawer Open 对照。
- **设计优点**：方法×时间网格可直接检查‘到达—抓取—抬升’动作链。；caption 直述每一行的关键 failure/success，证据关系明确。
- **设计弱点**：单个 rollout 不能估计策略成功率或稳定性；时间戳不含动作/空间尺度。；自然场景颜色复杂，方法比较完全依赖行标签而非视觉冗余。
- **可复用模式**：固定时间快照列、方法行，把抽象 success rate 展开为可观察的动作序列，并在 caption 说明失败机制。

### Figure 16（p.18，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；Drawer Open rollout snapshot：BC、P-IQL、VOTP 三行，七个时间快照 t=0、10、20、30、40、50、60；方法名和时间标签直接标注，末端以 T 指示方向。
- **类型与绘图语法**：`types=qualitative_grid, image_montage`；`rendering=raster`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=rollout time；y=visual state；color=自然场景色；方法由行位置编码；shape=robot/handle pose in frame；line=—；facet=method rows × time snapshots；text=BC/P-IQL/VOTP labels；三方法单个 Drawer Open rollout 的行为快照；caption 直接描述 wandering/handle failure 与 VOTP success，无统计重复。
- **Caption（PDF 逐字，44 词；moves=title, setup, comparison, main_finding, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=True）**：
  > Figure 16. Snapshot of rollouts on Drawer Open task from BC, P-IQL and VOTP. In both BC and P-IQL, the agent barely reaches the handle after wandering and fails to pull the drawer open. VOTP agent, however, reaches the handle directly and pull it open successfully.
- **证据关系**：Table 3 Drawer Open success rate → Figure 16 行为级 failure/success 机制 → Figure 14 reward traces；与 Figure 15 构成两个真实机器人任务的 qualitative pair。
- **设计优点**：与 Figure 15 同构，方法间动作差异在时间上可追踪。；caption 明确失败不是‘没到达’，而是绕行后无法拉开抽屉。
- **设计弱点**：没有多 episode 代表性或成功概率，且时间快照的控制步数未解释。；自然图像和同色物体可能遮蔽 handle 位置，缩小后辨识成本高。
- **可复用模式**：以同一 snapshot grid 模板覆盖不同 manipulation task，保持方法行和时间列一致。

### Figure 17（p.22，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；八个数据集各有 P-IQL/VOTP 两个 scatter panel，共 16 个 mini-panel；x=GT Reward、y=Estimated Reward，点为 segment，panel 标题直标方法/任务，面内显示 Pearson r。
- **类型与绘图语法**：`types=scatter`；`rendering=vector`；x/y=`linear/linear`；grid=`both`；legend=无（—，shared=False）；direct labels=有；markers=1；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=GT Reward；y=Estimated Reward；color=蓝色 segment 点；shape=圆点；line=无；facet=dataset × method panels；text=panel title 与 r 注释；八个任务上 P-IQL/VOTP learned reward 与 GT reward 的 segment-level scatter；每 panel 给 Pearson r point estimate，没有 CI/ellipse或分层统计。
- **Caption（PDF 逐字，20 词；moves=title, setup, encoding_key, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 17. Correlation between learned rewards and ground-truth rewards for P-IQL and VOTP. Pearson correlation coefficients (r) are shown for each dataset.
- **证据关系**：Figure 6 的 door-open 两 panel → Figure 17 跨 D4RL/MetaWorld 的 reward-alignment 扩展 → Table 13 pseudo-label accuracy → Table 1 policy outcomes。
- **设计优点**：统一坐标和 panel pairing 让跨任务 reward alignment 扫描高效。；r 直接放在每 panel，图外 caption 简短但图面信息完整。
- **设计弱点**：16 panel 的点密度高，低相关任务的 cloud 仍难从小图判断。；相关性依然是机制 proxy，不包含 causal intervention、样本数或置信度。
- **可复用模式**：将一个主文诊断扩展成 task×method paired scatter matrix，以保持跨任务可比的 reward-quality evidence。

### Figure 18（p.23，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；高密度复合图：左列 8 个 labeled pairs 与 preference matrix R；中列 4 个 unlabeled pair examples 及 score；右列每个 pair 的 cost matrix 和 transport plan。每个 segment 原 64 帧下采样为 4 帧，矩阵用彩色 cell 与标签显示。
- **类型与绘图语法**：`types=matrix, heatmap, qualitative_grid`；`rendering=mixed`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=pair/matrix position；y=matrix cell or preference score；color=淡粉/绿/蓝表示 pair/cost/transport roles；shape=video frame tiles and matrix cells；line=—；facet=labeled/unlabeled/cost/plan columns；text=R、S、Cost Matrix、Transport Plan labels；drawer-open 的 worked example：4 labeled pairs 组成 8×8 R；4 个 unlabeled pair 的 score 为 -0.5284、-0.5107、0.5827、0.4864；cost/transport matrix 条目四舍五入到两位，帧从 64 均匀下采样到 4。
- **Caption（PDF 逐字，44 词；moves=title, setup, encoding_key, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 18. Additional visualizations of the pseudo-labeling process from VOTP on the drawer-open task. We use 4 labeled pairs. All cost matrix and transport plan entries are rounded to two decimals. For clarity, each segment (originally 64 frames) is uniformly downsampled to 4 frames for visualization.
- **证据关系**：Figure 1(b) 的最小 OT computation → Figure 18 的完整 pseudo-labeling visualization → Eq. (4)–(7) 与 Algorithm 1 → Table 13 的 accuracy。
- **设计优点**：把抽象 R、cost、μ 与可观察 segment 帧逐一对应，机制透明度最高。；caption 说明 4 pairs、矩阵精度与 frame downsampling，避免把展示细节误当原始数据。
- **设计弱点**：矩阵与视频 tiles 极密，小字号和颜色 cell 在普通缩放下难读。；图展示一个 drawer-open example，不报告总体 accuracy、阈值通过率或跨样本稳定性。
- **可复用模式**：用‘labeled evidence→R→cost/transport→unlabeled score’的 worked example 解释算法，并明确展示下采样与四舍五入边界。

### Figure 19（p.23，appendix）
- **位置与结构**：`module=appendix`，`width=page_width`；四行 distraction montage：Lighting Changes (Direction + Position)、Lighting Changes (Ambient + Diffuse)、Texture Changes (Floor + Table)、Video Background；每行多个 segment clips，右侧另有 Labeled Data/Unlabeled Data 对照。
- **类型与绘图语法**：`types=qualitative_grid, image_montage`；`rendering=mixed`；x/y=`none/none`；grid=`none`；legend=无（—，shared=False）；direct labels=有；markers=0；line styles=0；reference lines=0；uncertainty=`none`；line width=— pt；provenance=`rendered_estimate`。
- **编码与数据统计**：x=distraction family / clip position；y=visual segment frames；color=自然场景色与行标签；shape=video-frame tile；line=—；facet=four distraction rows × labeled/unlabeled columns；text=lighting/texture/background labels；MetaWorld visual distractor 的定性样例：光源方向/位置、ambient/diffuse、table/floor texture、easy/hard video background；texture 组合数为 20，segment 内 distractor 固定、跨 segment 可变。
- **Caption（PDF 逐字，90 词；moves=title, setup, encoding_key, comparison, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Figure 19. Examples of scenarios with different types of visual distractions. For lighting changes, we consider two distractors: (1) variations in the direction and position of the light source, and (2) variations in ambient and diffuse lighting. For texture changes, we randomize the textures of the table and floor (20 possible combinations). For video background distractions, we use both the easy and hard videos from Yuan et al. (2023). Example segment clips are available at this link. Note that the distractor variation within each segment is fixed, but may vary across segments.
- **证据关系**：§5.4 Table 2 的 nuisance robustness → Figure 19 展示干扰构造与 Labeled/Unlabeled 对照 → Appendix C.5 pseudo-label accuracy 与 Table 2 的性能维持。
- **设计优点**：四种 nuisance family 以同一行结构并置，视觉干扰的覆盖面明确。；caption 详细定义变化范围、20 texture combinations 与 segment 内固定规则。
- **设计弱点**：大量自然图像 tile 无坐标或强度标尺，无法从图直接比较干扰大小。；caption 的外部 example clips link 依赖链接上下文，图本身不提供生成参数。
- **可复用模式**：以行=干扰类型、列=segment/label source 的 montage 展示 robustness 条件，同时在 caption 说明随机化边界。

### Table 1（p.6，main）
- **位置与结构/表头**：`module=results`，`width=inset`；12 列：Dataset + IQL+GT、Oracle、IPL、CPL、DPPO、P-IQL、SURF、LiRE、APPO、FTB、VOTP；10 行数据（4 个 D4RL 任务、loco avg.、4 个 MetaWorld 任务、mw avg.）。一层表头，D4RL/MetaWorld 由水平分组规则分开；数值为 final performance。
- **表格语法**：rows=10（数据行），columns=12，header_levels=1，row_groups=2，decimal_precision=1，rules=`minimal`，highlighting=`bold, best_second_best`。
- **表头、统计与不确定性**：D4RL normalized score 与 MetaWorld success rate 的最终 checkpoint 平均；表头同时固定 dataset、GT/Oracle 上界、PbRL baselines 与 VOTP，粗体为排除 IQL+GT/Oracle 后距最佳 5% 内。；每个任务值为 5 seeds 的 mean ± standard deviation；loco/mw average 行为跨任务平均点估计，没有 ±。
- **Caption（PDF 逐字，59 词；moves=title, setup, comparison, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 1. Average performance of methods on D4RL locomotion and MetaWorld. For D4RL tasks, “hop” denotes hopper, while “m”, “r”, and “e” denote medium, replay, and expert, respectively. We run five seeds and report the final performance at the end of training like Kostrikov et al. (2022). Bold values indicate results within 5% of the best-performing method (excluding IQL+GT and Oracle).
- **证据关系**：§5.2 的有限反馈 benchmark 主张 → Table 1 headline comparison → Figure 10/11 完整曲线 → Figure 2–5 组件/预算消融 → Table 10 GT reward sanity check。
- **设计优点**：一个表同时覆盖两个 domain、上界和 9 个 PbRL baseline，扫描效率高。；row group、avg 行和粗体规则使跨任务/方法的决策面清楚。
- **设计弱点**：12 列在 inset 尺寸下字体小，mean±SD 与 avg point estimates 混排。；5% bold rule 不是不确定性；caption 未给每个任务 evaluation episode denominator。
- **可复用模式**：固定 dataset→method 的宽表，使用 domain 分组、平均行和一致的 mean±SD 记法承载主比较。

### Table 2（p.8，main）
- **位置与结构/表头**：`module=results`，`width=page_width`；7 列：Dataset、Same Domain、Light(pos.+dir.)、Light(amb.+diff.)、Texture、Video(easy)、Video(hard)；3 行数据：door-open、drawer-open、Average；一层表头，任务与 Average 由规则分隔。
- **表格语法**：rows=3（数据行），columns=7，header_levels=1，row_groups=2，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：两个 MetaWorld 任务在同 domain、光源、texture、easy/hard video nuisance 下的 success-rate performance；视觉干扰条件是列轴，未提供每个 distractor 的样本分母。；5 个随机 seeds 的 mean ± standard deviation；Average 为跨两个 MetaWorld task 的点估计。
- **Caption（PDF 逐字，19 词；moves=title, setup, uncertainty_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 2. Performance of VOTP under various types of visual distractions. Mean and standard deviation are computed over 5 random seeds.
- **证据关系**：§5.4 的 visual nuisance robustness → Table 2 定量切片 → Figure 19 构造样例 → Table 13 pseudo-label accuracy 的任务异质性。
- **设计优点**：条件轴清晰，能直接比较 nuisance family 对 VOTP 的影响。；caption 明确 5-seed mean/SD，平均行提供快速汇总。
- **设计弱点**：只有 VOTP，缺少同条件 baseline，因此不能单独归因于相对鲁棒性。；列标题缩写较多，caption 未解释 Same Domain 或视频难度的构造。
- **可复用模式**：将 robustness 条件置于列轴、任务置于行轴，保留相同 success-rate 统计语法。

### Table 3（p.8，main）
- **位置与结构/表头**：`module=results`，`width=single_column`；3 列：Method、Lift Banana、Drawer Open；3 行 BC、P-IQL、VOTP；一层表头、一个 method row group、minimal horizontal rules，VOTP 的两个最高值以粗体显示。
- **表格语法**：rows=3（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=1，rules=`minimal`，highlighting=`bold, best_second_best`。
- **表头、统计与不确定性**：真实 Sawyer 任务的 BC/P-IQL/VOTP success rate，分母明确为 10 episodes；数值为 Lift Banana 20/50/80 与 Drawer Open 40/50/70 百分比。；每个单元是 10 episodes 的 success-rate 百分比点估计；未报告 SD、区间或 episode-level failure counts。
- **Caption（PDF 逐字，8 词；moves=title, setup；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 3. Success rates over 10 episodes on real-world tasks.
- **证据关系**：§5.5 real-robot utility → Table 3 任务级结果 → Figure 7/14–16 行为与 reward 机制案例 → Figure 9 setup。
- **设计优点**：表很小且直接给出任务/方法交叉比较，适合与 qualitative figures 并读。；10-episode denominator 写在 caption，避免把点估计误当大规模 benchmark。
- **设计弱点**：分母很小且没有不确定性，跨方法差异的精度有限。；没有成功标准或每个 episode 的失败类型，需回到 Appendix A.4。
- **可复用模式**：对真实机器人结果使用窄表给出明确分母，再以相邻视频帧图补充行为解释。

### Table 4（p.15，appendix）
- **位置与结构/表头**：`module=appendix`，`width=page_width`；3 列：Hyperparameter、D4RL、MetaWorld；9 行 Optimizer、Learning rate、Batch size、Hidden layer dim、Hidden layers、Activation、β、τ、Training steps；一层表头，无显式分组，minimal 横线。
- **表格语法**：rows=9（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=mixed/not applicable，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：IQL 的 optimizer、学习率、batch/network、β/τ 与 D4RL/MetaWorld 训练步数；类别型与数值型值混排。；超参数取值表，不是重复实验统计；无 mean/SD、区间或失败值。
- **Caption（PDF 逐字，3 词；moves=title；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Table 4. Hyperparameters of IQL.
- **证据关系**：Appendix A.3 实现细节 → Table 4 固定 policy learner → Table 1 结果与 Figure 10/11 曲线的复现边界。
- **设计优点**：按 domain 并列值，读者可逐项复制 IQL 设置。；表头简短、无多余竖线，适合和 Tables 5–6 组成参数组。
- **设计弱点**：caption 未给训练硬件、seed 或参数含义；β/τ 的指标语义需回到方法。；所有值是配置而非证据，无法从表判断敏感性。
- **可复用模式**：将相同超参数字段按 D4RL/MetaWorld 两列对齐，并把复现所需设置放在独立 appendix table。

### Table 5（p.15，appendix）
- **位置与结构/表头**：`module=appendix`，`width=page_width`；3 列 Hyperparameter、D4RL、MetaWorld；11 行 Optimizer、Learning rate、Batch size、Hidden layer dim、Hidden layers、Activation、Output activation、Segment length、Subsample length、Training steps、Score function；一层表头、minimal 规则。
- **表格语法**：rows=11（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=mixed/not applicable，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：reward model 的优化器、MLP、activation、segment/subsample length、训练步数和 score function，在 D4RL/MetaWorld 间并列。；配置表；无重复运行统计、误差或区间。
- **Caption（PDF 逐字，5 词；moves=title；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Table 5. Hyperparameters of the reward model.
- **证据关系**：§4.3 Bradley–Terry reward bridge → Table 5 复现参数 → Figure 6/17 reward alignment 与 Table 13 pseudo-label accuracy。
- **设计优点**：把 reward learning 的结构和输入 segment 长度集中呈现。；与 Table 4 同列结构，易于核对不同 domain 配置。
- **设计弱点**：caption 不说明 score function 的具体公式或 normalization；数值/类别混排。；不提供 reward model seed、早停或训练稳定性。
- **可复用模式**：将 reward-model architecture、segment geometry 和 optimizer 合并在一张 domain 对照表中。

### Table 6（p.15，appendix）
- **位置与结构/表头**：`module=appendix`，`width=single_column`；3 列 Hyperparameter、D4RL、MetaWorld；5 行 Total #labeled pairs、Total #unlabeled pairs、M (in Alg. 1)、Distance metric in Eq. 5、Preference threshold τP；一层表头、minimal 规则。
- **表格语法**：rows=5（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=mixed/not applicable，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：VOTP 的 label budget、unlabeled pool、Algorithm 1 的 M、cost metric 与 threshold；D4RL/MetaWorld 两列直接对应 Figure 4/5 的实验边界。；配置值没有不确定性；10/50k pairs、M=2、Euclidean 与 domain-specific τP 是点值或集合。
- **Caption（PDF 逐字，3 词；moves=title；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Table 6. Hyperparameters of VOTP
- **证据关系**：Eq. (4)–(7) 与 Algorithm 1 → Table 6 复现参数 → Figure 4 feedback budget、Figure 5 τP ablation、Table 11 cost。
- **设计优点**：把方法关键旋钮和 label budget 显式化，复现价值高。；D4RL/MetaWorld 的 threshold set 放在同一行，连接 Figure 5。
- **设计弱点**：caption 未给 threshold 选择原则或每个 task 的具体映射。；表只有配置，没有 pseudo-label pass rate 或算力代价。
- **可复用模式**：用短表固定算法输入规模、cost choice 和 threshold，并将任务域差异放在列而非脚注。

### Table 7（p.16，appendix）
- **位置与结构/表头**：`module=appendix`，`width=single_column`；2 列 Hyperparameter、Value；13 条数据行，按 IQL、Reward Model、VOTP 三个视觉 row group 分段。IQL 组含 Optimizer/Learning Rate/Batch Size/β/τ/Training Steps，Reward Model 组含 Batch size/Activation/Output activation/Segment length/Training steps，VOTP 组含 labeled/unlabeled pairs 与 τP；一层表头。
- **表格语法**：rows=13（数据行），columns=2，header_levels=1，row_groups=3，decimal_precision=mixed/not applicable，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：Sawyer 实验的 IQL、reward model、VOTP 参数，含 Lift/Drawer label and unlabeled pair counts；表中 β/τ 合并为一行。；真实机器人配置点值；无多 seed 统计或 success-rate uncertainty。
- **Caption（PDF 逐字，5 词；moves=title；headline_bold=False；self_contained=False；main_finding_stated=False）**：
  > Table 7. Hyperparameters of real robot experiments.
- **证据关系**：Appendix A.4 real-robot setup → Table 7 复现参数 → Table 3 success rates 与 Figures 7/9/14–16。
- **设计优点**：以三组模块分隔 policy/reward/VOTP，参数归属明确。；Value 列短且适合窄栏，包含真实任务 pair budget。
- **设计弱点**：不同模块的 ‘Batch size’ 重复出现，未在表头写模块外的 metric。；caption 没有将 5/10 labels 与具体 Lift/Drawer 行内对应关系完全展开。
- **可复用模式**：以模块 row group 组织真实机器人超参数，保持单值列简单并避免横向宽表。

### Table 8（p.16，appendix）
- **位置与结构/表头**：`module=appendix`，`width=page_width`；4 列 Algorithm、URL、Hyperparameters、Tuning；7 行 IPL、CPL、DPPO、SURL、LiRE、APPO、FTB；一层表头，minimal 横线，URL 使用蓝色/等宽视觉，搜索范围文字混排。
- **表格语法**：rows=7（数据行），columns=4，header_levels=1，row_groups=1，decimal_precision=mixed/not applicable，rules=`minimal`，highlighting=`text_color`。
- **表头、统计与不确定性**：表把每个 baseline 的公开 URL、默认/搜索变体和关键 λ/threshold/budget 参数放在同一行；FTB 标为 Default。；baseline tuning 配置和链接，不包含方法重复统计或 performance uncertainty。
- **Caption（PDF 逐字，10 词；moves=title, setup, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 8. Source code links and hyperparameter/variant search settings for all baselines.
- **证据关系**：§5.2 baseline selection → Table 8 复现实验来源与 tuning boundary → Table 1 主比较；与本论文 VOTP source repository 形成 provenance 对照。
- **设计优点**：URL 与 tuning range 同行，复现者可以直接追溯实现和干预范围。；四列语义稳定，不把 baseline 数值和超参混在一起。
- **设计弱点**：URL 较长，窄页面会压缩文本；某些 tuning 参数的语义未在表头解释。；表只列作者选择的范围，不展示各候选的运行失败或计算成本。
- **可复用模式**：以 algorithm→source URL→tuning scope 三列建立 baseline provenance table，把公平比较条件外显。

### Table 9（p.19，appendix）
- **位置与结构/表头**：`module=appendix`，`width=single_column`；3 列 Dataset、Euclidean、Cosine；7 行 6 个任务与 Average；一层表头，一个连续任务组，minimal 横线；Euclidean/Cosine 是 cost metric 对照。
- **表格语法**：rows=7（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：VOTP 在 Euclidean 与 cosine distance cost 下的 D4RL/MetaWorld performance；平均值 71.3 vs 70.7，任务级波动用 ±SD。；任务行是 5 runs mean ± standard deviation，Average 为跨任务点估计。
- **Caption（PDF 逐字，7 词；moves=title, comparison, uncertainty_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 9. Performance of VOTP with different cost functions.
- **证据关系**：Eq. (4) 的 d 选择 → Table 9 cost-metric ablation → Table 1 主配置使用 Euclidean；Figure 12/13 aggregate metrics 提供更广汇总。
- **设计优点**：直接对应方法中可选的 cost function，反事实轴单一。；保留任务级 mean±SD，避免平均差异掩盖 heterogeneity。
- **设计弱点**：只有 VOTP，没有计算时间或 pseudo-label accuracy 的联合视图。；caption 未明确 5-run 定义，平均行与任务行精度略不同。
- **可复用模式**：将可替换 cost function 放在列轴、任务放在行轴，复用主 benchmark 的任务命名。

### Table 10（p.19，appendix）
- **位置与结构/表头**：`module=appendix`，`width=page_width`；6 列 Dataset、BC、GT、Zero、Random、Negative；8 行四 D4RL + 四 MetaWorld 任务；一层表头，无显式 domain label，minimal 规则，GT/incorrect reward 为列轴。
- **表格语法**：rows=8（数据行），columns=6，header_levels=1，row_groups=1，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：IQL 在 BC、ground-truth、Zero、Random、Negative reward 下的 normalized score/success rate；Zero/Random/Negative 是 incorrect-reward sanity conditions。；5 random seeds 的 mean ± standard deviation；各 reward condition 以同一任务/评估方式比较。
- **Caption（PDF 逐字，25 词；moves=title, setup, comparison, uncertainty_definition, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 10. Performance of IQL (Kostrikov et al., 2022) on each dataset under GT and incorrect rewards. Mean and standard deviation are computed over 5 random seeds.
- **证据关系**：§4.3 reward relabeling → Table 10 验证 reward correctness 对 offline RL 的影响 → Table 1 VOTP performance 与 Figure 6/17 learned-reward alignment。
- **设计优点**：把 GT、错误 reward 和 BC 放到一个决策面，支持 reward 是关键中介。；5-seed mean/SD 与任务级行对齐，阅读路径简洁。
- **设计弱点**：caption 未说明不同 domain 的 y metric，表头没有 domain group。；错误 reward 的生成定义需回到正文，数值本身不能解释失败机制。
- **可复用模式**：用 reward condition 列替代多张 sanity-check 表，显式把 reward quality 与 RL outcome 连接。

### Table 11（p.19，appendix）
- **位置与结构/表头**：`module=appendix`，`width=page_width`；7 列：首列为 time row label，后六列 N labels=10、25、50、100、200、500；3 行 N labels/Sequential time (minutes)/Parallel time (minutes)，一层表头，minimal 横线并有一处竖向分隔。
- **表格语法**：rows=3（数据行），columns=7，header_levels=1，row_groups=1，decimal_precision=2，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：10k unlabeled pairs 下，label count 增加时 sequential 与 100-pair-concurrent parallel pseudo-label generation time；parallel 仅在 100/200/500 给出 1/1.7/6.6 min。；Sequential/parallel wall-clock minutes 的点估计；‘-’表示该 parallel condition 未给数值，不是零。
- **Caption（PDF 逐字，16 词；moves=title, setup；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 11. Computational cost of VOTP for generating pseudo-preference labels for 10k unlabeled pairs under different dataset sizes.
- **证据关系**：§4.3 Sinkhorn efficiency claim → Table 11 label-count cost curve → Figure 4 feedback budget → Appendix C.3 的 RTX 4090/24-core hardware context。
- **设计优点**：横轴直接是 label budget，sequential/parallel 行使成本折衷可扫描。；缺失值使用 ‘-’ 而非虚构 zero，表头和单位明确。
- **设计弱点**：没有 feature-extraction/policy-training 成本列，无法完整评估 end-to-end budget。；并行定义和硬件需要读正文，caption 未列 concurrent batch size。
- **可复用模式**：用 label budget 列轴、执行模式行轴报告 wall-clock cost，并保留未测条件为短横线。

### Table 12（p.20，appendix）
- **位置与结构/表头**：`module=appendix`，`width=single_column`；3 列 Dataset、Scripted Teacher、Human Teacher；7 行数据（3 个 D4RL/4 个 MetaWorld 任务）与 Average 行，共 8 行数据；一层表头、单一连续 row group、minimal 规则。
- **表格语法**：rows=8（数据行），columns=3，header_levels=1，row_groups=1，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：同一 VOTP 在 scripted teacher 与 human teacher preference labels 下的 task performance；human teacher 含四位非机器人参与者，walker2d 条件下降明显。；5 random seeds 的 mean ± standard deviation；Average 为跨任务 point estimate。
- **Caption（PDF 逐字，19 词；moves=title, setup, comparison, uncertainty_definition；headline_bold=False；self_contained=True；main_finding_stated=False）**：
  > Table 12. Performance of VOTP with preference feedbacks from human teachers. Mean and standard deviation are computed over 5 random seeds.
- **证据关系**：Appendix C.4 的 human preference extension → Table 12 teacher-source robustness → Table 1 scripted/GT main comparison → Figure 11 MetaWorld curves。
- **设计优点**：两类 label source 并列，直接暴露 human/scripted transfer。；任务级 mean±SD 让 walker2d 的下降可定位，而非只报总平均。
- **设计弱点**：参与者数量和 label collection protocol 不在表中；平均行掩盖任务异质性。；Human Teacher 列不能区分 label noise 与 task difficulty。
- **可复用模式**：将 supervision source 作为列干预，保持任务行和主 benchmark metric 结构一致。

### Table 13（p.20，appendix）
- **位置与结构/表头**：`module=appendix`，`width=single_column`；3 列 Domain、Task、Accuracy (%)；7 行任务（D4RL 3 行、MetaWorld 4 行），两 domain row groups 通过合并标签显示；一层表头，minimal 横线，accuracy 一位小数。
- **表格语法**：rows=7（数据行），columns=3，header_levels=1，row_groups=2，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **表头、统计与不确定性**：pseudo-preference labels 与 ground-truth scripted labels 的 task-level accuracy；多数任务 >90%，sweep-into 为 67.0%，直接显示机制异质性。；伪标签 accuracy 点估计，排除 equally preferred pairs；未报告样本量、区间或 confusion breakdown。
- **Caption（PDF 逐字，31 词；moves=title, setup, comparison, main_finding, abbreviation_definition；headline_bold=False；self_contained=True；main_finding_stated=True）**：
  > Table 13. Accuracy of generated pseudo-labels: We calculate accuracy by comparing against ground-truth scripted preference labels (excluding equally preferred pairs). Overall, VOTP generates high-quality pseudo-labels with only a handful of labeled preference queries.
- **证据关系**：Figure 18 的 worked pseudo-labeling → Table 13 accuracy validation → Figure 2 OT ablation 与 Table 1 policy performance；作为 reward alignment 的中介证据。
- **设计优点**：caption 给出 accuracy 分母边界（排除 ties）并直述主发现。；Domain row group 与任务行让低 sweep-into 点容易定位。
- **设计弱点**：accuracy 没有 label count、类别分布或不确定性，无法衡量 tie/错误类型。；‘high-quality’ 总结被 sweep-into 的 67% 限定，需要结合任务异质性解读。
- **可复用模式**：在伪标签机制主张旁放 task-level accuracy 表，显式排除 ties 并保留低点而不只报平均。

## 跨对象系统判断

- **视觉叙事**：Figure 1 先固定 VOTP 的 segment→ViFM→OT→pseudo-preference 接口；Table 1 给出跨 D4RL/MetaWorld 主比较；Figure 2–6 依次拆解 OT、encoder、label budget、threshold 和 reward alignment；Table 2/3 将 robustness 与真实机器人结果落地。附录 Figure 8/9 固定环境和 embodiment，Figure 10–13 补全训练曲线与 aggregate metrics，Figure 14–16 展开失败/成功行为，Table 9–13 覆盖 cost、错误 reward、计算成本、human teacher 与 label accuracy，Figure 17–19 形成 reward/伪标签/干扰的机制与边界证据。
- **Caption 系统**：caption 统一以对象标题开头；主文 Figure 1/7、Table 1/2 等提供 setup 与关系，附录 Fig. 10–13 明确 repeats/uncertainty，Fig. 15/16、Table 13 直接陈述 qualitative/main finding。明显缺口是 Fig. 4 的 `feedbackts` 拼写错误、Fig. 5 与 Tables 4–6 的短 caption，以及多幅图未在 caption 中列出 panel-specific y metric、分母或阈值 grid。
- **表头系统**：主结果使用 Dataset×method 宽表；robustness/cost/teacher 结果把干预条件放到列，任务放到行；超参数表用 domain 或 module 分组；Table 13 用 Domain→Task→Accuracy 的层级。minimal/booktabs 横线与粗体最佳值保持跨表一致。
- **方法—结果—消融链**：Figure 1/18 的 OT worked example 连接 Eq. (4)–(7) 与 Algorithm 1；Figure 2、3、5 对应 OT/encoder/threshold 干预；Figure 4 连接 feedback budget 与 Table 11 cost；Figure 6/17 与 Table 13 给 reward/pseudo-label 机制诊断；Table 1/2/3 则承载最终 benchmark、nuisance 和 robot outcome。
- **正文—附录边界**：正文图表承担主效果、机制和现实任务，附录提供全部 learning curves、aggregate CI、rollout、cost、teacher、accuracy 与 visual distractor 细节；附录 95% CI 仅出现在 Figure 12/13 caption，不把它们误写成正文对象。

## 最终判断

- **最可复用模式**：`method interface → benchmark table → component/budget ablations → mechanism scatter/qualitative trace → appendix validity/cost` 的层级叙事；固定 task panel 和 method palette；用 table 列轴表达干预条件；用时间快照+reward trace 对照成功/失败；用 worked OT example 连接矩阵数学与真实视频段。
- **最高价值对象**：Figure 1（方法接口与最小 OT 例子）、Table 1（D4RL/MetaWorld headline）、Figure 4（反馈预算效率）、Figure 7（真实机器人 reward failure 机制）、Figure 18（完整 pseudo-labeling worked example）、Table 13（伪标签 accuracy 的可证伪中介证据）。
- **主要失败模式**：高密度双栏图/宽表的小字号；caption 对 panel 指标、阈值、分母和 band 统计定义交代不足；颜色承担过多方法语义、灰度安全有限；qualitative 单案例容易被误读为总体成功率；Table 11/13 等仍缺失败类型、样本量或不确定性。
- **一句话视觉策略**：论文用一个可展开的 OT pipeline 将少量视觉偏好连接到跨域 benchmark，再以统一方法色、反馈预算曲线、reward/rollout 机制图和附录的 cost/accuracy/robustness 切片逐层约束“少量 feedback 仍能产生可靠 offline reward”的证据边界。

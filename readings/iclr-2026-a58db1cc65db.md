# CauKer：分类时间序列基础模型可以在合成数据上预训练

- **论文**：Shifeng Xie、Vasilii Feofanov、Jianfeng Zhang、Themis Palpanas、Ievgen Redko，*CauKer – Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data*；ICLR 2026 Oral。
- **读取版本**：官方 ICLR proceedings PDF；29 个物理页；`corpus/pdfs/iclr-2026-a58db1cc65db.pdf`。正文以 p.1–10 为边界，references 主要在 p.11–15，appendix 从 p.15 末开始延续至 p.29。
- **证据规则**：下文 `p.` 均为 PDF 物理页；图、表、算法和公式按 PDF 编号标注。没有在 PDF 中给出的实现、随机种子或统计细节记为 `not_present`，不以常识补全。

## 1. 文档边界、页级地图与篇幅

PDF 共 29 页。正文的结论和 limitations 在 p.10 结束；p.11 由 acknowledgements 和 references 开始。p.15 上半部仍是 references，下半部出现 `APPENDIX`、附录总览、Appendix A 和 Appendix B 的开头，因此 p.15 是 references/appendix 混合页。按物理页计，`main_pages=10`、`reference_pages=5`（p.11–15）、`appendix_pages=15`（p.15–29，和 references 在 p.15 重叠）。【p.10 §5；p.11 Acknowledgements/References；p.15 Appendix】

主文是双栏 ICLR 版式，正文图表多以跨栏或栏内浮动体出现。Figure 1 横跨 p.4 顶部；p.6 的 Table 1、Table 2 和 Figure 2 共同压缩 Q1 结果；p.8 的 Figure 3–5 形成四小图/多面板的密集结果页；p.9 的 Figure 6 和 Figure 7 同时承载训练时间与样本效率。附录仍为双栏排版，p.17 算法跨栏占据大部分页面，p.18–20 的 kernel/mean 图和消融表混排，p.26–29 以可视化、注意力图和附加表格为主。【p.4 Figure 1；p.6 Tables 1–2/Figure 2；p.8 Figures 3–5；p.9 Figures 6–7；p.17 Algorithm 1】

|区段|页码|语义模块|估计词数|版面事实与作用|
|---|---:|---|---:|---|
|Abstract|1|abstract|153|单栏摘要，6 句；依次给出对象、预训练成本、CauKer、规模结果和代码。|
|1 Introduction|1–2|introduction|682|p.2 上半部列三条 Findings，并以 roadmap 收束；没有独立图表。|
|2 Related Work|2–3|related_work|748|两个小标题覆盖 TSFM 方向和预训练数据；引用簇密集，最后一句建立 classification generator 的缺口。|
|3 Our Contributions / 3.1 Problem Setup|3|method|590|定义 zero-shot classification、OOD 协议以及 contrastive/masked 两种 SSL 范式。|
|3.2 CauKer|3–5|method|1,093|定义三类函数 bank、五步生成流程、设计选择和相对定位；Figure 1 在 p.4。|
|4 Experimental Results overview|5|experimental_design|303|列出 Q1–Q3、Mantis/MOMENT 和 128 个 UCR 数据集的统一评测框架。|
|4.1 Q1|5–7|experimental_design/results|770|固定 100K、四种合成生成器、UCR 平均准确率、运行时间和 DTW 聚类。|
|4.2.1 Data Scaling Laws|7|experimental_design/results|620|UEA 百分比子集与 CauKer 10K–10M 样本的 data-scaling 对照。|
|4.2.2 Model Scaling Laws|7–8|experimental_design/results|480|MOMENT 和 Mantis 的模型容量扫描，以及 PCA、non-linearity、CKA 解释。|
|4.3 Training Time Scaling Laws|9|experimental_design/results|300|在 UEA 10% 与 CauKer 1M 上比较 epoch 曲线。|
|4.4 Sample-efficient pre-training|9–10|experimental_design/results|950|比较真实语料、CauKer 和 forecasting 语料，回收 UCR、WOODS、clinical 与 Chronos 结论。|
|5 Conclusion|10|conclusion|280|重述合成数据、因果/时间结构和 scaling laws，没有新实验数字。|
|Limitations|10|limitations|47|只明确写出模型数量和未纳入大规模 forecasting benchmark 两项限制。|
|Acknowledgements|11|other|50|资助和 HPC 资源说明。|
|References|11–15|other|2,350|引用列表；不把引用条目计入语义模块正文词数。|
|Appendix preamble / A|15|appendix|400|附录职责总览和 TSFM 预训练数据表。|
|B Loss and architecture|15–16|appendix|700|Mantis 对比学习、MOMENT masked loss、架构与输入 patch 细节。|
|C Details of CauKer|16–20|appendix/ablation|1,300|伪代码、36-kernel bank、mean/activation bank、kernel/parent 与 graph-size 消融。|
|D Additional qualitative analysis|19–21|appendix|650|SWD 与 CKNNA 的定义、五次 synthetic draws 及全局/局部对齐结果。|
|E–G Scaling details|21–22|appendix|950|精确 data-scaling、model-scaling 表和 Section 4.4 训练 epoch 设置。|
|H–I UCR/WOODS|23–25|appendix|900|按领域的 UCR 分解和 17 个 WOODS 数据集的 OOD 结果。|
|J Chronos|25–26|appendix|500|MASE 定义、27 个 non-overlapping subsets 和 forecasting 表。|
|K–L representations|26–28|appendix|850|UMAP/PCA、多样性与 Attention Rollout。|
|M–O further experiments|28–29|appendix|740|downstream fine-tuning、irregular clinical evaluation 和 LLM writing assistance。|

主文基于自动测量文本的英文词元约 6,157 个（p.1–10）；附录 p.15–29 约 5,651 个，references p.11–15 约 2,400 个。附录约等于正文的 91.8%（物理页混合页按上述边界计数）。自动测量将 spaced-capital `A PPENDIX` 误判，故这些数字以逐页 PDF 边界修正，详见第 12 节。

## 2. 摘要逐句功能编码

|#|句子（按 PDF 还原 CauKer 拼写）|词数|功能|限定词/比较对象与证据|
|---:|---|---:|---|---|
|1|Time series foundation models (TSFMs) have recently gained significant attention due to their strong zero-shot capabilities and widespread real-world applications.|22|`object_scope`、`impact_claim`|范围是 TSFMs，理由是 zero-shot 与应用；p.1 §Abstract，“strong zero-shot capabilities and widespread real-world applications”。|
|2|Such models typically require a computationally costly pre-training on large-scale, carefully curated collections of real-world sequences.|16|`problem_gap`|成本和数据策展是背景约束；p.1 §Abstract，“computationally costly pre-training on large-scale, carefully curated collections”。|
|3|To allow for a sample-efficient pre-training of TSFMs, we propose CauKer, a novel algorithm designed to generate diverse, causally coherent synthetic time series with realistic trends, seasonality, and nonlinear interactions.|34|`core_idea`、`method`|“sample-efficient”是目标限定；生成多样、因果一致、具趋势/季节性/非线性；p.1 §Abstract，“generate diverse, causally coherent synthetic time series”。|
|4|CauKer combines Gaussian Process (GP) kernel composition with Structural Causal Models (SCM) to produce data for sample-efficient pre-training of state-of-the-art classification TSFMs having different architectures and following different pre-training approaches.|36|`method`、`object_scope`|组合 GP kernel composition 与 SCM；目标是不同架构/预训练范式的 classification TSFMs；p.1 §Abstract，“combines Gaussian Process (GP) kernel composition with Structural Causal Models (SCM)”。|
|5|Additionally, our experiments reveal that CauKer-generated datasets exhibit clear scaling laws for both dataset size (10K to 10M samples) and model capacity (1M to 783M parameters), unlike real-world datasets, which display irregular scaling behavior.|33|`quantitative_result`、`qualitative_result`|样本规模 10K–10M、模型规模 1M–783M；比较对象是 real-world datasets；p.1 §Abstract，“clear scaling laws for both dataset size and model capacity”。|
|6|The source code is publicly available at https://github.com/ShifengXIE/CauKer.|12|`impact_claim`|可复现性/可用性主张，未说明版本或 commit；p.1 §Abstract，“source code is publicly available”。|

摘要顺序是 `object_scope → problem_gap → core_idea/method → quantitative_result → impact_claim`。摘要报告了规模区间和相对 real-world datasets 的趋势，却没有报告 UCR 的具体 accuracy、运行时间、seed、误差表达或失败案例；没有理论定理，也没有 limitations。最强主张位于第 5 句：它把 CauKer 的效益包装为同时覆盖 dataset-size 和 model-capacity 的 scaling laws。【p.1 Abstract】

## 3. 引言的论证推进

引言的单一推进链是：TSFM 追求 OOD zero-shot → 现实预训练语料昂贵且 classification corpora 不足 → synthetic pre-training 可以节省采集、扩展规模并减轻 leakage → 现有 forecasting/kernel 与 tabular/SCM 生成器各自缺少 temporal motifs 或 class structure → CauKer 用 GP kernel composition 加 SCM 补齐两者 → 三项 Findings 和实验 Q1–Q3 回收该设计。【p.1–2 §1；p.2 Findings】

|段/动作|页码|上一段留下的问题|当前段回答与下一钩子|估计词数|
|---:|---:|---|---|---:|
|1 `context`|1|为什么 classification TSFM 值得研究。|列 healthcare、HAR、industrial monitoring，说明 forecasting/classification TSFM 及 OOD 目标；钩向预训练数据规模。|270|
|2 `problem`、`failure_of_prior_work`|1|大规模语料是否必要且足够。|指出已有工作在 synthetic data 上达到可比表现，并列出免采集、可任意扩展、降低 leakage 的优势；钩向 classification corpora 的不足。|180|
|3 `missing_insight`、`core_idea`|1–2|合成数据怎样适配分类而不是只拟合 forecasting。|要求样本间 meaningful correlations、序列内 realistic temporal dependencies；承诺 large-scale comparison；钩向 Findings。|155|
|4 `contribution_list`|2|需要怎样的生成器。|Findings 1 说 synthetic pipeline 需要重新思考既有 tabular/forecasting generator；钩向 scaling。|50|
|5 `contribution_list`|2|合成数据是否真的能随规模工作。|Findings 2 说 CauKer 有 data/model scaling，而 common benchmarks 破坏 scaling；钩向 SOTA classification。|48|
|6 `contribution_list`|2|是否能替代 real-world pretraining。|Findings 3 宣称 solely synthetic data 可达 state-of-the-art classification；钩向章节路线。|51|
|7 `roadmap`|2|读者如何核对这些主张。|按 Section 2–5 依次承诺 related work、pipeline、Q1–Q3 实验、结论和 limitations。|78|

引言约 46% 用于背景/缺口/生成器要求，约 36% 用于 Findings，约 12% 用于方法和实验路线，余量为连接句。贡献列表并非完全重复摘要：它明确写出对既有 synthetic generator 的重新思考和 scaling 破坏的比较，但仍没有列具体 accuracy、显著性、seed 或适用边界；可证伪性主要由后文图表而非引言措辞提供。【p.1–2 §1】

## 4. 相关工作与定位

相关工作是独立的 Section 2，位于引言之后、方法之前，正文约占 12%。它没有重复 CauKer 的五步算法，而是按模型用途和数据来源分类；末句把「没有 classification-oriented synthetic data generation for TSFM pretraining」设为缺口。【p.2–3 §2】

|段/引用簇|动作|比较维度|后文承担的论证|
|---|---|---|---|
|Time series foundation models|`taxonomy`、`chronology`|从 large-scale sequence-native models 到 LLM-backed models；再区分 forecasting 与 native classification，点名 Mantis、MOMENT、UniTS、NuTime 等。|为选择 Mantis contrastive 与 MOMENT masked 两种范式建立基础；p.2–3。|
|Classification TSFMs|`nearest_neighbor_contrast`、`credit_or_foundation`|Mantis、MOMENT、Time-series representation/ViT 等已在 real classification benchmarks 上预训练；不同模型架构与目标不同。|使本文的 synthetic pretraining 对照落到同一 zero-shot evaluation protocol；p.2–3。|
|Pre-training datasets|`taxonomy`、`limitation_of_prior`|real、synthetic、hybrid 三类；real corpora 从 300K 到 50M series，forecasting 的 scaling 可平或不足。|把 data diversity、domain mismatch、可扩展性变成 CauKer 的设计动机；p.2。|
|Forecasting/tabular generators|`nearest_neighbor_contrast`、`gap_creation`|Kernel-based GP/seasonal procedures、ForecastPFN/TimePFN 偏 forecasting；TabPFN SCM 偏 tabular，前者弱 class structure，后者丢 temporal structure。|直接引出「kernel composition + SCM」组合；p.3 §2、p.5 Positioning。|

引用在方法和实验中继续承担论证作用。具体而言，Ansari et al. (2024) 提供 zero-mean KernelSynth 对照，Hollmann et al. (2023) 提供 SCM 对照，Feofanov/Goswami 提供 Mantis/MOMENT 协议，Yao et al. (2025) 支撑 scaling-law 研究动机，Dau et al. (2019) 定义 UCR 评测边界。【p.3 §2；p.5–7 §4】

## 5. 方法、公式、算法与理论边界

### 5.1 形式化对象与方法链

- **Zero-shot classification**：TSFM 是冻结 encoder `F : R^T → R^Q`；下游数据 `D={(x_i,y_i)}_{i=1}^n`，先计算 `z_i=F(x_i)`，再只在 embedding 上训练轻量分类器 `h : R^Q → {1,…,C}`；测试为 `ŷ=h(F(x*))`。因此指标旨在测 representation quality，而非端到端 fine-tuning。【p.3 §3.1，“As F is kept frozen”】
- **OOD 协议**：CauKer 模型只见 synthetic series，预训练不见 UCR 或其他 real classification benchmark；官方 Mantis/MOMENT checkpoint 包含 UCR train split、但不含 UCR test，作者明确称其「to some extent」是 in-distribution，因此两组比较不是完全对称的 OOD 对照。【p.3 §3.1，“never see UCR”；p.9 Figure 7 caption】
- **预训练范式**：Mantis 是 contrastive、encoder-only，MOMENT 是 masked reconstruction、encoder-decoder；正文只给范式概览，loss 和架构公式移到 Appendix B。【p.3 §3.1；p.5 §4】
- **生成先验**：目标同时包含序列内 seasonality/periodicity/trend 与跨样本的 meaningful clustering。CauKer 的 `K` kernel bank、`M` mean bank、`A` activation bank 通过随机组合产生 GP root nodes，再经随机 DAG/activation 传播为 synthetic series。【p.3–4 §3.2】
- **五步生成**：Step 1 从 bank 随机取 `K∼U(1,n_K)` 个 kernels；Step 2 以随机 `+`/`×` 组合为 composite kernel；Step 3 随机取 mean functions，建立 `GP(µ_i,κ_i*)` 的 root nodes；Step 4 为 DAG edges 取 activation functions；Step 5 构造有 `M<V` 个 roots 的 DAG，沿拓扑序把 incoming trajectories 经随机线性层和 edge activation 传播，随后可插值并取 `d` 个 node outputs。【p.4 §3.2，Steps 1–5】
- **bank 设计**：mean bank 有 linear `ax+b`、exponential `ae^{bx}`、sparse anomaly；activation bank 有 affine/linear、ReLU、sigmoid、sine、modulo、Leaky ReLU；Appendix C 将 kernel bank 扩为 36 个不同超参数版本。【p.4；p.18 Appendix C.2】
- **设计对照**：零均值 KernelSynth 适合 smooth trend extrapolation，却抑制 mean level 这一分类 cue；TabPFN-style SCM 有 nonlinear dependency，却缺 seasonality/trend。CauKer 的因果语义来自 DAG，时间结构来自 GP kernel/mean；作者进一步把同一 SCM 的不同 nodes 解释为潜在 multivariate channels，但正文实验把每条 trajectory 当作 univariate sample。【p.4–5 §3.2】

段落动作序列为：`setup_notation → state_problem → contrast_alternative → define_component → instantiate_algorithm → explain_mechanism → connect_to_prediction → connect_to_experiment → scope_boundary`。核心因果链由三层组成。GP 给 temporal motifs，非零 mean 给 discriminative level，SCM 给跨变量 nonlinear dependencies；随后由 frozen encoder 的 UCR accuracy 检验。【p.4–6 §3.2–4.1】

### 5.2 公式和理论对象清单

论文没有 Theorem、Lemma、Proposition、Corollary，也没有正式 proof。唯一有编号的 display equation 是 Appendix J 的 MASE `(1)`；其余公式为无编号的定义/目标/伪代码中的更新式。按版面可辨认的 display 数为 8：方法 1 个、附录 7 个。方法中 `F`、`D`、`z_i`、`h`、`ŷ` 等多为行内数学，不应把每个符号当作独立编号公式。【p.3；p.4；p.15–16；p.20；p.25】

|对象|位置|角色|内容与证据|
|---|---|---|---|
|`t_{v_j}=φ(v_j)(W×[e_{·j}]+b)`|p.4 §3.2|`core_chain`|非 root 节点将 incoming edges 拼接，经随机 `W,b` 和 activation 传播；它是 SCM 生成机制的唯一主文 display。|
|`s_cos(a,b)`|p.15 Appendix B|`explanation`|Mantis 投影 embedding 的 cosine similarity。|
|`s_i(φ,ψ)`|p.16 Appendix B|`core_chain`|batch 内每个样本与两种随机 augmentation 的 pairwise similarities。|
|`L_contrastive`|p.16 Appendix B|`core_chain`|以 cross-entropy 和 temperature `T=0.1` 优化 Mantis。|
|`L_masked`|p.16 Appendix B|`core_chain`|MOMENT 在 masked patches 上的 MSE reconstruction loss。|
|`SWD_2(P,Q)`|p.20 Appendix D|`diagnostic`|对随机一维投影的二阶 sliced Wasserstein 距离，用于全局分布接近度。|
|`CKNNA_k`|p.20 Appendix D|`diagnostic`|冻结 encoder 下 target-to-source 的 classwise k-nearest-neighbour agreement，用于局部结构。|
|`MASE` `(1)`|p.25 Appendix J|`core_chain`|Chronos zero-shot forecasting 的 scale-free 指标；seasonal naive 约为 1。|

公式用于方法定义、训练目标和附加诊断；论文没有把公式用于理论保证。`SWD`/`CKNNA` 与 MASE 只在附录实验中使用；没有复杂度公式、收敛定理、统计检验推导或 causal identifiability 结果。`Algorithm 1` 是唯一伪代码，未提供渐近 time/space complexity；随机 DAG、GP sampling 和 node propagation 的成本只以实测秒数比较。【p.6 Table 2；p.17 Algorithm 1】

### 5.3 Algorithm 1 的可执行粒度

Appendix C.1 的 `Algorithm 1: CauKer: Synthetic Time-Series Generator for Classification` 输入 `N,L,d`、三类 banks、`K_max,V_max,P_max` 和 fixed-seed RNG，输出 `D_syn={x_1,…,x_N}`，每个 `x_i∈R^{d×L}`。伪代码先实现 `SAMPLECOMPOSITEKERNEL`（随机 kernel 数、choice、逐步 `+`/`×`），再实现 `SAMPLEMEAN`（有放回取两个 mean functions 并以 `+`/`×` 合成）。主循环随机 DAG，确定 roots 与每条 edge 的 activation，root 采 GP，按 `TopoSort` 传播 parent signals，最后从 `V` 个 node 中无放回选 `d` 个作为 sample channels，并循环至得到 `N` 个样本。【p.17 Algorithm 1】

关键不变量是：每个样本都由随机 DAG 的 root GP 生成并沿拓扑顺序传播；观测节点来自同一张 DAG 的 node outputs；输出长度固定为 `L`。伪代码没有给出 rejection/invalid graph 处理、插值失败处理、具体 `K_max/V_max/P_max` 默认值、内存上限或并行策略，故这些实现细节不是正文可复现的完整 contract。【p.17 Algorithm 1；p.4 Step 5】

## 6. 实验设计与复现信息

### 6.1 研究问题与统一评测

正文明确列出三个问题：Q1 比较 alternative synthetic generators；Q2 检查 data/model scaling laws；Q3 评估 synthetic data 是否可替代 real-world benchmarks。研究问题承担了预先组织作用，但没有注册、编号假设、预声明效应阈值或失败停止规则。【p.5 §4】

|设计项|PDF 给出的事实|状态与证据|
|---|---|---|
|目标模型|Mantis 8M encoder-only，contrastive；MOMENT 77M encoder-decoder，masked reconstruction。|`observed`；p.5 §4。|
|零样本分类器|Mantis frozen embeddings 上训练 Random Forest；MOMENT 使用 Support Vector Machine；报告 128 个 UCR 数据集 test accuracy 的平均值。|`observed`；p.5 §4。|
|Q1 synthetic baselines|FPFN（linear model of coregionalization）、KernelSynth（随机 covariance-kernel composition、zero mean）、Mean+KernelSynth（加入 non-zero mean）、SCM（重构 TabPFN generator）；series length `T=512`，每种固定 100K samples。|`observed`；p.5–6 §4.1。|
|Q2 data scaling|UEA 随机子集从 0.1%、1% 到 100%；CauKer 10K、50K、100K、500K、1M、5M、10M；每个 multivariate UEA channel 视作 univariate sample，总计约 12M channels。|`observed`；p.7 §4.2.1；p.21 Appendix E。|
|Q2 model scaling|MOMENT 77M/248M/783M；正文 Mantis 0.75M/2.59M/8.10M，附录扩展到 28.56M/114.14M；序列长度均 512。|`observed`；p.7–8；p.22 Appendix F。|
|Q2 training-time scaling|Mantis/MOMENT 分别在 UEA 10% 与 CauKer 1M 上跟踪 epoch→zero-shot accuracy。|`observed`；p.9 §4.3。|
|Q3 sample efficiency|Mantis 比较 CauKer 100K、real Mantis dataset 1.89M、UEA 100K、forecasting 100K；MOMENT 比较 CauKer 10M、Time Series Pile 13M、UEA/forecasting 100K。|`observed`；p.9–10 §4.4。|
|OOD/泄漏控制|CauKer 预训练从未接触 UCR/real classification benchmark；官方 real checkpoints 包含 UCR train split、不含 test。|部分 `observed`；p.3 §3.1；p.9 Figure 7 caption。未报告独立 contamination audit。|
|WOODS|17 个 OOD datasets，比较 ERM、Mantis-2M（约 1.89M real series）与 CauKer100K；冻结 encoder，仅用各 benchmark train split 训练轻量 classifier。|`observed`；p.24 Appendix I。|
|Chronos extension|1M 个长度 512 的 univariate series，约 0.512B observations；27 个与 official Chronos mixture disjoint 的 zero-shot subsets；比较 Tiny/Mini/Small/Base。|`observed`；p.10；p.25 Appendix J。|
|随机性/重复|Algorithm 1 输入 fixed-seed RNG；训练和评测没有报告 seed 值、独立重复次数或区间。|前者 `observed`，后者 `not_present`；p.17 Algorithm 1；p.5–10。|
|硬件、训练预算|只报告生成 1,000×512 series 的相同 hardware/software runtime；没有硬件型号、GPU 数量、wall-clock 训练时间、FLOPs、optimizer 或学习率。|`not_present`（生成 runtime 数字除外）；p.6 Table 2；p.10 Limitations。|
|下游 fine-tuning|Appendix M 采用 Mantis 官方 default fine-tuning pipeline，同一 optimizer/schedule/splits/classifier head 比较三种 pretraining。|`observed`；p.28–29 Appendix M。|
|不规则临床数据|P12、P19 为 sparsely/irregularly sampled multivariate physiological data，报告 AUROC/AUPRC。|`observed`；p.29 Appendix N。|

评测顺序基本沿着贡献列表：先 Q1 做组件/生成器对照，再 Q2 做数据、模型和 training-time scaling，最后 Q3 做 sample efficiency，并用 WOODS、Chronos 和 clinical benchmark 扩展外部性。主要复现缺口是随机种子、训练硬件/预算、生成超参数默认值和独立重复不完整；附录补充 model configuration 和 exact accuracy，但没有使不确定性可估计。【p.5–10；p.21–22】

## 7. 结果、统计与可视化

### 7.1 图表、算法和公式清单

|对象|模块|页码|任务、比较对象和编码通道|
|---|---|---:|---|
|Figure 1|method|4|五步 CauKer pipeline：kernel bank→composite GP/mean→SCM DAG/activations→synthetic series；流程图，无误差。|
|Table 1|results|6|四个 synthetic baselines 与 CauKer，在 Mantis/MOMENT 上的 128-UCR average accuracy。|
|Table 2|results|6|1,000×512 生成的 wall-clock 与 GP/SCM runtime breakdown。|
|Figure 2|results|6–7|200 CauKer samples 的 pairwise DTW matrix，排序后显示 cluster blocks 和 anomaly 条带。|
|Figure 3|results|8|MOMENT/Mantis 的 data-size 与 model-size scaling 曲线；四个面板，横纵轴为 dataset/model size 与 accuracy。|
|Figure 4|results|8|Mantis embedding 空间中 100K CauKer、UEA、UCR 样本的 PCA 投影。|
|Figure 5|results|8|CauKer 不同规模与 UEA 的 Mantis non-linearity（上）和 CKA（下）；无数字表格。|
|Figure 6|results|9|MOMENT/Mantis 在 epoch 轴上的 UEA vs CauKer test accuracy 曲线。|
|Figure 7|results|9|Q3 组合图：左侧 pretraining corpus/size/UCR inclusion/accuracy 表，右侧 training loss 与 test accuracy 曲线。|
|Table 3|appendix|15|代表性 TSFM 的 synthetic/real 数据、time points、series count、open status。|
|Algorithm 1|appendix|17|CauKer 生成器完整伪代码，while 循环和 TopoSort。|
|Figure 8|appendix|18|6 个代表 kernel 的 covariance matrix 和 GP sample paths。|
|Figure 9|appendix|19|zero/linear/exponential/sparse-anomaly mean function 样例。|
|Table 4|ablation|20|Kernel3/Parent2 到 Kernel7/Parent6 的 entropy、Hurst、stability、lumpiness、UCR accuracy。|
|Table 5|ablation|20|DAG graph size 10–50 的数据统计和 UCR accuracy。|
|Table 6|appendix|20|KernelSynth vs CauKer 的 global SWD2 和 CKNNA，五次 draws 的 mean±s.d.。|
|Table 7|appendix|21|UEA/CauKer data sizes 与 Figure 3 对应的 exact UCR accuracies。|
|Figure 10|appendix|23|Mantis model-size sweep 的 UEA/CauKer accuracy 曲线。|
|Table 8|appendix|22|MOMENT/Mantis 各 model size、UEA 1/10/100% 与 CauKer 100K/1M/10M exact accuracy。|
|Table 9|appendix|23|UCR 15 个 application Type 的 CauKer100K、Official 与 `∆`。|
|Table 10|appendix|24|WOODS 四个 domain、win counts 和 17-dataset average。|
|Table 11|appendix|25|Chronos Tiny–Base 在 27 subsets 上的 Official vs CauKer1M MASE。|
|Figure 11|appendix|26|frequency/slope/bias/combined 的 Mantis embedding UMAP。|
|Figure 12|appendix|27|UCR/UEA/CauKer embedding PCA，`n_max=10K/100K/1M`。|
|Figure 13|appendix|28|ECG/Fish 的 CauKer-100K vs real Mantis Attention Rollout 和 input series。|
|Table 12|appendix|29|Mantis UCR downstream fine-tuning：real 1.89M vs CauKer 100K/1M。|
|Table 13|appendix|29|P12/P19 irregular clinical AUROC/AUPRC。|

### 7.2 统计处理边界

- **聚合单位/分母**：主文 UCR 结果是 128 个 dataset 的 test accuracy 平均值；Appendix H 按 15 个 UCR Type 做 domain averages；WOODS 按 constituent datasets 求 domain average，并另报 17-dataset average；Chronos 在 27 个 disjoint subsets 上汇总 MASE。【p.5；p.23–25】
- **中心量和离散量**：Table 1、Table 7–11 的主要 UCR/MASE 数字是 point estimates；Table 6 明确为 5 个 independent synthetic draws 的 mean ± standard deviation；其他主结果没有 seed-level dispersion。Figure 5/6/7 是曲线，没有误差表达。【p.6；p.20–22；p.25】
- **假设检验**：仅 Appendix J 的 Chronos 扩展报告 two-sided Wilcoxon signed-rank test，`p=0.84`，significance level `0.05`；主分类结果没有 per-dataset test、multiple-comparison correction、bootstrap、Bayesian analysis、回归或 effect-size interval。【p.10；p.25】
- **评测指标**：zero-shot classification accuracy；Mantis 用 Random Forest，MOMENT 用 SVM。附加诊断使用 DTW、SWD2、CKNNA、non-linearity、CKA、MASE、AUROC/AUPRC。作者把 accuracy/MASE 的实质差异与 Chronos 的显著性叙述分开，但没有为主分类均值给不确定性。【p.5–10；p.20；p.25；p.29】
- **caption 自足性**：Table 1–2、Figure 1–7 的标题足以识别模型、数据和主要比较，但 Table 7 的「UCR Included?」含义需要读取 Figure 7 caption；Figure 3 的 UEA/CauKer 曲线对应关系需要参考正文和 Appendix E/F。【p.9；p.21–22】

### 7.3 主要结果与不利解释

1. **生成器组件对照。** 在固定 100K samples、长度 512 下，Mantis 的 UCR average accuracy 为 SCM 73.49、FPFN 77.52、KernelSynth 77.70、Mean+KernelSynth 78.20、CauKer 78.31；MOMENT 为 59.23、70.85、69.31、72.56、74.24。CauKer 相对 Mean+KernelSynth 只提高 0.11 个百分点（Mantis）和 1.68 个百分点（MOMENT），支持「mean + SCM」对 generic MOMENT 更重要的解释，但并未单独固定所有 graph/activation 超参数。【p.6 Table 1】
2. **生成成本。** 生成 1,000 条长度 512 的 univariate series 时，CauKer 121.64 s，KernelSynth 182.25 s；CauKer 内部 GP kernel sampling 118.54 s、SCM structure+propagation 1.14 s。作者据此将 SCM overhead 定位为总成本不足 1%，但未给硬件型号、并行度或跨规模复杂度。【p.6 Table 2】
3. **分类结构诊断。** Figure 2 对 200 个 CauKer samples 计算 DTW 距离并按 hierarchical-clustering memberships 排序，显示 block-like intra-cluster distances 与 anomaly 条带。它是 class-separability 的定性机制证据，没有真实 class labels、cluster purity 或与各 baseline 的同图对照。【p.6–7 Figure 2】
4. **数据 scaling。** CauKer 的 Mantis UCR accuracy 从 10K/50K/100K/1M/10M 的 76.91/78.08/78.55/78.91/79.09 逐步上升；MOMENT 的 100K/500K/1M/5M/10M 为 74.24/74.35/75.21/77.01/77.49。UEA 子集的曲线则不单调，例如 Mantis 从 12.7K 的 75.67 到 12.67M 降为 71.93，MOMENT 的 1.27M 为 70.49。作者解释为 UEA 的 domain mismatch、heterogeneous dataset size 和 diversity 不足；每个点仍是平均 accuracy，无重复误差。【p.7；p.21 Table 7】
5. **模型 scaling。** Appendix Table 8 显示 CauKer 上的 MOMENT 在 77M→248M→783M 对 100K 为 74.24→75.16→77.28、1M 为 75.21→76.16→77.20、10M 为 77.49→77.51→77.85；Mantis 在较小规模上也随容量总体上升，但 28.56M/114.14M 的 10M CauKer 反而是 78.19/78.81。UEA 列不稳定，例如 MOMENT 10% 为 70.49→66.91→64.18。作者将 CauKer 的单调趋势归因于更高数据 diversity，且把 10M MOMENT 的小增益解释为 saturation；该解释没有单独的 capacity-control 统计。【p.8；p.22 Table 8】
6. **表示空间解释。** Figure 4 的 PCA 显示 CauKer embeddings 覆盖 UEA 与 UCR 的大区域；Figure 5 显示 CauKer 规模增加伴随 Mantis non-linearity 变化，而 UEA 规模改变时 CKA/non-linearity 较平。作者将其作为 diversity 和 internal structural change 的提示，而非因果证明。【p.8 Figures 4–5】
7. **training-time scaling。** 在 UEA 10% 与 CauKer 1M 上，Figure 6 显示 CauKer 的 Mantis 和 MOMENT test accuracy 随 epoch 总体上升，UEA 曲线平或波动，尤其是 MOMENT。该结果与 data/model scaling 方向一致，但图中没有 seed、误差带或精确 epoch 数值表。【p.9 §4.3 Figure 6】
8. **样本效率与 UCR。** Figure 7 的 Mantis 行为 CauKer100K 78.55，官方 Mantis dataset 1.89M 为 78.66，UEA100K 为 76.73，forecasting100K 为 75.81；MOMENT 的 CauKer10M 为 77.49，Time Series Pile 13M 为 78.85，CauKer100K 74.24，UEA100K 73.55，forecasting100K 73.93。CauKer 用约 20×（Mantis）和约 1.3×（MOMENT）更少 series 接近 real checkpoint，但 real checkpoint 包含 UCR train split，故 accuracy 不是纯 OOD 公平上界。【p.9–10 Figure 7】
9. **WOODS 外部性。** Appendix I Table 10 的 overall average 为 ERM 0.800、CauKer100K 0.820、Mantis-2M 0.810；domain-level CauKer 在 CAP/HAR/SEDFx 高于两基线，MI 则低于 ERM/Mantis。作者称 CauKer 在 17 datasets 有 12 wins including ties，但表格的 `Win counts (out of 17; ties counted)` 是 ERM 7、CauKer 11、Mantis 4，文字与表格不一致。【p.24–25 Table 10】
10. **UCR domain heterogeneity。** 15 个 Type 中 8 个 CauKer100K 高于 official Mantis；Power 提高 +6.11 个百分点，Spectro 降低 −5.50 个百分点，其余 13 个 domain 在 ±3% 内。作者把 Spectro 的 deficit 与许多数据集少于 50 samples、official checkpoint 见过 UCR train split 的 in-distribution advantage 联系起来；这是可检验的解释，但没有 per-dataset dispersion。【p.23 Table 9】
11. **Chronos forecasting transfer。** 27 个 disjoint subsets 上，Official/CauKer1M 的 MASE 分别为 Tiny 0.87/0.89、Mini 0.84/0.87、Small 0.83/0.86、Base 0.81/0.83；Seasonal Naive 为 1.0000。作者报告 two-sided Wilcoxon signed-rank `p=0.84`，称差异 statistically indistinguishable。该扩展支持 synthetic temporal structure 可迁移到 forecasting，但任务、模型和指标已超出分类主线。【p.10；p.25 Table 11】
12. **全局/局部分布对齐。** Appendix D Table 6 在每个 UCR dataset 取 5 个 independent synthetic draws 后再平均：global SWD2 为 KernelSynth 7.11±1.13、CauKer 3.1486±0.21；CKNNA 为 0.014±0.03、0.015±0.03。CauKer 的 global discrepancy 显著更小，CKNNA 仅略高且区间相同量级，因此只能支持 distributional alignment 诊断，不能独立证明 SCM 的 causal necessity。【p.20–21 Table 6】
13. **下游 fine-tuning 与临床扩展。** Appendix M Table 12 的 UCR fine-tuning accuracy 为 real 1.89M 0.8496、CauKer100K 0.8291、CauKer1M 0.8457；Appendix N Table 13 中 P12 的 real/CauKer100K/CauKer1M AUROC 为 0.8121/0.7984/0.8189、AUPRC 为 0.4340/0.4276/0.4592，P19 对应 AUROC 0.8846/0.8534/0.8709、AUPRC 0.5368/0.4954/0.5005。CauKer1M 在 P12 超过 real baseline，在 P19 仍落后。【p.28–29 Tables 12–13】
14. **表示和注意力的定性解释。** Appendix K 的 frequency/slope/bias UMAP 颜色沿主方向平滑变化，combined view 形成少重叠簇；Appendix L 的 ECG/Fish attention rollout 让作者认为 CauKer-100K 的 attention 更集中于短的 discriminative subsequences，而 real Mantis 更分散。两者都是 selected examples/visual geometry，没有 classwise statistical test 或 negative-case rate。【p.26–28 Figures 11–13】

## 8. 消融、负面结果与自我设限

主文没有名为 `Ablation` 的章节。最接近的组件消融在 Q1 Table 1，专门的超参数敏感性在 Appendix C.3；消融和负面结果约占附录而非主文的很小部分。识别目标如下。

|对象|类型|结果/识别目标|证据|
|---|---|---|---|
|SCM vs Mean+KernelSynth|组件删除/替代|加入非零 mean 后 Mantis 78.20、MOMENT 72.56；再加入 SCM 后分别 78.31、74.24，隔离 temporal mean 与 causal propagation 的增量。|p.6 Table 1，`Mean-KernelSynth`/`CauKer`。|
|CauKer vs KernelSynth/FPFN/SCM|机制替代|SCM 单独最低，KernelSynth/FPFN 次之，CauKer 最高；检验 temporal structure、mean cue、SCM 是否共同需要。|p.6 §4.1。|
|Kernel/Parents co-sweep|超参数敏感性|Kernel3/Parent2→Kernel7/Parent6 时 Entropy 0.4629→0.6225、Hurst 0.7719→0.7519、Stability 0.9821→11.7237、Lumpiness 145.18→10,148,441.78，而 UCR accuracy 0.7848→0.7810，检验生成复杂度是否改变下游表现。|p.19–20 Appendix C.3/Table 4。|
|Graph size sweep|超参数敏感性|DAG nodes 10/20/30/40/50 时 UCR accuracy 0.7848/0.7811/0.7812/0.7815/0.7785，作者称对 graph size 不敏感。|p.20 Table 5。|
|Single-kernel failure|失败案例/数据异质性|DotProduct-only 生成近线性趋势，UCR 76.79%；RBF-only 78.07%，接近完整 CauKer；用于说明 kernel diversity/nonlinearity 的必要性。|p.19 Appendix C.3。|
|UEA vs CauKer scaling|数据/任务异质性|UEA 增大不保证更高 accuracy，CauKer 规模曲线更规则；检验结论是否由真实语料 diversity/domain mismatch 驱动。|p.7 Figure 3；p.21 Table 7。|
|Mantis vs MOMENT capacity|模型规模敏感性|同一 synthetic regime 下同时扫描容量；观察 Mantis 的 saturation 与 MOMENT 的 model/data interaction。|p.8 Figure 3；p.22 Table 8。|
|Training epochs|计算成本/时间敏感性|CauKer 上延长 epoch 仍有 accuracy 增益，UEA 上趋平/波动；检验 optimization horizon 是否受数据结构影响。|p.9 Figure 6。|
|Real vs synthetic corpus|样本效率/基线边界|100K/10M CauKer 与 1.89M/13M real corpus 比较，检验「较少样本接近大语料」而非只比较 generator。|p.9–10 Figure 7。|
|WOODS/clinical/Chronos|鲁棒性/扩展|跨 EEG-heavy、irregular multivariate clinical 和 forecasting subsets 扩展任务边界；不是主线组件消融。|p.24–29 Appendices I–N。|

不利信息主要通过四种方式呈现：

- **基线暴露差异主动放在 caption/正文**：作者说明 official Mantis/MOMENT 包含 UCR train splits，CauKer 不含 real data；这避免把官方 accuracy 直接当作严格 OOD，但仍保留了不对称比较。【p.3；p.9 Figure 7 caption；p.23 footnote】
- **异质性延后到附录**：主文报告 128-UCR aggregate 和核心 scaling curves，domain-wise Spectro/Power 反例在 Appendix H，MI 负面结果在 Appendix I；聚合均值承担主决策，领域例外需要额外翻页。【p.23–25】
- **失败案例有明确位置但规模小**：DotProduct-only 的 76.79% 与 RBF-only 的 78.07% 在 Appendix C.3 中直接给出，说明作者没有只保留完整 bank 的正向结果；但没有报告更多 single-family 或异常生成失败率。【p.19】
- **定性图替代了机制量化**：DTW matrix、PCA、UMAP、Attention Rollout 让 cluster/diversity/localization 可视化，但没有 cluster purity、classwise test、注意力 faithfulness 或负例覆盖率。【p.6–8、p.26–28】

## 9. 结论、limitations 与闭环

### 9.1 结论段落动作

|段|动作|回收内容|证据|
|---:|---|---|---|
|1|重述问题/方法|CauKer 将 GP kernel composition 与 SCM 结合；synthetic-only pretraining 可匹配更大 real datasets；data/model scaling 在 synthetic 上清晰、real-world 上 irregular/absent。|p.10 §5 第一段。|
|2|回收意义|将 pretraining data quality/structure 提升为与 architecture innovation 并列的 TSFM 路径，鼓励 scalable/general-purpose TSFM dataset design。|p.10 §5 第二段。|
|3|`limitations`|只研究两种不同范式的模型；compute-intensive，未纳入大规模 forecasting benchmark，理由是 forecasting benchmark 对 classification utility 有限。|p.10 Limitations。|

结论没有新数字，但以「match」「first in-depth」「profound impact」「equivalent gains」等较强措辞回收主张。limitations 仅两句，未回收 univariate-only、real-checkpoint leakage、seed/uncertainty、single-kernel failure、domain deficits 或 causal claim 的验证边界；这些边界分散在正文和附录。【p.5、p.9–10、p.19、p.23】

### 9.2 闭环矩阵

|引言主张|方法响应|证据响应|结论响应|状态|
|---|---|---|---|---|
|分类 synthetic data 需要 temporal motifs 与 class-separable structure|GP kernels/means + SCM DAG/activation pipeline|Figure 1、Table 1、DTW Figure 2、SWD/CKNNA Table 6|称 data temporally realistic、causally coherent|`partially_closed`：生成 DAG 给出机制，但没有 ground-truth causal validation 或 class labels 的定量识别。|
|CauKer 可高效生成且优于现有 synthetic generators|five-step pipeline、root-only GP sampling|Table 1、Table 2；Mantis/MOMENT 都以 100K 对照|称 synthetic-only 可 match larger corpus|`partially_closed`：Q1 比较完整，但生成默认超参数、跨硬件成本和重复不充分。|
|synthetic pretraining 有清晰 data/model scaling laws|改变 UEA/CauKer data size 与 Mantis/MOMENT capacity|Figures 3–6、Tables 7–8|称 synthetic scaling clear，real scaling irregular|`partially_closed`：只在两模型、UCR/UEA 设置中检验；部分文字与 Table 8 仍需对齐。|
|CauKer 可替代 real-world pretraining|冻结 encoder、相同 UCR zero-shot protocol|Figure 7、Appendix H/I、Table 12–13|称 sample-efficient、robust/transferable|`partially_closed`：官方 real corpus 包含 UCR train split，且 Mantis/MOMENT classifier/head 不同。|
|CauKer 支持 OOD generalization 并减轻 leakage|synthetic corpus 不接触 UCR/real classification benchmark|UCR test 未见于 official corpus；WOODS/clinical/Chronos 扩展|称 beyond UCR distribution generalization|`partially_closed`：对 CauKer 的数据隔离明确，但未提供独立 contamination audit 或所有 real baseline 的一致 OOD。|
|SCM causal structure 是额外收益|Mean+KernelSynth→CauKer 的 component progression|Table 1、Table 6、Figure 2|称 causal structure benefits zero-shot classification|`partially_closed`：结构替代结果存在，但没有因果干预或 ground-truth causal comparison。|
|可扩展到 multivariate TSFM|同一 SCM nodes 可视为 channels，Algorithm 1 输出 `d×L`|仅生成算法支持 `d`，主实验把 node trajectory 当独立 univariate series|结论未把 multivariate 当已验证能力|`not_testable_here`：正文明确限制到 univariate inputs。|
|可迁移到 forecasting|将 CauKer 直接用于 Chronos、无 task-specific modification|27 disjoint subsets、MASE 与 Wilcoxon `p=0.84`|称 forecasting transfer effective|`partially_closed`：有附录实证，但属于单一 Chronos pipeline 的扩展而非分类主线的普遍保证。|
|表示学习保留语义因子/聚焦判别片段|Mantis frozen encoder 及 UMAP/PCA/Attention Rollout|Figures 4–5、11–13|称 robust/interpretable/transferable representations|`partially_closed`：图形证据支持可解释性线索，没有 classwise/faithfulness 定量检验。|

## 10. 附录职责

附录 p.15–29 共 15 个物理页（p.15 与 references 混合）。其长度约为主文 91.8%，并承担了几乎所有复现和扩展信息：loss/architecture、生成器伪代码、bank 图、敏感性、完整 scaling 表、domain/OOD、forecasting、representation、fine-tuning 和 clinical evaluation。主文通过 Appendix A–N 的显式句子调用这些内容；Appendix O 是 LLM writing-assistance disclosure。

|附录一级模块|页码|对象/职责|类别|正文调用与依赖|
|---|---:|---|---|---|
|A Overview of pre-training datasets|15|Table 3；代表性 TSFM 的 synthetic/real、time points、series count、open status。|`dataset_detail`|p.3 相关工作讨论数据类别，附录总览明确指向。|
|B Loss and architecture of Mantis and MOMENT|15–16|Mantis cosine/contrastive loss、MOMENT masked MSE、T5/ViT architecture、patching。|`extended_method`|p.3 说明 detailed formulations 在 Appendix B；p.5 仅保留范式摘要。|
|C Details of CauKer|16–20|Algorithm 1；36-kernel bank；mean/activation bank；Tables 4–5 消融。|`extended_method`|p.4 伪代码和 bank visualizations 引用 Appendix C；p.5 指向 C.2/C.3。|
|D Additional qualitative analysis|19–21|SWD2/CKNNA 定义、five independent draws、Table 6。|`additional_result`|p.7 直接称 additional qualitative analysis 在 Appendix D。|
|E Experimental details of Section 4.2.1|21|Mantis/MOMENT configs、UEA 0.1–100%、CauKer scales、Table 7 exact values。|`implementation_detail`|p.7 data-scaling 段调用 Appendix E。|
|F Experimental details of Section 4.2.2|22|MOMENT 77/248/783M、Mantis 0.75–114.14M architecture、Table 8。|`implementation_detail`|p.7–8 model-scaling 段调用 Appendix F。|
|G Experimental details of Section 4.4|22|best-loss epoch、Mantis 100 epochs、MOMENT 10 epochs、checkpoint parameter note。|`implementation_detail`|p.9 Q3 只给主要 corpus，精确训练选择在 G。|
|H Domain-wise analysis on UCR|23–24|Table 9，15 Type domains，CauKer100K vs Official，Power/Spectro 例外。|`additional_result`|p.10 只笼统说 UCR；没有在主文展开 domain heterogeneity。|
|I Supplementary evaluation on WOODS|24–25|17 datasets、ERM/Mantis-2M/CauKer100K、Table 10。|`robustness`|p.10 明确指向 Appendix I。|
|J Pre-training Chronos on CauKer|25–26|MASE `(1)`、Table 11、27 disjoint subsets、Wilcoxon test。|`additional_result`|p.10 Extension to forecasting 指向 Appendix J。|
|K Visualization of embeddings|26–27|Figure 11 UMAP frequency/slope/bias 与 Figure 12 PCA UCR/UEA/CauKer。|`qualitative_example`|p.8 Figure 4–5 的 embedding/non-linearity 解释在此扩展。|
|L Attention Rollout analysis|27–28|Figure 13，ECG/Fish 中 CauKer-100K 与 real Mantis 的 attention maps。|`qualitative_example`|p.27 说明 representation comparison，主文未给 attention 结果。|
|M Additional experiments on downstream fine-tuning|28–29|Table 12，real 1.89M 与 CauKer 100K/1M fine-tuning accuracy。|`additional_result`|p.9 Q3 末尾直接指向 Appendix M。|
|N Supplementary evaluation on irregular time series|29|Table 13，P12/P19 的 AUROC/AUPRC。|`robustness`|p.10 Q3 结果和 p.29 标明 irregular multivariate extension。|
|O Use of Large Language Models|29|写作语言润色 disclosure；声称 LLM 未参与 ideation、design、analysis、conclusion。|`other`|没有主文调用；是附录末尾的声明。|

附录迁移保留了「CauKer 由什么组成、主分类结果是什么」这条正文闭环。Figure 1、五步 prose、Table 1、Figure 3/7 已留在正文。迁移显著增加复现成本：默认 bank 规模、精确 model variants、loss、完整 accuracy、OOD domain、seed/硬件仍需跨 p.15–29 拼接；附录也没有提供 formal proof、causal identification 或主结果的不确定性，因此它补足 implementation，却没有补足理论与统计闭环。

## 11. 用词与修辞观察

排除 references、公式碎片、表格数字和模板固定语后，正文高频实词集中在 `time series`、`synthetic`、`pre-training`、`classification`、`TSFM`、`data`、`model`、`UCR`、`scaling`、`real-world`、`CauKer`、`accuracy`、`dataset`、`generation`、`kernel`、`causal`。二元/三元短语主要是 `zero-shot classification`、`synthetic data generation`、`time series foundation models`、`Gaussian Process kernel composition`、`Structural Causal Models`、`real-world datasets`、`scaling laws`、`sample-efficient pre-training`；这些词同时是领域名词和论证动作，不是纯模板填充。

主张动词按语境可分为：提出 `propose/introduce/present`（方法与结论开头）；经验 `show/demonstrate/reveal/observe/find/indicate`（摘要、Findings、Q1–Q3 results）；推断 `suggest/hypothesize/believe/likely explain`（UEA mismatch、Mantis inductive bias、saturation、domain deficit）；限定 `restrict/consider only/note/without`（univariate、官方 corpus 泄漏、forecasting extension）。强主张通常用 `clear`, `state-of-the-art`, `superior`, `robust`, `effectively`, `strong`，弱主张用 `likely`, `may`, `hints`, `to some extent`, `plausibly`；但 conclusion 将 several empirical findings 合并为较强的 general-purpose TSFM 叙述。

词频定位的误切分风险包括：PDF 将 CauKer 设计名排成 `C AU K ER`，`GP`、`SCM`、`TSFM`、`UCR` 等缩写在提取文本中可能与相邻词分离；Figure/Table caption 的坐标刻度和公式变量不应当计入实词频。自动脚本的 `13,755` 英文 token 是全 PDF 的粗测量，不代表正文 13,755 词；正文/refs/appendix 的人工边界修正见第 1、12 节。

## 12. 测量分歧与定位修正

|项目|自动草稿/版面|按完整 PDF 的修正|证据|
|---|---|---|---|
|appendix 边界|自动 `APPENDIX_HEADING` 对 spaced-capital `A PPENDIX` 不稳，`main_words_provisional` 把 p.1–29 全算入，appendix 为空。|正文 p.1–10；references p.11–15；appendix 从 p.15 末至 p.29，p.15 为混合页。|p.10–15，layout observation。|
|图计数|自动 `figure_captions=10`，因 spaced-capital/复合 caption 和附录图识别不全。|逐页可见 Figure 1–13，共 13 个；Figure 7 是表格+两曲线复合图，仍按一个 Figure 计。|p.4、p.6、p.8–9、p.18–19、p.23、p.26–28。|
|表计数|自动 `table_captions=13`。|逐页 Table 1–13，共 13 个；Table 4–5 归 ablation，其余按 results/appendix。|p.6、p.20–25、p.29。|
|正文词数|自动全 PDF 13,755，无法区分 references/appendix。|英文词元粗估：正文 6,157、references 2,400、appendix 5,651；p.15 重叠页不作互斥总和。|p.1–29，layout/measurement correction。|
|Mantis 预训练 series count|主文 Figure 7 写 `1.89M`；Appendix A footnote 说 official repo 更新数约 `1.38M`，arXiv 初版约 `7M`。|保留两处事实并标明版本冲突；sample-efficiency 比例取主文叙述，不把 1.38M 推回主表。|p.9 Figure 7；p.16 footnote 1。|
|WOODS win count|p.24 prose 称 `12 wins (including ties)`；Table 10 行 `Win counts (out of 17; ties counted)` 给 CauKer100K=11。|结果记录两者，不选择性修正；overall average 0.820 和 domain 数字不受该文字/表格冲突影响。|p.24–25 Table 10。|
|Mantis accuracy drop|p.10 称 CauKer 与 official Mantis 的 accuracy drop `<0.1%`；Figure 7 数字 78.66−78.55=0.11 percentage point。|记录原文和由表格直接算出的 0.11 pp，不把 `<0.1%` 当精确事实。|p.9 Figure 7；p.10 Results。|
|MOMENT model-scaling wording|p.8 称除 `single outlier` 外 CauKer 随容量严格上升，同时称 10M 增益很小；Appendix Table 8 的 10M 列 77.49→77.51→77.85 实际单调上升。|以 Table 8 数值为版面事实；将“outlier/saturation”保留为作者解释，而非独立反例。|p.8；p.22 Table 8。|
|自动 theorem/equation|自动只识别 1 个 numbered equation、无 theorem；这与 PDF 一致，但可能漏掉无编号 display。|只有 Appendix J MASE `(1)` 有编号；另有 7 个无编号 display，未发现 theorem/lemma/proof。|p.15–16、p.20、p.25。|

## 13. 最终判断

- **单一主线**：分类时间序列预训练同时需要时间模式和可分的跨样本结构；CauKer 以随机 GP kernel/mean 生成具有趋势、周期和异常的 roots，再用 SCM DAG、随机线性聚合和非线性 activation 传播，形成合成分类语料；在冻结 Mantis/MOMENT 上，生成器对照、data/model/training-time scaling、sample efficiency 和外部 benchmark 按同一条链回收。其最强可辩护结论是「结构化 synthetic data 在此有限 zero-shot classification 设置中比简单 synthetic baselines 更有用」，而非已证明的一般 causal foundation-model 定律。【p.3–10】
- **正文保留的决策关键内容**：问题/缺口、Figure 1 pipeline、five-step mechanism、Q1–Q3、Table 1 generator comparison、Table 2 runtime、Figure 2 clustering、Figure 3–7 的主 scaling/sample-efficiency 证据，以及 official checkpoints 的 UCR train exposure 说明。这些足以让读者理解为什么比较以及结果方向。【p.4–10】
- **移入附录的细节及其代价**：Mantis/MOMENT losses、完整 architecture、Algorithm 1、36 kernels、activation/mean samples、exact scaling values、domain/OOD、Chronos MASE、UMAP/PCA/Attention Rollout、fine-tuning/clinical metrics和 LLM disclosure 均在附录。迁移保留了正文决策链，但降低了复现自足性；尤其 seed、硬件、默认生成超参数和不确定性仍未完整提供。【p.15–29】
- **最有效的写作/图表/公式模式**：Figure 1 把「GP temporal prior→SCM dependency→series」画成可读的机制链；Table 1 以 `SCM→FPFN→KernelSynth→Mean+KernelSynth→CauKer` 的逐级对照显示组件贡献；Figure 3 用四面板将 data/model scaling 并置；Figure 7 把 corpus size、UCR inclusion 和训练曲线合在同一结果对象中。相较于复杂公式，图表对核心论证更有效。【p.4、p.6、p.8–9】
- **最大叙事缺口**：`causally coherent`/`causal structure` 是生成机制的 DAG 语义。PDF 没有提供 ground-truth intervention 或 causal recovery 实验来验证因果结论；scaling-law 结论仅覆盖两种模型和 UCR/UEA 设定；主分类表大多是无重复的点估计，且真实 checkpoint 暴露 UCR train split。Mantis 计数、WOODS wins、accuracy-drop 和 model-scaling wording 还存在可定位冲突。【p.3、p.8–10、p.16、p.24】
- **可迁移规则**：合成预训练论文应把「生成先验的各组件」「数据隔离/基线暴露」「数据与模型规模曲线」「失败/敏感性对照」放在同一证据链中，并同时给出聚合指标的分母、重复层级和跨域异质性；否则可扩展性和 sample efficiency 只能是包装后的均值主张。
- **规则的适用边界**：该规则适用于 univariate/fixed-length time-series foundation-model pretraining 及相似的生成数据研究；若对象是 multivariate irregular series、forecasting 或需要 causal guarantee 的任务，必须增加与任务匹配的结构、OOD 控制和因果识别证据，不能由 CauKer 的 DAG 生成过程直接外推。【p.5、p.10、p.24–29】

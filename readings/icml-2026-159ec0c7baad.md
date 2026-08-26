# EcoVLA 深读备忘

- **paper_id**：`icml-2026-159ec0c7baad`
- **题目**：Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models
- **版本**：arXiv 2602.00780v1，PDF 日期 2026-01-31。本备忘以本地 verified preprint 为准。
- **选择标记**：ICML 2026 spotlight。
- **阅读范围**：`corpus/preprints/icml-2026-159ec0c7baad.pdf` 与 `corpus/preprint_text/icml-2026-159ec0c7baad.txt`；逐页核对物理页 1–12，包含 references、Appendix A–C。

## 1. 版面边界与页级地图

PDF 共 12 页。正文为物理页 1–8，references 为页 9–10，appendix 为页 11–12；正文最后一页的 `6. Conclusion` 在页 8，页 9 从 `References` 开始，页 11 从 `A. Experimental Settings` 开始。正文和 references 使用双栏排版；页 3 的 Fig. 2 跨两栏，页 7 的 Tables 1–3 为宽表，Table 4 与 Fig. 3/4 分布在局部栏宽内。页 8 的 Fig. 5、Table 5 与 Fig. 6 形成紧凑浮动体组合。页 10 只占左栏，右下方大面积留白；appendix 页 11–12 改为单栏。页 1 的 Fig. 1 位于 abstract 右侧，但它在引言中承担动态稀疏变化的动机，因此按引言语义归类。

| 版面区段 | 物理页 | 语义模块 | 估计词数 | 边界与作用 |
|---|---:|---|---:|---|
| Abstract | 1 | `abstract` | 191 | 9 句；包括方法、数字结果与真实机器人验证 |
| 1. Introduction | 1–2 | `introduction` | 900 | 从 VLA 延迟瓶颈推进到两项设计及结果预览 |
| 2. Related Work | 2 | `related_work` | 220 | 两个主题簇：VLA 与高效 VLA |
| 3. Preliminaries；3.1–3.2 | 2–3 | `other` | 510 | VLA 组成与 structured pruning 形式化；含 Eq. (1)–(4) |
| 4. Methodology；4.1–4.3 | 3–6 | `method` | 2,600 | EAP、I2O 与 kernel/metric 实现；含 Eq. (5)–(13) |
| 5. Experiments；5.1–5.2 | 6–8 | `experimental_design`/`results` | 1,350 | 设计在页 6，主结果跨页 6–8 |
| 5.3 More Results | 8 | `ablation` | 480 | 加速分解、pruning-ratio、overhead、α/p |
| 6. Conclusion | 8 | `conclusion` | 112 | 重述框架、验证场景与部署意义 |
| References | 9–10 | `other` | 930 | 26 条左右的参考文献条目；不计入正文语义词数 |
| Appendix A. Experimental Settings | 11 | `appendix` | 610 | 模型、加速方法、超参数和 benchmark 细节 |
| Appendix B. Real-robot Analysis；C. Hyperparameter Analysis | 12 | `appendix`/`limitations` | 365 | 失败位置分析与 α/p 解释 |

`theory` 没有独立 theorem、lemma、proposition、corollary 或 proof；理论性公式属于方法的形式化、复杂度和延迟解释。因此 `theory` 模块按 `not_applicable` 编码；工程公式仍保留为形式化、复杂度和延迟解释。

## 2. 摘要逐句功能编码

摘要共有 9 句，约 191 词。功能顺序为「对象与瓶颈 → 动态缺口 → 既有方法失败 → EcoVLA 核心方案 → 两个组件 → EAP 机制 → I2O 机制 → 仿真数字结果 → 真实机器人验证」。最强主张位于倒数第二句：`state-of-the-art performance`、`1.60×`、`0.4%`、`2.18×`、`0.5%` 同时出现；局限只以前述“latency/sparsity trade-off”间接呈现，摘要没有单独的失败条件或计算成本数字。

| # | 句子（按 PDF 原文） | 词数 | 功能 | 限定词、数字、比较对象与承接 |
|---:|---|---:|---|---|
| 1 | While Vision-Language-Action (VLA) models hold promise in embodied intelligence, their large parameter counts lead to substantial inference latency that hinders real-time manipulation, motivating parameter sparsification. | 25 | `object_scope`, `problem_gap` | `hold promise`、`substantial`；把 VLA 与 real-time manipulation 的延迟问题相连 |
| 2 | However, as the environment evolves during VLA execution, the optimal sparsity patterns change accordingly. | 14 | `problem_gap` | `However`、`evolves`；承接静态参数规模，提出环境条件变化 |
| 3 | Static pruning lacks the adaptability required for environment dynamics, whereas fixed-interval dynamic layer pruning suffers from coarse granularity and high retraining overheads. | 22 | `problem_gap` | `lacks`、`suffers`；比较 static pruning 与 fixed-interval dynamic layer pruning |
| 4 | To bridge this gap, we propose EcoVLA, a training-free, plug-and-play adaptive pruning framework that supports orthogonal combination with existing VLA acceleration methods. | 22 | `core_idea`, `method` | `training-free`、`plug-and-play`、`orthogonal`；直接回答上一句的缺口 |
| 5 | EcoVLA comprises two components: Environment-aware Adaptive Pruning (EAP) and Interleaved Inference Orchestration (I2O). | 13 | `method` | 两组件名称，承接总框架 |
| 6 | EAP is a lightweight adaptive channel pruning method that incorporates the temporal consistency of the physical environment to update sparsity patterns. | 21 | `method` | `lightweight`、`temporal consistency`；说明组件一的机制 |
| 7 | I2O leverages the FLOPs bubbles inherent in VLA inference to schedule the pruning method in parallel, ensuring negligible impact on latency. | 21 | `method` | `leverages`、`negligible`；说明组件二如何处理开销 |
| 8 | Evaluated on diverse VLA models and benchmarks, EcoVLA delivers state-of-the-art performance, achieving up to 1.60× speedup with only a 0.4% drop in success rate, and further reaches 2.18× speedup with only a 0.5% degradation when combined with token pruning. | 43 | `experimental_setup`, `quantitative_result`, `qualitative_result`, `impact_claim` | `diverse`、`state-of-the-art`、`up to`、`only`；比较 vanilla/Token pruning 组合，给出最强数字主张 |
| 9 | We further validate the effectiveness of EcoVLA on real-world robots. | 10 | `qualitative_result`, `impact_claim` | `further`；把证据范围从 simulator 扩展到 physical robot |

## 3. 引言的论证推进

引言的完整推进链是：`context → problem → failure_of_prior_work → missing_insight → core_idea → method_preview → result_preview`。它没有单独的 numbered contribution list；三个方法预览段落承担了贡献列表的功能。

| 段落动作 | 页码与证据锚点 | 上一段留下的问题 | 当前段回答与下一段钩子 |
|---|---|---|---|
| `context` | p.1, §1；“moving embodied intelligence toward generalization by injecting semantic understanding into robot control” | 需要说明 VLA 为何值得优化 | 交代 VLA 的任务价值，下一段转向实时部署瓶颈 |
| `problem` | p.1, §1；“inference latency remains the primary bottleneck for real-time control” | 价值带来何种系统约束 | 把参数规模、VLM backbone 与延迟绑定，下一段列 token/model pruning |
| `failure_of_prior_work` | p.1, §1；“token pruning ... at the risk of losing critical semantics” | 只减少输入 token 会损失什么 | 指出 token-level 加速的语义代价，下一段转向 model pruning |
| `failure_of_prior_work` | p.1–2, §1；“static pruning ... fail to adapt to the dynamic evolving task environment” | 静态稀疏模式如何面对环境变化 | 指出 static 失配与重训练成本，下一段说明 dynamic pruning |
| `failure_of_prior_work` | p.2, §1；“coarse layer-level granularity overlooks fine-grained intra-layer redundancy” | fixed-interval dynamic 方法为何仍不足 | 指出 router 开销与 layer 粒度问题，下一段抽象为研究缺口 |
| `missing_insight` | p.2, §1；“a training-free, fine-grained, and environment-aware ... method is urgently needed” | 现有两类方法都不能同时满足要求 | 明确目标组合：training-free、fine-grained、environment-aware |
| `problem` | p.2, §1；“two major challenges remain” | 目标组合的技术阻断点是什么 | 展开环境变化/时间连续性与在线开销两项挑战 |
| `core_idea` | p.2, §1；“we propose EcoVLA ... minimizing pruning overhead through non-blocking parallel inference” | 如何同时应对两项挑战 | 给出总框架；下一段拆解 EAP |
| `method_preview` | p.2, §1；“EAP ... temporal feature aggregation strategy” | 如何识别随环境改变的稀疏模式 | 用 visual similarity、历史特征和 temporal consistency 识别 channel |
| `method_preview` | p.2, §1；“I2O ... interleaving pruning computations into the FLOPs bubbles” | 如何让在线识别不拖慢控制环 | 用 inference/pruning 两条 stream 隐藏开销 |
| `result_preview` | p.2, §1；“evaluate EcoVLA ... two simulators ... three VLA models” | 方法是否跨模型、跨环境成立 | 预告 1.6×、0.4%、2.18×、0.5% 与 Kinova Gen3；随后进入 Related Work |

引言约 900 词，主要由 context/problem/failure 与方法预览构成；没有独立贡献列表，也没有以“我们的贡献是……”形式重复摘要。它包含可证伪的效率和成功率数字，但未把 seed、重复次数、失败判定或统计不确定性带入引言。`Figure 1` 的热图被放在 abstract 旁边，却在引言中以“as shown in Fig.1”承担动态 sparsity-shift 的动机，形成版面模块与论证模块的错位。

## 4. 相关工作

相关工作只有正文第 2 节，位于 p.2，分为两个粗粒度主题簇，约 220 词、约占正文 4%。它不按年代组织，也没有独立 taxonomy 图表。

1. **VLA Models（`credit_or_foundation` + `positioning_only`）**：以 RT-1、π0、OpenVLA 等工作建立 VLA 从 VLM 到 action modalities 的背景，比较维度是 action head 的轻量性与 VLM backbone 的计算瓶颈。证据为 p.2 §2 的“action heads ... are lightweight”与“VLM backbone remains the dominant computational bottleneck”。
2. **Efficient VLA Models（`taxonomy` + `nearest_neighbor_contrast` + `gap_creation`）**：按 token pruning/KV caching、static model sparsification、fixed-interval dynamic pruning 分类。最相近对比是 static 方法缺少环境适应且需要 retraining，dynamic 方法有 task dependence 但仍有 retraining cost、transferability 和粒度问题；段末建立 training-free、plug-and-play、fine-grained adaptive pruning 的缺口（p.2 §2）。

相关工作没有把 EAP 或 I2O 的算法介绍提前重复一遍，且引用主要只完成定位；后文引用仍承担机制来源或对照方法身份（例如 PPsp、FastV、VLA-Cache、Wanda），但没有逐项回到 related-work 的比较维度作因果验证。

## 5. 方法与理论性对象

### 5.1 形式化对象与方法链

- **全局目标（p.3, §3.2, Eq. (1)）**：VLA 为 `π_Θ`，LLM backbone 参数为 `Θ`；结构化 binary mask `m ∈ {0,1}^{|Θ|}`，分组元素共享 mask。目标是最小化 dense/pruned policy divergence `L(π_Θ, π_Θ⊙m, D)`，约束为 `||m||_0 = κ`，其中 `D` 是 calibration dataset，`κ` 是 sparsity constraint。
- **layer-wise reconstruction（p.3, §3.2, Eq. (2)–(3)）**：第 `l` 个 block 将 `X^l ∈ R^{B×S×D}` 映射为 `X^{l+1}=X^l+F^l(X^l)`；`F^l(X^l)=X^{l,int}(W^{l,final})^T`，`X^{l,int}=T^l(LN(X^l))`。`T^l` 可为 `W^K` 或 `W^up`，`W^{l,final}` 可为 `W^O` 或 `W^down`。
- **structured channel/head 对齐（p.3, §3.2, Eq. (4)）**：保留 `C^l ⊆ {1,...,C_in}`，对 gate/up 保留行、对 down 保留列；attention pruning 同时处理 `W^{Q,K,V}` 的 output channels 与 `W^O` 的 input channels。
- **EAP predictor（p.4, §4.1.1, Eq. (5)–(7)）**：用 visual encoder 的 `f_t,f_{t-1}∈R^{N×D}` 计算平均 token-wise cosine similarity `s_t`；滑动窗口 `H_t={s_{t-T},...,s_{t-1}}` 存最近 `T` 帧；当 `s_t < Quantile(H_t,p)` 时触发 `u_t=1`。`p` 越高越敏感，越低越稳定；作者进一步声称 rapid motion 时 quantile 自然降低、stable phase 时提高。
- **Temporal Consistency Pruning（p.4, §4.1.2, Eq. (8)–(11)）**：在 frame `t` 触发后先做 dense inference，算出的 pattern 从 `t+1` 起用于 sparse inference。对 `X^{l,int,τ}` 沿 sequence 求平方和得到 instantaneous channel feature `ε_k^{l,τ}`；以 calibration data 初始化历史向量 `E^{l,(0)}`，用 `α` 融合历史与当前，用 `λ` 对 full channels 做 EMA，再以 final-weight magnitude 与 fused feature 的组合分数 `S_k^{l,τ}` 选低重要度 channel。`α∈[0,1)` 越大，更新越保守。
- **I2O（p.5, §4.2.1–4.2.2）**：VLM backbone 的大 GEMM 被定义为 compute-bound，action expert 的轻量 MLP/diffusion 在 batch size 1 时留下 FLOPs bubbles。Inference Stream 运行当前 dense/sparse policy，Pruning Stream 在共享内存中取得中间 activation，在 backbone 与 action expert 的资源互补区计算下一步 pattern。
- **延迟关系（p.5, §4.2.2）**：串行方案为 `L_synch=T_infer+T_prune`；I2O 为 `L_I2O=T_infer+δ`，`δ` 包括 SM scheduling、memory-bandwidth contention 和 minor GPU competition。作者把 `δ` 归因于轻量模块与 FLOPs bubbles 中的执行。
- **硬件实现（p.6, §4.3.1–4.3.2）**：sparse linear transformation 使用直接加载 retained weights 的 Triton kernel；`W_down` 与 `W_O` 用 column-major 促进 coalescing；gate/up/SiLU/逐元素乘法融合为一个 Triton kernel。dense metric 侧预计算 weight norms（声称 99.97% reduction）、预分配 activation buffers，并把各层 metric 堆叠为 contiguous tensors 做 batched computation。

方法动作转移序列可写为：`setup_notation → state_problem → derive → define_component → explain_mechanism → derive → give_intuition → instantiate_algorithm → state_complexity → connect_to_prediction → connect_to_experiment → summarize`。其中 `connect_to_prediction` 由“环境变化应引起 pattern 更新”和“FLOPs bubbles 应吸收 pruning cost”组成；后者在 Table 5 与 Fig. 4 得到延迟层证据，前者主要靠 α/p 图与最终 success rate 间接支撑。

### 5.2 方法段落动作与证据

| # | 动作 | 页码、章节与证据 | 解决的前文问题 |
|---:|---|---|---|
| 1 | `setup_notation` | p.3, §3.2；“optimize a structural binary mask”与 Eq. (1) | 把“冗余参数”转成可约束的 structured mask |
| 2 | `derive` | p.3, §3.2；“Each block l transforms ... via a residual mapping”与 Eq. (2) | 提供逐层重构的计算单位 |
| 3 | `define_component` | p.3, §3.2；“structured pruning aligns output channels with input channels”与 Eq. (4) | 连接 channel/head mask 与可执行权重切片 |
| 4 | `define_component` | p.3–4, §4.1.1；“lightweight environment aware sparsity variations predictor” | 识别环境引起的 pattern 变化 |
| 5 | `derive` | p.4, §4.1.1, Eq. (5)–(7)；平均 cosine、`H_t` 与 quantile trigger | 避免静态阈值在分布漂移下失效 |
| 6 | `give_intuition` | p.4, §4.1.1；“rapid motion ... quantile naturally decreases” | 解释触发器的自调节叙事 |
| 7 | `state_problem` | p.4, §4.1.2；“relying solely on instantaneous features is sub-optimal” | 引出物理连续性与历史 prior |
| 8 | `derive` | p.4, §4.1.2, Eq. (8)–(11) | 从 activation norm、EMA/fusion 到 channel importance |
| 9 | `connect_to_prediction` | p.4, §4.1.2；“applied starting from frame t + 1 for sparse inference” | 明确 pattern 更新的时序因果 |
| 10 | `state_complexity` | p.5, §4.1.3, Eq. (12)；`FLOPs ≈ 5ND + 2SCin + 3CinCout + 4Cin` | 量化 EAP 在线开销 |
| 11 | `state_problem` | p.5, §4.2.1, Eq. (13)；“GPU Tensor Cores ... near-peak saturation” | 找到 VLA pipeline 的可用计算空隙 |
| 12 | `define_component` | p.5, §4.2.2；“decouple ... step t + 1 ... parallel pruning stream” | 用非阻塞两条 stream 处理 batch=1 的开销 |
| 13 | `derive` | p.5, §4.2.2；`L_synch` 与 `L_I2O` | 把资源调度转成延迟预测 |
| 14 | `instantiate_algorithm` | p.6, §4.3.1；Triton、coalescing、fused kernels | 将结构化 channel mask 变成硬件收益 |
| 15 | `instantiate_algorithm` | p.6, §4.3.2；allocation-free caching、batched metric computation | 降低 dense pattern computation 的内存与 launch 成本 |
| 16 | `summarize` | p.6, §5 前；“training-free ... diverse VLA architectures” | 从方法组件转入跨模型实验 |

### 5.3 公式、理论对象和伪代码计数

PDF 中公式总数、displayed equation 数和带编号公式数均为 13，编号为 Eq. (1)–(13)。Eq. (1)–(4) 位于 `other`（Preliminaries），Eq. (5)–(13) 位于 `method`。论文没有 theorem、lemma、proposition、corollary、proof，也没有 Algorithm/pseudocode。公式承担的角色如下：Eq. (1)–(4) 是核心形式化链；Eq. (5)–(11) 是 EAP 机制链；Eq. (12) 是复杂度估计；Eq. (13) 是 I2O 资源解释。Eq. (12)–(13) 是解释/诊断性质，未形成可证伪的复杂度定理或硬件保证。

## 6. 实验设计

### 6.1 研究问题与对象

论文没有预先列出编号化 research questions 或 hypotheses；目标由引言和 §5.1 隐含给出：EcoVLA 是否能跨 VLA 架构，在环境变化下保持 success，同时降低 latency，并能与 FastV/VLA-Cache 叠加。三类 VLA 为 OpenVLA-OFT、π0.5、CogACT；静态 pruning 对照为 Wanda；组合加速器为 FastV 与 VLA-Cache（p.6, §5.1）。

### 6.2 数据、任务、模型和评测

- **模拟器与任务**（p.6, §5.1）：LIBERO 含 LIBERO-Spatial、Object、Goal、Long 四个 suites；SIMPLER 含 Visual Matching 与 Variant Aggregation。Google Robot arm 上评估 Pick Coke Can、Move Near、Open/Close Drawer、Open Top Drawer and Place Apple 四项任务。
- **真实机器人**（p.6–7, §5.1、Table 4）：7-DoF Kinova Gen3，三项任务为 Place the apple in the basket、Put the pill bottle in the cabinet、Place the banana in the basket；Fig. 3 展示三项操作。
- **pruning ratios**（p.6, §5.1）：OpenVLA-OFT 与 CogACT 为 25%/40%；π0.5 为 25%/37.5%，以适应架构。
- **指标**（p.6, §5.1）：task success rate (%)、inference latency (ms)、FLOPs (T)。表格按四个 suite/task 汇总并给 Average；真实机器人按每项任务的成功次数与 20 次试验呈现。
- **实现与硬件**（p.6, §5.1）：NVIDIA RTX 3090；latency 按 VLA-Cache 的测量方式；集成 VLA-Cache 时使用 eager `LlamaAttention`，其他情形默认 FlashAttention。
- **训练与数据规模**（p.6 与 Appendix A.4, p.11）：EcoVLA 本身被定位为 training-free；真实 π0.5 为部署而 fine-tune 10,000 steps。每项真实任务收集 50 demonstrations，冻结 VLM、只 LoRA-adapt VLM、full fine-tune action expert，global batch size 32、single GPU。
- **超参数**（Appendix A.3, p.11）：OpenVLA-OFT 与 CogACT 用 `p=5, α=0.7`；OpenVLA-OFT 的 LIBERO-Object/Goal 用 `α=0.9`，Spatial/Long 用 `α=0.7`；π0.5 用 `p=80`、`α=0.7`。

### 6.3 控制、复现粒度与缺失项

同一 RTX 3090、沿用 FastV/VLA-Cache 原始设置、统一报告 success/latency/FLOPs，构成有限的测量控制（p.6）。但论文没有报告 simulation 的 random seeds、每个任务的 episode 数、重复测量次数、训练随机性、硬件时钟状态或显著性检验；也没有独立说明数据泄漏控制、匹配的随机轨迹、预注册 failure criterion。真实机器人每项任务的 20 个随机 object placements、每次重新随机位置在 Appendix B（p.12）明确给出，这一粒度没有扩展到模拟结果。实验顺序大体对应引言：Table 1–3 做跨模型/环境主结果，Table 4 做真实部署，Fig. 4–6 做加速、折衷和超参数分析，Appendix A–C 补充实现与失败解释。

## 7. 结果、统计与可视化

论文主要使用算术平均、成功次数/20 和单次 latency；没有报告 seed-level 离散量、置信区间、bootstrap、Bayesian analysis、hypothesis test、multiple-comparison correction 或 regression。表格注释能解释列名、方向箭头和 pruning ratio，但无法独立提供 episode 分母、重复次数或不确定性。

### 7.1 主结果清单

| 结果主张 | 数值与比较 | 统计处理与作者解释 | 不利解释/证据边界 |
|---|---|---|---|
| OpenVLA-OFT 主结果（Table 1） | 25%：Ours 96.8% average、113.98 ms、1.26×；40%：94.0%、101.58 ms、1.41×。Wanda 为 93.8%/124.32 ms/1.15× 与 88.8%/106.47 ms/1.35×。LIBERO-Goal 上 Ours 比 Wanda 高 7.4/12.4 个百分点。 | 四个 LIBERO suite 的 Average；无方差。作者归因于环境适应与 I2O 隐藏额外 pruning overhead（p.7, Table 1 与 §5.2）。 | 25% 的表格平均值高于 vanilla 96.7%，与正文“0.35% loss”不一致；不同 suite 的差异也未给 episode 分母。 |
| FastV/VLA-Cache 叠加（Table 1） | FastV+Ours：25% 96.2%、65.85 ms、2.18×；40% 92.9%、61.16 ms、2.35×。VLA-Cache+Ours：25% 95.5%、121.24 ms、1.34×；40% 93.6%、108.48 ms、1.50×。 | 与 vanilla 平均比较；作者称组合“orthogonal”，并将 25% FastV 的 −0.5 个百分点解释为 pruning 的 regularization effect（p.7–8）。 | 组合结果依赖多个算法同时改变 token/channel/cache，无法从表格识别每个组件的独立因果贡献。 |
| π0.5 跨模型结果（Table 2） | 25%：96.7%、62.66 ms、1.31×；37.5%：95.0%、55.98 ms、1.46×，vanilla 为 96.9%、81.94 ms。LIBERO-Object 在 37.5% 为 98.4%，比 vanilla 98.2% 高 0.2 个百分点。 | 四个 suite 算术平均；作者把 Object 的小幅提升解释为 selective pruning 的 regularization（p.8, §5.2）。 | 仅有一个 π0.5 表格和一个 GPU latency；没有 seed 或置信界，不能区分稳定提升与测量波动。 |
| CogACT / SIMPLER（Table 3） | Visual Matching：25% 71.7%、72.65 ms、1.44×；40% 73.6%、66.43 ms、1.57×，vanilla 73.3%。Variant Aggregation：25% 58.6%、73.98 ms、1.43×；40% 60.6%、66.25 ms、1.60×，vanilla 61.0%。 | 四个任务平均；作者称 40% 时分别仅 −0.3% 与 −0.6%（p.8）。 | 表中 Visual Matching 40% 是 +0.3、Variant Aggregation 40% 是 −0.4；正文数字与表格方向/幅度不一致。 |
| 真实机器人（Table 4、Fig. 3） | baseline：12/20、18/20、16/20，86.08 ms；Ours：12/20、16/20、15/20，68.40 ms，延迟比约 1.26×。 | 每项任务 20 次，未报告聚合成功率不确定性；作者称 minor performance drop 与 real-robot viability（p.7–8；Appendix B p.12）。 | 三项任务共 60 次且任务难度不同；失败集中在 workspace boundary（Appendix B），因此“real-world effectiveness”范围只覆盖该 setup。 |
| dense/sparse acceleration breakdown（Fig. 4） | dense 原始 215.24 ms，经 parallel paradigm 36.04、allocation-free 10.00、batched metric 21.14 后为 148.06 ms；sparse 原始 156.12 ms，经 sparse kernel 32.63、memory coalescing 13.49、kernel fusion 1.76 后为 108.24 ms。 | 累积时间分解，不是重复试验；作者把它作为硬件设计贡献的机制证据（p.7–8, Fig. 4）。 | 加速项为串联累计展示，缺少 component deletion、次序置换或资源计数，不能单独估计每项的可迁移效果。 |
| pruning-ratio trade-off（Fig. 5） | success rate 在 40% 以下保持相对稳定，超过 40% 后快速下降；speedup 随 ratio 上升；作者认为 40% 是折衷点（p.8, Fig. 5）。 | 曲线点，未给原始数表、重复数或误差表达。 | 图中 task/model 聚合方式未展开；“optimal”是本文 setup 的工程折衷，而非普适阈值。 |
| pruning-stream overhead（Table 5） | Normal VLA Inference 143.56 ms；I2O 148.06 ms；δ=4.50 ms。 | 单次或未说明次数的 latency 对照；作者称 overhead limited（p.8, Table 5）。 | “negligible”没有相对任务频率、吞吐或多次测量的误差支撑。 |
| α/p 超参数（Fig. 6、Appendix C） | LIBERO-Long 上 α=0.7 的 success rate 标注 87.0%；π0.5 的 p=80% 图点标注 87.0%。高 α 被解释为 sparsity lag，低 α 为不稳定；低 p 漏掉细节，高 p 对噪声敏感。 | 单一曲线/柱状图，无不确定性；作者以峰值支持 temporal consistency 与 noise filtering（p.8、p.12）。 | 峰值所在点未说明重复/分母；同一 `p` 在不同模型的取值尺度不统一（OpenVLA/CogACT `p=5`、π0.5 `p=80`）。 |

### 7.2 视觉与表格清单

| 对象 | 模块、页码、尺寸/内容 | 任务 |
|---|---|---|
| Fig. 1 | `introduction`，p.1，单栏右侧热图 | 展示 attention-head 与 MLP-channel importance 随 inference time 变化，建立 pattern shift 动机；证据锚点为图注“importance scores vary dynamically”。 |
| Fig. 2 | `method`，p.3，跨两栏 | 显示 EAP 的 predictor、historical/current feature fusion、sparse LLM，以及 I2O 的 inference/pruning streams 和 shared memory。 |
| Table 1 | `results`，p.7，宽表 | OpenVLA-OFT 在 LIBERO 四 suites、25%/40% 的 success/FLOPs/latency/speedup 与 FastV/VLA-Cache 组合。 |
| Table 2 | `results`，p.7，宽表 | π0.5 在 LIBERO、25%/37.5%。 |
| Table 3 | `results`，p.7，宽表 | CogACT 在 SIMPLER Visual Matching/Variant Aggregation、25%/40%。 |
| Table 4 | `results`，p.7，局部栏宽 | π0.5/Kinova Gen3 三任务成功次数与 latency。 |
| Fig. 3 | `results`，p.7，局部栏宽照片 | 三项真实机器人 manipulation 场景。 |
| Fig. 4 | `ablation`，p.7，局部栏宽堆叠柱状图 | dense/sparse latency 的累计加速分解。 |
| Fig. 5 | `ablation`，p.8，单栏上方曲线 | success rate 与 latency/speedup 随 pruning ratio 的折衷。 |
| Table 5 | `ablation`，p.8，局部栏宽 | Normal inference 与 I2O 的 pruning-stream overhead。 |
| Fig. 6 | `ablation`，p.8，局部栏宽双面板 | α temporal inertia 与 p sensitivity 对 success rate 的影响。 |
| Fig. 7 | `appendix`，p.12，单栏居中照片/示意 | Kinova Gen3、两台 Intel RealSense D435i 的硬件布置。 |

## 8. 消融、负面结果与自我设限

正文 §5.3 约占正文 8 的最后一页，使用 3 个 figures、1 个 table，覆盖四种识别目标：计算组件贡献、ratio 敏感性、并行 overhead、超参数敏感性。

| 对象/识别目标 | 状态 | 证据与解释 |
|---|---|---|
| acceleration component breakdown | `observed` | p.7–8 Fig. 4；依次报告 parallel paradigm、allocation-free caching、batched metric computation，以及 sparse kernel、coalescing、kernel fusion 的累计时间。它是累计分解，非严格组件删除实验。 |
| pruning-ratio sensitivity | `observed` | p.8 Fig. 5；超过 40% 后 success rate 快速下降，显示性能—latency 折衷。 |
| I2O overhead | `observed` | p.8 Table 5；I2O 比 normal inference 多 4.5 ms。 |
| α/p sensitivity | `observed` | p.8 Fig. 6、Appendix C p.12；α=0.7、p=80% 的峰值叙事。 |
| EAP vs no-EAP、I2O vs serial、temporal fusion vs instantaneous-only | `not_present` | 正文和 Appendix 没有给出这些完整组件删除或替代基线；Fig. 4 的硬件累计分解不能替代该识别。证据为 p.8 §5.3 只列四项“More Results”，以及 p.4–5 方法中仅给出最终流程。 |
| 跨模型/任务异质性 | `observed` | Tables 1–3 覆盖三种模型与两种 simulator 设置，但聚合列与有限任务数仍掩盖 suite/task 差异。 |
| 失败案例与计算成本 | `observed` | Appendix B p.12 报告 boundary placements 的失败集中；Fig. 4/ Table 5 报告 latency cost。 |

明确的负面信息包括：OpenVLA-OFT 在 40% 时平均从 96.7% 降到 94.0%；π0.5 在 37.5% 时为 95.0%；SIMPLER Variant Aggregation 25% 时为 58.6%；真实机器人 Ours 在 Task2/Task3 少于 baseline；Fig. 5 显示高 ratio 后性能下降；Appendix B 指出 workspace boundary 是失败高发位置（p.7–8、p.12）。作者将这些信息放在主结果、折衷图和 appendix 的 failure analysis 中，没有单独的 `Limitations` 节。

自我设限的位置与方式：

- **摘要**：只写“0.4% drop”“0.5% degradation”等范围限定，没有直接列出失败条件。
- **引言**：把挑战定义为环境变化、时间连续性与 overhead，未列 deployment scope。
- **实验**：使用“marginal/minor/negligible”等定性弱化词，同时报告有限的 benchmark、GPU 和 task 设定（p.6–8）。
- **结论**：称 real robots 与 high-fidelity simulators 均验证，但未回收 boundary failure 或数字不一致。
- **Appendix B**：最具体的 `data`/`deployment` 边界是 boundary placement 造成 representation loss 与 spatial-generalization 脆弱性（p.12）。
- **Appendix C**：给出 `hyperparameter` 边界，高 α/低 α、低 p/高 p 各自的失效机制（p.12）。
- **缺失**：没有 ethics、broader impact、energy、memory footprint、跨硬件或真实频率/吞吐的设限分析。

## 9. 结论与闭环矩阵

结论（p.8, §6）只有一段：重述 EcoVLA 是 training-free、plug-and-play adaptive pruning，回收 EAP + I2O 的在线更新与低 overhead，最后回收 real robot 与 simulator 验证。没有新数字，也没有新的方法组件。它没有显式回收 Fig. 5 的 40% 折衷、Table 5 的 4.5 ms、Appendix B 的 boundary failures 或 Table 1/3 的数字矛盾。

| 引言主张 | 方法回应 | 实验/消融回应 | 结论回应 | 闭环状态 |
|---|---|---|---|---|
| 环境变化会改变最优 sparsity pattern | EAP 的 visual similarity、quantile trigger、temporal fusion（p.4） | Fig. 6 α/p 与跨任务结果；没有直接 pattern-detection metric | 只笼统说 online update | `partially_closed` |
| 需要 training-free、fine-grained、environment-aware pruning | structured channel/head mask、EAP、无需 EcoVLA 训练（p.3–4） | 三种 VLA、Wanda 对照、多个 ratio（p.7–8） | 明确重述 training-free adaptive framework | `closed`（范围限于这些模型/设置） |
| 在线 pruning overhead 会伤害 batch=1 控制 | Eq. (13)、I2O 两条 stream、`T_infer+δ`（p.5） | Table 5 δ=4.5 ms、Fig. 4 latency breakdown | 称 negligible overhead | `partially_closed`（无重复/资源计数） |
| I2O 可与其他 acceleration 正交叠加 | shared-memory stream 与 retained kernels（p.5–6） | FastV+Ours 2.18×/2.35×，VLA-Cache+Ours 1.34×/1.50×（p.7–8） | 回收组合框架 | `closed`（仅测试两种组合） |
| EcoVLA 达到 state-of-the-art | 机制设计与硬件实现 | 主要对照 Wanda、FastV、VLA-Cache；未覆盖全部 contemporaneous baselines | 以 validated/real-world 概括 | `partially_closed` |
| 1.60× 且约 0.4% drop | EAP + I2O + kernels | CogACT 表给出 1.60×，但 success 表/正文 loss 口径不完全一致 | 摘要保留该范围 | `partially_closed` |
| FastV 组合 2.18×、0.5% degradation | channel pruning 与 token pruning 分工 | Table 1 25% FastV+Ours 2.18×、平均 96.2% 对 vanilla 96.7% | p.8 直接回收 | `closed`（该行数值闭合，因果归因仍有限） |
| 可用于真实机器人 | I2O/EAP 的 deployment path 与 π0.5 fine-tuning | Table 4 三任务、每任务 20 次、1.26×；Appendix B 识别 boundary failures | 仅称 validate effectiveness | `partially_closed` |

## 10. Appendix 职责

Appendix 共 2 页，约 975 词，物理长度约为正文 8 页的四分之一。正文通过 “See App.A”、 “More details are provided in the App.A.4”、 “We further analyze ... in App.B” 和 “Additional analysis is provided in the App.C” 调用 appendix。它承载复现所需的模型背景、超参数、真实数据采集和失败解释；主文仍承担决策关键的 Tables 1–5、Fig. 4–6、核心 latency/success 比较。

| 一级模块 | 页码 | 类别 | 对象与正文调用 | 对正文自足性的影响 |
|---|---:|---|---|---|
| A.1 VLA Model Details | 11 | `extended_method` | OpenVLA-OFT、π0.5、CogACT 的 backbone/action expert 说明；p.6 “See App.A for further details” | 模型组成细节移出正文，但主结果身份仍可读 |
| A.2 Acceleration Method Details | 11 | `extended_method` | FastV 与 VLA-Cache 的 token/cache 机制；被 §5.1 组合实验依赖 | 理解组合基线需要此处，正文只给名字 |
| A.3 Implementation Details | 11 | `hyperparameter` | `p`、`α` 按模型/suite 的取值；p.6 “More hyperparameter details ... App.A.3” | 不读 appendix 无法复现关键触发器设置 |
| A.4 Benchmarks Details | 11 | `dataset_detail`, `implementation_detail` | Kinova Gen3、两台 D435i、50 demonstrations、10k steps、LoRA/full fine-tune、batch 32；p.6 “More details ... App.A.4” | 真实实验训练与采集条件依赖 appendix |
| B. Real-robot Analysis | 12 | `failure_case` | 每任务 20 个随机 object placements；boundary failures 与 representation loss 推测；p.8 “underlying reasons in App.B” | 这是 real-robot 的核心适用边界，若只读正文会遗漏 |
| C. Hyperparameter Analysis | 12 | `hyperparameter`, `ablation` | p=80%、α 中间值峰值、过高/过低的机制解释；p.8 “Additional analysis ... App.C” | 补足 Fig. 6 的文字解释，未新增独立数据集 |

Appendix 没有 proof、正式 robustness suite、伦理/社会影响、energy/memory audit 或跨硬件测试。主张“real-world effectiveness”依赖 A.4/B 的采集和失败上下文；主张 α/p 机制依赖 C；EAP/I2O 的基本算法和决策结果仍留在正文。

## 11. 用词与修辞

排除 references、公式碎片、表格数值和模板固定语后，论文高频实词集中于 `VLA/model/inference/pruning/environment/sparsity/latency/feature/channel/temporal`；二元搭配集中于 `adaptive pruning`、`sparsity pattern`、`VLM backbone`、`real-time control`、`FLOPs bubbles`、`action expert`；三元搭配集中于 `environment-aware adaptive pruning`、`interleaved inference orchestration`、`temporal consistency pruning`。

主张动词包括 `propose`、`introduce`、`leverage`、`enable`、`achieve`、`validate`、`demonstrate`；限定词包括 `lightweight`、`training-free`、`plug-and-play`、`negligible`、`marginal`、`minor`、`substantial`、`robust`。对比词包括 `however`、`whereas`、`conversely`、`in contrast`；因果词包括 `to address`、`therefore`、`as a result`、`consequently`；贡献词包括 `propose`、`introduce`、`present`。

`we propose` 主要出现在引言与方法入口；`we introduce` 出现在 EAP/I2O 机制段；`we achieve`、`we observe`、`we evaluate`、`we validate` 主要集中在实验。强主张（`state-of-the-art`、`commanding lead`、`fully taps`、`redefines the standards`）与弱化/限定词（`only`、`negligible`、`minor`、`marginal`）并存。高频词主要由真实方法动作驱动，少量模板性修辞来自加速论文常见的“lightweight / plug-and-play / negligible overhead”组合。

## 12. 叙事规避、未闭合点与测量分歧

### 12.1 中性可验证的呈现策略

1. **聚合掩盖异质性**：Tables 1–3 报告四项 suite/task 的 Average，同时把 LIBERO-Goal、Variant Aggregation 等差异放在列内；平均值无法替代任务级分母（p.7）。
2. **不确定性缺席**：所有 success、latency、FLOPs 和超参数曲线均没有 seed、重复次数或误差表达（p.6–8）。这属于报告粒度缺口，不能据此推断作者动机。
3. **定性弱化**：真实结果使用 `minor performance drop`，overhead 使用 `negligible/limited`；相应数字仍给在 Table 4/5（p.7–8），因此可核对但语气比数值更强。
4. **附录迁移**：关键 hyperparameter、真实训练条件和 failure boundary 放入 A.3/A.4/B/C；正文通过交叉引用保留入口，但不读 appendix 会低估 deployment 条件（p.6、p.8、p.11–12）。
5. **基线范围收窄**：`state-of-the-art` 出现在摘要，正文主要使用 Wanda、FastV、VLA-Cache 和 vanilla；未提供完整 contemporary leaderboard（p.1、p.6–8）。
6. **口径不一致**：正文 success-loss 数字与表格平均值有冲突，且真实结果错误引用 Table 3；这些是可复核的编辑/测量分歧，不应解释为策略性行为（p.7–8）。

### 12.2 测量与版面分歧

- **OpenVLA-OFT 25%**：§5.2 写“0.35% reduction”；Table 1 的 Average 为 Ours 96.8%、Vanilla 96.7%，直接差值为 +0.1 个百分点。40% 的表格差值为 −2.7，接近正文写的 2.8%（p.7）。
- **FastV/VLA-Cache 25%**：FastV+Ours 平均 96.2% 相对 vanilla 96.7% 为 −0.5，正文此处吻合；VLA-Cache+Ours 平均 95.5% 相对 vanilla 为 −1.2，和“negligible 0.5% loss”不吻合（p.7–8）。
- **CogACT**：Visual Matching 40% 的 Ours 73.6% 高于 vanilla 73.3%，正文写“drop only 0.3%”；Variant Aggregation 40% 为 60.6% 对 61.0%，表格差值 −0.4，正文写 −0.6。两处幅度/方向至少有一处错误（p.7–8）。
- **真实结果交叉引用**：`Results on Real Robot` 写“as shown in Tab.3”，真实机器人数据在 Table 4；Table 3 是 CogACT/SIMPLER（p.7–8）。
- **峰值与尺度**：Appendix C 将 π0.5 的 `p=80%` 作为峰值；A.3 写 `p=80`，而 OpenVLA/CogACT 使用 `p=5`。论文没有解释 quantile 参数在不同实现中是否同尺度（p.8、p.11–12）。

## 13. 最终判断

1. **单一主线**：VLA 的最优 structured sparsity 随物理环境改变；EcoVLA 用 visual similarity + temporal feature fusion 及时重算 channel/head pattern，再用 I2O 把重算放入 VLA 的 FLOPs bubbles，从而在 batch=1 控制环中交换少量 success 变化换取低 latency。
2. **正文保留的决策关键内容**：Eq. (1)–(11) 的 mask、trigger、fusion、importance 链；Eq. (12)–(13) 的成本/资源解释；Fig. 2 的两流架构；Tables 1–4 的跨模型与机器人结果；Fig. 4–6 的速度、ratio、overhead、α/p 证据。
3. **移入 appendix 的细节及其影响**：模型结构、FastV/VLA-Cache 背景、每模型超参数、50 demonstrations、LoRA/full fine-tune、D435i 布置、20 次 placement 和 boundary failures移入 A/B/C。迁移使正文主结果可扫读，却让真实部署可复现性与适用边界依赖 appendix。
4. **最有效的模式**：Fig. 2 把机制、数据流、共享内存和时序放在同一图；Table 1 把 vanilla、Wanda、EcoVLA 与两种叠加方法置于同一 latency/success/FLOPs 表；Fig. 4 将“隐藏开销”的系统叙事落到可加总的毫秒数。
5. **最明显的叙事规避与读者成本**：state-of-the-art 的比较范围窄；平均值、单次 latency 和无误差曲线增加结果稳定性判断成本；组件累计分解不能识别 EAP/I2O 各自因果贡献；正文与表格的 loss 数字和 Table 3/4 引用错误削弱可审计性。
6. **可迁移规则**：当方法主张“在线适应且开销可隐藏”时，应把触发状态转移、并行调度、端到端 latency、task-level success、component-isolation 与失败边界放在同一闭环中，并让正文数字与表格使用同一分母和比较基线。
7. **适用边界**：该规则适用于 batch=1、环境连续变化、系统瓶颈同时包含 compute/memory 资源空隙的 embodied inference；对 batch 大小、硬件、传感器噪声、离散任务跳变或未测模型，本文证据不足以外推。

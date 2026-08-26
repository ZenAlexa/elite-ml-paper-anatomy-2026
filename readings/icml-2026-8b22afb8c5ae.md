# 深读备忘：Alignment-Sensitive Minimax Rates for Spectral Algorithms with Learned Kernels

- **paper_id**：`icml-2026-8b22afb8c5ae`
- **论文**：Dongming Huang、Zhifan Li、Yicheng Li、Qian Lin，ICML 2026 Spotlight。
- **事实源**：`corpus/preprints/icml-2026-8b22afb8c5ae.pdf`，73 个 PDF 物理页；页首标记为 arXiv 2509.20294v4（2026-05-11）。本次逐页读取了正文、references 与 Appendices A–I。没有随该 PDF 发现独立 supplementary 文件，记为 `not_present`。
- **版本边界**：这是与 OpenReview forum `4HrWo5x7YF` 对齐的已验证预印本，不把可能存在的 camera-ready 差异写入判断。

## 1. 文档边界、页级地图与版式

PDF 使用双栏排版。标题和作者信息跨栏；正文、references 和 appendix 均为双栏。图 1、图 2 位于第 8 页并横跨两栏，图 3 至图 5 位于附录并占据较大的横向版面。推导页的显示公式密集，尤其是 Appendix G（第 36–64 页）；第 73 页末留有大块空白，未承载新的文本内容。这些版式事实来自逐页 PDF 观察。

| PDF 物理页 | 边界与标题 | 语义模块 | 版面与内容作用 |
|---|---|---|---|
| 1 | title、Abstract、`1. Introduction` 开始 | abstract / introduction | Abstract 在左栏顶部；引言从同页展开。|
| 2 | 引言收束；`2. Background on Kernel Methods` | introduction / method | 贡献 (iii)、解释链和 notation 后进入 RKHS 背景与 sequence-model bridge。|
| 3–4 | `3. Effective Span Dimension and Span Profile`；`3.1` | method / theory | 定义 sequence model、spectral estimators、ESD、oracle-PC 风险与 ESD class。|
| 5 | `3.2. Span Profile`；`4. Minimax Optimal Convergence Rates` | method / theory | 从噪声索引的 span profile 转向 quota sequence 的 minimax rate。|
| 6–7 | `5. Adaptive Eigenvalues via Over-parameterized Gradient Flow`；`6. Numerical experiments` 开始 | method / theory / experimental_design | 给出 OP-GF、Assumption 5.1 和 Theorem 5.2；随后说明合成数据设计。|
| 8 | 图 1、图 2 | results | 两张跨栏图；图 1 为 span profile，图 2 为 oracle PC error 与 ESD。|
| 9 | §6 收束、`7. Discussion`、Acknowledgements、Impact Statements、References 开始 | results / conclusion / limitations / other | 第 9 页是混合页：左栏结束讨论，右栏下部已进入 references。|
| 9–12 | References | other | references 共 4 个物理页，首页与 conclusion 混排。|
| 13–15 | Appendix A: Related Work | related_work / appendix | 五个比较簇：early stopping、signal-agnostic dimension、target-kernel alignment、estimator-guided measures、PCR。|
| 15–18 | Appendix B: correlated noise 与 fixed-design linear model | appendix | whitening、SVD bridge、PCR 和图 3 的线性模型设置。|
| 18–25 | Appendix C: RKHS regression | appendix | KPCPE、随机设计方差、minimax extension；图 3 位于第 19 页，图 4 位于第 25 页。|
| 25–27 | Appendix D: Measuring Alignment via ESD | appendix | 稀疏信号对比与 evolving-eigenfunction 的 pathwise ESD；图 5 位于第 27 页。|
| 27–34 | Appendix E: sequence-model proofs | appendix / theory | Proposition 3.2、Theorems 3.3/4.3 与例子的证明。|
| 34–36 | Appendix F: proofs for Appendix C | appendix / theory | Proposition C.4、Theorems C.7/C.8 的证明。|
| 36–64 | Appendix G: OP-GF proof | appendix / theory | concentration、ODE lemmas、endpoint ordering、top-`m` exchange；为 Theorem 5.2 提供主体证明。|
| 64–69 | Appendix H: application of Theorem 5.2 | appendix | 在具体稀疏错配例子中逐项验证 theorem conditions。|
| 69–73 | Appendix I: ridge saturation | appendix / theory | 说明 ridge-guided dimension 不能代替 ESD。|

完整主论文页按完全承载主文的页计为 8 页（第 1–8 页）；第 9 页作为 conclusion/reference 混合页单列。references 为第 9–12 页，appendix 从第 13 页开始至第 73 页，共 61 个物理页。直接由 PDF 提取的词数估计为正文约 5,149 词、附录约 21,430 词；该比例约为 4.16:1，主要由证明附录驱动。

### 固定语义模块的篇幅与对象清单

下表的正文份额以约 5,149 词的主文基数计算；附录中的模块不计入这一份额。方法与理论在同一节交错，按段落功能而非标题机械切开。

| 模块 | 状态 | 估计词数 | 主文份额 | 图 / 表 / 算法 / 显示公式 | 依据 |
|---|---:|---:|---:|---:|---|
| abstract | observed | 141 | 0.027 | 0 / 0 / 0 / 0 | 第 1 页，8 句。|
| introduction | observed | 1,014 | 0.197 | 0 / 0 / 0 / 0 | 第 1–2 页。|
| related_work | observed | 1,290 | 0 | 0 / 0 / 0 / 1 | Appendix A，第 13–15 页。|
| method | observed | 1,362 | 0.265 | 0 / 0 / 0 / 8 | §2、§3 的对象/定义及 §5 的 OP-GF。|
| theory | observed | 1,001 | 0.194 | 0 / 0 / 0 / 4 | §3–§5 的 proposition/theorem 与 rate chain。|
| experimental_design | observed | 430 | 0.084 | 0 / 0 / 0 / 0 | 第 7、18、24、26 页的合成设计。|
| results | observed | 330 | 0.064 | 2 / 0 / 0 / 0 | 第 8–9 页，图 1–2。|
| ablation | not_present | 0 | 0 | 0 / 0 / 0 / 0 | 无组件删除或替代组件的 ablation section。|
| conclusion | observed | 328 | 0.064 | 0 / 0 / 0 / 0 | §7，第 9 页。|
| limitations | observed | 139 | 0.027 | 0 / 0 / 0 / 0 | 分散于第 6、7、9、18、21–23、26 页；无独立标题。|
| appendix | observed | 21,430 | 0 | 3 / 0 / 0 / 125 | Appendices A–I，第 13–73 页；编号公式延续 (13)–(137)。|
| other | observed | 404 | 0.078 | 0 / 0 / 0 / 0 | §2 的背景余量、Acknowledgements、Impact Statements 与 references。|

编号公式从 (1) 连续到 (137)，因此至少有 137 个编号显示公式；另有未编号的推导显示式，精确总显示式数因 PDF 数学提取分段而标为 `uncertain`。自动草稿曾给出 136 个 display count，与物理页中出现的 (137) 不一致，已在 JSON 的 `measurement_disagreements` 记录。

## 2. 摘要逐句功能编码

| # | 句子 | 词数 | 功能 | 限定、比较与承接 |
|---:|---|---:|---|---|
| 1 | “We study spectral algorithms in the setting where kernels are learned from data.” | 13 | object_scope | 锁定 learned-kernel spectral algorithms 的对象。|
| 2 | “We introduce the effective span dimension (ESD), an alignment-sensitive complexity measure that depends jointly on the signal, spectrum, and noise level σ².” | 23 | core_idea, method | `jointly` 把 signal、spectrum、noise 绑定为同一复杂度对象。|
| 3 | “The ESD is well-defined for arbitrary kernels and signals without requiring eigen-decay conditions or source conditions.” | 16 | theory | 用 `arbitrary` 与两个被免除的传统假设限定适用面。|
| 4 | “We prove that for sequence models whose ESD is at most K, the minimax excess risk scales as σ²K.” | 21 | theory, quantitative_result | 唯一显式定量主张为符号 rate，而非实验数值。|
| 5 | “Furthermore, we analyze over-parameterized gradient flow and prove that it can reduce the ESD.” | 14 | method, theory | `Furthermore` 将 rate result 接到 adaptive mechanism。|
| 6 | “This finding establishes a connection between adaptive feature learning and provable improvements in generalization of spectral algorithms.” | 17 | impact_claim | 把第 5 句压缩为解释链。|
| 7 | “We demonstrate the generality of the ESD framework by extending it to linear models and RKHS regression, and we support the theory with numerical experiments.” | 25 | experimental_setup, qualitative_result | `generality` 由两类 extension 与 numerical experiments 支撑；未报数据集或数值。|
| 8 | “This framework provides a novel perspective on generalization beyond traditional fixed-kernel theories.” | 12 | impact_claim | 以相对 fixed-kernel theory 的解释定位收尾。|

功能顺序为 **范围 → 核心定义 → 假设边界 → rate theorem → adaptive theorem → 意义 → extension/experiment → positioning**。摘要没有报告 benchmark、样本数、均值、error bar 或显著性；它报告了理论量 `σ²K`，并以 “support the theory with numerical experiments” 作无数值的经验结论。最强可证伪主张位于第 4–5 句，紧随定义之后。[PDF p.1, Abstract, “minimax excess risk scales as σ² K”, explicit]

## 3. 引言的论证推进

| 段落动作 | 页码与短锚点 | 上一段留下的问题 | 本段回答 | 下一段钩子 |
|---|---|---|---|---|
| context | p.1, §1, “Many modern learning procedures are adaptive” | 无 | representation update 会改变 induced kernel，且可能改善 generalization | 固定理论能否解释？ |
| failure_of_prior_work | p.1, §1, “NTK approximation is intrinsically non-adaptive” | adaptive advantage 未被解释 | NTK/RKHS fixed-kernel analysis 无法解释 feature evolution | 还缺什么理论对象？ |
| problem | p.1, §1, “fixed spectral assumptions” | 传统 source/eigen-decay 假设对 learned kernel 难以成立 | 把问题收束为需要不依赖固定谱假设的框架 | 引入 ESD。 |
| core_idea | p.1, §1, “propose the Effective Span Dimension” | 没有 alignment-sensitive quantity | ESD 联结 signal、spectrum 和 noise，并直接联系 minimax risk | 论文做出哪些可检验承诺？ |
| contribution_list | p.1, §1, “sharp minimax optimal convergence rates” | 定义尚未给出结果 | sequence-model rates、linear/RKHS extension | adaptive mechanism。 |
| contribution_list / scope_boundary | p.2, §1, “fixed eigenbasis” | learned eigenfunctions 的情形尚未解决 | OP-GF theorem 处理 fixed eigenbasis；evolving eigenfunctions 仅 pathwise formulation + deep linear experiment | 给出解释链。 |
| theory_preview | p.2, §1, “reduction in ESD” | 为什么对 generalization 有意义 | 大 ESD 对应 minimax-hard class；训练后较小 ESD 对应更容易的 class | 指向 appendix 的比较。 |
| roadmap | p.2, §1, “deferred to Appendix A” | 相关概念界限 | 将 balanced cutoff、alignment、effective dimension 的细节移至 Appendix A | §2 的背景和 sequence bridge。 |

推进链可概括为：**adaptive representation 可能改变 kernel → fixed-kernel conditions/NTK 无法说明 feature learning → 用 noise-indexed alignment ESD 替代 source/eigen-decay 前提 → ESD class 的 minimax rate → fixed-eigenbasis OP-GF 可降低 ESD → linear/RKHS extension 与数值图示**。贡献列表与摘要重复了核心对象、rate、OP-GF 和 extension；它增加了一个明确的范围边界（evolving eigenfunctions 的 general theorem 未给出）。贡献列表含可证伪理论主张，没有实验数字。[PDF pp.1–2, §1, “a general theorem ... is left for future work”, explicit]

## 4. 相关工作如何定位论文

相关工作没有独立的主文 section。引言内以 citation clusters 建立动机；完整的 taxonomy 位于 Appendix A（pp.13–15），并通过对象和假设差异避免重述方法。

| 簇 | 位置 | move | 比较维度 | 对论文主张的作用 |
|---|---|---|---|---|
| fixed-operator early stopping / spectral cutoff | p.13, A.1 | nearest_neighbor_contrast, gap_creation | stopping rule for one prescribed operator vs population alignment index over target–kernel pair | 说明同一 bias–variance crossing 的用途不同。|
| effective dimension / effective rank | p.13, A.2 | taxonomy, limitation_of_prior | spectrum-only vs signal–spectrum–noise | 建立 ESD 能区分 eigenvalue allocation 的缺口。|
| kernel-target alignment、cumulative power distribution | p.14, A.3 | nearest_neighbor_contrast, credit_or_foundation | global similarity / source-condition theory vs noise-indexed minimax class | 承认 alignment antecedents，同时说明 ESD 的 rate calibration。|
| estimator-guided measures / ridge | p.14, A.4 | contrast_alternative, gap_creation | chosen estimator 的 saturation vs intrinsic difficulty | 为 Appendix I 的 ridge counterargument 预埋逻辑。|
| PCR 文献 | pp.14–15, A.5 | credit_or_foundation, taxonomy | proportional asymptotics 与 non-asymptotic PCR | 把 oracle PC 选择放入现有 PCR context。|

后续正文确实再次使用这些比较：§3.1 指向 A.1/A.2/A.3/A.4，Appendix I 具体证明 ridge saturation；因此 citation 并非只作名录。[PDF p.4, §3.1, “Appendix A.2 contrasts ESD”, explicit]

## 5. 方法、理论与逻辑单元

### 5.1 对象、输入、输出与机制

1. **Sequence reduction**：从 RKHS transformed observation 得到近似 `z_j = θ_j* + ξ_j`，并设 noise variance `σ² = σ₀²/n`。第 2 节明确说这一 bridge 在有限样本会有 inflated variance，严格 RKHS treatment 在 Appendix C。[PDF p.2, §2, “error ... will inflate the estimation variance”, explicit]
2. **谱排序与 ESD**：按 decreasing `λ` 得到 permutation `π`；`d†(σ²; θ*, λ)` 是最小 `k`，使排序后 tail 的平均平方能量不超过 `σ²`。输出是 population descriptor，不是训练输入。[PDF p.3, Def. 3.1, “smallest number k of leading eigencoordinates”, explicit]
3. **Span profile**：`D_{θ*,λ}(τ)=d†(τ;θ*,λ)` 把 ESD 对 noise level 的变化编码为 profile。它允许在同一 target 下比较两个 spectra 的 alignment。[PDF p.5, Def. 3.6, “depends only on θ* and the ordering of λ”, explicit]
4. **ESD-bounded class**：固定 quota `K` 或 `K_n`，用 PC top-`K` estimator 构造上界、Assouad hypercube 构造下界，得到 minimax rate。[PDF pp.3–6, Thms. 3.3/4.3, “minimax risk grows linearly with K”, explicit]
5. **Adaptive eigenvalues**：OP-GF parameterizes `θ_j=a_j b_j^D β_j`。强信号坐标得到较快 eigenvalue growth；block ordering 与 top-`m` exchange 使 tail energy 不增，从而推出 endpoint ESD reduction。[PDF pp.6–7, §5; pp.39–48, G.2, “top-m set exchange”, explicit]
6. **Model extensions**：Appendix B 用 whitening/SVD 接 fixed-design linear regression；Appendix C 用 KPCPE 和 design-adjusted variance 接 RKHS；Appendix D 定义 evolving-eigenfunction 的 pathwise ESD。[PDF pp.15–26, Appendices B–D, explicit]

方法段落的动作转移为：`setup_notation → state_problem → derive sequence bridge → define_component (ESD) → explain_mechanism (tail bias/variance) → connect_to_prediction (PC/minimax) → define span profile → state rate class → instantiate OP-GF → connect_to_experiment → summarize`。没有 pseudocode 或 algorithm block；训练规则只以 Equation (12) 的连续时间 gradient flow 给出。

### 5.2 核心理论结果及闭环位置

| 结果 | 前提与结论 | 证明位置 | 后续实证/说明对应 |
|---|---|---|---|
| Proposition 3.2 | 对 sequence PC，oracle risk 在 `(d†−1)σ²` 与 `2d†σ²` 之间。 | pp.27–28, E.1 | 图 2 将 PC components 用 ESD oracle 决定。|
| Theorem 3.3 | 任意 spectrum、ESD≤`K` 的 class 的 minimax risk 为 `Θ(Kσ²)`。 | pp.28–30, E.2 | §3 的核心 rate claim；无必要的 empirical proof。|
| Proposition 3.7 | span profile 与 trade-off function 都 nonincreasing，且可比较两个 spectrum。 | p.5, §3.2；独立 proof 位置 `uncertain` | 图 1 以 profile 曲线展示其比较用途。|
| Theorem 4.3 | quota sequence 满足 Condition 4.1 时，风险下界 `c₀σ₀²K_n/n`；top-`K_n` PC 给 matching upper bound。 | pp.28–29, E.2 | Example 4.4 说明 source/eigen-decay rate 不 sharp 的情形。|
| Theorem 5.2 | Assumption 5.1 与强/弱信号、separation、top-block 条件下，以至少 `1−4/n` 概率有 `d†(t₂)≤d†(t₁)`。 | pp.36–64, Appendix G | 图 1–2 是同一 OP-GF 机制的数值图示；只支持、并不替代 theorem。|
| Theorem B.3 | fixed-design linear model、ESD quota `K` 的 minimax prediction risk 为 `Θ(σ₀²K/n)`。 | p.18；证明说明为 Theorem 3.3 的同类论证而省略 | 图 3 对 d† 与 rescaled oracle PCR risk。|
| Proposition C.4、Theorems C.7/C.8 | bounded target、`(K,n)`-regular kernel 等前提下，KPCPE risk/minimax RKHS rate 为 ESD-controlled `K/n` 量级。 | pp.34–36, Appendix F | 图 4 比较 empirical KPCPE risk 与 ESD bounds。|
| Theorem I.6 | 在 Assumption I.2 与 small-regularization regime，ridge risk 下界由 ridge saturating dimension 控制。 | p.72, I.4 | Example I.7 说明这个 index 在 smooth source class 不能恢复 intrinsic ESD complexity。|

Appendix G 含 Lemmas G.1–G.21 与 Propositions G.10、G.11、G.18、G.19：它们依次给 concentration、ODE hitting-time/control、strong/tiny-coordinate endpoint bounds、ordering relations、top-`m` exchange。该技术链直接服务 Theorem 5.2，没有以新经验结果包装。[PDF pp.36–64, Appendix G, “The proof ... consists of three stages”, explicit]

## 6. 实验设计与复现粒度

论文没有预先编号的 research questions、预注册计划、真实数据集或硬件报告；这些项目均为 `not_present`。实验依次对应：ESD/风险关系、fixed-eigenbasis adaptation、linear/RKHS extension、evolving-eigenfunction pathwise illustration。

| 实验 | 设置与控制 | 指标、比较与重复 | 复现边界 |
|---|---|---|---|
| 主文图 1–2：sequence OP-GF | `λ_j=j^{-γ}`；非零 signal 位于 `ℓ(j)=⌊j^q⌋`，`q≥1` 控制错配；`z_i∼N(θ_i*,σ²)`。图 1 固定 `n=10000, σ₀=1, d=5000, J=15, p=2.5, γ=1`，展示 `q=1,1.5,2,3`、`t=0,20,40,60,80`。 | 图 1 比 span profile；图 2 比 oracle-PC squared error 与 ESD，`D=0,1,3`。图 2 的平均基于 20 Monte Carlo replications，error bar 为 1 standard error。 | 以真 signal 和 ESD oracle 调 component count；gradient flow 以 discrete-time gradient descent 近似。step size、seed、code、hardware 未报告。|
| Appendix B 图 3：fixed-design linear | `n=300,p=400,σ₀²=1`；baseline `X₀` 随机生成后固定；两种 spectrum/signal decay；非正交 `A(α)` 逐步制造错配。 | 比 `d†(α)` 与 `nR*(α)/σ₀²`；20 replications，SE error bars。 | 响应有 random noise，但设计 hold fixed；没有外部 baseline 或 hypothesis test。|
| Appendix C 图 4：RKHS | cosine basis、`x∼Unif[0,1]`、`n=400,J=800,σ₀²=1`，`λ_{j,0}=j^{-1.1}`、`θ_j*=j^{-4}`，首 `D=80` coordinates 按 `α` 扰动。 | empirical oracle-KPCPE risk 与 ESD lower/upper bound；`B=10` replications，SE error bars。 | `‖f*‖∞` 用 dense grid 数值估计；grid density 和 seed 未报告。|
| Appendix D 图 5：deep linear | random-design linear，`p=900,n=1000`，`β_j*=j^{-1.1}` (`j≤200`)，`σ₀=0.1`；4 hidden affine layers、near-identity init、full-batch Adam、learning rate `10^{-4}`。 | 同一轨迹上画 pathwise ESD 与 `‖A(t)^⊤w(t)−β*‖²`。 | 无 replication/error bar、无真实 neural benchmark；这是 evolving-eigenfunction theorem 的 illustrative evidence。|

控制逻辑是改变一个 alignment lever（`q` 或 `α`）或 depth `D`，保持 signal/noise/ambient settings 的其余部分固定。没有数据泄漏讨论，因为所有主要实验都是合成构造；也没有预定义 failure threshold。图 1 的 `q=1` 曲线几乎不变被正文明确解释为初始 alignment 已好、没有改进空间，而非被隐藏的负例。[PDF p.7, §6, “there is no room for improvement”, explicit]

## 7. 结果、统计与可视化

### 7.1 图、表、算法清单

| 对象 | 模块 / 页 | 编码和任务 | 不确定性 |
|---|---|---|---|
| Figure 1 | results / p.8 | 2×2 log-scale profile panels；颜色为 training time，面板为 `q`；任务是显示 learned spectrum 对 span profile 的变化。 | 未给 error bar 或重复数。|
| Figure 2 | results / p.8 | 两张 line plot：oracle PC squared error 与 ESD 对 training time，颜色为 `D=0,1,3`。 | 20 MC averages；每条 error bar 为 1 SE。|
| Figure 3 | appendix / p.19 | 两个 spectrum/signal case 下 ESD（solid）与 rescaled oracle PCR risk（dashed）对 `α`。 | 20 repetitions；SE error bars。|
| Figure 4 | appendix / p.25 | lower bound、upper bound 与 oracle KPCPE risk 对 `α`。 | 10 repetitions；risk error bars 为 1 SE。|
| Figure 5 | appendix / p.27 | pathwise ESD 和 risk 对 epoch 的双 y-axis trajectory。 | repetition/interval 未报告。|
| Tables / Algorithms | all pages | `not_present`。 | 无表格、无 pseudocode。|

### 7.2 主要结果与统计处理

1. **ESD class 的 minimax difficulty**：Theorem 3.3 给出 `Θ(Kσ²)`；证据是固定-cutoff PC 的 bias/variance upper bound 与 Assouad hypercube lower bound。它是渐近/常数级理论结果，不含 seed aggregation 或 hypothesis test。[PDF pp.3–4, Thm. 3.3; pp.28–30, E.2, explicit]
2. **quota-sequence rate**：Theorem 4.3 在 Condition 4.1 下给 `σ₀²K_n/n`；主要不利解释是该结果依赖 class quota 和条件，论文在 definition 后明确 `K` 是 model-class descriptor，不是 distribution parameter。[PDF pp.5–6, §4, “K is a model-class descriptor”, explicit]
3. **OP-GF ESD reduction**：Theorem 5.2 是 conditional high-probability endpoint statement；它没有宣称所有 learned kernels 都会改善。Appendix G 的 ordering/top-set proof 处理这一定理的机制证据。[PDF pp.6–7, Thm. 5.2; p.48, G.2.4, explicit]
4. **图 1**：`q>1` 时随 `t` 增大，profile 向下；`q=1` 近乎恒定。比较对象是同一 synthetic signal 的 different `q` 和 time，未做显著性检验。[PDF p.7, §6; p.8, Fig. 1, explicit]
5. **图 2**：平均 ESD 和 squared error 总体下降；`D=0` 初期下降较早，充分训练后 `D=1/3` 可达到更低 ESD。该结论的分母是 20 Monte Carlo repetitions；作者没有给 p-value、多重比较、bootstrap、回归或置信区间。[PDF pp.8–9, Fig. 2 and §6, explicit]
6. **图 3 与图 4**：两类 controlled transformations 中，ESD 与 oracle risk 跟踪，图 4 的 empirical risk 位于 theoretical lower/upper curves 之间。它们检验的是 oracle spectral estimator 的 relation，不是 learned method 相对多个 baseline 的泛化排名。[PDF pp.18–19, Fig. 3; pp.24–25, Fig. 4, explicit]
7. **图 5**：深线性网络轨迹中 pathwise ESD 与 risk 一并下降；作者将其表述为 support for tracking alignment with evolving eigenfunctions，general theorem 留作 future work。[PDF pp.26–27, D.2, “supports the use of ESD”, explicit]

统计表达仅包括 Monte Carlo mean、standard error 和理论 risk bounds。图注能独立交代 Figure 1 的固定参数、Figure 2 的 20 repetitions/SE、Figure 3 的 20 repetitions/SE、Figure 4 的 10 repetitions/SE；Figure 5 缺少相同层级的独立统计说明。显著性、实质意义与机制证据没有被混为一个统计检验：机制主要由 theorem/controlled trajectory 提供，实证只作 illustration。

## 8. 消融、负面信息与自我设限

### 8.1 Ablation 状态

没有组件删除、替代模块、hyperparameter sweep 表或 formal ablation section。`q`、`α` 和 `D` 的变化是 **alignment/depth sensitivity illustrations**，不能写成 component-removal ablation。它们占主文图表 2/2，并在 Appendix B–D 扩展为模型/谱设置的 robustness-style checks。[PDF pp.7–9, §6; pp.18–27, Appendices B–D, layout_observation]

### 8.2 明示边界

| 限定类型 | 位置与证据 | 作用 |
|---|---|---|
| assumption / scope | p.4, §3.1, “population quantity for theoretical analysis” | ESD 不作为训练算法输入。|
| generality | p.6, §5, “fixed eigenbasis”; p.26, D.2 | OP-GF theorem 只处理 eigenvalue learning；evolving eigenfunctions 只定义 pathwise ESD。|
| generality | p.6, §5, “left for future work” | 不声称 general theorem 覆盖 evolving eigenfunctions。|
| assumption | pp.7, 39–48, Thm. 5.2 / Appendix G | strong/weak dichotomy、separation、top-block conditions 是 theorem 的必要前提。|
| data / metric | pp.18, 21–23, Appendix C | RKHS development 使用 bounded target、regular kernel，并先假设 `f*∈S_k`；超出 span 时加入 irreducible approximation error。|
| implementation | p.18, Appendix C, “do not analyze ... empirical eigenvalues” | 不分析 empirical eigenvalue/eigenfunction 的统计估计。|
| compute / scope | p.9, §6 | deeper models 的观察只提供 perspective；“comprehensive study ... future research”。|
| baseline | pp.69–73, Appendix I | ridge discussion 仅针对 specified small-regularization regime。|

作者对不利信息的可验证呈现方式有两类：第一，`q=1` 的无改善作为 Figure 1 的一个 panel 被直接解释；第二，evolving-eigenfunction theorem、empirical eigensystem、完整 depth study 等边界被明确迁移到 future work 或 appendices。没有证据支持“弱基线”“选择分母”“代表性案例”等意图性判断，故这些策略记为 `not_present`，不作推断。[PDF pp.7, 9, 18, 26, explicit]

## 9. 结论、limitations 与主张闭环

§7 不引入新数字或新 theorem；它重新陈述 ESD/span profile、population descriptor、adaptive kernel 使同一 signal 进入更容易 ESD class 的解释，并重复 fixed-eigenbasis 与 evolving-eigenfunction 的范围边界。[PDF p.9, §7, “establish this mechanism rigorously only for fixed-eigenbasis”, explicit]

| 引言主张 | 方法回应 | 理论/证据回应 | 状态 |
|---|---|---|---|
| ESD 可量化 signal–spectrum alignment，避免 source/eigen-decay 的先验 | Definition 3.1、span profile | Thm. 3.3、Examples 3.4–3.5、Appendix A/D | closed |
| ESD 给 sequence model 的 sharp minimax rate | ESD-bounded class 与 PC cutoff | Thm. 3.3；E.2 的 Assouad lower bound | closed |
| 框架可扩展至 linear 与 RKHS | whitening/SVD、KPCPE | B.3/B.4；C.2/C.7/C.8；F proofs | closed within stated assumptions |
| OP-GF 的 adaptive eigenvalue learning 可降低 ESD | Equation (12)、strong/weak/order mechanism | Thm. 5.2 与 Appendix G；图 1–2 illustration | partially_closed：只在 fixed eigenbasis 和列出的条件下 |
| ESD 解释 feature learning 的一般 generalization benefit | pathwise ESD formulation | deep linear Figure 5；general theorem 留 future work | partially_closed |
| ESD 比 ridge-guided index 更适合 intrinsic complexity | Appendix I 的 ridge saturation construction | Thm. I.6、Example I.7 | closed within small-regularization regime |

**单一主线**：学习过程改变 kernel 的谱排序；若这一变化把 signal energy 推向 leading eigencoordinates，则 tail-bias/variance crossing 所定义的 ESD 下降，同一 target 隶属更小的 minimax class，因而 oracle spectral estimation 的可达风险下降。主文保留了这个定义、三条主 theorem、OP-GF mechanism、两张主结果图和 discussion；证明、cross-model assumptions、更多 numerical validation 与 ridge counterexample 被移入附录。正文可自足地陈述主链，但 RKHS 与 OP-GF 的严格条件需读取附录才能完整评估。

## 10. 附录职责与正文调用

| 一级模块 | 页码 | 类别 | 正文调用与依赖 |
|---|---:|---|---|
| A. Related Work | 13–15 | other | p.2 “Detailed comparisons ... Appendix A”；支撑 novelty boundary。|
| B. Correlated Noise and Fixed-Design Linear Model | 15–18 | extended_method | p.3 指向 Appendix B；linear extension 和 Figure 3 依赖它。|
| C. RKHS Regression | 18–25 | extended_method / proof | p.2、p.5 指向 Appendix C；RKHS claim 的 boundedness/regularity 条件和 Figure 4 在此。|
| D. Measuring Alignment via ESD | 25–27 | additional_result | p.4 指向 D.1，p.6 指向 D.2；sparse counterexample 与 pathwise deep-linear illustration。|
| E. Proof | 27–34 | proof | 为 Props. 3.2、Thms. 3.3/4.3 与例子补足证明。|
| F. Proofs for Appendix C | 34–36 | proof | 为 C.4、C.7、C.8 补足 proof。|
| G. OP-GF proofs | 36–64 | proof | 为 Thm. 5.2 提供 concentration、ODE、ordering、exchange 链。|
| H. Application of Theorem 5.2 | 64–69 | robustness | 将 theorem conditions 在 concrete misalignment profile 上逐项可检查化。|
| I. Ridge saturation | 69–73 | other | 解释 §3.1 中为何不以 estimator-guided ridge index 代替 ESD。|

附录没有代码、hyperparameter table、hardware inventory、real-data protocol 或 standalone supplementary；这些内容在已读 PDF 中均为 `not_present`。附录最重的职责是 proof，不是把关键定义藏起来；同时，RKHS/OP-GF claims 的适用条件确实依赖附录才能完整成立。

## 11. 用词、修辞与可迁移规则

从直接 PDF 文本做的辅助计数显示：主文中 `ESD` 约 69 次、`alignment` 约 22 次、`kernel` 约 50 次、`minimax` 约 23 次；这些是领域词和主论证动作，而非模板性 filler。二元/三元高频概念组包括 `effective span dimension`、`signal-kernel alignment`、`minimax risk`、`span profile`、`learned eigenvalues`、`oracle-tuned PC estimator`。连字符断词（如 `over-parameterized`、`fixed-kernel`）和数学 token 会使统一 tokenization 有误切分风险；汇总器的原始 token 计数应覆盖这里的辅助计数。

主文中 `we show` 与 `we find` 均为 0；`we demonstrate` 1 次、`we propose` 2 次、`we observe` 2 次、`we prove` 2 次、`we introduce` 1 次、`we establish` 1 次。`we prove` 集中在 abstract/intro 的 theorem promise，`we observe` 集中在第 7、9 页的 Figure 1–2 解释；证明附录额外出现 `we show` 3 次与 `we prove` 5 次。强主张由 `prove`、`sharp`、`minimax optimal` 支撑；弱主张使用 `suggests`、`supports`、`expect`、`perspective`，尤其放在 deep-linear 和 future-work 边界。

- 最有效模式：先定义能落到一个明确 bias–variance crossing 的 population object，再用同一 object 串起 oracle estimator、minimax class、adaptive dynamics 和最小的 controlled numerical illustrations。
- 最大读者成本：OP-GF theorem 的 conditions 与 29 页技术证明很重，且主文两个实验均是合成/oracle setting。
- 可迁移规则：让每个“alignment improves generalization”的叙述同时给出可计算的排序/尾能量对象、该对象如何进入 decision-relevant risk，以及一个能失败的边界情形。
- 适用边界：当 empirical representation、data-dependent eigensystem 或非谱型 estimator 是主对象时，必须另外证明或测量这些对象，不能把 population ESD 直接当作完成的泛化解释。

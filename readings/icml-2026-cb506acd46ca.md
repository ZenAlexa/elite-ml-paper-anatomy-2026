# DiScoFormer：单篇深读备忘

- **paper_id**：`icml-2026-cb506acd46ca`
- *DiScoFormer: Plug-In Density and Score Estimation with Transformers*
- **版本边界**：已逐页读取 `corpus/preprints/icml-2026-cb506acd46ca.pdf`（arXiv v4，物理页 1–21）及其同版本提取文本。来源是 `verified_preprint`；没有单独 supplementary 文件，PDF 的 pp. 14–21 是同一文件内的附录。
- **证据标记**：`[E]` 为作者明示，`[L]` 为版面观察，`[I]` 为基于已列证据的解释。

## 结论先行

论文的单一主线是：把密度与 score 的一次性估计改写为「样本集合到函数值」的 Transformer operator；用 whitening 处理仿射变换，用 squared-norm lift 证明一个残差 cross-attention block 能精确表达 Gaussian KDE 的 score 与 log-density，随后用合成 GMM 训练的模型证明它在若干合成分布、不同样本数与高维条件下优于所列 KDE 基线，并可作为 score-debiased KDE、Fisher information、entropy 与 Landau 方程粒子法的 plug-in oracle。[E, pp. 1–2, §1；p. 4, §3.2；pp. 6–9, §4]

这条链条的强处在于结构性 bridge 超出类比。Proposition 3.5 给出需要的 lift、attention 条件和读出量，附录逐步构造 projection；实验中的 whitening 消融也与该结构动机对应。[E, p. 4, §3.2；pp. 15–16, Proposition A.3；p. 7, §4.3] 边界同样明确。经验训练只覆盖至多 10-mode GMM，rotation 只靠 augmentation 近似处理，且没有一致性／渐近保证。Theorem B.2 以 boundedness 与 (O(1/N)) stability 为前提给出外推风险界；softmax 本身不会自动带来该性质。[E, pp. 8–10, Limitations；p. 17, §B.2]

## A. 文档边界、页级地图与版面

| 物理页 | 内容与语义模块 | 证据 / 版面观察 |
|---|---|---|
| 1 | 标题、Abstract、Introduction 起始 | 双栏；abstract 位于左栏上半，introduction 跨两栏续写。[L, p. 1]
| 2 | Introduction 收束、Related Work 主体 | 四项 contribution list 后立即转入独立 Related Work 节。[E, p. 2, §§1–2]
| 3 | Related Work 收束、Methodology / 3.1 | 左上为 Table 1，右上为 Figure 1，正文在其周围流动。[L, p. 3]
| 4 | 3.1 续、3.2 Attention and KDE | Figure 2 为左栏上方的代码式 forward pass；右栏由命题与推导占主导。[L, p. 4]
| 5 | 3.3–3.5、Experiments 设计开头 | Algorithm 1 置于左栏上方；方法叙述与实验问题在同页相接。[L, p. 5]
| 6–8 | §4 的主结果、设计细节、ablation、applications、结论开头 | 双栏；p. 6–7 把表、图和正文交错排入两栏。[L, pp. 6–8]
| 9 | Figures 7–11 | 几乎整页为五个结果图，正文没有新增段落。[L, p. 9]
| 10 | Limitations 续、Acknowledgments、Impact Statement | 内容只占页面上半，较大空白未用于新增结果。[L, p. 10]
| 11–13 | References | 三个物理页；p. 13 仅左栏有少量尾部参考文献。[L, pp. 11–13]
| 14–17 | Appendix A proofs，Appendix B 起始 | 单篇附录仍为双栏，数学推导密集。[L, pp. 14–17]
| 18–19 | Appendix B 续、Appendix C attention visualization | p. 18–19 的 Figure 12–13 占大面积。[L, pp. 18–19]
| 20–21 | Appendix D score-matching comparison、Appendix E runtime | p. 20 的 Figure 14 与文字说明并置；p. 21 的 Figure 15 后有简短 runtime 解释。[L, pp. 20–21]

- PDF 共 21 页。主文为 pp. 1–10（10 页），References 为 pp. 11–13（3 页），Appendix 为 pp. 14–21（8 页）。主文在 Impact Statement 后结束；附录从 p. 14 的 `A. Proofs` 开始。[E/L, pp. 10–14]
- 全文使用 letter 双栏版式。跨栏或占大片面积的视觉对象集中在 Figure 7–15；p. 9、p. 18–21 的可读面积主要交给图，连续论证面积相应较少。[L, pp. 9, 18–21]
- 估计主文连续散文约 5,050 词（不把公式行、图表数值和 references 当作散文）；模块可重叠，因为 `theory` 嵌入 Methodology，`ablation` 嵌入 Results。Introduction 约 810 词、Related Work 约 840、方法叙述约 1,160、实验设计约 430、结果约 1,050、结论约 170、limitations 约 120。[I，按页级版面与可见段落估计]

## B. 摘要的句级功能

| # | 功能 | 承接与限定 | 证据 |
|---|---|---|---|
| 1 | `object_scope` | 以 density/score estimation 的应用范围设定对象。 | [E, p. 1, Abstract, “core problem”]
| 2 | `problem_gap` | 用「Existing methods are bifurcated」构造 KDE 泛化性与 score matching 精度／重训之间的张力。 | [E, p. 1, Abstract, “suffer from the curse”]
| 3 | `core_idea`、`method` | 引入 equivariant Transformer，并明确两个输出。 | [E, p. 1, Abstract, “maps i.i.d. samples”]
| 4 | `method`、`impact_claim` | 与单分布固定函数对照，主张跨 distribution 和 sample size 而无需 retraining。 | [E, p. 1, Abstract, “without retraining”]
| 5 | `theory`、`qualitative_result` | 先是可证明的 normalized KDE recovery，后是 attention-head 的经验模式。 | [E, p. 1, Abstract, “recover normalized KDE”]
| 6 | `qualitative_result`、`impact_claim` | 以 KDE superiority 和三类下游用途收束。没有报告具体数值。 | [E, p. 1, Abstract, “plug-in score oracle”]

功能顺序为 **对象 → 现有缺口 → 方法 → 可复用范围 → 理论与机制证据 → 结果与用途**。摘要没有量化结果、实验设置、显式 limitation 或不确定性陈述；最强的可检验主张放在最后两句的 KDE recovery、outperform 与下游用途上。[E, p. 1, Abstract]

## C. Introduction 的论证推进

| 段落 | 主动作 | 上一段遗留问题 → 当前回答 → 下一钩子 |
|---|---|---|
| 1 | `context` | 密度／score 是基础推断对象 → 说明应用范围 → 为什么现有工具不够。 [E, p. 1, §1, “foundational problem”] |
| 2 | `failure_of_prior_work` | KDE 与神经 score model 各有长处 → 标出 curse of dimensionality 与 per-target retraining → 需要通用 estimator。 [E, p. 1, §1, “precluding … off-the-shelf”] |
| 3 | `core_idea` | 需要一个通用 estimator → 定义从样本到 log-density / score 的 operator → 该 operator 应满足什么对称性。 [E, p. 1, §1, “sequence-to-operator”] |
| 4 | `missing_insight` | operator 的输入是无序、可仿射变换的样本 → 写出 permutation 与 affine equivariance 身份 → 需要架构实现。 [E, p. 1, §1, “critical requirement”] |
| 5 | `method_preview` | 需要满足对称性的架构 → 无 positional encoding 的 Transformer、whitening、rotation augmentation、cross-attention → 为什么不是黑箱。 [E, p. 1, §1, “specialized whitening mechanism”] |
| 6 | `theory_preview` | 需要结构上贴合 KDE 的理由 → attention 能 recover normalized KDE weights → 转向经验验证。 [E, pp. 1–2, §1, “theoretical bridge”] |
| 7 | `result_preview` | 理论 bridge 仍需实证效用 → 预告 ID/OOD、(n,d) scaling 与下游 plugin → 总结贡献。 [E, p. 2, §1, “outperforms KDE and score-debiased KDE”] |
| 8 | `contribution_list` | 前述叙事被压缩为四项贡献 → 方法、KDE bridge、精度、applications → 引至 Related Work。 [E, p. 2, §1, “In summary, our contributions”] |

按估计词数，`context` 约 9%、`failure_of_prior_work` 约 16%、`core_idea` 与 `missing_insight` 合计约 28%、`method_preview` 与 `theory_preview` 合计约 24%、`result_preview` 约 13%、contribution list 约 10%。四项 contribution 基本重述摘要末尾的同一组方法、理论、性能和用途；它们包含可被数据或构造反驳的主张，但不在引言中给出数字或限制。 [I/E, pp. 1–2, §1]

## D. Related Work 的定位方式

Related Work 是独立 §2，位于 Introduction 后、Methodology 前，跨 pp. 2–3，约占主文散文的六分之一。它有七个主题簇：KDE、其他 nonparametric estimator、score matching / diffusion、set/equivariant architecture、attention-as-kernel smoothing、neural operator、particle/Fokker–Planck solver。[E, pp. 2–3, §2]

- **分类而非编年**：每段都按问题或方法族命名；没有按年份的串联叙述。[E, p. 2, §2]
- **最近邻对照**：KDE 段将 SD-KDE 的 score oracle 缺口接到本文；attention 段把 Proposition 3.3 定位为任意 query 的 exact normalized Gaussian weights；neural-operator 段以 raw i.i.d. samples 而非 RKHS embedding 区分 Score Neural Operator。[E, p. 2, §2, “missing oracle”；“exactly reproduce”；p. 3, §2, “raw i.i.d. samples”]
- **引用的后续作用**：Epstein et al. 在 §4.5 作为 Emp-SD-KDE baseline 再出现；Scott 在 §4.1、Appendix E 作为 KDE choice；score matching 文献在 Appendix D 承接。因此它不是只在 §2 列出引用。[E, pp. 6, 8, 20]
- **避免重复方法介绍的手段**：§2 只给比较维度和差异，whitening、lift、cross-attention 的构造保留在 §3；但 Related Work 自身没有对每个近邻给出统一表格式比较。[I/E, pp. 2–4]

## E. 方法、理论与实现链

### 形式对象与组件

| 组件 | 首次位置 | 解决的前文问题 |
|---|---|---|
| 输入 (X)、query (Y)，输出 (T(X,Y)) 与 (S(X,Y)) | p. 1 的 operator 定义；p. 5 的 cross-attention variant | 将每个 target distribution 的单独训练改写为样本条件化估计。 [E, pp. 1, 5]
| permutation / affine equivariance | p. 1 的两个变换身份；Proposition 3.1 | 保证 sample index 置换与坐标变换的正确输出变换。 [E, pp. 1, 3]
| centering、regularized scatter、inverse-square-root whitening | Figure 2 与 §3.1 | 把一般仿射变换约化为 residual orthogonal transform。 [E, p. 4, §3.1]
| random orientation augmentation | §3.1 | 只近似处理 residual rotation/reflection，而非把它宣称为严格 architecture symmetry。 [E, p. 4, Remark 3.2]
| cross-attention、共享 backbone、density/score heads | §§3.2、3.5 | 允许任意 query；把两个耦合量放在同一 backbone，并提供 TTT consistency loss。 [E, pp. 4–5]
| squared-norm lift 与 attention log-normalizer | Proposition 3.5 | 移除 ordinary attention 到 exact Gaussian KDE 的 key-side quadratic obstruction，并保留 density normalizer。 [E, pp. 4, 15–17]
| on-the-fly GMM DataLoader 与加权 loss | §3.4、Algorithm 1 | 为两个输出提供闭式标签；训练时联合最小化 log-density 和 score MSE。 [E, p. 5]

方法动作序列可概括为：`state_problem → setup_notation → define_component → explain_mechanism → derive → state guarantee → instantiate_algorithm → connect_to_experiment`。其中 §3.3 以 Figure 1 从正式 KDE bridge 转向经验 head specialization，§3.5 从 arbitrary-query variant 转向 TTT 的可测试预测。[I/E, pp. 3–5]

### 理论清单与计数

- 主文有 3 个 Proposition（3.1、3.3、3.5）和 2 个 Corollary（3.4、3.6），没有 Lemma 或 Theorem。附录新增 Proposition B.1 与 Theorem B.2；Appendix A 的 A.1–A.3 是 3.1、3.3、3.5 的 restatement/proofs，不应被重复计成新主张。[E, pp. 3–4, 14–18]
- 以一个完整独立数学块为单位，目视计得全文约 **54 个 displayed formula blocks**，其中主文约 17、附录约 37；没有带圆括号编号的 equation tag。多行 aligned expression 只计一个块，行内符号不计入这个数字。[L, pp. 1–21]
- 核心因果链是 Proposition 3.1（目标的变换律）→ whitening/augmentation（实际架构近似达成）→ Proposition 3.3 / 3.5 / Corollary 3.6（attention 能表达 KDE）→ GMM training 与实验。B.1 是 adaptive bandwidth 的解释，B.2 是有条件的 OOD risk guarantee；后两者不是训练模型自动具备的保证。[E, pp. 3–5, 17–18]
- A.3 的 key condition 是 fixed squared-norm lift、exact softmax、无 positional encoding / normalization / FFN 的单头 residual cross-attention，以及可读出的 per-query log-normalizer；因此它是 expressivity construction，不是对训练后 4-layer model 参数的证明。[E, pp. 4, 15–17]

### 算法、复杂度和解释粒度

Algorithm 1 的输入为 batch size、dimension、context/query sample sizes 与 component range。它在每个 batch 抽取 component 数、两个随机 GMM、context (X) 和 query (Y)，输出 (X,Y,log f_X(Y),\nabla\log f_X(Y))，直到训练停止。循环层级是 outer training repeat 与 batch 内逐样本循环；它只生成标签，不构成 Transformer inference algorithm。[E, p. 5, Algorithm 1]

复杂度只在两个位置明确：whitening 的 residual orthogonal处理写为 (O(d))；Appendix E 说明 KDE 与 attention 都有 (O(n^2)) pairwise cost。没有给出训练总预算、FLOPs 或各组件的统一复杂度分解。[E, p. 4, §3.1；pp. 20–21, §E]

## F. 实验设计与复现边界

### 预列问题与对齐

§4 先列四个问题：accuracy against KDE/SD-KDE、(n,d) scaling、OOD generalization、以及 SD-KDE / entropy / Fisher / Fokker–Planck 的 plugin 用途。随后章节顺序为 score、high-dimensional、whitening ablation、relative Fisher、density、entropy/Fisher、plasma；大致回应了引言贡献，但 relative Fisher 只有 estimator construction/visualization，主文没有独立数值表。[E, pp. 5, 6–9]

### 已报告的设计事实

| 项目 | 论文给出的粒度 |
|---|---|
| 训练族 | 在线生成 GMM；通常为 1–10 modes，means in ([-3,3]^d)，diagonal covariances in ([0.2,1]^d)。 [E, p. 6, §4]
| 默认模型 | 4 encoder layers、hidden size 128、8 heads、GELU、pre-normalization、无 positional encodings、约 800k parameters。 [E, p. 6, §4]
| 默认运行 | batch 32、(n=2048)、dropout 0.1、单张 48GB L40S。 [E, p. 6, §4]
| 大 (n) / (d=100) variant | (d_{model}=256)、8 heads、6 layers、score-only；d=2/10 与 d=100 的相关说明给出 150,000 steps。 [E, pp. 6–7, §§4.1–4.2]
| 测试对象 | 2D Gaussian、3-mode GMM、1–19-mode GMM、2D Laplace、2D Student-(t) ((\nu=3))、d=100 2-component diagonal GMM、1D 3-mode GMM、d=10 Gaussian、homogeneous Landau equation。 [E, pp. 6–9]
| baseline | Scott KDE、oracle-(h) KDE、Emp-SD-KDE、不同 score-driven SD-KDE、sliced score matching（Appendix D），以及文献中的 SBTM 质量参照。 [E, pp. 5–9, 20]
| 指标 | score/log-density MSE、relative score MSE（zero predictor=100%）、entropy / Fisher MSE、covariance trajectory、wall-clock runtime 与 OOM。 [E, pp. 6–9, 20–21]

训练随机种子、重复次数（Table 1 之外）、optimizer、learning rate、loss weight (alpha)、训练停止条件、代码 URL 与完整 hyperparameter sweep 没有在 PDF 中给出。Table 1 是唯一明确「averaged over 50 trials」的量化表；其他主表和曲线未标明 seed-level aggregation、dispersion、interval 或 hypothesis test。[E, p. 3, Table 1；pp. 5–7, §4；L, pp. 6–9]

训练与测试的 synthetic distribution 参数族在文字中部分区分，Algorithm 1 也令 context 和 query 来自分别抽取的随机 GMM；但 PDF 没有给出随机种子或数据生成器版本，因此独立复现还需要作者未写入 PDF 的实现选择。[E, p. 5, Algorithm 1；I]

## G. 结果、统计和可视化

### 主要结果

| 主张 | 证据对象与数值 | 比较及统计处理 | 可能的替代解释 / 作者处理 |
|---|---|---|---|
| whitening 实现近似 full-affine behavior | Table 1：permutation、translation、isotropic/anisotropic scaling 为 0；rotation (5\times10^{-4})，full affine (1\times10^{-4})，50 trials 均值。 | 相对 MSE；无离散量。 | 这只是在所测 transform/sample 上的经验误差；作者在 Remark 3.2 明说 residual rotation 是近似而非严格保证。 [E, pp. 3–4]
| score estimation 优于 Scott KDE | Figure 3 的 2D Gaussian quiver；Figure 4 的 1D/10D MSE 曲线。 | 视觉和 MSE；图中无误差表达。 | 图是合成、KDE-favorable example；正文通过 d=1/10 curve 扩大范围，但无多-seed report。 [E/L, p. 6]
| 大样本外推仍低于 KDE | Table 2：d=2 在 (2^8) 为 14.67 vs 43.8、(2^{14}) 为 6.80 vs 17.2；d=10 为 7.49 vs 65.6、2.83 vs 52.9；KDE 在 (>2^{14}) OOM，Transformer 至 (2^{17}) 为 5.41/2.74。 | 相对 score MSE，zero predictor=100%。 | OOM 是单张 L40S 与所用 KDE 实现的边界；Appendix E 也承认二者渐近均为 (O(n^2))。 [E, p. 6；pp. 20–21]
| OOD Laplace score 可改善 | Table 3：(n=512,1024,2048,4096) 的 Transformer MSE 为 0.3598、0.2992、0.2756、0.2597，均低于 KDE 0.3810、0.3305、0.2990、0.2650；Figure 5 显示 TTT 改善。 | MSE；无误差表达。 | 只是 2D Laplace；作者的 limitation 保留了远离 GMM targets 需 retrain/finetune 的边界。 [E, p. 7；p. 8]
| Student-(t) 上 TTT 可改善 | Table 4：例如 (n=256)，KDE 0.1206，No TTT 0.1119，TTT-6 0.0908；(n=128) TTT-8 0.1450 略优 KDE 0.1515。 | MSE，TTT steps 4/6/8。 | TTT 不在每个 (n) 单调，例 (n=512) 的 TTT-8 0.0514 高于 TTT-6 0.0485；作者没有声称单调。 [E, p. 7, Table 4]
| d=100 GMM 的 large gain | Table 5：DiScoFormer score MSE 0.167、log-density MSE 20.8；best KDE row 为 1.090、781。 | 单表 MSE；正文计算为 6.5×、37.5×。 | 只对 random 2-component diagonal-covariance GMM；没有非 GMM 的 d=100 对照。 [E, p. 7, §4.2]
| whitening 是 OOD scale 的因果组件 | Table 6：OOD score MSE 0.020（with）vs 1.136（without）；log-density 0.123 vs 1.593。 | 保持其余模型相同的 component deletion；MSE。 | ablation 在 d=1，不能独自证实更一般 rotation behavior；作者把结果限定为 scale/approximate affine claim。 [E, p. 7, §4.3]
| learned score 改善 density / plugin estimates | Figures 7–10：learned-score SD-KDE 的密度图更接近真值；Figure 9 给出 1D/2D MSE scaling；Figure 10 比较 entropy / Fisher MSE。 | 可视化和 MSE 曲线；无可读出表格数值或误差带。 | 中央结果的可精确复核依赖图形读数；PDF 不报告 curve 的分母或重复。 [E/L, pp. 8–9]
| pre-trained oracle 用于 Landau simulation | Figure 11 的 covariance trajectory：文字称 Transformer matches analytic covariance, KDE struggles。 | 轨迹图；与文献 SBTM 做质量对照。 | 只展示 covariance entry Σ1,1 与三个 collision setting；没有完整误差汇总。 [E/L, pp. 8–9]

统计上，MSE 的中心量、Table 1 的 50-trial average、relative-MSE 归一化和 OOM failure label 都是明确的；其余表未声明 aggregate unit，图表也没有显示 standard deviation、interval、significance test、effect-size protocol 或 multiple-comparison procedure。[E/L, pp. 3, 6–9, 21] 图注大多能辨识任务和比较对象，但不足以单独恢复 sample generation、seeds 或训练预算。[I/L]

### 视觉对象的叙事作用

- **机制与结构**：Figure 1 将 learned attention 和 normalized KDE heatmap/scatter 并列；Figure 2 把 whitening forward pass 压成可读的代码块。它们把「不是黑箱」的中段论证可视化。[E/L, pp. 3–4]
- **决策图**：Tables 2–6 给出能逐行核对的数值；Figures 3–5、7–11 则承担趋势与案例展示，p. 9 用图群把 density、entropy/Fisher 和 PDE 应用并置。[L, pp. 6–9]
- **附录补强**：Figures 12–13 延展 head specialization；Figure 14 承担 score matching comparison；Figure 15 将 runtime/OOM 的限定带入主张。[E/L, pp. 18–21]

## H. 消融、负面结果与自我设限

主文的显式 component ablation 是 §4.3 / Table 6，约占主文连续散文的 3–4%，只有一张表；识别对象是 whitening，条件是 d=1 的 ID/OOD scale meta-distributions。Table 4 的 TTT steps 可视作敏感性比较，但并未标为 ablation；Table 2 的 larger model 也不是 architecture-factorial ablation。[E, p. 7]

作者直接给出三项 limitation：仅 GMM training family、whitening 后 rotation equivariance 仍依赖 augmentation、没有 asymptotic guarantee。它们在 Conclusion 之后紧接出现并跨 pp. 8–10，未被移入附录。[E, pp. 8–10, Limitations]

运行时的边界也被明确写出。Transformer 在小 (n\leq2048) 时较慢，二者渐近均 (O(n^2))；KDE OOM 的观察只针对该实现与单张 GPU。[E, pp. 20–21, §E]

没有足够证据把图多表少、实验留在正文或 score-matching/runtimes 放入附录解释为刻意的叙事规避。可核验的版面事实是：main-text limitations 是主动正面讨论；Appendix D/E 在主文 p. 5–6 有明确调用，而非未说明的隐藏材料。[E/I, pp. 5–6, 8–10, 20–21]

## I. Conclusion、limitations 与闭环

结论只有一个段落，依次回收问题（density/score from samples）、方法（equivariant Transformer）、理论（squared-norm self-attention exact KDE construction）、机制图证据（multi-scale heads）、性能与四类用途；没有新增数字。随后 limitations 给出训练族、rotation 和 asymptotic 的边界；Impact Statement 讨论 generic downstream synthetic-media misuse，没有提出本文专有的 ethics claim。[E, pp. 8–10]

| 引言主张 | 方法 / 理论回应 | 实验回应 | 闭环状态 |
|---|---|---|---|
| one-shot universal density/score operator | (T,S) 定义、cross-attention、GMM DataLoader。 [E, pp. 1, 5] | GMM、Laplace、Student-(t) 和 (n) extrapolation。 [E, pp. 6–7] | `partially_closed`：实证族有限，正文也承认远离 GMM 时需 adaptation。 |
| symmetry-aware architecture | Proposition 3.1、whitening、Remark 3.2。 [E, pp. 3–4] | Table 1、Table 6。 [E, pp. 3, 7] | `partially_closed`：translation/scaling 与实测 full-affine error 有证据，rotation 是近似。 |
| attention 是 KDE 的 functional generalization | Propositions 3.3/3.5、Corollaries 3.4/3.6，Appendix A construction。 [E, pp. 4, 15–17] | Figure 1/12/13 的 attention patterns。 [E, pp. 3, 18–19] | `closed`：表达性构造与相应机制图均在文中。 |
| 优于 classical KDE | 训练目标与 baseline choices。 [E, pp. 5–6] | Tables 2–6、Figures 3–10。 [E, pp. 6–9] | `partially_closed`：在报告 synthetic settings 内有支持，未报告 seed uncertainty，且不是所有 density 的全面比较。 |
| plugin 下游用途 | cross-attention 与 score / log-density heads。 [E, pp. 5, 8] | SD-KDE、entropy/Fisher、Landau 图。 [E, pp. 8–9] | `partially_closed`：用途演示存在；relative Fisher 没有单独定量主结果，PDE 只展示一项 covariance。 |
| asymptotic or general universal guarantee | Appendix B.2 的条件性 risk bound。 [E, pp. 17–18] | 无直接 consistency experiment。 | `open`：作者明确说没有 proven asymptotic guarantees。 [E, p. 10] |

## J. Appendix 的职责

| 模块 | 页数 | 类型 | 主文调用与依赖 |
|---|---:|---|---|
| A. Proofs | 14–17 | `proof` | §3.1/§3.2 的 proofs 均指向 Appendix；精确 KDE construction 依赖 pp. 15–17。 [E, pp. 3–4, 14–17] |
| B.1 Whitening as Adaptive Bandwidth Selection | 17 | `extended_method` | 把 whitening 解释为 full bandwidth KDE；主文只给 architecture motivation。 [E, p. 17] |
| B.2 Generalization from GMM Training to Non-GMM Targets | 17–18 | `proof` | Limitations 引 Theorem B.2；它依赖 boundedness/stability/GMM-risk assumptions。 [E, pp. 8, 17–18] |
| C. Attention visualization | 18–19 | `qualitative_example` | §3.3 明确调用；给全 attention matrices 和 query-centric scatter。 [E, p. 5; pp. 18–19] |
| D. Comparison with the Score Matching Loss | 20 | `additional_result` | §4 开头说比较在 Appendix D；Figure 14 说明 retraining/under-overfit 对照。 [E, pp. 5, 20] |
| E. Runtime comparison | 20–21 | `additional_result` | p. 6 指向 Appendix E；给 runtime crossover、(O(n^2)) 与 OOM 限定。 [E, pp. 6, 20–21] |

附录约为主文页数的 0.8 倍。它放入关键 proofs、generalization assumptions、附加 visualization、score-matching comparison 和 runtime；正文保留问题、实际构造概述、核心 tables 与 applications。理论精确性和 GMM-to-non-GMM 的条件必须读附录才完整成立；但是主文已经把每个 proposition 的可观察结论、关键条件和实验用途写出，因而其主要叙事并不依赖只在附录出现的未命名机制。[I/E, pp. 3–5, 14–21]

PDF 未提供 source-code URL、optimizer/learning-rate schedule、完整 seed protocol 或独立 supplementary artifact；这些是复现细节的明显缺口，不是 Appendix 已补足的内容。[E/I, pp. 5–7, 14–21]

## K. 用词与修辞

术语密度由领域名词驱动：`density`、`score`、`KDE`、`Transformer`、`samples`、`distribution`、`attention`、`equivariance`、`GMM`。常见搭配包括 `density and score estimation`、`score estimation`、`kernel density estimation`、`affine equivariance`、`test-time training`、`plug-in score oracle` 与 `sample size`。这些用词主要服务问题、方法与实验对象；未见由模板化 slogan 驱动的高频语。[E, pp. 1–9]

按主文可见散文逐页检索，`we demonstrate` 1 次、`we propose` 1 次、`we introduce` 3 次、`we prove` 1 次，`we show/find/observe` 为 0 次；`outperforms`/`improve` 在摘要、结果和结论中承担性能主张，`exact` 在理论构造中承担条件化的强主张，`approximate` 出现在 rotation 边界处。[E, pp. 1, 4–8] 这使强主张集中在结构构造与受限实验结果，弱化词集中在 affine rotation 和 limitations，而非靠同义反复强化结论。[I/E, pp. 4, 8–10]

## L. 最终判断

1. **单一主线**：以 equivariant set-to-operator Transformer 作为 KDE-like density/score estimator，并把构造性 attention–KDE bridge、synthetic accuracy 和 plug-in use 串成一条链。
2. **正文保留的决策内容**：问题张力、对称性目标、whitening/cross-attention 的核心机制、KDE expressivity 结论、GMM training 与 architecture defaults、Tables 1–6、关键应用图、三个 limitation。
3. **迁往附录的细节及影响**：完整 proofs、B.2 assumptions、更多 attention views、score-matching 和 runtime 对照。主文可理解主张，但要审查 exact construction、generalization precondition 或 runtime 边界必须进入附录。
4. **最有效模式**：先给可构造 Proposition 3.5，再用 Figure 1 和 Table 6 分别检查 mechanism 与 symmetry-motivated component，最后把相同 oracle 投入 SD-KDE、information functional 和 PDE；这一顺序让理论、消融和应用指向同一对象。
5. **最大读者成本 / 未闭合处**：性能表缺少除 Table 1 外的重复、seed 和离散信息；高维与 OOD 只覆盖有限 synthetic families；无 asymptotic guarantee；若读者跳过 Appendix A/B，会遗漏关键条件。
6. **可迁移规则**：当论文的核心价值是「通用模型并非黑箱」时，主文应给出能映射到一个现有 estimator 的可构造机制，并用一个直接组件消融和一个下游任务检查该机制的实际价值。
7. **规则边界**：这条规则适用于可给出结构性对应的估计／operator 方法；若模型无法精确对应已知 estimator，应改用明确的预测、反事实或失败边界，不能把 attention heatmap 当作替代证明。

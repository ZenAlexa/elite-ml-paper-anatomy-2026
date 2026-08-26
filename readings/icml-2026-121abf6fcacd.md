# How Many Different Outputs Can a Transformer Generate?

## 书目信息与文档边界

- **论文**：Maxime Meyer、Mario Michelessa、Caroline Chaux、Vincent Y. F. Tan，ICML 2026 Oral / Spotlight。
- **实际读取版本**：`corpus/preprints/icml-2026-121abf6fcacd.pdf`，arXiv 2605.22223v2；来源 URL 为 `https://arxiv.org/pdf/2605.22223`。OpenReview forum 为 `https://openreview.net/forum?id=x4xOtzoYa6`。没有单独提供 supplementary 文件。
- **物理页边界**：30 页。主叙事为 p. 1–9；p. 10 上半部是 Impact Statement 与 Acknowledgements，参考文献从同页开始并延至 p. 13；Appendix 从 p. 14 的 `A. Transformer Layers` 开始，至 p. 30 结束。证据见 p. 10 的 `References` 与 p. 14 的 `A. Transformer Layers`。
- **版式**：正文、参考文献与附录均以双栏为主。Figure 2 和 Table 1 跨两栏占据 p. 7、p. 8 顶部；p. 27、p. 28 与 p. 30 几乎完全由多面板图构成。Figure 5 位于 p. 15 顶部后才恢复双栏文字。该安排将核心定理和主实验压缩在九页内，跨模型曲线、支持集收敛图与 cell-volume 分布主要移入附录。

| 区段 | PDF 页 | 语义模块 | 估算文字 | 版面与证据 |
|---|---:|---|---:|---|
| Abstract | 1 | abstract | 153 | 左栏上部；`We study how` |
| 1. Introduction 与 Remark 1.1 | 1–2 | introduction | 425 | 两栏连续，贡献列表位于 p. 1 右栏；`structural limitations` |
| 1.1. Related Works | 2 | related_work | 725 | 五个主题段落；`Approximation Theory` |
| 1.2. Notations | 2–3 | other | 65 | 紧接相关工作，跨到 p. 3；`Bold lowercase letters` |
| 2. The Transformer Architecture | 3 | method | 370 | 定义 hard/soft prompt 与 mean-field 表示；`Standard Transformers` |
| 3. Representing the Embedding Space | 4 | method | 490 | Figure 1 后定义 decoder cells 与 prompt regions；`Partitioning the Embedding Space` |
| 4. The Sequences that are Accessible | 5–6 | theory | 1,020 | 定义、假设、定理与两个推论；`Finite Prompt Length` |
| 5.1. The Cramming Task | 6–7 | experimental_design | 585 | 目标、优化目标与训练对象；`we freeze the model weights` |
| 5.2–5.4. Support、cell volume 与 copying | 8–9 | results | 845 | Table 1、Figures 3–4 与结果解释；`Copying-Length Generalization` |
| 6. Conclusion | 9 | conclusion | 145 | 两段闭环；`We established fundamental limits` |
| 7. Future Work | 9 | limitations | 170 | 未评估 Theorem 4.10 与 lower bounds；`leave an empirical evaluation` |
| Impact、Acknowledgements、References | 10–13 | other | 2,132 | p. 10 是混合页，参考文献完整覆盖 p. 10–13；`Acknowledgements` |
| Appendix A–H | 14–30 | appendix | 6,229 | 定义、证明、实现细节、附加结果与全页图；`Supplementary Experimental Results` |

`main_word_share` 以下按 p. 1–9 的主叙事分配，摘要计入该分母。p. 10 的 Impact / Acknowledgements 与 p. 10–13 的 references 保留在 `other`，不扩大主叙事分母。

| 模块 | 状态 | 估算文字 | 主叙事占比 | 图 | 表 | 算法 | display equations |
|---|---|---:|---:|---:|---:|---:|---:|
| abstract | observed | 160 | 3.2% | 0 | 0 | 0 | 0 |
| introduction | observed | 425 | 8.5% | 0 | 0 | 0 | 0 |
| related_work | observed | 725 | 14.5% | 0 | 0 | 0 | 0 |
| method | observed | 860 | 17.2% | 1 | 0 | 0 | 10 |
| theory | observed | 1,020 | 20.4% | 0 | 0 | 0 | 10 |
| experimental_design | observed | 585 | 11.7% | 0 | 0 | 0 | 2 |
| results | observed | 845 | 16.9% | 3 | 1 | 0 | 0 |
| ablation | not_applicable | 0 | 0.0% | 0 | 0 | 0 | 0 |
| conclusion | observed | 145 | 2.9% | 0 | 0 | 0 | 0 |
| limitations | observed | 170 | 3.4% | 0 | 0 | 0 | 0 |
| appendix | observed | 6,229 | — | 7 | 2 | 0 | 64 |
| other | observed | 250 | 1.3% | 0 | 0 | 0 | 0 |

## 摘要的逐句设计

| # | 词数 | 功能 | 限定、数字与承接 | 页码与证据 |
|---:|---:|---|---|---|
| 1 | 30 | object_scope, core_idea | 以 `only a handful` 限定输入信息；先给研究对象和预测任务。 | p. 1, Abstract，`closely predict the number` |
| 2 | 31 | theory, experimental_setup, quantitative_result | 给出 prompt-length upper bound；报告跨架构、跨大小的 `< 10` 因子。 | p. 1, Abstract，`tight up to a factor` |
| 3 | 23 | problem_gap, theory | 将 copying 与 cramming 的既有失败连接到理论解释。 | p. 1, Abstract，`theoretical explanation for previously observed` |
| 4 | 58 | theory, qualitative_result | 三项形式结论按线性长度、指数比例、斜率上界展开。 | p. 1, Abstract，`Formally, we prove that` |
| 5 | 11 | impact_claim | 用 unbounded context / computation 扩大结论的适用语境。 | p. 1, Abstract，`unbounded context and computation time` |

功能顺序为范围与核心任务、量化上界、问题意义、三项理论结果、外延主张。摘要报告了经验结果，唯一直接数值是「less than 10」；理论与经验紧密交错。摘要没有主动陈述假设条件、搜索失败风险或统计不确定性。有限 precision、支持集几何和 arbitrary-prompt 假设留到正文与附录。证据：p. 1, Abstract，`Notably, these results hold`；p. 5, Assumption 4.3；p. 6, Assumption 4.9。

## 引言的论证推进

| # | 动作 | 估算词数 | 上一段遗留问题、当前回答与下一钩子 | 页码与证据 |
|---:|---|---:|---|---|
| 1 | context | 55 | 先给 Transformer 的跨域成功，形成能力预期。下一段转向简单任务失败。 | p. 1, §1，`dominant architecture in modern deep learning` |
| 2 | problem | 54 | 指出 copying / repeating 随长度失败，并将现象归为潜在架构约束。下一段承诺刻画约束。 | p. 1, §1，`fail on surprisingly simple tasks` |
| 3 | core_idea | 24 | 把问题重述为所有 Transformer 的 structural limitations。后续三个 bullet 定义贡献。 | p. 1, §1，`identifying structural limitations` |
| 4 | contribution_list | 75 | 第一项给有限 accessible sequences 与 exact-copying 含义。下一项转到长度阈值。 | p. 1, §1，`only a finite set` |
| 5 | contribution_list | 67 | 第二项给固定 prompt 下的指数衰减与 abrupt failure。下一项给可计算阈值。 | p. 1, §1，`decays exponentially fast` |
| 6 | contribution_list | 57 | 第三项主张架构函数形式的公式贴近多模型观察。下一段说明分析对象。 | p. 1, §1，`explicit formula to predict` |
| 7 | method_preview | 76 | 用 finite precision 与 representation geometry 连接 accessible sequences、Section 4 与 Section 5。 | p. 1, §1，`constrain the set of sequences` |
| 8 | scope_boundary | 61 | Remark 1.1 将范围延到 bounded representations 的架构，同时将 Mamba 留给 future work。 | pp. 1–2, Remark 1.1，`leave this direction for future work` |

引言约 45% 用于三个贡献 bullet，约 20% 给背景与问题，余量交代机制、章节与外延。贡献列表与摘要重复同一条有限性、指数衰减和阈值预测主线，但引言添加了「任何 prompt、context length、inference strategy」的解释性边界。所有三项核心贡献均可证伪。给定模型和假设可反驳有限可达数、衰减率或上界拟合。引言未给数值结果，量化证据留在 Figure 2、Table 1 和 Figure 4。证据见 p. 1, §1 的 `Remarkably, this theoretical result` 与 pp. 7–9, §§5.1–5.4。

## 相关工作如何定位

相关工作嵌入引言的独立子节 `1.1. Related Works`，位于 p. 2，约占主叙事 14.5%。它按问题与理论工具分类，没有按年份叙述。五个引用簇均在后文被实际调用：Kuratov et al. 支撑 cramming protocol，Sander et al. 支撑 mean-field，Vershynin 支撑 packing number，Huang et al. 形成 copying 假设差异。

| # | 编码 | 比较维度与作用 | 页码与证据 |
|---:|---|---|---|
| 1 | taxonomy + nearest_neighbor_contrast | Approximation theory 的 universal approximation 与本文 finite numerical precision 的 capacity constraint 对照；Meyer et al. (2025) 提供 packing-number 策略。 | p. 2, §1.1，`finite numerical precision constrains` |
| 2 | nearest_neighbor_contrast + credit_or_foundation + gap_creation | Barbero、Jelassi 处理 copying；Kuratov 的 cramming 给 operational accessibility；本文声称首个 rigorous theoretical explanation。 | p. 2, §1.1，`operational definition of accessibility` |
| 3 | taxonomy + credit_or_foundation | Mean-field work 连接任意 prompt 长度与 probability measures。 | p. 2, §1.1，`mapping between probability measures` |
| 4 | taxonomy + connect_to_method | embedding anisotropy、probes、logit lens 汇入 decoder hyperplanes 与 next-token cells。 | p. 2, §1.1，`partition the embedding space` |
| 5 | taxonomy + nearest_neighbor_contrast + limitation_of_prior | formal-language expressivity 与 Huang et al. 的 copying impossibility 对照；本文主张移除理想化条件并量化。 | p. 2, §1.1，`removing those assumptions` |

相关工作避免重复方法的方式是把每簇收束到一个后文技术对象，而非复讲 attention。最邻近工作由 Kuratov et al. 的 cramming 和 Huang et al. 的 length generalization 共同承担；前者成为实验协议，后者构成理论差异。证据：p. 2, §1.1，`We describe this further in Section 5`；p. 6, §5.1，`cramming setup of Kuratov et al.`。

## 方法、形式化与理论链

方法链首先把 hard prompt 和更强的 soft prompt 都视为 Transformer 输入；随后将长度无关的 prompt 集合转为 empirical measures；最后用 decoder argmax cells、packing number 与 finite precision 将「可达」改写为可计数对象。Section 4 把固定 prompt 与 arbitrary prompt 分开，因此经验部分可逐一对应两套预测。

**段落动作序列**：`setup_notation → define_component → define_component → state_problem → define_component → derive → explain_mechanism → derive → connect_to_experiment`。

| 最小逻辑单元 | 前文问题 | 形式对象、输入与输出 | 页码与证据 |
|---|---|---|---|
| 标准与 soft-prompt Transformer | 把离散 prompt 和连续优化 prompt 放在同一上界内。 | 输入为 token sequence 或 `X ∈ R^{d×m}`，输出为 next-token simplex；soft 输入更强。 | p. 3, Definitions 2.3–2.4，`more expressive than its hard prompt` |
| Mean-field 表示 | 任意长度 prompt 需要长度无关空间。 | `M(X)` 是 prompt 的 empirical measure；输入顺序经 permutation equivariance 折叠。 | p. 3, §2.2，`independent of the ordering` |
| decoder-cell 划分 | 单步 next token 如何成为几何区域。 | `E_t` 由 unembedding `F` 的 argmax 定义；Figure 1 显示切面。 | p. 4, §3.1，`partition the embedding support` |
| prompt-region 划分 | 一个完整 token sequence 如何对应 prompt。 | `E_t^m` 是可使 greedy decoding 生成 `t` 的 soft prompt 集。 | p. 4, §3.2，`lead to the sequence t` |
| accessible sequence | 何时把一个 prompt region 当作可稳定访问。 | 需要存在含 `ε/2` ball 的 prompt，避免边界 argmax。 | p. 5, Definition 4.1，`B(X, ε/2) subset` |
| fixed-length packing bound | 固定 m 能区分多少输入。 | finite precision 下，packing number 上界可达序列数。 | p. 5, Theorem 4.6，`only access a finite number` |
| fixed-length threshold | 上界如何变成长度规律。 | Corollary 4.7 将 `m` 映射到线性阈值及指数比例衰减。 | p. 5, Corollary 4.7，`decays exponentially fast` |
| arbitrary-length bound | m 无界时是否仍有限。 | Assumption 4.9 将输入 partition 成 finite Wasserstein net；Theorem 4.10 给有限上界。 | p. 6, Assumption 4.9，`finite Wasserstein precision` |
| experimental connection | 理论要观察什么。 | Section 5 提取三项可测试预测：sharp transition、`n⋆(m)=Cm`、C 的上界。 | p. 6, §5，`three concrete predictions` |

主文有 22 个 display formula blocks，其中带编号的公式有四个，分别为 cramming loss (1)、greedy generation (2)、附录中 cell-volume convolution (3) 和 median criterion (4)。主链上的命题共有四个，分别为 Theorem 4.6、Corollary 4.7、Theorem 4.10、Corollary 4.11。Appendix 增补 15 个不同的 theorem / lemma / proposition / corollary。没有 pseudocode 或 Algorithm 环境。

| 理论对象 | 角色 | 假设、结论、证明与经验对应 | 页码与证据 |
|---|---|---|---|
| Theorem 4.6 | core_chain | Assumption 4.3 的 uniform finite precision 与 embedding radius `r` 下，固定 m 的 distinct accessible sequences 有 packing 上界。证明在正文，Cramming 的线性斜率是经验对应。 | p. 5, Theorem 4.6，`finite number of distinct sequences` |
| Corollary 4.7 | core_chain | 由 Theorem 4.6 与 `|V|^n` 得固定 m 的线性阈值和指数比例衰减。Figure 2 与 Table 1 对应。 | p. 5, Corollary 4.7，`decays exponentially fast with n` |
| Theorem 4.10 | guarantee | 假定 finite Wasserstein precision，任意 prompt length 的可达序列总数有限。Appendix D、E 讨论条件，Figure 4 是间接经验对应。 | p. 6, Theorem 4.10，`only access a finite number` |
| Corollary 4.11 | guarantee | 由 Theorem 4.10 给长度阈值及 `O(1/|V|^n)` 比例；正文明确把其 empirical evaluation 留到未来。 | pp. 6, 9, Corollary 4.11，`proportion of accessible token sequences` |
| Proposition C.2 | guarantee | 给 bounded `d`-ball 的 packing upper / lower bounds，支撑 Theorem 4.6。 | p. 16, Proposition C.2，`packing number of the sets` |
| Proposition C.3 | guarantee | 给 empirical-measure set `G` 的 Wasserstein packing bounds，支撑 Theorem 4.10。 | p. 16, Proposition C.3，`mean-field framework` |
| Lemmas C.4–C.7 | proof | generalized-ball volume、bounded-set packing、Wasserstein upper and lower bounds 构成 C.2/C.3 的证明材料。 | pp. 16–17, Lemma C.4，`volume of the d-dimensional ball` |
| Proposition D.3 | explanation | 将 equal-length empirical measures 的 Wasserstein distance 与 permutation-invariant vector distance 关联，用于说明 Assumption 4.9 的尺度直觉。 | p. 18, Proposition D.3，`relate Wasserstein distance` |
| Theorem E.3 与 Lemmas E.4、E.6 | guarantee | elementary-operation precision 与有限 input alphabet `D` 下，构造有限基以限制可达 sequences。 | pp. 19–20, Theorem E.3，`upper bound f(p,D)` |
| Proposition F.2 | guarantee | ball enclosure 给 Cramming slope 上界。 | p. 21, Proposition F.2，`slope of the Cramming Task` |
| Proposition F.3 与 Lemma F.4 | explanation | cone enclosure 的体积与 Cramming slope 公式。Figure 6 解释几何分解。 | pp. 21–22, Proposition F.3，`support is a cone` |
| Corollary F.5 | guarantee | 从 cone volume 得 packing number，回接 Equation 4。 | p. 23, Corollary F.5，`packing number of the cone` |
| Proposition F.6 | guarantee | axis-aligned ellipsoid / rectangle enclosure 给每坐标范围的 slope bound。 | p. 23, Proposition F.6，`support is an ellipsoid` |

Theorem 4.6 和 Corollary 4.7 构成论文的核心因果链。Theorem 4.10、E.3 与附录 D 主要提供 arbitrary-length 版本的保证。Appendix F 的几何公式承担经验上界的解释与校准功能。Figure 1 是方法图；Table 1 与 Figures 2–4 承担决策证据。

## 实验设计与可复现粒度

| 设计项 | 实际做法 | 页码与证据 |
|---|---|---|
| 研究问题 | 检验固定 m 的 sharp transition、`n⋆(m)=Cm` 与 C 上界；用 copying 间接展示 arbitrary-prompt saturation。 | p. 6, §5，`three concrete predictions` |
| Cramming intervention | 冻结 pretrained Transformer，仅优化 length-m soft prompt `Y`。 | p. 7, §5.1，`freeze the model weights` |
| 优化目标与判定 | teacher-forcing cross-entropy 后，greedy 生成 n tokens；exact match 才是 success。 | p. 7, Eqs. (1)–(2)，`count a success if` |
| 聚合单位 | 每个 `(n,m)` 对 20 个 target strings 取 mean success rate。 | p. 7, §5.1，`mean success rate over 20` |
| target 来源 | PG19 contiguous token spans；uniform i.i.d. random tokens from a vocabulary subset。 | p. 7, §5.1，`two target sources` |
| 模型覆盖 | Pythia 160M–2.8B，Qwen-2.5 0.5B/1.5B，Llama-3.2 1B/3B，Gemma-3 270M/1B。 | p. 7, §5.1，`several model families and sizes` |
| 几何支持估计 | Ball、cone、axis-aligned ellipsoid 的 support 参数，依赖随机 token prompt 与内部 embedding。 | p. 8, §5.2，`Monte Carlo using 10K prompts` |
| 详细优化资源 | Adam，3000 steps，learning rate 0.01，weight decay 0.01，2 NVIDIA H100 GPUs。 | p. 24, §G.3，`Adam optimizer for 3000 steps` |
| copying-length 测试 | 在长度至 50 的随机字符串上 fine-tune；100% exact match 或 10K steps 停止；测试更长未见字符串。 | p. 9, §5.4，`100% exact-match accuracy` |
| cell-volume 估计 | ellipsoid 内均匀采样，greedy decoder token 频率估计 volume；Appendix 写 N = 50M。 | p. 25, §H，`number of samples (here N = 50M)` |
| 随机种子、置信区间与多重比较 | not_present。主文和附录报告 20-target 均值、Monte Carlo N、sigmoid / linear fit，但没有报告 seeds、intervals、p-values、bootstrap 或 multiplicity correction。 | pp. 7–9, §§5.1–5.4，`fit a sigmoid` |
| 竞争基线 | not_present。比较轴是 target distribution、模型家族和几何 enclosure，而非与另一个训练方法的性能竞赛。 | pp. 7–9, §5，`support refinement` |

正文已给出目标函数、success criterion、target source、样本聚合和模型族。optimizer、GPU、precision、support sampling 与 cell-volume 的采样方案留在 Appendix G–H。论文提供代码链接，证据：p. 1, footnote，`Code is available`。

## 结果、统计与可视化

| 对象 | 模块与页 | 视觉编码和独立可读性 | 结果、统计处理与不利解释 |
|---|---|---|---|
| Figure 1 | method, p. 4 | 二维 plane cut，以颜色编码 decoder argmax token；红点是三种 prompt embedding。caption 说明几何与 token 标注。 | 仅作机制说明，未将二维切面当作定量结果。证据：`Plane cut of the embedding space`。 |
| Figure 2 | results, p. 7 | 上两图用 target length、accessibility 与 memory length；右图用 `n50` 对 m 的线性拟合。caption 可独立定义数据来源、sigmoid、n50 与颜色。 | 每 `(n,m)` 为 20 target strings 的均值；sigmoid minimum `R²=0.88`，`n50(m)` 为 PG19 `R²=0.999`、random `R²=0.995`。PG19 的斜率更大；作者将其解释为可利用的文本结构。证据：p. 7，`same pattern`。 |
| Table 1 | results, p. 8 | 行为 Ball、Cone、Ellipsoid 及两种 refinement；列为七个模型。表题定义 ratio。 | Ball ratios 为 7.77–20.4；Ellipsoid + Non-uniform Cells 为 4.56–10.82。表没有不确定性或重复试验信息。证据：p. 8, Table 1，`Ratio between the theoretical upper bound`。 |
| Figure 3 | results, p. 8 | conceptual density curves 用浅紫 D1、深紫 Dn 和阈值线说明 median criterion。 | 是 bound tightening 的机制图，没有实验误差或样本点。证据：p. 8，`Conceptual example`。 |
| Figure 4 | results, p. 9 | length 为横轴，exact-match copying accuracy 为纵轴；七个模型的 sigmoid line 与 legend 中 `R²`。caption 说明训练长度和 out-of-range evaluation。 | 作者报告 median `R²=0.95`；图例的 Qwen2.5-1.5B 为 0.46、Llama-3.2-1B 为 0.70，拟合质量存在异质性。没有 seeds、error bars 或 independent replications。证据：p. 9，`falls abruptly`。 |
| Figure 5 | appendix, p. 15 | 七个小图以 sampled input length 为横轴、internal radius R 为纵轴。 | 支持 bounded embedding 的经验检查；没有误差表达。证据：`Maximal radius R`。 |
| Figure 6 | appendix, p. 22 | cone 内的 `Eδ` 与 `Fδ` 几何分解。 | 服务 Lemma F.4 的 volume proof。证据：`Decomposition of the cone`。 |
| Table 2 | appendix, p. 23 | 各模型 d、`|V|`、r 与 θ。 | 将 architecture constants 与 Monte Carlo estimates 分开。证据：`Model constants used`。 |
| Table 3 | appendix, p. 26 | 每模型五个最大 decoder-cell token 及 `|E_t|/|E|`。 | Qwen-2.5 1.5B 的空格 cell 为 0.81；Gemma-3 270M 最大 cell 为 `1.1e-4`。证据：`largest estimated decoder-cell volumes`。 |
| Figures 7–8 | appendix, pp. 27–28 | 将 Figure 2 的三面板设计复制到 Pythia scales 与三种 architecture。 | 显示 cross-model curves；主文只放 Qwen-2.5 1.5B 的完整曲线。证据：`Results shown for`。 |
| Figure 9 | appendix, p. 29 | Ball、Cone、Ellipsoid 的 C upper bound 随 maximum sampled input length 变化。 | caption 称 ℓ 约 500 后足以估计上界。证据：`longer than ell ≈ 500`。 |
| Figure 10 | appendix, p. 29 | log-log 排序的 decoder-cell relative volume。 | 少数 token 占大面积，多数 token 为 `10^-6` 至 `10^-8`。证据：`small set of tokens`。 |
| Figure 11 | appendix, p. 30 | 多模型的 n-fold convolution distribution。 | 多数模型随 n 将质量快速推向零；Gemma-3 较慢。证据：`rapid concentration of mass`。 |

统计层级以 target strings、模型和 Monte Carlo samples 为主。中心量是 mean accessibility、`n50` 和 median cell-volume criterion。拟合有 sigmoid 与 linear fits；没有命名的假设检验、effect size、Bayesian analysis 或相关 / 回归模型。Figure 2 和 Figure 4 的 captions 可独立说明判定、横纵轴和拟合，但不说明不确定性表达。

## 消融、负面结果与自我设限

严格意义的 component-removal ablation 不存在，所以 `ablation` 模块编码为 `not_applicable`、0。Table 1 和 Sections 5.2–5.3 是理论上界的 sensitivity / refinement，而非删除模型组件后的识别实验。

| 项目 | 状态 | 类型与结论 | 页码与证据 |
|---|---|---|---|
| 组件删除消融 | not_present | 未删除 Transformer、decoder 或 mean-field 组件并比较可达性。 | p. 8, Table 1，`different enclosure strategies` |
| support geometry | observed | Ball、cone、ellipsoid 改变支持集包络，测试公式对几何假设的敏感性。 | p. 8, §5.2，`capture anisotropy` |
| non-uniform cells / variable epsilon | observed | Table 1 的两行 refinement 检验 equal-volume 与 uniform-precision 近似的松紧。 | pp. 8–9, Table 1，`Non-uniform Cells` |
| target / architecture heterogeneity | observed | PG19 与 random、多个 family / scale 的曲线检验结果是否跨分布和模型保留。 | pp. 7, 24, 27–28，`different model architectures` |
| failure / cost | observed | cramming 在 m 增大时成本过高，故 arbitrary-length 主张改用 copying task 的间接测试。 | p. 9, §5.4，`cramming becomes prohibitively expensive` |

自我设限出现得较早。p. 5 的 Remark 4.5 标注 uniform-grid precision；p. 6 将 Assumption 4.9 称为 non-trivial；p. 6 明说 fully used ball 和 equal-volume cells 是 worst-case；p. 9 将 Theorem 4.10 的经验评估和 lower bounds 留给 future work；p. 25 将 volume 分布的 conditional independence 作为工作假设。类型覆盖 assumption、compute、generality、metric 与 data。证据：p. 6，`two crucial assumptions`；p. 9，`derivation of theoretical lower bounds`；p. 20，`Although strong`。

## 结论、闭环与未闭合处

Section 6 没有引入新数字。它重述固定 m 的线性尺度、任意 m 的长度限制、embedding geometry 的作用，并将 copying failure 作为理论解释对象。Section 7 提出 test-time training、Theorem 4.10 的经验测试、lower bounds 和 Mamba 的后续工作。证据：p. 9, §6，`accessible sequence length grows`；p. 9, §7，`leave an empirical evaluation`。

| 引言主张 | 方法 / 理论回应 | 实验回应 | 结论回应 | 闭合状态 |
|---|---|---|---|---|
| 每个 Transformer 只能输出有限可达序列 | Definitions 4.1–4.2、Theorem 4.10 与 Appendix E 将问题转为 packing / elementary operations。 | 无对 Theorem 4.10 的直接容量测量。 | 重述「most sequences become inaccessible」。 | partially_closed |
| 固定 m 后可达比例出现指数衰减 | Theorem 4.6 与 Corollary 4.7。 | Figure 2 的 sharp transition；其拟合是 sigmoid，未直接估计指数 rate。 | 重述 critical threshold。 | closed |
| 阈值随 m 近线性增加 | Corollary 4.7。 | Figure 2 的 `n50(m)`，PG19 0.999、random 0.995 的 linear fit。 | 重述「at most linearly」。 | closed |
| architecture formula 能近似预测阈值 | Appendix F 把 Ball/Cone/Ellipsoid 和 cell-volume 代入 C。 | Table 1 的 ratio；若干值高于摘要的 `<10` 描述。 | 以 embedding geometry 概括。 | partially_closed |
| 解释 copying / cramming 的失败 | accessible-region 机制、Theorem 4.10。 | Figure 4 是 synthetic copying-length transition。 | 明说 explaining empirical failure。 | partially_closed |
| 结论在 unbounded context / computation 下成立 | mean-field、Assumption 4.9、Theorem 4.10 与 E.3。 | 无 direct empirical evaluation；条件有效性在附录讨论。 | 保留这一强表述。 | partially_closed |

## 附录承担的职责

附录共 17 个物理页，约为九页主叙事的 1.89 倍。主文将定义、两套核心定理、Cramming protocol、Figure 2、Table 1 和 Figure 4 留在决策位置；证明、precision 细化、详细优化参数、跨模型曲线、support convergence 及 cell-volume 分布移入附录。

| 一级模块 | 页码 | 分类 | 内容与主文调用 |
|---|---|---|---|
| A. Transformer Layers | 14–15 | extended_method | self-attention、layer 定义与 bounded-embedding 经验检查 Figure 5；p. 3 将 formal proof / validation 指向 Appendix A。 |
| B. Mean-Field Transformers | 14–15 | extended_method | pushforward、mean-field attention / layer、masked attention 延伸；p. 3 说明 Appendix B。 |
| C. Packing Number | 15–17 | proof | ball 与 measure-space packing bounds、non-uniform precision；p. 5 说明 Appendix C。 |
| D. Permutation-Invariant Norms and Wasserstein Distances | 18 | proof | Empirical-measure metric 与 Assumption 4.9 的尺度讨论；p. 6 调用 Appendix D。 |
| E. Arbitrary Prompt Length via Elementary Operations | 19–20 | proof | 将 Assumption 4.9 换成 elementary-operation precision 的有限基 argument；p. 6 的 Remark 4.12 调用。 |
| F. Theoretical Slope of the Cramming Task | 20–23 | proof | volume distribution、Ball/Cone/Ellipsoid 的 slope formulas；p. 8 指向 detailed analysis。 |
| G. Supplementary Experimental Results | 23–29 | reproducibility | constants、fp16 precision、optimizer、hardware、support sampling 和 Figures 7–9；p. 7、p. 8 均调用。 |
| H. Computing the Cell Volume Distribution | 25–30 | implementation_detail | 50M ellipsoid samples、Table 3、Figures 10–11；p. 8 调用 Appendix H。 |

主叙事可独立理解 Theorems 4.6 / 4.10 的陈述、Cramming 判定与主要图表。Table 1 的完整再现、Theorem 4.10 假设的细部、几何上界公式、cell volume 估计和跨模型曲线依赖附录。附录没有提供随机种子、error bars、optimizer restart sensitivity 或 direct empirical test of Theorem 4.10。证据：p. 24, §G.3；p. 9, §7。

## 用词与修辞

高频的实义核心是 `accessible`、`sequence`、`prompt`、`embedding`、`precision`、`bound`、`slope`、`threshold` 与 `cell`。这些词由 formal object 和经验预测共同驱动，未主要依赖模板语言。

- 主张动词包括 `show`、`prove`、`derive`、`predict`、`establish`、`explain`。`we show` 的强度由 Theorem 4.6 / 4.10 和 Figures 2 / 4 支撑。证据见 p. 1 的 `We show that every transformer`。
- 限定语包括 `only`、`almost all`、`up to`、`close`、`likely`、`may`、`suggest`。它们分别围绕有限可达集、上界松紧、PG19 解释和 future work。证据见 pp. 1, 7–9 的 `A likely reason`。
- 对比语包括 `In contrast`、`Moreover`、`Finally`。它们先在 related work 与贡献列表中划分邻近工作，再在 Section 5 分为理论预测与经验校准。证据见 p. 2 的 `In contrast, we study`。
- 因果语包括 `This matters for our bound`、`As a result`、`This suggests`。它们将 support geometry、cell volumes 与 accessibility threshold 连起。证据见 p. 8 的 `This matters for our bound`。
- 强主张集中在摘要、引言 bullets、Theorem / Corollary 与结论；弱主张集中在机制解释和 future work。后者用 `likely`、`suggest` 与 `would be interesting` 标记。证据见 pp. 7, 9 的 `These results suggest`。

## 可核验的叙事边界

| 观察 | 具体证据 | 中性解释 |
|---|---|---|
| 摘要的 `<10` 与 Table 1 的全表数值不一致 | p. 1, Abstract，`factor less than 10`；p. 8, Table 1 有 20.4、15.30、10.82、10.71 等。 | 摘要没有限定它指哪一行 refinement 或哪些模型。表格支持「若干 refined ratios 接近十」，未支持全表的 `<10`。 |
| support-sampling 分母出现两个数 | p. 8, §5.2，`10K prompts`；p. 24, §G.4，`N = 10^5`。 | 主文与附录对 support-parameter Monte Carlo 采样量使用不同数字，文本未解释两者关系。 |
| cross-model 曲线放在附录 | p. 7, §5.1，`Figure 2` 报 Qwen-2.5 1.5B；pp. 27–28, Figures 7–8 报其余曲线。 | 主文保留一个完整曲线实例，并以 Table 1 给出多模型比率；原始形状对照在附录。 |
| 不确定性与搜索敏感性未报告 | p. 7 的 20-target mean、p. 9 的 Figure 4 captions、p. 24 的单一 Adam setting。 | 可观察的是没有 seed、interval、error bar、restart 或 optimizer-sensitivity 报告；这限制了经验曲线的采样与优化不确定性判读。 |
| 自动测量草稿的页界和 figure count 错位 | 自动草稿给 appendix start p. 11、main end p. 30、10 figure captions；PDF p. 14 才出现 `A. Transformer Layers`，且 Figure 1–11 均有编号。 | 采用 PDF 物理页界与 11 个 Figure labels；自动草稿仅作为核对线索。 |

## 最终判断

**单一主线**：finite numerical precision 与 bounded representation geometry 让不同 prompts 可落入的 greedy-decoding regions 可被 packing number 限制；固定 prompt budget 因而只支持线性增长的 accessible length，而 arbitrary-length 版本需要额外的 Wasserstein 或 elementary-operation 条件。

**正文保留的决策内容**：Definition 4.1、Assumptions 4.3 / 4.9、Theorems 4.6 / 4.10、Cramming loss 和 exact-match criterion、Figure 2、Table 1、Figure 4 都在主文。这些对象足以让读者判断主张对象、理论条件和两类经验现象。

**附录迁移的影响**：证明与公式推导、precision implementation、support sampling、cell-volume Monte Carlo、跨模型曲线、support convergence 和 volume distributions 被移入 Appendix。主文可读性受益；完整检查阈值 tightness、assumption validity 与跨模型形状时必须读取 Appendix C–H。

**最有效的写作模式**：先把可达性定义为具有 epsilon 邻域的 prompt region，再用 packing number 导出长度上界，随后把同一变量映射为 `n50`、support geometry 和 copying transition。Figure 1 的几何直觉、Theorem 4.6 / Corollary 4.7 的形式链与 Figure 2 的判定指标形成直接对应。

**最大读者成本**：arbitrary-length 结论依赖 Section 4.2 的 non-trivial Assumption 4.9 或 Appendix E 的 elementary-operation condition，正文未直接测量 Theorem 4.10。摘要的 `<10` 也需要与 Table 1 的完整数字一起阅读。

**可迁移规则**：当论文主张 architecture-level limitation 时，应把能力对象定义成可计数或可度量的 region，写明将理论量映射到实验判定量的函数，并将每个经验图对应到一个具体推论。

**适用边界**：该规则适合存在明确 representation space、稳定判定和可控 prompt / input budget 的模型。涉及未经验证的 global precision、搜索可达性或跨长度 mean-field 假设时，正文应同屏呈现条件、直接检验和不确定性。

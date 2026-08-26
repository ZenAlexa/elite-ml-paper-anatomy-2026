# 深读：Why DPO is a Misspecified Estimator and How to Fix It

- **论文**：Aditya Gopalan、Sayak Ray Chowdhury、Debangshu Banerjee，ICLR 2026，`oral`。
- **读取范围**：`corpus/pdfs/iclr-2026-8e4dfde7b55f.pdf` 的全部 11 个物理页；PDF 第 10 页开始为 acknowledgments / references，第 11 页为 references。未提供 supplementary 文件；该 PDF 中没有 appendix 页。`p.` 均指 PDF 物理页。 [p. 10, *ACKNOWLEDGMENTS* / *REFERENCES*, layout_observation, “ACKNOWLEDGMENTS”; p. 11, *REFERENCES*, layout_observation, “Ziegler et al.”]
- **证据记号**：每个判断以 `[p. | section | basis | anchor]` 标示；`explicit` 为作者文字或图表明示，`layout_observation` 为版面可见事实，`interpretation` 为在前两者约束下的编码。

## A. 文档边界、页级地图与版面

### 物理边界

| 项目 | 编码 | 证据 |
|---|---:|---|
| PDF 总页数 | 11 | `pdfinfo` 与每页页脚均为 1–11；第 11 页仍是 references。 [p. 11, *REFERENCES*, layout_observation, “Fine-tuning language models”] |
| 正文页 | 9（p. 1–9） | p. 9 以 `Evaluation and Methodology` 结束实验叙述；p. 10 直接转 acknowledgments。 [p. 9, §5, explicit, “Ablation studies”; p. 10, *ACKNOWLEDGMENTS*, layout_observation, “SRC would like”] |
| References 页 | 2（p. 10–11） | p. 10 的 acknowledgments 后即为 `REFERENCES`，并延续到 p. 11。 [p. 10, *REFERENCES*, layout_observation, “R EFERENCES”; p. 11, *REFERENCES*, layout_observation, “Yuda Song”] |
| Appendix 页 | 0 | p. 10–11 已被 acknowledgments / references 占满；PDF 无 `Appendix` 标题。 [p. 10, *ACKNOWLEDGMENTS* / *REFERENCES*, layout_observation, “R EFERENCES”] |
| Supplementary | `unavailable` | 本次已验证输入只有主 PDF；正文却把 ablations、implementation、dataset details 指向 `Appendix B.2`，该材料不在此 PDF 中。 [p. 9, §5, explicit, “presented in Appendix B.2”; p. 10, *REFERENCES*, layout_observation, “R EFERENCES”] |

### 逐页地图

| 物理页 | 可见内容 | 语义角色与版面观察 |
|---:|---|---|
| 1 | 标题、作者、Abstract、§1 开始 | 标题/作者区占上方约四分之一，Abstract 为居中的单栏窄块；Introduction 从下半页开始，双栏正文。 [p. 1, *ABSTRACT* / §1, layout_observation, “A BSTRACT”] |
| 2 | §1、Figure 1、贡献列表 1–3 开始 | Figure 1 位于右栏，左栏的核心诊断段与图并置；贡献列表改为跨栏宽度的编号段落。 [p. 2, §1, layout_observation, “Figure 1: The geometry”] |
| 3 | 贡献 3 收束、Related work、§2、Eq. (1) | Related work 作为 `Related work.` 段落嵌在 Introduction 末尾；§2 占下半页，Eq. (1) 放在页底。 [p. 3, §1 / §2, layout_observation, “Related work.”] |
| 4 | §2 收束、Eq. (2)–(3)、§3、Proposition 1 / Eq. (4) | 全页几乎由正式定义、损失和第一个核心 proposition 构成；无图表。 [p. 4, §2 / §3, layout_observation, “Proposition 1”] |
| 5 | §3.1、局部线性化、Proposition 3、Figure 2、证明开始 | Figure 2 占右栏中下部；三响应反例的证明在左栏继续并跨至 p. 6。 [p. 5, §3.1, layout_observation, “Figure 2: An example”] |
| 6 | Proposition 3 解释、Remark 4、§4、§4.1 | 反例的五点解释占上半页；RLHF 的二阶局部近似在页底以两个数学块给出。 [p. 6, §3.1 / §4.1, layout_observation, “The example exhibits”] |
| 7 | §4.1 的 Eq. (5)–(6)、Lemma 6、Propositions 7–8、§4.2 开始 | 这一页从局部 RLHF 关系转入 AuxDPO 的构造，脚注补充等价类中的归一化项。 [p. 7, §4.1 / §4.2, layout_observation, “The AuxDPO Algorithm”] |
| 8 | §4.2、Figure 3、Eq. (7)、Proposition 9、经验损失、§5 开始 | Figure 3 在右栏解释三条几何子空间；经验 AuxDPO loss 与参数量说明后立即进入数据集介绍。 [p. 8, §4.2 / §5, layout_observation, “Figure 3: AuxDPO fixes”] |
| 9 | Tables 1–2、Evaluation and Methodology | 两张跨双栏宽表占据大部分页面；正文只给出训练/评测定义与一个总体结论段。 [p. 9, §5, layout_observation, “Table 1: Algorithm comparison”] |
| 10 | Acknowledgments、References 前半 | 正文在此前结束；无 conclusion、limitations 或 appendix。 [p. 10, *ACKNOWLEDGMENTS* / *REFERENCES*, layout_observation, “R EFERENCES”] |
| 11 | References 后半 | 仅参考文献。 [p. 11, *REFERENCES*, layout_observation, “Fine-tuning language models”] |

### 节与语义模块

以下词数为人工版面估计，统计对象为正文的叙述、公式与图表说明，不把 references、表内数值或页眉页脚计入。正文估计总量约 **5,204** 词；比例按此分母计算。

| 标题或语义块 | 物理页 | 模块 | 估计词数 / 正文份额 | 映射理由与面积 |
|---|---:|---|---:|---|
| Abstract | 1 | `abstract` | 167 / 3.2% | 六句连续摘要，单栏窄块。 [p. 1, *ABSTRACT*, layout_observation, “Direct alignment algorithms”] |
| §1 Introduction（不含其内 Related work） | 1–3 | `introduction` | 906 / 17.4% | 从 alignment 背景、RLHF 成本到 tabular 假设与三项贡献。 [p. 1–3, §1, explicit, “More specifically, we make”] |
| `Related work.`（无独立编号节） | 3 | `related_work` | 412 / 7.9% | 四段按 tabular assumption、coverage、gradient dynamics、最近 bandit 例子定位文献。 [p. 3, §1, explicit, “Related work.”] |
| §2 Preliminaries；§3、§3.1；§4.1 | 3–7 | `theory` | 2,134 / 41.0% | 定义 BTL / policy / loss，推出投影、局部线性化、等价类和近似结果。 [p. 4, §3, explicit, “DPO is weighted KL-projection”; p. 7, §4.1, explicit, “Approximation errors”] |
| §4 的开场 + §4.2 The AuxDPO Algorithm | 6–8 | `method` | 810 / 15.6% | 用 nullspace auxiliary variables 定义 population 与 empirical AuxDPO loss。 [p. 8, §4.2, explicit, “introduce auxiliary variables”] |
| §5 的数据集、训练/评测协议 | 8–9 | `experimental_design` | 340 / 6.5% | 数据、模型、ID/OOD 划分、比较方法和指标集中于两段。 [p. 8–9, §5, explicit, “Evaluation and Methodology”] |
| §5 的 Tables 1–2 与结论句 | 9 | `results` | 435 / 8.4% | 两表报告模型/数据集/subject 的结果，末句给总体解释。 [p. 9, §5, explicit, “Across all three models”] |
| Ablation | — | `ablation` | 0 / 0% | 正文把 ablation 指向未随 PDF 提供的 `Appendix B.2`。 [p. 9, §5, explicit, “Ablation studies”] |
| Conclusion | — | `conclusion` | 0 / 0% | p. 9 后直接是 acknowledgments。 [p. 9, §5, layout_observation, “Appendix B.2”; p. 10, *ACKNOWLEDGMENTS*, layout_observation, “SRC would like”] |
| Limitations | — | `limitations` | 0 / 0% | 没有 `Limitations` 标题或集中段落；适用条件散在理论部分。 [p. 7, §4.1, layout_observation, “Approximation errors”] |
| Appendix | — | `appendix` | 0 / 0% | 此已验证 PDF 不含 appendix 页。 [p. 10, *REFERENCES*, layout_observation, “R EFERENCES”] |

**版面结论。** 主文全程采用双栏；三幅图均为约一栏宽的几何图，分别放在诊断、反例和修复处。两张实验表跨双栏，令 p. 9 成为结果密度最高的一页。没有跨栏图，也没有算法伪代码；p. 1 的标题/作者/摘要空白和 p. 9 的表格共同压缩了可供叙述的面积。 [p. 1, *ABSTRACT*, layout_observation, “A BSTRACT”; p. 2, §1, layout_observation, “Figure 1”; p. 5, §3.1, layout_observation, “Figure 2”; p. 8, §4.2, layout_observation, “Figure 3”; p. 9, §5, layout_observation, “Table 1”]

## B. Abstract：逐句功能编码

| # | 词数 | 功能 | 限定、数字、比较与承接 | 证据 |
|---:|---:|---|---|---|
| 1 | 28 | `object_scope`, `method` | 对象为 DPO/direct alignment；以 `only supervised learning` 对照 two-stage RLHF；无数字。 | [p. 1, Abstract, explicit, “using only supervised learning”] |
| 2 | 18 | `core_idea`, `theory` | 将 DPO 改述为 induced reward functions 上的 statistical estimation；无数字或比较对象。 | [p. 1, Abstract, explicit, “statistical estimation problem”] |
| 3 | 40 | `problem_gap`, `theory` | 条件为真 reward 不能由 policy class realize；列出 order reversal、worsening reward、data-distribution sensitivity。 | [p. 1, Abstract, explicit, “cannot be realized”] |
| 4 | 27 | `theory`, `method` | `On the other hand` 从 DPO 诊断转到 two-stage RLHF 的 local behavior 与 natural gradient。 | [p. 1, Abstract, explicit, “natural gradient step”] |
| 5 | 36 | `core_idea`, `method` | AuxDPO 加入 auxiliary variables，目标是 `move towards the RLHF solution` 与 `mitigate`；`principled` 是方法性质修饰词。 | [p. 1, Abstract, explicit, “introduces additional auxiliary variables”] |
| 6 | 18 | `experimental_setup`, `qualitative_result` | 覆盖 didactic bandit 与 LLM alignment；以 `superior performance` 作无数字结果断言。 | [p. 1, Abstract, explicit, “superior performance of AuxDPO”] |

**功能顺序。** 摘要以对象及相对 RLHF 的训练形态开场，依次给出统计重构、misspecification 的失败模式、RLHF 的局部几何、AuxDPO 的修复机制，最后才给跨两类任务的经验结论。它没有报告数值、置信区间或显著性；也没有独立的 limitations 句。第 3 句的不可实现条件承担了理论适用边界，第 5 句承载修复主张，第 6 句收束到实验价值。 [p. 1, Abstract, explicit, “When the true reward function”; p. 1, Abstract, explicit, “We empirically demonstrate”]

## C. Introduction：论证推进

| 段落/动作 | 估计词数（占 Introduction 核心 906 词） | 上一段留下的问题 → 本段回答 → 下一钩子 | 证据 |
|---|---:|---|---|
| `context` | 62（6.8%） | 起点为空泛的 preference-based alignment；定义比较数据和 latent reward，使后文可以讨论 policy 目标。 | [p. 1, §1, explicit, “given comparison data”] |
| `problem` | 181（20.0%） | 已知目标后，具体化标准 two-stage RLHF 的 reward-model + RL 两阶段、rollout 与工程成本；钩子是更轻的替代方案。 | [p. 1, §1, explicit, “computationally demanding”] |
| `method_preview` | 130（14.3%） | DPO 作为单一 supervised phase 的替代被介绍；其所谓 one-step equivalence 留下前提问题。 | [p. 1–2, §1, explicit, “one-step equivalent”] |
| `missing_insight` | 158（17.4%） | 指出该 equivalence 依赖 tabular policy class，而 LLM 是有限参数的 non-tabular class；连续提出是否仍等价、差多少、能否修复三个问题。 | [p. 2, §1, explicit, “does minimizing the DPO loss”] |
| `core_idea` / `method_preview` | 135（14.9%） | 用 reward-function manifold 上的 misspecified estimation 回答诊断问题，并预告 AuxDPO；Figure 1 将投影、RLHF 解和额外自由度放入同一图。 | [p. 2, §1, explicit, “geometry of direct preference optimization”; p. 2, Figure 1, explicit, “additional controlled degrees of freedom”] |
| `contribution_list` | 240（26.5%） | 将诊断落实为 weighted KL-projection，将失败落实为 clean / infinite BTL data 下的反例，再以等价类和 AuxDPO 连到实验；钩子转向 Related work。 | [p. 2–3, §1, explicit, “More specifically, we make”] |

完整链条依次为：RLHF 的高成本、DPO 的便利性、tabular 假设断裂、parametric reward manifold 的投影诊断、反例、RLHF nullspace 线索与 AuxDPO。

贡献列表与摘要重复诊断、修复与验证的顺序，并加入可检验条件：贡献 1 对应 weighted KL projection，贡献 2 限定 clean/infinite BTL data 与 large-β linearization，贡献 3 指向 held-out preferences。列表没有数字结果；三项均可被 proposition 或表格反驳。 [p. 2, §1, explicit, “weighted KL-projection”; p. 2, §1, explicit, “clean data”; p. 3, §1, explicit, “held-out human preferences”]

## D. Related work：定位方式

Related work 没有独立编号节，位于 Introduction 与 §2 之间，约 412 词、约正文 7.9%、4 个引用簇。每段先给已有工作处理的 failure mechanism，再说明本文与之不同，因而没有再次展开 AuxDPO 公式。 [p. 3, §1, explicit, “Related work.”]

| 段 | 编码 | 引用簇与比较维度 | 证据 |
|---:|---|---|---|
| 1 | `taxonomy`, `credit_or_foundation`, `limitation_of_prior` | tabular-policy assumption 下的 RLHF、likelihood displacement、margin/length/reference-policy fixes；维度是问题机制与修复方向。 | [p. 3, §1 Related work, explicit, “tabular policy class assumption”] |
| 2 | `gap_creation`, `nearest_neighbor_contrast`, `limitation_of_prior` | Xu / Song 的 coverage 条件与 counterexample；本文主张 uniform base policy 下也可出现 reordering / reward decrease。 | [p. 3, §1 Related work, explicit, “even with perfect coverage”] |
| 3 | `taxonomy`, `nearest_neighbor_contrast` | gradient-step dynamics 工作与本文的 loss minimizer 分析；对比轴是单步优化轨迹与 population-loss 最优点。 | [p. 3, §1 Related work, explicit, “studying the minimizer”] |
| 4 | `nearest_neighbor_contrast`, `gap_creation` | Shi et al. 的 no-movement、对称退化 bandit 例子；本文主张非退化例子可严格恶化且随数据频率变化。 | [p. 3, §1 Related work, explicit, “degenerate and symmetric reward”] |

引用在后文继续承担论证：Song 的 global coverage 在 Remark 4 中被用作不足条件，Tajwar 的 scarce-data 解释在 p. 6 被排除，Pal/Razin 的 likelihood displacement 被用作较弱对照。 [p. 6, §3.1 Remark 4, explicit, “Global coverage is not sufficient”; p. 6, §3.1, explicit, “circumvents the issue”]

## E. 方法与理论

### 最小逻辑单元与动作转移

| 首次对象 | 位置 | 解决的前文问题 | 证据 |
|---|---|---|---|
| 有限 `S`、`A`、比较数据 `D`、BTL preference model | §2，p. 3 | 把「preference data」变成可写 population loss 的生成模型。 | [p. 3, §2, explicit, “Bradley-Terry-Luce (BTL) model”] |
| 光滑参数化 policy `πθ`、base `θ0`、KL-regularized objective `J` | §2，p. 3–4 | 明确 tabular 与 `d ≪ m` 的 parametric class 差异，并给出 RLHF 目标。 | [p. 3–4, §2, explicit, “structured and non-tabular”] |
| implicit reward `rθβ`、empirical / population DPO loss | §2，p. 4 | 将 DPO 转写为 reward-space 估计问题。 | [p. 4, §2, explicit, “implicit reward function”; p. 4, §2, explicit, “population DPO loss”] |
| Jacobian `Aθ0` 与局部线性 reward manifold | §3.1，p. 5 | 解释低维 manifold 如何限制 DPO 的可投影奖励。 | [p. 5, §3.1, explicit, “local linear approximation”] |
| `Aρ,θ0`、Fisher matrix、RLHF equivalence class | §4.1，p. 6–7 | 把理想 RLHF 解关联到 natural policy gradient 与 reward nullspace。 | [p. 6–7, §4.1, explicit, “natural policy gradient update”] |
| auxiliary `δ ∈ N(Aρ,θ0)`、population / empirical AuxDPO loss | §4.2，p. 7–8 | 用 DPO manifold 外的 nullspace 自由度消除 misspecification。 | [p. 8, §4.2, explicit, “bypass misspecification”] |

段落级转移为：`setup_notation → state_problem → derive → explain_mechanism → contrast_alternative → derive → define_component → instantiate_algorithm → state_complexity → connect_to_experiment`。前半由 Eq. (1)–(4) 把 DPO 的目标建立为加权投影，中段以局部近似与三响应反例诊断失败，后半将 RLHF 的等价类改写为 AuxDPO 的可训练辅助变量。 [p. 4, §3, explicit, “weighted KL-projection”; p. 5, §3.1, explicit, “preference reversal”; p. 8, §4.2, explicit, “total number of trainable parameters”]

### 公式、定理与证明

- 按独立 display math block 计，正文有 **14** 个；其中带显式编号的方程为 **7 个，即 Eq. (1)–(7)**。p. 3 有 Eq. (1)，p. 4 有 Eq. (2)–(4)，p. 7 有 Eq. (5)–(6)，p. 8 有 Eq. (7)。行内数学式数量未离散相加，避免把同一推导拆成多个伪公式。 [p. 3, §2, explicit, “(1)”; p. 4, §2 / §3, explicit, “(2)” / “(3)” / “(4)”; p. 7, §4.1, explicit, “(5)” / “(6)”; p. 8, §4.2, explicit, “(7)”]
- 正式结果有 **5 个 Proposition（1、3、7、8、9）和 1 个 Lemma（6）**；另有 Remarks 2、4、5。没有标为 Theorem 或 Corollary 的结果。 [p. 4, §3, explicit, “Proposition 1”; p. 5, §3.1, explicit, “Proposition 3”; p. 7, §4.1, explicit, “Lemma 6”; p. 8, §4.2, explicit, “Proposition 9”]
- Proposition 3 的具体三响应构造及其推导在主文 p. 5–6 出现。Propositions 1、7、8、9 与 Lemma 6 在这个 11 页 PDF 中只有陈述，没有随文可见 proof；p. 10 已进入 references。 [p. 5, §3.1, explicit, “Proof. Consider”; p. 10, *REFERENCES*, layout_observation, “R EFERENCES”]

| 结果 | 前置条件 | 结论与在因果链中的作用 | 证明位置 / 实证对应 |
|---|---|---|---|
| Proposition 1 | BTL 生成偏好；每个 triplet 的 count 固定；`θDPO` 最小化 population DPO loss。 | DPO 是对真 reward 到 `Rβ` 的 count-weighted reverse-KL projection；这是全篇「misspecified estimator」的核心链。 | 未提供 proof；Proposition 3 将其几何含义实例化。 [p. 4, §3, explicit, “weighted KL-projection”] |
| Remark 2 + Proposition 8 | 局部邻域、足够大的 `β`、有界集合。 | DPO manifold 的线性近似与 RLHF 目标的二次近似可把误差压到 `ε`；它是后续局部论证的保证。 | Proposition 8 仅陈述于 p. 7；没有可见 proof。 [p. 5, §3.1, explicit, “sufficiently large”; p. 7, §4.1, explicit, “Approximation errors”] |
| Proposition 3 | 单 prompt、3 responses、1 维 linear softmax、imbalanced pair counts、large `β`。 | 存在 DPO 使最高 reward action 概率下降、次优 action 上升、preference 反转且 expected reward 低于 base；作用是诊断。 | 主文 proof 在 p. 5–6；无 LLM 量化对应，只是 didactic counterexample。 [p. 5, §3.1, explicit, “preference reversal and reward decrease”; p. 6, §3.1, explicit, “average reward decreases”] |
| Lemma 6 + Proposition 7 | 固定 policy 参数；局部 RLHF 近似。 | 同一 `Rβeq(θ)` 的 rewards 相差 `N(Aρ,θ0)` 元素；DPO 的线性化 reward 是该等价类的 minimum-Mahalanobis-norm representative。 | 无可见 proof；为 `δ` 的构造提供机制解释。 [p. 7, §4.1, explicit, “differ by a vector δ”; p. 7, §4.1, explicit, “minimum Mahalonobis-norm”] |
| Proposition 9 | Proposition 1 假设、容差 `ε`、足够大的 `β`。 | AuxDPO 的优化器在 `O(ε)` 误差内达到 `θ*`；这是方法的局部保证。 | 无可见 proof；经验表在不同模型/数据上给出有限数据结果。 [p. 8, §4.2, explicit, “bypass misspecification”; p. 9, §5, explicit, “Algorithm comparison”] |

### 算法可执行性与复杂度边界

本文没有 Algorithm 环境或伪代码。AuxDPO 的可执行定义是：在 population loss 中共同优化 `θ` 与受 nullspace 约束的 `δ`，再以 `‖Aρ,θ0δ‖²` penalty 和每个偏好对的 `δ` 值构成 empirical loss。文中唯一的复杂度/规模说明是训练参数总数 `d + 2n = O(d)`，条件为典型地 `n ≪ d`；没有给出迭代步骤、运行时间、硬件预算或收敛准则。 [p. 8, §4.2, explicit, “minimize it jointly”; p. 8, §4.2, explicit, “d + 2n = O(d)”]

## F. 实验设计、统计与可视化

### 设计事实与可复现粒度

| 项目 | 编码 | 证据 |
|---|---|---|
| 明示 research questions / hypotheses | `not_present` | §5 直接从 `Datasets` 开始，没有编号 research question 或预注册假设。 [p. 8, §5, layout_observation, “Datasets.”] |
| 评测数据 | `observed` | RewardBench v2：1.87K prompts、每个 prompt 含 chosen/rejected；MMLU-Pro：12K 问题、每题 10 个候选答案。 [p. 8, §5, explicit, “1.87K prompts”; p. 8, §5, explicit, “12K complex questions”] |
| 训练数据 | `observed` | 使用预处理并二值化的 UltraFeedback。 [p. 9, §5, explicit, “U LTRA F EEDBACK”] |
| 模型 | `observed` | Table 1 覆盖 Llama3.1-8B、Llama3.2-1B、Qwen3-0.6B；Table 2 只展开 Llama3.1-8B。 [p. 9, Table 1 / Table 2, layout_observation, “Llama3.1-8B”] |
| 比较方法 | `observed` | AuxDPO 对 DPO、IPO、DPOP。 [p. 9, §5, explicit, “compare AuxDPO with DPO”] |
| ID protocol | `observed` | 每个 dataset 80/20 train/evaluation split，并声称保证 IID comparisons。 [p. 9, §5, explicit, “split 80/20”] |
| OOD protocol | `observed` | 在 cleaned UltraFeedback 上训练，在 preference datasets 上评估。 [p. 9, §5, explicit, “trained on cleaned”] |
| 训练方式 | `observed` | 报告 full finetuning。 [p. 9, §5, explicit, “full finetuning results”] |
| 主要指标 | `observed` | Table 1 以 chosen-response logits 是否高于 rejected-response logits 定义 accuracy；Table 2 以 generated answer 是否匹配 correct answer 定义 MMLU-Pro accuracy。 [p. 9, §5, explicit, “logits of the chosen”; p. 9, §5, explicit, “generated answer with the correct answer”] |
| 随机种子、重复次数、硬件、训练预算、超参数 | `unavailable` | 该 PDF 未给出；p. 9 将 implementation / dataset details 指向未提供的 `Appendix B.2`。 [p. 9, §5, explicit, “implementation, and dataset details”; p. 10, *REFERENCES*, layout_observation, “R EFERENCES”] |
| 数据泄漏控制与失败判定 | `not_present` | ID 的 80/20 划分和 OOD train/evaluation 来源已说明；未见额外 leakage-control 程序或预先定义的 failure threshold。 [p. 9, §5, explicit, “ensuring IID comparisons”] |

实验顺序在叙事上与贡献链相连：先在 p. 8 给出能覆盖 nullspace 的 empirical loss，再进入两类 benchmark；但 didactic bandit 的经验结果仅在 abstract 中被提及，主文 §5 的可见表格只覆盖 LLM models / datasets。 [p. 1, Abstract, explicit, “didactic bandit settings”; p. 8, §4.2 / §5, explicit, “empirical AuxDPO loss”; p. 9, Table 1, layout_observation, “Llama3.1-8B”]

### 图表、统计表达与结果

| 对象 | 模块 / 页 | 比较、编码与独立任务 | 误差或不确定性 |
|---|---|---|---|
| Figure 1 | `introduction`, p. 2 | 左图以黑色 `r*`、橙色 DPO solution、绿色 implicit reward manifold 表示投影；右图以蓝色 ideal RLHF、绿色 local linearized manifold、蓝色箭头的 AuxDPO 自由度表达诊断至修复。 | 无数值坐标、误差条或统计区间。 [p. 2, Figure 1, explicit, “geometry of DPO”] |
| Figure 2 | `theory`, p. 5 | 二维 reward 坐标中的 3-response、1-D counterexample；红线是 `C(Aθ0ᵀ)`，橙色区域显示随 pair count 变化的可能投影。 | 为解析例子，无抽样误差编码。 [p. 5, Figure 2, explicit, “failure modes of DPO”] |
| Figure 3 | `method`, p. 8 | 蓝线为目标 RLHF equivalence class，红线为 DPO manifold，绿线为固定 `θ` 时 auxiliary `δ` 的域。 | 为机制示意，无数值误差。 [p. 8, Figure 3, explicit, “AuxDPO fixes DPO’s misspecification”] |
| Table 1 | `results`, p. 9 | 行为 model × dataset × ID/OOD，列为 DPO/AuxDPO/IPO/DPOP；值为相对 base policy 的 mean-accuracy percentage change，bold/underline 表示前二，red 标识退化。 | 单一 cell 值；caption 与方法段未给 seeds、离散量、interval、test 或 multiple-comparison procedure。 [p. 9, Table 1, explicit, “percentage change in mean accuracy”; p. 9, §5, layout_observation, “57.14”] |
| Table 2 | `results`, p. 9 | MMLU-Pro overall 和按字母排序的前 10 subjects，分别报告 OOD / ID 的 Base 与四方法 accuracy；相同的 bold/underline/red 编码。 | 单一 cell 值；caption 未给 subject aggregation weights 或不确定性。 [p. 9, Table 2, explicit, “top 10 subjects alphabetically”] |

统计的聚合单位可见为 model–dataset–split（Table 1）和 subject–split / overall（Table 2）。中心量是相对 base 的 mean-accuracy percentage change 或 accuracy；本文可见页中没有误差条、standard deviation、confidence interval、bootstrap、Bayesian analysis、regression、correlation、假设检验或多重比较。表注足以定义主要比较和视觉标记，却没有给分母、seed 层级或重复次数。 [p. 9, Table 1, explicit, “relative to the base policy”; p. 9, Table 2, explicit, “overall win-rates”]

### 主要结果与不利解释处理

| 主张 | 可见证据及数值 | 可替代解释 / 边界 | 作者在 PDF 中的处理 |
|---|---|---|---|
| DPO 的 misspecification 可导致反序与 reward decrease。 | Proposition 3 给出 `r*=[2,3,1]`、三响应、一维 policy 和失衡 counts 的存在性例子；p. 6 明示 expected reward 低于 base。 [p. 5, §3.1, explicit, “three responses”; p. 6, §3.1, explicit, “average reward decreases”] | 这是特定的 existential didactic construction，不能仅由该命题推出 LLM 中的发生频率。 [p. 5, §3.1, interpretation, “There exists a promptless policy”] | 作者把数据稀缺与 optimizer idiosyncrasy 排除到该例的因果解释之外，强调 population / oracle optimization；这保留了例子的条件边界。 [p. 6, §3.1, explicit, “unlimited pairwise preference data”; p. 6, §3.1, explicit, “optimized exactly”] |
| AuxDPO 在局部理论下可回到 `θ*`。 | Proposition 9：在 Proposition 1 假设和 sufficiently large `β` 下，误差为 `O(ε)`。 [p. 8, §4.2, explicit, “minimized at θ = θ∗”] | 结论依赖局部、大 `β` 近似；脚注也把 guarantee 限定为 local sense。 [p. 8, §4.2, explicit, “valid in the local sense”] | 经验 AuxDPO loss 明确给出，故理论变量可映射到有限偏好数据的训练目标；无 proof 附在 PDF。 [p. 8, §4.2, explicit, “empirical loss version”] |
| Table 1 的显示单元大多支持 AuxDPO。 | 手工逐 cell 读取：12 个 model–dataset–split 单元中 AuxDPO 为最高值 11 次；唯一例外是 Llama3.2-1B / MMLU-Pro / OOD，IPO `14.58` 高于 AuxDPO `12.52`。 [p. 9, Table 1, layout_observation, “14.58”; p. 9, Table 1, layout_observation, “12.52”] | 单 cell 结果没有不确定性或 seed 信息，且一格例外限制「每个条件均最好」的读法。 [p. 9, Table 1, layout_observation, “Best gains are in bold”] | 作者在段末使用较宽的总体句「Across all three models」，并在表内显示而非删去该例外。 [p. 9, §5, explicit, “Across all three models”] |
| Table 2 的列出 subjects 支持 AuxDPO。 | 22 个可见 overall/subject × ID/OOD 单元中，AuxDPO 均为表内最高；overall 为 OOD `39.26`、ID `51.95`。 [p. 9, Table 2, layout_observation, “39.26”; p. 9, Table 2, layout_observation, “51.95”] | 表只含「top 10 subjects alphabetically」；PDF 没有给剩余 subjects 或聚合细节。 [p. 9, Table 2, explicit, “top 10 subjects alphabetically”] | 作者把 selection rule 写为 alphabetically；对未列 subjects 的表现无法由该表推断。 [p. 9, Table 2, explicit, “top 10 subjects alphabetically”] |

## G. 消融、负面结果与自我设限

- **Ablation / robustness**：`unavailable`。主文唯一明确说法是「Ablation studies, implementation, and dataset details are presented in Appendix B.2」，但本 PDF 的下一页已经进入 references，因而无法检查 ablation 对象、机制替代解释、超参数敏感性或训练成本。 [p. 9, §5, explicit, “Ablation studies”; p. 10, *REFERENCES*, layout_observation, “R EFERENCES”]
- **负面结果的可见性**：Table 1 明示用红色标记所有相对 base policy 的退化；Qwen3-0.6B / RewardBench v2 / OOD 中，DPO、IPO、DPOP 为负而 AuxDPO 为 `18.36`。这显示表中可见负值没有被隐藏，但只说明该张表的呈现方式。 [p. 9, Table 1, explicit, “marked in red”; p. 9, Table 1, layout_observation, “−8.16” / “18.36”]
- **理论 scope**：有限 `S`、`A`、BTL preference generation、unique optimizer、local neighborhood 与 sufficiently large `β` 是作者直接写出的边界。 [p. 3, §2, explicit, “S and A are finite”; p. 4, §2, explicit, “unique minimizer”; p. 7, §4.1, explicit, “β > βmin”]
- **专门 limitations / ethics / deployment**：`not_present`。文中没有独立节；结论页面也不存在。 [p. 9, §5, layout_observation, “Appendix B.2”; p. 10, *ACKNOWLEDGMENTS*, layout_observation, “ACKNOWLEDGMENTS”]
- **中性呈现判断**：能由版面确认的迁移只有实验细节向 `Appendix B.2` 的迁移，以及 Table 1 对负值的显式着色。作者是否出于叙事规避而做此安排，没有文本或版面证据。 [p. 9, §5, explicit, “presented in Appendix B.2”; p. 9, Table 1, explicit, “marked in red”]

## H. 闭环、结论与附录职责

### Claim-closure 矩阵

| 引言主张 | 方法 / 理论回应 | 设计 / 结果回应 | 结论回应 | 状态 |
|---|---|---|---|---|
| Parametric DPO 是 weighted KL-projection。 | Eq. (3) 的 population loss 与 Proposition 1 的 Eq. (4) 直接对应。 [p. 4, §2 / §3, explicit, “population DPO loss”; p. 4, §3, explicit, “weighted KL-projection”] | 无单独实验检验该恒等式。 | 无 dedicated conclusion。 [p. 10, *ACKNOWLEDGMENTS*, layout_observation, “ACKNOWLEDGMENTS”] | `partially_closed`：主张有正式陈述，但 PDF 未给 proof 或结论回收。 |
| Misspecified DPO 可反序、降 reward、对 pair frequencies 敏感。 | Proposition 3 + 证明直接构造三种失败；Remark 4 进一步排除 coverage 的充分性。 [p. 5–6, §3.1, explicit, “preference reversal”; p. 6, §3.1, explicit, “not sufficient”] | 没有对这些 failure modes 的 LLM 定量频率实验。 | 无 dedicated conclusion。 | `closed` 对存在性反例；其外推范围保持在该构造。 |
| Local RLHF 产生 reward equivalence classes。 | Eq. (5)–(6)、Lemma 6、Proposition 7 给出 natural-gradient 与 nullspace 关系。 [p. 7, §4.1, explicit, “equivalence classes induced”] | 作为 AuxDPO 的机制前提，没有直接测量 equivalence class。 | 无 dedicated conclusion。 | `partially_closed`：链条明确，证明缺失。 |
| AuxDPO 缓解 misspecification。 | Eq. (7) 和 Proposition 9 将 `δ` 接入 reward space，并给出 local / large-β guarantee。 [p. 8, §4.2, explicit, “bypass misspecification”] | Tables 1–2 给出 ID/OOD 比较；无可见 ablation、seed 或 implementation details。 [p. 9, §5, explicit, “Algorithm comparison”] | p. 9 的总体句代替 conclusion。 [p. 9, §5, explicit, “AuxDPO outperforms”] | `partially_closed`。 |
| AuxDPO 在 held-out human preferences 上优于 DPO。 | 方法段定义可训练 loss。 [p. 8, §4.2, explicit, “finite preference dataset”] | Table 1 的 11/12 单元优势和 Table 2 的可见 cells 支持总体趋势，但 Table 1 有一格 IPO 更高，且无不确定性报告。 [p. 9, Table 1, layout_observation, “14.58” / “12.52”] | 无 dedicated conclusion。 | `partially_closed`。 |

### Conclusion 与 Appendix

本 PDF 没有 conclusion：p. 9 的最后一句是「Across all three models, we see that AuxDPO outperforms other finetuning methods」，随后 p. 10 是 acknowledgments。因而没有在结尾新增数字或新增主张，也没有专门回收 theoretical assumptions、counterexample 边界或表格例外。 [p. 9, §5, explicit, “Across all three models”; p. 10, *ACKNOWLEDGMENTS*, layout_observation, “SRC would like”]

`appendix_inventory = []`：可见 PDF 中没有 appendix / supplementary 一级模块。正文对 `Appendix B.2` 的调用使 ablations、implementation 与 dataset details 成为主文外依赖，但该依赖材料没有随本次 PDF 出现；主文保留了决策性内容，即投影命题、反例、AuxDPO loss 和两张主结果表。 [p. 9, §5, explicit, “Appendix B.2”; p. 4, §3, explicit, “weighted KL-projection”; p. 9, Table 1, layout_observation, “Algorithm comparison”]

## I. 用词、修辞与叙事结构

- **高频实词的语境**。`DPO`、`reward`、`policy`、`preference`、`RLHF`、`misspecification`、`implicit`、`local` 由论证动作驱动。它们分别绑定损失、reward manifold、policy class、pair counts、两阶段目标、统计错误、`rθβ` 与 large-`β` approximation。原始 token 排名留给项目聚合器；此处不将图注和 references 混入计数。 [p. 4, §2 / §3, explicit, “implicit reward function”; p. 5, §3.1, explicit, “local linear approximation”]
- **claim verbs**：主文 p. 1–9 中，精确表面短语 `we show` 出现 5 次；`we demonstrate` 出现 2 次，另有 `We empirically demonstrate` 1 次；`we propose` 1 次、`we introduce` 2 次、`we develop` 1 次、`we compare` 2 次。`we find` 与 `we observe` 未出现。`show` 主要承载诊断/命题，`introduce` 与 `develop` 承载 AuxDPO 的构造，`compare` 只在实验段出现。 [p. 1, Abstract, explicit, “We show”; p. 2, §1, explicit, “We show that”; p. 8, §4.2, explicit, “We introduce”; p. 9, §5, explicit, “We compare”]
- **限定与对比**。`however`、`in contrast`、`on the other hand` 把 RLHF、tabular DPO 与 parametric DPO 分隔；`local`、`sufficiently large β`、`can`、`typically`、`ideally` 将结论绑定到近似与作用域。按主张句人工粗编码，强断言与受条件限制的断言约为 **14 对 14（约 1 比 1）**，不是 token 频率。 [p. 2, §1, explicit, “In contrast”; p. 5, §3.1, explicit, “sufficiently large”; p. 8, §4.2, explicit, “This should ideally”]
- **最强修辞位置**：Figure 1 把诊断和修复同页并置，贡献列表把三项 claim 压缩成一段，Figure 2 再把失败画成可视反例，Figure 3 紧接着把 remedy 画成补足 nullspace 的自由度。这种「几何图 → formal claim → counterexample → mechanism 图 → 表格」结构形成主叙事。 [p. 2, Figure 1, explicit, “geometry of DPO”; p. 5, Figure 2, explicit, “failure modes”; p. 8, Figure 3, explicit, “fixes DPO’s misspecification”]

## J. 最终判断

1. **单一主线**：有限参数 policy 把 DPO 的 implicit reward 限制到低维 manifold，因此 DPO 是由 preference counts 加权的 KL-projection；当真 reward 在该 manifold 外时，可产生反序和降 reward。局部 RLHF 表明同一 policy 对应含 nullspace 的 reward equivalence class，AuxDPO 用 `δ` 扩张搜索空间以接近 `θ*`。 [p. 2, §1, explicit, “misspecified statistical estimation”; p. 4, §3, explicit, “weighted KL-projection”; p. 8, §4.2, explicit, “additional degrees of freedom”]
2. **正文保留的决策关键内容**：正文保留了 formal loss、Proposition 1、一个可复核的三响应反例、AuxDPO 的 empirical loss、三张几何图和两张主结果表；这些对象让读者能追到诊断、机制、修复和数值比较。 [p. 4, §3, explicit, “Proposition 1”; p. 5, §3.1, explicit, “three responses”; p. 8, §4.2, explicit, “empirical AuxDPO loss”; p. 9, Table 1, layout_observation, “Algorithm comparison”]
3. **被移出或缺失的细节**：主文把 ablations、implementation、dataset details 指向 `Appendix B.2`；已验证 PDF 未包含该 appendix。对大-`β` 理论的多数 proofs 也未在该 PDF 中出现。这个缺口妨碍复核方法稳健性与复现实验，但不改变主文中可见的损失定义和表格事实。 [p. 9, §5, explicit, “presented in Appendix B.2”; p. 10, *REFERENCES*, layout_observation, “R EFERENCES”]
4. **最有效的写作 / 图 / 公式模式**：Figure 1 先将论文问题压缩成 reward-space geometry，Proposition 1 给出这一几何的精确投影式，Figure 2 给一个会失败的最小反例，Figure 3 再让 `δ` 的作用与 Eq. (7) 对应。该模式使 remedy 的每个自由度都有可见的诊断来源。 [p. 2, Figure 1, explicit, “projection”; p. 4, §3, explicit, “weighted KL-projection”; p. 5, Figure 2, explicit, “preference reversal”; p. 8, Figure 3 / Eq. (7), explicit, “AuxDPO fixes”]
5. **最明显的读者成本 / 未闭合处**：没有 conclusion；多数 formal results 没有可见 proofs；实验的 seeds、hyperparameters、hardware 与 ablations 依赖不存在于该输入中的 `Appendix B.2`。Table 1 的一格 IPO 优势也要求将总体优越性读成表内趋势，不能读成每个条件的严格统治。 [p. 7, §4.1, explicit, “Proposition 8”; p. 9, §5, explicit, “Appendix B.2”; p. 9, Table 1, layout_observation, “14.58” / “12.52”]
6. **可迁移规则**：理论算法论文可先用一张表示核心失配的机制图，再给满足边界条件的最小反例；修复方法应把每个新增自由度明确连接到反例的结构性原因，并以同一指标的主表收束。 [p. 2, Figure 1, explicit, “implicit reward manifold”; p. 5, Figure 2, explicit, “failure modes”; p. 8, Figure 3, explicit, “additional degrees of freedom”]
7. **规则的适用边界**：这一规则适用于已有可形式化 failure mechanism 的方法论文。只有 benchmark 比较、没有可辨认机制或反例的论文，不能凭图形顺序制造同等强度的因果主线；此时主表与设计控制必须承担更多论证责任。该边界是对本论文中「命题、反例与修复」结构的解释，不是关于未读取论文的比较。 [p. 4, §3, explicit, “Proposition 1”; p. 5, §3.1, explicit, “Proposition 3”; p. 8, §4.2, explicit, “Proposition 9”]

## K. 自动测量核对

机器测量草稿把 `main_end_page_provisional` 记为 11、`figure_captions` 记为 1、`numbered_equations_provisional` 记为 6。按 PDF 人工核对：正文止于 p. 9，p. 10–11 为 acknowledgments/references；Figure 1、2、3 分别在 p. 2、5、8；Eq. (1)–(7) 均有可见编号。表格计数 2、algorithm 计数 0 与版面一致。 [p. 2, Figure 1, layout_observation, “Figure 1”; p. 5, Figure 2, layout_observation, “Figure 2”; p. 8, Figure 3 / Eq. (7), layout_observation, “Figure 3” / “(7)” ]

# DTO-KD：独立深读备忘

- **paper_id**：`iclr-2026-eadaf839df8b`
- **题目**：DTO-KD - Dynamic Trade-off Optimization for Effective Knowledge Distillation
- **会议与等级**：ICLR 2026；`oral`
- **作者**：Zeeshan Hayder、Ali Cheraghian、Lars Petersson、Mehrtash Harandi、Richard Hartley
- **来源**：`corpus/pdfs/iclr-2026-eadaf839df8b.pdf`；PDF 物理页数 13；OpenReview forum=`https://openreview.net/forum?id=QMItTyQW92`
- **阅读边界**：已逐页阅读物理页 1–13，包括 references。PDF 在物理页 10 结束结论，物理页 11–13 为 references；没有 appendix 或 supplementary 文件。所有页码以下均为 PDF 物理页码。

## 1. 总览判断

论文把知识蒸馏（KD）中的任务损失与蒸馏损失视作两个同时优化的目标，以每次迭代的梯度组合取代固定的手工 loss weight。作者用梯度内积定义 Gradient Conflict（GrC），用梯度范数差异定义 Gradient Dominance（GrD），随后把两目标更新写成 simplex 上的最小范数问题，给出二目标闭式权重，并用 amortized update 避免每步两次 backpropagation。[p.4–6，§3–§3.1，explicit "Gradient Conflict (GrC)"；"Gradient Dominance (GrD)"；式 (9)–(15)]

最强的经验主线是「同一优化规则跨分类和检测都提高单点指标，并在有限的曲线/消融图中显示更少冲突、更少错误与更快收敛」。ImageNet-1K、CIFAR-100 和 COCO 表中 DTO-KD 均高于表内列出的基线；但表格只提供单点结果，没有 seed、离散度、显著性检验或完整超参数/损失定义。理论主张的可成立范围也没有写出。闭式解被置于 simplex，却未给出内部解条件或边界投影；上界式 (17) 的分母在梯度范数相等或顺序相反时可能为零或负。[p.6–10，§4–§6，layout_observation/interpretation / 表 1–5 单点数值；式 (9)–(17)]

## 2. 文档边界、版面与页级地图

### 2.1 版面事实

- PDF 共 13 页；正文（含 Abstract、§1–§6）至物理页 10；references 为物理页 11–13；appendix 页数为 0。[p.10–13，章节标题与页脚，layout_observation]
- 全文是单栏版式：页眉为 “Published as a conference paper at ICLR 2026”，正文、图和表在单一文字栏中排版；没有双栏正文或跨双栏浮动体。[p.1–10，layout_observation]
- 浮动体承担明显的版面切分：Figure 1 占据 p.2 上部，Figure 2 占据 p.4 上部；Table 1 占 p.8 上部；Tables 2–5 集中在 p.9；Figures 3–4 占 p.10 上部。[p.2、p.4、p.8–10，layout_observation]
- p.1 的标题、作者和单栏 Abstract 占据上半页，Introduction 在页底开始并于 p.2 接续；p.8 的大表把 §4.1–§4.3 压缩到表后；p.9 的四个表把 §4.4 分成上下两段；p.10 的两幅图把结果解释置于图下，Limitations 与 Conclusion 共享下半页。[p.1、p.8–10，layout_observation]

### 2.2 页级地图

| 物理页 | 内容与模块 | 估计词数* | 版面/语义观察 |
|---|---|---:|---|
| 1 | 标题、Abstract；§1 Introduction 起始 | 约 500（Abstract 191） | 标题和摘要单栏居中；引言从页中开始，页尾截断至 p.2。[p.1，layout_observation] |
| 2 | §1 Introduction 续；Figure 1；贡献列表前两项 | 约 540 | Figure 1 在上部，随后是问题诊断、核心想法和贡献列表。[p.2，layout_observation] |
| 3 | §1 贡献列表末项；§2 Related Work | 约 640 | 相关工作完整占据单栏页；按四个主题小节推进。[p.3，layout_observation] |
| 4 | Figure 2；§3 Method、Problem formulation；式 (1)–(4) | 约 430 | 方法图先于正式问题定义，图后立即进入损失与梯度问题。[p.4，layout_observation] |
| 5 | §3.1 Stage 1/2；式 (5)–(10)；Theorem 3.1 开始 | 约 510 | min–max、simplex 和理论部分连续排版。[p.5，layout_observation] |
| 6 | Theorem 3.1 续；式 (11)–(17)；Corollary 3.2–3.5；Practical Implementation 开始 | 约 430 | 理论陈述密集，证明没有单独出现。[p.6，layout_observation] |
| 7 | Algorithm 1；式 (18)；§4 Experiments 与 Implementation details | 约 600 | 算法跨栏宽度显示；近似更新与实验设置接在理论之后。[p.7，layout_observation] |
| 8 | Table 1；§4.1 ImageNet-1K；§4.2 CIFAR-100；§4.3 COCO 开始 | 约 620 | Table 1 位于页首，实验叙述在表后。[p.8，layout_observation] |
| 9 | Table 2、Table 3；§4.3 续；§4.4 Ablation；Table 4、Table 5 | 约 800 | 四张结果/消融表挤在一页，正文解释被表格分隔。[p.9，layout_observation] |
| 10 | Figure 3、Figure 4；§4.4 续；§5 Limitations；§6 Conclusion | 约 480 | 两图在页首；限制和结论均只有短段落。[p.10，layout_observation] |
| 11 | References（A–L 左右） | 约 470 | 无正文模块。[p.11，layout_observation] |
| 12 | References（L–T） | 约 460 | 无正文模块。[p.12，layout_observation] |
| 13 | References（T–Z） | 约 540 | 页末为 references 结束，无 appendix 标题或正文。[p.13，layout_observation] |

\* 词数是从目标 PDF 的版面文本提取后按模块作的估计，不把它当作项目统一 lexical 分析的原始计数。页级提取总量含标题、表格、公式、页眉和页脚，因此模块估计不与页级值机械相加。

**章节—语义模块映射**：Abstract→`abstract`；§1→`introduction`；§2→`related_work`；§3 中问题定义、算法和 §3.1→`method`，其中 Theoretical Properties 单独计入 `theory`；§4 的设置→`experimental_design`，主表与 Figure 1/3/4 的实证→`results`，§4.4 的组件表→`ablation`；§5→`limitations`；§6→`conclusion`；§§references→`other`。论文没有独立的 theory 章节，`theory` 是 §3.1 的语义子模块。[p.4–10，章节标题，interpretation]

## 3. Abstract 逐句功能编码

Abstract 共 8 句，约 191 词；顺序为对象与背景 → 两个问题 → 方法 → 两个机制问题 → 更新性质 → 实验范围 → 综合结果 → 超越非蒸馏学生的强主张。[p.1，Abstract，layout_observation]

| # | 句子 | 词数 | 功能 | 限定词/数字/比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | Knowledge Distillation (KD) is a widely adopted framework for compressing large models into compact student models by transferring knowledge from a high-capacity teacher. | 23 | `object_scope` | “widely adopted”；large→compact；teacher | [p.1，Abstract，explicit “compressing large models into compact student models”] |
| 2 | Despite its success, KD presents two persistent challenges: (1) the trade-off between optimizing for the primary task loss and mimicking the teacher’s outputs, and (2) the gradient disparity arising from architectural and representational mismatches between teacher and student models. | 39 | `problem_gap` | “two persistent challenges”；两个 numbered challenges | [p.1，Abstract，explicit “two persistent challenges”] |
| 3 | In this work, we propose Dynamic Trade-off Optimization for Knowledge Distillation (DTO-KD), a principled multi-objective optimization formulation of KD that dynamically balances task and distillation losses at the gradient level. | 30 | `core_idea`, `method` | “propose”；dynamic、gradient-level、multi-objective | [p.1，Abstract，explicit “dynamically balances task and distillation losses at the gradient level”] |
| 4 | Specifically, DTO-KD resolves two critical issues in gradient-based KD optimization: (i) gradient conflict, where task and distillation gradients are directionally misaligned, and (ii) gradient dominance, where one objective suppresses learning progress on the other. | 34 | `problem_gap`, `core_idea` | “resolves”；GrC/GrD；方向和幅度 | [p.1，Abstract，explicit “gradient conflict” and “gradient dominance”] |
| 5 | Our method adapts per-iteration trade-offs by leveraging gradient projection techniques to ensure balanced and constructive updates. | 16 | `method` | “per-iteration”；“balanced and constructive” | [p.1，Abstract，explicit “adapts per-iteration trade-offs”] |
| 6 | We evaluate DTO-KD on large-scale benchmarks including ImageNet-1K for classification and COCO for object detection. | 15 | `experimental_setup` | ImageNet-1K、COCO；classification/detection | [p.1，Abstract，explicit “ImageNet-1K for classification and COCO for object detection”] |
| 7 | Across both tasks, DTO-KD outperforms prior KD methods, yielding state-of-the-art accuracy and improved convergence behavior. | 15 | `quantitative_result`, `qualitative_result` | “both tasks”；无具体数值；prior KD | [p.1，Abstract，explicit “outperforms prior KD methods”] |
| 8 | Furthermore, student trained with DTO-KD exceed the performance of their non-distilled counterparts, demonstrating the efficacy of our multi-objective formulation. | 19 | `quantitative_result`, `impact_claim` | “exceed”；与 non-distilled counterparts 比较 | [p.1，Abstract，explicit “exceed the performance of their non-distilled counterparts”] |

摘要报告了实验范围和方向性结论，但没有具体 Top-1/AP 数字、seed、误差表达、理论定理名称或局限。最强主张放在末句（超越非蒸馏学生），而“state-of-the-art”在倒数第二句以无数字形式出现。[p.1，Abstract，layout_observation]

## 4. Introduction 的论证推进

引言横跨 p.1–p.3 页首，共约 800 词；它不单列研究问题或假设，而是以问题、机制、贡献列表推进。[p.1–3，§1，layout_observation]

| # | 主动作 | 估计词数 | 上一段留下的问题 → 当前段回答 → 下一钩子 | 证据 |
|---:|---|---:|---|---|
| 1 | `context` | 150 | 视觉模型部署成本高 → KD 以 teacher 指导 compact student → 现有 KD 传什么知识？ | [p.1，§1，explicit “deployment … resource-limited platforms”] |
| 2 | `problem` | 130 | 只模仿 logits 信息压缩 → intermediate feature 传递更丰富知识，但带来 heuristic 与 hyperparameter → 近年的 feature KD 是否解决了冲突？ | [p.1，§1，explicit “relying solely on logits constrains the richness”] |
| 3 | `failure_of_prior_work` | 105 | feature-level 的表达力提高 → 与任务监督不一致的 objective mismatch 仍在 → 需要直接观察优化动态 | [p.1–2，§1，explicit “mismatches between the objectives”] |
| 4 | `problem` | 120 | 现有 balance heuristic 不足 → GrC（内积负）和 GrD（范数不平衡）成为两个具体瓶颈，并由 Figure 1 展示 → 需要新的优化策略 | [p.2，§1，explicit “The primary issue … is two-fold”] |
| 5 | `missing_insight` | 105 | 两种梯度问题 → 将 KD 重写为 dynamic trade-off / MOO，并寻求 Pareto-optimal solution → 如何得到每步 trade-off？ | [p.2，§1，explicit “frame the problem as a dynamic trade-off optimization”] |
| 6 | `core_idea` | 115 | 手工 α 权重无法跟随快速变化 → 闭式解产生同时对齐两目标的更新 → 可否端到端、少调参地训练？ | [p.2，§1，explicit “closed-form method for determining how to weight”] |
| 7 | `method_preview` + `result_preview` | 95 | 核心闭式 trade-off → 端到端、fewer epochs、两类视觉任务 → 贡献列表细分机制与实证 | [p.2，§1，explicit “trained end to end” and “requiring fewer epochs”] |
| 8 | `contribution_list` | 80 | 摘要中的方法/机制/实验主张 → 三项 bullet 分别承诺 dynamic gradient balance、GrC/GrD resolution、classification/detection SOTA 与 ablation → §2 相关工作 | [p.2–3，§1，explicit “the contributions of this paper are as follows”] |

**推进链**：部署约束 → KD 的知识容量与 objective mismatch → GrC/GrD 诊断 → dynamic MOO/Pareto 缺口 → closed-form trade-off → 端到端与速度主张 → 三项贡献。贡献列表基本复述摘要，没有预先编号的可证伪 hypothesis；它包含可检验的 SOTA、ablation 和 convergence 方向，但没有数字门槛或失败判定。[p.2–3，§1，interpretation]

## 5. Related Work

相关工作只有 p.3 的独立 §2，约 580 词、四个主题小节，先按蒸馏信号类型分类，再以 MOO 作为优化基础。每个小节都承担「列举→最近方法差异→仍有缺口→DTO-KD 定位」中的部分动作；它没有在后续方法段落重复逐篇介绍引用。[p.3，§2，layout_observation]

1. **Logit-level distillation**：以 classical KD、ensemble、teacher assistant、decoupled distillation 做 chronology/taxonomy；比较 forward KL、reverse KL、α–β divergence 的分布偏好，最后把只传 final-layer information 与 limited generalization 作为缺口。[p.3，§2 “Aligning Predictive Distributions via Logit-Level Distillation”，explicit “transfer only final-layer information”]
2. **Feature-level distillation**：从 FitNets、Margin ReLU、connection pathways 到 diffusion 与 norm/direction-aware losses，按 feature selection/alignment 分类；具体缺口是 long-range dependency 与 global context。[p.3，§2 “Transferring Intermediate Representations via Feature-Level Distillation”，explicit “struggles to encode long-range dependencies”]
3. **Token-level distillation**：从 DeiT 到 token matching、multiple teachers、manifold alignment、f-divergence；承认 transformer semantics 的优势，同时指出 dark knowledge 与 token relation 难传，已有方案 heuristic/fragmented，因而引出 unified end-to-end trade-off。[p.3，§2 “Leveraging Transformer Semantics via Token-Level Distillation”，explicit “heuristic and fragmented”]
4. **MOO**：先列 manual re-weighting，再列 gradient manipulation（upper bound、projection、closed form、fast dynamic weighting）；比较维度是 heuristic、动态梯度交互和理论基础，最后声称 DTO-KD 将 MOO 独特用于 KD。[p.3，§2 “Aligning Conflicting Objectives via Multi-objective Optimization”，explicit “uniquely applies it to knowledge distillation”]

相关工作最有效的定位句是「MOO 已用于 multi-task learning，但本文把它变成 KD 的 dynamic trade-off」。未给出逐项统一 benchmark 或同条件比较的文献表；后文的基线比较依赖实验表，related-work 的引用簇仅用于定位。[p.3，§2，interpretation]

## 6. 方法与理论

### 6.1 形式化对象与问题

- Teacher 参数为 `ϕ`，student 参数为 `θ`；数据为 `S={(x_i,y_i)}_{i=1}^N`，`x_i∈R^d`，`y_i` 可为 class label 或 bounding box。目标是让 student 模仿 teacher，同时服从任务监督。[p.4，§3 Problem formulation，explicit “parameters ϕ … parameters θ”]
- 定义 `L_distill(θ)` 与 `L_task(θ)` 的一般期望形式（式 (1)、(2)），再把常规 KD 写成固定 `α_1 L_distill+α_2 L_task`（式 (3)），总梯度为 `α_1 g_dist+α_2 g_task`（式 (4)）。作者说分类和检测的具体 loss 留到 appendix，但本 PDF 没有 appendix。[p.4，§3，explicit 式 (1)–(4)；p.11–13，layout_observation]
- GrC 定义为 `⟨g_dist,g_task⟩<0`；GrD 定义为梯度大小显著不同，文中用 `∥g_dist∥/∥g_task∥` 估计。作者将固定 α 的困难归因于梯度范数随训练变化。[p.4–5，§3，explicit “⟨g_dist , g_task ⟩ < 0” and “norm of gradients varies”]
- MOO 目标向量为 `(L_distill,L_task)^⊤`，以不存在同时不高于它的参数向量来定义 Pareto optimal（式 (5)）。作者把取消手工 α 与同时对齐两个梯度作为 MOO 的收益。[p.5，§3，explicit 式 (5)]

### 6.2 两阶段 dynamic trade-off

1. **Stage 1：改善率**。以 `θ_{t+1}=θ_t−ηg_t` 更新，定义两个相对改善率 `r_dist` 和 `r_task`（式 (6)）；更大的 rate 表示沿当前方向对应 loss 改善更多。[p.5，§3.1 Stage 1，explicit “A larger value … implies the associated task has been improved more”]
2. **Stage 2：最坏改善率的 min–max**。最大化两个 rate 中较小者并惩罚 `∥g_t∥²`（式 (7)，权重超参数 `γ`）；通过 Liu et al. (2023) 的 dual，把 `π=(π_1,π_2)` 放到 simplex `π_1+π_2=1, π_i≥0`，构造 `J_t=[∇log L_distill | ∇log L_task]^⊤`（式 (8)–(9)）。[p.5，§3.1 Stage 2，explicit 式 (7)–(9)]
3. **闭式二目标解**。令 `G=J_t^⊤J_t`，`g_11,g_12,g_22` 为两个 log-loss gradient 的 Gram 元素，作者给出 `π_1*=(g_22−g_12)/(g_11+g_22−2g_12)`、`π_2*=(g_11−g_12)/(g_11+g_22−2g_12)`（式 (10)–(15)）。[p.5–6，§3.1 Theoretical Properties，explicit 式 (10)–(15)]
4. **理论解释**。作者声称闭式更新同时与两个目标对齐（Corollary 3.2），两个内积贡献相等从而缓解 GrD（Corollary 3.3），并给出 norm 下界/上界（Corollary 3.4–3.5），最后借 Liu et al. (2023) 声称收敛到 Pareto front。[p.6，§3.1，explicit “aligned with both” and “guaranteed to converge”]

### 6.3 算法实现与精确/近似差异

Algorithm 1 的最小逻辑单元为：初始化 frozen teacher 和 trainable student；每 batch 前向得到 `z_t,z_s`；用多尺度 lightweight projector `P` 和 `DistillHead`/`TaskHead` 计算两 loss；按当前 `π` 组合 log-loss gradients；更新 student；在 frozen model inference 后计算相对改善率；更新 `π`。[p.6–7，§3.1 Practical Implementation、Algorithm 1，explicit "teacher as a frozen model"；算法第 1–12 行]

算法只有一个外层 `for t=1:T` 循环，没有嵌套循环；初始化 `π_distill=π_task=1/2`。正文指出精确 MTL 需要每任务梯度、每步两次 backpropagation；因此实际使用式 (18) 的 amortized π 更新，并用 softmax 重新归一化，因为式 (18) 本身不保证 `π∈Δ`。[p.7，Algorithm 1、式 (18)，explicit “two backpropagation per iteration” and “renormalize … via a softmax function”]

这里存在一个决定性边界：论文把闭式 simplex 解当作理论性质，却没有说明当式 (11)–(12) 给出负权重时如何投影到 simplex；实际 amortized 方案采用另一个带 `η_π` 的近似更新，与闭式解不同。式 (18) 还引入学习率 `η_π`，而 §3.1 的 Stage 1 使用 `η`、Algorithm 1 的 student update 使用 `γ`，符号没有完全统一。[p.5–7，§3.1、Algorithm 1、式 (18)，interpretation “π∈Δ”与“softmax”并列但无边界条件]

作者报告 amortized 版本「DTO-KD reaches the top performance of Roy Miles & Deng (2024) with 300 epochs in just 240 epochs」，但没有给出对应曲线、指标或重复次数；这是收敛速度的单个比较句，不是完整的效率分析。[p.7，§3.1，explicit “with 300 epochs in just 240 epochs”]

### 6.4 理论结果的条件、证明和风险

| 结果 | 文中结论 | 前置条件/证明位置 | 读法与闭合度 |
|---|---|---|---|
| Theorem 3.1 | simplex 约束下的二权重闭式表达 | `J_t`、Gram 矩阵；正文只有 statement，未给 proof | 形式上是核心链，但没有写出闭式解落在 `[0,1]^2` 的条件。[p.5–6，式 (9)–(15)，interpretation] |
| Corollary 3.2 | `g*` 与 `g_1,g_2` 都 aligned | 依赖式 (11) 的 `π*` | 若两梯度正好相反，最小范数组合可能为零；“aligned”需要非退化条件，正文未列出。[p.6，Corollary 3.2，interpretation] |
| Corollary 3.3 | 两个内积贡献相等 | 依赖 Gram 元素与 `∥g_1−g_2∥²` 分母 | 等贡献是代数陈述，但不等同于每个目标都有正下降；正文未区分这两点。[p.6，Corollary 3.3，interpretation] |
| Corollary 3.4 | `∥g*∥≥(1/√2)min(∥g_1∥,∥g_2∥)` | 无额外角度/非退化条件 | 取 `g_1=−g_2` 时左侧可为 0，故按正文的普遍语气该下界需要条件或修正。[p.6，式 (16)，interpretation] |
| Corollary 3.5 | `∥g*∥≤∥g_1∥∥g_2∥/(∥g_1∥−∥g_2∥)` | 无额外 norm 顺序条件 | 当 `∥g_1∥=∥g_2∥` 分母为 0，顺序相反时右侧为负；正文没有绝对值/条件，稳定性保证因此未闭合。[p.6，式 (17)，interpretation] |
| 收敛主张 | 收敛到 Pareto-optimal front | 仅说与 Liu et al. (2023) 框架一致；没有本文 proof | 精确算法与 amortized 近似不同，近似版的 Pareto guarantee 未单独建立。[p.6–7，§3.1，interpretation] |

## 7. 实验设计

实验设计按两个任务展开，但没有预先编号的 research question/hypothesis，也没有显式 failure criterion。实施细节只明确给出部分 ImageNet/COCO 设置；CIFAR-100 依赖先前工作 protocol。[p.7–8，§4，explicit “We evaluate DTO-KD on two distinct vision tasks”]

| 设计项 | 记录 | 状态与证据 |
|---|---|---|
| 研究问题/假设 | 没有 RQ/H 编号；按分类、检测及消融组织 | `not_present`。[p.7，§4，layout_observation] |
| ImageNet-1K | RegNetY-160（ImageNet-21K 预训练）→ DeiT-tiny/DeiT-small；student 300 epochs；Top@1 | `observed`。[p.7–8，§4、§4.1，explicit “pre-trained on the larger ImageNet-21K”] |
| CIFAR-100 | homogeneous：ResNet-56→ResNet-20、WRN-40-2→WRN-40-1、ResNet-32×4→ResNet-8×4；heterogeneous：ResNet-50→MobileNet-V2、ResNet-32×4→ShuffleNet-V1/V2 | `observed`，表 2；训练 epoch/seed 未给。[p.9，Table 2，explicit] |
| COCO | MS-COCO/COCO2017 val；ViDT/Swin-nano、tiny、small student；ViDT-base/Swin-base teacher；50 epochs；AP、AP50、AP75、APS、APM、APL、参数量、FPS | `observed`。[p.8–9，§4.3、Table 3，explicit] |
| 不同 teacher | Table 5 比较 ViDT-small 与 ViDT-base 作为 teacher，报告 ViDT-nano/tiny student 的 AP | `observed`，但只覆盖检测和两种 teacher。[p.9–10，Table 5、§4.4，explicit] |
| 优化器与超参数 | AdamW；正文先给整体 lr 0.025、wd 0.01，分类又给 lr 0.001、wd 0.05；检测 body/neck/head 初始 lr `10^-4`，其余沿用 ViDT/DeiT | `observed`，存在表述层级不清。[p.7，Implementation details，explicit/interpretation] |
| 增广与实现 | 分类增广沿用 Roy Miles & Deng (2024)，分类策略沿用 DeiT；检测沿用 ViDT；PyTorch；四张 NVIDIA H100 | `observed`。[p.7，Implementation details，explicit] |
| 随机种子与重复 | 全文没有 seed、重复次数、标准差、置信区间或显著性检验 | `not_present`。[p.7–10，Tables 1–5 与 captions，layout_observation] |
| 控制与匹配 | 表格给出 epoch、student/teacher、部分参数量；CIFAR 遵循先前 protocol；未给数据泄漏控制、冻结/初始化的完整对照或失败判定 | 部分 `observed`，其余 `not_present`。[p.8–9，Table captions；p.7，Implementation details] |
| 实现来源/代码 | 只写 PyTorch framework，没有本论文代码仓库或复现实验链接 | `not_present`。[p.7，Implementation details，layout_observation] |

实验顺序大致对应引言的三项贡献：先分类（ImageNet、CIFAR），再检测（COCO），最后做组件、权重曲线、错误与 teacher-scale 分析；理论中的 GrC/GrD 只有 Figure 1 的检测诊断和 Figure 3 的权重曲线对应，没有针对每个理论 corollary 的独立检验。[p.2–3、p.8–10，§1、§4，interpretation]

## 8. 结果、统计与可视化

论文报告的是点估计/单次表格数值。所有主表都没有误差条、seed 聚合、区间、假设检验、多重比较、bootstrap、Bayesian analysis、回归或 effect-size 分析；因此只能把数字解释为作者在给定设置下报告的点结果，不能从版面推断稳定性或统计显著性。[p.8–10，Tables 1–5、Figures 1、3–4，layout_observation]

### 8.1 Visual inventory 与主要结果

1. **Figure 1（p.2，§1）**：左右两个 500-iteration 曲线，比较 VKD（Roy Miles & Deng, 2024）与 Ours。左图是 `⟨g_dist,g_task⟩` conflict score，越负表示越强 disagreement；右图是 `|g_dist|/|g_task|` 的 log-scale dominance score，越低表示越强 dominance。作者的解释是 Ours conflict 更低、dominance 更平衡；图没有均值、误差带、seed 或数值汇总。[p.2，Figure 1 caption，explicit “500 iterations” and “lower values indicating stronger dominance”]

2. **Table 1（p.8，§4.1）**。ImageNet-1K Top@1。DeiT-Ti 的数据为非蒸馏 72.2、普通 KD 74.5、VKD-Ti 78.3、DTO-KD (Ti) 79.7；DeiT-S 的数据为非蒸馏 79.8、普通 KD 81.2、VKD-S 82.3、DTO-KD (S) 83.1。所有普通行默认 300 epochs，标注的 1000 epochs 行除外。作者计算 DTO 相对普通 KD 为 +5.2 pp（Ti）和 +1.9 pp（S），相对 VKD 为 +1.4 pp 和 +0.8 pp。[p.8，Table 1、§4.1，explicit 表值与 “5.2/1.9/1.4/0.8 pp”]

3. **Table 2（p.9，§4.2）**：CIFAR-100 Top-1，六个 homogeneous/heterogeneous teacher–student 设置。DTO-KD 行为 `72.35, 75.68, 76.40, 70.90, 77.95, 78.22`；每列均高于表中对应的 Student 和既有 KD 行。表格只给点 Top-1，未给平均/方差。[p.9，Table 2，explicit/layout_observation]

4. **Table 3（p.9，§4.3）**：COCO 检测，50 epochs。DTO-KD AP 为 nano 43.7、tiny 47.4、small 49.6；对应 VKD 为 43.0、46.9、48.5，因此作者报告 +0.7、+0.5、+1.1 pp。DTO small（61M）AP 49.6 高于从 scratch 的 Swin-base（0.1B）49.4；DTO tiny（38M）AP 47.4 接近 Swin-small（61M）47.5。其余 AP50/AP75/scale-specific AP、参数量与 FPS 也在表中给出，但没有误差表达。[p.8–9，Table 3、§4.3，explicit 表值与 “0.7/0.5/1.1 percentage points”]

5. **Table 4（p.9，§4.4）**：组件消融使用 DTO-KD-nano/ViDT-base，指标 AP/AP50/AP75。无组件为 41.0/59.2/42.8；仅 gradient clipping 为 41.8/61.2/44.7；仅 projector 为 43.1/61.7/46.4；projector+optimization 为 43.6/62.9/46.6；三者为 43.7/63.1/46.8。作者据此说各阶段有正向贡献；没有误差或独立重复。[p.9，Table 4 与其 caption，explicit/layout_observation]

6. **Figure 3（p.10，§4.4）**：动态权重曲线。分类面板横轴 0–250 epochs，显示 `π_distill`、`π_cls`、`π_kl` 三条权重；检测面板横轴 0–50 epochs，显示 `π_distill` 与 `π_task`。作者明确说检测先偏向 distillation、后逐步转向 task；图是曲线展示，不给数值表或不确定性。[p.10，Figure 3 caption 与 “Dynamic Balancing Strategy and π values”，explicit]

7. **Figure 4（p.10，§4.4）**：分类错误和定位错误的柱状图，比较 Baseline、Token、VKD、Ours。作者说 Ours 两类错误都更少，且 Token/VKD 的分类错误高于 baseline；柱图没有数据标签，不能从 PDF 可靠恢复精确数值。[p.10，Figure 4 caption 与 “Subtask error analysis”，explicit/layout_observation]

8. **Table 5（p.9，§4.4）**：teacher-scale robustness，仅报告 AP。无蒸馏/Token Matching/VKD/DTO-KD 在 ViDT-nano student（teacher small/base）为 40.4/44.8、41.5/41.9、42.2/43.0、43.2/43.7；ViDT-tiny student 为 45.8/46.5、45.9/46.9、46.9/47.4（其中每行按 small/base teacher 两列）。DTO-KD 在四列均为最高列出值。[p.9–10，Table 5，explicit]

9. **速度主张（p.7，§3.1）**：amortized DTO-KD 被说成以 240 epochs 达到 Roy Miles & Deng (2024) 300 epochs 的 top performance，但没有对应指标、曲线或 runtime/FLOP/memory 测量；这是一个单句比较而非统计结果。[p.7，§3.1，explicit/layout_observation]

### 8.2 不利解释与统计边界

- Table 1–3 的“state-of-the-art”严格只能解释为「在作者列出的比较行和设置中最高」；没有跨论文统一训练预算、seed 或显著性检验来证明总体 SOTA。[p.8–9，Tables 1–3，interpretation]
- Figure 1 的 conflict/dominance 曲线是检测任务 500 iterations 的示例，不能直接外推到所有 KD 任务；正文没有给出 across-seed 或 across-task 汇总。[p.2，Figure 1 caption，interpretation]
- Figure 4 只有柱形高度，没有原始数值和误差，结论可以支持方向性排序，但不能支持精确 effect magnitude。[p.10，Figure 4，layout_observation]
- Table 2 的六列确实覆盖 homogeneous 与 heterogeneous CNN，但每列只有一个 Top-1 数；“在两种数据集规模设置中建立新 SOTA”是作者叙述，表格本身不能判断跨 protocol 的可比性。[p.9，Table 2、§4.2，interpretation]

## 9. 消融、负面结果与自我设限

### 9.1 消融清单

- **组件删除**：Table 4 逐步加入 gradient clipping、projector、optimization；从 41.0 AP 上升到 43.7 AP。该消融识别 projector、dynamic optimization 与 clipping 的增量，但没有把 projector 的结构、优化器和 clipping 阈值分别展开。[p.9，Table 4，explicit]
- **动态权重机制**：Figure 3 展示分类三 loss 与检测两 loss 的 `π` 随 epoch 变化；它支持“权重随训练阶段变化”的机制可视化，但不是参数敏感性曲线。[p.10，Figure 3，explicit/interpretation]
- **机制替代/错误分析**：Figure 4 将 detection 错误拆为 classification 与 localization；它提供了结果分解，未构成对 GrC/GrD 的因果替代解释检验。[p.10，Figure 4，interpretation]
- **teacher-scale 鲁棒性**：Table 5 用 ViDT-small 与 ViDT-base teacher 做两种 teacher 对照；范围仍限于 COCO/ViDT 与 AP。[p.9–10，Table 5，explicit]
- **超参数/规模敏感性**：没有 `γ`、`η_π`、projector 数量、clipping threshold、student scale 或训练预算的系统敏感性表/图，状态为 `not_present`。[p.5–10，§3.1、§4.4，layout_observation]
- **计算成本**：正文说 amortization 避免额外 backpropagation，并在结论称 overhead minimal，但没有 wall-clock、FLOP、显存或每样本成本表，状态为 `not_present`。[p.7、p.10，§3.1、§6，layout_observation]

### 9.2 限制与负面信息

- 作者唯一明确的小节限制是数据可用性：DTO-KD 依赖 available data，data-free distillation 尤其是从大型预训练模型蒸馏仍是 open challenge；sample synthesis 可能因 min–max optimization 需要训练数据而更难。[p.10，§5 Limitations，explicit]
- 没有展示失败案例、负 AP、训练发散、teacher 较弱时的失败条件或伦理/部署风险；这些项目在 PDF 中是 `not_present`，不是“没有失败”。[p.1–10，全文，layout_observation]
- 自我设限集中在结尾 p.10，且只覆盖 data-free/data availability；正文没有把 theorem domain conditions、amortized guarantee、统计不确定性或 compute overhead 作为 limitations 明说。[p.6–7、p.10，§3.1、§5–§6，interpretation]

### 9.3 不利信息的呈现位置

只能确认版面策略，不能推断作者动机：

1. **位置延后**：最明确的适用边界仅在 p.10 的 §5，而 ImageNet/CIFAR/COCO 的主结果和“state-of-the-art”叙述位于 p.8–10 之前或同页上方；限制没有在 Abstract 或 Introduction 中出现。[p.1、p.8–10，layout_observation]
2. **聚合粒度有限**：主表按 architecture/task 给单点 Top@1/AP，未提供 seed-level dispersion；这会提高扫读效率，但读者无法从正文判断结果波动。[p.8–10，Tables 1–5，layout_observation]
3. **主动承认**：§5 明确承认 data availability bottleneck，并把 data-free extension 留作 open challenge；这是正文中的主动限制陈述。[p.10，§5，explicit]

## 10. 结论与闭环矩阵

### 10.1 Conclusion 段落编码

Conclusion 只有一段，按「重述方法 → 机制回收 → 结果回收 → 影响/部署」推进，没有新数字；它把 DTO-KD 称为 transformer-based KD 的 principled solution，回收稳定/高效训练与超越 non-distilled counterpart，最后称 overhead minimal、适合 real-world deployment。[p.10，§6，explicit "minimal computational overhead" and "practical for real-world deployment"]

### 10.2 主张闭环

| 引言主张 | 方法回应 | 证据回应 | 结论回应 | 状态 |
|---|---|---|---|---|
| 固定 loss weight 难以跟随两目标 | 式 (6)–(9) 的相对改善率与 simplex MOO | Figure 3、Tables 1–3 | dynamic balancing 回收 | `partially_closed`：amortized 更新引入新学习率，且精确/近似关系未闭合。[p.5–7、p.10] |
| GrC 会让更新方向相互破坏 | 内积负的形式化与最小范数组合 | Figure 1（仅 detection、500 iterations） | “mitigates supervision conflicts” | `partially_closed`：诊断图有对应，但没有跨任务统计或反事实梯度检验。[p.2、p.4–6、p.10] |
| GrD 使一个目标支配另一个 | Corollary 3.3 的 equal contribution | Figure 1 dominance 曲线、Figure 3 权重曲线 | “gradient imbalances” 回收 | `partially_closed`：等贡献和 dominance score 的实验关系未严格对应，且边界条件缺失。[p.2、p.6、p.10] |
| 闭式解给出 Pareto-optimal / convergence | Theorem 3.1、引用 Liu et al. (2023) | 没有独立 convergence/pareto 实验 | 结论称 stable/effective | `partially_closed`：没有本文 proof，式 (17) 及 simplex interior 条件未给，近似版 guarantee 未证明。[p.5–7、p.10] |
| 两任务达到 SOTA | Algorithm 1 与 ImageNet/COCO settings | Tables 1–3、Table 2 CIFAR | “consistently achieves state-of-the-art” | `partially_closed`：在列出基线中最高，但统计与统一 protocol 边界不足。[p.8–9、p.10] |
| 组件贡献与鲁棒性 | projector/optimization/clipping 组件 | Table 4、Figure 3、Table 5 | “robustness/adaptability” | `partially_closed`：有局部消融和两种 teacher，但没有敏感性、失败案例或更广泛 teacher/task。[p.9–10] |
| 更快收敛、计算开销小 | amortized π 更新 | 240 vs 300 epochs 单句；无 runtime/FLOP | “minimal overhead” | `open`：epoch 计数不等于 wall-clock/compute cost，结论的 overhead claim 没有量化证据。[p.7、p.10] |
| 学生超过非蒸馏学生 | teacher signal + dynamic trade-off | Table 1 的 Ti/S 与 Table 3 各 student 对 scratch baseline | Abstract/Conclusion 回收 | `partially_closed`：表内比较支持方向，但范围限于列出架构/任务，未证明普遍性。[p.1、p.8–9、p.10] |
| 可推广到 data-free KD | 方法使用 available data | 无 data-free 实验 | §5 说明 open challenge | `open`（作者也明确如此）：适用边界由数据可用性限制。[p.10，§5] |

## 11. Appendix / supplementary 职责

PDF 没有 appendix 或 supplementary（p.10 之后直接进入 p.11 References，p.13 结束）；因此 appendix 页数为 0，未提供 proof、classification/detection loss 的具体定义、hyperparameters、dataset detail、额外结果、robustness 或 reproducibility artifact。[p.4、p.10–13，§3 Problem formulation；references，layout_observation]

这造成一个明确的正文自足性问题：§3 说分类和检测的具体 `L_distill`/`L_task` 将在 appendix 定义，但文件中找不到该 appendix；读者只能从 Algorithm 1 的 `DistillHead`/`TaskHead` 和实验任务名知道接口，无法据本文复原各任务 loss。[p.4，§3 Problem formulation，explicit “define these more specifically … in the appendix”]

正文保留了决策所需的主表、核心算法、图和最小 optimizer 设置；被移出的内容在当前文件中没有可定位的 appendix 章节，原文只是作出「应在 appendix 出现」的承诺。故 appendix 迁移状态为 `not_present`，不能视为已完成的 extended method/implementation detail。[p.4、p.7–10，interpretation]

## 12. 用词与修辞

以下观察排除 references、表格数值和公式碎片，按正文语境归纳，不替代项目统一 lexical 脚本：

- 高频领域词围绕 `knowledge distillation`、`student/teacher`、`task/distillation loss`、`gradient`、`trade-off`、`optimization`、`classification`、`detection`、`objective`、`alignment`、`performance`。[p.1–10，全文，layout_observation]
- 高频二元概念是 `gradient conflict`、`gradient dominance`、`dynamic trade-off`、`multi-objective optimization`、`task-specific`、`state-of-the-art`；它们既是领域术语，也直接承担标题、问题和贡献动作。[p.1–7，Abstract、§1、§3，layout_observation]
- 主张动词以 `propose`、`resolve`、`ensure`、`demonstrate`、`outperforms`、`achieves`、`highlights` 为主，强动词集中在 Abstract、贡献列表、Results 和 Conclusion；限定词主要是 `largely`、`often`、`typically`、`particularly`、`nearly`、`minimal`。[p.1–3、p.8–10，layout_observation]
- `we evaluate`、`we conduct`、`we introduce`、`we propose` 结构把动作主体固定为作者；“significant improvements”“superior”“new SOTA”“consistently”频繁出现，但没有配套显著性检验或不确定性。[p.2–3、p.8–10，interpretation]
- 修辞强度从 Abstract 的 “principled/resolve/state-of-the-art” 延续到 Conclusion 的 “new standard/minimal overhead/practical deployment”；正文对数据可用性的限制只出现一次 §5，未对理论 domain conditions 做同等强度限定。[p.1、p.10，explicit/interpretation]

## 13. 最终判断

1. **单一主线**：把 KD 从固定标量加权改写成共享参数上的二目标梯度优化，用相对改善率、simplex 最小范数和动态 `π` 处理 GrC/GrD；Figure 1 是问题诊断，式 (9)–(15) 是机制，Tables 1–5 是任务结果。[p.2、p.4–9，explicit/interpretation]
2. **正文保留的决策关键内容**：问题定义、GrC/GrD 形式化、Pareto/MOO 转换、闭式权重、Algorithm 1、amortized 近似、ImageNet/CIFAR/COCO 点结果、组件消融和 teacher-scale 对照。[p.4–10，layout_observation]
3. **移入附录的细节与损害**：作者预告具体分类/检测 loss 在 appendix，但本文件无 appendix；因此正文对 `DistillHead`、`TaskHead`、projector 和数据集 protocol 的复现自足性不足。[p.4、p.7–10，explicit/interpretation]
4. **最有效的写作/图/表模式**：Figure 2 将 teacher/student、projector、loss head、两阶段优化放进一张流程图；Algorithm 1 随后把图转成可执行步骤；Table 1–3 按任务给紧凑横向比较，Table 4 再做组件增量，形成「机制→主结果→消融」顺序。[p.4、p.7–9，layout_observation]
5. **最大叙事缺口**：理论部分把 unconstrained 二目标解、simplex 可行性、alignment、norm bounds 和 Pareto convergence 以近似普遍语气陈述，但没有 domain conditions、proof 或对 amortized 版本的 guarantee；实验又缺少 seed、误差、完整 loss 定义和 compute cost，因此“state-of-the-art/稳定/低开销”只能在列出设置内部分闭合。[p.5–10，interpretation]
6. **可迁移规则**：任何动态多目标优化论文都应同时给出权重可行域的边界处理、退化梯度条件、精确算法与近似算法的差异，并为每个理论预测配独立且可重复的机制证据；否则闭式公式与漂亮的主表不能构成完整因果闭环。[p.5–7，interpretation]
7. **规则边界**：该规则适用于共享参数且目标梯度可直接比较的多目标训练；本文只在视觉 KD、available-data、ImageNet/CIFAR/COCO 和 ViDT/DeiT/RegNetY 设置中提供证据，不能外推到 data-free KD、其他模态、任意 teacher/student 或部署成本。[p.7–10，§4–§6，interpretation]

## 14. 证据覆盖与缺失值

- 已对正文、图、表、Algorithm 1、式 (1)–(18) 及 references 逐页阅读；没有把 title、abstract、review 或自动指标当作正文证据。
- 实质判断均附物理页码、章节和短锚点；缺少的 appendix、supplementary、seed、误差、显著性、代码链接、失败案例和 compute profiling 明确记为 `not_present`，没有从常识补写。
- 本读没有发现需要与自动测量草稿冲突的项目；`measurement_disagreements` 保持空数组。

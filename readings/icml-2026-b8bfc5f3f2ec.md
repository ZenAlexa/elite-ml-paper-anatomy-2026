# AI Engram

`paper_id`: `icml-2026-b8bfc5f3f2ec`

`题目`

AI Engram: In Search of Memory Traces in Artificial Intelligence

`来源`

已核验的 arXiv 预印本 `2606.14997v1`；PDF 共 26 个物理页；未提供独立 supplementary。所有页码均指 PDF 物理页。

## 文档边界和页级地图

研究正文从 PDF p.1 的摘要和第 1 节开始，到 p.9 的第 8 节结束。p.10 上半为 Impact Statement 与 Acknowledgment，下半开始 References；references 延至 p.12。Appendix 从 p.13 的 Appendix A 开始，到 p.26 的 Appendix H 结束。PDF 全文采用双栏 letter 版式；跨栏图、表和整页热图承担了较多论证面积。

| PDF 页码 | 章节或材料 | 语义模块 | 估计词数 | 版面与职责 |
|---|---|---:|---:|---|
| 1 | Title、Abstract、1 Introduction 起始 | abstract / introduction | 148 / 约 260 | 摘要置于左上；Fig. 1 占右上，随后双栏引言。 |
| 1–2 | 1 Introduction | introduction | 约 650 | p.2 顶部以三项贡献列表收束。 |
| 2 | 2 Related Work | related_work | 约 420 | 两个问题簇接入 selective manipulation 与 parameter decomposition。 |
| 2–3 | 3 Defining Learning and Memory、3.1 | method | 约 500 | 定义 system、experience、concept 与 inverse problem。 |
| 3–5 | 4 AI Engrams in Deep Neural Networks、4.1–4.6 | method | 约 1,440 | Table 1、Fig. 2、Fig. 3 与 Eq. (1)–(7) 构成主推导。 |
| 5–6 | 5 Experimental Validation、5.1–5.3 | experimental_design / results | 约 790 | Fig. 4–6 与 Table 2 给出视觉模型验证。 |
| 6–8 | 6 Geometric Analysis of Engram、6.1–6.3 | theory | 约 850 | Fig. 7–8 夹在理论展开中；Eq. (9)–(10)、Theorem 6.1、Corollary 6.3 位于此段。 |
| 8–9 | 7 In Search of Memory Trace in LLM | results | 约 610 | Table 3、Fig. 9、Table 4 将方法放入 TOFU 的计算–精度取舍。 |
| 9 | 8 Conclusion | conclusion | 约 230 | 回收 closed-form、Fisher-KFAC 与 LLM localization。 |
| 10 | Impact Statement、Acknowledgment | other | 约 150 | 伦理治理提示后转入文献。 |
| 10–12 | References | other | 约 1,520 | p.12 仅余末尾文献，留有大片空白。 |
| 13–14 | Appendix A Derivation | appendix | 约 1,140 | 完整 KKT、pseudoinverse 与 tabula-rasa 推导。 |
| 14–16 | Appendix B Experimental Details | appendix | 约 1,470 | 资源、模型、datasets、公式、grid 与评估流程。 |
| 16–20 | Appendix C Surgical Validation | appendix | 约 1,010 | Fig. 10–15；p.17、p.18、p.20 各以单幅近跨栏图为主。 |
| 21 | Appendix D Operator-Theoretic Formalism | appendix | 约 390 | Fig. 16、Eq. (24)–(25) 全局 block-diagonal 表述。 |
| 21–24 | Appendix E LLM Unlearning Setup | appendix | 约 2,050 | TOFU 任务、metric definitions、compute、closed-form comparisons 与 layer ablation。 |
| 24–25 | Appendix F Compositional Memory States | appendix | 约 590 | Fig. 17–18 将状态空间作概念化展示。 |
| 25–26 | Appendix G Tabula Rasa | appendix | 约 900 | Eq. (32)、Table 9 解释 single-pass 的结构条件。 |
| 26 | Appendix H Limitations | appendix / limitations | 约 590 | 四项限制集中于右栏。 |

以 p.1–p.9 约 5,800 个抽取词的粗分母，abstract、introduction、related work、method、experimental design、theory、results、conclusion 的估计占比分别约为 3%、11%、7%、34%、14%、15%、11%、4%。页内跨栏图表挤压最多的是 p.5、p.6、p.8 和 p.9；p.17、p.18、p.20 反向采用大面积留白来放大单个热图或样例网格。

## 摘要的逐句编码

1. **24 词**。`object_scope`、`problem_gap`。用 `yet` 把「memory formation」与 DNN 中可识别 memory trace 的开放问题相接；无数字，限定为 `whether` 与 `remains an open question`。（PDF p.1, Abstract, anchor: “remains an open question”, explicit）
2. **27 词**。`core_idea`、`method`。把 specificity、reactivation、sufficiency、necessity 翻译为 constrained inverse problem。（PDF p.1, Abstract, anchor: “constrained inverse problem”, explicit）
3. **30 词**。`method`、`theory`。声称 closed-form estimator 从 globally entangled parameters 中分离 trace，并给出 natural-gradient correspondence。（PDF p.1, Abstract, anchor: “natural gradient update”, explicit）
4. **23 词**。`qualitative_result`、`impact_claim`。以 linear arithmetic、without iterative optimization 说明 compose/erase 的操作性主张。（PDF p.1, Abstract, anchor: “composed or erased”, explicit）
5. **17 词**。`experimental_setup`、`qualitative_result`。覆盖 simple MLP 到 LLM，报告 causal validity 与 scalability；无可核查数字。（PDF p.1, Abstract, anchor: “simple MLPs to LLMs”, explicit）
6. **27 词**。`impact_claim`。把结果提升到 biological memory 与 artificial representation learning 的桥接及 distributed storage 的解释。（PDF p.1, Abstract, anchor: “functional specificity”, explicit）

功能顺序为问题缺口 → 生物准则的形式化 → estimator 与 theory → 可操作性 → 跨模型验证 → 学科影响。摘要报告的是定性实验结论，没有表格数字、统计检验或限制；最强能力主张置于第 4–5 句，收尾转向理论与领域意义。

## 引言的论证推进

| 段落 | 主要动作 | 约占引言词数 | 留下的问题与下一钩子 | 证据 |
|---|---|---:|---|---|
| 1 | `context` | 约 27% | 记忆是 intelligence 的结构表征；追问该结构能否成为模型内可定位的实体。 | p.1, §1, “concrete, identifiable structures”, explicit |
| 2 | `problem` / `failure_of_prior_work` | 约 23% | 参数同时参与多种行为，distributed、entangled representations 阻碍 physical trace 定位。 | p.1, §1, “inherently distributed and entangled”, explicit |
| 3 | `missing_insight` / `core_idea` / `method_preview` | 约 22% | 用四个 neuroscience criteria 约束 inverse problem，承诺从 trained weights 与 activation statistics 恢复 trace。 | p.1, §1, “unique optimal substrate”, explicit |
| 4 | `theory_preview` | 约 8% | 生物约束导向 Fisher metric 下的 minimum-norm projection，预告 information-geometric 解释。 | p.1–2, §1, “minimum-norm projection”, explicit |
| 5 | `contribution_list` | 约 20% | 三条条目依次给出 scalable estimator、amortized isolation、Fisher/natural-gradient link。 | p.2, §1, “main contributions”, explicit |

推进链是 **记忆的功能地位 → 参数纠缠的定位障碍 → 四项可检验准则 → closed-form 解 → 三项贡献**。贡献列表重复了摘要的 estimator、linear arithmetic 与 Fisher link，但补入 single forward pass、unique subcomponents、MLP 至 billion-parameter LLM 的范围。三项贡献含有可证伪内容：Eq. (4) 的估计式、Fig. 4–6 与 Table 2 的 surgical behavior、Section 6 的等价条件；列表本身没有报告具体数值，也没有列出限制。

## 相关工作如何定位

相关工作是独立第 2 节，位于引言后、方法前，约占正文非表格词数 8%。它形成两个引用簇。

| 段落 | 编码 | 比较维度与论证作用 | 证据 |
|---|---|---|---|
| Selective knowledge manipulation | `taxonomy`、`credit_or_foundation`、`nearest_neighbor_contrast` | 将 machine unlearning、model editing、UCE 放在「targeted intervention」簇；以 covariance 与 closed-form 的共同点引出其 neuroscience constraints 的差异。 | p.2, §2, “differs fundamentally”, explicit |
| Network decomposition | `taxonomy`、`limitation_of_prior` | 对比 activation-space sparse autoencoders 与 parameter-space masks，指出前者没有 parameter functional decomposition。 | p.2, §2, “do not yield a functional decomposition”, explicit |
| Linear parameter decomposition | `nearest_neighbor_contrast`、`limitation_of_prior`、`gap_creation` | APD 的 gradient attribution 与 hyperparameter sensitivity、SPD 的 learnable rank-one subcomponents，承接到 unique、single-forward-pass decomposition。 | p.2, §2, “non-unique subcomponents”, explicit |

该节避免复讲自己的公式，只按 intervention target、representation location、optimization cost 和 uniqueness 做比较。文献在后文继续承担论证作用：UCE/Task Arithmetic 出现在 Table 4 和 Appendix E.5，K-FAC 支撑 Theorem 6.1，TOFU/OpenUnlearning 规定 LLM protocol，MEMIT/ROME 支撑 Appendix G 的 sequential-dependency 对照。

## 方法和理论链

### 形式化对象与方法动作

| 单元 | 首次位置 | 解决的前文问题 | 主要动作与输出 |
|---|---|---|---|
| system / experience | p.2, Def. 3.1 | 将「记忆」从抽象词变成 mutable `μ` 与 immutable `π` 的状态变化 | `setup_notation`；`f=(μ,π)`、`μ0`、`μ1`。 |
| concept partition | p.2–3, Def. 3.2 | 指定何为目标知识与应保留知识 | `setup_notation`；`X+` 是 gain-of-function target，`X−` 是 reference。 |
| inverse problem | p.3, §3.1 | 将分布式更新写成一个可分离对象 | `state_problem`、`give_intuition`；specificity、reactivation、sufficiency、necessity。 |
| layer-wise synaptic engram | p.3, §4.1 | 将全模型 trace 拆为每层 `W+(l)` | `define_component`；Eq. (1)。 |
| Z-space constraints | p.3, §4.2–4.3 | 固定 nonlinear activation 后，改以 pre-activation `Z=WX` 比较 intervened state | `setup_notation`、`state_problem`；Table 1。 |
| constrained objective | p.4, §4.4 | 同时重构 `X+`、在 `X−` 上保持 inert | `derive`；Eq. (2)、Proposition 4.1、Eq. (3)。 |
| retrospective estimator | p.4, §4.5 | 消除未知 training trajectory 对逐层提取的阻塞 | `instantiate_algorithm`、`state_complexity`；Eq. (4)、one forward pass、`O(d²)` statistics。 |
| global and multi-concept operations | p.4–5, §4.5–4.6 | 将局部解连接到多个可选 erase/composition 目标 | `connect_to_prediction`、`connect_to_experiment`；Eq. (5)–(7)。 |

段落动作序列为 `setup_notation → state_problem → define_component → explain_mechanism → derive → instantiate_algorithm → state_complexity → connect_to_prediction → connect_to_experiment`。没有 pseudocode 或 Algorithm 环境；正文用 covariance accumulation、pseudoinverse、layer-wise application 解释到可实现的粒度，batching、SVD threshold、模型配置与 grid 被置入 Appendix B。

### 公式、理论结果与证明责任

物理版面可辨识 32 个编号 displayed equations，编号从 Eq. (1) 到 Eq. (32)。另有约 17 个未编号 display expressions，例如 Fisher distance、trace identity、CIFAR baseline losses 和 tabula-rasa state equations。主文有 10 个编号式，附录有 22 个；自动计量的 19 个编号式少计了附录连续推导与 LLM metric equations。

| 结果 | 前提 | 结论 | 证明位置与实证对应 |
|---|---|---|---|
| Proposition 4.1 Spectral AI Engram Estimator | 对 `W+X−=0` 施加 strict specificity；`Σ+`、`Σ−` 为 uncentered covariance | `W+ = ΔW Σ+ (Σ+ + Σ−)†` 是 minimum-norm closed-form solution。 | p.4 proof sketch；完整 KKT 在 Appendix A p.13；Fig. 4–6、Table 2 用 surgery/unlearning 对应。 |
| Theorem 6.1 Fisher-Engram Equivalence | K-FAC 的 layer factorization 与 isotropic output curvature `Gl≈σ²I` | Eq. (10) 的 Engram objective 等价于 Fisher metric 下 constraint manifold 的 minimum-norm projection。 | p.7–8 proof；没有单独的 Fisher-assumption falsification experiment。 |
| Corollary 6.3 Natural Gradient Interpretation | 同一 K-FAC、isotropic-curvature 条件与 forgetting loss | `W−W+` 对应 unit-step natural-gradient descent。 | p.8 proof；Table 2、3 仅测试编辑行为，未直接测量 natural-gradient trajectory。 |
| Proposition A.1 Engram Identification Objective | target reconstruction 与 reference null-space constraint | Eq. (11)–(12) 直接映射 reactivation 与 specificity。 | Appendix A p.13；为 Proposition 4.1 的完整起点。 |

理论在文章的核心因果链中承担 estimator 的由来与 single-pass 条件。Theorem 6.1 与 Corollary 6.3 同时提供解释性保证；它们明确依赖 K-FAC 和 isotropic curvature，正文也在 Remark 6.2 说明 Eq. (4) 的 empirical estimator 不调用该假设。（PDF p.8, §6.2, anchor: “does not invoke this assumption”, explicit）

## 实验设计与复现粒度

| 设计事实 | 论文提供的内容 | 证据 |
|---|---|---|
| 研究问题顺序 | §5 明列三类验证：architecture/dataset versatility、与 unlearning baselines 的 quantitative comparison、qualitative arithmetic；§7 再测 Llama-3.2-1B。 | p.5, §5, “three experiments”, explicit |
| 视觉分类 | CIFAR-10/100 上 ResNet-18/50；forget target 为 Class 0；`X+` 为该类训练样本，`X−` 为其他类。 | p.5, §5.2；p.15, §B.4.1, explicit |
| 生成与 attribute 编辑 | MNIST 3-layer ConvAE、CelebA DCGAN-based WAE、ImageNet-1K ViT-B/16；Appendix B 给出 architecture、loss、epochs、preprocessing 与提取层。 | p.14, §B.2, explicit |
| LLM protocol | Llama-3.2-1B-Instruct，TOFU forget10；全参数 fine-tune 后比较 GradDiff、IdkNLL/DPO、UNDIAL、RMU、NPO、SimNPO、AltPO。 | p.21, §E.1, explicit |
| extraction implementation | 单次 forward pass 累积 `Σ+` 与 `Σ−`，batch size 128；SVD pseudoinverse，threshold `10−6×λmax`。 | p.14–15, §B.3, explicit |
| compute | 全部 Engram extraction 在一张 NVIDIA A100 80GB 上执行；CIFAR-100 ResNet-18 的 100 类 engrams 少于两分钟。 | p.14, §B.1, explicit |
| controls | CIFAR 的 retrain reference 使用对应 seeds；hyperparameter selection 后每种方法运行 5 个 random seeds。 | p.16, §B.4.1, “5 different random seeds”, explicit |
| selection | CIFAR baseline 和 `αbest` 以最大 Tug-of-War (ToW) 的 grid 选择；CIFAR-10/CIFAR-100 的 `αbest` 分别为 0.6/1.6。 | p.15, §B.4.1, explicit |
| reproducibility boundary | code URL 在 p.2；模型 Hub source、dataset split、部分 hyperparameters 位于 Appendix B/E。LLM 结果的 seed count、raw per-seed values、CIFAR 和 LLM tables 的 interval estimates 未呈现。 | p.2, §1；p.14–16, Appendix B；p.21–23, Appendix E, explicit/layout_observation |

实验顺序与引言相符：先展示可隔离性和 architecture range，再以 CIFAR quantitative comparison 支撑 unlearning claim，接着以 Fig. 7–8 展示 arithmetic，最后将 scalability/compute story 延至 LLM。Fisher 的条件性预测没有对应的直接 ablation；语义重叠的 soft-projection prediction 在 Appendix C.4 获得专门检验。

## 图表、算法和统计证据

### 视觉清单

| 项目 | 页码 | 模块 | 一句话任务与编码 |
|---|---:|---|---|
| Fig. 1 | 1 | introduction | 四项 engram criteria 的状态干预图；以 target/reference、injection/ablation 区分 causal tests。 |
| Table 1 | 3 | method | 将 observed/intervened states 映射为 specificity、reactivation、sufficiency、necessity constraints。 |
| Fig. 2 | 4 | method | `W+ = WP+` 的 covariance surgical filter 流程。 |
| Fig. 3 | 5 | method | n 个 engrams 的 additive subspace 与 `2ⁿ−1` active states。 |
| Fig. 4 | 5 | results | CIFAR-10 ResNet-18 class-by-class heatmap；白色 diagonal 是 target accuracy drop，off-diagonal 表示 retain accuracy。 |
| Fig. 5 | 6 | results | ConvAE MNIST 样例与 target-specific test-MSE increase。 |
| Table 2 | 6 | results | CIFAR-10/100 的 ToW、DA、NMI point estimates 和相对 retrain gap。 |
| Fig. 6 | 6 | results | CKA scatter；x 轴 original similarity，y 轴 retrained similarity，理想区域是 top-left。 |
| Fig. 7 | 7 | results | CelebA WAE 的 attribute slider，编码 `μ−αμ+c` 的连续强度。 |
| Fig. 8 | 7 | results | Glasses/Goatee engram 的加减向量与重建样例。 |
| Table 3 | 8 | results | Llama-3.2-1B/TOFU 的 Memorization、Utility、Privacy、EM、FQ。 |
| Fig. 9 | 9 | results | Llama layer/projection heatmap，色彩为 relative `W-Norm`。 |
| Table 4 | 9 | results | TOFU 上 Engram、UCE、Task Arithmetic 的 closed-form comparison。 |
| Table 5 | 15 | appendix | CIFAR baselines 与 Engram 的 hyperparameter search spaces。 |
| Fig. 10 | 16 | appendix | CIFAR-100 的 CKA original/retrained scatter。 |
| Fig. 11 | 16 | appendix | MNIST 3-layer MLP 的 class-wise surgical heatmap。 |
| Fig. 12 | 17 | appendix | ImageNet-1K ViT 的 20-class grouped unlearning heatmap。 |
| Fig. 13 | 18 | appendix | CIFAR-100 ResNet-18 的 100-class heatmap。 |
| Fig. 14 | 19 | appendix | semantic overlap 下 accuracy-drop bar 与 cosine-similarity curve。 |
| Fig. 15 | 20 | appendix | CelebA 四属性、七个 `α` 值的 sample grid。 |
| Fig. 16 | 21 | appendix | global block-diagonal Engram operator。 |
| Table 6 | 22 | appendix | TOFU 14 个子指标及 harmonic-mean aggregate。 |
| Table 7 | 23 | appendix | 1B TOFU 的 FLOPs、memory、wall-time comparison。 |
| Table 8 | 24 | appendix | Q/K/Gate layer-type ablation。 |
| Fig. 17 | 24 | appendix | knowledge vacuum、A、B、AB 的 compositional-state 示意。 |
| Fig. 18 | 25 | appendix | n-concept hypercube 的 `2ⁿ` state space。 |
| Table 9 | 26 | appendix | naive fine-tuning delta 与 tabula-rasa instantiation 的对照。 |

未出现 Algorithm 环境或伪代码。主文四张表和九幅图中，Fig. 4、Fig. 6、Table 2–4 是决策性证据；Fig. 7–8 是 qualitative demonstration。附录追加九幅图、五张表，分别承担规模、鲁棒性、compute、layer ablation 与限制的证据责任。

### 主要结果和统计处理

| 主张 | 定量或证据对象 | 比较与统计处理 | 不利解释及论文处理 |
|---|---|---|---|
| class-specific ablation 在 CIFAR-10 保留非目标类别 | Fig. 4 的 diagonal drop 与 off-diagonal stability | 单一 class-by-class accuracy heatmap；caption 未给 interval。 | heatmap 没有显示 run-to-run variation；Appendix B 说明选择后用 5 seeds。 |
| ConvAE 可选择性损伤 target morphology | Fig. 5 的重建样例与 test MSE | target vs reference 的 qualitative samples 与 MSE bar。 | 无数值表、无 uncertainty；视觉案例补充为 appendix Fig. 15 的多属性网格。 |
| Engram 在 CIFAR class-wise unlearning 的 ToW 接近 retrain | CIFAR-10 `0.984`、CIFAR-100 `0.983` 的 `αbest` ToW | Table 2 报 ToW、DA、NMI point estimates；括号为同 retrain 的 gap。 | `αbest` 按 ToW grid 选择；同表也暴露 DA/NMI trade-offs。 |
| internal representation 接近 retrained state | Fig. 6 的 top-left CKA positioning | original/retrained CKA scatter；retrain-to-retrain 低于 1 的 seed note 在 Appendix B。 | 图形未显示 statistical interval；p.16 解释 reference model 也受 stochasticity 影响。 |
| linear arithmetic 支持连续和双向 semantic editing | Fig. 7、Fig. 8、Eq. (8) | WAE sample grids，未给 pixel-level summary statistic。 | 证据针对所示 attributes；Appendix C.5 给更多属性和 `α` trajectory。 |
| Fisher/natural-gradient link | Theorem 6.1、Corollary 6.3、Eq. (9)–(10) | 条件性代数推导，非样本统计。 | K-FAC 与 isotropic curvature 假设在 Remark 6.2 明示。 |
| LLM uniform α 强力抑制 exact memorization | Table 3 的 Engram `α=0.6`：EM `0.0069`、Mem. `0.9176`、Util. `0.8801`、Priv. `0.4832` | TOFU normalized point metrics；FQ 是 KS-test p-value 的 `log10` 变换。 | p.8–9 承认 Overall/Privacy 与 iterative methods 有差距。 |
| adaptive `αW-Norm` 改善 LLM balance | Table 3 的 Mem. `0.9627`、Util. `0.9256`、Priv. `0.6453`、EM `0.0276` | per-layer norm ratio rescaled to `[0,1]`；无 LLM seed count 或 interval。 | Table 6 分解 14 个子指标，显示 privacy 没有与 retain model 等同。 |
| Engram 优于两个 closed-form baselines | Table 4 的 Overall `0.818`、Mem. `0.963`、Util. `0.926`、Priv. `0.645`、EM `0.028` | Engram vs UCE/Task Arithmetic，在同一 layer set 与 best-over-sweep configuration 下比较。 | 表中 utility `0.926` 低于 UCE `0.951`；p.9 将其置入 compute–accuracy frontier。 |
| memory footprint 主要在 Q/K/Gate | Fig. 9 与 Table 8；Q/K+Gate Overall `0.819`，No Q/K/Gate `0.238` | layer-type component ablation，TOFU forget10 point scores。 | 仅 Llama-3.2-1B/TOFU；Appendix H 将更大层 covariance storage 列为限制。 |
| semantic overlap 带来连续而有限 interference | Appendix Fig. 14：same-superclass mean drop `0.80` percentage points；different-superclass near zero | 按 superclass 分组，并用 class-conditional input-representation cosine similarity。 | 设计局限于 CIFAR-100 的两级 taxonomy；作者把结果解释为 soft projection。 |
| single-pass 的 tabula-rasa choice 有实证后果 | Table 9：Overall `0.818→0.446`，EM `0.028→0.617` | TOFU forget10 中 naive delta substitution vs tabula rasa。 | 论文明确说 rigorous delta 需要 sequential `V*` optimization，本文没有实现该 alternative。 |

CIFAR 的聚合单位是目标类、retain set 与 full test set 相对于 retrained model 的 accuracy difference；ToW 是三项 `(1-da)` 的乘积。DA 与 NMI 提供 representation-level 读数，CKA 比较 unlearned、original、retrained representation。LLM 的 Memorization、Utility、Privacy scores 使用 safe harmonic mean；Privacy 来自四个 MIA AUC 的 indistinguishability score，FQ 使用 KS test。主表报告 point values；除 FQ 的 KS test 外，未报告 hypothesis-test decision、multiple-comparison control、effect-size interval 或 conventional confidence interval。

## 消融、负面结果和自我设限

主文没有独立的 ablation section，主文消融版面占比约为 0%。与识别目标直接相关的组件和边界检验位于附录。

| 类型 | 证据与识别目标 | 位置 |
|---|---|---|
| 组件删除 | Table 8 依次保留 all projections、Q/K、Q/K+Gate，或排除 Q/K/Gate，以测试 W-Norm localization 是否具有 causal sufficiency。 | p.24, §E.6 |
| hyperparameter sensitivity | Table 5 给出 α、LR、epochs、sparsity 的 search spaces；Table 2 使用 maximize-ToW 的 `αbest`。 | p.15, §B.4.1 |
| task heterogeneity / scale | Fig. 11–13 覆盖 MNIST、CIFAR-100、ImageNet-1K；Fig. 14 将 CIFAR-100 分为 same/different superclass。 | p.16–19, §C |
| mechanism alternative | Table 9 表明把 fine-tuning delta 直接代入会累积 cross-layer error。 | p.25–26, §G |
| compute cost | Table 7 估算 Engram `2.5 PFLOPs`、`10.9 GB`、约 2 分钟，对比 gradient-based `74.4 PFLOPs`、约 `24.8 GB`、10–60 分钟。 | p.23, §E.4 |

不利信息的呈现有可核查的三种方式。第一，主文 p.9 直接写出 Engram 在 Overall 与 Privacy 上落后 AltPO、NPO、SimNPO，并以 compute–accuracy frontier 解释适用情境。（PDF p.9, §7, anchor: “still trails dedicated iterative methods”, explicit）第二，完整 metric definitions、hyperparameter search、layer ablation 和 Table 9 被迁移到 Appendix B/E/G；主文以 `See Appendix` 调用它们。（PDF p.5–9, §§4–7, layout_observation）第三，Table 2 选择最大 ToW 的 `αbest`，而 Table 2 本身保留 DA/NMI 的不一致，Table 6 再展开 LLM 子指标。（PDF p.15, §B.4.1; p.22, Table 6, explicit）这些都是版面和选择事实，不能单独推导作者意图。

限制出现的位置和编码如下。

- `generality`：functional identification 指向 converged manifold 的 component，未重建 concept 在 learning trajectory 中的实际 perturbation。（p.26, §H, “not reconstructions”, explicit）
- `data`：需要显式构造 `X+` 和 `X−`，依赖 human labeling 或 domain knowledge。（p.26, §H, “requires explicit construction”, explicit）
- `deployment` / `causality`：方法是 retrospective-only，不能直接 online tracking 或 streaming/incremental learning。（p.26, §H, “Retrospective-Only Estimation”, explicit）
- `compute`：`d×d` covariance 在 8B–70B scale 可能很大；作者提出 truncated SVD 或 Q/K/Gate restriction。（p.26, §H, “Covariance Matrix Storage at Scale”, explicit）
- `compute` / `baseline`：主文承认 iterative unlearning 的 Overall/Privacy 更高，并把自身定位为 gradient-free operating point。（p.9, §7, “distinct operating point”, explicit）

## 结论和闭环

结论三段依次重述 inverse-problem framework、Fisher-KFAC link、LLM localization、deterministic spectral resolution 和 future directions。没有引入新的数字；关键边界没有放在第 8 节，而是放在 Appendix H。

| 引言主张 | 方法或理论回应 | 实验证据回应 | 结论回应 | 闭环状态 |
|---|---|---|---|---|
| 四项 neuroscience criteria 可定位 AI engram | Table 1、Eq. (2)–(4)、Proposition 4.1 | Fig. 4–5、Table 2 主要测试 ablation 与 task behavior | p.9 回收 “identifying and manipulating memory traces” | `partially_closed`：四项 criteria 的完整独立测试没有逐项量化展开。 |
| memory 可经 linear arithmetic compose/erase | Eq. (5)–(8)、global projector | Fig. 7–8；Appendix Fig. 15、17–18 | p.9 使用 deterministic spectral resolutions | `partially_closed`：示例支持 scalar/vector edits，未枚举验证全部 `2ⁿ−1` states。 |
| estimator 与 Fisher/natural gradient 相接 | §6、Theorem 6.1、Corollary 6.3 | 无独立 curvature diagnostic | p.9 重述 information geometry | `closed`：作为明示假设下的解析结论闭合。 |
| 方法从 MLP 扩展到 LLM 且 scalable | Eq. (4)、layer-wise parallelization | Fig. 11–13、Table 3–4、Table 7 | p.9 覆盖 MLP、CNN、ViT、1B LLM | `partially_closed`：8B–70B covariance storage 是明示边界。 |
| LLM memory traces 聚于 Q/K/Gate | W-Norm definition 与 global layer decomposition | Fig. 9、Table 8 | p.9 称 condensed localization pattern | `partially_closed`：证据局限于 Llama-3.2-1B/TOFU。 |

## 附录的职责

| 附录模块 | 页码 | 分类 | 正文调用与依赖 |
|---|---:|---|---|
| A Derivation of Closed-form Solution | 13–14 | proof / extended_method | §4.4 明说 full derivation 在 Appendix A；Proposition 4.1 的 KKT、sufficient-statistics 细节依赖此处。 |
| B.1–B.3 Resources、architectures、extraction | 14–15 | reproducibility / implementation_detail | §5 和 §5.2 调用 Appendix B；A100、batch 128、SVD threshold、models/datasets 位于此处。 |
| B.4 CIFAR evaluation protocols | 15–16 | hyperparameter / reproducibility | §5.2 把 detailed metric formulations 指向 B.4.1；ToW、DA、NMI、CKA、five-seed procedure 依赖此处。 |
| C Surgical Validation | 16–20 | additional_result / robustness / qualitative_example | §4.6、§5.1、§5.3 调用 Appendix C；MNIST、ImageNet、CIFAR-100、semantic overlap、CelebA examples 承担扩展范围。 |
| D Operator-Theoretic Formalism | 21 | extended_method | §4.5 指向 Appendix D；global operator 的 formal derivation 在此。 |
| E.1–E.3 LLM setup and metrics | 21–23 | implementation_detail / dataset_detail / reproducibility | §7 指向 Appendix E；TOFU split、baselines、harmonic-mean、MIA、FQ definitions 在此。 |
| E.4–E.6 compute、closed-form baselines、layer ablation | 23–24 | additional_result / ablation / hyperparameter | Table 4 caption、§7 的 compute/frontier 和 localization claims 依赖此处。 |
| F Compositional Memory States Hypothesis | 24–25 | other | §4.6 明指 Appendix F；提供 `2ⁿ` state-space 的概念性扩展。 |
| G Tabula Rasa Instantiation | 25–26 | extended_method / failure_case | §4.5、§7 指向 Appendix G；single-pass 条件和 naive delta failure 依赖此处。 |
| H Limitations | 26 | other | §7 指向 Appendix H；functional-versus-trajectory、concept datasets、retrospective-only、covariance scale 的边界位于此。 |

附录约为研究正文的 1.4 倍。正文保留决定性对象：准则到约束的转换、closed-form equation、CIFAR/LLM 的主结果、Fisher link 与 compute trade-off。推导、protocol、large visual matrices、metric definitions、hyperparameter grids、component ablation 与限制放入附录。正文可理解主方法和主比较，复现实验和判断扩展性时需要附录。

## 用词和修辞

高频领域名词集中在 `memory`、`engram`、`learning`、`representation`、`causal`、`weight`、`state`、`spectral`、`unlearning`。高频短语包括 `AI engram`、`memory trace`、`closed-form estimator`、`linear arithmetic`、`causal substrate`、`Fisher metric`、`natural gradient`、`single forward pass` 与 `parameter manifold`。这些词主要由问题定义、Eq. (1)–(7)、Section 6 和 LLM localization 驱动，模板性语言较少。

主张动词包含 `introduce`、`derive`、`isolate`、`demonstrate`、`confirm`、`enable`、`establish`；限定语常用 `approximately`、`typically`、`under the assumptions`、`can`、`suggest`、`promising`、`moderate`。显式比较词有 `unlike`、`in contrast`、`however`、`rather than`，因果连接词有 `therefore`、`thus`、`crucially`、`consequently`。主文检索得到 `we show` 约 2 次、`we demonstrate` 1 次、`we observe` 约 3 次、`we derive` 约 2 次；其中 Fig. 9 caption 的 `We show` 属于 caption，公式推导里的 `we observe` 不等同于实证发现。`we find` 与 `we propose` 没有明确命中。该计数受双栏 PDF extraction 顺序和 caption 混入影响，汇总器的 token count 应采用原始抽取规则。

强主张来自 `unique`、`precisely`、`surgical`、`fundamental`、`unprecedented efficiency`；弱化来自 `promising performance`、`suggests`、`may examine` 与 Appendix H 的范围限定。强主张密度在 Abstract、贡献列表、§4.4–4.6 与 Conclusion 较高；§7 明确写出 iterative baselines 的 residual gap，Appendix H 再给四项方法边界。

## 最终判断

1. **单一主线。** 将神经科学 engram 的四项标准转写成 target/reference covariance 上的 constrained inverse problem，得到可逐层并行的 spectral projection；该 projection 被用于 post-hoc functional memory isolation 与 linear edit。（PDF p.3–5, §§3–4, explicit）
2. **正文保留的决策关键内容。** Table 1 把生物概念接到可计算约束，Eq. (2)–(4) 给出 estimator，Fig. 4–6 和 Table 2 提供 visual-classification evidence，Section 6 给出 Fisher interpretation，Table 3–4 与 Fig. 9 决定 LLM 的能力–成本定位。（PDF p.3–9, explicit）
3. **附录迁移及其影响。** 证明、protocol、full metric definitions、scale tests、component ablation、compute accounting 和 all explicit limitations 都在附录。主文的论证连续性保持完整；复现、软投影边界和 LLM generality 的判断依赖附录。 （PDF p.13–26, layout_observation）
4. **最有效的写作模式。** Table 1 的 criterion-to-constraint translation 先固定因果语义，Eq. (2) 把语义压缩为目标函数，Eq. (4) 交付可实施 estimator，随后以 heatmap、scatter、table 分别承接 surgical behavior、representation similarity 与 benchmark trade-off。（PDF p.3–6, explicit/layout_observation）
5. **最大未闭合处与读者成本。** “AI engram” 的 functional causal component 与真实 training-trajectory contribution 有明确差别，且四项神经科学标准未被逐项独立、跨任务量化验证。关键范围限制位于最后一页 Appendix H，主文只在 §7 摘要性提及 scope conditions。（PDF p.9, §7; p.26, §H, explicit/layout_observation）
6. **可迁移规则。** 当跨学科概念要承担方法主张时，先把每个概念映射为可观测 intervention condition，再推导最小 objective 与 estimator；每项能力主张随后配一个直接的 behavior-level evidence object。
7. **规则边界。** 这一路线适合已有 target/reference dataset、可取得 trained weights/activations、且 functional intervention 是目标的场景。它不能替代 online memory tracking、无监督 concept discovery 或真实 learning-history attribution。（PDF p.26, §H, explicit）

## 自动测量差异

`preprint_auto_metrics.csv` 将该 PDF 的 provisional `main_end_page` 记为 26、`appendix_start_page` 记为 10，并记为 15 个 figure captions、6 个 table captions、19 个 numbered equations。逐页检查表明：research body 的第 8 节在 p.9 结束，p.10 是 impact/acknowledgment 与 references 的混合页，Appendix A 从 p.13 开始；全 PDF 可识别 Fig. 1–18、Table 1–9、Eq. (1)–(32)，且没有 Algorithm 环境。差异来自自动版面识别未分开 references/appendix，并漏计整页图、附录表和连续编号公式。（PDF p.9–13, p.15–26, layout_observation/interpretation）

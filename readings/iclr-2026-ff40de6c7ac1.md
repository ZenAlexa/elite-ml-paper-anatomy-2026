# `$p\textrm{-less}$ Sampling` 深读备忘

- **论文**：`$p\textrm{-less}$ Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding`
- **会议与等级**：ICLR 2026 Oral
- **paper_id**：`iclr-2026-ff40de6c7ac1`
- **证据记法**：`[p. 物理页, 章节, basis, “短锚点”]`。页码均从 PDF 首页起算；`explicit` 表示作者明示，`layout_observation` 表示版面事实，`interpretation` 表示本文分析。

## 1. 单一主线

论文把温度调整后的完整 token probability distribution 压缩为 collision probability：

\[
L[P_\theta]=\sum_{v\in V}P_\theta(v\mid x_{1:t-1})^2.
\]

该量直接充当逐步 truncation threshold；保留概率不低于阈值的 token，再归一化采样。[p. 4, §3.1, explicit, “sum of squared token probabilities”] 这一设计移除 top-p、min-p、epsilon、eta、mirostat 所需的采样超参数，并随分布集中度和温度变化。[p. 6, §3.5, explicit, “dynamically adjusts with temperature”] 论文随后沿同一中间量组织三类证据：高温 accuracy / win rate、per-token timing 与 generation length、entropy—admitted-token 轨迹。[p. 7, §4.2, explicit, “robust to high temperatures”][p. 30, Table 13, explicit, “Mean Entropy and Admitted Token Count”]

主线的数学部分闭合了**规则定义和候选集边界**；“correct random guess” 对应真实 desirability 的语义仍依赖一项未直接检验的代换：作者把 `Pθ` 作为真实 token distribution 的经验估计。[p. 4, §3.1, explicit, “best empirical estimate of the true token distribution”] 因而，实验可支持输出质量，无法单独验证该 correctness 解释。[p. 4, §3.1, interpretation, “sampling S and correctness T are independent events”]

## 2. 文档边界与页级地图

PDF 共 **44 个物理页**。正文内容出现在 pp. 1–11；Conclusion 于 p. 10 结束，p. 11 顶部为 Reproducibility Statement，随后同页进入 References。[p. 11, References, layout_observation, “REFERENCES”] References 延续到 p. 13；Appendix A 从 p. 14 开始。[p. 14, Appendix A, layout_observation, “A HUMAN EVALUATION”] 因 p. 11 同时承载正文与 references，按“出现页”计数得到 main 11 页、references 3 页、appendix 31 页，三者不可简单相加。

| 区段 | 物理页 | 估计词数 | 语义模块 |
|---|---:|---:|---|
| Abstract | 1 | 212 | `abstract` |
| 1 Introduction | 1–2 | 605 | `introduction` |
| 2 Related Work | 2–3 | 689 | `related_work` |
| 3.1 p-less | 3–4 | 445 | `method` |
| 3.2 p-lessnorm | 4 | 131 | `method` |
| 3.3 Rényi Entropies | 5 | 244 | `theory` |
| 3.4 Intuition | 5–6 | 403 | `method` |
| 3.5 Advantages | 6 | 234 | `method` |
| 4.1 Experimental Setup | 6 | 154 | `experimental_design` |
| 4.2 Reasoning Results | 7–8 | 507 | `results` |
| 4.3 Creative Writing | 8 | 230 | `results` |
| 5 Analysis | 8–10 | 约 1,046 | `results` |
| 6 Conclusion | 10 | 125 | `conclusion` |
| 7 Reproducibility | 11 | 112 | `other` |
| References | 11–13 | 1,085 | `other` |
| Appendix A | 14 | 239 | `appendix` |
| Appendix B | 15–22 | 约 1,514 | `appendix` |
| Appendix C | 20–44 | 约 13,685 | `appendix` |

全文使用单栏 ICLR 版式。正文 pp. 7–10 将全宽结果表、曲线图和解释文字交错排布，决策对象与论证距离较短。[p. 7, Table 1, layout_observation, “AUC of LLama2-7b”] Appendix Tables 5、8、10、12 为小字号高密度矩阵，其中 p. 26 的 Table 8 几乎占满页面。[p. 26, Table 8, layout_observation, “Full results (accuracies and AUCs)”] p. 14 下半页大面积留白；p. 31 几乎完全由 Figures 13–14 占据；pp. 38–42 主要用于逐字 prompt。[p. 31, §C.10, layout_observation, “Histogram of Entropy Distributions”]

附录与含正文内容页的页数比为 **31:11，约 2.82 倍**。Appendix B.6 与 Appendix C.1 在 pp. 20–22 交叠，因为 B.6 的大型 figures 继续浮动，而 C 已开始正文。[p. 20, §C.1, layout_observation, “ADDITIONAL EXPERIMENTAL DETAILS”]

## 3. 摘要逐句功能

| # | 词数 | 功能 | 关键内容 | 限定/比较 | 证据 |
|---:|---:|---|---|---|---|
| 1 | 28 | `object_scope` | sampling-based next-token decoding | 无 | [p. 1, Abstract, explicit, “Obtaining high-quality outputs”] |
| 2 | 33 | `problem_gap` | hyperparameter 对任务与温度敏感 | `can`, `may` | [p. 1, Abstract, explicit, “sensitive to the selection of hyperparameters”] |
| 3 | 29 | `core_idea`, `method` | 完整分布生成动态阈值 | 无 | [p. 1, Abstract, explicit, “dynamically sets a truncation threshold”] |
| 4 | 16 | `core_idea`, `impact_claim` | 无超参数；高温仍产出高质量文本 | `Unlike`, `consistently` | [p. 1, Abstract, explicit, “has no hyperparameters”] |
| 5 | 31 | `theory`, `experimental_setup` | theory perspectives；math、reasoning、writing | `across a range` | [p. 1, Abstract, explicit, “provide theoretical perspectives”] |
| 6 | 23 | `qualitative_result` | quality 胜过现有 sampling，退化更少 | `consistently`, `much less` | [p. 1, Abstract, explicit, “consistently outperforms existing sampling approaches”] |
| 7 | 25 | `qualitative_result`, `impact_claim` | 更低 token time 与更短 generation | `greater`, `lower`, `shorter` | [p. 1, Abstract, explicit, “lower average token sampling times”] |
| 8 | 18 | `experimental_setup`, `qualitative_result` | examples、case studies、diversity | `Finally` | [p. 1, Abstract, explicit, “qualitative examples, case studies”] |
| 9 | 5 | `impact_claim` | code pointer | 无 | [p. 1, Abstract, explicit, “The code is available at §.”] |

功能顺序为 `scope → gap → idea/method → differentiator → theory/setup → quality → efficiency → diagnostics → code`。摘要报告实验结论，却没有数字、分母、不确定性或 failure boundary。理论被称为 “perspectives”，没有定理级保证的摘要表述。[p. 1, Abstract, explicit, “theoretical perspectives”] 最强质量主张置于第 6 句，效率主张随后出现；限制项为零。

摘要末句的 `§` 没有解析到代码链接；p. 11 又写成“upon publication”才公开代码，二者形成文档内不一致。[p. 1, Abstract, explicit, “The code is available at §.”][p. 11, §7, explicit, “will make our source code publicly available”]

## 4. 引言的论证推进

引言只有四个实质段落，推进紧凑：

1. **`problem`，约 147 词，占 24.3%**：sampling 的多样性价值 → truncation 的作用 → 现有 threshold 依赖任务/温度超参数。[p. 1, §1, explicit, “depend upon the specification of hyperparameters”]
2. **`core_idea`，约 191 词，占 31.6%**：提出 distribution-aware 阈值，Figure 1 用高温长尾 admission 说明机制，Appendix B.6 承接 synthetic distributions。[pp. 1–2, §1, explicit, “entire token probability distribution”]
3. **`result_preview`，约 172 词，占 28.4%**：Rényi 解释、3 个 LLM、5 个 dataset、human evaluation、efficiency、diversity、case study 一次展开。[p. 2, §1, explicit, “three LLMs spanning multiple model sizes”]
4. **`contribution_list`，约 95 词，占 15.7%**：四条贡献依次回收 method、evaluation breadth、efficiency、additional analyses。[p. 2, §1, explicit, “our main contributions are as follows”]

贡献列表大体重复摘要；其中“3 LLM × 5 datasets”和“sampling speed + generation length”可证伪。[p. 2, §1, explicit, “three LLMs and five datasets”] 列表没有数字结果，也没有 seed、human agreement、diversity tradeoff 或 failure case。引言的钩子从“如何移除 tuning”转到“理论与实证能否共同支持阈值”，最后交给 Related Work 的 nearest-neighbor contrast。

## 5. Related Work 的定位方式

Related Work 独立占 pp. 2–3，约 689 词，占正文估计词数 12.1%。三段对应三个 citation cluster：

1. **固定/entropy-aware truncation taxonomy**：top-k、top-p、epsilon、eta，比较 threshold 定义与高熵适应。[pp. 2–3, §2, explicit, “remain lacking in adapting to high-entropy conditions”]
2. **最近邻对比与 gap creation**：mirostat、min-p、adaptive decoding，比较分布假设、需要调的量、使用的分布统计和迭代代价。[p. 3, §2, explicit, “min-p remains sensitive to the choice”]
3. **广义 decoding taxonomy**：contrastive、controlled、arithmetic decoding。该段主要界定互补关系，nearest-neighbor 差异弱于前两段。[p. 3, §2, explicit, “complementary approaches that can be used in conjunction”]

§2 负责命名 prior work 的 tuning/assumption burden；§3.4–3.5 随后把这些比较维度改写为 p-less 的三个性质：使用完整分布、候选集有界非空、阈值随温度变化。[p. 6, §3.5, explicit, “combines several desirable properties”] 这种分工避免逐篇工作在方法段重复出现，同时保留 citation 在后续论证中的作用。

## 6. 方法与理论

### 6.1 最小逻辑单元

方法动作序列为：

`state_problem → setup_notation → derive → instantiate_algorithm → define_component → connect_to_prediction → give_intuition → contrast_alternative → connect_to_experiment`

| 单元 | 输入/输出 | 解决的前文问题 | 证据 |
|---|---|---|---|
| `L[Pθ]` | 完整温度调整分布 → sum-of-squares threshold | 移除任务依赖的 threshold hyperparameter | [p. 4, Eq. 2, explicit, “sum of squared token probabilities”] |
| `Vp-less` | threshold → candidate set | 把阈值变为可执行 mask | [p. 4, Eq. 3, explicit, “Construct the sampling set”] |
| renormalization | masked probabilities → next token | 完成 sampling rule | [p. 4, Eq. 4, explicit, “normalized token probabilities”] |
| `p-lessnorm` | `L[Pθ]` 减去 normalized incorrect-guess likelihood | 多样性优先时放宽阈值 | [p. 4, §3.2, explicit, “diversity is favored over coherence”] |
| Rényi connection | `L[P]` ↔ `exp(-H₂)` | 将分布集中度连接到 threshold 变化 | [p. 5, Eq. 8, explicit, “collision entropy”] |
| Proposition 1 | finite categorical PMF → bounds | 保证 candidate set 非空 | [p. 16, Proposition 1, explicit, “guarantee a valid threshold”] |

形式化对象包括 prefix `x1:t-1`、token set `V`、sampling event `S`、correct/desirable event `T`、model distribution `Pθ`、threshold `L[Pθ]`、candidate set `Vp-less` 与 renormalized output distribution。论文没有优化目标函数；它定义逐步 admissibility rule。[p. 4, §3.1, explicit, “We formalize the method as follows”]

### 6.2 方程与理论计数

- 编号方程：**17**，其中正文 Equations 1–10，appendix Equations 11–17。
- 估计 displayed equation blocks：**26**，包括证明内的未编号推导。
- Proposition 计数为 3；Proof 计数为 3；Theorem/Lemma/Corollary 计数为 0。
- Algorithm / pseudocode：**0**。Figure 15 给出一段 11 行左右的 PyTorch function，属于 code figure。[p. 32, Figure 15, explicit, “Python code snippet for p-less sampling”]

Proposition 1 用 Cauchy–Schwarz 与 modal-probability bound 证明 `1/c ≤ L[P] ≤ max_i P(x_i)`，提供非空 candidate-set guarantee。[p. 16, Appendix B.3, explicit, “Proof of Proposition 1”] Propositions 2–3 将 `p-lessnorm` 连接到 second central moment，并给出相对 `p-less` 的 relaxed bounds。[pp. 17–18, Appendix B.4, explicit, “p-lessnorm bounds are relaxed”] Equation 17 定义 generalized `k`-order threshold，`k→0` 接近 uniform sampling，`k→∞` 接近 greedy decoding。[p. 19, §B.5, explicit, “generalized k-order threshold”]

理论在论文中的角色分两层：

- **核心链与保证**：Equations 2–4 定义可执行规则；Proposition 1 保证 threshold 合法。[p. 4, §3.1, explicit, “Determine the threshold probability”][p. 16, Proposition 1, explicit, “non-empty candidate set”]
- **解释层**：collision entropy、second moment、Index of Coincidence 为同一量提供不同语义。[pp. 5, 15, §§3.3/B.1, explicit, “exponential of the negative Rényi entropy”]

correctness 解释使用两个关键前提：`S` 与 `T` 独立；`Pθ` 代替真实 desirability distribution。[p. 4, §3.1, explicit, “independent events”][p. 4, §3.1, explicit, “best empirical estimate”] 这些前提未转化为 calibration prediction。理论因此能够保证候选集性质，无法保证生成质量。

Equation 9 的排版把 `-log` 放在 `Σ p_i log p_i` 前，周围文字意在使用标准 `H₂≤H₁` 关系；该处公式字面形式与文字说明存在排版疑点。[p. 5, Eq. 9, layout_observation, “H2(p) = -log L[P] ≤”]

## 7. 实验设计

### 7.1 设计事实

| 项目 | 设计 | 状态与证据 |
|---|---|---|
| Models | Llama-2-7B-Chat、Mistral-7B-Instruct、Llama3-70B-Instruct；DeepSeek-R1-Distill-Qwen-7B 为 robustness ablation | `observed` [p. 6, §4.1, explicit, “Llama-2-7B (Chat)”][p. 26, §C.5, explicit, “DeepSeek-R1-Distill-Qwen-7B”] |
| Datasets | GPQA、GSM8K、QASC、CSQA、Writing Prompts | `observed` [p. 21, §C.1, explicit, “five diverse datasets”] |
| Baselines | top-p、min-p、epsilon、eta、mirostat；另有 greedy 与 beam | `observed` [p. 6, §4.1, explicit, “Top-p, Min-p”][p. 24, §C.4, explicit, “Beam search (bs=3)”] |
| Temperature | 主网格 0.5、0.7、1.0、1.5、2.0；diversity 延伸至 2.25、2.5 | `observed` [p. 21, §C.1, explicit, “between 0.5 and 2.0”][p. 27, §C.8, explicit, “τ = 2.25 and τ = 2.5”] |
| Baseline hyperparameters | top-p 0.9；min-p 0.1；epsilon/eta 0.0002；mirostat 4.0 | `observed` [p. 22, §C.2, explicit, “set p = 0.9 for Top-p”] |
| Reasoning metrics | accuracy 与 normalized accuracy–temperature AUC | `observed` [p. 7, §4.2, explicit, “area under the accuracy-temperature curve”] |
| Writing metric | 100 prompts；每个 method-temperature 一次 generation；default τ=1.0 为 reference | `observed` [p. 8, §4.3, explicit, “one generation per method and temperature”] |
| Seeds | Llama2 为 3 seeds；Mistral/Llama3 因 compute 使用 1 seed | `observed` [p. 23, §C.3, explicit, “one random seed due to computational constraints”] |
| Prompting | CSQA/GSM8K/QASC：8-shot CoT；GPQA：zero-shot CoT；WP：instructional | `observed` [p. 33, §C.12.1, explicit, “used 8-shot prompting”] |
| Leakage control | 8-shot examples 来自与 test split 不同的 train/validation split | `observed` [p. 33, §C.12.1, explicit, “different from the test split”] |
| Hardware / versions | 未给出 GPU/CPU、accelerator 数量、precision、package versions | `not_present` [p. 11, §7, explicit, “all details necessary to fully reproduce”] |
| Generation budget | 未给出统一 maximum new tokens 与 stopping rule | `not_present` [p. 33, §C.12, explicit, “prompts constructed for the datasets”] |
| Failure handling | 未说明 malformed output、answer parsing、timeout、evaluator failure | `not_present` [p. 22, §C.1, explicit, “We measured accuracy”] |

实验没有预列 numbered research questions/hypotheses；§4.1 直接列模型、任务、baseline、temperature 和 metric。[p. 6, §4.1, explicit, “Our experiments were performed using”] 实验顺序与引言贡献大体对应：§4.2 回应 reasoning robustness，§4.3 回应 writing，§5.1 回应 efficiency，§5.2–5.4 回应 diversity/qualitative/case study。完整 hyperparameter、seed、prompt 和 failure case 被移入附录。

### 7.2 Human evaluation

Appendix A 使用 Llama2-7b 的 100 个 Writing Prompts pair，比较 `p-less τ=2.0` 与 `default τ=1.0`。annotator pool 包含 3 名作者与 3 名非作者，每对 story 获得 4 个 label。[p. 14, Appendix A, explicit, “total of 4 labels for each story pair”] 23.7% pair 全体一致，26.9% tie；其余使用 majority vote。p-less 的 majority-vote win rate 为 58.8%，在 unanimous 子集为 72.7%。[p. 14, Appendix A, explicit, “p-less won the majority vote 58.8%”] 该设计提供方向一致性；作者参与、低 unanimous 比例和 100-pair 分母限制结论范围。

## 8. 结果、统计与可视化

### 8.1 主结果

1. **Reasoning AUC**：Table 1 中，p-less/p-lessnorm 在 Llama2 与 Mistral 的 8 个 model–dataset cell 全部领先；Llama3 的值为最高或距最高不超过 0.005 的第二名。[p. 7, §4.2, explicit, “highest or second highest within 0.005”] AUC 将所选 temperature grid 聚合成一个决策量，温度级差异需看 Appendix Table 5。[p. 23, Table 5, explicit, “Accuracy of LLama2-7b”]
2. **高温 reasoning**：例如 Llama2 QASC 在 `τ=2.0` 时，p-less/p-lessnorm 为 52.1/52.2，min-p 为 44.3，其余 baseline 不高于 28.0；Llama3 GSM8K 中 p-less family 为 92.8，min-p 为 91.7。[p. 23, Table 5, explicit, “The best accuracy”] Mistral/Llama3 只使用一个 seed，无法估计 seed-level variability。[p. 23, §C.3, explicit, “one random seed”]
3. **Creative writing**：Llama2 p-less length-controlled win rate 在 `τ=1.5/2.0` 为 58.23/65.64；Mistral 为 66.97/60.32。多个 baseline 在高温接近 0。[p. 8, Table 2, explicit, “Length-controlled win rate for 100 sampled prompts”] 每个设置只有一次 generation，未报告 within-setting uncertainty。
4. **Human preference**：majority-vote 58.8% 支持 automated evaluation 的方向。[p. 14, Appendix A, explicit, “directional consistency”] 该证据没有 interval，也没有独立的全非作者评审组。
5. **Sampling time**：Table 3 的 p-less mean 为 0.01942 s/token，min-p 为 0.02497，top-p 为 0.02362；同时报告 SD 与 SEM。[p. 8, Table 3, explicit, “Average sampling time per token”]
6. **Generation length**：Llama2 的 CSQA、QASC、GSM8K 在所有温度下由 p-less family 取得最短 mean generation；Llama3 CSQA 等 cell 不符合该模式。[p. 29, Table 12, explicit, “Mean generation length”] 正文使用 “often”，与异质性相容。[p. 9, §5.1, explicit, “often more efficient”]
7. **Diversity**：Figure 3 只纳入 QASC mean accuracy `>0.5` 的 method-temperature setting，故 Pareto frontier 是条件性结论。[p. 9, §5.2, explicit, “mean accuracy > 0.5”] Table 10 给出完整 diversity matrix。[p. 28, Table 10, explicit, “Mean diversity values”]
8. **DeepSeek ablation**：`τ=2.0` 时 p-less family 在四个 dataset 均为 top-two；CSQA 的 p-lessnorm 为 67.2。[p. 26, Table 7, explicit, “Mean accuracy of DeepSeek-R1-Distill-Qwen-7B”] seed 数未说明。
9. **k-order ablation**：Table 9 中 default p-less/p-lessnorm 在多数 cell 领先 discrete `k∈{0.025,0.1,0.4,1.0,1.6}`；仅覆盖一个 model。[p. 27, §C.7, explicit, “specific k-order threshold is unnecessary”]
10. **Failure cases**：C.13 给出 final-sum arithmetic error 与 initial question-interpretation error，各配 entropy/admission trace；没有失败率分母。[pp. 42–44, §C.13, explicit, “two typical failure patterns”]

### 8.2 统计处理

| 对象 | 聚合单位与处理 | 不确定性 |
|---|---|---|
| Reasoning | example-level accuracy；再对 temperature curve 计算 normalized AUC | Llama2 为 3-seed mean；Mistral/Llama3 1 seed；主表无 dispersion [p. 23, §C.3, explicit, “three different random seeds”] |
| Writing | 100 prompts；每设置 1 generation；length-controlled win rate | 无 interval [p. 8, §4.3, explicit, “subset of 100 prompts”] |
| Human | 100 pairs；每 pair 4 labels；majority vote、tie、unanimity | 无 interval；报告 author/non-author marginal win rate [p. 14, Appendix A, explicit, “win rates for annotations produced by authors”] |
| Efficiency | mean、SD、SEM；pairwise t-test | Table 14 使用 nominal `p<0.05`；未说明 pairing、test unit、assumption、multiplicity [p. 30, Table 14, explicit, “Significant results (p < 0.05)”] |
| Diversity/length | mean n-gram diversity；mean generation length | 无 dispersion [pp. 28–29, Tables 10–12, explicit, “Mean diversity values”] |

论文没有为主 accuracy、AUC、win rate、diversity 或 length 报告 interval、effect size、bootstrap、Bayesian analysis、regression 或 multiplicity correction。timing 是唯一同时给出 SD、SEM 和 hypothesis test 的结果。[pp. 8, 30, Tables 3/14, explicit, “Standard Error of Mean”]

Table 14 显示 p-less 与 eta 的 `p=0.0902`，与其他 baseline 的 nominal p 值不超过 0.0486。[p. 30, Table 14, explicit, “Pairwise t-test results”] 正文准确保留 eta 例外。[p. 8, §5.1, explicit, “except η-sampling”] 五次对 p-less 的比较没有校正说明，最靠近阈值的结果需要按 nominal evidence 理解。

### 8.3 关键视觉对象

PDF 共 **19 figures、15 tables、0 algorithms**。正文保留 Figures 1–4 与 Tables 1–4；appendix 承载 Figures 5–19 与 Tables 5–15。

- **Figure 1**：三种 sampling rule × 三个温度，使用分布曲线、admitted-tail shading 和 threshold marker，使机制先于公式可见。[p. 2, Figure 1, explicit, “Comparison of truncation thresholds”]
- **Table 1 + Figure 2**：AUC 总表和 Llama2 温度曲线形成“概括 → 展开”组合。[p. 7, Table 1/Figure 2, layout_observation, “Accuracy vs. temperature curves”]
- **Table 2**：两个 model × 三温度 × 七方法，单表直接暴露高温 collapse。[p. 8, Table 2, explicit, “Length-controlled win rate”]
- **Table 3**：mean/SD/SEM 使 timing 的统计单位比其他主结果更完整。[p. 8, Table 3, explicit, “Standard Deviation”]
- **Figure 3**：accuracy–diversity scatter 的过滤条件写在正文，没有进入 caption；单独阅读图注无法恢复 selection rule。[p. 9, §5.2, explicit, “mean accuracy > 0.5”]
- **Figure 4**：单个 GSM8K item 的 dual trace 与文本推理对齐，适合解释机制，不能估计机制频率。[p. 10, Figure 4, explicit, “Step-wise entropy and number of admitted tokens”]
- **Figures 5–8**：synthetic distributions 系统改变 temperature、vocabulary size、profile、long tail，补足 Figure 1 的设计空间。[pp. 19–22, §B.6, explicit, “temperature, vocabulary size and distribution profiles”]
- **Tables 5、8、10、12**：完整矩阵承担可核查性，代价是小字号和高扫描成本。[pp. 23, 26, 28, 29, layout_observation, “Full results”]
- **Table 13 + Figures 12–14**：mean entropy/admission 与条件 histogram 共同形成机制诊断。[pp. 30–31, §C.10, explicit, “Entropy Distributions”]
- **Figures 15–17 + Table 15**：实现代码、CPU/RAM trace 和 summary 组成 profiling bundle；Table 15 的 `±` 未在 caption 定义。[pp. 32–33, §C.11, layout_observation, “Comparison of sampling methods”]
- **Figures 18–19**：失败案例的 entropy trace 位于 31 页 appendix 的末两页附近，结论没有回收。[p. 43, §C.13, explicit, “failure pattern 1”]

## 9. 消融、负面结果与自我设限

正文的 ablation 文字很少，主要内容位于 Appendix C：

| 消融/边界 | 识别目标 | 结论边界 | 证据 |
|---|---|---|---|
| baseline hyperparameter sweep | 默认 baseline 设置是否造成优势 | 只覆盖 Llama2-7b | [p. 26, §C.6, explicit, “for the Llama-2-7b model”] |
| generalized `k` | 默认 collision-order 是否需要 tuning | 一个 reasoning model，离散 `k` grid | [p. 27, Table 9, explicit, “different k-order generalizations”] |
| DeepSeek reasoning model | reasoning-specialized model robustness | seed 未说明 | [p. 26, Table 7, explicit, “DeepSeek-R1-Distill-Qwen-7B”] |
| p-less `τ>2.0` | diversity 能否继续增加 | 没有并列报告 accuracy | [p. 27, §C.8, explicit, “τ = 2.25 and τ = 2.5”] |
| greedy / beam | 是否近似 argmax/search | Mistral 单模型；GSM8K beam 更好 | [p. 25, §C.4.1, explicit, “exception of GSM8K”] |
| human vs automated | writing evaluator 方向一致性 | 100 pairs；作者参与 | [p. 14, Appendix A, explicit, “directional consistency”] |
| failure cases | arithmetic 与 ambiguity 边界 | 2 个 selected cases，无 prevalence | [p. 42, §C.13, explicit, “two typical failure patterns”] |

论文没有独立 Limitations section。[pp. 10–11, layout_observation, “CONCLUSION”/“REPRODUCIBILITY STATEMENT”] 明示限制散落在结果和附录：

- **compute**：Mistral/Llama3 仅一个 seed。[p. 23, §C.3, explicit, “due to computational constraints”]
- **metric/sampling**：Writing Prompts 每设置一条 generation。[p. 8, §4.3, explicit, “one generation per method and temperature”]
- **diversity**：高温下 p-less 的 diversity 低于若干 baseline；达到 min-p 的 diversity 可能需要更高 temperature。[pp. 9, 27, §§5.2/C.8, explicit, “lower diversity than other sampling methods”]
- **baseline**：beam search 在 GSM8K 更好。[p. 25, §C.4.1, explicit, “exception of GSM8K”]
- **failure**：复杂 arithmetic 与开头 ambiguity 可触发错误。[pp. 42–43, §C.13, explicit, “arithmetic operations may introduce a spike”]
- **reproducibility**：hardware、environment、stopping 和 failure handling 缺失；这与 “all details necessary” 的 statement 不一致。[p. 11, §7, explicit, “all details necessary to fully reproduce”]
- **ethics/deployment**：PDF 没有相关讨论。[p. 10, §6, layout_observation, “empirically effective”]

不利信息的呈现方式可以按版面事实描述：Figure 3 使用 accuracy filter；C.12 明说 favorable examples 是 “selected for illustration”；failure cases 位于 appendix 末端；seed constraint 位于 Table 5 后的 appendix prose。[pp. 9, 23, 33, 42, explicit, “selected for illustration of p-less”] 论文也主动正面讨论 diversity tradeoff、GSM8K beam exception 和两种 failure pattern，故不能把 appendix 迁移等同于隐瞒。

## 10. 文档内测量与表述不一致

1. **Efficiency sample**：§5.1 写 200 个 Mistral generations，覆盖 GSM8K 与 GPQA；C.11 写 100 个 GSM8K samples。[p. 8, §5.1, explicit, “over 200 Mistral-7b generations”][p. 32, §C.11, explicit, “100 GSM8K samples”]
2. **Efficiency wording**：0.02497→0.01942 是 mean time per token 降低约 22%，正文写成 “22% reduction in inference speed”。[p. 8, §5.1/Table 3, explicit, “22% reduction in inference speed”]
3. **Diversity scale**：Table 4 使用约 0.63；Table 10 对应 cell 使用约 63，未明确说明百分比 rescaling。[pp. 9, 28, Tables 4/10, layout_observation, “Mean diversity values”]
4. **Code availability**：摘要为 unresolved `§`；Reproducibility Statement 使用 future tense。[pp. 1, 11, explicit, “The code is available at §.”]
5. **Equation 9**：公式字面排版与标准 `H₂≤H₁` 文字说明之间存在疑点。[p. 5, Eq. 9, layout_observation, “H2(p) = -log L[P] ≤”]

## 11. Claim closure

| 引言/正文主张 | 闭环状态 | 回应对象 | 判断 |
|---|---|---|---|
| hyperparameter-free rule | `closed` | Eqs. 2–4；Figure 15 | 规则与实现直接对应 [pp. 4, 32, explicit, “We formalize the method”] |
| entropy response + non-empty set | `closed` | Eq. 8；Proposition 1；Figures 5–8 | 数学性质与 synthetic 可视化闭合 [pp. 5, 16, explicit, “guarantee a valid threshold”] |
| 3 LLM × 5 datasets robustness | `partially_closed` | Tables 1、2、5 | 覆盖面兑现；one-seed 与 one-generation 限制识别 [pp. 8, 23, explicit, “one random seed”] |
| sampling speed + shorter length | `partially_closed` | Tables 3、12、15 | empirical support 存在；hardware 与 sample 描述不完整 [pp. 8, 29, 33, explicit, “Average sampling time”] |
| creative-writing quality | `partially_closed` | Table 2；Appendix A | automated/human 方向一致；分母和 agreement 限制强度 [pp. 8, 14, explicit, “58.8%”] |
| accuracy–diversity frontier | `partially_closed` | Figure 3；Table 10 | frontier 依赖 accuracy filter [p. 9, explicit, “mean accuracy > 0.5”] |
| correctness/desirability interpretation | `not_testable_here` | independence + `Pθ` proxy | output experiments没有检验 proxy calibration [p. 4, interpretation, “best empirical estimate”] |
| not argmax-seeking | `partially_closed` | Table 6；Table 11 | writing 与 temperature-diversity 提供区分；单模型/设置 [pp. 24, 28, explicit, “Greedy decoding”] |
| generalized `k` 无需 tuning | `partially_closed` | Eq. 17；Table 9 | 一个 model、离散 grid [pp. 19, 27, explicit, “specific k-order threshold is unnecessary”] |
| characteristic failures | `partially_closed` | Figures 18–19 | 类型有实例，频率开放 [pp. 42–44, explicit, “two typical failure patterns”] |

## 12. Conclusion 与 appendix 职责

Conclusion 只有一个段落，动作顺序为：`restate_method → reclaim_properties → reclaim_results → reclaim_efficiency → impact`。[p. 10, §6, explicit, “We presented p-less sampling”] 没有新数字。末句把工作定性为 “principled”, “intuitive”, “empirically effective”，未回收 seed、diversity、agreement 或 failure boundary。[p. 10, §6, explicit, “principled sampling approach”]

Appendix 的职责分布如下：

- **A，p. 14**：human evaluation 设计、agreement、majority vote，`additional_result`。[p. 14, Appendix A, explicit, “three non-author annotators”]
- **B.1–B.5，pp. 15–19**：Index of Coincidence、moments、3 个 propositions/proofs、generalized `k`，`extended_method`/`proof`。[pp. 15–19, Appendix B, explicit, “Proof of Proposition 1”]
- **B.6，pp. 19–22**：synthetic threshold robustness，Figures 5–8。[p. 19, §B.6, explicit, “distribution profiles”]
- **C.1–C.2，pp. 20–22**：models、datasets、temperatures、metrics、baseline hyperparameters。[p. 22, §C.2, explicit, “set p = 0.9”]
- **C.3–C.7，pp. 23–27**：完整 primary results、greedy/beam、DeepSeek、hyperparameter sweep、`k` ablation。[p. 23, §C.3, explicit, “complete experimental results”]
- **C.8–C.10，pp. 26–31**：diversity、generation length、entropy distributions。[p. 30, §C.10, explicit, “Mean Entropy and Admitted Token Count”]
- **C.11，pp. 32–33**：code、t-tests、CPU/RAM profiling。[p. 32, §C.11, explicit, “pairwise t-tests”]
- **C.12，pp. 33–42**：prompt regime、favorable generation examples、full prompts。[p. 38, §C.12.4, explicit, “prompts used for the five datasets”]
- **C.13，pp. 42–44**：two failure cases。[p. 42, §C.13, explicit, “two typical failure patterns”]

正文自足性较强的部分是 rule、核心 equations、headline results、efficiency、diversity tradeoff 与一个 case study。非空 guarantee 的 proof、seed、完整矩阵、baseline sweep、human study、timing significance、prompts 和 failures 依赖附录。[p. 11, §7, explicit, “From Appendix C.3 to Appendix C.11”]

## 13. 用词与修辞

以下为正文至 Reproducibility Statement 的近似语境计数，排除 references、公式、表格数值和页眉；仓库统一 token 脚本应覆盖最终原始计数。

- 高频内容词：`p-less` 约 100、`temperature` 39、`entropy` 29、`threshold` 28、`diversity` 24、`generation` 22、`reasoning` 21、`accuracy` 14、`hyperparameters` 13。
- 高频 n-grams：`logical reasoning`、`truncation threshold`、`creative writing`、`temperature values`、`Rényi entropy`、`inference-time efficiency`、`generation lengths`。
- 结构计数：`we show` 1、`we find` 0、`we demonstrate` 2、`we propose` 0、`we observe` 0、`we introduce` 3、`we provide` 9、`our results show` 1、`results demonstrate` 1。
- 词族近似计数：show family 12、demonstrate family 6、`provide` 13、`introduce` 3、`outperform` 2；`however` 4、contrast family 8、`unlike` 4、`in contrast` 7；`often` 4、`similar` 6、`competitive` 3、`significantly` 4、`can` 9、`may` 1。

强动词与 global comparative 集中在 abstract、introduction、§4–5、conclusion。[p. 1, Abstract, explicit, “consistently outperforms”] 附录讨论异质性时才密集出现 “exception”, “generally”, “may require”。[p. 25, §C.4.1, explicit, “exception of GSM8K”][p. 27, §C.8, explicit, “may require slightly higher temperature values”] 近似 strong-to-qualified claim-act ratio 约 2:1。

PDF text extraction 的误切分风险包括 `p-less/p-lessnorm`、`Rényi` 被截为 `nyi`、epsilon/eta glyph、Llama model name 与跨行 hyphen；这些项不宜直接作为最终 lexical count。

## 14. 最终判断

1. **单一主线**：完整 token distribution → collision-probability threshold → 高温 robustness/efficiency/diversity evidence。[pp. 4–9, §§3–5, interpretation, “sum of squared token probabilities”]
2. **正文保留的决策关键内容**：Eqs. 1–10、Tables 1–4、Figures 1–4、complexity argument、一个高熵 case。[pp. 4–10, §5.4, layout_observation, “ROBUSTNESS UNDER HIGH ENTROPY”]
3. **附录迁移及影响**：完整矩阵和 proofs 移入附录提升正文可读性；seed、hardware、human agreement、failure boundary 同时离开正文，使复现与限制判断依赖长附录。[pp. 11–44, interpretation, “all details necessary”]
4. **最有效模式**：`formula → bound → temperature curve/full matrix → entropy/admission trace`。同一可观测中间量贯穿 definition、prediction 和 diagnosis。[pp. 4, 16, 30, interpretation, “Mean Entropy and Admitted Token Count”]
5. **最明显的未闭合处**：`Pθ` 作为真实 desirability proxy 的语义没有 calibration test；empirical success 只支持结果层。[p. 4, §3.1, interpretation, “best empirical estimate”]
6. **可迁移规则**：把方法压成一个可执行量，为该量提供 bounds 与可观测 prediction，主结果沿 prediction 组织，完整矩阵进入 appendix。[pp. 4–7, interpretation, “We formalize the method as follows”]
7. **适用边界**：该规则适合中间量在 inference 时可直接观测、并能跨任务定义共同 prediction axis 的工作。核心机制涉及不可观测标签或强交互干预时，单一诊断量无法替代 identification design。[p. 4, §3.1, interpretation, “P(T = v)”]

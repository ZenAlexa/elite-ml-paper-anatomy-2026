# In-Place Test-Time Training：单篇深读备忘

## 1. 读取边界与来源

- **论文**：*In-Place Test-Time Training*，ICLR 2026，oral。
- **作者**：Guhao Feng、Shengjie Luo、Kai Hua、Ge Zhang、Wenhao Huang、Di He、Tianle Cai；前两位作者标注 equal contribution，Wenhao Huang 与 Di He 为 correspondence authors（PDF p.1）。
- **身份证据**：PDF 首页写有 “Published as a conference paper at ICLR 2026”（p.1）。
- **事实源**：`corpus/pdfs/iclr-2026-6a94cca2daa0.pdf`，官方 proceedings 版本；配套提取文本为 `corpus/text/iclr-2026-6a94cca2daa0.txt`。OpenReview forum 为 `https://openreview.net/forum?id=dTWfCLSoyl`；官方 PDF 为 `https://proceedings.iclr.cc/paper_files/paper/2026/file/ba6f5879d7f382241316f7dda7e6b8ac-Paper-Conference.pdf`。
- **完整性**：物理页 21 页；正文至 p.10，p.11 先放 Ethics/Reproducibility/Acknowledgement 再开始 references；references 为 p.11–15；appendix 为 p.16–21；未提供 supplementary 文件。
- **版面**：正文、references、appendix 均为单栏；Figure 1–4 均为横跨正文宽度的图，Figure 2 为双面板、Figure 3 为三面板、Figure 4 为四面板。表格集中在 p.7–10 与 p.19–20，图表压缩段落可读面积但未形成双栏阅读路径（layout observation, pp.6–10, 19–20）。

### 1.1 页级地图

| 物理页 | 标题/范围 | 模块 | 估计词数 |
|---|---|---:|---:|
| 1 | Abstract；1 Introduction 开始 | abstract / introduction | 231 / 约 320 |
| 2 | 1 Introduction 续；2 Preliminary: Test-Time Training 开始 | introduction / other | 约 528 / 约 100 |
| 3 | 2 Preliminary 续；3 In-Place Test-Time Training 概述开始 | other / method | 约 594 / 约 28 |
| 4 | 3 概述续；3.1 Overall Framework | method | 657 |
| 5 | 3.1 续；3.2 LM-Aligned Objective；3.3 Theoretical Analysis 开始 | method / theory | 248 / 约 635（跨 p.5–6） |
| 6 | 3.3 续；Figure 1；Theorem 1；3.4 开始 | theory / method | 约 300 / 约 169 |
| 7 | 3.4 续；4 Experiments；Table 1；4.1 开始 | method / experimental_design | 402 / 约 151 / 约 80 |
| 8 | Table 2；4.1 续；4.2 开始；Figure 2 | experimental_design / results | 约 419 / 约 369 |
| 9 | Table 3；Figure 3；4.2 续 | results / ablation | 约 788 |
| 10 | Figure 4；4.3；5 Conclusion | ablation / conclusion | 315 / 104 |
| 11 | Ethics Statement；Reproducibility Statement；Acknowledgement；References 开始 | other | 53 / 63 / 34 / references |
| 12–15 | References 续 | other | 1,971（p.11–15 合计估计） |
| 16 | Appendix A Related Work；Appendix B Proof of Theorem 1 开始 | related_work / appendix | 644 / 约 80 |
| 17 | Appendix B proof 续 | appendix | 约 398 |
| 18 | Appendix B 结尾；Appendix C Algorithm 1；Appendix D、D.1 开始 | appendix | 约 411 |
| 19 | Appendix D.1 续；D.2；Tables 4–6 | appendix | 约 256 |
| 20 | Table 7；D.2 续；D.3；Table 8 | appendix | 约 417 |
| 21 | D.3 续；Initialization；E Usage of LLMs | appendix / other | 约 233 / 36 |

`page_map` 使用物理页码。正文主段落在 p.10 的 conclusion 末尾结束；p.11 的三个声明属于 front matter，不能并入正文页数。提取器将带空格的小型大写标题误判为未找到 references，自动 provisional 边界因此偏移，详见第 10 节。

## 2. 摘要逐句功能编码

| # | 摘要句（保留原文） | 词数 | 功能 | 限定词/数字/比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | The static “train then deploy” paradigm fundamentally limits Large Language Models (LLMs) from dynamically adapting their weights in response to continuous streams of new information inherent in real-world tasks. | 29 | `object_scope`, `problem_gap` | “fundamentally”；对象为 LLM 与 continuous streams | p.1, Abstract, “static train then deploy paradigm fundamentally limits” |
| 2 | Test-Time Training (TTT) offers a compelling alternative by updating a subset of model parameters (fast weights) at inference time, yet its potential in the current LLM ecosystem is hindered by critical barriers including architectural incompatibility, computational inefficiency and misaligned fast weight objectives for language modeling. | 45 | `core_idea`, `problem_gap` | “yet”“critical”；比较静态部署与 TTT；列出 3 个 barrier | p.1, Abstract, “architectural incompatibility, computational inefficiency” |
| 3 | In this work, we introduce In-Place Test-Time Training (In-Place TTT), a framework that seamlessly endows LLMs with Test-Time Training ability. | 20 | `core_idea`, `method` | “seamlessly”；提出框架 | p.1, Abstract, “we introduce In-Place Test-Time Training” |
| 4 | In-Place TTT treats the final projection matrix of the ubiquitous MLP blocks as its adaptable fast weights, enabling a “drop-in” enhancement for LLMs without costly retraining from scratch. | 28 | `method`, `impact_claim` | “drop-in”“without costly retraining”；组件为 `Wdown` | p.1, Abstract, “final projection matrix of the ubiquitous MLP blocks” |
| 5 | Furthermore, we replace TTT’s generic reconstruction objective with a tailored, theoretically-grounded objective explicitly aligned with the Next-Token-Prediction task governing autoregressive language modeling. | 23 | `method`, `theory` | “theoretically-grounded”“explicitly aligned”；比较 reconstruction 与 NTP | p.1, Abstract, “aligned with the Next-Token-Prediction task” |
| 6 | This principled objective, combined with an efficient chunk-wise update mechanism, results in a highly scalable algorithm compatible with context parallelism. | 20 | `method`, `theory` | “highly scalable”；CP compatibility | p.1, Abstract, “compatible with context parallelism” |
| 7 | Extensive experiments validate our framework’s effectiveness: as an in-place enhancement, it enables a 4B-parameter model to achieve superior performance on tasks with contexts up to 128k, and when pretrained from scratch, it consistently outperforms competitive TTT-related approaches. | 37 | `experimental_setup`, `quantitative_result`, `qualitative_result` | 4B、128k；比较 pre-trained enhancement 与 from-scratch baselines | p.1, Abstract, “contexts up to 128k” |
| 8 | Ablation study results further provide deeper insights on our design choices. | 11 | `experimental_setup`, `qualitative_result` | 未给数字；对象为 design choices | p.1, Abstract, “Ablation study results” |
| 9 | Collectively, our results establish In-Place TTT as a promising step towards a paradigm of continual learning in LLMs. | 18 | `impact_claim` | “promising step”；扩大到 continual learning | p.1, Abstract, “towards a paradigm of continual learning” |

摘要顺序为：部署缺口 → TTT 的三个障碍 → 框架与 `Wdown` 设计 → NTP 目标与 chunk/CP → 结果范围 → 消融 → continual-learning 影响。它报告实验数字（4B、128k），没有直接报告理论不等式、seed/区间或明确失败条件；最强的意义主张放在末句，具体可检验主张集中在第 7 句。

## 3. 引言论证推进

引言的动作链为：

`context → problem_gap → failure_of_prior_work → missing_insight → core_idea → method_preview → theory_preview → result_preview → scope_boundary`

| 段 | 页码 | 主动作 | 当前段回答的问题 | 下一段钩子 | 估计词数 | 证据 |
|---:|---:|---|---|---|---:|---|
| 1 | 1 | `context` → `problem_gap` | LLM 的静态 train-then-deploy 为何无法随流式输入适配？ | 转向 context-window 与 attention 成本 | 241 | p.1, §1, “once deployed, the model’s weights cannot be updated” |
| 2 | 1–2 | `context` → `failure_of_prior_work` | ICL 如何缓解缺口，为什么 context window 与 quadratic attention 仍限制它？ | 引出 TTT 作为动态参数更新范式 | 约 205 | p.1–2, §1, “its effectiveness is tethered to the model’s context window” |
| 3 | 2 | `failure_of_prior_work` | 现有 TTT 在 LLM 生态的三个障碍是什么？ | 需要一个同时处理三障碍的框架 | 约 184 | p.2, §1, “critical barriers: (i)…(ii)…(iii)” |
| 4 | 2 | `missing_insight` → `core_idea` | 如何避免替换 attention、重训全部参数？ | 直接复用 MLP final projection 作为 fast weights | 约 172 | p.2, §1, “repurpose existing MLP blocks” |
| 5 | 2 | `method_preview` → `theory_preview` | 如何解决 sequential update 与 reconstruction/NTP mismatch？ | chunk-wise update、attention 协同、NTP-aligned objective 与理论分析 | 约 160 | p.2, §1, “bespoke adaptation mechanism for language modeling” |
| 6 | 2 | `result_preview` → `scope_boundary` | 这些选择在哪些规模与任务上接受检验？ | Qwen3 drop-in、from-scratch 500M–4B、消融 | 约 145 | p.2, §1, “Through relatively cheap continual training” |

贡献列表没有单独编号，而是以连续段落给出。它比摘要多了三障碍的因果对应，包含可证伪的长上下文与 from-scratch 比较，但未在引言承诺理论的独立实验检验，也未给出 compute、seed 或失败边界。引言把 “drop-in”“highly effective/scalable”“promising continual learning” 推到较宽范围，正文证据主要落在 RULER、语言建模和有限模型族。

## 4. 相关工作

相关工作没有独立正文章节，完整版本位于 Appendix A（p.16），正文通过引言、方法和实验段落中的引用簇承担定位。Appendix A 约 644 词，占附录正文约四分之一；正文占比为 0。它使用三段组织：

1. **TTT taxonomy + chronology + nearest-neighbor contrast**，从 fast weights 的早期定义、视觉/语言/视频/音频扩展推进到 optimizer、online objective、chunk-wise TTT，最后指出三项缺口，包括大规模预训练模型的无缝集成、autoregressive-tailored objective、large chunks（p.16, “prior work has not addressed how to seamlessly integrate TTT”）。
2. **Efficient long-context architectures taxonomy**：按 sparse attention、linear-time variants、SSMs、delta rule 分类，并将 efficient processing 与 online adaptation 区分为互补方向；作者把未来与 efficient backbones 的集成留待后续（p.16, “These architectural advances are complementary to our framework”）。
3. **Memory design and augmentation taxonomy**：按 persistent external memory 与 transient contextual memory 区分，随后把 TTT 定位为以自身参数充当高容量动态 memory 的 RNN hidden-state 扩展（p.16, “TTT represents a powerful instance of this latter category”）。

因此相关工作避免逐一复述方法，但比较维度仍由作者选择，缺少统一的容量、训练预算、任务或理论假设矩阵；后续正文引用仍用于支持 chunk/CP、MLP memory、YaRN 与 baseline 选择，而非只停留在附录列举。

## 5. 方法与理论

### 5.1 形式对象与因果链

- **输入/状态**：token 序列 `X` 经 attention 与 gated MLP 得到中间激活 `Z`；`Wdown` 是每个启用层的 fast-weight state，`Wup`/`Wgate` 保持为 frozen slow weights（p.4, “we treat the input projections Wup and Wgate as frozen slow weights”）。
- **输出**：每个 chunk 用当前 `Wdown` 产生 `O[i]`，随后用 `Z[i]` 与 target `V[i]` 更新状态；apply 先于 update，保证严格因果（p.4, “For each chunk…two sequential operations”）。
- **目标**：用 `V̂ = Conv1D(X0)Wtarget` 产生含未来 token 信息的 target；`Conv1D` 的 causal kernel 控制未来范围，`Wtarget` 学习投影（p.5, “the amount of future token information can be controlled”）。
- **理论设定**：induction-head toy setting 中，历史位置 `t*` 的 `(k*,v*)` 与后续 query `k*` 对齐；假设 token embeddings 近似正交、对应 `Z` 的期望内积为正（p.5, “Approximate Orthogonality of Embeddings”; “Key-Query Alignment”）。
- **并行实现**：先并行算每个 chunk 的 `ΔW(i)`，再做 prefix sum，最后用前序累计状态计算输出；causal padding 与 document-boundary reset 让并行扫描与顺序过程等价（p.6–7, “mathematically equivalent to a sequential update”）。

方法段落推进序列为：

`state_problem → define_component → explain_mechanism → instantiate_algorithm → derive → give_intuition → connect_to_prediction → connect_to_experiment`

它把三项设计分别映射到引言障碍：MLP in-place 对应 architectural compatibility；chunk-wise/CP 对应 computational efficiency；future-token target 与 Theorem 1 对应 objective misalignment。复杂度只以硬件并行、throughput 和 memory 语言描述，没有给出渐近复杂度式或算子级 FLOP/通信量分解。

### 5.2 公式与理论对象清单

本读将 **17 个公式** 记为 16 个带编号公式（Eq. 1–16）加 1 个 Preliminary 中的未编号 generic TTT update rule；p.6 对 reconstruction target 的不等式是 Eq. (6) 的正文重复，未再次计数。自动正则表达式的 provisional 计数为 17，是因为把状态上标 `(0)` 与 equation labels 混合计数；该偏差单列于第 10 节。

| # | 标签 | 页码/章节 | 内容作用 | 角色 | 证据 |
|---:|---|---|---|---|---|
| 1 | Unnumbered generic TTT update | p.3, §2 | `Wi ← Wi−1 − η∇W L(fWi−1(ki),vi)`；定义 fast-weight update | `explanation` | p.3, §2, “Given a learning rate η, the update rule is” |
| 2 | Eq. (1) | p.5, §3.2 | `Wdown(i)=Wdown(i−1)+η V̂[i]ᵀ Z[i]`；LM-aligned gradient update | `core_chain` | p.5, §3.2, “gradient with respect to the fast weights” |
| 3 | Eq. (2) | p.6, §3.3 | 正确 token logit 的期望增量下界 | `guarantee` | p.6, §3.3, “Correct logit increases” |
| 4 | Eq. (3) | p.6, §3.3 | 其他 token logit 的期望变化上界 | `guarantee` | p.6, §3.3, “Other logits almost unchanged” |
| 5 | Eq. (4) | p.17, App. B | Theorem 1 restatement 的正确 logit 下界 | `guarantee` | p.17, App. B, “Correct logit increases” |
| 6 | Eq. (5) | p.17, App. B | restatement 的其他 logit 上界 | `guarantee` | p.17, App. B, “Other logits almost unchanged” |
| 7 | Eq. (6) | p.17, App. B | reconstruction target 对正确 logit 的小变化界 | `guarantee` | p.17, App. B, “reconstruction target…negligible” |
| 8 | Eq. (7) | p.17, App. B proof | 从 `ΔWdown` 到任意 logit 的展开 | `explanation` | p.17, App. B, “resulting change in the logit” |
| 9 | Eq. (8) | p.17, App. B proof | 标量项重排为 embedding × activation 内积 | `explanation` | p.17, App. B, “we can rearrange the terms” |
| 10 | Eq. (9) | p.17, App. B proof | 对 representation 取期望并使用线性性 | `explanation` | p.17, App. B, “Applying the linearity of expectation” |
| 11 | Eq. (10) | p.17, App. B proof | 将确定 target 向量移出期望 | `explanation` | p.17, App. B, “factor them out of the expectation” |
| 12 | Eq. (11) | p.17, App. B proof | 用 Assumption 2 将求和化为唯一 key-value 项 | `explanation` | p.17, App. B, “simplifies the summation to a single term” |
| 13 | Eq. (12) | p.17, App. B proof | NTP target 下正确 token 的 logit 期望 | `explanation` | p.17, App. B, “Case 1: NTP-Aligned Target” |
| 14 | Eq. (13) | p.17, App. B proof | 由 embedding magnitude 得 Eq. (4) 下界 | `guarantee` | p.17, App. B, “This gives us the lower bound” |
| 15 | Eq. (14) | p.17, App. B proof | 由近似正交性得错误 token 上界 | `guarantee` | p.17, App. B, “applying Assumption 1” |
| 16 | Eq. (15) | p.18, App. B proof | reconstruction target 下正确 logit 的表达 | `explanation` | p.18, App. B, “Case 2: Reconstruction Target” |
| 17 | Eq. (16) | p.18, App. B proof | reconstruction target 的 `ε` 上界 | `guarantee` | p.18, App. B, “Taking the absolute value gives the bound” |

四项理论对象按物理出现与职责拆分为：

1. **Assumption bundle**：Approximate Orthogonality of Embeddings 与 Key-Query Alignment（p.5）；前者给 `ε` 与 `cnorm`，后者给 `calign` 与无关位置零期望。
2. **Theorem 1 main statement**（p.6）：LM-Aligned target 提高正确 next-token logit，并近似保持其他 logit 不变；reconstruction target 没有相同预测增益。
3. **Theorem 1 restatement**（p.16–17）：在 Appendix B 以精确界重述，供证明使用。
4. **Proof of Theorem 1**（p.17–18）：从 Eq. (7)–(16) 逐步展开两种 target 的 logit effect。

Theorem 1 属于核心因果链中的 **conditional guarantee**，证明与实验之间的连接由 Figure 3(c) 的 objective ablation 提供；它没有证明任意任务、任意 embedding 或任意 optimizer 下的通用提升。

### 5.3 算法与方法图

- **Algorithm 1：In-Place TTT with Context Parallelism (Single Layer)**（p.18, Appendix C）。输入为 CP 切分的 `{X(i)}T i=1`、预训练 `θ`、`Conv1D` kernel、`Wtarget`、`η`；循环 1 并行计算 attention、`Z`、target 与 `ΔWi=ViᵀZi`，`CUMSUM` 聚合，循环 2 以前序 `Si` 更新 `Wdown` 并输出 `Oi`，文档边界重置到预训练 `Wdown(0)`。关键不变量是 chunk `i` 只使用 `<i` 的 fast-weight updates；causal padding 防止 `Vi` 看到未来 token（p.18, Algorithm 1, “Effective weight for chunk i uses updates from chunks < i”）。
- **Figure 1**（p.6）：把 Attention、Gated Linear Layer、Split into chunks、Apply、Update、Conv1D & Projection 放入一个 apply-then-update 流程，传达结构兼容与因果顺序；正文以 Figure 1 作为总体框架入口（p.6, caption “apply-then-update cycle”）。

## 6. 实验设计

论文明确列出 Q1–Q3：Q1 是预训练 LLM 的 drop-in enhancement，Q2 是 from-scratch 与既有 TTT 比较，Q3 是关键 design choices（p.7, §4）。实验顺序对应引言的三个主张，但没有单列理论预测的 induction-head 检验。

| 设计项 | 状态 | 具体事实 | 证据 |
|---|---|---|---|
| 预训练 drop-in 对照 | observed | Qwen3-4B-Base 与 `+ In-Place TTT` 使用完全相同 continual-training curriculum，方法是唯一变量。 | p.7, §4.1, “Both models undergo the exact same continual training curriculum” |
| 两阶段 continual training | observed | Stage 1 约 20B tokens/32k，Stage 2 约 15B/128k；Stage 2 用 YaRN；RULER 覆盖 4k–256k。 | p.8, §4.1；p.19, Table 6 |
| 跨模型扩展 | observed | LLaMA-3.1-8B、Qwen3-14B-Base，约 20B tokens、32k、Conv size 5；Qwen3-14B 另报 64k+YaRN。 | p.8, Table 2；p.20, Table 7 |
| from-scratch 500M/1.5B 对照 | observed | In-Place TTT 与 SWA、GLA、DeltaNet、LaCT 比较；500M/1.5B 均以 32k sequence length 训练。 | p.9, §4.2, “Various competitive baselines are compared” |
| 4B 扩展 | observed | Full Attention 与 SWA 各有 baseline/I.P. TTT；120B tokens、8k context。 | p.9, §4.2；p.19, Table 5 |
| 数据与任务 | observed | Sliding Window Perplexity 使用 Pile 与 Proof-Pile-2 validation；下游为 HellaSwag、ARC-E、ARC-C、MMLU、PIQA、RULER。 | p.9, §4.2 |
| 评价指标 | observed | RULER/commonsense 为平均 accuracy (%)；长上下文曲线为 fixed final block 的 sliding-window perplexity；效率为 prefill TPS 与 peak memory。 | p.7, Table 1；p.9, §4.2；p.10, Figure 4 |
| 硬件与框架 | observed | 训练/评估使用 Nvidia H800；commonsense 使用 `lm-evaluation-harness`，长上下文使用 `opencompass`。 | p.20, D.2, “All evaluation are conducted on Nvidia H800 GPUs” |
| 优化与预算 | observed | from-scratch 使用 AdamW；500M/1.5B 为 20B/60B tokens，4B 为 120B；continual 阶段学习率 5e-6、weight decay 0.1。 | p.19, Tables 4–6 |
| 控制变量 | observed | Qwen3-4B 的 baseline 与 In-Place TTT 共享 curriculum；from-scratch 对照按 attention/backbone 与 TTT 组合比较。 | p.7, §4.1；p.9, §4.2 |
| 随机种子与重复 | not_present | 未报告 random seeds、run 数、跨 run 聚合或 seed-level dispersion。 | p.19–20, Tables 4–8；“All models are trained…” |
| 数据泄漏/切分 | not_present | 说明 Pile/Proof-Pile-2 与自建 continual/pretraining mixture，但未给 train/validation 去重、泄漏检测或 document split protocol。 | p.9, §4.2；p.18–19, D.1 |
| 预注册假设/失败判定 | not_present | Q1–Q3 被列出，未给方向性阈值、预先失败标准或停止规则。 | p.7, §4, “research questions” |
| 估计不确定性 | not_present | 主表与四幅图均未显示 error bars、置信区间或显著性检验；Table 1–3 仅报告聚合分数。 | pp.7–10, Tables 1–3/Figures 2–4 |
| 稳定性处理 | observed | Qwen3-4B 评估对超阈值 `||ΔWdown(i)||F` 做 rescaling，`τ=1e-5`，以控制长上下文累积。 | p.20, D.2, “This prevents the accumulated updates from growing unboundedly” |

复现粒度在正文中保持决策核心（模型/对照/上下文长度/主指标），训练数据组成、硬件、超参数、clipping、架构和初始化移入 Appendix D。算法与理论证明也分别移至 Appendix C/B；因此正文能理解因果链，但无法独立重建训练 run 或验证数值稳定性。

## 7. 结果、统计与可视化

### 7.1 视觉对象清单

| 对象 | 页码/模块 | 尺寸与编码 | 传达的信息 | 证据 |
|---|---|---|---|---|
| Figure 1 | p.6 / method | 全宽流程图；箭头编码时序，框编码 Attention/MLP/Conv/Projection | `apply → update`、chunk state 与 causal target 的模块关系。 | p.6, Fig.1 caption, “module operates sequentially on input chunks” |
| Table 1 | p.7 / results | 7 个 context-length 列；accuracy (%)；best value bold | Qwen3-4B-Base 与 In-Place TTT 的 4k–256k RULER 对比。 | p.7, Table 1 |
| Table 2 | p.8 / results | 两个 base models、Baseline/I.P. TTT、4k–64k 与 64k+YaRN | LLaMA-3.1-8B 与 Qwen3-14B-Base 的外推/跨模型扩展。 | p.8, Table 2 |
| Figure 2 | p.8 / results | 两个折线面板；x 为 context length，y 为 perplexity；无误差带 | 500M/1.5B 在 Pile validation 上随上下文增加的 sliding-window perplexity。 | p.8, Fig.2 caption |
| Table 3 | p.9 / results | Full Attn./SWA 与 Baselines/I.P. TTT 行；多任务 accuracy | 4B common-sense 与 RULER 的规模/attention 组合结果。 | p.9, Table 3 |
| Figure 3 | p.9 / ablation | 三个柱状面板；state、chunk、objective 分组 | state size 扩展、chunk-size trade-off、Conv/Proj 组件作用。 | p.9, Fig.3 caption |
| Figure 4 | p.10 / ablation | 四面板；throughput 与 peak memory，SWA/Full × 8k/32k/128k | In-Place TTT 的效率 overhead 对照。 | p.10, Fig.4 caption |
| Algorithm 1 | p.18 / appendix | 14 行伪代码；两次并行循环、中间 CUMSUM、boundary reset | Context Parallel implementation 与 causality invariant。 | p.18, Algorithm 1 |
| Tables 4–6 | p.19 / appendix | 超参数表；500M/1.5B、1.7B/4B、two-stage | from-scratch 与 Qwen3 continual training budgets/configs。 | p.19, Tables 4–6 |
| Table 7 | p.20 / appendix | LLaMA-3.1-8B/Qwen3-14B 超参数 | 跨模型 continual training 配置。 | p.20, Table 7 |
| Table 8 | p.20 / appendix | 500M/1.5B architectural configuration | hidden size、layers、heads、FFN、window、vocab、RoPE base。 | p.20, Table 8 |

### 7.2 主要结果与统计处理

1. **Qwen3-4B drop-in（Table 1）**：Baseline → In-Place TTT 的 RULER 平均 accuracy (%) 为 4k `96.6→96.1`（−0.5）、8k `94.1→95.6`（+1.5）、16k `92.1→92.7`（+0.6）、32k `88.7→89.3`（+0.6）、64k `74.3→78.7`（+4.4）、128k `74.8→77.0`（+2.2）、256k `41.7→43.9`（+2.2）。作者重点解释长上下文增益与 256k extrapolation；4k 有小幅回落，未单独讨论（p.7–8, Tables 1；“clear trend”）。统计为 RULER task aggregation 的 average accuracy，没有 seed、方差、区间或显著性处理。
2. **跨模型与 YaRN（Table 2）**：LLaMA-3.1-8B 在 4k/8k/16k/32k/64k 分别 `93.9→94.4`、`92.1→93.0`、`92.5→93.3`、`91.1→91.7`、`81.6→83.7`，最大报告差为 64k `+2.1`；Qwen3-14B 在 4k/8k/16k/32k/64k/64k+YaRN 分别 `96.8→97.2`、`95.0→95.7`、`94.6→95.2`、`90.7→91.2`、`67.9→70.6`、`81.3→82.5`，64k 为 `+2.7`、YaRN 为 `+1.2`。统计仍为平均 accuracy，未给 dispersion（p.8, Table 2）。
3. **from-scratch sliding-window perplexity（Figure 2）**：500M 与 1.5B 两个面板中，In-Place TTT 曲线在展示的 context lengths 上低于 SWA、GLA、DeltaNet、LaCT；曲线随 context 增加持续下降至 32k。图中只有点线，没有数字表格、误差带或重复次数，因此可以支持排序与趋势，不能支持精确差值或跨 seed 稳健性（p.8, Fig.2 caption；p.9, “consistently achieves lower perplexity”）。
4. **4B downstream（Table 3）**：Full Attention 的 RULER-4k/8k/16k 从 `45.77/38.09/6.58` 变为 `49.98/43.82/19.99`，差值 `+4.21/+5.73/+13.41`；SWA 从 `14.77/9.91/5.07` 变为 `28.33/26.80/7.57`，差值 `+13.56/+16.89/+2.50`。common-sense 任务以 average accuracy 形式逐任务报数，Full Attn. 的 ARC-C `33.19→32.34` 下降，SWA 的 PIQA `72.58→72.03` 下降，其余列变化较小且方向不完全一致。作者的 “consistently improved across most” 与表中这两个回落相容，但“consistent”不能读成所有任务均提升（p.9–10, Table 3；p.10, “across most common sense reasoning tasks”）。
5. **State/chunk/objective ablation（Figure 3）**：state size 面板以 `4×/1×/0.5×` 比较启用层数，柱高随 state 扩展上升；chunk 面板比较 `C=256/512/1024/2048`，`512` 与 `1024` 最优，作者称 `1024` 更高效；objective 面板比较 `w Conv, Proj`、`w/o Conv`、`w/o Proj`、`w/o Conv, Proj`，作者解释 Conv 对 long context 更关键、`Wtarget` 对 short context 更关键。图只提供柱状读数，未列原始表值或误差（p.9–10, Fig.3 caption；p.10, §4.3）。
6. **效率（Figure 4）**：4B、SWA/Full、8k/32k/128k 的 prefill TPS 与 peak memory 柱形对照；作者结论为 practical scenarios 中 overhead negligible。图没有标注具体数值、batch/重复以外的统计摘要或误差，附录只给 batch size 1 和 H800（p.10, Fig.4 caption；p.20, D.2）。

## 8. 消融、负面结果与自我设限

| 消融/边界 | 状态 | 识别目标与观察 | 证据 |
|---|---|---|---|
| state size | observed | 通过启用层数控制 fast-weight state；更大 state 对 RULER 分数更有利。 | p.9–10, Fig.3(a), “performance improves as the state size scales” |
| chunk size | observed | `C=512` 与 `C=1024` 竞争性最好，`C=1024` 效率更优；显示更新粒度与并行度的 trade-off。 | p.9–10, Fig.3(b) |
| LM-Aligned components | observed | Conv1D 与 `Wtarget` 同时保留时最好；Conv 关联 long context，projection 关联 short context。 | p.9–10, Fig.3(c) |
| efficiency overhead | observed | Figure 4 对比 throughput/memory，结论为 negligible overhead；数值与重复信息不足。 | p.10, Fig.4；p.20, D.2 |
| downstream negative cells | observed | Table 3 的 Full-Attn ARC-C、SWA PIQA 低于各自 baseline；作者未给 failure-case analysis。 | p.9, Table 3 |
| 任务/模型异质性 | observed | Qwen3-4B、LLaMA-3.1-8B、Qwen3-14B、500M/1.5B/1.7B/4B 与两种 attention 组合被覆盖。 | pp.7–10, Tables 1–3/Figures 2–3 |
| optimizer/loss 替代 | not_present | 方法声称可与 loss/optimizer 正交，但正文没有替代 optimizer 或 loss 的实验。 | p.7, §3.4, “an exploration we leave…for future work” |
| 在线流式 deployment | not_present | 所有实验为离线 continual pretraining/evaluation proxy；没有交互 stream、forgetting、interference 或部署 latency study。 | p.7, §4, “language modeling tasks…as a practical proxy” |
| 理论机制直接检验 | not_present | induction-head assumptions 产生条件界，但没有直接测量 `calign`、embedding orthogonality 或 logit intervention。 | p.5–6, §3.3；p.17–18, App. B |

显式自我设限分布如下：

- **scope / causality**：用 language-modeling tasks 作为 long-horizon evolving task 的 practical proxy（p.7）；因此 continual-learning 影响是外推，不是直接 online-agent 证据。
- **compute**：from-scratch 最高 120B tokens，continual 两阶段约 35B，硬件固定为 H800（p.19–20）。
- **data**：自建 mixture 只给大类组成，没有数据规模、比例、去重与公开版本（p.18–19, D.1）。
- **metric**：RULER 与 common-sense 主要报平均 accuracy；Figure 2/4 缺少原始数值与 dispersion（pp.7–10）。
- **generality**：实验对象集中于 decoder-only Transformer、SwiGLU/RoPE 与指定 model families；efficient backbones 的集成被留到 future work（p.16, Appendix A）。
- **deployment**：continual-pretrained Qwen3 采用 inference-time clipping `τ=1e-5`，说明长上下文数值稳定性是实际运行条件（p.20）。
- **ethics**：Ethics Statement 说本文是 foundational architecture，没有 immediate direct real-world applications，同时承认 LLM bias 与 responsible deployment 需求（p.11）。

## 9. 结论、闭环与附录职责

### 9.1 结论段落编码

结论只有一段（p.10）：`restate_problem → restate_method → recover_results → scope/impact`。它回收三项设计（MLP in-place、chunk-wise、LM-aligned objective）、两条证据线（预训练 drop-in 与 from-scratch baseline）和 continual-learning 方向，没有引入新数字或新理论对象（p.10, §5, “We introduced In-Place Test-Time Training”）。

### 9.2 闭环矩阵

| 引言主张 | 方法回应 | 理论/机制回应 | 实验/消融回应 | 结论回应 | 状态 | 证据 |
|---|---|---|---|---|---|---|
| MLP in-place 可作为 drop-in enhancement | 更新 `Wdown`，保留 `Wup/Wgate` 与 attention | Figure 1 的结构兼容 | Table 1–2 跨预训练模型；同 curriculum | 明确重述 drop-in | partially_closed：需要 continual pretraining、未报告真正零重训成本/初始化前后行为曲线 | pp.4, 7–8, 21 |
| chunk-wise/CP 提升效率且保持因果 | apply-then-update、prefix scan、causal padding、boundary reset | 算法给出顺序等价不变量 | Figure 4 throughput/memory | 重述 scalable solution | partially_closed：算法路径清楚，实测 overhead 缺少数值与重复 | pp.6–7, 10, 18 |
| LM-aligned target 比 reconstruction 更适合 NTP | Conv1D future target + `Wtarget` + Eq. (1) | Theorem 1 与 App. B proof | Figure 3(c) 组件消融 | 重述 theoretically-grounded objective | partially_closed：理论依赖 stylized assumptions，未做 direct mechanism test | pp.5–6, 9–10, 16–18 |
| Qwen3-4B 长上下文增强至 128k/256k | two-stage continual training、clipping | 无独立 theorem | Table 1 | 回收长上下文提升 | closed（限于 RULER average accuracy 与测试配置） | pp.7–8, Table 1 |
| 方法跨 4B–14B/YaRN 有效 | 保持 MLP integration 与 target design | 无独立 theorem | Table 2 | 回收 generality | closed（限于两种扩展模型与指定训练预算） | p.8, Table 2 |
| from-scratch 胜过竞争 TTT/efficient attention | SWA backbone 与 baselines 对齐 | 无独立 theorem | Figure 2；4B Table 3 | 回收 strong baselines | partially_closed：Figure 2 只有曲线，Table 3 的 ARC-C/PIQA 有回落且非同一 baseline 集 | pp.8–10, Figures 2–3/Table 3 |
| state/chunk/objective 是关键设计选择 | state scaling、chunk C、Conv/Proj | Theorem 与机制给动机 | Figure 3 | 回收 deeper insights | closed（图示趋势层面） | p.9–10, Fig.3 |
| In-Place TTT 开启 continual learning paradigm | fast weights 随输入更新 | 条件 induction-head guarantee | 语言建模 proxy | 以 “promising step” 收束 | partially_closed：没有 streaming interaction、forgetting、online task 或 broader deployment 证据 | pp.1, 7, 10–11 |

### 9.3 附录清单

| 附录 | 页码 | 分类 | 对象与正文调用 | 依赖影响 | 证据 |
|---|---:|---|---|---|---|
| A Related Work | 16 | `other` | 3 个比较段；正文没有单独章节调用，方法/实验保留关键引用 | 不影响方法复现，但把最近邻比较从正文移走 | p.16, Appendix A |
| B Proof of Theorem 1 | 16–18 | `proof` | p.6 写 “proof is provided in Appendix B”；p.11 Reproducibility Statement 再次调用 | Theorem 的完整推导依赖本附录 | pp.6, 11, 16–18 |
| C Context Parallel Algorithm | 18 | `extended_method` | p.7 写 Algorithm 1 in Appendix C；p.11 以 pseudocode 调用 | CP 实现与 boundary reset 依赖本附录 | pp.7, 11, 18 |
| D Experiment Details | 18–21 | `reproducibility` | p.7 说明 detailed settings 在 D；p.9/10 调用 D.1–D.3；p.11 宣称 comprehensive details | 数据、训练预算、clipping、架构、初始化依赖本附录 | pp.7, 9–11, 18–21 |
| D.1 Details of Datasets | 18–19 | `dataset_detail` | §4 与 Appendix D 的 dataset calls | 自建 mixture 仍缺比例与版本 | pp.7, 18–19 |
| D.2 Details of Training and Evaluation | 19–20 | `hyperparameter` | p.7–10 的 training/evaluation calls | 数值复现、效率测量与 clipping 依赖本节 | pp.8–10, 19–20 |
| D.3 Details of Model Configuration | 20–21 | `implementation_detail` | p.9、p.10 调用 D.3；包括 every-sixth-layer 与初始化 | 预训练兼容性与 state placement 依赖本节 | pp.9–10, 20–21 |
| E Usage of LLMs | 21 | `other` | 无正文调用 | 只声明 grammar/readability 用途，不支撑科学主张 | p.21, Appendix E |

附录约 2,442 词，约为正文主段落（约 5,700 词）的 43%；它把 proof、algorithm、训练/模型细节和相关工作后置。正文仍保留 Table 1–3、Figure 1–4、Q1–Q3、Eq. (1) 与 Theorem 1，因此决策链可读；依赖附录才能复现的是 CP 的精确边界处理、H800/预算/超参数、clipping、初始化和数据大类组成。附录没有提供 seed、run-level logs、每任务 RULER 分解或 failure cases。

## 10. 自动测量核对与词频/修辞

### 10.1 测量分歧

1. `auto_metrics.csv` 对本 PDF 给出 `pdf_pages=21`、`figures=4`、`tables=8`、`algorithms=1`，这四项与人工 PDF 核对一致。
2. 自动章节探测因标题排版为小型大写加字母间空格，无法识别 `R EFERENCES`；它给出 provisional `main_end_page=21`、`appendix_start_page=15`。人工依据版面与标题修正为正文 p.1–10、references p.11–15、appendix p.16–21（p.11 为混合 front matter + references）。
3. 自动 `numbered_equations_provisional=17` 来自唯一标签 `(0)`–`(16)`；其中 `(0)` 是 `Wdown(0)` 等状态/初始化上标，不是独立公式。人工保留 16 个带编号公式并加入 p.3 的 generic TTT update，得到 17 个公式；p.6 reconstruction bound 作为 Eq. (6) 的正文重复记录，不重复计数。
4. 自动 `theorem_items=4` 统计四次 “Theorem 1” 字符串出现；人工将其整理为 4 个理论对象：两项假设、main theorem、restatement、proof，其中 theorem/restate/proof 的物理段落均保留定位。该差异属于“字符串提及”与“职责对象”的口径差异。
5. 自动全文词数约 10,284 包含 references、公式碎片与表格；本备忘的页/节词数仅作版面估计，不把自动总词数当作正文分母。

### 10.2 高频词与论证修辞（references、公式碎片、表格数值和模板固定语排除后的人工语境标注）

- **领域实词**：`TTT`、`fast weights`、`LLM`、`MLP`、`context`、`token`、`chunk`、`objective`、`attention`、`target`、`update`、`long-context`、`parallelism`。
- **二元/三元词组**：`In-Place TTT`、`fast weights`、`LM-Aligned objective`、`Next-Token Prediction`、`chunk-wise update`、`context parallelism`、`pre-trained LLMs`、`long-context evaluation`、`sliding window perplexity`。
- **主张动词**：`introduce`（提出框架）、`repurpose`（复用 MLP）、`replace`（目标替换）、`align`（与 NTP 对齐）、`enable`（能力主张）、`validate`/`demonstrate`/`confirm`（结果段）、`establish`（结论扩张）。这些动词集中于 abstract、§1、§4、§5；`show` 主要出现在结果叙述。
- **限定词/比较词**：`typically`、`often`、`potentially`、`e.g.`、`in particular`、`crucially`、`consistently`、`superior`、`negligible`、`promising`；其中 `consistently` 同时出现在 Figure 2/Table 2 的排序描述与较宽泛的结论句。
- **因果词**：`therefore`、`consequently`、`to tackle`、`to achieve`、`grounded in`、`enabling`、`leading to`；主要把三项 barrier 映射到三项 design choice。
- **强/弱主张比例（定性）**：正文强主张（`fundamentally`, `critical`, `superior`, `highly scalable`, `guaranteed`）明显少于机制/条件句，约为少数段落中的关键词；弱化主张通过 `promising step`、`practical proxy`、`leave ... future work` 表达。精确原始 token 计数由汇总脚本统一完成，本单篇只标注语境和误切分风险。
- **误切分风险**：`In-Place`、`Test-Time`、`Next-Token`、`long-context`、`from-scratch`、`LM-Aligned` 可能被一般 tokenizer 拆成多词；`Wdown`、`Conv1D`、`RULER`、`YaRN` 是机器/领域标识，应保留整体。

## 11. 最终判断

1. **单一主线**：把 MLP 的 final projection `Wdown` 变成可在线更新的 fast weights，以 in-place 兼容性承接预训练 LLM；再用 future-token `Conv1D + Wtarget` target、chunk-wise update 和 CP 扫描把动态记忆接入 NTP（pp.4–7, §§3.1–3.4）。
2. **正文保留的决策关键**：三项 barrier、MLP/Wdown 选择、Eq. (1)、Theorem 1、Figure 1、Q1–Q3、Table 1–3、Figure 2–4，以及每个消融的方向性结论；这些对象足以解释为何测长上下文、跨模型、from-scratch 与 efficiency（pp.5–10）。
3. **附录迁移与自足性**：proof、Algorithm 1、数据/训练/架构/初始化和相关工作全部后置；正文调用点清楚，科学决策链仍可扫读，但复现实验和判断 theorem assumptions 的边界需要附录（pp.6–7, 11, 16–21）。
4. **最有效模式**：把 `barrier → component → update equation → direct benchmark` 排成一一对应链，并用 Table 1 的 context-length axis、Figure 3 的组件拆除和 Figure 4 的运行代价覆盖能力/机制/成本三个问题（pp.2, 5, 7–10）。
5. **最大缺口**：理论只覆盖 induction-head、近似正交 embedding 与期望 logit effect；实验则没有 direct mechanism measurement、seed-level uncertainty、数据泄漏协议、online forgetting/interference 或真实 stream evaluation，因果解释因此停留在条件性和 proxy 层面（pp.5–7, 9–11, 17–20）。
6. **可迁移规则**：对在线适配方法，先固定“更新哪一个既有参数、更新是否严格因果、目标是否对应最终预测”三项接口，再让每项接口各有一条可定位公式、一个机制消融和一个运行代价结果（pp.4–7, 9–10）。
7. **规则边界**：该规则适用于有明确状态转移与预测目标的序列模型；当模型依赖外部检索、非自回归生成、交互式 agent reward 或跨模态状态时，需要重新定义 target、因果边界和可观测的机制检验，不能直接把本论文的 NTP/induction-head guarantee 外推（pp.5–7, 16）。

## 12. 证据覆盖

本备忘将摘要句、引言动作、方法/理论对象、实验设计、结果、消融、限制和闭环条目视为实质判断；每条均附物理页码、章节和短证据锚点。`substantive_claims=约 78`，`claims_with_page_evidence=约 78`，状态为 `complete`。公式与图表的重复说明共享同一物理对象证据，不额外制造主张。

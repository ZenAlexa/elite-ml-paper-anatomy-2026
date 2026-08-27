# P-GenRM 深读备忘

## 1. 论文身份与读取边界

- `paper_id`: `iclr-2026-af6a7ff26bd9`
- 标题：P-GenRM（Personalized Generative Reward Model with Test-time User-based Scaling）
- 会议与等级：ICLR 2026，Oral
- 作者：Pinyi Zhang、Ting-En Lin、Yuchuan Wu、Jingyang Chen、Zongqi Wang、Hua Yang、Ze Xu、Fei Huang、Yongbin Li、Kai Zhang
- 实际来源：`corpus/pdfs/iclr-2026-af6a7ff26bd9.pdf`，官方 ICLR proceedings PDF；无单独 supplementary 文件。
- 读取范围：PDF 物理页 1–29，包含正文、Acknowledgments、References、Appendix A–C、全部图表、Algorithm 1 和提示词页面。

### 页级地图

PDF 共 29 页。正文为第 1–10 页，References 为第 11–13 页，Appendix 从第 14 页开始并延伸至第 29 页。正文采用 LaTeX 双栏排版，Figure 1 和 Figure 2 为跨栏流程图，Figure 3 为跨栏双面板曲线图，Figure 4 为跨栏分布与案例图；第 8–10 页的表格与正文并排或跨栏浮动，造成部分语义模块跨页。附录中的提示词以整页单栏图像呈现，Figure 9–15 传达的是提示模板而非新模型结构。

| 物理页 | 版面或显式标题 | 语义模块 | 估计词数 | 说明 |
|---|---|---|---:|---|
| 1 | Abstract；1 Introduction 起始 | abstract；introduction | 418 | 摘要与引言首段同页 |
| 2 | Figure 1；1 Introduction 续 | introduction | 785（本页，含流程图文字） | 引言完成贡献列表 |
| 3 | 2 Related Works；3 Problem Formulation | related_work；method | 554 | 公式（1）–（2） |
| 4–6 | Figure 2；4 Methodology | method | 1,795（含流程图文字） | 三阶段训练、prototype refinement、公式（3）–（9） |
| 7 | 5.1；5.2 起始 | experimental_design；results | 627 | 数据集、设置、基线与主结果叙述 |
| 8 | Table 1–3；5.2 续 | results；ablation | 395 | 主结果、缩放、组件消融、adaptive vs. static |
| 9–10 | Figure 3–4；Table 4–5；5.3–5.5；6 | results；conclusion | 976 | prototypes、OOD、policy 训练、结论 |
| 11–13 | Acknowledgments；References | other | 1,191 | 非正文语义模块 |
| 14–21 | Appendix A | appendix；limitations | 5,290 | 预备实验、鲁棒性、案例、成本、策略训练、限制 |
| 21–22 | Appendix B | appendix | 620 | 数据集与基线细节 |
| 23–29 | Appendix C | appendix | 568 | 五类 judge prompt 图像 |

机器测量的英文词元总数为 13,202。按版面人工校正后，正文 5,533、References 1,191、附录 6,478；模块词数是用于论文级聚合的估计量，包含相应图表标题与图内文字。

## 2. 摘要逐句功能编码

| 序号 | 摘要句子 | 词数 | 功能 | 限定词、数字与比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | Personalized alignment of large language models seeks to adapt responses to individual user preferences, typically via reinforcement learning. | 18 | `object_scope` | “typically”限定训练范式；对象是 personalized alignment | p.1，Abstract，“adapt responses to individual user preferences” |
| 2 | A key challenge is obtaining accurate, user-specific reward signals in open-ended scenarios. | 12 | `problem_gap` | “key”标出主要困难；场景是 open-ended | p.1，Abstract，“accurate, user-specific reward signals” |
| 3 | Existing personalized reward models face two persistent limitations: (1) oversimplifying diverse, scenario-specific preferences into a small, fixed set of evaluation principles, and (2) struggling with generalization to new users with limited feedback. | 32 | `problem_gap` | 两项限制；比较对象为 existing personalized reward models | p.1，Abstract，“two persistent limitations” |
| 4 | To this end, we propose P-GenRM, the first Personalized Generative Reward Model with test-time user-based scaling. | 16 | `core_idea`、`method` | “first”是优先性主张；方法名首次完整出现 | p.1，Abstract，“the first Personalized Generative Reward Model” |
| 5 | P-GenRM transforms preference signals into structured evaluation chains that derive adaptive personas and scoring rubrics across various scenarios. | 18 | `method`、`core_idea` | 结构化 evaluation chain；跨场景 adaptive persona/rubric | p.1，Abstract，“structured evaluation chains” |
| 6 | It further clusters users into User Prototypes and introduces a dual-granularity scaling mechanism: at the individual level, it adaptively scales and aggregates each user’s scoring scheme; at the prototype level, it incorporates preferences from similar users. | 36 | `method` | individual 与 prototype 两个粒度 | p.1，Abstract，“dual-granularity scaling mechanism” |
| 7 | This design mitigates noise in inferred preferences and enhances generalization to unseen users through prototype-based transfer. | 16 | `qualitative_result`、`impact_claim` | 机制解释是 noise reduction 与 transfer | p.1，Abstract，“prototype-based transfer” |
| 8 | Empirical results show that P-GenRM achieves state-of-the-art results on widely-used personalized reward model benchmarks, with an average improvement of 2.31%, and demonstrates strong generalization on an out-of-distribution dataset. | 29 | `quantitative_result`、`qualitative_result` | 2.31%；SOTA；OOD 数据集 | p.1，Abstract，“average improvement of 2.31%” |
| 9 | Notably, Test-time User-based scaling provides an additional 3% boost, demonstrating stronger personalized alignment with test-time scalability. | 16 | `quantitative_result`、`impact_claim` | 3%；相对对象是未缩放 P-GenRM（正文给出更细数值） | p.1，Abstract，“additional 3% boost” |

摘要的功能序列为对象范围 → 缺口 → 两项失败 → 方法命名 → evaluation chain → 双粒度机制 → 机制解释 → 基准结果 → test-time 增益。摘要没有理论定理或形式保证，也没有直接列出限制。最强主张被放在末两句，优先突出 SOTA、OOD 泛化和约 3% 缩放收益。

## 3. 引言论证推进

| 段落动作 | 页码 | 上一段留下的问题 | 当前段回答 | 下一段钩子 | 证据 |
|---|---:|---|---|---|---|
| `context → problem` | 1 | 通用 RLHF 无法覆盖个体偏好 | 个性化 alignment 在开放式对话中依赖主观评价，显式信号稀疏、隐式历史嘈杂 | 混合信号仍有两个未解限制 | p.1，Introduction，“Explicit preference signals are often sparse” |
| `failure_of_prior_work` | 1 | 混合 demographics、behavior、context 是否足够 | 固定 evaluation rules 丢失场景变化，冷启动用户泛化弱 | 需要能随场景变化并转移的 reward model | p.1，Introduction，“Static modeling of preferences” |
| `core_idea → method_preview` | 2 | 缺少可执行的开放域个性化 reward | P-GenRM 用 persona prior 和显式 cue，训练 PSI、CRE、hard-negative curriculum 三阶段 | 结构化 evaluation chain 如何运行 | p.2，Introduction，“three-stage training framework” |
| `method_preview → result_preview` | 2 | 生成的偏好分析有噪声，新用户历史稀疏 | 用 prototype-based dual-granularity scaling 聚合个人样本并转移相似用户偏好 | 基准、缩放收益与可扩展性 | p.2，Introduction，“two questions” 与 “prototype-based, dual-granularity scaling” |
| `contribution_list` | 2 | 需要压缩论文承诺 | 三项贡献分别覆盖 P-GenRM、test-time scaling、SOTA 与新用户泛化 | 正文进入 related work | p.2，Introduction，“main contributions of this paper” |

引言的动作链可写为 `context → problem → failure_of_prior_work → missing_insight → core_idea → method_preview → result_preview → contribution_list`。贡献列表与摘要存在重叠，但加入了“first personalized generative reward model”和可扩展性主张；数字结果只在前一段的 “additional 3%” 中出现，列表本身不再重复数字。贡献主张可证伪，但“first”依赖相关工作范围，“strong generalization”依赖后文合成 OOD 排名。

## 4. 相关工作

相关工作集中在第 3 页独立章节，分成三段。正文未再逐篇展开已列方法，附录 A.4 只补充 user preference modeling 的若干方向。

| 段落 | 编码 | 比较维度 | 本文定位 | 证据 |
|---|---|---|---|---|
| Personalized alignment of LLMs | `taxonomy`、`nearest_neighbor_contrast`、`limitation_of_prior` | 参数个性化、推理时 steering、latent/prototype/MoE、multi-dimension、linear reward、persona prompt | 将 SynthesizeMe 指为最相近参照，并指出其 static design 不能适应 context-dependent preference | p.3，“its static design cannot adapt to context-dependent and shifting user preferences” |
| User Preference Modeling | `taxonomy`、`credit_or_foundation`、`positioning_only` | explicit attributes、system-prompt combinations、group preference transformer | 承认 preference modeling 的多领域基础，正文只做短定位 | p.3，“more details can be found in Appendix A.4” |
| Generative Reward Models | `taxonomy`、`credit_or_foundation`、`nearest_neighbor_contrast` | next-token verifier、generative judge、principle/critique scaling、process reward | 借用 GenRM 的泛化、解释性与 test-time scaling 能力，未给出定量比较 | p.3，“support for test-time scaling” |

相关工作主要承担分类、近邻对比和继承关系三种功能。引用在方法中再次承担 GRPO、K-means、prototype transfer 的基础作用，但没有形成独立理论比较表。

## 5. 方法与理论

### 5.1 形式化对象与核心链

第 3 页将当前 query 记为 `q_t`，用户为 `u`，历史偏好对为 `y_τ+` 与 `y_τ−`。历史集合 `H_t^(u)` 通过随机抽样限制为 `h` 条。显式 criteria `E^(u)` 与历史行为共同作为 preference signals。P-GenRM 先生成场景相关的文字 preference model `P_t^(u)`，再生成带权 rubrics 的 scoring scheme `S_t^(u)`，对每个候选 `y_t^i` 提取标量 `s_t^i`。公式（1）–（2）把“混合信号 → 文本 evaluation chain → 可提取分数”串成论文的最小任务定义。

### 5.2 三阶段训练

1. **Persona-guided Scoring Induction（PSI，SFT）**。Instruction LLM 读取历史与显式 criteria，先写 scenario-specific persona，再派生 preference criteria，并按 criteria 评分候选。Rejection sampling 过滤出的 Structured Evaluation Chain（SEC）数据用于 SFT。附录 A.2 的 prompt-engineering 试验以 PRISM 15% 测试集和 OpenAI o3-2025-04-16 为 judge，五次独立运行的 ACC 从 N-CoT 62.42 提升到 Persona 64.02，Persona+OSR+SDim 为 66.17，构成 PSI 的设计动机。
2. **Criteria-based Reasoning Enhancement（CRE，RL）**。给模型有限历史，先推断 plausible explicit preference，再生成同样的 evaluation chain。LLM-as-a-judge 以 0–1 分数 `PR_t` 评价过程是否覆盖用户显式或合成 criteria；rule-based outcome reward `OR_t` 检查 chosen response 的最终分数是否高于 rejected response，格式错误另罚 −0.1。总 reward 是 `R_t = α·PR_t + β·OR_t`，默认 `α=0.5, β=1.0`。论文使用 GRPO，并同时给出带 clipping、relative advantage 和 KL 项的目标函数。
3. **Hard negative-aware Curriculum Learning（RL）**。逐步提高 hard negative 比例，以扩大困难样本覆盖；这一阶段关闭 process-level reward，只保留 outcome reward 的同形 objective。正文没有给出 hard-negative 比例、增长 schedule 或训练步数。

### 5.3 Prototype 初始化、精炼与 test-time scaling

离线阶段用 Qwen3-Embedding-0.6B 将每个 `P_t^(u)` 嵌入并跨场景拼接为 `P`，对 `P` 做 K-means，得到 `k` 个 prototype centroids。History-aware Attentive Prototype Refinement 对关联用户随机抽取的历史进行编码，用当前 query 与 prototype 对历史记录加权，再将 prototype、query 和历史聚合向量组成先验 `z_t`。`L_pair` 使先验偏向正反馈，cluster-center 与 previous-state 两项正则限制 prototype 漂移；更新每个 prototype 后重新把样本分配到最近 prototype。

在线阶段有两个平均通道。Individual-level scaling 对当前用户并行采样 `m` 个 preference analyses 与 scoring schemes；prototype-level scaling 将用户指派至最近 prototype，取 embedding 相似的 `n` 个用户，生成额外评分。公式（8）定义两组生成，公式（9）将个人与相似用户得分分别求平均后相加。设计意图是用多次个人假设降低推断噪声，用同 prototype 用户作转移先验应对冷启动。

### 5.4 公式清单

PDF 中编号公式（1）–（9）共 9 个。另有一个未编号但独立 display 的 `J_GRPO(θ)` 目标函数，以及一个行内的历史三元组编码定义；两者不是编号公式。公式均服务于方法核心链，没有 theorem、lemma、proposition、corollary 或 proof。

| 标号 | 物理页 | 内容与作用 | 理论角色 |
|---|---:|---|---|
| (1) | 3 | `H_t^(u) = {(q_1,y_1+,y_1−), …, (q_{t−1},y_{t−1}+,y_{t−1}−)}`，定义历史输入 | `core_chain` |
| (2) | 3 | `[P_t^(u); S_t^(u)] ~ R_θ(q_t,H_t^(u),E^(u),y_t^i)`，并由 `Extract(S_t^(u))` 取分数 | `core_chain` |
| (3) | 5 | `R_t = α·PR_t + β·OR_t`，合并 process 与 outcome reward | `core_chain` |
| 未编号 | 5 | `J_GRPO(θ)`，对 sampled chains 的 clipped ratio、relative advantage 和 `−βD_KL(π_θ||π_ref)` 优化 | `core_chain` |
| (4) | 6 | `v_H = Σ_τ α_τo_τ`，`α_τ` 同时使用 query 与 prototype 注意力项 | `core_chain` |
| (5) | 6 | `z_t = a_j + λ_qW_qq_t + λ_sW_sv_H`，形成 prototype-informed prior | `core_chain` |
| (6) | 6 | `Δ_t = z_t^⊤y_t+ − z_t^⊤y_t−`，`L_pair = −logσ(Δ_t)` | `core_chain` |
| (7) | 6 | `L = L_pair + λ_cent||a_j−μ_j||_2^2 + λ_tr||a_j−p_j||_2^2`，限制中心偏离与跨步漂移 | `core_chain` |
| (8) | 6 | 并行生成个人 scheme 与相似用户 scheme | `core_chain` |
| (9) | 6 | `s_t^i = (1/m)Σ_x Extract(S_{t,x}^i) + (1/n)Σ_w Extract(S_{ti}^{(u_w)})`，聚合最终分数 | `core_chain` |

### 5.5 方法动作序列、算法与图

方法段的动作转移序列为 `setup_notation → state_problem → define_component → explain_mechanism → derive → give_intuition → instantiate_algorithm → state_complexity → connect_to_prediction → connect_to_experiment → summarize`。其中 `state_complexity` 只在 test-time scaling 的“modest increase”与附录 inference-time 实验中出现，正文没有渐近复杂度式或内存界。

Algorithm 1 位于 Appendix A.10 第 22 页。输入包括初始 prototypes、cluster means、用户当前 query、偏好对、随机抽样历史、`λ` 参数、权重矩阵和学习率；循环遍历每个 prototype，编码历史、计算 prototype-augmented attention、更新 prior、计算 pairwise loss 与两项正则，梯度更新后重分配最近 prototype。正文只在第 6 页以一句话调用它，算法解释粒度低于公式链。

## 6. 实验设计

| 设计对象 | 论文给出的事实 | 复现粒度与缺口 | 证据 |
|---|---|---|---|
| PersonalRewardBench | Chatbot Arena-personalized 与 PRISM-personalized，覆盖开放域对话和主观偏好 | 第 7 页说明任务范围；用户数、pair 构造在 Appendix B.1 | p.7，5.1，“three popular personalized alignment datasets” |
| Chatbot Arena / PRISM | Appendix B.1 给出 131 与 720 名用户；PRISM 的 N-way 评分转 pairwise，并移除质量差小于 10% 的 pair | 未给出完整 train/test 数量与用户隔离细节 | p.21，B.1，“data from 131 users” 与 “contains data from 720 users” |
| LaMP-QA | OOD personalized long-form QA，Arts & Entertainment、Lifestyle & Personal Development、Society & Culture 三类，超过 45 个子类 | 候选响应与 rubric 由附录流程构造，非原始固定 ground truth | p.21，B.1，“three major categories” |
| 模型与硬件 | PersonalRewardBench 使用 LLaMA-3.1-8B 与 70B；LaMP-QA 仅 8B；8B/70B 分别用 8/32 GPUs，70B 使用 LoRA | GPU 型号、训练步数、batch、学习率等正文未完整给出 | p.7，5.1，“8/32 GPUs” 与 “using LoRA” |
| 训练组件 | `α=0.5`、`β=1.0`；prototype embedding 为 Qwen3-Embedding-0.6B；PSI instruction model 为 OpenAI o3 | hard-negative schedule、`h`、`k` 及大多数优化超参缺失 | p.7，5.1，“The weight parameters α and β … are 0.5 and 1.0” |
| 基线 | in-context judge、Bradley–Terry、GPO、VPL、PAL、SynthesizeMe、FT RM + SynthesizeMe、o3 + PSI | scaling rows 主要报告 8B，70B 对应位置为空 | p.7–8，5.2 与 Table 1 |
| 指标与重复 | PersonalRewardBench 以 accuracy 评价；主表写明五次独立运行并报告 mean ± standard error | 未报告 p-value、多重比较校正或 effect size | p.8，Table 1，“mean ± standard error” |
| OOD 排名 | 六个生成模型产生候选，三名高级 LLM 按隐藏 rubric aspects 打分形成 ranking；reward model 在三条历史反馈下预测，用 Spearman correlation 比较 | 三名 judge 形成的 ranking 是替代 ground truth，非人工金标准 | p.18，A.7，“compute the Spearman rank correlation coefficient” |
| 泄漏与随机化控制 | 论文未描述用户级 train/test 隔离、去重、数据泄漏检查或固定随机种子 | 该缺口影响跨用户泛化解释 | p.7，5.1；p.21，B.1，未见相应控制说明 |

实验顺序与引言主线大体对应。Table 1 先检验总体 accuracy，Table 2–3 检验训练组件与 adaptive persona，Figure 3–4 检验 prototype，Table 5 检验稀疏反馈 OOD，Appendix A.9 与 A.13 补成本和 policy downstream。设计中缺少预先列出的研究问题、明确失败判定、完整预算和用户隔离协议。

## 7. 结果、统计与可视化

统计汇总单位主要是 benchmark pair 或 ranking 任务，主表以五次独立运行的 mean ± standard error 表示。论文没有在主结果中给出 p-value、multiple-comparison procedure、bootstrap 或 Bayesian analysis。Appendix A.13 额外给出五次运行的 standard error 与 95% CI；未报告独立假设检验。

| 结果 | 定量证据 | 比较对象与统计处理 | 作者解释及不利解释 | 定位 |
|---|---|---|---|---|
| PersonalRewardBench 总体 | P-GenRM-8B 为 Chatbot Arena 72.68±1.85%、PRISM 65.32±0.56%；70B 为 73.42±1.74%、66.21±0.76% | 与 FT RM、GPO、VPL、PAL、SynthesizeMe 和 judge baseline 比较；五次 mean±SE | 作者称跨尺度 SOTA；70B 采用 LoRA，scaling rows 没有 70B 结果 | p.8，Table 1 |
| Test-time User-based Scaling | Ind-8,Pro-4 为 74.30/67.54；Ind-16,Pro-8 为 75.92/68.06。相对未缩放的绝对差为 Chatbot +3.24 pp、PRISM +2.74 pp，均值 +2.99 pp | Table 4 同时展示 Ind-only、Pro-only 与混合设置；五次 mean±SE | 个人与 prototype 通道组合最优；Pro-only 8 为 66.90/57.65，显示相似用户分数不能单独替代个人采样 | p.8，Table 1；p.9，Table 4 |
| 与 prior SOTA 的差距 | 正文称 8B 平均提升 2.77%，70B 平均提升 1.99%，P-GenRM-8B 比此前最佳 70B 平均高 1.04% | “平均”跨两个 PersonalRewardBench 数据集；未给出逐项差值计算 | 基线包含 FT RM + SynthesizeMe；不同模型规模与 LoRA 使横向解释受限 | p.7，5.2 |
| Adaptive vs. Static Personas | Qwen3-8B + PSI 64.22/58.01，高于 +SMe 62.57/56.33；o3 + PSI 69.14/63.87，高于 o3 + SMe 67.73/58.49 | LLM-as-a-judge 条件；五次 mean±SE | 支持场景自适应 persona；仍是 prompt/judge 结果，未独立测量 persona 识别准确率 | p.8，Table 3；p.9 |
| Prototype 数量 | 0、25、50、100、125 个 prototype 的 Chatbot accuracy 为 72.68、73.23、74.30、73.69、73.45；PRISM 为 65.32、66.29、67.54、67.28、67.19 | Figure 3 与 Table 13；五次 mean±SE，PCA retained variance 只作选择依据 | 50 后平台或回落，作者归因于过细分组引入 inference noise；缺少对不同随机聚类的独立稳健性 | p.9，Figure 3；p.20，Table 13 |
| Prototype 异质性案例 | Figure 4 显示组内共享 fluency/factuality，个体仍有 creativity 等差异；Figure 6–7 展示同一用户在 music 与 serious discussion 下权重变化 | 视觉案例与文字说明，没有 participant-level 检验 | 直观支撑 intra-group similarity 与 inter-group heterogeneity；案例不能单独确立 causal mechanism | p.10，Figure 4；p.16–18，Figures 6–8 |
| LaMP-QA OOD | P-GenRM-8B + Ind-8,Pro-4 的 Arts、Pers.、Soc.、Avg. 为 0.543、0.714、0.657、0.638 | Spearman rank correlation；三类子集；地面 ranking 由六个生成模型和三名 judge 构造 | Avg 高于 Qwen3-235B-A22B 的 0.619；合成 judge ranking 使“ground truth”具有代理性质 | p.10，Table 5；p.18，A.7 |
| Inference time | P-GenRM-8B 14:16；Ind-8,Pro-4 18:22；Ind-16,Pro-8 23:05；后者相对未缩放增加 8:49 | Chatbot Arena-Personalized 全测试集；vLLM、8×A100；prop. model API 并发上限 40 | 作者将成本归因于一次共享 prompt KV cache 与并行 sampling；未给 token 数或吞吐量 | p.19，Table 11 与 A.9 |
| Policy downstream | Llama3.1-8B-Instruct-DPO 3.316，GRPO 3.354；70B base 为 3.156；五次运行的 95% CI 分别 [3.303,3.329]、[3.334,3.374] | 三个 judge 以 1–5 评分后取平均；附录以 CI 不重叠支持“statistically significant” | 8B policy 超过 70B baseline；样本为同一 Chatbot Arena-Personalized，judge 仍是 LLM ensemble | p.20–21，Tables 14–15 |

正文图表清单如下。Figure 1 是总流程，Figure 2 是三阶段训练与 evaluation chain，Figure 3 是 prototype 数量选择，Figure 4 是用户–prototype 分布与案例；Table 1 为总体基准，Table 2 为组件消融，Table 3 为 adaptive/static，Table 4 为 scaling 组合，Table 5 为 LaMP-QA。附录 Figure 5–15、Table 6–15 与 Algorithm 1 见附录职责部分。

## 8. 消融、负面结果与自我设限

| 消融或边界 | 结果与识别目标 | 证据与判断 |
|---|---|---|
| 去除 CL | Chatbot 72.68→71.07，PRISM 65.32→63.82 | Table 2；支持 hard-negative curriculum 的增量作用 |
| 去除 CL 与 process reward | 70.22/62.70 | Table 2 与 Table 7 的 `α=0,β=1` 对应；过程 reward 贡献是在同时去除 CL 的条件下测得 |
| 去除 CL 与 outcome reward | 69.05/60.94 | Table 2 与 Table 7 的 `α=1,β=0` 对应；不能等同于 full-model 单变量删除 |
| 去除 CL、RL | 66.76/57.08 | Table 2；支持 RL 阶段整体作用 |
| 再去除 SFT | 56.37/52.04 | Table 2；接近无个性化提示的 baseline，说明 SFT 是初始化能力来源 |
| α–β 敏感性 | α=.5,β=1 为 71.07/63.82；α=.5,β=.5 为 70.65/63.33；α=1,β=0 为 69.05/60.94；α=0,β=1 为 70.22/62.70 | Table 7；同时显示两类 reward 都有用途，过度 process 权重可能过拟合 criteria |
| 历史样本数 | 1、2、3、4 对 preference pairs 的 accuracy 为 59.78、64.62、72.68、72.50 | Table 12；3 条成为训练和评测设置，4 条没有继续提升 |
| prototype 数量与 scaling 组合 | 50 个 prototype 最优；Ind-16,Pro-16 回落到 72.59/64.61；Ind-0,Pro-8 为 66.90/57.65 | Figure 3、Table 4、Table 13；支持适度 prototype transfer，但也暴露过细分组与纯 prototype 的负结果 |

消融占正文篇幅很小，主文只有 Table 2 和对应两段说明。附录把 α–β、macro accuracy、history sample 数、prototype 数、latency 与 policy downstream 分开呈现。作者在摘要和引言中使用“strong generalization”“scalability”等正向表述，在附录 A.14 明示两项限制。论文没有人类评测、真实部署、跨语言或更广泛用户群的消融。

## 9. 结论、限制与闭环

### 9.1 结论段

第 10 页的结论只有一段，动作序列为 `restate_problem → restate_method → recover_results → boundary/compute → impact`。它回收结构化、场景感知 evaluation chain、individual/prototype scaling、PersonalRewardBench SOTA、modest compute、稀疏反馈泛化和 personas/rubrics 可解释性；没有引入新的数字或新的方法组件。

### 9.2 闭环矩阵

| 引言主张 | 方法回应 | 实验或附录回应 | 结论回收 | 状态 |
|---|---|---|---|---|
| 场景特定偏好需要动态 persona 与 rubric | PSI/SEC 先生成 `P_t^(u)` 再派生 `S_t^(u)` | Table 3；Figures 6–7 给出跨场景案例 | 明示 scenario-aware chain | `partially_closed`，系统性动态识别量化不足 |
| 推断偏好有噪声 | Individual-level 多次采样并平均 | Table 1、4；Ind-8/16 增益 | 明示 scaling 提升 fidelity | `closed`，但噪声本身未单独估计 |
| 新用户历史稀疏 | prototype 初始化、refinement、相似用户 transfer | LaMP-QA Table 5；三条历史反馈，附录 A.7 | 明示 sparse-feedback generalization | `partially_closed`，OOD ground truth 为 LLM judge 合成 |
| 三阶段训练提升 reward quality | PSI SFT、CRE RL、hard-negative curriculum | Table 2、Table 7 | 结论未逐项回收 | `partially_closed`，主要组件比较带有累积删除条件 |
| P-GenRM 在个性化 reward benchmark 达到 SOTA | structured GenRM + dual scaling | Table 1 与 Table 4 | 明示 SOTA | `closed`，范围限于所列基线、模型和数据集 |
| prototype 同时保留组内共性与个体差异 | K-means、attention refinement、pairwise regularization | Figure 4、Figure 8、Tables 8–10 | 结论只回收 prototype-level scaling | `partially_closed`，图示支撑强于统计识别 |
| test-time scaling 的额外成本有限 | 并行 sampling、共享 prompt encoding、轻量 similarity | Table 11；A.9 | 明示 modest compute cost | `partially_closed`，成本只在一个测试集和硬件配置测量 |
| reward model 能改善 policy training | 将 P-GenRM 接入 DPO/GRPO | Tables 14–15；A.13 | 5.5 在正文给出，结论未回收 | `closed`，但只覆盖一个 policy 数据与 LLM judges |
| evaluation chain 提供可解释性 | persona、weighted criteria、score breakdown | Figure 2；Figures 6–7；Appendix C prompts | 结论明示 interpretability | `partially_closed`，没有用户或专家可解释性研究 |

### 9.3 限制与缺失

| 限制 | 类型 | 证据 |
|---|---|---|
| 需要生成 evaluation chain，单纯推理速度可能慢于直接输出 scalar reward | `compute`、`deployment` | p.20，A.14，“less efficient than reward models that directly produce scalar values” |
| 需要三条历史 preference selections 才能形成合理分析，实际收集成本中等 | `data`、`deployment` | p.20，A.14，“relies on three historical preference selections” |
| LaMP-QA 的 ranking ground truth 由生成模型与三名 LLM judge 构造，缺少人工金标准 | `metric`、`causality` | p.18，A.7，“three highly-advanced LLMs” 与 p.10，5.4 |
| 训练/测试用户隔离、随机种子、hard-negative schedule、完整优化超参和 scaling token budget 未报告 | `data`、`generality`、`compute` | p.7，5.1；p.21，B.1；完整 PDF 未见相应说明 |

### 9.4 不利信息的呈现策略

| 策略 | 可核对的呈现 | 评价 |
|---|---|---|
| `附录迁移` | macro accuracy、95% CI、latency、history 数、prototype 数与 policy 细节主要放 A.5、A.9、A.11–A.13 | 主文保持短，但泛化和下游能力依赖附录才完整可核查 |
| `正面聚焦` | 主结果段强调 “additional 3% gain”“modest increase”，表中 scaling 的 70B 单元为空 | 数值存在，比较范围受模型规模与报告缺失限制 |
| `累积消融` | Table 2 的 process/outcome reward 行都写成 `w/o CL, ...`，没有 full-model 单独 `w/o PR` 或 `w/o OR` | 可识别阶段差异，无法把每个 reward 的边际效应完全分离 |
| `代理指标替代` | LaMP-QA 用三名 LLM 给 rubric aspects 打分后形成 ground ranking，再用 Spearman correlation | 过程稳定性有描述，外部效度仍受 judge ensemble 影响 |
| `案例代表` | Figure 4、6、7、8 用少量用户/场景展示异质性，正文写 non-cherry-picked 但未给完整抽样表 | 有机制直觉，不能替代系统性用户级检验 |
| `统计语气强化` | A.13 以 95% CI 不重叠表述“statistically significant”，没有配套 p-value 或预注册检验 | 区间信息可复核，显著性措辞超出所报告检验细节 |

## 10. 附录职责

附录占 16 个物理页，按正文 10 页计，页面比为 1.6。它承担设计动机、额外结果、复现细节、案例、成本、下游策略和 prompt 模板；正文仍保留主 benchmark、主要 scaling、核心 ablation、prototype 选择曲线、OOD 表和一段结论。

| 附录模块 | 页码 | 类别 | 对象与正文调用 | 对主张的作用 |
|---|---:|---|---|---|
| A.1 The Use of Large Language Models | 14 | `other` | ChatGPT 5 仅用于语言润色和语法检查；正文未调用 | 说明作者声明，未补充方法证据 |
| A.2 Preliminary Experiments on Effectiveness of User Persona | 14 | `additional_result` | Table 6；正文 4.1 指向该 preliminary finding | 支撑 persona 与显式 criteria 进入 PSI |
| A.3 The Impact of Variations in α and β | 14–15 | `ablation` | Table 7；正文 5.1 指向 | 补充 reward 权重敏感性 |
| A.4 User Preference Modeling | 15 | `other` | 正文 related work 指向 Appendix A.4 | 补充领域背景，不提供新实验 |
| A.5 Performance Across Different Prototypes | 15–17 | `robustness` | Figure 5、Tables 8–10；正文 5.2 指向 macro accuracy | 检验长尾 prototype 与 minority-group macro accuracy |
| A.6 Example of a Single User’s Differing Preferences | 16–17 | `qualitative_example` | Figures 6–7；正文 5.2 指向 | 展示同一用户在不同场景改变权重 |
| A.7 Evaluation Framework Used in LaMP-QA | 18 | `dataset_detail` | 正文 5.4 指向 Appendix A.7 | 定义六个生成模型、三名 judge、三次历史与八次 scaling 平均 |
| A.8 Visualization of User–Prototype Distribution | 18 | `qualitative_example` | Figure 8；正文 5.3 指向 Appendix 8 | 扩展用户–prototype 图示 |
| A.9 Comparisons of Inference Time | 19 | `additional_result` | Table 11；正文 5.2 指向 A.9 | 提供 latency、部署与并行化解释 |
| A.10 History-aware Attentive Refinement Algorithm | 19–22 | `extended_method` | Algorithm 1；正文第 6 页指向 Appendix 1 | 把公式化精炼过程落为伪代码 |
| A.11 Number of Samples Required for Generating Reasonable User Preference | 19–20 | `ablation` | Table 12；正文 5.2 指向 A.11 | 选择三条历史 preference pairs |
| A.12 P-GenRM’s Performance under Different Numbers of Prototypes | 20 | `ablation` | Table 13；正文 5.3 指向 A.12 | 给出 0–125 prototype 的均值与 SE |
| A.13 P-GenRM for Policy Model’s Training | 20–21 | `additional_result` | Tables 14–15；正文 5.5 指向 A.13 | 连接 DPO/GRPO policy downstream |
| A.14 Limitations | 20 | `other` | 正文结论不逐项调用 | 明示 chain generation 成本与三条历史要求 |
| B.1 Dataset | 21–22 | `dataset_detail` | 正文 5.1 指向 Appendix B.1 | 用户数、数据构造、类别和隐藏 rubric |
| B.2 Existing Personalized Reward Models | 22 | `extended_method` | 正文 5.2 指向 Appendix B.2 | GPO、VPL、PAL、SynthesizeMe 的实现摘要 |
| C Prompts | 23–29 | `implementation_detail` | Figures 9–15；正文方法未逐图调用 | 暴露 preference synthesis、PSI、CRE 和四类 judge prompt |

附录没有 theorem proof、正式复杂度分析、用户研究、伦理/社会影响章节或训练代码配置表。正文对 A.2、A.3、A.5、A.7、A.9、A.11、A.12、A.13 有显式引用；A.10、A.14 和 C 主要靠章节邻接或图示承担复现与限制信息。正文自足性在主 benchmark 判断上尚可，在 OOD ranking 构造、latency 分解、macro accuracy、policy downstream 与完整 prompt 方面依赖附录。

## 11. 用词与修辞

以下是基于第 1–10 页抽取文本的语境标注，排除了 References；数字、公式碎片、图表标签和模板固定语会造成少量误切分。统一 lexical script 的严格词形归一化应以汇总阶段输出为准。

- 高频领域词：`P-GenRM` 约 49 次，`prototype/prototypes` 合计约 44 次，`test-time/user-based` 组合约 33 次，`preference/preferences` 与 `scoring/score/scores` 构成方法叙事的主词群。
- 高频机制短语：`test-time user-based scaling`、`persona-guided scoring induction`、`curriculum learning`、`Chatbot Arena`、`P-GenRM`。前三者分别对应推理扩展、训练阶段和困难样本策略。
- 高频主张动词：正文抽取中 `propose` 约 8 次、`introduce` 约 4 次、`show/demonstrate` 约 5 次、`achieve` 约 6 次、`outperform` 约 5 次。它们集中在引言、结果叙述和结论，方法段更多使用 `infer`、`derive`、`generate`、`aggregate`。
- 高频限定与对比词：`limited`、`sparse`、`strong`、`additional`、`however`、`while`。限定词常与新用户、历史反馈、成本和 prototype 数量绑定；“strong”主要修饰 generalization、performance、effectiveness。
- 强主张与弱主张：强主张集中在 “first”“state of the art”“significantly outperforms”“strong generalization”；弱化位置出现在 “we believe”“suggesting”“may introduce inference noise” 和 A.14 的 limitation。强主张有表格数值承接，弱主张常用于机制解释或外推边界。
- 写作动作：先在引言把两个缺口压缩为 static preference 与 cold start，再用三阶段训练和双粒度 scaling 对应；结果按 benchmark → adaptive/static → prototype → OOD → policy 排列。图 1/2 先给全局可视路径，表 1/4 再给 scaling 数值，形成读者先理解对象、后比较收益的阅读顺序。

## 12. 最终判断

- **单一主线**：把用户的稀疏、嘈杂、场景变化偏好转译为带 persona 与 weighted rubric 的生成式 evaluation chain，再以 individual sampling 与 prototype transfer 在 test time 聚合分数。
- **正文保留的决策关键内容**：问题定义、三阶段训练、`R_t` reward、prototype refinement 的公式骨架、dual-granularity scaling、主 benchmark、组件消融、prototype 选择、OOD 表和结论。
- **移入附录的细节**：prompt 模板、用户群分布、macro accuracy、α–β、历史样本数、prototype 数表、latency、policy DPO/GRPO、数据集与基线描述。迁移使正文保持可扫读，但 OOD 代理 ground truth、成本分解和下游显著性只能在附录核查。
- **最有效的模式**：Figure 1 用一张跨栏图把 hybrid signals、persona、rubric、individual/prototype aggregation 串成闭环；Figure 2 再把训练 reward 与 evaluation chain 对齐；Table 4 用同一预算下的 Ind/Pro 组合暴露互补性。
- **最大缺口**：没有正式理论保证，scaling 的“降噪”和 prototype 的“转移”主要由 accuracy、合成 OOD ranking 和定性图示间接支撑；训练/测试隔离与完整预算也未报告。
- **可迁移规则**：当方法主张同时包含生成式解释和 test-time aggregation 时，正文应把对象、生成链、聚合算子、基准结果和至少一个机制消融放在同一因果顺序中。
- **规则边界**：该规则适用于以可解释生成链和推理时计算换取个性化评分的 reward/judge 方法；若论文核心是 formal guarantee、在线用户实验或安全部署，需将证明、干预设计或故障边界提升到正文，而不能只保留图示和附录代理指标。

## 13. 证据覆盖与测量校正

所有实质判断均绑定物理页、章节和不超过 20 个英文词的短证据或图表编号；本篇 `evidence_coverage` 记为 `complete`。以下校正保留自动测量与人工版面判断的差异。

1. 自动 heading detector 将 References 读成 `R EFERENCES`，因此把 `main_end_page_provisional` 误报为 29；根据 p.11 的 References 起点与 p.14 的 Appendix 起点，正文边界校正为 p.1–10。
2. 自动 Appendix 起点误报为 p.2，导致 `appendix_words_provisional=12679`；实际 Appendix 起点是 p.14，校正附录英文词元为 6,478。
3. 自动表格 caption 去重计数为 12；逐页核对 Table 1–15 共 15 个，主要漏计了并排 caption 与 Appendix 页面中的表格。
4. 自动编号公式计数为 9，与物理页的公式（1）–（9）一致。方法页另有未编号的 `J_GRPO(θ)` display，因此 displayed equation 总数为 10。
5. 自动 figure caption 计数为 15、Algorithm caption 计数为 1，与逐页核对结果一致。

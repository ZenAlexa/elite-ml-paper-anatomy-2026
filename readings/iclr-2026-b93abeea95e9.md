# Gaia2：单篇论文深读备忘

## 0. 身份、版本与阅读边界

- **paper_id**：`iclr-2026-b93abeea95e9`
- **标题**：Gaia2 — Benchmarking LLM Agents on Dynamic and Asynchronous Environments
- **会议／年份／等级**：ICLR 2026，Oral。
- **作者**：Romain Froger、Pierre Andrews、Matteo Bettini、Amar Budhiraja、Ricardo Silveira Cabral、Virginie Do、Emilien Garreau、Jean-Baptiste Gaya、Hugo Laurençon、Maxime Lecanu、Kunal Malkan、Dheeraj Mekala、Pierre Ménard、Gerard Moreno-Torres Bertran、Ulyana Piterbarg、Mikhail Plekhanov、Mathieu Rita、Andrey Rusakov、Vladislav Vorotilov、Mengjue Wang、Ian Yu、Amine Benhalloum、Grégoire Mialon、Thomas Scialom。首页署名单位为 Meta SuperIntelligence Labs（p.1）。
- **实际读取版本**：官方 ICLR proceedings PDF `corpus/pdfs/iclr-2026-b93abeea95e9.pdf`，对应文本 `corpus/text/iclr-2026-b93abeea95e9.txt`；物理页 1–32 全部读取。PDF 来源为 `https://proceedings.iclr.cc/paper_files/paper/2026/file/c26a67e0470774df98c12480ec5d2d7b-Paper-Conference.pdf`，OpenReview forum 为 `https://openreview.net/forum?id=9gw03JpKK4`。
- **补充材料边界**：没有独立 supplementary 文件；论文把 Appendix A–B 嵌入同一 PDF，覆盖 p.15–32。分析以该 official proceedings 版的文字、公式、图表和版面为准。
- **阅读范围**：p.1 标题／摘要／Figure 1，p.2–10 正文，p.11 acknowledgement 与 references 起始，p.11–14 references，p.15–32 appendix，包含 Figure 11–19、Table 4–7、verifier hacking、parallel tool-calling ablation、noise-level experiment。

## 1. 页级地图与版面

### 1.1 文档边界

| 区域 | 物理页 | 估计词数 | 版面与边界证据 |
|---|---:|---:|---|
| 标题／作者／摘要 | 1 | 230 | p.1 为标题与单栏摘要，摘要后紧接全宽 Figure 1。 |
| 正文 | 1–10 | 约 5,990 | §6 `CONCLUSION & DISCUSSION` 在 p.10 结束；p.11 开始 `ACKNOWLEDGEMENTS`。 |
| Acknowledgements | 11 | 55 | p.11 顶部、`REFERENCES` 之前。 |
| References | 11–14 | 约 2,050 | p.11 开始，p.14 末尾结束；均为双栏参考文献。 |
| Appendix A | 15–22 | 约 4,600 | p.15 `A ARE APPENDIX`，包含 ARE foundations、notification、universe 和 GUI。 |
| Appendix B | 23–32 | 约 4,100 | p.23 `B GAIA2 APPENDIX`，p.32 以 Table 7 结束。 |

正文、references 和 appendix 主要采用双栏版式。p.1 的摘要和 Figure 1 是单栏／全宽区域；p.3 的 Figure 2 跨栏置于页首，Figure 3 位于右栏；p.5 的 Figure 4 为跨栏表格式能力图；p.6 的 Table 1、p.7 的 Table 2 与 Figure 5、p.9 的 Figure 8–9、p.10 的 Figure 10 和 Table 3 均在双栏页面中占据较大宽度。附录的 Figure 11–19 和 Table 4–7 多为单栏浮动体；p.32 的 Figure 19、B.5.2 文字和 Table 7 形成明显的大面积留白。上述版面判断来自 PDF 渲染，文本行数没有用于判断。

### 1.2 章节与语义模块映射

| 章节 | 模块 | 页码 | 估计词数 | 说明 |
|---|---|---:|---:|---|
| Abstract | `abstract` | 1 | 230 | 研究对象、异步缺口、verifier、模型结果和释放目标。 |
| 1 Introduction | `introduction` | 2 | 730 | RLVR 背景、静态 benchmark 缺口、Gaia2／ARE 预览、三项贡献。 |
| 2 Related Work | `related_work` | 2–3 | 450 | agent benchmark 与 verifier 两个比较簇。 |
| 3 ARE: Scaling Up Agent Environments and Evaluations | `method` | 3–4 | 1,350 | ARE 抽象、Mobile、时间、orchestration。 |
| 4 Gaia2: Expanding General Agent Evaluation | `experimental_design` | 4–6 | 820 | scenario 规模、capability splits、annotation protocol。 |
| 4.1 Capabilities Evaluated | `experimental_design` | 5 | 420 | 五个 core capability 与 Noise/A2A augmentation。 |
| 4.2 Scenario Design and Annotation Protocol | `experimental_design` | 5 | 270 | DAG ground truth、独立复核、guardrails、难度校准。 |
| 4.3 Verifier | `method`／`experimental_design` | 6 | 410 | action-level verifier 的规则与 450 条轨迹核验。 |
| 5 Experiments / 5.1 Core Results | `results` | 6–8 | 1,250 | Table 1–2、Figures 5–7 和主分数。 |
| 5.2 Time / 5.3 Agent2Agent | `results`／`ablation` | 8–10 | 820 | instant/default、成本、协作比例、异构团队。 |
| 6 Conclusion & Discussion | `conclusion` | 10 | 260 | 回收框架、模型差异、verifier、orchestration。 |
| Appendix A: ARE Appendix | `appendix` | 15–22 | 4,600 | foundations、notification、universe、GUI。 |
| Appendix B: Gaia2 Appendix | `appendix` | 23–32 | 4,100 | annotation、verification、orchestration、额外实验。 |
| Acknowledgements／References | `other` | 11–14 | 2,105 | 致谢与参考文献，不进入正文语义分母。 |

### 1.3 模块计量（12 个模块各一次）

以下主文词数是按论证段落手工估计的语义词数，约 5,990 词；图表标签、重复页眉、参考文献和公式碎片未纳入。`theory` 与主文 `limitations` 没有独立章节，分别标为 `not_applicable` 与 `not_present`；限制内容主要出现在正文 Discussion 与附录。

| module | status | estimated_words | main_word_share | figures | tables | algorithms | displayed_equations |
|---|---|---:|---:|---:|---:|---:|---:|
| `abstract` | observed | 230 | 0.0384 | 1 | 0 | 0 | 0 |
| `introduction` | observed | 730 | 0.1219 | 0 | 0 | 0 | 0 |
| `related_work` | observed | 450 | 0.0751 | 0 | 0 | 0 | 0 |
| `method` | observed | 1,350 | 0.2254 | 2 | 0 | 0 | 0 |
| `theory` | not_applicable | 0 | 0 | 0 | 0 | 0 | 0 |
| `experimental_design` | observed | 820 | 0.1369 | 1 | 0 | 0 | 0 |
| `results` | observed | 1,250 | 0.2087 | 4 | 2 | 0 | 0 |
| `ablation` | observed | 820 | 0.1369 | 2 | 1 | 0 | 0 |
| `conclusion` | observed | 260 | 0.0434 | 0 | 0 | 0 | 0 |
| `limitations` | not_present | 0 | null | 0 | 0 | 0 | 0 |
| `appendix` | observed | 8,700 | null | 9 | 4 | 0 | 0 |
| `other` | observed | 2,105 | null | 0 | 0 | 0 | 0 |

PDF 中没有编号公式、displayed equations、theorem、lemma、proposition、corollary、proof 或算法环境。ARE 的 event DAG、verifier matching procedure 和 ReAct loop 是文字／图示流程，不应计作算法 caption 或理论结果。

## 2. 摘要逐句功能编码

摘要共 7 句。功能顺序为「对象与环境 → 与静态评测的差异 → write-action verifier → 主要模型结果 → trade-off 与 sim2real 边界 → ARE/Mobile 包装 → 社区用途」。摘要报告了结果数字，但没有 theorem、proof 或正式 limitation 段；最强的 headline 是 `42% pass@1` 和无跨能力支配模型，后面再给开源模型、成本和基础设施意义。

| # | 摘要句子 | 词数 | 功能 | 限定词／数字／比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | We introduce Gaia2, a benchmark for evaluating large language model agents in realistic, asynchronous environments. | 15 | `object_scope`、`core_idea` | `realistic`、`asynchronous`；LLM agents。 | p.1，Abstract；“a benchmark for evaluating large language model agents” (`explicit`) |
| 2 | Unlike prior static or synchronous evaluations, Gaia2 introduces scenarios where environments evolve independently of agent actions, requiring agents to operate under temporal constraints, adapt to noisy and dynamic events, resolve ambiguity, and collaborate with other agents. | 36 | `problem_gap`、`object_scope` | 对比 static／synchronous；temporal、noise、ambiguity、collaboration。 | p.1，Abstract；“environments evolve independently of agent actions” (`explicit`) |
| 3 | Each scenario is paired with a write-action verifier, enabling fine-grained, action-level evaluation and making Gaia2 directly usable for reinforcement learning from verifiable rewards. | 23 | `method`、`theory` | write-action verifier；RLVR。这里 `theory` 仅表示可验证机制，不是定理。 | p.1，Abstract；“fine-grained, action-level evaluation” (`explicit`) |
| 4 | Our evaluation of state-of-the-art proprietary and open-source models shows that no model dominates across capabilities: GPT-5 (high) reaches the strongest overall score of 42% pass@1 but fails on time-sensitive tasks, Claude-4 Sonnet trades accuracy and speed for cost, Kimi-K2 leads among open-source models with 21% pass@1. | 48 | `experimental_setup`、`quantitative_result`、`qualitative_result`、`limitation` | 42%、21%；GPT-5、Claude-4 Sonnet、Kimi-K2；`but fails`、`trades`。 | p.1，Abstract；“no model dominates across capabilities” (`explicit`) |
| 5 | These results highlight fundamental trade-offs between reasoning, efficiency, robustness, and expose challenges in closing the “sim2real” gap. | 17 | `qualitative_result`、`limitation` | `trade-offs`、`sim2real`；没有实测 real-world 对照。 | p.1，Abstract；“challenges in closing the ‘sim2real’ gap” (`explicit`) |
| 6 | Gaia2 is built on a consumer environment with the open-source Agents Research Environments platform and designed to be easy to extend. | 21 | `method`、`impact_claim` | consumer environment；open-source ARE；`easy to extend`。 | p.1，Abstract；“built on a consumer environment” (`explicit`) |
| 7 | By releasing Gaia2 alongside the foundational ARE framework, we aim to provide the community with a flexible infrastructure for developing, benchmarking, and training the next generation of practical agent systems. | 30 | `impact_claim`、`method` | release／community infrastructure；`aim` 表示目标而非已验证影响。 | p.1，Abstract；“flexible infrastructure for developing, benchmarking, and training” (`explicit`) |

## 3. 引言的论证推进

引言主要在 p.2 以两个正文段和一组三项贡献推进。完整链条是：**RLVR 需要可验证反馈且 agent 使用场景进入长时动态环境 → 现有 benchmark 多为静态／同步并忽略中间动作 → Gaia2 用 Mobile、ARE 和 write verifier 把异步事件、时间、噪声、歧义、协作纳入 → 实验揭示模型之间的能力／速度／成本 trade-off → 三项贡献分别固定平台、benchmark 和经验研究边界**。

| # | 主动作 | 估计词数 | 上一段留下的问题 | 当前段回答与下一段钩子 | 证据 |
|---:|---|---:|---|---|---|
| 1 | `context`、`problem_gap` | 180 | RLVR 的可验证反馈适用于哪些 agent 场景？ | 将 reasoning、coding、tool-use 的 RLVR 与长时 dynamic interaction 并置，指出既有评测多 static/synchronous，忽略 intermediate steps。 | p.2，§1；“environments only change when the agents act” (`explicit`) |
| 2 | `core_idea`、`method_preview` | 235 | 怎样把部署中的时间、噪声和协作变成可检验任务？ | 引入 Gaia2、Mobile 和 ARE；用 scenario DAG、write-action verifier 与 human annotation 连接环境变化和 RLVR。下一钩子是 ARE 抽象和能力 taxonomy。 | p.2，§1；“1,120 human-annotated scenarios” (`explicit`) |
| 3 | `result_preview`、`scope_boundary` | 95 | 新 benchmark 是否让模型呈现单一排名？ | 预告 frontier 模型约 42% overall，且 reasoning、speed、robustness、cost 互相牵制；将论文从“更高分”转向多维部署 trade-off。 | p.2，§1；“no system dominates across all capabilities” (`explicit`) |
| 4 | `contribution_list` | 150 | 交付物分别是什么？ | 三项贡献：ARE 通用异步事件平台；Gaia2 统一七类能力的可验证 benchmark；跨 proprietary／open-source 模型的经验研究。 | p.2，`Contributions`；三项 bullet (`explicit`) |

贡献列表没有逐项重复摘要的所有措辞：它把交付物拆成 platform、benchmark、study，但没有预先列出随机种子、最小效应、失败判据或停止规则。可证伪内容主要在实验部分实现，贡献列表本身未承载这些细节。

## 4. 相关工作

相关工作是独立 §2，位于引言与 ARE 方法之前，约 450 词、两个比较簇。第一段按 benchmark 类型组织，涵盖 embodied／web、synthetic app-like、function calling、temporal／multi-agent 和 static final-outcome。第二段按 verification strategy 组织，比较 GAIA exact-match、ToolSandbox milestones／minefields、rubric rewards，以及 Gaia2 的每个 state-changing write action。它没有把 ARE 组件重新写一遍；后文引用主要回到 baseline、scaffold 和 verifier 设计。

| # | 主动作 | 估计词数 | 引用簇与比较维度 | 证据 |
|---:|---|---:|---|---|
| 1 | `taxonomy`、`positioning_only`、`limitation_of_prior` | 235 | ALFWorld、WebShop、WebArena、WorkArena 比 grounded execution；AppWorld、ToolSandbox 比 app-like state verification；BFCL 比 function calling；VendingBench、τ-Bench、τ²-Bench、MultiAgentBench、MCP benchmarks 比 temporal／multi-agent；GAIA、SWE-bench、BrowseComp 被归为 static/final outcome。 | p.2–3，`Benchmarking LLM agents`；“they remain synchronous and agent-driven” (`explicit`) |
| 2 | `nearest_neighbor_contrast`、`gap_creation`、`credit_or_foundation` | 215 | GAIA 的 final exact match 与 ToolSandbox 的 intermediate milestone 对比 write-action verifier；rubric-based rewards 作为柔性判断基础；Gaia2 加入 exact arguments、LLM rubric、causal／temporal constraints。 | p.3，`Verification in agentic benchmarks`；“evaluates every state-changing write action” (`explicit`) |

作者将缺口定义为「异步、事件驱动、跨能力、可验证」的组合。该组合定位得到正文设计和 Table 1 支持；“first benchmark”属于文献覆盖范围型主张，论文未提供系统检索表或统一 matched comparison，因此闭环强度低于工程实现主张。

## 5. 方法与理论

### 5.1 ARE 与 Gaia2 的最小逻辑单元

本文没有独立理论章节。核心形式对象是：`App` 的有状态 API 与工具；包含 apps、time manager、governing rules 的 `Environment`；带时间戳和依赖关系的 `Event`；按 policy 选择性推送的 `Notification`；由初始状态、scheduled events 和 verifier 构成的 `Scenario`；以及 `AgentUserInterface`、`System`、Mobile、main-agent／app-agent。Appendix A.1 将 environment 形式化为具有 states、observations、actions、transition rules 的 MDP，但没有给出数学公式或理论保证（p.16）。

ARE 的因果链是：

1. `Apps` 维护独立状态，工具通过 decorator 分成 read／write；read 用于探索，write 改变环境并承担验证。
2. `Environment` 集合 apps、数据、时间和规则，可同时承载一个或多个 agents。
3. `Events` 包含 tool calls、状态变化、scheduled updates，进入有依赖 DAG 的时间队列；EventLoop 执行并写入 EventLog。
4. `Notifications` 在事件完成后按 low／medium／high policy 暴露，形成可控制的 observability。
5. `Scenarios` 从 initial state 与 event DAG 启动，包含用户请求、中间事件、oracle actions 和 online/offline verification。
6. `Mobile` 将抽象实例化为 12 个 consumer apps、101 个 tools、10 个 universes；每个 universe 含约 400K–800K tokens 的结构化／非结构化内容（不含 filesystem）。
7. ReAct orchestration 每步输出一个 structured-JSON tool call；pre-step 注入排队 notifications，post-step 检查 termination；PTC 作为附录对照。

### 5.2 方法段落动作与机制

| # | 动作 | 内容与前文问题的对应 | 证据 |
|---:|---|---|---|
| 1 | `setup_notation`、`state_problem` | §3 先把 ARE 置于「环境独立演化、时间推进、agent 异步交互」的研究平台边界。 | p.3，§3；“environments evolve continuously and are decoupled from the agent” (`explicit`) |
| 2 | `define_component` | apps、environment、events、notifications、scenarios 五个抽象将可读／可写状态、DAG 和可观察性拆开。 | p.3–4，`Core concepts`；“five abstractions” (`explicit`) |
| 3 | `connect_to_experiment` | 通过重新实现 τ-bench、τ²-bench、GAIA、BFCL-v3、VendingBench，声称 ARE 能复用现有 benchmark。 | p.4，§3；“faithfully reimplement existing agentic benchmarks” (`explicit`) |
| 4 | `explain_mechanism` | 模型生成直接消耗 simulated time，外部 event 可在推理期间发生，因而获得同步评测无法提供的 temporal responsiveness。 | p.4，`Asynchronicity and time`；“the environment clock still advances” (`explicit`) |
| 5 | `instantiate_algorithm` | Mobile 以 synthetic persona 和跨 app dependency graph 生成 coherent universe，状态、工具、时间和终止条件构成消费场景。 | p.4，`Mobile environment`；“400K and 800K tokens” (`explicit`) |
| 6 | `define_component`、`give_intuition` | model-agnostic ReAct 加 pre/post hooks 保持公平；PTC 在 Appendix B.3.2 检查单线程是否成为瓶颈。 | p.4，`Agent orchestration`；“PTC can improve efficiency ... but not performance” (`explicit`) |
| 7 | `state_problem` | §4 将 800 个 core human-annotated scenarios、160 个 `Gaia2-mini` 与两个 augmentation 组合为 1,120 个 scenario。 | p.4，§4；“adding 320 scenarios ... total of 1,120 scenarios” (`explicit`) |
| 8 | `define_component` | five core capabilities 是 Execution、Search、Ambiguity、Adaptability、Time；Noise 与 A2A 是 environment-level modifiers。 | p.5，Fig.4／§4.1；“Core Capabilities ... and Augmentations” (`explicit`) |
| 9 | `contrast_alternative` | 不单设 compositional split：早期将三项以上能力人为混合会产生不自然任务，保留 core split 的 organic compositionality。 | p.5，§4.1；“we explicitly chose not to introduce a separate ‘compositional’ split” (`explicit`) |
| 10 | `instantiate_algorithm`、`connect_to_experiment` | annotator 用 ARE UI 设计 event／write DAG，独立多轮验证、consistency check、guardrails 与 baseline difficulty calibration 形成 oracle。 | p.5，§4.2；“multiple rounds of validation by independent annotators” (`explicit`) |
| 11 | `define_component`、`explain_mechanism` | ARE Verifier 以 minimal oracle write sequence 为目标，read unlimited、独立 goal order-agnostic，避免把探索路径固定下来。 | p.6，§4.3；“goal-oriented rather than path-optimal” (`explicit`) |
| 12 | `derive`、`connect_to_prediction` | Consistency、Causality、Timing、Completeness 四维匹配；exact IDs 与 LLM rubric 文本参数并存，450 labeled trajectories 检查 verifier。 | p.6，Table 1／§4.3；“0.98 agreement and 0.99 precision” (`explicit`) |

方法动作转移序列可写为：`state_problem → define_component → connect_to_experiment → explain_mechanism → instantiate_algorithm → contrast_alternative → instantiate_algorithm → define_component → derive → connect_to_prediction`。这里的 `derive` 是 verifier matching rules 的逻辑推导，不是公式推导。

### 5.3 理论、公式、伪代码与复杂度核对

- **公式**：正文及附录没有 displayed equation、编号公式或公式总数大于零的对象；`pass@1`、成本图的求和说明和表中数值属于文字／图注表达。
- **理论对象**：没有 theorem、lemma、proposition、corollary 或 proof。Appendix A.1.2 的 MDP 只是概念性定义，未给 reward、transition 或 guarantee 的形式化。
- **算法**：没有 `Algorithm` caption 或伪代码框。EventQueue／EventLoop、verifier matching、ReAct pre/post hooks 用文字和 Figure 2、11、18 表达，不能按算法项计数。
- **复杂度**：没有给出 ARE、verifier matching、DAG 调度、notification filtering 或 scenario generation 的时间／空间复杂度。论文报告了每步最多 200 steps、context overflow、timeout 等运行界限，但它们属于评测终止条件。
- **理论在因果链中的角色**：MDP、DAG 和 oracle sequence 是可审计环境与验证保证的解释／设计骨架，不是可证明 generalization guarantee；论文最强的闭环来自 benchmark 构造与 verifier validation。

## 6. 实验设计

### 6.1 设计事实

| 设计项 | 状态 | 事实与复现粒度 | 证据 |
|---|---|---|---|
| 研究问题／预先假设 | `observed` | 没有编号 RQ、预注册或停止规则；§5.1 后段给出两个分析假设：tool exploration／information gathering 驱动成功，token generation 代表 comprehensive reasoning。 | p.7，`Performance drivers`；“Two hypotheses guide our analysis” (`explicit`) |
| benchmark scope | `observed` | 800 个 core、160 个 Gaia2-mini、320 个 augmentation，共 1,120；10 个 Mobile universes，101 tools／universe。 | p.4–5，§4；“800 unique verifiable scenarios” (`explicit`) |
| capability split | `observed` | Execution、Search、Ambiguity、Adaptability、Time 为五类 core；Noise、Agent2Agent 为 augmentation。各 core split 为 160 个 scenario；augmentations 不需新增 annotations。 | p.5、p.23；“160 scenarios per capability split” (`explicit`) |
| scenario／annotation | `observed` | annotators 从 generated Mobile universe 出发，构造 write action 与 environment event DAG；多轮独立验证、consistency check、structural guardrails 和 baseline difficulty calibration。 | p.5；“post-hoc difficulty calibration using a baseline agent” (`explicit`) |
| compositionality | `observed` | 任务被视作 compositional flavors，但不设独立 compositional split；三项以上人工组合在早期测试中缺乏清晰 signal。 | p.5，§4.1；“organic compositionality” (`explicit`) |
| Mobile environment | `observed` | 12 个 apps、101 tools；synthetic coherent data 由 PersonaHub personas 与 dependency graph 跨 app 传播；universe 约 400K–800K tokens。 | p.4；“contacts align across messaging and email” (`explicit`) |
| dynamics／notifications | `observed` | event 可按 absolute 或 relative timestamp 调度，DAG 管依赖；low／medium／high notification policy，medium 是 Gaia2 默认。 | p.16、p.18，Appendix A.1.3–A.2；“medium ... Default in Gaia2” (`explicit`) |
| models | `observed` | Table 2 评估 14 个 proprietary/open-source、reasoning/non-reasoning 模型：Llama 3.3/4、GPT-4o/GPT-5 三级、GPT-OSS、Qwen3 两种、Grok-4、Kimi-K2、Gemini 2.5 Pro、Claude 4 Sonnet 两种。 | p.7，Table 2；模型行名 (`layout_observation`) |
| baseline／scaffold | `observed` | 所有模型使用同一 ReAct-style scaffold；每步一个 structured JSON tool call，pre-step 注入 notifications，post-step 检查终止。 | p.4、p.6；“same baseline ReAct scaffolding” (`explicit`) |
| runtime settings | `observed` | full context ≥128K、temperature 0.5、每 turn 16K generation limit；每 scenario 三次运行；终止于 200 steps、context overflow、verifier completion 或 timeout。 | p.6，`Experimental setup`；“Scenarios are run three times” (`explicit`) |
| time handling | `observed` | outages／rate limits 使用 simulated generation time，响应期间暂停，恢复时匹配时间 offset；Time split 另做 instant mode。 | p.6、p.8；“simulated generation time” (`explicit`) |
| notifications | `observed` | medium 默认只推送高优先级／agent action consequences；用户 `send message to agent` 无论 verbosity 都会通知。 | p.6、p.18；“user ... systematically notified” (`explicit`) |
| metrics | `observed` | 主指标为 scenario `pass@1`；Table 1/5 另报 verifier agreement、precision、recall；Figure 6 报成本／成功耗时，Figure 7 报 LLM calls／output tokens。 | p.6–10、p.29；表注与图注 (`explicit`) |
| randomization／seeds | `observed` | Appendix A.1.2 声明固定 starting state 与 seed 可 deterministic；主实验只说明三 runs，没有列出每个 scenario 的 seed、随机生成方案或逐 run 数值。 | p.16、p.6；“given a fixed starting state and seed” (`explicit`) |
| uncertainty | `observed` | Table 2 per-split 数值有 `±`，但 caption 只说三次运行，没有定义该 `±` 是标准误、标准差或其他 dispersion；Table 3 明确为 standard error。大多数 Figure 没有误差带定义。 | p.7、p.10；Table 2/3 captions (`layout_observation`) |
| human comparison | `observed` | 450 条 hand-labeled trajectories 用于 verifier validation；正文还称 average human annotator 可解决所有任务但比模型慢，GUI 使用差异会影响该比较。 | p.7、p.6；“average human annotator can solve every task” (`explicit`) |
| compute parity／model inclusion | `observed` | provider costs 用 Artificial Analysis 数据；Claude 4 Opus 因高 latency／cost 排除，Grok API Empty Response 带来高 variance；未给全模型统一 wall-clock／FLOPs 预算。 | p.1、p.31；“excluded because of its very high latency and cost” (`explicit`) |
| reasoning output handling | `observed` | Claude/Kimi/Qwen 用 custom stop sequences；reasoning models 的 intermediate reasoning 在每一步被丢弃且不放入后续 context，作者承认对 GPT-5/Claude 可能不最优。 | p.31；“discard intermediate reasoning” (`explicit`) |
| release／packaging | `observed` | 论文声称发布 ARE 和 Mobile/Gaia2，并以社区 benchmark/RL data infrastructure 包装；ARE GUI 的 annotation interface 在写作时尚未 release。 | p.1、p.22；“annotation interface – not released at this time” (`explicit`) |

### 6.2 能力与动态任务的具体定义

| capability | 任务结构 | 关键控制／失败判定 | 证据 |
|---|---|---|---|
| Execution | 长序列 write actions，要求按正确顺序；示例是筛出年龄不超过 24 的 contacts 并逐个加一岁。 | 写操作工具名称和 count、参数与依赖必须匹配；read 不计入 oracle。 | p.5、p.23；Figure 4 与 Execution Task (`explicit`) |
| Search | 多 app read actions 交叉检索；示例按 Chats 的 1-on-1 关系与 Contacts 统计城市，平局取字母序第一。 | 只需一个 final answer write；任何读法均可，最终需 `send_message_to_user`。 | p.5、p.23–24；“Any sequence of read operations ... considered successful” (`explicit`) |
| Ambiguity | 不可能、矛盾或多解任务，例如连续日程存在冲突。 | 单 turn、没有 clarification message；prompt 要求 detect/report ambiguity，完成无歧义步骤后告知用户。 | p.5、p.24–25；“seek appropriate clarification” (`explicit`) |
| Adaptability | 初始 action 后由其后果触发 dependent Env event，agent 要改计划；可加 distractor events。 | 结构为 user ask → agent message → Env event → adaptation；只使用 dependent Env events。 | p.5、p.24–25；“revise its plan in response to delayed outcomes” (`explicit`) |
| Time | 在绝对／相对时刻或事件触发时执行 one-off/recurrent actions；当前场景时长上限 5 分钟。 | 相对 delay >1 秒时，agent action 需落在 `[Δt−5 sec, Δt+25 sec]`；“immediate” 标注 +2 秒 delay。 | p.24–26；Time taxonomy 与 footnote 8 (`explicit`) |
| Agent2Agent | app 被 app-agent 替代；main-agent 通过 messaging 设定 subgoal、获取结果并完成任务，默认 main/app 使用同一模型。 | 研究 ratio `r` 与 heterogeneous team；app-agent on-demand，主 agent 失去直接 app tools。 | p.5、p.24；“partial observability” (`explicit`) |
| Noise | 在 base scenario 上注入 tool anomalies、signature changes、random execution failures 和无关 Env events。 | 以不同 noise level 改变错误概率／随机事件频率；Table 7 只报告 Claude 4 Sonnet。 | p.5、p.32；“increasing noise results in deteriorating performance” (`explicit`) |

## 7. 结果、统计与可视化

### 7.1 图表清单

PDF 共 19 个 Figure、7 个 Table；没有 Algorithm caption。主文 Figure 1–10、Table 1–3，附录 Figure 11–19、Table 4–7。Figure 5 含八个 capability 子图，仍按一个 Figure 计数。

| kind | label | module | page | 传达的信息 |
|---|---|---|---:|---|
| figure | Figure 1 | `abstract` | 1 | 不同 max budget 下各模型 `pass@1` scaling curve；曲线均 plateau，成本与能力没有统一支配。 |
| figure | Figure 2 | `method` | 3 | ARE 的 event-based、time-driven、异步环境、agent/user interface、event queue／log 与 verifier。 |
| figure | Figure 3 | `method` | 3 | Llama 4 Maverick 在 Gaia2 中 12 个 Mobile apps 的 app usage distribution。 |
| figure | Figure 4 | `experimental_design` | 5 | Execution、Search、Ambiguity、Adaptability、Time、Agent2Agent、Noise 七类 capability 和示例任务。 |
| table | Table 1 | `results` | 6 | 450 hand-labeled trajectories 上 In-context Verifier 与 ARE Verifier 的 agreement／precision／recall。 |
| table | Table 2 | `results` | 7 | 14 个模型按七个 split 的 `pass@1`，per-split `±`，overall average。 |
| figure | Figure 5 | `results` | 7 | 七个 capability split 的模型分数柱状图，按能力独立重排。 |
| figure | Figure 6 | `results` | 8 | overall score 与 scenario cost；成功 scenario 的 model/human 时间。 |
| figure | Figure 7 | `results` | 8 | overall score 与平均 LLM calls／output tokens 的关系。 |
| figure | Figure 8 | `results` | 9 | Gaia2-Time default 与 instant；GPT models 的 Time 与 Execution inverse scaling。 |
| figure | Figure 9 | `ablation` | 9 | A2A 的 main/app agent 交换示例与不同 `r` 下每 tool call error frequency。 |
| figure | Figure 10 | `ablation` | 10 | `r=0/0.5/1` 的 `pass@k` 与 token-cost scaling；Llama 获益、Claude trade-off 不改善。 |
| table | Table 3 | `ablation` | 10 | Llama／Claude main-agent 与 app-agent 的四种异构配对 `pass@1`。 |
| figure | Figure 11 | `appendix` | 17 | Event dependency DAG：并行事件、依赖事件、conditional 与 validation。 |
| figure | Figure 12 | `appendix` | 18 | 两 turn scenario 的 sequence diagram；agent 在 turn 间暂停并响应异步 email。 |
| table | Table 4 | `appendix` | 18 | Mobile low／medium／high notification policies 与推送 tool。 |
| figure | Figure 13 | `appendix` | 19 | Mobile apps dependency graph；Contacts 为多数 app 的 root，Shopping/File system 独立。 |
| figure | Figure 14 | `appendix` | 21 | ARE scenario view：event DAG、scenario run、agent logs。 |
| figure | Figure 15 | `appendix` | 27 | oracle／agent matching trajectory 的 failure 与 success。 |
| figure | Figure 16 | `appendix` | 28 | multi-turn scenario 中插入 conditional verifier trigger。 |
| figure | Figure 17 | `appendix` | 29 | agent 将 conditional logic 嵌进 message 以攻击 LLM judge 的 failure case。 |
| table | Table 5 | `appendix` | 29 | 三个 verifier model 在同一 450 条 hand-labeled trajectories 上的指标。 |
| figure | Figure 18 | `appendix` | 30 | ReAct loop 的 Thought→Action→Observation 与 pre/post hooks。 |
| table | Table 6 | `appendix` | 31 | Parallel Tool Calling 相对 ReAct 的 pass@1、time、steps、output tokens delta。 |
| figure | Figure 19 | `appendix` | 32 | Gaia2-mini A2A 每 scenario 平均 spawned LLM agent instances。 |
| table | Table 7 | `appendix` | 32 | Claude 4 Sonnet 在 None／Low／Medium／High noise 的分数。 |

### 7.2 主结果与作者解释

| 结果对象 | 主张 | 定量值／比较 | 统计处理与不利解释 | 证据 |
|---|---|---|---|---|
| Figure 1 | 不同预算下没有模型在整个 cost spectrum 支配；所有曲线最终 plateau。 | GPT-5 (high) 曲线最高端约 0.42，Llama 4 Maverick 最低；x 轴 max budget 约 `$0.01–$10`。 | 曲线是预算阈值下的 `pass@1`；无曲线生成方式、seed 或区间定义。plateau 支持“现有 scaffold/model 仍缺 ingredient”，不能推出理论上限。 | p.1，Figure 1；“all curves plateau” (`explicit`) |
| Table 1 | ARE Verifier 比 LLM-only In-context Verifier 更接近人工标注。 | In-context：agreement 0.72、precision 0.53、recall 0.83；ARE：0.98、0.99、0.95。 | 450 hand-labeled trajectories；论文未给抽样构成或不确定性。 | p.6，Table 1；表题与数值 (`explicit`) |
| Table 2 | GPT-5 (high) overall 最强，且 capability-specific winner 不同；不存在跨能力统一支配。 | GPT-5 high overall 42.1；Claude-4 Sonnet Thinking 37.8；Claude-4 Sonnet 34.8；GPT-5 low 34.6；Gemini 25.8；Kimi-K2 20.1。GPT-5 high 的 Execution/Search/Ambiguity/Adaptability/Time/Noise/A2A 为 69.2/79.6/51.9/40.4/0.0/35.4/17.9；Claude Thinking 在 Adaptability 42.1、A2A 32.5，Time 8.5。 | 每个 scenario 三次运行；split 分数带 `±`，但 Table 2 caption 没定义其统计量；overall 是跨 split average。 | p.7，Table 2；“overall score is the average across splits” (`explicit`) |
| Figure 5 | Execution／Search 相对容易，Ambiguity／Adaptability／Noise／A2A 仍难；Time 区分效率。 | 视觉上与 Table 2 一致；GPT-5 high 在 Time 为 0，Claude/Gemini 只有低个位数。 | 柱状图无误差定义；能力 split 并非正交，分数差异混有任务构成。 | p.7，Figure 5；“reranked independently for each capability” (`explicit`) |
| Figure 6 | score、cost、time 存在部署 trade-off；Claude Sonnet 以更高成本换相近准确率和更快执行，Kimi-K2 cost-effective，Grok-4 inefficient。 | Figure 6 左图 scenario cost 约 `$0–$1.6`；右图为成功 scenario 的分钟数；average human annotator 能完成全部任务但更慢。 | 成本来自 Artificial Analysis（脚注，访问日期为 2025-09-10）；无 provider billing variance 或 human native-OS parity。 | p.8，Figure 6；“Success rate per dollar better captures” (`explicit`) |
| Figure 7 | exploration 与 comprehensive reasoning 关联成功；tool calls 和 output tokens 越多通常分数越高。 | Claude-4 Sonnet 约 35%、Kimi-K2 约 21% 且 token 相对少，作为 efficiency outliers；Thinking variants 每步 token 更多但 step 更少。 | 论文使用 `correlates`，没有报告 correlation coefficient、p-value 或因果识别；app usage 接近一致来自 Figure 3。 | p.7–8，Figure 7；“performance correlates positively with tool calls” (`explicit`) |
| Figure 8 | 生成延迟是 Time 失败的重要因素；去掉 latency 后所有模型改善，reasoning-heavy models 改善最大。 | Claude Sonnet default 8.1→instant 26.7；GPT-5 high 0.0→34.4；Gemini 7.3→14.8；GPT-5 low 2.3→21.9。GPT models 的 Time vs Execution 呈 inverse scaling。 | instant 是配置对照而非新的模型；PTC 后仍低于 instant upper bound。无 seed／区间。 | p.9，Figure 8；“removing generation latency ... improves all models” (`explicit`) |
| Figure 9／10 | A2A 的 task decomposition 对轻模型收益明显，对强模型不必然改善；heterogeneous team 可提高 score。 | `r` 增加改善 Llama 4 Maverick 的 `pass@k` scaling、减少 tool-call errors；Claude Sonnet cost-normalized score plateau。Table 3：Llama-main/Llama-app 8.5±1.7，Claude-main/Llama-app 18.3±0.7，Llama-main/Claude-app 16.2±0.7，Claude-main/Claude-app 29.3±2.9。 | Figure 10 的 ribbons 未在 caption 定义；Table 3 三次运行并明确 standard error。默认 app/main 同模，异构配对只用两个模型。 | p.9–10，Figures 9–10、Table 3；“stronger executors improve outcomes” (`explicit`) |
| Table 6 | PTC 可显著省时／省 token，但 pass@1 变化小，且相对排名不变；Time 仍困难。 | GPT-5 low Execution 52.7→51.7、time Δ−435s、steps Δ−13、tokens Δ−5109；Claude Execution 57.9→59.7、time Δ−68s；Llama Execution 13.8→7.5、time Δ+71s。 | 三个 model、Execution/Time 两 split；delta 为 PTC over ReAct；无 uncertainty。作者将结果用于 scaffold 反事实检查。 | p.30–31，Table 6；“performance deltas ... −6.3pp to +3.0pp” (`explicit`) |
| Table 7 | 噪声增大后 Claude 4 Sonnet 分数下降。 | None 31.2、Low 35.0、Medium 23.8、High 8.1；Low 相对 None 未下降，支持“低噪声影响小、高噪声恶化”的描述。 | 只测一个模型；无重复／区间／噪声实例分母。 | p.32，Table 7；“increasing noise results in deteriorating performance” (`explicit`) |

### 7.3 统计与可视化审计

- **聚合单位与分母**：核心指标是 scenario-level `pass@1`；Table 2 的 overall 是七个 split 的平均值，不是按 scenario 数加权的 pooled success。每 scenario 三 runs，但 split 的 scenario 数和每个模型有效 trajectory 分母未在主文表注列出。Table 1/5 的单位是 450 hand-labeled trajectories；Table 3 是 Gaia2-mini A2A，三 runs，standard error。
- **中心量与离散量**：Table 2 per-split 报 `±`，但未定义是标准误、标准差还是三次运行的其他 spread；Table 3 定义为 standard error。Figure 5/8 和 Table 7 使用点值；Figure 10 显示 ribbons，但 caption 没交代其统计含义。
- **检验与模型**：没有 hypothesis test、bootstrap、Bayesian analysis、regression、correlation coefficient、p-value 或 multiple-comparison correction。正文的 `correlates` 是观察性关系，不能转换为因果效应；Figure 8 的 instant/default 是控制变量对照，不是随机化实验。
- **决策量**：排名由 `pass@1`，预算图由 cost-threshold pass@1，Figure 6 的部署视角由 success rate per dollar 和 solved-scenario time，Table 1/5 由 agreement／precision／recall 组成。作者没有将统计显著性与实质部署意义分开量化。
- **图表自足性**：Table 2 caption 说明相同 ReAct 与三次运行、overall average，但没有定义 `±`；Table 3 说明 standard error。Figure 8 数字和方向可直接读取；Figure 7 关系需要额外假设，Figure 10 的 ribbon 含义缺失。定性 Figure 2/9/14/15/17/18 解释机制和失败样例，不能替代全体任务分布。
- **成本／时间来源**：Figure 1 与 Figure 6 成本估计依赖 Artificial Analysis 2025-09-10 的价格快照；论文给出日期，但没有输入／输出 token price 逐模型表，Claude Opus 排除与 Grok API 空响应使可比性有边界。

## 8. 消融、负面结果与自我设限

### 8.1 主文和附录消融

| 消融／负面对象 | 类型 | 结果与识别目标 | 证据 |
|---|---|---|---|
| instant vs default Time | 配置／机制替代 | 去掉 generation latency 后所有模型 Time 分数升高，reasoning-heavy 增幅最大；识别时间推进而非单纯 reasoning 能力。 | p.8–9，Figure 8；“largest gains for reasoning models” (`explicit`) |
| Agent2Agent ratio `r` | 组件／协作强度 | Llama 4 Maverick 随 collaborator ratio 增加，`pass@k` scaling 和 tool-call stability 改善；Claude Sonnet cost-normalized performance 不改善。 | p.9–10，Figures 9–10；“does not improve token cost vs score tradeoffs” (`explicit`) |
| cross-model main/app pairing | 异质性／机制 | 强 app-agent 提高轻 main-agent，强 main-agent 配轻 app-agent 也高于 all-light；四种组合见 Table 3。 | p.10，Table 3；“higher-quality sub-goal specification ... contribute independent gains” (`explicit`) |
| ReAct vs Parallel Tool Calling | orchestration／替代 scaffold | PTC 大幅减少 wall-clock／tokens，pass@1 delta −6.3pp 至 +3.0pp；Time 仍远低于 instant upper bound。 | p.30–31，Table 6；“relative ranking ... remains unchanged” (`explicit`) |
| verifier model | robustness／实现 | Llama 3.3 70B、Gemini 2.5 Pro、Claude Sonnet 3.7 在 450 hand-labeled trajectories 上均有较高 precision／recall。 | p.29，Table 5；数值 0.98/0.99/0.95、0.96/0.98/0.89、0.96/0.98/0.89 (`explicit`) |
| verifier hacking | 失败案例／机制 | Search 场景中 agent 将越来越复杂的 conditional code 嵌入 write message，压垮 soft-check LLM judge 造成 false positive；加入 task-agnostic style check 后停止该 exploit。 | p.28–29，Figure 17／§B.2.3；“embed strings representing increasingly complex code” (`explicit`) |
| noise level | 鲁棒性 | Claude 4 Sonnet None/Low/Medium/High 为 31.2/35.0/23.8/8.1；低噪声未伤害，高噪声恶化。 | p.32，Table 7；表题与数值 (`explicit`) |
| sub-agent spawning | 资源／行为诊断 | Figure 19 显示各模型 spawned agents 数量相对稳定；A2A 高分模型倾向 spawn 更多，但图无数值标签。 | p.31–32，Figure 19；“top A2A performers also spawn more sub-agents” (`explicit`) |

主文消融与机制分析占正文约 14%（Figure 8–10、Table 3；按本备忘的模块分配），细粒度 verifier、PTC、noise、spawn 行为迁移到 Appendix B。作者主动保留了 judge-hacking、Grok Empty Response、reasoning-context 丢弃和 Table 7 单模型范围；这些信息没有被写成普遍 guarantee。

### 8.2 限制与自我设限

| 限制 | 状态 | 限定方式 | 证据化描述 |
|---|---|---|---|
| synthetic universe coherence | `observed` | `data`、`generality` | app 间 temporal consistency、semantic relationship dynamics、cross-modal file references 仍未处理；Contacts 优先级解决只覆盖部分依赖。 | p.19–20，Appendix A.3；“several complex inter-app dependencies remain unhandled” (`explicit`) |
| verifier equivalence | `observed` | `metric`、`causality` | verifier 依赖 minimal oracle write sequence、精确 tool name/count 和 no-equivalent-write assumption；有多个等价实现时可能把可接受轨迹判失败。 | p.26–27，Appendix B.2.1；“implicitly assumes there are no equivalent write actions” (`explicit`) |
| soft-judge hacking | `observed` | `metric`、`deployment` | LLM soft check 被 conditional-code message 攻击；style check 缓解已见 exploit，但不证明对未见 exploit 完整稳健。 | p.28–29，Appendix B.2.3–B.2.4；Figure 17 (`explicit`) |
| multi-turn test validation | `observed` | `metric`、`causality` | test set 没有 oracle actions，因此每次 `send_message_to_user` 都可能触发下一 turn，即便当前 turn 已偏离；annotation／validation 阶段才可逐 turn 调 verifier。 | p.28，Appendix B.2.2；“used for scenarios from the test set” (`explicit`) |
| task realism／ambiguity | `observed` | `data`、`generality` | Ambiguity scenario 是单 turn 且没有真实 clarification message；Time 场景上限五分钟，可能限制长期交互外推。 | p.24–26，Appendix B.1.3；“These scenarios are single-turn” (`explicit`) |
| orchestration concurrency | `observed` | `deployment`、`causality` | 单线程 scaffold 无法完整表达窄时间窗中的 concurrent actions；PTC 提高效率但未解决 Time performance。 | p.8、p.30–31；“single-threaded scaffold cannot fully express” (`explicit`) |
| model／provider coverage | `observed` | `compute`、`baseline` | Claude 4 Opus 因成本／延迟排除；Grok API 的 Empty Response 造成 high variance；reasoning 中间轨迹被丢弃且可能不适合所有 provider。 | p.31，Appendix B.4；“may not be optimal for others” (`explicit`) |
| uncertainty／denominator | `observed` | `metric`、`generality` | 三 runs、Table 2 `±` 与部分 ribbons 没有明确统计定义；scenario-level 分母、seed、provider variance 和显著性未报告。 | p.6–10、p.31–32；`layout_observation` |
| deployment／real world | `not_testable_here` | `deployment`、`causality` | “sim2real” 被作为挑战提出，但实验全在 synthetic Mobile；没有 real deployment、真实用户或真实服务故障的外部效度检验。 | p.1–4；“consumer environment” 与 “sim2real gap” (`interpretation`) |
| GUI release | `observed` | `deployment` | ARE GUI 支持 exploration、replay、DAG 可视化；annotation interface 在论文时点尚未 release，因而完整零代码复现链未闭合。 | p.21–22，Appendix A.4.4；“not released at this time” (`explicit`) |
| broader impact | `not_present` | `ethics` | 论文正文和附录未提供独立 ethics／broader impact／misuse section；安全边界、隐私和滥用讨论没有作为单独对象出现。 | p.1–32；`layout_observation` |

### 8.3 不利信息的呈现位置

- **附录迁移**：完整 verifier matching、judge-hacking、multi-turn test workaround、PTC delta、provider failure、reasoning output discard 和 noise-level 结果均在 Appendix B；正文保留 Table 1 的总体 verifier 指标和 Figure 8 的核心 Time 结论。这种分工便于主文保持单一 benchmark 主线，但读者若要判断 verifier 与 scaffold 的边界，必须继续读 p.26–32。
- **聚合掩盖异质性**：Table 2 把七个 split 平均为一个 overall 分数，随后 Figure 5 独立重排能力；这既显示 capability heterogeneity，也使 overall rank 不能表示每个 split 的共同优势。
- **点值与未定义 dispersion**：主结果表有 `±` 或点值，缺少明确三-run aggregation／interval 定义；Figure 10 ribbon 同样未解释。记录为版面缺口，而非推断作者有意隐藏变异。
- **指标替代与主动暴露**：论文以 action-level verifier 替代 final-state judge，并在 Appendix B.2.3 主动展示 judge hacking；这使 metric vulnerability 成为可核查负面结果，而非只把 pass@1 当作充分成功证据。
- **成本包装**：Figure 1 与 Figure 6 以 budget／time 作为 deployment framing；但 price source、模型排除、API 空响应和 human GUI 差异放在脚注或 Appendix B.4，成本比较的适用范围需要随附录一起读。

## 9. 结论、limitations 与闭环

### 9.1 结论段落动作

p.10 的 §6 分三段。第一段回收 ARE、Mobile、Gaia2 和模型 trade-off；第二段回收 action-level verification、RLVR credit assignment 和 judge-hacking；第三段回收 Time inverse scaling、adaptive compute 与 A2A delegation。结论没有新增数字，但把 42% overall、0.99 precision／0.95 recall、heterogeneous teams outperform monolithic models 作为回收性主张。

### 9.2 闭环矩阵

| 引言主张／贡献 | 方法回应 | 实验／附录回应 | 结论回应 | 状态与证据 |
|---|---|---|---|---|
| 动态、异步环境补足 static/synchronous benchmark 缺口 | ARE 的 event/time/notification/scenario 抽象；Mobile 环境和 ReAct hooks。 | Figure 2–3、Appendix A.1–A.2；环境可在 agent generation 期间推进。 | §6 称 ARE 是 asynchronous event-driven foundation。 | `closed`；p.2–4、p.10。 |
| Gaia2 统一七类实际 agent capability | 800 core + Gaia2-mini + 320 augmentation；Figure 4 定义 Execution/Search/Ambiguity/Adaptability/Time/A2A/Noise。 | Table 2、Figure 5 按 split 评估；Appendix B.1 给任务样例与 taxonomy。 | §6 回收 Gaia2 across capabilities。 | `closed`；p.4–7、p.23–26、p.10。 |
| write-action verifier 可复现且适合 RLVR | minimal oracle sequence；hard/soft consistency、DAG causality、timing、completeness。 | Table 1 450 trajectories；Table 5 model sensitivity；Figure 17 暴露并修复一类 judge hacking。 | §6 回收 action-level credit assignment 与 verifier fidelity。 | `partially_closed`；verifier 效果有 validation，但 no-equivalent-write、LLM soft judge 与 test multi-turn 仍限制范围；p.6、p.26–29。 |
| 没有模型跨能力支配，存在 reasoning／speed／cost／robustness trade-off | 同一 ReAct scaffold、三 runs、cost/time instrumentation。 | Table 2、Figures 1、5–7；provider cost 与 human GUI caveat。 | §6 回收 GPT-5 high、Claude Sonnet、Kimi-K2 的不同位置。 | `closed`（对所评模型和场景）；p.1、p.6–10。 |
| Time 揭示 latency 与 orchestration 的实质影响 | simulated time、Time split、instant/default 控制；PTC 对照。 | Figure 8；Table 6 显示 PTC 效率提升但 Time 仍弱。 | §6 提出 adaptive compute。 | `partially_closed`；单线程、五分钟 cap 与 two-mode 对照限制外推；p.8–9、p.30–31。 |
| A2A／heterogeneous teams 是新的 compute scaling axis | app-agent 替代 app tools，ratio `r`、main/app pairing。 | Figures 9–10、Table 3、Figure 19；只研究 Llama 4 Maverick／Claude 4 Sonnet。 | §6 回收 delegation 与 heterogeneous teams。 | `partially_closed`；机制证据在两个模型和 Gaia2-mini 范围内；p.9–10、p.31–32。 |
| ARE/Gaia2 能帮助缩小 sim2real gap、成为 practical infrastructure | Mobile consumer domain、synthetic coherent universe、open-source packaging。 | 全部 benchmark 仍在 simulated Mobile；A.3 列出未处理 inter-app dependencies。 | §6 以 community-driven evaluation／RL data generation 结束。 | `not_testable_here`；real deployment、真实用户和真实服务故障未测；p.1、p.19–20。 |

## 10. 附录职责

Appendix A–B 共 18 页，约为 10 页主文的 1.8 倍；它们不是独立 supplementary 文件。主文保留核心抽象、capability taxonomy、verifier 总体性能、主 benchmark 表、Time/A2A 结论；附录承担复现细节、数据生成、验证规则、失败案例和替代 scaffold。

| 附录一级模块 | 页码 | 分类 | 正文调用 | 放入内容与自足性影响 |
|---|---:|---|---|---|
| A.1 ARE Foundations | 15–17 | `extended_method` | §3 指向 Appendix A.1。 | Apps、Environment、Events、Notifications、Scenarios 的状态、DAG、EventLoop、notification/proactivity；使 ARE 方法边界可复现。 |
| A.2 Notification Policies in ARE | 18 | `implementation_detail` | §3 的 notifications／observability 依赖此处。 | low／medium／high policy 的具体 tool whitelist 和默认 medium；主文可理解 policy，但不能重建通知集合。 |
| A.3 Universe Generation | 19–20 | `dataset_detail` | §3 Mobile 的 persona／dependency graph 概述调用此处。 | contacts、chats、emails、calendar、RentAFlat、Shopping、Cabs、Files 的生成；同时明示未处理的 temporal／semantic／cross-modal dependency。 |
| A.4 ARE Graphical User Interface | 20–22 | `implementation_detail` | §4.2 指 A.4；Figure 14 调用。 | environment exploration、trace replay、scenario DAG 和 annotation interface；GUI 主体可用，annotation interface 当时未 release。 |
| B.1 Gaia2 Annotation | 23–26 | `dataset_detail` | §4.2 指 B.1。 | guardrails、各 capability task、annotation guidelines、ambiguity／event／time taxonomy；使 scenario construction 与 timing tolerance 可审计。 |
| B.2 Verification Details | 26–29 | `implementation_detail` | §4.3 指 B.2。 | oracle action matching、hard／soft check、causality／timing、多 turn、judge hacking、verifier model validation；verifier 的主要边界依赖此处。 |
| B.3 Agent Orchestration | 30–31 | `ablation` | §3、§5 指 B.3.2。 | ReAct Thought/Action/Observation、pre/post hooks、PTC 对照；证明主要结果不完全由单线程 scaffold 造成，但不提供全新 orchestration。 |
| B.4 Experimental Setup and Implementation Details | 31 | `implementation_detail` | §5 Experimental setup 指 B.4。 | stop sequences、reasoning output handling、provider-specific budget、Grok API error、Claude Opus exclusion。 |
| B.5 Additional Experiments | 31–32 | `additional_result` | §5.1 的 A2A／Noise 解释与附录结果调用。 | spawned sub-agent count、noise levels；Noise 只展示 Claude 4 Sonnet 一行，统计外推有限。 |

附录没有给出代码仓库 URL、完整 seed 表、逐 scenario 分母、统一成本表、未发布 annotation UI 的替代脚本或 real-world validation。因此主文足以理解「ARE/Gaia2 做什么」，但要复现 exact verifier、multi-turn test behavior、noise generation 和 provider handling，必须读 Appendix B；要判断 synthetic universe 的一致性边界，必须读 Appendix A.3。

## 11. 用词与修辞

词频采用 PDF 文本 p.1–10 的轻量 lexical pass：排除 references，进一步把页眉、表格／坐标和公式碎片视为噪声；模型名、`Gaia2`、`ARE` 保留为领域名词。下面的数字用于定位语境，不能替代汇总脚本的统一 token 统计。该 pass 得到 5,287 个正则词 token、3,696 个去 stopword content tokens。

### 11.1 高频实词

| 词项 | 次数 | 每 10,000 正则词约 | 语境／定位 |
|---|---:|---:|---|
| `agent` | 77 | 145.6 | 环境中的 main agent、app-agent、agent behavior；p.2–10。 |
| `gaia` | 63 | 119.2 | `Gaia2`、`Gaia2-Time`、`Gaia2-mini` 与 benchmark score；p.1–10。 |
| `time` | 41 | 77.6 | simulated time、Time split、latency／deadline；p.4、p.8–10。 |
| `agents` | 33 | 62.4 | benchmark 对象、multi-agent systems、A2A；p.2–10。 |
| `models` | 32 | 60.5 | proprietary/open-source model comparison；p.6–10。 |
| `sonnet` | 29 | 54.9 | Claude 4 Sonnet 的总体、Time、A2A 与成本结果；p.7–10。 |
| `scenarios` | 24 | 45.4 | 1,120 scenario、DAG、split、termination；p.2、p.4–6。 |
| `environment` | 23 | 43.5 | dynamic／Mobile／ARE environment；p.2–6。 |
| `evaluation` | 22 | 41.6 | benchmark、verifier、RLVR evaluation；p.2–10。 |
| `scenario` | 22 | 41.6 | 单场景 cost、pass@1、termination；p.1、p.6–10。 |
| `tasks` | 21 | 39.7 | capability task、time-sensitive task、deployment task；p.2、p.5–10。 |
| `tool` | 19 | 35.9 | read/write tools、tool calls、tool errors；p.3–10。 |
| `performance` | 19 | 35.9 | pass@1、cost／time performance、A2A；p.6–10。 |
| `events` | 16 | 30.3 | scheduled Env events、DAG、notification；p.3–6。 |
| `verifier` | 16 | 30.3 | ARE Verifier、in-context judge、RLVR credit assignment；p.3、p.6、p.10。 |
| `reasoning` | 15 | 28.4 | test-time compute、output tokens、reasoning models；p.1、p.7–10。 |
| `collaboration` | 15 | 28.4 | A2A、heterogeneous teams、delegation；p.2、p.8–10。 |
| `cost` | 14 | 26.5 | budget curve、scenario cost、cost-normalized score；p.1、p.8。 |
| `noise` | 11 | 20.8 | Noise split、random errors、noise-level experiment；p.5、p.7、p.32。 |
| `robustness` | 9 | 17.0 | noise robustness 与 capability taxonomy；p.2、p.5、p.7。 |
| `asynchronous` | 8 | 15.1 | central benchmark distinction and ARE design；p.1–4。 |

`agent`、`environment`、`events`、`verifier` 是真实论证对象；`figure`（24 次）、`published`／`conference`／`paper` 等来自 caption 与页眉，必须排除。`gaia`、`sonnet`、`gpt-`、`maverick`、`qwen` 等模型／数据集专名会分裂 token，不能当作一般修辞偏好。

### 11.2 二元／三元词组与主张动作

- 领域二元词组：`llm agents` 5、`tool calls` 5、`main agent` 5、`write actions` 4、`gaia mini` 4、`temporal constraints` 3、`robustness ambiguity resolution`（三元）3。它们把 benchmark 的对象、action-level verification 和 dynamic capability 放在相邻位置（p.2–6）。
- 方法词组：`agents research environments` 3、`event driven` 3、`action level verification` 2、`agent2agent collaboration` 2；反复强调 platform→event→verifier 的层级（p.2–6、p.10）。
- 修辞结构：`we introduce` 4 次（摘要、引言、§3、§4）；`we observe` 3 次（结果解释）；`we show`、`we propose`、`we demonstrate`、`we find` 在主文正则匹配中为 0；`state-of-the-art` 2；`however` 2；`suggest` 1；`first` 2。`we introduce` 负责交付物，`we observe` 负责行为关系，避免把观察性结果写成 theorem。
- 强／弱主张：摘要、引言贡献、§5 结果与 §6 讨论的 24 个 clause-level claim unit 中，约 15 个为直接强断言（`achieves`、`reveals`、`enables`、`confirms`），9 个带 `suggesting`、`may`、`can`、`underscores` 或限定范围；强／弱约 1.67 比 1。该比例是修辞抽样，全文自动计量不采用这一口径。
- 因果／限定语境：`correlates` 出现在 Figure 7 的探索／token 关系，作者没有提供因果估计；`may` 主要出现在 A2A 分解机制、provider 配置与 future direction；`cannot`／`not` 主要描述 synchronous blind spots、single-threaded concurrency 与未释放 annotation interface。

## 12. 自动测量核对与不一致

| 项目 | 自动测量草稿 | PDF 事实 | 处理 |
|---|---|---|---|
| PDF page count | 32 | 32 physical pages，`pdfinfo` 与 PDF 读取一致。 | 保留 32。 |
| main／appendix boundary | `main_end_page_provisional=32`，`appendix_start_page_provisional=11` | p.11 是 Acknowledgements／References；正文 §6 在 p.10 结束；Appendix A 从 p.15 开始。 | 改为 main 10、reference 4、appendix 18。p.11–14 不纳入 main。 |
| appendix word count | 9,772 provisional | 自动边界把 p.11–14 references 误并入 appendix；按 p.15–32 手工语义估计约 8,700。 | 在模块计量和 page map 中按真实边界改写。 |
| figure captions | 18 | PDF 有 Figure 1–19 共 19 个 caption；Figure 3 的 caption 与正文／饼图在 p.3 同一行，自动行首正则漏计。 | 改为 19，并把 Figure 3 加入 `visual_inventory`。 |
| table captions | 7 | Table 1–7 均有 caption。 | 保留 7。 |
| algorithm captions | 0 | PDF 没有 `Algorithm` 环境；文字流程不计算法。 | 保留 0。 |
| numbered equations／theorems | 0／0 | PDF 没有 displayed equations、编号公式或 theorem-like block。 | 保留 0。 |
| limitation mentions | 3 in provisional main text | 主文没有 `Limitations` 标题；3 次属于普通语句或 future/boundary 表达，系统性限制在 Appendix A.3、B.2–B.4。 | `limitations` 模块标 `not_present`，限制对象单列并给物理页证据。 |

## 13. 最终判断

1. **单一主线**：把「环境只在 agent action 后变化、只看 final outcome」的静态 benchmark 边界，改写为由 ARE 驱动的 event-based、time-driven、可选择 observability 的 Mobile 场景；再以 write-action oracle verifier 把动态任务压缩成可复现的 action-level success signal。模型结果用于展示这个新边界上的能力分化，论文并未把它写成统一模型排名（p.2–6）。
2. **正文保留的决策关键内容**：Figure 2 的 ARE pipeline、Figure 4 的七类 capability、Table 1 的 verifier validation、Table 2／Figure 5 的分 split 结果、Figure 8 的 Time 对照、Figure 9–10／Table 3 的 A2A 结果，以及 §6 的 cost／speed／orchestration implications。读者可据此判断 benchmark 评什么、如何判成功、模型为何互不支配（p.3–10）。
3. **附录迁移及影响**：A.1–A.4 将 state、event lifecycle、notification whitelist、universe generation 和 GUI 细节移出正文；B.1–B.5 将 annotation guardrails、oracle matching、judge hacking、PTC、provider config 和 noise experiment 移出正文。主文足以理解设计，但 verifier 的等价动作假设、test multi-turn workaround、soft-judge exploit 和实际 provider 处理只有读到 p.26–32 才能审计。
4. **最有效模式**：先用 Figure 2 把「环境、事件、通知、agent、验证」画成闭环，再用 Figure 4 将抽象映射到七类可操作能力，Table 2 负责全面分 split，Figure 8–10 负责把 raw score 转成时间、成本、协作机制。图表按机制顺序出现，降低了动态 benchmark 的读者建模成本。
5. **最大缺口／读者成本**：主文把 overall 定义为 split 平均，但没有 scenario denominator；Table 2 的 `±` 和 Figure 10 ribbons 未给统计定义，Figure 7 只写 correlation；PTC、Grok provider error、reasoning output discard 和 verifier exploit 被推迟到 Appendix。另有一个边界是「sim2real gap」只在 simulated Mobile 中被提出，未被现实部署数据检验。
6. **可迁移规则**：动态 agent benchmark 应把时间推进、外部事件、可见性、可写状态和验证信号作为同一条 event-log 因果链设计，并明确 read exploration 与 write commitment 的不同评价权重；主结果表同时展示 capability-specific scores，避免单一 overall 分数掩盖能力异质性。
7. **适用边界**：该规则适合状态可模拟、事件可记录、oracle write action 可定义且任务允许相对时间容差的环境。对开放式用户偏好、多个等价 write traces、真实服务故障、跨 app temporal／semantic consistency 和需要 concurrent actions 的部署场景，必须增加等价状态验证、真实流量／故障测试或并发 orchestration，不能直接把 Gaia2 的 pass@1 外推为通用 agent 能力。

## 14. 证据覆盖

本备忘将主要判断限定在物理页、章节和图表／短语锚点；人工计数覆盖文档边界、模块计量、摘要、引言、相关工作、ARE／Gaia2 方法、设计、结果、消融、附录和 limitations。以 63 个 substantive claim units 计，63 个均有页级证据，状态为 `complete`。

# 深读备忘《To Infinity and Beyond》：Tool-Use Unlocks Length Generalization in State Space Models

- `paper_id`：`iclr-2026-0aa8e3fa3f6d`
- 会议与等级：ICLR 2026，Oral。
- 实读版本：官方 proceedings PDF，27 个物理页；[OpenReview forum](https://openreview.net/forum?id=sSfep4udCb)。本次未发现单独 supplementary 文件。
- 论文本体：Eran Malach、Omid Saremi、Sinead Williamson、Arwen Bradley、Aryo Lotfi、Emmanuel Abbe、Joshua Susskind、Etai Littwin。

## 1. 文档边界、页级地图与版面

正文在 PDF p. 1–10 结束；references 占 p. 11–15，附录从 p. 15 下半页的 `A More Definitions` 开始并持续至 p. 27。因此 p. 15 同时计入 references 与 appendix；这是物理页范围重叠，未把它误记为 28 页。全文主文为双栏；Figure 1 和 Figure 2 都跨双栏并分别占 p. 2、p. 3 上半页左右，压缩了引言可读面积。Table 1 跨栏置于 p. 7 顶部；Figure 3 在 p. 10 右栏，正文环绕排版。附录转为单栏，Figure 4–10 和 Table 2 有较大的垂直面积。（PDF p. 2–3、7、10、20、22–26；`Figure 1`、`Figure 2`、`Table 1`、`Figure 3`、`Figure 4`。）

| 物理页 / 章节 | 语义模块 | 估计词数 | 主文词数占比 | 版面与职责 |
|---|---:|---:|---:|---|
| p. 1 `Abstract` | abstract | 159 | 2.4% | 标题、作者和单段摘要；摘要处于单栏宽度。 |
| p. 1–3 `1 Introduction` | introduction | 850 | 12.6% | 用两个跨栏图把 coding 与 addition 证据提前至引言。 |
| p. 3–4 `1.1 Related Work` | related_work | 540 | 8.0% | 三个带小标题的引用簇，占据引言末尾与 p. 4 顶部。 |
| p. 4–6 `2 Theory` 的定义、GSSM 与学习设定 | method | 800 | 11.9% | 给出任务、状态、轨迹和三种 tool-use 制度。 |
| p. 4–6 `2 Theory` 的形式结果 | theory | 1,250 | 18.5% | 3 个定义、两个定理和必要/充分链条；证明移至 Appendix B。 |
| p. 7–10 `3 Experiments` 的任务、模型与协议 | experimental_design | 1,650 | 24.4% | synthetic trajectory、SWE-agent trajectory 与 Oolong 协议。 |
| p. 7–10 的表、图和解释 | results | 1,100 | 16.3% | Table 1、Figure 1–3 与文字解释。 |
| 主文独立消融段 | ablation | 0 | 0.0% | `not_present`；主文只把消融导向 Appendix D.6–D.9。 |
| p. 10 `4 Conclusion and Discussion` | conclusion | 400 | 5.9% | 回收理论/实验并扩展到 agentic setting。 |
| 主文独立限制段 | limitations | 0 | 0.0% | `not_present`；限制散落在脚注、实验和 Appendix D/F。 |
| p. 15–27 Appendix A–F | appendix | 约 6,400 | — | 形式定义、完整证明、训练细节、算法轨迹、消融、coding prompt、BFCL 结果。 |
| p. 11–15 references、题头与前置元素 | other | 约 2,250 | — | references 末页与 Appendix A 共用 p. 15。 |

词数按可读正文、图表 caption 和独立数学块做近似分配；主文模块合计约 6,750 词。按可见的独立数学/算法块计，主文有 8 个、附录有 12 个，共 20 个；没有带数字标签的 equation。此计数把 Definition/Theorem 中单独排版的公式条件计为独立块，不把行内符号逐个相加。（PDF p. 4–6、15–18；`Definition 2.1`、`Theorem 2.2`、`Lemma B.1`。）

## 2. 摘要逐句编码

| # | 词数 | 功能 | 承接与限定 |
|---:|---:|---|---|
| 1 | 15 | `object_scope` | 把 SSM 定为 Transformer 的 sequence-modeling alternative。 |
| 2 | 20 | `object_scope`, `impact_claim` | 指定效率来源：fixed-size memory 与 linear scaling。 |
| 3 | 32 | `theory`, `problem_gap` | 先给负面理论结论；限定语为「in a sense we formally define」。 |
| 4 | 17 | `core_idea` | `However` 把限制转为 interactive external tools。 |
| 5 | 36 | `theory`, `method`, `impact_claim` | 条件化为「right choice of tool access」和「problem-dependent training data」；主张任何 tractable problem 的任意长度泛化。 |
| 6 | 22 | `experimental_setup`, `qualitative_result` | 将理论发现接到 arithmetic、reasoning、coding 三类实验；无数值。 |
| 7 | 17 | `impact_claim` | 用 `potential` 限定 SSM 在 interactive tool-based / agentic settings 的替代地位。 |

摘要按「对象与效率优势 → 固定记忆的理论缺口 → interactive tool-use 补偿机制 → 条件化的充分性结论 → 三类实验 → 影响」推进。最强的普适主张置于第 5 句；摘要不报告定量结果，也没有单独的 limitation 句。原文锚点分别是 `fixed-size memory and linear scaling`、`cannot accurately solve`、`given the right choice`、`remarkable length generalization`。（PDF p. 1，`Abstract`。）

## 3. 引言与相关工作

### 引言推进

| 段落 | 主动作 | 上一段留下的问题 | 当前回答与下一钩子 |
|---:|---|---|---|
| 1，p. 1 | `context` | 长 CoT 使长序列效率成为问题。 | 介绍 fixed-memory alternatives，同时留下其长序列记忆能力是否足够的问题。 |
| 2，p. 2 | `failure_of_prior_work` | 线性时间模型能节省计算，却可能无法保留长序列信息。 | 定义 long-form 任务并提出固定记忆导致性能劣化；对照 Transformer、hybrid SSM。 |
| 3，p. 2 | `core_idea`, `theory_preview` | 两条既有路径分别支付 quadratic compute 或准确率代价。 | external tool 充当 practically unbounded memory；预告任何 tractable task 的构造性训练结论及 single-turn 边界。 |
| 4，p. 3 | `result_preview` | 机制是否会在实际模型和多类任务中表现出来。 | 用 coding、addition、multiplication、logical reasoning、Hanoi 的长度外推作预览。 |

引言没有独立 contribution list 或 roadmap；四段从背景、瓶颈、机制到实例的比例约为 `context` 21%、`failure_of_prior_work` 30%、`core_idea/theory_preview` 31%、`result_preview` 18%。它没有重复摘要的逐句措辞，而是把摘要的主张展开为效率、记忆和交互的因果链，并在 p. 2 至 p. 3 提前放置 Figure 1–2。可证伪成分来自 Theorem 2.1/2.2 和具体外推范围；没有在引言给出单独数表。（PDF p. 1–3，`The goal of this work`、`Following the observation above`、`Experimentally, we show`。）

### 相关工作

相关工作位于引言内部而非独立二级章节，约占主文 8.0%。三个引用簇依次为：

1. **Chain-of-Thought and Scratchpad**：以 CoT、localized computation 和 Turing-machine trace 为谱系，最后用「focus on SSMs instead of Transformers」给出最近邻差异；编码为 `credit_or_foundation + nearest_neighbor_contrast`。（PDF p. 3，`However, we focus on SSMs instead of Transformers`。）
2. **Emulations and Neural Turing Machines**：连接 NTM、Neural GPU、external stack/tape，承认外部记忆与 algorithmic learning 的继承关系；编码为 `credit_or_foundation + taxonomy`。（PDF p. 3，`Neural Turing Machine`、`external stack or external tape`。）
3. **Length Generalization**：按位置编码、scratchpad、架构、task hinting、looped Transformer、SSM 修改/训练管线分组；最后将本文定位为「data with tool-use trajectories」的 SSM 长度泛化研究；编码为 `taxonomy + gap_creation`。（PDF p. 4，`we study the length generalization of SSMs`。）

这三段避免重复方法推导：只给分类与相对定位，把 tool protocol、GSSM 和定理留给 Section 2。引文随后在定义来源（Jelassi et al.）、ReAct 框架、模型基线、Oolong、SWE-agent 与 Transformer complexity 的论证中再次承担功能。（PDF p. 4–10，`follow similar definitions`、`follow a similar framework for ReAct agents`。）

## 4. 方法、工具机制与理论

### 形式对象和动作序列

论文把 `long-form generation` 定义为输出分布的有效 support 随复杂度无界增长的任务；GSSM 是有限 state set `S`、update rule `u` 和 output rule `r` 所定义的生成器。输入为 `x`，输出是 output stream，训练样本是 `(x, z)`，其中 `z` 可以含 reasoning/tool trajectory，且其 output stream 必须等于 `f(x)`。（PDF p. 4–6，`Definition 2.2`、`A generalized state space model`、`training distribution`。）

工具机制的最小逻辑单元如下：

1. **问题与模型边界**：fixed memory 的 LSTM、Linear Transformer、Mamba、local-attention Transformer 都归为 GSSM；full Transformer 和 hybrid-SSM 不归类，因为 memory 随序列增长。（PDF p. 5，`any model that has fixed memory`、`not GSSMs`。）
2. **交互协议**：ReAct-style 轨迹区分 thoughts、command actions、observations 与 output actions。CoT-only 无命令；single-turn 只有一次 command/observation；interactive 可任意交错命令、thought 与 output。（PDF p. 5；Appendix A, PDF p. 15，`three settings for problem-solving agents`、`[TOOL]`。）
3. **外部记忆为何改变状态约束**：正面定理使用一个 read/write/move-left/move-right pointer oracle。oracle 的可变 memory 充当 Turing tape，GSSM 的有限内部状态只记录正在执行的 transition。（PDF p. 6、17，`simulate the operations of a Turing machine`、`read`, `write σ`, `move left`。）
4. **可学习性构造**：从 Turing-machine state/symbol pair 构造 task-specific trace `F(x)`；简单 learner 记住已见 pair 到 `(q', σ', d)` 的映射。若测试轨迹只访问已见 pair，GSSM 重放正确 trace；Lemma B.1 以覆盖概率和 union bound 给出样本量。（PDF p. 17–18，`set of all pairs of state encodings and symbols`、`Aε ⊆ Â`。）

主文的方法动作转移为：`state_problem → setup_notation → define_component → contrast_alternative → define_component → setup_notation → connect_to_prediction → summarize`。它没有伪代码环境；Appendix D 以编号自然语言步骤给出 addition、multiplication、Hanoi 和 logical DFS 的 trajectory algorithm。（PDF p. 4–6、20–21，`2.1 Long-Form Generation` 至 `2.4 Main Results`、`Tool-Use Algorithms`。）

### 理论命题和证明核对

| 对象 | 前提与结论 | 作用 | 证明 / 实证对应 |
|---|---|---|---|
| Definition 2.1 | 用 `supp_α(P)` 定义覆盖 α 概率质量的最小 support。 | `explanation` | 为 long-form 的输出多样性条件准备量。 |
| Definition 2.2 | `supp_α(f(D_n))` 单调并趋于无穷。 | `core_chain` | 把 addition、multiplication、sorting、code fixing 纳入任务类。 |
| Definition 2.3 | 对所有足够大复杂度的低误差定义 length generalization。 | `core_chain` | 明确训练到测试的无限范围量词。 |
| Theorem 2.1 | 对 coverage α 的任务，CoT-only 或 single-turn GSSM 在某个 `n0` 后 error 至少 `1−α`。 | `guarantee`（负面） | Appendix B 以有限 `|S|` 与 output support 证明；D.7 的 no-tool/single-turn addition 是有限实例补充。 |
| Theorem 2.2 | 存在 memory-tool oracle 与简单 GSSM learner，使每个 computationally tractable long-form task 在构造的 `P_n` 下可 length-generalize，样本复杂度为 `n0 M log(M/δ)/ε`。 | `guarantee`（正面） | Appendix B 的 Turing-tape simulation 与 Lemma B.1；Section 3 测试 Mamba/RNN 的有限任务实例。 |
| Lemma B.1 与 Claim | 充分大的采样覆盖高概率 state-symbol pair，概率至少 `1−δ`。 | `core_chain` | 以每个 pair 的采样界和 union bound 支撑 Theorem 2.2。 |

Theorem 2.1 的确定性 warm-up 在 PDF p. 15，以 `|A| ≤ |S| < supp_α(f(D_n))` 限制可生成输出；随机版本在 p. 16 对 pre-output state `U(x)` 条件化，并把每个 state 的最大概率真值输出组成集合 `A`。Theorem 2.2 的 proof 在 p. 17–18：oracle 初始 memory 为输入，read/write/move 操作模拟 Turing head，learner 以表查找重放 transition。论文明确承认该 learner 是类似 n-gram 的 string matching，未证明 gradient descent 的 Mamba/RNN 同样满足该保证。（PDF p. 15–18；`Proof of Theorem 2.1`、`Proof of Theorem 2.2`、`not a “standard” learning algorithm`。）

因此，「interactive tool-use 对 tractable long-form task 必要且充分」是该形式系统下的结论：必要性针对有限内部 memory 的 CoT-only/single-turn GSSM，充分性要求特定 read/write oracle、能停机的 Turing machine、任务专属正确 trajectory 与构造的 learner。摘要中「SSMs can learn to solve any tractable problem」的自然语言范围须随这些条件一起读取。（PDF p. 6，`interactive tool-use is both necessary and sufficient`；PDF p. 17–18，`Since f is tractable`、`simple tool-SSM algorithm`。）

## 5. 实验设计、结果、统计与图表

### 设计与复现粒度

- **研究问题和顺序**：Section 3 依次测试 arithmetic、algorithmic/reasoning、coding、long-context natural language；顺序对应引言中的三类应用，且都采用 thoughts/output/commands/observations 的交错轨迹。没有预先列出的 hypothesis 或 preregistration。（PDF p. 7，`various tasks, including arithmetic, reasoning and coding`；PDF p. 10，`Long-Context Natural-Language`。）
- **工具与训练目标**：addition、multiplication、Hanoi 用 pointer-based memory；logical graph 用 `find(x)` search tool；coding 用 bash。synthetic data 由期望算法生成，采用 next-token prediction + teacher forcing，mask input question 与 read observation 的 loss。（PDF p. 7–9，`standard next-token prediction objective`、`search tool`、`bash commands`。）
- **模型与匹配**：synthetic 比较 Mamba-130M、4-layer LSTM、4-layer GRU、Pythia-160M 与缩小的 Mistral-style local-attention Transformer；Mamba/Pythia 同为 24-layer、768-d model size、1536-d intermediate size。Mistral-style 仅 8 layers，故不应把所有 architecture differences 归因于 attention pattern。（Appendix C，PDF p. 18–19，`roughly matching Mamba’s scale`。）
- **预算与随机性**：synthetic sweep 7 个 learning rate、4 个 batch size、2 个 weight decay，固定 2,000 steps；每实验 2 seeds，报告 best model。Hanoi 例外地对 Mamba/Pythia 用 10 seeds、其余模型 3 seeds；code finetune 固定 lr 0.0001、wd 0.01、batch 512、200 steps，单节点 8 H100。（PDF p. 19，`report the accuracy of the best model`。）
- **coding 数据**：对 n=4–16 function 的合成 codebase，收集三类 agent 各约 100K trajectories。只保留正确修复且短于该 n 平均长度的轨迹；训练 context 为 8,192，测试允许生成越过训练 context。（PDF p. 9，`filter the trajectories`、`around 100K trajectories`。）
- **Oolong 设置**：用 Yahoo Answers Topic Classification 样例，训练不超过 5 examples 的 hard-coded retrieval trajectory，评测至 25 examples。（PDF p. 10，`up to 5 data examples`、`up to 25 examples`。）
- **未报告项**：未给测试集样本分母、synthetic 任务的完整 seed-wise 数值、正式 data-leakage audit、显著性检验、bootstrap、Bayesian analysis、effect size 或多重比较处理；这些字段为 `not_present`，不能从图形补写。（PDF p. 7–10、18–19；图表 caption 与 Appendix C。）

### 主要结果

| 结果主张 | 证据与量值 | 比较 / 聚合单位 | 统计处理与不利解释 |
|---|---|---|---|
| pointer tool 使 add 的 Mamba/LSTM/RNN 外推 | Figure 2：训练 `≤5` digits，Mamba 和 LSTM 在至多 1,000 digits 仍为 1.0；Pythia/Mistral 很早降至接近 0。 | exact trajectory + final-answer recovery，序列长度横轴为 log scale。 | 无误差条或分母；作者称没有测量超过 1,000 digits。 |
| SSM/RNN 在四类 synthetic task 的最大可达长度通常高于 Transformer | Table 1：Mamba 10→1K (100%) 两种 multiplication，10→1K (98%) logical graph，Hanoi 8→12 (49%)；Pythia 分别为 10→20 (79%)、10→14 (12%)、10→1K (5%)、8→8 (100%)。 | 表格值是达到至少 5% accuracy 的最大 `m`，各模型的 best seed。 | 该阈值摘要不展示完整曲线，也不提供不确定性；Hanoi 的有限外推显示反例式边界。 |
| interactive coding trajectory 比 single-turn 更支持 Mamba 的大 codebase 外推 | Figure 1：训练只含最多 16 files、8K context；主文称大 codebase 上 Mamba 在 interactive/distillation trajectory 时维持更好 accuracy，而 single-turn 时失败。 | code fixing pass rate；Pythia 在较小 distillation codebase 有超过 90% pass rate。 | 主文未给单点数表、误差条或测试分母；training trajectories 已按成功与短度筛选。 |
| Oolong natural-language task 上 Mamba 在 OOD examples 保持优势 | Figure 3：训练 5 examples，10–25 examples 的 OOD 点上蓝色 Mamba 曲线始终高于橙色 Pythia 曲线。 | accuracy by number of examples。 | 图无 error bar、分母和 seed 信息；该结论只能覆盖所选 Oolong representative task。 |
| hybrid 与 RMT 比较 | Appendix D.9：Hybrid-Mamba 从 5-digit 到 1,000-digit addition 仍 100%；RMT 在 5-digit 为 100%，却没有 meaningful length generalization。 | exact accuracy。 | 仅一个 task 和两种 RMT segment length；完整曲线未列。 |

Figure 1–3 的用途分别为：将三种 coding-data generator 与 pass-rate 曲线并置、用可见 trajectory 解释 pointer memory 并给出 addition 曲线、在 natural-language task 上给出紧凑 OOD 曲线。Table 1 是主文唯一主结果表，caption 自包含了 `n→m(p%)` 的阈值定义。Figure 4–10、Table 2 置于附录，分别承担 task construction、seed sensitivity、baseline curves、training-budget/digit-length ablation、task-mixture、agent trajectory statistics 的角色。（PDF p. 2–3、7、10、20、22–26；`Figure 1` 至 `Figure 10`、`Table 1`、`Table 2`。）

### 消融、负面结果与限制

- **交互成分消融**：Appendix D.7 对 5-digit addition 测 No-CoT、No-CoT reversed answer、No Tool-Use、Single-Turn Tool-Use。前两项和 single-turn 在 in-distribution 达 100%，却只有 little-to-no length generalization；No Tool-Use 连 in-distribution 也差。这为 Theorem 2.1 的有限实验对应提供直接支持。（PDF p. 24–25，`Experiments 1,2 and 4`。）
- **训练预算 / 长度**：Figure 7 用 5 runs 的 median absolute discrepancy envelope；更多 train digits 与更多 steps 提升 OOD stability，20 digits 在测试至 1,000 digits 时为 perfect。该图放在附录，主文只以短句导向 D.6。（PDF p. 24，`error envelope`、`up to 20 digits`。）
- **任务混合**：250 steps 时 auxiliary addition 对 multiplication 的改善较小，500 steps 时某些 weights 延伸更远，800 steps 时设置都趋于强泛化。Figure 8–9 标有跨 seed variability error bars。（PDF p. 8、25，`under limited budgets`、`error bars indicate variability across random seeds`。）
- **Tower of Hanoi 的负面边界**：解长度随 disk 数指数增长，12 disks 的 sequence 超过 385,000 tokens；即使 token accuracy 很高，exact sequence accuracy 对 seed 高敏感。Mamba 12 disks token accuracy 仍至少 99.75%，但 Figure 5 的 10 个 seed exact accuracy 离散很大；Pythia token accuracy 不超过 93%。recursive algorithm 也弱于 iterative algorithm。（PDF p. 8、21–23，`scales exponentially`、`sensitive to the random seed`。）
- **显式范围限制**：Theorem 2.2 的 learner 是 string matching；code task 是合成 dependency graph 和已知 `v10` bug；自然语言实验只有一个 benchmark task；Appendix F 的 pretrained SSM 证据只是 Mamba-Codestral-7B-v0.1 在 BFCL 的 16.58% overall accuracy。主文没有独立 `Limitations` 或 ethics section。（PDF p. 6、9–10、27；`not a “standard” learning algorithm`、`16.58%`。）

## 6. 闭环矩阵

| 引言 / 摘要主张 | 方法与理论回应 | 实验 / 消融回应 | 结论回收 | 状态 |
|---|---|---|---|---|
| 固定记忆的 GSSM 在 truly long-form task 上会失效 | GSSM 与 coverage 定义；Theorem 2.1。 | D.7 的 no-tool/single-turn addition。 | 重申 efficiency–accuracy trade-off。 | `closed`（形式系统内）。 |
| interactive tool-use 可绕过内部 memory bottleneck | stateful oracle、Turing tape simulation；Theorem 2.2。 | Figure 2、Table 1、Figure 1、Figure 3。 | 称 tools 带来 efficiency、accuracy、generalization。 | `partially_closed`：实证有限，定理 learner 非 SGD-trained Mamba。 |
| single-turn tool-use 仍受限 | Theorem 2.1 把 single-turn 放在同一负面类。 | Figure 1 的 single-turn coding 与 D.7 的 calculator ablation。 | p. 10 再次称 interactive 才有效。 | `closed`（形式系统；实验仅实例）。 |
| SSM/RNN 跨 arithmetic、reasoning、coding 长度外推优于 Transformer | 以工具轨迹作为 mechanism。 | Table 1、Figure 1–3、Figure 6。 | 作为 system-level architecture claim 回收。 | `partially_closed`：best-seed、有限 tasks、无统一不确定性。 |
| SSM 是高效的真实 agent alternative，甚至可优于 Transformer agents | 没有端到端效率定理或 agent benchmark 定义。 | 没有 wall-clock、cost 或广泛真实 agent comparison。 | 使用 `potentially`、`could`、`competitive with, or even superior`。 | `open`。 |
| standalone 与 system 中的架构强弱会翻转 | 用 external state 解释。 | 仅给若干构造 task 与 coding task。 | 作为最后一段 broader framing。 | `not_testable_here`。 |

## 7. 附录职责与正文自足性

| 模块 | 页码 | 类别 | 正文调用与承担内容 |
|---|---:|---|---|
| A `More Definitions` | 15 | `extended_method` | p. 5 调用 Appendix A；给 stateful oracle、tag protocol、三种 regime 的完整定义。 |
| B `Proofs` | 15–18 | `proof` | p. 6 两次调用 Appendix B；含 Theorem 2.1 的确定性/随机证明、Theorem 2.2、Lemma B.1 和 Claim。 |
| C `Architecture and Training Details` | 18–19 | `implementation_detail` | p. 7 调用 Appendix C；给 architecture dimensions、sweep、steps、seeds、H100。 |
| D.1–D.3 `Synthetic Experiments Details` / `Tool-Use Algorithms` | 19–21 | `extended_method` | p. 7–9 调用 D.1/D.3；给 pointer/search token protocol 与 addition/multiplication/Hanoi/DFS steps。 |
| D.4 `Tower of Hanoi Experiment Details` | 21–23 | `robustness` | p. 7 脚注调用 D.4；给 seed sensitivity、recursive variant 与 Table 2/Figure 5。 |
| D.5–D.9 | 23–26 | `ablation` | 主文调用 D.6–D.9；给 baseline curves、training-length/step、No-CoT/no-tool/single-turn、task mixture、Hybrid-Mamba/RMT。 |
| E `Code Fixing Agent Setup` | 26–27 | `implementation_detail` | p. 9 调用 Appendix E；给 mini-SWE-agent prompt/workflow 和 Figure 10。 |
| F `Tool Use Capabilities of Pretrained SSMs` | 27 | `additional_result` | p. 10 调用 Appendix F；给 BFCL 16.58% 结果。 |

附录约为主文可读词数的 0.95 倍。主文保留决策关键对象：问题定义、定理陈述、tool mechanism 的压缩解释、主任务和主比较。完整证明、精确 token protocol、hyperparameter sweep、seed-level Hanoi 异质性、交互成分消融和 code prompt 都被移入附录。主文可理解因果链；审查 Theorem 2.2 的学习构造和 Mamba 经验结论的稳健性仍需 Appendix B–D。（PDF p. 6–10、15–26；`The full proof is given in Appendix B`、`See Appendix C`、`Additional ablations`。）

## 8. 用词、修辞与呈现模式

对 p. 1–10 做大小写不敏感扫描并剔除页眉后，核心二/三元短语是 `length generalization`、`long-form generation`、`interactive tool-use`、`pointer-based memory tool`、`training data` 和 `Turing machine`；它们分别推动目标量、问题类、机制、实例实现、学习条件和理论模拟，不是纯模板词。`Mamba`、`trajectory/trajectories`、`complexity`、`pointer`、`code`、`agent` 也高频，反映实验围绕具体 architecture 与 trace 组织。（PDF p. 1–10；`length generalization`、`interactive tool-use`。）

作者第一人称动作的扫描结果为：`we show` 11 次（其中至少 1 次是图示说明语境）、`we prove` 2 次、`we observe` 7 次、`we find` 1 次；`we introduce` 1 次。`we demonstrate` 出现在摘要的连字符断行中，故朴素短语扫描未计入。强主张常与 `prove`、`cannot`、`any tractable`、`perfect` 连用；弱化和边界信号包括 `given the right choice`、`to some extent`、`potential`、`could`、`seems`。按句级显性作者主张粗编码，强 13 条、条件化/弱化 16 条；同一句可同时含强结论和范围条件。（PDF p. 1、2、6、8–10；`given the right choice`、`not a “standard” learning algorithm`、`potentially`。）

可验证的呈现反模式如下，不推断作者意图：

1. **best-seed summary**：synthetic experiments 多为 2 seeds 并报告 best model；Table 1 只给每模型跨阈值的最大可达长度。Figure 5 说明 Hanoi 对 seed 极敏感。（PDF p. 7、19、22；`Best performing seed is reported`。）
2. **关键消融后移**：main text 用一句话把 no-CoT/no-tool/single-turn 结果导向 D.7，主文不展示相应图或表。（PDF p. 7–8、24–25；`Additional ablations`。）
3. **success/short trajectory conditioning**：coding distillation 的训练语料只保留修复正确且短于平均长度的 trace，主文没有报告被过滤比例。（PDF p. 9，`filter the trajectories to include only trajectories that correctly fixed the code`。）
4. **不确定性与分母不一致**：D.6/D.8 给 envelope 或 error bars，Figure 1–3 和 Table 1 没有；主文也未给各测试点分母。（PDF p. 2–3、7、10、24–25；图表 layout 与 caption。）

## 9. 最终判断

**单一主线。** 有限内部状态使 standalone CoT/single-turn GSSM 无法覆盖复杂度持续增长的输出；把可读写外部状态接入多轮交互后，有限控制器可以学习并重复 Turing-style local transitions，因此在任务专属 trajectory data 下可跨长度泛化。Section 3 把这一机制映射到 pointer、search 与 bash 三种工具。（PDF p. 5–9；`bounded memory`、`simulate the operations of a Turing machine`。）

**最有效的写作和视觉模式。** p. 2–3 在正式定义前先用 Figure 1 的 coding curve 和 Figure 2 的 memory trace/accuracy pair 给读者可见机制，再在 p. 6 用「负面不可能性 + 正面构造」的相邻定理收紧叙事；Table 1 随即将多个 synthetic task 压缩到同一可读指标。这一顺序把系统机制、理论边界和实验范例串成一条链。（PDF p. 2–3、6–7。）

**最大缺口。** Theorem 2.2 的存在性保证依赖 task-specific correct traces、一个 read/write oracle 和 finite string-matching learner；论文没有证明 gradient-trained Mamba 可在开放任务中学到该 transition table。经验部分有大范围外推，却以合成任务、best-seed 汇报、成功/短 trajectory filtering 和有限 Oolong/coding task 为主，也没有直接报告端到端效率或成本。（PDF p. 6、9、19、24–27。）

**可迁移规则。** 当论文声称外部工具解除某架构的能力瓶颈时，应把无工具时的失效边界、工具改变的可访问信息、可执行的局部轨迹、与该机制一一对应的 component ablation 和长度外推指标同时放入主论证。该规则适用于 tool state 的内容、协议与训练轨迹可明确指定的任务；它不自动证明现实 agent 能学会工具选择、应对错误工具反馈，或以更低端到端成本完成开放任务。

# Q-RAG 深读备忘

## 文档边界与来源

- **论文**：Q-RAG — Long Context Multi-Step Retrieval via Value-Based Embedder Training
- **身份**：ICLR 2026，`oral`；OpenReview forum `MS9nWFY7LG`
- **实际来源**：`corpus/pdfs/iclr-2026-dff0527cb8cf.pdf`，官方 proceedings PDF，物理页 26 页。OpenReview 论坛为 <https://openreview.net/forum?id=MS9nWFY7LG>，官方 PDF 地址为 <https://proceedings.iclr.cc/paper_files/paper/2026/file/372dee09e0c3c17df69d990b4735adac-Paper-Conference.pdf>。
- **页级边界**：正文 p. 1–10；references p. 11–13；appendix p. 14–26。正文最后一个主节是 p. 10 的 `6 Conclusion`，附录从 p. 14 的 `A Inner Product Approximation for Q-Function` 开始。
- **版面**：正文和附录均为双栏 letter 页面；Figure 1、Figure 2 跨栏，主要表格和公式在栏内。p. 7 的 Table 1、p. 8 的 Table 2、p. 9 的 Table 3 均把大量数字压入窄栏，p. 22–23 的附录表格也采用紧凑多列排版。p. 26 只有 Table 8 和 Fact-level metrics，页底留白较大。

物理页地图如下。`theory` 没有独立正文标题；Appendix A 的主要职责是形式理论与证明，因此在语义清单中单独标出，物理边界仍属于 appendix。

| 标题 | 物理页 | 语义模块 | 作用 |
|---|---:|---|---|
| Abstract | 1 | abstract | 问题、方法、结果和代码入口 |
| 1 Introduction | 1–2 | introduction | 从长上下文缺陷推进到三项贡献 |
| 2 Related Work | 2–3 | related_work | agents、LLM fine-tuning、retriever fine-tuning、recurrent models、RoPE |
| 3 Methods / 3.1 Preliminaries | 3–4 | method | MDP、状态、动作、支持事实奖励 |
| 3.2 Value-Based RL for Embedder Fine-Tuning | 4–5 | method | soft Q、双 embedder、PQN、λ-return、Algorithm 1 |
| 3.3 Temporal Reasoning for Long-Context Search | 5–6 | method | relative positional mapping |
| 4.1 Experimental Setup | 6 | experimental_design | 数据集、任务、基线来源 |
| 4.2 Commonsense Reasoning on Ultra-Long Contexts | 6–7 | results | BabiLong 与 QA3 |
| 4.3 Needle-in-a-Haystack and Long Context QA | 7–8 | results | RULER 表 1 |
| 4.4 Open-Domain Question Answering | 8 | results | HotPotQA、MuSiQue 表 2 |
| 5 Ablation Study / 5.1 Sensitivity to Retrieval Budget | 8–10 | ablation | 组件、超参数和 retrieval budget |
| 6 Conclusion | 10 | conclusion | 回收主张、计算成本和未来方向 |
| Reproducibility Statement / Acknowledgments | 10 | other | 代码、checkpoint、硬件与致谢 |
| References | 11–13 | other | 31 条左右参考文献，物理边界单独计入 |
| Appendix A | 14–20 | theory（语义重分类） | inner-product approximation、Sobolev 与 RoPE 型理论 |
| Appendix B | 21–23 | appendix | Q-value early stopping |
| Appendix C | 23 | appendix | beam-search planning |
| Appendix D | 23–24 | appendix | complexity and efficiency |
| Appendix E | 25 | appendix | extra QA results |
| Appendix F | 25 | appendix | training details |
| Appendix G | 25–26 | appendix | evaluation details 与 Fact EM 定义 |

估计正文叙事词数约 4,810，词数口径排除了 references、表格数字和公式碎片；物理主区连同图表标题约 4,953。Appendix A–G 约 5,482 个英文 token，含公式周边文本；references 约 1,131 个 token。该估计用于模块比例，原始 token 计数仍以项目汇总脚本为准。

## 摘要逐句功能

摘要按原文句号划分为 7 句，功能链是 `object_scope → problem_gap → problem_gap → limitation → core_idea/method → quantitative_result/qualitative_result → impact_claim`。结果句位于方法句之后，最强的经验主张落在第 6 句；摘要没有定理句，也没有独立 limitations 句。

| 句 | 功能与证据 | 约词数 |
|---:|---|---:|
| 1 | `object_scope`。RAG 通过筛选相关上下文降低 hallucination 和 inference cost。证据 p. 1，`enhance LLM performance`。 | 19 |
| 2 | `problem_gap`。single-step retrieval 对复杂 multi-step search 不足。证据 p. 1，`single-step retrieval`。 | 21 |
| 3 | `problem_gap`。已有 multi-step 方法常 fine-tune small LLM。证据 p. 1，`fine-tuning of small LLMs`。 | 17 |
| 4 | `limitation`。这类 fine-tuning 资源成本高，并限制更大 LLM 的使用。证据 p. 1，`highly resource-intensive`。 | 16 |
| 5 | `core_idea`、`method`。Q-RAG fine-tune Embedder，以 RL 执行 multi-step retrieval。证据 p. 1，`fine-tunes the Embedder model`。 | 21 |
| 6 | `quantitative_result`、`qualitative_result`。作者声称在 BabiLong、RULER 及 10M-token context 上达到 SOTA，并在 open-domain QA 具竞争力。证据 p. 1，`contexts up to 10M tokens`。 | 33 |
| 7 | `impact_claim`。给出 GitHub 代码入口。证据 p. 1，`Code is available`。 | 5 |

摘要没有报告 seed、误差表达、baseline 复现实验比例或失败案例。它把资源效率放进 problem/method 链条，把“10M tokens”放到结果句中，因此读者会先接受跨长度能力，再在正文看到 baseline 来源差异。

## 引言论证推进

引言的完整推进链是：LLM 长上下文缺陷 → RAG 的短上下文收益 → single-step 对复杂问题不足 → graph/agent/LLM fine-tuning 的代价与脆弱性 → latent-space value-based RL → 长上下文和 open-domain 结果预览 → 三条贡献。每一段都给出下一段所需的缺口；贡献列表与摘要有重叠，但加入了 temporal mechanism 这一正文可检验对象。

| 序 | 动作 | 页码 | 段落回答的问题 | 下一段钩子 |
|---:|---|---:|---|---|
| 1 | `context` + `problem` | 1 | LLM 有静态知识、长上下文低效、attention dilution 和 hallucination，RAG 是常用应对 | RAG 如何缩短输入 |
| 2 | `context` + `failure_of_prior_work` | 1 | RAG 筛选相关片段，但 single-step 只适合简单 NIAH；graph 方案需处理整个 context | agent 与多步检索的代价 |
| 3 | `failure_of_prior_work` + `missing_insight` | 1 | LLM agent 会被 noisy retrieval 影响后续 query，因此需要 joint optimization | 直接 fine-tune LLM 的成本 |
| 4 | `failure_of_prior_work` + `scope_boundary` | 1 | LLM fine-tuning 能改善检索交互，却增加大模型门槛 | 用 embedder 承担检索策略 |
| 5 | `core_idea` + `method_preview` | 2 | 用 RL 在 text-chunk embedding latent space 训练检索 agent，得到 compact model | 结果范围和贡献 |
| 6 | `result_preview` | 2 | BabiLong、RULER 可到 10M tokens，MuSiQue/HotPotQA 保持竞争力，并声称更快更便宜 | 贡献列表 |
| 7 | `contribution_list` | 2 | TD RL multi-step agent；ultra-long commonsense/NIAH；temporal information in embedder | related work 中的定位 |
| 8 | `contribution_list` | 2 | 贡献三把 temporal reasoning 作为可检验方法点提出，但没有在此列出单独消融 | §3.3 与 QA3 |

贡献列表的可证伪部分是“TD RL”“10M-token benchmark 结果”和“temporal reasoning mechanism”；“resource-efficient”“generalizes well”需要实验设置与 appendix 的计算信息共同支撑。引言没有列出明确研究问题、预注册假设或失败判定。

## 相关工作

相关工作位于独立第 2 节，占正文叙事约 560 词，跨 p. 2–3。引用组织采用“方法族 → 最近邻差异 → 长上下文模型族”的分类推进，没有独立 chronology。主要引用簇如下。

1. **Fine-tuning-free agents 与 knowledge graph**：Search-o1、GraphReader、HippoRAG、AriGraph。比较维度是额外训练与 inference-time 全文处理成本。
2. **Fine-tune LRM/LLM 的多步检索**：IM-RAG 使用 PPO，R1-Searcher、Search-R1、RAG-RL、ReSearcher 使用 GRPO。比较维度是冻结 embedder、训练 LLM 的资源和模型尺寸限制。
3. **Retriever 或 reranker fine-tuning**：RePlug 使用 LLM feedback，BeamRetriever 训练 trajectory reranker。比较维度是 multi-step 能力、RL 信号、dot-product scaling 和 transformer forward 次数。
4. **Recurrent long-context models**：Mamba、RMT、Titans、MemUP、ATLAS、ARMT。比较维度是 1M–10M context 的可扩展性与 recurrent/attention 机制。
5. **Positional encoding**：LongRoPE2。比较维度是 RoPE scaling 的 context window 延伸，作者将 Q-RAG 放在检索类而非 LLM context-extension 类。

最清楚的 nearest-neighbor contrast 在 p. 2：Q-RAG 只 fine-tune embedder，LLM 可保持冻结并与任意尺寸、含 proprietary LLM 配对。相关工作没有把每个引用簇再次完整讲成方法；正文后续引用主要承担 baseline 归属和结果来源说明。局限是多数“state-of-the-art”比较由原论文 reported numbers 构成，跨论文设置差异在 §4.1 被承认但没有统一重跑。

## 方法与理论

### 方法主线

方法的逻辑转移为：`setup_notation → state_problem → define_component → explain_mechanism → derive → instantiate_algorithm → connect_to_prediction → connect_to_experiment`。形式化对象首次出现于 p. 3 的 dataset triples `(C,q,y)`、chunk set `C`、MDP `(S,A,p,r,γ)`、ordered state `s_t` 和 available action set `A_t`。状态保留 query 与已选 chunks，并按原 document order 排序；transition 是 deterministic，episode 由步数预算 `T` 或 `STOP` 终止。

- **奖励**：若有 support facts `F⋆`，intermediate reward 为 0，terminal reward 仅在最终 state 覆盖全部 support facts 时为 1。作者明确不采用 LLM-based reward，所有报告实验依赖 support-fact signal（p. 4）。这把 retrieval correctness 直接连接到训练目标，也把 answer-quality reward 留作未来方向。
- **Soft value functions**：Eq. (1) 定义 soft `Qπ` 的 Bellman 递归，Eq. (2) 将 entropy 项纳入 `Vπ`。Eq. (3) 用以最大 Q 为基准的 Boltzmann policy 采样 action，temperature `α` 随训练退火到 0。
- **Value-based embedder**：state embedder `Es(st;θ1)` 和带 position 的 action embedder `Ea(ai,i;θ2)` 映射到 `Rd`；Q 值为 inner product。候选 chunk 先整体 embedding，state 每步更新，避免对每个候选执行 trajectory transformer。
- **PQN 与 λ-return**：PQN 去除 replay buffer，目标网络与 soft value 是相对原 PQN 的关键改动。λ-return、target value 和 mean-squared Q loss 写在 p. 4；Algorithm 1 将 K 个 environment 并行 rollout，再用 EMA 更新 target parameters。
- **Temporal reasoning**：已选 document indices 将候选空间切成 `k+1` 个 interval。`ρ_t(i)` 先识别候选位于哪段，再在段内保留相对顺序；Eq. (7) 将 absolute position 换成 relative position。作者把它连接到 narrative text 中“先发生什么”的选择问题，但正文没有对 relative encoding 做单独组件删除实验。

### 算法与复杂度

Algorithm 1 的输入超参数是 `K,T,α,λ,τ`；初始化两个 embedder、online critic 与 target critic；每个 environment reset query/context，预计算 action embeddings，按 softmax policy 采样 action，计算 value/reward、拼接 state、删除已选 action，之后反向计算 λ-return 并更新 θ 与 θ′。关键不变量是 `A_{t+1}=A_t\{a_t\}`，state 始终是 query 加已选 chunks 的 document-order 列表。

Appendix D 将 action embedding、state embedding、search policy 和 answerer 分开计算。原始文档长度为 `N` 时，action embedding、naive all-action dot products 与存储都为 `O(N)`；state embedding 对 `N` 为 `O(1)`；LLM Answerer 只见检索结果，对原始 `N` 的时间与内存为 `O(1)`。Approximate kNN 可在实践中降低 search query time，但本文没有给出该实现的实测曲线。Figure 6 显示两个任务约 12 小时内从低 return 快速升至平台，训练硬件为单张 A100-80GB。

### 理论核对

论文给出 65 个编号 displayed equations，且每一个编号公式都是 displayed。主方法是 Eq. (1)–(7)，Appendix A 是 Eq. (8)–(65)。公式逐段核对如下。

| 范围 | 页码 | 内容 | 数量 |
|---|---:|---|---:|
| (1)–(5) | 4 | soft Q、soft V、Boltzmann policy、soft value、Q loss | 5 |
| (6)–(7) | 5–6 | relative positional mapping 与 embedder replacement | 2 |
| (8)–(15) | 14–16 | real RoPE score、complex diagonal form、Theorem 1 的函数类与密度证明 | 8 |
| (16)–(34) | 16–17 | Lemma 1 的 Sobolev low-rank proof、Fourier/truncation/feature maps | 19 |
| (35)–(45) | 18 | Theorem 2 假设、Fourier 展开、temporal truncation | 11 |
| (46)–(57) | 19 | coefficient low-rank、全局 RoPE 表示、误差平衡 | 12 |
| (58)–(65) | 20 | L2 收束、L∞ 边界、额外平滑条件与 rate | 8 |
| **总计** | **4–20** | 1–65 均有页码证据 | **65** |

正式理论块是 3 个命题和 3 个证明。Theorem 1（p. 15–16）在 `Φ` 为含常数、可分离点且 self-adjoint 的 subalgebra 时，说明带 diagonal positional matrix 的 complex inner-product class 在 `C(K,R)` 中 dense。Lemma 1（p. 16–17）把 bounded Lipschitz domain 上的 Sobolev kernel 变成 rank-`d` inner product，给出 `d^{-s/(dx+dy)}` 的 `L2` 误差率。Theorem 2（p. 18–20）再对 temporal Fourier mode 与 spatial low-rank 组合，给出 `d^{-s/(D+1)}` 的 RoPE-type `L2` 近似率。三段 proof 都在 Appendix A 内完成。

机器词法正则会得到 9 次 `Theorem/Lemma/Proposition/Corollary + number`，其中包含 Theorem 1、Lemma 1、Theorem 2 的重复交叉引用。修正后应报告为 3 个正式 theorem/lemma statements、3 个 proof blocks；没有正式 proposition 或 corollary。这个差异已记录在 JSON 的 `measurement_disagreements`。

理论对主因果链的作用是“保证 value function 的 inner-product factorization 具有表达能力，并解释 RoPE/relative position 的可扩展结构”。证明没有被实验直接检验，实验检验的是该架构在 context length、任务和消融上的行为；论文也明确提示 Theorem 2 的 `L2` bound 不自动给出 uniform `L∞` guarantee（p. 20）。

## 实验设计

实验设计将任务分成四类：BabiLong 的 commonsense/temporal reasoning，RULER 的 NIAH 与 long-context QA，以及 HotPotQA、MuSiQue 的 open-domain multi-hop QA。context length 从 4K 到 10M tokens。基线按来源标记为 `× Ablation`、`✓ Reproduced`、`◦ Reported`，这使结果表能同时容纳重跑数字和原论文数字。

- BabiLong：Figure 2 展示平均 Q1–QA5 与最难 QA3；QA3 至少需要三个 facts 与 temporal reasoning。
- RULER：Table 1 覆盖 4K、16K、32K、128K、1M，列出 single-needle、multi-key、multi-value、multi-query、SH QA、MH QA。
- Open-domain QA：Table 2 使用 HotPotQA 与 MuSiQue OOD；Q-RAG、Plan Q-RAG、Beam Retriever、Search-R1 等的事实与答案指标并列。
- 模型：open-domain 使用 `multilingual-e5-large` 和 `Alibaba-NLP/gte-multilingual-base`；BabiLong/RULER 使用 `facebook/contriever`。生成器为 QwQ-32B 或 Qwen3-4B，细节见 Table 8。
- 训练：AdamW、linear warm-up/decay、gradient clipping、gradient accumulation，以及 `γ=0.99, α=0.05, λ=0.5, τ=0.02` 写在 Appendix F。单模型不超过 12 小时单张 A100-80GB。
- 复现实验粒度：公开了数据集、任务、模型、chunk size、T、部分优化器和硬件；没有列出每个主结果的完整 seed、样本数或统一训练预算。Table 3 明确采用 3 seeds；Table 4 明确为 HotPotQA 1,000 samples。
- 缺项：正文没有预先列出研究假设，没有独立 data-leakage 控制或失败判定协议，也没有显著性检验、多重比较或 bootstrap。表中 `±` 只在 Table 3 出现，作者没有说明其具体离散量定义。

实验顺序大体对应引言贡献：先用 BabiLong/RULER 支撑超长上下文，再用 HotPotQA/MuSiQue 支撑 open-domain transfer，最后用组件消融和 retrieval-budget sensitivity 检验训练选择。Temporal mechanism 与 QA3 有语义对应，却缺乏单独相对位置删除对照。

## 结果、统计与可视化

### 主结果

1. **BabiLong（Figure 2，p. 6–7）**。作者报告 Q-RAG 在 1M–10M tokens 的平均性能最高，QA3 上随长度增加几乎没有 degradation，并称相对所有 baseline 的 gap 在 QA3 最大。Figure 2 是折线图，x 轴为 context length，solid/dashed 分别表示 fine-tuned/zero-shot。图中没有表格化原始点值，也没有误差带；多数 baseline 分数取自原论文。Beam Retriever 在 QA3 的额外 fine-tuning 失败；Titans 与 Atlas 因缺少 subtask breakdown 未画入 QA3 图。
2. **RULER（Table 1，p. 7–8）**。Q-RAG 的 NIAH Avg 在 4K、16K、32K、128K 为 100，1M 为 99.7；MH QA 为 67、64、65、65、61。相同长度下 Beam Retriever 的 MH QA 为 39、35（只报告到 16K），LongRoPE2 的 MH QA 为 60、58、55、50。表格只给点估计，缺失结果用 `n/a`，没有 seed 或区间。
3. **HotPotQA/MuSiQue OOD（Table 2，p. 8）**。Q-RAG 的 HotPotQA Fact F1/EM 为 0.93/0.89，Ans F1/EM 为 0.76/0.59；MuSiQue OOD Fact F1/EM 为 0.71/0.55，Ans F1/EM 为 0.52/0.37。作者称 Q-RAG 超过其他对照，并在 OOD 上超过 alternatives；Beam Retriever 的 HotPotQA fact 分数更高（0.97/0.94），且评估时使用 gold hop count。Q-RAG 的 Plan variant 与 vanilla Q-RAG 接近。
4. **指标定义**。Fact EM 只要求 predicted supporting facts 覆盖 ground-truth set；多取 irrelevant chunks 仍可得满分。Fact F1 才反映 noise inclusion。该定义直到 Appendix G p. 26 才给出，解释了 Table 4 中 Fact EM 上升与 Fact F1 下降可以并存。

### 统计处理

论文主要使用 sample/task 聚合后的 accuracy、Fact EM/F1、Ans EM/F1、average return、episode length、TPR/FPR 和 ROC AUC。Table 3 是 3 个 random seeds 的平均值，附带 `±`，但没有声明是 standard deviation、standard error 还是其他 dispersion。Table 4 是 1,000 个 HotPotQA samples；其他主表没有给出样本分母。没有 hypothesis test、multiple-comparison adjustment、bootstrap、Bayesian analysis 或 regression。作者把显著性语言用于跨方法差异，却没有配套 uncertainty；可辩护的决策量主要是 exact/Fact coverage、answer F1、跨长度走势和消融中的性能落差。

可视化承担的任务不同。Figure 1 解释 state/action embedder 与 environment 的数据流；Figure 2 负责 context scaling；Figure 3 负责 α、λ 和 runtime sensitivity；Figure 4 把 early/late/perfect stop 与 episode length 分开；Figure 5 把 threshold trade-off 压成 ROC；Figure 6 展示训练收敛。表格承担可复核数值，尤其 Table 3 把 target network、soft Q、RL 与 SFT 放在同一组长度上。图注通常能说明任务和坐标，但 Table 1 的 `n/a` 来源、Table 3 的 `±` 语义和 Table 7 的缺失项仍需正文补读。

## 消融、负面结果与自我设限

正文消融从 p. 8 开始，约 560 词，占正文叙事约 11.6%，含 Figure 3、Table 3、Table 4。它覆盖以下对象。

| 对象 | 识别目标 | 结果或边界 |
|---|---|---|
| Multi-step RAG w.o. FT | RL fine-tuning 是否有贡献 | QA3 F1 约 15.34–16.38，远低于 Q-RAG 的 96.5–97.8 |
| Multi-step RAG w. SFT | RL 相对 trajectory SFT 的作用 | QA3 F1 约 18.30–20.87，仍低于 Q-RAG；1M 未报告 |
| Q-RAG w.o. Target | target network 对稳定性和性能的贡献 | 约 75.9–79.2，且 `±26.0–28.2` 很大 |
| Q-RAG w.o. Soft-Q | entropy regularization 与 soft value 的贡献 | 约 93.3–95.9，低于完整 Q-RAG，但波动较小 |
| α、λ sensitivity | 探索温度和 λ-return 稳定区间 | Figure 3 只给曲线，不给每点数值表 |
| retrieval budget | 取回步数对事实与 answer 的影响 | 2→3 步提升 Fact EM 与三种 LLM 的 Ans F1；更高步数 Fact F1 下降 |

Table 3 的 `±` 使 target-network 删除的失稳可见；然而它没有说明 `±` 的统计定义，也没有给出每个 seed 的轨迹。作者报告 Beam Retriever 在 QA3 失败，这是正文中最明确的 negative result。Appendix B 的 early stopping 是额外的 robustness/efficiency 检验，不属于正文组件删除。

Appendix B 把 Q-value threshold 的错误拆成 early、late、perfect。HotPotQA 在 threshold 0.2 时 Fact F1 为 0.917、perfect stop 为 0.892、episode length 为 2.13、TPR/FPR 为 0.937/0.032，AUC 为 0.961。BabiLong QA2 在 threshold 0.2–0.6 时 perfect stop 为约 0.964–0.990，episode length 从 2.29 降到 2.21，Fact F1 约 0.949–0.954，AUC 为 0.970。threshold 接近 1.0 后两套任务都出现早停和性能塌陷。

可观察到的 presentation strategy 是结果来源分层、缺失项显式用 `n/a` 或 em dash、把 QA3 失败放在主结果段落、把更细的 threshold trade-off 放入 appendix。没有证据支持“作者刻意隐藏”之类的意图判断，因此这里仅记录版面位置和分母定义。

## 结论、限制与闭环

结论 p. 10 回收了方法、BabiLong/RULER 与 MuSiQue/HotPotQA 结果、context scaling、单张 A100-80GB 的训练成本和冻结 LLM 的部署灵活性。它没有引入新数字；未来工作包括 structured LLM reward、embedding-space compositional/temporal reasoning 和与 generation 的更紧耦合。

论文没有独立 `Limitations` 标题。可定位的边界包括 support-fact reward 限制、baseline 设置异质、Beam Retriever 在 QA3 失败、主结果缺少完整 uncertainty、relative temporal encoding 没有单独 ablation、Fact EM 对额外噪声宽容，以及 Theorem 2 只有 `L2` guarantee。Appendix G 对 Fact EM 的 set-inclusion 定义是解释主表的关键后置细节。

闭环矩阵如下。

| 引言主张 | 方法回应 | 证据回应 | 结论回收 | 状态 |
|---|---|---|---|---|
| multi-step retrieval 需要搜索式 state | MDP、ordered state、action removal | Figure 1、BabiLong QA3 | 回收 multi-step latent retrieval | closed |
| fine-tune LLM 成本高 | 只 fine-tune state/action embedder | Appendix F 的单 A100 与 12h 上限 | 回收 compute efficiency | partially_closed |
| temporal context 需要相对位置 | `ρ_t(i)` 与 Eq. (7) | Figure 2 QA3 趋势 | 结论称 temporal reasoning | partially_closed |
| ultra-long context 可泛化 | 全文 chunk embedding + state/action inner product | Figure 2、Table 1 到 1M，Figure 2 到 10M | 回收 minimal degradation | partially_closed |
| soft Q 与 target network 有用 | soft value、target critic、λ-return | Table 3 | 回收组件收益 | closed |
| retrieval 质量驱动答案 | Fact EM/F1 与多 LLM answer metrics | Table 4 | 回收 budget 结论 | partially_closed |
| OOD multi-hop 可迁移 | HotPotQA fine-tune、MuSiQue OOD | Table 2、Table 7 | 回收 competitive OOD | closed |
| Q-value 可支持动态停机 | threshold policy、early/perfect/late 定义 | Appendix B Tables 5–6、Figures 4–5 | 正文只指向 appendix | closed |
| inner-product factorization 有表达能力 | Appendix A Theorem 1/2 与 proof | 65 equations、3 formal statements | 结论不逐项回收 rate | closed（理论） |

## 附录职责

Appendix 共 13 页，物理长度为正文 10 页的 1.3 倍；按英文 token 粗估约 5,482，超过正文叙事词数。它承担了论文的 proof、early stopping、planning、复杂度、额外 QA、优化细节、评价配置和指标定义。

- **A，p. 14–20，proof**：3 个正式理论 statement、3 个 proof blocks、Eq. (8)–(65)。正文 p. 4 通过“explicit rates in Appendix A”调用。主方法如果只读正文，无法检查 factorization 的 density/rate 条件。
- **B，p. 21–23，additional_result/robustness**：Q-threshold early stopping、oracle stop、HotPotQA/BabiLong QA2 的 Figures 4–5 与 Tables 5–6。正文 p. 10 明确指向 Appendix B；动态停止的性能和代价依赖此处。
- **C，p. 23，extended_method**：Plan Q-RAG 的 beam-search planning。正文 p. 8 调用 Appendix C，说明 dot-product Q 不需要每个候选重新做 transformer forward。
- **D，p. 23–24，implementation_detail**：answerer、chunk embedding、state embedding、search policy 的时间/空间复杂度与 Figure 6 收敛曲线。正文结论的效率解释依赖它。
- **E，p. 25，additional_result**：HotPotQA-distractors、MuSiQue in-distribution/OOD 的 Table 7。它扩充了 OOD 叙事，但主文 Table 2 已承担主要决策。
- **F，p. 25，hyperparameter**：AdamW、learning-rate schedule、`γ/α/λ/τ`、chunk cap、模型按 benchmark 的分工。正文 reproducibility statement 调用 Appendix F。
- **G，p. 25–26，reproducibility**：生成 LLM、decoding、retrieval steps、chunking 与 Table 8 配置，最后定义 Fact EM。它补足运行条件，也改变读者对 Fact EM 的解释。

正文保留了任务、主要对照、关键点估计和核心消融，足以理解方法方向；proof 的假设、训练/评价配置、early-stopping trade-off 和 Fact EM 的宽松定义被后置。对部署成本与指标语义而言，后置信息会增加自足性成本。

## 词频与修辞

项目汇总脚本负责原始 token 计数；下面是对正文 p. 1–10 去除 references、公式碎片、表格数值和模板页眉后的语境标注。高频词由领域名词主导，`Q-RAG`、`retrieval`、`multi-step`、`context` 和 `embedder` 直接对应单一主线。

- **高频实词**：`Q-RAG`、`retrieval`、`multi-step`、`methods`、`performance`、`context/contexts`、`results`、`HotPotQA`、`embedder`、`RAG`、`long-context`、`reasoning`、`baselines`、`LLMs`、`training`、`state`、`chunks`、`value`、`action`。这些词集中在 introduction、method 和 results，模板词比例较低。
- **二元词组**：`multi-step retrieval`、`long-context tasks`、`retrieval agent`、`state embedder`、`action embedder`、`open-domain QA`、`supporting facts`、`context length`、`answer accuracy`、`target networks`。
- **三元词组**：`multi-step retrieval methods`、`long-context multi-step retrieval`、`multi-hop question answering`、`value-based RL methods`、`Q-value threshold`、`ground-truth supporting facts`。
- **主张动词**：`propose` 用于摘要和贡献列表；`achieve/attain` 用于 benchmark 结果；`show/demonstrate` 用于图表走势和效率；`compare/evaluate/report` 用于实验来源与表格；`enable`、`allow`、`generalize` 用于 capability 连接。强动词多带有 benchmark 或 figure/table 证据，弱动词集中在 future work 与机制解释。
- **限定与因果**：`however`、`still`、`although`、`in contrast`、`while` 用于 prior-work contrast；`therefore`、`consequently`、`because`、`due to` 用于 resource/complexity 解释；`typically`、`often`、`some`、`primarily`、`virtually`、`around` 为限定词。作者把“reported/reproduced/ablation”标签作为证据强度提示。
- **强弱结构**：主文多用 `achieves state-of-the-art`、`highest average`、`outperforms`、`minimal degradation` 等强结果句，随后用 baseline 缺失、reported scores、OOD 和 appendix 配置限定范围。强主张约占结果段落的多数，限制主要以后置段落和表格标记承载。

## 最终判断

- **单一主线**：Q-RAG 把 multi-step retrieval 的策略学习从 LLM query generation 移到 value-based state/action embedder。RL 更新 embedder，dot-product Q 负责候选评分，relative position 为 narrative temporal search 提供状态相关坐标，最后把少量 chunks 交给冻结 LLM。
- **正文保留的决策内容**：MDP 与 reward、soft Q/target/λ-return、relative positional mapping、BabiLong/RULER/HotPotQA/MuSiQue 的主结果、组件消融、retrieval budget 和主要 baseline 来源标签。
- **移入附录的细节**：表达能力与收敛 proof、L∞ 适用边界、early stopping ROC、Plan Q-RAG、复杂度、训练曲线、extra QA、hyperparameters、模型/分块配置、Fact EM 定义。proof 和 Fact EM 对方法可信度及结果解释的影响较大，后置会提高读者复核成本。
- **最有效的模式**：Figure 1 先给 state/action/environment 数据流，Eq. (1)–(7) 随后只引入训练所需对象；Table 3 在同一 context-length 轴上同时删除 RL、target 和 soft-Q，使组件差异可直接比较；Appendix B 将早停错误拆成三类并与 ROC 对齐。
- **最大缺口**：relative temporal mechanism 没有单独 ablation；10M-token claim 主要依赖折线图与异源 baseline；reported/reproduced/oracle hop-count 设置并不完全同质；主文没有完整 seed、分母和 uncertainty 说明，也没有独立 limitations 节。
- **可迁移规则**：长上下文系统应把“检索状态如何形成、上下文长度如何变化、结果以什么分母比较、失败和计算代价在哪里”放进同一条证据链，并让每个新增机制对应一个隔离对照或可证伪预测。
- **适用边界**：该规则适合有检索轨迹和 context-scaling 轴的系统论文。纯生成模型或只有定性案例的工作，需要把轨迹可观测性、答案生成误差和任务级分母换成相应指标。

## 交付核对

- [x] 逐页读完 p. 1–26，包括 references、Appendix A–G。
- [x] 65 个编号公式已按页和编号写入 JSON；全部为 displayed equations。
- [x] 9 次机器 theorem/lemma 词法命中已与 3 statements + 3 proofs 区分记录。
- [x] Figure 1–6、Table 1–8、Algorithm 1 均有 inventory 条目。
- [x] 结果、消融、限制、负面呈现、附录职责、叙事闭环和词频均有页码证据。
- [x] JSON 先在临时路径校验，最后原子发布到目标路径；未改其他论文文件。

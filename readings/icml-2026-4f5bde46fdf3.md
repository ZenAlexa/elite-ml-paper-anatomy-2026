# Learning Unmasking Policies for Diffusion Language Models

- `paper_id`: `icml-2026-4f5bde46fdf3`
- 版本：`arXiv:2512.09106v4`，2026-06-01；本地文件为已验证预印本。
- 会议标记：ICML 2026，`oral`、`spotlight`。
- 读取边界：39 个 PDF 物理页，含正文、References 与 Appendix A–J；未提供独立 supplementary 文件。

## 1. 文档边界、页级地图与版面

| 区域 | PDF 页 | 作用与版面事实 |
|---|---:|---|
| 标题与摘要 | 1 | 标题、作者、摘要置于跨栏浅灰圆角面板；引言从页下半部进入双栏。 |
| Introduction | 1–2 | 以两段背景、问题转折、方法预览、结果预览和三条贡献完成论证链。 |
| Background | 2–3 | `2.1` 给出 MDM 训练与生成记号，`2.2` 用 Figure 1 展示置信度启发式的区块长度依赖。 |
| Learning Unmasking Policies | 3–6 | `3.1` MDP、`3.2` 轻量 policy、`3.3` GRPO 与 reward；Figure 2 跨栏结构图，Figure 3 为训练动态。 |
| Experiments | 6–11 | Figure 4 跨栏主 Pareto 图承担核心比较；Figure 5–8 依次处理机制、测试时控制、全扩散顺序和迁移；Figure 9 为四格消融。 |
| Related work | 11–12 | 约四段，按 heuristic、dLLM RL、其他加速、adaptive computation 分簇。 |
| Conclusion / limitations | 12–13 | 结论在页 12 开始，limitations 段落延续至页 13 的 References 标题前。 |
| References | 13–16 | 四页双栏参考文献；页 13 与正文尾段重叠。 |
| Appendix | 17–39 | Appendix 总览、算法、补充实验、定性轨迹、替代采样、expert steering、背景、配置、架构图与精确表格。 |

正文有 13 个承载主文内容的物理页；References 占 13–16 页，Appendix 占 17–39 页。页 13 因正文尾段与参考文献共页而与前两项重叠。主文基本为双栏，Figure 4、8、9 跨两栏；Appendix B 的小多图、D 的 token-grid 轨迹和 J 的并排窄表压缩了文字可读面积。页 17、18、35–37 留有大块留白，页 37 仅引出精确数表，数值本体被移至页 38–39。

按提取文本的近似词数，正文的语义份额为：摘要 2.2%，引言 9.1%，背景 10.2%，方法 22.0%，实验设计 4.1%，结果 27.3%，消融 10.2%，相关工作 12.1%，结论 1.7%，limitations 1.0%。这些是排除 References 后的版面近似，不把图内 token grid 当作普通论述文字。

## 2. 摘要的句级设计

| # | 主要功能 | 词数 | 证据与承接 |
|---:|---|---:|---|
| 1 | `object_scope` | 27 | 以 dLLM 与 AR 的性能、推理效率承诺界定对象。 |
| 2 | `object_scope` | 20 | 收窄到每个 diffusion step 的 unmasking procedure。 |
| 3 | `problem_gap` | 23 | 承认 confidence thresholding 相对 random unmasking 的质量与吞吐收益。 |
| 4 | `problem_gap` | 20 | 给出人工调参和大 block 退化两个缺口。 |
| 5 | `core_idea`、`method` | 13 | 将采样 procedure 的训练改为 reinforcement learning。 |
| 6 | `method` | 37 | 指定 MDP、冻结 dLLM 环境、single-layer transformer 与 confidence-to-decision 映射。 |
| 7 | `qualitative_result` | 25 | 以 semi-AR 持平、full-diffusion 超过 heuristics 收束。 |

功能顺序为「对象与机会 → 现有收益 → 缺口 → RL 方案 → 两个情境下的比较结论」。摘要报告经验结论，但未报具体数值、统计处理、理论保证或限制；最强主张放在最后一句。[PDF p. 1, Abstract]

## 3. 引言与相关工作的论证推进

### 引言

1. `context`：离散 diffusion 是 AR 之外的语言建模路径，并以 LLaDA、Dream 说明可比表现。[PDF p. 1, §1]
2. `context`：生成可并行，但开源 dLLM 的效率曾落后；Fast-dLLM 通过 confidence thresholding 改变这一状态。[PDF p. 1–2, §1]
3. `problem` / `missing_insight`：heuristics 需要调参、依赖 semi-AR；作者把「选择何种 unmasking order」表述为 correctness–efficiency 的 sequential decision problem。[PDF p. 2, §1]
4. `core_idea` / `method_preview`：把 dLLM 视为固定 environment，以独立 transformer policy 做 RL，不修改 dLLM 容量。[PDF p. 2, §1; Fig. 2]
5. `result_preview`：semi-AR 中与 Fast-dLLM 相当，full-diffusion 中超过 heuristics。[PDF p. 2, §1]
6. `contribution_list`：MDP + policy + GRPO；两种 decoding regime；model/domain transfer、设计稳定性与定性顺序分析。[PDF p. 2, §1]

贡献列表重复摘要的「match / surpass」结论，但把可检验对象改为具体章节、实验和 appendix。可证伪部分是 Pareto 曲线、transfer 与 ablation；「自动发现 scalable and robust mechanisms」留到结论，本文没有跨任务族的大范围验证。

### 相关工作

相关工作为独立 Section 5，约占主文 12%。其四个引用簇分别是：

- heuristic samplers：以 Fast-dLLM 为代表，随后按 spatial / temporal signal、confidence measure、token dependency、remasking 和 dynamic length 区分；比较维度是训练自由的 sampling rule。[PDF p. 11, §5]
- dLLM 的 RL post-training：与 d1、DiffuCoder、DCOLT、DiFFPO 和并发 unmasking policy 对比；差异落在冻结 base dLLM、standalone policy、可变数量 Bernoulli action。[PDF p. 12, §5]
- orthogonal acceleration：KV cache、speculation、decoder pretraining、diffusion forcing 与 trajectory distillation；比较维度是加速机制和是否用 RL 学采样。[PDF p. 12, §5]
- adaptive computation：连接 stochastic gating、block skipping、early exit 和 AR reasoning length；比较维度是按输入分配计算的 policy。[PDF p. 12, §5]

该节把方法细节留在 Section 3，仅在 nearest-neighbor contrast 处重述最小差异。后续 Section 4 与 Appendix C 再把 Fast-dLLM 作为实证基线，而非只在 related work 中列名。

## 4. 方法、形式化与理论位置

核心链条是：把部分 masked generation 作为 state，把每个位置是否 unmask 作为 Bernoulli action，把 dLLM sampling 作为 transition，并在 terminal correctness reward 上乘以 computation factor。policy 只读每个位置的最大 token confidence、当前 mask 与 timestep；它输出 logits，经 temperature 后得到 Bernoulli parameter。训练时使用 GRPO，组内 variation 由 action 而非 token temperature 产生；测试时的 all-zero action 用最大参数位置兜底。[PDF pp. 4–6, §§3.1–3.3]

| 组件 | 解决的前文问题 | 位置 |
|---|---|---|
| MDP state/action/transition/reward | 将 hand-crafted token order 转为可优化决策过程 | p. 4, §3.1 |
| confidence-only transformer policy | 复用 dLLM 已计算的预测分布，避免 token-level policy 的大开销 | pp. 4–5, §3.2; Fig. 2 |
| Bernoulli likelihood 与 policy temperature | 允许每步选择可变数量 token，且提供测试时速度旋钮 | p. 5, §3.2 |
| GRPO objective | 在冻结 dLLM 环境中把 terminal reward 回传到各 unmasking step | p. 5, §3.3 |
| multiplicative reward | 让 correctness 成为速度收益的前提，限制 additive reward 的 reward hacking | p. 6, Eq. (3.1); pp. 10–11, §4.4 |
| expert steering | 向 full-diffusion RL 注入一个 semi-AR expert sample，以增大 AR-like rollout 的可见性 | pp. 8–9, Appendix F p. 33 |

主文可见的编号公式为 Eq. (2.1)、(2.2)、(3.1)，分别给出 MDM ELBO、partial unmasking transition 与 multiplicative reward。另有 MDP expected return、policy logits、Bernoulli likelihood、GRPO advantage / clipped objective 等 display。Appendix E 增补 DPLS 的 PL likelihood 与 STOP construction；Appendix F 增补 expert-mixture distribution；Appendix G 列出 masked / uniform kernel。全文没有 theorem、lemma、proposition、corollary 或 proof；形式化承担机制定义与优化目标的角色，不构成理论保证。[PDF pp. 2–6, 32–34]

Algorithm 1 的输入为 prompt、`L`、`T`、`pθ`、`πϕ` 和 `τπ`，输出为生成序列与采样步数。主循环从 `t=T` 到 1：计算 dLLM token distribution、confidence、mask、logits 与 Bernoulli action；空 action 时 argmax fallback；更新 masked set 后返回 `T − T̂`。循环不变量是已经 unmasked 的位置不再参加 policy action，masked set 单调缩小。[PDF p. 18, Appendix A, Algorithm 1]

## 5. 实验设计与复现粒度

- **研究安排**：Section 4 按 effective sampling、full-diffusion、transferability、policy design 组织；这与引言三条贡献基本一一对应。[PDF pp. 6–11]
- **基础模型与任务**：主模型为 LLaDA-8B-Instruct；Dream-7B-Instruct 位于 Appendix B.4。训练数据是 GSM8K 与 MATH training set 的比例混合；主文称约 15,000 samples。测试覆盖 GSM8K、MATH-500、HumanEval、MBPP，另有 KodCode-RL-10K 的 coding-trained policy。[PDF p. 6, §4.1; pp. 9–10, §4.3; Appendix H p. 35]
- **控制与 baselines**：random、high-confidence、Fast-dLLM 组成主对照；补图加入 Kim et al. (2025a) 与 Ben-Hamu et al. (2025) 的 heuristic。核心控制是 `BL=32` 对 `BL=256`、`L=256` 对 `L=512`，以及 greedy token decoding `τ=0`。policy 使用不同 `α` 与 `τπ`。[PDF pp. 6–8; Appendix B pp. 19–24]
- **训练与选择**：五个主 policy 对应 `α ∈ {10, 3, 1, 0.3, 0}`，单 epoch。作者训练两颗 seed，按最终 training loss 选一颗，policy 结果平均三个 test-time seed；Figure 3 是两个 training seed 的 rolling average 与 min–max，`α=10` 仅一颗 seed。[PDF pp. 5–7]
- **配置与硬件**：policy 是 1-block transformer、hidden 128、FFN 512、2 heads、time embedding 128、约 300K parameters；GRPO group size 8，learning rate `3e-5`，A100 GPU 的 wall-clock replication 在 Appendix B.3。代码链接置于首页。[PDF p. 1; pp. 20, 35–36]
- **未报告项**：没有预注册 research question、data-leakage procedure、训练总 wall-clock / GPU-hours、显著性检验或多重比较方案。Table 1 没有随机 seed 值；正文只叙述 seed 使用方式。[PDF p. 35, Appendix H; p. 7, §4.1]

主指标是 accuracy 对 network function evaluations (NFEs)。wall-clock time 复核 policy overhead；非贪婪设置增加 pass@k、majority vote 与 outcome reward model 选择；定性诊断加入 average NFE per block、adjacent-unmask frequency 与 Spearman rank correlation。主 Pareto 图的 curves 未见不确定性标记；Appendix J 对 policy 的若干点给出 `±` 值，但文字没有定义该离散量类型或做假设检验。[PDF pp. 6–11; pp. 20, 24–27, 38–39]

## 6. 主结果、统计与图表

### 决策结果

1. **semi-AR**：在 `BL=32`，policy 超过 random 与 high-confidence，整体与 Fast-dLLM 对齐。低 NFE 的 `α=10` policy 在 GSM8K 的 10.3 NFE 达 35.2 ± 0.3%，Fast-dLLM 在 10.6 NFE 为 17.5%；MATH-500 对应为 15.3 ± 0.2% 对 7.4%。中高 NFE 的差距收窄，支持作者关于 heuristic frontier 接近最优的谨慎推测。[PDF pp. 6–7, Fig. 4; Appendix J p. 38, Tables 2–3]
2. **测试时控制**：固定 `α=1` 后缩放 Bernoulli probability 的 `β` 形成比训练时调 `α` 更平滑的 trade-off；MATH-500 约 25 NFE 处为 20% 对 Fast-dLLM 10%。该点是图读数，非表格精确值。[PDF p. 8, §4.1, Fig. 6]
3. **full-diffusion**：`BL=L=256` 时，LLaDA/GSM8K policy 在 13.0 NFE 达 48.3 ± 0.6%，50.5 NFE 达 56.1 ± 0.9%；同页的 high-confidence 与 Fast-dLLM 在高 NFE 仍分别退化或停留在约 34% 左右。MATH-500 的绝对准确率较低，policy 的 121.5 NFE 点为 22.9 ± 1.0%。[PDF pp. 8–9, Fig. 4; Appendix J p. 39, Tables 4–5]
4. **expert steering**：GSM8K full-diffusion 在约 70.5 NFE 达 77.2 ± 0.4%，接近 semi-AR 的高 accuracy 区；MATH-500 在 86.7 NFE 达 31.4 ± 0.5%。作者同时报告训练 instability 与 `α` controllability 下降。[PDF pp. 8–9; Appendix J p. 39]
5. **transfer**：LLaDA-trained policy 在 Dream 上大体接近 Fast-dLLM，极端 `α=10` 没保留 LLaDA 的低-NFE 优势；数学训练 policy 在 HumanEval、MBPP 上不完全转移，KodCode-trained policy 缩小 HumanEval 缺口并改善 MBPP 低-NFE 区；`L=256→512` 迁移中 learned policy 较 heuristics 更稳定。[PDF pp. 9–10, Fig. 8; Appendix B pp. 23]
6. **非贪婪 decoding**：`τ=0.8` 下，主文报 policy 相对 Fast-dLLM 的平均 pass@1 增幅为 0.98%，pass@32 增幅为 2.56%；Figure 19 还给出 GSM8K 与 MATH-500 的 pass@k、majority vote、ORM 曲线。GSM8K 使用 `Ntest=300` 子集以降低计算量。[PDF p. 10, §4.3; p. 24, Fig. 19]
7. **reward / likelihood / input 消融**：additive reward 易把所有 token 同时 unmask，multiplicative reward 限制此 reward hacking；DPLS 与 Bernoulli 接近；top-50 confidence 输入略差于 max confidence；300M hidden-state policy 更差、更不稳定；zeroing time 或 mask 多数降低 accuracy。[PDF pp. 10–11, Fig. 9; p. 24, Fig. 20]

### 全部图表与算法清单

**主文**：Figure 1（p. 3，semi-AR 与 full-diffusion 的启发式失效诊断）；Figure 2（p. 4，frozen dLLM 与 learned policy 的数据流）；Figure 3（p. 5，`α` 对 correctness 与 NFE 训练动态的影响）；Figure 4（p. 6，四个主 Pareto 比较）；Figure 5（p. 7，按 block 分配 NFE）；Figure 6（p. 8，`β` 的测试时控制）；Figure 7（p. 9，全扩散 position-wise unmask time）；Figure 8（p. 9，model / domain / length transfer）；Figure 9（p. 11，reward、likelihood、input ablation）。

**Appendix B**：Figure 10–11（p. 19，更多 models/datasets 与 baselines）；Figure 12–13（p. 20，wall-clock 与 Dream）；Figure 14–15（p. 21，`α` grid 与 training-seed spread）；Figure 16（p. 22，`τπ`）；Figure 17–18（p. 23，Dream / length transfer）；Figure 19–20（p. 24，non-greedy 与 input zeroing）。

**Appendix C–D**：Figure 21–22（p. 25，qualitative selection 与 block-wise rank correlation）；Figure 23–24（p. 26，BL32-slow order 与 adjacent-token frequency）；Figure 25–26（p. 27，BL32-fast 与 BL256 order）；Figure 27–33（pp. 28–31，七种 token generation trajectory）。

**表与算法**：Algorithm 1（p. 18）；Table 1（p. 35，training / policy configuration）；Table 2–3（p. 38，`BL=32` 的 GSM8K、MATH）；Table 4–5（p. 39，`BL=256` 的 GSM8K、MATH）。

每个主图都有 caption，Figure 4、8、9 的 caption 可以独立识别 tasks、regimes 与部分 settings。Table 2–5 提供所有 plotted LLaDA points 的精确 NFE / accuracy；这使得 Figure 4 易读，但读者需要到 Appendix J 才能查数值。[PDF pp. 6, 9, 11, 37–39]

## 7. 消融、负面信息与边界

Section 4.4 占约 1.5 个主文页，另有 Appendix B.5、B.6、B.10 三页补图。其识别对象是 reward shape、action likelihood、policy input、`α` 的可控性、`τπ` 和 expert steering。该论文没有传统「去掉单一网络层」的 component-deletion ablation；最接近的干预是 zeroing time / mask input。[PDF pp. 10–11; pp. 21–24]

负面信息有明确落点：

- `α=10` 因 reward slope 陡峭而训练不稳定；密集 `α` grid 在 `α≥4` 时会落到两个极端附近，固定 `α` 的不同 seed 也会给出不同 accuracy–speed 点。[PDF p. 7; p. 21, Figs. 14–15]
- full-diffusion policy 仍低于 semi-AR policy 的中高 NFE 表现；expert steering 可缩小差距，同时带来 instability 和更差 controllability。[PDF p. 8]
- math-trained policy 不能完整转到 coding，尤其 HumanEval；扩大训练 mixture 被提出为改善方向。[PDF p. 10]
- BL32-slow policy 有时在 EOS 后没有并行完成 padding token，造成额外计算。[PDF p. 26, Fig. 23]
- 文末把每个 `α` 需单独训练、成本高、控制粒度不足列为 core limitation；测试时 intervention 仍需更多验证。[PDF pp. 12–13]

可验证的呈现方式包括：精确数值迁移到 Appendix J，Figure 4 主图没有可见不确定性标记，Appendix J 对部分 policy 点给出未定义类型的 `±` 值；Appendix D 以一个随机 GSM8K sample 作 trajectory visualization。上述均为版面或文字事实，不能单独推出作者的选择动机。[PDF pp. 28–31, 37–39]

## 8. 结论闭环与最终判断

| 引言主张 | 方法回应 | 证据回应 | 状态 |
|---|---|---|---|
| dLLM sampling 可被形式化为 MDP，并学得 standalone policy | state/action/transition/reward、confidence transformer、GRPO | Eq. (2.2)、Fig. 2、Algorithm 1 | `closed` |
| 学得 policy 在 semi-AR 中可匹配强 heuristic | `BL=32` training，reward 控制 speed | Fig. 4a/4c、Tables 2–3 | `partially_closed`：覆盖两个 math datasets 与有限模型 |
| RL 可解决 full-diffusion 中 heuristic 的困难 | `BL=256` policy 与 expert steering | Fig. 4b/4d、Tables 4–5 | `partially_closed`：强于所列 baselines，离 semi-AR upper range 仍有距离 |
| policy 可跨 model、domain、length 迁移 | confidence-only input、transformer length generalization | Fig. 8、17、18 | `partially_closed`：model / length 结果较好，coding domain 暴露失败 |
| training / design insights 能解释性能 | reward、DPLS、input、trajectory ablations | Fig. 5、9、20、22–26 | `partially_closed`：相关图与干预支持，未建立跨模型机制定律 |
| learned sampler 展示不同 unmasking behavior | order and trajectory analysis | Fig. 5、7、22–33 | `partially_closed`：`N=100` GSM8K samples 的描述性证据 |

**单一主线**：confidence heuristic 实际在近似求解 adaptive sequential decision problem；将 dLLM 固定为环境、把 unmask action 交给轻量 RL policy，能在保持 dLLM 能力的条件下自动找到 accuracy–efficiency trade-off，特别是在 heuristics 脆弱的 full-diffusion setting。[PDF pp. 2, 4–6, 8]

**正文保留的决策关键内容**：问题诊断、MDP、policy / reward、主 Pareto 图、transfer、reward/input ablation 和结论限制都留在主文。精确曲线数据、更多 baselines、time / `α` / `τπ` sensitivity、qualitative token grids 和 complete configuration 被分散到 Appendix B–J；主文仍能判断主结论，复现和精确比较需打开附录。[PDF pp. 6–11, 17–39]

**最有效的叙事模式**：先以 Figure 1 把 heuristic failure 放在 full-diffusion 的可观察现象上，再用 MDP 与 Figure 2 给出最小机制，随后以相同 axes 的 Figure 4 提供 regime-by-regime 反证空间；最后用 Figure 9 和 Appendix C 解释为什么 speed/reward/input 会改变结果。该结构把「提出 RL」与「为何需要 RL」连在同一证据链中。

**最大缺口与读者成本**：最广泛的 scalable / robust 结论超出两类 7–8B dLLM、几组 reasoning / coding benchmarks 和一次 seed-selection protocol 的直接覆盖；policy 的 domain transfer 失效和 expert-steering instability 同时限制泛化表述。主图有利于阅读，但 exact values、`±` 语义、训练成本和配置细节后移，使复核需要跨页访问 Appendix H 与 J。[PDF pp. 7–10, 12–13, 35, 37–39]

**可迁移规则**：当研究主张是「按输入分配计算」，先把真正的 sequential decision unit 写成 state/action/reward，再将机制与现有 heuristic 的同轴 Pareto comparison、失败 regime、和最少一组替代解释 ablation 绑定。该规则适合能冻结生成器并在 action 后观测任务 reward 的系统；如果 policy 必须改变 base model、需要丰富语义状态、或 reward 不能在 rollout 后可靠计算，confidence-only 独立 policy 与本文的证据链都需要重做。

## 9. Appendix 的职责

| 一级模块 | 页 | 类别 | 主文调用与责任 |
|---|---:|---|---|
| A Policy Sampling Algorithm | 18 | `extended_method` | §3.2 直接调用；给出 full-diffusion pseudocode 与 fallback。 |
| B Additional Results | 19–24 | `additional_result` | §2.2、§4.1–4.4 多次调用；补 model/dataset/baseline、wall-clock、`α`、`τπ`、transfer、non-greedy 与 input ablation。 |
| C What are RL unmasking policies actually doing? | 25–27 | `qualitative_example` | §4.1、§4.2 与引言调用；以 order / correlation 解释不同 sampler。 |
| D Generation Trajectories Visualizations | 28–31 | `qualitative_example` | 为 C 的 token-level reading 提供一个随机样本的七种网格。 |
| E Dynamic Plackett-Luce Sampling | 32 | `extended_method` | §3.2、§4.4 调用；给出 Bernoulli 的替代 action distribution。 |
| F Expert Steering | 33 | `extended_method` | §4.2 调用；说明 expert mixture 与 likelihood ratio。 |
| G Extended Background | 34 | `other` | §2.1 调用；比较 masked、uniform 与 continuous-input diffusion。 |
| H Training and Policy Network Configuration | 35 | `hyperparameter` | §4.1 调用；集中写参数、GRPO、data mixture。 |
| I Policy Architecture Diagram | 36 | `implementation_detail` | §4.1 调用；图示 c/m/t 到 logits 的 block。 |
| J Tabular Reference for Main LLaDA Experiments | 37–39 | `additional_result` | Figure 4 的精确点表，便于 future comparison。 |

附录不含 theorem proof、独立 ethics / broader-impact section、独立 supplementary，也没有完整训练成本或 seed 列表。Appendix 的长度约为正文承载页的 1.8 倍；它强化复现性和诊断，但精确的主结果依赖 J 才可完整核查。

## 10. 用词与修辞

主文中最常出现且承担论证动作的领域词包括 `policy`、`sampling`、`unmasking`、`confidence`、`Fast-dLLM`、`reward`、`NFE`、`semi-AR` 与 `full-diffusion`。常见二元 / 三元词组是 `learned policy`、`confidence-based heuristic`、`full-diffusion setting`、`accuracy-efficiency trade-off`、`test-time Pareto frontier`。这些词由机制、对照和结果重复驱动，未只停留在模板性贡献句。

提取文本的主文计数为：`we find` 7 次，`we observe` 6 次，`we show` 2 次，`we demonstrate` 1 次，`we introduce` 2 次，`we study` 2 次。强断言通常与 Figure / Table 相邻，例如「outperform」「match」「achieve」；弱断言使用 `may suggest`、`one hypothesis`、`likely`、`appears`，主要出现在 full-diffusion optimum、qualitative order 与 mechanism interpretation。[PDF pp. 7–10, 25–27]

# Video-Based Optimal Transport for Feedback-Efficient Offline Preference-Based Reinforcement Learning：单篇深读备忘

- **paper_id**：`icml-2026-c65beb96fda3`
- **版本边界**：唯一读取版本为 `corpus/preprints/icml-2026-c65beb96fda3.pdf`，PDF 物理页 1–23；`source_kind=verified_preprint`，`source_url=https://arxiv.org/pdf/2606.16856`。
- **身份**：ICML 2026 oral；OpenReview forum 为 <https://openreview.net/forum?id=G8LVO5easu>。
- **作者/机构**：Tung M. Luu、Hwanhee Kim、Younghwan Lee、Chang D. Yoo；Korea Advanced Institute of Science and Technology (KAIST)。
- **代码**：论文摘要给出 <https://github.com/tunglm2203/votp>。

## 1. 文档边界与页级地图

PDF 为双栏排版。正文的主要连续页为 1–8；第 9 页左栏继续 `6. Discussion`、`Limitations`、`Acknowledgements` 和 `Impact Statement`，右栏从 `References` 开始。因此，下面的 `main_pages=8` 按完整正文页计，`reference_pages=5` 按物理页 9–13 计；第 9 页是正文与参考文献的混排页。Appendix 从物理页 14 开始至 23 结束，共 10 页。图表浮动使 C 节的若干对象实际落在物理页 22–23。

| 物理页 | 内容与语义模块 | 版面观察 |
|---|---|---|
| 1–2 | Abstract、`1. Introduction` | 摘要位于首页上方；引言首段跨栏延续。 |
| 2 | `2. Related Work` | 三个主题段落：PbRL、VLM/ViFM reward、OT in RL。 |
| 2–3 | `3. Preliminaries` | RL、Preference-based RL、Discrete OT；公式跨页。 |
| 3–5 | `4. Method` | Fig. 1 在 p.4；Eq. (3)–(7) 集中在 p.3–4；实现细节延续至 p.5。 |
| 5–8 | `5. Experiments` | Table 1、Fig. 2–7；实验、结果和消融交错于双栏。 |
| 8–9 | `6. Discussion` | Discussion 在 p.8 右栏开始，p.9 左栏收束。 |
| 9 | `Limitations`、`Acknowledgements`、`Impact Statement` | 均位于 References 之前的左栏。 |
| 9–13 | `References` | 参考文献从 p.9 右栏开始。 |
| 14–16 | `Appendix`、Algorithm 1、`A. Details on Experiments` | 任务、数据、实现、超参数、真实机器人设置和基线源码。 |
| 15–18 | `B. Learning Curves` | Fig. 10–16；包括训练曲线、IQM/Median/Mean/Optimality Gap 和轨迹可视化。 |
| 19–23 | `C. Additional Results and Analysis` | C.1–C.8；C.6/C.7 的图浮动到 p.22–23。 |
| 21 | `D. Extended Discussion on Broader Context and Future Directions` | 讨论生成式 policy、VLA、表征质量和跨领域可能性。 |

估计正文（排除 References、保留正文图表标题的近似英文 token）为约 6,734 词；Appendix 约 4,560 词。正文模块相对篇幅以这 6,734 词为分母，四舍五入到四位小数。Appendix 的 `main_word_share` 记为 0.0000，因为它不属于正文分母。

## 2. 12 个语义模块与计数

下表是固定 12 个模块的唯一一次映射；`figures/tables/algorithms/displayed_equations` 为人工核对后的 PDF 计数。

| 模块 | 状态 | 估计词数 | 正文占比 | 图 | 表 | 算法 | display 公式 |
|---|---|---:|---:|---:|---:|---:|---:|
| `abstract` | observed | 150 | 0.0223 | 0 | 0 | 0 | 0 |
| `introduction` | observed | 700 | 0.1040 | 0 | 0 | 0 | 0 |
| `related_work` | observed | 482 | 0.0716 | 0 | 0 | 0 | 0 |
| `method` | observed | 1,212 | 0.1800 | 1 | 0 | 0 | 5 |
| `theory` | not_present | 0 | 0.0000 | 0 | 0 | 0 | 0 |
| `experimental_design` | observed | 430 | 0.0639 | 0 | 0 | 0 | 0 |
| `results` | observed | 1,600 | 0.2376 | 3 | 3 | 0 | 0 |
| `ablation` | observed | 1,200 | 0.1782 | 3 | 0 | 0 | 0 |
| `conclusion` | observed | 84 | 0.0125 | 0 | 0 | 0 | 0 |
| `limitations` | observed | 116 | 0.0172 | 0 | 0 | 0 | 0 |
| `appendix` | observed | 4,560 | 0.0000 | 12 | 10 | 1 | 0 |
| `other` | observed | 760 | 0.1129 | 0 | 0 | 0 | 4 |

正文有 19 个 figure、13 个 table 和 1 个唯一算法；正文有 9 个 display 公式，其中 7 个带编号，Appendix 没有新增 display 公式。`other` 的 4 个公式来自 Preliminaries：return、Bradley–Terry probability、Eq. (1) 和 Eq. (2)。`theory` 没有 theorem/lemma/proposition/corollary/proof；方法中的 Eq. (6) 只给出归一化范围保证，不能替代学习性能理论。

## 3. 摘要逐句功能编码

摘要共 7 句，报告了定性实验结论和代码链接，但没有 theorem、复杂度或明确数值结果，也没有显式 limitation 句。最强主张位于第 5–6 句：在有限反馈下优于 offline PbRL，并在视觉干扰与真实机器人任务中有效（p.1, `Abstract`）。

| # | 句子 | 词数 | 功能 | 限定词/数字/比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | Conveying complex objectives to reinforcement learning (RL) agents often requires meticulous reward engineering. | 13 | `object_scope` | `often`；无数字。 | p.1, `Abstract`，“often requires meticulous reward engineering” |
| 2 | Preference-based RL (PbRL) offers a promising alternative by learning reward functions from human feedback, but its scalability is hindered by high labeling costs. | 23 | `object_scope`, `problem_gap` | `promising`、`but`；比较手工 reward 与 human feedback。 | p.1, `Abstract`，“scalability is hindered by high labeling costs” |
| 3 | Inspired by advances in Video Foundation Models (ViFMs), we present Video-based Optimal Transport Preference (VOTP), a semi-supervised framework that learns effective reward functions from only a handful of labels. | 29 | `core_idea`, `method` | `only a handful`；提出 VOTP。 | p.1, `Abstract`，“we present Video-based Optimal Transport Preference” |
| 4 | By leveraging optimal transport to align visual trajectories within the rich representation space of ViFMs, VOTP effectively generates high-fidelity pseudo-labels for large amounts of unlabeled data, substantially reducing human supervision. | 30 | `core_idea`, `method`, `impact_claim` | `effectively`、`high-fidelity`、`substantially`；labeled 对 unlabeled。 | p.1, `Abstract`，“align visual trajectories ... generate high-fidelity pseudo-labels” |
| 5 | Extensive experiments across locomotion and manipulation benchmarks demonstrate the superiority of VOTP, which outperforms state-of-the-art offline PbRL methods under limited feedback budgets. | 22 | `experimental_setup`, `qualitative_result` | `Extensive`、`superiority`、`state-of-the-art`、`limited`；对比 offline PbRL。 | p.1, `Abstract`，“outperforms state-of-the-art offline PbRL methods” |
| 6 | We also showcase the robustness of VOTP in the presence of visual distractors and validate its utility on real robotic tasks, where it learns meaningful rewards with minimal human input. | 30 | `experimental_setup`, `qualitative_result`, `impact_claim` | `robustness`、`minimal human input`；视觉干扰、真实机器人。 | p.1, `Abstract`，“robustness ... visual distractors ... real robotic tasks” |
| 7 | The code is available at: https://github.com/tunglm2203/votp. | 11 | `impact_claim` | 代码可用性；URL。 | p.1, `Abstract`，“The code is available at” |

摘要功能顺序为：reward engineering 背景 → PbRL 成本缺口 → VOTP 核心想法 → OT/ViFM 机制 → benchmark 结果 → robustness/real robot 扩展 → code。它将实证优势放在末两句，把机制放在结果前，未用理论保证或局限稀释主张。

## 4. 引言的论证推进

引言由 4 个段落动作组成，完整链条为：

`context/problem → problem + pipeline → failure_of_prior_work → missing_insight → core_idea/method_preview/result_preview`

| 段落动作 | 估计词数 | 上一段留下的问题 | 当前段回答与下一段钩子 | 证据 |
|---|---:|---|---|---|
| `context` + `problem` | 140 | 决策任务需要 reward。 | 手工 dense reward 依赖 motion capture、proprioception、tactile sensing，仍会 reward misspecification；为 PbRL 留出问题空间。 | p.1, `1. Introduction`，“reward design remains challenging” 与 “reward misspecification” |
| `problem` + `method_preview` | 175 | 手工 reward 可能被 exploit。 | Human data、expert demonstrations、natural language 和 PbRL 可替代手工设计；PbRL 以 preference reward learning → policy optimization 两阶段闭环。 | p.1, `1. Introduction`，“The PbRL framework often consists of two stages” |
| `failure_of_prior_work` + `missing_insight` | 205 | PbRL 有效但需要覆盖 state/action。 | 现有方法常需数千 queries；半监督、meta-learning、active learning、ranking 已减负，但忽略“人类偏好由行为的视觉感知塑造”；ViFM 表征空间成为新切入点。 | p.1–2, `1. Introduction`，“human preferences are shaped by the visual perception of agent behaviors” |
| `core_idea` + `method_preview` + `result_preview` | 174 | 需要把少量视觉偏好扩展到未标注行为。 | VOTP 在 ViFM latent space 中用 OT 将 labeled/unlabeled segment 对齐，以相对 alignment 聚合偏好；随后预告 D4RL、MetaWorld 与真实桌面任务的结果、分析和消融。 | p.2, `1. Introduction`，“uses optimal transport ... automatically assign preference labels” |

贡献列表采用叙事段落而非单独 bullet list，因此没有把摘要逐字复制成四个贡献点；它给出“10 feedbacks”示例、D4RL/MetaWorld/real-world 范围和 pseudo-label 机制，具有可证伪的组件与低反馈主张。

## 5. 相关工作

相关工作仅有独立第 2 节，位于 p.2，分为三个加粗主题；每段都在最后转向 VOTP，避免在方法节重新讲完整背景。引用簇按比较维度计为：PbRL 约 6 个簇、VLM/ViFM reward 约 3 个簇、OT in RL 约 5 个簇。

| 段落 | 动作 | 比较维度与 VOTP 定位 | 证据 |
|---|---|---|---|
| `Preference-based RL (PbRL)` | `taxonomy` → `gap_creation` → `nearest_neighbor_contrast` | 按 query selection、pretraining、uncertainty、ranking、sub-optimal data 分类；指出 SURF 依赖 learned reward model，VOTP 使用 offline 数据中的 unlabeled segment pairs，并将 OT 放入 ViFM latent space。 | p.2, `2. Related Work / Preference-based RL`，“we utilize unlabeled segment pairs from offline datasets” |
| `Vision Foundation Models in Reward Learning` | `taxonomy` → `limitation_of_prior` → `nearest_neighbor_contrast` | 区分 VLM trajectory–task alignment 的 noisy/inconsistent reward 与依赖 prompt 的 VLM feedback；VOTP 让 ViFM 生成 pseudo-preference labels，而非直接 reward 或 prompt feedback。 | p.2, `2. Related Work / Vision Foundation Models in Reward Learning`，“we instead leverage ViFMs to generate pseudo-preference labels” |
| `Optimal Transport in Reinforcement Learning` | `chronology` → `limitation_of_prior` → `nearest_neighbor_contrast` | 从 domain adaptation、graph matching、semi-supervised learning 到 imitation learning；PEARL 受同 state/action space 与 cross-domain uncertainty 限制，VOTP 在同一 domain 的高维视觉输入中传播偏好。 | p.2, `2. Related Work / Optimal Transport in Reinforcement Learning`，“performs pseudo-labeling directly within the same domain” |

后续正文中的引用主要承担方法组件与 baseline 定位（S3D、POT、IQL、SURF、FTB 等），没有把相关工作再写一遍。论文没有独立“理论相关工作”小节。

## 6. 方法与理论

### 6.1 方法因果链

方法解决的是“少量 human preference 无法覆盖 state/action space”这一前文问题。组件与问题一一对应：

1. **Trajectory representation**：将 segment 视为短视频，用 ViFM 同时保留 frame-level spatial detail 与 segment-level temporal dynamics，降低视觉 nuisance 对比较的影响。
2. **OT pseudo-labeling**：在 labeled 与 sampled unlabeled segments 之间求 coupling，以 alignment strengths 传播已知偏好，避免只用单个最近邻或 group mean。
3. **Threshold filtering**：对归一化分数施加 `τP`，只保留高置信 pseudo-label，控制错误标签的质量—数量折衷。
4. **Reward-to-policy bridge**：用 labeled+pseudo-labeled pairs 训练 Bradley–Terry reward，再重标 offline dataset 的所有 state-action rewards，最后用 IQL 训练 policy。

方法段落动作序列为：

`state_problem → define_component → setup_notation → explain_mechanism → derive → give_intuition → connect_to_prediction → instantiate_algorithm → state_complexity → connect_to_experiment`

### 6.2 最小逻辑单元与公式

- p.3 `§4` 先声明反馈效率目标和两个关键组件，并调用 Fig. 1。
- p.3 `§4.1` 定义 `σ={o1,…,oH}`、`z=fϕ(o1:H)`；解释 ViFM 的 spatial/temporal 表征、Human activity 预训练、actor-agnostic/semantic embedding 与 unseen robotic environments 的泛化预期。
- p.3–4 `§4.2` 定义 `Dl`、`Du`、总 labeled segments `N=2Nl`、preference matrix `R∈{−1,0,1}N×N` 和 skew-symmetry；再构造 uniform empirical measures `μL`、`μU`。
- p.4 `Eq. (4)` 用 latent distance 作为 cost 求 OT coupling；`d` 可用 Euclidean 或 cosine distance。
- p.4 `Eq. (5)` 对所有有偏好的 labeled segment pairs 聚合正向/反向 alignment difference，形成 unlabeled pair 的 preference score。
- p.4 `Interpretation` 解释：正差值表示保留 labeled preference，负差值表示翻转；`R` 的 skew-symmetry 保证交换 pair 顺序时推断一致。
- p.4 `Eq. (6)` 定义 `Smax` 并把分数归一化到 `[−1,1]`；`Eq. (7)` 用 `τP` 将分数转成 hard preference 或 tie。
- p.4–5 `§4.3` 说明 exact OT 是 linear program，实践改用 entropy-regularized Sinkhorn（POT toolbox）；仅保留超过阈值的 pseudo-label，然后 relabel rewards 并训练 policy。

### 6.3 理论清单与边界

Preliminaries 给出 MDP、Bradley–Terry、discrete OT 的形式定义；Method 给出 VOTP 的可执行构造。论文没有 theorem、lemma、proposition、corollary、proof，没有 sample-complexity、consistency、pseudo-label error 或 policy performance bound。Eq. (6) 的 `[−1,1]` 是由 uniform masses 与 `Smax` 归一化得到的范围保证，属于构造性保证，不能支撑“在有限 feedback 下必然有效”的理论因果结论（p.4, `§4.2`）。

### 6.4 算法与复杂度

唯一伪代码是 Appendix 的 Algorithm 1（p.14）：输入 offline dataset `B`、labeled dataset `Dl`、unlabeled segment 数 `M`、阈值 `τP`；循环采样 `M/2` 个 segment pairs、用 Eq. (5) 计算 score、用 Eq. (7) 生成 pseudo-label 并追加到 `Du`；合并 `Dl∪Du` 训练 reward，重标 `B`，用 offline RL 训练 policy。循环不变量是 `Du` 只累积通过阈值的 pseudo-labeled pairs。正文只解释到 pipeline 粒度，没有给出 Big-O；它用“standard solver expensive / Sinkhorn efficient and numerically stable”说明计算取舍（p.4–5）。

## 7. 实验设计

论文在 p.5 开头显式列出五个问题：低数据反馈效率、组件贡献、超参数影响、视觉干扰下的泛化、真实机器人可用性。它们是研究问题列表，未被写成带方向的 formal hypotheses。

| 设计事实 | 具体设置 | 证据 |
|---|---|---|
| benchmark/task | D4RL locomotion：Hopper、Walker2d；MetaWorld manipulation：Door Open、Drawer Open、Plate Slide、Sweep Into。 | p.5, `§5.1 Setups`，“D4RL provides locomotion tasks and MetaWorld involves manipulation tasks” 和 Appendix p.14 `A.1` |
| dataset | D4RL 使用 Kim et al. (2023) offline PbRL 数据；MetaWorld 使用 Hejna et al. (2024)；Appendix 指明 D4RL 为 medium-expert-v2 与 medium-replay-v2，MetaWorld 为 pre-collected dataset。 | p.5 `§5.1`；p.14 `A.2 Dataset Details` |
| labeled/unlabeled budget | 主实验 10 labeled segment pairs；均匀随机采样 10k D4RL、50k MetaWorld unlabeled pairs；视觉观察从 state 渲染。 | p.5 `§5.1`；p.15 `Table 6` |
| label source | 默认 scripted teacher 基于 ground-truth reward；`hopper-medium-replay-v2` 改用 Kim et al. 的 human labels，因为 scripted labels 在该任务对 baseline 无效。 | p.5 footnote 2；p.14 `A.2` |
| representation/cost/solver | S3D ViFM，预训练于 HowTo100M；主实验 Euclidean cost；POT 的 Sinkhorn solver。 | p.5 `Training and Evaluation`；p.15 `Table 6` |
| reward/policy | 用 Eq. (1) 的 reward model 学习；重标 offline dataset 的所有 state-action pairs；policy 使用 IQL。 | p.4–5 `§4.3`、`§5.1` |
| control across baselines | PbRL baseline 的 policy/reward model 从 states 训练，共用 policy-learning hyperparameters；差异放在 reward-learning process。 | p.5 `Training and Evaluation`，“the only difference lies in the reward learning process” |
| baselines | 无显式 reward：IPL、CPL、DPPO；显式 reward：P-IQL、SURF、LiRE、APPO、FTB；另有使用 unlabeled GT preferences 的 Oracle。 | p.5 `§5.2 Baselines` |
| metrics/repeats | D4RL 用 normalized score，MetaWorld 用 success rate；5 runs，主评估每个 evaluation step 25 episodes；报告 mean±standard deviation。 | p.5 `Training and Evaluation` |
| robustness design | 固定 labeled segments，在 unlabeled 数据中改变 light position/direction、ambient/diffuse、texture、video background easy/hard。 | p.8 `§5.4`；Appendix p.23 `Fig. 19` |
| real robot design | 7-DoF Rethink Sawyer；Lift Banana、Drawer Open；main text 写每任务 50 demonstrations、50% success，5/10 preference labels、2,000/3,000 unlabeled pairs；IQL policy。Appendix A.4 给出更细的视觉/状态输入、10 Hz、RealSense D435i、10-episode evaluation。 | p.8 `§5.5`；p.15 `A.4` |
| implementation/reproduction | IQL/reward/VOTP 超参数在 Tables 4–7；baseline source URLs 与 tuning ranges 在 Table 8；FTB 使用 default，因为每 run 约 2 天。 | p.15–16 `A.3–A.5` |
| human-teacher extension | D4RL 使用 Kim et al. human labels；MetaWorld 由 4 位非机器人参与者收集 preference，比较 scripted vs human teacher。 | p.20 `C.4` |

未提供或未单独声明：各随机 seed 的具体数值、跨任务 train/test split、正式 failure 判定阈值、显著性检验、多重比较方案、数据泄漏审计。超参数与硬件细节依赖 Appendix。D4RL IQL 1e6 steps、MetaWorld 4e5，reward model 2e4；真实机器人 IQL 1e5、reward 2000（p.15–16）。

## 8. 结果、统计与可视化

统计处理以 5 runs 的 mean±standard deviation 为主；正文没有 hypothesis test 或 p-value，也没有主文 confidence interval。Table 1 的粗体规则是排除 IQL+GT 与 Oracle 后，落在最佳值 5% 内。Appendix Fig. 12–13 另给 stratified percentile bootstrap 的 95% CI、Median、IQM、Mean 和 Optimality Gap；这些是附录分析，不改变正文的主要决策量。

### 8.1 主结果

- **Table 1，D4RL**：VOTP 的 locomotion average 为 **92.8**，P-IQL 为 65.3，FTB 为 85.4，Oracle 为 92.4，IQL+GT 为 93.6。逐任务 VOTP 为 hopper-medium-replay 91.1±4.7、hopper-medium-expert 105.7±6.0、walker2d-medium-replay 66.3±5.6、walker2d-medium-expert 108.1±2.2；因此作者称其在 D4RL 接近 Oracle。这个比较是最终 checkpoint、5 seeds 的 mean±SD（p.6, `Table 1`）。
- **Table 1，MetaWorld**：VOTP average **67.6**，高于 P-IQL 31.0、SURF 51.0、FTB 48.6 和 LiRE 64.0，但低于 IQL+GT 71.0 与 Oracle 80.1。Door-open 84.0±8.4、drawer-open 71.2±11.7、plate-slide 57.6±5.4、sweep-into 57.6±7.4。故“全面匹配 Oracle”只适用于作者对 D4RL 的表述，不能扩展到 MetaWorld（p.6, `Table 1`）。
- **Baseline 解释**：无显式 reward 的 IPL/CPL/DPPO 通常远离 GT；显式 reward 更稳。SURF 在 MetaWorld 和 walker2d 改善 P-IQL，却在 hopper 退化；作者把它归因于 reward-model pseudo-label 错误造成 confirmation bias。APPO 对 MetaWorld 有益但对 D4RL 不利；FTB 通常优于 P-IQL，但每 run 约 2 天，而 VOTP 少于 2 小时。LiRE 稳定优于 P-IQL，但在 hopper-medium-replay 与 plate-slide 仍落后 GT/Oracle（p.5–6, `§5.2`）。

### 8.2 机制与反馈效率结果

- **Fig. 2，OT 机制**：在 hopper、walker2d、door-open、drawer-open 上，VOTP 的训练曲线整体高于 SIM-individual、SIM-mean、SIM-weighted。SIM-mean 的 group feature averaging 丢掉 pair-level fine-grained distinction；SIM-weighted 虽改善部分任务但更低且不稳定。曲线为 5 runs mean，阴影为 standard deviation，没有逐点显著性检验（p.6, `Fig. 2` 与 `§5.3 Effect of Optimal Transport`）。
- **Fig. 3，表征**：S3D、VideoCLIP、InternVideo 等 ViFM 通常优于 R3M、CLIP 等 IFM，尤其在 walker2d 与 door-open。作者据此强调 temporal dynamics/subtle motion cues；选 S3D 因 31M 参数少于 VideoCLIP 208M、InternVideo 478M，且跨任务稳定（p.6, `Fig. 3`）。
- **Fig. 4，query count**：横轴为 5–1000/1K labels。无 pseudo-label 时，P-IQL 在 D4RL 约需 50–100 labels、MetaWorld 约需 1k 才接近 task-reward performance；除 walker-medium-replay 外，VOTP 需要更少 labels 达到该水平；door-open 中 10 labels 的 VOTP 超过 IQL+GT。图中没有表格化精确值，作者以曲线与这些近似阈值作结论（p.7, `Fig. 4`）。
- **Fig. 5，threshold**：D4RL 测 `τP∈{0.05,0.1,0.15,0.2}`，MetaWorld 约 `0.1–0.5`。阈值增加通常提升 performance，过大则因 pseudo-label 数量下降而回落；hopper-medium-replay 的大阈值展示了 quality–quantity trade-off（p.7, `Fig. 5`）。
- **Fig. 6，reward alignment**：door-open 的 Pearson correlation 为 P-IQL `r=0.57`、VOTP `r=0.93`；散点以 learned reward 对 GT reward，作者将其解释为 pseudo-label 扩大 state/action coverage 并带来更好 policy（p.7, `Fig. 6`）。相关性支持 reward alignment，不能单独识别 coverage→policy 的因果路径。

### 8.3 Robustness 与真实机器人

- **Table 2，visual nuisance**：door-open/drawer-open 的 same-domain 平均为 77.6；light position+direction 81.6、ambient+diffuse 78.4、texture 74.4、video easy 73.6、video hard 74.6。VOTP 在各设置保持性能，light position+direction 略升；结果来自 5 seeds 的 mean±SD（p.8, `Table 2`）。
- **Table 3，real robot**：Lift Banana 的 BC/P-IQL/VOTP success rate 为 `20.0/50.0/80.0`；Drawer Open 为 `40.0/50.0/70.0`。分母是每任务 10 episodes，未给标准差或区间（p.8, `Table 3`）。
- **Fig. 7，real-robot mechanism example**：成功轨迹上两种 reward 都合理；失败轨迹的 timestep 11–20，P-IQL 错把失败行为赋高 reward，VOTP 将成功与失败 reward 分开。它是单个 Lift Banana 的定性案例（p.8, `Fig. 7`）。

### 8.4 Appendix 结果

- **Table 9**：Euclidean 与 cosine cost 的平均 VOTP 分别为 71.3 与 70.7，任务级方向不完全一致，支持 cost choice robustness（p.19, `C.1`）。
- **Table 10**：IQL 在 GT reward 下高于 Zero、Random、Negative reward；例如 hopper-medium-replay 为 87.5±7.4 vs 28.0±8.3、48.2±6.7、0.6±0.0。该 sanity check 说明 reward 选择会改变 offline RL，不能把 VOTP 改善归因于任意 reward（p.19, `C.2`）。
- **Table 11**：对 10k unlabeled pairs，10/25/50/100/200/500 labels 的 sequential pseudo-label time 为 0.15/0.2/0.75/3/12/60 分钟；parallel（100 pairs concurrently）在 100/200/500 labels 为 1/1.7/6.6 分钟。Feature extraction 50k segments 约 20 分钟；policy training 每 run 约 1.5 小时（RTX 4090、24 CPU cores，p.19 `C.3`）。
- **Table 12**：scripted teacher 平均 78.6，human teacher 平均 75.5；walker2d 的 human teacher 下降明显（medium-replay 59.4、medium-expert 90.8），其余环境相对稳定。表中实际列出 7 个任务（p.20, `C.4`）。
- **Table 13**：相对于 scripted GT preference、排除 ties，pseudo-label accuracy 为 hopper-medium-expert 90.3%、walker2d-medium-replay 98.8%、walker2d-medium-expert 93.6%、door-open 93.1%、drawer-open 97.4%、plate-slide 95.2%、sweep-into 67.0%。这把“高质量 pseudo-label”从泛化主张落到 task-level accuracy，但 sweep-into 是明显低点（p.20, `C.5`）。
- **Fig. 17**：8 个任务的 P-IQL→VOTP Pearson `r` 依次为 hopper-m-r .04→.59、hopper-m-e .84→.94、walker2d-m-r .65→.70、walker2d-m-e .42→.88、door .57→.93、drawer .59→.91、plate .58→.71、sweep .45→.56。图中结果支持 reward alignment 普遍改善，但仍是 correlation（p.22, `Fig. 17`；正文 C.6 在 p.20 调用）。
- **Fig. 18**：drawer-open 的 4 labeled pairs、preference matrix、cost matrix、transport plan 与四个 unlabeled pair 的 scores `−0.5284`、`−0.5107`、`0.5827`、`0.4864`；原 64 frames 均匀下采样为 4 frames，矩阵项四舍五入到两位（p.23, `Fig. 18`）。

## 9. 消融、负面结果与自我设限

主文 `§5.3` 约占正文 1,200 词，包含 Fig. 2–6 中的 OT、encoder、label budget、threshold 与 reward-correlation 对照；Appendix 再补 cost metric、human teacher、pseudo-label accuracy、完整 reward scatter 和 compute cost。

| 消融/诊断 | 识别目标 | 结果与边界 | 证据 |
|---|---|---|---|
| OT vs SIM-individual/SIM-mean/SIM-weighted | 组件删除/替代 | OT 曲线整体更高；SIM-mean 丢 pair-level distinctions，SIM-weighted 较低且不稳。 | p.6, `Fig. 2` |
| IFM vs ViFM encoder | 组件/表征替代 | ViFM 尤其在 walker2d、door-open 更好；S3D 以 31M 参数作为效率选择。 | p.6, `Fig. 3` |
| labeled query count | feedback-budget sensitivity | VOTP 大多用更少 labels 达到 task-reward performance；walker-medium-replay 是例外。 | p.7, `Fig. 4` |
| threshold `τP` | hyperparameter sensitivity | 高阈值提高质量但减数量；过大造成性能回落。 | p.7, `Fig. 5` |
| Euclidean vs cosine cost | method robustness | 平均 71.3 vs 70.7，任务级差异保留。 | p.19, `Table 9` |
| scripted vs human teacher | data/label-source heterogeneity | 平均 78.6 vs 75.5；walker2d 是负面环境。 | p.20, `Table 12` |
| pseudo-label accuracy | mechanism diagnostic | 大多数任务 >90%，sweep-into 67.0%，揭示异质性。 | p.20, `Table 13` |

自我设限按位置与类型记录：

| 限制 | 类型 | 论文如何表达 | 证据 |
|---|---|---|---|
| ViFM 固有 bias 可能进入 learned reward 与 policy | `data`, `ethics`, `deployment` | 明确建议 safety-critical deployment 前评估 policy。 | p.9, `Limitations`，“biases ... may be reflected in the learned reward function” |
| OT cost 随 preference labels 增加而上升 | `compute` | 承认大数据集更贵，提出 approximate/hierarchical transport。 | p.9, `Limitations` |
| 实验 policy 仅为 standard Gaussian policies | `generality` | Appendix D 将 generative/flow/VLA policy 留作 future direction。 | p.21, `D. Extended Discussion` |
| representation quality 影响细粒度 manipulation 的 propagation | `generality` | 提出 self-supervised pretraining 与 3D scene understanding 作为后续改进。 | p.21, `D. Extended Discussion` |
| 多数 benchmark labels 为 scripted teacher，真实 human labels 只在例外/附录 | `data`, `causality` | C.4 补充 human teacher，但参与者仅 4 位且 walker2d 下滑。 | p.5 footnote 2；p.20 `C.4` |
| robustness 只覆盖两类 MetaWorld task 与预设 visual distractors | `scope`, `deployment` | Table 2 给出有限 nuisance family，没有跨相机/跨 embodiment 验证。 | p.8, `§5.4`；p.23 `Fig. 19` |
| real robot 只覆盖两个任务、每任务 10 episodes | `scope`, `metric` | Table 3 用小分母 success rate，未给不确定性。 | p.8 `Table 3`；p.15 `A.4` |
| “any offline RL algorithm” 只在 IQL 上实测 | `generality` | 方法写兼容任意 offline RL，但实验没有第二种 policy learner。 | p.5 `Training and Evaluation` |

负面结果处理总体是显式披露。hopper 的 threshold 回落、walker-medium-replay 的 label-count 例外、sweep-into 67% accuracy、human teacher 的 walker2d 下滑、FTB 计算代价均出现在结果或 Appendix。因果边界仍偏弱；reward correlation 和 pseudo-label accuracy 让机制更可信，但没有独立 intervention 证明“coverage 增加”是 policy 提升的唯一中介。

## 10. 结论、limitations 与闭环矩阵

`6. Discussion` 先重述 VOTP 的 OT-over-ViFM 机制与 semi-supervised preference learning，再回收少量 labels、locomotion/manipulation/real-world 结果和“scalable/practical”定位；p.9 的 `Limitations` 随后回收 ViFM bias 与 OT cost。Discussion 没有新增数值，新增的 future directions 在 Appendix D。

| 引言/摘要主张 | 方法回应 | 证据回应 | 结论回应 | 闭环状态 |
|---|---|---|---|---|
| OT + ViFM 可从少量 feedback 生成 pseudo-preference | Eq. (3)–(7)、Algorithm 1 | Fig. 2、Fig. 18、Table 13 | Discussion 重述 OT latent-space propagation | `closed` |
| VOTP 提升低反馈 offline PbRL | reward relabel + IQL | Table 1、Fig. 4；D4RL avg 92.8，MetaWorld avg 67.6 | Discussion 称 limited labels 下有效 | `partially_closed`：MetaWorld 仍低于 GT/Oracle，walker-m-r 不是 label-count 最优 |
| OT 是核心增益来源 | Eq. (5) 的双向 alignment score | Fig. 2 与 similarity-only baselines | Discussion 将 gain 归于 OT+ViFM | `closed`（仅在所测任务与 similarity baselines 范围内） |
| temporal ViFM representation 比 image feature 更适合 | `z=fϕ(o1:H)` 与 spatial/temporal rationale | Fig. 3；ViFM 在关键任务更好 | Discussion 回收 representation quality | `partially_closed`：只测 5 个 encoder |
| 对 visual distractors 稳健 | labeled fixed、unlabeled perturbation | Table 2 六类视觉设置 | Discussion/§5.4 以 nuisance robustness 表述 | `partially_closed`：任务与干扰范围有限 |
| 真实机器人上可用 | reward model + IQL，真实视频/状态输入 | Table 3 80%/70%，Fig. 7、Fig. 15–16 | Discussion 称 practical solution | `partially_closed`：两个任务、10 episodes、demo 数在正文/附录有差异 |
| pseudo-label 提升 reward coverage/alignment | OT pseudo-label + reward training | Fig. 6、Fig. 17 correlation，Table 13 accuracy | §5.3 称 coverage 带来更好 policy | `partially_closed`：correlation 支持 alignment，未识别唯一因果中介 |
| VOTP scalable/practical | Sinkhorn 替代 exact LP；threshold filtering | Table 11 时间随 labels 增长，VOTP <2h vs FTB ~2 days | Discussion 使用 scalable/practical | `partially_closed`：规模边界和 ViFM bias 明确存在 |
| 可接任意 offline RL、可与 active query/ranking 正交组合 | 只把 reward 输出与 policy learner 解耦 | 正文只实测 IQL，无组合实验 | 引言以 potential compatibility 表述 | `not_testable_here` |
| uniform marginals 是合理 relaxation | uniform sampling without replacement | Appendix C.8 给出数据加载理由 | 无正文新主张 | `closed`（design rationale，不是泛化定理） |
| 可扩展到 generative policy/VLA 与医疗等 sequential domains | Appendix D 提出 future directions | 没有对应实验 | 作为未来方向，而非已验证能力 | `not_testable_here` |

## 11. 附录职责与正文衔接

| 附录一级/子模块 | 页数 | 对象数量与内容 | 类别 | 正文调用与依赖 |
|---|---:|---|---|---|
| Algorithm 1 | 14 | 1 个伪代码；从采样到 reward/policy pipeline。 | `extended_method` | p.5 `§4.3` 明确调用；VOTP 的可执行顺序依赖该算法。 |
| A. Details on Experiments | 14–16 | Fig. 8 环境 1 个；Tables 4–8 共 5 个；任务、数据集、IQL/reward/VOTP 超参数、real robot setup、baseline URLs/tuning。 | `implementation_detail` | p.5、p.8 写“Further implementation details ... Appendix”；复现细节主要依赖此节。 |
| B. Learning Curves | 15–18 | Fig. 10–16 共 7 个；D4RL/MetaWorld curves、aggregate metrics、Drawer/Lift Banana qualitative rollouts。 | `additional_result` | p.5 说 full learning curves 与 IQM 在 Appendix；主文结论不依赖每条曲线。 |
| C.1 Cost Metric | 19 | Table 9，Euclidean/cosine。 | `ablation` | p.4 允许两种 `d`；主文只用 Euclidean，鲁棒性依赖附录。 |
| C.2 GT vs Incorrect Rewards | 19 | Table 10，GT/Zero/Random/Negative。 | `additional_result` | 为 reward-sensitive offline RL 提供 sanity check；主文未调用。 |
| C.3 Computational Cost | 19 | Table 11，sequential/parallel 时间；RTX 4090 + 24 CPU cores。 | `implementation_detail` | p.6 主文只给 FTB/VOTP 粗粒度时间，细粒度 scaling 依赖此处。 |
| C.4 Human Teachers | 20 | Table 12，scripted/human 7 个任务；4 位非机器人参与者。 | `additional_result` | 主文使用 scripted labels；human robustness 只在附录成立。 |
| C.5 Pseudo-label Accuracy | 20 | Table 13，7 个任务 accuracy。 | `additional_result` | “high-quality pseudo-preferences” 的直接 task-level 证据依赖此处。 |
| C.6 Reward Comparison | 20、22 | Fig. 17，8 个任务 P-IQL/VOTP scatter；物理图浮动到 p.22。 | `additional_result` | p.7 `Fig. 6` 为 door-open 主文案例，跨任务结论依赖 Fig. 17。 |
| C.7 Pseudo-label Visualization | 20、23 | Fig. 18，4 个 unlabeled pair 的 matrix/plan/score；物理图浮动到 p.23。 | `qualitative_example` | p.4 称 examples 在 Appendix；算法可读性与数值例子依赖此处。 |
| C.8 Uniformity Assumption | 20 | 1 段设计解释：uniform sampling without replacement → uniform marginals。 | `other` | Eq. (4) 使用 uniform marginals 的理由在此闭合。 |
| D. Extended Discussion | 21 | 1 个 future-direction 模块；generative/flow/VLA、representation、3D、跨领域。 | `other` | 正文未要求这些能力；仅承接 future work，不支撑当前结果。 |
| Fig. 19 visual distractors | 23 | lighting、texture、easy/hard video 的场景样例。 | `qualitative_example` | p.8 `§5.4` 调用；Table 2 的视觉设置解释依赖该图。 |

Appendix 迁移的收益是把完整曲线、bootstrap IQM/CI、超参数、计算成本、human teacher 和机制诊断从正文主线中隔离出来；代价是正文只能看到 Table 1–3、Fig. 2–7，读者需要打开附录才能核对 pseudo-label accuracy、跨任务 reward correlation、真实机器人输入细节与计算 scaling。正文对主要决策仍自足：主 benchmark、组件对照、反馈预算、robustness 和 real-robot success 都在 p.5–8；“高质量 pseudo-label”“coverage”与成本边界则部分依赖附录。

## 12. 用词与修辞

按正文语境人工排除 references、公式碎片、表格数值和模板固定词后，最频繁的领域实词为 `reward`、`preference`、`VOTP`、`learning`、`unlabeled`、`labeled`、`transport`、`label(s)`、`performance`、`pair(s)`、`segment(s)`、`PbRL`、`video`、`feedback`、`task(s)`、`offline`、`model(s)`、`visual`。高频二元/三元短语如下。

- `optimal transport`；`video foundation models`；`reward learning`；`preference labels`；`feedback efficiency`；`segment pairs`；`OT plan`；`latent space`；`transport plan`；`GT rewards`；
- `video-based optimal transport`；`unlabeled segment pairs`；`optimal transport plan`；`explicit reward modeling`；`preference-based RL`；`introduce video-based optimal`。

主张动词主要是 `introduce`、`present`、`leverage`、`generate`、`infer`、`demonstrate`、`observe`、`highlight`、`suggest`、`validate`；限定和对比词包括 `only`、`limited`、`generally`、`likely`、`in contrast`、`however`、`while`、`substantially`。正文中可直接检出的 `we` 结构以 `we adopt`、`we use`（各约 6 次）和 `we introduce`（约 3 次）最常见；它们把设置事实和方法动作写在同一段。

**可迁移的写作模式**：先用“反馈成本 → 视觉缺口”建立单一问题，再用一个可画出的 OT/ViFM pipeline 解释机制，随后按“主结果 → 组件替代 → 预算/阈值 → robustness → real robot”顺序推进；每个机制 claim 都有一个对应图或表。公式 Eq. (5) 的 forward/reverse alignment difference 同时给定义和直觉，是最有效的桥接句式。

**明显反模式/读者成本**：`§5.3` 同时承载 OT、encoder、query count、threshold 和 reward correlation，机制消融与结果诊断密集；“coverage improves policy”由 correlation 与 accuracy 间接支撑，因果措辞强于识别设计；主文称“extensive/scalable/practical”，但真实机器人分母很小，OT scaling 与 human-teacher 异质性在 Appendix 才完整出现。另有 benchmark label 主要 scripted、Table 12 任务数与正文叙述不一致、main text 与 Appendix 的真实机器人 demonstrations 数不一致，增加复核成本。

## 13. 最终判断

1. **单一主线**：把人类只标注少量视频 preference 的 PbRL，转成“ViFM 轨迹表征 → OT 相对 alignment → pseudo-preference → Bradley–Terry reward → offline IQL”的半监督闭环；核心创新是用 pairwise forward/reverse transport difference 传播偏好，而非直接用 VLM 评分（p.3–5, `§4`）。
2. **正文保留的决策内容**：问题与缺口、VOTP pipeline、Eq. (3)–(7)、Table 1 主 benchmark、Fig. 2–6 组件/反馈/阈值诊断、Table 2 robustness、Table 3 real-robot success，以及 Section 6 的两项限制。它足够支持“方法如何工作、在哪些任务上改善、哪些变量影响结果”。
3. **移入 Appendix 的细节**：完整 learning curves、bootstrap IQM/95% CI、超参数、源码/tuning、真实机器人输入、cost/human-teacher/pseudo-label accuracy/reward scatter/compute scaling。迁移保持主线清晰，却让“pseudo-label 高质量”“coverage 机制”和计算可扩展性需要读附录才能完全判断（p.14–23）。
4. **最佳模式**：Eq. (5) 将 preference matrix 与 OT plan 组合成可解释 score，Fig. 1 用一个四 labeled/two unlabeled 的数值示例展示相同运算；这比只给 pipeline 图更能让读者复现机制（p.4, `Fig. 1`、`Eq. (5)`）。
5. **最大缺口**：没有 formal performance theory，也没有将 reward coverage 作为独立 intervention；相关性、pseudo-label accuracy 和 policy score 形成支持链，但不能证明唯一因果中介。真实任务、human labels、non-Gaussian policies 和大规模 OT 的外部效度仍开放（p.9、p.19–21）。
6. **可迁移规则**：对于“少量标签 + 大量结构化序列数据”的方法，正文至少应把“标签传播机制、组件替代、标签预算曲线和失败/成本边界”按同一因果顺序呈现，并把每个强主张绑定到直接图表对象。
7. **适用边界**：该规则适合有明确 pairwise/sequence correspondence 的半监督学习；当标签传播依赖未验证的表征语义、数据分布高度非均匀、或 downstream policy 只测单一 learner 时，必须把“可迁移/可扩展”降为部分闭环或 future direction。

## 14. 计数争议与证据覆盖

- PDF 自动测量草稿把 References 起点漏判为 p.9 的混排 heading，因而将 main end provisional 记为 p.23；人工按版面修正为 main complete pages 1–8、references 9–13、Appendix 14–23。
- 自动 caption 识别漏掉 p.15 与真实机器人设置同一行的 `Figure 9`；人工图表清单计为 Figure 1–19 共 19 个。
- 自动算法正则会把 p.5 对 Algorithm 1 的正文提及与 p.14 的 caption 都计数；语义唯一算法为 1 个。
- Appendix C.4 写“across six datasets”，但 Table 12 列出 7 个任务，且 Average 按 7 行计算（p.20）。
- 主文 `§5.5` 写每个真实任务收集 50 demonstrations，Appendix A.4 写 Lift Banana 40、Drawer Open 50；两处事实需并列保留，不能自行选择一个（p.8、p.15）。
- Appendix Table 8 将 SURF 的源码行写作 `SURL`，正文 baseline 与 Table 1 均写 `SURF`；按正文/主表保留 `SURF`，并记录该版面 typo（p.5–6、p.16）。

已追踪的 11 个重要 claim 均具备至少一个 PDF 物理页、章节和短证据锚点；JSON `evidence_coverage` 记为 `11/11, complete`。

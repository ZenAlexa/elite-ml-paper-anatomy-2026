# Visual Planning: Let's Think Only with Images

- **paper_id**：`iclr-2026-dedfde9d7c99`
- **来源**：ICLR 2026 官方 proceedings PDF，物理页 34 页；实际读取 `corpus/pdfs/iclr-2026-dedfde9d7c99.pdf` 及对应 `corpus/text/iclr-2026-dedfde9d7c99.txt`。
- **样本位置**：`replication_200`，ICLR `oral`。本备忘只依据本地 PDF；references、Appendix A–G 和 Prompting Templates 均已读到第 34 页。

## A. 文档边界与页级地图

PDF 为 letter 纸双栏排版，正文主体为双栏；Figure 1、2、3、4 跨栏，Figure 5–6 并列，表格多为跨栏或栏宽浮动体。p10 同时承载结论、致谢和 references 起始部分，因此正文／references 的物理页计数重叠该页。p16–34 为附录；附录中的图表多占整栏或整页，p28–30 的轨迹图文字量很低，但图像面积占主导。

| 物理页 | 内容与模块 | 估计词数（英文词） |
|---|---|---:|
| 1 | 标题、摘要、引言开头 | 511 |
| 2 | 引言、Figure 1 | 558 |
| 3 | 引言收束、贡献、§2 开头与 Eq. (1) | 632 |
| 4 | §2.2、Figure 2、Eq. (2)–(3) | 493 |
| 5 | Eq. (4)、§3 Tasks/Models 开头 | 659 |
| 6 | Table 1、模型、指标与主结果开头 | 557 |
| 7 | Figure 3、Table 2、主结果与难度结果 | 490 |
| 8 | Figure 4、§4 error analysis、初始化与 invalid-action 分析 | 595 |
| 9 | Figure 5–6、§5 Related Work | 551 |
| 10 | §6 Conclusion、Acknowledgements、References 起始 | 551 |
| 11–15 | References | 2365 |
| 16–17 | Appendix A–D（LLM、ethics、reproducibility、limitations/broader impact） | 1237 |
| 17–20 | Appendix E（implementation details） | 2178 |
| 20–32 | Appendix F（results、OOD、消融、图像质量、成本） | 3650 |
| 33–34 | Appendix G（prompting templates） | 783 |

**章节边界与语义映射**：

- `Abstract`：p1，`abstract`。
- `1 Introduction`：p1–3，`introduction`；Figure 1 是引言中的范式对照。
- `2 Visual Planning via Reinforcement Learning`：p3–5，`method`。其中 §2.1 的形式化定义和 §2.2 的优化目标属于方法内部的形式化对象；论文没有独立的 theory 章节。
- `3 Experiments and Results`：p5–8；Tasks/Models/Evaluation Metrics 记为 `experimental_design`，Table 1–2 及正文实证记为 `results`。
- `4 Discussions and Analysis`：p8–9，`results` 与 `ablation`；包括 error analysis、Stage 1 exploration 和 invalid-failure ratio。
- `5 Related Work`：p9，`related_work`。
- `6 Conclusion`：p10，`conclusion`。
- `Acknowledgements` 与 `References`：p10–15，`other`。
- `Appendix A Use of Large Language Models`、`B Ethics Statement`、`C Reproducibility Statement`：p16，`other`/`appendix` 支撑声明。
- `Appendix D Limitations and Future Work`：p16–17，`limitations`。
- `Appendix E Implementation Details`：p17–20，`appendix`。
- `Appendix F Results`：p20–32，`appendix`。
- `Appendix G Prompting Templates`：p33–34，`appendix`。

物理页计数：`pdf_pages=34`、`main_pages=10`、`reference_pages=6`（p10–15）、`appendix_pages=19`（p16–34）。`main_pages` 与 `reference_pages` 因 p10 混排而有一页重叠。

## B. 摘要逐句功能编码

| # | 摘要句（保留术语） | 词数 | 功能 | 限定词、数字、比较对象、承接 | 证据 |
|---:|---|---:|---|---|---|
| 1 | Recent advancements in Large Language Models (LLMs) and their multimodal extensions (MLLMs) have substantially enhanced machine reasoning across diverse tasks. | 20 | `object_scope` | `substantially`；对象为 LLM/MLLM 与广泛任务；为背景起点 | p1，摘要；“enhanced machine reasoning across diverse tasks”；`explicit` |
| 2 | However, these models predominantly rely on pure text as the medium for both expressing and structuring reasoning, even when visual information is present. | 23 | `problem_gap` | `predominantly`、`even when`；与视觉输入形成反差 | p1，摘要；“predominantly rely on pure text”；`explicit` |
| 3 | In this work, we argue that language may not always be the most natural or effective modality for reasoning, particularly in tasks involving spatial and geometrical information. | 27 | `problem_gap` | `may not always`、`particularly`；空间／几何任务为范围限定 | p1，摘要；“language may not always be the most natural or effective modality”；`explicit` |
| 4 | Motivated by this, we propose a new paradigm, Visual Planning, which enables planning through purely visual representations for these “vision-first” tasks, as a supplementary channel to language-based reasoning. | 28 | `core_idea`, `object_scope` | `vision-first`、`supplementary channel`；把图像规划定位为语言推理的补充 | p1，摘要；“we propose a new paradigm, Visual Planning”；`explicit` |
| 5 | In this paradigm, planning is executed via sequences of images that encode step-by-step inference in the visual domain, akin to how humans sketch or visualize future actions. | 27 | `method` | `step-by-step`；以连续中间图像编码推理 | p1，摘要；“planning is executed via sequences of images”；`explicit` |
| 6 | We introduce a novel reinforcement learning framework, Visual Planning via Reinforcement Learning (VPRL), empowered by GRPO for post-training large vision models, leading to substantial improvements in planning in a selection of representative visual navigation tasks, FROZEN LAKE, MAZE, and MINI BEHAVIOR. | 41 | `method`, `experimental_setup`, `qualitative_result` | `novel`、`selection of representative`；GRPO、LVM、三个任务；只称 `substantial`，未给数字 | p1，摘要；“VPRL ... empowered by GRPO”；`explicit` |
| 7 | Our visual planning paradigm outperforms all other planning variants that conduct reasoning in the text-only space. | 16 | `qualitative_result` | `all other` 是强比较主张；比较对象为 text-only planning variants | p1，摘要；“outperforms all other planning variants”；`explicit` |
| 8 | Our results establish Visual Planning as a viable and promising supplement to language-based reasoning, opening new avenues for tasks that benefit from intuitive, image-based inference. | 25 | `impact_claim` | `viable and promising`、`opening new avenues`；将结果外推到受益于图像推理的任务 | p1，摘要；“viable and promising supplement”；`explicit` |
| 9 | Code is available at: https://github.com/yix8/VisualPlanning. | 8 | `impact_claim` | 可复现入口；无实验数字 | p1，摘要；“Code is available at”；`explicit` |

摘要功能顺序为 `object_scope → problem_gap → core_idea → method → experimental_setup/qualitative_result → impact_claim`。它报告定性比较，却没有在摘要给出 27% 或 Table 1 的具体数字；没有理论定理，也没有直接写出局限。最强结果位于句 7–8，分别使用 `outperforms all` 和 `viable/promising`；句 6 将证据范围限定为三个代表性视觉导航任务。

## C. 引言论证推进

| 段/动作 | 页 | 估计词数 | 上一段留下的问题 | 当前段回答与下一段钩子 | 证据 |
|---:|---:|---:|---|---|---|
| 1 `context` | 1 | 115 | 需要说明推理能力的背景 | LLM/MLLM 具备语言推理和多模态输入；引出视觉空间推理与导航 | p1，§1；“MLLMs ... incorporate visual embedded information at the input”；`explicit` |
| 2 `problem` | 1 | 92 | 多模态输入是否带来视觉推理 | 现有方法在推理时仍将视觉内容转成文本并生成 verbal rationales；留下媒介问题 | p1，§1；“perform reasoning purely in the text format during inference”；`explicit` |
| 3 `failure_of_prior_work` | 1 | 105 | 文本路径是否总是合适 | 空间、几何、物理动态任务中，纯语言推理表现不足；留下 modality gap | p1，§1；“purely language-based reasoning falls short in certain domains”；`explicit` |
| 4 `missing_insight` | 1–2 | 145 | modality gap 怎样影响状态推理 | 文本 grounding 阻碍视觉特征和 state transition 捕捉；提出“能否直接用非语言模态规划” | p1–2，§1；“can models directly plan in non-verbal modalities”；`explicit` |
| 5 `context` + `failure_of_prior_work` | 2 | 135 | 视觉化是否已经解决问题 | Dual Coding Theory 提供 verbal/nonverbal 双通道动机，但 Visual Sketchpad、MVoT 仍由文本驱动、视觉只是工具或辅助 | p2，§1；“still remain fundamentally text-driven”；`explicit` |
| 6 `core_idea` | 2 | 155 | 现有 interleaving 是否等于 visual-only | 定义 Visual Planning：用无语言中介的图像序列承载规划步骤；宣称避免 modality mismatch、强化 state transitions | p2，§1；“reasoning is structured as a sequence of images, but without the mediation of language”；`explicit` |
| 7 `method_preview` | 2–3 | 165 | 如何在无语言条件下研究与训练 | 选择只用图像/视频预训练的 LVM，提出 GRPO 驱动的两阶段 VPRL；Stage 1 初始化探索，Stage 2 用 progress reward | p2，§1；“two-stage reinforcement learning framework empowered by GRPO”；`explicit` |
| 8 `result_preview` | 3 | 100 | 该范式是否可行 | 在 FROZEN LAKE、MAZE、MINI BEHAVIOR 上验证；摘要式预告平均 EM 比文本 SFT 高 27%，并有更强 OOD 泛化 | p3，§1；“achieving 27% higher average exact-match rate”；`explicit` |
| 9 `contribution_list` | 3 | 90 | 具体贡献如何归纳 | 三点：纯视觉范式、两阶段 VPRL、相对文本与 supervised baselines 的实证优势/泛化 | p3，贡献列表；“We propose ... We introduce ... We demonstrate empirically”；`explicit` |

引言链为：`context → problem → failure_of_prior_work → missing_insight → context/limitation_of_prior → core_idea → method_preview → result_preview → contribution_list`。估计引言约 900 词，占正文语义文字约 18.8%；贡献列表与摘要存在术语重复（Visual Planning、VPRL、视觉优于文本），但新增了两阶段结构和 27% EM 结果，三条贡献均为可检验主张。它没有明确给出失败边界、成本数字或统计不确定性。

## D. 相关工作

相关工作是独立的 §5（p9），约 420 词，正文估计占比约 8.8%；分成三个段落，每段一个引用簇和一个定位对照维度。

1. **MLLM Reasoning**（`nearest_neighbor_contrast`、`gap_creation`）：先列 grounding、symbolic representations 与 tool visualization，再指出 o3、MVoT 等仍以语言为推理媒介、图像仅作 rationale illustration；本文将差异收束为“多步规划是否可完全在视觉表征中出现”。证据，p9，“visual components merely illustrating the textual rationale”。
2. **Reinforcement Learning for Visual Reasoning**（`chronology`、`nearest_neighbor_contrast`）：从 GRPO/DeepSeek-R1 到 detection、VQA、图像生成的 RL 应用，比较维度是 pixel-level fidelity/text alignment 与本文 goal-oriented visual state transitions 的差别。证据，p9，“optimizing multi-step decision-making through visual state transitions”。
3. **Action-conditional Generative Models**（`credit_or_foundation`、`limitation_of_prior`、`nearest_neighbor_contrast`）：承认 world models/latent dynamics 对未来观测预测和 model-based RL 的基础作用；指出它们通常仍需外部 planner，而本文把 planning internalize 到 visual generative flow。证据，p9，“do not perform planning and must therefore be coupled with an external planner”。

相关工作没有单独再写一遍 VPRL 的算法步骤；每个引用簇都服务于媒介、优化目标或 planner ownership 的对比。其引用在后续仍承担论证作用：p8 用 modality-gap 解释误差，p16 用 image-generation 模型文献支持可扩展性。

## E. 方法与理论

### E.1 形式化对象与机制

- **输入／状态／输出**：输入初始视觉状态 `v_0`；前缀 `v_{≤i}=(v_0,…,v_i)`；输出为中间视觉状态序列 `T̂=(v̂_1,…,v̂_n)`。动作不以显式 action token 预测，动作由当前图像到下一图像的 transition 隐式表达。证据，p3 §2.1，“actions are not explicitly predicted but instead implicitly represented by transitions between visual states”。
- **模型**：`π_θ` 为自回归生成视觉模型；LVM-7B 仅在 image sequences/video frames 上预训练，图像 tokenizer 基于 VQGAN，把图像编码为 256 个 visual tokens。证据，p3、p18，§2.1/E.2。
- **Stage 1**：主文以 random walks 产生的轨迹 warm up；从 `(v_0,…,v_n)` 提取 `n−1` 个 `(v_{≤i},v_{i+1})` 图像对；对每个前缀从所有 valid next states 随机选一个 `ṽ_{i+1}`，用 VPFT 目标保持有效格式与随机探索。
- **Stage 2**：行为模型 `π_{θold}` 对每个前缀采样 `G` 个候选图像；`D` 将 transition 解析为 valid/invalid action，`P` 估计离目标的剩余步数；候选按 progress 与有效性分为 optimal、non-optimal、invalid，GRPO 在组内计算相对优势并以 clipped ratio 加 KL penalty 更新。
- **Reward**：`α_opt=1`、`α_nopt=0`、`α_inv=−5`。这样把“有效且减少剩余距离”“有效但不前进”“违反环境约束”分开；invalid action 惩罚幅度大于其它两类。
- **实现级 interpreter**：Appendix E.3 采用灰度化、网格划分、局部 IoU 判断 agent 位置；用坐标间 MSE 识别 disappearance/appearance；Maze 用 movement rules 检查穿墙；MiniBehavior 额外用 printer/table 的 IoU/MSE 变化识别 `pick`/`drop`。`P` 通过 BFS 构造每个位置的 progress map。

### E.2 五个编号公式核对

论文有 **5 个 displayed numbered equations，5 个均带编号，均位于 §2 或 E.4 的方法/基线说明**；无 theorem、lemma、proposition、corollary 或 proof。Eq. (4) 前另有一个未编号的集合划分 `A_opt/A_nopt/E_inv`；EM/PR 的数学定义嵌入指标段落，未进入编号公式清单。

1. **Eq. (1), p3，`core_chain`**：
   `v̂_i ∼ π_θ(v_i | v_0, v̂_1, …, v̂_{i−1})`。
   这是视觉轨迹的自回归生成定义，表达当前中间视觉状态依赖初始状态和此前生成状态。证据，p3 §2.1，“generated autoregressively”；`explicit`。
2. **Eq. (2), p4，`core_chain`**：
   `L_VPFT(θ) = − E_(v≤i, ṽi+1) [ log π_θ(ṽi+1 | v≤i) ]`。
   这是 Stage 1 的 visual planning fine-tuning loss；随机 valid next-state 作为监督目标，作用是视觉连贯性、格式与探索初始化。证据，p4 §2.2，“minimize the following loss function ... VPFT”；`explicit`。
3. **Eq. (3), p4，`core_chain`**：
   `J_VPRL(θ)=E[ (1/G) Σ_i min(ρ^(k)A^(k), clip(ρ^(k),1−ε,1+ε)A^(k)) − β D_KL(π_θ || π_ref) ]`，其中正文定义 `A^(k)=(r^(k)−mean(r))/std(r)`、`ρ^(k)=π_θ(v̂^(k)|v≤i)/π_θold(v̂^(k)|v≤i)`。
   该目标把 group-relative advantage、PPO-style clipping 与 reference-policy KL penalty 接到视觉候选生成。PDF 中求和下标按排版显示为 `i=1…G`，候选上标为 `(k)`；这里保留其版面记号，不替作者改写。证据，p4 §2.2，Eq. (3)；`layout_observation`。
4. **Eq. (4), p5，`core_chain`**：
   `r(v_i,v̂^(k)_{i+1}) = α_opt I[D(v_i,v̂^(k)_{i+1})∈A_opt] + α_nopt I[D(·)∈A_nopt] + α_inv I[D(·)∈E_inv]`。
   它是复合 progress reward；三个 indicator 对应 optimal、non-optimal、invalid。证据，p5 `Reward Design`，Eq. (4)；`explicit`。
5. **Eq. (5), p20，`explanation`**：
   `L_SFT(θ)=−E_(v,t)[ Σ_(i=1)^L log π_θ(t_i | t_<i,v,p) ]`。
   它给出文本 action-sequence baseline 的 cross-entropy，承担 visual-vs-language 对照，而非 VPRL 的核心目标。证据，p20 E.4，“minimize the cross-entropy loss for action prediction”；`explicit`。

**公式推进序列**：`setup_notation → define_component → derive (1) → instantiate_algorithm → derive (2) → explain_mechanism → derive (3) → define_component (D/P) → derive (4) → connect_to_experiment → contrast_alternative (5)`。理论对象承担核心因果链和优化定义；没有独立可证明保证，故 `theory` 模块为 `not_present`。

### E.3 算法、图和表的解释粒度

论文没有标号为 Algorithm 的伪代码（`algorithm_captions=0`）。Figure 2 是框架图：LVM 解码候选图像对，interpreter 解析 action，reference current state 提供 optimal/all valid action 对照，reward 回到 policy update。算法循环虽无伪代码，但正文覆盖到候选采样、组内优势、ratio clipping、KL penalty 和 reward partition；没有逐 token 的生成循环或复杂度表达。方法图 1 个（Figure 2），用于框架接口而非性能结果。

## F. 实验设计

| 设计项 | 论文事实与粒度 | 证据 |
|---|---|---|
| 研究问题 | 视觉序列能否在没有文本推理代理的条件下完成 vision-first planning；VPRL 是否比 VPFT 和 text planning 更有效、更能 OOD 泛化 | p2–3 §1，p5 §3；“whether models can achieve planning purely through visual representations”；`explicit` |
| 任务 | FROZEN LAKE、MAZE、MINI BEHAVIOR；前两者 action space 为 up/down/left/right，MiniBehavior 再加 pick/drop | p5、p17 E.1；`explicit` |
| 数据与划分 | FrozenLake/Maze 每个 3×3–6×6 尺寸 1250 environments，1000 train/250 test；MiniBehavior 7×7/8×8，train 796/801、test 204/199；layout identity 分割，避免 train/test layout overlap | p17–18、Table 3；`explicit` |
| 初始状态 | agent 从可达目标的随机位置初始化；测试只给每个环境的初始状态 `v_0` | p17；`explicit` |
| 方法/基线 | LVM-7B VPFT、VPRL；Qwen 2.5-VL-Instruct-7B Direct/CoT/SFT/RL；Gemini 2.0 Flash Direct/CoT 与 Gemini 2.5 Pro (think) | p6 Table 1，E.2/E.4；`explicit` |
| 控制与公平性 | VPRL Stage 2 使用与 VPFT 相同的 input states；语言与视觉 setup 使用相同环境数据；image tokenizer/detokenizer 冻结；post-training 使用 LoRA | p17、p20；`explicit` |
| 指标 | Exact Match (EM)：预测轨迹是否匹配任一最短 optimal trajectory；Progress Rate (PR)：从起点开始连续正确 forward moves 的比例。状态相等按环境 transition/action 语义判断，不按 pixel-wise image equality 判断 | p6，Evaluation Metrics；`explicit` |
| 优化/预算 | AdamW；SFT 最多 30 epochs；VPRL Stage 1 10 epochs + Stage 2 10 epochs，组大小 10，`β=0.001`；文本 RL 10 epochs、组大小 8；8×A100；详细值见 Table 5 | p19–20、Table 5；`explicit` |
| 随机性 | 论文未报告随机 seed、重复运行次数、跨 seed 汇总或 seed-level uncertainty | p19–20/Table 5 全文；`layout_observation` |
| 统计处理 | 主表为 test trajectory 聚合百分比；Figure 7 给 group-level reward standard deviation 并做 Gaussian smoothing；其余图表未给 CI、显著性检验、bootstrap、Bayesian model 或回归 | p6、p21、p32；`explicit`/`layout_observation` |
| 设计顺序 | 先主结果（Table 1–2），再难度/错误/探索/invalid 分析（Figures 3–6），附录提供文本变体、OOD、Stage 1、图像质量和成本 | p6–9、p20–32；`layout_observation` |
| 复现粒度 | 主文有任务描述、模型类别、指标和主数字；数据样本、reward parser、超参数、许可、prompt 全部移至 E/G | p5–6、p16–20、p33–34；`explicit` |

## G. 结果、统计与可视化

### G.1 主结果

- **Table 1（p6，主结果）**：VPRL 在 FROZEN LAKE/MAZE/MINI BEHAVIOR 的 EM/PR 分别为 `91.6/93.2`、`74.5/77.6`、`75.8/83.8`，平均 `80.6/84.9`。VPFT 为 `75.4/79.5`、`59.0/64.0`、`33.8/52.2`，平均 `56.1/65.2`；Qwen SFT 平均 `53.6/69.9`。因此 VPRL 比 text-SFT 平均 EM 高 `27.0` 个百分点，与摘要“27% higher”对应。统计是每个 test environment/trajectory 的确定性 EM/PR 百分比；没有 seed、误差条或显著性检验。表注独立解释了 `EM`、`PR`、`†`、文本/图像输入符号和 AVG。作者将结果解释为 VPRL 跨任务一致最好。
- **Table 2（p7，文本 reward/representation 对照）**：FrozenLake 上 Qwen SFT Direct 为 `68.6/84.4`，Coordinates `74.4/82.7`，ASCII `73.1/83.4`；text GRPO + VPRL reward 为 `54.4/69.9`，+ PR metric reward 为 `60.1/74.3`。聚合仍为 EM/PR，无不确定性。作者解释为结构化文本不足以消除 modality gap，text RL 未超过 SFT。
- **Figure 3（p7，定性动作类别）**：三行分别展示 FrozenLake、Maze、MiniBehavior 的 generated visual traces，标注 optimal、non-optimal、invalid（穿墙、进入 table cell 等）。图的任务是把 reward partition 对应到可观察状态转移；无统计聚合。
- **Figure 4（p8，案例比较）**：同一 FrozenLake 输入下，对照 Gemini 2.5 Pro 的长文本 CoT、Qwen textual SFT 的 invalid action 与 VPFT/VPRL visual traces；VPRL 示例绕开障碍，VPFT 卡住。它支持 modality-gap 和 detour 的解释，但属于单案例，无法单独估计频率。
- **Figure 5（p9，复杂度）**：FrozenLake 网格由 3×3 增至 6×6；文本模型准确率陡降，visual planners 曲线更平缓。正文给出 Gemini 2.5 Pro EM 从 `98.0%` 降至 `38.8%`、VPRL 从 `97.6%` 仍有 `82.4%`。按 grid-size 分层确定性 EM，无误差表达。

### G.2 机制、探索与失败

- **Figure 6（p9）**：横轴 invalid ratio、纵轴 average entropy，比较 VPRL Stage 1 与 VPFT 2/5/10/30 epoch checkpoint。VPRL Stage 1 接近 uniform random planner 的高 entropy，同时维持较低 invalid ratio；VPFT 训练越久 entropy 下降，并在早期 checkpoint 出现较高 invalid ratio。图注使用 “significantly”，但未提供检验方法或 p 值；这里只编码为 checkpoint-level diagnostic，不把“significantly”当作已完成的推断统计。
- **Table 6（p20）**：在所有 failed trajectories 中，至少含一个 invalid action 的比例为 FrozenLake VPRL `36.9%` vs VPFT `60.6%`；Maze `25.1%` vs `73.7%`；MiniBehavior `29.6%` vs `78.3%`。分母是失败轨迹，不是全部测试轨迹；作者据此主张 VPRL 改善 action-validity control。无区间、检验或 seed 分解。
- **Figure 7（p21）**：VPRL 三任务的 progress reward 随 step 曲线；阴影为 groups 间 standard deviation，作者对 reward 和对应 standard deviation 做 Gaussian smoothing。它是训练动态诊断，不能替代最终 EM/PR。

### G.3 附录结果、消融与成本

- **Table 7（p21）**：FrozenLake 各 difficulty L3–L6 的 text/visual 方法。7B Qwen Direct EM 从 `97.6` 降到 `34.4`，VPRL 从 `97.6` 降到 `82.4`，平均 EM `91.6`；均值是 difficulty-level 算术平均，未报告区间。
- **Table 8（p22）**：VPFT*（Stage 1 后再做 optimal-trajectory SFT）在 3×3–6×6 的 EM 为 `86.4,73.6,50.0,33.2`，标准 VPFT 为 `92.0,82.8,68.8,58.0`；Stage 1 初始化本身不提高 supervised planning。
- **Table 9（p22）**：更大 OOD grid，FrozenLake 7×7，VPFT/VPRL EM/PR=`9.6/15.3` vs `20.4/31.2`；Maze 7×7=`9.2/17.8` vs `10.0/21.6`；MiniBehavior 9×9=`0.0/5.8` vs `0.4/14.7`。相对优势存在，但绝对 OOD EM 很低；无不确定性。
- **Table 10（p27）**：VPRL Stage 1 的 EM/PR 为 FrozenLake `11.1/27.2`、Maze `9.6/22.7`、MiniBehavior `0.5/14.2`；Stage 2 为 `91.6/93.2`、`74.5/77.6`、`75.8/83.8`。此项直接区分 format/exploration warm-up 与 outcome-based RL。
- **Table 11（p31）**：FrozenLake 以 self-generated images 与 ground-truth images 作为中间输入。EM 平均 `91.6` vs `92.1`，PR 平均 `93.2` vs `93.4`；作者据此认为图像噪声不是主要性能瓶颈。
- **Figure 10（p25）**：Maze 与 MiniBehavior 的 grid-size accuracy 曲线；visual planners 整体更高、更平坦。MiniBehavior 准确率随 grid size 增长，作者解释为布局组件固定（table/printer），结构模式可迁移；这是假设性解释，未有额外控制。
- **Figure 11–12（p26–27）**：Figure 11 比较 OOD 大网格的 VPFT/VPRL 轨迹；Figure 12 对输入做黑/灰遮挡，定性显示 VPRL 仍跟随可见结构。后者没有遮挡比例、样本量或定量汇总。
- **Figures 13–15（p28–30）**：分别列 FrozenLake、Maze、MiniBehavior 的 optimal、non-optimal、invalid VPRL 轨迹。失败包括局部循环、穿墙、agent disappearance、同时左右、teleportation；图像承担 failure taxonomy，作者没有将代表性案例转成 failure count。
- **Figure 16 / Tables 12–13（p31–32）**：Figure 16 对比 original、predicted、tokenizer reconstructed images，支持 artifact 来自 tokenizer；Table 11/ground-truth 结果支持规划对中间图像噪声的鲁棒性。Table 12 的平均 token cost，Gemini 2.0 Flash Direct `12.7`、CoT `171.2`，Gemini 2.5 Pro Think `1178.6`，Qwen Direct `41.1`、CoT `298.3`、SFT `11.8`，LVM VPFT/VPRL `1082.5`；Table 13 的 text variants Direct `10.7`、Coordinates `179.0`、ASCII `84.3`、GRPO+VPRL reward `129.8`、GRPO+PR reward `74.9`。这是跨任务/变体的平均生成 token 数，不是 wall-clock 或 GPU cost；作者据此称 visual planning 比 Qwen CoT 约 3 倍、比 Gemini 2.0 CoT 约 6 倍，仍可行。

## H. 消融、负面结果与自我设限

消融和扩展材料占正文很小比例（§4 p8–9 约 310 词、Figure 6 为 1 个图；主体消融移到 Appendix F）。对象、识别目标和证据如下：

| 对象/类型 | 识别目标 | 结果与证据 |
|---|---|---|
| text Coordinate vs ASCII vs Direct（组件/表示替代） | 判断结构化文本是否弥补视觉 grounding | Table 2 p7、Tables 7/Figure 8 p21–23：EM 有轻微变化但 PR 下降或仍落后 VPRL；`observed` |
| text GRPO reward（机制替代） | 区分 VPRL progress reward 与 PR metric reward 的学习信号 | Table 2 p7、F.2 p22–25：`54.4/69.9` 与 `60.1/74.3`，均低于 text SFT；`observed` |
| VPFT checkpoint entropy（探索机制） | 检验 teacher-forcing 是否导致相同 reward/zero advantage | Figure 6 p9、§4 p8：VPFT entropy 下降，invalid ratio 随 checkpoint 变化；`observed` |
| Stage 1 → Stage 2（组件删除/阶段对照） | 区分 format warm-up 与 goal-directed outcome optimization | Table 10 p27：Stage 1 近随机，Stage 2 大幅提升；`observed` |
| VPFT*（阶段结构敏感性） | 判断 Stage 1 是否直接提高 supervised planning | Table 8 p22、F.5 p26：VPFT* 低于 VPFT；Stage 1 的价值落在 RL exploration initialization；`observed` |
| grid size / difficulty（规模敏感性） | 测试复杂度提升下的曲线稳定性 | Figures 5 p9、10 p25，Table 7 p21：VPRL 曲线更平；MiniBehavior 的反常上升由固定布局解释；`observed` |
| OOD enlarged grids（泛化） | 判断是否学到 planning strategy 而非仅记忆布局 | Table 9 p22、Figure 11 p26：VPRL 相对优于 VPFT，但绝对 EM 低；`observed` |
| masked input（鲁棒性） | 测试部分遮挡下是否保留结构一致性 | Figure 12 p27：定性成功；没有遮挡率/样本级统计；`observed` |
| self-generated vs ground-truth intermediate image（输入质量） | 判断图像 tokenizer/生成 artifact 是否损害 planning | Figure 16、Table 11 p31：平均 EM/PR 几乎相同；`observed` |
| invalid trajectory cases（失败案例） | 列出 semantic format/环境约束失败 | Figures 13–15 p28–30：loop、穿墙、disappearance、contradiction、teleportation；`observed` |

**负面结果**：VPFT* 低于 VPFT；Stage 1 单独近随机；text RL 低于 text SFT；OOD 的 absolute EM/PR 很低；VPRL 仍有 non-optimal 和 invalid traces；中间图像有 tokenizer artifacts；visual planning token cost 高于 text SFT/CoT 的若干基线。它们出现在 p8 的讨论、Appendix F.2/F.5/F.6/F.7/F.8 和图表中。

**呈现方式（中性编码）**：

- **附录迁移**（`scope`/`compute`）：数据构造、parser、超参数、文本变体、OOD、Stage 1、失败图和 token cost 大多放到 p16–32；正文仍保留 Table 1、2、Figure 3–6 的决策关键数字。证据，p6 “Full training details ... Appendix E.4”；`layout_observation`。
- **相对优势与绝对低值并置不足**（`generality`/`metric`）：Table 9 报告 VPRL 优于 VPFT，但三项 OOD EM 最高仅 `20.4`；正文与附录文字强调“certain level/consistently outperforms”。证据，p22 Table 9；`layout_observation`。
- **定性鲁棒性替代定量覆盖**（`metric`）：Figure 12 展示 masked-input traces，未报告遮挡比例、样本数、失败率或对照。证据，p27 Figure 12；`layout_observation`。
- **单案例承载机制解释**（`causality`）：Figure 4 的 detour/caught-stuck 案例支持 modality-gap 叙事，但没有逐样本的 detour 统计；正文把它与 Table 2/6 并列讨论。证据，p8 Figure 4 及 error analysis；`interpretation`。
- **“significantly”无统计细节**（`metric`）：Figure 6 图注与正文使用 `significantly` 描述 entropy/invalid ratio，但全篇未给检验、分母、seed 或区间。证据，p9 Figure 6，p19–20 Table 5；`layout_observation`。
- **成本以 token 数代理**（`compute`）：Appendix F.8 给出平均 token cost，未给 wall-clock、显存、吞吐或端到端 rollout latency；“affordable/feasible”属于 token 代理下的解释。证据，p32 Table 12–13；`explicit`/`interpretation`。

## I. 结论、限制与闭环

### I.1 结论段落编码

p10 §6 为一个段落，动作序列为 `重述问题 → 重述方法 → 回收结果 → 回收影响`。它重申 Visual Planning 以 visual state transitions 取代 textual mediation，回收 VPRL/GRPO 两阶段方法，回收“三个任务、27% EM、OOD 更强”的结果，最后把方向外推到更广的 multimodal research。没有引入新数字；`27%` 已在 p3 与摘要出现。证据，p10，“It obtains significant gains across three visual navigation tasks”。

### I.2 Limitations / broader impact

- **LVM-7B 与模型范围**：只有 publicly available 7B LVM 可用；该选择排除 native multimodal output models，限制规模和模态覆盖。p16 D，`scope`。
- **图像生成计算开销**：显式生成图像带来 inference overhead；论文只用 token cost 与 Gemini 长 CoT 对照，建议 compact representations。p16 D、p32 F.8，`compute`。
- **Dynamics interpreter 依赖受控规则**：当前用 pixel-wise features、IoU/MSE、task-specific movement rules；复杂视觉结构和可靠 progress signal 尚未验证。p16 D、p18–19 E.3，`generality`/`causality`。
- **任务与数据范围**：三个 synthetic grid/navigation tasks，MiniBehavior 布局组件固定；未覆盖复杂自然图像、开放世界或长时程机器人部署。p5、p17–18，`data`/`deployment`。
- **OOD 与图像质量边界**：更大网格的 VPRL absolute EM 很低（p22 Table 9）；Figure 13–15 仍有 loop、穿墙、disappearance、teleportation，tokenizer 带来 artifacts。p22、p28–31，`generality`/`metric`。
- **风险/伦理**：Appendix B 说明已核对软件与数据许可，作者“do not anticipate any additional potential risks”；这属于作者声明，不等同于跨领域部署风险评估。p16 B，`ethics`。

### I.3 闭环矩阵

| 引言主张 | 方法回应 | 证据回应 | 结论回应 | 状态 |
|---|---|---|---|---|
| 纯图像序列可承载 vision-first planning | §2.1 轨迹定义 Eq. (1)，LVM 只用视觉 token | Table 1、Figure 3–4 在三种导航任务展示 EM/PR 与 traces | p10 重申 visual state transitions | `partially_closed`：任务范围窄，未覆盖一般视觉规划 |
| VPRL 的两阶段结构能学习有效 visual planning | Stage 1 valid/random exploration；Stage 2 GRPO reward/clip/KL | Table 1、Table 10、Figure 6 | p10 回收 VPRL/GRPO | `closed`（在三项受控任务内） |
| VPRL 优于 text planning 与 VPFT | Eq. (4) reward；相同 input state/data 的对照 | Table 1–2、Table 7、Figure 5 | p10 回收 27% EM | `partially_closed`：比较依赖选定模型/任务，`all` 的外推不足 |
| Stage 1 主要提供 exploration，而非 planning ability | 随机轨迹 VPFT loss；Stage 2 outcome optimization | Figure 6、Table 8、Table 10 | p8 与 p26 明确分工 | `closed`（机制证据为 entropy、阶段对照，仍未有独立 causal randomization） |
| VPRL 学到可泛化策略 | RL 由 progress/validity 反馈，而非只拟合 optimal traces | Table 9、Figure 10–12 | p10 声称 stronger OOD generalization | `partially_closed`：OOD absolute score 很低且只扩大 grid/遮挡 |
| modality gap 是 text baseline 瓶颈 | visual-only transition，text baseline 需 grounding/ASCII/coordinates | Table 2、Figure 4、Figure 8–9 的 layout mismatch | p10 将 visual planning 定位为 alternative | `partially_closed`：错误归因主要是观察性比较 |
| reward 可扩展到更广视觉任务 | D/P 抽象、三类 action partition；E.3 给 IoU/MSE/BFS 实现 | 三个 synthetic task、Table 6 invalid ratio | p16 提出 segmentation/neural validator/trajectory rollouts 作为未来工作 | `open`：未在更广任务验证 |
| 视觉生成 artifacts 不妨碍规划 | tokenizer reconstruction 与 feedback parser | Figure 16、Table 11 | F.7 结论为 robust to visual noise | `partially_closed`：仅 FrozenLake，GT image 替换是窄对照 |
| 视觉规划在成本上可行 | 自回归图像生成，未提供部署优化 | Table 12–13 token averages | p16/p32 用“affordable/feasible”表述 | `partially_closed`：token 代理未覆盖 wall-clock/显存 |

## J. 附录职责

| 一级模块 | 页 | 类别 | 内容、对象数量与正文调用 |
|---|---:|---|---|
| A Use of Large Language Models | 16 | `other` | 说明 LLM 只用于 writing polish；正文无直接调用。 |
| B Ethics Statement | 16 | `ethics_impact` | 软件/数据许可与潜在风险声明；正文无直接调用。 |
| C Reproducibility Statement | 16 | `reproducibility` | 指向 E.1–E.5、G 和 release plan；复现职责总览。 |
| D Limitations and Future Work | 16–17 | `broader_impact` | LVM-7B范围、成本、interpreter scope、broader impact；正文结论未逐条回收，p16 作为唯一集中限制段。 |
| E.1 Dataset | 17–18 | `dataset_detail` | action space、数据构造、train/test、layout leakage control、Table 3–4；主文 p5/p17 调用 E.1。 |
| E.2 Models | 18 | `implementation_detail` | LVM tokenizer/256 tokens、7B 可用性、Qwen 对照；主文 p6 的 model setup 依赖 E.2。 |
| E.3 Reward Implementation | 18–19 | `implementation_detail` | BFS progress map、grayscale/grid/IoU/MSE parser、pick/drop、reward 1/0/−5；主文 p6 调用 E.3。 |
| E.4 Training Details | 19–20 | `hyperparameter` | VPFT/SFT/RL 定义、LoRA、AdamW、epochs、group sizes、β、GPU、Table 5；主文 p6 调用 E.4。 |
| E.5 Licenses | 20 | `reproducibility` | LVM/Qwen/TRL Apache-2.0、FrozenLake MIT、Maze 自建脚本；C 的许可声明依赖本节。 |
| F.1 VPRL Training | 20–21 | `additional_result` | Figure 7 reward curves + standard deviation/Gaussian smoothing。 |
| F.2 Trained Textual Baselines and Reward Design | 21–25 | `ablation` | Table 7、文本 representation 与 GRPO reward variants；主文 Table 2/p8 error analysis 调用 F.2。 |
| F.2.1 Examples of Trained Textual Variants | 25 | `qualitative_example` | Figure 8–9 的 layout mismatch 例子；p22 明确调用 Figure 8 in Appendix F.2.1。 |
| F.3 Performance with Scaling Difficulties | 25 | `robustness` | Figure 10、Maze/MiniBehavior 难度曲线与固定布局解释；p7 调用 F.3。 |
| F.4 Out-of-Distribution Performance | 25–26 | `robustness` | Figure 11、Table 9、masked input Figure 12；p8 调用 F.4。 |
| F.5 Ablation: The Role of Stage 1 | 26 | `ablation` | VPFT* 及 Stage 1 只作 RL-friendly initialization 的解释。 |
| F.6 Visual Planning Results | 26–31 | `qualitative_example` | Table 10、Figures 13–15 及 optimal/non-optimal/invalid taxonomy；p7–8 多次调用 F.6。 |
| F.7 Image Quality Analysis | 31–32 | `additional_result` | Figure 16、Table 11；tokenizer artifacts 与 self-generated/GT image 对照。 |
| F.8 Computational Cost Analysis | 32 | `additional_result` | Table 12–13 token cost；正文没有等价的 wall-clock 证据。 |
| G Prompting Templates | 33–34 | `implementation_detail` | FrozenLake Direct/Coordinate/ASCII/GRPO、Maze、MiniBehavior 的完整 prompts；主文 p5–8 和 F.2 的格式解读依赖 G。 |

附录总长 19 页，相对正文物理页比为 `1.9`；按估计文字约 6546 词，约为正文语义文字 1.37 倍。它补足了数据、奖励、超参数、prompt、OOD 和失败图，支撑 Table 1 的复现与解释；但规则解析器的边界、随机 seed、推断时延和跨任务统计仍未提供。正文保留了 Table 1–2、Figure 3–6、主要 EM/PR、invalid-failure ratio 以及 Stage 1/2 的核心机制判断，因此决策链可读；复现和外推判断若不看 E/F/G 会失去关键条件。

## K. 用词与修辞

下面的数字是对本地 `pdftotext` 中 p1–10、references 前正文的定位性粗计；正式 raw token 计数由汇总脚本统一完成。表格、公式碎片、模板固定语和 references 不用于解释论证动作。由于 PDF small caps 将 `FROZEN LAKE` 等拆成字母，短词计数有切分风险。

| 词/短语 | 粗计次数 | 主要定位与语境 |
|---|---:|---|
| `visual planning` | 41 | 摘要、引言定义、贡献列表、§2、结论；核心对象名词 |
| `visual` | 119 | 范式、state、reasoning、planning 的广义修饰，受标题/图注驱动 |
| `planning` | 73 | 问题、trajectory、baselines、结果和结论；真实论证动作与领域模板共同驱动 |
| `language` | 34 | modality gap、text pathway、text baseline、结论边界；主要出现在问题/对照段 |
| `reasoning` | 49 | 引言问题、related work、结论影响；模板和主线共同驱动 |
| `image`/`images` | 40 | visual state、tokenizer、generation、图像质量附录；方法与成本边界 |
| `state`/`states` | 44 | Eq. (1)、transition、interpreter、指标；机制术语驱动 |
| `action`/`actions` | 79 | reward partition、valid/invalid、任务约束；结果与失败分析高频 |
| `reward`/`rewards` | 23 | Eq. (3)–(4)、Stage 2、文本 RL 对照、Figure 7；优化机制驱动 |
| `VPRL` | 29 | 摘要、方法、Table 1、主结果、讨论和结论；主张中心 |
| `VPFT` | 24 | baseline、Stage 1/teacher forcing、Figure 6、Table 8；对照中心 |
| `modality gap` | 4 | p1–2 引言，p7–8 error analysis；关键因果解释 |
| `outperforms` | 2 | 摘要句 7、贡献列表；强主张集中在摘要/贡献 |
| `demonstrate(s)`/`show(s)` | 17 | Table/Figure 引用和结论回收，部分是图表引导语 |
| `observe` | 5 | 结果解释、错误分析、探索/鲁棒性；较弱的观察性语气 |
| `significant(ly)` | 5 | 贡献、主结果、Figure 6、结论；其中部分无推断统计支撑 |

主张动词从强到弱约为 `outperforms / demonstrate / show / establish` 与 `observe / suggest / hypothesize / attribute` 并存。强主张集中在摘要、贡献列表和结论，弱主张集中在 error analysis、MiniBehavior 解释和 OOD/图像质量段。因果词主要围绕 `leads to`、`driven by`、`enables`、`causing`、`due to`；其中 modality-gap 与 Stage 1 机制主要由平行基线和 checkpoint 对照支持，仍缺少随机干预。`visual planning`、`VPRL`、`state/action/reward` 的高频来自真实方法推进；`visual`、`reasoning` 还受标题、图注和 related-work 模板影响。

## L. 最终判断

1. **单一主线**：对于空间/几何状态转移，直接把推理轨迹表示成连续图像，让 LVM 在视觉状态空间内规划；Stage 1 先学可解析且可探索的状态转移格式，Stage 2 用 `validity + progress` reward 和 GRPO 将探索变成目标导向规划。
2. **正文保留的决策关键内容**：范式对照 Figure 1、VPRL 框架 Figure 2、五个编号公式、任务/模型/EM-PR 定义、Table 1–2、难度曲线、error analysis、Stage 1 exploration 和 invalid-failure ratio。这些内容足以形成“问题、机制、任务、主要结果、机制诊断”的短闭环。
3. **移入附录的细节及自足性**：数据统计、layout split、parser 的 IoU/MSE/BFS、所有超参数、文本 prompts、OOD 数字、Stage 1/2、失败轨迹、tokenizer reconstruction 与 token cost 均在附录。正文叙事可独立成立；复现、外推和成本判断依赖附录，尤其是 Table 9 的低绝对分数与 E.3 的受控 parser 边界。
4. **最有效的写作/图/表/公式模式**：Figure 1 以同一输入并列 Direct/CoT/Visual Planning，Figure 2 把 image pair→interpreter→reward→policy update 画成闭环，Table 1 同时给三任务与平均 EM/PR，Table 10 把 Stage 1/2 数字化拆开。Eq. (1)–(4) 从视觉轨迹、初始化 loss、GRPO objective 到 reward partition 逐层落地。
5. **最大叙事缺口与读者成本**：摘要和结论的 `outperforms all`、`generalization`、`feasible` 范围大于三项 synthetic grid tasks、低绝对 OOD EM、规则型 interpreter 和 token-only 成本证据；Figure 12 的鲁棒性与 Figure 4 的机制解释主要是定性/单案例。读者需要跨 p16–32 拼接限制、统计缺口和失败频率。
6. **可迁移规则**：若方法主张“新推理媒介”，先用同一输入的媒介对照图建立接口差异，再用一个可解释的阶段/组件对照把中间机制与最终任务指标分开，并在主结果表同时展示跨任务分项与聚合值。
7. **适用边界**：该规则适用于状态转移可从图像直接验证、存在明确 progress/validity 判定的视觉规划任务；当状态语义开放、动作不可由图像差分可靠解析或成本目标是 wall-clock latency 时，需要增加独立 dynamics validator、真实时延/资源测量和跨域任务，而不能由本论文的 token 或定性轨迹证据替代。

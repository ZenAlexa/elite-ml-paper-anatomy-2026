# DCFold：单次前向的蛋白质结构生成

## 读取边界与身份

- **论文**  DCFold: Efficient Protein Structure Generation with Single Forward Pass
- **作者**：Zhe Zhang、Yuanning Feng、Yuxuan Song、Keyue Qiu、Hao Zhou、Wei-Ying Ma
- **会议与等级**：ICLR 2026，Oral
- **身份证据**  PDF 第 1 页页眉为 ICLR 2026，标题和作者与目录一致。[p.1, 标题区, explicit, “DCFOLD: EFFICIENT PROTEIN STRUCTURE GENERATION WITH SINGLE FORWARD PASS”]
- **实读版本**：`corpus/pdfs/iclr-2026-a8e7c788acec.pdf`，官方 proceedings PDF，18 个物理页。对应文本缓存为 `corpus/text/iclr-2026-a8e7c788acec.txt`。
- **引用入口**  OpenReview forum `LMsdys7t1L`；官方 PDF URL 写入 JSON 的 `source_files.source_url`。
- **版面**  双栏 ICLR 论文模板。第 1 页标题和摘要居中，正文从第 1 页开始；Figure 1 为正文右栏浮动体，Figure 2 跨栏；表格大多嵌在两栏之一。第 14 页上半部先放 Figure 6、Figure 7，再开始 Appendix A。公式独立居中，编号从 (1) 连续到 (22)。[p.1, p.3, p.14, layout_observation, “Figure 2: Overview of Dual Consistency framework”]

## A. 页级地图

| 区域 | 物理页 | 说明 |
|---|---:|---|
| 标题、摘要、引言 | 1–2 | 摘要在 p.1；引言跨 p.1–2 |
| Preliminary | 2–3 | Consistency Models、PF-ODE 和 Eq. (1) |
| Method | 3–6 | Dual Consistency、TGM、Downstream Task |
| Experiment | 6–10 | Structure Prediction、Diversity and Confidence、Binder Hallucination、TGM 验证 |
| Related Work、Conclusion、Ethics | 10–11 | §5、§6；Ethics 从 p.10 延续至 p.11 |
| Reproducibility、Acknowledgments | 11 | References 从 p.11 开始 |
| References | 11–13 | 参考文献结束于 p.13 |
| Appendix 图与附录 | 14–18 | Figure 6–7、Appendix A–C、LLM statement |

- **PDF 总页数**：18。
- **主文页数**：10 页，按 References 起始于 p.11 计；主文最后一个研究章节为 §6 Conclusion（p.10）。
- **References 页数**：3 页（p.11–13）。
- **Appendix 页数**：5 页（p.14–18）。
- **精确边界**：§6 Conclusion 在 p.10；Ethics Statement 从 p.10 下半部开始并在 p.11 开头续完。`REFERENCES` 从 p.11 中段开始。Appendix A 的 Figure 6–7 位于 p.14 上半部，`A DERIVATION OF TGM` 从 p.14 下半部开始。
- **章节与语义模块映射**：`2 Preliminary` 作为 method 的预备逻辑；`3.3 Temporal Geodesic Matching` 的 Definition、Proposition 和推导归入 theory；§4 中的 Baselines、Data、Metrics 和任务协议归入 experimental_design，数值比较归入 results；§4.4 的 baseline/schedule/训练动态比较归入 ablation。Ethics、Reproducibility、Acknowledgments 和 LLM 使用声明归入 `other`。

## B. 摘要逐句功能

1. **文本**：AlphaFold3 introduces a diffusion-based architecture that elevates protein structure prediction to all-atom resolution with improved accuracy.
   - 词数：16。
   - 功能：`object_scope`、`qualitative_result`。
   - 限定词、数字与比较：`all-atom`、`improved`；背景对象为 AlphaFold3。
   - 承接：建立高精度基础模型背景，为后文的效率缺口作铺垫。
   - 证据：[p.1, Abstract, explicit, “diffusion-based architecture”]
2. **文本**：This state-of-the-art performance has established AlphaFold3 as a foundation model for diverse generation and design tasks.
   - 词数：16。
   - 功能：`object_scope`、`impact_claim`。
   - 限定词、数字与比较：`state-of-the-art`、`diverse`；没有数值。
   - 承接：把结构预测转成下游生成与设计的适用范围。
   - 证据：[p.1, Abstract, explicit, “foundation model for diverse generation and design tasks”]
3. **文本**：However, its iterative design substantially increases inference time, limiting practical deployment in downstream settings such as virtual screening and protein design.
   - 词数：21。
   - 功能：`problem_gap`、`limitation`。
   - 限定词、数字与比较：`substantially`、`limiting`；下游场景为 virtual screening 和 protein design。
   - 承接：把准确率优势转为部署瓶颈。
   - 证据：[p.1, Abstract, explicit, “iterative design substantially increases inference time”]
4. **文本**：We propose DCFold, a single-step generative model that attains AlphaFold3-level accuracy.
   - 词数：12。
   - 功能：`core_idea`、`method`。
   - 限定词、数字与比较：`single-step`、`AlphaFold3-level`；比较对象为 AlphaFold3。
   - 承接：直接给出模型和目标精度。
   - 证据：[p.1, Abstract, explicit, “single-step generative model”]
5. **文本**：Our Dual Consistency training framework, which incorporates a novel Temporal Geodesic Matching (TGM) scheduler, enables DCFold to achieve a 15× acceleration in inference while maintaining predictive fidelity.
   - 词数：26。
   - 功能：`core_idea`、`method`、`quantitative_result`。
   - 限定词、数字与比较：`novel`、`15×`、`maintaining`；比较对象隐含为原始推理过程。
   - 承接：说明双一致性与 TGM 的组合以及速度量级。
   - 证据：[p.1, Abstract, explicit, “15× acceleration in inference”]
6. **文本**：We validate its effectiveness across both structure prediction and binder design benchmarks.
   - 词数：12。
   - 功能：`experimental_setup`、`qualitative_result`。
   - 限定词、数字与比较：`both`；两个任务为 structure prediction 和 binder design。
   - 承接：把主张交给两个实验场景检验。
   - 证据：[p.1, Abstract, explicit, “structure prediction and binder design benchmarks”]

**摘要顺序与强主张位置**：`对象背景 → foundation-model 影响 → 迭代效率缺口 → DCFold 核心方法 → 15× 定量结果 → 两类验证任务`。摘要报告了 15× 加速，却没有给出具体 accuracy 表值、统计区间或失败条件；没有理论对象名称，也没有单独的 limitations 句。最强的速度主张放在第 5 句，适用范围和验证任务收尾。

## C. 引言的论证推进

| 段 | 页码 | 主动作 | 上一段留下的问题 | 当前段回答与下一钩子 | 估计词数 |
|---:|---:|---|---|---|---:|
| 1 | 1 | `context` → `failure_of_prior_work` | 为什么蛋白结构预测值得高成本建模 | AF2/AF3 提供精度和复杂生物分子范围，但 Pairformer recycle 与 diffusion 迭代造成计算开销；钩子是长序列和下游吞吐 | 350 |
| 2 | 1–2 | `problem` | 开销在实际工作流中有多严重 | 长序列推理以分钟计，数千候选使 screening 不可承受；钩子是已有手工减少 recycle 的折衷 | 180 |
| 3 | 2 | `failure_of_prior_work` | 能否简单减少迭代次数 | BindCraft 的手动 recycle reduction 换取效率却损失精度，hallucination 的多步 refinement 也阻碍梯度回传；钩子是 diffusion acceleration | 170 |
| 4 | 2 | `problem` → `missing_insight` | 现有 diffusion solver 是否足够 | high-order solver 通常仍需 10 步以上，CM 的固定维度/欧氏配对不适合 variable-length 序列，且不能处理 Pairformer recycle | 220 |
| 5 | 2 | `core_idea` → `method_preview` → `theory_preview` | 两类迭代瓶颈如何同时处理 | Dual Consistency 同时约束 diffusion 和 Pairformer，TGM 在 intrinsic geometric space 配对 timestep；钩子是 accuracy/fidelity 验证 | 300 |
| 6 | 2 | `result_preview` → `scope_boundary` | 方法是否只服务标准 folding | Posebusters V2、Recent PDB 和 binder design 同时验证速度、结构准确率和梯度可用性 | 120 |
| 7 | 2 | `contribution_list` | 论文具体贡献是什么 | DCFold 以 Dual Consistency 消除 AF3 迭代开销；是摘要的模型层复述 | 70 |
| 8 | 2 | `contribution_list` | 调度贡献是什么 | TGM 针对 variable-length 序列的 CM 限制，主张稳定训练和提升性能；包含可检验机制 | 75 |
| 9 | 2 | `contribution_list` → `result_preview` | 证据覆盖哪些任务 | 两个结构 benchmark 的 AF3-level accuracy 与 15× speedup，以及 binder screening success；没有列出限制 | 115 |

**推进链**：`AF2/AF3 精度与范围 → 迭代开销 → 长序列/下游吞吐 → 减少 recycle 的精度代价与梯度障碍 → 固定维度 CM 的失配 → Dual Consistency + TGM → 三项贡献与 benchmark 预览`。贡献列表重复了摘要中的模型、TGM 和 benchmark 三块，但第 2 项把 variable-length mismatch 明确为可证伪的机制主张。引言没有给出表格数字，15× 与 AF3-level 只在第三项以结果预览出现。[p.1–2, §1, explicit, “We propose DCFold, a single-step folding model”]

## D. 相关工作

- **位置**：独立 §5，位于 §4 Experiment 之后、§6 Conclusion 之前，仅 p.10 两段。没有在方法段再次展开相关工作。
- **估计篇幅**：约 320 词，约占主文估计词数 6.1%。引用簇约 15 个，主要用于方法谱系与分类。正文的 48 次 `et al.` 由引用标记驱动，未把它当成论证词。
- **段 1，p.10**：`taxonomy` + `chronology` + `nearest_neighbor_contrast`。先从 Rosetta/co-evolution 到 RaptorX/trRosetta，再到 AF2、MSA-free 模型、AlphaFold-Multimer、AlphaFold3。比较维度为 MSA 依赖、结构精度、交互类型和计算开销；结尾把 acceleration/distillation/approximation 建成缺口。[p.10, §5 Protein Structure Prediction, explicit, “Despite setting new standards in accuracy and scope”]
- **段 2，p.10**：`taxonomy` + `nearest_neighbor_contrast`。把 diffusion acceleration 分为 training-free solvers、training-based distillation、flow-based reformulations，并分别列 high-order solver、progressive/adversarial/CM 和 flow matching。比较维度是 sampling steps、极少步退化、self-consistency 与轨迹直化；对 DCFold 的 TGM 差异只作定位，没有再次介绍算法。[p.10, §5 Diffusion Acceleration, explicit, “fall into three categories”]
- **作用**：先承认 AF3 的准确率与范围基础，再把计算开销和 variable-length consistency schedule 定为 DCFold 的最近缺口。相关工作引用在 §4.3 继续承担 BindCraft pipeline 的基线来源，在 §4.4 继续承担 CD/sCM/ECM 对照，而非只停留在背景列表。[p.8–9, §§4.3–4.4, explicit, “Following the same hallucination strategy and filtering pipeline as BindCraft”]

## E. 方法与理论

### E.1 形式对象与单次前向机制

- **输入与输出**：训练输入包括 PDB 结构数据、噪声 `ϵ`、时间 `t` 以及 AF3/Protenix 特征；模型输出蛋白或复合物结构，并产生 diffusion、Pairformer 和 confidence 表征。[p.4, §3.2, explicit, “After the n-th cycle, the model produces a pair representation zn and a single representation sn”]
- **两类迭代瓶颈**：AF3 的 diffusion 多步采样与 Pairformer recycling 都造成推理开销。关闭噪声注入 `γ0=0`、固定 `λ=1`、步长归一化 `η=1` 后，AF3 ODE 可作 one-step sampler；再以 Pairformer Consistency 对单次前向内部的不同 cycle depth 进行约束。[p.3–4, §3.2, explicit, “a single forward pass through the network inherently provides representations corresponding to different cycle depths”]
- **单次前向的关键含义**：DCFold 的实验配置只保留 1 个 recycle 和 1 个 diffusion denoising step。Pairformer 的多个中间表示来自同一 forward pass 的层间传递，不再为每个 cycle 单独执行整网；这解释了单次推理如何同时保留结构 refinement 信号。[p.7, §4.1, explicit, “uses only 1 recycle and 1 diffusion denoising step”]

### E.2 方法动作序列

1. `setup_notation`：Preliminary 用 PF-ODE、`fθ(xt,t)`、EMA teacher 和 `x̃ti` 定义 CM 背景，并给出 Eq. (1)。[p.2–3, §2, explicit, “probability flow ODE (PF-ODE)”]
2. `state_problem`：§3.2 将 diffusion process 和 Pairformer recycling 标成两个效率瓶颈。[p.3, §3.2, explicit, “iterative diffusion process and Pairformer recycling”]
3. `derive`：分析 AF3 few-step sampler，给出 `γ0=0`、`λ=1`、`η=1` 的稳定化改动。[p.3, §3.2, explicit, “disabling noise injection”]
4. `define_component`：Diffusion Consistency 以 timestep `t` 输出和 reference timestep `r` 输出的 MSE 作为 Eq. (2)。[p.4, §3.2, explicit, “diffusion consistency loss”]
5. `explain_mechanism`：Pairformer 每个 cycle 依赖前一 cycle，因此一个 forward pass 暴露不同 cycle depth 的 `zn`、`sn`。[p.4, §3.2, explicit, “progressive refinement of structural accuracy”]
6. `define_component`：Pairformer cycle consistency 以相邻 cycle 的 pair/single 表征传输误差形成 Eq. (3)，实验 `N=4`。[p.4, §3.2, explicit, “with N = 4 in our experiments”]
7. `instantiate_algorithm`：按 token 类型使用 AlphaFold 权重 `α`；pair 表征用逐元素平方根外积 `√α√α⊤`，nucleic acids/small molecules 权重更高。[p.4, §3.2, explicit, “positions corresponding to nucleic acids and small molecules are assigned higher weights”]
8. `derive` → `summarize`：引入 `Lconfidence = Lplddt + Lpde + Lresolved + αpae Lpae`，然后以 Table 1 规定两阶段训练和损失权重。[p.4, §3.2, explicit, “our training procedure can be summarized in two stages”]
9. `state_problem`：TGM 指出固定欧氏间隔对 variable-size outputs 产生 ill-posed curriculum，长序列小 `Δt` 也可能引发大分布位移。[p.4–5, §3.3, explicit, “the core issue lies in scheduling for variable-size outputs”]
10. `define_component`：把 forward diffusion 的中间分布族 `pt(x)` 看作一维 temporal information manifold `Mt`，以 Fisher information 定义时间度量，再以其积分定义 geodesic distance。[p.5, §3.3, explicit, “a one-dimensional temporal information manifold Mt”]
11. `derive` → `connect_to_prediction`：Proposition 1 连接局部 geodesic distance 与 KL divergence，TGM 以固定 `dg(t,r)=C(u)` 配对 reference timestep。[p.5, §3.3, explicit, “the geodesic distance between neighboring distributions”]
12. `instantiate_algorithm`：设置 `C(0)=C0`、`C(1)=0`、`C(u)=C0(1-u)^β`，用 Euler 近似 `r(t,u)=t−√C0(1−u)^β/√I(t)`，并给出 Algorithm 1。[p.5, §3.3, explicit, “approximate r(t, u) via one-step Euler method”]
13. `derive`：Proposition 2 给出 classical Gaussian diffusion 的解析 `I(t)`，指出维度 `D` 对 schedule 的作用，再特化到 EDM 的 Eq. (8)。[p.5–6, §3.3, explicit, “where D denotes the dimensionality of the vector”]
14. `connect_to_experiment`：§3.4 将单次、可微和低成本特性连接到 binder hallucination，并把实验细节移到 §4.3。[p.6, §3.4, explicit, “fully differentiable and amenable to gradient-based optimization”]

**段落动作转移**：`setup_notation → state_problem → derive → define_component → explain_mechanism → define_component → derive → summarize → state_problem → define_component → derive → instantiate_algorithm → derive → connect_to_experiment`。

### E.3 理论对象与公式核对

- **编号公式**：22 个，Eq. (1)–(22) 连续。
- **displayed equations**：23 个。除 Eq. (1)–(22) 外，p.4 还有未编号的 `Lconfidence` 展示式。自动计量的 22 对应编号公式；未编号损失式单独保留在 inventory 中。[p.4, §3.2, layout_observation, “Lconfidence = Lplddt + Lpde + Lresolved + αpae · Lpae”]
- **理论对象按本次 schema 计 3 项**：Proposition 1、Proposition 2、Appendix A.1 proof。PDF 还以 Definition 1 和 Definition 2 介绍 `g(t)=I(t)` 与 `dg(t,r)`，这两个定义已经作为 Eq. (4) 和 Eq. (5) 的公式条目记录，没有把理论对象数量重复增加。
- **Proposition 1**：局部步长 `Δt=t−r≥0` 下，`dg(t,r)=√2 DKL(pr(x)||pt(x))^{1/2}+O((Δt)^3)`；证明在 Appendix A.1。[p.5, §3.3, explicit, “Proposition 1 (Local Metric-KL Equivalence)”]
- **Proposition 2**：若 `pt(x|x0)=N(x; α(t)x0, σ²(t)I)`，则 `I(t)=E[σ̇(t)/σ(t)·2D + α̇(t)/σ(t)·||x0||²]`；用于把维度放进 schedule。[p.5, §3.3, explicit, “For any diffusion model that satisfies the classical setting”]
- **证明**：Appendix A.1 以 Eq. (9)–(16) 展开 KL、Taylor、score integral 与 Fisher information 关系；Appendix A.2 以 Eq. (17)–(22) 推导 Gaussian/EDM 形式。[p.14–16, Appendix A, explicit, “The proof of Proposition 1 is provided in the Appendix A.1”]

### E.4 图、表与算法传达的信息

Figure 2 把 AF3 的多次 Pairformer/diffusion 流程与 DCFold 的单次流程上下对照，虚线箭头对应两类 consistency，右侧 binder hallucination/complex assembly/feature extraction 说明下游接口保持不变。[p.3, Figure 2, layout_observation, “top/bottom AlphaFold3 and DCFold”]

Table 1 是两阶段训练契约。Stage (i) 只更新 Diffusion，`Lconfidence=10^-4`、`Ldiffusion=1`；Stage (ii) 只更新 Pairformer，`Lconfidence=10^-4`、`Lpairformer=1`。正文说明 Stage (ii) 使用 16-block Pairformer。[p.3–4, Table 1, explicit, “Training stages and the weights of each term”]

Algorithm 1 是 TGM 的可执行粒度：输入 `D, θ, p(t), w(t), u`；每轮抽样 `x0, ϵ, t`，计算 `r′=max(r(t,u),0)`，用同一随机噪声构造 `xt` 与 `xr′`，对 `fθ` 和 stop-gradient teacher 的 MSE 更新参数。[p.4, Algorithm 1, explicit, “using the same random seed”]

### E.5 方法细节位置

- `w(t)=1`：作者称实验中权重影响 negligible。[p.4, §3.2, explicit, “we therefore set w(t) = 1”]
- Pairformer consistency 的 cycle 数：理论描述为 `N`，实验取 `N=4`；推理配置最终使用 1 recycle。[p.4, §3.2; p.7, §4.1]
- TGM schedule：`C0`、`β`、EDM 的 `p,smax,smin` 在 Appendix B.3 给出为 `C0=32, β=2, p=7, smax=160, smin=4×10^-4`。[p.17, Appendix B.3, explicit, “Hyperparameter search yields C0 = 32 and β = 2”]
- 训练配置：64 张 NVIDIA H800，effective batch size 64；Stage 1 约 40 小时/9,000 steps，Stage 2 约 7 小时/1,500 steps。[p.16, Appendix B.1, explicit, “64 NVIDIA H800 GPUs”]

## F. 实验设计

| 设计项 | 论文事实 | 证据 |
|---|---|---|
| 研究目标 | 同时评估 accuracy 与 practical utility；没有列出预注册假设或预先决策阈值 | p.6, §4, explicit, “evaluate both the accuracy and practical utility” |
| 训练数据 | 2021-09-30 之后发布的 PDB entries，按 Protenix scheme 和 identical filtering protocols 组织 | p.7, §4.1, explicit, “released after September 30, 2021” |
| 结构评测 | PoseBusters V2 的 post-2021 protein–ligand crystal complexes；Low Homology Recent PDB，含 protein/nucleic-acid interfaces | p.7, §4.1, explicit, “two benchmarks” |
| 基线 | AlphaFold3、AF3 ODE、AF3 TGM、DCFold、Protenix-Mini | p.6–7, §4.1, explicit, “We compare these AlphaFold3 variants” |
| 结构指标 | PoseBusters 使用 predicted/experimental ligand RMSD，best/worst 低于 1、2、3、5 Å 的比例；Recent PDB 使用 TM-score、SR（RMSD < 2 Å）和 lDDT | p.7, §4.1, explicit, “Ground truth is not used for any filtering” |
| 泄漏控制 | GT 不用于 PoseBusters filtering；训练 cutoff 之前条目从评测排除 | p.7, §4.1, explicit, “All entries predating the training cutoff are excluded” |
| 多样性与置信度 | 每个 test sequence 采样 5 个结构，计算 pairwise TM-score 平均；pLDDT 均值作为 confidence；另测 15 samples 与 5 seeds × 1 sample | p.7–8, §4.2, explicit, “we sampled five structures” |
| Binder 任务 | 六个 target：IL2-Rα、TrkA、H3、VirB8、ALK、LTK；binder 长度 55–65 residues；连续 hallucination 48 小时 | p.8, §4.3, explicit, “perform a continuous 48-hour hallucination run” |
| Binder 流程 | BindCraft strategy/filtering；用 DCFold confidence 和 losses 作为 sequence feedback；folding constraints 固定用 AF2 输出 | p.8, §4.3, explicit, “folding constraints are consistently computed using the outputs of AlphaFold2” |
| Binder 指标 | model-based constraints 来自 AF2 confidence，physics-based constraints 来自 Rosetta；详细阈值在 Appendix B.2 | p.8、p.16, §§4.3/B.2, explicit, “using the same two filters as BindCraft” |
| TGM 对照 | CD、sCM、ECM、TGM；Table 6 报告 time per step 与 PoseBusters success rate；sCM 长序列 OOM | p.9, §4.4, explicit, “processing long sequences often results in out-of-memory (OOM) errors” |
| 硬件与实现 | Protenix open-source reimplementation 作为 baseline 和 DCFold initialization；训练 H800 配置在 B.1 | p.7、p.16, explicit, “derived from Protenix” |
| 随机种子与训练预算 | 多样性实验给出 sampling seeds 设置；训练未报告独立 random seeds、完整 optimizer 配置或每 benchmark 的重复次数 | p.8, §4.2, layout_observation, “5 seeds × 1 sample” |
| 失败判定与不确定性 | Binder 有明确过滤阈值；主结果未报告显著性检验、bootstrap、置信区间或 seed-level error bars | p.16、p.6–9, explicit/layout_observation, “Final designs are filtered using predefined thresholds” |

**实验顺序**：结构预测先检验 one-step accuracy 与效率，再检验 diversity/confidence；binder hallucination 连接下游 utility；最后用 CD/sCM/ECM 对照和 gradient/loss/Euler-error 图拆解 TGM。该顺序大体对应引言中的两个 bottleneck 和三个贡献，但没有为每个理论假设预先列出单独假设编号。

## G. 结果、统计与可视化

### G.1 图表清单

| 编号 | 模块 | 页码 | 内容与编码通道 |
|---|---|---:|---|
| Figure 1 | introduction | 1 | 左图按 token bins 比较 AF3/DCFold folding time，右图比较 PoseBusters success rate；折线、虚线平均线与柱状图结合 |
| Figure 2 | method | 3 | 上下流程图对比 AF3 与 DCFold，虚线箭头标 Pairformer/Diffusion Consistency |
| Table 1 | method | 3 | 两训练阶段、模块和三项 loss 权重 |
| Algorithm 1 | method | 4 | TGM sampling、reference timestep、same-seed 更新循环 |
| Table 2 | results | 6 | PoseBusters V2 best/worst RMSD threshold proportions |
| Table 3 | results | 6 | Recent PDB 三类复合物的 TM-score 与 SR |
| Figure 3 | results | 8 | Recent PDB 的 Pairformer cycles、Diffusion NFE、Complex lDDT、Prot-Prot lDDT 四组柱状比较 |
| Table 4 | results | 8 | 5/15 samples 与 5 seeds × 1 sample 的 diversity/confidence，均值 ± 数值 |
| Table 5 | results | 9 | 六 target 的 physics-based/model-based binder success rate 及平均值 |
| Table 6 | ablation | 9 | CD、sCM、ECM、TGM 的 time/step 与 PoseBusters success rate |
| Figure 4 | ablation | 9 | `r(t,u)` Euler solver relative error 的 `t × u` 三维表面图 |
| Figure 5 | ablation | 10 | ECM/TGM 的 gradient norm 与 loss 随训练 step 曲线及阴影 |
| Figure 6 | appendix | 14 | 7r6r、7wux、7pzb 三个 case study，Experimental、AlphaFold3、DCFold 叠加结构 |
| Figure 7 | appendix | 14 | ALK、H3、IL2Rα、VirB8 四个 binder-target 结构示例 |
| Table 7 | appendix | 17 | 七个 token bins 的 AF3/DCFold average inference time |
| Table 8 | appendix | 18 | 六 target 的 generated sample counts，BindCraft 与 DCFold 对照 |
| Table 9 | appendix | 18 | 六 binder target 的 PDB ID、family、description |

手工按 PDF 可见标题计数为 **7 figures、9 tables、1 algorithm**。自动计量的 5 figures、7 tables、1 algorithm 漏掉了嵌在正文行内的 Figure 1、Figure 4、Table 1、Table 6；附录标题和行内 caption 也造成正则边界差异，见 `measurement_disagreements`。

### G.2 主要结果与统计处理

1. **速度与总览**  Figure 1 标注 AF3 平均 133.3 s、DCFold 平均 8.9 s，约 15× 差异；PoseBusters success rate 为 AF3 82.9、DCFold 78.6。按 token bin 的 Appendix Table 7 显示 AF3/DCFold 从 ≤255 tokens 的 92.63/3.76 s 到 ≥896 tokens 的 212.12/27.40 s。统计单位是样本或 token bin 的平均时间，未报告方差、重复次数或显著性检验。[p.1, Figure 1, explicit, “AF3 avg: 133.3s”]
2. **PoseBusters V2**：Table 2 报告每个复合物预测 pose 的 best/worst RMSD 阈值比例。AF3 best `<1/<2/<3/<5` 为 67.14/82.86/87.14/93.81%，DCFold 为 58.10/78.57/86.67/94.29%；AF3 worst 为 45.71/70.00/79.05/87.62%，DCFold 为 46.67/71.43/80.00/90.48%。作者用 worst-case 的提升和 best-case 的近似不变解释为输出分布收紧；聚合分母为 benchmark predictions，未给出样本数或区间。[p.6, Table 2; p.7, §4.1, explicit, “best and worst RMSDs”]
3. **Recent PDB**：Table 3 在 PL-complex、Monomer、PP-complex 三类报告 TM-score 与 SR。DCFold 分别为 0.824/94.9%、0.850/95.7%、0.800/92.2%，相对 AF3 ODE 的绝对提升分别标为 +1.2/+2.6pp、+2.3/+2.9pp、+4.8/+5.2pp。作者另以 AF3 对照值说明 DCFold 达到或超过；统计单位是类别聚合，未给出每类样本量和离散度。[p.6, Table 3, explicit, “Values in parentheses denote the absolute improvement relative to AF3 ODE”]
4. **lDDT 与 NFE/cycle**：Figure 3 的 Complex lDDT 柱为 AF3 ODE 0.455、AF3 TGM 0.489、DCFold 0.507、Protenix-mini 0.490、AF3 0.501；Prot-Prot lDDT 为 0.623、0.637、0.646、0.622、0.650。Pairformer cycles 的 NFE 图标注 1、1、1、2、200，Diffusion NFE 标注 1、1、1、2、? 的可见比较。作者用此图同时支持单步能力和两个 consistency 组件的互补收益，但没有显著性或 error bars。[p.8, Figure 3, layout_observation, “Complex LDDT”]
5. **Diversity/confidence**：Table 4 的 AF3 (5 samples) 为 diversity 0.9646 ± 0.0410、confidence 93.97 ± 2.92；DCFold (5 samples) 为 0.9701 ± 0.0565、94.14 ± 2.97。15 samples 和 5 seeds × 1 sample 的 DCFold diversity 为 0.9708 ± 0.0567、0.9712 ± 0.0570，confidence 为 94.13 ± 2.96、94.15 ± 2.97。作者称 diversity 轻微下降、confidence 轻微上升；`±` 的具体统计定义未明示。[p.8, Table 4; §4.2, explicit, “Diversity (↓)”]
6. **Binder hallucination**：Table 5 的六 target 平均 physics/model success rate 为 BindCraft `.26/.69`、DCFold `.29/.78`。DCFold 在 H3 `.23/.71`、VirB8 `.21/.85`、LTK `.47/.93` 的两个约束或大部分约束上提升明显；IL-2Rα 与 ALK 的 physics rate 为 `.37`、`.12`，低于 BindCraft 的 `.38`、`.14`。作者强调 majority targets 和平均值，实验单位是六个 target 的过滤后 success rate，未报告跨 run 离散度或 wet-lab validation。[p.9, Table 5, explicit, “physics-based constraints / model-based constraints”]
7. **TGM baseline**：Table 6 的 time/step 为 CD 18.5、sCM 38.1、ECM 11.6、TGM 11.6 s；success rate 为 CD 25.6↓、sCM `-`、ECM 75.7↑、TGM 77.5↑。CD 训练 collapse，sCM 长序列 OOM，作者后续以 ECM 作为 prior generic consistency 代表。[p.9, Table 6, explicit, “TGM yielding the largest performance gains”]
8. **训练动态与数值误差**：Figure 5 显示 ECM 的梯度方差和 staircase-like loss pattern 更明显，TGM 曲线较平衡；Figure 4 显示 Euler relative error 在训练早期较大，随后降低且整体保持 low。两图是机制诊断，不是独立精度检验；作者用它们支持 fixed temporal distance 和 one-step Euler 的解释。[p.9–10, §§4.4, explicit, “balanced gradients”]
9. **结构与 binder 定性案例**：Figure 6 展示三个 PDB ID 的 Experimental/AF3/DCFold 叠加结构；Figure 7 展示四个 binder-target complex。它们传达几何相似和界面示例，未给出案例选择规则或逐例数值，不能替代 benchmark 统计。[p.14, Figures 6–7, layout_observation, “Experimental result AlphaFold 3 DCFold”]
10. **追加 runtime 与 sample count**：Appendix Table 7 显示短序列最大约 24×，中长序列仍超过 7.7×；Table 8 的 BindCraft/DCFold samples 分别为 IL-2Rα 312/375、TrkA 243/256、H3 269/295、VirB8 347/439、ALK 188/177、LTK 348/402。runtime 结论只给平均时间，sample count 显示各 target 生成量并不完全相等。[p.17–18, Appendix C, explicit, “up to a 24× speedup”]

**统计边界**：论文主要报告均值、比例、类别聚合、最好/最坏阈值比例和训练曲线。没有 conventional significance test、bootstrap、Bayesian model、回归或相关性分析；Table 4 使用 `mean ±` 格式，但未说明是标准差还是其他离散量。图注大多能独立说明比较对象，Figure 3 的 NFE 柱和 Figure 5 的阴影需结合正文读取。显著性、实质差异和机制证据通过定量表、曲线和定性解释分开承担，但没有 uncertainty quantification。

## H. 消融、负面结果与自我设限

### H.1 消融与机制识别

| 类型 | 对象与识别目标 | 证据 |
|---|---|---|
| 组件删除/部分蒸馏 | AF3 ODE → AF3 TGM → DCFold，对应先加入 TGM diffusion consistency，再加入 Pairformer consistency；Figure 3 比较 NFE、lDDT 与 cycles | p.6–8, §§4.1/4.1 Figure 3, explicit, “isolating the contribution of TGM” |
| NFE/cycle 敏感性 | Figure 3 将 Pairformer cycles 与 Diffusion NFE 并列，区分 1-step、2-step 与 AF3 完整配置 | p.8, Figure 3, layout_observation, “Pairformer Cycles” |
| 调度 baseline | CD、sCM、ECM、TGM 的 time/success；识别 TGM 相对通用 CM schedule 的增益 | p.9, Table 6, explicit, “Only ECM and TGM are able to enhance” |
| 机制替代解释 | ECM/TGM gradient norm 与 loss curve，检验训练平滑性和 variable-length 难度是否被平衡 | p.9–10, Figure 5, explicit, “large gradient variance” |
| 数值误差 | TGM 的 one-step Euler `r(t,u)` relative error 随 `t,u` 变化，检验高阶 solver 是否必要 | p.9, Figure 4, explicit, “error remains consistently low” |
| 多样性 robustness | 5 samples、15 samples、5 seeds × 1 sample，检查加大采样是否改善 diversity | p.8, Table 4, explicit, “neither ... exhibited meaningful improvements in diversity” |
| 计算成本 | Table 7 按 token bins 给 AF3/DCFold time，识别长度增长时 Pairformer bottleneck 的变化 | p.17, Appendix C.1, explicit, “Pairformer component becomes the dominant cost” |
| 失败案例 | CD training collapse、sCM OOM；不是把失败值隐藏为成功率 | p.9, §4.4 footnote, explicit, “training collapse” |

消融证据是**部分闭合**：Figure 3 同时含模型、NFE 和 cycle 对照，但没有一张独立的 full factorial 表把 `Diffusion Consistency only` 与 `Pairformer Consistency only` 的所有组合列出。TGM 的训练动态和 Euler 误差有可视化机制证据，仍缺少不同 sequence-length 分层的数值统计和重复 run。

### H.2 自我设限

- **`scope`**：结构训练/评测受 post-2021 PDB、PoseBusters V2 与 Low Homology Recent PDB 约束；binder 仅六个 target。[p.7–9, explicit, “six representative entries”]
- **`assumption`**：Proposition 2 依赖 classical Gaussian conditional `pt(x|x0)`，EDM 特化还使用 `α(t)=1` 等设定；这不是对任意 protein diffusion trajectory 的无条件结论。[p.5, §3.3, explicit, “classical setting”]
- **`compute`**：sCM 长序列 OOM，无法进入公平 Table 6 比较；TGM 的 Euler 近似虽被 Figure 4 检查，早期 error 较大。[p.9, footnote and Figure 4, explicit, “OOM errors”]
- **`data`**：没有 wet-lab binder validation，binder 结果是 in silico filters 下的 success rate；生成 sample 数量按 target 不同。[p.8–9、p.17–18, explicit, “in silico success rates”]
- **`metric`**：PoseBusters 用 ligand RMSD 阈值、Recent PDB 用 TM-score/SR/lDDT，binder 同时报告 AF2 model-based 与 Rosetta physics-based constraints；指标之间不构成同一效用量。[p.7–9, explicit, “two constraint sets”]
- **`baseline`**：DCFold 与 AF3/Protenix 生态比较；CD/sCM/ECM 的可运行性受具体配置和 OOM 影响。[p.6–7、p.9, explicit, “feasible generic consistency-model baselines”]
- **`generality`**：TGM 被表述为 general/scalable，但实验只覆盖蛋白/复合物与 EDM；没有图像或其他 variable-size modality 的迁移实验。[p.5, §3.3, explicit, “general and scalable distillation framework”]
- **`causality`**：训练动态支持机制解释，却没有随机化或统计检验来隔离所有 schedule 与 architecture 影响。[p.9–10, interpretation, “corroborates our hypothesis”]
- **`deployment`**：Binder hallucination 采用连续 48 小时、单 H800 的特定 pipeline；不能直接外推到实验室筛选吞吐或湿实验成功。[p.8、p.17, explicit, “single H800 GPU”]
- **独立章节状态**：PDF 没有名为 `Limitations` 的章节；限制通过引言问题、§4.2 diversity conditionality、§4.4 OOM/early Euler error、附录配置和结论边界分散出现。[p.10–11, layout_observation, “6 CONCLUSION”]

### H.3 不利信息呈现策略

- **位置延后**：先在 §4.2 给出 “strong diversity and confidence” 的正面结论，随后才说明 15 samples 和多 seeds 没有 meaningful diversity improvement。[p.8, §4.2, explicit, “neither AlphaFold3 nor DCFold exhibited meaningful improvements”]
- **分母聚合与异质性**：Table 5 把六 target 的两类 success rate 与平均值放在同一行。正文突出 majority targets 与平均 `.29/.78`，而 IL-2Rα、ALK 的 physics-based rate 低于 BindCraft，异质性留在表格中。[p.9, Table 5, layout_observation, “across the majority of targets”]
- **基线不可运行**：sCM 的 `-` 与 OOM footnote 明示缺失值，作者随后只把 ECM 作为 prior representative；这限制了 schedule 横向比较范围。[p.9, Table 6 and footnote, explicit, “preventing it from participating in a fair comparison”]
- **附录迁移**：binder 过滤阈值、ProteinMPNN/AF2/Rosetta 流程、runtime bins、sample counts 和 target metadata 均移到 Appendix B/C，正文通过 B.2/C.2 调用。主文可以读懂任务目标，但复现 success rate 需要附录。[p.8–9、p.16–18, explicit, “Additional details are provided in Appendix B.2”]
- **代表性案例**：Figure 6/7 只展示三个结构 case study 和四个 binder complex，没有给出选择规则或失败案例；它们承担几何直观，不能承担总体效果量。[p.14, Figures 6–7, layout_observation, “Examples from binder-design experiments”]
- **语气弱化**：Table 4 的结论使用 “no substantial deviation”“slight decrease/increase”，将变化描述为轻微；表格仍保留 `±` 数值，但离散量定义缺失。[p.8, §4.2, explicit, “no substantial deviation”]

## I. 结论、闭环与包装

### I.1 Conclusion 段落

§6 只有一段，按 `重述问题 → 重述方法 → 回收结果 → 影响` 推进。它回收 Dual Consistency、TGM、single-step sampler、variable-length stability、up to 15×、structure prediction 与 binder design，并提出把 AF2 efficiency 与 AF3 accuracy 桥接到 scalable differentiable protein design。没有新增数字，没有单独列 future work，没有独立 limitation 段。[p.10, §6 Conclusion, explicit, “reducing inference cost by up to 15×”]

### I.2 Claim closure matrix

| 主张来源 | 方法回应 | 实验证据回应 | 结论回收 | 状态 |
|---|---|---|---|---|
| AF3 两个迭代瓶颈可同时消除 | Diffusion Consistency、Pairformer Consistency、单次 forward 的内部 cycle 表征、Figure 2、Eq. (2)–(3) | Figure 1、Figure 3、Table 7 的 NFE/cycle/time；没有 full cost decomposition 表 | §6 回收 dual-consistency distillation 与 single-step sampler | `partially_closed`：双组件方向有证据，完整 attribution 和所有长度层级仍不足 |
| DCFold 达到 AF3-level accuracy 并加速约 15× | one-step sampler、两阶段训练、Table 1、TGM | Table 2/3、Figure 3、Figure 1/7；未报告显著性、样本量完整表和 uncertainty | §6 回收 accuracy 与 up to 15× | `partially_closed` |
| TGM 解决 variable-length schedule 失配 | temporal manifold、Fisher metric、KL proposition、Euler schedule、Algorithm 1 | Table 6、Figure 4、Figure 5；支持 success、gradient/loss 和数值误差，但无 formal convergence/stability theorem | §6 回收 stable training | `partially_closed`：局部理论与诊断实验闭合，普遍稳定性未闭合 |
| Dual Consistency 改善 worst-case/输出分布 | Pairformer/Diffusion consistency losses 与加权策略 | Table 2 worst RMSD、Table 3 SR、Figure 3；best-case 变化较小 | §6 以 accuracy/usability 概括，未直接回收 distribution tightening | `partially_closed` |
| DCFold 保持 diversity/confidence | 无额外结构，沿用 AF3 输出接口 | Table 4 5/15/seeds；只覆盖 PoseBusters V2，`±` 定义未说明 | Conclusion 未回收 diversity | `partially_closed` |
| DCFold 能用于 binder hallucination 并提高 screening success | 可微单次模型、AF2 confidence + Rosetta filters、BindCraft pipeline | Table 5 六 targets、Figure 7、Appendix B.2/C.2；没有 wet-lab | §6 回收 downstream usability 与 differentiable design | `partially_closed`：in-silico 闭合，外部实验效用未检验 |
| lightweight architecture 确保 feasible gradient propagation | Figure 2 和 one-step Pairformer 设计 | binder 成功率与 pipeline 可运行，未报告梯度 memory/time 或反向稳定度独立测量 | §6 以 differentiable protein design 概括 | `partially_closed` |

## J. 附录职责

| 一级模块 | 页码 | 类别 | 对象与正文调用 |
|---|---:|---|---|
| Figure 6/7 case studies | 14 | `qualitative_example` | Figure 6 三个结构对照，Figure 7 四个 binder-target 示例；Figure 7 在 p.9 被正文调用，Figure 6 未见正文调用 |
| A.1 Proof of Local Metric-KL Equivalence | 14–15 | `proof` | 证明 Proposition 1；正文明确调用 “Appendix A.1” |
| A.2 Temporal Fisher Information in EDM | 15–16 | `extended_method`、`proof` | 展开 Gaussian conditional、Eq. (17)–(22)；正文以 Eq. (8) 使用其解析形式 |
| B.1 Training Configuration | 16 | `implementation_detail`、`reproducibility` | 给出 64 H800、batch 64、9,000/1,500 steps；正文 Reproducibility Statement 宣称训练细节在 §§3.2–3.3，但实际资源和时长在 B.1 |
| B.2 Binder Hallucination | 16 | `implementation_detail`、`hyperparameter` | ProteinMPNN、AF2、Rosetta、阈值；§4.3 明确调用 B.2 |
| B.3 Hyperparameter Settings for Consistency Model Baselines | 17 | `hyperparameter` | CD/sCM/ECM/TGM 参数和 EDM schedule；§4.4 明确调用 B.3 |
| C.1 Runtime Characteristics Across Sequence Lengths | 17 | `additional_result`、`robustness` | token bins、Table 7、长度与瓶颈解释；表格主要在附录承担 runtime 细分 |
| C.2 Binder Hallucination | 17–18 | `additional_result`、`implementation_detail` | 单 H800 GPU time、Table 8 sample count、Table 9 target metadata；§4.3 明确调用 C.2 |
| The Use of Large Language Models (LLMs) | 17–18 | `other` | 仅用于 spelling correction/minor grammar，声明没有参与研究构思或代码开发；属于论文包装与透明度声明 |

附录约 1,593 个自动词元，物理页 5 页；主文 p.1–10 约 5,190 个自动词元。附录承担 proof、Gaussian/EDM derivation、训练/过滤复现细节、runtime 长度分析、sample counts 和 target metadata。正文仍保留 Equation (4)–(8)、Algorithm 1、主要 benchmark 定义、Table 2–6 和 Figures 1–5，因而决策主线可自足；binder 的过滤阈值、训练硬件和 success rate 的运行语境依赖 B/C 才能复现。Appendix A.1 对 Proposition 1 的证明依赖明确，Appendix A.2 对 Eq. (8) 的展开有帮助，但没有把新主结果放在附录后再回填正文。

## K. 用词与修辞

词频采用主文 p.1–10 的文本代理，排除页眉、页码、References、公式碎片和大部分 caption/table 行。自动 token 仍由仓库统一计量，以下标注用于解释语境。

- **高频实词**：`alphafold` 61、`dcfold` 53、`consistency` 49、`diffusion` 46、`training` 32、`protein` 26、`tgm` 26、`pairformer` 25、`accuracy` 20、`design` 19、`performance` 18、`model` 16、`step` 15、`prediction` 14、`sampling` 14、`binder` 13、`success` 13、`temporal` 13、`distribution` 12、`time` 12。
- **高频二元词组**：`dual consistency` 13、`diffusion consistency` 8、`pairformer consistency` 7、`success rate` 7、`structure prediction` 7、`diffusion module` 7、`temporal geodesic` 6、`geodesic matching` 6、`binder design` 5、`diffusion acceleration` 5、`fisher information` 4、`output distribution` 4、`computational overhead` 3、`foundation model` 3。
- **高频三元词组**：`temporal geodesic matching` 6、`geodesic matching TGM` 5、`dual consistency framework` 3、`protein structure prediction` 3、`alphafold-level accuracy` 3、`temporal information manifold` 2、`temporal fisher information` 2、`protein modeling tasks` 2。
- **主张动词次数**：`we propose` 4、`we observe` 5、`we introduce` 4、`we evaluate` 3、`we report` 3、`we find` 2、`we identify` 2、`we conduct` 2、`we present` 2、`we validate` 2、`we demonstrate` 1、`we compare` 1、`we show` 0。
- **限定与对比词**：`while` 16、`however` 4、`although` 1、`typically` 2、`substantially` 6、`notably` 2、`particularly` 2、`effectively` 3、`therefore` 2。高频限定词主要围绕效率/准确率权衡、输出分布、长序列和实验解释。
- **修辞判断**：高频词由模型组件名、任务指标和 TGM 机制驱动，`et al.` 等引用碎片不代表论证动作。强主张集中于 `achieves/attains/matches/surpasses/substantially improves`，弱化表达集中于 `approximately correct`、`no substantial deviation`、`slight`、`comparable`。摘要和结论使用较强的 capability 句式，§4.2 和附录用较弱的 scope/uncertainty 句式。

## L. 最终判断

1. **单一主线**：先把 AF3 的 diffusion 与 Pairformer 两个循环瓶颈拆开，再分别以 diffusion consistency 和 cycle consistency 蒸馏；TGM 用 Fisher/KL 几何按 temporal information distance 配对 variable-length 序列，最后以结构准确率、速度、训练动态和 binder hallucination 检验单次前向的可用性。[p.3–10]
2. **正文保留的决策内容**：Figure 1/2、Table 1–6、Algorithm 1、Eq. (1)–(8)、PoseBusters/Recent PDB/binder 任务定义、worst-case RMSD、TM-score/SR/lDDT、TGM baseline 和训练曲线。它们共同回答效率、结构质量、组件作用、调度机制和下游 utility。[p.3–10]
3. **移入附录的细节与自足性**：证明、Gaussian/EDM 解析推导、训练资源/时长、binder 过滤阈值、runtime bins、sample counts、target metadata 和定性案例在 p.14–18。正文可理解方法和主结果，但复现 binder 和训练成本需要 Appendix B/C；理论局部等价性的可检查细节需要 A.1。[p.14–18]
4. **最有效模式**：Figure 2 的双瓶颈流程图、Table 1 的两阶段 loss 契约、Figure 3 的 NFE/cycle/lDDT 并置，以及 Table 2 的 best/worst RMSD 分拆。它们把架构、训练信号、尾部可靠性和精度放在同一条证据链上。[p.3–8]
5. **最大缺口**：15× 和 AF3-level accuracy 的总体表述缺少完整样本量、重复 seed、不确定性和显著性；binder 只有六个 in-silico targets，没有 wet-lab；TGM 的稳定性理论只在局部 Fisher/KL 与 Gaussian/EDM 设定下给出，实验动态没有长度分层或 formal convergence。sCM OOM 也使 schedule baseline 横向比较不完整。[p.5、p.8–10、p.16–18]
6. **可迁移规则**：压缩含多个推理循环的科学模型时，先为每个循环建立独立 consistency target，再用与数据维度或轨迹内在距离匹配的 schedule；评测同时报告平均精度、尾部失败、真实推理成本、机制诊断和下游任务。[p.3–10]
7. **适用边界**：该规则适合存在可复用中间表征、可区分 denoising/recycle depth 的 diffusion-plus-recycle 模型。Fisher/KL 推导依赖平滑分布和 classical Gaussian/EDM 假设；binder 结论只覆盖六个目标与 in-silico filtering，不能替代更广泛数据或实验验证。[p.5、p.8、p.15–18]

## 提交核对

- [x] 18 个 PDF 物理页已读，包括 p.11–13 references、p.14–18 appendix、Figures 6–7、Tables 7–9。
- [x] 12 个固定 `module_metrics` 各出现一次；`theory` 与 `limitations` 的分工已在页级地图说明。
- [x] 编号公式 Eq. (1)–(22) 已逐项核对；另记录 p.4 未编号 `Lconfidence` 展示式；理论 inventory 按 schema 计 3 项。
- [x] 图表手工计数为 7 figures、9 tables、1 algorithm，并记录自动计量差异。
- [x] 统计单位、分母、均值/比例、`±` 未定义、OOM、失败训练、sample count 和案例图定位已记录。
- [x] 所有结构化证据使用 PDF 物理页、section、短 anchor；缺失项保持显式缺失状态。

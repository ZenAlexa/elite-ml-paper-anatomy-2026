# 单篇深读：Decoupling The “What” and “Where” With Polar Coordinate Positional Embedding

## 0. 读取边界与身份

- `paper_id`：`icml-2026-cca969cd8cab`
- 会议与等级：ICML 2026，`spotlight`。论文首页标注 Proceedings of the 43rd International Conference on Machine Learning、PMLR 306（PDF p. 1，版面事实）。
- 论文身份：Anand Gopalakrishnan、Robert Csordás、Jürgen Schmidhuber、Michael C. Mozer；OpenReview forum `I3Z9za1EkO` 与目录标题一致（PDF p. 1；目录元数据）。
- 事实源为 `corpus/preprints/icml-2026-cca969cd8cab.pdf`。PDF 为 arXiv:2509.10534v3，日期 8 Jun 2026；读取了 PDF 全部 18 个物理页。`corpus/preprint_text/icml-2026-cca969cd8cab.txt` 仅用于定位文字，所有判断以 PDF 版面为准。
- supplementary：未提供独立 supplementary 文件；论文附录 A–D 已嵌入同一 PDF（PDF pp. 12–18）。

## 1. 页级地图与版面边界

### 1.1 物理页分区

| 区段 | 物理页 | 估计词数 | 语义模块 | 说明 |
|---|---:|---:|---|---|
| Abstract | 1 | 169 | `abstract` | 左栏；右栏同时开始引言。 |
| 1. Introduction | 1–2 | 500 | `introduction` | 第 1 页右栏和左栏下部开始，末句跨至 p. 2 顶部。 |
| 2. Background | 2 | 500 | `theory` | RoPE 记号、极坐标展开和 confound 机制；标题是 Background，按功能映射为理论模块。 |
| 3. Method | 2–4 | 700 | `method` | PoPE 定义、可学习偏置、Triton 实现与成本。 |
| 4. Results | 4–8 | 1,970 | `experimental_design` + `results` + `ablation` | 结果章节跨多页、多栏；实验设计与结果以语义边界拆分。 |
| 5. Related Work | 6–8 | 900 | `related_work` | 独立章节，含 “RoPE and its extensions” 与 “Alternative positional embeddings” 两个小标题。 |
| 6. Conclusion | 8 | 124 | `conclusion` | 右栏下部。 |
| Impact Statement | 9 | 142 | `limitations` | 位于 References 之前；包含适用影响与 dual-use 自我设限。 |
| References | 9–11 | 1,428 | `other` | p. 9 右栏及 p. 10–11；不计入正文比例。 |
| A. Method Details | 12–13 | 427 | `appendix` | A.1 推导、A.2 FLOPs。 |
| B. Experimental Details | 13–15 | 896 | `appendix` | 数据集、模型、训练配置。 |
| C. Additional Results | 15 | 132 | `appendix` | Indirect Indexing 的额外位置编码基线。 |
| D. Additional Visualizations | 16–18 | 249 | `appendix` | 253M 频率使用和 δ 可视化。 |

PDF 共 18 页；主文物理页为 1–8（8 页），References 为 9–11（3 页），附录为 12–18（7 页）。页 9 的 Impact Statement 位于 References 标题之前，因此在语义计量中单列为 `limitations`。估计词数按 PDF 版面文字的正则词数并人工按栏、公式、表格和图注归属；主文分母为约 4,863 个版面词元，包含必要的标题、图表文字和公式碎片，属于可复核的近似量，不是出版社的自然语言词数。

### 1.2 版面观察

- 主文与 References 使用双栏；公式在栏内居中，Figure 1（p. 3）、Figure 2（p. 7）和 Figure 3（p. 8）占跨栏区域，压缩了相邻正文的可读面积（PDF pp. 3、7、8；`layout_observation`）。
- p. 1 的 Abstract 位于左栏上部，引言从右栏上部开始，导致引言首段跨栏且跨页；按语义而非物理栏切分（PDF p. 1；`layout_observation`）。
- 附录 A–D 为单栏排版，公式推导、数据集描述、超参数表和可视化均有较大可读面积；p. 18 基本由 Figure 7 和图注构成（PDF pp. 12–18；`layout_observation`）。
- PDF 未标注 tagged/accessibility 结构，正文无独立 “Limitations” 小节；Impact Statement 承担该模块的显式边界说明（PDF pp. 1、9；`layout_observation`）。

### 1.3 12 模块计量

| 模块 | 状态 | 估计词数 | 主文词份额 | 图 | 表 | 算法 | displayed equations |
|---|---|---:|---:|---:|---:|---:|---:|
| `abstract` | observed | 169 | 3.5% | 0 | 0 | 0 | 0 |
| `introduction` | observed | 500 | 10.3% | 0 | 0 | 0 | 0 |
| `related_work` | observed | 900 | 18.5% | 0 | 0 | 0 | 0 |
| `method` | observed | 700 | 14.4% | 1 | 0 | 0 | 8 |
| `theory` | observed | 500 | 10.3% | 0 | 0 | 0 | 2 |
| `experimental_design` | observed | 450 | 9.3% | 0 | 0 | 0 | 0 |
| `results` | observed | 1,350 | 27.8% | 2 | 5 | 0 | 0 |
| `ablation` | observed | 170 | 3.5% | 0 | 1 | 0 | 0 |
| `conclusion` | observed | 124 | 2.5% | 0 | 0 | 0 | 0 |
| `limitations` | observed | 142 | — | 0 | 0 | 0 | 0 |
| `appendix` | observed | 1,704 | — | 4 | 3 | 0 | 16 |
| `other` | observed | 1,428 | — | 0 | 0 | 0 | 0 |

主文九个模块的估计词数合计 4,863，份额合计 100%。`theory` 使用 Background 的功能归属；`experimental_design`、`results` 和 `ablation` 从 Section 4 内部拆分。没有单独的伪代码或算法环境（PDF pp. 2–8；`layout_observation`）。

## 2. Abstract 逐句功能编码

| # | 原句 | 词数 | 功能 | 限定词、数字、比较对象 | 证据 |
|---:|---|---:|---|---|---|
| 1 | The attention mechanism in a Transformer architecture matches key to query based on both content—the what—and position in a sequence—the where. | 24 | `object_scope` | “both”并列 what/where；无数字。 | p. 1, Abstract；`explicit` |
| 2 | We present an analysis indicating that what and where are entangled in the popular Rotary Position Embedding (RoPE). | 18 | `problem_gap` | “indicating”弱化分析结论；对象为 RoPE。 | p. 1, Abstract；`explicit` |
| 3 | This entanglement can impair performance particularly when decisions require independent matches on these two factors. | 15 | `problem_gap`, `limitation` | “can”“particularly”限定失败条件；独立匹配 what/where。 | p. 1, Abstract；`explicit` |
| 4 | We propose an improvement to RoPE, which we call Polar Coordinate Position Embedding or PoPE, that eliminates the what-where confound. | 20 | `core_idea`, `method` | “propose”；方法名 PoPE；主张消除 confound。 | p. 1, Abstract；`explicit` |
| 5 | PoPE is far superior on a diagnostic task requiring indexing solely by position or by content. | 16 | `qualitative_result` | “far superior”；对象为 Indirect Indexing 类诊断任务，摘要未给数值。 | p. 1, Abstract；`explicit` |
| 6 | On autoregressive sequence modeling in music, genomic, and natural language domains, Transformers using PoPE as the positional encoding scheme outperform baselines using RoPE with respect to evaluation loss (perplexity) and downstream task performance. | 33 | `experimental_setup`, `qualitative_result` | 三类域；比较 PoPE/RoPE；指标为 perplexity 与 downstream performance。 | p. 1, Abstract；`explicit` |
| 7 | On language modeling, these gains persist across model scale, from 124M to 774M parameters. | 14 | `quantitative_result` | 124M–774M；未列具体差值。 | p. 1, Abstract；`explicit` |
| 8 | Crucially, PoPE shows strong zero-shot length extrapolation capabilities compared not only to RoPE but even a method designed for extrapolation, YaRN, which requires additional fine tuning and frequency interpolation. | 29 | `quantitative_result`, `limitation` | “strong”“Crucially”；比较 RoPE、YaRN；指出 YaRN 的 fine-tuning/interpolation 条件。 | p. 1, Abstract；`explicit` |

摘要共 8 句、约 169 词。功能顺序为「对象与双因素 → RoPE 缺口 → 失败条件 → PoPE 核心 → 诊断结果 → 跨域结果 → 跨规模结果 → 长度外推比较」。它报告了方向性结果和一个规模范围，但没有给表格数值、不确定性或形式定理。最强主张放在末句：零样本长度外推优于 RoPE，并与需要额外处理的 YaRN 比较（p. 1；`interpretation`）。

## 3. Introduction 的论证推进

引言为四个自然段，约 500 词；没有单独的项目符号式 contribution list。下表按“上一段问题、当前回答、下一段钩子”记录。

| 段 | 页码 | 动作 | 估计词数 | 上一段留下的问题 | 当前回答与下一段钩子 | 证据 |
|---:|---:|---|---:|---|---|---|
| 1 | 1 | `context` | 104 | 顺序或位置编码为何重要尚未展开。 | 回顾早期序列任务，并引出 RNN 与 slot-based encoding 的历史分化。 | p. 1, §1；“prehistory of deep learning… sequential or position-coded data”；`explicit` |
| 2 | 1 | `context`, `failure_of_prior_work` | 121 | 两类早期表示各自怎样处理位置与迁移。 | 对照 RNN 的近似 translation equivariance 与 slot 表示的跨 slot 泛化困难；引出 Transformer。 | p. 1, §1；“RNNs… approximate translation equivariance”；`explicit` |
| 3 | 1 | `problem`, `context` | 126 | Transformer 的 slot/self-attention 组合如何保留相对位置。 | 说明基本 Transformer 具有 translation/permutation invariance，同时需要注入 relative positions；承认 what 与 where 都必要。 | p. 1, §1；“translation and permutation invariant… relative positions”；`explicit` |
| 4 | 1–2 | `missing_insight`, `core_idea`, `method_preview`, `result_preview`, `scope_boundary` | 149 | 现有位置编码同时携带内容和位置时是否会产生不必要耦合。 | 指出 RoPE 的 phase interaction，提出 PoPE 的 what/where conjunction，并预告 data efficiency、asymptotic accuracy、context-length generalization。 | pp. 1–2, §1；“conjunction of a what match and a where match”；`explicit` |

完整推进链为：历史背景 → 早期表示的迁移性差异 → Transformer 的位置敏感性缺口 → RoPE 的 entanglement → PoPE 的解耦预告 → 跨任务与长度泛化预告。最后一段重复了摘要中的核心方法和结果方向；它提供了“data efficiency / asymptotic accuracy / context-length generalization”三项较强但未数字化的主张，也没有给出明确限制或可证伪阈值（pp. 1–2；`interpretation`）。

## 4. Related Work

### 4.1 位置与组织

Related Work 是独立的 Section 5，跨 pp. 6–8；可见两个小标题，共约 900 词、7 个引用簇。它没有另设方法综述表，而是以叙述方式比较。

| 段/簇 | 动作 | 比较维度 | 证据 |
|---|---|---|---|
| RoPE 及扩展（簇 1–2） | `taxonomy`, `chronology`, `nearest_neighbor_contrast` | 训练长度与外推；频率缩放、插值、fine-tuning、block-wise masking、整数波长。 | pp. 6–7, “RoPE and its extensions”；Chen et al., YaRN, LongRoPE, Sun et al., Resonance RoPE；`explicit` |
| 无显式位置与早期相对编码（簇 3–4） | `chronology`, `credit_or_foundation` | 无位置编码的长度泛化与分布内代价；inverse-time、relative key、offset encoding、complex-valued encoding。 | p. 7, “Alternative positional embeddings”；Schmidhuber、Irie、Shaw、Music Transformer、Transformer-XL、Wang et al.；`explicit` |
| T5/ALiBi/CosFormer（簇 5–6） | `nearest_neighbor_contrast`, `limitation_of_prior` | scalar decay 与 per-component frequency weighting；远距离衰减与精确位置模式。 | pp. 7–8；“single scalar decay… per-component (per-channel)”；`explicit` |
| Geometric/stick-breaking attention（簇 7） | `positioning_only`, `credit_or_foundation` | 替代 softmax 或显式位置的不同路线及其长度泛化主张。 | pp. 7–8；Csordás et al.、Tan et al.；`explicit` |

相关工作避免完整重复 PoPE 推导；PoPE 只在 CosFormer 对比处被放回“每通道、多频率、可形成精确位置模式”的定位。引用在后文继续承担论证：RoPE/YaRN 出现在外推实验，Barbero et al. 出现在频率使用分析，数据集与模型引用出现在实验设计（pp. 5–8；`explicit`）。

## 5. Method 与 theory

### 5.1 最小逻辑单元

| # | 动作 | 内容 | 解决的前文问题 | 证据 |
|---:|---|---|---|---|
| 1 | `setup_notation` | 将 query (q_t)、key (k_s) 设为 d 维向量，并按 d/2 个二维块旋转；定义 component-specific θ。 | 使 RoPE 的 what/where 关系可代数化。 | p. 2, §2；Eq. (1) 前；`explicit` |
| 2 | `derive` | 得到 RoPE attention score 的 relative-rotation 形式。 | 表明绝对位置被约化为 (s-t)。 | p. 2, Eq. (1)；`explicit` |
| 3 | `derive` | 将二维块改写成 magnitude/phase，得到 φᵏ−φᑫ interaction。 | 定位 what 与 where 的耦合项。 | p. 2, Eq. (2)；`explicit` |
| 4 | `explain_mechanism`, `connect_to_prediction` | 明确 key/query 的特征存在性和相对位置被同时调节，提出删除 interaction term 的 hypothesis。 | 解释 Indirect Indexing 与长度外推的预测方向。 | p. 2, §2；“removing the interaction term”；`explicit` |
| 5 | `define_component` | PoPE 将每个原始 real-valued 元素映射到 Cᵈ 的 magnitude，用 softplus σ(x)=ln(1+eˣ) 保证非负。 | 把内容强度与相位分开。 | p. 2, Eq. (3)；`explicit` |
| 6 | `define_component` | phase 只依赖位置：φ(k̃ₛ,꜀)=sθ꜀、φ(q̃ₜ,꜀)=tθ꜀，频率数从 d/2 增至 d。 | 去除 key/query phase interaction，并提高频率通道数。 | p. 2, Eq. (4)；p. 3；`explicit` |
| 7 | `derive`, `contrast_alternative` | 用 Re[q̃ₜᴴk̃ₛ] 得到仅含 cos((s−t)θ꜀) 的 score；逐元素索引且无 interaction。 | 形式化“what match × where match”的可分结构。 | p. 2, Eq. (5)；p. 3；`explicit` |
| 8 | `define_component`, `connect_to_prediction` | 增加固定但可学习的 δ꜀，将 relative offset 调为每个频率的最优值。 | 恢复可调的频率相位偏移，但不让 key/query 内容动态改写相位。 | p. 3, Eq. (6)；`explicit` |
| 9 | `instantiate_algorithm` | δ꜀=0 或 Uniform(−2π,0) 初始化，并限制在 [−2π,0]；作者称 zero init 有利于长度泛化，uniform 略利于分布内表现。 | 处理初始化与长度外推的稳定性。 | p. 3, §3；`explicit` |
| 10 | `instantiate_algorithm`, `derive` | Triton/Flash Attention 2 kernel 在 Cartesian form 中直接算复积实部；Eq. (7)–(10) 给出实虚部和高效 score。 | 使复数表示可落地，不物化 query-key 复矩阵。 | pp. 3–4, “Efficient Implementation”；`explicit` |
| 11 | `state_complexity`, `contrast_alternative` | 选用较慢的通用实现；理论上只有一次额外乘法，但所选实现对 complex-valued keys/values 使用两倍 memory/bandwidth；可在 kernel 内旋转以消除内存开销。 | 暴露 PoPE 的工程成本和未采用的优化。 | p. 4, Eq. (10) 后；`explicit` |

方法动作转移为：`setup_notation → derive → derive → explain_mechanism → define_component → define_component → derive → contrast_alternative → instantiate_algorithm → derive → state_complexity`。核心因果链在 Eq. (2) 的 interaction 诊断与 Eq. (5) 的删除之间闭合；δ、Cartesian kernel 与 FLOPs 属于可实现性和成本层，而非新的机制假设（pp. 2–4；`interpretation`）。

### 5.2 理论对象、公式与可证明性质

- 编号公式共 16 个。正文为 Eq. (1)–(10)，附录 A.1 为 Eq. (11)–(16)；另有 10 个未编号 display：A.1 的 polar form 与 rotation matrix 两个，A.2 的四个 FLOPs 行、一个 overhead ratio、三个长度实例。全 PDF displayed equations 估计 26 个（PDF pp. 2–4、12–13；`layout_observation`）。
- 正式 theorem、lemma、proposition、corollary 均为 0。A.1 是代数推导，不是带假设域和结论边界的定理；A.2 是 FLOPs bookkeeping。理论角色为 `core_chain`（Eq. 1–6）、`explanation`（Eq. 7–16）和 `diagnostic`（FLOPs），没有独立的性能保证（PDF pp. 2–4、12–13；`explicit`）。
- A.2 在 (r=4) 下给出 PoPE 相对 Transformer layer 的额外 FLOPs 比例 (L/(12d+2L))。对 774M、(d=1280)，(L=1024/2048/4096) 时分别为 5.882%、10.526%、17.391%；这些是代数成本估计，论文未给实测吞吐或端到端延迟（PDF pp. 12–13, A.2；`explicit`）。

## 6. Experimental design

### 6.1 研究问题与控制

| 设计项 | 状态 | 记录 | 证据 |
|---|---|---|---|
| 预先列出的 RQ/假设清单 | `not_present` | 没有编号的 RQ；Background 明确提出“删除 interaction 可提升性能”的 hypothesis。 | p. 2, §2；`explicit` |
| 主控制变量 | observed | 每个实验用两个架构和训练超参数相同的 Transformer，仅改变 positional encoding；decoder-only、causal masking。 | p. 4, §4 开头；`explicit` |
| 归一化与架构 | observed | 使用 RMSNorm 替代 LayerNorm；这是所有实验共同设置。 | p. 4；`explicit` |
| 训练/验证/测试指标 | observed | Indirect Indexing 用 final-token accuracy；音乐与 HRG 用 best test NLL；OpenWebText 用 validation perplexity；下游用 zero-shot accuracy 与六任务平均；PG-19 用 zero-shot perplexity。 | pp. 4–6；`explicit` |
| 随机种子 | observed（范围有限） | 只有 Indirect Indexing 明报 3 seeds 的 mean ± SD；其他表未报 seed 数或不确定性。 | p. 4 Table 1；pp. 5–6 Tables 2–6；`explicit` |
| 数据泄漏控制 | `not_present` | PDF 未说明去重、文档隔离、染色体/书籍泄漏检查。 | pp. 4–6、13–15；`interpretation` |
| 失败判定/停止规则 | `not_present` | 没有预设失败阈值或统计决策规则。 | pp. 4–6、15；`interpretation` |
| 硬件与运行时间 | `not_present` | 给出 Triton 与 FLOPs，但未报告 GPU/CPU、峰值显存、吞吐或 wall-clock。 | pp. 3–4、12–13；`explicit` |
| 复现来源 | observed | p. 3 脚注给出 GitHub `agopal42/pope`；附录给数据集 URL、模型配置与训练配置。 | pp. 3、13–15；`explicit` |

### 6.2 数据集、任务与复现粒度

- **Indirect Indexing**：程序生成长度 20–40、无放回采样的大小写字母串；从串中采 source character，shift 均匀采样 ([-15,+15])，train/validation/test 为 1M/10k/10k；字符级 tokenization，模型只见 target 前的序列。它测试 content 与 relative position 的 pointer arithmetic（PDF p. 13, B.1；`explicit`）。
- **JSB/Bach-Chorales**：四声部、16th-note quantization 的二维矩阵以 raster-scan 序列化，长度 2048，229/76/77 条 train/validation/test，词表 90（PDF pp. 4、13–14；`explicit`）。
- **MAESTRO**：约 200 小时 MIDI/audio；v3.0.0，pitch transposition 从 {-3,…,+3} 均匀抽样，最长 2048，90/5/5 划分，REMI 词表 328（PDF p. 14, B.1；`explicit`）。
- **Human Reference Genome (HRG)**：GRCh38/hg38 的常染色体与性染色体，约 3.2B nucleotides；最大长度 1000、词表 4107，按 Nucleotide Transformer 流程预处理（PDF p. 5、14；`explicit`）。
- **OpenWebText**：训练/验证约 9B/4M tokens，最大预训练长度 1024，GPT-2 tokenizer 词表 50257；模型为 124M/253M/774M（PDF pp. 5、13–15；`explicit`）。
- **PG-19**：Project Gutenberg 的 1919 年前书籍，测试集 100 本、约 7M tokens；用于测试长度外推，测试长度为 1024 的倍数直到 10240（PDF pp. 5、7、14；`explicit`）。

实验顺序为 Indirect Indexing → music → genome → OpenWebText language modeling → downstream tasks → PG-19 extrapolation → frequency usage。该顺序从机制诊断逐步扩展到跨域性能、规模和外推；频率图是事后机制诊断，不能单独识别因果（pp. 4–8；`interpretation`）。人类评测与部署实验对本文模型研究不适用，伦理内容仅在 Impact Statement 中出现。

## 7. Results、统计与可视化

### 7.1 结果清单

| 结果主张 | 证据对象与定量值 | 比较/统计处理 | 作者解释与不利解释 | 证据 |
|---|---|---|---|---|
| Indirect Indexing 上 PoPE 几乎解决任务 | Table 1：RoPE (11.16\pm2.45)，PoPE (94.82\pm2.91)；从表值计算差 83.66 个百分点。 | final-token accuracy；3 seeds mean ± SD；无显著性检验。 | 作者称 RoPE 难以拆分 what/where，PoPE 学到可泛化解；单一程序诊断不等于所有任务的机制保证。 | p. 4, Table 1；`explicit` + `interpretation` |
| 音乐 NLL 在两个数据集下降 | Table 2：JSB RoPE 0.5081、PoPE 0.4889；MAESTRO RoPE 1.501、PoPE 1.486。 | best test NLL；无 SD、区间或检验。 | 两个结果方向一致；数据域是作者特意选择的、预期需要精确位置的信息。 | p. 4, Table 2；p. 5；`explicit` |
| HRG NLL 下降 | Table 3：RoPE 4.217、PoPE 4.152；表值差 0.065。 | best test NLL；作者称 “significant drop”，但未给统计方法。 | 支持跨到 genomic 域；单个 genome 数据集且无 seed/不确定性。 | p. 5, Table 3；`explicit` |
| OpenWebText perplexity 跨规模下降 | Table 4：124M 21.55→21.33、253M 18.88→18.55、774M 15.85→15.45；差值分别为 0.22、0.33、0.40。 | validation perplexity；相同模型/训练参数，仅位置编码变化；无 SD/检验。 | 作者称 gap 保持或随规模增大；差值由表值计算，尚未提供跨 seed 方差。 | p. 5, Table 4；`explicit` + `interpretation` |
| 下游平均 accuracy 在三种规模都更高 | Table 6 Avg：124M 45.33→46.19、253M 48.76→48.78、774M 51.80→52.46。 | 六任务平均 accuracy；zero-shot；无不确定性。 | 平均值方向一致，但 253M 仅 +0.02，且 124M/253M 的个别任务出现 PoPE 回退；平均值不能替代任务级决策。 | p. 6, Table 6；`explicit` + `interpretation` |
| 长度外推优于 RoPE 与 YaRN | Figure 2：测试长度为 1024 的倍数至 10240；RoPE 长度增加时急剧上升，YaRN 在超过 4096 后也上升，PoPE 保持低曲线，PoPE+ft 更低。 | PG-19 zero-shot perplexity；图中未标出完整数值或误差；YaRN/PoPE+ft 均在长度 4096 上 fine-tune 500 steps。 | 作者将此归因于 PoPE 不让内容动态移动 frequency tuning；图形是方向证据，精确效应与 seed 稳健性未报告。 | pp. 5–7, Figure 2；`explicit` + `interpretation` |
| 频率使用从稀疏低频转向更广泛高频 | Figure 3：124M 模型的 RoPE/PoPE query/key 热图；PoPE 除第一层外在高频通道有高 norm，频率使用更分散。 | mean over 10 Shakespeare sonnets 和每层 12 heads；无显著性或误差。 | 这是表示使用的描述性诊断；模型规模、训练数据与 Gemma 对比不同，作者承认只能作定性解释。 | p. 6、8, Figure 3；`explicit` |

### 7.2 Table 6 的任务级记录

Table 6 的列为 LAMBADA、BLiMP、CBT、HellaSwag、PIQA、ARC-E、Avg（均为 accuracy，方向为 ↑）。

| 模型 | RoPE（六任务，Avg） | PoPE（六任务，Avg） | 直接观察 |
|---|---|---|---|
| 124M | 28.74, 77.55, 38.80, 29.55, 60.28, 37.08；45.33 | 27.67, 77.75, 44.43, 29.18, 59.58, 38.52；46.19 | PoPE 在 LAMBADA/HellaSwag/PIQA 回退，在其余三项提升。 |
| 253M | 31.38, 79.12, 48.51, 31.47, 62.24, 39.87；48.76 | 30.47, 80.01, 49.39, 31.82, 61.70, 39.32；48.78 | PoPE 在 LAMBADA/PIQA/ARC-E 回退；Avg 仅高 0.02。 |
| 774M | 35.95, 81.05, 52.56, 35.39, 63.55, 42.28；51.80 | 36.89, 82.03, 53.67, 35.86, 63.93, 42.37；52.46 | PoPE 六项均高于 RoPE，Avg 高 0.66。 |

上述“回退/提升”仅是同表配对数值的版面观察；论文只强调三种规模的平均值更高，没有任务级显著性或实质阈值（PDF p. 6；`layout_observation`）。

### 7.3 统计与可视化边界

- 聚合单位是 seed（仅 Table 1 明示 3 seeds）、dataset split、模型规模或 downstream task；Table 6 的 Avg 是六个任务的算术平均，Table 2–4 是单个 split 的 best NLL/perplexity（pp. 4–6；`explicit`）。
- 只有 Table 1 报告 mean ± standard deviation。其余结果无误差条、bootstrap、Bayesian posterior、回归、相关性、p-value 或多重比较校正；Figure 2–7 也未显示误差表达（pp. 4–8、15–18；`explicit`）。
- “significant drop”只出现在 HRG 文字中，统计显著性检验、样本层级和 decision rule 均未给出；因此本报告保留作者措辞，同时将可验证证据限定为 NLL 数值差（p. 5；`interpretation`）。
- 图注通常能独立说明任务、颜色和序列长度；Figure 3 图注对 124M/253M 的覆盖存在文字与图面错位，见第 10 节。表注能说明 split 与指标，但不能独立提供 seed 或不确定性（pp. 4–8、16–18；`layout_observation`）。

### 7.4 图、表和算法清单

| 类型 | 编号 | 模块 | 页码 | 一句话任务 |
|---|---|---|---:|---|
| figure | Figure 1 | `method` | 3 | 对照 RoPE 的二维块/初始 phase 与 PoPE 的 softplus magnitude/位置旋转。 |
| table | Table 1 | `results` | 4 | Indirect Indexing final-token accuracy 与 3-seed SD。 |
| table | Table 2 | `results` | 4 | JSB、MAESTRO 的 best test NLL。 |
| table | Table 3 | `results` | 5 | HRG 的 best test NLL。 |
| table | Table 4 | `results` | 5 | OpenWebText 124M/253M/774M validation perplexity。 |
| table | Table 5 | `ablation` | 5 | softplus、ReLU 替代和 δ 删除的 perplexity。 |
| table | Table 6 | `results` | 6 | 六个 zero-shot 下游任务及平均 accuracy。 |
| figure | Figure 2 | `results` | 7 | PG-19 测试长度 1024–10240 的 RoPE/YaRN/PoPE/PoPE+ft perplexity 曲线。 |
| figure | Figure 3 | `results` | 8 | 124M RoPE 与 PoPE 的 query/key frequency usage heatmap。 |
| table | Table 7 | `experimental_design` | 14 | 各数据集 Transformer model configuration。 |
| table | Table 8 | `experimental_design` | 15 | batch、长度、学习率、AdamW 等训练配置。 |
| table | Table 9 | `ablation` | 15 | Indirect Indexing 的额外位置编码基线。 |
| figure | Figure 4 | `appendix` | 16 | 253M RoPE 的 query/key 频率 norm。 |
| figure | Figure 5 | `appendix` | 16 | 253M PoPE 的 query/key frequency magnitude。 |
| figure | Figure 6 | `appendix` | 17 | 124M 各层 learned δ。 |
| figure | Figure 7 | `appendix` | 18 | 253M 各层 learned δ。 |

全 PDF 无伪代码、无算法编号（pp. 1–18；`layout_observation`）。

## 8. Ablation、负面结果与自我设限

### 8.1 消融与额外基线

Table 5 的主文消融占主文约 3.5%（约 170 词及 1 表）。它在 124M 与 253M 列报告：

| 变体 | 124M | 253M | 识别目标 |
|---|---:|---:|---|
| PoPE without σ() | 21.57 | 18.93 | softplus magnitude 是否贡献。 |
| PoPE with ReLU for σ() | 21.55 | 18.90 | softplus 的具体非线性是否重要。 |
| PoPE without δ | 21.42 | 18.57 | learnable phase bias 是否贡献。 |
| Full PoPE | **21.33** | **18.55** | 完整组件的 validation perplexity。 |

作者将三项组件都描述为性能增益来源，但各差异没有 seed/误差或统计检验；Table 5 caption 称 “124M Transformer model”，同时列出 253M，属于需要保留的版面不一致（p. 5；`explicit` + `layout_observation`）。

附录 C 的 Table 9 将 Indirect Indexing 扩展为位置编码基线：RoPE 11.16 ± 2.45、RoPE half-channels 28.50 ± 6.10、ALiBi half-heads 27.35 ± 10.77、Learnable 10.08 ± 0.19、Sinusoidal 1.90 ± 0.04、PoPE 94.82 ± 2.91。作者解释半通道 RoPE/半头 ALiBi 仍保留 interaction，learnable 与 sinusoidal 约为 10% 与 2% 解题率（p. 15, C；`explicit`）。

### 8.2 负面结果与成本

- RoPE 在 PG-19 长度测试中显著退化；YaRN 在超过 fine-tuning context 4096 后也退化。PoPE+ft 优于零样本 PoPE，说明 fine-tuning 仍能适配低频组件；作者将这一点放在 Figure 2 文字后段（pp. 5–7；`explicit`）。
- Table 6 的 124M 与 253M 个别任务回退，尤其 253M 的平均提升仅 0.02；正文只回收“平均值更高”，没有单独讨论这些任务级差异（p. 6；`layout_observation`）。
- PoPE 的算法 FLOPs 增加为 (2L^2d)；所选通用 kernel 使用两倍 complex-valued key/value memory 与 bandwidth，且作者称其较慢。FLOPs 例子随长度从 5.882% 增至 17.391%（pp. 4、12–13；`explicit`）。
- 频率热图显示的是使用模式，不是对“解耦导致泛化”的独立干预检验；作者也指出与 Gemma 7B 的预训练规模不同，比较只能定性解释（p. 6；`explicit`）。

### 8.3 限制出现位置与编码

| 限制 | 位置 | 编码 | 状态与证据 |
|---|---|---|---|
| 数据域选择偏向预期需要位置/内容分离的任务，语言是否同样满足尚不清楚 | Results 叙述 | `scope`, `generality`, `data` | 作者明确说明选择 music/genome 的理由，并承认 human language less clear（p. 5；`explicit`）。 |
| 复杂度与内存 | Method、Appendix A.2 | `compute`, `deployment` | 额外乘法、两倍 memory/bandwidth、未采用的 kernel 内旋转优化均有明示（pp. 4、12–13；`explicit`）。 |
| 统计不确定性覆盖有限 | Results | `metric`, `causality` | 仅 Table 1 有 3-seed SD；其余表和图未报告方差或检验（pp. 4–8；`explicit`）。 |
| dedicated limitations section | 未出现 | `scope` | `not_present`；Impact Statement 承担社会影响边界，但未列模型/数据/统计限制（p. 9；`layout_observation`）。 |
| 硬件、吞吐、峰值显存 | 未出现 | `compute`, `deployment` | `not_present`；只给 FLOPs 和 memory/bandwidth 方向（pp. 4、12–13；`explicit`）。 |
| 理论保证 | 未出现 | `generality` | `not_present`；只有 RoPE/PoPE 代数等式和 FLOPs，不提供 accuracy/generalization theorem（pp. 2、12–13；`explicit`）。 |
| dual-use 风险 | Impact Statement | `ethics` | 作者称无直接 societal implications，同时列出 foundation-model、deepfake、harmful-content 的潜在风险（p. 9；`explicit`）。 |

### 8.4 不利信息的呈现策略（中性编码）

| 策略 | 可验证表现 | 证据 |
|---|---|---|
| 选择与机制匹配的任务/域 | 作者显式说明 music 与 genome 因“似乎需要”位置—内容分离而被选入；这会把机制支持集中在有利任务上。 | p. 5；`explicit` + `interpretation` |
| 聚合掩盖异质性 | Table 6 只在结论段突出三种规模的 Avg；124M/253M 的若干单任务下降与 253M +0.02 的幅度没有单独统计。 | p. 6, Table 6；`layout_observation` |
| 显著性措辞替代检验细节 | HRG 使用 “significant drop” 但表中只有单值，没有检验或 seed 方差。 | p. 5, Table 3；`explicit` |
| 附录迁移额外比较 | 更广的位置编码基线在 Section C，正文只提示“refer to Section C”；主文决策主要依赖 RoPE。 | p. 4、15；`explicit` |
| 图形证据替代精确数值 | Figure 2 支撑外推方向，但没有完整曲线数据表和误差；Figure 3 支撑频率模式，但没有统计检验。 | pp. 6–8；`layout_observation` |

以上编码描述信息所处位置和可观察的聚合方式，不推断作者动机。

## 9. Conclusion、limitations 与闭环

### 9.1 Conclusion 逐段功能

Conclusion 为一个长段，约 124 词，动作顺序为：`重述问题 → 重述方法 → 回收机制诊断 → 回收跨域结果 → 回收规模 → 回收长度边界`。它没有新数字，复述 Indirect Indexing、music/genome/language、124M–774M 和 RoPE/YaRN 外推主张（p. 8, §6；`explicit`）。

### 9.2 闭环矩阵

| 引言主张 | 方法回应 | 证据回应 | 结论回应 | 状态 |
|---|---|---|---|---|
| RoPE 将 what/where entangle，影响独立匹配 | Eq. (2) 显示 φᵏ−φᑫ interaction；Eq. (5) 删除它 | Table 1、Table 9 的 Indirect Indexing | Conclusion 复述 RoPE 在 what/where 上困难 | `partially_closed`：机制是代数解释，实证只有一个核心诊断任务。 |
| PoPE 用 what match 与 where match 的 conjunction | Cᵈ magnitude/position phase、Eq. (5)、可学习 δ | Figure 1、Table 1、Table 5 | Conclusion 首句回收 decoupled score | `closed`（定性机制与组件消融均有对应物）。 |
| data efficiency / asymptotic accuracy 改善 | 方法本身给出 inductive bias，但未定义 data-efficiency estimand 或 asymptotic limit | 1M Indirect Indexing 与若干单点 NLL/PPL；无训练曲线或样本量扫描 | 引言/摘要方向性回收 | `partially_closed`。 |
| 跨 music、genome、language 改善 | 同一 PoPE/RoPE 控制设计 | Tables 2–4、Table 6 | Conclusion 回收跨域结果 | `partially_closed`：域选择有机制偏向，语言 downstream 的任务级异质性未展开。 |
| 跨 124M–774M 规模保持收益 | OpenWebText 三规模配置 | Table 4、Table 6 | Conclusion 明示规模范围 | `closed`（范围内的表格证据直接对应）。 |
| 零样本长度外推优于 RoPE 与 YaRN | 频率不插值的 PoPE 与可 fine-tune 的 PoPE+ft | Figure 2，测试到 10240 | Conclusion 回收 RoPE 退化、PoPE 强外推 | `partially_closed`：图无完整数值/误差，且 YaRN/PoPE+ft 的训练条件不对称于零样本 PoPE。 |
| 实现只增加少量计算 | Cartesian kernel Eq. (10)、A.2 FLOPs | 额外 (2L^2d)、两倍 memory/bandwidth；无 runtime | Conclusion 未回收成本 | `partially_closed`：代数成本有，真实系统成本无。 |

## 10. Appendix 职责

| 附录一级模块 | 页码 | 类别 | 对象数量 | 正文调用 | 放入与未放入的内容 | 证据 |
|---|---:|---|---|---|---|---|
| A.1 Derivation of RoPE in Polar Form | 12 | `proof` | Eq. (11)–(16) 加 2 个未编号 display | p. 2：“complete derivation refer to Section A.1” | 放完整旋转矩阵代数；未提供 PoPE 性能定理或泛化保证。 | p. 12, A.1；`explicit` |
| A.2 FLOPs Comparison between RoPE and PoPE | 12–13 | `implementation_detail` | 4 个模块 FLOPs、1 个比例、3 个长度实例 | 未找到显式 Section A.2 调用 | 放复杂度推算与 774M 示例；未放硬件、吞吐、峰值显存实测。 | pp. 12–13, A.2；`explicit` |
| B.1 Datasets | 13–14 | `dataset_detail` | 6 个数据集 | p. 4/5 调用 B.1 | 放生成规则、划分、tokenizer、词表和数据 URL；主文只保留任务摘要。 | pp. 4–5、13–14；`explicit` |
| B.2 Models | 14 | `implementation_detail` | Table 7，5 个数据设置、3 个 OWT 规模 | p. 4 调用 B.2 | 放 embedding size、heads、layers、norm、base wavelength、δ init、dropout；未放硬件。 | p. 14, Table 7；`explicit` |
| B.3 Training Details | 15 | `hyperparameter` | Table 8，5 个数据设置 | p. 4 调用 B.3 | 放 batch、长度、学习率、min LR、weight decay、clipping、AdamW β2、迭代与 warmup；未放 seed 列表。 | p. 15, Table 8；`explicit` |
| C. Additional Results | 15 | `additional_result` | Table 9，6 个位置编码条件 | p. 4 调用 Section C | 放 Indirect Indexing 的额外基线；主文不承担完整 baseline landscape。 | p. 15, C；`explicit` |
| D. Additional Visualizations | 16–18 | `additional_result` | Figure 4–7，4 图 | 未见正文直接调用；Figure 3 的主题在正文出现 | 放 253M frequency usage 与 124M/253M learned δ；未提供数值表、统计检验或频率—性能因果分析。 | pp. 16–18, D；`explicit` |

附录约 1,704 个版面词元，约为主文近似词数的 35.0%。B.1–B.3 对复现自足性帮助明显；A.1 的推导是正文 Eq. (2) 的可核查展开。C、D 的额外基线与可视化被移出主文后，读者仍能理解主结论，但无法在主文内检查更多基线、任务异质性和 253M 频率图；因此附录迁移对“PoPE 优于 RoPE”的方向结论影响有限，对机制外推与完整比较范围有影响（pp. 4–8、12–18；`interpretation`）。

## 11. 用词与修辞

以下为主文 pp. 1–8 的 PDF 文本线索；计数对换行和连字符做了规范化，公式碎片、表格数字和引用不作为论证词。括号中的数字是近似文本计数，语境判断以人工阅读为准。

### 11.1 高频实词与词组

- 方法/基线名最密集：`RoPE` 约 64 次、`PoPE` 约 61 次；其次是 `positional/position/positions` 合计约 78 次、`query/key` 合计约 59 次、`model/models` 合计约 39 次。驱动力是方法对照与位置编码机制，而非模板套话（pp. 1–8；`interpretation`）。
- 论证对象词：`attention` 约 25、`length` 约 19、`frequency/frequencies` 约 22、`sequence/sequences` 约 37、`performance` 约 18、`relative` 约 23。高频词组包括 `key and query`（约 12）、`positional encoding`（约 9）、`complex-valued`（约 9）、`attention score`（约 7）、`zero-shot`（约 6）、`length extrapolation`（约 5）、`downstream tasks`（约 5）。
- `what/where` 是概念对而非泛化模板：`where` 约 22、`what` 约 13；反复出现在 interaction、diagnostic task 和 conclusion 回收中（pp. 1–8；`interpretation`）。

### 11.2 主张动词、限定词与强弱比例

- 规范化 whitespace 后，`we propose` 3 次、`we find` 3 次、`we introduce` 2 次、`we evaluate` 2 次、`we compare` 2 次、`we train` 2 次、`we test` 2 次、`we measure` 2 次、`we see` 1 次；显式 `we show`、`we demonstrate`、`we observe` 未出现。作者更常用“find/see”承载结果，用“propose/introduce”承载方法（pp. 1–8；`interpretation`）。
- 强主张词包括 `superior`、`outperform`、`eliminates`、`solves`、`strong`、`significant`；弱化/限定词包括 `can`（约 15）、`might`（约 2）、`possibly`、`presumably`、`largely`、`appears`/“less clear”等。方向性结果明确，机制因果和跨域普适性在措辞上留有缓冲（pp. 1–8；`interpretation`）。
- 主文强结果段与方法定义段占主要论证空间；作者没有给形式 theorem 或可证伪的效果阈值。最强语言集中在 Indirect Indexing 的“almost perfectly”和 Figure 2 的“out-of-the-box length extrapolation”，而统计不确定性只集中在 Table 1（pp. 4–7；`explicit` + `interpretation`）。

## 12. 最高层判断

1. **单一主线**：RoPE 的二维块把内容 magnitude 与 key/query-dependent phase 放在同一个匹配通道，产生 what–where interaction；PoPE 用逐元素 softplus magnitude 和仅由相对位置决定的 phase，将注意力分数改写为可分的内容权重乘位置核，并以 Indirect Indexing、跨域 NLL/PPL、下游平均准确率和长度外推检验该偏置（pp. 2–8, Eq. (2)/(5), Tables 1–6, Figure 2；`explicit`）。
2. **正文保留的决策关键内容**：RoPE→PoPE 的代数差异、对照条件、四类主结果表、三种规模、PG-19 长度曲线、主要组件消融和工程成本方向；这些对象让读者能判断方法是否解决目标机制与是否付出计算代价（pp. 2–8；`explicit`）。
3. **移入附录的细节与代价**：RoPE 完整推导、FLOPs 公式、所有数据集生成/划分、模型与训练表、额外位置编码基线、253M 频率与 δ 图。A/B 附录提高复现粒度；C/D 的移出降低主文对 baseline 完整性和机制诊断的自足性（pp. 12–18；`interpretation`）。
4. **最有效的模式**：先用 Eq. (2) 把抽象的 what/where confound 变成单一 interaction term，再用 Eq. (5) 只删该项；随后在最小诊断任务 Table 1 给出大幅配对差异，最后扩展到真实域和 Figure 2。代数对象、机制诊断和跨域性能形成可追踪链条（pp. 2–8；`interpretation`）。
5. **最大叙事缺口**：外推图与跨域单点结果缺少 seed/误差、完整数值与 runtime；Table 6 的任务级回退被 Avg 覆盖，Table 5 caption 的模型规模与列不一致，Figure 3 caption 的规模覆盖也有错位（pp. 5–8、16；`layout_observation`）。
6. **可迁移规则**：当新位置编码声称消除一个交互机制时，先给出能单独要求该机制的最小诊断任务，再用匹配控制的跨域结果和组件/替代基线消融回收同一机制；主文同时列出关键成本与任务级异质性。
7. **适用边界**：该规则适用于机制主张能被程序化诊断、组件化实现且存在对照编码的模型论文；若任务无法隔离机制，或结果只有无配对的应用 benchmark，则不能把性能提升直接归因为交互项被消除。

## 13. 版面/测量不一致记录

1. 自动预处理把 Appendix 起点识别为 p. 10、main end 识别为 p. 18；人工按 PDF 的 “References” 与 “A. Method Details” 标题修正为 References p. 9–11、Appendix p. 12–18。原因是双栏标题检测与 p. 9 Impact Statement/References 的混排（PDF pp. 9、12；`layout_observation`）。
2. 自动编号公式扫描得到 13 个候选；人工逐页核对得到 Eq. (1)–(16) 共 16 个，另有 10 个未编号 display。原因是多行公式的编号与 PDF 文本行断裂（PDF pp. 2–4、12–13；`layout_observation`）。
3. Table 5 caption 写“124M Transformer model”，表头同时有 124M、253M 两列；正文消融段也只说训练 124M。保留两处文本，不替作者猜改哪一处（PDF p. 5；`explicit`）。
4. Figure 3 caption 写 “124M and 253M models”，主文图面展示 124M 的两幅图，253M 的对应图出现在附录 Figure 4–5；正文 p. 6 也只将 Figure 3a/b 作为 124M 证据。保留为 caption/图面范围错位（PDF pp. 6、8、16；`layout_observation`）。
5. Section 3 约束偏置的印刷公式把被截断/限制的符号写成 θ꜀，上下文在该段持续讨论 δ꜀；报告按 PDF 原样记录，未进行符号校正（PDF p. 3；`explicit`）。

## 14. 证据覆盖

本备忘录将 34 个实质判断计为可定位主张，均附物理页、章节/对象和 `explicit`、`layout_observation` 或 `interpretation` 标记；证据覆盖为 34/34，状态 `complete`。

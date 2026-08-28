# Visual audit — `iclr-2026-6a94cca2daa0`

## 论文与审计边界

- **标题**：In-Place Test-Time Training
- **论文 ID**：`iclr-2026-6a94cca2daa0`
- **PDF 事实源**：`corpus/pdfs/iclr-2026-6a94cca2daa0.pdf`
- **物理页数**：21 页（正文 p.1–p.10；Ethics、Reproducibility、Acknowledgement 与 references p.11–p.15；附录 p.16–p.21）。
- **渲染**：使用 `pdftoppm -r 220` 渲染全部 21 页，并以原始分辨率检查含对象的 p.6–p.10、p.19–p.20；其余页面以全页 contact sheet 和逐页 PDF 文本核对，确认没有漏记 Figure/Table。
- **对象清单原则**：PDF 是对象清单事实源。p.6 的 Figure 1、p.7 的 Table 1、p.8 的 Table 2/Figure 2、p.9 的 Table 3/Figure 3、p.10 的 Figure 4，以及附录 p.19–p.20 的 Table 4–8 均实际出现。p.18 的 Algorithm 1 是伪代码对象，不属于当前 JSON 的 Figure/Table 数组，单独记录在 Markdown；p.11–p.15 references 和 p.21 附录文字没有视觉对象。

## PDF 对象清单

| 对象 | 物理页 | 模块 | 版面位置 |
|---|---:|---|---|
| Figure 1 | 6 | method / overall framework | 正文宽度，页面上部 |
| Table 1 | 7 | results / pre-trained drop-in | 正文宽度，页面下部 |
| Table 2 | 8 | results / model extension | 居中窄表 |
| Figure 2 | 8 | results / from-scratch perplexity | 正文宽度，页面下部 |
| Table 3 | 9 | results / 4B evaluation | 正文宽度，页面上部 |
| Figure 3 | 9 | ablation / design choices | 正文宽度，Table 3 下方 |
| Figure 4 | 10 | ablation / efficiency | 正文宽度，页面上部 |
| Table 4 | 19 | appendix D.2 / training hyperparameters | 居中窄表 |
| Table 5 | 19 | appendix D.2 / pretraining hyperparameters | 居中窄表 |
| Table 6 | 19 | appendix D.2 / continual pretraining | 正文宽度 |
| Table 7 | 20 | appendix D.2 / continual pretraining | 居中表 |
| Table 8 | 20 | appendix D.3 / model configuration | 居中窄表 |

## 来源核查

`reports/tables/visual_source_inventory.csv` 的目标行标为 `no_public_source_found`，自动候选误指向 `open-compass/opencompass`；该仓库是评测框架，不是本文的作者视觉源。`corpus/visual_sources/iclr-2026-6a94cca2daa0/` 不存在可用文件。PDF 正文没有 GitHub URL，只在 p.10/p.18 说明将发布 source code 和 checkpoints。

随后用 `gh` 只读按标题、方法名和作者团队检索，找到 [ByteDance-Seed/In-Place-TTT](https://github.com/ByteDance-Seed/In-Place-TTT)。仓库 README 的标题、作者列表、ICLR 2026 Oral 标识、OpenReview `dTWfCLSoyl` 和 arXiv `2604.06169` 与本文直接对应；默认分支 `main` 当前提交为 `be2324829b0e91c8fd10a74d4b43714fde6676e1`。仓库树只有一份 `assets/pipeline.png` 视觉资产，未提供 Figure 2–4 的 plot script、LaTeX/TikZ/PGF 或表格生成器；模型实现和 YAML 配置属于方法/复现实验代码，不是图表源。

来源状态为 **partial visual source**：`assets/pipeline.png` 是与 PDF Figure 1 语义和构图相同的 README 方法概览渲染资产，但 PDF 本身使用矢量图形，仓库未提供其原始编辑文件；Figure 2–4 和所有表格没有精确的公开视觉生成源。README 的 `pipeline.png` 只能作为相关 rendered asset，不把其 PNG 像素值冒充 PDF 的 source-exact 绘图参数。

## Figure 审计

### Figure 1 — overall In-Place TTT framework（p.6）

**caption（逐字）**：

> Figure 1: The overall framework of our In-Place Test-Time Training. The module operates sequentially on input chunks. For each chunk, the current fast weights are first applied to the intermediate activations Z to produce the output. Then, these weights are updated using the activations Z and a value V derived from the token embeddings. This ”apply-then-update” cycle allows the model to dynamically adapt to incoming context in a strictly causal manner.

- **版面/几何**：正文宽度单一大图；左侧是竖直 `Generating Direction` 箭头与 `Input Embedding`，中间是 `Attention` 与 `Gated Linear Layer`，右侧大虚线框标记 `MLP with In-Place TTT`。右框再分为 `Apply` 和 `Update` 两个虚线子区；输入经 `Split into chunks` 后沿 `Wdown^(i-1) → Wdown^(i) → Wdown^(i+1)` 状态路径流动，并以 `Conv1D & Projection` 生成更新目标。约 2 个逻辑区域、15 个以上标注框/箭头，复杂度 4/5。
- **图型/plot grammar**：`architecture`, `pipeline`, `conceptual_diagram`；PDF 中是矢量形状与文字（`vector`），x/y 均为 `none`，无 grid、legend、marker、hatching 或 uncertainty；direct labels=true；solid 流程线与 dotted 分组边界为 2 种 line styles；无 reference line；线宽约 1 pt，均为 rendered estimate。
- **Typography**：图内字体由 PDF object 记录为 Arial/Arial Bold，数学状态标签使用 Cambria Math；约 8–14 pt，regular 与 bold，roman，数学下标有缩小字号。黑色文字/边界，蓝灰、红、紫和米黄色填充形成层级。PDF object provenance，高置信度。
- **颜色**：categorical；从 PDF 矢量填充/220 dpi 渲染读到的代表色包括 `#BD374A`（Attention）、`#31778E`（Gated Linear Layer）、`#778495`（fast-weight/loss boxes）、`#D66E49`（chunk/update blocks）、`#EFE9D1`（input embedding）、`#D6C88B`（value/update stream）、`#A0CFDE`（output stream）、`#001473`（generating-direction arrow）与 `#000000`（文本/边界）。这些 HEX 是 PDF 视觉估计而非仓库原始 source-exact 色值；颜色编码组件角色，箭头方向、位置和文字提供冗余，灰度下仍可依靠文字/线型区分但填充层级会减弱。
- **编码与证据关系**：x/y 是流程空间；color 是组件类型/状态；shape 是模块框、圆形加法节点和虚线 group；line/arrow 是数据依赖及因果方向；facet 不是统计 facet；text 是模块名、状态、损失和 `Conv1D & Projection`。它是 method_interface/theory_mechanism 的核心入口，直接把 p.4 的 in-place `Wdown`、p.5 的 NTP-aligned target、p.6–p.7 的 apply→update→parallel-scan 连接起来。
- **数据/统计**：没有数值数据或不确定性；图传达每个 chunk 先 apply 当前 fast weights、再用 `Z` 与 `V` update，并在 context parallelism 下保持严格 causal 语义。caption 明确了输入 chunks、`Z`、`V` 和 apply-then-update 结论。
- **优点**：左到右的生成方向和分组虚线边界将标准 Transformer 路径与 TTT 增量路径分离；`Apply` 与 `Update` 的先后顺序可直接读出；状态下标和损失框让实现对象与方法文字对应。
- **缺陷**：组件多且箭头交叉，读者需要在 `Wdown`、`ΔW`、`V` 之间来回追踪；颜色虽有角色差异但没有图例，浅色填充在灰度打印中层级变弱；caption 没有解释 `CP`、`Z`/`V` 的维度或 boundary reset。
- **可复用范式**：把标准 backbone、可更新 state、apply/update 两阶段和并行聚合放入同一条有向流程；使用外层/内层虚线框表达“既有模块内嵌新状态”，并在 caption 明确顺序和因果边界。

### Figure 2 — sliding-window perplexity（p.8）

**caption（逐字）**：

> Figure 2: Sliding Window Perplexity at varying context lengths on the Pile dataset for 500M (left) and 1.5B (right) parameter models. Our In-Place TTT consistently achieves lower perplexity than all competitive baselines.

- **版面/几何**：正文宽度、左右两个 panel；panel 标题为 `(a) Sliding Window Perplexity of 500M Model` 与 `(b) Sliding Window Perplexity of 1.5B Model`。每 panel 5 条折线（In-Place TTT、SWA、GLA、Deltanet、LaCT），x 轴 `Context Length`，y 轴 `Perplexity`；2k–32k context 标记点沿曲线排列，背景有横纵 dotted grid。复杂度 3/5：2 panels、5 series、每 panel 5 项 legend。
- **Plot grammar**：`line`，vector；x=`log`（2k、4k、8k、16k、32k 的等距 log2-style context positions），y=`linear`；grid=`both`；每个 panel 有独立 legend，位置 `upper_right`，shared_legend=false；direct labels=false；marker_types=5（circle、square、diamond、triangle-up、triangle-down）；line_styles=1（solid）；hatching=false；reference_lines=0；无 uncertainty；线宽约 1.2 pt，rendered estimate。
- **Typography**：Times New Roman/`CNAJXZ+TimesNewRomanPSMT`，panel title 与 axis label 约 8–10 pt，ticks/legend 约 6–8 pt，regular roman。PDF object provenance，高置信度。
- **颜色**：categorical；代表色为 `#342F8E`（In-Place TTT）、`#8FA9FF`（SWA）、`#9E9E9E`（GLA）、`#7D7D7D`（Deltanet）、`#BDBDBD`（LaCT）。marker 形状和 legend 对颜色有冗余，但五条灰/蓝线在低质量灰度复制中仍可能混淆，故 grayscale_safe=false；HEX 为 PDF vector fill/stroke 的渲染估计。
- **编码与证据关系**：x 是 context length，y 是 validation sliding-window perplexity，color/marker 是方法，facet 是模型规模。Figure 2 承担 main_comparison/headline：p.9 §4.2 将较低 perplexity、持续下降到 32k 解释为 TTT 压缩并利用 incoming context 的证据。
- **数据/统计**：数据集为 Pile validation（正文还说明 Proof-Pile-2 用于 from-scratch 评估）；指标是在固定 final token block 上随前置 context 延伸计算的 perplexity。没有误差带、seed、重复或置信区间；右 panel 的 SWA 在 4k 后近似平台，In-Place TTT 曲线继续下降，这一形态来自 rendered observation。
- **优点**：两个模型规模使用相同图语法和共享坐标语义；方法间曲线差异和上下文趋势比单个终点表更直观；marker 加 legend 使多系列可追踪。
- **缺陷**：caption 没有定义 sliding-window final block、context sampling、重复或线型/marker 语义；x 轴 log2-style 排列没有明示；没有 uncertainty band，无法判断小差距的运行变异。
- **可复用范式**：对 context-scaling 曲线使用相同 y 指标的并排模型 panel、固定方法颜色/marker、同时显示关键 context ticks，并在 caption 定义 log 轴、评估 block 和重复协议。

### Figure 3 — ablation of design choices（p.9）

**caption（逐字）**：

> Figure 3: Ablation studies on the key design choices of the In-Place TTT framework, evaluated on the RULER benchmark with a 1.7B parameter model. The plots illustrate the impact of: (a) State size, showing that performance improves as the state size scales; (b) Chunk size, demonstrating a performance trade-off where intermediate sizes (e.g., 512, 1024) are optimal; and (c) The LM-Aligned Value objective, confirming that both the convolution (w Conv) and the projection (w Proj) are crucial.

- **版面/几何**：正文宽度、三个并排 panel：`(a) State size`、`(b) Chunk size`、`(c) LM-Aligned Objective`。每 panel 横轴为 RULER-4k/8k/16k，纵轴为 `Score`；背景为水平 dotted grid。panel (a) 3 系列（4×、1×、0.5×，9 bars），panel (b) 4 系列（C=256、C=512、C=1024、C=2048，12 bars），panel (c) 4 系列（w Conv, Proj；w/o Conv；w/o Proj；w/o Conv, Proj，12 bars）。共 33 个 bars，复杂度 3/5。
- **Plot grammar**：`bar`，vector；x=`categorical`，y=`linear`；grid=`y`；三个 panel 各有独立 legend（分别 3、4、4 items），位置均为 `upper_right`，shared_legend=false；direct_labels=false；marker_types=0；line_styles=1；hatching=false；reference_lines=0；无 uncertainty；bar outline 约 0.5 pt，rendered estimate。
- **Typography**：Times New Roman；panel titles约 9–10 pt，axis/ticks约 6–8 pt，legend约 5–7 pt，regular roman。PDF object provenance，高置信度。
- **颜色**：categorical；`#7A7FD6`、`#9FB5F2`、`#B6C5E6`、`#7A8896` 依次复用于各 panel 的 variant series。颜色和 legend 是主要系列编码，bar 高度是 score；相邻浅色在灰度下区分度有限，grayscale_safe=false；HEX 为 PDF vector fill 的渲染估计。
- **编码与证据关系**：x 是 RULER context task，y 是 score，color 是 state/chunk/objective variant，facet 是三种设计选择。它是 ablation/mechanism 对象：panel (a) 连接 fast-weight state size，(b) 连接 p.4 chunk update，(c) 连接 p.5 LM-aligned `Conv1D` 与 `Wtarget`，并在 p.10 文字中回收到 Theorem 1。
- **数据/统计**：实验为 1.7B model 的 RULER，图内没有数值 labels、误差条、重复或不确定性。caption 直接给出三个 qualitative main findings：更大 state 更好、512/1024 chunk 的 trade-off、Conv 与 projection 均关键。
- **优点**：一个共同 y 轴和相同三项 RULER context 让三个机制问题能并列比较；panel 标题和 legend 使 variant 归属清晰；图注同时说明模型、benchmark 和方向性结论。
- **缺陷**：没有显示 exact values 或 variability；单栏压缩后 legend 与 x tick 字号很小；panel (c) 的 `w Conv, Proj` 等缩写虽出现在图例和 caption，但没有说明基准配置；颜色不能独立支持灰度复制。
- **可复用范式**：将一个 ablation question 拆成并排 panel，共享任务轴和 y 语义，每 panel 保留完整 variant legend，并在 caption 用一句话绑定 variant 到方法组件与结论。

### Figure 4 — efficiency analysis（p.10）

**caption（逐字）**：

> Figure 4: Efficiency analysis of In-Place TTT. Both prefill throughput (a, b) and peak memory (c, d) metrics are presented for 4B models with Sliding-Window Attention (SWA) and Full Attention at various context lengths. Our In-Place TTT introduces negligible overhead in practical scenarios.

- **版面/几何**：正文宽度、四个并排 panel：(a) `Throughput (SWA)`、(b) `Throughput (Full)`、(c) `Memory (SWA)`、(d) `Memory (Full)`。每 panel x 为 8k、32k、128k，两个 bars 比较 Baseline 与 TTT；(a,b) y=`Prefill TPS (K tokens/s)`，(c,d) y=`Peak Memory (GB)`。共 24 bars，复杂度 4/5。
- **Plot grammar**：`bar`，vector；x=`categorical`，y=`linear`；grid=`y`；每 panel 有独立 2-item legend（upper right），shared_legend=false；direct_labels=false；marker_types=0；line_styles=1；hatching=false；reference_lines=0；无 uncertainty；bar outline约0.5 pt，rendered estimate。
- **Typography**：Times New Roman；panel title约 9–10 pt，axis/ticks约 5–8 pt，legend约 5–6 pt，regular roman。PDF object provenance，高置信度。
- **颜色**：categorical；Baseline 与 TTT 使用 `#9FB5F2` 和 `#B6C5E6` 两种蓝色，legend 解释 panel 内映射。色彩区分依赖明度与 legend，灰度安全性有限，记录为 false；HEX 为 PDF vector fill 的渲染估计。
- **编码与证据关系**：x 是 context length，y 分别是 throughput 或 memory，color 是 baseline/TTT，facet 是 attention mode × efficiency metric。它承担 efficiency_cost/robustness 证据，将 p.7 的 CP-native/chunk-wise scalability 主张与 4B inference 的 throughput/memory overhead 连接起来。
- **数据/统计**：正文 D.2 说明 sequence length 8k–128k、batch size 1、Nvidia H800；图中没有 error bars、重复数、峰值定义或运行方差。caption 直接声称 practical overhead negligible，但柱高仍需结合 axis 和实验设置解释。
- **优点**：吞吐与显存分成明确的 2×2 panel，SWA/Full 对照保留；相同三档 context 使成本趋势可扫读；legend 简短。
- **缺陷**：没有 direct numeric labels，单栏小图难以精确读柱高；caption 未给 batch/hardware、重复、峰值窗口或 throughput 计时定义；“negligible overhead”是宽结论，而图未给误差或相对百分比。
- **可复用范式**：对效率同时展示速度和内存，把系统模式拆成小 multiples，保持统一 context levels，并在 caption/脚注明确 hardware、batch、计时和重复协议。

## Table 审计

### Table 1 — RULER evaluation（p.7）

> **Table 1: Evaluation results on the RULER benchmark (Hsieh et al., 2024). We report the average accuracy (%) as scores, with the best results in bold.**

- **结构**：7 个数据行（Mistral、GLM3、Phi3、Llama3、Qwen3-Instruct、Baseline、In-Place TTT），8 列（Model + 4k/8k/16k/32k/64k/128k/256k）；2 级表头，顶层为 `In-Domain Evaluation`（4k–128k）和 `Extrapolation`（256k）；2 个行组（参考模型 vs 本文 Baseline/In-Place TTT）；一位小数；booktabs 横线，另有 256k 的竖直分隔线。`Baseline` 和 `In-Place TTT` 的最优值加粗，256k 参考模型为 `-`。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头和 best cells 粗体，其余 regular；黑色文字和规则，无 cell color，grayscale-safe=true。
- **数据/证据关系**：RULER average accuracy (%)，按 context length 比较预训练 Qwen3-4B baseline 与 In-Place TTT，并放入已有模型参考行。Table 1 是 Q1/drop-in 的 main comparison，p.8 文字用 64k、128k、256k 的差异解释长上下文泛化。没有均值方差、seed 或置信区间。
- **优点**：顶层 in-domain/extrapolation header 显示评测边界；参考模型与自有对照同表；bold best 简化决策读取。
- **缺陷**：caption 没说明每个 RULER 子任务如何平均、evaluation seeds 或 256k extrapolation protocol；模型行的训练/参数条件不在表内；竖直分隔线与 booktabs 语言略不一致。
- **可复用范式**：用分组表头区分域内与外推 context，并将 baseline、方法和外部参考置于同一 accuracy/% 决策面。

### Table 2 — cross-model RULER extension（p.8）

> **Table 2: Extension of In-Place TTT to LLaMA-3.1-8B and Qwen3-14B-Base on the RULER benchmark. We report the average accuracy (%) with the best results in bold.**

- **结构**：4 个数据行（每个 Base Model 下 Baseline/In-Place TTT），8 列（Base Model、Method、4k、8k、16k、32k、64k、64k+YaRN）；一级列头、2 个模型行组；一位小数；booktabs，模型组间有横线；所有模型组内最佳值加粗，缺少 YaRN 条件处以 `–`。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头和最优值粗体，其余 regular；黑白、无高亮、灰度安全。
- **数据/证据关系**：RULER average accuracy (%)，比较 LLaMA-3.1-8B 与 Qwen3-14B-Base 的 drop-in 增强和 YaRN 组合。它是 Q1 的跨模型 robustness/main-comparison 支撑；p.8 文字指出长 context 和 64k+YaRN 的增益。无不确定性、重复或成本列。
- **优点**：Base Model/Method 两层行分组清楚，context 与 YaRN 条件在同一表面；caption 交代 benchmark、模型和单位。
- **缺陷**：`64k+YaRN` 只对 Qwen 行有值，caption 未说明缺失原因；continual-training token budget、RoPE 和评估实现依赖正文/附录；仍无方差。
- **可复用范式**：将跨 backbone 的同一长上下文评测按 model group 展开，特殊 position-extension 条件作为显式列而非另表。

### Table 3 — 4B downstream/long-context evaluation（p.9）

> **Table 3: Evaluation results of 4B models on common sense reasoning and long-context evaluation benchmarks. Best performance is in bold. “SWA” is Sliding-Window Attention, “Full Attn.” is Full Attention, and “I.P. TTT” is our In-Place TTT.**

- **结构**：4 个数据行（Baselines/ I.P. TTT 各含 Full Attn.、SWA），10 列（Model、Architecture、HellaSwag、ARC-E、ARC-C、MMLU、PIQA、RULER-4k、RULER-8k、RULER-16k）；2 级列头，`Common Sense Reasoning` 跨 5 个任务，`Long-Context Evaluation` 跨 3 个任务；2 个行组；两位小数；booktabs，组间和底部横线；最优 cell 粗体。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头和 best cells 粗体，regular body；纯黑白，无 cell color，灰度安全。
- **数据/证据关系**：4B model accuracy scores，比较 Full Attention/SWA baseline 与对应 I.P. TTT；它是 Q2 的 main comparison，将普通 commonsense 与 RULER 长上下文放在同一 decision surface。p.10 回收 RULER-16k 6.58→19.99 和 RULER-8k 9.91→26.80。无重复/区间。
- **优点**：按任务家族分组，Full/SWA architecture 与 Baseline/I.P. TTT 两种因素同时显式；caption 定义三处缩写；best bold 易读。
- **缺陷**：表头密度高，长任务名与小字号挤压；不同 benchmark 的 aggregation/shot protocol 不在 caption；没有显存、吞吐或方差。
- **可复用范式**：将 task family 作为二级列头、system variant 作为行组，适用于同时报告能力指标与长上下文指标的模型对照。

### Table 4 — 500M/1.5B training hyperparameters（p.19，附录）

> **Table 4: Training hyperparameters for 500M and 1.5B models.**

- **结构**：9 个超参数行（Optimizer、Learning Rate、Batch Size、Weight Decay、Gradient Clipping、Warmup Steps、Sequence Length、Tokens Trained、Sliding Window Size），3 列（Hyperparameter、500M Model、1.5B Model）；一级表头；2 个行组（优化/预热与训练/窗口，内部横线分隔）；混合精度，科学计数法 `5e-4/3e-4` 与整数/文本并列；booktabs；无高亮。
- **数据/证据关系**：附录 D.2 的 from-scratch 训练配置，连接 Figure 2 的 500M/1.5B perplexity curves；AdamW、batch、20B/60B tokens、32,768 sequence 和窗口大小使复现实验边界可见。无不确定性。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt，表头粗体，正文 regular；黑白、灰度安全。
- **优点**：把优化器与数据/窗口预算放到同一小表，两个规模可直接比对；横线分隔语义组。
- **缺陷**：caption 不说明哪些行是 baseline 共同配置；`5e-4` 等科学记法未统一为 LaTeX 风格；warmup、token budget 与评估重复协议仍需读正文。
- **可复用范式**：用两列模型并列、按训练阶段分组的超参数表支持 from-scratch 曲线复现。

### Table 5 — 1.7B/4B pretraining hyperparameters（p.19，附录）

> **Table 5: Training hyperparameters for 1.7B models and 4B models pretraining**

- **结构**：8 个行（Optimizer、Learning Rate、Batch Size、Weight Decay、Gradient Clipping、Warm-up Tokens¹、Sequence Length、Tokens Trained），2 列（Hyperparameter、value）；一级表头；无行组；混合精度（`3e-4`、`8M tokens`、`1.6B` 等）；booktabs；无高亮。
- **数据/证据关系**：附录 D.2 的 1.7B ablation 与 4B from-scratch 共享训练设定，支撑 Figure 3 的 1.7B RULER ablation 和 Table 3/ Figure 4 的 4B 实验。脚注 Warm-up Tokens¹ 在页面下方/正文未形成单独对象，需结合上下文解释；无不确定性。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头粗体、正文 regular；黑白、灰度安全。
- **优点**：短表避免重复模型列，突出共享配置；适合附录快速查阅。
- **缺陷**：caption 没有明确 value 对 1.7B 和 4B 均相同；脚注标记 `¹` 的具体含义不在表边界内；没有硬件/seed。
- **可复用范式**：当多个模型共享超参时，用 `value` 单列并在 caption 明示共享范围，避免制造重复矩阵。

### Table 6 — two-stage continual pretraining（p.19，附录）

> **Table 6: Hyperparameters for two-stage continual pre-training.**

- **结构**：8 个行（Base Model、Optimizer、Learning Rate、Weight Decay、Sequence Length、Tokens Trained、RoPE Extension、Conv Size），3 列（Hyperparameter、Stage 1 (32k Context)、Stage 2 (128k Context)）；一级表头；2 个行组（optimizer/base 与 sequence/extension，横线分隔）；混合 scientific/integer/text precision（`5e-6`、`32,768`、`∼20B`、`YaRN`）；booktabs；无高亮。
- **数据/证据关系**：附录 D.2 给 Qwen3-4B-Base 的两阶段 continual training 配置：约 20B/15B tokens、32,768/131,072 sequence、None/YaRN、Conv size 5；它是 Table 1 的 drop-in RULER 结果和 Figure 4 4B efficiency 的复现边界。无不确定性。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头粗体，正文 regular；黑白、灰度安全。
- **优点**：阶段列将 context、token budget、RoPE extension 放在一处，直观表达课程式长上下文训练。
- **缺陷**：caption 没有写 base model；`128k Context` 对应实际 131,072 未在标题中解释；没有写 inference-time clipping threshold（正文 D.2 另述）。
- **可复用范式**：用 stage columns 表示课程/continual training 的状态转移，同时保留 sequence、token、position extension 和 kernel 参数。

### Table 7 — LLaMA/Qwen continual pretraining（p.20，附录）

> **Table 7: Hyperparameters for continual pre-training of LLaMA-3.1-8B and Qwen3-14B-Base.**

- **结构**：7 个行（Optimizer、Learning Rate、Weight Decay、Sequence Length、Tokens Trained、RoPE Extension、Conv Size），3 列（Hyperparameter、LLaMA-3.1-8B、Qwen3-14B-Base）；一级表头；2 个行组（optimizer/learning 与 sequence/extension，横线分隔）；混合科学计数法/整数/文本；booktabs；无高亮。
- **数据/证据关系**：附录 D.2 给 Table 2 两个 backbone 的共同 continual-pretraining 设置（AdamW、5e-6、0.1、32,768、约20B、None、Conv size 5）；无不确定性。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头粗体、正文 regular；黑白、灰度安全。
- **优点**：两种 backbone 横向对齐，能确认 Table 2 的增益比较共享训练预算与 context。
- **缺陷**：caption 不说明两列使用相同两阶段协议的哪些部分；不含评测 context、YaRN extension 或 clipping 设置；没有 seed/硬件列。
- **可复用范式**：把跨 backbone 的共同超参用对称列呈现，并将模型特有差异留在数值/文本 cell 中。

### Table 8 — architectural configurations（p.20，附录）

> **Table 8: Model architectural configurations for 500M and 1.5B Model.**

- **结构**：8 个参数行（Parameters (Approx.)、Hidden Size、Num Layers、Num Attention Heads、FFN Hidden Size、Window Size、Vocabulary Size、Rope Base），3 列（Parameter、500M、1.5B）；一级表头；无行组；整数与 `1e6` 混合表示，`decimal_precision` 记为 null；booktabs；无高亮。
- **数据/证据关系**：附录 D.3 的 model configuration，给 Figure 2 的 from-scratch 500M/1.5B architecture（hidden 1024/2048、24 layers、8/16 heads、FFN 3072/6144、window 2048/4096、vocab 32,000、RoPE base 1e6）。无不确定性。
- **Typography/颜色**：Nimbus Roman/Computer Modern 约 10 pt；表头粗体、正文 regular；黑白、灰度安全。
- **优点**：参数名、两个规模和窗口/词表放在同一紧凑表，适合复现。
- **缺陷**：caption 的单数 `Model` 不够精确；没有 4B/1.7B 架构列，正文要求读者从 Qwen base 继承；`Rope Base` 与正文 RoPE 命名大小写不一致。
- **可复用范式**：在附录用参数行 × 模型列的最小表固定架构边界，避免把训练 hyperparameter 与 model architecture 混在一个表中。

## 算法对象（schema 外补充）

**Algorithm 1：In-Place TTT with Context Parallelism (Single Layer)**（p.18）是全宽伪代码，不计入 Figure/Table 数量。它有 14 个 numbered lines，先并行算 `H_i/U_i/G_i/Z_i/V_i/ΔW_i`，再用 `CUMSUM` 聚合，最后以 `Wdown^(i-1)=Wdown^(0)+ηS_i` apply 输出，并在 document boundary reset fast weights。该对象没有颜色/图例/统计不确定性；它与 Figure 1 的 apply/update pipeline、Figure 4 的 efficiency claim 构成实现闭环。

## 交叉对象系统

- **视觉叙事**：Figure 1 先给 architecture/interface；Table 1–2 验证预训练模型的 drop-in 与跨模型扩展；Figure 2 和 Table 3 转向 from-scratch 的 perplexity 与 downstream accuracy；Figure 3 逐项拆解 state/chunk/objective；Figure 4 量化 throughput/memory；Table 4–8 在附录固定训练预算、continual stages 与模型架构。对象顺序对应“方法机制 → Q1 → Q2 → Q3 → 复现设置”。
- **Caption 系统**：Figure 1–4 的 caption 都包含 setup，Figure 1/2/3/4 还直接写出流程或主发现；Table 1–3 的 caption 定义 benchmark、单位、缩写和 bold 规则，Table 4–8 主要是 title-only。图注强于附录表注，但几乎所有对象都没有 uncertainty/repeat/seed 定义。
- **表头系统**：主结果表用多级列头表达 in-domain/extrapolation、任务家族，行组表达模型/方法；附录表用参数行 × 模型/阶段列，并在 Table 4/6/7 以横线切分训练语义。所有表采用黑白 booktabs 和少量横线。
- **方法—结果—消融链**：Figure 1 的 `Wdown`/chunk/apply/update 对应 §3.1/§3.4；Table 1/2 对应 Q1；Figure 2/Table 3 对应 from-scratch Q2；Figure 3 将理论中的 LM-aligned target 映射为 Conv/Proj 消融；Figure 4 和 Table 4–8 把吞吐、内存、训练与架构边界补齐。
- **主文—附录链**：主文图表只给结论和少量设置，p.19–p.21 的 Table 4–8、D.1–D.3 负责数据 mixture、token budget、H800、clipping、模型配置和初始化细节；Algorithm 1 p.18 负责 parallel scan 的可执行语义。附录是复现入口，但没有公开 Figure 2–4/table 的生成文件。
- **字体/颜色一致性**：正文和表格稳定使用 Nimbus Roman/Computer Modern；图 2–4 也使用 Times New Roman，Figure 1 内嵌 Arial/Cambria Math。表格完全 grayscale-safe；图使用蓝/灰线或蓝色系 bars，Figure 1 使用角色色，颜色和 marker/位置通常有冗余但没有统一色板说明。

## 最终判断

- **最可复用模式**：Figure 1 的 backbone-in-place + apply/update 流程；Figure 2 的双 panel context-scaling 曲线；Figure 3 的同轴多机制 ablation；Table 1/3 的分组表头与方法行组；Table 6 的 stage-column 复现表。
- **最高价值对象**：Figure 1 最有效地把抽象 fast-weight 机制压缩为可追踪的因果流程；Figure 2 直接展示 context length 下的方法曲线差异；Figure 3 把理论目标拆成可证伪的组件；Table 3 把 common-sense 与 long-context 结果放到同一 4B 对照面。
- **失败模式**：附录表格的 caption 多为标题，未在对象边界内定义共享范围、单位、seed、硬件或重复；Figure 2–4 无 uncertainty；单栏小 multiples 的 legend/tick 字号偏小；颜色/明度缺少统一说明；Figure 1 PDF 矢量原稿和 Figure 2–4/table generator 未公开，视觉复现不完整；Table 5 脚注、Table 6 的 128k/131,072 映射依赖正文上下文。
- **一句话视觉策略**：论文以低装饰 serif/booktabs 系统把“MLP 内嵌 fast weights—长上下文结果—机制消融—系统成本—附录复现设置”串成一条视觉证据链，但应补齐图表生成源、caption-level 评测协议和不确定性，才能让这条链独立可审计。

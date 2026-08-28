# Rational Transductors 视觉审计

- **paper_id**：`icml-2026-ef7b30eeedea`
- **论文**：Rational Transductors
- **PDF 事实源**：`corpus/preprints/icml-2026-ef7b30eeedea.pdf`，49 个物理页；正文、参考文献、Appendix A 和 Appendix B 全部读取。全页以 200 dpi 渲染为 1700×2200 PNG，并逐页检查。正文为 p. 1–42，参考文献 p. 43–45，附录 p. 46–49。
- **对象清单口径**：PDF 实际存在 **11 幅 Figure、2 张 Table**。主文 Figure 1–11 和 Table 1；附录无 Figure，Appendix B p. 48 有 Table 2。没有把公式、证明、目录或段落标题误报为视觉对象。

## 1. PDF 对象清单核对

PDF 是对象清单的事实源；`pdftotext`、200 dpi 页面渲染和 PDF 文本/线对象复核得到：

| PDF 标签 | 页 | 模块 | 视觉核对 |
|---|---:|---|---|
| Figure 1 | 5 | method | WFA 状态更新的左右状态列与加权转移箭头 |
| Figure 2 | 7 | method | Rational Head、Attention Stream、逐层投影和并行扫描 |
| Figure 3 | 9 | method | Orthogonal/Stochastic 双头、Concat 与 Universal RT 输出 |
| Figure 4 | 11 | method | Wide Recurrence 与 Deep Recurrence 的双面板拓扑对照 |
| Figure 5 | 15 | theory | Parity 二状态翻转和 Modulo-3 三状态循环自动机 |
| Figure 6 | 23 | theory | h_t 注入 Q/K 后形成虚拟张量化二次项的代数管线 |
| Figure 7 | 36 | results | Modulo-5 regular gap：长度 50 训练到 500 测试 |
| Figure 8 | 37 | results | 长度 40 训练到 1000 测试的泛化曲线 |
| Figure 9 | 39 | results | RNN/RT/Attention 的 log-log latency 曲线 |
| Figure 10 | 40 | results | 长整数加法 exact-match accuracy |
| Figure 11 | 41 | results | Base-2 Float64 MSE 对数柱状图 |
| Table 1 | 13 | theory | Transformer 与 Transductor 的理论能力矩阵 |
| Table 2 | 48 | appendix B | 四类实验的架构和优化超参数 |

Appendix A（p. 46–47）只有定义、定理和证明，没有 Figure/Table；Appendix B（p. 48–49）只有上述 Table 2 和稳定性说明。PDF 内无其他 Figure/Table 标签。`pdfimages -list` 为空，图和表均为 PDF vector objects。

## 2. 视觉源检索

先核查 `reports/tables/visual_source_inventory.csv` 和 `corpus/visual_sources/icml-2026-ef7b30eeedea/`：inventory 旧行是 `no_public_source_found`，本地视觉源目录为空。随后只读使用 `gh`：

- `seshurajup/myclew` 的 `info.json` 以论文完整标题、OpenReview `uEZpyELNuB` 和 arXiv `2602.07599` 严格匹配；`vimarsh244/hf-ICML-2026-agent-repro` README 明确链接 `https://arxiv.org/abs/2602.07599`，trackio 元数据带 `paper-uEZpyELNuB`。
- 选定 `vimarsh244/hf-ICML-2026-agent-repro` 的 commit `00664eca86ec28a8e6a15a66aff4efb646eef4e9` 下 `repro_rational_transductors/paper/source/`：`rbt.tex` 直接引用 7 个 TikZ 图源和 5 个 PDF 图资产，Table 1/2 也在同一 LaTeX 源中。仓库同时提供 `paper/arxiv_source.tar`；解包后所有 listed TikZ 和 `rbt.tex` 与 `paper/source` 副本逐一 `cmp` 相同。
- PDF 本身没有作者 GitHub URL；其他只命中标题的结果没有论文链接或元数据双重匹配，因此没有当作来源。由于完整 LaTeX 图源和被 LaTeX 直接包含的五个矢量图资产都已核实，`source_acquisition.status` 为 `exact_visual_source`。

## 3. 全局视觉系统

- **字体**：正文和数学主要嵌入 `URWPalladioL`/PazoMath/CMSS；TikZ 标签使用 `NimbusSanL`/CMSS；五张结果图使用 `DejaVuSerif`/`DejaVuSans`。图内字体约 5.3–13.3 pt；Table 1 约 10.7 pt，Table 2 经 `resizebox` 后正文约 5.3 pt、表头约 7.3 pt。
- **颜色**：蓝色反复表示 rational state/RT，红色表示 Transformer/RNN 或失败，绿色表示 attention/stochastic/LSTM，橙色表示 WFA sidecar，灰色表示 chance/grid/reference。标记、线型、位置和直接标签多数提供冗余。
- **渲染**：`pdfimages -list` 无嵌入位图；TikZ 结构图、五个 included chart PDF、文本和表格规则均以 vector objects 存在。
- **不确定性**：Figure 7 caption 报告 5 seeds 且 SD < 0.01% 但省略；Figure 8 caption 说明 shaded SD regions 在当前尺度不可见；Figures 9–11 不绘制不确定性；Table 1 是理论 check/cross，Table 2 是配置表。

## 4. 逐对象审计

### Figure 1（p. 5，method，正文）

- **类型/目的/几何**：`network, conceptual_diagram`；purpose=`method_interface, theory_mechanism`；page_width。复杂度 3/5，1 panel，约 4 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–11.0 pt（中位约 8.0）；颜色模式 `categorical`，色数 4，Blue circular nodes and pale blue state braces identify hidden-state components; gray arrows carry transitions, black matrix labels/formula carry the algebra. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=2，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Left/right position encodes previous versus current time step.；y=The two node rows encode state-vector components.；color=Blue node outlines/fills distinguish state nodes from gray transition arrows.；shape=Circles and braces encode vector components and grouped hidden states.；line=Arrow direction and matrix-entry labels encode weighted state transitions; a dashed input connector marks x_t.；facet=无；text=Node labels h_{t-1,i}/h_{t,i}, braces, and the Linear Update formula provide direct semantic labels.。
- **数据/统计**：Mechanism diagram only; it contains no sample, denominator, aggregation, estimate, or uncertainty.
- **与方法/理论/实验关系**：Equation (1) h_t = M_{x_t}h_{t-1} and the sum-of-paths interpretation establish the WFA update intuition used by the architecture in Figure 2 and Section 2.
- **Caption（42 词）**：Figure 1: Visualizing the Rational State Update. The hidden state vector h_t (right) is computed as a linear transformation of the previous state h_{t-1} (left). Each component h_{t,i} aggregates the weighted paths from the previous step, illustrating the "sum of paths" definition.
  - moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：The paired state columns make the one-step transition and component aggregation immediately traceable.；Formula, arrows, braces, and labels redundantly encode the same recurrence.；Vector geometry remains legible without a raster image.
- **缺陷**：Matrix-entry labels cross the diagonal arrows and become small at page scale.；The arrow convention for matrix rows versus columns is not stated inside the diagram.；No uncertainty or data semantics are applicable, so the visual cannot quantify approximation.
- **可复用范式**：Use two aligned state columns with weighted arrows, an input connector, and a compact equation to turn an abstract recurrence into a checkable visual mechanism.

### Figure 2（p. 7，method，正文）

- **类型/目的/几何**：`architecture, pipeline, conceptual_diagram`；purpose=`method_interface, theory_mechanism`；page_width。复杂度 4/5，1 panel，约 10 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–11.0 pt（中位约 8.0）；颜色模式 `mixed`，色数 8，Blue blocks/stream denote transformer semantics, orange denotes the rational WFA state and parallel scan, green projections inject h_t into each layer, and gray connectors denote aggregation; pale fills separate roles. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=2，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Horizontal flow encodes input-to-layer-to-output processing.；y=Vertical placement separates the attention stream, rational head, and layer-specific injection paths.；color=Blue semantic stream, orange WFA state/scan, and green projections encode module ownership.；shape=Rounded blocks encode transformer layers; projection trapezoids and sum nodes encode transformations and merge points.；line=Solid arrows encode data flow; orange dashed Parallel Scan encodes the associative O(log T) state computation.；facet=无；text=Direct labels identify x_t, z_t^(l), h_t, Proj W^(l), and the scan operation.。
- **数据/统计**：Architecture schematic; no observations or statistical aggregation. Complexity is structural rather than a plotted data series.
- **与方法/理论/实验关系**：Sections 2.3 and equations (5)-(6) define the layer-specific projection/injection interface; the orange scan path visualizes the parallel state computation that is contrasted with deep recurrence in Figure 4.
- **Caption（31 词）**：Figure 2: The Rational Transductor Architecture. The Rational Head extracts state variables h_t. These states are injected into the Attention Stream via layer-specific projections W^(l), augmenting the semantic hidden states z_t^(l).
  - moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：The state path and semantic path are visually separated but connected at every layer.；Layer-specific projections make the interface contract explicit.；The scan annotation ties the diagram to the claimed computational mechanism.
- **缺陷**：Many small labels and repeated projection boxes compete for attention.；The diagram does not show tensor dimensions or an explicit causal mask.；Orange/green role colors are not accompanied by a legend, so isolated viewing requires reading labels.
- **可复用范式**：Separate semantic and algebraic streams, then show each injection point with a repeated projection primitive and one explicit complexity annotation.

### Figure 3（p. 9，method，正文）

- **类型/目的/几何**：`architecture, conceptual_diagram`；purpose=`method_interface, theory_mechanism`；page_width。复杂度 3/5，1 panel，约 3 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–10.5 pt（中位约 8.0）；颜色模式 `categorical`，色数 4，Blue top head is Orthogonal/infinite-memory, green bottom head is Stochastic/discrete switching, gray Concat is the merge, and black arrows/text carry structure. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=1，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Left-to-right placement encodes input, parallel head computation, concatenation, and output.；y=Top/bottom position separates the two dynamical biases.；color=Blue versus green identifies the Orthogonal and Stochastic heads.；shape=Head boxes and the vertical Concat bar encode independent branches and direct-sum composition.；line=Solid connectors encode parallel data flow into a shared output.；facet=无；text=Head titles, dynamic icons, Concat, and h_t provide direct labels.。
- **数据/统计**：Universal-architecture concept diagram; no empirical sample, estimate, denominator, or uncertainty is shown.
- **与方法/理论/实验关系**：The direct-sum statement in equation (4) and Section 2.3 is made concrete as parallel Orthogonal and Stochastic heads; the same head roles reappear in Figures 7-8 and 10.
- **Caption（41 词）**：Figure 3: The Universal Rational Transductor. The architecture instantiates parallel heads with distinct dynamical biases: Orthogonal (top) for infinite memory and Stochastic (bottom) for discrete switching. These independent features are concatenated, corresponding to the direct sum (⊕) of the underlying automata.
  - moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：Parallelism and direct-sum composition are visible in one glance.；Head labels state the intended dynamical bias rather than leaving color semantics implicit.；The Concat node makes composition explicit.
- **缺陷**：The icons are qualitative and do not specify parameterization equations.；There is no tensor-size annotation or ablation showing the contribution of either head.；Top/bottom ordering may be mistaken for a hierarchy rather than parallel branches.
- **可复用范式**：Represent a universal model as parallel, explicitly named dynamical heads followed by one concatenation node; pair each color with a textual bias label.

### Figure 4（p. 11，method，正文）

- **类型/目的/几何**：`architecture, conceptual_diagram`；purpose=`method_interface, main_comparison, theory_mechanism`；page_width。复杂度 4/5，2 panel，约 12 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–10.5 pt（中位约 8.0）；颜色模式 `mixed`，色数 10，Panel (a) uses blue transformer blocks, orange WFA state/scan, green injection paths and gray connectors; panel (b) adds red dependency/bottleneck emphasis. Pale fills group branches and black labels anchor the comparison. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=3，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Horizontal position encodes processing order within each architecture.；y=Panel position and vertical layer stacks encode the wide-versus-deep topology.；color=Blue/orange/green identify the wide architecture roles; red highlights the sequential dependency in the deep stack.；shape=Repeated rectangles encode transformer blocks; state boxes, projections, and sidecar stacks encode recurrence placement.；line=Solid arrows show information flow; dashed orange scan/dependency arrows highlight parallel versus sequential computation.；facet=Two panels explicitly facet Wide Recurrence and Deep Recurrence.；text=(a)/(b), Layer labels, h_t, and the red State depends on Layer 1 callout are direct annotations.。
- **数据/统计**：Topology comparison rather than data: no sample size, measured statistic, aggregation, or uncertainty.
- **与方法/理论/实验关系**：Section 2.5 and Propositions/Theorems 2-3 use this wide/deep distinction to connect one parallel scan to O(log T) training versus interleaved sequential recurrence; it motivates later efficiency and generalization results.
- **Caption（57 词）**：Figure 4: Architectural Comparison. (a) Wide Recurrence: The Rational Transductor computes a single high-dimensional state h_t directly from the input via a parallel scan, injecting it into all layers. (b) Deep Recurrence: Stacked architectures (e.g., H3, Mamba) interleave recurrence, where Layer k depends on the output of Layer k − 1, reintroducing a sequential bottleneck during training.
  - moves=`title, setup, comparison, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：The matched two-panel layout isolates recurrence placement as the design variable.；The red dependency callout makes the claimed bottleneck visually falsifiable.；Dashed scan/dependency lines distinguish computational regimes without axes.
- **缺陷**：The phrase high-dimensional state is not quantified by a dimension label.；Examples H3/Mamba are named in text but not structurally disambiguated.；No measured runtime appears in the architecture comparison itself.
- **可复用范式**：Hold model depth and block geometry constant while moving one recurrence primitive from a shared sidecar to interleaved layers, then annotate the resulting dependency difference.

### Figure 5（p. 15，theory，正文）

- **类型/目的/几何**：`network, conceptual_diagram`；purpose=`theory_mechanism, method_interface`；page_width。复杂度 4/5，2 panel，约 6 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–10.0 pt（中位约 8.0）；颜色模式 `categorical`，色数 3，Blue panel encodes parity states and orange panel encodes the modulo-3 cycle; black arrows, input labels, and initial-state markers preserve transition semantics. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=1，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Circular arrangement encodes cyclic state transitions rather than a numeric x-axis.；y=No quantitative y-axis; node placement separates states and transition routes.；color=Blue/orange panel colors distinguish parity and modulo-3 examples.；shape=State circles encode automaton states; self-loops and cross/cyclic arrows encode identity and permutation actions.；line=Arrow direction and labels 0/1 encode symbol-conditioned transitions; an incoming arrow marks h_0.；facet=Two panels facet the 2-state parity and 3-state modulo examples.；text=State numbers, Even/Odd, h_0, and symbol labels are direct semantic text.。
- **数据/统计**：Constructive finite-state diagrams; no sampled observations or uncertainty. The states and transitions are exact symbolic objects.
- **与方法/理论/实验关系**：Theorem 5/6 constructive automata explain why parity and modular counting are exactly representable; Figures 7 and 8 test the corresponding length/generalization claims.
- **Caption（54 词）**：Figure 5: State tracking mechanisms for exact regular languages. (a) The Parity WFA uses a 2-state flip mechanism to track L_parity. (b) The Modulo-3 WFA generalizes this to a cyclic group structure to solve L_k for k = 3. Input “0” acts as the Identity I (self-loop), while input “1” acts as a permutation.
  - moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：The transition labels make the language-recognition mechanism executable by inspection.；Self-loops versus flips/cycles provide shape and direction redundancy.；The two panels scale one construction from two to three states.
- **缺陷**：Only k=2 and k=3 are pictured, so the general k construction remains textual.；Initial-state and accepting-state semantics are not fully distinguished graphically.；The color split is panel-specific rather than a global method key.
- **可复用范式**：Show exact regular-language constructions as small labeled state graphs before plotting their learned length behavior; use symbol labels on every transition.

### Figure 6（p. 23，theory，正文）

- **类型/目的/几何**：`conceptual_diagram, architecture`；purpose=`theory_mechanism, method_interface`；page_width。复杂度 4/5，1 panel，约 8 个数据/结构 mark。
- **字体与颜色**：字体 `NimbusSanL-Regu, NimbusSanL-Bold, CMSS10, CMSSBX10, PazoMath`，约 6.0–10.0 pt（中位约 8.0）；颜色模式 `mixed`，色数 5，Purple blocks and arrows encode rational-state/attention algebra; red dashed callout and pale red fill identify the quadratic interaction; black formulas provide exact symbolic semantics. 灰度安全=True。
- **plot grammar**：vector；x=`none`，y=`none`，grid=`none`；legend=False（无），shared_legend=None；direct_labels=True；marker_types=0，line_styles=2，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.0 pt；provenance=`source_exact`。
- **编码**：x=Left-to-right pipeline encodes h_t/h_t′ injection through projections and attention operations.；y=Vertical alignment pairs Q/K branches before the dot-product interaction.；color=Purple denotes the main algebraic path; red callout color isolates the implicit quadratic term.；shape=Rounded boxes encode operators (W_Q/W_K, Q/K, product), while the tensor-product bracket groups the derived interaction.；line=Solid arrows encode algebraic data flow; red dashed callout lines identify the expanded term.；facet=无；text=Q, K, QK^T, h_t^T M h_t′, and Quadratic Interaction are direct mathematical labels.。
- **数据/统计**：Algebraic mechanism diagram; it contains no experimental sample, denominator, aggregation, or uncertainty.
- **与方法/理论/实验关系**：Section 4.4 derives the virtual tensorization term h_t^T(W_proj^T W_Q^T W_K W_proj)h_t′; the diagram explains how attention gains higher-order interaction without explicitly storing a d^2 state.
- **Caption（56 词）**：Figure 6: Virtual Tensorization. By injecting the linear rational state h_t into the Attention mechanism, the dot product QK^T implicitly computes quadratic terms of the form h_t^T M h_t′. This effectively simulates a kernel over the tensor product space h_t ⊗ h_t′, enabling the model to capture higher-order dependencies without explicitly materializing the O(d^2) state space.
  - moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：The diagram maps every algebraic factor to an operator box.；The red callout makes the claimed implicit expansion visible rather than leaving it as prose.；It links the rational head interface to the attention mechanism in a compact page-width object.
- **缺陷**：The tensor-product space is named but not dimensioned with a concrete example.；The diagram does not separate causal versus non-causal attention paths.；Several formulas are small and require the surrounding derivation for notation resolution.
- **可复用范式**：Use an operator pipeline plus one colored algebraic callout to expose a hidden interaction term and its computational-saving interpretation.

### Figure 7（p. 36，results，正文）

- **类型/目的/几何**：`line`；purpose=`headline, main_comparison, failure, robustness`；inset。复杂度 2/5，1 panel，约 12 个数据/结构 mark。
- **字体与颜色**：字体 `DejaVuSerif, DejaVuSans`，约 6.7–10.7 pt（中位约 9.3）；颜色模式 `categorical`，色数 4，Dark red dashed circles identify the Standard Transformer, dark blue solid triangles identify the Rational Transductor, gray dotted line is random chance, and light gray is the grid. 灰度安全=True。
- **plot grammar**：vector；x=`linear`，y=`linear`，grid=`both`；legend=True（upper_right），shared_legend=False；direct_labels=False；marker_types=2，line_styles=3，hatching=False，reference_lines=1，uncertainty=`none`，line width≈1.5 pt；provenance=`source_exact`。
- **编码**：x=Sequence length at four tested values (50, 100, 300, 500).；y=Accuracy on a linear 0-1 scale.；color=Model identity and chance baseline use dark red, dark blue, and gray.；shape=Circle versus triangle markers distinguish Transformer and Rational Transductor.；line=Dashed Transformer, solid Rational Transductor, and dotted chance lines encode model/baseline roles.；facet=无；text=Legend names all three plotted roles; no direct point labels.。
- **数据/统计**：Four length points per series, accuracy outcome, 5 random seeds; caption reports negligible standard deviation (<0.01%) but the bands/error bars are omitted.
- **与方法/理论/实验关系**：This is the empirical modulo-5 counterpart to Figure 5 and the exact regular-language construction/Theorem 6: the Transformer failure versus the orthogonal RT plateau tests length extrapolation.
- **Caption（92 词）**：Figure 7: The Regular Gap (Modulo-5 Counting). The models are trained on short sequences (L = 50) and evaluated on longer lengths up to L = 500. The Standard Transformer (red) achieves high accuracy on the training distribution but fails to generalize, collapsing to near-random chance (20%) as length increases. The Rational Transductor (blue), leveraging the strictly orthogonal parameterization, learns the exact underlying automaton and maintains 100% accuracy across all tested lengths. Results are averaged over 5 random seeds; standard deviations are negligible (< 0.01%) and omitted for clarity (see Appendix B).
  - moves=`title, setup, comparison, main_finding, uncertainty_definition, appendix_pointer`；self-contained=True；main_finding_stated=True。
- **优点**：The chance reference makes the failure mode immediately interpretable.；Color, marker, and line style redundantly identify both models.；Caption states training/evaluation lengths, seeds, and the main finding.
- **缺陷**：Uncertainty is summarized only in prose and not drawn.；Four x positions provide a sparse view of the transition to failure.；The inset scale leaves tick and legend text small.
- **可复用范式**：Pair a short-training regime with longer evaluation points, add a chance reference, and use orthogonal marker/line encodings so exact-length failure is visible.

### Figure 8（p. 37，results，正文）

- **类型/目的/几何**：`line`；purpose=`headline, main_comparison, failure, robustness`；inset。复杂度 3/5，1 panel，约 8 个数据/结构 mark。
- **字体与颜色**：字体 `DejaVuSerif, DejaVuSans, DejaVuSans-Oblique`，约 6.7–10.7 pt（中位约 9.3）；颜色模式 `categorical`，色数 5，Dark red/blue identify Transformer/RT; gray dotted is chance, darker gray long-dashed is the training horizon, and light gray is the grid. 灰度安全=True。
- **plot grammar**：vector；x=`linear`，y=`linear`，grid=`both`；legend=True（upper_right），shared_legend=False；direct_labels=False；marker_types=2，line_styles=4，hatching=False，reference_lines=2，uncertainty=`band`，line width≈1.5 pt；provenance=`source_exact`。
- **编码**：x=Sequence length with labeled values 40, 100, 500, and 1K.；y=Accuracy on a linear 0-1 scale.；color=Red/blue encode model identity; gray tones encode chance, training horizon, and grid.；shape=Circle and triangle markers distinguish the two model curves.；line=Dashed model line and solid RT line are combined with a vertical long-dashed train-horizon reference.；facet=无；text=The vertical dashed line and legend directly label the training horizon and plotted roles.。
- **数据/统计**：Four evaluation lengths and 5-run accuracy curves; caption states shaded standard-deviation regions exist but are invisible at the rendered scale.
- **与方法/理论/实验关系**：Theorem 6 predicts algebraic length invariance; this figure extends the modulo task from the training horizon to 25x length and complements Figure 7 with a longer range.
- **Caption（83 词）**：Figure 8: Length Generalization. Models were trained only on sequences of length L = 40 (vertical dashed line) and evaluated on lengths up to L = 1000. The Standard Transformer (red) overfits to the training positions; its accuracy collapses to random chance (≈ 20%) on longer sequences. The Rational Transductor (blue) generalizes almost perfectly, maintaining 99% accuracy even at 25× the training length. This validates the algebraic exactness guarantee (Theorem 6). Shaded regions (invisible at this scale) denote standard deviation across 5 runs.
  - moves=`title, setup, comparison, main_finding, uncertainty_definition`；self-contained=True；main_finding_stated=True。
- **优点**：The vertical train-horizon reference makes extrapolation boundary explicit.；The chance line and caption jointly define the failure baseline.；A band is conceptually included even though it is not legible at the final size.
- **缺陷**：Invisible uncertainty bands cannot be inspected or compared.；Only four evaluation points understate the detailed shape of the transition.；The legend does not explain the nearly flat RT curve beyond its name.
- **可复用范式**：Mark the training horizon in the same coordinate system as extrapolation points and reserve a dedicated visual channel for run variability, but ensure it remains visible after publication scaling.

### Figure 9（p. 39，results，正文）

- **类型/目的/几何**：`line`；purpose=`efficiency_cost, main_comparison, headline`；inset。复杂度 3/5，1 panel，约 24 个数据/结构 mark。
- **字体与颜色**：字体 `DejaVuSerif, DejaVuSans`，约 6.7–10.7 pt（中位约 9.3）；颜色模式 `categorical`，色数 4，Dark red is Sequential RNN, dark blue is Rational Transductor, dark green is Standard Attention, and light gray is grid. 灰度安全=True。
- **plot grammar**：vector；x=`log`，y=`log`，grid=`both`；legend=True（lower_right），shared_legend=False；direct_labels=False；marker_types=3，line_styles=2，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.5 pt；provenance=`source_exact`。
- **编码**：x=Sequence length on a log scale with labels 128, 512, 2K, 8K, and 32K.；y=Wall-clock latency in milliseconds on a log scale.；color=Red/blue/green encode RNN/RT/attention.；shape=Circle, triangle, and square markers distinguish the three methods.；line=Dashed RNN versus solid RT/attention lines encode method and scaling role.；facet=无；text=Legend provides method names; asymptotic orders are stated in the caption rather than directly annotated.。
- **数据/统计**：Latency measurements over approximately eight lengths from 128 to 32K; the body describes B=1, A100, 20-100 warm trials, but no error bars or quantiles are drawn.
- **与方法/理论/实验关系**：The efficiency claim connects the parallel associative scan in Sections 2 and 6 to empirical latency, contrasting O(T) sequential recurrence and O(T^2) attention in the isolated sequence-mixer experiment.
- **Caption（70 词）**：Figure 9: Latency vs. Sequence Length. Wall-clock inference latency (ms) on a log-log scale. The Sequential RNN (red) scales linearly (O(T)), becoming prohibitively slow for long sequences. The Transformer (green) exhibits quadratic scaling (O(T^2)), eventually running out of memory. The Rational Transductor (blue) leverages parallel associative scans to achieve sub-linear scaling, outperforming the RNN on sequences longer than T = 512 and maintaining high throughput even at T = 32k.
  - moves=`title, setup, comparison, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：Log-log axes put three scaling regimes on a common visual frame.；Distinct markers retain method identity in grayscale.；The long-length tail makes the claimed crossover visible.
- **缺陷**：No uncertainty or run distribution is shown for wall-clock measurements.；The caption states sub-linear scaling without specifying the measured fit or hardware conditions.；The inset plot and small legend limit exact latency readout.
- **可复用范式**：Use log-log latency curves with method-specific markers and a long-length tail to align asymptotic claims with measured operating cost; report hardware and repetitions alongside the plot.

### Figure 10（p. 40，results，正文）

- **类型/目的/几何**：`line`；purpose=`headline, main_comparison, failure, robustness`；inset。复杂度 2/5，1 panel，约 8 个数据/结构 mark。
- **字体与颜色**：字体 `DejaVuSerif, DejaVuSans`，约 6.7–10.7 pt（中位约 9.3）；颜色模式 `categorical`，色数 3，Dark red dashed circles identify the Standard Transformer, dark blue solid triangles identify the Universal RT, and light gray provides the grid. 灰度安全=True。
- **plot grammar**：vector；x=`linear`，y=`linear`，grid=`both`；legend=True（upper_right），shared_legend=False；direct_labels=False；marker_types=2，line_styles=2，hatching=False，reference_lines=0，uncertainty=`none`，line width≈1.5 pt；provenance=`source_exact`。
- **编码**：x=Number of input digits at 20, 100, 500, and 1000.；y=Exact sequence accuracy on a linear 0-1 scale.；color=Red/blue encode Transformer/Universal RT.；shape=Circle versus triangle markers distinguish the two curves.；line=Dashed Transformer versus solid RT encodes baseline and proposed model.；facet=无；text=Legend names both model curves; values are not directly labeled at points.。
- **数据/统计**：Four length points per model and exact-match accuracy; no error bars, bands, denominator, or seed variability are drawn in the object.
- **与方法/理论/实验关系**：Section 7.4 uses the Universal stochastic head to represent full-adder switching logic; the curve tests the constructive automaton claim beyond the L=20 training distribution.
- **Caption（83 词）**：Figure 10: Experiment D: Long-Integer Addition. Sequence-level accuracy (exact match of the entire sum). The Standard Transformer (red) fits the training distribution (L = 20) but fails completely on longer sequences (0% at L = 100), unable to propagate carry bits over long distances. The Universal Rational Transductor (blue), leveraging a Stochastic head, learns the exact finite state automaton for addition. It generalizes perfectly to L = 1000 digits, demonstrating that the architecture can autonomously learn the correct switching logic for the task.
  - moves=`title, setup, comparison, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：Exact-match y-axis directly matches the task success definition.；The training point and long-length collapse form an easily read failure contrast.；Marker/line redundancy survives grayscale conversion.
- **缺陷**：The training horizon is only described in the caption, not marked by a reference line.；No per-seed or carry-length diagnostic explains the failure mechanism.；The sparse inset cannot show where the baseline first departs from training behavior.
- **可复用范式**：Plot exact-match performance at the training length and several much longer lengths, using a discrete-state model as the positive control and an explicit baseline failure curve.

### Figure 11（p. 41，results，正文）

- **类型/目的/几何**：`bar`；purpose=`headline, main_comparison, failure, robustness`；inset。复杂度 2/5，1 panel，约 3 个数据/结构 mark。
- **字体与颜色**：字体 `DejaVuSans, DejaVuSans-Bold`，约 5.3–13.3 pt（中位约 7.3）；颜色模式 `categorical`，色数 4，Dark green, red, and navy bars identify LSTM, Transformer, and Rational Transductor; gray dashed Random Guessing is the reference baseline. 灰度安全=True。
- **plot grammar**：vector；x=`categorical`，y=`log`，grid=`y`；legend=True（upper_right），shared_legend=False；direct_labels=True；marker_types=0，line_styles=1，hatching=False，reference_lines=1，uncertainty=`none`，line width≈0.8 pt；provenance=`source_exact`。
- **编码**：x=Categorical architecture labels LSTM, Transformer, Rational Transductor.；y=Mean squared error on a logarithmic scale.；color=Bar fill identifies architecture; gray line identifies random guessing.；shape=Rectangular bars encode one aggregate value per architecture.；line=Dashed horizontal reference line encodes the random-guessing baseline.；facet=无；text=Exact scientific-notation values are directly printed above all three bars.。
- **数据/统计**：Three aggregate MSE bars for Float64, L=64 binary evaluation; caption reports approximately 8.4e-2 for LSTM/Transformer and 5.9e-9 for RT, with no uncertainty or replicate distribution.
- **与方法/理论/实验关系**：Section 7.5 tests the affine recurrence promised by the general rational parameterization; the near-zero RT bar contrasts with recurrent/attention baselines and complements the regular-language experiments.
- **Caption（57 词）**：Figure 11: Quantitative Precision (Base-2 Evaluation). We trained models to compute the integer value of binary strings of length L = 64 using double precision. Standard architectures (LSTM, Transformer) fail completely (MSE ≈ 8.4 × 10−2), collapsing to the random-guessing baseline. The Rational Transductor learns the exact affine recurrence, achieving near-perfect precision (MSE ≈ 5.9 × 10−9).
  - moves=`title, setup, comparison, main_finding`；self-contained=True；main_finding_stated=True。
- **优点**：Log y-scale exposes the many-order-of-magnitude precision gap.；Direct values and architecture names remain interpretable without color.；A baseline line makes the failure magnitude concrete.
- **缺陷**：Only one aggregate bar per architecture hides seed and input-level variation.；The dashed reference is the only legend item, so bar-color semantics rely on x labels.；The tiny inset and log tick labels make exact values difficult to read.
- **可复用范式**：For numerical-recursion claims, use a log-scale bar chart with direct scientific-notation labels and a clearly named random baseline.

### Table 1（p. 13，theory，正文）

- **结构/目的**：page_width；purpose=`theory_mechanism, main_comparison`；5 个可见 body rows、4 列、1 层表头、0 个 row group；rules=`booktabs`；highlighting=`none`。
- **字体**：`URWPalladioL-Roma, URWPalladioL-Bold, MnSymbol10, Dingbats`；body≈10.7 pt、header≈10.7 pt、header weight=`bold`，provenance=`pdf_object`。
- **Caption（29 词）**：Table 1: Theoretical comparison of capabilities between finite-depth Transformers and Rational Transductors. Transductors strictly expand expressivity to include all regular languages while sharing the fundamental limitation on context-free grammars.；moves=`title, setup, encoding_key, main_finding`；self-contained=True；main_finding_stated=True。
- **数据/不确定性**：Five task/property rows—Parity, Modular Counting, All Regular Languages, Length Generalization, All Context-Free Languages—compare Transformer and Transductor columns with a theoretical-reason column; values are symbolic checks/crosses rather than samples or aggregates. No empirical uncertainty is present. Check/cross marks encode theoretical capability; the dagger footnote limits the soft-attention TC0 statement to fixed lengths.
- **证据关系**：Section 4 summary and Theorems 5-6 use this matrix to state the expressivity expansion while retaining the context-free limitation; Figure 5 gives the constructive automata behind two rows.
- **优点**：A compact capability matrix makes the theory boundary scanable.；The reason column ties each check/cross to a theorem or limitation.；Booktabs rules and symbolic marks avoid color dependence.
- **缺陷**：The fixed-length qualification is relegated to a dagger footnote.；The table does not distinguish exact recognition from approximation beyond the prose labels.；Symbols require the reader to read the header and footnote for scope.
- **可复用范式**：Use rows for formal language/task classes, columns for competing model families, and a final reason column that binds each symbolic capability mark to a theorem.

### Table 2（p. 48，appendix B，附录）

- **结构/目的**：page_width；purpose=`experimental_design, reproduction`；16 个可见 body rows、5 列、2 层表头、2 个 row group；rules=`booktabs`；highlighting=`italic`。
- **字体**：`URWPalladioL-Roma, URWPalladioL-Bold, URWPalladioL-Italic, MnSymbol10`；body≈5.3 pt、header≈7.3 pt、header weight=`bold`，provenance=`pdf_object`。
- **Caption（12 词）**：Table 2: Hyperparameters for Rational Transductor Experiments. (RT: Rational Transductor, TF: Transformer.)；moves=`title, setup, abbreviation_definition`；self-contained=True；main_finding_stated=False。
- **数据/不确定性**：Sixteen visible body rows include two italic group rows (Model Architecture and Optimization) plus 14 parameter rows. Five task columns report hidden/state dimensions, layers/heads, parameterization, sequence length, optimizer, rates, clipping, steps, loss, and precision. No uncertainty is displayed; this is a configuration specification, not a result table. The Long Addition sequence length U[10,40] is a curriculum sampling rule.
- **证据关系**：Appendix B defines the exact configurations used by Figures 7-11; it enables reproduction but does not provide seeds, raw outcomes, denominators, or evaluator code.
- **优点**：Task-as-column layout makes cross-experiment settings comparable.；Explicit group rows separate architecture from optimization.；The table records the nonstandard curriculum and Float64 choice that materially affect interpretation.
- **缺陷**：The resizebox produces very small body type and long cells.；No seed list, evaluation set size, hardware assignment, or raw data location is included.；Mixed numeric/text precision and RT/TF slash cells make automated extraction difficult.
- **可复用范式**：Keep a common configuration schema across tasks, group architectural and optimization controls, and add seed/evaluation-denominator/artifact columns when publishing a reproducibility table.

## 5. 跨对象系统判断

- **视觉叙事**：Figure 1 establishes the WFA state update; Figures 2-4 place that state beside attention and contrast wide versus deep recurrence; Table 1 and Figures 5-6 turn the mechanism into exact automata and virtual tensorization theory; Figures 7-11 test modulo counting, length extrapolation, latency, addition, and precision; Table 2 collects the appendix configurations.
- **Caption 系统**：Method/theory captions state the object title, mechanism setup, and symbolic interpretation. Result captions add training/evaluation boundary, baseline comparison, and a headline finding; Figures 7-8 also define or point to run variability. Figure 9 has no uncertainty definition, and Table 2 is intentionally a short abbreviation/configuration caption.
- **表头系统**：Table 1 uses one header level with task/property, model-family columns, and a reason column. Table 2 uses two header levels: task names followed by section references, with Config/Task as the row axis and italic architecture/optimization group rows. Both use booktabs-style horizontal rules and no vertical grid.
- **方法—结果—消融关系**：There is no component-ablation Figure/Table. Instead, Figures 5-6 provide constructive/theoretical mechanisms, Figures 7-8 test orthogonal regular-language tracking, Figure 10 tests the stochastic full-adder path, Figure 11 tests the affine path, and Figure 9 tests efficiency. Table 2 links each result to its configuration but does not isolate head-removal counterfactuals.
- **正文—附录关系**：The main body contains every Figure 1-11 and Table 1; Appendix A is text/proofs without a visual object, while Appendix B contributes Table 2 and stability/seed descriptions used to interpret Figures 7-11. The appendix supplies settings, not raw per-seed values or denominators.
- **字体一致性**：Body/caption text uses the Palladio/Computer Modern family; TikZ diagrams use Nimbus/CMSS sans labels and chart assets use DejaVu. The vector medium is consistent, but the font switch and tiny inset/table text reduce cross-object typographic continuity.
- **颜色一致性**：Blue consistently marks rational state/RT, red marks Transformer/RNN or failure, green marks attention/stochastic/LSTM, orange marks WFA sidecars, and gray marks chance/grid/reference. Marker shapes, line styles, panel labels, and direct bar values provide redundancy, though no global legend spans all objects.

## 6. 最终判断

- **最可复用模式**：
  1. State-machine and recurrence diagrams with explicit arrows, symbol labels, braces, and a companion equation make a formal mechanism inspectable.
  1. A concept-to-theory-to-experiment sequence (Figures 1-6 then 7-11) assigns each visual object one role in the proof/evidence chain.
  1. Fixed baseline/proposed color pairs with orthogonal marker and line-style encodings survive grayscale and small-panel reproduction.
  1. Task-as-column hyperparameter tables with grouped architecture/optimization rows provide a compact cross-experiment reproduction contract.
  1. Result captions combine training boundary, extrapolation regime, baseline behavior, main finding, and where variability is defined.
- **最高价值对象**：Figure 2 (architecture interface)；Figure 5 (constructive automata)；Figure 7 (regular-language gap)；Figure 8 (length generalization)；Figure 9 (efficiency scaling)；Figure 11 (quantitative precision)；Table 2 (reproduction configuration)
- **主要失败模式**：
  1. No direct component ablation or head-removal diagnostic isolates the contribution of each Universal RT head.
  1. Several plots omit uncertainty bars/bands; Figure 8 says bands are invisible, and Figure 9 reports no timing spread or fitted scaling uncertainty.
  1. No raw point tables, evaluation denominators, or per-seed outcomes accompany the result plots.
  1. Inset chart labels and the resizeboxed Table 2 body are very small; chart fonts also differ from diagram fonts.
  1. Efficiency and exactness claims are demonstrated on synthetic/isolated tasks and fixed hardware/configurations, so the visuals do not by themselves support broad deployment claims.
- **一句话视觉策略**：以 WFA 状态图建立机制直觉，以统一色彩的结构图和理论表完成定义，再用五张小型矢量实验图把正则语言、长度泛化、效率、加法和数值精度依次闭合，配置细节集中在附录表。

---

**Evidence paths**：PDF `corpus/preprints/icml-2026-ef7b30eeedea.pdf`；文本 `corpus/preprint_text/icml-2026-ef7b30eeedea.txt`；200 dpi renders `/tmp/icml-ef7b30eeedea/render200/page-01.png`–`page-49.png`；verified source tree commit `00664eca86ec28a8e6a15a66aff4efb646eef4e9`.

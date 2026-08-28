# Visual audit — `icml-2026-4f5bde46fdf3`

## 审计范围与 PDF 事实源

- **论文**：*Learning Unmasking Policies for Diffusion Language Models*。
- **PDF**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/preprints/icml-2026-4f5bde46fdf3.pdf`；`pdfinfo` 报告 39 个 Letter 物理页（612×792 pt）。正文为 p.1–13，参考文献跨 p.13–16，附录为 p.17–39。
- **渲染与检查**：全部 39 页用 `pdftoppm -r 200 -png` 渲染为 1700×2200 px/页，并逐页检查；含对象的页面再以同一 200 dpi 分辨率核对布局、字体、图例、轴、颜色、表线与 caption。已用 `pdffonts`、`pdfimages -list` 和 `pdftotext -layout` 交叉核对 PDF 对象。
- **PDF 清单**：33 个 Figure（Figure 1–33）和 5 个 Table（附录打印为 Table 1–5）；另有 Algorithm 1（p.18），按协议记录为上下文但不计入 Figure/Table 数组。reading inventory 与逐页 PDF 对齐，PDF 为最终清单事实源。
- **页图表分布**：Figure 1–9 在正文 p.3–11；Figure 10–33 在附录 p.19–31；Table 1 在 p.35，Tables 2–3 在 p.38，Tables 4–5 在 p.39。

## 公开视觉源核查

- `reports/tables/visual_source_inventory.csv` 对该 paper 的自动行是 `no_public_source_found`；`corpus/visual_sources/icml-2026-4f5bde46fdf3/` 不存在本地视觉源。
- PDF p.1 的 Code 链接为 [`apple/ml-rl-dllm`](https://github.com/apple/ml-rl-dllm)。已用认证 `gh` 读取仓库元数据、README 和 main 的递归 tree；标题/README 与论文精确匹配，仓库含 `common/`、`configs/`、`data/`、`eval/`、`train/` 等实现代码。
- GitHub tree 未发现 `plot*`、`figure*`、`visual*`、`table*`、`.ipynb`、`.tex`、`.tikz`、`.pgf`、`.svg`、style 或论文图表资产；因此状态为 **`repository_without_visual_source`**，未把实现代码冒充为 Figure/Table 源。

## 全文视觉系统

- **main_figures**：9
- **main_tables**：0
- **appendix_figures**：24
- **appendix_tables**：5
- **dominant_figure_typography**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}
- **dominant_table_typography**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}
- **palette_strategy**：Line charts use a recurring categorical palette: gray for Random, blue for High Confidence, orange for Fast-dLLM, green for Ours and purple for Ours/ES, with brown/red/yellow for added baselines or ablations. Blue-to-red sequential colorbars encode early-to-late unmasking time in token grids. Tables remain black/white with booktabs-like rules; header typography is stronger but body cells have no explicit colour or best-value highlighting. Color is often paired with marker/line style or panel position, but most quantitative series still rely substantially on color and are not fully grayscale-safe.
- **vector_raster_mix**：The two-column PDF text, captions, table text/rules and much of the diagram typography are PDF text/vector objects; plot interiors and appendix token grids include embedded raster/image XObjects. The figures are therefore mixed vector/raster overall, while Tables 1–5 are primarily PDF text/rule objects. All 39 pages were rendered at 200 dpi (1700×2200 px) for visual inspection.
- **style_consistency**：Computer Modern/Nimbus Roman body and caption typography, compact legends, repeated gray/blue/orange/green method roles and minimal table rules are consistent across the main paper and appendix. Consistency weakens where appendix replicas add baselines, temperature/seed markers or dense token grids; uncertainty conventions and caption self-containment vary by object.

## 跨对象论证链

- **visual_narrative**：Figure 1 establishes the confidence-heuristic failure when semi-AR block structure is removed; Figure 2 inserts the learned unmasking policy into the frozen dLLM interface; Figure 3 shows reward/compute training dynamics; Figure 4 is the main accuracy–NFE frontier. Figures 5–7 explain block allocation, test-time control and full-diffusion ordering; Figure 8 tests model/domain/length transfer; Figure 9 ablates reward, sampling and inputs. Appendix Figures 10–20 replicate, stress-test and extend those claims, while Figures 21–26 connect selected frontiers to order-level mechanisms and Figures 27–33 provide matched token-grid trajectories. Appendix Tables 1–5 hold configuration and exact NFE–accuracy values.
- **caption_system**：Captions consistently begin with a Figure/Table label and then state the setting, comparison or appendix pointer. Main quantitative captions usually define regime, model, α/τπ and NFE, but primary uncertainty/seed conventions are uneven; captions for qualitative grids are intentionally terse and rely on nearby section text. Several appendix captions directly state the finding, while Figures 1–2 and 8 leave more of the conclusion to the surrounding prose.
- **table_header_system**：All five tables use a compact three-column header. Table 1 uses Category–Parameter–Value with three grouped sections; Tables 2–5 use Method–NFE–Accuracy (%) with six or seven method row groups. Horizontal booktabs-like rules and explicit percentage units form a stable header/body grammar; body cells have no explicit highlighting and there are no vertical cell grids.
- **method_result_ablation_link**：The method interface in Figure 2 and the α/reward dynamics in Figure 3 lead to the main policy frontiers in Figure 4. Figure 5–7 diagnose why the frontier changes, Figure 9 tests the reward/sampling/input design choices, and Appendix Figures 14–16 separate α, seed and τπ effects. Appendix J Tables 2–5 preserve the exact values underlying the plotted method comparisons.
- **main_appendix_link**：Main Figures 1–9 are expanded by direct replicas (10–13, 21), denser control/seed/temperature analyses (14–20), and qualitative order evidence (22–33). Appendix H Table 1 records the training/policy configuration, and Appendix J Tables 2–5 provide exact semi-AR/full-diffusion values for the headline curves.
- **typography_consistency**：Body/caption typography and math symbols are stable Computer Modern/Nimbus forms; plot labels use rasterized sans-serif variants and the pipeline diagram uses SFPro-like display faces. Figure text is generally 5–10 pt at PDF size, with token grids and legends at the lower readability edge; tables are more typographically regular and PDF-object evidence is high.
- **color_consistency**：Gray/blue/orange recur for the three heuristic baselines, green identifies learned policy, and purple identifies expert steering in most Pareto charts. Added baselines and ablations introduce brown/red/yellow locally; sequential blue-to-red is reserved for unmask time. Marker/line style and panel labels provide partial redundancy, but cross-figure color semantics are less strict in training and qualitative panels.

## 全部对象清单

| 类型 | 标签 | PDF 页 | 模块 | 放置 | 视觉职责 |
|---|---|---:|---|---|---|
| Figure | Figure 1 | 3 | §2.2 / motivating comparison | main | headline、failure、main_comparison |
| Figure | Figure 2 | 4 | §3.2 method interface | main | method_interface、theory_mechanism |
| Figure | Figure 3 | 5 | §3.2 policy training | main | experimental_design、mechanism |
| Figure | Figure 4 | 6 | §4.1–§4.2 main results | main | headline、main_comparison、efficiency_cost |
| Figure | Figure 5 | 7 | §4.1 mechanism | main | mechanism、efficiency_cost |
| Figure | Figure 6 | 8 | §4.1 test-time control | main | mechanism、efficiency_cost、robustness |
| Figure | Figure 7 | 9 | §4.2 full-diffusion diagnosis | main | mechanism、failure、qualitative_evidence |
| Figure | Figure 8 | 9 | §4.3 transfer | main | robustness、main_comparison |
| Figure | Figure 9 | 11 | §4.4 ablation | main | ablation、mechanism、robustness |
| Figure | Figure 10 | 19 | Appendix B.1 | appendix | reproduction、failure、robustness |
| Figure | Figure 11 | 19 | Appendix B.2 | appendix | reproduction、main_comparison |
| Figure | Figure 12 | 20 | Appendix B.3 | appendix | reproduction、efficiency_cost |
| Figure | Figure 13 | 20 | Appendix B.4 | appendix | reproduction、main_comparison |
| Figure | Figure 14 | 21 | Appendix B.5 | appendix | robustness、mechanism |
| Figure | Figure 15 | 21 | Appendix B.5 | appendix | robustness、failure |
| Figure | Figure 16 | 22 | Appendix B.6 | appendix | robustness、efficiency_cost、mechanism |
| Figure | Figure 17 | 23 | Appendix B.7 | appendix | robustness、reproduction |
| Figure | Figure 18 | 23 | Appendix B.8 | appendix | robustness、reproduction、efficiency_cost |
| Figure | Figure 19 | 24 | Appendix B.9 | appendix | robustness、main_comparison、efficiency_cost |
| Figure | Figure 20 | 24 | Appendix B.10 | appendix | ablation、mechanism |
| Figure | Figure 21 | 25 | Appendix C overview | appendix | qualitative_evidence、mechanism、reproduction |
| Figure | Figure 22 | 25 | Appendix C.1 | appendix | mechanism、qualitative_evidence |
| Figure | Figure 23 | 26 | Appendix C.1 | appendix | qualitative_evidence、mechanism、failure |
| Figure | Figure 24 | 26 | Appendix C.1 | appendix | mechanism、qualitative_evidence |
| Figure | Figure 25 | 27 | Appendix C.2 | appendix | qualitative_evidence、mechanism、failure |
| Figure | Figure 26 | 27 | Appendix C.3 | appendix | qualitative_evidence、mechanism |
| Figure | Figure 27 | 28 | Appendix D | appendix | qualitative_evidence、mechanism |
| Figure | Figure 28 | 29 | Appendix D | appendix | qualitative_evidence、mechanism |
| Figure | Figure 29 | 29 | Appendix D | appendix | qualitative_evidence、mechanism |
| Figure | Figure 30 | 30 | Appendix D | appendix | qualitative_evidence、mechanism |
| Figure | Figure 31 | 30 | Appendix D | appendix | qualitative_evidence、mechanism |
| Figure | Figure 32 | 31 | Appendix D | appendix | qualitative_evidence、mechanism、failure |
| Figure | Figure 33 | 31 | Appendix D | appendix | qualitative_evidence、mechanism、reproduction |
| Table | Table 1 | 35 | Appendix H | appendix | experimental_design、reproduction |
| Table | Table 2 | 38 | Appendix J | appendix | reproduction、main_comparison、efficiency_cost |
| Table | Table 3 | 38 | Appendix J | appendix | reproduction、main_comparison、efficiency_cost |
| Table | Table 4 | 39 | Appendix J | appendix | reproduction、main_comparison、efficiency_cost |
| Table | Table 5 | 39 | Appendix J | appendix | reproduction、main_comparison、efficiency_cost |

## 逐对象审计

### Figure 1 — p.3，§2.2 / motivating comparison，single_column

- **类型/职责**：`line`；`headline, failure, main_comparison`。
- **Caption/header（PDF 提取）**：Figure 1 LLaDA-8B-Instruct (Nie et al., 2025) on GSM8K, with semi-AR generation (BL = 32; solid) and without (full-diffusion regime, BL = L = 256; dashed). More datasets and models in Appendix B.1. Generation speed is measured in network function evaluations (NFEs), which corresponds to the number of sampling steps.
  - caption moves=`title, setup, encoding_key, comparison, appendix_pointer`；50 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top/inside", "shared_legend": false, "direct_labels": false, "marker_types": 3, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 2, "panels": 1, "series": 3, "legend_items": 5, "annotations": 1, "data_marks_estimate": 36}。
- **编码**：{"x": "NFEs / sampling steps (8–256); shared log-like spacing", "y": "Accuracy (%)", "color": "Random, High Confidence, Fast-dLLM", "shape": null, "line": "solid=semi-AR BL=32; dashed=full-diffusion BL=256", "facet": "none", "text": "panel/line-style legend and caption labels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 7.5, "maximum": 10.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 3, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22"], "semantic_mapping": "灰=Random，蓝=High Confidence，橙=Fast-dLLM；solid/dashed additionally encode semi-AR/full-diffusion。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：GSM8K accuracy versus network function evaluations for LLaDA-8B-Instruct; solid and dashed curves compare semi-AR and full-diffusion regimes. Random has a shaded range in the rendered plot; the caption does not define a replicate count or interval statistic.
- **证据关系**：Introduction/§2.2 identifies the failure of confidence heuristics without blockwise semi-AR; Figure 1 supplies the first visual contrast, which motivates learning a policy and is expanded across models/datasets in Figure 10 and across learned policies in Figure 4.
- **设计优点**：Same axes make the regime reversal immediately legible.；Solid/dashed encoding adds redundancy to the condition labels.；Caption defines NFE and points to broader Appendix B.1 evidence.
- **设计弱点**：Curves and small legend are dense at the low-NFE end.；Random uncertainty is visible but its aggregation is not captioned.；The line-style legend and model/dataset details require careful reading at single-column scale.
- **可复用模式**：Use identical accuracy–compute axes and a redundant line-style encoding to expose a regime-dependent failure before introducing the proposed policy.
- **证据**：PDF p.3，`Figure 1`；basis=`rendered_observation`。

### Figure 2 — p.4，§3.2 method interface，single_column

- **类型/职责**：`pipeline, architecture, conceptual_diagram`；`method_interface, theory_mechanism`。
- **Caption/header（PDF 提取）**：Figure 2 Diagram showing how our policies are used on top of a pretrained dLLM to unmask tokens and generate text.
  - caption moves=`title, setup, encoding_key`；21 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "none", "y_scale": "none", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 1, "series": 1, "legend_items": 0, "annotations": 7, "data_marks_estimate": 0}。
- **编码**：{"x": "left-to-right data flow from masked y_t to generated y_{t−1}", "y": "module/stage lane", "color": "gray frozen dLLM; green unmasking policy; blue token/state examples", "shape": "rounded boxes distinguish model/policy/state", "line": "arrows encode data/control flow", "facet": null, "text": "labels y_t, c_t, u_t and y_{t−1}"}。
- **字体/颜色**：字体 `{"family": ["SFPro-Regular", "SFProDisplay-Bold", "Computer Modern Math"], "size_pt": {"minimum": 5.5, "median": 8.0, "maximum": 11.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 4, "hex": ["#5B6470", "#4F9D69", "#76A9E8", "#D9E2EC"], "semantic_mapping": "灰=冻结 dLLM，绿=unmasking policy，蓝=token/state，黑=箭头与符号；颜色由框中文字冗余。", "redundant_encoding": true, "grayscale_safe": true, "provenance": "rendered_estimate"}`。
- **数据与统计**：Conceptual architecture: a pretrained frozen dLLM supplies masked-token state/confidence c_t to a ~300K unmasking policy, which samples action u_t and returns the next sequence. No observations or uncertainty intervals are plotted.
- **证据关系**：§3.2 formalizes policy inputs, Bernoulli action and frozen base model; Figure 2 is the interface between that MDP description and the training curves in Figure 3 / main Pareto results in Figure 4.
- **设计优点**：Clear vertical pipeline and arrow direction.；Color and shape separate frozen base, learned policy and token states.；Mathematical symbols in the diagram match the method notation.
- **设计弱点**：Small token examples and labels are difficult at page width.；No explicit legend or parameter/shape key; interpretation relies on labels.；Conceptual arrows do not quantify latency or action probabilities.
- **可复用模式**：Show the learned module as a small green policy inserted between a frozen model state and an explicit action/output loop, retaining notation used in equations.
- **证据**：PDF p.4，`Figure 2`；basis=`rendered_observation`。

### Figure 3 — p.5，§3.2 policy training，single_column

- **类型/职责**：`line, area`；`experimental_design, mechanism`。
- **Caption/header（PDF 提取）**：Figure 3 Correctness reward (rolling average, 20 steps) on GSM8K (left) and average number of sampling steps (right) during training of our policies for various values of α (cf. Equation (3.1)). Averaged over two random seeds, with shaded areas indicating (min, max); only one seed shown for α = 10.0 (dotted orange) due to training instability.
  - caption moves=`title, setup, encoding_key, uncertainty_definition, abbreviation_definition`；56 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 5, "legend_items": 5, "annotations": 1, "data_marks_estimate": 1800}。
- **编码**：{"x": "training step (0–900)", "y": "left correctness reward; right mean NFEs", "color": "α∈{10,3,1,0.3,0}", "shape": null, "line": "dotted orange α=10; solid lines for other α", "facet": "two panels: reward and compute", "text": "shared α legend above panels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 5, "hex": ["#E67E22", "#2CA25F", "#2F6DB2", "#7B4FA3", "#C43C39"], "semantic_mapping": "橙/绿/蓝/紫/红依次编码 α=10/3/1/0.3/0；dotted line单独标 α=10。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Two time-series panels show rolling-average correctness reward and mean NFEs during policy training for five regularization values α. Two random seeds are averaged with min–max ribbons; α=10 has one seed because training is unstable.
- **证据关系**：Equation (3.1) defines α; Figure 3 tests reward/compute learning dynamics before Figure 4 evaluates the resulting Pareto policies. The instability and multi-seed caveat are carried forward to Appendix Figures 14–16.
- **设计优点**：Paired reward and compute panels expose the learning trade-off.；Ribbons and explicit seed statement make the main variation visible.；Dotted α=10 line marks the exceptional training condition.
- **设计弱点**：Five trajectories and overlapping ribbons make late-step differences hard to separate.；Min–max is defined in caption but seed imbalance for α=10 limits comparability.；Shared legend consumes the narrow space above both panels.
- **可复用模式**：Pair quality and compute trajectories over the same training x-axis, and visibly mark a seed/instability exception rather than hiding it in prose.
- **证据**：PDF p.5，`Figure 3`；basis=`rendered_observation`。

### Figure 4 — p.6，§4.1–§4.2 main results，double_column

- **类型/职责**：`line, pareto`；`headline, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Figure 4 Results for LLaDA in semi-AR (Figure 4a & Figure 4c) and full-diffusion (Figure 4b & Figure 4d) generation regimes (L = 256). Results for Dream-7B are provided in Figure 13. For our policies we vary α ∈ {10, 3, 1, 0.3, 0} and use τπ = 0.5 for BL = 32 and τπ = 1 for BL = 256. Expert steering (ES) described in detail in Appendix F. Wall-clock time plots shown in Figure 12. For plot readability, we leave out some baselines (Kim et al., 2025a; Ben-Hamu et al., 2025) here and provide the comparison with them in Figure 11.
  - caption moves=`title, setup, encoding_key, comparison, appendix_pointer`；103 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 1, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 5, "legend_items": 5, "annotations": 2, "data_marks_estimate": 340}。
- **编码**：{"x": "NFEs (log-like 8–256)", "y": "Accuracy (%)", "color": "Random, High Confidence, Fast-dLLM, Ours, Ours (ES)", "shape": "circle markers identify sampled Pareto points", "line": "method curves; panel titles encode dataset/regime", "facet": "2×2: GSM8K/MATH-500 × BL=32/256", "text": "panel titles and shared legend"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 5, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3"], "semantic_mapping": "灰=Random，蓝=High Confidence，橙=Fast-dLLM，绿=Ours，紫=Ours (ES)；圆点和 panel regime 提供冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four accuracy–NFE Pareto panels for LLaDA across GSM8K and MATH-500, with semi-AR BL=32 and full-diffusion BL=256. Curves compare three heuristics, learned Ours, and expert-steering Ours (ES); α and τπ settings are given in the caption. Random bands appear in the render, while the caption does not define their statistic.
- **证据关系**：§4.1–§4.2 claim learned policies match strong heuristic performance in semi-AR and improve the full-diffusion frontier; Figure 4 is the central result, with Figures 11–13 adding baselines, wall-clock units and Dream transfer.
- **设计优点**：Same four axes support direct regime and task comparisons.；Method colors and point markers preserve a common Pareto grammar.；Caption records α, temperature, ES and appendix pointers.
- **设计弱点**：Five curves plus bands and four panels create substantial visual load.；Primary policy curves do not show an uncertainty definition or seed count.；Leaving baselines out for readability weakens standalone completeness.
- **可复用模式**：Use a shared 2×2 accuracy–compute frontier with fixed method colors, then move expanded baselines and alternate efficiency units to appendix replicas.
- **证据**：PDF p.6，`Figure 4`；basis=`rendered_observation`。

### Figure 5 — p.7，§4.1 mechanism，single_column

- **类型/职责**：`line, area`；`mechanism, efficiency_cost`。
- **Caption/header（PDF 提取）**：Figure 5 Average number of sampling steps (NFEs) per block for LLaDA on GSM8K with semi-AR generation (same setting as in Figure 4a). Left we show NFEs per block for ‘slow’ variants of Fast-dLLM and policy sampling (∼ 75 NFEs), while in the right plot we show ‘fast’ variants (∼ 10 NFEs). Fast-dLLM exhibits a pattern of allocating more compute to earlier blocks. Our policy sampling, by contrast, distributes compute more uniformly across blocks, except in the fast (α = 10) policy, where most compute is expended in the final block while generating numerical answers. To see where evaluated policies here are located on the pareto frontier, see Figure 21a. More details on qualitative differences between Fast-dLLM and policy sampling are provided in Appendix C.
  - caption moves=`title, setup, encoding_key, comparison, appendix_pointer`；125 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "categorical", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "per-panel top", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 1, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 2, "legend_items": 2, "annotations": 1, "data_marks_estimate": 32}。
- **编码**：{"x": "block index 1–8", "y": "average NFEs per block", "color": "green=policy sampling; orange=Fast-dLLM", "shape": "circles=policy; squares=Fast-dLLM", "line": "solid method trajectories", "facet": "two panels: slow (~75 NFE) and fast (~10 NFE)", "text": "slow/fast panel labels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 2, "hex": ["#2CA25F", "#E67E22"], "semantic_mapping": "绿=policy sampling，橙=Fast-dLLM；圆/方 marker与方法名提供形状冗余。", "redundant_encoding": true, "grayscale_safe": true, "provenance": "rendered_estimate"}`。
- **数据与统计**：Per-block compute allocation for LLaDA/GSM8K semi-AR BL=32. Eight block positions are plotted for slow and fast variants; translucent ribbons show variation, but the caption does not identify the aggregation or replicate count.
- **证据关系**：Figure 5 explains the mechanism behind the Figure 4 frontier: policy compute is more uniform except for the fast α=10 final block, while Fast-dLLM front-loads compute. Appendix C and Figures 23–25 inspect the token-level cause.
- **设计优点**：Block-index alignment makes allocation differences concrete.；Marker shape and color redundantly distinguish the two methods.；Two speed regimes prevent one average curve from masking behavior.
- **设计弱点**：Ribbons overlap and their statistical meaning is omitted.；Only eight blocks from one task/regime are shown.；The fast policy’s final-block behavior needs the caption prose to interpret.
- **可复用模式**：Plot compute allocation by block in paired slow/fast panels and connect the summary curve to token-level qualitative trajectories.
- **证据**：PDF p.7，`Figure 5`；basis=`rendered_observation`。

### Figure 6 — p.8，§4.1 test-time control，single_column

- **类型/职责**：`line, pareto`；`mechanism, efficiency_cost, robustness`。
- **Caption/header（PDF 提取）**：Figure 6 Scaling unmasking probabilites at test-time as u_t^k ∼ Ber(min{1, β · s_t^k}) for β ∈ ℝ_+ leads to smoother pareto frontier compared to changing α (Equation (3.1)) at train-time. Results for LLaDA in semi-AR regime. Note that results for Fast-dLLM and train-time pareto of policy sampling are reproduced from Figure 4.
  - caption moves=`title, setup, encoding_key, comparison`；53 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 3, "legend_items": 3, "annotations": 1, "data_marks_estimate": 100}。
- **编码**：{"x": "NFEs (log-like)", "y": "Accuracy (%)", "color": "orange=Fast-dLLM; green=train-time/test-time policy frontiers", "shape": "circles at frontier points; squares for test-time scaling", "line": "solid=train-time; dashed=test-time", "facet": "GSM8K and MATH-500 panels", "text": "legend distinguishes train/test Pareto"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 3, "hex": ["#E67E22", "#2CA25F", "#9B59B6"], "semantic_mapping": "橙=Fast-dLLM，绿=policy train-time，紫/虚线=test-time β；线型提供干预冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Two semi-AR BL=32 accuracy–NFE frontiers compare Fast-dLLM with policy families obtained by changing α during training versus scaling Bernoulli actions by test-time β. Caption gives the Bernoulli formula but no uncertainty or replicate summary.
- **证据关系**：The controllability claim in §4.1 is that β offers a smoother post-training trade-off than α. Figure 6 places that mechanism on the Figure 4 axes; Appendix Figure 16 further varies policy temperature.
- **设计优点**：Solid/dashed line encoding makes train/test control legible.；Formula in caption anchors the test-time intervention to the method.；Shared axes preserve direct comparison across GSM8K and MATH.
- **设计弱点**：Color similarity between policy variants can obscure curves.；No confidence bands or seed information are shown.；Log-like NFE spacing is not explicitly labeled as log in the caption.
- **可复用模式**：Compare training-time and test-time control on identical Pareto axes, using line style rather than another color family for the intervention.
- **证据**：PDF p.8，`Figure 6`；basis=`rendered_observation`。

### Figure 7 — p.9，§4.2 full-diffusion diagnosis，single_column

- **类型/职责**：`line, area`；`mechanism, failure, qualitative_evidence`。
- **Caption/header（PDF 提取）**：Figure 7 Mean unmasking time for each token position (L = 256), averaged over N = 100 samples, for LLaDA on GSM8K under full-diffusion generation (same setting as in Figure 4b). For visualization purposes, time is shown in reverse. Fast-dLLM (orange) exhibits somewhat reverse (i.e., right-to-left) generation due to LLaDA’s corrupted confidence on padding tokens (see Appendix C). Encouragingly, the expert steering policy (purple) learns to overcome this issue and recovers left-to-right generation (observe how tokens at earlier positions are generated first on average). The locations of the evaluated policies on the Pareto frontier are shown in Figure 21b (see circle markers).
  - caption moves=`title, setup, encoding_key, main_finding, appendix_pointer`；102 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top", "shared_legend": false, "direct_labels": false, "marker_types": 0, "line_styles": 1, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 2, "panels": 1, "series": 3, "legend_items": 3, "annotations": 1, "data_marks_estimate": 256}。
- **编码**：{"x": "token position k (1–256)", "y": "mean unmasking time t (visualized in reverse)", "color": "orange=Fast-dLLM; green=policy; purple=policy with ES", "shape": null, "line": "solid method curves", "facet": null, "text": "legend and caption explain reverse-time display"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 3, "hex": ["#E67E22", "#2CA25F", "#7B4FA3"], "semantic_mapping": "橙=Fast-dLLM，绿=policy，紫=expert steering；caption文字与颜色共同编码。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Position-wise mean unmasking time over N=100 LLaDA/GSM8K full-diffusion samples. Three curves diagnose right-to-left Fast-dLLM behavior versus learned policy and ES recovery of earlier-position-first generation; shaded bands are visible but not statistically defined.
- **证据关系**：Figure 7 supplies a mechanism/failure diagnosis for the full-diffusion gain in Figure 4b: padding-token confidence corrupts Fast-dLLM order, while ES repairs it. Figure 21 identifies the selected policies and Figures 26/31–33 show trajectories.
- **设计优点**：Single aligned curve turns an ordering failure into a readable diagnostic.；Caption states N=100 and explains reverse-time convention.；Policy/ES distinction is visually explicit.
- **设计弱点**：Reversing time for display is easy to miss.；Band semantics and per-sample variability are not defined.；The chart cannot show whether order differences are caused by token type without Appendix C.
- **可复用模式**：Use a position-wise timing curve with an explicit reversed-axis note to connect a frontier result to a generation-order mechanism.
- **证据**：PDF p.9，`Figure 7`；basis=`rendered_observation`。

### Figure 8 — p.9，§4.3 transfer，double_column

- **类型/职责**：`line, pareto`；`robustness, main_comparison`。
- **Caption/header（PDF 提取）**：Figure 8 Results for the transferability experiments. Note that in (a), the α = 10 policy is represented separately by a (green X) in the lower left to avoid misleading visualization when interpolating to α = 3. For results on coding datasets in (b) and (c), we omit the low-NFE regime, as all approaches degrade to near-zero performance in this setting.
  - caption moves=`title, setup, encoding_key, comparison`；61 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 5, "legend_items": 5, "annotations": 2, "data_marks_estimate": 360}。
- **编码**：{"x": "NFEs (log-like; panel d extends to 512)", "y": "Accuracy (%)", "color": "baseline and Ours variants; yellow=KodCode-trained policy where shown", "shape": "green X marks α=10 in panel (a)", "line": "method curves", "facet": "four panels: model, domain and length transfer", "text": "panel titles, task/model labels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 6, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#D9A441"], "semantic_mapping": "灰/蓝/橙为启发式，绿/紫为 learned/ES，黄为 KodCode-trained policy；panel title和X marker冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four transfer panels cover LLaDA→Dream, math→coding (HumanEval/MBPP), and length 256→512. Accuracy is plotted against NFE; coding low-NFE points are omitted because all approaches approach zero. No common uncertainty definition is visible.
- **证据关系**：§4.3 tests whether the learned action policy transfers beyond its training model, domain and length. Figure 8 is the main robustness companion to Figure 4; Figures 17–18 isolate model and length transfer with larger appendix plots.
- **设计优点**：Small multiples separate distinct transfer axes without changing metric grammar.；Panel titles identify model/task/direction and preserve context.；Caption explicitly records omitted low-NFE coding regime and α=10 marker exception.
- **设计弱点**：Four panels use different task scales and can invite false cross-panel magnitude comparisons.；Transfer policies and baselines rely heavily on color.；Omitted low-NFE coding points remove part of the operating range from view.
- **可复用模式**：Use a compact transfer matrix with one panel per shift type, retain common axes where possible, and explicitly mark omitted regimes.
- **证据**：PDF p.9，`Figure 8`；basis=`rendered_observation`。

### Figure 9 — p.11，§4.4 ablation，double_column

- **类型/职责**：`line, bar, pareto`；`ablation, mechanism, robustness`。
- **Caption/header（PDF 提取）**：Figure 9 Ablations for our proposed RL framework. (a) Training reward for LLaDA with additive vs. multiplicative reward function (both α = 1.0). (b) Mean NFEs when training LLaDA with additive vs. multiplicative reward (both α = 1.0). (c) Bernoulli vs DPLS sampling. Both for LLaDA on GSM8K. (d) Bernoulli policies with varying inputs. All for LLaDA on GSM8K.
  - caption moves=`title, setup, encoding_key, comparison`；59 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "unknown", "y_scale": "unknown", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 5, "line_styles": 4, "hatching": false, "reference_lines": 0, "uncertainty_display": "multiple", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 5, "panels": 4, "series": 7, "legend_items": 7, "annotations": 4, "data_marks_estimate": 500}。
- **编码**：{"x": "training step or NFEs depending on panel", "y": "reward, mean NFEs or accuracy (%)", "color": "additive/multiplicative reward; Bernoulli/DPLS; input variants", "shape": "marker/line style distinguish ablation arms", "line": "solid/dashed/dotted arms", "facet": "2×2: reward, compute, sampling distribution, inputs", "text": "panel letters and shared legends"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#C43C39", "#7B4FA3", "#D9A441"], "semantic_mapping": "灰/蓝/橙为 baselines，绿=Ours，红=DPLS或 additive，紫/黄=input variants；marker/line style提供冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four panels test reward formulation, training compute, Bernoulli versus DPLS sampling, and policy input removal/variants. Panels (a,b) show training curves with ribbons; (c,d) show accuracy–NFE or input ablations, with method labels in shared legends.
- **证据关系**：Figure 9 closes the causal chain from Figure 3 training behavior and Figure 6 controllability to implementation choices. It supports the claim that multiplicative reward and Bernoulli inputs are not cosmetic, while Appendix B.10 gives a more direct test-time input deletion.
- **设计优点**：Four targeted ablations share the same policy/result vocabulary.；Paired reward and NFE panels separate objective effect from speed effect.；Panel (d) makes input dependence visible rather than reporting only an aggregate score.
- **设计弱点**：Mixed chart types and multiple legends increase decoding cost.；Some variants have different axis meanings, so a shared visual rhythm can mislead.；Seed/uncertainty detail is concentrated in captions and not uniform across panels.
- **可复用模式**：Organize ablations as a 2×2 matrix that pairs objective and compute diagnostics with sampling and input interventions.
- **证据**：PDF p.11，`Figure 9`；basis=`rendered_observation`。

### Figure 10 — p.19，Appendix B.1，double_column

- **类型/职责**：`line, pareto`；`reproduction, failure, robustness`。
- **Caption/header（PDF 提取）**：Figure 10 Performance comparison with (BL = 32; solid) and without (BL = 256; dashed) semi-AR generation. The same trend observed in Figure 1 holds across all models and datasets: confidence-based heuristics perform well under semi-AR generation but degrade significantly without it.
  - caption moves=`title, setup, encoding_key, main_finding`；42 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 3, "legend_items": 5, "annotations": 3, "data_marks_estimate": 250}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "4 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：same four-panel comparison across LLaDA/Dream and GSM8K/MATH; solid/dashed BL regimes; random bands.
- **证据关系**：Appendix B.1 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Cross-model/dataset replication is compact and directly comparable.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：The four panels repeat many curves and small legends; per-panel sample/seed details remain absent.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Treat a motivating failure as a replication grid before claiming generality.
- **证据**：PDF p.19，`Figure 10`；basis=`rendered_observation`。

### Figure 11 — p.19，Appendix B.2，double_column

- **类型/职责**：`line, pareto`；`reproduction, main_comparison`。
- **Caption/header（PDF 提取）**：Figure 11 Figure 4 reproduced using additional baselines from (Kim et al., 2025a) and (Ben-Hamu et al., 2025). We observe our main findings still hold: our policies mainly match the performance of the best-performing baselines under the semi-AR regime (BL = 32) while outperforming them in the full-diffusion setting (BL = 256).
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；52 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 7, "legend_items": 7, "annotations": 4, "data_marks_estimate": 360}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "4 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Figure 4 layout with Margin and EB Sampler added to the baseline set; shared two-row legend and random ribbons.
- **证据关系**：Appendix B.2 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Additional baselines are inserted without changing axes or method order.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Seven series and two-row legend are crowded; policy uncertainty is not consistently shown.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Add baselines by expanding the legend and preserving the main panel/axis grammar.
- **证据**：PDF p.19，`Figure 11`；basis=`rendered_observation`。

### Figure 12 — p.20，Appendix B.3，double_column

- **类型/职责**：`line, pareto`；`reproduction, efficiency_cost`。
- **Caption/header（PDF 提取）**：Figure 12 Figure 4 reproduced using wall-clock time (in seconds) as the efficiency metric instead of NFEs. The difference in our policy curves (green) when measured in wall-clock time versus NFEs (see Figure 4) is minimal to non-existent, demonstrating the negligible computational overhead of our policy. This low overhead is primarily due to the small size of the unmasking model relative to the base dLLM (300K vs. 8B parameters in the case of LLaDA). All experiments run on an A100 GPUs.
  - caption moves=`title, setup, encoding_key, main_finding`；81 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 5, "legend_items": 5, "annotations": 3, "data_marks_estimate": 340}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "4 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Figure 4 is redrawn with wall-clock seconds on x; same panels, methods, and bands, shared legend.
- **证据关系**：Appendix B.3 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Near-identical layout enables metric substitution audit.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Clock scale and GPU hardware are captioned only briefly; ticks are small and compute overhead is inferred from curves.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Replicate a compute frontier in an operational unit while retaining method and panel identity.
- **证据**：PDF p.20，`Figure 12`；basis=`rendered_observation`。

### Figure 13 — p.20，Appendix B.4，double_column

- **类型/职责**：`line, pareto`；`reproduction, main_comparison`。
- **Caption/header（PDF 提取）**：Figure 13 Results for Dream in semi-AR (Figure 13a & Figure 13c) and full-diffusion (Figure 13b & Figure 13d) generation regimes. For the policies we vary α ∈ {10, 3, 1, 0.3, 0} and use τπ = 0.5 for BL = 32 and τπ = 1 for BL = 256.
  - caption moves=`title, setup, encoding_key`；50 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 5, "legend_items": 5, "annotations": 3, "data_marks_estimate": 340}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "4 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Figure 4 layout for Dream-7B across GSM8K/MATH and BL32/BL256, with policy settings in caption.
- **证据关系**：Appendix B.4 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：The four-regime grid makes model-specific behavior comparable to Figure 4.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：No uncertainty or seed summary is visible; repeated baseline curves create dense overlap.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use a model-specific replica to test whether the method grammar transfers with the result.
- **证据**：PDF p.20，`Figure 13`；basis=`rendered_observation`。

### Figure 14 — p.21，Appendix B.5，single_column

- **类型/职责**：`line, pareto`；`robustness, mechanism`。
- **Caption/header（PDF 提取）**：Figure 14 BL = 32 results for LLaDA with a denser regularization grid, α ∈ {10.0, 9.0, . . . , 1.0, 0.3, 0.0}. Single training seed due to cost; error bars show (min, max) over three test-time seeds. Note that for α ≥ 4.0, the change in NFEs is not monotonic; different values lead to convergence either close to the α = 3.0 policy, or to that of the α = 10.0 policy. Points for policy results are connected by α to emphasize the non-monotone behavior.
  - caption moves=`title, setup, encoding_key, uncertainty_definition, main_finding`；87 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 5, "legend_items": 5, "annotations": 3, "data_marks_estimate": 220}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "2 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Dense α sweep in two BL=32 panels; policy points connected by α, baseline curves and min–max error bars over three test-time seeds.
- **证据关系**：Appendix B.5 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Connected α order plus error bars reveal a failure of monotonicity directly.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Single training seed limits inference about the dense curve; many nearby points are hard to label.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Connect ordered hyperparameter points only when non-monotonicity itself is the claim, and state seed asymmetry.
- **证据**：PDF p.21，`Figure 14`；basis=`rendered_observation`。

### Figure 15 — p.21，Appendix B.5，single_column

- **类型/职责**：`scatter, line, pareto`；`robustness, failure`。
- **Caption/header（PDF 提取）**：Figure 15 BL = 256 (GSM8K) and BL = 32 (MATH-500) results for LLaDA with all training seeds scattered. Even for a fixed value of α, the resulting policy can vary in accuracy and speed due to the randomness of the training procedure. Marker shape denotes the value of α.
  - caption moves=`title, setup, encoding_key, uncertainty_definition, main_finding`；50 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 3, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 5, "legend_items": 5, "annotations": 3, "data_marks_estimate": 260}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "2 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：All training seeds are scattered for BL=256 GSM8K and BL=32 MATH; marker shape encodes α, with baseline frontiers behind the points.
- **证据关系**：Appendix B.5 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Scatter overlay exposes variability hidden by a single mean frontier.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Marker shape/colour combinations are difficult to decode and points overlap.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Add raw training-seed points to a summary frontier when stochastic training is a substantive limitation.
- **证据**：PDF p.21，`Figure 15`；basis=`rendered_observation`。

### Figure 16 — p.22，Appendix B.6，double_column

- **类型/职责**：`line, pareto`；`robustness, efficiency_cost, mechanism`。
- **Caption/header（PDF 提取）**：Figure 16 We study the effect of changing the policy temperature τπ (cf. Section 3.2). For each α ∈ {3, 0.3, 0}, we construct a corresponding test-time Pareto frontier by varying τπ ∈ {1.5, 1.0, 0.5}. Interestingly, in some cases—such as α = 0 with BL = 32—adjusting τπ enables an effective trade-off between compute and performance. Moreover, we find that τπ = 0.5 is optimal in the semi-AR, while τπ = 1 performs best in the full-diffusion (BL = L = 256) setting.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；84 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 5, "legend_items": 7, "annotations": 3, "data_marks_estimate": 520}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "4 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：2×2 GSM8K/MATH × BL32/BL256; green policy curves use solid/dashed/dotted styles for τπ=1/0.5/1.5 while baselines remain fixed.
- **证据关系**：Appendix B.6 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Temperature styles are compared on common axes and linked to α values in caption.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Many green curves and three τπ styles create clutter; no uncertainty bands.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Encode a test-time control parameter with line style while reserving method color for policy identity.
- **证据**：PDF p.22，`Figure 16`；basis=`rendered_observation`。

### Figure 17 — p.23，Appendix B.7，single_column

- **类型/职责**：`line, pareto`；`robustness, reproduction`。
- **Caption/header（PDF 提取）**：Figure 17 Model transfer results. We use policies trained on LLaDA and evaluate them on Dream with τπ = 0.5. Encouragingly, transferred policies give comparable results to training Dream specific policies (cf. Figure 13a & Figure 13c). Note that the α = 10 policy is represented separately by a (green X) in the lower left to avoid misleading visualization when interpolating to α = 3.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；65 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 1, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 4, "legend_items": 4, "annotations": 3, "data_marks_estimate": 160}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "2 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Two BL=32 LLaDA-trained→Dream panels with Random, High Confidence, Fast-dLLM and Ours; α=10 shown as green X.
- **证据关系**：Appendix B.7 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Two panels are less dense than Figure 8 and preserve the same method axes.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Only τπ=0.5 is shown and policy variance is not displayed.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use a focused two-panel transfer check after a broader summary figure.
- **证据**：PDF p.23，`Figure 17`；basis=`rendered_observation`。

### Figure 18 — p.23，Appendix B.8，single_column

- **类型/职责**：`line, pareto`；`robustness, reproduction, efficiency_cost`。
- **Caption/header（PDF 提取）**：Figure 18 BL = L = 256-trained policies from Section 4.2 evaluated with a 2x longer sequence length (BL = L = 512) with τπ = 1. Note that the learned policies yield almost identical performance, while the heuristic methods degrade further compared to L = 256 (cf. Figure 4b & Figure 4d). Both for LLaDA-8B-Instruct.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；56 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 1, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 5, "legend_items": 5, "annotations": 3, "data_marks_estimate": 180}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "2 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Two panels extend x to NFE=512 for 2× sequence length; learned and heuristic policies use the Figure 4 method palette.
- **证据关系**：Appendix B.8 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Longer x range and same axes make extrapolation visible.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：The length change and sample budget are caption-dependent; no confidence region is given.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Stress-test sequence length by preserving metrics and extending the compute axis.
- **证据**：PDF p.23，`Figure 18`；basis=`rendered_observation`。

### Figure 19 — p.24，Appendix B.9，double_column

- **类型/职责**：`line`；`robustness, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Figure 19 We compare our policy (α = 1) sampling with Fast-dLLM (λ = 0.6) in BL = 32 setting under non-greedy decoding (using temperature τ = 0.8). Left: we observe that policy sampling exhibits better scaling in terms of pass@k, indicating that additional stochasticity due to Bernoulli sampling of unmasking decisions can help with exploring the solution space compared to “deterministic” Fast-dLLM. Middle: when the final answer is picked based on majority vote (i.e., self-consistency) policy sampling outperforms Fast-dLLM. Right: when then final answer is picked using an outcome reward model (ORM; Liu et al. 2025b) instead, the policy sampling maintains its edge over Fast-dLLM. For GSM8K, we use a subset of N_test = 300 samples to ease computational burden.
  - caption moves=`title, setup, encoding_key, comparison, main_finding, abbreviation_definition`；121 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "categorical", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "left lower/shared", "shared_legend": true, "direct_labels": false, "marker_types": 1, "line_styles": 1, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 6, "series": 2, "legend_items": 2, "annotations": 6, "data_marks_estimate": 300}。
- **编码**：{"x": "sample count k (1,2,4,8,16,32)", "y": "accuracy (%)", "color": "green policy vs orange Fast-dLLM", "shape": "point markers", "line": "solid method curves", "facet": "task × answer-selection rule", "text": "Δ@1/Δ@32 annotation boxes"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 2, "hex": ["#E67E22", "#2CA25F"], "semantic_mapping": "橙=Fast-dLLM，绿=policy；task and selection rule由facet位置编码，Δ文字提供冗余。", "redundant_encoding": true, "grayscale_safe": true, "provenance": "rendered_estimate"}`。
- **数据与统计**：Six panels (GSM8K/MATH × pass@k/majority vote/ORM); x k=1–32, y accuracy, Fast-dLLM orange vs policy green, Δ annotations.
- **证据关系**：Appendix B.9 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Rows/columns form an interpretable metric-by-task matrix; Δ boxes provide direct effect annotations.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Six small panels and repeated y labels are dense; k-axis and ORM abbreviations require caption reading.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Place decoding/selection robustness in a row×column matrix with direct delta annotations.
- **证据**：PDF p.24，`Figure 19`；basis=`rendered_observation`。

### Figure 20 — p.24，Appendix B.10，single_column

- **类型/职责**：`bar`；`ablation, mechanism`。
- **Caption/header（PDF 提取）**：Figure 20 We perform (test-time) ablations on the policy inputs during generation. We use policy trained with α = 1 on LLaDA with BL = 32. Concretely, we set to zero either i) time (t), ii) masks (m_t), or iii) both. We report drops in accuracy as (negative) bars and display the change in average NFEs as text underneath each bar. We observe that zeroing out part of the input leads to reduced performance in all cases, except when zeroing out only time on GSM8K. Interestingly, zeroing out time or masks seems to have a minimal impact on the speed of the policy (speed changes at most for 1.2 NFEs on average).
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；112 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "categorical", "y_scale": "linear", "grid": "both", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": false, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 1, "uncertainty_display": "none", "line_width_pt": 0.8, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 3, "legend_items": 3, "annotations": 3, "data_marks_estimate": 6}。
- **编码**：{"x": "input ablation condition", "y": "accuracy change (%)", "color": "−t, −m_t, −t,m_t", "shape": null, "line": null, "facet": "GSM8K/MATH-500", "text": "NFE change printed under each bar"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 3, "hex": ["#E67E22", "#C43C39", "#8C564B"], "semantic_mapping": "三种输入删除条件由橙/红/棕柱和条件标签编码；NFE变化用文字而非第二轴。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Grouped negative accuracy-change bars for GSM8K and MATH-500 under −t, −m_t, and −t,m_t; NFE changes printed below bars.
- **证据关系**：Appendix B.10 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Baseline text and NFE annotations prevent bars from conflating two metrics.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Negative bars and small annotations require a zero baseline; color is the main condition key.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use paired bar groups with a secondary text annotation when the intervention affects quality and compute differently.
- **证据**：PDF p.24，`Figure 20`；basis=`rendered_observation`。

### Figure 21 — p.25，Appendix C overview，single_column

- **类型/职责**：`line, pareto`；`qualitative_evidence, mechanism, reproduction`。
- **Caption/header（PDF 提取）**：Figure 21 Results for LLaDA in semi-AR (BL = 32; replicated from Figure 4a) and full-diffusion (BL = 256; figure replicated from Figure 4b) generation regimes. We highlight the policies used in our qualitative analysis of unmasking orders: red circle for BL32-slow, black circle for BL32-fast, and brown circle for BL256.
  - caption moves=`title, setup, encoding_key, comparison`；51 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "log", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 3, "line_styles": 3, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 2, "series": 5, "legend_items": 5, "annotations": 5, "data_marks_estimate": 180}。
- **编码**：{"x": "NFEs or wall-clock time depending on the replica", "y": "Accuracy (%)", "color": "method identity; appendix-specific variants in green/purple/yellow", "shape": "circle/X/seed markers where stated", "line": "solid/dashed regimes or interventions", "facet": "2 panels", "text": "panel titles, legends and selected-policy markers"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 7, "hex": ["#6B6B6B", "#2F6DB2", "#E67E22", "#2CA25F", "#7B4FA3", "#8C564B", "#D9A441"], "semantic_mapping": "Appendix replicates preserve the main method palette; line style encodes regime/control and marker shape encodes seeds or selected policies.", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Two replicated Pareto panels highlight three policies with red/black/brown circle outlines for the qualitative trajectory selections.
- **证据关系**：Appendix C overview extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Colored outline markers bridge quantitative and qualitative sections without adding a new metric.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Marker outlines can be overlooked under dense curves; caption does not repeat exact NFE/accuracy.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Mark the representative policies on a reproduced frontier before showing qualitative traces.
- **证据**：PDF p.25，`Figure 21`；basis=`rendered_observation`。

### Figure 22 — p.25，Appendix C.1，single_column

- **类型/职责**：`line, area`；`mechanism, qualitative_evidence`。
- **Caption/header（PDF 提取）**：Figure 22 Spearman rank correlation between the unmasking orders of Fast-dLLM and our RL policies per block for semi-AR policies considered here. Note that for certain blocks, the unmasking orders exhibit zero correlation: first and last block for BL32-fast (black circle), and last block for BL32-slow (red circle).
  - caption moves=`title, setup, encoding_key, uncertainty_definition, main_finding`；48 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "categorical", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top", "shared_legend": true, "direct_labels": false, "marker_types": 2, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "band", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 1, "series": 2, "legend_items": 2, "annotations": 2, "data_marks_estimate": 16}。
- **编码**：{"x": "block index", "y": "Spearman correlation", "color": "BL32-slow/fast", "shape": null, "line": "colored curves with bands", "facet": null, "text": "zero-correlation note or diagonal"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 2, "hex": ["#C43C39", "#222222"], "semantic_mapping": "红=BL32-slow，黑=BL32-fast", "redundant_encoding": true, "grayscale_safe": true, "provenance": "rendered_estimate"}`。
- **数据与统计**：Block index 1–8 versus Spearman correlation, with BL32-slow red and BL32-fast black curves and translucent bands; zero-correlation blocks are called out by caption.
- **证据关系**：Appendix C.1 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Correlation summary gives a compact bridge from order trajectories to mechanism.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Correlation uncertainty and sample aggregation are not defined in the caption; low series count limits generality.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Summarize order similarity by block before displaying representative trajectories.
- **证据**：PDF p.25，`Figure 22`；basis=`rendered_observation`。

### Figure 23 — p.26，Appendix C.1，double_column

- **类型/职责**：`line`；`qualitative_evidence, mechanism, failure`。
- **Caption/header（PDF 提取）**：Figure 23 BL32-slow: unmasking orders for policy sampling (o_α=0.3) and Fast-dLLM (o_λ=0.9) for four GSM8K test samples under semi-AR generation (BL=32, L=256). Vertical dashed lines indicate position where model outputs EOS. Interestingly, Fast-dLLM appears more effective at accelerating generation after producing EOS, whereas policy sampling tends to sometimes waste compute by not unmasking all padding tokens (within current block) after EOS in parallel, see third test sample.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；67 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 0, "line_styles": 1, "hatching": false, "reference_lines": 1, "uncertainty_display": "none", "line_width_pt": 0.8, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 2, "legend_items": 2, "annotations": 4, "data_marks_estimate": 1024}。
- **编码**：{"x": "token position", "y": "unmasking order/time", "color": "policy vs Fast-dLLM and ES", "shape": null, "line": "step/trajectory lines", "facet": "four test samples", "text": "EOS vertical rule"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 2, "hex": ["#2CA25F", "#E67E22"], "semantic_mapping": "绿=policy，橙=Fast-dLLM，紫=ES（仅 Figure 26）；EOS/面板标题提供冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four sample panels show token position versus unmasking order for BL32-slow policy α=.3 and Fast-dLLM λ=.9; vertical dashed EOS lines.
- **证据关系**：Appendix C.1 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Per-sample panels preserve concrete trajectories and an EOS reference.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Step-like dense traces are hard to read at full page; only four samples are shown.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Show representative trajectories in small multiples with an explicit terminal/EOS reference.
- **证据**：PDF p.26，`Figure 23`；basis=`rendered_observation`。

### Figure 24 — p.26，Appendix C.1，single_column

- **类型/职责**：`scatter`；`mechanism, qualitative_evidence`。
- **Caption/header（PDF 提取）**：Figure 24 BL32-slow: for each of N=100 samples, report frequency of tokens whose right-adjacent token was unmasked at same sampling step under Fast-dLLM versus policy sampling. Policy sampling unmasks adjacent tokens much less frequently than Fast-dLLM.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；36 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": null, "shared_legend": false, "direct_labels": false, "marker_types": 0, "line_styles": 1, "hatching": false, "reference_lines": 1, "uncertainty_display": "none", "line_width_pt": 1.0, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 3, "panels": 1, "series": 1, "legend_items": 1, "annotations": 2, "data_marks_estimate": 100}。
- **编码**：{"x": "policy adjacent-token frequency", "y": "Fast-dLLM adjacent-token frequency", "color": "sample points", "shape": null, "line": "none", "facet": null, "text": "zero-correlation note or diagonal"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 1, "hex": ["#2F6DB2"], "semantic_mapping": "蓝点=100 matched samples；dashed diagonal is equality.", "redundant_encoding": true, "grayscale_safe": true, "provenance": "rendered_estimate"}`。
- **数据与统计**：Scatter of adjacent-token same-step frequency for Fast-dLLM (y) versus policy (x) across N=100 samples; dashed diagonal y=x.
- **证据关系**：Appendix C.1 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Diagonal reference and 100 sample points make the direction of disagreement obvious.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：Point cloud lacks density summary or overplot handling; frequencies and sampling unit are caption-dependent.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Pair two synchronization statistics around a y=x reference to expose systematic ordering differences.
- **证据**：PDF p.26，`Figure 24`；basis=`rendered_observation`。

### Figure 25 — p.27，Appendix C.2，double_column

- **类型/职责**：`line`；`qualitative_evidence, mechanism, failure`。
- **Caption/header（PDF 提取）**：Figure 25 BL32-fast: unmasking orders for policy sampling (o_α=10) and Fast-dLLM (o_λ=0.1) for four GSM8K test samples under semi-AR generation (BL=32,L=256). Under low-NFE constraints, both strategies often predict all tokens within a block simultaneously (flat lines). In final block, numerical answer policy slows down.
  - caption moves=`title, setup, encoding_key, comparison, main_finding`；44 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`True`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 0, "line_styles": 1, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.8, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 2, "legend_items": 2, "annotations": 4, "data_marks_estimate": 1024}。
- **编码**：{"x": "token position", "y": "unmasking order/time", "color": "policy vs Fast-dLLM and ES", "shape": null, "line": "step/trajectory lines", "facet": "four test samples", "text": "sample labels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 2, "hex": ["#2CA25F", "#E67E22"], "semantic_mapping": "绿=policy，橙=Fast-dLLM，紫=ES（仅 Figure 26）；EOS/面板标题提供冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four BL32-fast sample panels compare policy α=10 with Fast-dLLM λ=.1; step-like unmasking order curves.
- **证据关系**：Appendix C.2 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Common axes make flat simultaneous predictions visible.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：The dense trajectories and no uncertainty summary limit extrapolation beyond four samples.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use low-budget representative traces to explain why a frontier endpoint behaves differently.
- **证据**：PDF p.27，`Figure 25`；basis=`rendered_observation`。

### Figure 26 — p.27，Appendix C.3，double_column

- **类型/职责**：`line`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 26 BL256: unmasking orders for policy sampling (o_α=0.3) and Fast-dLLM (o_λ=0.9) for four GSM8K test samples under full-diffusion generation (BL=256, L=256).
  - caption moves=`title, setup, encoding_key, comparison`；22 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "mixed", "x_scale": "linear", "y_scale": "linear", "grid": "both", "legend_present": true, "legend_placement": "top shared", "shared_legend": true, "direct_labels": false, "marker_types": 0, "line_styles": 2, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.8, "provenance": "mixed"}。
- **面板与复杂度**：{"score": 4, "panels": 4, "series": 3, "legend_items": 3, "annotations": 4, "data_marks_estimate": 1024}。
- **编码**：{"x": "token position", "y": "unmasking order/time", "color": "policy vs Fast-dLLM and ES", "shape": null, "line": "step/trajectory lines", "facet": "four test samples", "text": "sample labels"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "categorical", "color_count": 3, "hex": ["#2CA25F", "#E67E22", "#7B4FA3"], "semantic_mapping": "绿=policy，橙=Fast-dLLM，紫=ES（仅 Figure 26）；EOS/面板标题提供冗余。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Four BL256 sample panels compare policy α=.3, Fast-dLLM λ=.9 and policy ES; unmasking order versus position.
- **证据关系**：Appendix C.3 extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Three-method overlay links ES to the non-ES policy and heuristic in the same samples.；Caption identifies the intervention, regime or sampling unit needed to read the object.
- **设计弱点**：No uncertainty and only four samples; overlapping noisy curves are visually demanding.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Overlay heuristic, learned and steered trajectories on shared samples to attribute a qualitative gain.
- **证据**：PDF p.27，`Figure 26`；basis=`rendered_observation`。

### Figure 27 — p.28，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 27 BL32-slow: generation trajectory for policy sampling (α=0.3, semi-AR).
  - caption moves=`title, setup, encoding_key, comparison`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 8, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Token grid with B=1–8 block rows, token text/time cells, and blue→red within-block unmasking-time colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Colorbar and block labels make the temporal order inspectable.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Tiny token text and many cells are difficult to audit; no legend for padding/token categories.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use a fixed token-cell grid and sequential time colorbar for qualitative order evidence.
- **证据**：PDF p.28，`Figure 27`；basis=`rendered_observation`。

### Figure 28 — p.29，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 28 BL32-slow: generation trajectory for Fast-dLLM sampling (λ=0.9, semi-AR).
  - caption moves=`title, setup, encoding_key`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 8, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：Same BL32-slow token grid for Fast-dLLM λ=.9, with block rows, token/time cells and blue→red within-block colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Identical geometry permits cell-by-cell comparison with the policy grid.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Repeated tiny text and color-only temporal encoding are demanding in grayscale.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Keep paired qualitative grids geometrically identical to support matched visual comparison.
- **证据**：PDF p.29，`Figure 28`；basis=`rendered_observation`。

### Figure 29 — p.29，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 29 BL32-fast: generation trajectory for policy sampling (α=10, semi-AR).
  - caption moves=`title, setup, encoding_key`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 8, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：BL32-fast policy α=10 token grid; mostly early blue cells with late-block warm cells and a sequential colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Same grid as Figures 27–28 preserves comparison.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Warm/cool cells are small and the trajectory needs the caption/preceding figures for interpretation.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use identical qualitative-grid dimensions across speed regimes, changing only the trajectory source.
- **证据**：PDF p.29，`Figure 29`；basis=`rendered_observation`。

### Figure 30 — p.30，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 30 BL32-fast: generation trajectory for Fast-dLLM sampling (λ=0.1, semi-AR).
  - caption moves=`title, setup, encoding_key`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 8, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：BL32-fast Fast-dLLM λ=.1 grid with block rows and blue→red unmask-time colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：The pair makes simultaneous block predictions visually comparable.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Dense cell labels and similar blue fields make small timing differences hard to see.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Present matched heuristic/policy grids side by side or on adjacent pages with unchanged color semantics.
- **证据**：PDF p.30，`Figure 30`；basis=`rendered_observation`。

### Figure 31 — p.30，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism`。
- **Caption/header（PDF 提取）**：Figure 31 BL256: generation trajectory for policy sampling (α=0.3, full-diffusion).
  - caption moves=`title, setup, encoding_key`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 16, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：BL256 policy α=.3 full-diffusion grid, 16×16 token cells with global blue→red time colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Full sequence grid retains spatial position and generation time in one object.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Small cells and token strings are barely legible at page scale; no uncertainty or multiple samples.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Use a square token lattice when spatial position and global unmasking time must be seen together.
- **证据**：PDF p.30，`Figure 31`；basis=`rendered_observation`。

### Figure 32 — p.31，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism, failure`。
- **Caption/header（PDF 提取）**：Figure 32 BL256: generation trajectory for Fast-dLLM sampling (λ=0.9, full-diffusion).
  - caption moves=`title, setup, encoding_key`；10 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 16, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：BL256 Fast-dLLM λ=.9 16×16 grid with global sequential time colorbar; late warm regions contrast with early blue rows.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Matched lattice and colorbar permit direct comparison with policy Figure 31.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：Token/cell density is high and color remains the dominant timing code.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Pair a full-sequence heuristic heatmap with the learned-policy lattice to expose order failure.
- **证据**：PDF p.31，`Figure 32`；basis=`rendered_observation`。

### Figure 33 — p.31，Appendix D，double_column

- **类型/职责**：`qualitative_grid, heatmap`；`qualitative_evidence, mechanism, reproduction`。
- **Caption/header（PDF 提取）**：Figure 33 BL256: generation trajectory for policy sampling (α=0.3, expert steering, full-diffusion).
  - caption moves=`title, setup, encoding_key`；12 词；headline_bold=`False`；self_contained=`True`；main_finding_stated=`False`。
- **绘图语法**：{"rendering": "raster", "x_scale": "categorical", "y_scale": "categorical", "grid": "none", "legend_present": false, "legend_placement": null, "shared_legend": null, "direct_labels": true, "marker_types": 0, "line_styles": 0, "hatching": false, "reference_lines": 0, "uncertainty_display": "none", "line_width_pt": 0.0, "provenance": "rendered_estimate"}。
- **面板与复杂度**：{"score": 5, "panels": 16, "series": 1, "legend_items": 0, "annotations": 2, "data_marks_estimate": 256}。
- **编码**：{"x": "token/cell position", "y": "block row or token position", "color": "unmasking time within block/global time", "shape": "cell rectangles", "line": null, "facet": "block rows and token cells", "text": "token strings and time indices"}。
- **字体/颜色**：字体 `{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "SFPro-Regular", "Arimo", "Computer Modern Math"], "size_pt": {"minimum": 5.0, "median": 8.0, "maximum": 12.0}, "weight": ["regular", "bold"], "style": ["roman", "italic"], "provenance": "mixed", "confidence": "medium"}`；颜色 `{"mode": "sequential", "color_count": 8, "hex": ["#2166AC", "#67A9CF", "#D1E5F0", "#FDDDAA", "#F4A582", "#D6604D", "#B2182B", "#762A83"], "semantic_mapping": "蓝→红顺序色带编码早→晚 unmasking time；block标签、token文字和单元格形状提供位置冗余，但定量读数仍依赖颜色。", "redundant_encoding": true, "grayscale_safe": false, "provenance": "rendered_estimate"}`。
- **数据与统计**：BL256 policy α=.3 with expert steering, 16×16 grid and global blue→red colorbar.
- **证据关系**：Appendix D extends the corresponding main-paper result or mechanism with the appendix condition named in the caption; it links back to Figures 1–9 and forward to the exact configuration/value tables where applicable.
- **设计优点**：Same lattice as Figures 31–32 isolates the effect of expert steering.；Fixed token lattice and sequential colorbar preserve the order encoding.
- **设计弱点**：No quantitative summary or replicate variation is embedded; tiny text limits standalone reading.；Some uncertainty, seed or sampling details are not encoded in the object.
- **可复用模式**：Hold the qualitative grid fixed while changing only the steering intervention.
- **证据**：PDF p.31，`Figure 33`；basis=`rendered_observation`。

### Table 1 — p.35，Appendix H，double_column

- **类型/职责**：``；`experimental_design, reproduction`。
- **Caption/header（PDF 提取）**：Table 1 Training and policy configuration for our main experiments.
  - caption moves=`title, setup`；10 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **表头与结构**：rows=18，columns=3，header_levels=1，row_groups=3，decimal_precision=None，rules=`booktabs`，highlighting=`none`。
- **表格字体**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}。
- **数据与统计**：Three-column Category–Parameter–Value configuration table. Training has 7 rows, GRPO 5 rows and Policy Network 6 rows; values include learning rate, batch size, reward description and 300K parameter count.
- **证据关系**：Appendix H documents the settings behind Figures 3–9 and the main Pareto curves; it is the reproducibility anchor for the policy and GRPO implementation.
- **设计优点**：Booktabs-like horizontal rules and grouped category rows make a long configuration list scannable.；One value column avoids mixing units across metrics.
- **设计弱点**：Mixed numeric/text values make a single precision summary artificial.；The table does not expose random seeds, hardware or all evaluation settings.
- **可复用模式**：Use a three-column grouped configuration table to make the training/policy interface auditable without turning every parameter into prose.
- **证据**：PDF p.35，`Table 1`；basis=`pdf_object`。

### Table 2 — p.38，Appendix J，single_column

- **类型/职责**：``；`reproduction, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Table 2 BL = 32, GSM8K.
  - caption moves=`title, setup`；6 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **表头与结构**：rows=41，columns=3，header_levels=1，row_groups=6，decimal_precision=1，rules=`booktabs`，highlighting=`none`。
- **表格字体**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}。
- **数据与统计**：Method–NFE–Accuracy (%) table with 41 body rows: Random, High Conf., Fast-dLLM, Margin, EB Sampler and Ours. NFE is the efficiency column and Accuracy is the task outcome; Ours uses values such as 10.3/35.2±0.3 through 135.8/80.5±0.5.
- **证据关系**：Appendix J supplies exact values for the BL=32 GSM8K curves in Figures 1, 4, 6, 11 and 21, allowing the rendered frontier to be checked numerically.
- **设计优点**：Method row groups preserve the comparison order used in the plots.；Separate NFE and Accuracy headers expose the quality–compute decision pair.
- **设计弱点**：Long repeated method blocks are harder to scan than the frontier plot.；Baseline uncertainty and the definition of ± are not uniform across rows.
- **可复用模式**：Pair exact NFE and accuracy columns with method row groups so plotted Pareto points can be reproduced.
- **证据**：PDF p.38，`Table 2`；basis=`pdf_object`。

### Table 3 — p.38，Appendix J，single_column

- **类型/职责**：``；`reproduction, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Table 3 BL = 32, MATH.
  - caption moves=`title, setup`；6 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **表头与结构**：rows=41，columns=3，header_levels=1，row_groups=6，decimal_precision=1，rules=`booktabs`，highlighting=`none`。
- **表格字体**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}。
- **数据与统计**：Same 41-row Method–NFE–Accuracy (%) structure as Table 2 for MATH at BL=32. Groups are Random, High Conf., Fast-dLLM, Margin, EB Sampler and Ours.
- **证据关系**：It is the exact numerical companion to the MATH semi-AR panels in Figures 4, 6, 11, 13 and 21, separating visual interpolation from reported values.
- **设计优点**：Identical header and group order with Table 2 supports task comparison.；Percentage unit is explicit in the header.
- **设计弱点**：Repeating many rows across two tables increases lookup burden.；Uncertainty notation is sparse and not defined in the caption.
- **可复用模式**：Duplicate the exact-value table layout across tasks so differences are attributable to values rather than table grammar.
- **证据**：PDF p.38，`Table 3`；basis=`pdf_object`。

### Table 4 — p.39，Appendix J，single_column

- **类型/职责**：``；`reproduction, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Table 4 BL = 256, GSM8K.
  - caption moves=`title, setup`；6 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **表头与结构**：rows=44，columns=3，header_levels=1，row_groups=7，decimal_precision=1，rules=`booktabs`，highlighting=`none`。
- **表格字体**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}。
- **数据与统计**：Method–NFE–Accuracy (%) table with 44 body rows across Random, High Conf., Fast-dLLM, Margin, EB Sampler, Ours and Ours (ES). Full-diffusion Ours includes 13.0/48.3±0.6 through 135.8/80.5±0.5; ES includes 15.7/50.6±0.8 through 87.9/75.1±0.1.
- **证据关系**：It provides exact full-diffusion GSM8K values for the main gain in Figure 4b, the ES curve and the Appendix replicas/qualitative selections.
- **设计优点**：Adds ES as a separate method group while retaining the established columns.；Exact values make the full-diffusion quality–NFE trade-off auditable.
- **设计弱点**：Seven method blocks make the page dense.；Asymmetric uncertainty reporting makes cross-method variance comparisons difficult.
- **可复用模式**：Extend the common exact-value table with an explicit intervention row when steering changes the frontier.
- **证据**：PDF p.39，`Table 4`；basis=`pdf_object`。

### Table 5 — p.39，Appendix J，single_column

- **类型/职责**：``；`reproduction, main_comparison, efficiency_cost`。
- **Caption/header（PDF 提取）**：Table 5 BL = 256, MATH.
  - caption moves=`title, setup`；6 词；headline_bold=`False`；self_contained=`False`；main_finding_stated=`False`。
- **表头与结构**：rows=44，columns=3，header_levels=1，row_groups=7，decimal_precision=1，rules=`booktabs`，highlighting=`none`。
- **表格字体**：{"family": ["Computer Modern Roman", "Nimbus Roman No9 L", "Computer Modern Math"], "body_size_pt": 8.5, "header_size_pt": 8.5, "header_weight": "bold", "provenance": "pdf_object", "confidence": "high"}。
- **数据与统计**：Same 44-row Method–NFE–Accuracy (%) structure as Table 4 for MATH at BL=256, with Ours and Ours (ES) groups separated from heuristic baselines.
- **证据关系**：It is the exact numerical companion to the MATH full-diffusion panels in Figures 4d, 11, 13 and 21, and records the ES intervention values.
- **设计优点**：Shared table grammar makes BL=256 GSM8K/MATH lookups direct.；Method groups expose the additional ES comparison rather than folding it into Ours.
- **设计弱点**：Dense rows and small type slow per-cell comparisons.；No explicit denominator or seed count appears in the table.
- **可复用模式**：Keep an intervention-specific method group in the exact appendix table so the plotted frontier remains reconstructable.
- **证据**：PDF p.39，`Table 5`；basis=`pdf_object`。

## 最终判断

- **most_reusable_patterns**：
  - Use a failure-first accuracy–compute frontier (Figure 1), then a frozen-model/learned-policy interface (Figure 2), followed by training dynamics and matched Pareto panels.
  - Keep method identity fixed in color and use line style, marker or panel position for regime and test-time control.
  - Pair aggregate mechanism curves with matched sample-level trajectories and fixed token grids to explain why a frontier changes.
  - Move exact NFE–accuracy values and configuration into grouped appendix tables without changing method order or metric headers.
- **highest_value_objects**：
  - Figure 1
  - Figure 2
  - Figure 4
  - Figure 5
  - Figure 7
  - Figure 9
  - Figure 22
  - Figure 26
  - Table 1
  - Tables 2–5
- **failure_patterns**：
  - Primary charts omit or inconsistently define uncertainty and training/test seed variation; appendix captions sometimes reveal single-seed or instability limits.
  - Dense shared legends, small plot labels and token-cell text make several appendix objects difficult to read at page scale.
  - Color carries most method semantics and is not fully grayscale-safe despite some marker/line redundancy.
  - The visual source gap prevents source-exact reconstruction of curves, grids and tables; the public repository contains implementation but no editable visual assets.
  - The headline robustness language extends beyond the two base models, limited tasks and finite sequence/seed settings shown in the PDF.
- **one_sentence_visual_strategy**：The paper uses a failure-first, mechanism-linked Pareto narrative: expose heuristic regime failure, insert and train a lightweight policy, show matched quality–compute frontiers, then use ablations, transfer panels, order diagnostics and exact appendix tables to make the full-diffusion gain auditable.

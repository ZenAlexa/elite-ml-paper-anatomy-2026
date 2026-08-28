# Visual audit — `iclr-2026-dedfde9d7c99`

## 范围、事实源与完成边界

- **论文**：*Visual Planning: Let’s Think Only with Images*.
- **PDF 事实源**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/pdfs/iclr-2026-dedfde9d7c99.pdf`；`pdf_verified=true`，34 个物理页，Letter（612 × 792 pt），pdfTeX 1.40.27。
- **完整读取与渲染**：物理页 1–34 全部用 `pdftoppm -png -r 200` 渲染为 1700 × 2200 px；含对象页逐个在 200 dpi 原图查看，覆盖正文、参考文献和附录。PDF 作为 Figure/Table 清单事实源，与 reading 的 16 Figures + 13 Tables 逐一对齐。
- **对象范围**：正文 Figure 1–6、Table 1–2；附录 Figure 7–16、Table 3–13。无 supplementary PDF；未把附录章节中的普通文本或公式误计为视觉对象。
- **PDF 对象核查**：`pdfimages -list` 显示编号 Figure 为嵌入 raster/compound assets；`pdffonts` 显示 native table/页面文字使用 Nimbus Roman No9 L、Nimbus Mon L 与 Computer Modern 字体对象。

## 公开源、source inventory 与 GitHub

- 自动清单 `reports/tables/visual_source_inventory.csv` 将该行标为 `exact_visual_source`，候选为 `https://github.com/yix8/VisualPlanning`；本地 `reports/tables/visual_source_files_local.csv` 取得 `evaluation/visual_planning_evaluator.py`（27,452 bytes）。
- `gh repo view yix8/VisualPlanning` 的仓库描述为 `[ICLR 2026 Oral] Visual Planning: Let’s Think Only with Images`，默认分支 `main`，公开树包含 `assets/visual_planning.png`、`README.md`、训练/评估代码。
- `assets/visual_planning.png` 为 1814 × 975 indexed PNG；其 Text/Image key、Direct Prompting、Multimodal Chain-of-Thought、Visual Planning 三行与 PDF Figure 1 内容和布局匹配，登记为 exact rendered asset。
- `evaluation/visual_planning_evaluator.py` 是评估/统计上下文源而非编号图表生成器；GitHub 树中没有 paper TeX、plot/figure/table generator、notebook、TikZ/PGF/SVG 或完整其余对象源。其余属性均以 PDF 200 dpi 视觉观察或 native PDF object 为准。

## PDF 对象清单

|对象|物理页|模块|版面|
|---|---:|---|---|
|Figure 1|2|introduction|main，page_width|
|Figure 2|4|method|main，page_width|
|Figure 3|7|results|main，page_width|
|Figure 4|8|results|main，page_width|
|Figure 5|9|results|main，single_column|
|Figure 6|9|ablation|main，single_column|
|Figure 7|21|appendix|appendix，page_width|
|Figure 8|23|appendix|appendix，page_width|
|Figure 9|24|appendix|appendix，page_width|
|Figure 10|25|appendix|appendix，page_width|
|Figure 11|26|appendix|appendix，page_width|
|Figure 12|27|appendix|appendix，page_width|
|Figure 13|28|appendix|appendix，page_width|
|Figure 14|29|appendix|appendix，page_width|
|Figure 15|30|appendix|appendix，page_width|
|Figure 16|31|appendix|appendix，page_width|
|Table 1|6|results|main，page_width|
|Table 2|7|results|main，single_column|
|Table 3|18|appendix|appendix，page_width|
|Table 4|18|appendix|appendix，page_width|
|Table 5|19|appendix|appendix，page_width|
|Table 6|20|appendix|appendix，page_width|
|Table 7|21|appendix|appendix，page_width|
|Table 8|22|appendix|appendix，page_width|
|Table 9|22|appendix|appendix，page_width|
|Table 10|27|appendix|appendix，page_width|
|Table 11|31|appendix|appendix，page_width|
|Table 12|32|appendix|appendix，page_width|
|Table 13|32|appendix|appendix，inset|

## 全文视觉风格

- **对象计数**：正文 6 Figures / 2 Tables；附录 10 Figures / 11 Tables。
- **图内字体**：Google Sans-like sans-serif, DejaVu Sans, Computer Modern math；约 4.0–12.0 pt，主要为 raster rendered estimate。
- **表格字体**：Nimbus Roman No9 L, Computer Modern math；body 8.0 pt、header 8.5 pt，来自 PDF font objects。
- **调色与渲染**：示意图使用浅蓝、紫、黄、绿和橙红色块编码视觉状态、动作类别与奖励角色；Matplotlib-like 图表使用固定的 categorical 方法色（VPRL 绿、VPFT 桃、Gemini 蓝、Qwen 粉、CoT 灰）；qualitative grid 保留环境自然色，表格采用黑白 native PDF rules 加粗体最佳值。颜色在各子系统内有语义，但并未为所有 Figure 提供一套可量化的全局色标。
- **一致性判断**：两栏 ICLR 正文与单栏 appendix 浮动对象使用一致的 caption 前缀、Nimbus Roman/Computer Modern 页面字体、部分横线表格和 EM/PR 指标命名。图内 sans-serif 字体、自然图像色和 chart 方法色在各局部对象内稳定，但 textual screenshot、architecture diagram 与 numeric charts 形成不同子风格，且小图字号和颜色冗余度不完全一致。

## Figure 1 — p.2（introduction，main，page_width）

- **类型与职责**：conceptual_diagram, pipeline, qualitative_grid；purpose = headline, method_interface, qualitative_evidence；复杂度 3/5（panels=3，series=None，legend_items=2，annotations=18，marks≈None）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=True（upper-left modality key），direct_labels=True，marker_types=None，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.0 pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 5.0–12.0 pt（median 8.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，8 色，近似 `#4C91D7, #7F2A78, #E7DDEE, #F5E6B7, #B4D9F5, #A8D5C1, #F4B7AA, #222222`；Blue marks Text in the modality key; purple marks Image; pastel blue/purple blocks and natural map thumbnails distinguish the three rows and their visual states. Color is reinforced by row labels, arrows and image-versus-text form. grayscale_safe=False。
- **编码**：x=left-to-right reasoning step / state transition order；y=three paradigm rows；color=Text/Image modality and row-specific pastel accents；shape=outlined modality swatches, map thumbnails and block cards；line=horizontal arrows encode transition or generated response；facet=Direct Prompting / Multimodal Chain-of-Thought / Visual Planning；text=row titles, modality key and state labels。
- **Caption（PDF 文字规范化，40 words）**：“Figure 1: Comparison of reasoning paradigms. The traditional approaches (top and middle rows) generate verbose and inaccurate textual plan, while the Visual Planning paradigm (bottom row) predicts the next visual state directly, forming a pure image trajectory without language mediation.”
- **Caption 动作**：title, setup, encoding_key, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Illustrative schematic rather than an experiment: it contrasts verbal outputs with image-state trajectories and has no sample, denominator, metric, aggregation or uncertainty. The map thumbnails are example states, not a quantitative trace count.
- **证据关系**：The introduction’s modality-gap claim leads to this three-way interface contrast. Figure 1 establishes why image-state reasoning is the object of study; Figure 2 supplies the VPRL mechanism, while Table 1, Table 2 and Figures 3–6 test cross-task performance, textual baselines, scaling and exploration. The schematic’s “verbose and inaccurate” language is not itself a measured rate.
- **设计优点**：
  - Three paradigms are aligned in identical left-to-right rows, so the image-only trajectory is immediately comparable with verbal reasoning.
  - The modality key, direct row labels and repeated arrows make the interface distinction legible without a long legend.
  - The caption states the central transition from text mediation to direct visual-state prediction.
- **设计缺点**：
  - The claim that traditional plans are verbose and inaccurate is qualitative here and is not paired with a denominator or error statistic.
  - Map thumbnails and ellipses are decorative examples; the caption does not define the task instance or state sampling.
  - Small labels and pastel fills lose separation when the page is reduced or printed in grayscale.
- **可复用模式**：Use a three-row modality comparison with one repeated transition grammar, but pair the schematic with one quantitative grounding-error measure and explicitly define the example state sequence in the caption.
- **证据定位**：page=2，label=Figure 1; 200 dpi PDF render, with matching author asset content in assets/visual_planning.png，basis=rendered_observation。

## Figure 2 — p.4（method，main，page_width）

- **类型与职责**：architecture, pipeline, conceptual_diagram；purpose = method_interface, theory_mechanism, experimental_design；复杂度 4/5（panels=1，series=None，legend_items=0，annotations=30，marks≈None）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=2，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.0 pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 5.0–12.0 pt（median 8.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，8 色，近似 `#E7DDEE, #F5E6B7, #B4D9F5, #E3E3E3, #A8D5C1, #F4B7AA, #7F2A78, #222222`；Pastel purple/yellow/blue cards identify visual states, candidate/action blocks and reference/score areas; green, orange/red and gray cards separate optimal, non-optimal and invalid reward outcomes. Arrows and labels redundantly carry the flow. grayscale_safe=False。
- **编码**：x=left-to-right state prediction and decoding flow；y=feedback loop from scoring to policy update；color=pastel block colors for image states, candidate responses, action classes and reward cards；shape=image thumbnails, rounded boxes and dashed candidate group；line=solid arrows for data flow and a feedback arrow; dashed boundaries for candidate/action groups；facet=无；text=v_t, candidate index k, action labels, α_opt/α_non-opt/α_inv and GRPO update。
- **Caption（PDF 文字规范化，50 words）**：“Figure 2: An overview of the proposed VPRL framework, illustrated with autoregressive large vision models for image generation in the context of a visual navigation task. We train the visual policy model with GRPO, using the progress reward that encourages progressing actions and penalizes invalid actions, yielding goal-aligned visual planning.”
- **Caption 动作**：title, setup, encoding_key, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Mechanism diagram only. G denotes a group of candidate visual responses; α_opt, α_non-opt and α_inv denote reward coefficients, with the text specifying 1, 0 and −5. No empirical sample size, distribution, error or uncertainty is encoded.
- **证据关系**：Section 2.2 defines image-prefix pairs, dynamics parsing, action categories and the progress reward; Figure 2 renders those operations as a closed loop from visual prediction through action scoring to GRPO. Figures 3–4 show resulting traces and error cases, while Table 1, Table 2, Figure 6 and Table 10 evaluate the mechanism and its ablations.
- **设计优点**：
  - The figure exposes the complete causal path from predicted image to parsed action, reward category and policy update.
  - Optimal/non-optimal/invalid reward cards connect the conceptual loop to the later failure-ratio table and trace grids.
  - Dashed grouping and direct mathematical labels distinguish candidate generation from environment interpretation.
- **设计缺点**：
  - Many small blocks and arrows require the surrounding equations to disambiguate the exact input prefix and reward timing.
  - The architecture does not show the numerical reward values or a failure boundary in the diagram itself.
  - Color is informative but not fully grayscale-safe, especially for the three reward categories.
- **可复用模式**：Show a visual-policy loop as prediction → state/action parser → typed reward → policy update, with the reward categories drawn as explicit outcome cards and a single feedback arrow.
- **证据定位**：page=4，label=Figure 2; 200 dpi PDF render of VPRL architecture，basis=rendered_observation。

## Figure 3 — p.7（results，main，page_width）

- **类型与职责**：image_montage, qualitative_grid；purpose = qualitative_evidence, method_interface, failure；复杂度 4/5（panels=3，series=None，legend_items=0，annotations=10，marks≈21）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.0 pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 5.0–10.0 pt（median 7.5），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#A8D5C1, #F4B7AA, #F6D365, #B4D9F5, #7F2A78, #222222, #C8E6C9, #F2C4B0, #E3E3E3`；Environment image colors carry state content; green, warm/orange and dark text/action labels identify optimal, non-optimal and invalid examples. Row names and direct annotations provide redundancy. grayscale_safe=False。
- **编码**：x=left-to-right trajectory step；y=FrozenLake / Maze / MiniBehavior task rows；color=state appearance and action-category annotation color；shape=environment tiles and agent/goal icons；line=thin trajectory arrows/step order where shown；facet=three task rows；text=Optimal Action, Non-Optimal Action, Invalid Action and task/constraint labels。
- **Caption（PDF 文字规范化，30 words）**：“Figure 3: Illustration of each task with generated visual planning traces from LVM, covering different types of actions (optimal, non-optimal and invalid). More cases can be found in Appendix F.6.”
- **Caption 动作**：title, setup, encoding_key, appendix_pointer；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Selected generated traces from three tasks; approximately seven state frames per row are illustrative examples. There is no stated number of trajectories sampled for this montage, no rate of each action type and no uncertainty display.
- **证据关系**：The method’s three-way action partition becomes tangible here: a generated trace can be optimal, valid-but-non-optimal or invalid. The main narrative points to Appendix F.6 Figures 13–15 for denser examples; Table 6 quantifies invalid-failure ratios and Figure 4 provides a modality case study.
- **设计优点**：
  - The same row grammar is reused across all three environments, supporting fast cross-task comparison.
  - Direct action and constraint labels make failure semantics visible without decoding a separate legend.
  - The compact montage links the abstract reward partition to actual image-state transitions.
- **设计缺点**：
  - The montage does not say how many traces were sampled or how representative each category is.
  - Frame-level text is small, and the visual density makes individual state changes hard to inspect at single-column scale.
  - Qualitative examples cannot establish the frequency of optimal, non-optimal or invalid actions.
- **可复用模式**：Use one repeated task-row montage for a typed action taxonomy, then link each category to a quantitative rate table and a larger appendix gallery.
- **证据定位**：page=7，label=Figure 3; 200 dpi PDF render with three task rows，basis=rendered_observation。

## Figure 4 — p.8（results，main，page_width）

- **类型与职责**：qualitative_grid, image_montage, screenshot；purpose = qualitative_evidence, mechanism, main_comparison, failure；复杂度 4/5（panels=3，series=None，legend_items=0，annotations=18，marks≈15）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.0 pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.5–10.0 pt（median 7.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，8 色，近似 `#E7DDEE, #F5E6B7, #B4D9F5, #F4B7AA, #A8D5C1, #D3D3D3, #222222, #FFFFFF`；Prompt and textual reasoning are shown in light cards and dark text; VPFT/VPRL image trajectories use natural environment colors and row labels. Labels rather than hue carry the method identity. grayscale_safe=False。
- **编码**：x=sequence order within each visual trace；y=prompt/text reasoning versus VPFT and VPRL rows；color=natural image-state colors; light/dark text cards distinguish textual and visual bands；shape=image frames and dashed containers；line=horizontal state progression; row boundaries separate methods；facet=prompt band, VPFT trace and VPRL trace；text=model names, answer text and non-optimal/constraint labels。
- **Caption（PDF 文字规范化，20 words）**：“Figure 4: Visualization of a test example from FROZENLAKE comparing visual planning variants (VPFT and VPRL) with language-based reasoning variants.”
- **Caption 动作**：title, setup, comparison；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：One FrozenLake test example is juxtaposed across text and visual variants. It contains no denominator, error frequency, confidence or aggregate metric; the example is a case study of grounding and detour behavior.
- **证据关系**：The error-analysis claim about visual-to-text grounding is shown as a concrete example: the textual block misreads the layout while visual traces retain state structure and can detour. Table 1 and Table 2 supply aggregate EM/PR; Figures 8–9 expand textual failure cases.
- **设计优点**：
  - Holding the input example fixed makes the modality comparison concrete.
  - The prompt, textual response and two visual rows form a readable causal sequence from input to planning output.
  - The visual traces reveal behavior that a single scalar metric would hide, including non-optimal detours.
- **设计缺点**：
  - A single case cannot support the general error claim or estimate how often the shown behavior occurs.
  - The text excerpt and labels are too small to independently verify every layout assertion at reduced scale.
  - The caption does not identify the exact test instance, metric context or sampling rule.
- **可复用模式**：Pair one fixed input with text and image-state outputs to explain a mechanism, but place the aggregate grounding-error rate beside the case study.
- **证据定位**：page=8，label=Figure 4; 200 dpi PDF render of FrozenLake case study，basis=rendered_observation。

## Figure 5 — p.9（results，main，single_column）

- **类型与职责**：bar；purpose = headline, main_comparison, robustness；复杂度 3/5（panels=1，series=5，legend_items=5，annotations=0，marks≈20）。
- **版面与绘图语法**：raster；x=categorical，y=linear，grid=both，legend=True（upper center），direct_labels=False，marker_types=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans, DejaVu Sans Oblique；约 6.0–10.0 pt（median 8.0），regular, bold/roman, italic，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=categorical，5 色，近似 `#A6D4C3, #F2C4B0, #C7D2E2, #E2BFD9, #BDBDBD`；VPRL is green, VPFT peach, Gemini (Think) light blue, Qwen (SFT) pink and Gemini (CoT) gray; method names are supplied by the legend. grayscale_safe=False。
- **编码**：x=FrozenLake grid size 3, 4, 5, 6；y=Accuracy (0–1)；color=method identity；shape=grouped bars；line=无；facet=无；text=legend method labels and axis labels。
- **Caption（PDF 文字规范化，43 words）**：“Figure 5: Evaluation of model performance on FROZENLAKE under varying levels of difficulty. As the environment complexity increases with larger grid sizes, language-based reasoning methods experience a sharp decline in performance, whereas visual planning methods exhibit a more gradual drop, demonstrating greater robustness.”
- **Caption 动作**：title, setup, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Grouped bars show accuracy by grid size; the caption and axis establish the task and metric. Values are point estimates without error bars, replicate counts, failure values or sample denominators. The exact VPFT/VPFT* grid-size slice is tabulated in Table 8 and text-variant detail in Table 7.
- **证据关系**：The paper’s robustness-to-scaling claim is first visualized in the main text. Figure 5 connects task difficulty to the cross-method result in Table 1; Appendix Figure 10 extends the same bar grammar to Maze and MiniBehavior, while Tables 7–9 provide exact difficulty and OOD slices.
- **设计优点**：
  - A fixed categorical x-axis and shared y-axis make the robustness slope immediately visible.
  - Five method colors allow the headline visual planner versus language comparison in a small footprint.
  - The caption states both the difficulty manipulation and the qualitative slope difference.
- **设计缺点**：
  - The methods are distinguished almost entirely by color, which is weak in grayscale and for readers with color-vision differences.
  - No uncertainty or test-set denominator is visible, so the separation of nearby bars cannot be assessed statistically.
  - The figure does not show exact values or explain whether accuracy is EM until the surrounding text is read.
- **可复用模式**：Use grouped difficulty bars for a headline robustness claim, but add direct values or a redundant marker/line encoding and link the bars to a full numeric table.
- **证据定位**：page=9，label=Figure 5; left single-column chart in 200 dpi PDF render，basis=rendered_observation。

## Figure 6 — p.9（ablation，main，single_column）

- **类型与职责**：scatter, line；purpose = ablation, mechanism, robustness；复杂度 3/5（panels=1，series=2，legend_items=0，annotations=5，marks≈5）。
- **版面与绘图语法**：raster；x=linear，y=linear，grid=both，legend=False（无），direct_labels=True，marker_types=3，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.2 pt。
- **字体**：DejaVu Sans, DejaVu Sans Oblique；约 6.0–10.0 pt（median 8.0），regular, bold/roman, italic，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=categorical，5 色，近似 `#4F81BD, #E78AC3, #F4A261, #CC79A7, #7A7A7A`；VPRL Stage 1 is directly labeled in blue; VPFT checkpoints 2/5/10/30 epochs use distinct pink/orange/gray markers and labels. Position supplies the main trade-off encoding. grayscale_safe=False。
- **编码**：x=Invalid Ratio (%)；y=Average Entropy；color=VPRL Stage 1 versus VPFT training checkpoints；shape=marker shapes and checkpoint labels；line=connected VPFT checkpoint path；facet=无；text=direct labels for VPRL and VPFT epoch points。
- **Caption（PDF 文字规范化，43 words）**：“Figure 6: Comparison of exploration capabilities between VPFT and VPRL Stage 1 on FROZENLAKE. VPRL Stage 1 achieves significantly better exploration efficiency, balancing high entropy with a low invalid action ratio, whereas VPFT struggles with diminishing entropy and increased invalid actions over training.”
- **Caption 动作**：title, setup, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：A two-dimensional exploration summary compares one VPRL Stage 1 point with VPFT checkpoints at 2, 5, 10 and 30 epochs. Entropy and invalid ratio are point summaries; no replicate count, error bar, confidence display or exact checkpoint aggregation is shown.
- **证据关系**：The Stage 1 hypothesis predicts that random initialization preserves exploration while VPFT teacher forcing collapses entropy or produces invalid actions. Figure 6 is the mechanism ablation; Table 10 measures Stage 1 versus Stage 2 outcomes and Table 6 measures invalid-failure ratios.
- **设计优点**：
  - The x/y trade-off directly encodes the proposed exploration mechanism rather than a generic training curve.
  - Direct labels avoid a separate legend for the few points and expose the checkpoint progression.
  - The connected VPFT path makes entropy decline and invalid-ratio increase easy to read as a trajectory.
- **设计缺点**：
  - The caption uses “significantly” without showing uncertainty or an inferential basis.
  - Point labels are crowded near the lower/right region, and the two quantities have no units beyond the axis names.
  - One point per checkpoint hides variation across groups or runs.
- **可复用模式**：Plot an ablation’s mechanism as a trade-off plane with direct checkpoint labels and a connected path, while adding uncertainty or replicate markers before using inferential language.
- **证据定位**：page=9，label=Figure 6; right single-column chart in 200 dpi PDF render，basis=rendered_observation。

## Figure 7 — p.21（appendix，appendix，page_width）

- **类型与职责**：line, area；purpose = mechanism, ablation, robustness；复杂度 2/5（panels=1，series=3，legend_items=3，annotations=0，marks≈3）。
- **版面与绘图语法**：raster；x=linear，y=linear，grid=both，legend=True（lower right），direct_labels=False，marker_types=0，line_styles=3，hatching=False，reference_lines=0，uncertainty=band，line_width≈1.2 pt。
- **字体**：DejaVu Sans, DejaVu Sans Oblique；约 6.0–10.0 pt（median 8.0），regular, bold/roman, italic，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=categorical，3 色，近似 `#E98989, #77A84B, #5B9BD5`；Red/pink is MiniBehaviour, green is Maze and blue is FrozenLake; translucent bands encode standard deviation around each mean curve. grayscale_safe=False。
- **编码**：x=training Step；y=Progress Reward；color=task identity；shape=无；line=one smoothed mean curve per task；facet=无；text=axis labels and three-item legend。
- **Caption（PDF 文字规范化，14 words）**：“Figure 7: Reward curves with standard deviation for VPRL on FROZENLAKE, MAZE and MINIBEHAVIOR.”
- **Caption 动作**：title, setup, encoding_key, uncertainty_definition；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Three smoothed reward curves are shown with shaded standard deviation across groups; the surrounding appendix states that Gaussian smoothing is applied to rewards and deviations. The number of groups, raw values and training seeds are not printed in the figure.
- **证据关系**：Figure 2 introduces the progress reward; Figure 7 shows its training dynamics across tasks. It supports the Stage 1/Stage 2 interpretation later quantified by Table 10 and complements the exploration snapshot in Figure 6.
- **设计优点**：
  - The uncertainty band is explicitly named in the caption and visually paired with each task curve.
  - A common linear step/reward coordinate system allows cross-task convergence comparison.
  - The legend is compact and placed inside unused lower-right plot space.
- **设计缺点**：
  - Smoothing can obscure transient reward failures, while the caption does not state the smoothing width or group count.
  - The bands overlap heavily early in training, and color is the only task encoding.
  - No raw run traces or terminal performance summary are provided.
- **可复用模式**：Use a shared reward-learning plot with transparent task-specific bands, but expose smoothing and replicate definitions so the band remains interpretable.
- **证据定位**：page=21，label=Figure 7; 200 dpi PDF render and shaded SD bands，basis=rendered_observation。

## Figure 8 — p.23（appendix，appendix，page_width）

- **类型与职责**：screenshot, qualitative_grid, image_montage；purpose = qualitative_evidence, failure, ablation, method_interface；复杂度 4/5（panels=4，series=3，legend_items=0，annotations=20，marks≈5）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.5–10.0 pt（median 7.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，7 色，近似 `#4A4A4A, #F0F0F0, #E7DDEE, #B4D9F5, #F5E6B7, #222222, #FFFFFF`；Dark gray section headers identify input/SFT/GRPO blocks; white/gray cards separate textual output formats; environment thumbnails retain natural colors. grayscale_safe=False。
- **编码**：x=not applicable; columns/boxes enumerate output variants；y=input/output sections；color=gray header bands and natural image-state colors；shape=screenshot cards and text boxes；line=无；facet=input example, SFT with coordinates, SFT with ASCII, GRPO；text=variant headings, layout symbols and output tags。
- **Caption（PDF 文字规范化，52 words）**：“Figure 8: Examples of model outputs under different trained textual variants: SFT (w/ Coordinate), SFT (w/ ASCII), and GRPO. Each variant follows a distinct format for representing the environment. Even for the relatively simple 3 × 3 example input, we observe that the ASCII and GRPO models still produce erroneous layout descriptions.”
- **Caption 动作**：title, setup, encoding_key, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：One 3×3 input case is shown with coordinate, ASCII and GRPO textual outputs. It is a qualitative grounding-error example; no sample denominator, error rate or uncertainty is encoded.
- **证据关系**：The textual-baseline ablation asks whether adding a coordinate/ASCII representation or RL reasoning bridges the modality gap. Figure 8 gives the concrete layout errors, while Table 7 and Table 2 report the corresponding EM/PR and Figure 9 shows failures across levels.
- **设计优点**：
  - The input is held fixed across three output formats, isolating representation changes.
  - Section headers and direct labels make the intended format of each textual variant explicit.
  - The caption states that layout errors persist even on a simple 3×3 case.
- **设计缺点**：
  - Only one example is shown, so the observed errors are not prevalence estimates.
  - Long textual responses are rendered at very small size and require zooming to verify the exact mismatch.
  - The figure does not mark which output tokens are wrong or provide a compact error annotation.
- **可复用模式**：Present a fixed input beside multiple representation-specific outputs, using section headers and one highlighted grounding discrepancy; pair it with aggregate error rates.
- **证据定位**：page=23，label=Figure 8; 200 dpi PDF render of textual-variant cards，basis=rendered_observation。

## Figure 9 — p.24（appendix，appendix，page_width）

- **类型与职责**：screenshot, qualitative_grid, image_montage；purpose = failure, qualitative_evidence, ablation；复杂度 4/5（panels=4，series=1，legend_items=0，annotations=25，marks≈8）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.5–10.0 pt（median 7.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，7 色，近似 `#4A4A4A, #F0F0F0, #B4D9F5, #F5E6B7, #F4B7AA, #222222, #FFFFFF`；Dark gray headers identify FrozenLake levels; natural grid colors show the input while black text carries the generated reasoning/action output. grayscale_safe=False。
- **编码**：x=difficulty progression L3→L6 across boxes；y=input image versus model response within each box；color=level header and natural environment colors；shape=screenshot cards；line=无；facet=four difficulty-level examples；text=<think>/<answer> output and level labels。
- **Caption（PDF 文字规范化，51 words）**：“Figure 9: Examples of responses from the textual GRPO baseline with PR metric as the reward on FROZENLAKE across different difficulty levels. Each box shows the input image and the corresponding model output. In all cases, the model produces incorrect layout descriptions, which in turn lead to incorrect predicted action sequences.”
- **Caption 动作**：title, setup, encoding_key, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Four qualitative cases, one for each FrozenLake level L3–L6, show input, textual reasoning and action output. The caption says all shown cases have layout/action errors, but gives no denominator or failure frequency.
- **证据关系**：Figure 9 expands the text-GRPO failure introduced in Table 2: the PR reward still cannot prevent visual-to-text grounding errors as difficulty changes. Table 7 provides complete level-wise metrics; Figure 8 isolates format differences.
- **设计优点**：
  - Repeating the same box structure across L3–L6 makes the failure pattern comparable.
  - The input and resulting action sequence are adjacent, so the grounding-to-action chain is visible.
  - The caption clearly states the causal interpretation of the examples.
- **设计缺点**：
  - The examples are selected cases and do not establish that every test item fails.
  - Dense narrative text is difficult to read without high zoom and lacks token-level error marking.
  - The figure does not visually separate layout misclassification from downstream action error.
- **可复用模式**：Use aligned level-specific failure cards to show a repeated grounding breakdown, but annotate the first wrong layout element and report prevalence next to the cards.
- **证据定位**：page=24，label=Figure 9; 200 dpi PDF render of L3–L6 response cards，basis=rendered_observation。

## Figure 10 — p.25（appendix，appendix，page_width）

- **类型与职责**：bar；purpose = robustness, main_comparison, ablation；复杂度 4/5（panels=2，series=5，legend_items=5，annotations=0，marks≈30）。
- **版面与绘图语法**：raster；x=categorical，y=linear，grid=both，legend=True（upper center of each panel），direct_labels=False，marker_types=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans, DejaVu Sans Oblique；约 6.0–10.0 pt（median 8.0），regular, bold/roman, italic，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=categorical，5 色，近似 `#A6D4C3, #F2C4B0, #C7D2E2, #E2BFD9, #BDBDBD`；The five method colors match Figure 5: VPRL green, VPFT peach, Gemini (Think) blue, Qwen (SFT) pink and Gemini (CoT) gray. Each panel repeats the method key. grayscale_safe=False。
- **编码**：x=Maze grid size 3–6; MiniBehavior grid size 7–8；y=Accuracy (0–1)；color=method identity；shape=grouped bars；line=无；facet=left Maze / right MiniBehavior；text=panel labels, axes and method legend。
- **Caption（PDF 文字规范化，30 words）**：“Figure 10: Performance across different grid sizes, reflecting task difficulty. Left: MAZE. Right: MINIBEHAVIOR. Visual planners consistently maintain higher accuracy and exhibit flatter performance curves, indicating robustness to increasing complexity.”
- **Caption 动作**：title, setup, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Accuracy bars extend the difficulty comparison beyond FrozenLake; no uncertainty, replicate count, failure count or test denominator is shown. The appendix text notes that MiniBehavior accuracy can rise with grid size because layout components are fixed.
- **证据关系**：Figure 10 is the appendix extension of main Figure 5. It tests whether the visual-planning robustness pattern transfers to Maze and MiniBehavior; Tables 1 and 7–9 provide the corresponding exact cross-task, level and OOD values.
- **设计优点**：
  - Identical color and grouped-bar grammar preserves the main-to-appendix comparison.
  - Two task panels fit the same visual question—accuracy under increasing grid size—without introducing a new axis convention.
  - The caption states the intended robustness interpretation.
- **设计缺点**：
  - Only two MiniBehavior grid sizes make its “curve” visually underdetermined.
  - Color remains the sole method distinction and no uncertainty is visible.
  - The fixed-layout explanation for MiniBehavior is outside the caption, so the rising bars could be misread as easier larger grids.
- **可复用模式**：Repeat a main robustness chart across tasks with a shared y-scale, but annotate task-specific difficulty semantics and show exact values or intervals.
- **证据定位**：page=25，label=Figure 10; two-panel 200 dpi PDF render，basis=rendered_observation。

## Figure 11 — p.26（appendix，appendix，page_width）

- **类型与职责**：qualitative_grid, image_montage；purpose = robustness, qualitative_evidence, main_comparison, failure；复杂度 5/5（panels=3，series=None，legend_items=0，annotations=6，marks≈45）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width≈1.0 pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.5–10.0 pt（median 7.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#A8D5C1, #F4B7AA, #B4D9F5, #F5E6B7, #7F2A78, #222222, #D9EAD3, #FCE5CD, #FFFFFF`；Top/bottom method identity is positional and directly labeled; natural task colors show environment states. Green/pink accents distinguish successful/failing visual paths where visible. grayscale_safe=False。
- **编码**：x=left-to-right OOD trajectory steps；y=VPFT top versus VPRL bottom, grouped by task；color=environment state appearance and success/failure accents；shape=grid/image frames；line=trajectory step order and occasional path arrow；facet=Maze, FrozenLake and MiniBehavior task sections；text=method/task row labels。
- **Caption（PDF 文字规范化，49 words）**：“Figure 11: Qualitative comparison of visual planning outputs from VPFT (top) and VPRL (bottom) on out-of-distribution (OOD) scenarios with unseen larger grid size across MAZE, FROZENLAKE, and MINIBEHAVIOR. Each example shows a failure case from VPFT contrasted with a successful trajectory generated by VPRL under the same environment configuration.”
- **Caption 动作**：title, setup, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Paired qualitative OOD examples on enlarged, unseen grids compare VPFT and VPRL under the same configuration. The quantitative EM/PR and grid sizes are in Table 9; this montage gives no number of cases, success denominator or uncertainty.
- **证据关系**：Table 9 establishes the OOD performance difference; Figure 11 supplies matched visual failure/success cases that make the generalization claim inspectable. Figure 12 then perturbs inputs, while Figures 13–15 show in-distribution failure categories.
- **设计优点**：
  - Matched top/bottom examples turn the OOD comparison into a controlled visual pairing.
  - Task sections retain a common trajectory grammar despite different environment layouts.
  - The caption explicitly identifies VPFT failures and VPRL successes as the comparison target.
- **设计缺点**：
  - The selected cases may overrepresent the claimed contrast and are not a frequency estimate.
  - The dense multi-frame grid is hard to inspect at normal page size.
  - Success/failure is conveyed by labels and outcomes rather than a consistent symbol or quantitative annotation.
- **可复用模式**：Pair baseline and proposed trajectories for the same OOD state, place quantitative OOD scores in a neighboring table, and preserve task-specific panels with one shared row grammar.
- **证据定位**：page=26，label=Figure 11; 200 dpi PDF render of VPFT/VPRL OOD trace pairs，basis=rendered_observation。

## Figure 12 — p.27（appendix，appendix，page_width）

- **类型与职责**：qualitative_grid, image_montage；purpose = robustness, qualitative_evidence, mechanism；复杂度 4/5（panels=3，series=None，legend_items=0，annotations=3，marks≈22）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.5–10.0 pt（median 7.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#000000, #808080, #A8D5C1, #B4D9F5, #F5E6B7, #F4B7AA, #7F2A78, #222222, #FFFFFF`；Black/gray regions encode masked input; natural environment colors encode visible layout and generated states. Row labels identify FrozenLake, Maze and MiniBehavior. grayscale_safe=False。
- **编码**：x=left-to-right generated-state sequence；y=task rows；color=black/gray mask versus visible environment colors；shape=masked input and subsequent image states；line=state progression by ordered frames；facet=FrozenLake / Maze / MiniBehavior；text=task row labels and initial masked-input position。
- **Caption（PDF 文字规范化，48 words）**：“Figure 12: Qualitative analysis of VPRL under perturbed inputs (the first image of each trace). When parts of the input environment are masked (black/gray regions), VPRL maintains consistent planning traces aligned with the visible structure, demonstrating robustness to incomplete visual information without deviating from the underlying environment layout.”
- **Caption 动作**：title, setup, encoding_key, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Qualitative traces begin with masked black/gray input regions and show subsequent VPRL image states. No mask fraction, number of trials, failure rate, or uncertainty is reported, so “robustness” is a selected-example conclusion.
- **证据关系**：Figure 12 extends the OOD/generalization analysis in Figure 11 from larger grids to incomplete visual input. It is a mechanism-facing qualitative check; Figure 16 and Table 11 address image quality, while Table 9 supplies the only numeric OOD comparison.
- **设计优点**：
  - The perturbation is visible in the first frame, making the causal input change inspectable.
  - All three tasks share the same row-and-trace layout, which supports cross-task comparison.
  - The caption states both the mask encoding and the claimed structural consistency.
- **设计缺点**：
  - No mask area, placement policy or trial selection rule is stated.
  - The figure cannot distinguish robust behavior from an easy visible subset without aggregate masked-input evaluation.
  - The black/gray perturbation dominates the visual palette and may hide subtle state differences.
- **可复用模式**：Show the perturbation in the first frame and carry the same trace layout across tasks, but quantify perturbation severity and success over a predefined sample.
- **证据定位**：page=27，label=Figure 12; 200 dpi PDF render of masked-input traces，basis=rendered_observation。

## Figure 13 — p.28（appendix，appendix，page_width）

- **类型与职责**：qualitative_grid, image_montage；purpose = qualitative_evidence, failure, robustness；复杂度 5/5（panels=3，series=None，legend_items=0，annotations=10，marks≈78）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.0–10.0 pt（median 6.5），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#A8D5C1, #F4B7AA, #B4D9F5, #F5E6B7, #7F2A78, #222222, #FFCCCB, #D9EAD3, #FFFFFF`；Three category headers (Correct/optimal, Non-optimal, Invalid) and direct labels encode trajectory class; natural grid/agent colors encode states. Category position is redundant with text labels. grayscale_safe=False。
- **编码**：x=ordered frames within each trajectory；y=trajectory categories and numbered cases；color=natural grid state colors and category accents；shape=small environment-state tiles；line=frame order; occasional implicit path progression；facet=optimal/correct, non-optimal, invalid blocks；text=category headings, case numbers and visible agent/goal icons。
- **Caption（PDF 文字规范化，77 words）**：“Figure 13: Generated visual planning trajectories from VPRL on the FROZENLAKE test set. We illustrate three representative categories: optimal, non-optimal, and invalid cases. In non-optimal examples, the model occasionally enters local loops but still has the chance to make progress toward the goal, see the first and third trajectories. In invalid cases, despite a significant reduction in failure rate, VPRL still exhibits errors such as disappearing agents, contradictory actions (e.g., simultaneous left and right), or unrealistic teleportation.”
- **Caption 动作**：title, setup, encoding_key, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Representative FrozenLake test traces are grouped into optimal, non-optimal and invalid cases. The caption names qualitative error modes; it does not give how many test trajectories were sampled, the invalid rate or uncertainty. Table 6 provides the aggregate invalid-failure ratio.
- **证据关系**：The action taxonomy in Figure 3 is expanded into a failure gallery. Figure 13 grounds Table 6’s invalid-failure metric in concrete modes—loops, disappearing agents, contradictory actions and teleportation—and is interpreted alongside reward dynamics in Figure 7 and Stage 1/2 results in Table 10.
- **设计优点**：
  - Category blocks create a clear visual taxonomy of success, valid detour and invalid behavior.
  - Multiple numbered examples show that invalidity has several distinct visual manifestations.
  - The caption links the gallery to the main failure-rate claim and names specific error modes.
- **设计缺点**：
  - The high-density grid is difficult to read without zooming and has no per-trajectory text summary.
  - “Representative” is not operationalized, so selection bias cannot be assessed.
  - The phrase “significant reduction” is not accompanied by uncertainty or a numerical comparison in the caption.
- **可复用模式**：Organize qualitative traces by an explicit action taxonomy and name failure modes in the caption, then bind each category to a measured denominator and failure-rate table.
- **证据定位**：page=28，label=Figure 13; 200 dpi PDF render of FrozenLake trace gallery，basis=rendered_observation。

## Figure 14 — p.29（appendix，appendix，page_width）

- **类型与职责**：qualitative_grid, image_montage；purpose = qualitative_evidence, failure, robustness；复杂度 5/5（panels=3，series=None，legend_items=0，annotations=10，marks≈70）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.0–10.0 pt（median 6.5），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#A8D5C1, #F4B7AA, #B4D9F5, #F5E6B7, #7F2A78, #222222, #FFCCCB, #D9EAD3, #FFFFFF`；Category headings and direct labels identify optimal, non-optimal and invalid blocks; natural maze colors carry structural state and agent location. grayscale_safe=False。
- **编码**：x=ordered maze states per trajectory；y=category blocks and numbered examples；color=maze structure and category accents；shape=maze-state tiles with agent/goal positions；line=implicit temporal order across frames；facet=optimal/correct, non-optimal, invalid blocks；text=category headings, case numbers and environment labels。
- **Caption（PDF 文字规范化，82 words）**：“Figure 14: Generated visual planning trajectories from VPRL on the MAZE test set. We illustrate three representative categories: optimal, non-optimal, and invalid cases. In non-optimal examples, similar to FROZENLAKE, the model occasionally enters redundant loops but still progresses toward the goal. Invalid cases include maze-specific errors, such as the agent erroneously traversing through walls, violating the structural constraints of the environment. Notably, we observe that in the last invalid case, the agent is able to plan an optimal trajectory in subsequent steps.”
- **Caption 动作**：title, setup, encoding_key, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Representative Maze test traces are grouped by optimality and validity. Wall traversal and later recovery are qualitative observations; no trajectory sampling denominator or uncertainty is shown.
- **证据关系**：Figure 14 specializes the Figure 3 action taxonomy to Maze constraints. Its wall-traversal examples explain the high VPFT invalid ratio in Table 6 and complement the OOD and cross-task numeric results in Table 9 and Table 1.
- **设计优点**：
  - The category layout is consistent with Figures 13 and 15, making task-specific failure differences easy to compare.
  - The wall constraint is visually obvious in the maze tiles and explicitly named in the caption.
  - The final invalid-but-recovering example illustrates that invalidity and later progress are separable events.
- **设计缺点**：
  - Many small frames make wall crossings and recovery hard to verify at page scale.
  - The gallery shows selected cases and does not estimate how often a later recovery occurs.
  - No arrow or per-frame action label identifies the precise wall-crossing transition.
- **可复用模式**：Keep a cross-task failure-gallery template while letting the caption name domain-specific invalid transitions such as wall traversal; annotate the exact offending step for auditability.
- **证据定位**：page=29，label=Figure 14; 200 dpi PDF render of Maze trace gallery，basis=rendered_observation。

## Figure 15 — p.30（appendix，appendix，page_width）

- **类型与职责**：qualitative_grid, image_montage；purpose = qualitative_evidence, failure, robustness；复杂度 5/5（panels=3，series=None，legend_items=0，annotations=8，marks≈80）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 4.0–10.0 pt（median 6.5），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，9 色，近似 `#A8D5C1, #F4B7AA, #B4D9F5, #F5E6B7, #7F2A78, #222222, #FFCCCB, #D9EAD3, #FFFFFF`；Direct category headings identify correct, non-optimal and invalid cases; natural MiniBehavior tiles encode agent, printer and table states. grayscale_safe=False。
- **编码**：x=ordered MiniBehavior state frames；y=category blocks and numbered examples；color=natural task-state colors and category accents；shape=grid tiles with agent/printer/table icons；line=implicit frame order；facet=optimal/correct, non-optimal, invalid blocks；text=category headings and case numbers。
- **Caption（PDF 文字规范化，13 words）**：“Figure 15: Generated visual planning trajectories from VPRL on the MINIBEHAVIOR test set.”
- **Caption 动作**：title, setup；headline_bold=False，self_contained=False，main_finding_stated=False。
- **数据与统计**：Representative MiniBehavior traces are displayed across the three same category blocks used for FrozenLake and Maze. The caption gives no category definitions, task constraints, sample count or uncertainty.
- **证据关系**：Figure 15 completes the Figure 3/13/14 qualitative taxonomy for the third task. Table 1 and Figure 10 provide the cross-task and scaling context, while Table 6 quantifies invalid-failure ratios; the sparse caption leaves most interpretation to the surrounding appendix text.
- **设计优点**：
  - The repeated three-block template supports visual comparison across all three environments.
  - The larger gallery exposes varied pick/drop and movement states that are not visible in the compact main figure.
  - Direct category headings preserve a clear top-level reading order.
- **设计缺点**：
  - The caption is title-only and does not define the categories, task constraints or what constitutes an invalid trace.
  - The high-density grid has no per-case action annotation or selection rationale.
  - Qualitative cases cannot establish the frequency of MiniBehavior failure modes.
- **可复用模式**：Reuse a common task-gallery layout for cross-domain qualitative evidence, but give every panel a self-contained caption that defines categories and the domain-specific validity rule.
- **证据定位**：page=30，label=Figure 15; 200 dpi PDF render of MiniBehavior trace gallery，basis=rendered_observation。

## Figure 16 — p.31（appendix，appendix，page_width）

- **类型与职责**：image_montage, qualitative_grid；purpose = qualitative_evidence, mechanism, robustness；复杂度 4/5（panels=3，series=None，legend_items=0，annotations=3，marks≈24）。
- **版面与绘图语法**：raster；x=none，y=none，grid=none，legend=False（无），direct_labels=True，marker_types=None，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width≈None pt。
- **字体**：DejaVu Sans-like sans-serif, Computer Modern math；约 5.0–11.0 pt（median 8.0），regular, bold/roman，provenance=rendered_estimate，confidence=medium。
- **颜色**：mode=mixed，8 色，近似 `#B4D9F5, #58C7E8, #D7EEF8, #F5E6B7, #A8D5C1, #F4B7AA, #808080, #FFFFFF`；Natural FrozenLake colors encode grid state, agent and goal; row position—not color—identifies Original, Predicted and Reconstructed images. grayscale_safe=False。
- **编码**：x=left-to-right trajectory/image index；y=Original / Predicted / Reconstructed rows；color=natural environment image appearance；shape=small grid-image tiles；line=无；facet=three representation rows；text=row labels and image sequence order。
- **Caption（PDF 文字规范化，26 words）**：“Figure 16: Qualitative comparison between original images (top), predicted images by the model (middle), and reconstructed images obtained by encoding and decoding the original inputs (bottom).”
- **Caption 动作**：title, setup, encoding_key, comparison；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Qualitative tokenizer/image-quality comparison with roughly eight image states per row. No pixel metric or uncertainty is embedded; Table 11 tests downstream EM/PR with self-generated versus ground-truth intermediates.
- **证据关系**：Figure 4 exposes artifacts in predicted intermediate images; Figure 16 tests whether similar artifacts arise from encoding/decoding alone. Table 11 shows that replacing intermediates with ground-truth images changes performance little, closing the image-quality robustness argument.
- **设计优点**：
  - Three aligned rows let readers compare the same state sequence across original, predicted and reconstructed representations.
  - The reconstruction control makes the tokenizer limitation visually inspectable.
  - Row labels provide a non-color encoding that survives grayscale viewing.
- **设计缺点**：
  - The montage lacks an objective reconstruction metric or a visible indication of the exact input pairing.
  - Small tile differences are hard to distinguish at page scale.
  - The caption does not state the task, number of samples or criterion for visual comparability.
- **可复用模式**：Use aligned original/predicted/reconstructed rows as a visual control for generative artifacts, and bind it to a downstream replacement experiment plus a quantitative image metric.
- **证据定位**：page=31，label=Figure 16; 200 dpi PDF render of original/predicted/reconstructed rows，basis=rendered_observation。

## Table 1 — p.6（results，main，page_width）

- **表结构**：8 data rows × 11 columns；header_levels=2，row_groups=2，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，47 words）**：“Table 1: Performance of the closed- and open-source models on FROZENLAKE, MAZE, and MINIBEHAVIOR. VPRL performs consistently the best (bold) across all tasks. † denotes the post-trained model. ~ represents texts and [image icon] represents images. The last column AVG. reports the average performance across three tasks.”
- **Caption 动作**：title, setup, comparison, encoding_key, main_finding；headline_bold=False，self_contained=True，main_finding_stated=True。
- **数据与统计**：Eight model/variant rows are grouped into Closed-Source Model and Open-Source Model. Columns report EM and PR (%) for FrozenLake, Maze, MiniBehavior and their three-task average; values use one decimal place. VPRL is bolded as the best row across the displayed metrics.
- **不确定性**：No error bars, intervals, replicate summaries or significance marks; all cells are point estimates in percent.
- **证据关系**：This is the headline cross-task result: it tests the introduction’s visual-planning claim after Figure 2’s method setup. Table 2 isolates text-planning variants; Figures 3–6 provide trace, case, scaling and exploration explanations, while Tables 4 and 6 expose sample and failure-rate context.
- **设计优点**：
  - Multi-level task/metric headers make the cross-task comparison compact.
  - Closed/open-source row groups and bold VPRL values direct attention to the intended decision.
  - The AVG. columns summarize the same EM/PR estimands without introducing a new metric.
- **设计缺点**：
  - The table is wide and dense; †, modality glyphs and the model hierarchy require careful reading at normal page size.
  - Point estimates omit test-set denominators and uncertainty, so small method differences cannot be evaluated for variability.
  - AVG. averages task percentages but the aggregation rule and task weighting are not elaborated in the caption.
- **可复用模式**：Use a two-level task/metric header, explicit model-family groups and a single bold best row for a cross-task headline; retain denominator and uncertainty notes outside the visual only when space is constrained.
- **证据定位**：page=6，label=Table 1; native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 2 — p.7（results，main，single_column）

- **表结构**：5 data rows × 3 columns；header_levels=1，row_groups=1，decimal_precision=1，rules=partial_grid，highlighting=none。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，19 words）**：“Table 2: Performance of text-based planning variants on FROZENLAKE. See Table 7 in Appendix F.2 for the full results.”
- **Caption 动作**：title, setup, comparison, appendix_pointer；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Five Qwen 2.5-VL-Instruct-7B variants are listed: direct SFT, coordinate and ASCII SFT, and two GRPO reward variants. EM (%) and PR (%) are point estimates; the table is the main-text snapshot and Table 7 expands it over L3–L6.
- **不确定性**：No uncertainty, replicate count or significance annotation.
- **证据关系**：Table 2 isolates whether textual representation or RL reward closes the modality gap identified in the introduction and Figure 4. It is the bridge to Appendix Table 7 and Figures 8–9, and provides the text baseline against which VPRL is described in Table 1.
- **设计优点**：
  - The compact two-metric table fits beside the narrative claim and compares all text variants directly.
  - The appendix pointer prevents the main body from repeating the full difficulty slice.
  - Variant indentation communicates SFT versus GRPO hierarchy without extra columns.
- **设计缺点**：
  - A one-level header leaves the training/representation conditions encoded only in row labels.
  - No uncertainty or per-level breakdown is visible in the headline snapshot.
  - The caption does not state the exact reward definitions; readers must follow the appendix pointer.
- **可复用模式**：Keep a small main-text ablation table for the decision metric and link to a full level-wise appendix table, while making variant conditions explicit in the row labels.
- **证据定位**：page=7，label=Table 2; right-column native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 3 — p.18（appendix，appendix，page_width）

- **表结构**：6 data rows × 5 columns；header_levels=2，row_groups=3，decimal_precision=0，rules=partial_grid，highlighting=none。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，18 words）**：“Table 3: Distribution of training dataset by grid sizes for each task. Value indicates the number of environments.”
- **Caption 动作**：title, setup, encoding_key；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Three stacked task blocks list Train and Test counts by grid size: FrozenLake and Maze each use 1,000 train/250 test environments for sizes 3–6; MiniBehavior uses 796/204 at size 7 and 801/199 at size 8. The widest block has five columns (Grid Size plus four sizes).
- **不确定性**：Counts are integers; no uncertainty or sampling interval is applicable.
- **证据关系**：Table 3 fixes the environment distribution underlying the difficulty plots and evaluation denominators. It supports Figure 5, Figure 10 and OOD comparisons, and pairs with Table 4’s image-pair/trajectory sample conversion.
- **设计优点**：
  - Stacking task-specific blocks avoids a sparse wide table while retaining identical Train/Test semantics.
  - The integer counts and grid-size headers are easy to audit against the dataset description.
  - The caption defines the unit as environments.
- **设计缺点**：
  - MiniBehavior has a different grid-size span, so the repeated block geometry requires visual reorientation.
  - The table does not describe generation seeds, filtering or whether test environments are disjoint beyond the Train/Test labels.
  - No total row summarizes the per-task counts.
- **可复用模式**：Use repeated compact blocks when task-specific domains have different category ranges, but add totals and split-generation rules for reproducibility.
- **证据定位**：page=18，label=Table 3; three stacked native PDF blocks inspected at 200 dpi，basis=pdf_object。

## Table 4 — p.18（appendix，appendix，page_width）

- **表结构**：6 data rows × 8 columns；header_levels=2，row_groups=3，decimal_precision=0，rules=partial_grid，highlighting=none。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，36 words）**：“Table 4: Number of training and test samples for each task and method. For visual planning, the numbers here are represented in image pairs, which correspond to the same number of trajectories for SFT in Text.”
- **Caption 动作**：title, setup, encoding_key；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：FrozenLake, Maze and MiniBehavior each have Train/Test rows and columns for SFT in Text, VPFT, VPRL Stage 1/Stage 2 and VPFT* Stage 1/SFT. Visual counts are image pairs and correspond to trajectory counts for text SFT; VPRL Stage 1 test entries are N/A. Values range from 403 to 170,621.
- **不确定性**：Integer sample counts and N/A cells; no uncertainty is applicable.
- **证据关系**：Table 4 documents how trajectories become training samples for the model variants in Table 1 and Table 2. It is the denominator/reproduction companion to Table 3 and helps interpret why Stage 1 and Stage 2 have different data volumes.
- **设计优点**：
  - Two header levels cleanly group VPRL and VPFT* stages while preserving task/split rows.
  - The caption explicitly resolves the potentially confusing image-pair versus trajectory unit.
  - N/A cells expose non-applicable stages rather than silently dropping them.
- **设计缺点**：
  - The very wide header and large counts are difficult to scan at single-page scale.
  - The caption does not state whether samples are unique image pairs or overlapping prefixes beyond the conversion note.
  - No total or normalization column helps compare relative sample expansion across tasks.
- **可复用模式**：Make unit conversion explicit in the caption and use grouped stage headers for a reproduction table; add a normalized expansion column when sample growth is central to the claim.
- **证据定位**：page=18，label=Table 4; wide native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 5 — p.19（appendix，appendix，page_width）

- **表结构**：6 data rows × 8 columns；header_levels=2，row_groups=0，decimal_precision=None，rules=partial_grid，highlighting=none。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，10 words）**：“Table 5: Hyper-parameters of training both textual and visual planners.”
- **Caption 动作**：title, setup；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Rows list Epochs, Learning Rate, Train Batch Size, Group Size, Grad Accumulation and GPUs for SFT in Text, RL in Text, VPFT, VPRL Stage 1/Stage 2 and VPFT* Stage 1/SFT. Numeric formats mix integers, scientific notation and N/A by parameter type.
- **不确定性**：Configuration values rather than estimates; N/A denotes a non-used group size.
- **证据关系**：Table 5 is the training-control companion to the main results and separates optimization conditions from the visual evidence. It supports reproduction of Tables 1–2, Figure 7 and Table 10, and makes the 8×A100 compute setting visible.
- **设计优点**：
  - Grouped headers expose the two VPRL stages and VPFT* controls without duplicating task rows.
  - The parameter rows are aligned across textual and visual planners for direct audit.
  - Scientific notation is used consistently for learning rates.
- **设计缺点**：
  - The table gives hardware count but not wall-clock time, memory or effective token/image batch size.
  - Mixed N/A and numeric cells require readers to infer which hyperparameters apply to each method.
  - The caption does not define abbreviations such as VPFT* or distinguish training from inference settings.
- **可复用模式**：Align hyperparameters by method family and stage, while pairing hardware counts with effective batch, runtime and abbreviation definitions when compute is part of the comparison.
- **证据定位**：page=19，label=Table 5; native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 6 — p.20（appendix，appendix，page_width）

- **表结构**：3 data rows × 3 columns；header_levels=2，row_groups=0，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，32 words）**：“Table 6: We compute the percentage of failed trajectories that are caused by at least one invalid action, rather than a suboptimal but valid action. Lower values indicate better action validity control.”
- **Caption 动作**：title, setup, comparison, main_finding；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Three task rows compare VPRL and VPFT invalid-failure ratios (%): FrozenLake 36.9 vs 60.6, Maze 25.1 vs 73.7 and MiniBehavior 29.6 vs 78.3. Lower is better and VPRL cells are bold.
- **不确定性**：Invalid-failure ratios are point percentages; no failed-trajectory denominator, interval or replicate variation is displayed.
- **证据关系**：Table 6 quantifies the invalid-action mechanism illustrated by Figures 3 and 13–15 and hypothesized in Figure 2. It also sharpens Figure 6’s exploration interpretation by separating invalid failures from valid-but-non-optimal trajectories.
- **设计优点**：
  - The denominator concept is explained directly in the caption, distinguishing invalid from suboptimal failure.
  - A compact three-row table makes the cross-task reduction immediately visible.
  - Bold VPRL values plus the lower-is-better sentence provide a clear direction cue.
- **设计缺点**：
  - The caption does not report the number of failed trajectories behind each ratio.
  - No interval or run-level variability is available for the apparently large task differences.
  - The table does not show the complementary proportion of valid-but-non-optimal failures.
- **可复用模式**：Define a failure subtype in the caption, show task-wise ratios with a direction cue and bold the preferred cells, while reporting the failure counts alongside the percentage.
- **证据定位**：page=20，label=Table 6; centered native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 7 — p.21（appendix，appendix，page_width）

- **表结构**：12 data rows × 11 columns；header_levels=2，row_groups=3，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，29 words）**：“Table 7: Performance of text-based variants of Qwen-2.5-VL-Instruct-3B and 7B on FROZENLAKE. We report Exact Match (EM) and Progress Rate (PR) across all difficulty levels (L3–L6) and their average.”
- **Caption 动作**：title, setup, comparison, abbreviation_definition；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Three model-family blocks contain five textual variants for Qwen 3B, five for Qwen 7B and two LVM-7B visual baselines. EM and PR are split across L3–L6 plus Avg., for 11 physical columns including Model. VPRL is bold in the displayed best row.
- **不确定性**：All EM/PR entries are point estimates; no uncertainty, test counts or significance marks are shown.
- **证据关系**：Table 7 is the complete appendix expansion of main Table 2 and supports Figure 5’s level-wise interpretation. It links the coordinate/ASCII/GRPO qualitative failures in Figures 8–9 to exact EM/PR across difficulty levels.
- **设计优点**：
  - The two-level EM/PR header and repeated L3–L6 columns expose both difficulty and metric dimensions.
  - Model-family groups keep 3B, 7B and visual baselines comparable in one table.
  - The average columns connect directly back to the main-text snapshot.
- **设计缺点**：
  - Twelve data rows and eleven columns create a dense scan path with italic/indented variant labels.
  - Bold best values do not convey uncertainty or whether differences are statistically stable.
  - The caption defines EM/PR but not the exact trajectory-level equality rule used by the paper.
- **可复用模式**：Use one full-factorial appendix table for model × difficulty × metric and keep a compact average snapshot in the main text; preserve family grouping and a stable column order.
- **证据定位**：page=21，label=Table 7; wide native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 8 — p.22（appendix，appendix，page_width）

- **表结构**：2 data rows × 5 columns；header_levels=2，row_groups=0，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，15 words）**：“Table 8: Exact Match performance of VPFT and VPFT* across different grid sizes in FROZENLAKE.”
- **Caption 动作**：title, setup, comparison；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Two rows compare VPFT* and VPFT across 3×3, 4×4, 5×5 and 6×6 FrozenLake grids. Values are EM (%) with one decimal place: VPFT* 86.4/73.6/50.0/33.2 and VPFT 92.0/82.8/68.8/58.0; VPFT is bold.
- **不确定性**：Exact Match percentages are point estimates without uncertainty or test-count columns.
- **证据关系**：Table 8 supplies the exact grid-size values behind the visual-planning portion of Figure 5 and the Stage 1 ablation discussion. It isolates the effect of the VPFT* control from the broader cross-task result in Table 1.
- **设计优点**：
  - The four difficulty columns make the slope difference immediately auditable.
  - Bold VPFT row clearly identifies the preferred training variant.
  - The table is small enough to read without sacrificing the full difficulty slice.
- **设计缺点**：
  - Only EM is shown, so progress quality and invalidity are not visible.
  - No uncertainty or environment count accompanies the percentages.
  - The caption does not define what differs between VPFT and VPFT*; that distinction is left to the appendix prose.
- **可复用模式**：Use a two-row control table to isolate one training choice across a fixed difficulty axis, but define the control and include the companion metric when the claim is multidimensional.
- **证据定位**：page=22，label=Table 8; native PDF table object inspected at 200 dpi，basis=pdf_object。

## Table 9 — p.22（appendix，appendix，page_width）

- **表结构**：2 data rows × 7 columns；header_levels=2，row_groups=0，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，22 words）**：“Table 9: Out-of-distribution (OOD) performance on enlarged grids. Models are trained on smaller grids and evaluated on the sizes indicated in parentheses.”
- **Caption 动作**：title, setup, comparison, abbreviation_definition；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：VPFT and VPRL are compared on FrozenLake 7×7, Maze 7×7 and MiniBehavior 9×9, with EM/PR (%) for each task. VPRL values are bold: 20.4/31.2, 10.0/21.6 and 0.4/14.7 versus VPFT 9.6/15.3, 9.2/17.8 and 0.0/5.8.
- **不确定性**：OOD EM/PR values are point estimates; no uncertainty or OOD sample denominator is shown.
- **证据关系**：Table 9 is the numeric anchor for the OOD claim; Figure 11 visualizes matched failure/success cases and Figure 12 tests a different perturbation. It extends Table 1 beyond the training grid distribution and motivates the qualitative appendix gallery.
- **设计优点**：
  - Task names include the unseen evaluation size in parentheses, so the OOD condition is visible in the header.
  - Paired EM/PR columns preserve the paper’s primary estimands.
  - Bold VPRL cells make the cross-task direction easy to audit.
- **设计缺点**：
  - The very low MiniBehavior EM values need context about task length and test count that the table does not provide.
  - No interval or per-grid sample count is shown.
  - A single enlarged size per task cannot characterize the full OOD scaling curve.
- **可复用模式**：Put the unseen condition directly in grouped headers and retain the same metrics as the main table; report multiple OOD sizes or sample counts when generalization breadth matters.
- **证据定位**：page=22，label=Table 9; native PDF OOD table object inspected at 200 dpi，basis=pdf_object。

## Table 10 — p.27（appendix，appendix，page_width）

- **表结构**：2 data rows × 7 columns；header_levels=2，row_groups=0，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，15 words）**：“Table 10: Performance comparison of VPRL Stage 1 and Stage 2 across all three tasks.”
- **Caption 动作**：title, setup, comparison；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Rows compare VPRL Stage 1 and Stage 2 across FrozenLake, Maze and MiniBehavior, each with EM (%) and PR (%). Stage 1 values are 11.1/27.2, 9.6/22.7 and 0.5/14.2; Stage 2 values are 91.6/93.2, 74.5/77.6 and 75.8/83.8, with the stronger Stage 2 row bolded.
- **不确定性**：EM/PR values are point estimates without run variation or intervals.
- **证据关系**：Table 10 is the outcome-side test of the exploration mechanism in Figure 6 and reward process in Figure 7. It substantiates the main text’s claim that Stage 2 outcome optimization, rather than Stage 1 alone, drives the final planning capability.
- **设计优点**：
  - A two-row design isolates the stage transition with identical task/metric columns.
  - The extreme Stage 1/Stage 2 contrast makes the mechanism claim visually unmistakable.
  - The same EM/PR task order as Table 1 enables direct cross-reference.
- **设计缺点**：
  - No uncertainty or training-curve context explains variation around the stage transition.
  - Stage 1’s low values could be misread without the Figure 6 exploration rationale.
  - The caption does not explain what data or initialization changes between stages.
- **可复用模式**：Use a minimal before/after stage table for a two-stage mechanism, but pair it with an explicit intervention description and learning-dynamics plot.
- **证据定位**：page=27，label=Table 10; native PDF stage-ablation table object inspected at 200 dpi，basis=pdf_object。

## Table 11 — p.31（appendix，appendix，page_width）

- **表结构**：2 data rows × 11 columns；header_levels=2，row_groups=1，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，24 words）**：“Table 11: Exact Match (EM) and Progress Rate (PR) on FROZENLAKE under VPRL when using ground-truth images versus self-generated images as inputs during inference.”
- **Caption 动作**：title, setup, comparison, abbreviation_definition；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Two VPRL input conditions are compared across EM and PR at L3–L6 plus Avg. Self-generated images yield EM 97.6/95.6/90.8/82.4/91.6 and PR 98.4/96.0/93.0/85.6/93.2; ground-truth images yield EM 98.4/95.2/93.2/81.6/92.1 and PR 98.5/95.8/94.1/85.3/93.4. Per-level best cells are bold.
- **不确定性**：EM/PR point estimates only; no uncertainty or replacement-trial count is shown.
- **证据关系**：Figure 16 attributes intermediate-image artifacts to the tokenizer; Table 11 tests whether replacing self-generated states with ground-truth renders changes planning performance. Similar averages support the claim that semantic planning tolerates visual noise.
- **设计优点**：
  - The controlled input swap isolates image quality while holding VPRL and task fixed.
  - The full L3–L6 breakdown makes robustness visible beyond one average.
  - EM and PR are kept in the same header system used throughout the paper.
- **设计缺点**：
  - No uncertainty or paired-test design is reported, so “similar” differences cannot be assessed for stability.
  - The table does not state whether ground-truth images are available at every intermediate step in the replacement condition.
  - Bold per-cell maxima can visually overemphasize tiny differences.
- **可复用模式**：Use a matched input-quality swap with the same task/metric grid as the main result, and predeclare the replacement protocol and equivalence criterion.
- **证据定位**：page=31，label=Table 11; native PDF image-quality table object inspected at 200 dpi，basis=pdf_object。

## Table 12 — p.32（appendix，appendix，page_width）

- **表结构**：8 data rows × 5 columns；header_levels=1，row_groups=2，decimal_precision=1，rules=partial_grid，highlighting=bold。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，27 words）**：“Table 12: Average inference token cost across FROZENLAKE, MAZE, and MINIBEHAVIOR. We also report the average of the task-level average costs. Higher values indicate higher computational cost.”
- **Caption 动作**：title, setup, comparison, encoding_key；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Eight model/variant rows are grouped into Closed-Source and Open-Source Models. Three task columns and one Avg. column report mean inference token cost; values range from 10.7 to 1,619.9 and are shown to one decimal place.
- **不确定性**：Average generated-token costs are point summaries without token-count dispersion or latency intervals.
- **证据关系**：Table 12 supplies the efficiency trade-off omitted from the headline performance Table 1. It supports the appendix cost discussion comparing visual generation overhead with textual CoT and frames the practical interpretation of VPRL’s performance.
- **设计优点**：
  - The task columns and Avg. column make both per-task and overall cost visible.
  - Model-family groups align with Table 1, making performance/cost cross-reading straightforward.
  - The caption provides the direction of the cost measure.
- **设计缺点**：
  - Token count is only a proxy for runtime, memory or monetary cost.
  - No uncertainty, output-length distribution or hardware normalization is shown.
  - The table does not visually mark the performance-cost frontier; readers must join it to Table 1.
- **可复用模式**：Keep a task-by-model cost table aligned with the headline model order, define the aggregation and direction in the caption, and pair token count with latency or resource use when feasibility is claimed.
- **证据定位**：page=32，label=Table 12; wide native PDF cost table object inspected at 200 dpi，basis=pdf_object。

## Table 13 — p.32（appendix，appendix，inset）

- **表结构**：5 data rows × 2 columns；header_levels=1，row_groups=1，decimal_precision=1，rules=partial_grid，highlighting=none。
- **字体**：Nimbus Roman No9 L, Computer Modern math；body≈8.0 pt，header≈8.5 pt，header_weight=bold，provenance=pdf_object，confidence=high。
- **Caption（PDF 文字规范化，13 words）**：“Table 13: Average inference token cost of trained textual planner variants on FROZENLAKE.”
- **Caption 动作**：title, setup；headline_bold=False，self_contained=True，main_finding_stated=False。
- **数据与统计**：Five trained textual Qwen variants are listed in a compact Model/Token Cost inset: Direct 10.7, Coordinates 179.0, ASCII 84.3, GRPO with VPRL progress reward 129.8 and GRPO with PR metric reward 74.9. Values use one decimal place.
- **不确定性**：Average token costs are point summaries; no dispersion or latency is given.
- **证据关系**：Table 13 expands the text-variant cost discussion associated with Table 2 and contrasts representation/reward overheads. Together with Table 12 it contextualizes the computational price of visual planning versus textual reasoning.
- **设计优点**：
  - The inset is compact and keeps the detailed text-cost breakdown beside the cost narrative.
  - Indentation preserves SFT and GRPO variant hierarchy.
  - A single cost column avoids a misleading cross-task aggregation for this FrozenLake-only comparison.
- **设计缺点**：
  - The caption does not state the inference prompt or tokenization rule.
  - No uncertainty or relation to the EM/PR values in Table 2 is visible.
  - The narrow inset and italic row labels are easy to overlook.
- **可复用模式**：Use a small one-task cost inset for an ablation detail, but include a direct performance-cost join or cross-reference so the extra tokens have an interpretable payoff.
- **证据定位**：page=32，label=Table 13; right-column inset native PDF table object inspected at 200 dpi，basis=pdf_object。

## 跨对象系统

- **visual_narrative**：主叙事按“Figure 1 模态动机 → Figure 2 VPRL 闭环 → Table 1/2 主比较 → Figure 3/4 轨迹与案例 → Figure 5/6 鲁棒性与探索机制”展开；附录再用 Figure 7、Tables 3–10 补足训练/数据/失败/OOD，Figures 11–16 和 Tables 11–13 收束泛化、图像质量与成本。
- **caption_system**：所有 caption 都以 Figure/Table n: 开头并置于对象下方；主图 caption 通常包含 title、setup、comparison 和结果方向，部分对象用 Appendix 指针或 uncertainty 定义补充。Figure 15 是明显的 title-only 例外，Figure 4/8/9 等 qualitative case 的抽样边界仍依赖正文。
- **table_header_system**：性能表稳定使用 Model/Task/Metric 分组、EM (%) 与 PR (%) 子列及 Avg.；附录按 grid level、task、stage 或 cost 复用同一层级表头。表格以部分横竖规则、缩进方法行和粗体 preferred row/cell 编码层级与方向。
- **method_result_ablation_link**：Figure 2 的视觉状态→解析→typed reward→GRPO 更新在 Figure 6/7 和 Table 10 中得到机制/阶段消融，Figure 3/13–15 与 Table 6 将 optimal/non-optimal/invalid taxonomy 回连到失败模式。
- **main_appendix_link**：主文 Figure 3 指向 Appendix F.6，Table 2 指向 Table 7；Figure 5/6 的 scaling/exploration 解释分别由 Figures 10/7 和 Tables 8/10 扩展，Table 1 的 OOD、图像质量和成本边界则由 Tables 9/11–13 与 Figures 11–16 补足。
- **typography_consistency**：页面文字和 native tables 的 Nimbus Roman/Computer Modern 对象稳定；raster figure 内部主要是 sans-serif/Google-Sans-like 标签，字号随 qualitative density 下降，图内字体并未完全统一。
- **color_consistency**：方法图与 qualitative traces 多用 pastel/natural colors，quantitative charts 重复 VPRL green、VPFT peach、Gemini blue、Qwen pink、CoT gray；但 screenshot 和 reward 图使用局部色表，跨对象颜色语义需依赖图例或标签。

## 最终判断

- **一句话视觉策略**：论文以“视觉状态替代语言中间推理”为主线，先用模态示意和 VPRL 闭环建立接口，再以 EM/PR 主表、难度/探索消融、失败类型画廊、OOD 配对和图像质量/成本附录组成从机制到边界的证据链。
- **最可复用模式**：
  - 用三行模态对照（Figure 1）把抽象 representation gap 变成可见接口，再用单一箭头语法接到方法环路。
  - 用 Figure 2 的“预测图像→状态/动作解析→typed reward→策略更新”闭环把机制组件和后续消融绑定。
  - 用 main 的紧凑平均表 + appendix 的难度/任务分解表（Tables 1/2/7–11）同时服务 headline 与可审计细节。
  - 用同一 optimal/non-optimal/invalid trace gallery（Figures 3、13–15）跨环境复用视觉故障词典，并由 Table 6 给出失败子类型比例。
- **最高价值对象**：
  - Figure 2：最完整地连接视觉生成、动态解释器、reward 和 GRPO 更新。
  - Table 1：在统一 EM/PR 表头下给出三任务主结果和平均值。
  - Figure 6 + Table 10：分别显示探索机制与 Stage 1/Stage 2 outcome gap。
  - Table 9 + Figure 11：将 OOD 泛化从数值对比落实到 matched visual traces。
- **失败模式**：
  - 定性截图和高密度 trajectory gallery 依赖小字号与自然色，缩放/灰度下可读性下降。
  - 绝大多数 Figure/Table 只给点估计或代表性案例，缺少重复、分母和不确定性，尤其 Figure 6 的“significantly”缺少可见依据。
  - 方法/任务颜色在 chart 子系统内可复用，但 screenshot、reward curve 和 natural montage 的跨对象语义不完全稳定。
  - Figure 15 的 caption 只给标题；多幅 qualitative figure 也没有在 caption 中定义选择标准和样本覆盖。

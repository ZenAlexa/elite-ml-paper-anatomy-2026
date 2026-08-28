# Visual audit — iclr-2026-4ddcea898ef4

## 范围与事实源

- 论文：**Latent Fourier Transform**（ICLR 2026；Mason L. Wang、Cheng-Zhi Anna Huang）。
- 清单事实源：`corpus/pdfs/iclr-2026-4ddcea898ef4.pdf`；`pdfinfo` 显示 32 页、letter、612×792 pt，`pdfimages -list` 与嵌入字体对象用于区分栅格/矢量和字体家族。
- 渲染：全部 32 页按 **200 dpi** PNG 渲染（高于协议要求的 180 dpi），逐页检查正文、参考文献、附录和附录 Table of Contents；对象页逐一放大复核，非对象页用 contact sheet 排查隐藏 Figure/Table。
- PDF 清单与 reading 对齐：13 个 Figure、12 个 Table；PDF 另有 Algorithm 1（p.5）、Algorithm 2/3（p.7），它们已检查并在下方列为算法范围，但最新 schema 只收录 Figure/Table，故不进入 JSON 计数或 `figures`/`tables` 数组。
- 正文边界：p.1–10；参考文献/可复现性：p.11–16；附录目录 p.17；附录对象从 p.18 开始。正文对象为 Figures 1–5、Table 1；附录对象为 Figures 6–13、Tables 2–12。

## PDF 对象清单核对

| PDF 对象 | 页码 | 模块/用途 | JSON 计入 |
|---|---:|---|---|
| Figure 1–2 | 4–5 | 理论分解、方法接口 | 是 |
| Algorithm 1–3 | 5、7 | 训练、条件生成、blending 伪代码 | 否（schema 无 algorithm 类型） |
| Table 1 | 9 | MTG-Jamendo 主结果 | 是 |
| Figure 3–5 | 10 | 听测、频率隔离、属性解释 | 是 |
| Tables 2–7 | 18–20 | encoder/decoder/training/mask 复现细节 | 是 |
| Figure 6 / Table 8 | 21–22 | 听测界面与显著性 | 是 |
| Tables 9–10；Figures 7–10 | 24–26 | B.1 组件消融与谱图例子 | 是 |
| Tables 11–12 | 27 | GTZAN、Maestro | 是 |
| Figure 11–13 | 28–30 | 解释性、移除 DFT、per-band error | 是 |


## 源码与视觉源核查

- `reports/tables/visual_source_inventory.csv` 将该 paper 标为 `no_public_source_found`，`corpus/visual_sources/iclr-2026-4ddcea898ef4/` 不存在可用文件。
- PDF p.18 脚注明确链接 `https://github.com/maswang32/latentfouriertransform/`；`gh repo view` 确认公开仓库、默认分支 `main`，本轮检查 commit `c6455088bf8e3049ad2bdc772120a891e532037c` 的递归树。
- 仓库没有提交的 PNG/JPEG/SVG/PDF/TEX/TikZ/PGF/notebook 图表资产或表格生成器；README 明确说 `reproduce_results/sweep/sweep.py` 产生 Figure 5 preservation curves、`reproduce_results/demos/eq_plots.py` reproduces EQ/blending figures，因此 JSON 记录这两个程序性来源，但不把它们冒充为精确 PDF composition source。最终状态为 `repository_without_visual_source`。

## 逐对象审计

### Figure 1（PDF p.4）
- **模块**：theory；**证据**：page=4，label=Figure 1，basis=rendered_observation。
- **设计**：['conceptual_diagram']；purpose=['theory_mechanism']；placement=main；width=inset；complexity=3/5，6 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=vector；x=none，y=none，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=None，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=1.0，provenance=rendered_estimate。
- **编码/数据**：x=sample index n and the schematic signal trace；y=signal amplitude；color=original signal versus component traces；shape=stacked component cards；line=sinusoidal traces；facet=k = 0, 1, 2, 3, …, 8 cards；text=x, k labels, and Eq. 1 pointer。An illustrative x ∈ R^16 signal is shown as a sum of real sinusoids; it is a mathematical example rather than an empirical sample or estimate.
- **caption/header**：Figure 1: x ∈ R^{16} decomposed via Eq 1.（word_count=9；moves=['setup', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：Introduction/method motivation for Fourier orthogonality → Figure 1 makes the decomposition legible → Eq. 1 and Appendix D.1 supply the derivation → the latent-frequency controls in Figures 4–5 reuse this mechanism. The figure establishes a mechanism, not a performance claim.
- **strengths**：The stacked cards make the basis expansion and the omitted middle components immediately readable.；Position and k labels preserve the frequency/component identity even without relying on color.
- **weaknesses**：The signal and component traces are schematic and have no numeric x/y ticks or amplitude scale.；The ellipsis hides most components, so it cannot be used to verify a numerical reconstruction.
- **reusable_pattern**：Use a source trace followed by a vertically stacked, labeled basis-expansion strip when introducing an orthogonal decomposition.

### Figure 2（PDF p.5）
- **模块**：method；**证据**：page=5，label=Figure 2，basis=rendered_observation。
- **设计**：['pipeline', 'architecture', 'conceptual_diagram']；purpose=['method_interface', 'theory_mechanism']；placement=main；width=double_column；complexity=4/5，1 panels，series=None，legend_items=0，annotations=2。
- **plot_grammar**：rendering=mixed；x=none，y=none，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=None，line_styles=2，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=1.5，provenance=rendered_estimate。
- **编码/数据**：x=left-to-right processing order；y=None；color=red training path versus blue user/inference path; pastel component roles；shape=rounded input/output cards and hourglass-like encoder/decoder blocks；line=arrows for data flow, Add Noise, and Reconstruction Loss；facet=none；text=Input, Encoder, DFT, Latent Spec., masks, DFT^{-1}, Decoder, Variation。A workflow schematic for waveform/spectrogram input, latent encoding, DFT masking, inverse DFT, diffusion decoding, and output variation; no empirical observations or uncertainty are plotted.
- **caption/header**：Figure 2: Latent Fourier Transform (LATENTFT). We encode audio (which may be represented as a waveform or spectrogram) into a series of latent vectors and compute a latent spectrum. During training (red), this spectrum is masked randomly and used to reconstruct the input. During inference (blue), the user specifies a spectral mask, which selects features from the input at specific latent frequencies and conditions a generative process.（word_count=67；moves=['title', 'setup', 'encoding_key', 'comparison']；headline_bold=True；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Method overview and Algorithms 1–3 → Figure 2 binds encoder/DFT/mask/decoder to the red training and blue inference paths → Tables 2–7 provide reproducibility details → Tables 9–10 test the corresponding components.
- **strengths**：The two colored paths explicitly separate training-time random masking from inference-time user masks.；The schematic includes both waveform and spectrogram interfaces and names the latent spectrum operation.
- **weaknesses**：The raster thumbnails and small labels make the figure dependent on color and zoom.；The decoder's diffusion/noise state and exact tensor dimensions are not shown.
- **reusable_pattern**：Represent a method interface as a left-to-right pipeline with a visually distinct training path and user-control path.

### Figure 3（PDF p.10）
- **模块**：results；**证据**：page=10，label=Figure 3，basis=rendered_observation。
- **设计**：['bar']；purpose=['main_comparison', 'qualitative_evidence']；placement=main；width=single_column；complexity=3/5，2 panels，series=4，legend_items=0，annotations=0。
- **plot_grammar**：rendering=vector；x=linear，y=categorical，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=error_bar，line_width_pt=0.8，provenance=rendered_estimate。
- **编码/数据**：x=number of wins (0–125)；y=system category；color=system identity；shape=None；line=thin horizontal uncertainty whiskers；facet=Audio Quality versus Ability to Blend；text=panel titles, system labels, and axis titles。Counts of head-to-head wins from the 29-musician, pairwise listening study, split into audio quality and ability to blend; thin error bars are visible but their statistic is not defined in the caption.
- **caption/header**：Figure 3: Listening study with pairwise comparisons. We achieve the most head-to-head wins on both criteria.（word_count=16；moves=['setup', 'comparison', 'main_finding']；headline_bold=False；self_contained=False；main_finding_stated=True）。
- **evidence relation**：Section 4.4 listening-study design → Figure 3 is the subjective outcome → Figure 6 documents the survey question and Table 8 reports pairwise significance. It complements, rather than duplicates, the objective metrics in Table 1.
- **strengths**：Two criteria are placed in matched panels with a common wins scale.；Direct y-axis labels remove a separate legend and make the headline ordering fast to scan.
- **weaknesses**：The caption does not name the 29 participants, the two criteria, or the error-bar definition.；Color is the only visual distinction among systems and is not reliably grayscale-safe.
- **reusable_pattern**：Use paired horizontal win-count panels with a common axis when a human study has two aligned preference criteria.

### Figure 4（PDF p.10）
- **模块**：results；**证据**：page=10，label=Figure 4，basis=rendered_observation。
- **设计**：['heatmap', 'qualitative_grid']；purpose=['mechanism', 'qualitative_evidence']；placement=main；width=single_column；complexity=3/5，3 panels，series=None，legend_items=0，annotations=2。
- **plot_grammar**：rendering=mixed；x=time，y=log，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=time (s)；y=audio frequency (Hz), logarithmic-looking octave ticks；color=spectrogram energy；shape=None；line=None；facet=Reference, 0–1 Latent Hz, 7.5–8.5 Latent Hz；text=panel titles, Bass/Bass Reduced labels, and 8 Hz Accentuated annotation。Three approximately 5-second mel-spectrogram renderings of one electronic clip: reference, 0–1 Hz latent isolation, and 7.5–8.5 Hz latent isolation; no sample aggregation or uncertainty is shown.
- **caption/header**：Figure 4: Isolating frequencies from an electronic music clip. We show three audio spectrograms. The second spectrogram smooths the reference spectrogram, and the third accentuates patterns occurring at 8 Hz while removing lower-frequency patterns, like the bass.（word_count=37；moves=['setup', 'encoding_key', 'comparison', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：Section 4.5's frequency-isolation claim → Figure 4 provides a qualitative realization → Appendix A.8 describes self-blending and Algorithm 3 supplies the blending operation. It is a mechanism demonstration, not a metric comparison.
- **strengths**：Shared time/frequency framing makes the smoothing and 8 Hz accent visually comparable.；The annotation and bass labels connect the latent-band operation to an audible musical pattern.
- **weaknesses**：The sequential palette has no colorbar or energy units, so absolute intensity is not interpretable.；Only one electronic clip is shown and the caption does not state the spectrogram transform parameters.
- **reusable_pattern**：Show reference and band-isolated spectrograms side by side with shared axes and one explicit musical interpretation annotation.

### Figure 5（PDF p.10）
- **模块**：results；**证据**：page=10，label=Figure 5，basis=rendered_observation。
- **设计**：['line']；purpose=['mechanism', 'qualitative_evidence']；placement=main；width=single_column；complexity=3/5，2 panels，series=4，legend_items=4，annotations=0。
- **plot_grammar**：rendering=vector；x=log，y=linear，grid=both；legend=True (inside lower right)，shared_legend=False，direct_labels=False；markers=0，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=1.1，provenance=rendered_estimate。
- **编码/数据**：x=latent frequency (Hz), log-scaled presentation；y=normalized preservation (0–1)；color=musical attribute；shape=None；line=four solid curves per song；facet=Rock Song and Jazz Song；text=panel titles, axis titles, and legend。Smoothed normalized preservation curves for genre, chords, tempo, and predominant pitch across a latent-frequency sweep for one Rock and one Jazz reference song; no confidence bands or replicate variability are shown.
- **caption/header**：Figure 5: Preservation curves indicating where tempo, pitch, genre reside in in the latent spectra of two reference songs.（word_count=19；moves=['setup', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Section 4.6 asks where attributes reside → Figure 5 supplies the main interpretability curves → Appendix A.9 defines the sweep metrics and Figure 11 extends it to eight song panels. The plot supports a distribution-by-frequency interpretation, not causal attribution.
- **strengths**：Matched panels, fixed 0–1 y-range, and a repeated four-item legend support cross-song comparison.；A log-like frequency axis gives high-frequency bands usable visual width while retaining Hz labels.
- **weaknesses**：The caption has a duplicated 'in' and does not state the smoothing or number of variants per bin.；Curves can cross heavily and have no uncertainty display, making small differences easy to overread.
- **reusable_pattern**：Use a fixed-scale, multi-attribute preservation sweep with repeated panels for representative experimental units.

### Figure 6（PDF p.21）
- **模块**：appendix A.7 listening-study details；**证据**：page=21，label=Figure 6，basis=rendered_observation。
- **设计**：['screenshot']；purpose=['experimental_design', 'qualitative_evidence']；placement=appendix；width=page_width；complexity=3/5，1 panels，series=None，legend_items=0，annotations=8。
- **plot_grammar**：rendering=raster；x=none，y=none，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=None；y=None；color=interface hierarchy only；shape=audio-player controls and Likert radio buttons；line=None；facet=Inputs, Blendings, and two survey questions；text=Example 3, player labels, instructions, and five Likert response anchors。A single survey screen with two input players, two blending players, and two five-point Likert questions; it is a UI artifact rather than an observational dataset.
- **caption/header**：Figure 6: A question from our listening study survey. A participant will compare each ordered pair of systems in the study once.（word_count=22；moves=['setup', 'comparison']；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **evidence relation**：Appendix A.7 survey protocol → Figure 6 shows the task participants performed → Figure 3 aggregates wins and Table 8 reports pairwise tests. It makes the listening-study measurement interface reproducible.
- **strengths**：The screenshot exposes the comparison unit and response anchors rather than describing them only in prose.；Inputs, outputs, instructions, and rating rows are spatially grouped in the same screen.
- **weaknesses**：Small screenshot text is difficult to read at paper scale and depends on a web-player rendering.；The figure does not show randomization, attention checks, or participant-level responses.
- **reusable_pattern**：Include one complete survey-screen screenshot when a subjective measurement depends on a multi-stage comparison UI.

### Figure 7（PDF p.25）
- **模块**：ablation B.1 correlation masking；**证据**：page=25，label=Figure 7，basis=rendered_observation。
- **设计**：['heatmap', 'matrix']；purpose=['mechanism', 'ablation']；placement=appendix；width=single_column；complexity=2/5，1 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=mixed；x=categorical，y=categorical，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=latent frequency bin (categorical index)；y=example index 0–7；color=binary mask state；shape=None；line=None；facet=None；text=Uncorrelated Masking title and axis labels。Eight illustrative binary masks over approximately 128 latent-frequency bins; no aggregate statistic or uncertainty is shown.
- **caption/header**：Figure 7: Example masks where there is no correlation between the scores associated with each frequency bin. The masks are speckled and erratic.（word_count=23；moves=['setup', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1's claim that independent bin scores create local leakage → Figure 7 visualizes the speckled mask failure → Figure 8 shows the correlated alternative → Tables 9–10 quantify the quality/adherence degradation without correlation.
- **strengths**：The matrix layout makes local fragmentation visible across many examples.；A common bin axis enables direct visual contrast with Figure 8.
- **weaknesses**：There is no legend defining which color is masked versus unmasked.；The examples are illustrative and do not state the random seed or mask rate.
- **reusable_pattern**：Contrast independent and locally correlated binary masks as matched matrices with the same axes.

### Figure 8（PDF p.25）
- **模块**：ablation B.1 correlation masking；**证据**：page=25，label=Figure 8，basis=rendered_observation。
- **设计**：['heatmap', 'matrix']；purpose=['mechanism', 'ablation']；placement=appendix；width=single_column；complexity=2/5，1 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=mixed；x=categorical，y=categorical，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=latent frequency bin (categorical index after log-frequency mapping)；y=example index 0–7；color=binary mask state；shape=None；line=None；facet=None；text=Our Masking title and axis labels。Eight illustrative binary masks with long contiguous regions across approximately 128 bins; no aggregate statistic or uncertainty is shown.
- **caption/header**：Figure 8: Example masks from our masking strategy, where bin scores are locally correlated after being mapped to a logarithmic axis. The mask forms contiguous regions.（word_count=26；moves=['setup', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1's locally correlated score mechanism → Figure 8 shows the intended contiguous structure → Figure 7 is the negative control → Tables 9–10 measure downstream effects.
- **strengths**：The matched matrix form isolates correlation as the visual difference from Figure 7.；The long runs make the inference-time user-mask analogy easy to inspect.
- **weaknesses**：As in Figure 7, the binary color semantics are not defined in a legend.；The logarithmic remapping is asserted in the caption but not shown as a secondary axis or tick transform.
- **reusable_pattern**：Use matched binary-mask matrices to show why a local correlation prior changes the topology of an intervention.

### Figure 9（PDF p.26）
- **模块**：ablation B.1 conditional-generation examples；**证据**：page=26，label=Figure 9，basis=rendered_observation。
- **设计**：['heatmap', 'qualitative_grid']；purpose=['ablation', 'qualitative_evidence', 'failure']；placement=appendix；width=page_width；complexity=4/5，6 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=mixed；x=time，y=log，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=time (s)；y=audio frequency (Hz), octave-like ticks；color=mel-spectrogram energy；shape=None；line=None；facet=Reference, LATENTFT, w/o Freq. Masking, w/o Correlation, w/o Log. Scale, w/o Encoder；text=panel titles and shared Time/Hz labels。Six qualitative mel-spectrogram panels for one 0.68–2.70 Hz conditional-generation example: one reference, the full model, and four ablations; no aggregate or uncertainty display.
- **caption/header**：Figure 9: A conditional generation example, where we take 0.68–2.70 Hz from the latent spectrum of the reference (top left). LATENTFT generates a variation capturing the rhythmic pattern near 2 Hz. The frequency-masking, correlation, and log-scaling ablations also have a pattern near 2 Hz, but the audio quality is much worse. The encoder ablation does not follow the conditioning.（word_count=61；moves=['setup', 'comparison', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1 component ablations → Figure 9 gives the conditional qualitative counterpart of Table 9 → the frequency/correlation/log-scale panels retain a 2 Hz pattern while encoder removal breaks adherence.
- **strengths**：A six-panel grid keeps the reference and all ablations in one visual decision surface.；The caption names the selected band and interprets the 2 Hz rhythm, reducing ambiguity about the qualitative comparison.
- **weaknesses**：The quality judgment is qualitative and lacks a common quantitative color scale or audio-quality measure.；The dense small multiples require zooming to inspect high-frequency structure.
- **reusable_pattern**：Pair one reference with the full model and one panel per ablation, while stating the selected conditioning band in the caption.

### Figure 10（PDF p.26）
- **模块**：ablation B.1 blending examples；**证据**：page=26，label=Figure 10，basis=rendered_observation。
- **设计**：['heatmap', 'qualitative_grid']；purpose=['ablation', 'qualitative_evidence', 'failure']；placement=appendix；width=page_width；complexity=4/5，7 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=mixed；x=time，y=log，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=time (s)；y=audio frequency (Hz), octave-like ticks；color=mel-spectrogram energy；shape=None；line=None；facet=Reference 1, Reference 2, LATENTFT, and four ablations；text=panel titles and shared Time/Hz labels。Seven qualitative mel-spectrogram panels for one blending example: two references, LATENTFT, and four ablation variants; no aggregate or uncertainty display.
- **caption/header**：Figure 10: A blending example, where we take 0–0.68 Hz from the first reference, and 10.78–43 Hz from the second reference. LATENTFT generates a variation that contains characteristics from both examples. For instance, the rapid rhythmic patterns of Reference 2 are retained, as well as the horizontal line from Reference 1. The correlation and log-scaling ablations retain some of these characteristics, while the encoder and frequency masking ablations ignore the references.（word_count=73；moves=['setup', 'comparison', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1 blending setup → Figure 10 is the qualitative counterpart of Table 10 → the two selected bands are mapped to the two references and the ablation panels show which components ignore or retain them.
- **strengths**：The two reference panels establish the visual sources before the generated and ablated outputs.；The caption explicitly maps the low/high bands to Reference 1/2 and names interpretable retained structures.
- **weaknesses**：The caption does not enumerate the seven panel labels or state their fixed order.；The spectrogram palette has no colorbar, so intensity differences are qualitative only.
- **reusable_pattern**：For a two-source blend, place both references first, then the full model and matched ablations in a fixed panel order.

### Figure 11（PDF p.28）
- **模块**：appendix B.3 interpretability；**证据**：page=28，label=Figure 11，basis=rendered_observation。
- **设计**：['line']；purpose=['mechanism', 'robustness']；placement=appendix；width=page_width；complexity=4/5，8 panels，series=4，legend_items=4，annotations=0。
- **plot_grammar**：rendering=vector；x=log，y=linear，grid=both；legend=True (inside lower right)，shared_legend=False，direct_labels=False；markers=0，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=1.0，provenance=rendered_estimate。
- **编码/数据**：x=latent frequency (Hz), log-like tick placement；y=preservation (0–1)；color=musical attribute；shape=None；line=four solid curves per panel；facet=eight GTZAN song panels in a 4×2 grid；text=song titles, axis labels, and repeated legends。Smoothed 0–1 preservation curves for four attributes across eight GTZAN song panels (the rendered titles include repeated Blues Song and Hip-hop Song labels); no uncertainty bands or per-song sample counts are shown.
- **caption/header**：Figure 11: More Sweep Examples. Songs are taken from the GTZAN dataset. Generally, genre tends to be a global characteristic, lying around 0 Hz. Chord changes also lie in the low end of the latent spectrum, while tempo and pitch are associated with higher latent frequencies. Please refer to Sec. 4.6 for our motivations behind this experiment, and Appendix A.9 for implementation details.（word_count=65；moves=['title', 'setup', 'encoding_key', 'main_finding', 'appendix_pointer']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：Figure 5's two-song interpretation → Figure 11 expands the same sweep to additional GTZAN examples → Appendix A.9 defines genre/chord/pitch/tempo measurements. It is a robustness/heterogeneity extension, not a new estimator.
- **strengths**：Eight small multiples expose heterogeneity while preserving the same four encodings and axes.；Repeated legends and fixed scales make the qualitative attribute-frequency pattern easy to compare.
- **weaknesses**：The duplicate panel titles ('Blues Song' and 'Hip-hop Song') weaken traceability of the eight examples.；The dense, oscillatory curves and lack of uncertainty make local peaks visually persuasive but statistically unqualified.
- **reusable_pattern**：Extend a main interpretability curve to a fixed-grid panel of real experimental units using identical axes, colors, and legend order.

### Figure 12（PDF p.29）
- **模块**：appendix B.4 removing the latent DFT；**证据**：page=29，label=Figure 12，basis=rendered_observation。
- **设计**：['heatmap', 'qualitative_grid', 'image_montage']；purpose=['failure', 'ablation', 'qualitative_evidence']；placement=appendix；width=double_column；complexity=4/5，6 panels，series=None，legend_items=0，annotations=0。
- **plot_grammar**：rendering=mixed；x=time，y=log，grid=none；legend=False (None)，shared_legend=False，direct_labels=True；markers=0，line_styles=0，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=None，provenance=rendered_estimate。
- **编码/数据**：x=time (s)；y=audio frequency (Hz)；color=mel-spectrogram energy；shape=None；line=None；facet=three rows, each Reference versus Generation；text=Reference/Generation titles and shared Hz/Time labels。Three paired reference/generation mel-spectrogram examples after removing latent DFT masking; the figure is qualitative and shows no aggregate metric or uncertainty.
- **caption/header**：Figure 12: Mel-spectrograms where we remove the DFT during both training and inference. During inference, we condition the diffusion process on the full latent sequence z derived from a reference (left). This reconstructs the input without creating a variation (right).（word_count=40；moves=['setup', 'comparison', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.4 removes the central mechanism → Figure 12 visualizes the failure mode → Tables 9–10 quantify the related w/o frequency-masking degradation and the main conclusion is that the unmasked latent reconstructs rather than varies.
- **strengths**：Repeated Reference/Generation pairing makes the reconstruction-versus-variation failure immediately visible.；Three examples reduce dependence on a single clip while keeping the layout compact.
- **weaknesses**：No quantitative similarity or diversity measure is attached to the displayed pairs.；The shared color scale is not stated, so apparent intensity differences should not be read numerically.
- **reusable_pattern**：Show a mechanism-removal failure as repeated reference/output pairs with identical axes and an explicit failure caption.

### Figure 13（PDF p.30）
- **模块**：appendix B.5 per-band error；**证据**：page=30，label=Figure 13，basis=rendered_observation。
- **设计**：['line']；purpose=['robustness', 'main_comparison', 'mechanism']；placement=appendix；width=double_column；complexity=2/5，2 panels，series=2，legend_items=0，annotations=0。
- **plot_grammar**：rendering=vector；x=unknown，y=linear，grid=both；legend=False (None)，shared_legend=False，direct_labels=True；markers=1，line_styles=1，hatching=False，reference_lines=0，uncertainty=none，line_width_pt=1.2，provenance=rendered_estimate。
- **编码/数据**：x=left: discrete RVQ level; right: latent frequency (Hz) with log-like ticks；y=FAD (Audio Quality), lower is better；color=one line per panel；shape=circle markers；line=solid trend line；facet=RVQ-Based Generation versus LatentFT - UNet；text=panel titles and axis labels。FAD values averaged across 1,024 MTG-Jamendo test songs; the left panel conditions on individual Vampnet RVQ levels and the right on individual LatentFT frequency bands, with no error bars.
- **caption/header**：Figure 13: Conditioning on various RVQ layers in the Vampnet Model (left) and on various latent frequencies in our model (right). Our model maintains generation quality even when conditioning on finer-scale features.（word_count=32；moves=['setup', 'comparison', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.5 tests the fine-scale quality claim → Figure 13 contrasts discrete RVQ depth with latent-frequency conditioning → the result extends Table 1's quality comparison and supports the claim that higher latent frequencies do not cause the RVQ-like degradation.
- **strengths**：The side-by-side panels use the same FAD y-axis and show the contrasting trend directly.；Markers plus connecting lines expose the discrete level/frequency sweep without a legend.
- **weaknesses**：The x-scale semantics differ between panels and are not made explicit by a shared axis label.；The caption omits the 1,024-song averaging detail that appears in the surrounding text.
- **reusable_pattern**：Compare a discrete-token sweep and a continuous/frequency sweep in matched panels with a common quality axis.

### Table 1（PDF p.9）
- **模块**：results；**证据**：page=9，label=Table 1，basis=rendered_observation。
- **设计**：purpose=['headline', 'main_comparison']；placement=main；width=page_width；rows=10，columns=11，header_levels=3，row_groups=2，decimal_precision=3，rules=booktabs，highlighting=['bold']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：No mean±SD, interval, or run-variability display; '-' denotes an unavailable adherence metric or inapplicable task. Point estimates for conditional generation and blending on the MTG-Jamendo test set: four adherence metrics plus FAD for each task, across seven baselines and three LATENTFT variants; arrows encode direction and timbre is divided by 100.
- **caption/header**：Table 1: Results on Conditional Generation and Blending on the MTG-Jamendo Test set. Mel-Cepstral Distortion (Timbre) is divided by 100. Compared to baselines, LATENTFT variants achieve superior adherence and audio quality. The Masked Token Model and Cross Synthesis baselines do not offer frequency-based controls, so we do not compute adherence. Cross Synthesis also only applies to the blending task.（word_count=59；moves=['title', 'setup', 'encoding_key', 'comparison', 'main_finding', 'uncertainty_definition']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：The method's two target applications → Table 1 is the primary objective comparison → Figure 3 tests human preference, Figures 4–5 show qualitative/mechanistic consequences, Tables 9–12 test ablations and additional datasets.
- **strengths**：Two task groups share the same metric vocabulary and expose adherence-quality tradeoffs in one decision surface.；Bold best cells and explicit arrows make directionality visible without color.
- **weaknesses**：All cells are point estimates, so the table cannot distinguish sampling noise or run variability.；The caption explains dashes but not the 1,024-clip denominator or aggregation procedure.
- **reusable_pattern**：Use nested task/adherence/quality headers and direction arrows to place multi-objective model selection in one monochrome table.

### Table 2（PDF p.18）
- **模块**：appendix A.1.1 MLP encoder architecture；**证据**：page=18，label=Table 2，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=5，columns=2，header_levels=1，row_groups=0，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic architecture specification; no uncertainty or repeated runs. Five attribute/value rows specify input, output, frame-wise MLP architecture, hidden dimension 512, and 16 hidden layers.
- **caption/header**：Table 2: MLP Encoder Architecture（word_count=5；moves=['title']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Appendix A.1 encoder choice → Table 2 fixes the MLP implementation used in the LATENTFT-MLP rows of Tables 1, 9, and 10.
- **strengths**：Compact two-column key/value format is easy to reproduce.；The table avoids unnecessary vertical rules and keeps the architecture facts grouped.
- **weaknesses**：The caption does not repeat that the input/output are 80×512 mel/latent sequences.；There is no parameter count or compute/memory field.
- **reusable_pattern**：Record a small architecture as an attribute/value booktabs table with exact tensor shapes and depth.

### Table 3（PDF p.19）
- **模块**：appendix A.1.2 1D U-Net encoder architecture；**证据**：page=19，label=Table 3，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=7，columns=2，header_levels=1，row_groups=0，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic architecture specification; no uncertainty or repeated runs. Seven attribute/value rows specify 80×512 input/output, 1D U-Net, kernel size 3, six resolutions, channels per resolution, and attention resolutions.
- **caption/header**：Table 3: 1D U-Net Encoder Hyperparameters（word_count=6；moves=['title']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Appendix A.1.2 → Table 3 defines the encoder used in the UNet variants of Tables 1, 9–12 and the qualitative panels.
- **strengths**：Lists multiresolution and attention configuration in a compact, readable form.；Long vector-valued settings remain aligned in the value column.
- **weaknesses**：The bracketed resolution/channel arrays require prose context to interpret as a down/up path.；No parameter count or receptive-field summary is provided.
- **reusable_pattern**：Use aligned list-valued cells for multiresolution network configurations rather than expanding each block into many rows.

### Table 4（PDF p.19）
- **模块**：appendix A.1.3 DAC encoder architecture；**证据**：page=19，label=Table 4，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=5，columns=2，header_levels=1，row_groups=0，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic architecture and tensor-shape specification; no uncertainty. Five attribute/value rows describe DAC + 1D U-Net, raw waveform input, 1024×512 DAC embeddings, and the 80×512 latent output.
- **caption/header**：Table 4: DAC Encoder Hyperparameters（word_count=5；moves=['title']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Appendix A.1.3 → Table 4 explains the DAC encoder path behind LATENTFT-DAC in Table 1 and the method comparison narrative.
- **strengths**：The table makes the 1024-channel DAC-to-80-channel U-Net interface explicit.；The short list avoids conflating the pretrained DAC front end with the learned temporal encoder.
- **weaknesses**：The caption calls these hyperparameters although most entries are architecture/shape facts.；Sampling rate and checkpoint/version details are not included.
- **reusable_pattern**：Separate a pretrained frontend's embedding shape from the learned encoder in a compact interface table.

### Table 5（PDF p.19）
- **模块**：appendix A.2 decoder/diffusion model architecture；**证据**：page=19，label=Table 5，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=8，columns=2，header_levels=1，row_groups=0，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic decoder specification; no uncertainty or repeated runs. Eight attribute/value rows specify noisy mel and frequency-masked latent inputs, clean mel output, and the 1D U-Net kernel/resolution/attention configuration.
- **caption/header**：Table 5: Decoder Hyperparameters（word_count=4；moves=['title']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Appendix A.2 decoder description → Table 5 fixes the decoder interface used by Figure 2 and Algorithms 1–3.
- **strengths**：Input 1/Input 2/Output rows map cleanly to the pipeline's decoder boundary.；Configuration mirrors Table 3, making encoder/decoder differences easy to compare.
- **weaknesses**：The concatenation operation described in prose is not represented as a diagram or table field.；No diffusion schedule or sampling-step count appears here.
- **reusable_pattern**：Use explicit Input 1/Input 2/Output rows before shared architecture rows for a conditional decoder.

### Table 6（PDF p.20）
- **模块**：appendix A.3 training details；**证据**：page=20，label=Table 6，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=13，columns=3，header_levels=1，row_groups=4，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic training settings; no uncertainty or run-variance display. Grouped rows report schedule (700k/4k/350k/cosine), optimizer (Adam/1e−4/β values), batching (1024/256/DDP), and other precision/gradient/EMA settings.
- **caption/header**：Table 6: Training Hyperparameters（word_count=4；moves=['title']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Appendix A.3 → Table 6 binds training choices to all main and ablation metrics; the 350k ablation schedule is described immediately above.
- **strengths**：Four bold row-group labels create a clear hierarchy without vertical rules.；Mixed symbolic and numeric values are aligned in a stable attribute/value structure.
- **weaknesses**：The table mixes main-run and implementation settings without a column marking which rows differ for ablations.；The caption does not state hardware (4 L40S) or the two-stage annealing context given in prose.
- **reusable_pattern**：Group training hyperparameters by schedule, optimizer, batching, and precision/EMA to make a dense recipe scannable.

### Table 7（PDF p.20）
- **模块**：appendix A.4 other hyperparameters；**证据**：page=20，label=Table 7，basis=rendered_observation。
- **设计**：purpose=['reproduction']；placement=appendix；width=single_column；rows=7，columns=3，header_levels=1，row_groups=2，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Deterministic mask/diffusion values; no uncertainty or repeated runs. Two groups list DFT/frequency-mask parameters (L, σ, p, ε) and diffusion parameters (σmax, α, β). Values mix integers, decimals, and scientific notation.
- **caption/header**：Table 7: Other Hyperparameters. Full descriptions can be found in the Methods section (Sec. 3)（word_count=15；moves=['title', 'appendix_pointer']；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **evidence relation**：Methods Sec. 3 → Table 7 supplies the constants used by Algorithm 1 and the frequency masks visualized in Figures 7–8.
- **strengths**：The two-level group/parameter/value layout makes symbols and values easy to match.；The caption points readers back to the method definitions.
- **weaknesses**：Symbols are not defined in the table itself and the caption depends on Sec. 3.；Mixed precision formats are not normalized to a single decimal convention.
- **reusable_pattern**：Use a grouped symbol/value table for compact mathematical hyperparameters, with a caption pointer to definitions.

### Table 8（PDF p.22）
- **模块**：appendix A.7 listening-study significance；**证据**：page=22，label=Table 8，basis=rendered_observation。
- **设计**：purpose=['robustness']；placement=appendix；width=page_width；rows=6，columns=4，header_levels=1，row_groups=0，decimal_precision=None，rules=booktabs，highlighting=['none']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：P-values are the uncertainty/significance summary; an asterisk marks the stated non-significant pairs after the paper's correction. No confidence interval or effect-size column is shown. Six pairwise system comparisons with p-values for Audio Quality and Ability to Blend, shown in scientific notation with varying significant digits.
- **caption/header**：Table 8: Results from a Kruskal-Wallis H test performed on listening study results. All pairs of systems have statistically significant differences in audio quality, except for ILVR and Cross Synthesis. All pairs of systems have statistically significant differences in “Ability to Blend” besides LATENTFT and Cross Synthesis. These pairs are indicated with an asterisk (*).（word_count=54；moves=['title', 'setup', 'comparison', 'uncertainty_definition', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：Figure 6 survey interface → Figure 3 win counts → Table 8 supplies pairwise significance context for the subjective headline; the reported test label follows the PDF caption.
- **strengths**：System-pair rows make the comparison universe explicit.；The asterisk convention is explained in the caption instead of requiring a separate legend.
- **weaknesses**：The caption's test description is not aligned with the surrounding prose's post-hoc Wilcoxon/Bonferroni description.；P-values without effect sizes or sample counts do not convey practical preference magnitude.
- **reusable_pattern**：Report pairwise subjective-study tests in a compact pair-by-pair table with an explicit significance marker definition.

### Table 9（PDF p.24）
- **模块**：ablation B.1 conditional generation；**证据**：page=24，label=Table 9，basis=rendered_observation。
- **设计**：purpose=['ablation']；placement=appendix；width=page_width；rows=6，columns=6，header_levels=2，row_groups=0，decimal_precision=3，rules=booktabs，highlighting=['bold']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Point estimates only; no standard deviation, interval, or run-to-run variation is displayed. Conditional-generation adherence (Loudness/Rhythm/Timbre/Harmony) and FAD for LATENTFT-MLP versus five component variants, trained for the 350k-step ablation schedule.
- **caption/header**：Table 9: Ablation results on the Conditional Generation Task. Mel-Cepstral Distortion (Timbre) is divided by 100. Ablating any component of the model generally leads to worse audio quality and adherence.（word_count=30；moves=['title', 'setup', 'comparison', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1 component hypotheses → Table 9 quantifies conditional-generation degradation → Figures 7–9 visualize correlation/log-scale/encoder failure modes → Table 1 is the full-run headline reference.
- **strengths**：The two-level Adherence/Quality header maps metrics to the task objective.；Bold best cells highlight the full model/metric winners in monochrome.
- **weaknesses**：The generic 'generally' conclusion hides metric-specific tradeoffs and the w/o Encoder FAD exception.；The caption does not state the 1,024-song denominator or whether values are means over runs.
- **reusable_pattern**：Keep a single task's adherence metrics and quality metric together, with matched rows for each mechanism ablation.

### Table 10（PDF p.24）
- **模块**：ablation B.1 blending；**证据**：page=24，label=Table 10，basis=rendered_observation。
- **设计**：purpose=['ablation']；placement=appendix；width=page_width；rows=6，columns=6，header_levels=2，row_groups=0，decimal_precision=3，rules=booktabs，highlighting=['bold']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Point estimates only; no standard deviation, interval, or run-to-run variation is displayed. Blending adherence (Loudness/Rhythm/Timbre/Harmony) and FAD for LATENTFT-MLP versus five component variants under the ablation schedule.
- **caption/header**：Table 10: Ablation results on the Blending Task. Mel-Cepstral Distortion (Timbre) is divided by 100. Ablating any component of the model generally leads to either significantly worse audio quality, or significantly worse adherence.（word_count=33；moves=['title', 'setup', 'comparison', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.1 blending claim → Table 10 quantifies the tradeoff between adherence and quality → Figure 10 gives the corresponding two-reference qualitative example → Table 1 supplies full-run context.
- **strengths**：Identical columns to Table 9 make task differences easy to compare.；Bold cells expose which mechanism removal changes each metric's best value.
- **weaknesses**：The caption's 'either' wording does not identify which metric fails for each row.；No uncertainty or multiple-seed information is shown for the ablations.
- **reusable_pattern**：Mirror conditional-generation and blending ablation tables so the mechanism comparison has a stable visual grammar.

### Table 11（PDF p.27）
- **模块**：appendix B.2 GTZAN results；**证据**：page=27，label=Table 11，basis=rendered_observation。
- **设计**：purpose=['robustness', 'main_comparison', 'dataset']；placement=appendix；width=page_width；rows=8，columns=11，header_levels=3，row_groups=2，decimal_precision=3，rules=booktabs，highlighting=['bold']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Point estimates on the GTZAN evaluation clips; no uncertainty, interval, or run-variance display. Dashes denote unavailable adherence or inapplicable tasks. The same 10 metrics as Table 1 are reported for six baselines and two LATENTFT variants on GTZAN; timbre is divided by 100.
- **caption/header**：Table 11: Results on Conditional Generation and Blending on the GTZAN dataset. Compared to baselines, LATENTFT achieves superior adherence and audio quality, demonstrating the generality of LATENTFT when it comes to new datasets with multiple genres. Mel-Cepstral Distortion (Timbre) is divided by 100. The Masked Token Model and Cross Synthesis baselines do not offer frequency-based controls, so we do not compute adherence. Cross Synthesis also only applies to the blending task.（word_count=71；moves=['title', 'setup', 'comparison', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.2 generalization setup → Table 11 tests the main comparison on a multi-genre dataset → Figure 11 expands the GTZAN interpretability sweep; Tables 1 and 12 provide the matched reference datasets.
- **strengths**：Maintains Table 1's nested task/metric header, enabling direct cross-dataset reading.；Caption states the generalization claim and missing-control convention.
- **weaknesses**：No sample count or aggregation definition appears in the caption.；Point estimates make the apparent cross-dataset quality change hard to calibrate.
- **reusable_pattern**：Reuse the main multi-task comparison table unchanged when testing generalization to a new dataset.

### Table 12（PDF p.27）
- **模块**：appendix B.2 Maestro results；**证据**：page=27，label=Table 12，basis=rendered_observation。
- **设计**：purpose=['robustness', 'main_comparison', 'dataset']；placement=appendix；width=page_width；rows=8，columns=11，header_levels=3，row_groups=2，decimal_precision=3，rules=booktabs，highlighting=['bold']。
- **header/typography**：['NimbusRomNo9L-Regu', 'NimbusRomNo9L-Medi']；body/header≈8.7/8.7 pt；header_weight=medium。
- **不确定性/数据**：Point estimates on the Maestro piano evaluation clips; no uncertainty, interval, or run-variance display. Dashes denote unavailable adherence or inapplicable tasks. The same 10 metrics as Table 1 are reported for six baselines and two LATENTFT variants on Maestro, an aligned piano-performance dataset; timbre is divided by 100.
- **caption/header**：Table 12: Results on Conditional Generation and Blending on the Maestro dataset. Even though the Maestro dataset is only piano recordings, LATENTFT demonstrates super audio quality and adherence compared to baselines. Mel-Cepstral Distortion (Timbre) is divided by 100. The Masked Token Model and Cross Synthesis baselines do not offer frequency-based controls, so we do not compute adherence. Cross Synthesis also only applies to the blending task.（word_count=66；moves=['title', 'setup', 'comparison', 'encoding_key', 'main_finding']；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **evidence relation**：B.2 cross-domain setup → Table 12 tests the main comparison on piano-only data → Table 11 tests multi-genre generalization and Table 1 remains the MTG-Jamendo headline.
- **strengths**：The stable header and row order make dataset-specific differences easy to locate.；The caption identifies the piano-only setting and the unavailable-control convention.
- **weaknesses**：The caption contains the PDF's typo 'super audio quality' and does not provide a sample count.；No uncertainty display distinguishes the apparent FAD improvements from evaluation variability.
- **reusable_pattern**：Pair a multi-genre and a single-instrument replication table with identical metric geometry and row order.

## 跨对象系统判断

- **visual_narrative**：Figure 1 从 DFT 正交分解建立理论直觉，Figure 2 将编码-频谱-mask-解码绑定为方法接口，Table 1 给出两项主任务的 objective metrics，Figures 3–5 分别补充听测、频率隔离和属性解释；附录 Figures 7–13 与 Tables 2–12 按实现、消融、跨数据集和失败模式展开。
- **caption_system**：Caption 普遍按标题/设置/比较/结论顺序书写；Table 1、Figures 3–5 和 Figures 9–13 明确给出主要结论，Figure 2 明确定义红/蓝路径。多数 caption 没有样本分母、聚合方式或 uncertainty 定义；附录 caption 通过 Sec./Appendix 指针连接正文。
- **table_header_system**：主结果与跨数据集表统一使用 Conditional Generation/Blending → Adherence/Quality → metric 的三级分组，消融表使用 Adherence/Quality 二级分组，架构表使用 Attribute/Value 键值结构；表格均用 booktabs 风格和方向箭头，不使用竖线或 cell color。
- **method_result_ablation_link**：Figure 2 和 Algorithms 1–3 定义 mask/DFT/decoder 接口；Tables 9–10 逐项移除 frequency masking、correlation、log scale、encoder 与 bandpass augmentation；Figures 7–10 将 mask topology、conditional 和 blending 的后果可视化，Figure 12 则展示移除 latent DFT 的失败。
- **main_appendix_link**：正文 Table 1、Figures 3–5 的每个结论都在 Appendix A/B 找到实现或扩展：Tables 2–7 是复现配方，Figure 6/Table 8 是听测细节，Tables 9–10/Figures 7–10 是消融，Tables 11–12/Figure 11–13 是数据集、解释性和细粒度质量扩展。
- **typography_consistency**：表格系统最一致；图内实验曲线使用 DejaVu Sans，Figure 2 使用 Calibri，Figure 1/正文数学符号使用 Computer Modern/Nimbus Roman。字号在主文小图和附录复合图中变化较大，截图文字最难复核。
- **color_consistency**：四属性曲线在 Figures 5/11 中保持绿/红/橙/蓝映射，spectrogram 图保持紫-橙-黄能量语义，mask 图保持黄/紫二值对比；但系统条形图 Figure 3 和流程图 Figure 2 使用独立色板，且没有跨图统一色标。

## 总结

### 最可复用模式
- Figure 2 的双路径 pipeline：用红色训练路径和蓝色用户推理路径把方法接口与控制点分开。
- Table 1/11/12 的任务→目标→指标三级表头，把 adherence 与 FAD 放在同一黑白决策面并用方向箭头和 bold 冗余编码。
- Figures 5/11 的固定 0–1 preservation sweep：以相同四属性颜色、log-like Hz 轴和重复 small multiples 展示机制异质性。
- Tables 9/10 与 Figures 7–10 的配对消融：数值表回答性能后果，mask/谱图小 multiples 回答机制和失败形态。

### 最高价值对象
- Figure 2：最清楚的方法接口与训练/推理边界。
- Table 1：主任务、基线和三种 LATENTFT 变体的 headline 比较。
- Figure 5 + Figure 11：把 latent frequency 解释连接到属性保存并展示跨歌曲变化。
- Tables 9–10 + Figures 9–10：把组件消融的数值与 qualitative failure 闭合。

### 失败模式
- 绝大多数数值表只有 point estimates，没有 SD/区间/运行变异；Figure 3 的 error bars 也未在 caption 定义。
- Spectrogram 和 binary-mask 图没有 colorbar 或二值语义图例，图内强度/颜色难以脱离正文复核。
- 主结果与跨数据集表没有在 caption 写出样本分母和聚合方式，Table 8 的检验描述与正文 post-hoc 叙述不完全对齐。
- 复合图的小字号、不同渲染后端以及 Figure 11 重复 song titles 提高了对象追踪和精确复核成本。

**一句话视觉策略**：论文用 DFT 分解与双路径流程图建立 latent-frequency 控制的直觉，再用统一 objective tables、human-study bars、preservation sweeps 和 mechanism-aligned ablations 逐层证明控制有效，但不确定性和色标元数据仍主要留在正文叙述之外。

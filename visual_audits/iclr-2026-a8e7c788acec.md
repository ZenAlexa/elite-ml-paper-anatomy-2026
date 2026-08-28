# iclr-2026-a8e7c788acec 视觉审计

## 审计范围与对象清单

- 论文：`DCFOLD: EFFICIENT PROTEIN STRUCTURE GENERATION WITH SINGLE FORWARD PASS`；PDF：`corpus/pdfs/iclr-2026-a8e7c788acec.pdf`；文本缓存：`corpus/text/iclr-2026-a8e7c788acec.txt`。
- 完整读取 PDF 18 页：正文 p.1–10，参考文献 p.11–13，附录 p.14–18；无 supplementary。所有页面按 200 dpi（高于 180 dpi 要求）渲染到 `/tmp/iclr-a8e7c788acec/render200/`，逐页以实际 PDF 对象核对。
- PDF 是清单事实源：7 幅 Figure（正文 Figure 1–5，附录 Figure 6–7）和 9 张 Table（正文 Table 1–6，附录 Table 7–9）。Algorithm 1 是另一个非 Figure/Table 对象；Appendix A 的证明、B/C 的文字与公式不另建视觉记录。
- 自动 inventory 只识别 5 Figure/7 Table，因为 Figure 1、Figure 4、Table 1、Table 6 的 caption 嵌在双栏正文附近；人工页面渲染与 `pdftotext -layout` 确认它们实际存在，故本审计按 7/9 记录。
- `pdfimages -list` 确认 Figure 2、Figure 6–7 含嵌入图像，Figure 4 含色条图像；Figure 1、Figure 3、Figure 5 和表格主要由 PDF vector/text 对象组成。

## 视觉源核查

- `reports/tables/visual_source_inventory.csv` 对本论文记录 `no_public_source_found`；`corpus/visual_sources/iclr-2026-a8e7c788acec/` 不存在。
- PDF 首页/正文未提供作者 GitHub 或代码 URL，仅在正文承诺将发布 pretrained weights/source code。OpenReview 入口为 `https://openreview.net/forum?id=LMsdys7t1L`，官方 PDF 为 proceedings URL。
- 只读 `gh search repos/code` 以完整标题与 DCFold 检索，命中 `zhaoyang97/Paper-Notes` 与 `Paper-Notes-en` 的第三方解读文件；`gh repo view` 元数据显示它们是多论文阅读集合，未发现作者仓库或绘图源。未将这些笔记及其任何图片视作本文源。故 JSON 状态为 `no_public_source_found`。

## 页级对象表

| 区域 | Figure | Table |
|---|---|---|
| 正文 | Figure 1 p.1；Figure 2 p.3；Figure 3 p.8；Figure 4 p.9；Figure 5 p.10 | Table 1 p.3；Table 2–3 p.6；Table 4 p.8；Table 5–6 p.9 |
| 附录 | Figure 6–7 p.14 | Table 7 p.17；Table 8–9 p.18 |

## 全局风格

- 计数：正文 5 Figure / 6 Table；附录 2 Figure / 3 Table。
- 图字体：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, DejaVuSans, TimesNewRomanPSMT, TimesNewRomanPS-BoldMT, NimbusMonL-Regu, AppleColorEmoji；约 5.0–14.0 pt，中位约 8.5 pt；来源 `mixed`。
- 表字体：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, NimbusRomNo9L-ReguItal, CMR10, CMR7, CMMI10, CMSY10, NimbusMonL-Regu；正文约 7.5 pt，表头约 8.5 pt；字体对象来源 `pdf_object`。
- 调色板：Charts use local categorical roles: blue/teal for AF3 versus DCFold, yellow/green/teal/gray for method bars, and teal/yellow for TGM versus ECM. Sequential viridis-like color is reserved for the Euler-error surface; molecular case studies use cyan/blue overlays or red binder/gray target roles. Tables are monochrome booktabs with bold/gray emphasis and occasional arrows.
- 矢量/栅格：PDF inspection and pdfimages show vector/text plot and table objects on pages 1, 3, 8–10, plus embedded raster/soft-mask structure images in Figure 2 and raster molecular images in Figures 6–7; the Euler surface includes a raster colorbar alongside vector content. Captions, surrounding prose, table text and rules are PDF text/vector objects.
- 一致性：Body, captions, equations and tables consistently use Nimbus Roman with Computer Modern math; plots add DejaVuSans and some Times New Roman labels, while molecular assets carry raster typography/labels. Caption labels are italic and table rules are stable, but figure color roles and legend placement are local rather than governed by a paper-wide key.

## Figure 逐项审计

### Figure 1（p.1；introduction；single_column）

- 类型：`line`, `bar`；目的：`headline`, `main_comparison`, `efficiency_cost`；复杂度 3/5；面板 2，系列 2，图例项 2，标注约 4，数据标记约 16。
- Caption：

`Figure 1: The acceleration ratio and generative quality of DCFold on Posebusters V2.`

- 词数：13；动作：title；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：DejaVuSans, NimbusRomNo9L-Regu, NimbusRomNo9L-Medi；6.0–11.0 pt（中位 8.0）；字重 regular, bold；字形 roman, italic；来源 `mixed`，置信度 `high`。
- Color：`categorical`，约 4 色（#6387BB, #57B1A9, #7E9AC8, #77C2BC）；蓝色折线/圆点为 AlphaFold3，青绿色折线/方点为 DCFold；同色虚线水平线标注各自平均 folding time；右侧柱高与柱顶数字编码 PoseBusters success rate。 冗余编码：有；灰度安全：是；来源 `rendered_estimate`。
- Plot grammar：渲染 `vector`；x/y `categorical`/`linear`；网格 `both`；图例 `有`（upper-left of folding-time panel; none in bar panel），共享图例 `False`；direct label `True`；marker 2；线型 2；hatch `False`；reference line 2；不确定性 `none`；线宽约 1.0 pt；来源 `rendered_estimate`。
- Encodings：
  - x：token-length bins (≤255 through ≥896) in the left panel; model categories in the right panel
  - y：folding time in seconds; success rate (%)
  - color：AF3 versus DCFold method identity
  - shape：circle for AF3 and square for DCFold
  - line：solid trajectories with dashed average guides
  - facet：folding time across sequence length versus success-rate bars
  - text：average labels, 59% diffusion/38% Pairformer annotations, and bar-top 82.9/78.6 values
- 数据与统计：The left panel has seven token bins and two point trajectories, with dashed average guides labelled AF3 avg 133.3s and DCFold avg 8.9s; annotations apportion AF3 time to Diffusion (59%) and Pairformer (38%). The right panel reports one success proportion per method (82.9 and 78.6). These are averages/proportions without run variance, token-bin counts, tail latency, or a confidence interval.
- 证据关系：Introduction identifies AlphaFold3’s iterative diffusion/Pairformer cost → Figure 1 quantifies speed/quality trade-off → Dual Consistency in Figure 2 and TGM in Figure 4/5 address the two bottlenecks → Appendix Table 7 gives the bin-wise runtime detail.
- 设计优点：
  - Combines efficiency and quality in a compact two-panel headline object.
  - Token-bin trajectories expose length dependence instead of reporting only one global speed ratio.
  - Average guides, bracket annotations, markers, and color provide redundant method identification.
- 设计缺陷：
  - Caption does not define the token bins, averaging unit, or whether success uses best/worst pose.
  - The 15× claim is visually inferable but no ratio annotation or uncertainty is given.
  - Small rotated bin labels and dual metric scales limit exact reading at column width.
- 可复用范式：Use a paired cost-versus-quality composition: a length-stratified line panel with average guides next to a simple outcome bar panel, while naming all aggregation units in the caption.

### Figure 2（p.3；method；double_column）

- 类型：`pipeline`, `architecture`, `conceptual_diagram`；目的：`method_interface`, `theory_mechanism`；复杂度 4/5；面板 2，系列 不适用，图例项 0，标注约 23，数据标记约 28。
- Caption：

`Figure 2: Overview of Dual Consistency framework (top: AlphaFold3; bottom: DCFold).`

- 词数：11；动作：title, setup；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：TimesNewRomanPSMT, TimesNewRomanPS-BoldMT, NimbusRomNo9L-Regu, AppleColorEmoji；5.5–14.0 pt（中位 8.0）；字重 regular, bold；字形 roman, italic；来源 `mixed`，置信度 `high`。
- Color：`categorical`，约 7 色（#A8D995, #F7C2A6, #FFF2CC, #E9F5DC, #B6D9C7, #7A8F94, #8AB8E8）；绿色 MSA/Input Feature、桃色 Embedder/Pairformer/Diffusion 模块、淡黄色 Pairformer 区、淡绿色 Diffusion 区、蓝色下游任务框；蓝色箭头表达数据流，虚线弧线表达 consistency 约束，问号/勾表示上/下配置的下游可用性。 冗余编码：有；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `mixed`；x/y `none`/`none`；网格 `none`；图例 `无`（无），共享图例 `False`；direct label `True`；marker 0；线型 2；hatch `False`；reference line 0；不确定性 `none`；线宽约 1.0 pt；来源 `rendered_estimate`。
- Encodings：
  - x：none; left-to-right module/data-flow order
  - y：none; AlphaFold3 top and DCFold bottom
  - color：architecture modules, consistency regions, input/output and downstream roles
  - shape：rounded blocks, triangular diffusion blocks, arrows, question/check symbols and downstream braces
  - line：solid forward arrows and dotted consistency arrows
  - facet：top full AlphaFold3 versus bottom DCFold one-Pairformer/one-Diffusion configuration
  - text：MSA, Input Feature, Embedder, Pairformer 1/2/N, Diffusion 1/2, consistency labels, and binder/assembly/extraction outputs
- 数据与统计：A non-quantitative architecture comparison: the top row contains repeated Pairformer and Diffusion blocks, while the bottom row keeps one of each and labels Pairformer Consistency and Diffusion Consistency. Both rows feed the same binder hallucination, complex assembly, and feature-extraction downstream interface. The diagram encodes no sample, metric, denominator, or uncertainty.
- 证据关系：AlphaFold3 dual iterative bottleneck in §3.2 → Figure 2 maps each loop to its own consistency target → Table 1 specifies the two-stage loss contract → Figure 3 and Tables 2–3 test one-step accuracy and downstream utility.
- 设计优点：
  - Matched top/bottom flow makes the removed iteration visible without requiring a separate legend.
  - Dashed arrows directly link each bottleneck to its consistency loss.
  - The same downstream boxes communicate that efficiency changes are intended to preserve application interfaces.
- 设计缺陷：
  - Caption does not define “Dual Consistency”, one-step semantics, or the question/check symbols.
  - Dense small labels and formula-like arrows are difficult to read after rasterization.
  - Color is essential for separating regions and is not robust under grayscale printing.
- 可复用范式：Show an iterative baseline and compressed proposal on aligned rows, then draw one explicit intervention arrow from each removed loop to its corresponding loss or control.

### Figure 3（p.8；results；single_column）

- 类型：`bar`；目的：`headline`, `main_comparison`, `ablation`, `efficiency_cost`；复杂度 4/5；面板 4，系列 5，图例项 5，标注约 20，数据标记约 20。
- Caption：

`Figure 3: lDDT performance on the Recent PDB dataset.`

- 词数：9；动作：title；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：DejaVuSans, NimbusRomNo9L-Regu, NimbusRomNo9L-Medi；5.0–10.0 pt（中位 8.0）；字重 regular, bold；字形 roman；来源 `mixed`，置信度 `high`。
- Color：`categorical`，约 5 色（#F2D99E, #A8CB97, #57B1A9, #B8B8B8, #707070）；五种方法分别用浅黄 AF3 ODE、浅绿 AF3 TGM、青绿 DCFold (Ours)、浅灰 Protenix-mini、深灰 AF3；同一方法颜色贯穿 Pairformer Cycles、Diffusion NFE、Complex lDDT 和 Prot-Prot lDDT 四个面板。 冗余编码：有；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `vector`；x/y `categorical`/`linear`；网格 `none`；图例 `有`（shared legend centered beneath the four panels），共享图例 `True`；direct label `True`；marker 0；线型 0；hatch `False`；reference line 0；不确定性 `none`；线宽约 0.5 pt；来源 `rendered_estimate`。
- Encodings：
  - x：method categories within each metric panel
  - y：Pairformer cycles, Diffusion NFE, Complex lDDT, or Prot-Prot lDDT
  - color：method identity shared across all four panels
  - shape：rectangular bars
  - line：无
  - facet：two efficiency counts followed by two lDDT outcomes
  - text：bar-top numeric values and one shared five-method legend
- 数据与统计：Four categorical bar panels show the staged comparison AF3 ODE, AF3 TGM, DCFold, Protenix-mini, and AF3. Pairformer cycles are 1/1/1/2/200; Diffusion NFE is 1/1/1/2/visible full-AF3 high count; Complex lDDT values are 0.455/0.489/0.507/0.490/0.501 and Prot-Prot lDDT values are 0.623/0.637/0.646/0.622/0.650. All are displayed point values without sample sizes, uncertainty, or significance tests.
- 证据关系：§3.2 Dual Consistency and TGM → Figure 3 aligns compute counts with lDDT to show one-step efficiency and quality → Table 3 supplies category-level TM-score/SR → Table 6 isolates generic consistency schedules.
- 设计优点：
  - Shared method colors make the four metrics comparable at a glance.
  - Bar-top numbers preserve exact displayed values despite small panels.
  - Placing cycle/NFE diagnostics beside lDDT makes the efficiency–quality trade-off explicit.
- 设计缺陷：
  - The caption names only lDDT and does not explain the NFE/cycle panels or method abbreviations.
  - Different y units share a visual template, which can invite false magnitude comparison.
  - No error bars or sample counts make tiny lDDT differences look more decisive than documented.
- 可复用范式：Use a shared categorical palette across compute and quality facets, and print values on each bar when panels are too small for reliable axis reading.

### Figure 4（p.9；ablation；single_column）

- 类型：`other`；目的：`theory_mechanism`, `ablation`, `robustness`；复杂度 3/5；面板 1，系列 不适用，图例项 1，标注约 3，数据标记约 900。
- Caption：

`Figure 4: The relative error of the Euler solver for r(t, u).`

- 词数：12；动作：title；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：DejaVuSans, NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMSY10；5.0–10.0 pt（中位 8.0）；字重 regular, bold；字形 roman, italic；来源 `mixed`，置信度 `high`。
- Color：`sequential`，约 6 色（#440154, #482878, #31688E, #35B779, #90D743, #FDE725）；viridis-like 连续色阶编码 Euler reference-time 映射的 relative error；右侧 colorbar 从接近 0 到约 0.1，颜色是误差值而非方法类别。 冗余编码：无；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `mixed`；x/y `linear`/`linear`；网格 `both`；图例 `有`（colorbar at right of 3-D surface），共享图例 `False`；direct label `False`；marker 0；线型 0；hatch `False`；reference line 0；不确定性 `none`；线宽约 未估计 pt；来源 `rendered_estimate`。
- Encodings：
  - x：u in [0,1] on the temporal schedule
  - y：t in [0,1] on the diffusion trajectory
  - color：relative error magnitude via continuous colorbar
  - shape：3-D surface over the t×u grid
  - line：无
  - facet：无
  - text：t/u axis labels, relative-error z label and colorbar ticks
- 数据与统计：A deterministic surface evaluates the relative error of the one-step Euler approximation r(t,u) over a two-dimensional t×u grid. Height and color encode error; the rendered surface peaks near an early/large-step corner and is low across most of the remaining domain. No replicate, sampling uncertainty, or formal error tolerance is shown.
- 证据关系：TGM geodesic schedule and Euler approximation in §3.3 → Figure 4 tests the numerical approximation invoked by Algorithm 1 → Figure 5 diagnoses training dynamics → Appendix A derives the Gaussian/EDM Fisher-information form.
- 设计优点：
  - A surface exposes interaction between diffusion time and training-progress coordinate better than a single average.
  - The colorbar supplies a continuous scale while the perspective conveys the error ridge.
  - Placed beside the TGM ablation text, it gives a concrete numerical check on the proposed scheduler.
- 设计缺陷：
  - Caption omits axis meanings, color scale, and the early-stage error pattern discussed in the prose.
  - 3-D perspective can obscure exact values and is not grayscale-safe.
  - The figure does not state the threshold at which the approximation would be considered acceptable.
- 可复用范式：Use a compact t×u surface plus a labeled colorbar to audit a numerical approximation, but state the acceptable error criterion and grid construction in the caption.

### Figure 5（p.10；ablation；single_column）

- 类型：`line`, `area`；目的：`mechanism`, `ablation`, `robustness`；复杂度 3/5；面板 2，系列 2，图例项 2，标注约 2，数据标记约 900。
- Caption：

`Figure 5: Gradient norm and loss curve during training for ECM and TGM.`

- 词数：13；动作：title；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：DejaVuSans, NimbusRomNo9L-Regu；5.0–10.0 pt（中位 8.0）；字重 regular, bold；字形 roman, italic；来源 `mixed`，置信度 `high`。
- Color：`mixed`，约 4 色（#57B1A9, #F2D086, #B9DED9, #F8E8C5）；青绿色 TGM、黄橙色 ECM；同色浅透明带表示曲线周围的训练波动/重复轨迹范围；竖向灰色虚线分隔约 3k 与 6k step 的阶段边界。 冗余编码：有；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `vector`；x/y `linear`/`linear`；网格 `both`；图例 `有`（upper-right in each panel），共享图例 `False`；direct label `False`；marker 0；线型 2；hatch `False`；reference line 2；不确定性 `band`；线宽约 1.2 pt；来源 `rendered_estimate`。
- Encodings：
  - x：training step ×10^3 (0–9)
  - y：gradient norm (left) or loss (right)
  - color：ECM versus TGM and their associated variability bands
  - shape：无
  - line：solid method curves; dashed vertical stage markers
  - facet：gradient norm and loss
  - text：axis labels, two method legends, and stage separators
- 数据与统计：Two training diagnostics run from 0 to 9×10^3 steps. ECM has wide gradient bands and staircase-like loss phases around the two vertical stage boundaries; TGM stays lower/more balanced in gradient norm and smoother near loss 0.9–1.0. The shaded range is visible but its construction, number of runs, and aggregation are not defined.
- 证据关系：Table 6 chooses ECM as the runnable generic consistency comparator → Figure 5 explains the claimed TGM stability mechanism through gradients/loss → Figure 4 checks Euler error → TGM variable-length rationale in §3.3.
- 设计优点：
  - Same x-axis and method key permit a direct gradient-versus-loss comparison.
  - Bands reveal instability that a mean line alone would hide.
  - Stage separators make the staircase behavior interpretable as training-phase changes.
- 设计缺陷：
  - Caption does not identify the bands, stage boundaries, or why ECM is the comparator.
  - Curve smoothness is a visual diagnostic rather than a convergence or causal test.
  - Pale bands and small legends reduce contrast, particularly in grayscale.
- 可复用范式：Pair outcome-independent optimization diagnostics in aligned panels and show variability bands plus phase separators, while defining the band estimator and run count.

### Figure 6（p.14；appendix；double_column）

- 类型：`image_montage`, `qualitative_grid`；目的：`qualitative_evidence`, `main_comparison`, `robustness`；复杂度 3/5；面板 3，系列 3，图例项 3，标注约 9，数据标记约 3。
- Caption：

`Figure 6: A structure prediction case study of DCFold, compared against AlphaFold3 and the experimental result.`

- 词数：16；动作：title, setup, comparison；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, DejaVuSans, TimesNewRomanPSMT；6.0–12.0 pt（中位 8.5）；字重 regular, bold；字形 roman；来源 `rendered_estimate`，置信度 `high`。
- Color：`categorical`，约 4 色（#FFFFFF, #00D8D8, #4A82B5, #24358A）；白/灰色 Experimental result、青色 AlphaFold 3、蓝色 DCFold；PDB ID 与复合物名称为蓝色直接标签，底部色块图例定义叠加结构的身份。 冗余编码：有；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `mixed`；x/y `none`/`none`；网格 `none`；图例 `有`（bottom-center below the three structures），共享图例 `True`；direct label `True`；marker 0；线型 0；hatch `False`；reference line 0；不确定性 `none`；线宽约 未估计 pt；来源 `rendered_estimate`。
- Encodings：
  - x：none; three PDB case columns
  - y：none; 3-D structure projection
  - color：experimental versus AlphaFold3 versus DCFold overlay identity
  - shape：ribbon/cartoon molecular structures
  - line：overlaid backbone traces
  - facet：PDB 7r6r, 7wux and 7pzb
  - text：PDB IDs, target descriptions, and three-item color legend
- 数据与统计：Three representative PDB cases (7r6r, 7wux, 7pzb) overlay experimental, AlphaFold3, and DCFold structures. The object provides qualitative spatial agreement only; it reports no per-case RMSD, case-selection rule, confidence score, or population denominator.
- 证据关系：Main structure-prediction Tables 2–3 quantify RMSD/TM-score/SR → Figure 6 supplies visual examples after the quantitative claims → Appendix Table 9 identifies binder targets separately; the main text does not visibly call this case-study figure.
- 设计优点：
  - Overlay colors let a reader see structural agreement without switching panels.
  - PDB IDs and descriptions make the examples traceable to concrete complexes.
  - A shared legend avoids repeating method labels under each structure.
- 设计缺陷：
  - Representative examples can hide failures and have no selection rule.
  - Ribbons and overlays are hard to compare exactly without an RMSD or aligned-view annotation.
  - Color/line overlap is not grayscale-safe and the small legend lacks confidence encoding.
- 可复用范式：Use aligned experimental/baseline/proposed structure overlays with PDB identifiers and a shared legend as qualitative support after quantitative structural metrics.

### Figure 7（p.14；appendix；double_column）

- 类型：`image_montage`, `qualitative_grid`；目的：`qualitative_evidence`, `dataset`；复杂度 4/5；面板 4，系列 2，图例项 0，标注约 12，数据标记约 8。
- Caption：

`Figure 7: Examples from binder-design experiments, with targets: (A) ALK, (B) H3, (C) IL2Rα, and (D) VirB8.`

- 词数：17；动作：title, setup；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, Arial-BoldMT, CMMI10；6.0–12.0 pt（中位 8.5）；字重 regular, bold；字形 roman, italic；来源 `rendered_estimate`，置信度 `high`。
- Color：`categorical`，约 3 色（#EEEEEE, #9B1C1F, #333333）；浅灰/白色半透明 target surface、深红 binder ribbon、黑色/深灰框线与箭头；每个 panel 用圆圈和放大 inset 标出界面区域。 冗余编码：有；灰度安全：否；来源 `rendered_estimate`。
- Plot grammar：渲染 `mixed`；x/y `none`/`none`；网格 `none`；图例 `无`（无），共享图例 `False`；direct label `True`；marker 0；线型 1；hatch `False`；reference line 0；不确定性 `none`；线宽约 未估计 pt；来源 `rendered_estimate`。
- Encodings：
  - x：none; four target panels
  - y：none; 3-D complex projection
  - color：target versus generated binder identity and interface highlight
  - shape：molecular surface, ribbons, circle, rectangular zoom inset and arrow
  - line：black leader arrows from interface circle to inset
  - facet：A ALK, B H3, C IL2Rα, D VirB8
  - text：panel letters and target names in caption
- 数据与统计：Four qualitative binder–target complex examples are shown with a surface/ribbon view and an interface zoom for each target. No per-target success rate, structural score, selection rule, sample count, or failure example is encoded; the examples are visual companions to Table 5 rather than population evidence.
- 证据关系：Binder task and six-target quantitative Table 5 → Figure 7 gives four representative interfaces → Appendix Tables 8–9 expose generated counts and target metadata; §4.3 and Appendix C.2 define the filtering pipeline.
- 设计优点：
  - Repeated circle-to-inset geometry directs attention to the binding interface.
  - Four target panels provide a compact cross-target qualitative check.
  - The red/gray structural roles remain visually consistent across panels.
- 设计缺陷：
  - Caption does not state that the complexes are generated/filtered or identify the structural rendering source.
  - No quantitative interface metric or negative case accompanies the attractive examples.
  - Red/gray overlays and thin arrows lose meaning in grayscale or small print.
- 可复用范式：Use a repeated target-plus-interface-inset layout for qualitative binder evidence, paired with a quantitative table and explicit case-selection rule.

## Table 逐项审计

### Table 1（p.3；method；single_column）

- 目的：`method_interface`, `experimental_design`, `reproduction`；正文/附录：`main`；行 2，列 5，表头层级 1，行分组 0，小数精度约 混合/不适用；规则 `booktabs`；高亮：`none`。
- Caption：

`Table 1: Training stages and the weights of each term.`

- 词数：10；动作：title, setup；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, NimbusRomNo9L-ReguItal, CMR10, CMMI10；正文约 8.0 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：No statistical uncertainty; this is a loss/configuration contract.
- 数据与表头：Columns are Stage, Module, L_confidence, L_diffusion, and L_pairformer. Stage (i) updates Diffusion with weights 10^-4, 1, ×; Stage (ii) updates Pairformer with 10^-4, ×, 1. The × entries denote an inactive loss in that stage.
- 证据关系：Dual Consistency method → Table 1 makes the two-stage update boundary explicit → Figure 2 maps the modules → benchmark tables/figures evaluate the resulting one-step model.
- 设计优点:
  - Compactly records which module is trained in each stage and which loss is active.
  - Inactive terms are visibly separated from numeric weights.
  - The table is adjacent to the method prose that interprets it.
- 设计缺陷：
  - Caption does not define the loss symbols or explain ×.
  - No optimizer, number of epochs, or schedule parameter is included; those details are deferred to appendix text.
  - Tiny math glyphs require the surrounding paragraphs to disambiguate modules.
- 可复用范式：Put staged update ownership and loss weights in a small matrix, with inactive terms marked explicitly rather than omitted.

### Table 2（p.6；results；double_column）

- 目的：`headline`, `main_comparison`, `robustness`；正文/附录：`main`；行 3，列 9，表头层级 2，行分组 0，小数精度约 2；规则 `booktabs`；高亮：`bold`, `cell_color`。
- Caption：

`Table 2: Posebusters V2 RMSD benchmark results. We report the percentage of predictions with RMSD below different thresholds.`

- 词数：18；动作：title, setup, encoding_key；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, NimbusRomNo9L-ReguItal, CMMI7；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Point percentages of predictions below 1/2/3/5 Å for best and worst pose RMSD; no sample count, error bars, or uncertainty interval is provided.
- 数据与表头：Method rows are AlphaFold3, AF3 ODE, and DCFold (Ours). Two four-column header groups, Best (%) and Worst (%), contain RMSD thresholds <1, <2, <3, <5. DCFold best values are 58.10/78.57/86.67/94.29 and worst values 46.67/71.43/80.00/90.48.
- 证据关系：Structure-prediction benchmark → Table 2 separates best-case and worst-case ligand RMSD tails → Table 3 tests Recent PDB categories → Figure 3 supplies lDDT/NFE context.
- 设计优点:
  - Best/worst grouping exposes tail behavior instead of a single average RMSD.
  - Threshold units and percentage direction are explicit in the caption/header.
  - Bold/gray DCFold row and bold best cells guide scanning while retaining all baselines.
- 设计缺陷：
  - The denominator and number of complexes are absent.
  - Best and worst pose definitions are left to §4.1, so the caption is not fully standalone.
  - The visual emphasis can obscure that DCFold is below AlphaFold3 at the strict best-case thresholds.
- 可复用范式：Report a thresholded error distribution with separate best/worst blocks when downstream reliability depends on tails, and define the pose selection and denominator in the caption.

### Table 3（p.6；results；double_column）

- 目的：`headline`, `main_comparison`, `robustness`；正文/附录：`main`；行 3，列 7，表头层级 2，行分组 0，小数精度约 3；规则 `booktabs`；高亮：`bold`, `cell_color`。
- Caption：

`Table 3: TM-score and Success Rate (SR) on different protein categories in the Homology Recent PDB dataset. Values in parentheses denote the absolute improvement relative to AF3 ODE.`

- 词数：28；动作：title, setup, encoding_key, comparison；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, NimbusRomNo9L-ReguItal, CMR10, CMMI10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Point category aggregates; parenthetical entries are absolute improvements, not uncertainty. Category sample sizes and dispersion are not stated.
- 数据与表头：Rows AF3 ODE, AlphaFold3, DCFold (Ours); grouped columns PL-complex, Monomer, PP-complex, each with TM-score and SR (%). DCFold values are 0.824/94.9, 0.850/95.7, and 0.800/92.2 with gains +1.2/+2.6pp, +2.3/+2.9pp, +4.8/+5.2pp relative to AF3 ODE.
- 证据关系：Recent PDB setup → Table 3 reports category-level fold quality and success → Figure 3 adds lDDT and compute counts → Figure 6 gives selected visual overlays.
- 设计优点:
  - Three protein categories are compared under the same two outcome metrics.
  - The parenthetical gain convention is defined directly in the caption.
  - The wide grouped header makes category-specific trade-offs visible.
- 设计缺陷：
  - The caption does not define SR’s RMSD threshold or category denominators.
  - TM-score and SR use different units but occupy repeated cells, requiring careful header reading.
  - Bold/gray emphasis and aggregate pooling do not expose target-level heterogeneity.
- 可复用范式：Use a grouped category header with paired structural metrics and explicit absolute-gain annotations, while reporting category counts alongside the values.

### Table 4（p.8；results；single_column）

- 目的：`robustness`, `main_comparison`；正文/附录：`main`；行 6，列 3，表头层级 1，行分组 2，小数精度约 4；规则 `booktabs`；高亮：`none`。
- Caption：

`Table 4: Diversity and confidence metrics on the Posebusters V2 benchmark.`

- 词数：11；动作：title, setup；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, SFRB1000, CMMI10, CMSY10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Rows report mean ± values for diversity and confidence; the paper does not define whether ± is SD/SE or give a formal test.
- 数据与表头：Rows compare AF3 and DCFold under 5 samples, 15 samples, and 5 seeds × 1 sample. Columns are Diversity (↓) and Confidence (↑). DCFold values range 0.9701–0.9712 ± 0.0565–0.0570 and 94.13–94.15 ± 2.96–2.97.
- 证据关系：§4.2 asks whether one-step distillation preserves diversity/confidence → Table 4 compares matched sampling regimes → prose reports no meaningful diversity gain from more samples/seeds → Figure 6/7 provide qualitative cases.
- 设计优点:
  - Places two quality dimensions beside the sampling design rather than using separate tables.
  - Separates fixed-seed and multi-seed sampling explicitly.
  - Down/up arrows signal preferred direction.
- 设计缺陷：
  - The caption omits definitions of diversity, confidence, and the ± statistic.
  - No sample count per benchmark or confidence interval lets small differences look interpretable.
  - The grouped row separator is subtle at small size.
- 可复用范式：Cross sampling protocols in rows and place quality dimensions in columns, with direction arrows and an explicit dispersion definition.

### Table 5（p.9；results；inset）

- 目的：`headline`, `main_comparison`, `efficiency_cost`；正文/附录：`main`；行 2，列 8，表头层级 1，行分组 0，小数精度约 2；规则 `booktabs`；高亮：`bold`。
- Caption：

`Table 5: In silico success rates across six targets for binder design (values shown as physics-based constraints / model-based constraints).`

- 词数：20；动作：title, setup, encoding_key；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMMI10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Per-target filtered success proportions, shown as physics-based/model-based constraint rates; six-target Average is also a point proportion. No run-level uncertainty, target counts, or wet-lab validation is reported.
- 数据与表头：Columns are IL-2Rα, TrkA, H3, VirB8, ALK, LTK, and Average, with BindCraft and DCFold rows. Averages are .26/.69 for BindCraft and .29/.78 for DCFold; target behavior is heterogeneous (e.g. DCFold physics .37 for IL-2Rα and .12 for ALK versus BindCraft .38 and .14).
- 证据关系：§3.4 downstream-task motivation → §4.3 binder hallucination → Table 5 compares AF2-based BindCraft to DCFold → Figure 7 examples and Appendix Tables 8–9 expose samples/target metadata.
- 设计优点:
  - Puts two constraint families and six targets on one compact decision surface.
  - Average plus per-target cells prevents the majority-target claim from being completely opaque.
  - Fraction slash convention is stated in the caption.
- 设计缺陷：
  - The average weights targets without reporting target sample counts or aggregation rule.
  - “Success rate” is filtered in silico and not a wet-lab outcome, which is not visible from the short caption.
  - Inset width forces very small target headers and values.
- 可复用范式：Report downstream success by target and by constraint family, retaining the average only as a summary and exposing heterogeneous targets.

### Table 6（p.9；ablation；inset）

- 目的：`ablation`, `failure`, `efficiency_cost`；正文/附录：`main`；行 4，列 3，表头层级 1，行分组 0，小数精度约 1；规则 `booktabs`；高亮：`bold`, `arrows`, `cell_color`。
- Caption：

`Table 6: Success Rates of Different Consistency Models on Posebusters V2.`

- 词数：11；动作：title, setup；粗体结论标题：否；脱离正文可理解：否；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMSY10, CMR10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：One time-per-step and one success percentage per method; sCM has “-” because long sequences cause OOM, and no variability or denominator is shown.
- 数据与表头：Rows CD, sCM, ECM, TGM; columns Method, Time (s/step), Success rate (%). CD is 18.5/25.6↓, sCM 38.1/–, ECM 11.6/75.7↑, TGM 11.6/77.5↑. Arrows mark degradation/improvement relative to a reference not explained in the table.
- 证据关系：§4.4 compares generic consistency baselines → Table 6 records runnable time/success and the sCM OOM failure → ECM is selected as prior representative → Figure 5 contrasts ECM/TGM training dynamics.
- 设计优点:
  - Preserves the negative sCM result instead of imputing a success value.
  - Time and quality are adjacent, matching the practical utility claim.
  - Arrows and gray/bold TGM/ECM rows highlight the intended comparison.
- 设计缺陷：
  - The arrow baseline and “success rate” reference are not defined in the caption.
  - Missing sCM performance means the schedule comparison is incomplete.
  - A single value per method cannot distinguish stable training from one favorable run.
- 可复用范式：Keep failed/unsupported baselines explicit in a compact speed–quality ablation, and explain arrow directions and missingness in the caption.

### Table 7（p.17；appendix；single_column）

- 目的：`efficiency_cost`, `robustness`, `reproduction`；正文/附录：`appendix`；行 7，列 3，表头层级 1，行分组 0，小数精度约 2；规则 `booktabs`；高亮：`none`。
- Caption：

`Table 7: Average inference time of AlphaFold3 and DCFold across token bins.`

- 词数：12；动作：title, setup, encoding_key；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMR10, CMMI10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Average seconds per token-length bin; no bin sample count, dispersion, or hardware variability is reported.
- 数据与表头：Rows are ≤255, 256–383, 384–511, 512–639, 640–767, 768–895, and ≥896 tokens; columns are #Tokens, AlphaFold3 Avg Time (s), DCFold Avg Time (s). AF3 rises 92.63→212.12 s while DCFold rises 3.76→27.40 s.
- 证据关系：Figure 1 global speed/quality overview → Appendix C.1 bins runtime by input length → Table 7 supports the 24× short-sequence and >7.7× moderate/long acceleration explanation → Figure 5 addresses training rather than inference.
- 设计优点:
  - Explicit bins expose how the speedup changes with sequence length.
  - Units are stated in the header and every row is directly comparable.
  - Appendix placement keeps cost detail available for reproduction.
- 设计缺陷：
  - No number of sequences per bin or uncertainty makes averages hard to audit.
  - The table does not include the derived speedup column, so readers must calculate ratios.
  - Token count is a proxy for complex input size, not a complete runtime decomposition.
- 可复用范式：Use fixed-width token bins with paired runtime columns to make scaling and bottleneck shifts visible; add counts and derived ratios when claiming robustness.

### Table 8（p.18；appendix；double_column）

- 目的：`reproduction`, `dataset`, `robustness`；正文/附录：`appendix`；行 2，列 7，表头层级 1，行分组 0，小数精度约 0；规则 `booktabs`；高亮：`none`。
- Caption：

`Table 8: The total number of generated samples in the binder hallucination experiments.`

- 词数：13；动作：title, setup；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMMI10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Counts only; no uncertainty applies. Counts differ by target and method.
- 数据与表头：Columns are IL-2Rα, TrkA, H3, VirB8, ALK, and LTK; rows BindCraft and DCFold (Ours). Counts are 312/243/269/347/188/348 for BindCraft and 375/256/295/439/177/402 for DCFold.
- 证据关系：Appendix C.2 runtime comparison → Table 8 makes generated-sample exposure visible for the six-target binder averages in Table 5 → Table 9 identifies the targets.
- 设计优点:
  - Provides the denominator context that Table 5’s short caption lacks.
  - Target columns make unequal exposure easy to spot.
  - Minimal rules keep a small count table legible.
- 设计缺陷：
  - No target-wise success numerator is supplied, so counts cannot reconstruct Table 5 rates.
  - The caption does not state the 48-hour/one-H800 collection protocol.
  - Wide float with a narrow body leaves substantial white space.
- 可复用范式：Publish per-target generation counts beside downstream rates so target imbalance is visible before interpreting an average.

### Table 9（p.18；appendix；double_column）

- 目的：`dataset`, `experimental_design`, `reproduction`；正文/附录：`appendix`；行 6，列 4，表头层级 1，行分组 0，小数精度约 混合/不适用；规则 `booktabs`；高亮：`none`。
- Caption：

`Table 9: Detailed information of binder targets in the binder hallucination experiments.`

- 词数：12；动作：title, setup；粗体结论标题：否；脱离正文可理解：是；直接主发现：否。
- Typography：NimbusRomNo9L-Regu, NimbusRomNo9L-Medi, CMMI10；正文约 7.5 pt，表头约 8.5 pt；表头字重 `mixed`；来源 `pdf_object`，置信度 `high`。
- 不确定性：Descriptive metadata only; no statistical uncertainty.
- 数据与表头：Columns Target, PDB ID, Family, Description list ALK/7NWZ, H3/3ZTJ, IL2Rα/1Z92, LTK/7NX0, TrkA/2IFG, and VirB8/4O3V. Family and descriptions provide biological context for the six targets used in binder hallucination.
- 证据关系：Binder protocol in §4.3 and Appendix B.2 → Table 9 defines target identity → Table 8 reports generation exposure → Table 5 reports filtered success by target; Figure 7 qualitatively depicts four of the six.
- 设计优点:
  - PDB IDs make target identities externally traceable.
  - Description column gives enough biological context to interpret target heterogeneity.
  - Stable four-column header is easy to reuse for other binder panels.
- 设计缺陷：
  - Descriptions do not state why these six targets were selected or how representative they are.
  - Family labels appear biologically inconsistent for some entries and are not checked against a canonical source in the figure audit.
  - The long description column creates uneven row heights and dense small text.
- 可复用范式：Include target identifiers, provenance IDs, biological family, and a concise description when a downstream benchmark aggregates heterogeneous structures.

## 跨对象系统判断

- **视觉叙事**：Figure 1 motivates the speed/quality bottleneck; Figure 2 maps AlphaFold3’s two iterative loops to Dual Consistency; Table 1 fixes the two-stage loss contract; Figure 3 joins NFE/cycles to lDDT; Tables 2–5 report structure and binder outcomes; Table 6 and Figures 4–5 diagnose TGM’s schedule and training dynamics. Appendix Figures 6–7 and Tables 7–9 extend the story with qualitative cases, token-binned runtime, sample exposure and target metadata.
- **Caption 系统**：Captions use a colon after the Figure/Table label and concise sentence-style titles. Figure 1 and Tables 2–3 include some setup/encoding detail, whereas Figures 2–5 and 7 mostly name the object without its key interpretation. None of the captions defines uncertainty; Table 4 displays ± without identifying SD/SE, and Figures 5’s bands lack a construction.
- **表头系统**：Tables rely on booktabs top/mid/bottom rules, bold headers, grouped multi-level headers for threshold/category comparisons, and sparse gray/bold emphasis. Table 1 is a compact loss matrix; Tables 2–3 use nested metric groups; Table 4 groups sampling regimes; Tables 5–9 use compact target, runtime, count or metadata columns. Units and denominators are unevenly visible.
- **方法—结果—消融链**：Figure 2 and Table 1 connect the architecture to the two training objectives; Figure 3 and Tables 2–3 evaluate one-step structural quality; Table 4 checks diversity/confidence; Table 5 tests binder utility; Table 6 plus Figures 4–5 isolate TGM versus generic schedules and numerical/training mechanisms.
- **正文—附录链**：The main Figure 1 speed overview is expanded by Appendix Table 7’s token bins; Table 5 binder averages are contextualized by Appendix Tables 8–9 and Figure 7; Figure 6 supplies structure examples; Appendix B/C supplies the filtering, hardware, runtime and sample-count details needed to interpret main claims.
- **字体一致性**：PDF object fonts are stable for captions/tables (Nimbus Roman and Computer Modern), with italic caption labels and bold headers. Figures mix vector DejaVuSans/Times-like labels with raster molecular assets and occasional emoji/icons, so small-label readability is less consistent than the paper-level typography.
- **颜色一致性**：Blue/teal method roles recur in Figures 1 and 5; yellow/green/teal/gray method colors recur in Figure 3; red/gray binder roles recur in Figure 7. However, Figure 2 uses architecture-region colors and Figure 4 uses a sequential error map, with no global legend tying colors to a single method or meaning.

## 最终判断

### 最可复用模式
- Two-bottleneck interface: align baseline/proposed iterative diagrams and draw one consistency intervention to each loop.
- Cost-quality composite: show length-stratified runtime beside an outcome comparison instead of hiding speed in one average.
- Mechanism chain: pair a compute/quality ablation with a numerical-error surface and training-dynamics curves.
- Downstream audit: pair per-target success rates with generated-sample counts, target metadata and representative interface insets.

### 最高价值对象
- Figure 2, because it gives the clearest visual mapping from AlphaFold3’s two loops to Dual Consistency.
- Figure 3, because compute counts and lDDT are aligned across the same method palette.
- Table 2, because best/worst RMSD thresholds expose reliability tails rather than only a mean.
- Figure 1 plus Appendix Table 7, because global and length-binned runtime evidence are connected.

### 失败模式
- Captions and tables omit sample denominators, run counts and uncertainty definitions; Figure 5 bands are especially under-specified.
- Table 2 strict best-case rates are below AlphaFold3 while prose foregrounds worst-case gains; the trade-off is easy to miss.
- Table 6 has an unavailable sCM result due to OOM, limiting the completeness of generic schedule comparison.
- Binder success averages aggregate heterogeneous targets with unequal sample counts and no wet-lab validation.
- Small raster molecular/plot labels and color-dependent encodings reduce grayscale and small-print auditability.

**一句话视觉策略**：The paper visualizes DCFold as a compression of AlphaFold3’s iterative cost: first show the cost/quality gap, then map each removed loop to a consistency objective, validate one-step structure and binder outcomes, and use ablation, runtime bins, diagnostics and qualitative cases to support the TGM mechanism.

## 审计证据路径

- PDF：`corpus/pdfs/iclr-2026-a8e7c788acec.pdf`；文本：`corpus/text/iclr-2026-a8e7c788acec.txt`。
- 200 dpi 页面：`/tmp/iclr-a8e7c788acec/render200/page-01.png`–`page-18.png`；图像对象：`/tmp/iclr-a8e7c788acec/work/pdfimages.txt`；字体对象：`/tmp/iclr-a8e7c788acec/work/pdffonts.txt`。
- GitHub 只读检索结果与候选拒绝依据记录于 JSON `source_acquisition.search_note`；未注册任何第三方笔记图像为视觉源。

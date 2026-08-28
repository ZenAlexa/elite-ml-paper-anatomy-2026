# Visual audit — iclr-2026-ff40de6c7ac1

## 审计范围与事实源

- **论文**：$p\textrm{-less}$ Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding；PDF 事实源：corpus/pdfs/iclr-2026-ff40de6c7ac1.pdf。
- **完整覆盖**：PDF 共 44 个物理页；已将全部页面以 **200 dpi（1700×2200 px）** 渲染到 /tmp/iclr_ff40_render200/page-01.png–page-44.png，并检查正文、References、Appendix A–C 的页面与对象。
- **对象清单**：19 个 Figure、15 个 Table、0 个 Algorithm。正文对象为 Figures 1–4 / Tables 1–4；附录对象为 Figures 5–19 / Tables 5–15。页码按 PDF 物理页。
- **页级地图**：Figure 1 p.2；Tables 1/Figure 2 p.7；Tables 2–3 p.8；Table 4/Figure 3 p.9；Figure 4 p.10；Figures 5–8 pp.19–22；Table 5/Figure 9 p.23；Figure 10/Table 6 p.24；Figure 11 p.25；Tables 7–8 p.26；Table 9 p.27；Tables 10–11 p.28；Table 12 p.29；Table 13/Figure 12/Table 14 p.30；Figures 13–14 p.31；Figure 15/Figure 16 p.32；Figure 17/Table 15 p.33；Figures 18–19 p.43。
- **页面边界**：正文/Conclusion 在 pp.1–10，Reproducibility 与 References 在 pp.11–13，Appendix A 从 p.14 开始；pp.34–42 主要是 generation examples/prompts，仍纳入 44 页完整检查但不含新的 Figure/Table。

## Source inventory、GitHub 与本地视觉源

- inventory row：reports/tables/visual_source_inventory.csv 当前记录 no_public_source_found；本地目录 corpus/visual_sources/iclr-2026-ff40de6c7ac1/ 不存在。
- fresh GitHub check：unicli gh search-repos 与 gh search repos 找到作者匹配的 https://github.com/ryttry/p-less；检查 main tree 和 commit a681f23682a329099306eea9cf7b1dd0447e2eec。
- 该仓库提供 p_less_samplers.py（与 Figure 15 代码片段一致）、p_less_examples.ipynb 和 README，但没有 PDF 的 TeX、plot scripts、table generators 或 static assets；因此 source status 为 partial_visual_source，不是 exact visual source。
- PDF references 的 arXiv/GitHub 字符串是被引论文/外部链接；没有另一个可核验的作者 figure source。

## Paper-level visual style

- **计数**：main = 4 figures / 4 tables；appendix = 15 figures / 11 tables。
- **Figure typography**：约 4.8–10.0 pt，Computer Modern, Nimbus Roman No9 L, DejaVu Sans；mixed。
- **Table typography**：body 约 5.0 pt、header 约 5.5 pt，Nimbus Roman No9 L, Computer Modern；大矩阵更小。
- **Palette**：主结果曲线固定使用七色 categorical method palette；synthetic threshold plots固定复用 probability/cumulative/tail/threshold 颜色；histogram、profiling 与 failure traces各自采用蓝/红/绿语义。颜色常配合位置、线型、marker、box 结构或文字 legend，但普通 line charts 仍主要靠颜色。
- **Rendering / consistency**：正文曲线、阈值图、表格、直方图和箱线图在 PDF 中以可缩放绘图/文字对象呈现；Figure 15 是 monospace code card。未发现可追溯的原始 raster asset 或 source export，判断以 200 dpi rasterized pages 与 PDF text/object appearance 为准。 ICLR 单栏模板、caption 位置、booktabs 表线、方法顺序、温度刻度和七色方法 palette 在主文与 appendix 较一致。可读性在 appendix 大矩阵、20k-token synthetic plots 和重复 legends 处显著下降；caption 的 sample/seed/uncertainty 自包含程度不一致。

## Object index

| Label | Page | Placement | Module | Width | Types / table shape |
|---|---:|---|---|---|---|
| Figure 1 | 2 | main | introduction | page_width | bar, line, area |
| Figure 2 | 7 | main | results | page_width | line |
| Figure 3 | 9 | main | results | single_column | scatter, pareto |
| Figure 4 | 10 | main | results | page_width | line |
| Figure 5 | 19 | appendix | appendix_B.6 | page_width | bar, line, area |
| Figure 6 | 20 | appendix | appendix_B.6 | page_width | bar, line, area |
| Figure 7 | 21 | appendix | appendix_B.6 | page_width | bar, line, area |
| Figure 8 | 22 | appendix | appendix_B.6 | page_width | bar, line, area |
| Figure 9 | 23 | appendix | appendix_C.3 | single_column | line |
| Figure 10 | 24 | appendix | appendix_C.4 | page_width | line |
| Figure 11 | 25 | appendix | appendix_C.3 | page_width | line |
| Figure 12 | 30 | appendix | appendix_C.9.1 | page_width | histogram |
| Figure 13 | 31 | appendix | appendix_C.9.1 | page_width | histogram |
| Figure 14 | 31 | appendix | appendix_C.9.1 | page_width | histogram |
| Figure 15 | 32 | appendix | appendix_C.11 | page_width | screenshot |
| Figure 16 | 32 | appendix | appendix_C.11 | page_width | box |
| Figure 17 | 33 | appendix | appendix_C.11 | page_width | box |
| Figure 18 | 43 | appendix | appendix_C.13 | page_width | line |
| Figure 19 | 43 | appendix | appendix_C.13 | page_width | line |
| Table 1 | 7 | main | results | page_width | 7 rows × 13 cols, 2 header levels |
| Table 2 | 8 | main | results | single_column | 6 rows × 9 cols, 1 header levels |
| Table 3 | 8 | main | efficiency | single_column | 3 rows × 7 cols, 1 header levels |
| Table 4 | 9 | main | results | single_column | 7 rows × 6 cols, 1 header levels |
| Table 5 | 23 | appendix | appendix_C.3 | page_width | 21 rows × 21 cols, 2 header levels |
| Table 6 | 24 | appendix | appendix_C.4 | page_width | 4 rows × 11 cols, 2 header levels |
| Table 7 | 26 | appendix | appendix_C.5 | page_width | 7 rows × 21 cols, 2 header levels |
| Table 8 | 26 | appendix | appendix_C.6 | page_width | 22 rows × 25 cols, 3 header levels |
| Table 9 | 27 | appendix | appendix_C.7 | page_width | 20 rows × 8 cols, 1 header levels |
| Table 10 | 28 | appendix | appendix_C.8 | page_width | 21 rows × 21 cols, 2 header levels |
| Table 11 | 28 | appendix | appendix_C.8 | page_width | 10 rows × 9 cols, 1 header levels |
| Table 12 | 29 | appendix | appendix_C.9 | page_width | 21 rows × 21 cols, 2 header levels |
| Table 13 | 30 | appendix | appendix_C.10 | page_width | 3 rows × 11 cols, 2 header levels |
| Table 14 | 30 | appendix | appendix_C.11 | single_column | 6 rows × 6 cols, 1 header levels |
| Table 15 | 33 | appendix | appendix_C.11 | single_column | 3 rows × 3 cols, 1 header levels |

## Figure-by-figure audit

### Figure 1 — p. 2

- **Module / placement / width / purpose**：introduction / main / page_width / headline, method_interface, theory_mechanism。
- **Types**：bar, line, area；**complexity** score 4/5，3 panels，5 series，4 legend items，约 75 data marks。
- **Caption**：Figure 1: Comparison of truncation thresholds produced by p-less, min-p, and top-p for a token probability distribution with different applied temperatures (τ ). As temperature increases, p-less avoids admitting a large number of lower-likelihood tokens by considering the entropy of the distribution in computing the threshold.（46 words；moves = title, setup, encoding_key, comparison, main_finding；self-contained=True；main finding=True）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.5–10.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，7 colors (#3E8EBA, #D95F5F, #BDBDBD, #C77CFF, #63B86B, #333333, #FFFFFF）；蓝柱为 token probability，红线为 cumulative probability，灰色区域为 top-p admitted tail；洋红、绿色、灰色水平线分别标记 p-less、min-p、top-p 阈值。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (bottom-center)；shared=False；direct_labels=False；markers=0；line_styles=4；hatching=False；reference_lines=3；uncertainty=none。
- **Encodings**：x=按降序排列的 token index；y=左轴 probability；右轴 cumulative probability；color=probability/cumulative/threshold roles；shape=bars versus threshold line styles；line=red cumulative curve and four threshold guides；facet=τ = 0.5, 1.0, 2.0 panels；text=τ titles, axes and legend。
- **Data/statistics**：合成固定 token 分布在三个温度下的阈值示意，不是模型样本统计；每 panel 画 probability bars、累计曲线和截断尾部，无重复、误差或置信区间。
- **Evidence relation**：§1 用高温长尾 admission 提出问题，§3.1–§3.5 定义完整分布上的 collision-probability threshold；Appendix B.6 Figures 5–8 扩展同一机制。它支持阈值随熵/温度变化的直观关系，不单独证明质量结果。
- **Design strengths**：三 panel 共享 token-index 与阈值语法，温度变化可直接横向扫描。；尾部遮罩、累计曲线和多种线型同时给出 admission 解释。
- **Design weaknesses**：双 y 轴量纲在小尺寸下容易混淆。；阈值线颜色在灰度输出中区分度有限；合成分布未给生成参数。
- **Reusable pattern**：用固定分布的温度 small multiples，把候选集大小变化放在概率柱、累计曲线和阈值线的同一坐标框中。
- **Evidence**：p.2 Figure 1，basis=rendered_observation。

### Figure 2 — p. 7

- **Module / placement / width / purpose**：results / main / page_width / headline, main_comparison, robustness。
- **Types**：line；**complexity** score 4/5，3 panels，7 series，7 legend items，约 105 data marks。
- **Caption**：Figure 2: Accuracy vs. temperature curves of each method on CSQA, QASC, and GSM8k using Llama-2-7b. AUC values achieved by each method are provided in the legend (in parentheses) with the best AUC in bold.（35 words；moves = title, setup, encoding_key, comparison；self-contained=True；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.5–10.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，8 colors (#3E8EBA, #F28C38, #5AAE61, #E34A4A, #8A63C7, #8C564B, #E78AC3, #333333）；七种方法由固定颜色区分，legend 同时写出每方法 AUC，粗体标出最佳 AUC；黑灰为轴和文字。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (lower-left in each panel)；shared=False；direct_labels=False；markers=1；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=Temperature ∈ {0.5, 0.7, 1.0, 1.5, 2.0}；y=accuracy；color=sampling method；shape=one marker family per method；line=solid method trajectories；facet=CSQA, QASC, GSM8K；text=method names and AUC in repeated legends。
- **Data/statistics**：三 panel 各含 7 方法 × 5 温度的 accuracy point estimates；legend 括号内是沿温度曲线归一化计算的 AUC。无 error bar、seed dispersion 或 sample denominator。
- **Evidence relation**：Table 1 给出同一主结果的 AUC 概括，Figure 2 将 CSQA/QASC/GSM8K 的温度响应展开；正文 §4.2 的高温退化与 p-less 稳定性由曲线支撑，Figures 9–11 补齐其他模型/数据集。
- **Design strengths**：三 panel 共享温度/accuracy 语法，legend 提供 AUC，适合从总表下钻到曲线。；高温处曲线分叉清楚呈现 baseline degradation 与 p-less family 稳定。
- **Design weaknesses**：七条曲线和重复 legend 在窄版面中有遮挡风险，方法识别主要依赖颜色。；caption 未说明温度网格或 seed 聚合，不能从图恢复不确定性。
- **Reusable pattern**：先用 AUC 表建立总览，再以固定 x 网格的 method-colored small multiples 展示温度退化。
- **Evidence**：p.7 Figure 2，basis=rendered_observation。

### Figure 3 — p. 9

- **Module / placement / width / purpose**：results / main / single_column / main_comparison, robustness, ablation。
- **Types**：scatter, pareto；**complexity** score 3/5，1 panels，7 series，7 legend items，约 35 data marks。
- **Caption**：Figure 3: QASC diversity by method & temperature（8 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.5–9.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，8 colors (#3E8EBA, #F28C38, #5AAE61, #E34A4A, #8A63C7, #8C564B, #E78AC3, #333333）；颜色表示 sampling method；点位置同时编码 accuracy 与 n-gram diversity，legend 补足方法名。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (lower-right)；shared=False；direct_labels=False；markers=0；line_styles=0；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=mean n-gram diversity；y=mean QASC accuracy；color=sampling method；shape=point marker only；line=None；facet=method × temperature settings；text=legend with method names。
- **Data/statistics**：Llama2-7b QASC 的 method–temperature mean summary；正文说明只保留 overall mean accuracy > 0.5 的设置，所以点数少于完整 7×5 网格。无误差或 frontier uncertainty。
- **Evidence relation**：§5.2 从 Table 4 的 diversity matrix 转到 accuracy–diversity trade-off；Figure 3 用条件筛选散点支持 p-less/p-lessnorm 的局部 Pareto 优势，完整跨模型结果在 Table 10。过滤条件在正文而非 caption。
- **Design strengths**：x/y 轴直接对应论文讨论的两个 estimand，点云快速显示同一 diversity 水平下的 accuracy 差异。；图例保留七种方法。
- **Design weaknesses**：accuracy > 0.5 的选择规则不在 caption，容易把条件性 frontier 读成全网格结论。；没有温度标记或点标签，单个点无法回溯具体 τ；颜色在灰度下不可辨。
- **Reusable pattern**：将 diversity–quality trade-off 放在二维坐标中，并把筛选规则与 temperature marker 写入图内或图注。
- **Evidence**：p.9 Figure 3，basis=rendered_observation。

### Figure 4 — p. 10

- **Module / placement / width / purpose**：results / main / page_width / theory_mechanism, qualitative_evidence, failure。
- **Types**：line；**complexity** score 4/5，2 panels，2 series，2 legend items，约 240 data marks。
- **Caption**：Figure 4: Step-wise entropy and number of admitted tokens for a GSM8K question answered with Llama3-70b.（16 words；moves = title, setup, encoding_key；self-contained=True；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.5–10.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，5 colors (#E34A4A, #1746D1, #000000, #BDBDBD, #FFFFFF）；红 x 为 entropy，蓝圆点/线为 admitted-token count，黑圈标出 min-p 的可疑 admission spike。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=y；legend=True (upper-right)；shared=False；direct_labels=False；markers=2；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=generation step index；y=叠加显示 entropy 与 admitted token count；color=entropy versus token-count role；shape=x marker versus circle；line=solid red/blue traces；facet=min-p versus p-less；text=panel legend and circled region。
- **Data/statistics**：一个 Llama3-70b、τ=2.0 的 GSM8K 题目逐步 trace；红色 entropy 与蓝色 admission count 叠画在共同 y 标度上，没有跨样本分布或不确定性。
- **Evidence relation**：正文 §5.4 将 min-p 错误解释步骤与 Figure 4a 的 admission spike 对齐，再用 Figure 4b 展示 p-less 在高 entropy 时的受控 admission；Table 13 与 Figures 12–14 提供总体诊断。这是机制案例而非失败率估计。
- **Design strengths**：同一 step 轴把文本推理事件、entropy 与候选数变化放在可追踪路径上。；x/circle marker 与颜色双重区分两条 trace，黑圈指定局部区域。
- **Design weaknesses**：两个不同量共用 y 轴且没有第二轴/单位，峰值相对尺度不能直接比较。；单个案例被置于正文 headline 位置，caption 没有题目、τ 或失败类型摘要。
- **Reusable pattern**：以 step-wise dual trace 对齐具体推理事件和机制异常；实例必须与总体诊断和案例选择规则分开。
- **Evidence**：p.10 Figure 4，basis=rendered_observation。

### Figure 5 — p. 19

- **Module / placement / width / purpose**：appendix_B.6 / appendix / page_width / experimental_design, theory_mechanism, robustness。
- **Types**：bar, line, area；**complexity** score 5/5，6 panels，5 series，8 legend items，约 126 data marks。
- **Caption**：Figure 5: Effect of temperature on a fixed token logits distribution with small vocabulary size.（15 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，7 colors (#3E8EBA, #D95F5F, #BDBDBD, #C77CFF, #63B86B, #333333, #FFFFFF）；蓝 probability、红 cumulative、灰 top-p tail、洋红/绿/灰 threshold；与 Figure 1 复用同一 palette。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (below panels)；shared=True；direct_labels=False；markers=0；line_styles=4；hatching=False；reference_lines=4；uncertainty=none。
- **Encodings**：x=sorted token index；y=probability and cumulative probability；color=sampling-rule threshold；shape=None；line=cumulative curve and four threshold rules；facet=τ = 0.5, 0.7, 1.0, 2.0, 3.0, ∞；text=panel labels and admitted-token counts。
- **Data/statistics**：固定 logits/probability 分布的六温度 synthetic sweep；每 panel 画 sorted probability bars、cumulative curve、top-p tail 和四种 threshold，legend 括号给出 admitted-token counts；无重复或误差。
- **Evidence relation**：Appendix B.6 是 Figure 1 的系统扩展：先隔离 temperature 对小词表分布的影响，再由 Figures 6–8 改变 profile、长尾和 vocabulary size。它支持 rule geometry，不是 downstream quality evidence。
- **Design strengths**：阈值颜色、累计曲线和 tail shading 与 Figure 1 一致，跨页比较成本低。；legend 中 admitted-token count 把视觉尾部连接到离散候选集大小。
- **Design weaknesses**：六 panel、双 y 量与多 threshold 线在论文尺寸下拥挤，小字号和淡色线降低可读性。；caption 没有列出每个 synthetic distribution 的完整生成参数或样本分母。
- **Reusable pattern**：固定 probability/cumulative/threshold 视觉 grammar，逐步改变 temperature、profile、long-tail 与 vocabulary size，并把 distribution parameters 和 admitted-set counts 一起报告。
- **Evidence**：p.19 Figure 5，basis=rendered_observation。

### Figure 6 — p. 20

- **Module / placement / width / purpose**：appendix_B.6 / appendix / page_width / experimental_design, theory_mechanism, robustness。
- **Types**：bar, line, area；**complexity** score 5/5，6 panels，5 series，8 legend items，约 6006 data marks。
- **Caption**：Figure 6: Effect of different token probability distribution profiles with a moderate vocabulary size. The legend shows the size of the admitted tokens for each sampling method in parentheses.（29 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，7 colors (#3E8EBA, #D95F5F, #BDBDBD, #C77CFF, #63B86B, #333333, #FFFFFF）；蓝 probability、红 cumulative、灰 top-p tail、洋红/绿/灰 threshold；与 Figure 1 复用同一 palette。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (below panels)；shared=False；direct_labels=False；markers=0；line_styles=4；hatching=False；reference_lines=4；uncertainty=none。
- **Encodings**：x=sorted token index；y=probability and cumulative probability；color=sampling-rule threshold；shape=None；line=cumulative curve and four threshold rules；facet=six moderate-vocabulary probability profiles；text=panel labels and admitted-token counts。
- **Data/statistics**：中等词表（约 1000 tokens）的六种 probability-profile synthetic distributions；每 panel 约千个 bar positions并标出方法 admitted-token 数。不是 LLM 样本，无 uncertainty。
- **Evidence relation**：B.6 在 Figure 5 的 temperature control 后改变 distribution profile，检验 p-less 是否依据整个分布调整 threshold；Figures 7–8 继续推到 long-tail 与更大 vocabulary。
- **Design strengths**：阈值颜色、累计曲线和 tail shading 与 Figure 1 一致，跨页比较成本低。；legend 中 admitted-token count 把视觉尾部连接到离散候选集大小。
- **Design weaknesses**：每 panel 近千个柱形使有效 mark 数极高，标签和细节只能依赖放大。；caption 没有列出每个 synthetic distribution 的完整生成参数或样本分母。
- **Reusable pattern**：固定 probability/cumulative/threshold 视觉 grammar，逐步改变 temperature、profile、long-tail 与 vocabulary size，并把 distribution parameters 和 admitted-set counts 一起报告。
- **Evidence**：p.20 Figure 6，basis=rendered_observation。

### Figure 7 — p. 21

- **Module / placement / width / purpose**：appendix_B.6 / appendix / page_width / experimental_design, theory_mechanism, robustness。
- **Types**：bar, line, area；**complexity** score 5/5，2 panels，5 series，8 legend items，约 1600 data marks。
- **Caption**：Figure 7: Effect of long-tail token probability distributions with a moderate vocabulary size. The legend shows the size of the admitted tokens for each sampling method in parentheses.（28 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，7 colors (#3E8EBA, #D95F5F, #BDBDBD, #C77CFF, #63B86B, #333333, #FFFFFF）；蓝 probability、红 cumulative、灰 top-p tail、洋红/绿/灰 threshold；与 Figure 1 复用同一 palette。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (below panels)；shared=False；direct_labels=False；markers=0；line_styles=4；hatching=False；reference_lines=4；uncertainty=none。
- **Encodings**：x=sorted token index；y=probability and cumulative probability；color=sampling-rule threshold；shape=None；line=cumulative curve and four threshold rules；facet=two moderate-vocabulary long-tail profiles；text=panel labels and admitted-token counts。
- **Data/statistics**：两个中等词表 long-tail probability distributions 的 synthetic threshold view；bar/cumulative/area layer 和 admitted counts 比较各规则纳入尾部的大小，无重复或误差。
- **Evidence relation**：B.6 从 profile 变化过渡到 long-tail stress test，支持 p-less 可在高 entropy/长尾时增加 admission但不固定放宽；Figure 8 再提高 vocabulary size。
- **Design strengths**：阈值颜色、累计曲线和 tail shading 与 Figure 1 一致，跨页比较成本低。；legend 中 admitted-token count 把视觉尾部连接到离散候选集大小。
- **Design weaknesses**：长尾形状与具体生成参数未写入 caption；x 轴 token index 过密，尾部差异在缩小后难读。；caption 没有列出每个 synthetic distribution 的完整生成参数或样本分母。
- **Reusable pattern**：固定 probability/cumulative/threshold 视觉 grammar，逐步改变 temperature、profile、long-tail 与 vocabulary size，并把 distribution parameters 和 admitted-set counts 一起报告。
- **Evidence**：p.21 Figure 7，basis=rendered_observation。

### Figure 8 — p. 22

- **Module / placement / width / purpose**：appendix_B.6 / appendix / page_width / experimental_design, theory_mechanism, robustness。
- **Types**：bar, line, area；**complexity** score 5/5，2 panels，5 series，8 legend items，约 20000 data marks。
- **Caption**：Figure 8: Effect of long-tail token probability distributions with a large vocabulary size. For simplicity, we include a modal token that is on the left-most of each distribution chart (not clearly visible due to the sheer size of the vocabulary). The legend shows the size of the admitted tokens for each sampling method in parentheses.（55 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，7 colors (#3E8EBA, #D95F5F, #BDBDBD, #C77CFF, #63B86B, #333333, #FFFFFF）；蓝 probability、红 cumulative、灰 top-p tail、洋红/绿/灰 threshold；与 Figure 1 复用同一 palette。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (below panels)；shared=False；direct_labels=False；markers=0；line_styles=4；hatching=False；reference_lines=4；uncertainty=none。
- **Encodings**：x=sorted token index；y=probability and cumulative probability；color=sampling-rule threshold；shape=None；line=cumulative curve and four threshold rules；facet=two long-tail profiles with vocabulary size 10,000；text=panel labels and admitted-token counts。
- **Data/statistics**：大词表 long-tail synthetic stress test（约 10,000 tokens）；作者说明 modal token 位于最左端且因规模不可见。各 panel仍展示 probability bars、cumulative curve、top-p tail与threshold，无 uncertainty。
- **Evidence relation**：它是 B.6 的最大规模边界，回应 Figure 1 的高温尾部直觉是否依赖小词表；与 Proposition 1 的非空候选集保证方向一致，但仍是合成而非真实模型校准。
- **Design strengths**：阈值颜色、累计曲线和 tail shading 与 Figure 1 一致，跨页比较成本低。；legend 中 admitted-token count 把视觉尾部连接到离散候选集大小。
- **Design weaknesses**：约万级 x 轴和柱层在论文尺寸几乎不可逐点读取；caption 没给 long-tail 参数或可见范围，legend 计数需放大核验。；caption 没有列出每个 synthetic distribution 的完整生成参数或样本分母。
- **Reusable pattern**：固定 probability/cumulative/threshold 视觉 grammar，逐步改变 temperature、profile、long-tail 与 vocabulary size，并把 distribution parameters 和 admitted-set counts 一起报告。
- **Evidence**：p.22 Figure 8，basis=rendered_observation。

### Figure 9 — p. 23

- **Module / placement / width / purpose**：appendix_C.3 / appendix / single_column / main_comparison, robustness。
- **Types**：line；**complexity** score 3/5，1 panels，7 series，7 legend items，约 35 data marks。
- **Caption**：Figure 9: Accuracy versus temperature curves of each method for the GPQA dataset using Llama2-7b. AUC values achieved by each method are provided in the legend (in parentheses) with the best AUC in bold.（34 words；moves = title, setup, encoding_key；self-contained=True；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.5–10.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，8 colors (#3E8EBA, #F28C38, #5AAE61, #E34A4A, #8A63C7, #8C564B, #E78AC3, #333333）；七种方法用固定 categorical colors；AUC 在 legend 中作为括号文本，黑灰是坐标与文字。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (lower-left)；shared=False；direct_labels=False；markers=1；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=Temperature；y=GPQA accuracy；color=sampling method；shape=single marker family；line=solid curves；facet=one GPQA panel for Llama2-7b；text=method plus AUC in legend。
- **Data/statistics**：Llama2-7b GPQA 的七方法×五温度 accuracy point estimates，legend给归一化 AUC；无 error bar、seed spread或每温度样本分母。
- **Evidence relation**：C.3 作为 Figure 2 的 GPQA 补充，对应 Table 5 的 GPQA columns 和 Table 1 的 GPQA AUC；panel 展示 p-less family 在高温的相对位置。
- **Design strengths**：单 panel 减少 Figure 2 多 panel 的拥挤，AUC 仍保留在 legend。；方法颜色和温度刻度与主 Figure 2 一致。
- **Design weaknesses**：无 uncertainty，AUC/accuracy 聚合层级必须回到正文；legend 占据左下，低准确度曲线附近可读性有限。
- **Reusable pattern**：用同一 method palette 将缺失 dataset 的温度曲线作为总表下钻，让 AUC 与 pointwise curve 共存。
- **Evidence**：p.23 Figure 9，basis=rendered_observation。

### Figure 10 — p. 24

- **Module / placement / width / purpose**：appendix_C.4 / appendix / page_width / main_comparison, robustness。
- **Types**：line；**complexity** score 4/5，4 panels，7 series，28 legend items，约 140 data marks。
- **Caption**：Figure 10: Accuracy versus temperature curves of each method for each of the four math and logical reasoning datasets GSM8K, GPQA, QASC and CSQA using Mistral-7b. AUC values achieved by each method are provided in the legend (in parentheses) with the best AUC in bold.（45 words；moves = title, setup, encoding_key；self-contained=True；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.0–9.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，8 colors (#3E8EBA, #F28C38, #5AAE61, #E34A4A, #8A63C7, #8C564B, #E78AC3, #333333）；固定七色方法 palette；每 panel legend 写 AUC，黑灰仅作坐标和文字。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (lower-left in each panel)；shared=False；direct_labels=False；markers=1；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=Temperature；y=accuracy；color=sampling method；shape=single marker family；line=solid curves；facet=CSQA/QASC/GSM8K/GPQA for Mistral-7b；text=panel titles and method/AUC legends。
- **Data/statistics**：Mistral-7b 四 dataset 温度—accuracy curves；每 panel 7 方法×5 温度并显示 AUC。Mistral 主结果使用一个 random seed，图中没有 dispersion。
- **Evidence relation**：C.4 的展开对应 Table 5 Mistral block 和 Table 6 的 τ=1.0 对照；把正文高温稳定性扩展到 Mistral，但 one-seed 限制在周围文字而非 caption。
- **Design strengths**：四 panel 共享曲线 grammar，跨 dataset 的退化模式易比较。；caption 指明模型、数据集和 AUC 位置，方法顺序与 Figure 2 一致。
- **Design weaknesses**：重复四个 legend 占用版面，且颜色承担七方法区分；caption 没写 one-seed 或每点 accuracy 分母。
- **Reusable pattern**：将模型扩展结果组织成 matched dataset panels，保留 palette/AUC key，并把 seed/aggregation 写进 caption 或旁表。
- **Evidence**：p.24 Figure 10，basis=rendered_observation。

### Figure 11 — p. 25

- **Module / placement / width / purpose**：appendix_C.3 / appendix / page_width / main_comparison, robustness。
- **Types**：line；**complexity** score 4/5，4 panels，7 series，28 legend items，约 140 data marks。
- **Caption**：Figure 11: Accuracy versus temperature curves of each method for each of the four math and logical reasoning datasets GSM8K, GPQA, QASC and CSQA using Llama3-70b. AUC values achieved by each method are provided in the legend (in parentheses) with the best AUC in bold.（45 words；moves = title, setup, encoding_key；self-contained=True；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.0–9.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，8 colors (#3E8EBA, #F28C38, #5AAE61, #E34A4A, #8A63C7, #8C564B, #E78AC3, #333333）；七方法沿用主文固定颜色；AUC 数字附在 legend，黑灰为坐标文字。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=True (lower-left in each panel)；shared=False；direct_labels=False；markers=1；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=Temperature；y=accuracy；color=sampling method；shape=single marker family；line=solid curves；facet=CSQA/QASC/GSM8K/GPQA for Llama3-70b；text=panel titles and method/AUC legends。
- **Data/statistics**：Llama3-70b 四 dataset 的 accuracy—temperature point estimates；每 panel 7 方法×5 温度，legend 给 AUC。Llama3 只用一个 random seed，图内无误差。
- **Evidence relation**：与 Figures 2/9/10 组成跨模型曲线组，并与 Table 1/5 的 Llama3 AUC/accuracy 对照；正文的“最高或相差 0.005 内”依赖这些数值而非线宽。
- **Design strengths**：复用同一四 panel layout 与 method colors，跨 model 读取成本低。；各 panel保留局部 y 范围，dataset 内差异清楚。
- **Design weaknesses**：四 panel y 轴范围不同，跨 dataset 的垂直高度不能直接比较；one-seed/无 uncertainty 未进入 caption。
- **Reusable pattern**：固定 panel 顺序和方法 palette 展开另一模型的同一温度网格，并在图注/旁表明确尺度和 replicate boundary。
- **Evidence**：p.25 Figure 11，basis=rendered_observation。

### Figure 12 — p. 30

- **Module / placement / width / purpose**：appendix_C.9.1 / appendix / page_width / mechanism, robustness, qualitative_evidence。
- **Types**：histogram；**complexity** score 4/5，12 panels，1 series，0 legend items，约 未量化 data marks。
- **Caption**：Figure 12: Histogram of Entropy Distributions at τ = 0.5 for Llama-3-70b on GPQA（14 words；moves = title, setup；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：sequential，3 colors (#4C78A8, #D9D9D9, #FFFFFF）；蓝 histogram bars 表示 entropy frequency；method row 与 admission-count column 用位置区分条件。 grayscale_safe=True。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=False (None)；shared=None；direct_labels=True；markers=0；line_styles=0；hatching=False；reference_lines=0；uncertainty=distribution。
- **Encodings**：x=entropy bins；y=frequency；color=none (same blue fill)；shape=admitted-token-count column；line=None；facet=3 methods × 4 admission-count groups；text=row labels top-p/min-p/p-less and column labels。
- **Data/statistics**：Llama3-70b GPQA、τ=0.5 的三方法×四 admitted-token-count group entropy histograms；频数分布而非均值，未给 bin width、样本数或误差。
- **Evidence relation**：Table 13 的 mean entropy/admission summary → Figure 12 的 distributional decomposition；Figures 12–14 共同支持同一 admission size 下的 entropy shift，但不提供因果或完整 prevalence。与 Table 13 的 τ=0.5 row 对齐
- **Design strengths**：12-cell matrix 把 method 与 admission-size 条件固定在位置上，避免重复 legend。；histogram 形状比单一 mean 更能展示高 entropy tail。
- **Design weaknesses**：caption 不解释四列分组与共同 scale；仅靠蓝色填充，灰度安全主要来自位置。；没有 sample denominator 或 uncertainty，不能从柱高判断 method prevalence。
- **Reusable pattern**：用 method rows × admission-bin columns 的 histogram grid 分解机制，并在 caption 写清 bin edges、共同 axes、样本分母与 aggregation。
- **Evidence**：p.30 Figure 12，basis=rendered_observation。

### Figure 13 — p. 31

- **Module / placement / width / purpose**：appendix_C.9.1 / appendix / page_width / mechanism, robustness, qualitative_evidence。
- **Types**：histogram；**complexity** score 4/5，12 panels，1 series，0 legend items，约 未量化 data marks。
- **Caption**：Figure 13: Histogram of Entropy Distributions at τ = 1.0 for Llama-3-70b on GPQA（14 words；moves = title, setup；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：sequential，3 colors (#4C78A8, #D9D9D9, #FFFFFF）；蓝 histogram bars 表示 entropy frequency；method row 与 admission-count column 用位置区分条件。 grayscale_safe=True。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=False (None)；shared=None；direct_labels=True；markers=0；line_styles=0；hatching=False；reference_lines=0；uncertainty=distribution。
- **Encodings**：x=entropy bins；y=frequency；color=none (same blue fill)；shape=admitted-token-count column；line=None；facet=3 methods × 4 admission-count groups；text=row labels top-p/min-p/p-less and column labels。
- **Data/statistics**：Llama3-70b GPQA、τ=1.0 的三方法×四 admitted-token-count group entropy histograms；频数分布而非均值，未给 bin width、样本数或误差。
- **Evidence relation**：Table 13 的 mean entropy/admission summary → Figure 13 的 distributional decomposition；Figures 12–14 共同支持同一 admission size 下的 entropy shift，但不提供因果或完整 prevalence。作为 τ=0.5 的中温扩展
- **Design strengths**：12-cell matrix 把 method 与 admission-size 条件固定在位置上，避免重复 legend。；histogram 形状比单一 mean 更能展示高 entropy tail。
- **Design weaknesses**：caption 不解释四列分组与共同 scale；仅靠蓝色填充，灰度安全主要来自位置。；没有 sample denominator 或 uncertainty，不能从柱高判断 method prevalence。
- **Reusable pattern**：用 method rows × admission-bin columns 的 histogram grid 分解机制，并在 caption 写清 bin edges、共同 axes、样本分母与 aggregation。
- **Evidence**：p.31 Figure 13，basis=rendered_observation。

### Figure 14 — p. 31

- **Module / placement / width / purpose**：appendix_C.9.1 / appendix / page_width / mechanism, robustness, qualitative_evidence。
- **Types**：histogram；**complexity** score 4/5，12 panels，1 series，0 legend items，约 未量化 data marks。
- **Caption**：Figure 14: Histogram of Entropy Distributions at τ = 2.0 for Llama-3-70b on GPQA（14 words；moves = title, setup；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，4.8–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：sequential，3 colors (#4C78A8, #D9D9D9, #FFFFFF）；蓝 histogram bars 表示 entropy frequency；method row 与 admission-count column 用位置区分条件。 grayscale_safe=True。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=none；legend=False (None)；shared=None；direct_labels=True；markers=0；line_styles=0；hatching=False；reference_lines=0；uncertainty=distribution。
- **Encodings**：x=entropy bins；y=frequency；color=none (same blue fill)；shape=admitted-token-count column；line=None；facet=3 methods × 4 admission-count groups；text=row labels top-p/min-p/p-less and column labels。
- **Data/statistics**：Llama3-70b GPQA、τ=2.0 的三方法×四 admitted-token-count group entropy histograms；频数分布而非均值，未给 bin width、样本数或误差。
- **Evidence relation**：Table 13 的 mean entropy/admission summary → Figure 14 的 distributional decomposition；Figures 12–14 共同支持同一 admission size 下的 entropy shift，但不提供因果或完整 prevalence。作为高温 entropy/admission stress case
- **Design strengths**：12-cell matrix 把 method 与 admission-size 条件固定在位置上，避免重复 legend。；histogram 形状比单一 mean 更能展示高 entropy tail。
- **Design weaknesses**：caption 不解释四列分组与共同 scale；仅靠蓝色填充，灰度安全主要来自位置。；没有 sample denominator 或 uncertainty，不能从柱高判断 method prevalence。
- **Reusable pattern**：用 method rows × admission-bin columns 的 histogram grid 分解机制，并在 caption 写清 bin edges、共同 axes、样本分母与 aggregation。
- **Evidence**：p.31 Figure 14，basis=rendered_observation。

### Figure 15 — p. 32

- **Module / placement / width / purpose**：appendix_C.11 / appendix / page_width / method_interface, reproduction。
- **Types**：screenshot；**complexity** score 2/5，1 panels，None series，0 legend items，约 未量化 data marks。
- **Caption**：Figure 15: Python code snippet for p-less sampling（8 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：DejaVu Sans Mono, Computer Modern，5.2–8.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：grayscale，3 colors (#F2F2F2, #333333, #FFFFFF）；浅灰 code block、深色 monospace code 和白色背景只区分容器，不编码实验量。 grayscale_safe=True。
- **Plot grammar**：rendering=vector；x/y=none/none；grid=none；legend=False (None)；shared=False；direct_labels=True；markers=None；line_styles=None；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=None；y=None；color=None；shape=None；line=None；facet=None；text=monospace function name, tensor operations, and comments。
- **Data/statistics**：Figure 15 是 p_less_decode 的 PyTorch code card：平方概率求和得 p，mask 低于阈值的 token，原地归一化后 multinomial 采样；无样本、统计量或 uncertainty。公开仓库 commit a681f23682a329099306eea9cf7b1dd0447e2eec 的 p_less_samplers.py 与片段逐行对应，但不是绘图源。
- **Evidence relation**：§3.1 Equations 2–4 → Figure 15 executable implementation → C.11 CPU/RAM profiling Figures 16–17；图能闭合规则到代码接口，但不能验证速度或质量。
- **Design strengths**：核心 mask、平方和、renormalization 与 multinomial 顺序在一个完整 code card 内。；monospace 与灰底形成清晰的实现证据层。
- **Design weaknesses**：片段未显示 p-lessnorm，也没有说明 probs 原地修改、shape/edge handling 或版本环境；caption 只有标题。
- **Reusable pattern**：将最小 executable kernel 作为 code figure，并在 caption/source manifest 绑定公式、版本、输入 shape 与副作用。
- **Evidence**：p.32 Figure 15，basis=rendered_observation。

### Figure 16 — p. 32

- **Module / placement / width / purpose**：appendix_C.11 / appendix / page_width / efficiency_cost, robustness。
- **Types**：box；**complexity** score 5/5，1 panels，3 series，3 legend items，约 96 data marks。
- **Caption**：Figure 16: CPU time（4 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：DejaVu Sans, Nimbus Roman No9 L，5.0–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，4 colors (#3E8EBA, #5AAE61, #E34A4A, #FFFFFF）；蓝 top-p、绿 min-p、红 p-less 表示 method；白色为 canvas。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=categorical/linear；grid=y；legend=True (upper-right)；shared=False；direct_labels=False；markers=None；line_styles=0；hatching=False；reference_lines=0；uncertainty=box。
- **Encodings**：x=32-step generation bins from 0–31 to 992–1023；y=CPU time (ms)；color=sampling method；shape=box-and-whisker distribution；line=None；facet=one panel with 32 temporal bins；text=legend for top-p_0.9/min-p_0.1/p-less。
- **Data/statistics**：C.11 的 Mistral-7b、100 GSM8K samples fine-grained CPU trace；每 32 generation steps 合并为一个 bin，三方法各画 boxplot。箱体/whisker 的中心与 outlier 规则未在 caption 定义。
- **Evidence relation**：Table 3 mean/SD/SEM → C.11 t-test → Figure 16 temporal CPU distribution → Table 15 summary；它扩展平均速度为 temporal distribution，但不直接标 mean/median 或 test result。
- **Design strengths**：箱线图显示随 generation step 的波动，而非只重复均值。；方法颜色与 Figure 17/Table 15 profiling bundle 一致，32-step bin 使长 trace 可读。
- **Design weaknesses**：x 轴 32 个类别标签密集，颜色没有 marker/line redundancy；caption 未写硬件、时间单位以外的 profiling 细节或箱体统计语义。
- **Reusable pattern**：用固定时间 bin 的 grouped boxplots 展示资源轨迹，明确 replication unit、统计定义、硬件和共同 y-scale。
- **Evidence**：p.32 Figure 16，basis=rendered_observation。

### Figure 17 — p. 33

- **Module / placement / width / purpose**：appendix_C.11 / appendix / page_width / efficiency_cost, robustness。
- **Types**：box；**complexity** score 5/5，1 panels，3 series，3 legend items，约 96 data marks。
- **Caption**：Figure 17: RAM usage（4 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：DejaVu Sans, Nimbus Roman No9 L，5.0–8.5 pt，regular, bold，provenance=rendered_estimate。
- **Color**：categorical，4 colors (#3E8EBA, #5AAE61, #E34A4A, #FFFFFF）；蓝 top-p、绿 min-p、红 p-less 表示 method；白灰为背景。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=categorical/linear；grid=y；legend=True (upper-right)；shared=False；direct_labels=False；markers=None；line_styles=0；hatching=False；reference_lines=0；uncertainty=box。
- **Encodings**：x=32-step generation bins；y=RAM usage (GB)；color=sampling method；shape=box-and-whisker distribution；line=None；facet=one panel with 32 temporal bins；text=legend for three methods。
- **Data/statistics**：同一 100 GSM8K-sample profiling protocol 的 RAM usage boxplots；每 32 generation steps 一 bin，三方法并排，纵轴 GB。caption 没定义 box summary、硬件或 memory accounting。
- **Evidence relation**：Figure 16 CPU companion → Figure 17 RAM companion → Table 15 mean ± spread；二者共同支持 p-less resource footprint 较低，但不提供跨硬件迁移性。
- **Design strengths**：与 Figure 16 完全匹配 x/bin/颜色 grammar，CPU 与 RAM 可并读。；boxplot 保留 temporal variability，避免只凭 Table 15 均值。
- **Design weaknesses**：caption 只有标题，读者不知道 binning、sample count 或方法超参数；三色在灰度下混淆。
- **Reusable pattern**：将同一分箱和方法 palette 复制到第二资源指标，并明确 profiling window、boxplot statistics、硬件和样本分母。
- **Evidence**：p.33 Figure 17，basis=rendered_observation。

### Figure 18 — p. 43

- **Module / placement / width / purpose**：appendix_C.13 / appendix / page_width / failure, mechanism, qualitative_evidence。
- **Types**：line；**complexity** score 4/5，1 panels，2 series，2 legend items，约 220 data marks。
- **Caption**：Figure 18: Entropy trace for failure pattern 1 example（9 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.0–9.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，5 colors (#E34A4A, #1746D1, #000000, #D9D9D9, #FFFFFF）；红 x 是 entropy、蓝圆点是 admitted-token count、黑色椭圆圈出 failure region。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=y；legend=True (upper-left)；shared=False；direct_labels=False；markers=2；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=generation Step Index；y=entropy and admitted-token count；color=entropy versus admission roles；shape=x versus circle markers；line=solid red/blue traces；facet=one selected failure-pattern-1 generation；text=legend and circled region。
- **Data/statistics**：C.13 的一个 failure-pattern-1 generation；trace 同时画 entropy 与 admitted tokens，并圈出 末段 uncertainty/admission 区域。没有 failure prevalence、抽样分母、重复或 uncertainty。
- **Evidence relation**：正文 §5.3 指向 C.13；Figure 18 将复杂 arithmetic 的末段 spike 具体化，并与 Figure 19 的 question-interpretation failure 对照。
- **Design strengths**：黑圈把文字描述的 failure step 绑定到具体局部轨迹，红/蓝 marker 使两量可追踪。；顶部 μ/σ tokens 与 μ/σ entropy summary 给出案例级 context。
- **Design weaknesses**：只选择一个 final-sum arithmetic failure，不能估计发生率。；双量共用 y 轴且无单位/第二轴，局部峰值容易被过度因果化；caption 没有 prompt、τ或选择标准。
- **Reusable pattern**：把典型 failure 的文本位置与 entropy/admission trace 并置；同时提供 case-selection denominator 和总体 failure rate。
- **Evidence**：p.43 Figure 18，basis=rendered_observation。

### Figure 19 — p. 43

- **Module / placement / width / purpose**：appendix_C.13 / appendix / page_width / failure, mechanism, qualitative_evidence。
- **Types**：line；**complexity** score 4/5，1 panels，2 series，2 legend items，约 220 data marks。
- **Caption**：Figure 19: Entropy trace for failure pattern 2 example（9 words；moves = title；self-contained=False；main finding=False）。
- **Typography**：Computer Modern, Nimbus Roman No9 L, DejaVu Sans，5.0–9.0 pt，regular, bold，provenance=rendered_estimate。
- **Color**：mixed，5 colors (#E34A4A, #1746D1, #000000, #D9D9D9, #FFFFFF）；红 x 是 entropy、蓝圆点是 admitted-token count、黑色椭圆圈出 failure region。 grayscale_safe=False。
- **Plot grammar**：rendering=vector；x/y=linear/linear；grid=y；legend=True (upper-right)；shared=False；direct_labels=False；markers=2；line_styles=1；hatching=False；reference_lines=0；uncertainty=none。
- **Encodings**：x=generation Step Index；y=entropy and admitted-token count；color=entropy versus admission roles；shape=x versus circle markers；line=solid red/blue traces；facet=one selected failure-pattern-2 generation；text=legend and circled region。
- **Data/statistics**：C.13 的一个 failure-pattern-2 generation；trace 同时画 entropy 与 admitted tokens，并圈出 早期 uncertainty/admission 区域。没有 failure prevalence、抽样分母、重复或 uncertainty。
- **Evidence relation**：Figure 19 与 Figure 18 构成两种 failure pattern 的 paired qualitative evidence；支持案例边界而非总体 model error analysis。
- **Design strengths**：黑圈把文字描述的 failure step 绑定到具体局部轨迹，红/蓝 marker 使两量可追踪。；顶部 μ/σ tokens 与 μ/σ entropy summary 给出案例级 context。
- **Design weaknesses**：只选择一个 ambiguous-question failure，不能估计发生率。；双量共用 y 轴且无单位/第二轴，局部峰值容易被过度因果化；caption 没有 prompt、τ或选择标准。
- **Reusable pattern**：把典型 failure 的文本位置与 entropy/admission trace 并置；同时提供 case-selection denominator 和总体 failure rate。
- **Evidence**：p.43 Figure 19，basis=rendered_observation。

## Table-by-table audit

### Table 1 — p. 7

- **Module / placement / width / purpose**：results / main / page_width / headline, main_comparison。
- **Caption**：Table 1: AUC of LLama2-7b, Mistral-7b, and Llama3-70b across different sampling methods for math and logical reasoning datasets. The best AUC is in bold and the second best is underlined.（30 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.5/7.0 pt，header weight=bold；7 rows × 13 columns，2 header levels，0 row groups，decimal precision=3。
- **Rules / highlighting**：booktabs；bold, underline, best_second_best。
- **Uncertainty**：无 uncertainty columns；AUC 是五温度 accuracy curve 的 normalized area summary，Llama2 底层 accuracy 跨 3 seeds，Mistral/Llama3 为单 seed。
- **Data/statistics**：七方法 × 3 models × 4 datasets 的 AUC point estimates；模型为 grouped column headers，dataset 为第二层 header。
- **Evidence relation**：§4.2 的核心跨模型/数据集比较；Table 1 概括，Figure 2/9–11 展开温度曲线，Table 5 给全温度 accuracy。best/second-best 只表达表内 point-estimate 排名。
- **Design strengths**：模型和数据集两级表头把 12 个 cell 组织成可扫描矩阵。；粗体/下划线提供明确的 best/second-best key，且表位于正文结果段落旁。
- **Design weaknesses**：13 列小字号仍需横向扫描，method 名称与 model grouping 的层级较轻。；AUC 把温度轨迹压成单值，caption 未报告 integration 网格、seed 和样本分母。
- **Reusable pattern**：用 grouped column header 把 model×dataset 总结成 benchmark surface，再以同一方法顺序连接到温度曲线和完整 appendix matrix。
- **Evidence**：p.7 Table 1，basis=rendered_observation。

### Table 2 — p. 8

- **Module / placement / width / purpose**：results / main / single_column / headline, main_comparison。
- **Caption**：Table 2: Length-controlled win rate for 100 sampled prompts from the Writing Prompts dataset.（14 words；moves = title, setup；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.5/7.0 pt，header weight=bold；6 rows × 9 columns，1 header levels，2 row groups，decimal precision=2。
- **Rules / highlighting**：booktabs；bold。
- **Uncertainty**：每个 model×temperature row 是 100 prompts 的 length-controlled win-rate point estimate；无 interval、重复 generation dispersion 或 tie-rate columns。
- **Data/statistics**：两 model row groups × 三温度 × 七采样方法；Model/Temperature 是左侧条件列，方法是七个结果列。
- **Evidence relation**：§4.3 creative-writing 主结果；temperature=1.0 的 default reference 与高温 degradation 在行内可见，Appendix A human evaluation 提供方向性外部检查。
- **Design strengths**：row-group 与温度列使高温 collapse 可直接逐行比较。；最佳值用粗体突出，数据密度适中，caption 给出 100-prompt denominator。
- **Design weaknesses**：caption 未定义 win-rate pairing/length control 或 reference generation 细节。；每 setting 一次 generation，且无 dispersion；高温 0 值容易被读成确定性失败。
- **Reusable pattern**：用 model row groups 与温度行把 creative-writing quality 退化路径放进紧凑表，并把 reference、length control 和 repetition unit 写在 caption。
- **Evidence**：p.8 Table 2，basis=rendered_observation。

### Table 3 — p. 8

- **Module / placement / width / purpose**：efficiency / main / single_column / efficiency_cost, main_comparison。
- **Caption**：Table 3: Average sampling time per token (in seconds) for p-less and other methods.（14 words；moves = title, setup, uncertainty_definition；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.2/6.8 pt，header weight=bold；3 rows × 7 columns，1 header levels，0 row groups，decimal precision=5。
- **Rules / highlighting**：booktabs；bold。
- **Uncertainty**：Mean、Standard Deviation、Standard Error of Mean 明确给出 timing dispersion；表没有 sample count、pairing、hardware 或 per-generation aggregation。
- **Data/statistics**：三 statistic rows × 六 methods plus row-label column，单位为 seconds/token；p-less mean 粗体突出。
- **Evidence relation**：正文 §5.1 的 200 Mistral-7b generations timing summary；Table 14 pairwise t-test 和 Figures 16–17 temporal boxplots 是后续证据。正文“22%”应按 mean time 变化理解。
- **Design strengths**：三行统计量在一个 compact table 中显示中心和 spread，优于只报单一均值。；统一小数位和 booktabs rule 让六方法比较快速。
- **Design weaknesses**：SD/SEM aggregation unit、200 generations 与 C.11 的 100 GSM8K samples 存在描述差异。；没有硬件、batch、token length 或计时窗口，跨机器可比性有限。
- **Reusable pattern**：把 mean、SD、SEM 纵向堆叠并在 caption 写清计时单位、sample unit、硬件和 pairing，避免速度百分比脱离分母。
- **Evidence**：p.8 Table 3，basis=rendered_observation。

### Table 4 — p. 9

- **Module / placement / width / purpose**：results / main / single_column / main_comparison, robustness。
- **Caption**：Table 4: QASC diversity by method & temperature（8 words；moves = title, setup；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.2/6.8 pt，header weight=bold；7 rows × 6 columns，1 header levels，0 row groups，decimal precision=2。
- **Rules / highlighting**：booktabs；none。
- **Uncertainty**：QASC n-gram diversity 的 method×temperature means；正文以 accuracy > 0.5 条件筛 Figure 3，但 Table 4 给完整七方法×五温度 values，无 uncertainty。
- **Data/statistics**：七方法行 × 五温度列，加 method label column；单层 header，数值约两位小数。
- **Evidence relation**：§5.2 diversity baseline matrix；与 Figure 3 accuracy–diversity 条件散点、Table 10 跨模型扩展相连。p-less 相对稳定和 baseline 高温 spikes 由列方向读取。
- **Design strengths**：method rows/temperature columns 直接，适合检查高温 diversity spike。；compact table 与同页 Figure 3 构成 metric-to-frontier pair。
- **Design weaknesses**：caption 没有写 n-gram order、aggregation unit 或 Figure 3 的 accuracy filter。；没有 uncertainty，且 0.62–1.00 窄范围需结合 accuracy 才有决策意义。
- **Reusable pattern**：用 method×temperature matrix 作为散点图的可追溯底表，并在 caption 绑定 diversity definition、sample unit 和 selection rule。
- **Evidence**：p.9 Table 4，basis=rendered_observation。

### Table 5 — p. 23

- **Module / placement / width / purpose**：appendix_C.3 / appendix / page_width / main_comparison, reproduction, robustness。
- **Caption**：Table 5: Accuracy of LLama2-7b, Mistral-7b, and Llama3-70b across sampling methods and temperatures (τ ) for math & logical reasoning datasets. The best accuracy for each model, dataset, and τ is in bold and the second best is underlined.（39 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=4.8/5.2 pt，header weight=bold；21 rows × 21 columns，2 header levels，3 row groups，decimal precision=1。
- **Rules / highlighting**：partial_grid；bold, underline, best_second_best。
- **Uncertainty**：没有 uncertainty columns；Llama2 accuracy 跨 3 seeds 平均，Mistral/Llama3 为单 seed，seed 说明在表后 prose。
- **Data/statistics**：3 model row groups × 7 methods；四 dataset column groups，每组五温度；method 加 20 numerical columns。
- **Evidence relation**：C.3 完整 temperature-level accuracy surface；Table 1/AUC 和 Figures 2/9–11 从这里抽取聚合或曲线，正文高温结论依赖这些 cells。
- **Design strengths**：模型 row groups 与 dataset/temperature column groups 支持跨模型、跨任务、跨温度核查。；粗体/下划线逐 cell 指出 best/second-best，覆盖范围比主表完整。
- **Design weaknesses**：21×21 矩阵字号极小，模型/方法/温度三级关系需长距离追踪。；单 seed 和缺少 dispersion 让粗体容易显得比实际证据更确定。
- **Reusable pattern**：用 model×method 行组和 dataset×temperature 列组承载完整 accuracy surface，并把 seed/aggregation 置入 caption 或紧邻注释。
- **Evidence**：p.23 Table 5，basis=rendered_observation。

### Table 6 — p. 24

- **Module / placement / width / purpose**：appendix_C.4 / appendix / page_width / main_comparison, efficiency_cost, robustness。
- **Caption**：Table 6: Greedy decoding, beam search and p-less results for Mistral-7b on the 5 Math, Logical Reasoning and Creative Writing Datasets.（21 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.0/6.5 pt，header weight=bold；4 rows × 11 columns，2 header levels，0 row groups，decimal precision=1。
- **Rules / highlighting**：booktabs；none。
- **Uncertainty**：Mistral-7b 单一 τ=1.0 条件的 mean accuracy/diversity；未给 seed、spread 或 beam-search decoding cost。
- **Data/statistics**：四 decoding rows（beam bs=3/5、greedy、p-less）× 五 dataset groups；四组 Acc./Div. 与 WP 的 Win-rate/Div. 共 10 numeric columns，加 method column。
- **Evidence relation**：C.4.1 greedy/beam versatility check；将 p-less 与 search baselines 放在同一表，解释 GSM8K beam 例外和 WP win-rate 优势。
- **Design strengths**：Acc./Div. 子列把 quality 与 diversity 并置，五 dataset groups 适合横向检查。；表结构紧凑，search baseline 与 sampler 差异不需要额外图形。
- **Design weaknesses**：不同 decoding family 的计算成本没有呈现，且单模型/单温度限制弱化推广。；caption 未说明 mean 的 sample unit、temperature 或 beam scoring 设置。
- **Reusable pattern**：在同一 decoding row set 中用 paired Acc./Div. columns 对照 search 与 sampling，并在 caption 绑定固定温度和成本边界。
- **Evidence**：p.24 Table 6，basis=rendered_observation。

### Table 7 — p. 26

- **Module / placement / width / purpose**：appendix_C.5 / appendix / page_width / robustness, main_comparison。
- **Caption**：Table 7: Mean accuracy of DeepSeek-R1-Distill-Qwen-7B across sampling methods and temperatures (τ ) for math and logical reasoning datasets. The best accuracy is in bold and the second best is underlined.（31 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=4.8/5.2 pt，header weight=bold；7 rows × 21 columns，2 header levels，0 row groups，decimal precision=1。
- **Rules / highlighting**：partial_grid；bold, underline, best_second_best。
- **Uncertainty**：DeepSeek-R1-Distill-Qwen-7B 的 mean accuracy；没有 seed、dispersion 或 uncertainty columns。
- **Data/statistics**：七方法行 × 四 dataset groups × 五 temperatures，加 method column；dataset 是第一层 grouped header，τ 是第二层。
- **Evidence relation**：C.5 reasoning-model robustness ablation；把 p-less family high-temperature performance 与主三模型 Table 5 分开，验证方法不只依赖 Llama/Mistral/Llama3。
- **Design strengths**：在 reasoning-specialized model 上复用主表 temperature surface，结构易与 Table 5 对照。；best/second-best formatting 把 τ=2.0 强结果快速标出。
- **Design weaknesses**：只给 mean accuracy，caption 没有 seed 或 test-set denominator；“significantly superior”不能由此表 alone 支持。；21 columns 极密，行/列导航负担高。
- **Reusable pattern**：把 robustness model 作为同构的 method×dataset×temperature matrix，保持主表 header/formatting，并单列 replicate boundary。
- **Evidence**：p.26 Table 7，basis=rendered_observation。

### Table 8 — p. 26

- **Module / placement / width / purpose**：appendix_C.6 / appendix / page_width / ablation, main_comparison, reproduction。
- **Caption**：Table 8: Full results (accuracies and AUCs) of sampling methods and temperatures (τ ) for math and logical reasoning datasets for Llama-2-7b. The best accuracy or AUC is in bold and the second best is underlined.（36 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=4.2/4.8 pt，header weight=bold；22 rows × 25 columns，3 header levels，1 row groups，decimal precision=3。
- **Rules / highlighting**：partial_grid；bold, underline, best_second_best。
- **Uncertainty**：Llama-2-7b 各 baseline hyperparameter variant 的 accuracy 与 AUC point estimates；没有 seed、dispersion 或 interval columns。
- **Data/statistics**：22 hyperparameter rows：epsilon 4、eta 4、min-p 4、mirostat 4、top-p 4、p-less/p-lessnorm 2；每 dataset 五 temperatures + AUC，共 method/config + 24 numeric columns。
- **Evidence relation**：C.6 baseline hyperparameter sweep；检验 Table 1 默认设置是否给 p-less 不公平优势，并把各 variant 的 accuracy/AUC 与主表相连。
- **Design strengths**：temperature-level accuracy 与 AUC 放在同一三层 header，便于查 tuning 后的最优值。；粗体/下划线逐 cell 直示 baseline sweep 中的竞争结果。
- **Design weaknesses**：25 列、22 行且字号极小，是全 PDF 扫描成本最高的表之一。；hyperparameter 行名和 AUC 子列易错位；没有 sweep selection 或 multiple-comparison 说明。
- **Reusable pattern**：用 method+hyperparameter 行与 dataset×temperature×AUC 三层列头记录完整 sweep，并注明 selection、seed 和 multiplicity 边界。
- **Evidence**：p.26 Table 8，basis=rendered_observation。

### Table 9 — p. 27

- **Module / placement / width / purpose**：appendix_C.7 / appendix / page_width / ablation, robustness, main_comparison。
- **Caption**：Table 9: Mean accuracy of DeepSeek-R1-Distill-Qwen-7B across different k-order generalizations of the p-less sampling method and temperatures (τ ) for math and logical reasoning datasets.（25 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=5.8/6.2 pt，header weight=bold；20 rows × 8 columns，1 header levels，4 row groups，decimal precision=1。
- **Rules / highlighting**：booktabs；bold, underline, best_second_best。
- **Uncertainty**：DeepSeek-R1-Distill-Qwen-7B 的 mean accuracy；k-order 与 default p-less/p-lessnorm 每 cell 都无 uncertainty。
- **Data/statistics**：四 dataset row groups × 五 τ rows，共 20 data rows；列为 τ、五 generalized k-order、p-less、p-lessnorm，共 8 columns。
- **Evidence relation**：C.7 k-order ablation；按 dataset→temperature 展开离散 k grid，测试 default threshold 是否需要 tuning。
- **Design strengths**：dataset row groups 和 τ 行让同一任务内 k-order 横向对照清楚。；八列宽度适中，比 Table 8 更适合复核 generalized threshold。
- **Design weaknesses**：仅一个 reasoning model、离散 k grid，无法支持连续 k 或跨模型普适性。；caption 没报告 sample/seed，粗体 best 仍是无 uncertainty 的 pointwise winner。
- **Reusable pattern**：把 generalized parameter 放在列、temperature 放在行，保留默认方法作为 anchor，并显式报告 model/seed/grid 边界。
- **Evidence**：p.27 Table 9，basis=rendered_observation。

### Table 10 — p. 28

- **Module / placement / width / purpose**：appendix_C.8 / appendix / page_width / main_comparison, robustness, ablation。
- **Caption**：Table 10: Mean diversity values of sampling methods and temperatures (τ ) for math and logical reasoning datasets. The highest diversity for each model, dataset, and τ is in bold and the second highest is underlined.（36 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=4.5/5.0 pt，header weight=bold；21 rows × 21 columns，2 header levels，3 row groups，decimal precision=1。
- **Rules / highlighting**：partial_grid；bold, underline, best_second_best。
- **Uncertainty**：三模型跨四 dataset×五 temperature 的 mean diversity；无 dispersion、interval 或 n-gram detail columns。
- **Data/statistics**：3 model row groups × 7 methods × 20 dataset-temperature values；method 加 20 numeric columns，dataset/τ 为两层 grouped header。
- **Evidence relation**：C.8 complete diversity matrix；为正文 Figure 3 的 QASC conditional frontier 和 Table 4 主文 slice 提供跨模型/任务/温度底层 evidence。
- **Design strengths**：与 Table 5/12 同构的 model row groups 让 diversity、accuracy、length surfaces 可互相定位。；best/second-best formatting 使高温 diversity spike 一眼可见。
- **Design weaknesses**：21×21 小字号矩阵与 Table 5/12 重复高扫描负担；diversity scale 与 Table 4 的约 0.63/表内约 63 存在需解释的重标度问题。；均值无 dispersion，最高 diversity 不代表质量最优。
- **Reusable pattern**：将 diversity 与 accuracy/length 使用同一 dataset×temperature header，使 trade-off 矩阵可直接回溯到主文筛选图。
- **Evidence**：p.28 Table 10，basis=rendered_observation。

### Table 11 — p. 28

- **Module / placement / width / purpose**：appendix_C.8 / appendix / page_width / robustness, ablation, main_comparison。
- **Caption**：Table 11: Mean diversity values for min-p and p-less sampling methods over temperatures (τ ) 0.5 to 2.0, including τ = 2.5 and τ = 2.25 for p-less, using Mistral-7b.（30 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=5.8/6.2 pt，header weight=bold；10 rows × 9 columns，1 header levels，5 row groups，decimal precision=1。
- **Rules / highlighting**：booktabs；none。
- **Uncertainty**：Mistral-7b min-p/p-less mean diversity；τ=2.25/2.5 只对 p-less 延伸，未给 uncertainty 或 paired sample details。
- **Data/statistics**：五 dataset row groups，每组 min-p/p-less 两行；七 temperature columns（0.5,0.7,1.0,1.5,2.0,2.25,2.5）加 dataset/method columns。
- **Evidence relation**：C.8 high-temperature diversity extension；支撑正文“p-less 可通过略高 τ 追上 min-p diversity”的边界，而不宣称同温度等效。
- **Design strengths**：把 extended p-less temperatures 与 min-p baseline 放在每 dataset 内，trade-off 易定位。；列方向呈现 diversity 随 τ 的趋势，结构简洁。
- **Design weaknesses**：min-p 没有 2.25/2.5 对照，延伸实验不是 full factorial。；caption 没说明样本数、model seed 和 diversity normalization。
- **Reusable pattern**：在不平衡温度扩展表中明确哪些 cells 未测量，并把 baseline 与延伸方法按 dataset row group 配对。
- **Evidence**：p.28 Table 11，basis=rendered_observation。

### Table 12 — p. 29

- **Module / placement / width / purpose**：appendix_C.9 / appendix / page_width / efficiency_cost, main_comparison, robustness。
- **Caption**：Table 12: Mean generation length of sampling methods and temperatures (τ ) for math and logical reasoning datasets. The shortest generation length for each model, dataset, and τ is in bold and the second shortest is underlined.（37 words；moves = title, setup, encoding_key, comparison；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=4.5/5.0 pt，header weight=bold；21 rows × 21 columns，2 header levels，3 row groups，decimal precision=0。
- **Rules / highlighting**：partial_grid；bold, underline, best_second_best。
- **Uncertainty**：三模型×四 dataset×五 temperature 的 mean generation length；无 dispersion、停止规则或 maximum-new-tokens columns。
- **Data/statistics**：3 model row groups × 7 methods；四 dataset groups × 五 τ columns，共 20 numeric columns加 method column。
- **Evidence relation**：C.9 efficiency-by-length surface；与 Table 13 entropy/admission、Figures 16–17 profiling 和正文 §5.1 shorter-generation claim 相连。
- **Design strengths**：与 accuracy/diversity matrices 同构，支持逐 cell 检查“短而不一定低质”。；粗体/下划线把 shortest/second-shortest pattern 显式化。
- **Design weaknesses**：整数长度矩阵极密，caption 没有 generation stopping/max budget，跨方法可比性受限。；mean 没有 spread，容易把不同长度分布压成一个强结论。
- **Reusable pattern**：用 model×dataset×temperature grouped matrix 汇总 length，并锁定 stop rule、token budget、sample unit 与 uncertainty。
- **Evidence**：p.29 Table 12，basis=rendered_observation。

### Table 13 — p. 30

- **Module / placement / width / purpose**：appendix_C.10 / appendix / page_width / mechanism, efficiency_cost, robustness。
- **Caption**：Table 13: Mean Entropy and Admitted Token Count（8 words；moves = title, setup, encoding_key；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=5.8/6.2 pt，header weight=bold；3 rows × 11 columns，2 header levels，0 row groups，decimal precision=3。
- **Rules / highlighting**：booktabs；none。
- **Uncertainty**：Llama3-70b GPQA 的 mean entropy 与 mean admitted-token count，三 methods×五 temperatures；无 SD/SEM/interval。
- **Data/statistics**：method rows top-p/min-p/p-less；每 τ 有 Entropy/Tokens 两个 subcolumns，共 10 numeric columns。
- **Evidence relation**：C.10 central diagnostic summary；top-p high-τ token-count explosion 与 Figures 12–14 histogram distributions共同支撑 entropy-aware regularization 和 length interpretation。
- **Design strengths**：Entropy/Tokens paired subcolumns 让中间机制量与候选数同向比较。；五温度横向结构紧凑，极端 top-p values 很醒目。
- **Design weaknesses**：均值掩盖极端分布，caption 未定义 entropy estimator、step aggregation 或 sample denominator。；top-p counts 跨数量级，普通列宽下小数和单位需要仔细读。
- **Reusable pattern**：用 metric-pair subcolumns 将机制中间量与 outcome proxy 并置，并将均值表与分布图、原始 step aggregation 绑定。
- **Evidence**：p.30 Table 13，basis=rendered_observation。

### Table 14 — p. 30

- **Module / placement / width / purpose**：appendix_C.11 / appendix / single_column / efficiency_cost, ablation, robustness。
- **Caption**：Table 14: Pairwise t-test results (t-statistic, p-value). Significant results (p < 0.05) are highlighted in bold.（16 words；moves = title, setup, uncertainty_definition；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=5.5/6.0 pt，header weight=bold；6 rows × 6 columns，1 header levels，0 row groups，decimal precision=4。
- **Rules / highlighting**：partial_grid；bold, cell_color。
- **Uncertainty**：6×6 symmetric matrix 的 pairwise t-statistic 和 p-value；nominal p<0.05 cells bold，未说明 pairing/test unit、assumptions、multiplicity correction 或 interval。
- **Data/statistics**：六 methods（top-p、min-p、epsilon、eta、mirostat、p-less）作行列；对角线为 dash，每个 off-diagonal cell 含 t 与 p。
- **Evidence relation**：C.11 efficiency hypothesis-test matrix；从 Table 3 mean/SD/SEM 转向 pairwise significance，p-less 与 eta 的 p=0.0902 是正文 except-eta 例外来源。
- **Design strengths**：对称矩阵避免重复长表，显著 cell 的粗体直接暴露比较结构。；同页与 code/profiling figures 形成从实现到统计检验的 evidence bundle。
- **Design weaknesses**：nominal threshold 和多重比较缺口没有在表注解释，粗体容易被读成 confirmatory guarantee。；一个 cell 混合 t/p 两类数值，列名没有把二者拆开。
- **Reusable pattern**：用对称 matrix 展示 pairwise test，但把 test unit、pairing、multiplicity、effect estimate 与 p-value 分成明确 header/footnote。
- **Evidence**：p.30 Table 14，basis=rendered_observation。

### Table 15 — p. 33

- **Module / placement / width / purpose**：appendix_C.11 / appendix / single_column / efficiency_cost, main_comparison。
- **Caption**：Table 15: Comparison of sampling methods by CPU time and RAM usage.（12 words；moves = title, setup, uncertainty_definition；self-contained=False；main finding=False）。
- **Typography / shape**：Nimbus Roman No9 L, Computer Modern，body/header=6.2/6.7 pt，header weight=bold；3 rows × 3 columns，1 header levels，0 row groups，decimal precision=3。
- **Rules / highlighting**：booktabs；none。
- **Uncertainty**：三方法 CPU Time/RAM Usage 以 mean ± spread 给出，但 caption 没定义 ± 是 SD、SEM、范围还是 boxplot summary，也没有 hardware/sample denominator。
- **Data/statistics**：三 method rows × CPU Time (ms) 与 RAM Usage (GB) 两 numeric columns，加 Method column。
- **Evidence relation**：C.11 profiling summary，压缩 Figures 16–17 temporal distributions；p-less 的资源最低点与 Table 3 sampling-time mean 互补但不是同一单位。
- **Design strengths**：尺寸小、结构清晰，CPU 与 RAM paired columns 适合快速比较。；method row order 与 Figures 16/17 palette 形成 profiling bundle 索引。
- **Design weaknesses**：± 定义缺失是关键可解释性问题；没有 hardware、measurement window、n 或 outlier rule。；单一 mean±spread 会掩盖按 generation bin 的异质性。
- **Reusable pattern**：用 compact method×resource summary 作为 boxplot companion，并在 caption 明确定义 ±、测量窗口、硬件和样本聚合。
- **Evidence**：p.33 Table 15，basis=rendered_observation。

## Cross-object system

- **visual_narrative**：视觉叙事沿“阈值机制（Figure 1）→ AUC 总览与温度曲线（Table 1/Figure 2）→ writing、timing、diversity 与案例（Tables 2–4/Figures 3–4）→ synthetic threshold stress tests（Figures 5–8）→ 完整 accuracy、diversity、length matrices（Tables 5、7–12）→ entropy/admission diagnosis（Table 13/Figures 12–14）→ implementation/profiling（Figures 15–17/Table 15）→ selected failure patterns（Figures 18–19）”。主文先给 decision surface，appendix 负责覆盖、诊断和复现线索。
- **caption_system**：caption 统一以 Figure/Table label + 一句标题开头；主结果通常写模型、数据集、温度、AUC 或 best/second-best key，synthetic 与 appendix diagnostics 多只说明对象名称。caption 很少定义样本分母、seed、误差语义或筛选条件，Figure 3 的 accuracy filter、Figures 16–17 的 32-step binning 和 Table 15 的 ± 语义留在周围 prose。
- **table_header_system**：主表采用 booktabs/partial-grid 的 grouped headers：model→dataset→temperature 或 dataset→metric pair。Tables 1–4 是轻量单/双层 header；Tables 5、8、10、12 用大规模 model/method 与 dataset×temperature matrix；Tables 13–15 改用 metric-pair、symmetric matrix 和 resource columns。
- **method_result_ablation_link**：Figures 1/5–8 与 Eq. 2–4、Proposition 1 定义 threshold/admission mechanism；Tables 1/5/7–10 将 rule 放进 model×dataset×temperature accuracy/ablation surface；Tables 2–4、11–13 和 Figures 3–4、12–14/16–19 分别连接 writing quality、diversity、length、entropy/admission、efficiency 与 failure boundaries。Figure 15 是规则到代码的桥。
- **main_appendix_link**：Figure 1→Figures 5–8 是 synthetic geometry 扩展；Table 1/Figure 2→Table 5/Figures 9–11 是 AUC 到完整温度曲线；Table 4/Figure 3→Table 10/11 是 conditional frontier 到跨模型/高温 diversity；Table 3→Table 14/Figures 16–17/Table 15 是 mean timing 到 test/distribution/profile；Figure 4→Table 13/Figures 12–14/18–19 是单案例机制到总体诊断与 failure examples。
- **typography_consistency**：正文和 appendix 共享 Times/Nimbus Roman 风格的 caption、表格与数学字形，plot labels 多为 sans/Computer Modern 混合。表格字号从主文约 6–7 pt 降到完整矩阵约 4–5 pt；Figure 15 使用 monospace。模板风格一致，但 appendix 极小 headers 和多级表头显著增加可读性负担。
- **color_consistency**：七方法 categorical palette 在 Figures 2/3/9–11 中稳定；threshold plots 在 Figures 1/5–8 中稳定；entropy/failure traces 复用红 entropy、蓝 admitted tokens。Tables 依赖 bold/underline 而非颜色。主要缺口是 line charts 缺少颜色外的 method marker/line redundancy，synthetic threshold palette 的灰/洋红在灰度下较弱。

## Final judgment

### most_reusable_patterns
- 先用 Figure 1 的单一 mechanism schematic 建立 threshold/admission 语法，再用 Figures 5–8 做受控 distribution stress ladder。
- 以 Table 1 的 AUC 总览配 Figure 2/9–11 的温度曲线，形成 aggregate-to-trajectory 的主结果组合。
- 用 grouped matrix headers（model/dataset/temperature）承载完整 accuracy、diversity、length surfaces，并保持方法顺序一致。
- 用 Table 13 + Figures 12–14 将均值机制量与 entropy distribution 并置，再用 Figures 16–17 + Table 15 将 temporal profile 与 summary 互补。

### highest_value_objects
- Figure 1：最有效地把 p-less threshold 随温度/分布变化的核心机制变成可扫描的视觉对照。
- Table 1 + Figure 2：正文最短路径的跨模型总览与温度退化展开。
- Tables 5、8、10、12：覆盖完整 temperature/hyperparameter surface，虽然扫描成本很高。
- Table 13 + Figures 12–14：把 entropy、admitted-token count 和 distributional tail 连接为机制诊断。
- Figure 15 + Figures 16–17/Table 15：实现、资源分布和资源摘要组成可复核的 efficiency bundle。

### failure_patterns
- 大量 line charts 主要靠颜色区分七方法，灰度/色觉异常下缺少稳定 marker 或 line-style redundancy。
- appendix full matrices（尤其 Table 8、10、12）和 1000/10000-token threshold plots 过密，信息存在但不易逐对象核验。
- caption 经常省略 seed、sample unit、筛选条件和 uncertainty definition；Figure 3、Figures 16–17、Table 15 的关键解释要从周围 prose 补回。
- 单案例 traces（Figure 4、18、19）用黑圈把局部异常与文字事件对齐，但没有 prevalence 或 selection denominator，不能承担总体机制频率。
- 表内 bold/underline 和 nominal p<0.05 强化 winner 视觉，却没有同步呈现 multiplicity、effect size 或 uncertainty boundary。

**One-sentence visual strategy**：该论文采用“合成分布阈值图建立机制、AUC 表与温度曲线建立性能、分层矩阵扩展覆盖、entropy/admission 与 profiling/failure traces 补足解释”的单栏 ICLR 视觉系统，核心优点是方法语法跨对象复用，主要代价是 appendix 密度与不完整的统计/复现 caption。

## Validation record

- Markdown is written before JSON publication. JSON is schema-validated in memory and then atomically published with os.replace from /tmp/iclr-2026-ff40de6c7ac1.visual-audit.json.
- Target pair only: visual_audits/iclr-2026-ff40de6c7ac1.md and visual_audits/iclr-2026-ff40de6c7ac1.json.

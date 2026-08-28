# icml-2026-cca969cd8cab 视觉审计

## 审计边界与事实源

- **论文**：*Decoupling the "What" and "Where" With Polar Coordinate Positional Embedding*，Anand Gopalakrishnan、Robert Csordás、Jürgen Schmidhuber、Michael C. Mozer。
- **PDF 事实源**：`corpus/preprints/icml-2026-cca969cd8cab.pdf`。`readings/icml-2026-cca969cd8cab.json` 的 `visual_inventory` 仅作为起始清单；本轮以 PDF 逐页核对。PDF 共 18 个物理页，正文 p.1–8，Impact Statement p.9，References p.9–11，附录 A–D p.12–18；同一 PDF 未提供独立 supplementary 文件。
- **完整性核对**：对 PDF 全部 18 页执行 `pdftotext -layout` 逐页读取，并以 200 dpi（1700×2200 px/页）渲染。p.3–8、p.14–18 的含对象页面逐对象放大检查；p.1–2、p.9–13 的缩略页确认没有未登记的 Figure/Table。最终对象数为 7 幅 Figure、9 张 Table；与 PDF 标签和页码一致。
- **渲染性质**：`pdfimages -list` 显示 Figure 2（2400×1500）、Figure 3 的两行图（各 4800×2100）、Figures 4–5（各 4800×2100）、Figure 6（4766×2701）和 Figure 7（4767×3597）是嵌入栅格图；Figure 1 与表格主要是 PDF 矢量文字/线条。200 dpi 高于协议要求的 180 dpi。`pdffonts` 显示正文/表格以 Nimbus Roman No9 L、Computer Modern 和 Nimbus Mono L 为主，Figure 1 还包含 HelveticaNeue、STIX/CMU 字体对象；栅格图内字体不能由 PDF 字体表直接读取。
- **保留的版面不一致**：Figure 3 caption 末句写“124M and 253M”，但图面 (a)/(b) 均标为 124M，253M 对应的图在附录 Figures 4–5；Table 5 caption 写“the 124M Transformer model”，但表头同时有 124M、253M 两列。审计记录 PDF 原文，不替作者修正。

## 公共视觉源核查

- PDF p.3 脚注明确给出 `https://github.com/agopal42/pope`。只读检查该仓库的 metadata、README、递归 tree 和 commit 信息：仓库描述与 README 标题均直接对应本文，README 的 `assets/rope-vs-pope.png` 与 PDF Figure 1 的布局/内容一致。
- 公开仓库树包含 `assets/rope-vs-pope.png`、`plots.ipynb` 和 `freq_analysis.ipynb`。`plots.ipynb` 的 length-generalization cell 使用 matplotlib 的 8×5 inch、4 色、三种线型、方形 marker 和 300 dpi，与 Figure 2 的图例和曲线 grammar 对应；其另一个 cell 是不在 PDF 中的间接索引 bar plot，不能当作本文 Figure 1–7 的生成器。`freq_analysis.ipynb` 的聚合 cell 对 10 个 Shakespeare sonnets 的 query/key activation 求均值，绘图 cell 使用 `imshow`、`origin='lower'`、`aspect='auto'`、`interpolation='nearest'`、`cmap='viridis'`，并显式设置 title/axis/tick 字号，支持 Figures 3–5 的 grammar。
- `corpus/visual_sources/icml-2026-cca969cd8cab/agopal42__pope/` 的紧凑本地源目前只保存 `plots.ipynb`；`freq_analysis.ipynb`、README 和 Figure 1 asset 通过公开仓库只读核查，未把临时下载物写入本仓库。远程 notebook 的默认配置是 774M，且没有 Figures 3–5 的最终 PNG/数据 checkpoint，因此它精确支持绘图例程和参数，不能证明每一个 PDF 热图的数据文件。
- 递归 tree 没有 Figure 6–7 learned-bias 生成脚本、Table 1–3/5–9 生成器或论文 TeX；`model.py`/`position.py` 是实现文件而不是已核对的视觉源。`czhuang/JSB-Chorales-dataset` 是数据仓库，不是图表源。综合覆盖范围，`source_acquisition.status` 从自动 inventory 的 `exact_visual_source` 下调为 **`partial_visual_source`**：Figure 1 有匹配 asset，Figure 2 有对应 notebook，Figures 3–5 有参数化绘图例程，Figures 6–7 和大多数表格没有可核对的最终视觉源。

## PDF 对象清单

| 对象 | 物理页 | 模块 | 放置 | 宽度/结构 |
|---|---:|---|---|---|
| Figure 1 | 3 | method | main | page-width；RoPE/PoPE 两分支概念图 |
| Table 1 | 4 | results | main | single-column；2×2 |
| Table 2 | 4 | results | main | single-column；2×3 |
| Table 3 | 5 | results | main | single-column；2×2 |
| Table 4 | 5 | results | main | single-column；2×4 |
| Table 5 | 5 | ablation | main | single-column；4×3 |
| Table 6 | 6 | results | main | page-width；6×9、3 个模型规模组 |
| Figure 2 | 7 | results | main | page-width；单面板 12 条曲线 |
| Figure 3 | 8 | results | main | page-width；两行、四个热图面板 |
| Table 7 | 14 | experimental_design | appendix | page-width；7×6 |
| Table 8 | 15 | experimental_design | appendix | page-width；10×6 |
| Table 9 | 15 | ablation | appendix | inset；6×2 |
| Figure 4 | 16 | appendix | appendix | page-width；query/key 两个热图面板 |
| Figure 5 | 16 | appendix | appendix | page-width；query/key 两个热图面板 |
| Figure 6 | 17 | appendix | appendix | page-width；12 个 layer 面板（4×3） |
| Figure 7 | 18 | appendix | appendix | page-width；16 个 layer 面板（4×4） |

## 全文视觉系统

- **版式**：主文双栏；Figure 1、Figure 2、Figure 3 跨栏。附录 A–D 单栏，Table 7/8 横跨可用正文宽度，Table 9 为居中的窄表。Figures 4–7 的图内留白较多，仍以附录单栏的 page-width 视觉区块呈现；p.18 几乎只剩 Figure 7 和 caption。
- **字体**：正文与表格使用 Nimbus Roman No9 L regular/medium/italic，数学符号使用 Computer Modern 系列，少量链接/代码使用 Nimbus Mono L。表格和 caption 约 9–10 pt；Figure 1 内部混用 HelveticaNeue 与 STIX/CMU 数学字体；Figures 2–5 的 source notebook 字号为 title 16、axis 12–14、tick/legend 9–12 pt，栅格缩放后约 5–12 pt；Figures 6–7 的栅格文字约 5–13 pt。
- **颜色**：Figure 1 使用浅色 feature blocks 与橙/黑/绿/蓝的箭头和弧线；Figure 2 用 red/ orange/ green/ blue 表示 RoPE/YaRN/PoPE/PoPE+ft，点划/虚线/实线表示 124M/253M/774M；Figures 3–5 使用 viridis，每个 query/key 面板单独 colorbar；Figures 6–7 使用白到深蓝的 δ 顺序色阶。颜色没有跨对象的全局语义 token；Figure 2 有线型冗余，热图依赖连续亮度与 colorbar，表格主要依赖粗体和线条。
- **统计边界**：只有 Table 1 和 Table 9 显示 3-seed mean ± standard deviation；其他表和所有 Figure 都没有 error bar、band、区间或重复运行信息。Heatmap 及 learned-bias 图是均值/单 checkpoint 的描述性诊断，不能单独构成因果检验。

## Figure 1（p.3，main）

- **结构与类型**：`conceptual_diagram`、`pipeline`；page-width。左右两条并行分支（RoPE、PoPE），上方是 query 向量，中段各有 3 个 component 示例，下方各有 3 个旋转坐标小图；复杂度 4（两分支、多个步骤和数学标记）。PDF 主要由矢量线框、箭头和文字构成。
- **绘图语法与编码**：无坐标轴、网格、统计 legend 或不确定性。`direct_labels=true`；灰色 query/container 框、浅色 feature blocks、橙色输入箭头、黑色 magnitude 箭头、绿色初始 phase 弧、蓝色 rotation 弧共同编码过程；左/右 branch 是 facet-like 并行布局，不是共享 legend。
- **字体与颜色**：内部 PDF 字体对象包含 HelveticaNeue、STIXGeneral、CMUSerif 和 Nimbus Roman；估计约 4.7–14.4 pt，步骤标签为 sans-serif，公式/变量为数学斜体。约 8 个可见主色（浅色块、灰色容器、橙/黑/绿/蓝标记）；图形与箭头形状提供部分冗余，但灰度下颜色语义仍不完全保留。
- **Caption**：`Figure 1. Illustration compares how RoPE and PoPE encode relative positions via rotations of queries. Left: Three complex-valued RoPE components having magnitudes µqtc (black arrows) and initial phases ϕqtc (green arcs) are constructed from three pairs of embedding features (orange arrows) of the query vector qt (gray box) at sequence position t. These RoPE components are then rotated by angles tθc (blue arcs). Right: Three magnitude components µq̃tc (black arrows) of complex-valued PoPE components are constructed from three embedding features of the query vector qt (gray box) by applying softplus activation. These magnitudes (complex numbers with zero phases) are then rotated by angles tθc (blue arcs). PoPE uses twice the number of components than RoPE as it applies rotations to each component of the query vector qt.`（按自然语言 token 计 128 词）。动作：title、setup、encoding_key、comparison；无粗体结论标题，`self_contained=true`，`main_finding_stated=false`。
- **数据与证据关系**：这是 §2 的 RoPE 极坐标展开、Eq. (2) 的 phase interaction 与 §3 Eq. (3)–(6) 的 PoPE 方法接口。Figure 1 把“二维成对输入+初始 phase”与“逐元素 softplus magnitude+位置旋转”并置；Table 1 和 Appendix Table 9 检验该接口在 Indirect Indexing 上的结果。
- **设计评价**：优点是两分支共享 component 编号和阅读方向，读者可以直接比较 RoPE 的初始 phase 与 PoPE 的零 phase；缺点是图面只画 query，key 的对称作用需依赖 caption/公式，且“PoPE uses twice...”没有维度数字标记。**可复用模式**：将方法改动拆成“共同输入 → 并行转换 → 局部几何结果”，在分支间保持同一 component 骨架。

## Table 1（p.4，main）

- **结构与类型**：single-column，2 个数据行×2 列（`Positional Enc.`、`Indirect Idx.`），1 层表头、无 row group；三条水平规则和一条内部竖线，属于 `partial_grid`。两位小数；PoPE 数值粗体。表体约 9–10 pt，Nimbus Roman/Computer Modern math，PDF text object 可读。
- **表头/数据表达**：行是 RoPE/PoPE，列是 final-token accuracy；11.16 ± 2.45 与 94.82 ± 2.91。表头没有 `%` 或分母；`±` 的 standard deviation 由 caption 定义。
- **Caption**：`Table 1. Accuracy (with standard deviation) on the test split for the Indirect Indexing task.`（15 词）。动作：title、setup、uncertainty_definition；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：把 Figure 1 的 what/where 解耦接口接到 §4 最小诊断任务；正文 p.4 解释 RoPE 约 11%、PoPE 约 95%，Appendix Table 9 扩展替代位置编码。优点是两行配对、统一精度、粗体方向明确；缺点是没有原始 seed、分母或检验。**可复用模式**：机制诊断使用两行配对表，并在表注明确重复统计量和指标单位。

## Table 2（p.4，main）

- **结构与类型**：single-column，2×3（`Positional Enc.`、`JSB`、`MAESTRO`），1 层表头、无 row group；横向 booktabs-like 规则加内部竖线，`partial_grid`。JSB 4 位、MAESTRO 3 位小数；PoPE 两列粗体。
- **表头/数据表达**：列是两个音乐数据集，指标为 test-split best NLL（越低越好）；RoPE 为 0.5081/1.501，PoPE 为 0.4889/1.486。没有误差、箭头或分母。
- **Caption**：`Table 2. Best NLL on the test split for Transformer models with RoPE or PoPE positional encodings on music datasets (JSB and MAESTRO).`（23 词）。动作：title、setup、comparison；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：连接 §4 symbolic-music 设置与 PoPE/RoPE 主比较；Table 7/8 提供配置和训练条件。优点是 dataset-as-column、method-as-row 扫读快且黑白稳定；缺点是 `best` 的 checkpoint/选择规则、seed 和不确定性均未给出，小数精度跨列不一致。**可复用模式**：配对控制下使用“数据集列×方法行”结果表，并在 caption 定义 best 的选择单位。

## Table 3（p.5，main）

- **结构与类型**：single-column，2×2（`Positional Enc.`、`Human Ref. Genome`），1 层表头、无 row group；三位小数，横线和内部竖线组成 `partial_grid`；PoPE 的 4.152 粗体。
- **表头/数据表达**：test-split best NLL；RoPE 4.217、PoPE 4.152，未显示 uncertainty、颜色或方向箭头。
- **Caption**：`Table 3. Best NLL on the test split for the Human Reference Genome dataset.`（14 词）。动作：title、setup；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：将 Figure 1/Indirect Indexing 的机制主张扩展到 HRG；正文称 “significant drop”，但表只给单次 best NLL，没有统计依据。优点是差异紧凑且精度一致；缺点是缩写/指标方向依赖 caption，缺少 seed、分母和检验。**可复用模式**：单域配对表应同时给出 best 选择和重复统计定义，避免用显著性措辞代替证据。

## Table 4（p.5，main）

- **结构与类型**：single-column，2×4（`Positional Enc.`、`124M`、`253M`、`774M`），1 层表头、无 row group；两位小数，横线和内部竖线组成 `partial_grid`；PoPE 全行粗体。
- **表头/数据表达**：OpenWebText validation perplexity（越低越好），模型规模为列；RoPE 21.55/18.88/15.85，PoPE 21.33/18.55/15.45。无误差、seed 或规模趋势线。
- **Caption**：`Table 4. Perplexity on the validation split of OpenWebText for Transformer models with RoPE or PoPE positional encodings.`（18 词）。动作：title、setup、comparison；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：这是“同 architecture/training parameters、只改变 positional encoding”的跨规模主证据；Figure 2 使用对应 OWT 模型做 PG-19 外推，Figures 3–7 展开频率/δ 诊断。优点是三种规模横向并置、方向统一；缺点是 checkpoint/评估时点和重复统计未说明，公开 notebook cell 7 把 774M 写成 772M，不能当作完整表生成器。**可复用模式**：把规模作为列、方法作为行，并同时保留原始重复结果。

## Table 5（p.5，main）

- **结构与类型**：single-column，4×3（`Positional Encoding`、`124M`、`253M`），1 层表头、无 row group；两位小数，横线和内部竖线组成 `partial_grid`；Full PoPE 两列粗体。
- **表头/数据表达**：四行是 `PoPE without σ()`、`PoPE with ReLU for σ()`、`PoPE without δ`、`Full PoPE`；值分别为 21.57/18.93、21.55/18.90、21.42/18.57、21.33/18.55。指标为 OpenWebText validation perplexity。caption 只写 124M，但表中有 253M 列。
- **Caption**：`Table 5. Validation set perplexity scores for the 124M Transformer model with ablated versions of PoPE pretrained on OpenWebText.`（19 词）。动作：title、setup、comparison；无粗体标题，`self_contained=false`（模型范围与表头矛盾），`main_finding_stated=false`。
- **证据关系与评价**：把 Eq. (3) softplus 与 Eq. (6) learnable δ 接到组件消融，Table 4 是完整 RoPE/PoPE 参照。优点是变体→完整方法顺序清楚；缺点是 caption/正文没有解释 253M 列，且没有 seed/误差，点差稳定性不可判定。**可复用模式**：消融表可保留多规模，但 caption 必须与所有模型列一致。

## Table 6（p.6，main）

- **结构与类型**：page-width，6 个数据行×9 列（model size、position encoding、六个任务、Avg），1 层表头、3 个 row group（124M/253M/774M）；两位小数，外框横线与内部竖线组成 `partial_grid`。每个规模组内按列粗体，表头用 `↑`。
- **表头/数据表达**：六项为 LAMBADA、Blimp、CBT、HellaSwag、PIQA、ARC-E，及算术平均 `Avg. ↑`，均为 accuracy。124M Avg 45.33→46.19，253M 48.76→48.78，774M 51.80→52.46；个别任务在前两种规模回退。
- **Caption**：`Table 6. Zero-shot performance on downstream tasks using Transformer models pretrained on OpenWebText with RoPE or PoPE positional encoding.`（19 词）。动作：title、setup、comparison；无粗体标题，`self_contained=false`（未展开任务含义、分母和平均规则），`main_finding_stated=false`。
- **证据关系与评价**：这是 OWT 预训练模型到六个 zero-shot task 的结果接口，与 Table 4 的训练 perplexity、Figure 2 的外推结果互补。优点是规模×方法×任务×平均值在同一面；缺点是 Avg 掩盖任务异质性，253M 仅高 0.02，未给 seed/不确定性。**可复用模式**：保留任务级列和汇总列，并在 caption 明确平均规则，不让平均值替代任务级证据。

## Figure 2（p.7，main）

- **结构与类型**：`line`；page-width，单面板 12 条曲线（4 方法×3 规模），每条 10 个长度点，复杂度 4。嵌入 raster PNG 2400×1500。
- **绘图语法与编码**：x/y 均 linear；x 为 inference-time sequence length，y 为 perplexity，二者均有 dotted grid。图例位于绘图区左上，12 项；颜色是 RoPE red、YaRN orange/yellow、PoPE green、PoPE+ft blue；`: / -- / -` 表示 124M/253M/774M；方形 marker（1 种）；无 direct label、hatching、reference line、error bar 或 band。source cell 6 没显式设置 line width，按 matplotlib 默认值估计约 1.5 pt；明确设置 marker size 5、title 16、axis 12、legend 9、300 dpi。
- **Caption**：`Figure 2. Length extrapolation at test-time on PG-19 dataset for different model sizes. We evaluate baselines that use RoPE (red) or YaRN (yellow) against PoPE (green) which does not apply any fine-tuning or interpolation techniques and PoPE+ft (blue) which only uses fine-tuning. Sequences at test-time are multiples of 1024 up to 10240.`（53 词）。动作：title、setup、encoding_key、comparison；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **数据与证据关系**：PG-19 test split、长度 1024 的倍数至 10240；RoPE、YaRN、PoPE、PoPE+ft 的三种规模曲线。正文说明 YaRN 与 PoPE+ft 在 4096 上 fine-tune 500 steps，PoPE 为 zero-shot；曲线把 Table 4 的 OWT 模型连接到长度外推主张。无完整数值表、seed 或误差。
- **设计评价**：优点是颜色×线型二维编码同时表达方法和规模，曲线退化趋势直观，caption 说明测试长度与 fine-tuning 语义；缺点是 12 项图例密集并可能覆盖曲线，方法识别依赖颜色，且 fine-tuned 与 zero-shot 条件不对称。**可复用模式**：长序列外推用方法颜色×模型规模线型，但应同时提供可下载的 length/value 表和重复统计。

## Figure 3（p.8，main）

- **结构与类型**：`heatmap`、`matrix`；page-width，四面板按两行两列排列：上排 RoPE query/key、下排 PoPE query/key；复杂度 5。嵌入两张 4800×2100 栅格行图；每面板独立 viridis colorbar。
- **绘图语法与编码**：`imshow`、`origin='lower'`、`aspect='auto'`、`interpolation='nearest'`；x 为 1–12 的 categorical layer，y 为离散 frequency/component（仅标 High/Low Frequencies），无网格、marker、line、hatching、reference line 或 uncertainty。query/key 是 panel title；colorbar 是本地 legend，未共享。source notebook cell 12 设置 title 16、axis 14、tick 12、serif family。
- **Caption**：`(a) 2-norm plotted over 2D RoPE ‘chunks’ of queries (left) and keys (right) in each layer of the 124M Transformer over different RoPE frequencies. Mean over 10 different Shakespeare sonnets and 12 attention heads at each layer. (b) Magnitude of each complex-valued features of queries (left) and keys (right) in each layer of the 124M Transformer over different PoPE frequencies. Mean over 10 different Shakespeare sonnets and 12 attention heads at each layer. Figure 3. Frequency usage analysis for 124M and 253M models pretrained on OpenWebText from Table 4.`（89 词）。动作：title、setup、encoding_key、comparison；无粗体标题，`self_contained=false`，`main_finding_stated=false`。
- **数据与证据关系**：每面板是 10 个 Shakespeare sonnets、每层 12 个 heads 的均值；RoPE 为约 32 行、PoPE 为约 64 行。正文 p.6/8 将其用于描述 RoPE 的稀疏频率与 PoPE 的更分散/高频使用，Figures 4–5 是 253M 扩展。四个 colorbar 的范围不同，颜色不能直接给跨 panel 的绝对比较。
- **设计评价**：优点是 query/key 横向配对、RoPE/PoPE 纵向对应、layer 轴完整；缺点是 y 轴没有具体频率编号，caption 把 124M 图与 253M 范围合并，且没有误差或数值导出。**可复用模式**：固定 query/key 面板骨架对照表示使用模式，并统一跨模型 color scale 或提供长表。

## Table 7（p.14，appendix）

- **结构与类型**：page-width，7 个数据行×6 列（`Hyperparameter`、`Indirect Idx.`、`OpenWebText`、`JSB`、`MAESTRO`、`HRG`），1 层表头、无 row group；mixed integer/decimal/text precision；顶/表头/底线与内部竖线组成 `partial_grid`，无粗体或颜色。
- **表头/数据表达**：OpenWebText 用 slash-separated triples：embedding 768/1024/1280、heads 12/16/20、layers 12/16/36、δ init 0/0/0、dropout 0.0/0.0/0.0；其余行还列出 RMSNorm、base wavelength 10,000 等。表格约 10–12 pt，表头较大，PDF text object。
- **Caption**：`Table 7. Transformer model configurations for the different datasets. For the OpenWebText language modeling dataset we train 3 model sizes 124M/253M/774M and the hyperparams for each of these model sizes as a triple in column 2.`（38 词）。动作：title、setup、encoding_key；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：Appendix B.2 的复现接口，连接正文“identical architecture/training hyperparameters”与 Tables 2–6。优点是跨域/跨规模配置集中；缺点是 triple 与单一数据集值处于同一视觉层级，读者需回 caption 解码，且没有硬件、seed、runtime。**可复用模式**：用“超参数×数据集”宽表，并在 caption 约束 slash-separated 多规模值的顺序。

## Table 8（p.15，appendix）

- **结构与类型**：page-width，10 个数据行×6 列，1 层表头、无 row group；数字、科学记数法和整数混排；顶/表头/底线与内部竖线组成 `partial_grid`，无高亮。
- **表头/数据表达**：列为 Indirect Idx./OpenWebText/JSB/MAESTRO/HRG，行是 batch size、sequence length、learning rate、min learning rate、weight decay、grad clipping、β₂、max/decay iters、warmup iters；`2e-4`、`6e-4`、`100,000` 等保留实现级格式，无 uncertainty。
- **Caption**：`Table 8. Hyperparameter configurations for training on different datasets. For OpenWebText dataset we train Transformer models at sizes 124M/253M/774M using identical hyperparameters.`（24 词）。动作：title、setup、encoding_key；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：Appendix B.3 展开 Tables 1–6 的优化条件，支持 Table 4 配对训练和 Figure 2 的 4096 fine-tuning 背景。优点是 architecture 与 optimization 配置分表，列方向固定；缺点是不同量纲相邻但没有单位列，500-step length fine-tune 特例不在表中，未提供硬件/runtime。**可复用模式**：将模型配置与训练配置分成相邻附录表，并在 caption 说明跨规模共享项。

## Table 9（p.15，appendix）

- **结构与类型**：inset，6×2（`Positional Enc.`、`Indirect Idx.`），1 层表头、无 row group；两位小数，横线与内部竖线组成 `partial_grid`；PoPE 94.82 ± 2.91 粗体，其余无高亮。
- **表头/数据表达**：行是 RoPE、RoPE half-channels、ALiBi half-heads、Learnable、Sinusoidal、PoPE；值为 11.16 ± 2.45、28.50 ± 6.10、27.35 ± 10.77、10.08 ± 0.19、1.90 ± 0.04、94.82 ± 2.91。指标为 test-split accuracy；caption 说明 standard deviation，表头不写百分号或 seed 数。
- **Caption**：`Table 9. Accuracy (with standard deviation) on the test split for the Indirect Indexing task.`（15 词）。动作：title、setup、uncertainty_definition；无粗体标题，`self_contained=true`，`main_finding_stated=false`。
- **证据关系与评价**：Appendix C 把 Table 1 的二元对照扩展为替代编码 landscape，检验 half-channel/half-head 是否仍保留 interaction。优点是与 Table 1 保持相同精度和不确定性格式；缺点是没有原始 seed，half-channels/half-heads 的含义需回 Appendix C 正文，窄表没有方向箭头。**可复用模式**：将完整 baseline landscape 放在附录，同时保持主表的指标和重复统计格式。

## Figure 4（p.16，appendix）

- **结构与类型**：`heatmap`、`matrix`；page-width，query/key 两个并排面板，复杂度 4。每面板 16 layers×32 2D RoPE-frequency rows，独立 viridis colorbar；嵌入 4800×2100 栅格图。
- **绘图语法与编码**：同 Figure 3 的 `imshow` grammar；x 为 categorical layer 1–16，y 为离散 frequency，左侧只给 High/Low Frequencies 文字；无网格、marker、line、hatching、reference line 或 uncertainty；query/key 为 panel title，colorbar 不共享。source `freq_analysis.ipynb` cell 12 给出 title 16、axis 14、tick 12、serif。
- **Caption**：`Figure 4. 2-norm plotted over 2D RoPE components of queries (left) and keys (right) in each layer of the 253M Transformer over different RoPE frequencies. Mean over 10 different Shakespeare sonnets and 16 attention heads at each layer.`（38 词）。动作：title、setup、encoding_key；无粗体标题，`self_contained=false`，`main_finding_stated=false`。
- **数据与证据关系**：10 个 sonnets、每层 16 heads 均值；这是 Figure 3a 的 253M scale extension，用于 Appendix D 的“RoPE 稀疏且不使用最高频率”描述，并与 Figure 5 成对。query/key colorbar 范围不同，不能用颜色直接做绝对值比较；没有误差或最终数据文件。**可复用模式**：固定 query/key 热图 grammar 做模型规模扩展，但应统一色阶并提供具体频率索引。

## Figure 5（p.16，appendix）

- **结构与类型**：`heatmap`、`matrix`；page-width，query/key 两个并排面板，复杂度 4；16 layers×64 PoPE frequency/component rows，独立 viridis colorbar，嵌入 4800×2100 栅格图。
- **绘图语法与编码**：同 Figure 4；x 为 categorical layer 1–16，y 为离散 PoPE component/frequency，panel title 为 query/key，颜色表示 Mean norm；无网格、marker、line、hatching、reference line 或 uncertainty。
- **Caption**：`Figure 5. Magnitude of each complex-valued features of queries (left) and keys (right) in each layer of the 253M Transformer over different PoPE frequencies. Mean over 10 different Shakespeare sonnets and 16 attention heads at each layer.`（37 词）。动作：title、setup、encoding_key；无粗体标题，`self_contained=false`，`main_finding_stated=false`。
- **数据与证据关系**：10 个 sonnets、每层 16 heads 均值；与 Figure 4 对照，支持 PoPE 使用更宽频率范围、尤其是高频 component 的描述性解释；Figure 3b 是 124M 对应图。query 与 key colorbar 独立，未给误差或频率数值表。**可复用模式**：对照图保持同一 panel geometry，并明确区分模式比较和绝对强度比较。

## Figure 6（p.17，appendix）

- **结构与类型**：`heatmap`、`matrix`；page-width，12 个 layer 小面板、4×3 排列，复杂度 5；每面板 x 为 attention head index 0–11，y 为 query/key component index 0–约 64，右侧有独立 δ colorbar。嵌入 4766×2701 栅格图。
- **绘图语法与编码**：稀疏的离散 head×component 色块/水平 marks 位于每个矩阵面板，颜色表示 learned bias δ；无内部网格、marker、line、hatching、reference line 或 uncertainty；`Layer 1`–`Layer 12` 是 direct panel labels，12 个 colorbar 均未共享。x/y 视为 categorical index scale；图内文字约 5–13 pt，无法从 PDF 对象得出内部源字号。
- **Caption**：`Figure 6. Visualization of the learned biases for the 124M pretrained PoPE model across all layers.`（16 词）。动作：title、setup；无粗体标题，`self_contained=false`，`main_finding_stated=false`。
- **数据与证据关系**：Appendix D p.17 上方文字说明 δ 从零初始化、限制在 −2π 到 0，高频 component 更易偏离而低频保持接近零；Figure 6 将该观察展开到 124M 的 layer×head×component。它补充 Eq. (6)、Table 5 消融和 Figure 7 scale contrast，但没有数值导出、seed 或 aggregation 说明。**设计评价**：规则网格便于定位层/头/组件，但重复 colorbar 与稀疏浅色 marks 使跨层绝对比较困难，caption 缺少轴、范围和 checkpoint 定义。**可复用模式**：参数诊断用固定 layer grid，同时发布长表和统一色阶。

## Figure 7（p.18，appendix）

- **结构与类型**：`heatmap`、`matrix`；page-width，16 个 layer 小面板、4×4 排列，复杂度 5；每面板 x 为 attention head index 0–15，y 为 query/key component index 0–约 64，独立 δ colorbar。嵌入 4767×3597 栅格图。
- **绘图语法与编码**：与 Figure 6 相同，`Layer 1`–`Layer 16` direct label；每面板白到深蓝顺序色表示 δ，零值接近白、负偏移更深；无内部网格、marker、line、hatching、reference line 或 uncertainty。x/y 是离散 index，16 个 colorbar 不共享；图内文字约 5–13 pt。
- **Caption**：`Figure 7. Visualization of the learned biases for the 253M pretrained PoPE model across all layers.`（16 词）。动作：title、setup；无粗体标题，`self_contained=false`，`main_finding_stated=false`。
- **数据与证据关系**：这是 Figure 6 的 253M 扩展，对应 Table 4 的 OWT 253M checkpoint；与 Appendix D 文字的高频 δ 偏离观察一致。它没有误差、checkpoint 选择规则或数值导出，p.18 也几乎没有额外解释。**设计评价**：4×4 规则布局保留跨层结构，但图内字号、稀疏色块和重复 colorbar 造成高密度，颜色深浅不能跨面板直接比较。**可复用模式**：同一 layer-grid grammar 做规模对照，并用共享色阶/长表承载可复核数值。

## 跨对象证据系统

- **视觉叙事**：Figure 1 先把 Eq. (2)/(5) 的 what–where interaction 与 PoPE softplus/relative rotation 变成方法接口；Tables 1–3 给出 Indirect Indexing、音乐和 HRG 的配对结果；Table 4 沿规模给出 OWT perplexity，Table 5 做组件消融，Table 6 接到 zero-shot downstream；Figure 2 展示 PG-19 长度外推，Figure 3 回收 124M 的 frequency usage，Figures 4–7 在附录扩展到 253M 和 learned δ。
- **Caption 系统**：Figure 1/2 caption 的 setup 与编码最完整；Tables 1–4、6、9 说明 split/指标但通常不写主发现；Table 5 的模型范围与表头矛盾；Figure 3 的 124M/253M 范围错位；Figures 6–7 caption 过短，初始化、δ 范围和轴语义留在相邻正文。
- **表头系统**：结果表稳定使用“position encoding × dataset/model size/task”矩阵，以粗体表达较低 NLL/Perplexity 或较高 accuracy；Table 6 增加 `↑` 和模型规模 row groups。附录 Table 7/8 采用“hyperparameter×dataset”，用 slash-separated triples 压缩 OWT 多规模配置，Table 9 复用 Table 1 的两列 baseline 结构。
- **方法—结果—消融链**：Eq. (2)/(5) → Figure 1 方法接口 → Table 1/Appendix Table 9 机制诊断 → Tables 2–4 跨域/跨规模比较 → Table 5 组件消融 → Table 6 下游 → Figure 2 长度外推 → Figures 3–7 频率/δ 描述性诊断。热图没有独立统计检验，Table 3 的 “significant” 也没有对应检验信息。
- **正文—附录链**：正文 p.3–8 承担 Figure 1、Tables 1–6、Figure 2–3；附录 p.14–18 承担 Tables 7–9 和 Figures 4–7。正文显式调用 Section B/C 和 Table 4，但没有逐图回指 Figures 4–7；附录补足配置、替代 baseline 和 scale diagnostics，却未补足共享 seed/误差契约。
- **字体与颜色一致性**：Nimbus Roman/Computer Modern 与 `partial_grid` 表格结构稳定；Figure 1 是嵌入式 sans/math 矢量图，Figure 2–5 是 notebook 栅格图，Figures 6–7 是未知生成源的栅格图，形成明显但可读的字体断层。颜色按对象局部定义：Figure 2 方法色、Figures 3–5 viridis、Figures 6–7 δ 蓝色，表格依赖黑体而非颜色；不存在跨图的统一绝对色阶。

## 最终判断

- **最可复用范式**：用 Figure 1 的“共同输入 → 并行转换 → 局部几何结果”定义方法接口；用 Tables 1/9 的最小诊断与 baseline landscape 固定机制对照；用 Tables 4–6 的“规模×方法×任务”矩阵承载主结果；用 Figure 2 的颜色×线型二维编码展示长度外推；用 Figures 3–7 的固定 query/key 或 layer-grid grammar 展开表示诊断。
- **最高价值对象**：Figure 1 是 what/where 解耦的视觉入口；Table 1/9 是最直接的机制诊断与替代基线；Table 4/6 是跨规模性能和下游主证据；Figure 2 是最强的外推趋势对象；Figures 3–5 对理解频率使用最有价值，但仍是描述性表示诊断。
- **主要失败模式**：除 Tables 1/9 外，结果表和所有 Figure 缺少重复、不确定性或误差表达；Table 3 用 “significant drop” 但没有统计方法；Table 5 caption 与 253M 列不一致；Figure 3 caption 与图面模型范围不一致；Figure 2 图例密集且无完整数值表；Figures 3–7 使用独立 colorbar，learned-bias 图没有公开最终生成源或数值导出。
- **一句话视觉策略**：论文先用并行几何示意定义 PoPE 的 what/where 解耦，再用配对表格、规模/任务矩阵和长度曲线展示收益，最后用频率与 learned-bias 栅格把机制诊断扩展到附录，但不确定性、统一色阶和最终视觉源仍不完整。

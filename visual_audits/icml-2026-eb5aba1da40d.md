# Visual audit — `icml-2026-eb5aba1da40d`

## 审计范围与 PDF 事实源

- **论文**：John Cooper、Ilias Diakonikolas、Mingchen Ma、Frederic Sala，*Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models*。
- **唯一审计对象**：`paper_id=icml-2026-eb5aba1da40d`。本文件只描述该 paper 的视觉对象。
- **PDF 事实源**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/preprints/icml-2026-eb5aba1da40d.pdf`。`pdfinfo` 报告 29 个 Letter 物理页、612 × 792 pt、PDF 1.7、未加密；作者和标题与 reading 一致。
- **逐页渲染**：使用 `pdftoppm -r 200 -png` 渲染 p. 1–29，生成的页面为 1700 × 2200 px，文件内分辨率为 199.9996 dpi，满足至少 180 dpi。29 页全部逐页检查；含对象的 p. 2、5、6、8–12、16、25–29 另作高分辨率检查，所有参考文献页和证明页也检查了文字流与留白。
- **PDF 对象清单**：16 幅 Figure、2 张 Table。正文 Figure 1–8、Table 1；附录 Figure 9–16、Table 2。p. 12 同时包含 Figure 8、Conclusion 结尾和 References 开头；References 占 p. 12–14；附录占 p. 15–29。
- **版面纠正**：reading 的页级说明多次写作「双栏」，但 PDF 渲染和 `pdftotext -bbox-layout` 显示正文、参考文献、附录均为单一文本栏（例如 p. 8 的主要文本行约为 x=72–542 pt）。本审计按 PDF 观察记录为单栏；不修改 reading 文件。
- **reading 对齐**：`readings/icml-2026-eb5aba1da40d.json` 的 `visual_inventory` 与 PDF 的 18 个编号对象、标签和页码一致；`reports/tables/visual_inventory_disagreements.csv` 对该 paper 记录 `reading=18`、`pdf=18`、差异为 0。reading 对 F5/F7 的比较字段较泛，PDF 图例实际显示 3 条曲线，以下以 PDF 为准。

### PDF 对象索引

| 标签 | 物理页 | 模块 | PDF 中的视觉对象 | 宽度判断 |
|---|---:|---|---|---|
| Figure 1 | 2 | introduction | 篮球问答/函数组合概念插图，嵌入 RGB 栅格 1536 × 1024 | `single_column`，居中 |
| Figure 2 | 5 | method | `x → SSM(u,v) → TF(F)` 架构流程图，矢量路径与文字 | `single_column`，居中 |
| Figure 3 | 6 | method | Selective Copy 的 SSM 记忆与相对查找架构图，矢量路径与文字 | `single_column`，居中 |
| Figure 4 | 8 | results | 参数量—准确率折线、分位带与图内数表 | `single_column` |
| Figure 5 | 9 | results | 三层 Associative Recall with Decoding 参数量—准确率折线 | `single_column` |
| Figure 6 | 10 | results | MKAR 参数量—准确率折线与图内数表 | `single_column` |
| Figure 7 | 11 | results | Needle in a Haystack 参数量—准确率折线 | `single_column` |
| Table 1 | 11 | results | OOD bit-proportion 点准确率表 | `single_column` |
| Figure 8 | 12 | results | Evaluation length—character accuracy 折线 | `single_column` |
| Table 2 | 16 | appendix B | `Symbol / Meaning` 符号表 | `single_column` |
| Figure 9 | 25 | appendix D.5 | Selective Copy Input/Output 双热图 | `page_width`，两 panel |
| Figure 10 | 26 | appendix D.5 | Associative Recall with Decoding Input/Output 双热图 | `page_width`，两 panel |
| Figure 11 | 27 | appendix E.2 | vocab=200/1000 的双参数量图 | `page_width`，两 panel |
| Figure 12 | 27 | appendix E.2 | number of heads/state dimension 双消融图 | `page_width`，两 panel |
| Figure 13 | 28 | appendix E.2 | adversarial distribution 参数量—最终准确率图 | `single_column` |
| Figure 14 | 28 | appendix E.2 | Selective Copy window-size 图 | `single_column` |
| Figure 15 | 29 | appendix E.2 | MKAR window-size 图 | `single_column` |
| Figure 16 | 29 | appendix E.2 | MKAR heads/state dimension 双消融图 | `page_width`，两 panel |

`pdfimages -list` 进一步确认：Figure 1 是 1536 × 1024 栅格；Figure 4–8、11–12、14–16 使用 1200 × 800 RGB 图像嵌入（带灰度 soft mask）；Figure 13 使用 600 × 400 RGB 图像；Figure 9–10 的热图由每个 panel 的 indexed raster image 组成；Figure 2–3 没有对应的嵌入图像对象，主要为 PDF 矢量路径和文字。

## 公开视觉源获取

自动行 `reports/tables/visual_source_inventory.csv` 将该 paper 标为 `no_public_source_found`，并只列出 `corpus/preprint_text/icml-2026-eb5aba1da40d.txt`；`corpus/visual_sources/icml-2026-eb5aba1da40d/` 没有本地文件。随后按协议核对 PDF、reading 中的 arXiv/OpenReview 链接，并使用 `unicli search`、`agent-reach doctor --json`、`gh auth status`、GitHub API 和递归 tree：

- arXiv 结构化查询 `unicli arxiv paper 2603.08859` 返回标题、作者和 `https://arxiv.org/abs/2603.08859`，与 PDF 一致。`unicli scholar code 2603.08859` 返回 `SCHOLAR_RESOURCE_NOT_FOUND`；OpenReview 查询因过期认证 token 失败，因此没有把未验证的 OpenReview 结果当作源码证据。
- GitHub 搜索得到最可信的作者/项目仓库：`https://github.com/SprocketLab/hybrid-expressivity`。README 明确写着该仓库包含 associated paper 的全部实验；递归 tree 含 `micro_hf`、`micro`、`mini`、`constructions`、结果图和 notebook。读取的 `main` revision 为 `7beeb0de80f89eb9b36ca999`（2026-03-29）。
- 可复用的实验绘图源为 `micro_hf/process.ipynb`、`micro_hf/plt_utils.py`、`micro/process.ipynb`、`micro/plt_utils.py` 和 `mini/process.ipynb`。这些文件给出 `matplotlib` 的 figsize、网格、线宽、命名颜色、`fill_between` 以及均值/分位数或 min/max 聚合。Figure 4–7、11–12、14–16 的 task/result 路径与 notebook 输出名对应；Figure 5、Figure 6、Figure 15、Figure 16 的 PDF 嵌入 RGB 像素与当前仓库同名 PNG 做了逐像素 RGB 核对，完全匹配。其他图的当前仓库结果可能因 notebook 后续 cell 覆盖同名文件而与预印本当时的导出版本不同，故只将路径和绘图机制视为源证据，不把当前数值文件无条件当作 PDF 的唯一版本。
- Figure 9–10 的 construction notebook 和四个作者仓库 PDF 资产直接对应标题与输出：`constructions/construction_var_copy.ipynb` 写出 `selective_copy_input.pdf`/`selective_copy_output.pdf`，`constructions/construction_decode_recall.ipynb` 写出 `decode_recall_input.pdf`/`decode_recall_output.pdf`。这些是可编辑/可追溯的 construction visualization source。
- `https://github.com/MachineLearning-Nerd/icml26-hybrid-sequence-models` 是独立 reproduction audit；其 README 明确说不是作者官方实现。它被记录为候选但没有用于归因本文视觉源。
- Figure 1 的篮球概念插图、Figure 2–3 的纸面架构图和论文 TeX 未在上述作者仓库 tree 中找到；没有把 PDF 的嵌入图像伪装成可编辑源码。

因此 JSON 的源状态为 **`partial_visual_source`**：作者仓库为结果图、热图和 construction visualization 提供了可核对的部分源文件，但未提供 Figure 1–3 的完整原始图/TeX，也没有本地 source inventory 缓存。

## 全文视觉风格

- **版式**：PDF 是单栏 article。Figure 1–8 与 Table 1 主要占单栏内的居中区域；Figure 9、10、11、12、16 使用双 panel 横向组合，延伸至页面文本宽度。F4/F6 的图内数表与折线共用一个 Figure，不另计 Table。
- **字体**：页面正文、caption 和表格主要使用 Computer Modern Roman/Italic/Bold；`pdffonts` 还报告 Times-Roman、SFRM1000 和 DejaVu Sans Type3。Matplotlib 栅格图中的标题、坐标、图例主要是 DejaVu Sans。图内字号按渲染约 6–12 pt，正文 caption 约 9–10 pt；正文数学使用 Computer Modern math。
- **颜色**：结果图以四个命名类别色固定表示 architecture：blue `#0000FF`、orange `#FFA500`、red `#FF0000`、green `#008000`；`micro_hf/plt_utils.py` 明确维护 `TF-TF`、`TF-SSM`、`SSM-TF`、`SSM-SSM` 以及三层变体的颜色映射。Figure 8 的 `hybrid`/`T_rope`/`mamba` 同样为 green/blue/red。Figure 9–10 使用离散的 viridis-like 三色，约为 dark purple `#440154`、cyan/teal `#21918C`、yellow `#FDE725`，caption 明确对应 -1/0/1。
- **不确定性**：结果 PNG 使用同色半透明 `fill_between`。主文 E.1 写明 11 runs、均值及 10th/90th percentiles；Figure 8 的公开 `mini/process.ipynb` 使用每个长度的均值以及 min/max 带，PDF caption 未说明这一点。Table 1 和 Table 2 没有区间或重复统计。
- **矢量/栅格**：F2–F3 的箭头、框、文字和数学说明是矢量；F1、所有 Matplotlib 曲线、Figure 9–10 热图为嵌入栅格；caption、正文和表格线条仍是 PDF 矢量。图像导出实际为 PNG/PDF 后嵌入，导致图内标题和小刻度的最终字号小于源 notebook rcParams 的字号。
- **一致性与代价**：相同任务族使用同一套 blue/orange/red/green 语义、虚线 reference line 和同色不确定性带，便于跨 Figure 4、6、11–16 比较。代价是颜色承担了几乎全部 architecture 识别，线型/marker 没有作为冗余编码；灰度打印和色觉缺陷环境下的可区分性有限。许多 caption 把不确定性定义留给 Appendix E.1，脱离正文时不完全自足。

## Figure 1 — 函数组合任务的引言概念图

- **位置与职责**：p. 2，Introduction 页首，居中单栏栅格图。类型为 `conceptual_diagram`、`pipeline`、`qualitative_grid`；复杂度 **3/5**（单画布但含 notebook、人物、模型、云朵、箭头和多个答案节点）。用途为 `headline`、`theory_mechanism`、`qualitative_evidence`。
- **面板与阅读方向**：从左下问题气泡和左侧 Basketball Update 记事本开始，进入中部 NLP Model 的 question interpretation，再分出 `Learn Precise Question` 与 `Learn Key Info` 两个云朵；下方另画 Function Composition，再经 `Extract Key Info` 到右侧答案。机器人与两个 answer 气泡把抽象问题映射回示例结论。没有坐标轴、legend 或 panel labels。
- **绘图语法与编码**：栅格插图用人物、记事本、圆角框和箭头编码输入—解释—抽取—答案的有序流程；绿色/橙色/蓝色/青色区域分别强调 question interpretation、key information、function composition 和 answer 流。图中没有数值数据、marker、reference line 或不确定性。
- **字体与颜色**：PDF 事实为嵌入 RGB image 1536 × 1024，图内约 7–12 pt 的衬线/无衬线混合字形，颜色约 `#6AA84F`、`#F6B26B`、`#3D85C6`、`#76A5AF`、`#FFF2CC`、`#434343`；这些为渲染估计，灰度安全性低于文字/位置编码。
- **Caption（PDF 逐字提取，22 个空白分词）**：
  > Figure 1: Example function composition task. The answer to a learned question only depends on a part of the long context input.

  Caption 只有 title、setup 和一句机制结论，没有粗体 headline、颜色 key、缩写或不确定性定义；`self_contained=false`、`main_finding_stated=true`。脱离图内标签时不能恢复两个分支的具体语义。
- **数据与统计**：无实验数据或聚合；这是把长上下文与局部可寻址片段放入同一示例的定性证据。它不应被解释为 performance result。
- **证据关系**：Introduction 的 `function-composition` 主张 → Figure 1 把 `u/v/F` 的抽象分解转成问题、key info 和局部答案 → Figure 2 给通用 `SSM→TF` 接口 → Figure 3 给 Selective Copy 实例 → Figures 4–8 和 Table 1 验证 learned models。
- **优点**：用一个具体篮球例子降低抽象函数组合的进入门槛；箭头、answer bubble 和中部模型使读者可沿单向流程理解。
- **不足**：栅格图内文字在单栏中偏小，颜色没有形状/线型冗余；caption 没有说明各颜色或两个答案节点的关系，也没有把局部片段与后续任务形式化符号显式对应。
- **可复用模式**：在理论论文引言中以一个真实语义例子画出「长上下文抽取 → 局部寻址 → 函数组合 → 答案」；定量版本应在 caption 中补充每个通道的语义和评测单位。

## Figure 2 — 通用 Hybrid 接口

- **位置与职责**：p. 5，Section 4 前置架构图，居中单栏矢量图。类型为 `architecture`、`pipeline`、`conceptual_diagram`；复杂度 **3/5**。用途为 `method_interface`、`theory_mechanism`、`experimental_design`。
- **面板与阅读方向**：上方 `x` token strip 中以淡紫背景框出输入、以浅橙框出 `u` 区段；全部 token 进入灰色 `SSM, u(x) and v(x)`。SSM 输出两行 `u` 与 `v`，其中最后控制 token 为紫色；两行进入灰色 `TF`，最后输出 token 以红色表示完整任务结果。箭头从上至下，单一阅读方向。
- **绘图语法与编码**：没有 x/y 轴、legend、网格或统计 marks。位置和箭头编码信息流，灰色框编码模块，淡橙/紫/红分别编码截断内容、控制参数和最终输出；`u`/`v` 文字提供颜色之外的语义锚点。线型为实线箭头，无 hatching、reference line 或不确定性。
- **字体与颜色**：矢量文字主要为 Computer Modern/数学斜体，渲染约 8–12 pt；颜色约 `#C9D0FF`、`#FCE1C5`、`#D9D9D9`、`#A64AC9`、`#FF6666`、`#000000`，均为 rendered estimate。图内没有公开可编辑 diagram file。
- **Caption（PDF 逐字提取，52 个空白分词）**：
  > Figure 2: The construction’s style follows taking an input x and implementing 2 functions u, v with an SSM. Typically, u is a truncation of the input, and v is a control parameter (represented in purple). Lastly, a Transformer combines these by implementing F to perform the complete task (represented in red).

  Caption 有 title、setup、encoding key 和 comparison/interface 说明；没有粗体 headline 或实验数值，`self_contained=true`、`main_finding_stated=false`。
- **数据与统计**：这是 `x → (u,v) → F` 的接口示意，无样本、参数或不确定性统计。
- **证据关系**：Theorems 3.3/3.7 对纯模型资源瓶颈的理论预告 → Section 4 的 `SSM_u/SSM_v` 合并与 TF 读出公式 → Figure 2 作为方法接口 → Figure 3 的 Selective Copy 具体实例和 Figure 4–6 的 learned comparison。
- **优点**：`u`、`v` 和最终 `F` 的责任边界同时由位置、颜色和文字表达；图下 caption 解释紫色/红色语义，适合承接公式。
- **不足**：只展示抽象 token 流，不标出 state size、window 或层数/参数量；颜色仍是主通道，灰度下截断区和控制区难以区分；无公开原始 diagram source。
- **可复用模式**：把长上下文编码器和局部组合器拆成同构的上下游框，并用一个控制 token 和一个输出 token 标出接口；应在旁边补充资源边界和符号映射。

## Figure 3 — Selective Copy 的机制图

- **位置与职责**：p. 6，Hybrid Model for Selective Copying 开头，居中单栏矢量图。类型为 `architecture`、`pipeline`、`conceptual_diagram`；复杂度 **3/5**。用途为 `method_interface`、`theory_mechanism`、`experimental_design`。
- **面板与阅读方向**：顶端输入序列含多个彩色 token 和灰色 number token `4/3/1`；SSM 下方的 `u` 行保留当前内容，`v` 行在多列输出 number token/相对距离；TF 再把这些行转换为底端目标 token。彩色 token、数字和箭头共同表示最新 number token 及 relative lookup。
- **绘图语法与编码**：无轴、legend、网格或不确定性。横向位置表示 sequence position，纵向层次表示 input→SSM→TF；绿色/橙色/蓝色/红色块和灰色 number box 表示内容类别、控制位置和输出，向下箭头表示层间传递。线型和 marker 不承担统计语义。
- **字体与颜色**：Computer Modern 数学字形与简洁模块字体，约 8–12 pt；颜色约 `#00FF00`、`#FFA500`、`#0000FF`、`#FF0000`、`#D9D9D9`、`#000000`，为 rendered estimate。作者仓库没有该 paper 图的 diagram source。
- **Caption（PDF 逐字提取，49 个空白分词）**：
  > Figure 3: The construction solving selective copy takes an input sequence and finds the most recent number token (as represented in the bottom squares of the output of the SSM). The Transformer can then use these to look back some relative distance to find the correct token to output.

  Caption 有 title、setup、encoding key 和机制结论；没有粗体 headline 或不确定性，`self_contained=true`、`main_finding_stated=true`。
- **数据与统计**：无聚合结果；图示的是 Theorem 4.3 的构造接口，SSM 输出的 number token/距离和 TF 的目标 token 不是实验样本统计。
- **证据关系**：Theorem 4.2 的 Selective Copy 纯模型下界 → Theorem 4.3 的 Mamba+attention 构造 → Figure 3 解释“存最新 number、按相对距离回看” → Figure 4 学习实验和 Figure 9 的构造 embedding/output。
- **优点**：比 Figure 2 更具体地把 number token、相对位置和最终 copy 对齐，能解释为什么 SSM-first 顺序有意义。
- **不足**：数字块、颜色块和箭头密度较高，未标注固定 window/N/L；没有把图示 token 与 Definition 4.1 的符号逐一列出。
- **可复用模式**：对“先提取控制 token，再用 attention 读回内容”的构造，用上下两层 token strip 显示状态摘要和局部检索；应附上窗口和位置索引，减少读者从颜色推断。

## Figure 4 — Selective Copy 参数效率

- **位置与职责**：p. 8，Section 5.2 页首，单栏图像，折线下方嵌入 4 行值表。类型为 `line`、`area`、`table` 不在 Figure 类型枚举中，JSON 以 `line`、`area` 表示带状图；复杂度 **3/5**。用途为 `headline`、`main_comparison`、`efficiency_cost`。
- **面板与绘图语法**：一个 panel，标题为 `Average Accuracies across Parameter Counts`。x=`Parameter count`，线性；y=`Accuracy`，线性且约 0–1；双向浅灰虚线网格。四条实线为 TF-TF 蓝、TF-SSM 橙、SSM-SSM 红、SSM-TF 绿，图例在右下，色相同的半透明带位于曲线周围；无 marker、hatching 或 reference line。下方小表列 `Parameters / Pure TF / Pure SSM / TF→SSM / SSM→TF`，行约 1000、2000、6000、12000。
- **源精确样式**：`micro_hf/process.ipynb` cell 1 将 figure 设为 `(12,8)`、title 30、axis label 24、tick 20、font 22、line width 4、marker size 10、grid dashed width 1；`micro_hf/plt_utils.py` 用 `plt.plot` 和 `fill_between(..., alpha=0.08)`，颜色字典明确四类。PDF 端这些源字号经缩放后约为标题 10–11 pt、轴/legend 7–9 pt、线宽约 1–1.5 pt，故 typography/grammar provenance 为 mixed。
- **数据与统计**：PDF 图内表给出点值：约 1000 为 `.056/.084/.100/.087`，约 2000 为 `.352/.305/.433/.999`，约 6000 为 `.727/.485/.822/1.000`，约 12000 为 `.923/.931/.908/1.000`（列顺序见表头）。正文 E.1 说明 11 runs，以均值和 10th/90th percentiles 形成误差带；图内值表本身没有分散度列。
- **Caption（PDF 逐字提取，41 个空白分词）**：
  > Figure 4: Results from training small models on Selective Copy, across an increase in the hidden dimension of the models. At 2000 parameters, hybrid models consistently attain perfect accuracy. The pure models, with 6x the parameters, only attain around 0.9 accuracy.

  Caption 有 title、setup、comparison 和 main finding，但不解释颜色、带宽、11 runs 或 valid-token denominator；`self_contained=false`、`main_finding_stated=true`。
- **证据关系**：Introduction 的资源分离主张 → Theorems 4.2/4.3 与 Figure 3 → Figure 4 把 SSM-first 顺序映射为 learned parameter frontier → Figure 11–14 检查 vocabulary、head/state、adversarial distribution 和 window 边界 → Conclusion 的“larger pure baseline”总结。
- **优点**：曲线与嵌入值表同屏，读者可以同时看趋势和四个锚点；统一 y 轴让 SSM-first 与 pure/reverse hybrid 的比较路径短。
- **不足**：图例遮住右下带状区域，颜色缺少线型/符号冗余；caption 把误差定义留给 E.1；`6x` 是参数效率叙述而不是图内显式阈值标记，读者需返回正文核对比较口径。
- **可复用模式**：用一张参数 frontier 配合少量精确值表表达 efficiency claim；应在同一 caption 中说明聚合、分位带和模型顺序。

## Figure 5 — Associative Recall with Decoding

- **位置与职责**：p. 9，三层模型结果，单栏图像。类型为 `line`、`area`；复杂度 **2/5**。用途为 `main_comparison`、`headline`、`efficiency_cost`。
- **面板与绘图语法**：一个 panel，标题 `Average Accuracy across Parameter Counts`；x 为线性 parameter count，右端约 `1.4e7`；y 为线性 accuracy，约 0.1–0.65；双向浅灰虚线网格。PDF 图例只有三条线：TF-TF-TF 蓝、SSM-SSM-SSM 红、SSM-SSM-TF 绿；实线与同色半透明带，图例靠下方中央/右侧，无 marker、hatching 或 reference line。
- **数据与统计**：三层设置、参数规模接近 1 million；正文与 caption 的主事实为 Hybrid 到 0.5，而测试尺度内 pure models 不超过 0.4。E.1 的 11-run mean/p10/p90 规则适用于该带；图自身未写带宽定义或每个点的样本数。
- **Caption（PDF 逐字提取，48 个空白分词）**：
  > Figure 5: Results from training small models on Associative Recall with Decoding. Even at much smaller scales than the pure models, the hybrid is the only architecture that attains 0.5 accuracy. At the scales tested, none of the pure models performed the task with more than 0.4 accuracy.

  Caption 有 title、setup、comparison 和 main finding，但未定义三层图例、带和训练/评估分母；`self_contained=false`、`main_finding_stated=true`。
- **证据关系**：Theorem 4.5/4.6 与三层 construction → Figure 5 的 learned Associative Recall separation → Appendix E.1 的三层与 sweep 条件 → Figure 6 的 MKAR 扩展。PDF 图例的 3 条曲线优先于 reading 的泛化比较字段。
- **优点**：y 轴范围放大了 0.1–0.6 的 learnability 分离；caption 直接给出 0.5/0.4 两个判别值。
- **不足**：缺少 fourth/reverse three-layer variant 的明确说明；科学记数法的 x 轴在小图中难读；带状不确定性和 11-run 只在附录解释。
- **可复用模式**：对“只有某一层顺序在小规模达到目标”的结果，用三层同色语义和放大的 y 轴呈现；caption 应列出所有实际图例项及带宽定义。

## Figure 6 — MKAR 参数效率

- **位置与职责**：p. 10，单栏折线与嵌入值表。类型为 `line`、`area`；复杂度 **3/5**。用途为 `headline`、`main_comparison`、`efficiency_cost`。
- **面板与绘图语法**：一个 panel，标题 `Average Accuracies across Parameter Counts`；x/y 均线性，y 约 0–1。TF-TF 蓝、TF-SSM 橙、SSM-SSM 红、SSM-TF 绿；图例在左中/下方，四条实线配同色半透明带，双向虚线网格，无 marker/hatching/reference line。图下表为 `Parameters / Pure TF / Pure SSM / TF→SSM / SSM→TF`，四行约 1000、2000、6000、12000。
- **数据与统计**：图内表给出 `.124/.158/.131/.144`、`.159/.173/.183/.512`、`.230/.356/.286/.990`、`.668/.517/.524/.989` 四行；正文将 60% accuracy 的 6× 参数效率作为 learned-model 结果。曲线带依 E.1 为 11 runs 的 mean/p10/p90；嵌入表没有不确定性。
- **Caption（PDF 逐字提取，53 个空白分词）**：
  > Figure 6: Results from training small models on Multi-Key Associative Recall, across an increase in the hidden dimension. The hybrid consistently outperforms the pure models of the same depth and similar parameter counts. The hybrid models could perform the task to 60% accuracy with 6× fewer parameters than any of the pure Transformers.

  Caption 有 title、setup、comparison 和 main finding，但没有定义带状范围、11 runs 或四种线的颜色；`self_contained=false`、`main_finding_stated=true`。
- **证据关系**：MKAR Definition 5.1 与 function-composition 的空 `v` 特例 → Figure 6 测量 SSM-first hybrid、pure TF/SSM、reverse hybrid 的 parameter frontier → Figure 7/NH 与 E.2 window/head/state 消融 → Conclusion 的 learned hybrid 总结。
- **优点**：数表让 6× 叙述有可复核锚点；同一图同时展示 pure/hybrid 走势和具体参数点，证据密度高。
- **不足**：不同架构的参数轴终点不完全一致；6× 的阈值/选点没有图内参考线；图例和带状范围重叠，读者需结合正文理解“same depth and similar parameter counts”。
- **可复用模式**：对参数效率主张同时保留 frontier 曲线和少量精确行表；若声称“× fewer”，应在图中画等性能水平线或直接标出比较点。

## Figure 7 — Needle in a Haystack

- **位置与职责**：p. 11，Table 1 上方，单栏图像。类型为 `line`、`area`；复杂度 **2/5**。用途为 `main_comparison`、`robustness`、`failure`。
- **面板与绘图语法**：一个 panel，标题 `Average Accuracies across Param Counts`；x 为线性 parameter count，约 1,000–22,000；y 为线性 accuracy 0–1；TF-TF 蓝、SSM-SSM 红、SSM-TF 绿三条实线及半透明带，双向虚线网格，图例在右下，无 marker、hatching 或 reference line。PDF 图例是 3 条曲线，reading 的四架构描述不代表图中实际系列数。
- **数据与统计**：无 context windowing；图示 SSM 和 SSM-first hybrid 在较小参数量已接近 1，TF-TF 在小维度区间较低。E.1 的 11-run mean/p10/p90 规则适用于该曲线，caption 没有重复或带宽定义。
- **Caption（PDF 逐字提取，63 个空白分词）**：
  > Figure 7: Results from training small models on Needle in a Haystack, across an increase in the hidden dimension of the models with no context windowing. The hybrid and SSM perform this task with fewer parameters than the Transformer, however we still see the hybrid with a slight improvement. This task was expected to be hard for the Transformer and not the SSM.

  Caption 有 title、setup、comparison、main finding 和预期难度，但缺少具体数值、3 条图例和不确定性定义；`self_contained=false`、`main_finding_stated=true`。
- **证据关系**：NH Definition 5.2 的 marker-copy 任务 → 正文对 full-context/no-window 的设置 → Figure 7 作为 function-composition 之外的扩展比较 → 正文承认其 separation mechanism 未被理论直接刻画，并由 E.2 继续讨论 learnability。
- **优点**：caption 主动写出 no windowing 与理论预期，且曲线清楚显示 SSM/Hybrid 与 TF 的量级差异。
- **不足**：作者明确说机制未被 function-composition 解释，但图没有辅助诊断；绿色/红色/蓝色只有颜色区分；y=1 附近带状区域和图例挤压。
- **可复用模式**：把理论未覆盖的扩展任务单独放入结果图，并在 caption 直写适用边界；同时应增加 task-specific failure/diagnostic panel。

## Table 1 — OOD bit-proportion accuracy

- **位置与结构**：p. 11，Figure 7 下方，居中单栏表。用途为 `robustness`、`main_comparison`。表头一层，4 列：`Train Proportion`、`SSM`、`TF`、`Hybrid`；6 个数据行：0.05、0.1、0.3、0.5、0.8、0.9；无 row group。横线为 top/header/bottom，第一列后有一条竖分隔线，属于 `partial_grid`；没有 uncertainty 列。
- **表头与高亮**：caption 才给出 test bit proportion=0.2 和任务名；每行最高值加粗：0.05 行 TF/Hybrid 同为 0.47，0.1 为 Hybrid 0.47，0.3/0.5/0.8 为 Hybrid，0.9 为 SSM 0.86。没有 underline、cell color、arrow 或第二名标记。
- **数据与统计**：6×3 为 evaluation accuracy 点值：`.24/.47/.47`、`.34/.40/.47`、`.17/.64/.74`、`.46/.63/.77`、`.67/.63/.83`、`.86/.61/.80`。小数位混用 1–2 位（0.1、0.3 等行）；没有 run count、SD/SE、区间、失败值或样本分母。
- **Caption（PDF 逐字提取，46 个空白分词）**：
  > Table 1: Results from training 12-layer models with different proportions of bits for Associative Recall with Decoding. Data are evaluation accuracies for evaluation bit proportions of 0.2. Each architecture tends to improve performance as the training bit proportion increases, with hybrids consistently out-performing the pure models.

  Caption 有 title、setup、条件、comparison 和主趋势；`self_contained=true`、`main_finding_stated=true`，但没有解释加粗规则和精确重复数。
- **证据关系**：OOD Generalization 的 train/test distribution shift → Table 1 把六个训练比例和固定 test=0.2 放在同一决策面 → p. 11 正文的“almost all distributions”限定 → Conclusion 的 robustness 总结。Figure 8 负责 length generalization，二者是互补泛化轴。
- **优点**：行顺序直接表达训练分布变化，加粗让逐行 winner 易扫读；test condition 在 caption 中明确，避免把训练比例误读为评估比例。
- **不足**：指标名、单位和分母没有进入表头；点值无不确定性，无法判断 0.47 tie 或 0.03 差距的稳定性；加粗规则没有 caption 说明。
- **可复用模式**：对分布外实验使用“训练分布作行、模型作列”的短表，并在 caption 写固定测试条件；应增加样本/重复和波动列。

## Figure 8 — Length generalization

- **位置与职责**：p. 12 顶部，Conclusion 前的单栏图像。类型为 `line`、`area`；复杂度 **2/5**。用途为 `headline`、`robustness`、`main_comparison`。
- **面板与绘图语法**：一个 panel，标题 `Character Accuracy vs Evaluation Length`；x=`Evaluation Length` 线性，约 10–190；y=`Character Accuracy` 线性，约 0.1–1.0；hybrid 绿、T_rope 蓝、mamba 红三条实线，半透明带，双向虚线网格，legend 右上，无 marker/hatching/reference line。图是 PNG 栅格嵌入。
- **源精确样式与统计**：`mini/process.ipynb` 使用 `colors={'T_rope':'blue','hybrid':'green','mamba':'red'}`，按长度画均值，并以 `fill_between` 的 `mins`/`maxs`、alpha=0.2 表示范围，标题和轴标签与 PDF 相同；这与 E.1 对 F4–F7 的 10/90 规则不同。PDF caption 没有说明 min/max 带，故以公开源和 PDF 分开记录。
- **Caption（PDF 逐字提取，27 个空白分词）**：
  > Figure 8: The distribution of accuracies across different input sequence lengths. Hybrid models with comparatively similar parameters as their attention/Transformer counterparts perform better at longer lengths consistently.

  Caption 有 title、x 轴对象、comparison 和 main finding，但未说明训练长度 20–50、模型配置或带宽；`self_contained=false`、`main_finding_stated=true`。
- **数据与统计**：纵轴为 character accuracy，横轴为 evaluation length；正文给出的解释是短长度差距约 2% 随长度扩大到约 10%。没有显式检验、样本数或分母。
- **证据关系**：Section 5.3 的短序列训练/长序列测试设置 → Figure 8 的 Hybrid/T_rope/Mamba trajectories → Conclusion 的 stronger length generalization → 与 Table 1 的 OOD robustness 并列。
- **优点**：长序列范围直接可见，hybrid 与 Transformer 的缓慢下降趋势易读；颜色与结果图系统一致。
- **不足**：caption 未给 training-length range 和 band 统计口径；不同模型的参数匹配只在正文解释，图内无法判断；红色 mamba 很快贴近低值，后段差异被 y 轴压缩。
- **可复用模式**：用 evaluation-length 横轴直接测试外推曲线，并保持 matched-parameter baseline；caption 应同时写训练区间、聚合方式和不确定性。

## Table 2 — Notation glossary

- **位置与结构**：p. 16，Appendix B 顶部，单栏居中表。用途为 `method_interface`、`theory_mechanism`、`reproduction`。2 列、1 层表头（`Symbol`、`Meaning`）、13 个数据行、无 row group；横向 top/mid/bottom 规则、无竖线，属于 `minimal`。没有 bold/underline/cell color 或不确定性。
- **行内容**：依次列 `ϕ, ψ, Φ`—Token and Positional Embeddings；`u, v`—Control parameters of the task；`F`—The target task；`H`—(Relative) Entropy；`I`—Mutual Information；`Wq, Wk, Wv, Wo`—Transformer parameters；`WA, WB, WC, Δ`—SSM parameters；`x`—The input sequence；`V`—Vocabulary space；`N,M`—Number/Vocabulary components of V；`Y`—Target space, typically V^n；`d`—The token dimension；`ds`—The state dimension。
- **Typography**：body 约 8–9 pt、header 约 9–10 pt，Computer Modern Roman/数学字形，regular；符号使用数学字体，PDF object provenance 高。
- **Caption（PDF 逐字提取，3 个空白分词）**：
  > Table 2: Notation.

  只有 title move，没有 setup、encoding key 或 main finding；`self_contained=true`（表头和单元格足够解释词条）、`main_finding_stated=false`。
- **数据与统计**：无数值实验数据；它是后续 attention、SSM、Mamba 定义和证明的符号索引。
- **证据关系**：正文 p. 2 将完整 preliminaries 指向 Section B → Table 2 固定 `u/v/F`、参数矩阵和维度符号 → 支撑 Figures 2–3 的方法接口、Theorems 4.2–4.6 的证明和 Figure 9–10 的 construction 复现。
- **优点**：两列、横线极简，数学符号与含义紧邻；附录入口低成本，适合在证明页反查。
- **不足**：13 行仍需与正文交叉阅读，caption 不说明覆盖范围；`N,M` 和 `V^n` 的任务依赖关系在表格内没有展开。
- **可复用模式**：将贯穿全文的符号集中为 `Symbol / Meaning` 表，并用数学字形保持公式一致；若面向复现，可再加“首次出现页”列。

## Figure 9 — Selective Copy construction heatmaps

- **位置与职责**：p. 25，Appendix D.5，两个热图横向排列，延伸至页面文本宽度。类型为 `heatmap`、`matrix`；复杂度 **3/5**（两个高密度矩阵 panel）。用途为 `theory_mechanism`、`qualitative_evidence`、`reproduction`。
- **面板与绘图语法**：左 panel 标题 `Selective Copy Input`，右 panel 标题 `Selective Copy Output`；x 轴为 0–100 sequence/column position，y 轴为 0–40 embedding/state row，数值轴线性；无 legend/colorbar、网格或误差。暗紫、青色、黄色的离散块显示 -1、0、1；两个 panel 共享任务/色义但各有坐标刻度。
- **源精确样式**：`constructions/construction_var_copy.ipynb` 以 `m = model.embedding(x) + model.pos_emb`、`plt.imshow(...); plt.title(...)`、`plt.tight_layout()` 输出 `fig/selective_copy_input.pdf` 和 `fig/selective_copy_output.pdf`；作者仓库 tree 同名 PDF 可直接读取。PDF 嵌入的 indexed image 约 568 × 239 px/panel，最终观察为 raster。
- **Caption（PDF 逐字提取，38 个空白分词）**：
  > Figure 9: An example of the input/embedding and the output for selective copy. The aspects of the construction are kept in relatively similar positions in the implementation. Dark purple is -1, cyan is 0, and yellow is 1.

  Caption 有 title、setup、comparison（input/output）、encoding key 和 implementation 语境；`self_contained=true`、`main_finding_stated=false`。
- **数据与统计**：是一个构造实例的 embedding/output 矩阵，不是跨样本聚合；颜色对应离散值 -1/0/1，没有不确定性、分母或性能统计。
- **证据关系**：Theorem 4.3 的 Selective Copy 构造 → D.5 实现 → Figure 9 让输入、embedding、输出布局可视化 → Figure 3 的机制图和 Figure 4 的 learned comparison；它补充可复现性而非 headline accuracy。
- **优点**：input/output 并排且保留相同 row/column 位置，颜色 key 写在 caption，适合核对构造是否真的写入状态。
- **不足**：没有 colorbar、矩阵行语义和具体 token legend；热图中大面积 0 色块降低局部结构的可见度；单一实例不能证明对所有输入成立。
- **可复用模式**：对离散构造并排画 input/embedding 与 output，用同一坐标和离散色义；应补充 row 名称、实例参数和一个可验证的 output check。

## Figure 10 — Associative Recall with Decoding construction heatmaps

- **位置与职责**：p. 26，Appendix D.5，两个热图横向排列，页面文本宽度。类型为 `heatmap`、`matrix`；复杂度 **3/5**。用途为 `theory_mechanism`、`qualitative_evidence`、`reproduction`。
- **面板与绘图语法**：左为 `Associative Recall with Decoding Input`，右为 `Associative Recall with Decoding Output`；x 轴 0–100，y 轴 0–50，均线性；无 grid、legend/colorbar 或 uncertainty；暗紫/青/黄离散编码 -1/0/1。比 Figure 9 多出 bit-decoding 和 recall 的结构行，仍使用同一读图方向。
- **源精确样式**：`constructions/construction_decode_recall.ipynb` 用 `model.embedding(x) + model.pos_emb`、`imshow`、`tight_layout` 输出 `fig/decode_recall_input.pdf` 和 `fig/decode_recall_output.pdf`；作者仓库 tree 具有同名资产。
- **Caption（PDF 逐字提取，40 个空白分词）**：
  > Figure 10: An example of the input/embedding and the output for associative recall with decoding. The aspects of the construction are kept in relatively similar positions in the implementation. Dark purple is -1, cyan is 0, and yellow is 1.

  Caption 有 title、setup、input/output comparison 和 encoding key；`self_contained=true`、`main_finding_stated=false`。
- **数据与统计**：单个 100-column construction matrix；没有性能均值、重复、不确定性或 success rate。图面只能支持结构/实现关系。
- **证据关系**：Theorem 4.6 的三层 associative-recall construction → D.5 → Figure 10 显示每个位置的 decoded/output state → Figure 5 的 learned three-layer result；与 Figure 9 组成两个 prototypical construction 的复现对照。
- **优点**：保持与 Figure 9 相同的 color grammar 和 input/output 版式，读者可直接比较两种 construction 的额外状态结构。
- **不足**：行索引没有语义标注，bit 区、key 区、output 区要依靠色块和正文推断；没有同时放 attention pattern 或 decoded token label。
- **可复用模式**：对更复杂的 discrete-state construction 复用 input/output 双热图，但应在 y 轴标出 bit/key/output 分段。

## Figure 11 — Selective Copy vocabulary-size ablation

- **位置与职责**：p. 27，上方，两个参数量图横向并列，页面文本宽度。类型为 `line`、`area`；复杂度 **3/5**（2 panel × 4 series）。用途为 `ablation`、`robustness`、`efficiency_cost`。
- **面板与绘图语法**：左 panel 为 vocabulary size 200，右 panel 为 1000；每 panel 标题 `Average Accuracies across Param Counts`，x/y 线性，y 0–1，四架构颜色和同色半透明带沿用 Figure 4。两 panel 各有独立 legend（TF-TF、TF-SSM、SSM-SSM、SSM-TF），双向虚线网格，无 marker/reference line。
- **源精确样式**：`micro_hf/process.ipynb` 的 task/data comments 明确切换 `var-copy` 的 `data_100_5_200` 与 `data_100_5_1000`，cell 10 以 `x_axis='params'` 输出 `layers_dim`；`micro_hf/plt_utils.py` 提供同一颜色和 p10/p90 band。当前仓库同名 PNG 可能被 cell 14 的 later output 覆盖，故 PDF 的双 panel 以渲染为事实。
- **数据与统计**：两个不同词表规模下的 parameter sweep；E.2 文字说两种 vocab 的行为没有显著差异，图本身无检验或差异量。每 panel 为 11-run mean/p10/p90 convention，caption 不复述。
- **Caption（PDF 逐字提取，41 个空白分词）**：
  > Figure 11: Results of training the same architecture as the other, smaller vocabulary experiments, except with more tokens. The left figure shows results for a vocabulary of size 200, and the right figure shows results for a vocabulary of size 1000.

  Caption 有 title、setup、panel mapping，但没有 main finding、颜色 key、带宽和运行次数；`self_contained=false`、`main_finding_stated=false`。
- **证据关系**：Figure 4 的小词表 Selective Copy efficiency claim → E.2 的 vocabulary robustness question → Figure 11 的 200/1000 side-by-side → Figure 12–14 的 parameter/distribution/window ablations。
- **优点**：左右 panel 直接隔离词表规模，便于检查“扩大词表后趋势是否保留”；同一 y 轴和颜色系统有利于与 Figure 4 对读。
- **不足**：两个 panel x 轴范围不同且各自重复 legend，caption 只说“results”而不写行为结论；大面积 band 可能遮住低值曲线。
- **可复用模式**：将一个离散难度参数的两个规模并置，保持 shared y 轴与相同 architecture palette；caption 应补充跨 panel 的实际结论和 uncertainty rule。

## Figure 12 — Selective Copy heads/state dimension 消融

- **位置与职责**：p. 27，下方，两个 panel 横向并列。类型为 `line`、`area`；复杂度 **3/5**。用途为 `ablation`、`mechanism`、`failure`。
- **面板与绘图语法**：左标题 `Average Accuracy across Number of Heads`，x=1–4；右标题 `Average Accuracy across State Dimensions`，x=1–12；两者 y=accuracy 线性约 0.1–1.0。四架构实线及同色带；每 panel 有一条水平 dashed reference line（左为 SSM-SSM baseline，右为 TF-TF baseline，依据 `plt_utils.py` 的条件分支），legend 在 panel 内，双向网格、无 marker/hatching。
- **数据与统计**：head/state sweep 固定 token dimension/window 等默认项；E.2 文字结论为 head>1 时 tiny models 普遍变差，state dimension 没有清晰单调收益。Caption 明确 error bars 为 mean 周围的 0.1/0.9 quantiles；没有样本量。
- **Caption（PDF 逐字提取，49 个空白分词）**：
  > Figure 12: Results from training small models on Selective Copy. (a) changes the number of heads, and (b) increases the state dimension as described in Mamba. Defaults are token dimension 12, number of heads 1, and state dimension 1. Error bars are 0.1 and 0.9 quantiles around the mean.

  Caption 有 title、panel setup、default configuration 和 uncertainty definition，但没有说明 dashed reference 的语义或主结果；`self_contained=false`、`main_finding_stated=false`。
- **证据关系**：Figure 4 的 tiny Selective Copy separation → E.2 对 attention heads/Mamba state 的优化与表达力诊断 → Figure 12 → Figure 13 adversarial distribution 和 Figure 14 window ablation。
- **优点**：两个关键容量轴同屏，默认配置和 quantile 口径写在 caption，能够约束读者的比较条件；reference line 暗示固定 baseline。
- **不足**：dashed line 没有 caption key，颜色没有形状冗余；两个 panel 重复 legend 且没有 shared legend；caption 不写 head>1/state 非单调这一核心观察。
- **可复用模式**：把容量消融拆成并列 heads/state panels，并在 caption 写默认值与 quantile；应明示 reference line 的来源和主趋势。

## Figure 13 — adversarial Selective Copy distribution

- **位置与职责**：p. 28 上方，单栏栅格图。类型为 `line`、`area`；复杂度 **2/5**。用途为 `ablation`、`robustness`、`failure`、`main_comparison`。
- **面板与绘图语法**：一个 panel，标题 `Average Final Accuracies (1 head, 1 state dimension)`；x=`Parameter count` 线性约 1,000–12,000，y=`Accuracy` 线性约 0.1–1.0；TF-TF 蓝、TF-SSM 橙、SSM-TF 绿、SSM-SSM 红四条实线和同色带，legend 右下，无 marker、hatching 或 reference line。
- **源精确样式与统计边界**：题名和 task 对应 `micro/process.ipynb` cell 9 以及 `micro/results/binary_recall_mix/fig/layers_dim.png`；该旧 `micro` notebook 的绘图工具使用 mean/median 变量与 0.10/0.90 quantiles，当前 PDF E.1 统一叙述为 11-run mean + 10/90 percentile。由于公开仓库当前版本与 PDF 导出版本可能有覆盖，JSON 将 PDF 观察和 source path 分开标注，不把当前 PNG 的数值替换进 PDF。
- **Caption（PDF 逐字提取，51 个空白分词）**：
  > Figure 13: Selective Copy trained on an adversarial distribution, where half of the instances have a number token as their final token (hard for SSM), and half of the instances embed their last number token early in the sequence (hard for Transformers). This distribution is empirically easier for SSMs than uniform.

  Caption 有 title、adversarial setup、两类 failure comparison 和 main finding，但不定义带状统计或四条线；`self_contained=false`、`main_finding_stated=true`。
- **数据与统计**：训练分布一半把 number token 放在末尾、一半让 last number 很早出现；图画最终 accuracy 对 parameter count。没有单独给出两半实例的分层准确率，故不能从图中分离 SSM-hard 与 Transformer-hard 子分布。
- **证据关系**：Theorem 4.2 的两种 pure-model bottleneck → E.2 adversarial mixture → Figure 13 检验 hybrid 是否仍超过 pure/reverse hybrid → Figure 4 uniform distribution 作为对照 → Figure 14 window/learnability 边界。
- **优点**：caption 把 adversarial 分布和两个模型失败模式写清楚，读者知道该图是 mechanism stress test 而非普通 scale curve。
- **不足**：标题没有写 adversarial setting；没有分面展示两半数据，也没有 reference line/显式 effect size；颜色独占架构语义，band 口径仍需附录。
- **可复用模式**：把理论预测的两个 failure mode 混合为一项 adversarial ablation，并在 caption 直写每半样本的困难来源；最好再提供分层结果。

## Figure 14 — Selective Copy context window

- **位置与职责**：p. 28 中部，单栏图。类型为 `line`、`area`；复杂度 **2/5**。用途为 `ablation`、`robustness`、`failure`。
- **面板与绘图语法**：一个 panel，标题 `Average Accuracy across Window Sizes`；x=`Window` 线性 0–100，y=`Accuracy` 线性 0–1。TF-TF 蓝、TF-SSM 橙、SSM-TF 绿实线；SSM-SSM 以红色 dashed horizontal reference/baseline 表示，所有系列有同色带；图例在右上，双向虚线网格，无 marker/hatching。
- **数据与统计**：固定 Selective Copy 小模型条件，改变 Transformer context window；E.2 的文字结论是 window 变大时 Transformer 反而变差，Hybrid 在大 window 也常退化到 Transformer，原因偏向 learnability。结果带沿 E.1 11-run mean/p10/p90 convention，图注不定义。
- **Caption（PDF 逐字提取，21 个空白分词）**：
  > Figure 14: Results from training small models on Selective Copy. This changes the window of the context available to the model.

  Caption 只有 title、setup 和 x 轴操作，没有主结论、reference-line key 或 uncertainty；`self_contained=false`、`main_finding_stated=false`。
- **证据关系**：Theorem 3.7 的 window lower bound → Figure 4 的 fixed-window comparison → Figure 14 的 window sensitivity → E.2 对 Transformer/Hybrid learnability 退化的解释。
- **优点**：隔离 window 这一直接理论变量，并保留虚线 baseline 以显示 pure SSM 的参考水平。
- **不足**：caption 没有写随 window 增大而退化这一最有价值观察；dashed SSM-SSM 参考线未解释，且改变 window 同时可能改变优化难度，因果解释不能只从图读取。
- **可复用模式**：在表达力曲线之外单独画 context-window sweep，显式区分理论成本和 learnability；应同时画固定性能阈值或注明 baseline 生成规则。

## Figure 15 — MKAR context window

- **位置与职责**：p. 29 上方，单栏图。类型为 `line`、`area`；复杂度 **2/5**。用途为 `ablation`、`robustness`、`failure`。
- **面板与绘图语法**：一个 panel，标题 `Average Accuracy across Window Sizes`；x=`Window` 线性 0–100，y=`Accuracy` 线性约 0.1–1.0。SSM-TF 绿、TF-SSM 橙、TF-TF 蓝实线，SSM-SSM 红色 dashed reference；四个同色 band、右上 legend、双向虚线网格，无 marker/hatching。PDF 中嵌入的 1200 × 800 RGB 图像与作者仓库 `micro_hf/results/assoc-recall-mk/fig/layers_window.png` 逐像素 RGB 匹配。
- **数据与统计**：改变 MKAR context window，固定其余 tiny-model 参数；E.1 的 11-run mean/p10/p90 规则提供带的统计背景。E.2 正文指出 window 增大时 Transformer 退化，Hybrid 也可能受 learnability 影响。
- **Caption（PDF 逐字提取，22 个空白分词）**：
  > Figure 15: Results from training small models on Multi-Key Associative Recall. This changes the window of the context available to the model.

  Caption 有 title 和 setup，没有 main finding、band/reference-line 定义或固定参数；`self_contained=false`、`main_finding_stated=false`。
- **证据关系**：Figure 6 MKAR parameter frontier → Figure 15 window ablation → Figure 16 heads/state ablation → E.2 对理论预期和优化问题的分离解释。
- **优点**：与 Figure 14 使用同一 x 轴问题和视觉模板，便于比较 Selective Copy 与 MKAR 的 window sensitivity；source asset 可直接复核。
- **不足**：caption 未告诉读者 Transformer 曲线退化，虚线 SSM-SSM 语义仍未解释；没有将 window cost、latency 或 memory 放入同一决策面。
- **可复用模式**：在跨任务 ablation 中保持相同 window 图语法，以便直接对照；caption 应写出任务间共同趋势与例外。

## Figure 16 — MKAR heads/state dimension

- **位置与职责**：p. 29 下方，两个 panel 横向并列、接近页面文本宽度。类型为 `line`、`area`；复杂度 **3/5**。用途为 `ablation`、`mechanism`、`failure`。
- **面板与绘图语法**：左 panel `Average Accuracy across Number of Heads`，x=1–4；右 panel `Average Accuracy across State Dimensions`，x=1–12；y 均为线性 accuracy 约 0.1–1.0。四架构实线和同色带，SSM-SSM/TF-TF 条件下的 dashed horizontal reference line 按 panel 出现，双向虚线网格、panel 内 legend，无 marker/hatching。两幅 1200 × 800 资产分别与作者仓库 `layers_num_heads.png`、`layers_state_dim.png` 逐像素 RGB 匹配。
- **数据与统计**：固定 MKAR 小模型配置，扫描 heads/state；caption 明确带是 mean 周围的 0.1/0.9 quantiles。正文 E.2 观察到先有优化退化，增加足够 head/state 后性能回升；pure SSM 随 state 2→6 有一段增长后又下降。
- **Caption（PDF 逐字提取，50 个空白分词）**：
  > Figure 16: Results from training small models on Multi-Key Associative Recall. (a) changes the number of heads, and (b) increases the state dimension as described in Mamba. Defaults are token dimension 12, number of heads 1, and state dimension 1. Error bars are 0.1 and 0.9 quantiles around the mean.

  Caption 有 title、panel setup、defaults、uncertainty definition，但没有把先降后升/非单调主发现写出，也未解释 dashed references；`self_contained=false`、`main_finding_stated=false`。
- **证据关系**：Figure 6 的 MKAR hybrid frontier → Figure 16 对 heads/state 的机制敏感性 → E.2 对 optimization 与理论预期的区分 → 与 Figure 15 window sweep 共同给出扩展边界。
- **优点**：同屏比较 attention head capacity 与 Mamba state capacity，caption 固定默认值并明确 quantile，且源资产可追溯。
- **不足**：两 panel 反复绘制 legend，dashed baseline 没有文字解释；颜色无 marker/线型冗余，caption 没有总结非单调结果；没有同尺度参数量或计算成本信息。
- **可复用模式**：用并列 head/state sweeps 区分两类容量瓶颈，并把默认点、误差口径和 baseline key 写进 caption；若要支持机制结论，应增加分层/优化诊断。

## 跨对象证据系统

- **视觉叙事**：Figure 1 先用篮球问答把长上下文控制变量与局部 lookup 变成可见问题；Figure 2 抽象为 `SSM(u,v)→TF(F)`，Figure 3 将其实例化为 Selective Copy。Figure 4–8 再按 Selective Copy、Associative Recall、MKAR、NH、length/OOD 把方法接口带到 learned results；Table 1 固定 OOD bit-proportion；Figure 9–10 回到 construction implementation；Figures 11–16 用 vocabulary、head、state、adversarial distribution、window 消融检验边界。
- **Caption 系统**：18 个对象均在下方以 `Figure n:`/`Table n:` 起始，使用常规 Computer Modern caption。F2/F3、F9/F10 的 caption 更偏接口和 encoding key；F4–F8、F13 写出结果结论；F11、F14–F15 主要只命名 sweep；F12/F16 额外定义 0.1/0.9 quantile。E.1 的统计规则没有统一回填至所有结果 caption。
- **表头系统**：Table 1 用单层 `Train Proportion / SSM / TF / Hybrid` 并把固定 test condition 放 caption；Table 2 用 `Symbol / Meaning` 符号 glossary；F4/F6 的图内小表将 `Parameters` 与四种 architecture 列并置。没有多层横跨表头，简洁但成本/不确定性被移出对象。
- **方法—结果—消融链**：F2→F3 定义 `SSM-first` 的机制接口，F4/F5/F6 给 headline parameter/accuracy comparison，F7/F8/Table 1 扩展到理论外任务与泛化，F9/F10 让 construction 可复查，F11–F16 检查词表、容量、分布和窗口边界。该链条的机制方向清楚，但大量结果依赖附录 E.1 才能解释 band。
- **正文—附录链**：正文 Theorems 4.2–4.6 与 F2/F3 对接；D.5 的 F9/F10 对应 Section 5.1 的 construction implementation；E.1 定义 F4–F8 和附录 sweep 的训练/聚合；E.2 的 F11–F16 把主文趋势拆成 learnability/failure 边界。Table 2 为所有证明和 construction 提供符号索引。
- **字体与颜色一致性**：页面正文/表格/数学的 Computer Modern 稳定，Matplotlib 图内 DejaVu Sans 是独立子系统。architecture 色在结果图中一致，但 Figure 9/10 的 viridis-like discrete palette 是另一套结构编码；没有统一形状、marker 或线型冗余，因此颜色和 legend 是主要识别通道。

## 最终判断

- **最可复用模式**：
  1. Figure 2 的“抽象 SSM 编码器 → TF 组合器”接口图，用位置和控制/输出颜色把理论分解映射到可实现组件。
  2. Figure 4/6 的折线 + 精确锚点小表，把参数 frontier 与关键准确率同时呈现。
  3. Figure 9/10 的 input/output 双热图，用同一离散 color grammar 支撑 construction reproduction。
  4. Figure 11/12/16 的横向双 panel ablation，把一个研究问题拆成两个可直接对照的容量/规模轴。
  5. Figure 13 的 adversarial mixture caption，明确写出两类模型各自的困难来源，而不是把异常曲线隐藏。
- **最高价值对象**：Figure 4 是最直接的 Selective Copy efficiency headline；Figure 6 是 MKAR 的主参数比较并配有数表；Figure 2/3 把理论—实现接口讲清；Table 1 以最短形式呈现 OOD 条件；Figure 9/10 对 construction 的复现价值最高。
- **失败或低价值模式**：结果图常以颜色单通道区分架构，灰度和色觉缺陷环境不安全；F4–F8、F11、F13–F16 的 caption 多不说明 band 的统计定义、run 数或分母；F11/F12/F16 重复 legend 占空间；Table 1 无波动信息；Figure 14/15 caption 没有写出 window 增大后的退化；Figure 1–3 没有公开原始图源，F13 当前 `micro` 工具与 PDF E.1 的聚合命名存在版本口径差异。
- **一句话视觉策略**：用概念图和 SSM→TF 架构建立函数组合机制，以参数 frontier/表格承载主比较，再用 input/output 热图与容量、分布、窗口双 panel 消融补齐 construction 可复现性和 learnability 边界；主要改进点是把颜色、带宽、重复和比较条件在对象级 caption 中补全。

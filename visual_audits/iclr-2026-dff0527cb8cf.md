# iclr-2026-dff0527cb8cf 视觉审计

## 审计边界与 PDF 事实源

- **论文**：Q-RAG: Long Context Multi-Step Retrieval via Value-Based Embedder Training，Artyom Sorokin、Nazar Buzun、Alexander Anokhin、Egor Vedernikov、Petr Anokhin、Mikhail Burtsev、Evgeny Burnaev，ICLR 2026。
- **唯一对象事实源**：`corpus/pdfs/iclr-2026-dff0527cb8cf.pdf`。该 PDF 共 26 个物理页，letter（612 × 792 pt），由 pdfTeX 生成；正文 p.1–10，参考文献 p.11–13，附录 p.14–26。`corpus/text/iclr-2026-dff0527cb8cf.txt` 与 PDF 逐页核对，附录 A–G、公式、算法、参考文献均纳入阅读。
- **渲染**：26 页全部以 200 dpi（1700 × 2200 px）PNG 渲染，超过协议要求的 180 dpi。含对象页面 p.3、p.6–10、p.22–26 另行放大查看；对象页的图内文字、坐标、图例、线型、表格横线和 caption 以渲染结果核验。`pdfimages -list` 显示 p.6 Figure 2、p.9 Figure 3、p.22 Figure 4、p.23 Figure 5 使用嵌入栅格图；Figure 1、Figure 6 与所有表格主要由 PDF 矢量对象排版。
- **PDF 对象数量**：6 幅 Figure（Figure 1–6）和 8 张 Table（Table 1–8）。Algorithm 1 是算法框而非 schema 视觉对象，已在方法关系中记录但不计入 `figures`/`tables`。没有跨页 Figure/Table，附录中的 Figure 4–6 与 Table 5–8 均实际存在。
- **与 reading inventory 的核对**：`readings/iclr-2026-dff0527cb8cf.json` 起始清单列出 Figure 1–6、Table 1–8 和 Algorithm 1；逐页以 PDF 为准，编号、页码和模块完全一致。PDF 的实际对象清单是本审计的最终依据，而不是自动 inventory。

## 公共视觉源核查

先核对 `reports/tables/visual_source_inventory.csv`：该行标题为 `Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training`，候选为 `griver/Q-RAG`，自动状态为 `repository_without_visual_source`，匹配依据包括 PDF 明确 URL、README 标题精确匹配和代码上下文。`corpus/visual_sources/iclr-2026-dff0527cb8cf/` 不存在，没有可直接复用的本地视觉源。

随后仅用只读 `gh` 核对 `https://github.com/griver/Q-RAG` 的 `pqn-qa` 分支：仓库描述为 ICLR 2026 Oral 的 Q-RAG 官方仓库，README 标题与论文标题精确一致，README 还明确嵌入 `images/Ruler.png`、`images/OpenQA.png` 和 `images/Babilong_graphics.png`。递归 tree 在提交 `42358d78ac491843763b90677f07237471c97086` 下没有 plot/figure/visual/table 生成脚本、`.tex`/TikZ/PGF、notebook 或样式文件；只有训练/评测代码和 README 展示用 PNG。只读读取的 PNG 为：

- `images/babilong_avg_ans_v2.png`（1177 × 679）与 `images/babilong_qa3_ans.png`（1118 × 679）：分别逐项对应 PDF Figure 2 的两个面板；
- `images/Babilong_graphics.png`（2034 × 602）：README 合并展示的 Figure 2 两面板资产；
- `images/Ruler.png`（1744 × 1290）：行列、数值和高亮与 PDF Table 1 对应；
- `images/OpenQA.png`（1084 × 426）：行列、数值和高亮与 PDF Table 2 对应。

这些文件是经过论文 README 与 PDF 逐项核对的 **rendered assets**，不是可编辑绘图/表格源；它们仅支持 Figure 2、Table 1、Table 2 的像素/内容关系，不能反推 Figure 3–6、Table 3–8 的绘图参数。故 JSON 将状态从自动的 `repository_without_visual_source` 细化为 `partial_visual_source`，仅登记上述资产和用于身份验证的 README，不把通用训练/评测代码冒充成视觉源。其余对象均以 PDF 对象和 200 dpi 渲染为事实。

## PDF 对象清单

|对象|物理页|模块|版面|可见内容|
|---|---:|---|---|---|
|Figure 1|3|method|main，page_width|Q-RAG agent、state/action embedder、Q values、policy、environment 的多步检索数据流|
|Figure 2|6|results|main，page_width|BabiLong 平均 Q1–QA5 与 QA3 随 context length 的 answer accuracy 折线|
|Table 1|7|results|main，page_width|RULER 各 context length、NIAH 子任务与 SH/MH QA|
|Table 2|8|results|main，page_width|HotPotQA、MuSiQue (OOD) 的 fact/answer 指标及平均值|
|Figure 3|9|ablation|main，page_width|α、λ sensitivity 与 QwQ-32B inference runtime 三面板|
|Table 3|9|ablation|main，single_column|BabiLong QA3 上 Q-RAG 组件、SFT 与无 fine-tuning 对照|
|Table 4|10|ablation|main，single_column|HotPotQA retrieval steps 与三种 Qwen3 answerer 的 EM/F1|
|Figure 4|22|appendix|appendix，page_width|HotPotQA/BabiLong QA2 的 early、late、perfect stopping 与 episode length 六面板|
|Table 5|22|appendix|appendix，page_width|HotPotQA Q-value threshold 的 stop 类型、TPR/FPR、长度和质量|
|Figure 5|23|appendix|appendix，page_width|HotPotQA/BabiLong QA2 early-stopping ROC 与 oracle point|
|Table 6|23|appendix|appendix，page_width|BabiLong QA2 Q-value threshold 的 stop 类型、长度和质量|
|Figure 6|24|appendix|appendix，page_width|HotPotQA 与 BabiLong QA2 average episodic return 学习曲线|
|Table 7|25|appendix|appendix，page_width|HotPotQA-distractors、MuSiQue in-distribution/OOD 的扩展比较|
|Table 8|26|appendix|appendix，page_width|数据集、chunk size、retrieval budget、retriever 和 answerer 配置|

## 全文视觉系统

PDF 正文、caption 和表格主要使用 Nimbus Roman No9 L；数学符号使用 Computer Modern 数学字体，等宽配置/模型名在正文和 Appendix G 使用 Nimbus Mono。Figure 1 的组件标签还使用 DejaVu Sans Type 3；Figure 2–5 的嵌入图内标签是 DejaVu Sans 栅格字；Figure 6 的图内文字为 PDF DejaVu Sans 矢量对象。正文和 caption 约 9–10 pt；主文表格正文约 7 pt，附录的密集表格约 6.5–7 pt；图内刻度、图例和标题约 5.5–8 pt。

Figure 1 使用浅绿、浅蓝、粉、黄、灰等语义色区分 agent/environment/chunk 状态；Figure 2 使用多色 categorical palette 区分方法，且两个面板的方法颜色并不完全保持同一映射；Figure 3–6 多采用 Matplotlib 风格的蓝/橙/绿/红线和浅灰网格。表格保持黑白矢量排版，以粗体、下划线、灰色 `n/a` 和方法前的 `✓/◦/×` 表达状态，不使用 cell fill 或误差带。整体字体和 booktabs 规则稳定，但图的颜色语义没有跨图统一，且图内栅格标签在单页缩放下偏小。

## Figure 1（p.3，main）

- **类型、版面和复杂度**：`conceptual_diagram`、`pipeline`、`architecture`；`headline`、`method_interface`、`theory_mechanism`、`experimental_design`。单个 page-width 多层流程图，Q-RAG Agent 的绿色框位于上部，Long-Context Document 的 chunk 序列位于中部，Environment 的蓝色框位于下部；箭头连接 state/action embedding、Q values、policy、selected chunk、reward/critic 和 next timestep。复杂度 4：虽然无数值 panel，但组件、路径和方向信息密集。
- **绘图语法**：无 x/y 轴、网格、数值 legend、marker、reference line 或不确定性；组件标题、公式符号和 chunk 文本是 direct labels。实线/箭头表示数据流，橙色虚线/指示线连接 chunk 与 action embedder，绿色/灰色框和路径区分 agent、document 与 environment，约 1 pt 线宽。`rendering=vector`，`x_scale/y_scale=none`。
- **字体与颜色**：图内 DejaVu Sans 和 Computer Modern math 约 5.5–9 pt，caption 为 Nimbus Roman 约 9–10 pt；组件标签有 regular/medium，数学符号有 italic。近似色为 #B7E095（state/action embedder）、#D5F0C7（agent 容器）、#C5DFFF（environment）、#F4A5E3（question/state query）、#FFE3A1（文本 chunk）、#C9C9C9（selected chunk）、#7BCB7B（路径/箭头）和 #000000（文字/边框）。这些色彩表达组件语义，标签、框形和布局提供部分冗余，但颜色仍承担主要区分，灰度安全有限。
- **Caption**：`Figure 1: Q-RAG agent interacts with multi-step retrieval environment. The starting state s0 contains the initial query q. At the start of the episode, the agent embeds all chunks of the long context C. At each step t, the agent computes a vector embedding of the current state st , which includes q and all previously selected chunks. For every chunk ci ∈ At , the utility of retrieving it is evaluated by the Q-function Qθ (st , a = ci ). The policy πθ selects the next chunk from At with probability proportional to its Qθ (st , ci ) value.`（102 词）。动作是 `title`、`setup`、`encoding_key`、`main_finding`；label 没有粗体 headline，self-contained=true、main_finding_stated=true。Caption 将符号和组件关系写出，但没有解释颜色。
- **数据与证据关系**：无样本、单位、聚合或统计不确定性；这是 MDP state/action 环境和 Q-function 的机制示意。它把 §3.1 的 ordered state、§3.2 的 Eq. (1)–(5)、§3.3 的 relative positional mapping Eq. (6)–(7) 和 Algorithm 1 接到 Figure 2/Table 1–2 的实验及 Figure 3/Table 3–4 的组件验证；它不单独证明 reward 设计或 temporal encoding 的效果。
- **优点**：把 query、已选 chunk、候选 action、Q values、policy、环境反馈压缩在同一数据流中；下方 environment 与上方 agent 的闭环箭头直接表达多步检索，而不是只画静态 encoder。
- **缺陷**：候选 chunk 数、Q-value 到 softmax policy 的具体公式和 STOP action 没有在图中显示；多种 pastel 色在灰度和普通缩放下区分变弱；相对位置机制没有单独视觉标记。
- **可复用范式**：用同一条从 state→candidate actions→value/policy→environment reward→next state 的闭环，把算法接口和后续公式的符号一一映射，避免把方法图做成没有可验证状态转移的装饰性架构图。

## Figure 2（p.6，main）

- **类型、版面和复杂度**：`line`；`headline`、`main_comparison`、`robustness`、`dataset`。page-width 两面板：(a) BabiLong QA1–QA5 平均性能，(b) 最难的 QA3；每个面板在 1K、4K、32K、128K、1M、10M context length 上画多方法曲线。面板 (a) 约 10 个系列，(b) 约 8 个系列，复杂度 4。
- **绘图语法**：x 轴 context length 为对数式布局（1K→10M），y 轴 answer accuracy 为 0–1 线性；x/y 均有浅灰网格，含对数式次刻度。每面板有独立的 bottom legend，不共享 legend；实线表示 BabiLong fine-tuned，虚线表示 zero-shot。圆点和方形点混用以辅助区分曲线，约 1.2–1.5 pt 线宽；无 reference line、hatching 或 error bar/band。`rendering=raster`，`direct_labels=false`。
- **字体与颜色**：图内 DejaVu Sans 栅格标题、刻度和图例约 5.5–7 pt，caption 为 Nimbus Roman 约 9–10 pt；字体主要 regular。近似 categorical 色为 #1F77B4（蓝）、#FF7F0E（橙）、#2CA02C（绿）、#D62728（红）、#9467BD（紫）、#8C564B（棕）、#E377C2（粉）、#7F7F7F（灰）、#BCBD22（橄榄）和 #17BECF（青）。颜色表达方法，实/虚线表达 fine-tuned/zero-shot；方法多时颜色区分在灰度下不安全，`redundant_encoding=true` 仅对训练状态成立。
- **Caption**：`Figure 2: Comparison of answer accuracy on the long-context benchmark BabiLong. Solid lines denote methods fine-tuned on BabiLong, while dashed lines denote zero-shot methods. a) Average performance across tasks Q1–QA5. b) Performance on the hardest task, QA3, which requires the longest reasoning chain and temporal awareness.`（46 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；caption label 没有粗体 headline，self-contained=true、main_finding_stated=false。
- **数据与证据关系**：每个 marker 是一个 context length 下的 answer accuracy 点，未显示误差或 seed 聚合；(a) 为 Q1–QA5 平均，(b) 为 QA3。正文说明 Q-RAG 的曲线延伸至 10M，许多基线为原论文 reported numbers，QA3 的 Beam Retriever 额外 fine-tuning 失败。图把摘要/§4.2 的 ultra-long claim 接到 Table 1 的 1M RULER 结果，但没有统一重跑和共同不确定性。
- **优点**：共享 y 轴和相同 context-length 轴让“随长度退化”成为直接比较；面板 (a)/(b) 将总体表现和三 supporting facts/temporal reasoning 的 hardest case 分离；实线/虚线在 caption 中定义清楚。
- **缺陷**：多色 legend 密集且两个面板的颜色与方法映射不完全一致；没有误差、样本分母或 reported/reproduced 的图内标识；对数式 x 轴虽适合跨度，却没有在轴标签中明确 `log`，10M 点的跨方法同质性受 baseline 来源差异限制。
- **可复用范式**：当研究问题是 context scaling 时，用同一对数式长度轴并排放总体平均与最难子任务，同时以线型表达训练状态、caption 解释来源和面板语义；应额外配套 provenance/uncertainty 标记。

## Figure 3（p.9，main）

- **类型、版面和复杂度**：`line`；`ablation`、`robustness`、`efficiency_cost`。page-width 三面板：(a) policy entropy coefficient α，(b) λ-return parameter，(c) QwQ-32B inference time；复杂度 3。前两面板各有 QA2/QA3 两条曲线，(c) 有 Beam Retriever、Q-RAG、GraphReader(memorize)、GraphReader(retrieve)、QwQ-32B 五条运行时间曲线。
- **绘图语法**：面板 (a) x 为 α=0–0.05、y 为 average return 线性；(b) x 为 λ≈0.4–0.8、y 为 average return 线性；(c) x 为 context length/tokens 线性、y 为 Time (sec) 对数。各 panel 有 x/y grid；(a)/(b) 独立 bottom legend，(c) upper-right legend，故不共享。曲线有圆点或 x marker，(c) 含一条 GraphReader(retrieve) 虚线；无 reference line 和不确定性带。`rendering=raster`、`marker_types=2`、`line_styles=2`。
- **字体与颜色**：DejaVu Sans 图内文字约 6–7 pt，caption/外部文字为 Nimbus Roman 约 9–10 pt；regular 为主。近似色为 #1F77B4（QA2/Q-RAG）、#FF7F0E（QA3/Beam Retriever）、#2CA02C（GraphReader）、#D62728（若干运行曲线）、#000000（QwQ-32B）和 #D9D9D9（grid）。颜色区分系列，x/circle marker 和虚线提供部分冗余，灰度对 GraphReader 多系列仍不理想。
- **Caption**：`Figure 3: Ablation for (a) policy entropy coefficient (α) in soft Q function and (b) for λ-return parameter. Inference runtime comparison (c), context length in tokens on the x-axes.`（29 词）。动作是 `title`、`setup`、`encoding_key`；caption label regular，self-contained=true、main_finding_stated=false。
- **数据与证据关系**：面板 (a)/(b) 是 soft-Q 的 α、λ 敏感性，连接 Eq. (2)–(5) 与 Table 3 的去 Soft-Q/target ablation；(c) 是 Appendix D 的复杂度叙事在主文的 runtime 对照，x 是 context length，y 为秒数且 log scale。无 seed、区间或重复说明，运行曲线不是端到端同一 answer-quality estimand。
- **优点**：把训练超参数敏感性和运行成本放在同一视觉对象，避免只报最终点；(c) 使用 log y 轴让毫秒至千秒量级同时可见；面板标题和 legend 可定位方法。
- **缺陷**：(a)/(b) 没有误差或 sampled values 的完整说明；(c) 的方法色/marker 与 Figure 2 不共享稳定语义，且 QwQ-32B、retriever 和 agent 的计算边界不同；caption 没有解释对数 y 轴或曲线缺失点。
- **可复用范式**：将算法组件的局部敏感性和成本轴并列，前两 panel 固定同一指标，成本 panel 明确单位、尺度和比较边界；不要把不同测量边界的运行时间当成单一 headline。

## Table 1（p.7，main）

- **类型、版面和复杂度**：`headline`、`main_comparison`、`robustness`、`dataset`。page-width RULER 结果表，13 列、5 个 context-length row groups（4K/16K/32K/128K/1M），18 个数据行；表头两层：S、MK、MV、MQ、NIAH Avg.、QA 下的指标/子任务。`booktabs` 式顶线、分组线和底线，无竖线。
- **表头与编码**：`Len`、`Methods`；S 的 1st/2nd/3rd，MK 的 1st/2nd/3rd，MV、MQ、NIAH Avg.、QA 的 SH/MH。方法名前的 `◦`/`✓` 是 reported/reproduced 状态，Q-RAG 无标记。最佳值用粗体，`n/a` 以浅灰文字表示。多数列为百分比/accuracy 点值，最大显示精度为 1 位小数。
- **Caption**：`Table 1: Results on the RULER benchmark, evaluating long-context retrieval performance across various context lengths. S (Single-needle): Find one value for one key. MK (Multi-keys): Find one value for one key among many. MV (Multi-values): Find all values for one key. MQ (Multi-query): Answer multiple questions over the context. MH QA: open-domain multi-hop question answering. SH QA: single-hop question answering.`（60 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`abbreviation_definition`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：没有 mean±SD、区间、seed 或显著性；缺失项为 n/a，所有单元是点估计。表将 4K→1M 的 context scaling、NIAH retrieval 与 QA 指标放在一个决策面，支持正文 §4.3 的“4K 训练泛化至 1M”主张；Q-RAG 在 NIAH Avg. 多处为 100，但 MH QA 仍随长度变化。它延伸 Figure 2 的长上下文故事，并为 Table 2 的 open-domain 转移提供另一任务族。
- **优点**：两层表头明确区分单钥匙、多钥匙、多值、多查询和 QA；长度 row group 使跨尺度退化直接可读；粗体与灰色缺失值保持黑白可读。
- **缺陷**：列数多且数值密集，caption 虽定义缩写但没有说明点值的样本/seed；`◦/✓` 的 provenance key 需要回读 §4.1；1M 只保留 Q-RAG，横向 baseline coverage 随长度变化。
- **可复用范式**：对多个子任务共享同一长度轴时，用两层任务表头和长度 row groups 把 retrieval 与 answer-level 结果并排；同时在表注中写清来源类别、样本分母和重复方式。

## Table 2（p.8，main）

- **类型、版面和复杂度**：`headline`、`main_comparison`、`dataset`、`robustness`。page-width 比较表，11 列、8 个方法数据行，2 个 body row groups（Fine-tuned on HotPotQA、Zero-shot methods）；表头两层：HotPotQA、MuSiQue (OOD)、Avg. 下分别是 Fact/Ans 指标。使用 booktabs 顶/底线、分组线和少量竖分隔线。
- **表头与编码**：HotPotQA 和 MuSiQue 各含 Fact F1、Fact EM、Ans F1、Ans EM，Avg 只含 Ans F1、Ans EM。`✓/◦/×` 与 §4.1 的 reproduced/reported/ablation 对应；最佳值粗体，第二名下划线，缺失值用短横线。列值统一两位小数。
- **Caption**：`Table 2: Comparison of methods on HotPotQA and MuSiQue benchmarks. Bold text and underline denote the best and second best scores respectively.`（22 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：没有区间、seed 或显著性，值为聚合 Fact/Ans EM/F1；正文说明 Q-RAG/Beam Retriever 在 HotPotQA fine-tune 后在 MuSiQue OOD 评估，Beam Retriever 使用 oracle gold hop count，基线数字直接取原论文。表是 §4.4 的主比较，连接 Appendix C 的 Plan Q-RAG 和 Appendix E Table 7 的额外数据切片；Avg 只对 answer metrics 聚合，不能解释为所有 Fact/Ans 单元的统一平均。
- **优点**：数据集、训练状态、fact retrieval 和 answer generation 在一个表中，粗体/下划线直接呈现 best/second-best；把 Plan Q-RAG 与 vanilla Q-RAG 放在同一表有助于判断 planning 变体。
- **缺陷**：reported、reproduced、ablation 混在一张表且只用小 glyph 标记；Beam Retriever 的 gold hop count 与 Q-RAG 的动态策略不完全同质；没有样本数、误差或统一重跑标识。
- **可复用范式**：用数据集组列和训练 regime 行把 retrieval-level 与 answer-level estimand 同时展示，并用可打印的来源 glyph 配合 caption 定义；跨数据集平均必须标清聚合范围。

## Figure 3 / Table 3–4 的方法消融链

Figure 3、Table 3 和 Table 4 在正文 p.9–10 连续出现，形成从训练组件到 retrieval budget 的局部证据链：Figure 3 看 α、λ 和 runtime，Table 3 删除 Soft-Q/target/RL，Table 4 改变 retrieval steps 并观察 Fact 与三种 answerer。Figure 3 的视觉对象已单独记录；以下表对象独立审计。

## Table 3（p.9，main）

- **类型、版面和复杂度**：`ablation`、`mechanism`、`robustness`。single-column、6 列（Method、1K、4K、32K、128K、1M），5 个数据行、单层表头；Method 与数值之间有一条竖分隔线，采用极简横线/留白而非完整 grid。
- **表头与编码**：context length 是列分组，行是 Q-RAG、去 Soft-Q、去 Target、Multi-Step RAG w. SFT、Multi-Step RAG w.o. FT。单元报告支持事实 retrieval F1，最大两位小数；`—` 表示未报告的 1M 结果。无粗体、下划线、cell color 或箭头。
- **Caption**：`Table 3: Ablation results on BabiLong QA3. The Table shows F1 score for supporting facts retrieval. All values are averaged over 3 runs with different seeds.`（26 词）。动作是 `title`、`setup`、`comparison`、`uncertainty_definition`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：数值写作 mean ± reported spread，但作者没有说明 ± 是 SD、SE 还是其他聚合；明确平均 3 个不同 seed。去 target 行的 spread 约 ±26–28，完整 Q-RAG 为约 97.8→96.5，去 Soft-Q 略低，无 FT/SFT 显著更低。它是 Figure 1/§3.2 的 soft value、target network 和 RL 训练主张的直接隔离对照，连接 Figure 3(a,b) 超参数敏感性。
- **优点**：同一 QA3、同一长度列轴同时删除 RL、Soft-Q 和 target，因果阅读顺序清楚；3-seed 聚合比主结果表更透明。
- **缺陷**：没有把 ± 的统计含义写进表注；1M 对 SFT/no-FT 缺失，不能把所有行视为完整长度扫描；表中没有直接高亮完整 Q-RAG 最优或将大波动视觉化。
- **可复用范式**：对一个最难任务固定长度轴，并在相邻行逐个去除机制组件；将 seed 数与 spread 定义写在 caption，而不是让读者猜测 ± 的含义。

## Table 4（p.10，main）

- **类型、版面和复杂度**：`ablation`、`mechanism`、`robustness`。single-column、9 列、4 个 retrieval-step 行（2–5），两层表头：Facts、Qwen3-4B、Qwen3-14B、Qwen3-32B 各下设 EM/F1；无 row group，booktabs 顶线/底线和组内短横线。
- **表头与编码**：第一列为 Retrievals；Facts 的 EM/F1 是支持事实 retrieval，三个 Qwen3 组的 EM/F1 是 answer generation；数值固定三位小数。无粗体、下划线、箭头或颜色。
- **Caption**：`Table 4: Sensitivity to the number of retrieval steps. Dataset: HotPotQA (1000 samples). Embedder Alibaba-NLP/gte-multilingual-base was trained on HotPotQA+MuSiQue.`（19 词）。动作是 `title`、`setup`、`encoding_key`、`abbreviation_definition`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：1,000 个 HotPotQA samples，点估计，没有 seed、区间或显著性。2→5 retrieval steps 时 Fact EM 上升而 Fact F1 下降，三种 Qwen3 的 answer EM/F1 大致在 3–5 steps 改善或平台化；正文解释 F1 对额外 noise 有惩罚。它将 §5.1 的“正确 chunk 驱动答案质量”连到 Appendix G 的 Fact-EM 集合包含定义，并补充 Figure 3 的效率/预算边界。
- **优点**：把 retriever 的正确性和三个 answerer 的响应放在同一 step 轴，能观察“覆盖更多事实”与“噪声增加”的张力；caption 给出数据集、分母和 embedder。
- **缺陷**：只有一个数据集和一次聚合，没有 error/seed；EM/F1 的方向在 Facts 与答案列之间不直观；表注没有指出不同 Qwen3 模型的解码设置。
- **可复用范式**：对预算型干预同时列 retrieval-level 和 answer-level 指标，保持相同的步数列轴，并把分母、训练数据和解码边界写入 caption/header。

## Figure 4（p.22，appendix）

- **类型、版面和复杂度**：`line`；`mechanism`、`robustness`、`efficiency_cost`、`failure`。appendix page-width 的 2×3 六面板；上排 HotPotQA，下排 BabiLong QA2。每个数据集有：(a,d) early/late error rate，(b,e) perfect stopping rate，(c,f) mean episode length。复杂度 4。
- **绘图语法**：所有 x 为 `Q_threshold` 线性，(a,b,d,e) y 为 rate 0–1 线性，(c,f) y 为 average number of selected chunks 线性；每 panel 均有 x/y grid。a/d 为蓝色 Early stopping 与橙色 Late stopping，b/e 为蓝色 Perfect stopping，c/f 为蓝色 Mean Len；圆点 marker，实线，独立小 legend，未共享。无 reference line、hatching、error bar/band；`rendering=raster`，`marker_types=1`、`line_styles=1`。
- **字体与颜色**：DejaVu Sans 图内标题/刻度约 5.5–6.5 pt，caption 为 Nimbus Roman 约 9–10 pt；regular。近似色为 #1F77B4（early/perfect/mean）、#FF7F0E（late）、#BFBFBF（grid）和 #000000（文字）。蓝/橙在灰度下可读性一般，但 legend 文本和 panel 位置提供部分冗余。
- **Caption**：`Figure 4: Early stopping analysis on HotPotQA (top row) and BabiLong QA2 (bottom row). Panels (a,d) show the proportions of early and late errors as a function of the Q-value threshold Qthreshold . Panels (b,e) show the proportion of perfect stops. Panels (c,f) show the average number of selected chunks (episode length).`（52 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；caption label regular，self-contained=true、main_finding_stated=false。
- **数据与证据关系**：每个数据点对应 Table 5/6 中的 threshold，图把 early/late/perfect 分类与 episode length 共享同一 x 轴。它支持 Appendix B 关于中等阈值降低长度、过高阈值造成 early-stop failure 的机制解释，并为 Figure 5 的 ROC 与 Tables 5–6 的数值展开提供视觉入口。作者说明从未收集全部 ground-truth chunks 的 episode 被丢弃，但图未显示分母。
- **优点**：2×3 版式把错误类型、perfect stop 和计算代价放在同一阈值轴；上下排使用相同 panel 语义，跨 HotPotQA/BabiLong QA2 读取成本低。
- **缺陷**：六个 panel 的 legend 重复占空间；没有样本数、误差或阈值标签的关键转折注释；不同 y 量纲共用视觉网格但未用更明确的 panel 标题区分数据集。
- **可复用范式**：对动态停止同时画错误分解、理想事件比例和平均长度，固定 row-wise dataset 与 column-wise outcome，使效率—质量 trade-off 不被单一最终分数隐藏。

## Table 5（p.22，appendix）

- **类型、版面和复杂度**：`mechanism`、`robustness`、`efficiency_cost`、`failure`。page-width、11 列、13 个 threshold 行，单层表头；booktabs 顶/底线，无竖线。列为 Q-value threshold、stopped early/later、perfect stop、TPR、FPR、Episode len、Fact EM/F1、Ans EM/F1，最大显示精度为三位小数。
- **Caption**：`Table 5: HotPotQA early stopping experiments`（6 词）。动作仅为 `title`；caption label regular，self-contained=false、main_finding_stated=false。阈值、字段含义和 oracle 解释放在 Appendix B 正文，而非 caption。
- **不确定性、数据与证据关系**：无区间、seed 或显著性；单元为 threshold 条件下的比例、平均长度和质量点估计。p.22 正文说明 GTE embedder、`penalize_extra_steps=True`、`never_terminate=True`，并将 TPR/FPR 视为二分类停止器；Qthreshold=0.2 的 Fact F1=0.917、perfect stop=0.892、episode length=2.13，接近质量—成本折中。它与 Figure 4(a–c) 一一对应，并由 Figure 5(a) 用 TPR/FPR 形成 ROC；表不提供 episode 分母。
- **优点**：将 stop 类型、分类器指标、长度和答案质量放在一个完整决策表；阈值细网格可复核 Figure 4/5 的趋势。
- **缺陷**：caption 极短，依赖正文才能知道列语义、丢弃规则和 oracle；没有用粗体标出推荐阈值或注明 best/second；高阈值处性能塌缩没有视觉高亮。
- **可复用范式**：把动态阈值、分类器质量、平均计算步数和任务质量放在同一表，并在表注直接定义 discarded cases、正类和推荐 operating point。

## Figure 5（p.23，appendix）

- **类型、版面和复杂度**：`line`；`mechanism`、`robustness`、`efficiency_cost`。page-width 两面板：(a) HotPotQA，(b) BabiLong QA2；每 panel 一条橙色 ROC 曲线、深蓝虚线随机性能对角线和红色星形 oracle point，复杂度 3。
- **绘图语法**：x 为 False Positive Rate、y 为 True Positive Rate，均线性 0–1；x/y grid。每 panel 有 bottom-right legend，非共享；ROC 为实线，随机性能为虚线，oracle 为 red star marker。无 hatching、误差带或 reference beyond the random-performance diagonal；`reference_lines=1`、`marker_types=1`、`line_styles=2`、`uncertainty_display=none`、`rendering=raster`。
- **字体与颜色**：DejaVu Sans 图内标题/轴约 7–8 pt，caption 为 Nimbus Roman 约 9–10 pt；regular。近似色为 #FF7F0E（ROC）、#000080（random diagonal）、#FF0000（oracle star）、#BFBFBF（grid）和 #000000（文字）。线型、星标和 legend 对颜色有冗余，但蓝/橙/红灰度区分仍一般。
- **Caption**：`Figure 5: ROC curves for the early-stopping rule. Panel (a) shows HotPotQA; panel (b) shows BabiLong QA2. The dashed line indicates random performance. Each point corresponds to a different Q-value threshold Qthreshold . The red star denotes the oracle stopping policy that always stops at tearliest , i.e. exactly when the last ground-truth chunk has been retrieved.`（57 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`、`abbreviation_definition`；caption label regular，self-contained=true、main_finding_stated=false。
- **数据与证据关系**：曲线点来自 Tables 5–6 的 TPR/FPR threshold sweep；p.23 legend 还显示 AUC=0.961/0.970，红星是知道 `t_earliest` 的 oracle。图是 Appendix B 从阈值行为到 classifier trade-off 的压缩总结，不能把 oracle 当作可部署模型，也没有区间或 bootstrap。
- **优点**：随机对角线和 oracle point 给出清楚的下界/上界参照；两个数据集并排且共享 FPR/TPR 语义，AUC 在 legend 中可见。
- **缺陷**：threshold 顺序未在曲线上标注；ROC 曲线看起来接近饱和但没有样本数和 operating point 推荐；图把不同任务的点密度、丢弃规则和正类定义留给正文。
- **可复用范式**：从同一张阈值结果表直接生成 ROC，保留随机线和 oracle 上界，并在图中标注 threshold 或推荐 operating point 以避免只呈现漂亮 AUC。

## Table 6（p.23，appendix）

- **类型、版面和复杂度**：`mechanism`、`robustness`、`efficiency_cost`、`failure`。page-width、9 列、13 个 threshold 行，单层表头，booktabs 顶/底线，无竖线。列为 Q-value threshold、stopped early/later、perfect stop、Episode len、Fact EM/F1、Ans EM/F1，最大三位小数。
- **Caption**：`Table 6: BabiLong QA2 early stopping experiments.`（7 词）。动作仅为 `title`；caption label regular，self-contained=false、main_finding_stated=false。
- **不确定性、数据与证据关系**：无区间、seed 或显著性；每行是 BabiLong QA2 threshold 下的 stop 比例、episode 长度和 Fact/Ans EM/F1 点估计。正文指出 Qthreshold∈[0.2,0.6] 时 perfect stop 约 0.95–0.99、长度约 2.2 且 Fact F1 约 0.95，接近最优；接近 1.0 时 early stop 比例升高、性能坍塌。它数值化 Figure 4(d–f)，并支持 Figure 5(b) 的 ROC；未报告分母与 discarded episode 数量。
- **优点**：与 Table 5 保持列语义和 threshold 网格的一致性，便于跨数据集比较；把质量和长度同表呈现。
- **缺陷**：缺少 TPR/FPR 列，读者需要回到正文或从 Figure 5 推断分类器指标；caption 没有定义 `perfect stop` 或说明 step budget；没有突出 [0.2,0.6] 的工作区间。
- **可复用范式**：保持跨任务的阈值表 schema 一致，同时为不完全相同的指标列在 caption 说明差异，并在推荐工作区间加轻量可打印标记。

## Figure 6（p.24，appendix）

- **类型、版面和复杂度**：`line`、`scatter`；`efficiency_cost`、`robustness`。page-width 两面板，左为 Babilong QA2，右为 HotPotQA；各一条蓝色带圆点曲线，x 为 Time (hours)，y 为 Eval return，复杂度 2。
- **绘图语法**：两个 panel 均为 linear x/y，x 范围约 0–4.5 小时（BabiLong）和 0–6.2 小时（HotPotQA），y 为约 0.2/0.3–1.0；有浅灰 x/y grid。没有 legend，panel title 是 direct label；蓝色实线和圆点 marker，未显示 reference、hatching、error bar、band 或重复曲线。`rendering=vector`、`marker_types=1`、`line_styles=1`。
- **字体与颜色**：PDF DejaVu Sans 图内 title/轴约 7–8 pt，caption/正文 Nimbus Roman 约 9–10 pt；regular。近似色为 #1F77B4（return 曲线）、#D9D9D9（grid）和 #000000（文字）；单曲线加 panel 标题使灰度仍可读，`grayscale_safe=true`。
- **Caption**：`Figure 6: Learning curves for HotPotQA and BabiLong QA2 runs. Both graphs show the average episodic return with respect to training time.`（22 词）。动作是 `title`、`setup`；caption label regular，self-contained=true、main_finding_stated=false。
- **数据与证据关系**：曲线展示两个训练 run 的 average episodic return，正文/Appendix D 用它支持“初始快速上升、随后 plateau、约 12 小时内收敛”的效率叙事；图实际 x 轴约 6 小时以内，12 小时是训练上限而非图中可见终点。无 seed 平均、error band 或 wall-clock 硬件分解。它是 Appendix D 对单 A100/复杂度主张的定性补充，不是跨方法 training-cost 对照。
- **优点**：两任务使用同一 return 语义和近似 y 范围，快速上升与 plateau 直观；无 legend 减少重复。
- **缺陷**：没有多 seed 或 baseline，曲线的训练/评测频率和 12 小时边界未写入 caption；BabiLong/HotPotQA 的 x 范围不同，不能直接比较收敛小时数。
- **可复用范式**：用并排单曲线展示训练动态时固定 y 语义、明确单位和 run/seed，并在 caption 区分“可见曲线终点”和“训练预算上限”。

## Table 7（p.25，appendix）

- **类型、版面和复杂度**：`main_comparison`、`robustness`、`dataset`。page-width、17 列、7 个方法数据行，四个 dataset groups（HotPotQA、MuSiQue、MuSiQue (OOD)、Average）各含 Fact F1/EM、Ans F1/EM；单层指标子表头加 group header，booktabs 顶/底线和组间竖分隔线。
- **表头与编码**：Methods 之外共 16 个指标列；行包含 Plan Q-RAG/Q-RAG/Beam Retriever（均配 QwQ-32B）、Search-R1、Search-o1、GraphReader、HippoRAG。最佳值粗体、第二名下划线，缺失为短横线；最大两位小数。没有不确定性列。
- **Caption**：`Table 7: Comparison of methods on HotPotQA-distractors, MuSiQue (in-distribution), and MuSiQue (OOD). Bold text and underline denote the best and second best scores respectively.`（24 词）。动作是 `title`、`setup`、`encoding_key`、`comparison`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：聚合 Fact/Ans EM/F1 点估计，无 seed/区间/显著性；缺失表示原方法没有对应数据/指标。它扩展 Table 2 的 HotPotQA/MuSiQue OOD 主比较，新增 HotPotQA-distractors 和 MuSiQue in-distribution，支持正文“OOD 泛化”和 Appendix E 的 robustness 叙事；平均列只保留 Ans F1/EM，仍混合不同方法报告来源。
- **优点**：同一表同时显示 distractors、ID 和 OOD，能看出 Beam Retriever 的 in-domain 优势与 Q-RAG 的 OOD 保持；Fact/Ans 两层指标和 best/second 高亮规则沿用 Table 2。
- **缺陷**：17 列导致文字极小，Search-o1/GraphReader/HippoRAG 大片缺失使比较面不对称；caption 没有说明各方法的训练/reader 设置、样本分母和平均列的范围。
- **可复用范式**：当主表只覆盖一个 OOD 切片时，在附录用相同列 schema 添加 ID/distractor/OOD，并保持 best/second 规则和缺失标记一致，同时把比较同质性写清楚。

## Table 8（p.26，appendix）

- **类型、版面和复杂度**：`experimental_design`、`reproduction`、`dataset`。page-width、6 列、5 个配置行、单层表头；Dataset、Setting、Chunk size、T、Backbone retriever、Answering LLM。booktabs 顶/底线和表头底线，无竖线；整数配置无小数。
- **表头与编码**：行覆盖 HotPotQA Q-RAG/Plan Q-RAG、HotPotQA early stopping、MuSiQue、BabiLong、RULER；chunk size 为 tokens，T 为 maximum retrieval steps，retriever/answerer 直接列模型名。无粗体、下划线、颜色或不确定性。
- **Caption**：`Table 8: Retrieval and generation configuration for each dataset. Chunk size is in tokens; T is the maximum number of retrieval steps.`（21 词）。动作是 `title`、`setup`、`encoding_key`；caption label regular，self-contained=true、main_finding_stated=false。
- **不确定性、数据与证据关系**：不是结果估计，无不确定性；它把主文 Table 1/2/4 与 Appendix B 的 retrieval budget、chunk segmentation、backbone retriever、LLM answerer 配置绑定起来。与 Appendix G 的文字说明互补，能解释 HotPotQA 的 220/256 token chunk、BabiLong/RULER 的 64 token chunk 以及 T=2/4/5；没有 seed、解码温度或训练时长列。
- **优点**：把跨数据集的关键检索/生成边界压缩成可复现配置表，模型名用等宽字体较易定位；caption 明确定义 chunk size 与 T 的单位。
- **缺陷**：Setting 列含多个变体，无法从单行看出 fine-tuning 数据或评测 split；没有硬件、seed、decoder 参数和样本数；附录最后大块留白，配置表没有利用空间提供这些边界。
- **可复用范式**：在结果表附近提供独立 configuration table，把数据集、chunk、步数、retriever、reader 放在同一行，并追加 seed/decoder/split 列避免“可复现”只剩模型名。

## 跨对象关系与最终判断

### 视觉叙事

Figure 1 先把 state/action embedder、Q policy 和环境闭环固定为方法接口；Figure 2 与 Table 1 展示 BabiLong/RULER 的 context scaling，Table 2 展示 HotPotQA/MuSiQue 的 open-domain transfer。Figure 3、Table 3、Table 4 接着隔离 soft-Q、target、RL、α/λ 和 retrieval budget。Appendix B 的 Figure 4、Table 5、Figure 5、Table 6 把动态 stop 的错误—长度—质量 trade-off 展开；Appendix D Figure 6 给训练曲线，Appendix E Table 7 扩展数据切片，Appendix G Table 8 固化配置。主线完整覆盖“方法接口→长上下文/开放域结果→组件和预算消融→停止机制与复现细节”，但 relative positional mechanism 没有独立删除或替代对照。

### Caption 与表头系统

Figure caption 多为 regular Nimbus Roman 9–10 pt，通常依次写 title、setup、panel/encoding；Figure 2、4、5 定义线型或 panel 语义，Figure 1、3、6 更依赖正文解释。Table 1/2/4/7 caption 提供设置、缩写或 best/second 规则，Table 5/6 caption 过短，列含义依赖正文。表头普遍使用居中的 dataset/metric 分组和 booktabs 规则；Table 3/5/6/8 采用更简洁的单层表头。视觉系统没有统一写出 uncertainty、seed、sample denominator 的表注模板。

### 证据强度与主要缺口

最高价值的证据闭环是 Figure 1→Table 3：方法图中的 soft-Q/target/RL 组件被 QA3 多长度、三 seed 的 ablation 直接拆开；Figure 2→Table 1 共同支持 context scaling，但 Figure 2 多数 baseline 是 reported、Table 1 的长长度 coverage 不对称。Table 2/Table 7 把 fact retrieval 与 answer generation 分开并覆盖 OOD，但 Beam Retriever 使用 oracle hop count，跨方法成本边界不完全同质。Figure 4/5 与 Tables 5/6 对 early stopping 的机制拆解最完整，却缺少分母、seed 和区间。Figure 6 只显示两条单 run 矢量曲线，不能单独支撑跨方法 wall-clock 优势。论文在 Appendix A 有理论证明但没有对应图表；relative temporal position 也没有独立 ablation。

### 最可复用模式

1. 用 Figure 1 的闭环状态转移图，把方法符号、候选动作、策略和奖励反馈放在一条可追踪路径上，再由公式和算法逐项落地。
2. 用 Figure 2 的双面板 context-scaling 轴，把总体平均与最难子任务并置，并用线型而非仅颜色区分 fine-tuned/zero-shot。
3. 用 Table 3 的同轴删除组件设计，把训练机制的必要性和波动直接放在最难任务上；用 Table 4 同时列 retrieval/answer 指标观察预算 trade-off。
4. 用 Figure 4/5 与 Table 5/6 的阈值链，将错误类型、perfect stop、episode length、ROC 和任务质量绑定到同一 threshold，而不是只报告单一最优点。

### 失败模式

1. Figure 2 的多色、双 legend 和异源 baseline 让方法比较很密集，缺少 uncertainty、分母和 provenance 的视觉编码。
2. Table 2、Table 7 的 best/second 高亮容易被读作同质实验结果，实际含 reported/reproduced、oracle hop count 和缺失指标混合。
3. Figure 3、Figure 6 及 Appendix B 图表都没有统一 seed/误差模板；Figure 6 的“约 12 小时”是训练上限叙述，不是曲线内可见的跨方法成本测量。
4. Figure 1 解释了 relative position 的接口方向，但没有与不使用该机制的图表对照；因此 temporal reasoning 结果支持相关性而非独立因果贡献。

**一句话视觉策略**：以 Figure 1 的多步检索闭环为视觉锚，用 context-scaling 主图和分层结果表承载性能，再以组件/预算/停止阈值的同轴消融和附录配置表闭合“效果—机制—成本—复现”证据链，同时显式标注 baseline provenance、分母和不确定性。

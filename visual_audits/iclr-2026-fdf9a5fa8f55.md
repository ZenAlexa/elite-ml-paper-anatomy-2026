# 视觉审计 — iclr-2026-fdf9a5fa8f55

## 范围、事实源与完整性

- **论文**：*Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training*（ICLR 2026 oral）。
- **PDF 事实源**：/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/pdfs/iclr-2026-fdf9a5fa8f55.pdf。readings/iclr-2026-fdf9a5fa8f55.json 记录的官方 proceedings PDF 为 https://proceedings.iclr.cc/paper_files/paper/2026/file/2b5c5689fae6fa9a4883e73e511d52c8-Paper-Conference.pdf，OpenReview 页面为 https://openreview.net/forum?id=0wSlFpMsGb。PDF 为 letter、双栏、34 个物理页；正文结束于 p10，参考文献为 p11–18，Appendix A 从 p19 开始。
- **渲染与检查**：完整 PDF 以 pdftoppm -png -r 200 渲染到 /tmp/iclr-2026-fdf-render/page-01.png–page-34.png（每页 1700×2200 px，超过 180 dpi）。逐页检查了全部 34 页，并对含视觉对象的 p2、p3、p5、p9、p10、p19、p20、p21、p23、p24、p26、p32、p33、p34 做了 200 dpi 高分辨率检查；使用 pdfimages -list、pdffonts 与 pdftotext -layout 交叉核对 PDF 对象、字体对象、caption 和表格文本。
- **对象清单**：PDF 最终清单为 5 幅 Figure、14 张 Table，共 19 个对象。正文为 Figure 1–4、Table 1–2；附录为 Figure 5、Table 3–14。readings/...json 的 visual inventory 与 reports/tables/visual_inventory_pdf.csv 逐项一致，标签和页码没有 reading-only 或 pdf-only 差异。reading 中 p8 的 algorithm/not_present 是全文没有 algorithm/pseudocode block 的记录；按协议算法不进入 Figure/Table 数组。
- **核对重点**：PDF 中的小图、组合图、地图、treemap、t-SNE、qualitative density grid、长表和双层表头均按一个所属 Figure/Table 计数；表格跨行的换行不拆成新对象。

## 公开视觉源获取

reports/tables/visual_source_inventory.csv 将本论文标为 no_public_source_found，reports/tables/visual_source_files_local.csv 没有该论文行，corpus/visual_sources/iclr-2026-fdf9a5fa8f55/ 也没有文件。随后按“PDF 链接 → OpenReview → inventory/local → 完整标题/GitHub”的顺序核查：

- PDF 首页显示项目名 PleIAs/common_corpus，但没有可直接解析的论文绘图仓库 URL；正文和 Appendix F 明确提到 PleIAs/Segmentext、PleIAs/OCRoscope、PleIAs/OCRerrcr、PleIAs/OCRonos、PleIAs/celadon。以 PDF 中的大小写路径调用 gh repo view 时，前者及 OCRerrcr/OCRonos/celadon/两个模型 preview 仓库均未找到。
- gh repo view 找到的相关公开仓库包括 Pleias/OCRoscope（OCR 质量评估包）、Pleias/open_data_toolkit（开放数据处理工具）、Pleias/toxic-commons（Toxic Commons/Celadon）、Pleias/synthetic-ocr（合成 OCR 修正脚本）、Pleias/nanotron-pleias（训练框架）和 Pleias/pleias_ScholasticAI。读取这些仓库的默认分支树后，未发现与本文 Figure/Table 对应的 plot*、figure*、visual*、table*、.ipynb、.tex、.tikz、.pgf、.svg 或图表数据文件；它们只能证明工具/训练代码存在，不能作为本文视觉源。
- inventory 自动候选 aboSamoor/pycld2、natliblux/nautilusocr、nlpaueb/edgar-crawler 以及搜索候选 Xiaocanran1230/awesome-data-problems-for-foundation-models 与本文的 Figure/Table 源没有直接关系。完整标题和方法名的 GitHub 检索也没有找到 Common Corpus 的可编辑视觉源。
- 因此 JSON 的 source_acquisition.status 为 **no_public_source_found**，selected_repository 为 null，visual_source_files 为空。下文涉及字号、HEX、线宽和渲染类型的数值均来自 PDF 对象或 200 dpi rendered estimate；没有把工具仓库的代码或截图冒充本文绘图源。

## 论文级视觉风格

- **版式与密度**：页面为 letter 双栏，但 Figure 1–4 和 Table 1–2 使用跨双栏的宽浮动体；附录的 Figure 5 及长表也占页面主体宽度，Table 4、Table 9、Table 10 是居中的窄 inset。正文 Figure 1/2/3 先给 corpus 的组成、语言和时间/语义结构，Figure 4 给质量分布，Table 2 连接到模型效能；附录把数量、来源和逐语言分数展开。
- **字体**：pdffonts 显示页面主体/Caption 以 Nimbus Roman No9 L（regular、medium、italic）为主，数学符号使用 CMSY/CMMI；表格中也出现嵌入的 Palatino Type3 和 Dingbats，等宽元数据/工具名使用 NimbusMonL，Figure 5 的绘图字形可见 DejaVu Sans。正文与 caption 字体对象稳定，图内字号由 200 dpi 渲染估计约 6–10 pt（个别地图/图例更小），caption inventory 的 PDF 对象约 9.963 pt。
- **颜色**：六个 collection 在 treemap、timeline、density histograms 中复用粉/橙/黄/绿/蓝/紫家族；Figure 2 用连续紫—粉—橙—黄 colorbar；Figure 5 使用紫到黄的七色 tokenizer 序列。颜色经常配合标签、空间位置或形状，但六 collection 和 tokenizer 对灰度不完全安全。
- **矢量/栅格**：图表线、矩形、文字和表格规则主要是 PDF vector paths/text；Figure 2 的地图/点图含 raster 或嵌入图层，PDF 也含若干模板/链接相关的小图像对象。故 Figure 1、3、4、5 与表格记为 vector 或以向量为主的 mixed，Figure 2 记为 mixed，不把 pdfimages 中的通用小资源解释成整幅图的视觉源。
- **一致性**：无竖线的横向 booktabs 表格和 Nimbus Roman caption 形成稳定的出版系统；六 collection 的颜色形成数据系统。Figure 2 的连续色标、Figure 5 的 tokenizer 色序和正文表格的黑白符号是局部子系统，图内字体并非完全统一。

## Figure 1 — collection 与语言的 treemap

- **位置/职责**：p2，§2 About Common Corpus，正文 main，跨双栏 page_width。类型 tree + conceptual_diagram；用途 headline、method_interface、dataset；复杂度 3/5，单一画布、六个一级 collection 区块及多个语言子块。
- **布局与图形语法**：矩形面积按 collection/语言层级编码，一级区块从左到右/上下分布，内部以细白边界分割语言；下方共享图例依次给出 Open Science、Open Semantic、Open Source、Open Web、Open Culture、Open Government。无 x/y 坐标轴、网格、参考线或误差表示；direct label=true，白/黑文字嵌在矩形中，约 0.5 pt 边界线。渲染以 vector text/paths 为主，局部颜色块含混合嵌入。
- **编码与数据**：x/y 是 treemap 的空间布局，不是测量轴；面积表示 collection 与最流行语言在语料中的相对份额，颜色表示六个 collection，文字给出语言/Other。图中没有数字刻度、文档分母或不确定性，读者只能做结构和相对面积判断。
- **颜色/字体**：六个类别的渲染估计色为 #E84775（Open Science）、#F48440（Open Semantic）、#F7C638（Open Source）、#3A9775（Open Web）、#2B79A8（Open Culture）、#8A608E（Open Government）；颜色模式 categorical，约 6 色，标签提供冗余但灰度下区块差异下降。Nimbus/Palatino 风格图中文字约 7–10 pt，regular/medium，roman；字号/HEX 为 rendered estimate。
- **Caption（PDF 逐字，13 个空白分词）**：Figure 1: Proportional treemap of Common Corpus collections and their most popular languages. 只有 title；未定义颜色、面积、Other 或数字含义，未给主发现，脱离图例不能完全自洽。
- **证据关系**：引言关于规模、开放许可和多语言覆盖的主张 → §2 的六 collection 接口 → Figure 1 作为 corpus headline 概览 → Figure 2 的语言地理分布、Figure 3 的时间/语义结构 → Appendix B/D 的精确数量与来源表。
- **优点**：一个画布同时给出层级和相对规模，六 collection 的图例固定了后续 Figure 3/4 的语义；短 caption 和大面积区块使整体定位迅速。
- **缺点**：面积的具体值和归一化分母不在图中；小语言块与 Other 的颜色/字号在缩放和灰度下难以辨识；caption 没有把 collection 与下游评测连接起来。
- **可复用模式**：用一级 collection—二级语言的面积树形结构交代大语料组成，再在附录表给出可审计的绝对文档/词/token 计数。
- **证据**：PDF p2 Figure 1 及其 caption，basis=rendered_observation，bbox 未强行推断。

## Figure 2 —语言分布地图

- **位置/职责**：p3，§2，正文 main，page_width。类型 map + scatter；用途 dataset、qualitative_evidence、method_interface；复杂度 3/5，单地图、多语言点和一个连续色标。
- **布局与图形语法**：浅灰世界底图上放置语言点；点的位置是作者选取的代表城市/区域，点色按文档数映射到下方水平 colorbar。无经纬度轴和网格，地图读作地理示意而非经纬度测量；legend_present=true，位置 bottom_center，颜色语义共享；direct label=false；无线型/hatching/reference line/error bar。地图和点层表现为混合 vector/raster，近似线宽 0.4–0.6 pt。
- **颜色/字体**：连续色标从深紫到紫粉、橙再到黄，约 #2E0F6D、#762A8A、#B73786、#E36B60、#F59B3E、#F8C83D、#FDE725；模式 sequential，颜色语义为 Total number of documents (log-scale, 10^N)，没有第二编码，灰度区分较弱。刻度/色标字体约 7–8 pt，Nimbus/Palatino，rendered estimate。
- **数据与统计**：仅纳入文档数 10,000+ 的语言；颜色编码每种语言的文档数的 log-scale，图面刻度为约 4.5–8.0（10^N）。没有点级语言名称、样本重复或不确定性。城市位置是“该语言最 specific 的区域”的示意选择，不能作为语言边界或人口估计。
- **Caption（PDF 逐字，48 个空白分词）**：Figure 2: A schematic world map of languages in Common Corpus with a log-scaled distribution of document counts. For each language, we chose a city that is located in the region where this language is most specific to. To avoid outliers, we show only languages with 10,000+ documents. 包含 title、setup、encoding_key、筛选规则；没有具体主发现，但与色标和图面合在一起基本自洽。
- **证据关系**：§2 关于高/低资源语言和多语言覆盖 → Figure 2 的地理/规模入口 → Appendix B Table 5 的 top-50 language 绝对计数 → Figure 5/Appendix G 的 tokenizer 与逐语言评测。
- **优点**：连续色标把数量级压缩到全球视图；阈值和 log-scale 在 caption 明示，底图为跨语言比较提供直观空间索引。
- **缺点**：点没有语言名，密集的欧洲/亚洲点难以逐一追溯；城市代理位置可能被误读为语言地理边界；颜色和点重叠在灰度、小屏幕下不利于核查。
- **可复用模式**：地图只承担覆盖和数量级导航，把逐语言名称、绝对值和长尾排序转移到配套表格，并在 caption 写清阈值与地理代理规则。
- **证据**：PDF p3 Figure 2 及 colorbar/caption，basis=rendered_observation。

## Figure 3 —时间与语义结构

- **位置/职责**：p5，§3/Related Work 相邻，正文 main，跨双栏 page_width。类型 area、line、scatter、qualitative_grid；用途 headline、dataset、qualitative_evidence；复杂度 4/5，两个并列面板、六个 collection 及 FineWeb/C4 对照。
- **布局与图形语法**：左 (a) 为约 1450–2020 的时间轴、文档计数 log y 轴的多色叠加面积/线图；右 (b) 为 t-SNE Component 1/2 的散点图，背景有半透明类别区域/椭圆。两面板各有内部 legend（a 左上、b 右上），不共享 legend；a 的 x=time、y=log，b 的两轴为线性 t-SNE 坐标，因此 JSON 的复合图 scale 标为 unknown 并在编码中保留面板差异。右图有 x/y 网格，左图以 log tick 和面积层次为主；direct label=false，marker 类型 1，line style 1，无 reference line，ellipse/distribution 作为不确定性/密度语义，线宽约 0.7 pt。
- **编码与数据**：面板 (a) 颜色编码六 collection 随时间出现和文档量；面板 (b) 点位置编码 t-SNE 投影，颜色区分 FineWeb、C4、Open Source、Open Web、Open Culture、Open Government、Open Semantic、Open Science，半透明椭圆/区域显示局部聚集。图面是样本/投影概览，未给 t-SNE 参数、抽样分母或重复稳定性。
- **颜色/字体**：渲染中复用 collection 的蓝/粉/紫/黄/绿，右图另有 FineWeb、C4 的浅色；约 8 色，模式 categorical，标签和面板位置提供少量冗余，灰度下类别分离下降。图内字体约 6–8 pt，Nimbus/DejaVu 混合，rendered estimate。
- **面板子 caption（图内逐字）**：(a) A timeline of the main collections with their numbers of documents in the Common Corpus.；(b) A two-component t-SNE visualization of subsets of Common Corpus collections, C4, and FineWeb.
- **Global caption（PDF 逐字，11 个空白分词）**：Figure 3: Temporal and semantic overview of the Common Corpus collections. 只有 title；面板子 caption 解释图型，global caption 未说明 log 轴、抽样或 t-SNE 参数，self-contained=false、main_finding_stated=false。
- **证据关系**：正文关于 Common Corpus 与 crawl corpora 的低重叠/不同内容 → Figure 3(a) 的时间覆盖和 3(b) 的语义分离 → Appendix B/D 的 collection 绝对规模和来源 → Figure 4 的质量分布与 Table 2 的模型效能。
- **优点**：时间覆盖与语义差异并置，把 corpus 的“多样性”拆成两个可见维度；对照 FineWeb/C4 让 collection 的相对位置进入同一坐标阅读路径。
- **缺点**：t-SNE 的非度量性质和抽样规则未写入 caption；面积叠加让小 collection 在左图被遮蔽；颜色在多个面板中承担过多类别。
- **可复用模式**：用同一 Figure 的时间面板和语义投影分别承载 coverage 与 distributional difference，并在附录固定抽样/降维配置和绝对计数。
- **证据**：PDF p5 Figure 3 两面板、子 caption 与 global caption，basis=rendered_observation。

## Figure 4 —文档质量指标分布

- **位置/职责**：p9，§6 Evaluation，正文 main，page_width。类型 histogram、area、qualitative_grid；用途 qualitative_evidence、mechanism、dataset；复杂度 4/5，2×3=6 面板、每面板六个 collection。
- **布局与图形语法**：六个面板分别为 Character Repetition、Type-Token Ratio、Top Word Proportion、Alphanumeric Characters、Whitespace Characters、Uppercase Characters；每个 x 范围约 0–1、y=Density，叠加/堆叠填充密度直方图；x/y 为 linear，网格主要为 x/y 的浅灰线；共享 bottom legend，位置 bottom_center，六个 collection；无 direct label、marker、reference line、hatching、error bar 或 band，边界线约 0.5 pt。
- **颜色/字体**：六色为粉 #ED6F93、橙 #F69F69、黄（约 #F6C344）、绿 #65AE93、蓝 #5996BB、紫 #A383A7，模式 categorical；legend 与 panel 标题提供文字冗余，但颜色的堆叠顺序在灰度下不易分辨。DejaVu/Nimbus 图内约 6–8 pt，rendered estimate。
- **数据与统计**：caption 明确是 300,000-document sample，x 为六种文档级组成/质量指标，y 为 probability density；正文指出 code 的 repetition/whitespace 和 Open Government 的 linguistic diversity 偏离。没有分 collection 的样本数、带宽、置信带、误差、重复或失败值；“stacked”让每层厚度与总密度同时可读，但不应解释为 collection 的份额。
- **Caption（PDF 逐字，27 个空白分词）**：Figure 4: Stacked histograms of probability density for qualitative evaluations of Common Corpus on a sample of 300,000 documents. Metric descriptions can be found in Appendix G. 含 title、setup、appendix_pointer；metric 定义被移至 Appendix G，未陈述具体主发现，self-contained=false。
- **证据关系**：§5 清洗/质量目标 → Figure 4 对 300k 文档的质量分布 → Appendix G 的六个 metric 定义 → Table 2 的下游 benchmark。图支持“分布整体合理、collection 有预期偏离”的定性判断，不提供治理效果的因果比较。
- **优点**：六个指标同构布局、共享 x 范围和 legend，便于横向扫描；填充面积能快速展示峰值和长尾。
- **缺点**：多层透明填充遮蔽较小类别；没有样本量与不确定性，density 峰差可能受带宽影响；caption 依赖附录才能解释指标。
- **可复用模式**：把同一 quality schema 放入 2×3 small multiples，统一坐标和 legend；若用于决策应额外显示每层 n、带宽/重复规则和可验证阈值。
- **证据**：PDF p9 Figure 4 六面板和 caption，basis=rendered_observation。

## Figure 5 —多语言 tokenizer fertility

- **位置/职责**：p21，Appendix C Tokenizer Details，附录，page_width。类型 bar + qualitative_grid；用途 main_comparison、efficiency_cost、qualitative_evidence；复杂度 5/5，2×3=6 面板、每面板 7 个 tokenizer、42 根柱。
- **布局与图形语法**：English、French、German、Italian、Polish、Spanish 六个面板，x 为 7 个 categorical tokenizer（mBERT、GPT-2、SmallLM 2.7B、Llama 3.2 1B、Qwen 3 1.7B、Gemma 3 1B、Ours 1B），y=Fertility (tokens per word) linear；面板 y 上限不同，柱顶直接标两位小数。无 legend（x 标签自解释）、无网格/marker/line/reference、无误差条或 band；direct_labels=true，约 0.6 pt 柱边界。
- **颜色/字体**：七色顺序约为 #440154、#443983、#31688E、#21918C、#35B779、#90D743、#FDE725，模式 categorical，直接 x 标签和数值标签形成冗余；灰度下相邻颜色仍可能混淆。DejaVu Sans 图内约 6–8 pt，regular/bold，rendered estimate。
- **数据与统计**：FLORES-200 devtest，比较六种语言上每词 token 数；caption 和正文给出 Ours 1B 及 65,536 vocabulary，正文称其只被 Gemma 3 超过且 Gemma tokenizer 词表约四倍大。图面只有点估计，未给 devtest 样本数、方差、区间或 tokenizer 推理成本。
- **Caption（PDF 逐字，36 个空白分词）**：Figure 5: Comparing the fertility of PleIAs tokenizer (marked as “Ours 1B”) and other language models for six languages. The data source for all languages is the devtest set of FLORES 200 (Costa-jussà et al., 2022). 含 title、setup、encoding_key/data source；未写出“只被 Gemma 超过”的主发现，图面与 caption 合起来基本自洽。
- **证据关系**：Appendix B 对 BPE token counts 的定义 → Figure 5 检查 tokenizer fertility → Table 3/5 的词/token 规模 → Table 2 与 Tables 11–14 的下游 multilingual results。它是 token 数量解释的校验图，不是模型质量主结果。
- **优点**：六面板同构、数值标签直接可读，Ours 1B 在不同语言的相对位置清晰；数据源和 devtest 入口写进 caption。
- **缺点**：每个 panel 的 y 上限不一致，跨语言高度比较容易误读；七色编码重复 tokenizer 顺序但没有图例；无不确定性或 tokenization failure 信息。
- **可复用模式**：对多个语言/域使用同构 grouped bar，并直接标值；跨 panel 比较时固定 y 轴或在 caption 中强调每 panel 独立尺度。
- **证据**：PDF p21 Figure 5 六面板与 caption，basis=rendered_observation。

## Table 1 — 四维 dataset taxonomy

- **位置/结构**：p5，Related Work，main，跨双栏 page_width；用途 headline、main_comparison、dataset。表头 1 层、9 列（stub criterion + KL3M、Dolma、C4、ROOTS、DCAD 2000、FineWeb 2、Common Pile、Common Corpus），4 行指标：Multidomain、Beyond Web Crawl、Multilingual、Open data；无 body row group。
- **表头/规则/高亮**：横向 booktabs（top/header/bottom），无竖线；绿色 ✓ 与黑色 ✗ 是 text_color/符号高亮，不是性能排序；小数精度不适用。表头长名以换行压缩，指标方向由行名给出。
- **Caption（PDF 逐字，10 个空白分词）**：Table 1: Comparison of the contemporary datasets for LLM training. 只有 title，未解释 ✓/✗ 的定义或四项标准，self-contained=false、main_finding_stated=false。
- **数据与统计**：四个布尔覆盖标准的 qualitative matrix，Common Corpus 在四行均为 ✓；无样本、分母、误差或 failure 值。
- **证据关系与评价**：引言关于既有语料单语/网页限制 → Table 1 四维定位 → Figure 1/2 的多域多语言结构 → Table 2 的效能。优点是一个视图给出论文定位；缺点是 ✓/✗ 把多域和开放程度压成二元，无法表达质量、规模或法律边界的梯度。可复用模式是用明确的 criterion 行做 taxonomy，但应在 caption 或脚注定义判定规则。
- **证据**：PDF p5 Table 1 与 caption，basis=rendered_observation。

## Table 2 — 聚合 benchmark 结果

- **位置/结构**：p10，Evaluation，main，跨双栏 page_width；用途 main_comparison、headline、qualitative_evidence。表头 2 层、9 列：stub Model；两个列组（350M：Ours 350M、Gemma 3 270M、XGLM 564M、BLOOM 560M；1B 级：Ours 1.2B、Gemma 3 1B、XGLM 1.7B、OLMo 1B），3 个 benchmark 行 MultiBLiMP、XStoryCloze、XCOPA；列组按模型规模形成 2 个 header groups。
- **表头/规则/高亮**：横向 booktabs、无竖线；三位小数一致；PDF 中没有系统性粗体/下划线或 cell fill，highlighting=none。模型名与规模分两层，任务名作为 stub。
- **Caption（PDF 逐字，13 个空白分词）**：Table 2: Benchmarking results. “Ours” refers to PleIAs models pre-trained on Common Corpus. 含 title 与 Ours 定义；未说明每项聚合方式、评测分母、seed 或不确定性。
- **数据与统计**：三个任务的 aggregate score；正文说明模型在 2944/23040 H100 hours 上训练并用 LM Evaluation Harness 评测。表中点估计：MultiBLiMP Ours 350M/1.2B 为 0.774/0.797，Gemma 为 0.762/0.799；XStoryCloze Ours 为 0.509/0.526，XCOPA 为 0.533/0.541。无区间、重复、失败数、成本同列或每语言分母。
- **证据关系与评价**：§6 模型训练与三个 benchmark → Table 2 aggregate utility → Appendix G Tables 11–14 的逐语言异质性。优点是把模型规模、对照和三个任务压进同一阅读面；缺点是聚合隐藏低资源语言差异，且没有 uncertainty/成本列，无法单凭表格判断稳定性。可复用模式是双层 model-size header，但应在脚注附评测样本、聚合方向和重复规则。
- **证据**：PDF p10 Table 2 与 caption，basis=rendered_observation。

## Table 3 — collection 总量

- **位置/结构**：p19，Appendix B Corpus Composition，附录，page_width；用途 dataset、reproduction。4 列（Dataset、Documents、Words、Tokens），1 层表头，6 个 collection 行加 Total 总结行，共 7 body rows，Total 是 1 个 summary row group。
- **规则/表头**：横向 booktabs，Total 前后用横线分隔，无竖线；整数逗号分组、无小数；无高亮、无 uncertainty。表头直接写出三个计数单位，Words 在 caption 中定义为 whitespace-separated。
- **Caption（PDF 逐字，21 个空白分词）**：Table 3: Dataset composition of Common Corpus. For each collection, we report the total number of documents, words (whitespace-separated), and tokens. 有 title、setup/unit 定义，未提供误差或主发现。
- **数据与统计**：Open Government 75,652,998 docs / 257,561,830,682 words / 407,067,554,189 tokens；Open Culture 93,156,602 / 549,608,763,966 / 885,982,490,090；Open Science 19,220,942 / 147,305,783,453 / 281,193,563,789；Open Code 202,765,051 / 77,669,169,092 / 283,227,402,898；Open Web 96,165,348 / 33,208,509,065 / 73,217,485,489；Open Semantic 30,072,707 / 23,284,201,782 / 67,958,671,827；Total 517,033,648 / 1,088,638,258,040 / 1,998,647,168,282。总量是聚合 count，不是估计区间。
- **证据关系与评价**：Figure 1 面积/collection → Table 3 精确总量 → Tables 4–10 的许可证、语言和来源分解 → Table 2 模型训练语料规模。优点是三种计数并排且 Total 清晰；缺点是没有说明 collection overlap/去重关系或 tokenizer 的版本细节。可复用模式是把总量、分母和计数定义放在同一表头/Caption。
- **证据**：PDF p19 Table 3，basis=rendered_observation。

## Table 4 — license token counts

- **位置/结构**：p19，Appendix B，居中 inset；用途 dataset、reproduction。2 列（License type、Tokens），1 层表头，10 个 license rows，无 row group，整数计数。
- **规则/高亮**：booktabs、无竖线；无粗体/下划线/颜色高亮；精度为 0（逗号分组）；没有 uncertainty、license validity interval 或 unknown category。
- **Caption（PDF 逐字，13 个空白分词）**：Table 4: Token counts for the ten most common licenses in Common Corpus. 只有 title，未说明排序、license normalization 或长尾截断。
- **数据与统计**：Public Domain 1,138,508,375,958；CC-By 287,749,264,457；MIT 142,694,227,607；CC-By-SA 74,768,060,836；Apache-2.0 68,750,977,037；BSD-3-Clause 18,483,944,333；Open license 10,432,513,767；BSD-2-Clause 5,497,145,480；CC-BY-4.0 2,110,966,243；CC0-1.0 1,877,206,195。计数按 token 聚合，没有置信区间/重复。
- **证据关系与评价**：Table 3 总量 → Table 4 许可证组成 → Appendix E 权利核验规则 → “fully open”定位。优点是把最大 license categories 定量化；缺点是 Open license 与 CC 变体的归并规则没有表内说明。可复用模式是用窄 inset 递送长尾前十项，但需显式写排序和归一化。
- **证据**：PDF p19 Table 4，basis=rendered_observation。

## Table 5 — top-50 languages

- **位置/结构**：p20，Appendix B，page_width；用途 dataset、reproduction、qualitative_evidence。4 列（Language、Documents、Words、Tokens），1 层表头、50 body rows，无 row group，按 token count 降序。
- **规则/表头**：booktabs top/header/bottom、无竖线；所有计数为整数逗号格式、精度 0；无高亮或 uncertainty。表头对语言名、文档、词和 token 的分母直白。
- **Caption（PDF 逐字，33 个空白分词）**：Table 5: Top-50 languages in Common Corpus by token count. Each language is presented with its number of documents, words, and tokens in the corpus. The rows are ordered by the token count. 含 title、setup、排序说明；没有 tokenizer 版本，但正文说明 BPE tokenizer 并指向 Figure 5。
- **数据与统计**：50 行从 English（154,175,907 docs；968,757,721,747 tokens）到 Basque（439,582；348,891,265 tokens），并同时报告 Words。排序以 tokens，不等同 documents 排序；没有区间、语言识别准确度或长尾截断误差。
- **证据关系与评价**：Figure 2 地图的数量级 → Table 5 可审计的 top-50 → Figure 5 tokenizer fertility → Tables 11–14 逐语言 benchmark。优点是把语言、词和 token 放在同一行；缺点是 50 行密度高、未给语言识别/多标签规则。可复用模式是“排序指标 + 同行辅助分母”，并在 caption 说清排序列。
- **证据**：PDF p20 Table 5，basis=rendered_observation。

## Table 6 — Finance Commons 来源

- **位置/结构**：p21，Appendix D.1，附录，page_width；用途 dataset、reproduction。4 列（Dataset、Main Languages、Documents、Tokens），1 层表头，5 个来源行（SEC、WTO、AMF、TED EU Tenders、GATT Library），无 body row group。
- **规则/表头**：横向 partial grid：top/header/bottom 规则并以若干横线分隔长行，无竖线；整数计数、精度 0；长语言列表在第二列自动换行；无高亮或 uncertainty。
- **Caption（PDF 逐字，8 个空白分词）**：Table 6: Finance Commons sources distribution with languages. 只有 title；没有解释 Documents/Tokens 计数口径或来源排序。
- **数据与统计**：SEC English 1,085,113 docs / 9,653,919,837 tokens；WTO English/Spanish/French and small partitions 772,508 / 2,835,007,015；AMF French/English 595,397 / 9,823,755,281；TED EU Tenders 覆盖 German、French、Polish、Spanish、Dutch、Czech、Romanian、English、Swedish、Italian、Bulgarian、Finnish、Latvian、Danish、Lithuanian、Croatian、Estonian、Hungarian、Portuguese、Slovenian、Slovak、Greek、Irish，137,837 / 650,396,761；GATT Library English/French/Spanish/Catalan/Portuguese/German，67,596 / 224,526,628。均为聚合 count。
- **证据关系与评价**：Open Government 总量 → Table 6 Finance 来源/语言 → Appendix D.1 prose provenance → Table 3 的 collection 合计。优点是并列语言和规模；缺点是长语言列挤压可读性，caption 对 small partitions 和来源处理过短。可复用模式是宽表把来源、语言、文档和 token 放在同一行，长列表需要脚注或可检索附表。
- **证据**：PDF p21 Table 6，basis=rendered_observation。

## Table 7 — Legal Commons 来源

- **位置/结构**：p23，Appendix D.1，附录，page_width；用途 dataset、reproduction。3 列（Dataset、Languages、Tokens），1 层表头、9 个来源 rows：Caselaw Access Project、Court Listener、EUR-lex、Eurovoc、French open data、USPTO、UN Digital Library、European Open Data、OECD；无 body row group。
- **规则/表头**：partial grid，长语言列表以横线分隔行、无竖线；整数 token、精度 0；无高亮/uncertainty。来源名称与语言列的多行换行保持阅读顺序。
- **Caption（PDF 逐字，8 个空白分词）**：Table 7: Legal Commons sources distribution with languages. 只有 title，没有写 Eurovoc 的 39 languages 或行排序口径。
- **数据与统计**：Tokens 依次为 Caselaw Access Project 13,821,842,995；Court Listener 22,625,121,735；EUR-lex 65,044,763,781；Eurovoc 31,648,136,898；French open data 24,597,392,089；USPTO 200,509,900,178；UN Digital Library 1,781,037,875；European Open Data 7,098,502,579；OECD 584,969,458。Languages 列记录从单语到 EU 语言、多语 UN 数据的覆盖；没有不确定性或跨来源重复估计。
- **证据关系与评价**：Open Government/Legal Commons prose → Table 7 来源和语言 → Appendix D.1 的 provenance links → Table 3 Open Government token 总量。优点是把法律来源与语言覆盖绑定；缺点是 3 列宽表的长列表密集、未同时报告 document counts。可复用模式是把 provenance 的“来源—语言—tokens”最小闭环做成宽表，并将外部 URI 放在正文脚注。
- **证据**：PDF p23 Table 7，basis=rendered_observation。

## Table 8 — Open Culture 子集

- **位置/结构**：p24，Appendix D.2，附录，page_width；用途 dataset、reproduction。4 列（Corpus、Language、Domain、Tokens），1 层表头、26 个 body rows、无 body row group。
- **规则/表头**：横向 partial grid/booktabs 风格的 top/header/bottom 规则，无竖线；token 以一位小数的 B 单位（例如 174.2B、0.3B），精度 1；无高亮/uncertainty。长名称 New Zealand PD Newspapers、BnL Newspapers 在单元格中换行。
- **Caption（PDF 逐字，15 个空白分词）**：Table 8: Subsets of Open Culture with language coverage, type of document, and token count. 含 title、字段说明；没有解释 B 的数量级或后处理后与上游来源的差异。
- **数据与统计**：26 个 Open Culture 子集覆盖 English/French/German/Portuguese/Spanish/Italian/Dutch/Danish/Serbian/Czech/Greek/Polish/Latin/Russian/Arabic、Māori 和 multilingual；Domain 为 Books、Newspapers 或 Books and Newspapers；Tokens 从 English PD 174.2B、US PD Newspapers 199.3B、French PD Newspapers 110.8B 到多个 0.3B 子集。均为四舍五入到 0.1B 的聚合计数。
- **证据关系与评价**：Open Culture provenance → Table 8 的 source split → Table 3 collection total；与 Figure 1 的 Open Culture 面积、Figure 2/5 的语言覆盖互补。优点是把 domain 与 language 置于 token count 同行；缺点是四舍五入会隐藏小差异，未给文档/词分母。可复用模式是“子集—语言—文档类型—规模”的宽表，适合文化档案的多维 provenance。
- **证据**：PDF p24 Table 8，basis=rendered_observation。

## Table 9 — Open Science 来源

- **位置/结构**：p26，Appendix D.3，居中 inset；用途 dataset、reproduction。2 列（Dataset、Tokens），1 层表头，6 个 source rows 加 Total，共 7 rows、1 个 Total summary group。
- **规则/表头**：booktabs top/header/summary/bottom 规则、无竖线；整数 token、精度 0；无高亮/uncertainty。
- **Caption（PDF 逐字，8 个空白分词）**：Table 9: Token count by dataset Open Science. 只有 title，未把 Total 定义为 collection sum。
- **数据与统计**：OpenAlex 191,616,437,384；Open Science Pile 11,096,766,324；Open Science French 46,961,690,792；Open Science Spanish 16,523,491,767；Open Science German 7,806,446,050；ArXiv 7,188,731,472；Total 281,193,563,789。全部是 token count 点值。
- **证据关系与评价**：Open Science prose → Table 9 source sum → Table 3 Open Science total → Figure 3/4 的 collection 语义与质量。优点是 Total 清晰、窄表可快速复核；缺点是没有 source language/domain 或 document count。可复用模式是对每个 collection 给一个相同结构的 source total 表，并保持 Total 规则一致。
- **证据**：PDF p26 Table 9，basis=rendered_observation。

## Table 10 — Open Code top ten

- **位置/结构**：p26，Appendix D.4，居中 inset；用途 dataset、reproduction。2 列（Language、Tokens），1 层表头，10 个 body rows，无 row group。
- **规则/表头**：booktabs、无竖线；整数 token、精度 0；无高亮/uncertainty。按 token 规模降序，语言名包含 C++、C# 等代码标识。
- **Caption（PDF 逐字，9 个空白分词）**：Table 10: Token counts by programming language or framework. 只有 title，未写 top-ten 排序但正文写明。
- **数据与统计**：Java 35,697,451,454；JavaScript 28,894,772,110；Python 26,681,331,771；C++ 25,481,950,314；C 23,277,000,113；PHP 23,077,121,733；C# 16,806,995,110；Go 11,200,587,099；Rust 3,888,428,173；Ruby 3,718,918,983。没有代码识别误差或分母。
- **证据关系与评价**：Open Code provenance → Table 10 语言/框架分布 → Figure 1 Open Code 区块 → Table 3 Open Code 总量。优点是窄表直给排序；缺点是 language 与 framework 混在同一列且未说明归类。可复用模式是用紧凑 top-k 表补足 treemap 的相对面积。
- **证据**：PDF p26 Table 10，basis=rendered_observation。

## Table 11 — MultiBLiMP 语言 a*–i*

- **位置/结构**：p32，Appendix G，附录，page_width。9 列（Model stub + 8 model columns）、2 层表头：350M 组 Ours/Gemma 3/XGLM/BLOOM，1.2B/1B 组 Ours/Gemma 3/XGLM/OLMo；48 个 ISO 639 三字母代码 body rows（abk 到 ita），2 个 column header groups。
- **规则/高亮**：横向 booktabs、无竖线；三位小数；caption 明确每个 model group 的 best 为 bold、second-best 为 underline，JSON 记录 bold、underline、best_second_best；没有 uncertainty interval、seed 或失败列。语言代码按 a*–i* 字母区间排序。
- **Caption（PDF 逐字，39 个空白分词）**：Table 11: Multilingual benchmarking results on MultiBLIMP (ISO 639 language codes a*–i* in alphabetical order). “Ours” refers to PleIAs models pre-trained on Common Corpus. Within each model group, the best score is in bold, and the second-best is underlined. 含 title、setup、abbreviation_definition、encoding_key；没有跨语言主发现。
- **数据与统计**：逐语言 MultiBLiMP score，8 个模型列，每格 0.000–1.000 的三位小数；覆盖从 abk/aln 到 fra/ita 的 48 个语言代码。正文 Table 2 的 aggregate 可在这里拆解，例如 fra/frm 接近 0.99，而部分低资源代码明显更低；表中没有样本数、方差、置信区间、缺失/失败标记。
- **证据关系与评价**：Table 2 aggregate → Tables 11/12 的完整 MultiBLiMP slice → Figure 2/5 的语言与 tokenizer context。优点是双层模型表头和 best/second redundant highlighting 提高横向比较速度；缺点是 48×8 密集矩阵仍需要读者记住模型组，且高亮在灰度/小字号下弱。可复用模式是按 ISO code 分页、固定双层 header，并用文字样式而非颜色标排名。
- **证据**：PDF p32 Table 11，basis=rendered_observation。

## Table 12 — MultiBLiMP 语言 k*–y*

- **位置/结构**：p33，Appendix G，附录，page_width。9 列、2 层模型/规模表头与 Table 11 相同；53 个 ISO 639 三字母代码 body rows（kat 到 yrl），2 个 column header groups。
- **规则/高亮**：booktabs、无竖线、三位小数；best bold、second-best underline，caption 同时定义了这两个样式；无 uncertainty/失败标记。
- **Caption（PDF 逐字，39 个空白分词）**：Table 12: Multilingual benchmarking results on MultiBLIMP (ISO 639 language codes k*–y* in alphabetical order). “Ours” refers to PleIAs models pre-trained on Common Corpus. Within each model group, the best score is in bold, and the second-best is underlined. 含 title、setup、abbreviation_definition、encoding_key。
- **数据与统计**：逐语言 MultiBLiMP scores，覆盖 kat、kaz、kir、…、wol、xcl、xnr、xpg、yrl 共 53 行；每行 8 个模型点值，精度 0.001。页面中可见 tpn/wbp 等低分尾部，说明 aggregate 表不能代替长尾切片；仍无 n、seed 或 uncertainty。
- **证据关系与评价**：Table 2 aggregate → Table 12 的后半语言覆盖 → Figure 2 的稀疏语言地图和 Table 5 的 token count。优点与 Table 11 的两层 header/样式系统一致，分割页面避免更高密度；缺点是跨页比较要回看 header，ISO code 对非熟悉读者不友好。可复用模式是稳定分页的 long-form benchmark matrix，并在 caption 写明代码区间和排名语法。
- **证据**：PDF p33 Table 12，basis=rendered_observation。

## Table 13 — XStoryCloze 逐语言分数

- **位置/结构**：p34，Appendix G，附录，page_width。9 列、2 层模型/规模表头，13 个 body rows（ar、ca、en、es、eu、gl、hi、id、my、ru、sw、te、zh），2 个 column header groups。
- **规则/高亮**：booktabs、无竖线；三位小数；PDF 没有系统性 bold/underline/highlight，highlighting=none；无 uncertainty/失败列。两字母 ISO 639 code 作 stub。
- **Caption（PDF 逐字，25 个空白分词）**：Table 13: Multilingual benchmarking results on XStoryCloze. “Ours” refers to PleIAs models pre-trained on Common Corpus. Languages are represented as two-letter codes in ISO 639. 含 title、setup、abbreviation_definition，不写主发现或不确定性。
- **数据与统计**：13 语言×8 模型的 XStoryCloze aggregate point scores，0.000–1.000、三位小数；与 Table 2 的 aggregate row 对应。没有样本数、重复/区间或每语言 failure。
- **证据关系与评价**：Table 2 XStoryCloze row → Table 13 的语言切片 → Table 5 语言规模与 Figure 5 fertility。优点是与 Table 14、Tables 11/12 共享 header，便于跨任务对读；缺点是 8 个模型列宽窄且没有 best/second encoding，caption 仍需正文提供评测细节。可复用模式是保留统一 model header，让不同 benchmark 的逐语言表可直接对齐。
- **证据**：PDF p34 Table 13，basis=rendered_observation。

## Table 14 — XCopa 逐语言分数

- **位置/结构**：p34，Appendix G，附录，page_width。9 列、2 层模型/规模表头，13 个 body rows（es、et、eu、ht、id、it、qu、sw、ta、th、tr、vi、zh），2 个 column header groups。
- **规则/高亮**：booktabs、无竖线；三位小数；无 bold/underline/cell color，highlighting=none；无 uncertainty 或 failure 标记。两字母 ISO 639 code 作 stub。
- **Caption（PDF 逐字，25 个空白分词）**：Table 14: Multilingual benchmarking results on XCopa. “Ours” refers to PleIAs models pre-trained on Common Corpus. Languages are represented as two-letter codes in ISO 639. 含 title、setup、abbreviation_definition。
- **数据与统计**：13 语言×8 模型的 XCopa point scores，三位小数，补充 Table 2 的 aggregate XCOPA row；没有 n、seed、区间、成本或失败值。
- **证据关系与评价**：Table 2 XCOPA row → Table 14 的逐语言 slice → Tables 11–13 的多任务对照和 Figure 2 语言覆盖。优点是与 Table 13 完全同构，任务切换成本低；缺点是单页下半部两个表共享密集 header，caption 未写每项聚合/评测样本。可复用模式是把相近任务用同一表头和规则排在同页，但需留足视觉分隔与统计脚注。
- **证据**：PDF p34 Table 14，basis=rendered_observation。

## 跨对象系统与最终判断

- **视觉叙事**：Figure 1 先把六个 collection 和语言层级压缩成面积结构，Figure 2 给语言的地理/数量级入口，Figure 3 将 coverage 展开为时间与语义两轴，Table 1 将“多域、跨网页、多语言、开放”四个定位条件显式化，Figure 4 展示文档质量分布，Table 2 再给两个小模型的三个 aggregate benchmark。附录 Figure 5 和 Tables 3–14 把 tokenizer、总量、许可证、来源、语言长尾和逐语言分数拆成可核查对象。
- **Caption 系统**：19 个对象均采用对象下方 Figure/Table n: caption。Figure 2、Figure 4、Figure 5 的 caption 写了筛选/样本/数据源，Table 11/12 写了 ISO code 区间与 bold/underline 规则；Figure 1、Figure 3、Table 1、Table 4、Table 6–10 的 caption 更偏标题式，关键定义留给正文、图例或附录指针。
- **表头系统**：Table 1 是 criterion×dataset taxonomy；Table 2、Tables 11–14 共享 model family×size 的双层 header；Tables 3、5、6、8 将 dataset/language/domain/count 置于同行；Tables 4、9、10 采用两列窄表。横向规则优先于竖线，长语言列表通过换行承载。
- **方法—结果—附录链**：Figure 1/2/3 定义 corpus 的层级、语言和时间/语义接口；Figure 4 连接清洗到质量分布；Table 2 连接训练两个小模型到下游 benchmark；Figure 5 和 Appendix G 展开 tokenizer/逐语言证据。论文没有单独的 ablation Figure/Table，算法 block 也不存在；视觉链依赖 description、aggregate score 和 appendix slices，而不是 component ablation。
- **字体与颜色一致性**：页面和表格的 Nimbus Roman/Computer Modern 基础稳定；Figure 5 的 DejaVu/viridis 和 Figure 2 的连续色标形成局部 plotting 风格。collection 色在 Figure 1、3、4 之间有语义复用，具备迁移价值；但 color-only 区分对灰度和小尺寸仍有风险。
- **最高价值对象**：Figure 1 是 corpus 结构的入口，Figure 3 是时间/语义多样性的压缩证据，Table 2 是 corpus utility 的主比较；Table 3/5/6–10 对复现和 provenance 最有价值，Tables 11–14 对识别 aggregate 结果的语言异质性最有价值。
- **失败/低价值模式**：窄字号、多色叠加和长语言表在缩放后增加阅读成本；Figure 4 与 Table 2 主要给点估计，缺少样本量/重复/不确定性；Figure 2 无点级语言标签；Table 1 的二元 ✓/✗ 隐藏程度差异；很多 caption 只命名对象，需回到正文或附录才能解释编码和统计口径。公开仓库只有工具代码，无法让读者从源文件精确重建这些视觉对象。
- **最可复用模式**：六 collection 颜色跨 treemap/timeline/density grid 复用；时间面板 + 语义散点的双视图；宽表的横向 booktabs 与双层模型 header；长尾数据用排序列和同行分母展开；逐语言 benchmark 按 code 区间分页，并以 bold/underline 做文字冗余排名。
- **一句话视觉策略**：论文以稳定的 collection 色彩和宽幅出版表格，把“开放、多语言、多域语料的组成与 provenance”从面积/地图/时间—语义概览推进到质量分布和 aggregate/逐语言模型证据，同时把绝对计数与长尾细节留在附录。

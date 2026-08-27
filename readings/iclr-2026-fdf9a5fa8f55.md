# Common Corpus：单篇论文深读备忘

- **论文**：Common Corpus - The Largest Collection of Ethical Data for LLM Pre-Training
- **Paper ID**：`iclr-2026-fdf9a5fa8f55`
- **会议与资格**：ICLR 2026；`oral`
- **实际读取版本**：官方 proceedings PDF，物理页 34 页；文本为 `corpus/text/iclr-2026-fdf9a5fa8f55.txt`。
- **来源**：[`official proceedings PDF`](https://proceedings.iclr.cc/paper_files/paper/2026/file/2b5c5689fae6fa9a4883e73e511d52c8-Paper-Conference.pdf)；[`OpenReview forum`](https://openreview.net/forum?id=0wSlFpMsGb)。没有单独 supplementary 文件。

## 1. 文档边界与页级地图

### 1.1 物理边界

| 区域 | 物理页 | 说明 |
|---|---:|---|
| 标题、摘要与正文 | 1–10 | 正文在 p10 的 `Limitations` 最后一段结束；p10 同时包含结论和限制。
| Acknowledgements | 11 | 与 references 同页开始。
| References | 11–18 | p11 首条参考文献至 p18 最后一条参考文献。
| Appendix | 19–34 | Appendix A 从 p19 开始，Appendix G 的逐语言结果在 p31–34。
| PDF 总页数 | 34 | PDF 物理页从 1 开始；文本末尾的空分页不计入 PDF 页数。

正文与附录均采用双栏排版。p2 的 Figure 1、p3 的 Figure 2、p5 的 Figure 3 与 Table 1、p9 的 Figure 4、p10 的 Table 2 跨栏或占据栏宽，图表会把正文段落推到其下方；p21 的 Figure 5 以及 p19–20、p23–26、p32–34 的大表格主要占据整页可用宽度。图内标签、表格数值和页眉会使自动文本词数高于连续正文词数。页 11–18 的 references 仍为双栏，小字体和 URL 换行提高阅读成本；p19–34 的附录以双栏为主，表格和代码块示例会造成明显的留白与栏高不均。

### 1.2 章节到语义模块的映射

| 论文标题 | 页码 | 模块 | 估计词数 |
|---|---:|---|---:|
| Abstract | 1 | `abstract` | 215 |
| 1 Introduction | 1–3 | `introduction` | 1,350 |
| 2 About Common Corpus | 3–4 | `method` | 800 |
| 3 Related Work | 4–5 | `related_work` | 434 |
| 4 Provenance | 5–8 | `method` | 1,800 |
| 4.1 Open Government | 5–6 | `method` | 230 |
| 4.2 Open Culture | 6 | `method` | 450 |
| 4.3 Open Science | 6–7 | `method` | 240 |
| 4.4 Open Code | 7 | `method` | 330 |
| 4.5 Open Web | 7–8 | `method` | 280 |
| 4.6 Open Semantic | 8 | `method` | 270 |
| 5 Cleaning and Curation | 8–9 | `method` | 866 |
| 6 Evaluation：数据质量设计 | 9–10 | `experimental_design` | 180 |
| 6 Evaluation：模型与基准结果 | 9–10 | `results` | 250 |
| 7 Conclusion | 10 | `conclusion` | 95 |
| Limitations | 10 | `limitations` | 200 |
| Acknowledgements | 11 | `other` | 110 |
| References | 11–18 | `other` | 4,020 |
| A LLM Usage Statement | 19 | `appendix` | 30 |
| B Corpus Composition | 19–20 | `appendix` | 597 |
| C Tokenizer Details | 21 | `appendix` | 340 |
| D Provenance | 21–26 | `appendix` | 2,159 |
| E Open Culture Verification | 26–27 | `appendix` | 263 |
| F Cleaning and Curation | 27–31 | `appendix` | 2,086 |
| G Evaluations | 31–34 | `appendix` | 1,444 |

`method` 是对章节标题的语义归并：About、Provenance 和 Cleaning and Curation 共同描述数据构造与治理流程；论文没有独立理论章节。`Evaluation` 按“设计”和“结果”拆开，便于把训练配置、指标和基线与实际数值分开。上述词数是依据 PDF 页面和段落的估计，不把 references 的作者列表当作正文论证。

## 2. 摘要逐句功能编码

| # | 摘要句（清理了 PDF 换行） | 词数 | 功能 | 限定词、数字、比较对象与承接 | 证据 |
|---:|---|---:|---|---|---|
| 1 | Large Language Models (LLMs) are pre-trained on large amounts of data from different sources and domains. | 16 | `object_scope` | 以一般性背景开启对象范围；无数字。 | p1，Abstract；“pre-trained on large amounts of data from different sources and domains” `explicit` |
| 2 | Such datasets often contain trillions of tokens, including large portions of copyrighted or proprietary content, which raises questions about the legal use of such models. | 25 | `problem_gap` | `often` 弱化普遍性；“trillions”给出数量级；问题是版权／专有内容导致的合法使用疑问。 | p1，Abstract；“copyrighted or proprietary content” `explicit` |
| 3 | This underscores the need for truly open pre-training data that complies with data security regulations. | 15 | `problem_gap`, `object_scope` | `truly open` 与“security regulations”收窄为合规开放数据；承接句 2 的法律问题。 | p1，Abstract；“need for truly open pre-training data” `explicit` |
| 4 | In this paper, we introduce Common Corpus, the largest open dataset for LLM pre-training. | 14 | `core_idea`, `method` | `largest` 是全摘要最强的规模定位；首次给出数据集名称。 | p1，Abstract；“we introduce Common Corpus, the largest open dataset” `explicit` |
| 5 | The data assembled in Common Corpus are either uncopyrighted or under open licenses, totaling about two trillion tokens. | 18 | `method`, `quantitative_result` | `either...or` 是版权状态范围；`about two trillion` 是总量。 | p1，Abstract；“either uncopyrighted or under open licenses” `explicit` |
| 6 | The dataset contains a wide variety of languages, ranging from the high-resource European languages to some low-resource languages rarely represented in pre-training datasets. | 23 | `object_scope`, `qualitative_result` | `wide variety`、`high-resource`／`low-resource`构成多语言异质性；`rarely represented` 是覆盖缺口表述。 | p1，Abstract；“wide variety of languages ... low-resource languages” `explicit` |
| 7 | In addition, it includes a large amount of code data. | 10 | `object_scope`, `qualitative_result` | `In addition` 将代码作为独立内容类型补入。 | p1，Abstract；“large amount of code data” `explicit` |
| 8 | The diversity of data sources in terms of covered domains and time periods opens up the paths for both research and entrepreneurial needs across diverse areas of knowledge. | 28 | `qualitative_result`, `impact_claim` | 以领域和时间跨度解释多样性；`research and entrepreneurial needs` 是外延影响主张。 | p1，Abstract；“covered domains and time periods” `explicit` |
| 9 | In this paper, we present the detailed provenance of data assembling and the details of dataset filtering and curation. | 19 | `method` | `detailed` 承诺可追溯来源与清洗过程；承接句 4–8 的数据集定位。 | p1，Abstract；“detailed provenance ... filtering and curation” `explicit` |
| 10 | We train two small language models on Common Corpus and find that they perform comparably to other models of their size, indicating that our dataset is suitable for multilingual pretraining. | 30 | `experimental_setup`, `quantitative_result`, `qualitative_result` | `two`；比较对象是同规模模型；`comparably` 与 `indicating` 把模型分数连接到“适合预训练”的数据集结论。 | p1，Abstract；“perform comparably to other models of their size” `explicit` |
| 11 | Common Corpus represents a key contribution to the ecosystem for open science research on Large Language Models. | 17 | `impact_claim` | `key contribution` 是摘要末尾的总括性影响主张，无新数字。 | p1，Abstract；“key contribution to the ecosystem for open science research” `explicit` |

摘要的功能顺序为：对象背景 → 版权缺口 → 合规需求 → 数据集定位 → 规模与覆盖 →  provenance/curation 方法 → 小模型验证 → 生态影响。它报告了总量和“两模型”的结果，但没有给出表格中的具体 benchmark 数字，也没有理论结果或限制条件。最强主张先出现在句 4 的 `largest`，最后以生态影响收束；“适合多语言预训练”依赖句 10 的比较性结果。

## 3. 引言的论证推进

引言从训练数据规模的趋势进入，在法律与可复现性断点处制造需求，再将 Common Corpus 定位为四个标准同时满足的开放语料，并预告 provenance、curation 和小模型评测。动作链如下；估计总词数约 1,350。

| # | 页 | 动作 | 估计词数 | 上一段留下的问题 | 当前段回答与下一段钩子 | 证据 |
|---:|---:|---|---:|---|---|---|
| 1 | 1 | `context` | 180 | LLM 需要多少训练数据？ | 从 GPT-3 的 300B tokens、Common Crawl/Books3 到 2025 年公开模型的 14–36T tokens，说明规模已成为基础约束；随后转入数据质量成本。 | p1，Introduction；“Large Language Models demand large amounts of training data” `explicit` |
| 2 | 1–2 | `problem` | 350 | 大规模数据如何获得并维护？ | 网页可访问不等于 public domain；fair-use 依赖、NYT 诉讼、C4 的 crawling restrictions 和 AI crawler 影响把问题从规模转为法律／社会外部性。下一段把风险落到已消失的研究产物。 | p2，Introduction；“web data is publicly available, it is not always in the public domain” `explicit` |
| 3 | 2 | `failure_of_prior_work` | 240 | 法律不确定性会造成什么可观测后果？ | Books3、LAION、GEITje、MATH 等数据集或模型被下架，论文指出突然移除使既有工作不可复现，并造成小团队投入损失。下一段转向获取限制持续恶化。 | p2，Introduction；“removed suddenly, making previous work unreplicable” `explicit` |
| 4 | 2 | `problem` | 150 | 下架之外，正在使用的 web 数据是否仍可持续？ | C4、RefinedWeb、Dolma 的分析被用来说明受限 token 增加且集中在高质量来源；后文需要一种许可清晰的数据获取路径。 | p2，Introduction；“5% of all tokens in C4 now have restricted use” `explicit` |
| 5 | 2–3 | `failure_of_prior_work`, `nearest_neighbor_contrast` | 180 | 已有开放项目能否覆盖语言和领域？ | C4C、Open License Corpus、KL3M、Common Pile 等提供部分开放数据，但作者把它们概括为 monolingual 或范围受限；C4C 是早期多语言例外。下一段提出统一方案。 | p3，Introduction；“All these projects are monolingual” `explicit` |
| 6 | 3 | `missing_insight`, `core_idea` | 170 | 缺少同时满足开放、规模、多语言和多领域的数据集。 | Common Corpus 被定位为约 2T tokens、fully open、highly multilingual，并声称在满足法规的情况下可做开放 LLM research/development；同时承认 open data paradox。 | p3，Introduction；“largest fully open pre-training dataset at about 2 trillion tokens” `explicit` |
| 7 | 3 | `method_preview`, `result_preview`, `scope_boundary` | 80 | 方案如何被核验？ | 论文将展开 composition、data collection/curation、license clearing，并以两个小模型给出 comparable performance；不承诺覆盖全部开放资源。 | p3，Introduction；“detail the composition ... collection and curation, and license clearing” `explicit` |

贡献列表没有以单独编号的“Contributions”小节出现；它以连续叙述重复摘要的四个元素（规模、开放许可、多语言／多领域、curation）并添加 open data paradox 与两模型预览。可证伪部分主要是 token 数、跨语料标准比较、FineWeb overlap 和 Table 2 分数；限制在引言末尾以“far from covering the entire range”以及小模型结果的范围声明出现。

## 4. Related Work

相关工作是独立的第 3 节，位于 About Common Corpus 之后、Provenance 之前（p4–5），约占正文估计 6.9%。它采用四个维度的 taxonomy 和相邻语料对照建立缺口：`Multidomain`、`Beyond Web Crawl`、`Multilingual`、`Open data`；论证按属性矩阵推进。

### 4.1 段落动作与引用簇

| # | 页 | 动作 | 估计词数 | 比较维度 | 证据 |
|---:|---:|---|---:|---|---|
| 1 | 4–5 | `taxonomy`, `nearest_neighbor_contrast` | 170 | Table 1 将 KL3M、Dolma、C4、ROOTS、DCAD-2000、FineWeb 2、Common Pile 与 Common Corpus 按四个属性横向排列。 | p5，Related Work；Table 1 `explicit/layout_observation` |
| 2 | 4 | `limitation_of_prior`, `gap_creation` | 120 | KL3M 超越 web crawl 但英文行政／法律受限；Dolma 多域但主要英文；Common Pile 多样且开放但英文-only。 | p4，Related Work；“limited to administrative and legal documents in English” `explicit` |
| 3 | 5 | `nearest_neighbor_contrast`, `gap_creation` | 70 | 作者由表格推出 Common Corpus 同时满足四项标准；这是相关工作到自身定位的唯一显式跃迁。 | p5，Related Work；“unique in satisfying all four criteria simultaneously” `explicit` |
| 4 | 5 | `nearest_neighbor_contrast`, `quantitative_result` | 74 | 与 FineWeb 的 top-1000 domains overlap 少于 2% pages、1% domain names；PDF 集合与 crawl 的 HTML/abstract 内容也不同。 | p5，Related Work；“less than 2% of pages and 1% of domain names” `explicit` |

引用簇至少包括：开放数据最佳实践（AI Alliance、Longpre、Baack 等）；开放语料与 multilingual corpus（C4C、ROOTS、C4、FineWeb 2、Common Pile、KL3M、Dolma、DCAD-2000）；网页抓取／许可证识别；以及后续 OpenAlex、Stack、Wikidata、toxicity 与 OCR 工具的基础工作。正文后续引用这些工作时主要承担数据源或工具来源的归属（例如 OpenAlex、Stack、Presidio、DeBERTa、Llama），方法章节则保持数据集和工具的具体比较。

## 5. 方法与理论

### 5.1 方法的最小逻辑单元

| # | 页 | 推进动作 | 方法单元与解决的问题 | 证据 |
|---:|---:|---|---|---|
| 1 | 3 | `setup_notation`, `state_problem` | 将 `open` 定义为最强口径：可获取、提供 provenance/processing/content details，并满足“any purpose and without asking permission”的开放使用。 | p3，About Common Corpus；“we use the word ‘open’ in the strongest sense” `explicit` |
| 2 | 3 | `state_problem`, `connect_to_prediction` | 把无版权或无限制许可的数据设为可发布 LLM source 的前提，并将多语言、时间跨度、领域多样性连接到 generalizable performance。 | p3，About Common Corpus；“free from copyright or other legal limitations” `explicit` |
| 3 | 4 | `define_component`, `explain_mechanism` | 用六项最佳实践约束管线：documentation、preference signals、diversity/local communities、reciprocity、quality/fitness、PII removal。 | p4，About Common Corpus；六个项目符号 `explicit` |
| 4 | 4 | `summarize`, `connect_to_prediction` | 组合 Open Government、Open Culture、Open Science、Open Web、Open Code、Open Semantic 六类，形成 1,998,647,168,282 tokens 的可过滤对象集合。 | p4，About Common Corpus；“composed of six collections ... 1,998,647,168,282 tokens” `explicit` |
| 5 | 4 | `explain_mechanism` | 每个对象带 license、language(s)、domain/collection 及其他 metadata，使下游可按用途筛选；多数数据被声明为 public domain，九种语言各至少 10B tokens。 | p4，About Common Corpus；“Each data object contains a license, language(s) ... metadata” `explicit` |
| 6 | 5 | `instantiate_algorithm` | Open Government 以 Finance Commons 与 Legal Commons 承载金融、法律、行政数据；Finance Commons 还保留 1.36M 原始 PDF，为 VLM、文档分割和结构化数据研究提供入口。 | p5，Provenance §4.1；“more than 1.36 million original PDF documents” `explicit` |
| 7 | 6 | `define_component` | Open Culture 聚合 13 个以上语言的文化遗产、书籍与期刊；以公共领域核验、OCR 修复和年份 metadata 支撑历史语言与创意写作场景。 | p6，Provenance §4.2；“over 13 languages” `explicit` |
| 8 | 6–7 | `define_component`, `contrast_alternative` | Open Science 从 OpenAlex、CC-BY/PD/CC0/CC-BY-SA 及欧洲子集汇聚科学文档；作者明确其约 85% 文档为英文，语言多样性低于其他集合。 | p7，Provenance §4.3；“nearly 85% of documents ... English” `explicit` |
| 9 | 7 | `define_component`, `instantiate_algorithm` | Open Code 取 Stack v1/v2，按扩展名、格式、许可和人工质量规则过滤，并删除至少 75% 数字的文件；最终 283,227,402,898 tokens。 | p7，Provenance §4.4；“removed files consisting of 75% or more of digits” `explicit` |
| 10 | 7–8 | `define_component`, `contrast_alternative` | Open Web 目前含 Wikipedia/Wikisource、YouTube Commons（2,063,066 个 CC-BY 视频转录）和 StackExchange；许可识别的 web archive 被留作 future work。 | p7–8，Provenance §4.5；“audio transcripts of 2,063,066 videos” `explicit` |
| 11 | 8 | `define_component`, `give_intuition` | Open Semantic 将 Wikidata RDF triples 改写为无文本合成的自然语言序列，覆盖约 300 languages，并保留每条 entry 的多语言块以期待 language alignment。 | p8，Provenance §4.6；“simple natural language sequences, without textual synthesis” `explicit` |
| 12 | 8 | `setup_notation`, `explain_mechanism` | Cleaning and Curation 以工具链处理 multilingual、historical、OCRed data；Segmentext 负责 raw-character structural segmentation，避免依赖丢失的 layout。 | p8，Cleaning and Curation；“custom tools ... multilingual, historical, and OCRed data” `explicit` |
| 13 | 8–9 | `define_component`, `contrast_alternative` | OCRoscope 以 cld2 的 rolling 7-grams 估计文档级质量；OCRerrcr 以 400M DeBERTa-v2-style token classifier 做细粒度检测；前者快，后者精度高但更贵。 | p8–9，Cleaning and Curation；“lower accuracy ... faster and less computationally expensive” `explicit` |
| 14 | 8–9 | `define_component`, `explain_mechanism` | OCRonos 基于 Llama 3 8B 修复错误分词／合并和结构；Presidio 检测 phone/email/IBAN/IP/URL 并以 fictitious realistic values 替代 PII；PDF metadata 与去重来源用于 deduplication。 | p8–9，Cleaning and Curation；“replace PII with fictitious but realistic values” `explicit` |
| 15 | 9 | `define_component`, `connect_to_prediction` | Celadon 是约 140M 参数的多语言 toxicity classifier，以 2M synthetic samples 训练，用于 public-domain 内容的 harmful/bias filtering。 | p9，Cleaning and Curation；“trained from scratch on 2M synthetically annotated samples” `explicit` |
| 16 | 9–10 | `instantiate_algorithm`, `connect_to_experiment` | 用 300,000-document sample 做质量分布，用 Llama-style 两模型和三个 multilingual benchmarks 检验可用性；细粒度 tokenizer、provenance 和逐语言评测移入附录。 | p9–10，Evaluation；“sample ... 300,000 documents” `explicit` |

方法动作的转移序列为：`setup_notation → state_problem → define_component → explain_mechanism → instantiate_algorithm → connect_to_prediction → connect_to_experiment`。论文的“方法”是开放数据基础设施与清洗／权利核验管线，不是带目标函数的学习算法；每个组件都被映射到 provenance、质量、隐私或毒性问题，但组件删除和替代机制没有被单独实验。

### 5.2 形式化、公式、理论与伪代码

- 形式化对象是带 `identifier/open type/collection/license/date/title/creator/language/word count/token count/text` 字段的数据对象（Appendix B, p19）。
- 输入是多源 PDF、文本、代码、网页转录和 RDF-derived records；输出是带许可、语言、域和 token metadata 的清洗后 corpus，以及两个预训练模型（p4、p10）。
- 目标是许可证可追溯、内容可复用、质量可筛选和多语言预训练可用；论文没有显式目标函数、概率模型或优化公式。
- PDF 中 displayed equation、numbered equation、theorem、lemma、proposition、corollary 和 proof 的数量均为 0；没有伪代码／algorithm 环境。流程解释通过段落、项目符号、图表和工具描述完成。
- 因此 `theory` 模块为 `not_applicable`。PDF 未提供前置假设、结论、证明与实证对应的理论结果；“可审计”“合规”属于数据治理主张与设计约束，不能当作形式定理。

## 6. 实验设计

论文没有预先编号的 research questions 或 hypothesis；Evaluation 直接以“evaluate a sample”开启（p9）。设计、实现和缺失项如下。

| 项目 | 状态 | 论文给出的事实 | 证据 |
|---|---|---|---|
| 质量评测样本 | `observed` | 从 Common Corpus 抽取 300,000 documents，使用 Figure 4 的六个 document-level composition/quality metrics。抽样方式、随机种子和分层比例没有说明。 | p9、p31；“sample of 300,000 documents” `explicit` |
| 训练模型 | `observed` | PleIAs 350M 与 PleIAs 1.2B；Llama-based architecture；custom Llama-style tokenizer，vocabulary 65,536。 | p10；“architecture is based on Llama” `explicit` |
| 训练数据量 | `observed` | 350M 使用 filtered subset 约 1T tokens；1.2B 使用全 Common Corpus 加 filtered subset 三个 epochs。 | p10；“approximately 1T tokens” `explicit` |
| 训练预算／硬件 | `observed` | 训练耗时分别 2,944 和 23,040 H100 hours；未报告 H100 数量、precision、optimizer 或 batch size。 | p10；“trained for 2944 and 23040 H100 hours” `explicit` |
| benchmark 与基线 | `observed` | MultiBLiMP、XStoryCloze、XCOPA；对照 Gemma 3、XGLM、BLOOM，1.2B 组另有 OLMo。 | p10 Table 2；模型列与任务列 `layout_observation` |
| 评测执行 | `observed` | 所有评测使用 LM Evaluation Harness；主文提供聚合分数，逐语言值在 Appendix G。 | p10、p31；“All evaluations were run using the LM Evaluation Harness” `explicit` |
| 指标定义 | `partially_closed` | 主文只称 benchmark scores；Appendix G 说明 MultiBLiMP 多数分数高于 random 0.5，但没有给出 score aggregation、标准误或检验过程。 | p10、p31；“most of the scores are significantly above random (0.5)” `explicit` |
| 随机种子 | `not_present` | 未找到 training/evaluation seed。 | p10、Appendix G p31–34；设计与表格未出现 seed `layout_observation` |
| 超参数与复现粒度 | `partially_closed` | 公开 tokenizer vocab、模型规模、tokens、epochs 和 H100 hours；未提供学习率、batch、schedule、精度、checkpoint 或完整硬件配置。 | p10；“custom Llama-style tokenizer with a vocabulary size of 65536” `explicit` |
| 控制／匹配 | `not_present` | 没有同数据量、同 compute、同 tokenizer 或同训练配方的 matched control；基线的训练来源与规模不同。 | p10 Table 2；异质模型列 `layout_observation` |
| 数据泄漏／失败判定 | `not_present` | 未报告 benchmark contamination 检查、数据泄漏控制或预先失败阈值。 | p9–10、Appendix G；相关章节没有这些项目 `layout_observation` |

实验顺序与引言基本对应：先用 Figure 4 支撑“数据可读”的质量概览，再用 Table 2 支撑小模型可用性；provenance、OCR、PII、toxicity 组件没有各自的对照实验，因此“工具存在”与“工具造成的性能收益”没有被区分。

## 7. 结果、统计与可视化

### 7.1 可视化与表格清单

| 类型 | 编号 | 页 | 模块 | 尺寸／比较对象 | 任务与编码通道 |
|---|---|---:|---|---|---|
| figure | Figure 1 | 2 | `method` | 跨栏 treemap；六种 open collections，标注主要语言。 | 展示 collection 比例与语言构成；图注明确为 proportional treemap。 |
| figure | Figure 2 | 3 | `method` | 跨栏 schematic world map；横轴为 document count 的 log scale，仅显示 10,000+ documents 的语言。 | 展示语言地理／数量覆盖；图注与坐标承担解释。 |
| figure | Figure 3 | 5 | `method` | 两个子图：1500–2000+ 的 collection document timeline；Common Corpus、C4、FineWeb 子集的 two-component t-SNE。 | 同时编码时间跨度和语义差异；正文用其说明 diversity 与 crawl corpus 的差异。 |
| table | Table 1 | 5 | `related_work` | 八个数据集 × 四个属性；✓/✗ 比较。 | 判断 Common Corpus 是否同时满足 multidomain、beyond-web-crawl、multilingual、open-data。 |
| figure | Figure 4 | 9 | `results` | 六个 stacked histograms，300,000-document sample；六类 open type 的 density。 | Character Repetition、TTR、Top Word Proportion、Alphanumeric、Whitespace、Uppercase。 |
| table | Table 2 | 10 | `results` | 两组模型与 Gemma 3/XGLM/BLOOM/OLMo 的三项 aggregate scores。 | 比较多语言语法、故事选择和因果常识基准。 |
| figure | Figure 5 | 21 | `appendix` | 六种语言在 FLORES-200 devtest 上的 tokenizer fertility；比较 Ours 1B 与其他 tokenizer。 | 验证 65,536 vocabulary 的 token/word 效率。 |
| table | Tables 3–5 | 19–20 | `appendix` | collection composition、top licenses、top-50 languages。 | 公开文档／词／token 分母、许可和语言长尾。 |
| table | Tables 6–10 | 21–26 | `appendix` | Finance/Legal/Open Culture/Open Science/Open Code 的来源与 token 分布。 | 使 provenance 细节可核对。 |
| table | Tables 11–14 | 32–34 | `appendix` | MultiBLiMP 逐语言（两页）、XStoryCloze 与 XCOPA 逐语言。 | 暴露聚合分数背后的语言异质性。 |
| algorithm | not_present | — | `ablation` | PDF 没有算法框或伪代码。 | 工具链仅以 prose 和附录说明。 |

### 7.2 主要结果

| 结果主张 | 证据对象与数值 | 比较／统计处理 | 作者解释与不利解释 |
|---|---|---|---|
| 六类 collection 的文档质量分布大体处于预期范围；代码与 Open Government 有结构性偏移。 | Figure 4，p9：300,000-document sample；正文称 code 的 repetition 较高、whitespace 较低，Open Government 的 lexical diversity 较低。 | Stacked probability-density histograms；没有误差表达、区间或显著性检验。Appendix G 定义六个指标。 | 作者把偏移归因于 code syntax/punctuation 与行政固定术语；分布没有逐集合数字摘要，读者需从图形估读。 |
| 350M 在 MultiBLiMP 上达到 0.774，高于 Gemma 3 270M 的 0.762、XGLM 564M 的 0.711、BLOOM 560M 的 0.683。 | Table 2，p10；`Ours 350M = 0.774`。 | 单次 aggregate score；未报告 seed、离散量、区间或检验。 | 作者称对更大模型也有“outstanding performance”；逐语言表显示低分语言仍存在，例如 Appendix G Table 11 的 `aqz = 0.214`、`tpn = 0.111`（p32–33）。 |
| 1.2B 在 MultiBLiMP 上为 0.797，略低于 Gemma 3 1B 的 0.799，但高于 XGLM 1.7B 的 0.710 与 OLMo 1B 的 0.699。 | Table 2，p10；完整四列数值。 | 同上，aggregate benchmark score。 | “comparably”比“全面优胜”更贴近这一行；作者仍称 MultiBLiMP 表现 outstanding。 |
| Common Corpus 模型在 XStoryCloze 与 XCOPA 上没有全面胜出，但 1.2B 高于 OLMo 1B。 | XStoryCloze：350M 0.509 vs Gemma 0.533/XGLM 0.537/BLOOM 0.532；1.2B 0.526 vs Gemma 0.594/XGLM 0.569/OLMo 0.517。XCOPA：350M 0.533 vs 0.544/0.550/0.541；1.2B 0.541 vs 0.593/0.574/0.518。 | 三个任务都只有一个 aggregate score；无不确定性或多重比较处理。 | 论文把总评写成 comparable，并突出 MultiBLiMP；表格本身显示在 XStoryCloze、XCOPA 对 Gemma/XGLM 的差距。 |
| 逐语言结果支持高资源语言的强表现，也显示低资源或特殊语言的脆弱点。 | Appendix Tables 11–14，p32–34；例：MultiBLiMP `fra` 350M 0.994、`eng` 0.981，但 `tpn` 0.111；XStoryCloze `en` 350M 0.569；XCOPA `vi` 350M 0.550。 | 语言级 score 表；没有按语言加权规则、样本量、区间或 significance procedure。 | Appendix G 仅说明多数 MultiBLiMP 分数显著高于 0.5，并标出 best/second-best；它没有解释低分语言或 aggregate 分母。 |
| 自定义 tokenizer 的 fertility 只被 Gemma 3 超过。 | Figure 5，p21：FLORES-200 devtest，六种语言；ours tokenizer vocabulary 65,536。 | 每语言 tokens per word 的柱状比较；未报告区间或统计检验。 | 这是 tokenizer 效率的辅助结果，不能独立证明 corpus 的模型 efficacy。 |

### 7.3 统计口径

聚合单位是 benchmark × model 的 reported score；逐语言表的行是 language × model。质量图的聚合单位是 document，分母为 300,000 样本。论文没有报告 participants、seed、task-level variance、bootstrap、Bayesian analysis、regression 或 multiple-comparison correction。作者在 Appendix G 使用“significantly above random (0.5)”的措辞，但没有提供检验名称、样本数或 p-value。因而可区分的证据层级为：Figure 4 的分布形状、Table 2 的点值差异、Appendix G 的异质性；“显著”本身缺少可复核统计处理。

## 8. 消融、负面结果与自我设限

### 8.1 消融清单

| 对象 | 状态 | 识别目标与观察 | 证据 |
|---|---|---|---|
| 组件删除（OCR、PII、toxicity、segmentation） | `not_present` | Cleaning 逐项介绍工具，没有保留／删除组件的 matched model 或 corpus 对照。 | p8–9；工具描述无 removal comparison `layout_observation` |
| 超参数／规模敏感性 | `not_present` | 只有 350M 与 1.2B 两个模型，训练 token、epochs 和 compute 同时变化；无 sweep。 | p10；两模型配置 `explicit` |
| 数据／任务异质性 | `observed` | 逐语言 MultiBLiMP、XStoryCloze、XCOPA 表揭示语言差异，但没有将其作为控制实验。 | p32–34；Tables 11–14 `explicit` |
| 机制替代解释 | `not_present` | 未比较 web-only、public-domain-only、code-removed 或无 toxicity/OCR 版本，无法把效能变化归因到某一组件。 | p9–10；未出现替代管线 `layout_observation` |
| 失败案例 | `observed` | Appendix G 包含低于或接近 random 的语言分数，例如 `tpn` MultiBLiMP 0.111、`kxh` 350M 0.483、XStoryCloze `ru` 350M 0.503。 | p32–34；逐语言表 `explicit` |
| 计算成本 | `observed` | 报告 2,944／23,040 H100 hours，但没有 cost-normalized baseline。 | p10；训练耗时 `explicit` |
| 鲁棒性／扰动 | `not_present` | 没有跨版本、污染、OCR 噪声或许可变化下的 robustness test。 | p9–10、Appendix G；无对应实验 `layout_observation` |

正文中的消融比例为 0：Table 2 是基准比较，Figure 4 是质量描述，工具组件没有 deletion study。逐语言表提供了异质性和失败信号，却没有被设计成 mechanism ablation。

### 8.2 明示限制的位置与类型

- **scope / data**（p10, `Limitations`）：作者承认 open data paradox，Common Corpus 尚未覆盖全部可用开放数据。
- **compute / generality**（p10, `Limitations`）：2T tokens 单独只足以训练 limited-size models；更大模型需要更多数据。
- **scope / metric**（p10, `Limitations`）：数据不含 instruction-tuning 或 specialized-task data，不能直接用于 task-specific fine-tuning。
- **assumption / data**（p10, `Limitations`）：curation 方法无法达到 100% accuracy；OCR errors 仍可能影响模型，用户可按 metadata 过滤潜在问题集合。
- **ethics / assumption**（p26–27, Appendix E）：权利核验采用 non-US author life + 70、US publication + 95、未知作者／集体作品的 1884 cutoff 和“不产生额外 digitization rights”等规则；这是披露的操作假设，正文没有给出独立法律审计。

## 9. 结论、限制与主张闭环

### 9.1 结论段动作

| 段落 | 页 | 动作 | 证据 |
|---|---:|---|---|
| Conclusion | 10 | 重述问题／方法：发布 Common Corpus 与详细 data collection/curation documentation，主张 LLM development 可在 regulatory norms 下进行。 | p10；“strictly adhering to the regulatory norms” `explicit` |
| Conclusion | 10 | 回收结果与边界：当前只足以训练 small models；工具与方法可用于扩展 permissively licensed data。 | p10；“only large enough to train small models currently” `explicit` |
| Conclusion | 10 | 影响／未来：希望成为 open-science LLM infrastructure 并推动后续 initiatives。没有新数字。 | p10；“grow as a critical infrastructure” `explicit` |

`Limitations` 两段没有新数字，集中回收范围、规模、任务适用性、curation accuracy 和 metadata filtering。它没有回收 Appendix G 的逐语言失败值或 Table 2 的具体任务差异。

### 9.2 闭环矩阵

| 引言主张 | 方法回应 | 实验／结果回应 | 结论回应 | 状态与证据 |
|---|---|---|---|---|
| 规模大且 fully open（约 2T tokens） | 六 collection、许可字段、provenance；Appendix B Tables 3–5 给总量／许可／语言。 | Table 3 总计 1,998,647,168,282 tokens；Table 4 Public Domain 为 1,138,508,375,958 tokens。 | Conclusion 保留“release”与 infrastructure 叙述。 | `partially_closed`：规模与许可统计直接给出，但“fully open”依赖内部权利规则及外部法律适用范围；p4、p19、p26–27。 |
| 同时多语言、多领域、超越 web crawl | 六 collections；Table 1 四维 taxonomy；Figure 3 t-SNE/timeline。 | FineWeb overlap 少于 2% pages、1% domains；Table 5 给语言长尾。 | Conclusion 泛化为 open ecosystem infrastructure。 | `closed`（相对于论文定义）：有表格、图和具体 overlap；p5、p19–20。 |
| 数据来源可追溯并可审计 | 每对象 license/language/domain metadata；OpenAlex、national libraries、Stack/Wikidata 来源；Appendix D/E。 | 没有独立 audit experiment；但表格和 rights criteria 给出可核对材料。 | Conclusion 强调 thorough documentation。 | `partially_closed`：文档可审计性已回应，外部审计与长期可用性未测；p4、p19–27。 |
| 清洗能处理 OCR、PII、toxicity | Segmentext、OCRoscope、OCRerrcr、OCRonos、Presidio、Celadon。 | Figure 4 只验证总体质量分布；没有工具对照或 error-recall 结果。 | Limitations 明示无法 100% accuracy。 | `partially_closed`：组件与自限有证据，因果 efficacy 未闭合；p8–10、p27–31。 |
| Common Corpus 适合多语言预训练 | Llama-style tokenizer、350M/1.2B 训练配方。 | Table 2：MultiBLiMP 0.774/0.797；XStoryCloze 0.509/0.526；XCOPA 0.533/0.541。 | Conclusion 将其限定为 small models。 | `partially_closed`：有三项 benchmark 与基线，但无 matched control、seed/区间，且两任务对强基线落后；p10。 |
| 小模型之外可扩展并推动开放生态 | 公开工具与 collection 作为 infrastructure。 | 没有更大模型、增量收集或长期维护实验。 | Future work 形式重申扩展许可数据。 | `partially_closed`：生态愿景有发布物支持，scale-out 仍是未验证预测；p10。 |
| Common Corpus 在尺寸范围内是唯一同时满足四项属性的数据集 | Table 1 选择八个相邻语料作比较。 | ✓/✗ 表与 FineWeb overlap 提供局部对照。 | 结论不再重复“唯一”。 | `partially_closed`：比较集和四项标准是作者自定义且有限，不能扩展成全领域穷尽证明；p5。 |

## 10. 附录职责

论文无独立 supplementary；Appendix A–G 是 PDF p19–34 的连续附录。附录约 6,958 词，约为正文（摘要至 Limitations，估计 6,325 词）的 1.10 倍。它承载了大部分 provenance 数量、权利规则、工具说明和逐语言结果。

| 一级模块 | 页 | 类别 | 对象数量／内容 | 正文调用 | 依赖判断 |
|---|---:|---|---|---|---|
| A LLM Usage Statement | 19 | `other` | 1 个披露段；说明 grammar correction、rewriting 和 data visualization 使用 LLM。 | 无显式正文调用。 | 不影响数据或模型主张；属于披露。 |
| B Corpus Composition | 19–20 | `dataset_detail` | 文档 schema；Tables 3–5（六 collection 总量、top-10 licenses、top-50 languages）。 | p4 “token counts ... listed in Appendix B”；p4 language distribution。 | 总 token、public-domain 比例、语言覆盖依赖此处数字。 |
| C Tokenizer Details | 21 | `implementation_detail` | Figure 5；FLORES-200 devtest 上六种语言的 fertility。 | p4 footnote 说明 PleIAs tokenizer；p10 说明 vocab 65,536。 | tokenizer efficiency 的辅助主张依赖此处；不决定 corpus 合规。 |
| D Provenance | 21–26 | `dataset_detail` | D.1 Finance/Legal（Tables 6–7）、D.2 Open Culture（Table 8）、D.3 Open Science（Table 9）、D.4 Open Code（Table 10）。 | p4 “token counts ... Appendix B”；p5–8 各 provenance 小节指向 Appendix D。 | collection 组成、来源语言和 token 分布依赖此处，正文仍保留 collection 级解释。 |
| E Open Culture Verification | 26–27 | `other` | 四项权利规则：non-US life+70、unknown/collective 1884 cutoff、US +95、无 digitization rights。 | p6 “complete criteria list in Appendix E”。 | “public domain” 的文化集合主张依赖这些规则；法理正确性未由本文独立验证。 |
| F Cleaning and Curation | 27–31 | `implementation_detail` | F.1 Segmentext、F.2 OCRoscope、F.3 OCRerrcr、F.4 OCRonos、F.5 Celadon；输入输出例子、训练数据和速度／泛化描述。 | p8 “document the tools in detail in Appendix F”；p9 对应各工具。 | 工具的训练规模、输入输出、已知问题依赖附录；正文保留选择逻辑。 |
| G Evaluations | 31–34 | `additional_result` | Figure 4 六指标定义；Tables 11–12 MultiBLiMP，13 XStoryCloze，14 XCOPA 逐语言分数。 | p9 Figure 4；p10 Table 2 与 Appendix G；p31–34 表格。 | 语言异质性、低分语言和指标定义依赖附录；aggregate decision 留在正文。 |

附录迁移总体提高了 provenance 和复现线索，但正文自足性不完全：读者无需附录即可看到 Table 2 和训练预算，却无法核对总量、语言长尾、权利规则、指标定义或低资源语言失败点。附录没有提供 seed、optimizer、完整超参数、component ablation 或独立 legal audit，因此这些缺口不是“迁移后已解决”的细节。

## 11. 不利信息的呈现策略

以下只记录版面和语句可验证的呈现，不推断作者动机。

| 策略 | 具体证据 | 中性判断 |
|---|---|---|
| `附录迁移` | 主文 p10 只给 Table 2 aggregate scores；逐语言结果置于 Appendix G p31–34。 | 聚合主张先承担决策作用，语言异质性需读者翻到附录。 |
| `聚合掩盖异质性` | Table 2 以每个 benchmark 一个点值；Appendix G 的 MultiBLiMP 既有 `fra/en` 高分，也有 `tpn = 0.111`（p32–33）。 | 分母、语言权重和低分语言没有在主文中展开，aggregate 与 tail risk 同页不可见。 |
| `语气弱化／指标选择` | p10 先称“perform comparably”并突出 MultiBLiMP；Table 2 同时显示 XStoryCloze 和 XCOPA 的 Ours 低于 Gemma 3、XGLM、BLOOM。 | 这是结果陈述顺序与措辞的事实描述；不能据此判断是否有意规避。 |
| `未来工作化` | Open Web 的 permissive web archives 和 license identification challenge 在 p8 被放到“future work”；p10 也把更大规模开放数据写为希望。 | 尚未完成的 web coverage 与 scale-out 没有进入主结果验证。 |
| `限定延后` | 2T 只能训练 limited-size models、无 instruction tuning、curation 不能 100% accuracy 的限制集中在 p10 `Limitations`，位于 benchmark 表之后。 | 读者先看到可用性与生态主张，再看到适用范围和准确率边界。 |

## 12. 高频用词与修辞

以下是对正文 p1–10 的语境标注；references、公式碎片、表格数值和模板页眉已排除，频数仅作词形线索，不替代项目的原始 token 统计。

- **高频实词**：`data`、`open`、`Common Corpus`、`corpus`、`models/model`、`language/languages`、`dataset(s)`、`collection(s)`、`source(s)`、`documents`、`training`、`tokens`、`legal`、`domain`、`text`、`curation`、`license(s)`、`code`、`OCR`。
- **高频二元词组**：`Common Corpus`、`language models`、`open science`、`training data`、`open culture`、`public domain`、`open government`、`trillion tokens`、`open source`、`open data`、`open web`、`code data`、`data sources`、`creative commons`、`OCR errors`。
- **高频三元词组**：`large language models`、`language model training`、`open pre-training data`、`open science collection`、`small language models`、`data Common Corpus`（后者多由段落衔接和 PDF 词切分造成，不能视为术语）。
- **主张动词**：`introduce`、`present`、`provide`、`include`、`describe`、`show`、`train`、`find`、`evaluate`、`compare`、`filter`、`remove`、`replace`、`release`、`hope`。`show/find`主要出现在引言、Evaluation 和 Conclusion；`provide/describe`主要承担 provenance 与 documentation。
- **限定词**：`about`、`approximately`、`mostly`、`nearly`、`currently`、`at least`、`primarily`、`often`、`far from`、`may`、`if desired`。它们集中在规模估计、语言比例、未来 web coverage 和 limitations。
- **对比／因果词**：`in contrast`、`despite`、`however`、`therefore`、`due to`、`while`、`rather than`、`enables`、`allowing`、`indicating`。最关键的因果跃迁是“许可／治理约束 → 可发布数据基础设施 → 小模型 benchmark 可用”。
- **贡献词与强弱比例**：强主张词包括 `largest`、`only`、`unique`、`key contribution`、`outstanding`；弱主张词包括 `comparably`、`aims`、`hope`、`may`、`far from`、`suitable for limited size`。正文同时使用两组词，规模、唯一性和合规性承担强定位，适用规模、future work 和 curation accuracy 用限定语收边界。

## 13. 最终判断

1. **单一主线**：以可追溯许可、公共领域核验和面向 OCR/PII/toxicity 的清洗管线，把多源多语言资料组织成约 2T-token 的开放 corpus；再用两个小模型和 multilingual benchmarks 证明它具备有限的预训练可用性。数据治理是主线，模型分数是可用性验证，不是独立算法贡献。
2. **正文保留的决策关键内容**：六 collection 的概念、总量、核心 provenance、清洗工具选择、PII/毒性处理、两模型规模与 H100 hours、三个 benchmark 及 Table 2 aggregate scores。读者可以据此判断“是否值得使用”和“是否能训练小模型”。
3. **移入附录的细节及影响**：总量分解、许可证／语言长尾、来源表、权利核验规则、工具训练数据与例子、Figure 4 指标定义和逐语言分数全部后移。附录使审计路径存在，但把合规主张和多语言 tail performance 的核验成本转移给读者；seed、超参数和 component ablation 仍未提供。
4. **最有效的写作／图表模式**：Table 1 的四维 ✓/✗ taxonomy 快速建立定位；Figure 3 将时间与语义差异并置；Table 2 用紧凑三行数字把 corpus utility 绑定到模型规模。六 collection 的段落按来源、许可、用途推进，能让基础设施叙事落到可筛选对象。
5. **最大叙事缺口**：`fully open`、`ethical` 与“适合预训练”的范围强于直接证据。权利规则是内部标准，不是独立法律证明；清洗工具没有 removal/alternative ablation；Table 2 没有 seed、区间、matched controls，且两个任务落后于多个基线。Figure 4 的“expected range”和 Appendix G 的“significantly”也缺少可复核统计口径。
6. **可迁移规则**：当论文把数据治理能力作为贡献时，正文至少要把“治理约束 → 可复核数据对象 → 预先声明的效能检验”串成同一闭环，并在主文保留能改变决策的分母、对照和异质性摘要。
7. **适用边界**：这条规则适用于数据集、benchmark、infrastructure 和 model-card 型论文；对纯理论论文，闭环应换成假设、定理、反例或实验预测，不能要求不存在的数据治理字段。

## 14. 测量校正与证据覆盖

自动草稿把 `main_end_page_provisional=34`、`appendix_start_page_provisional=12`，并将全 PDF 估计词数记为 15,651；逐页阅读 PDF 后按 p10 正文结束、p11 acknowledgements/references、p19 appendix start 修正边界。自动草稿的 Figure captions=5、Table captions=14、numbered equations=0、theorem items=0 与版面核对一致。Appendix G 的正文说明写“across the five open types”，但 Figure 4 图例实际列出六类 open type；此处按图例和正文 Figure 4 记为六类，并保留该文字差异。

- **实质主张数**为 12，**具有物理页证据的主张数**也为 12，状态为 `complete`。
- 所有 JSON evidence 的页码均在 1–34，anchor 使用短语、图／表编号或可定位的版面事实；`basis` 区分 `explicit`、`layout_observation`、`interpretation`。

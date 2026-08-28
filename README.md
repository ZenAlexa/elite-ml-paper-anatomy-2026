# Elite ML Paper Anatomy 2026

本项目从 **250 篇 ICLR/ICML 2026 Outstanding、Oral、Spotlight 论文**中提取可复用的写作结构、图表组织、实验设计、理论表达、证据闭环和附录分工。每篇论文均有独立中文深读备忘、schema-valid JSON、PDF 页码证据和来源链接；聚合结果进一步形成统计报告与论文写作手册。

## 从这里开始

| 目标 | 入口 |
|---|---|
| 直接起草一篇完整 ICLR 论文 | [ICLR 全文写作蓝图](docs/iclr-full-paper-blueprint.md) |
| 按 250 篇证据设计全部 Figure/Table | [ICLR 图表执行手册](docs/iclr-visual-design-handbook.md) |
| 阅读图表统计、源码与逐对象证据 | [250 篇图表解剖](reports/visual_design_analysis_250.md) |
| 复用绘图、方法图与表格模板 | [`templates/visuals/`](templates/visuals/) |
| 阅读全部统计结论 | [250 篇统计报告](reports/statistical_analysis_250.md) |
| 按顶会高频模式设计论文 | [250 篇顶会论文写作手册](docs/writing-playbook.md) |
| 查找某篇论文的深读与结构化数据 | [逐篇深读索引](reports/reading_index.md) |
| 查看统一阅读标准 | [单篇论文独立深读协议](prompts/deep-read.md) |
| 查看统计定义与加权方法 | [统计分析方案](docs/statistical-analysis-plan.md) |
| 查看会议、层级与来源口径 | [语料范围与分层口径](docs/corpus-scope.md) |
| 复算全部报告和图 | [复现命令](#复现) |
| 提交新阅读或分析改进 | [贡献指南](CONTRIBUTING.md) |

![250 篇论文的正文篇幅分配](reports/figures/checkpoint_250_module_shares.svg)

## 核心发现

| 维度 | 250 篇高频模式 |
|---|---|
| 正文篇幅 | 方法 23.83%、结果 17.01%、引言 14.84%、理论 10.15%、实验设计 9.83%、相关工作 8.43%、消融 5.38% |
| 摘要 | 平均 188 词、7.97 句；98.0% 写方法，98.0% 至少给出一种结果，55.6% 给出定量结果 |
| 相关工作 | 中位数 507 词、正文占比中位数 8.42%；高频链为「分类轴 → 最近邻 → 明确差异 → 方法缺口」 |
| 方法与理论 | 方法平均 1.21 图、0.39 算法、5.52 公式；理论平均 5.97 公式 |
| 结果与消融 | 结果平均 2.34 图、2.09 表；消融平均 1.67 图、0.90 表 |
| 图表总体 | 逐对象审计 3,071 个 Figure、2,329 个 Table；会议等权均值上取整为正文 6 图/4 表、附录 8 图/7 表 |
| 视觉规格 | 正文 Figure 中位 2 个面板、4 个系列、8 pt 图中文字、1 pt 数据线；Table 中位 6 行×6 列、2 位小数 |
| 视觉源码 | 20 篇 exact、132 篇 partial；取得 824 个逐篇核验源文件，源码样式解析覆盖 101 篇 |
| 证据闭环 | 30.8% 形成「对象 → 缺口 → 洞见 → 组件 → 公式 → 预测 → 实验 → 结果 → 消融 → 结论」完整链 |
| 附录 | 附录/正文页数比中位数 1.40，词数比中位数 0.84；追加结果、实现细节、扩展方法和证明最常见 |
| 修辞 | `we introduce`、`we propose`、`we show`、`we find`、`however`、`in contrast` 构成高频主张与转折语言 |
| ICLR 起稿配置 | 9 页正文，以 105 个向上取整写作单位起稿；正文预留 6 图、4 表、1 算法、13 个展示公式，附录预留 8 图、7 表 |

统计报告同时给出论文覆盖率、会议等权比例、中位数、四分位数、图表公式计数、动作转移和逐篇案例。

## 如何使用

### 设计一篇论文

从 [ICLR 全文写作蓝图](docs/iclr-full-paper-blueprint.md)取得 9 页逐节整数预算、9 句摘要模板、方法与理论结构、实验协议表、结果与消融写法、附录架构和完稿检查表。再用[图表执行手册](docs/iclr-visual-design-handbook.md)确定 6 图、4 表的职责、尺寸、字体、配色、caption 和证据关系，并用[写作手册](docs/writing-playbook.md)建立 claim map 与正文—附录分工。

### 审阅一篇论文

按以下链条检查每项贡献：

```text
claim → method object → equation or guarantee → prediction
→ experiment → result → ablation → conclusion → appendix evidence
```

使用 [`claim_closure.csv`](reports/tables/claim_closure.csv) 对照闭环状态，使用 [`checkpoint_250_module_summary.csv`](reports/tables/checkpoint_250_module_summary.csv) 对照篇幅、图表、算法和公式配置。

### 研究某篇顶会论文

在[逐篇深读索引](reports/reading_index.md)中按标题或会议查找论文。每篇记录包含：

- 中文全文深读备忘；
- 结构化 JSON；
- PDF 来源与 OpenReview 页面；
- 摘要逐句功能；
- 引言、相关工作和方法动作；
- 图、表、算法、公式与理论对象；
- 实验、统计、消融、局限、附录和 claim closure；
- PDF 物理页码、章节和证据短语。

### 复算统计

`make checkpoint` 从逐篇 JSON 重建聚合表、taxonomy、词频、图形和索引。所有主报告数值均来自 `reports/tables/`。

## 数据与方法

### 统计总体

250 篇统计总体包含：

- ICLR 150 篇：2 Outstanding、148 Oral；
- ICML 100 篇：2 Outstanding、49 Oral、49 Spotlight；
- `foundation_200` 完整队列 200 篇；
- `replication_200` 前 50 篇。

仓库另收录 3 篇扩展阅读。候选目录共 760 篇 ICLR/ICML 2026 Main Track Outstanding、Oral、Spotlight 论文。样本、等级、纳入概率和来源记录位于 [`analysis_sample.csv`](data/processed/analysis_sample.csv) 与 [`papers.csv`](data/processed/papers.csv)。

### 统一深读

每个阅读单元完整处理一篇论文，并按 [`deep-read.schema.json`](schemas/deep-read.schema.json) 编码 12 个语义模块：

```text
abstract · introduction · related_work · method · theory
experimental_design · results · ablation · conclusion
limitations · appendix · other
```

编码覆盖摘要功能、段落动作、实验设计、统计方法、图表公式、主张闭环、局限类型、不利信息呈现和附录职责。逐项判断连接 PDF 页码、章节与证据锚点。

### 相对化与汇总

不同会议先在论文内转换为相对量，再计算会议内分布与会议等权结果：

```text
module_share = module_main_words / total_main_words
module_visual_density = module_visual_count / module_words × 1000
appendix_ratio = appendix_pages / main_pages
```

正文篇幅报告会议等权均值；论文特征报告 `n/N` 与覆盖率；长尾计数同时报告均值、中位数和四分位数。摘要功能、段落动作、实验字段、统计方法、局限和附录类别均保留论文级数据。

## 产物索引

### 结论与指南

- [`reports/statistical_analysis_250.md`](reports/statistical_analysis_250.md)：完整统计分析、案例和写作研判；
- [`reports/visual_design_analysis_250.md`](reports/visual_design_analysis_250.md)：全部 Figure/Table 的对象级统计、视觉源码、论证关系与反模式；
- [`docs/iclr-visual-design-handbook.md`](docs/iclr-visual-design-handbook.md)：9 页 ICLR 正文的 6 图、4 表执行配置；
- [`reports/visual_audit_index.md`](reports/visual_audit_index.md)：250 篇逐篇视觉审计入口；
- [`templates/visuals/`](templates/visuals/)：可运行的 Matplotlib、TikZ 和 booktabs 模板；
- [`docs/iclr-full-paper-blueprint.md`](docs/iclr-full-paper-blueprint.md)：全部数值向上取整的 ICLR 全文起稿与定稿规范；
- [`docs/writing-playbook.md`](docs/writing-playbook.md)：可直接用于未来论文的写作与设计手册；
- [`reports/reading_index.md`](reports/reading_index.md)：253 篇深读的论文级索引；
- [`docs/corpus-scope.md`](docs/corpus-scope.md)：语料、分层与来源；
- [`docs/statistical-analysis-plan.md`](docs/statistical-analysis-plan.md)：统计单位、相对化与汇总方法。

### 核心统计表

- [`checkpoint_250_module_summary.csv`](reports/tables/checkpoint_250_module_summary.csv)：模块篇幅、覆盖率、图、表、算法和公式；
- [`checkpoint_250_abstract_summary.csv`](reports/tables/checkpoint_250_abstract_summary.csv)：摘要功能与首次位置；
- [`checkpoint_250_move_summary.csv`](reports/tables/checkpoint_250_move_summary.csv)：引言、相关工作和方法动作；
- [`checkpoint_250_transition_summary.csv`](reports/tables/checkpoint_250_transition_summary.csv)：段落动作转移；
- [`checkpoint_250_experimental_design_summary.csv`](reports/tables/checkpoint_250_experimental_design_summary.csv)：15 类实验设计字段；
- [`checkpoint_250_limitation_type_summary.csv`](reports/tables/checkpoint_250_limitation_type_summary.csv)：局限类型；
- [`checkpoint_250_packaging_strategy_summary.csv`](reports/tables/checkpoint_250_packaging_strategy_summary.csv)：不利信息呈现策略；
- [`checkpoint_250_categorical_summary.csv`](reports/tables/checkpoint_250_categorical_summary.csv)：理论、视觉、统计、附录和闭环类别；
- [`iclr_full_paper_blueprint.csv`](reports/tables/iclr_full_paper_blueprint.csv)：正文比例、词数和图表算法公式的整数上包络；
- [`reading_index.csv`](reports/tables/reading_index.csv)：论文、等级、队列、来源与深读文件。
- [`visual_audit_object_inventory.csv`](reports/tables/visual_audit_object_inventory.csv)：全部 Figure/Table 的对象级设计、绘图语法、caption、表头和证据关系；
- [`visual_design_categorical_summary.csv`](reports/tables/visual_design_categorical_summary.csv)：论文覆盖率与逐篇归一后的视觉预算；
- [`visual_design_numeric_summary.csv`](reports/tables/visual_design_numeric_summary.csv)：面板、系列、字号、线宽、行列、精度与复杂度；
- [`visual_cross_object_system.csv`](reports/tables/visual_cross_object_system.csv)：逐篇视觉叙事、caption、表头和正文—附录关系；
- [`visual_source_inventory.csv`](reports/tables/visual_source_inventory.csv)：自动发现的仓库与视觉文件候选；`discovery_*` 字段记录检索阶段，最终状态来自逐篇审计；
- [`visual_source_files_local.csv`](reports/tables/visual_source_files_local.csv)：公开视觉源码与论文源码的逐文件获取结果；
- [`visual_source_style_summary.csv`](reports/tables/visual_source_style_summary.csv)：源码中的绘图库、字号、线宽、透明度、DPI 与导出格式。

### 逐项证据表

- [`result_inventory.csv`](reports/tables/result_inventory.csv)：实验结果、比较、统计方法和作者解释；
- [`visual_inventory.csv`](reports/tables/visual_inventory.csv)：图、表、算法及其模块职责；
- [`theory_inventory.csv`](reports/tables/theory_inventory.csv)：公式、定理、引理、证明及角色；
- [`ablation_inventory.csv`](reports/tables/ablation_inventory.csv)：组件、敏感性、失败和机制消融；
- [`appendix_inventory.csv`](reports/tables/appendix_inventory.csv)：附录类别、页码和正文调用；
- [`limitation_inventory.csv`](reports/tables/limitation_inventory.csv)：局限、位置和证据；
- [`adverse_strategy_inventory.csv`](reports/tables/adverse_strategy_inventory.csv)：分母、聚合、案例、语气和位置策略；
- [`lexical_frequencies.csv`](reports/tables/lexical_frequencies.csv)、[`ngram_frequencies.csv`](reports/tables/ngram_frequencies.csv)、[`rhetorical_patterns.csv`](reports/tables/rhetorical_patterns.csv)：词、短语和修辞频率。

### 项目结构

```text
data/processed/     论文目录、样本、来源和自动测量
corpus/             论文来源文件与版面文本
prompts/            单篇独立深读协议
schemas/            结构化结果 schema
readings/           每篇论文的 Markdown 与 JSON
visual_audits/      每篇论文的全部 Figure/Table 视觉审计
reports/            统计报告、阅读索引、图和表
docs/               写作手册、语料与统计方法
templates/visuals/  ICLR 绘图、方法图与表格模板
scripts/            获取、测量、验证、聚合与渲染
```

## 复现

```bash
make validate       # 校验目录、来源和 253 份深读结果
make checkpoint     # 重建 250 篇统计、词频、图和阅读索引
make index          # 单独更新逐篇深读索引
make blueprint      # 重建 ICLR 全文整数预算表
make visual-sources # 获取已核验的公开视觉源码并提取样式
make visual-validate # 校验 250 份逐篇视觉审计
make visual-analysis # 重建图表统计、索引、报告与手册
make visual-templates # 生成可复用的 ICLR 图表示例
```

完整流程入口位于 [`Makefile`](Makefile)：`catalog → hydrate → resolve → acquire → measure → sample → validate → checkpoint`。

## 贡献与许可

贡献格式、证据标准和验证命令见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。项目采用 [MIT License](LICENSE)。论文来源链接、标题、作者和短证据锚点继续指向各自原始出版页面。

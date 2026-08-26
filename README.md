# Elite ML Paper Anatomy 2026

本项目解剖 ICLR、ICML、NeurIPS 2026 年官方 `Outstanding`、`Oral`、`Spotlight` 论文的正文、附录、统计表达、图表组织和叙事结构。分析总体只来自这三个会议的官方 2026 年记录，不混入往届论文、普通 poster、workshop、journal track 或 position paper track。

## 当前样本边界

截至 2026-08-26：

- ICLR 2026 已举办，纳入 224 篇论文：2 篇 Outstanding、222 篇其他 Oral。224 份官方 proceedings PDF 均已下载、验证和完成机器测量。
- ICML 2026 已举办，纳入 536 篇 Main Track 论文：2 篇 Outstanding、157 篇其他 Oral、377 篇 Spotlight。47 个 Position Paper Track 日程事件单独排除。
- ICML 2026 已预留 [PMLR v306 仓库](https://github.com/mlresearch/v306)，当前只有 2025-10-30 的模板初始提交，[卷页面](https://proceedings.mlr.press/v306/) 返回 404。本机访问 OpenReview PDF 会进入挑战页。项目已按 OpenReview ID 定位并验证 417 份 arXiv 版本；这些版本直接进入深读与统计，119 篇尚无公开 PDF 入口。
- NeurIPS 2026 的作者通知日期为 2026-09-24 AoE。当前总体状态为 `pending-official-decision`，不使用 NeurIPS 2025 替代。

Outstanding、Oral、Spotlight 可能重叠。`data/processed/papers.csv` 以论文为单位去重，保留 `selection_flags`，并用 `analysis_stratum` 设定互斥分析层级：`outstanding > oral > spotlight`。跨会议分析先计算会议内相对比例，再对会议等权汇总，避免篇幅、样本量和类别命名差异主导结论。

分析集固定为两个连续队列，共 400 篇。`foundation_200` 包含 ICLR 100 篇和 ICML 100 篇，两会 4 篇 Outstanding 全部纳入；`replication_200` 再从未入选论文中抽取 ICLR 100 篇和 ICML 100 篇。合并后，ICLR 为 2 篇 Outstanding 和 198 篇 Oral；ICML 为 2 篇 Outstanding、99 篇 Oral 和 99 篇 Spotlight。抽样只在已有已验证 PDF 的论文中进行。队列、固定种子、条件纳入概率和合并纳入概率均保存在 `data/processed/analysis_sample.csv`。

调度器默认先完成 `foundation_200`，再派发 `replication_200`。两个队列使用同一深读 Prompt、schema、证据页码规则和统计变量。报告同时保留首批 200、复现批 200 和合并 400 的估计，用于检验高频模式是否随样本扩展保持稳定。此前按同一协议完成且恰好进入复现批的论文直接计入，不重复读取。

## 目录

```text
data/raw/official/       官方页面和结构化响应快照
data/processed/          去重目录、排除项、获取状态和测量表
corpus/pdfs/             本地 PDF 缓存，不提交 Git
corpus/text/             本地正文提取缓存，不提交 Git
prompts/                 一文一 agent 的统一深读协议
schemas/                 结构化深读结果 schema
readings/                每篇论文的独立深读结果
reports/                 汇总报告、图和表
scripts/                 目录、下载、测量、校验与汇总脚本
```

## 运行

```bash
make catalog       # 从官方 2026 页面重建去重目录
make hydrate       # 获取每篇论文的 OpenReview forum/PDF URL
make acquire       # 下载并用 %PDF、pdfinfo 验证 PDF
make resolve-preprints  # 建立 ICML arXiv 临时入口，不替代官方 PDF
make acquire-preprints  # 下载并验证可定位的临时版本
make measure       # 提取版面文本和初步结构测量
make sample        # 重建两个固定队列，共 400 篇
make validate      # 校验目录、PDF 和一文一读结果
make next          # 按已验证 PDF、预计阅读成本和模型路由给出下一批三篇
make aggregate     # 更新会议内相对量；总体齐备后生成跨会议等权结果
make cohort        # 比较首批 200、复现批 200 和合并 400
make lexical       # 按队列、会议和等级更新词频与修辞模式
```

机器测量用于一致计量与异常发现。语义模块边界、论证推进、负面结果包装、附录职责等结论来自 `prompts/deep-read.md` 约束下的逐篇人工式深读编码。每个子智能体只处理一篇论文，写入该论文独立的 Markdown 和 JSON 后停止。

`reports/tables/module_distributions.csv` 以论文为等权单位，报告各语义模块的正文词数占比、图表算法数、公式数、每千词密度及其在正文中的相对份额。`weighted_module_means.csv` 按逐层纳入概率还原会议内部构成，`conference_equal_module_means.csv` 再对 ICLR 与 ICML 等权。`cohort_module_comparison.csv`、`cohort_paper_comparison.csv` 和 `cohort_categorical_comparison.csv` 使用同一变量分别计算两个 200 篇队列与合并 400 篇。`abstract_function_summary.csv` 汇总摘要功能及句序，`inventory_summaries.csv` 汇总图、表、算法、理论对象、附录职责和主张闭环，实验设计、结果、消融、统计方法、局限与不利信息呈现策略另保留逐项证据表。对应队列尚未读完时，结果标为 `interim`，不作为最终普适结论。

## 证据原则

1. 样本资格以会议官方页面为准。
2. 论文内容只从身份对齐且已验证的 PDF、supplementary 和 OpenReview 公开记录提取；实际版本写入每篇 `source_files`。
3. 每个论文级结论附页码、章节或原文短语定位。
4. 缺失数据显式编码为 `not_present`、`not_applicable`、`unavailable` 或 `not_yet_observed`。
5. 自动计数与 agent 编码分别保留，聚合前报告分歧。

PDF 是可重建的本地缓存，不提交 Git。`data/processed/pdf_manifest.csv` 与 `preprint_manifest.csv` 记录来源、状态、字节数和页数。统计对应实际读取版本；同一论文获得新版 PDF 时可以复核并更新，不阻塞当前分析。

本地已下载的 ICLR 与 ICML PDF 缓存约 4.3 GiB。400 篇分析集的来源文件已经在缓存中，后续阅读不会重复下载；新增空间主要来自 Markdown、JSON 和小型 CSV。空间不足时可删除分析集以外的 PDF 或文本缓存，再按 manifest 重建。

详细口径见 [`docs/corpus-scope.md`](docs/corpus-scope.md) 和 [`docs/statistical-analysis-plan.md`](docs/statistical-analysis-plan.md)。

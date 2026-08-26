# Elite ML Paper Anatomy 2026

本项目解剖 ICLR、ICML、NeurIPS 2026 年官方 `Outstanding`、`Oral`、`Spotlight` 论文的正文、附录、统计表达、图表组织和叙事结构。分析总体只来自这三个会议的官方 2026 年记录，不混入往届论文、普通 poster、workshop、journal track 或 position paper track。

## 当前样本边界

截至 2026-08-26：

- ICLR 2026 已举办，纳入官方 Outstanding 与 `Accept (Oral)` 论文。
- ICML 2026 已举办，纳入 Main Track 的 Outstanding、Oral 和 Spotlight；Position Paper Track 单独排除。
- NeurIPS 2026 的作者通知日期为 2026-09-24 AoE。当前总体状态为 `pending-official-decision`，不使用 NeurIPS 2025 替代。

Outstanding、Oral、Spotlight 可能重叠。`data/processed/papers.csv` 以论文为单位去重，保留 `selection_flags`，并用 `analysis_stratum` 设定互斥分析层级：`outstanding > oral > spotlight`。跨会议分析先计算会议内相对比例，再对会议等权汇总，避免篇幅、样本量和类别命名差异主导结论。

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
make measure       # 提取版面文本和初步结构测量
make validate      # 校验目录、PDF 和一文一读结果
make aggregate     # 生成会议内比例及跨会议等权汇总
```

机器测量用于一致计量与异常发现。语义模块边界、论证推进、负面结果包装、附录职责等结论来自 `prompts/deep-read.md` 约束下的逐篇人工式深读编码。

## 证据原则

1. 样本资格以会议官方页面为准。
2. 论文内容只从已验证 PDF、supplementary 和 OpenReview 公开记录提取。
3. 每个论文级结论附页码、章节或原文短语定位。
4. 缺失数据显式编码为 `not_present`、`not_applicable`、`unavailable` 或 `not_yet_observed`。
5. 自动计数与 agent 编码分别保留，聚合前报告分歧。

详细口径见 [`docs/corpus-scope.md`](docs/corpus-scope.md) 和 [`docs/statistical-analysis-plan.md`](docs/statistical-analysis-plan.md)。

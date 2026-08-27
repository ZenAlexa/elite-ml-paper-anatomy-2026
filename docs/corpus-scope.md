# 语料范围与分层口径

## 发布语料

本次发布围绕 ICLR/ICML 2026 Main Track 的 Outstanding、Oral、Spotlight 论文建立三层数据：

| 层级 | 数量 | 用途 |
|---|---:|---|
| 资格目录 | 760 篇 | 论文身份、会议等级、官方事件和来源目录 |
| 250 篇统计总体 | 250 篇 | 模块比例、图表公式、写作动作、统计方法和附录结构 |
| 扩展阅读 | 3 篇 | 论文级案例与结构化证据 |

250 篇统计总体由 ICLR 150 篇和 ICML 100 篇组成：

- ICLR：2 Outstanding、148 Oral；
- ICML：2 Outstanding、49 Oral、49 Spotlight。

样本单位为论文。`selection_flags` 保留论文获得的全部等级标记，`analysis_stratum` 按 `outstanding > oral > spotlight` 形成互斥统计层。

## 资格定义

资格目录采用以下条件：

1. 会议年份为 2026；
2. 会议为 ICLR 或 ICML；
3. 轨道为 Main Track；
4. 官方记录标注 Outstanding、Oral 或 Spotlight；
5. 论文标题、会议事件、OpenReview 和 PDF 来源可以对齐。

其他轨道、poster、workshop、tutorial、demo、competition proposal、test-of-time 和 position paper 记录进入 [`exclusions.csv`](../data/processed/exclusions.csv)，与 Main Track 统计总体分开保存。

## 两阶段样本

[`analysis_sample.csv`](../data/processed/analysis_sample.csv) 保存两个连续队列：

1. `foundation_200`：ICLR 100 篇、ICML 100 篇，包含两会全部 4 篇 Outstanding；
2. `replication_200`：从其余候选中抽取 ICLR 100 篇、ICML 100 篇。

本次 250 篇统计总体包含完整 `foundation_200` 和 `replication_200` 的前 50 篇。每行记录会议、等级、队列、抽样种子、候选数、条件纳入概率、合并纳入概率和论文来源。

## 论文来源

- ICLR 深读使用官方 proceedings PDF；
- ICML 深读使用与 OpenReview ID、标题和作者对齐的 arXiv 版本；
- 每篇 JSON 的 `source_files` 保存 `source_kind`、`source_url`、OpenReview 页面和版本识别证据；
- [`reading_index.md`](../reports/reading_index.md) 连接论文来源、中文深读和结构化数据。

主要会议来源：

- ICLR 2026 论文与日程：<https://iclr.cc/virtual/2026/papers.html>
- ICLR 2026 Outstanding：<https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/>
- ICML 2026 Spotlight：<https://icml.cc/virtual/2026/events/2026SpotlightPosters>
- ICML 2026 Oral：<https://icml.cc/virtual/2026/events/oral>
- ICML 2026 Awards：<https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/>

## 数据文件

| 文件 | 内容 |
|---|---|
| [`papers.csv`](../data/processed/papers.csv) | 760 篇资格目录 |
| [`analysis_sample.csv`](../data/processed/analysis_sample.csv) | 队列、等级、概率和来源 |
| [`pdf_manifest.csv`](../data/processed/pdf_manifest.csv) | ICLR PDF 来源、状态、字节数和页数 |
| [`preprint_manifest.csv`](../data/processed/preprint_manifest.csv) | ICML 预印本来源、状态、字节数和页数 |
| [`checkpoint_250_status.json`](../reports/checkpoint_250_status.json) | 250 篇统计总体组成 |
| [`reading_index.csv`](../reports/tables/reading_index.csv) | 253 篇深读与来源索引 |

## 一篇论文的证据单元

每篇论文对应：

```text
readings/<paper_id>.md
readings/<paper_id>.json
```

Markdown 面向研究者阅读；JSON 面向验证、聚合和二次分析。两者共享 `paper_id`，并连接同一 PDF 来源、页码地图和证据锚点。

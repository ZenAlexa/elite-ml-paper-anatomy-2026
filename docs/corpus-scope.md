# 语料范围与分层口径

## 研究总体

目标总体由下列官方记录的并集构成：

- `ICLR 2026 Outstanding Paper`
- `ICLR 2026 Accept (Oral)`
- `ICLR 2026 Spotlight`，仅在官方记录实际存在时纳入
- `ICML 2026 Outstanding Paper Award`
- `ICML 2026 Main Track Oral`
- `ICML 2026 Main Track Spotlight`
- `NeurIPS 2026 Best/Outstanding Paper`、`Oral`、`Spotlight`，待官方决定后纳入

样本单位是论文。单篇论文获得多种标记时只出现一行，全部标记写入 `selection_flags`。

## 纳入规则

论文须同时满足：

1. 会议年份为 2026；
2. 来源属于会议官网、官方虚拟日程、官方 proceedings 或 OpenReview 会议组；
3. 官方记录明确标为 Outstanding、Oral 或 Spotlight；
4. 公开 PDF 可定位，或将获取状态明确记为受限。

## 排除规则

- 普通 poster；
- workshop、tutorial、demo、competition proposal；
- ICLR Blog Track、Journal Track；
- ICML Position Paper Track，包括其独立 Outstanding／Oral／Spotlight；
- test-of-time 论文；
- 拒稿、withdrawn、desk rejected；
- 2025 或更早论文；
- 非官方整理榜单和预测名单。

排除项保留在 `data/processed/exclusions.csv`，包含官方事件 ID、标题、排除原因和来源 URL。

## 分层

`analysis_stratum` 为互斥字段：

1. `outstanding`
2. `oral`
3. `spotlight`

层级只用于去重聚合。`selection_flags` 保留全部资格事实。例如一篇 Outstanding 论文同时出现在 Oral 日程中时，`analysis_stratum=outstanding`，`selection_flags=outstanding|oral`。

## 时间截断

项目的首个冻结时间为 `2026-08-26T14:28:58Z`。NeurIPS 2026 官方作者通知计划在 2026-09-24 AoE 发布，因此首版分析只包含 ICLR 与 ICML。报告必须把 NeurIPS 标为 `not_yet_observed`，不得把两会议结果描述为三会议总体结论。

## 阅读停止条件

首个完整分析版本以 `data/processed/analysis_sample.csv` 的 200 篇全部完成为停止条件。两会 Outstanding 全部阅读；其余层采用固定随机样本。760 篇资格总体继续保留，样本之外已完成的论文作为扩展证据，不改变主分析分母。

## 官方来源

- ICLR 2026 官方论文和日程：<https://iclr.cc/virtual/2026/papers.html>
- ICLR 2026 Outstanding announcement：<https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/>
- ICML 2026 Spotlight Posters：<https://icml.cc/virtual/2026/events/2026SpotlightPosters>
- ICML 2026 Orals：<https://icml.cc/virtual/2026/events/oral>
- ICML 2026 Awards：<https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/>
- NeurIPS 2026 CFP：<https://neurips.cc/Conferences/2026/CallForPapers>

## PDF 版本边界

ICLR 使用官方 proceedings PDF。ICML 2026 已预留 [PMLR v306 仓库](https://github.com/mlresearch/v306)，截至冻结日只有模板初始提交，[PMLR v306 页面](https://proceedings.mlr.press/v306/) 尚未发布。OpenReview 直连触发访问挑战时，`data/processed/preprint_sources.csv` 提供按 OpenReview ID 和标题对齐的 arXiv 入口；入口由 [ICML2026 数据集](https://huggingface.co/datasets/ai-conferences/ICML2026) 定位。已验证的预印本直接进入深读与统计，每篇结果记录实际来源。后续发现新版 PDF 时按需复核，当前分析无需等待 camera-ready。

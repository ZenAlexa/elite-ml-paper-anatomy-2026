# 统计分析方案

## 研究问题

分析回答五类问题：

1. 各模块占正文和全文的相对篇幅；
2. 图、表、算法和公式在各模块中的密度与位置；
3. 摘要、相关工作、方法、理论、实验、消融、结论、局限的高频组织方式；
4. 正文与附录如何分工并形成前后引用；
5. 顶级论文常见的叙事策略、证据闭环和反模式。

## 分析单位

- 论文级：每篇论文一条观测；
- 模块级：一篇论文中的语义模块；
- 章节级：PDF 显式 section；
- 页面级：正文和附录页面；
- 句子／词项级：摘要功能、叙事动作和词频。

## 两阶段分析集

分析集固定为 400 篇，分两个互不重叠的 200 篇队列：

- `foundation_200`：ICLR 100 篇、ICML 100 篇。两会 Outstanding 各 2 篇全部纳入；ICLR 另抽取 98 篇 Oral，ICML 另抽取 49 篇 Oral 和 49 篇 Spotlight。固定种子为 `elite-ml-paper-anatomy-2026-primary-v1`。
- `replication_200`：在首批未入选论文中，抽取 ICLR Oral 100 篇、ICML Oral 50 篇和 ICML Spotlight 50 篇。固定种子为 `elite-ml-paper-anatomy-2026-replication-v1`。

合并 400 篇包含 ICLR 2 篇 Outstanding 和 198 篇 Oral，以及 ICML 2 篇 Outstanding、99 篇 Oral 和 99 篇 Spotlight。逐层候选数、队列目标数、抽取时剩余候选数、条件纳入概率、合并纳入概率和实际来源均保存在 `data/processed/analysis_sample.csv`。

调度器在队列内可以优先读取短论文或低复杂度论文，但默认在 `foundation_200` 完成前不派发 `replication_200`。调度顺序不改变分析集。已完成而未被抽中的论文属于扩展集，只用于敏感性分析和例证，不进入主要比例估计。

## 主要变量

- 篇幅：页面占比、词数占比、栏面积占比；
- 密度：每 1,000 词和每正文页的公式、图、表、算法数量；
- 模块：`introduction`、`related_work`、`method`、`theory`、`experimental_design`、`results`、`ablation`、`conclusion`、`limitations`、`appendix`；
- 摘要功能：对象、缺口、核心思想、方法、理论、定量结果、定性结果、局限、影响；
- 闭环边：问题→方法、理论→预测、实验设计→主张、结果→主张、消融→机制、局限→适用边界；
- 呈现策略：负面结果位置、限定词、自我设限位置、基线选择、指标选择、附录迁移和标题框架。

## 相对化

不同会议的页数与格式不同。每篇论文先转换为相对量：

```text
module_share = module_main_words / total_main_words
visual_density = visual_count / total_main_pages
module_visual_density = module_visual_count / module_words * 1000
appendix_ratio = appendix_pages / main_pages
```

会议内先报告中位数、四分位数、20% 截尾均值、经验分布和论文级 bootstrap。队列内估计使用 `cohort_selection_probability`，合并 400 篇估计使用 `selection_probability`。ICML 的 Oral 与 Spotlight 按逐层纳入概率加权还原；Outstanding 作为全纳层单列。跨会议主结果采用会议等权：先得到每个会议的论文级统计量，再对可观测会议取算术平均。另给论文等权结果作为敏感性分析。Outstanding、Oral、Spotlight 使用互斥 `analysis_stratum` 比较，同时用多标签结果检查重叠影响。

同一指标分别在 `foundation_200`、`replication_200` 和 `combined_400` 中计算。两批方向一致、量级接近且合并估计不由单一会议或等级层主导时，才归纳为稳定的普适模式。队列差异本身作为异质性结果保留，不通过改动编码规则消除。

## 推断边界

- Outstanding 属于全纳层，直接报告有限总体值；其他层属于固定分层样本，报告估计值与抽样稳定性。
- bootstrap 在会议与等级层内重采样论文，用于描述论文构成变化时的稳定性。
- 首批 200 的结果在进入复现批前冻结；复现批使用同一 schema，不回改首批变量定义。
- NeurIPS 未产生决定前，跨三会估计均记为 `not_yet_observed`。
- 自动章节分类与 agent 编码的分歧率单独报告；分歧不静默覆盖。
- 词频先词形归一化，去除参考文献、公式碎片、数据集专名和模板固定语；同时报告每 10,000 正文词的相对频率和文档频率。

## 主要输出

1. 模块占比的会议内分布与会议等权汇总；
2. 模块×对象类型的图表公式密度矩阵；
3. 摘要功能组合和句序的高频路径；
4. 方法段落推进动作的转移矩阵；
5. 正文—附录职责和引用边；
6. 高频词、词组、修辞动作及其文档频率；
7. 可直接用于论文写作的正文／附录决策规则；
8. 反模式及其真实出现频率、位置和上下文。

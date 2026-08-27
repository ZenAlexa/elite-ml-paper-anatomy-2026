# 统计分析方案

## 研究问题

分析回答七类问题：

1. 摘要、引言、相关工作、方法、理论、实验设计、结果、消融、结论和 Limitations 各占多少正文篇幅；
2. 图、表、算法和公式如何分布在不同模块；
3. 摘要功能、引言动作、相关工作动作和方法动作如何推进；
4. 实验设计展示哪些字段，结果使用哪些统计方法；
5. 方法、理论、实验、结果和消融如何形成 claim closure；
6. 局限、不利结果和附录如何组织；
7. 高频词、短语和修辞动作如何支持叙事。

## 分析单位

| 单位 | 用途 |
|---|---|
| 论文 | 覆盖率、篇幅、对象总数、附录比例和闭环状态 |
| 语义模块 | 模块词数、图、表、算法、公式和密度 |
| 章节与页面 | 正文、参考文献、附录和证据位置 |
| 句子 | 摘要功能与首次位置 |
| 段落动作 | 引言、相关工作和方法的推进与转移 |
| 证据对象 | 结果、统计、消融、理论、局限与附录调用 |
| 词项 | 单词、二元短语、三元短语和修辞模式 |

## 250 篇统计总体

统计总体采用 250 份完整深读：

| 会议 | Outstanding | Oral | Spotlight | 合计 |
|---|---:|---:|---:|---:|
| ICLR | 2 | 148 | 0 | 150 |
| ICML | 2 | 49 | 49 | 100 |
| 合计 | 4 | 197 | 49 | 250 |

队列结构为 `foundation_200=200`、`replication_200=50`。每篇论文使用同一 Prompt、schema、页码规则和变量定义。

## 主要变量

- 篇幅：模块正文词数、逐篇正文占比、正文页数、附录页数；
- 视觉：图、表、算法及每千词密度；
- 理论：展示公式、编号公式、定理、引理、命题、证明及角色；
- 摘要：对象、缺口、洞见、方法、理论、设置、定量结果、定性结果、局限和影响；
- 写作动作：引言、相关工作、方法动作及相邻转移；
- 实验：数据、任务、模型、基线、指标、重复、预算、超参数、硬件、控制和人类评测；
- 统计：中心量、点估计、离散量、区间、检验、多重比较、bootstrap、Bayesian、回归、相关和 effect size；
- 闭环：对象→缺口→洞见→组件→公式→预测→实验→结果→消融→结论；
- 附录：证明、扩展方法、实现、数据、追加结果、鲁棒性、消融、失败、复现和案例；
- 修辞：主张动词、转折词、限定词、贡献词和文档频率。

## 相对化

每篇论文先转换为相对量：

```text
module_share = module_main_words / total_main_words
visual_density = visual_count / total_main_pages
module_visual_density = module_visual_count / module_words × 1000
appendix_page_ratio = appendix_pages / main_pages
appendix_word_ratio = appendix_words / main_words
```

模块 `main_word_share` 在论文内归一化，使正文模块合计为 100%。正文比例先计算 ICLR 与 ICML 的会议内均值，再取会议等权均值。

## 汇总统计

连续量报告：

- 论文数 `n`；
- 均值；
- 中位数；
- 第一与第三四分位数；
- 最小值与最大值；
- ICLR、ICML 和会议等权均值。

类别变量报告：

- `papers_present / papers`；
- 论文覆盖率；
- 会议等权覆盖率；
- 每篇平均对象数；
- 每篇对象数中位数。

词汇报告总次数、论文覆盖数、论文覆盖率和每 10,000 正文词频率。动作序列报告论文级出现率与相邻转移率。

## 结构化 taxonomy

实验设计、统计实践、局限类型和呈现策略采用显式 taxonomy：

- 每篇论文对每个类别计一次；
- 同一论文可进入多个类别；
- 计数使用 `status=observed` 的结构化记录；
- 同义字段由版本化正则归并；
- 归并脚本与汇总 CSV 同步发布。

对应脚本：

- [`checkpoint_design_taxonomy.py`](../scripts/checkpoint_design_taxonomy.py)；
- [`checkpoint_limitation_taxonomy.py`](../scripts/checkpoint_limitation_taxonomy.py)；
- [`checkpoint_analysis.py`](../scripts/checkpoint_analysis.py)。

## 证据链

统计结果可沿以下路径回到论文页面：

```text
主报告数值
→ checkpoint_250_*.csv
→ inventory CSV
→ readings/<paper_id>.json
→ readings/<paper_id>.md
→ source_url + PDF page + section + evidence anchor
```

[`reading_index.md`](../reports/reading_index.md)提供论文级入口。

## 主要输出

1. 正文模块占比与分布；
2. 模块 × 图/表/算法/公式矩阵；
3. 摘要功能、顺序和结果类型；
4. 引言、相关工作和方法动作转移；
5. 实验设计字段与统计方法；
6. claim closure 与模块衔接；
7. 局限类型与不利信息呈现；
8. 正文—附录分工与调用；
9. 高频词、短语和修辞；
10. 面向未来论文的写作手册。

## 复算

```bash
make validate
make checkpoint
```

`make checkpoint` 重建聚合表、队列比较、词频、250 篇 checkpoint 表、taxonomy、SVG 图和逐篇阅读索引。

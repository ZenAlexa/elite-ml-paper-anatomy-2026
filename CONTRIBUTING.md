# 贡献指南

本项目接受五类贡献：

1. 新增或校正一篇论文的深读；
2. 新增或校正一篇论文的 Figure/Table 视觉审计；
3. 改进 schema、taxonomy、聚合或可视化；
4. 修正论文来源、等级、标题和作者信息；
5. 改进统计报告、写作手册和文档索引。

## 新增一篇深读

1. 在 [`papers.csv`](data/processed/papers.csv) 中确认 `paper_id`、会议和等级。
2. 按 [`deep-read.md`](prompts/deep-read.md) 完整阅读论文正文、参考文献和附录。
3. 写入 `readings/<paper_id>.md`。
4. 按 [`deep-read.schema.json`](schemas/deep-read.schema.json) 写入 `readings/<paper_id>.json`。
5. 为实质判断填写 PDF 物理页码、章节和短证据锚点。
6. 运行 `make validate`。
7. 运行 `make index` 更新逐篇索引。

一篇论文构成一个独立贡献单元。Markdown 面向研究者阅读，JSON 面向校验与聚合；两者使用相同 `paper_id` 和来源信息。

## 新增一篇视觉审计

1. 按 [`visual-audit.md`](prompts/visual-audit.md) 检查 PDF 正文与附录中的全部 Figure/Table。
2. 以至少 180 dpi 渲染对象页，记录字体、字重、字号、颜色、几何、轴、legend、marker、线型、网格、不确定性、caption、表头、统计量和证据关系。
3. 核查作者 GitHub、arXiv source package、项目页和 [`visual_source_inventory.csv`](reports/tables/visual_source_inventory.csv) 的自动发现候选；最终源码状态写入逐篇审计。
4. 先写 `visual_audits/<paper_id>.md`，再原子发布符合 [`visual-audit.schema.json`](schemas/visual-audit.schema.json) 的 JSON。
5. 运行 `make visual-validate`；涉及聚合、报告或模板时再运行 `make visual-analysis` 和 `make visual-templates`。

每篇视觉审计覆盖一个 `paper_id`。PDF 决定 Figure/Table 清单，源码决定可精确读取的样式参数；从渲染结果估计的属性在 JSON 中保留 provenance。

## 改进统计或 taxonomy

统计改动同时提交：

- 变量定义或归并规则；
- 生成脚本；
- 对应 CSV；
- 报告中的数值、解释与链接；
- `make checkpoint` 的实际输出。

论文级覆盖率按 `paper_id` 去重。会议篇幅先在论文内归一化，再计算会议内结果与会议等权结果。长尾计数保留均值、中位数和四分位数。

## 改进文档

文档按以下证据顺序写作：

```text
结论 → 统计表 → 逐项 inventory → reading JSON/Markdown
→ source URL → PDF page/section/evidence anchor
```

README 承载结论、使用路径和索引；统计报告承载完整分析；写作手册承载可执行模板；逐篇深读承载论文级事实。

## 验证

```bash
make validate
make checkpoint
make visual-validate
make visual-analysis
git diff --check
```

文档改动同时运行：

```bash
~/.claude/scripts/prose-lint.py README.md CONTRIBUTING.md docs/*.md reports/statistical_analysis_250.md reports/visual_design_analysis_250.md
```

## Pull Request 内容

Pull Request 写明：

- 变更对象；
- 对应论文、字段或统计量；
- 证据位置；
- 执行过的验证命令；
- 结果发生的变化。

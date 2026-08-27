# 贡献指南

本项目接受四类贡献：

1. 新增或校正一篇论文的深读；
2. 改进 schema、taxonomy、聚合或可视化；
3. 修正论文来源、等级、标题和作者信息；
4. 改进统计报告、写作手册和文档索引。

## 新增一篇深读

1. 在 [`papers.csv`](data/processed/papers.csv) 中确认 `paper_id`、会议和等级。
2. 按 [`deep-read.md`](prompts/deep-read.md) 完整阅读论文正文、参考文献和附录。
3. 写入 `readings/<paper_id>.md`。
4. 按 [`deep-read.schema.json`](schemas/deep-read.schema.json) 写入 `readings/<paper_id>.json`。
5. 为实质判断填写 PDF 物理页码、章节和短证据锚点。
6. 运行 `make validate`。
7. 运行 `make index` 更新逐篇索引。

一篇论文构成一个独立贡献单元。Markdown 面向研究者阅读，JSON 面向校验与聚合；两者使用相同 `paper_id` 和来源信息。

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
git diff --check
```

文档改动同时运行：

```bash
~/.claude/scripts/prose-lint.py README.md CONTRIBUTING.md docs/*.md reports/statistical_analysis_250.md
```

## Pull Request 内容

Pull Request 写明：

- 变更对象；
- 对应论文、字段或统计量；
- 证据位置；
- 执行过的验证命令；
- 结果发生的变化。

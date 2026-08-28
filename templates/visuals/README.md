# ICLR 图表模板

本目录提供可直接移入论文仓库的三类源文件：

- `iclr_style.py`：ICLR 双栏宽度、8 pt 图内文字、1 pt 数据线、主色与冗余线型；
- `latex_preamble.tex`：表格与 TikZ 图共用的宏包和宏；
- `method_figure.tex`：全栏方法接口图；
- `table_style.tex`：8 pt、`booktabs`、两位小数、最佳/次佳高亮的主结果表。

Python 图以 2.63 in 单栏或 5.50 in 全栏尺寸直接生成 PDF/SVG。绘图时用颜色、marker 和线型共同编码系列；caption 依次写标题、设置、编码、比较结论和不确定性定义。

在论文 preamble 中先写 `\input{templates/visuals/latex_preamble.tex}`，再于正文按需输入 `method_figure.tex` 或 `table_style.tex`。

```python
import matplotlib.pyplot as plt

from iclr_style import apply_iclr_style, figure_size, plot_series, save_figure, style_axis

apply_iclr_style()
x = [1, 2, 4, 8]
series = {"Ours": [61, 68, 74, 79], "Baseline": [58, 63, 67, 69]}
fig, ax = plt.subplots(figsize=figure_size("single"))
for index, (label, values) in enumerate(series.items()):
    plot_series(ax, x, values, index=index, label=label)
style_axis(ax, grid="both")
ax.legend(ncol=2)
save_figure(fig, "figures/result.pdf")
```

运行 `uv run --with matplotlib python generate_examples.py` 可生成全栏 PDF/SVG 示例。示例的左图用颜色、marker、线型和明确的标准差带表达预算与效果的关系。右图用直接标注表达质量与成本的关系。

在最终 LaTeX 尺寸下检查 100% 缩放页：最小文字不低于 6 pt，常规图中文字保持 8 pt，caption 保持模板字号；颜色之外必须保留 marker、线型、形状或文字标签。

# ICLR 9 页论文图表执行手册

本手册把 250 篇论文的视觉统计压缩为一套直接执行的 ICLR 配置。正文固定 **6 幅 Figure + 4 张 Table**，附录固定 **8 幅 Figure + 7 张 Table**。对象可以复合职责，图表总数保持稳定。

## 一、9 页正文配置

| 页码 | 对象 | 版式 | 必须表达的内容 |
|---:|---|---|---|
| 1 | Figure 1 | 5.50 in 全栏，1–2 panel | 工作对象、现有缺口、方法主接口、headline 结果；同一视觉语言贯穿全文 |
| 2–3 | Figure 2 | 5.50 in 全栏，2–3 panel | 输入→组件→状态/表示→输出；每个组件写名称、变量和箭头语义 |
| 3–4 | Table 1 | 2.63 in 单栏或 5.50 in 全栏 | 数据、任务、模型、基线、指标方向、预算、seed/run、分母与硬件 |
| 5 | Table 2 | 5.50 in 全栏 | 主比较精确数值；按 benchmark/模型 row group；性能、成本和失败值同表 |
| 5–6 | Figure 3 | 2.63 in 单栏或双 panel 全栏 | budget/scale/time/data 的折线趋势；4 个系列；明确 band/error bar |
| 6–7 | Figure 4 | 5.50 in 全栏，2–4 panel | 机制诊断→组件消融→替代解释控制；panel 顺序对应贡献顺序 |
| 7 | Table 3 | 2.63 in 单栏 | 组件删除、替代组件、超参和交互消融；同一指标与主表对应 |
| 7–8 | Figure 5 | 2.63 in 单栏或双 panel 全栏 | 跨数据、规模、任务或扰动的鲁棒性与异质性；保持主结果的坐标和编码 |
| 8 | Figure 6 | 5.50 in 全栏 | 效率—效果、失败面或匹配质性样本；直接标出 operating point 与失败 |
| 8 | Table 4 | 2.63 in 单栏 | latency、memory、token/query、训练成本、OOM/failure count |
| 9 | 结论回指 | 无新增视觉对象 | 按 Figure/Table 标签回收对象、机制、结果、成本和失败面 |

这一顺序覆盖超过 60% 论文出现的 conceptual diagram、line chart、pipeline、主比较、headline、鲁棒性、方法接口、理论/机制、消融、实验设计、质性证据、复现和效率成本。

## 二、每个 Figure 的精确规格

| 属性 | 配置 |
|---|---|
| 单栏宽度 | 2.63 in |
| 全栏宽度 | 5.50 in |
| 正文面板 | 中位 2；主结果最多 4 |
| 附录面板 | 中位 2；同一 facet 语法扩展 |
| 常规字号 | 8 pt |
| tick/legend | 7.5 pt |
| panel 标题 | 8.5 pt bold |
| 绝对最小字号 | 6 pt |
| 数据线 | 1.0 pt |
| 轴线 | 0.6–0.8 pt |
| marker | 3.5 pt；`o/s/^/D/v` |
| 系列数 | 4 个主系列；超过 5 个拆 panel 或移附录 |
| 主色 | `#1F77B4 #FF7F0E #2CA02C #D62728 #9467BD` |
| 冗余编码 | 每个系列同时绑定颜色、marker、线型；关键点直接标注 |
| 网格 | 折线图使用 0.45 pt 浅灰双轴网格；示意图不加网格 |
| 输出 | PDF/SVG；含真实图像的 panel 单独以 300 dpi 栅格嵌入 |

### Figure 1：工作对象与 headline

左侧画输入和任务约束，中间画现有方法断点，右侧画本文接口与一个 headline operating point。Figure 1 同时完成问题定义、方法预告和结果预告；不使用装饰性大图。

### Figure 2：方法接口

每条箭头写明传递对象，每个组件下方放一个变量或公式锚点；组件名称与方法小节、算法、消融 row 完全一致。颜色表达组件角色，箭头/边框/位置同时编码。

### Figure 3：主趋势

x 轴只承载一个干预量：预算、规模、时间、数据量或阈值。y 轴是主决策量。主方法和关键基线共 3–4 条曲线；band/error bar 在 caption 中定义为 SD、SE 或分布统计；对数轴在轴标签和 caption 同时声明。

### Figure 4：机制与消融

panel a 展示诊断量，panel b 展示组件干预，panel c 展示替代解释控制，panel d 展示跨任务一致性。所有 panel 使用同一方法顺序、颜色、marker、范围和聚合。

### Figure 5：鲁棒性与异质性

沿用 Figure 3 的坐标、方法顺序和统计单位，改变一个外部条件：数据域、模型规模、任务组或扰动强度。主结论保持可见，反向切片直接标注。

### Figure 6：成本、失败与质性证据

数值工作使用质量—成本 Pareto、latency/memory scaling 或 failure rate；生成式工作使用固定 prompt/target × method grid，并保留 reference/ground truth、随机种子、样本数量和失败样本。

## 三、每张 Table 的精确规格

| 属性 | 配置 |
|---|---|
| 表体 | 8 pt，行距 9 pt，`arraystretch=1.08` |
| 正文行列 | 6 行 × 6 列为中心；控制在 6–10 行、6–8 列 |
| 表头 | 2 层；第一层写 benchmark/setting，第二层写 metric 与 ↑/↓ |
| 精度 | 2 位小数；同一 metric 全表一致 |
| 线条 | `booktabs`；`toprule/midrule/bottomrule`，不用完整网格 |
| 对齐 | 方法列左对齐；数值列按小数点对齐 |
| 高亮 | best bold、second underline；failure/OOM 用固定符号并在 caption 定义 |
| 统计 | `mean ± SD/SE`；表注写 seed/run、聚合层级、分母和 imported result 来源 |

Table 1 固定实验协议，不使用 best/second-best 排名高亮；Table 2 给主结果，Table 3 给组件消融，Table 4 给成本与失败，并只在可比较数值中使用 bold/underline。宽表通过 row group 和两层表头压缩；不使用 `\resizebox` 把正文压到 6 pt 以下。

## 四、caption 的精确写法

正文 Figure caption 写 48 词，正文 Table caption 写 33 词。统一采用六步结构：

```text
1. 粗体功能标题
2. 对象、数据集、预算或干预
3. panel、颜色、线型、marker、箭头和符号的编码
4. 比较对象与指标方向
5. 一个决定性读数
6. seed/run、聚合、band/error bar、failure 记号和附录指针
```

Figure caption 例式：

```text
Method scaling and operating point. Test success versus inference budget on
three benchmarks. Color identifies the method; marker and line style repeat
the same encoding. Lines are means over five seeds and bands show ±1 SD.
Our method remains above both baselines across the full budget range and
reaches the selected operating point at B=8. Per-task values appear in Table 6.
```

Table caption 例式：

```text
Main comparison. Test performance and cost across three settings; ↑/↓ marks
the preferred direction. Values are mean ± SD over five seeds. Bold and
underline indicate the best and second-best result within each column; × marks
budget failure. Full per-task results and run-level values are in Appendix C.
```

## 五、附录配置

附录固定 8 幅 Figure 与 7 张 Table：

1. Figure A1：完整数据集/任务趋势，与正文 Figure 3 同坐标和配色；
2. Figure A2：超参、规模或阈值敏感性；
3. Figure A3：run/seed 分布、失败率、长尾或 per-unit 异质性；
4. Figure A4：完整质性网格，包含成功、失败、reference 与选择协议；
5. Figure A5：扩展机制诊断、额外 architecture 或复现流程；
6. Figure A6：鲁棒性分解、校准、分布偏移或反向任务切片；
7. Figure A7：正文 Figure 的同构扩展；
8. Figure A8：正文 Figure 的同构扩展；
9. Table A1：逐任务/逐数据集主结果；
10. Table A2：完整消融与替代组件；
11. Table A3：超参、软件、硬件、预算和训练/推理设置；
12. Table A4：成本、失败、OOM、样本数与 run-level 汇总；
13. Table A5：完整 seed/run 数值、不确定性和统计检验；
14. Table A6：逐模型×数据集×指标的全矩阵与 imported result 来源；
15. Table A7：正文 Table 的逐单位完整数值；

正文每个主张在首次出现处调用对应附录对象；附录沿用正文的方法顺序、颜色、marker、缩写、指标单位和精度。

## 六、交付流程

1. 先定义 claim→visual map，再运行实验；每个贡献绑定一个 Figure/Table 和一个附录扩展。
2. 结果统一落到 tidy CSV/JSON；绘图脚本只读结果表，不手填最终数值。
3. 使用 [`templates/visuals/iclr_style.py`](../templates/visuals/iclr_style.py) 生成 2.63 in/5.50 in PDF/SVG。
4. 使用 [`table_style.tex`](../templates/visuals/table_style.tex) 与 [`method_figure.tex`](../templates/visuals/method_figure.tex) 建表和方法图。
5. 在最终 ICLR 页面 100% 缩放检查字体、legend、线型、颜色、caption 与跨页位置。
6. 逐对象核对数据分母、方向、seed/run、聚合、单位、failure/OOM 和正文引用。
7. 运行 `make visual-templates` 复现示例，使用 [`main_result.pdf`](../templates/visuals/examples/main_result.pdf) 对照最终输出密度。

## 七、写作与视觉语言

- 图表直接陈述对象、干预、读数和解释；删除防御性铺垫、自我设限和 claim-boundary 话术。
- 不在 caption 里重复“我们的方法有效”；写清比较量、方向、数值、范围和机制读数。
- 不用“for completeness”引出附录；正文先给决策接口，再直接指向完整数值、分布、失败和复现设置。
- 不把不利结果藏在语言里；用 failure panel、失败计数、OOM 符号、长尾分布和停止条件形成可见证据。
- 同一对象在方法图、公式、主结果、消融、结论和附录保持同名、同色、同顺序。

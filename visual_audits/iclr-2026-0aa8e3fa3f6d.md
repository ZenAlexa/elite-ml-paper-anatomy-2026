# Visual audit — `iclr-2026-0aa8e3fa3f6d`

## 审计范围与事实源

- 论文：*To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models*（ICLR 2026）。
- PDF：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/pdfs/iclr-2026-0aa8e3fa3f6d.pdf`，27 页，letter 纸张（612 × 792 pt）。
- 阅读范围：逐页读取 PDF 第 1–27 页，涵盖正文、References（第 11–15 页）和 Appendix A–F（第 15–27 页）。含视觉对象的页面以 200 dpi 渲染（1700 × 2200 px）；PDF 的对象清单、字体对象、嵌入图像清单和渲染结果共同用于核对。
- 对象核对：PDF 实际包含 Figure 1–10 与 Table 1–2，共 10 幅图、2 张表。正文对象为 Figure 1–3、Table 1；附录对象为 Figure 4–10、Table 2。与 `readings/iclr-2026-0aa8e3fa3f6d.json` 的初始 inventory 一致；第 15 页的 References/Appendix 交界处没有遗漏对象。
- 页面布局：正文为双栏；Figure 1、Figure 2 横跨正文栏宽，Table 1 位于第 7 页上方，Figure 3 位于第 10 页右栏。附录为单栏。图中坐标与颜色以下述 200 dpi 渲染为主要视觉判断，字体名称和线条对象以 PDF 为准。

### 公共视觉源检索

先核查了 `/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/reports/tables/visual_source_inventory.csv` 与 `corpus/visual_sources/iclr-2026-0aa8e3fa3f6d/`：inventory 将此论文标为 `no_public_source_found`，自动候选为 `SWE-agent/mini-swe-agent`（score 0）及 `radarFudan/Awesome-state-space-models`；目标 visual-source 目录不存在。随后沿 PDF 的明确链接与标题执行只读 `gh` 检索：

1. PDF 第 9 页脚注和 Appendix E 第 26 页明确链接 `https://github.com/SWE-agent/mini-swe-agent`。`gh api repos/SWE-agent/mini-swe-agent` 的仓库描述是通用 GitHub issue/CLI agent；递归 tree 只有 `docs/assets/mini-swe-agent-banner.svg`、`docs/assets/mini_square.svg` 等产品文档素材，没有本论文的 `plot*`、`figure*`、`table*`、`.tex`、`.tikz`、`.pgf`、`.ipynb` 或 style/data 文件。
2. 完整论文标题、`iclr-2026-0aa8e3fa3f6d` 和精确 Figure 1 caption 的 `gh search repos/code` 没有找到论文源。精确 caption 的 code 搜索只命中本仓库 reading 文件，属于审计数据，已排除。
3. `radarFudan/Awesome-state-space-models` 的仓库元数据仅表明它是 SSM 论文集合，未提供本文标题、作者、paper ID 或图表源的直接关系，按规则排除。

结论：没有可由作者链接、仓库元数据或标题严格验证的公开绘图/表格/LaTeX 源；不把 `mini-swe-agent` 的文档素材或 PDF 内嵌编译资产登记为本文 source file。

## 对象总表

| 对象 | PDF 页 | 模块 | 位置 | 物理布局与职责 |
|---|---:|---|---|---|
| Figure 1 | 2 | 1 Introduction | main | 三种 coding trajectory 示意 + 右侧六系列 pass-rate 折线，headline/实验设置 |
| Figure 2 | 3 | 1 Introduction | main | 左侧 pointer-memory trajectory + 右侧 addition accuracy，机制与 headline |
| Table 1 | 7 | 3 Experiments / 3.1 | main | 五种模型 × 四类 synthetic task 的最大外推长度 |
| Figure 3 | 10 | 3.4 Long-Context Natural-Language | main | Oolong 任务中 5–25 examples 的两系列 accuracy |
| Figure 4 | 20 | Appendix D.2 | appendix | Logical Graph 与 Code Fixing 的图结构、代码表达和截图 |
| Table 2 | 22 | Appendix D.4 | appendix | recursive Hanoi 的五模型结果 |
| Figure 5 | 22 | Appendix D.4 | appendix | 10 个 Mamba seeds 的 Hanoi exact accuracy |
| Figure 6 | 23 | Appendix D.5 | appendix | 四 panel、五模型 baseline accuracy |
| Figure 7 | 24 | Appendix D.6 | appendix | 六 panel 的训练步数 × 训练长度消融，带误差 envelope |
| Figure 8 | 25 | Appendix D.8 | appendix | 三个 training-budget panel 的 multiplication task-mixture accuracy |
| Figure 9 | 25 | Appendix D.8 | appendix | 三个 training-budget panel 的 auxiliary addition accuracy |
| Figure 10 | 26 | Appendix E | appendix | SWE-agent-LM-32B 的 trajectory-length 与 pass-rate 统计 |

## Figure 1

- **页面与几何**：PDF p.2，`main`，`page_width`。上部约四个视觉单元：左侧 Single-Turn、左下 Interactive、中部 Distillation 三组 trajectory 卡片，右侧一个折线图；图例位于折线图下方。三组卡片用箭头、命令/观察/思考框展示 agent 轨迹。
- **类型与用途**：`line`、`pipeline`、`conceptual_diagram`；`headline`、`experimental_design`、`main_comparison`、`qualitative_evidence`。图把 coding task 的三种数据生成策略与外推曲线放在同一视线内。
- **渲染、坐标与绘图语法**：PDF 以矢量路径和文字为主，SWE-agent 图标含一个小型 JPEG，整体为 mixed。折线图 x 为 4–30 个 functions 的线性数值轴，y 为 0–100% pass rate 的线性轴；x/y 网格均可见；右图有 6 个系列、底部横向 legend、无 direct label、无 hatch、无 uncertainty；三种 strategy 用 dotted/dashed/solid 三种线型；红色虚线为 1 条训练上限 reference line（16 functions）；折线约 1.4 pt。左侧示意区无坐标轴。
- **数据编码**：x=`number of functions`；y=`pass rate (%)`；color=`Mamba` 蓝与 `Pythia` 橙；shape=null；line=`Single-Turn` dotted、`Interactive` dashed、`Distillation` solid；facet=`三种轨迹示意 + 一张六系列结果图`；text=`strategy heading、16-function marker、legend`。
- **复杂度**：score 4；4 个视觉 panel；6 条数据系列；6 个 legend 项；约 4 个显式 annotation；数据标记数量未从图中固定读出，代码图和折线图的观测粒度不同。
- **视觉属性**：PDF 对象中的正文/示意文字包含 `NimbusRomNo9L`、`Times New Roman`、`Aptos`、`Lucida Console`、`Cambria Math`；示意命令为等宽体，标题为粗体，图中估计 4.7–7.3 pt，折线图 sans-serif 约 6–8 pt。主色近似为 `#376380`（Mamba）、`#BF572E`（Pythia）、`#F08080`（训练上限）、`#B0B0B0`（网格）、`#F6C6AD`/`#B4E5A2`/`#DCEAF7`（命令/观察/提示卡片），黑色承担文字和边框。颜色、strategy 名称和线型有冗余编码，灰度下仍可借助线型与 legend 区分。
- **Caption**：
  > Figure 1: We finetune Mamba and Pythia (Transformer) on trajectories collected from different tool-use agents for solving a coding problem. 1) Single-Turn Tool-Use: Hard-coded agent that prints all the files in the repository and then outputs all the required changes. 2) Interactive Tool-Use: Hard-coded agent that iteratively runs the code, changes a few files, runs the code again etc. until all problems are resolved. 3) Distillation: SWE-agent Language Model (Yang et al., 2025) instructed to solve the bug in the code. Models are trained on codebases of up to 16 files (dashed red line), with context length 8K, and evaluated on larger codebases with longer context. While Pythia outperforms Mamba on smaller codebases and single-turn tool use, Mamba displays favorable performance on large codebases when trained to imitate interactive agents (agents 2 and 3), extrapolating beyond the training distribution.

  词数约 139；动作：`title`、`setup`、`encoding_key`、`comparison`、`main_finding`。caption 内三种 strategy 名称加粗，开头标题本身不单独加粗；脱离正文可理解训练上限、评测范围、比较对象和主发现，`self-contained=true`、`main_finding_stated=true`。
- **数据与统计**：训练 codebase 最多 16 files、context 8K，评测更大 codebase。小规模和 single-turn 上 Pythia 较高；interactive/distillation 在大规模 codebase 上 Mamba 曲线下降较慢。图没有 error bar、band、seed 分解、测试分母或失败计数；被筛选的成功且较短 SWE trajectories 的条件出现在正文 p.9，caption 未重复。
- **证据关系**：引言的「bounded memory 与 interactive tool-use」主线 → Section 3.3 的 code-fixing dependency graph 和三类 agent → Figure 1 的数据策略/外推比较 → Appendix E 的 prompt 与 Figure 10 的 agent 轨迹统计。它承担 headline 与实验设计接口，未承担单独的组件消融。
- **优点**：三种 trajectory 的信息流程与曲线 strategy 一一对应；训练上限用醒目的红色竖线定位；caption 同时给出 agent 定义、训练边界、评测扩展和主结论。
- **缺陷**：六条曲线主要依靠颜色与线型，图例较小；单列图中三组示意卡片占据大量面积，曲线的具体数值难以读取；过滤成功/短 trajectory、best-seed 汇报和缺失分母没有进入 caption；“大 codebase”没有给出精确函数范围。
- **可复用模式**：将数据生成策略的局部 trajectory 画面与同一 x 轴上的外推曲线并置，使用 strategy-specific 线型、训练边界 reference line 和自包含 caption，适合解释「训练接口 → 长度外推」链条。
- **证据定位**：p.2 上半部，bbox 约 `[108, 60, 504, 238]`；依据 `rendered_observation`。

## Figure 2

- **页面与几何**：PDF p.3，`main`，`page_width`。左侧为四个时间切片（Step 0、9、20、21）的 pointer-memory 轨迹，右侧为一张 addition accuracy 折线图；两个 panel 横向共享视觉焦点。
- **类型与用途**：`line`、`conceptual_diagram`；`headline`、`method_interface`、`theory_mechanism`、`main_comparison`。
- **渲染、坐标与绘图语法**：全为矢量；右 panel x 为 10–1000 的 log 轴，y 为 0–1 的 linear accuracy 轴，x/y 网格可见；5 个模型系列、右侧 legend、无 direct label、无 hatch/reference line/uncertainty；5 种 marker（circle/square/triangle/diamond/down-triangle），曲线为实线，约 1.5 pt。左 panel 用 step 行、指针红色箭头、彩色 token 卡片和省略号组织生成顺序。
- **数据编码**：x=`sequence length`（右图 log）；y=`accuracy`；color=`Mamba/LSTM/GRU` 三种蓝色与 `Pythia/Mistral` 两种橙色；shape=`五模型 marker`；line=`模型系列实线`；facet=`左 trajectory、右结果曲线`；text=`Step、pointer、command、read observation、sum/carry、legend`。
- **复杂度**：score 3；2 个主 panel（左侧含 4 个时间切片）；5 个系列；5 个 legend 项；约 16 个指针/步骤标注；数据标记约 80 个。
- **视觉属性**：图表文字使用 PDF `DejaVu Sans` Type 3（约 7.3–10.7 pt），轨迹命令使用 `Lucida Console`/`Aptos` 等宽或 sans-serif，pointer 标签为红色。主色为 `#376380`、`#4782A6`、`#7FB1D1`、`#BF572E`、`#E37944`；轨迹颜色为 `#EEF6AD`（输入 token）、`#A6CAEC`（thought/状态）、`#F6C6AD`（command）、`#B4E5A2`（observation）、`#E59EDD`（output）、`#C00000`（pointer label），并有 `#D1D1D1` 省略号/中性块、`#B0B0B0` 网格。颜色与 token 角色共同表达语义，marker 为模型身份冗余；图表蓝/橙系列在灰度下仍有 marker 辅助。
- **Caption**：
  > Figure 2: Left: Illustration of an interactive tool-use agent trajectory with pointer-based memory tool for solving multi-digit addition. The agent can generate thoughts (blue), outputs (purple) or commands (orange), and receive observations (green) from the memory tool. At each step, we show the state of the memory context on the top row, and below it show the sequence of generated tokens. Right: Accuracy of recurrent/SSM models (Mamba, LSTM, GRU) and Transformers (Pythia, Mistral) trained on trajectories for ≤ 5-digit addition, evaluated on up to 1,000-digits (log scale).

  词数约 87；动作：`title`、`setup`、`encoding_key`、`comparison`。`Left`/`Right` 及 token role 在 caption 中解释，图例解释模型；`self-contained=true`、`main_finding_stated=false`。
- **数据与统计**：训练轨迹为不超过 5-digit addition，评测到 1,000 digits；指标是 trajectory 与 final answer 的 exact-recovery accuracy。Mamba/LSTM 在图示范围保持高准确率，Pythia/Mistral 在短长度后接近 0，GRU 在最长点约 0.8。无误差带、重复运行摘要、分母或 seed 汇总；正文 p.7 说明未测量 1,000 digits 以外的范围。
- **证据关系**：Figure 2 左侧将 Section 2.2 的 external-memory protocol 变成可读轨迹，右侧对应 Theorem 2.2 后的 addition 实验；正文 p.7 调用它作为 5-digit→1,000-digit 例证，Appendix D.1/D.3 给 token protocol 与算法步骤，Appendix D.7 给无工具/单轮消融。
- **优点**：用相邻时间切片展示 pointer 如何读写并回看上下文；右侧 log x 轴覆盖三个数量级；caption 定义四类 token 颜色、模型分组与训练/评测范围。
- **缺陷**：左图的四个切片只展示一个短例子，不能直接显示长序列的状态容量；右图没有误差/分母，模型的五种 marker 和小 legend 在缩放后拥挤；exact-recovery 的统计定义依赖正文。
- **可复用模式**：把「可执行 memory interface 的局部 trace」与「同一 interface 的长度曲线」成对展示，并用角色颜色、模型 marker 和 log 轴同时承载机制与外推。
- **证据定位**：p.3 上半部，bbox 约 `[108, 60, 504, 251]`；依据 `rendered_observation`。

## Table 1

- **页面与几何**：PDF p.7，`main`，`page_width`；caption 在表上方，表格居中，5 行模型、5 列（Model、n×1、n×2、Logical Graph、Hanoi⁷），无竖线。横线把前三个 SSM/RNN 行与 Pythia/Mistral 行分组。
- **用途与表格语法**：`headline`、`main_comparison`。表头为单层，row group 为 2，`booktabs` 风格；Mamba、LSTM、GRU 的部分最佳单元以粗体突出，没有颜色、下划线或箭头；数值均为整数/百分比，精度为 0 位小数。
- **字体与规则**：主体和表头为 `NimbusRomNo9L` 约 10 pt，`n`、`×`、`→`、`p`、`≥` 等使用 Computer Modern math/symbol 对象；粗体使用 Nimbus medium。PDF 中可见 top/mid/bottom horizontal rules，线宽约 0.398 pt。
- **Caption**：
  > Table 1: Experimental results for synthetic tasks for different models. The notation n → m(p%) means a model trained on length n achieves accuracy p on length m (for the largest m s.t. p ≥ 5%).

  词数约 36；动作：`title`、`setup`、`encoding_key`、`comparison`。它定义了 `n → m(p%)` 和 5% 阈值，`self-contained=true`；没有在 caption 中直接说出哪个模型胜出，`main_finding_stated=false`。
- **表头、数据与统计**：模型行是 Mamba、LSTM、GRU、Pythia、Mistral；四个任务列分别为 n×1、n×2、Logical Graph、Hanoi⁷。单元格报告最大 `m` 与对应 accuracy：Mamba 为 `10→1K (100%)`、`10→1K (100%)`、`10→1K (98%)`、`8→12 (49%)`；LSTM 为 `10→500 (100%)`、`10→100 (100%)`、`10→1K (100%)`、`8→8 (100%)`；GRU 同样为 `10→500`、`10→100`、`10→1K`、`8→8`；Pythia 为 `10→20 (79%)`、`10→14 (12%)`、`10→1K (5%)`、`8→8 (100%)`；Mistral 为 `10→13 (25%)`、`10→20 (33%)`、`10→500 (9%)`、`8→8 (100%)`。这些是各模型 best seed 的点结果；没有 SD/SE、区间、seed 数、测试分母或失败计数。脚注说明 Hanoi 使用 Mamba/Pythia 10 seeds、其他模型 3 seeds，表中仍只呈现最佳 seed。
- **证据关系**：Section 3.1 的 multiplication 与 Logical Graph、Section 3.2 的 Hanoi → Table 1 的统一「最大长度且 p≥5%」摘要；Figure 2 展示 addition，Figure 6 展开三个 baseline 曲线，Table 2 展开 recursive Hanoi。
- **优点**：统一 `n→m(p%)` 压缩训练长度、外推长度和准确率；四个任务并排后可快速比较模型族；横线分出 recurrent/SSM 与 Transformer。
- **缺陷**：表格把阈值后的最大长度作为单点摘要，隐藏完整曲线和 seed 异质性；Hanoi⁷ 的脚注标记小且阈值与测试分母仍需回正文；没有成本、失败数或不确定性列。
- **可复用模式**：在跨任务外推表中固定 `train length → largest test length (accuracy)` 语法，并在表头/ caption 同时定义筛选阈值、聚合规则和 seed 处理。
- **证据定位**：p.7 caption 与表格，bbox 约 `[108, 82, 504, 178]`；依据 `pdf_object`。

## Figure 3

- **页面与几何**：PDF p.10，`main`，`single_column`，位于右栏与 Section 3.4 正文并排。单 panel line chart，x ticks 为 5、10、15、20、25，y 范围 0.4–1.0；legend 在图内下方。
- **类型与用途**：`line`；`main_comparison`、`robustness`。它给出 Oolong long-context task 的简短 OOD slice。
- **渲染、坐标与绘图语法**：全为矢量；x 是离散 examples 数（5 个等距观测点，按 categorical 处理），y 为 linear accuracy；x/y 网格均可见；2 个系列、2 个 legend 项、circle marker、solid line、无 direct label/hatch/reference line/uncertainty，线宽约 1.5 pt。
- **数据编码**：x=`Number of Examples`；y=`Accuracy`；color=`Mamba (1.4B)` 蓝、`Pythia (1.4B)` 橙；shape=`circle`；line=`solid`；facet=null；text=`title、axes、legend`。
- **复杂度与颜色**：score 2；1 panel；2 series；2 legend items；0 annotation；约 10 个 marker。PDF 图表对象使用 `DejaVu Sans`，标题约 10–13 pt、轴/刻度约 7–10 pt；主色 `#1F77B4`、`#FF7F0E`，网格 `#B0B0B0`，背景/边界含 `#FFFFFF`、`#CCCCCC`。两系列只用颜色区分，灰度安全性低。
- **Caption**：
  > Figure 3: Accuracy of Pythia and Mamba trained on in-context datasets with 5 examples, evaluated on up to 25 examples.

  词数约 20；动作：`title`、`setup`、`comparison`。caption 没有定义 Oolong/Yahoo task、误差或样本分母，也没有直接写出 Mamba 的相对优势；`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：模型在最多 5 examples 的 in-context trajectory 上训练，在 5–25 examples 上评测。渲染点约显示两模型在 5 examples 均为 0.85，25 examples 时 Mamba 约 0.65、Pythia 约 0.59；正文把该任务称为 Yahoo Answers Topic Classification 的代表性 Oolong slice。无 error bar、seed、分母或失败值。
- **证据关系**：Section 3.4 从 synthetic/coding 外推转向自然语言长上下文；Figure 3 支持「两模型 in-distribution 类似、Mamba 在更长 dataset 上保持较高」的有限任务实例，正文 p.10 的 conclusion 回收这一观察。
- **优点**：x 轴观测点和训练边界直观；两模型 legend 与标题足够简短，读者可迅速看到随 examples 增长的差距。
- **缺陷**：只有一个 Oolong task slice；caption 缺少任务内容、accuracy 分母、重复数和 uncertainty 定义；circle marker 相同且没有线型冗余，颜色依赖明显。
- **可复用模式**：用少量固定 context-length 点画同尺度 OOD 曲线，并在 caption 补齐任务、训练上限、评测分母和重复运行说明。
- **证据定位**：p.10 右栏，bbox 约 `[365, 136, 504, 283]`；依据 `rendered_observation`。

## Figure 4

- **页面与几何**：PDF p.20，`appendix`，`page_width`。单栏宽度内上下两行：上方 Logical Graph，中央 graph→code 箭头；下方 Code Fixing，中央 dependency graph→代码编辑器截图。左侧任务标签、右侧代码表达形成对照。
- **类型与用途**：`network`、`screenshot`、`conceptual_diagram`；`method_interface`、`experimental_design`、`qualitative_evidence`。
- **渲染、坐标与绘图语法**：整体 mixed。图结构、节点、箭头和公式文本是矢量；右下代码树和编辑器是 PDF 内嵌 raster PNG。无 x/y 轴、无网格、无 legend、无 uncertainty/reference line；节点圆形、定向箭头和直接标签承载关系。
- **数据编码**：x/y=`无数量轴，位置表示图层与从 graph 到 code 的转换`；color=`蓝色输入/箭头、绿色中间节点、桃色输出节点、深色公式文字`；shape=`圆形变量/函数节点、箭头、代码框`；line=`有向依赖边`；facet=`Logical Graph top / Code Fixing bottom`；text=`v630、v872、v622、v191、v240、v539、main、f169、f352、f643、f816、foo`。
- **复杂度与颜色**：score 4；4 个视觉子单元；无数据 series/legend；约 15 个节点、边和代码注释 annotation；数据标记未作为统计点定义。矢量部分颜色包括 `#4E95D9`、`#156082`、`#163E64`、`#A6CAEC`、`#84E291`、`#F6C6AD`、`#F2F2F2`、`#7F7F7F`、`#042433`、`#000000`、`#FFFFFF`；嵌入代码截图还出现 `#008000`、`#498BA7`、`#0000FF`、`#A21515`。字体对象含 `Times New Roman`、`Lucida Console`、`Cambria Math`，约 6–10 pt；截图内部文字按 rendered estimate 处理。
- **Caption**：
  > Figure 4: Illustration of Logical Graph reasoning task and code fixing task. We generate random graphs that define logical function structure (top) or code dependencies (bottom), and synthetically generate problems according to these graph structures.

  词数约 35；动作：`title`、`setup`、`comparison`。caption 没有写出 search tool、bug variable 或节点数，`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：上图示意 `k=3` input nodes、Boolean AND/OR/negation 的 DAG；右侧把随机变量赋值转成 Python-like expression。下图示意 main 到 foo 的 dependency paths 与文件列表/代码片段。对象是任务构造的概念证据，不报告样本、聚合或 uncertainty。
- **证据关系**：Section 3.2/3.3 的 Logical Graph 与 Code Fixing 定义 → Figure 4 的 graph/code representation → Appendix D.2 的随机 DAG 与 Appendix E 的 agent prompt；Figure 1 使用该 code-fixing graph 的 trajectory strategy，Table 1/Figure 6 测量图结构任务的外推。
- **优点**：同一页面同时展示逻辑计算图和代码依赖图，graph→representation 的箭头清楚；节点颜色与直接标签让 AND/OR/negation 和函数路径可定位。
- **缺陷**：没有图例，颜色语义由局部位置和正文推断；右下 screenshot 在单栏阅读时细字密集；逻辑图与代码图的随机生成规模、search command 和 bug 变量没有写在 caption 中。
- **可复用模式**：对结构化 synthetic task 使用「抽象图 → 可执行代码表达」双行版式，保持节点颜色、方向箭头和直接标签一致，并在 caption 明确构造参数和工具接口。
- **证据定位**：p.20 上半部，bbox 约 `[121, 87, 489, 241]`；依据 `rendered_observation`。

## Table 2

- **页面与几何**：PDF p.22，`appendix`，`single_column`；小型居中表格位于页面上方，2 列（Model、Hanoi (recursive)）、5 个模型行。横线分出 GRU 与 Transformer 行，无竖线。
- **用途与表格语法**：`main_comparison`、`robustness`；单层表头、2 个 row group、`booktabs`；LSTM 的 `7→9 (83%)` 粗体，其他单元为 regular；0 位小数。
- **字体与规则**：`NimbusRomNo9L` 约 10 pt，箭头与括号中的数学符号来自 Computer Modern math/symbol；horizontal rules 约 0.398 pt；无 cell color、underline、italic 或 arrow annotation。
- **Caption**：
  > Table 2: Experimental results for the Tower of Hanoi puzzle solved recursively by different models.

  词数约 15；动作：`title`、`setup`、`comparison`。caption 未定义 `n→m(p%)`，需要 Table 1 语法或 Appendix D.4 上下文才能解释，`self-contained=false`、`main_finding_stated=false`。
- **表头、数据与统计**：Mamba `7→8 (100%)`，LSTM `7→9 (83%)`，GRU `7→8 (100%)`，Pythia `7→7 (100%)`，Mistral `7→8 (87%)`。数据是 recursive Hanoi 的 exact solution accuracy 摘要；没有重复数、seed 分散、分母、区间或 token-level failure。正文说明该 recursive variant 的外推弱于 iterative variant，Table 1 的 Hanoi 列承担主表对照。
- **证据关系**：Appendix D.3 recursive algorithm → D.4 Table 2 → Figure 6 的 recursive baseline curves；与 Figure 5 的 iterative Mamba seed sensitivity 形成边界对照。
- **优点**：小表格直接给出五模型的训练/最大外推长度和准确率；粗体 LSTM 行把唯一到 9 disks 的结果暴露出来。
- **缺陷**：notation 依赖 Table 1；表格没有把 recursive 与 iterative 的区别放入表头，也没有把 Hanoi 的指数输出长度、seed 数和 exact/token accuracy 区分开。
- **可复用模式**：在 appendix 变体结果中沿用主表 notation，同时在表头加入 algorithm variant 与 seed/metric 定义，便于和主实验直接对齐。
- **证据定位**：p.22 上方，bbox 约 `[250, 82, 367, 175]`；依据 `pdf_object`。

## Figure 5

- **页面与几何**：PDF p.22，`appendix`，`single_column`。居中的单 panel line chart，x 为 7–12 disks 的离散轴，y 为 0–1 accuracy；10 条同色 seed 曲线有明显交叉和重合。
- **类型与用途**：`line`；`robustness`、`failure`、`qualitative_evidence`。
- **渲染、坐标与绘图语法**：矢量；x=`categorical` disk count，y=`linear` accuracy；x/y 网格均有；无 legend、无 direct label、无 hatch/reference line/uncertainty band；circle marker、solid line、约 1.5 pt；10 个 seed 以单独 series 叠画。
- **数据编码**：x=`Number of Disks`；y=`Accuracy`；color=`all Mamba seeds, #1F77B4`；shape=`circle`；line=`seed-wise solid trajectory`；facet=null；text=`axes and ticks`。
- **复杂度与颜色**：score 4；1 panel；10 series；0 legend；0 annotation；约 60 个点。PDF 字体为 `DejaVu Sans` 约 7–9 pt；颜色为 `#1F77B4`、`#B0B0B0` 网格、黑色轴和白色背景。单色使灰度稳定，但 seed 身份没有冗余编码。
- **Caption**：
  > Figure 5: Performance of different seeds when training a Mamba model on Tower of Hanoi puzzles with up to 8 disks.

  词数约 21；动作：`title`、`setup`、`comparison`。caption 说明模型、seed 维度和训练上限，`self-contained=true`；没有直接说出 seed sensitivity 的主结论，`main_finding_stated=false`。
- **数据与统计**：10 个 Mamba seeds 均训练至 8 disks，图示 7–12 disks 的 exact accuracy；正文同时指出 12 disks 的 token accuracy 可达至少 99.75%，但 exact accuracy 随 seed 大幅变化。图没有均值、误差带、seed label、分母或失败类型。
- **证据关系**：Appendix D.4 解释 Hanoi 输出长度指数增长和 seed sensitivity；Figure 5 把 Table 1 的 best-seed 摘要展开成 seed-wise robustness evidence，并与 Table 2 的 recursive 结果区分。
- **优点**：不压缩 seed 差异，直接暴露 exact-match 的不稳定性；统一离散 x 轴让训练点 8 与 OOD 点 9–12 易比较。
- **缺陷**：没有 legend 或 seed 编号，曲线重合后无法追踪单个 seed；图只给 exact accuracy，读者需回正文才能理解高 token accuracy 与低 exact accuracy 的差异。
- **可复用模式**：当 best-seed 汇报可能掩盖初始化敏感性时，保留所有 seed 的同图轨迹，并在图注补充 metric、训练边界、seed 数和不确定性摘要。
- **证据定位**：p.22 中下部，bbox 约 `[185, 306, 425, 462]`；依据 `rendered_observation`。

## Figure 6

- **页面与几何**：PDF p.23，`appendix`，`page_width`。四 panel 2×2：Multiplication by 1-Digit、Multiplication by 2-Digit、Logical Graph、Tower of Hanoi (Recursive)。每个 panel 复现五模型 legend。
- **类型与用途**：`line`；`main_comparison`、`robustness`。
- **渲染、坐标与绘图语法**：全为矢量。前三个 panel 的 x 为 sequence length log 轴，右下 x 为 6–9 disks 的离散/线性轴；四 panel y 均为 linear accuracy 0–1；网格 both；每 panel 5 series、5 项重复 legend、无 direct label/hatch/reference line/uncertainty；circle/square/triangle/diamond/down-triangle 五种 marker，实线约 1.5 pt。
- **数据编码**：x=`sequence length` 或 `# of Discs`；y=`Accuracy`；color=`Mamba #376380、LSTM #4782A6、GRU #7FB1D1、Pythia #BF572E、Mistral #E37944`；shape=`模型 marker`；line=`solid`；facet=`四个任务/乘法设置`；text=`task title、axes、per-panel legend`。
- **复杂度与字体**：score 4；4 panels；每 panel 5 series；20 legend entries（重复 legend）；0 annotation；约 100 个 marker。PDF `DejaVu Sans` 字体约 5.3–8 pt，caption 使用 `NimbusRomNo9L` 约 10 pt；颜色 palette 在 SVG 对象中可读为上述五色、灰网格 `#B0B0B0`、黑/白边界。
- **Caption**：
  > Figure 6: We train various transformer (Pythia, Mistral) and SSM (Mamba, LSTM, GRU) models on Multi-Digit Multiplication, Logical Graph and Tower of Hanoi tasks, with CoT + pointer-based memory tool. Multi-Digit Multiplication: We train models on multiplying a number of up to 10-digit by a 1-digit number or 2-digit number, using the pointer-based memory tool. Logical Graph: We train models to perform a logical graph reasoning problem using search-based memory tool, training on graphs with up to 10 variables. Tower of Hanoi: We train models to solve the Tower of Hanoi (recursive implementation) reasoning problem using search-based memory tool, training on problems with up to 7 disks. The first point in each plot is the maximal problem size seen during training (i.e., all other points are out-of-distribution extrapolation).

  词数约 128；动作：`title`、`setup`、`encoding_key`、`comparison`、`appendix_pointer`。caption 给出任务、模型、训练规模和 OOD point rule，`self-contained=false`，`main_finding_stated=false`。开头的“pointer-based memory tool”与后面对 Logical Graph/Hanoi 的“search-based memory tool”形成工具描述不一致。
- **数据与统计**：multiplication 训练第一 operand ≤10 digits、第二 operand 为 1 或 2 digits；Logical Graph 训练 ≤10 variables；recursive Hanoi 训练 ≤7 disks；每 panel 第一个点为训练最大规模，后续点为 OOD。图给 exact accuracy 曲线，没有 seed/分母/error bar；正文/Appendix C 说明 hyperparameter search 与 best model 选择。
- **证据关系**：Table 1 的 synthetic summary → Figure 6 的完整 multiplication/Logical Graph/recursive Hanoi baseline curves → Appendix D.3 tool algorithms 与 D.4 recursive implementation；它补足主文只给最大外推点的可视化细节。
- **优点**：统一五模型颜色和 marker，四 panel 便于横向比较任务难度；log x 轴让 multiplication/graph 的数量级扩展可见；首点 OOD 规则写入 caption。
- **缺陷**：每 panel 重复 legend 消耗空间；caption 的工具类型表述存在冲突；best-seed、测试分母和 exact/token metric 没有进入图注；右下 Hanoi 的离散轴与前三 panel 的 log sequence length 需要读者辨认。
- **可复用模式**：用共享模型 palette、marker 和同尺度 y 轴将多任务外推曲线组成 compact baseline atlas，同时在每个 panel 标出训练边界并为不同工具接口使用明确 caption。
- **证据定位**：p.23 上半部，bbox 约 `[185, 79, 437, 305]`；依据 `rendered_observation`。

## Figure 7

- **页面与几何**：PDF p.24，`appendix`，`page_width`。2×3 六 panel：上排 Task 1、下排 Task 2，每排的 max_steps 为 250、500、800；每 panel 含 train_len=5/10/20 三条曲线与局部 legend。
- **类型与用途**：`line`、`area`；`ablation`、`robustness`。
- **渲染、坐标与绘图语法**：全矢量。x 为 10–1000 的 log sequence-length 轴，y 为 0–1 linear accuracy；网格 both；每 panel 3 series、legend 重复放置、无 direct label/hatch/reference line；circle/square/triangle marker、solid line；部分/多数配置带半透明误差 envelope，表示 5 runs 的 median absolute discrepancy；线宽约 1.5 pt。
- **数据编码**：x=`Sequence Length`；y=`Accuracy`；color=`train_len 5 #1F77B4、10 #FF7F0E、20 #2CA02C`；shape=`circle/square/triangle`；line=`solid`；facet=`Task 1/2 × max_steps 250/500/800`；text=`panel title、train_len legend`。
- **复杂度与颜色**：score 4；6 panels；每 panel 3 series；18 个重复 legend 项；0 annotation；约 144 个 marker。PDF `DejaVu Sans` 约 7–9 pt，颜色为 `#1F77B4`、`#FF7F0E`、`#2CA02C`，网格 `#B0B0B0`，band 使用对应透明色；marker 对颜色提供冗余编码，灰度中仍可借助形状。
- **Caption**：
  > Figure 7: Multiplication generalization performance for Mamba across different training configurations. Each subplot shows accuracy as a function of sequence length for a specific maximum training steps value. Different colored lines represent different training sequence lengths, with error envelope indicating median absolute discrepancy across 5 runs.

  词数约 46；动作：`title`、`setup`、`encoding_key`、`uncertainty_definition`。caption 没有定义 Task 1/Task 2 对应哪种 multiplication 设置，也没有说明 band 的上下界形式，`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：Mamba 在 train_len 5/10/20、max_steps 250/500/800 的组合上比较 sequence-length accuracy；band 为五 runs 的 median absolute discrepancy。图示 20-digit training 在三种 budget 下更稳定，5-digit/10-digit 配置在较少 steps 或长 sequence 时下降；没有各 run 数值或分母。
- **证据关系**：Section 3.1 的 task mixture/训练配置主线 → Appendix D.6 的 steps × training-digit ablation → Figure 7 展开「更多 training digits/steps 改善 OOD 稳定性」；它为 Table 1 的 best-seed summary 提供机制与稳定性背景。
- **优点**：六格矩阵把两个 task、三个 budget 和三种 train length 正交展开；band 直接显示跨 run 离散度；log x 轴覆盖到 1000。
- **缺陷**：Task 1/2 语义未在图注解释；legend 位置随 panel 改变，重复信息多；band 的统计定义只有一句 median absolute discrepancy，缺少上下界/聚合方向。
- **可复用模式**：将预算、训练长度和任务变体做成规则 facet grid，曲线保持固定颜色/marker，并把重复运行的不确定性作为 envelope 与定义一起呈现。
- **证据定位**：p.24 上半部，bbox 约 `[134, 79, 490, 313]`；依据 `rendered_observation`。

## Figure 8

- **页面与几何**：PDF p.25，`appendix`，`page_width`。三个横向 panel，标题分别为 Multiplication / Max Steps: 250、500、800；每 panel 画四个 mixing weights。
- **类型与用途**：`line`；`ablation`、`mechanism`、`robustness`。
- **渲染、坐标与绘图语法**：全矢量。x 为 Number of Digits 的 log 轴，y 为 0–1 linear accuracy；网格 both；每 panel 4 series，legend 在 panel 内重复，circle/square/triangle/diamond 等 marker，solid line；vertical error bars 含 caps，表示 random-seed variability；无 direct label/hatch/reference line，线宽约 1.5 pt。
- **数据编码**：x=`Number of Digits`；y=`Accuracy`；color=`w=0.0 #7FB1D1、w=0.33 #BF572E、w=0.5 #3A8C52、w=0.6 #992335`；shape=`四个 weight 的 marker`；line=`solid`；facet=`max_steps 250/500/800`；text=`panel title、weight legend`。
- **复杂度与颜色**：score 3；3 panels；4 series；12 个 legend 项；0 annotation；约 180 个 marker/errorbar 组合。PDF `DejaVu Sans` 约 7–9 pt，palette 还含黑/白、`#B0B0B0` 网格和 `#CCCCCC` 边界。marker 与颜色提供冗余，灰度可读性中等。
- **Caption**：
  > Figure 8: Multiplication task accuracy under co-training with varying training budgets (see Sec 3.1).

  词数约 14；动作：`title`、`comparison`、`appendix_pointer`。caption 未列 250/500/800、weight 定义或 error bar 语义；`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：primary multiplication 与 auxiliary addition 共训；`w=0` 表示只训练主任务，更高 `w` 为 auxiliary fraction。250 steps 时所有曲线很快降到低 accuracy；500 steps 时多数 weight 保持高值但部分长序列崩落；800 steps 时三组 weight 接近高 accuracy。error bars 表示 seed variability，未给 seed 数、分母或 exact failure counts。
- **证据关系**：Section 3.1 的 task mixture 主张 → Figure 8 的 primary multiplication view → Figure 9 的 auxiliary addition companion；Appendix D.8 文字解释 budget、weight 和 error bar。
- **优点**：同一 y 轴和三个 budget panel 把训练预算效应直接并排；error bar 显示 seed variability，weight marker/颜色稳定。
- **缺陷**：caption 把关键定义放到正文；中间 budget 中 weight-specific collapse 需要放大才能读；没有把 task mixture 的样本分母、seed 数或 loss/accuracy 聚合写入图中。
- **可复用模式**：固定主任务、横向预算 facet 和归一化 mixture weight palette，配合 error bar 展示预算不足时的协同/退化边界。
- **证据定位**：p.25 上部，bbox 约 `[134, 208, 491, 329]`；依据 `rendered_observation`。

## Figure 9

- **页面与几何**：PDF p.25，`appendix`，`page_width`。三个横向 panel，标题为 Addition / Max Steps: 250、500、800；位置紧随 Figure 8，作为同一 task mixture 的 auxiliary view。
- **类型与用途**：`line`；`ablation`、`mechanism`、`robustness`。
- **渲染、坐标与绘图语法**：全矢量。x 为 log Number of Digits，y 为 linear 0–1 accuracy；网格 both；每 panel 4 weight series，legend 重复、solid line、四种 marker、error bars/caps；无 direct label/hatch/reference line，线宽约 1.5 pt。
- **数据编码**：x=`Number of Digits`；y=`Accuracy`；color=`w=0.0 #7FB1D1、w=0.33 #BF572E、w=0.5 #3A8C52、w=0.6 #992335`；shape=`weight marker`；line=`solid`；facet=`max_steps 250/500/800`；text=`panel title、weight legend`。
- **复杂度与颜色**：score 3；3 panels；4 series；12 个 legend 项；0 annotation；约 180 个 marker/errorbar 组合。字体为 `DejaVu Sans` 约 7–9 pt；palette 与 Figure 8 完全一致，提供跨图语义稳定性，marker 对灰度有辅助。
- **Caption**：
  > Figure 9: Addition task accuracy under co-training with varying training budgets (250, 500, 800 steps). Curves show different mixing weights. See (3.1).

  词数约 22；动作：`title`、`setup`、`encoding_key`、`comparison`、`appendix_pointer`。caption 给出 budgets 和 weight 角色，但 error bar 仍由前一段正文解释，`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：w=0 的 addition accuracy 接近 0，符合「只训练 multiplication」基线；w>0 的 addition 曲线在 250/500/800 steps 多数保持高值，较高长度和有限 budget 处出现下降；误差条表示 random-seed variability。图无样本分母、seed 数、区间或失败类别。
- **证据关系**：Figure 8 的 primary-task 曲线 → Figure 9 的 auxiliary-task capability → Appendix D.8 关于 shared computational structure 与有限训练预算的机制解释。两图共同支撑 task mixture 的 component-level interpretation。
- **优点**：与 Figure 8 共用 panel 结构、颜色和 weight legend，读者可直接对照主任务/辅助任务；`w=0` 的低基线清楚显示 auxiliary exposure。
- **缺陷**：重复 legend 和 error bars 在长序列处拥挤；caption 的 `See (3.1)` 对独立阅读帮助有限；没有把 sample mixture 的实际计数和每点评测分母写出。
- **可复用模式**：用成对主任务/辅助任务图保持完全一致的 palette 与 facet，使协同收益和任务本身的可学性同时可见。
- **证据定位**：p.25 中部，bbox 约 `[134, 414, 491, 536]`；依据 `rendered_observation`。

## Figure 10

- **页面与几何**：PDF p.26，`appendix`，`page_width`。单张嵌入 raster image 包含两个横向 panel：左为 Sequence Length vs Functions，右为 Pass Rate vs Functions。左 panel 有三系列 legend，右 panel 为单条红色曲线。
- **类型与用途**：`line`；`experimental_design`、`failure`、`qualitative_evidence`。
- **渲染、坐标与绘图语法**：PDF 对象是 RGB raster，原始嵌入尺寸 3569 × 1469 px，`pdfimages -list` 报告约 811 dpi；页面渲染中显示为横向高信息密度图。两个 panel x 均为 4–16 functions 的 linear 数值轴；左 y 为 sequence length（tokens，约 0–30000），右 y 为 pass rate（%）；网格 both；左 panel 3 series/legend，右 panel 1 series；左 marker 为 circle/square/triangle，右为 circle；solid lines；无 hatch/reference line/uncertainty，线宽按 raster 渲染估计约 2 pt。
- **数据编码**：x=`Number of Functions`；左 y=`Sequence Length (tokens)`，右 y=`Pass Rate (%)`；color=`Min blue #0000FF、Average green #008000、Max red #FF0000`；shape=`circle/square/triangle`；line=`solid`；facet=`length statistics / pass rate`；text=`panel titles、legend、axes`。
- **复杂度与颜色**：score 3；2 panels；左 3 series、右 1 series；3 个 legend 项；0 annotation；约 52 个 marker。图中主字体为 raster 内的 sans-serif，渲染估计约 8–16 pt，未在 PDF 文本对象中单独保留。主色来自嵌入图像像素：`#0000FF`、`#008000`、`#FF0000`；网格/背景有 `#E7E7E7`、`#D4D4D4`、`#FAFAFA`、`#FFFFFF`。marker 形状对颜色提供冗余，灰度下三系列仍能部分区分。
- **Caption**：
  > Figure 10: Pass rate and median sequence length for SWE-agent-LM-32B on the code fixing task.

  词数约 15；动作：`title`、`setup`、`comparison`。caption 指出模型、task 和两类统计，但左 legend 实际写的是 `Average Length`，图像和 caption 存在 median/average 术语不一致；`self-contained=false`、`main_finding_stated=false`。
- **数据与统计**：SWE-agent-LM-32B 在函数数 4–16 的 code-fixing codebase 上生成 trajectory。左 panel 的 min/average/max sequence length 随 functions 总体上升，max 约从 10k 增到 28–30k tokens；右 panel pass rate 从约 79.5% 降至约 61.5%，中间有局部反弹。图没有 trajectory 数、函数规模分母、seed 或误差条；Appendix E 正文只说明绘制 pass rate 与 generated trajectory length。
- **证据关系**：Section 3.3 的 codebase complexity 与 agent trajectory filtering → Appendix E 的 mini-SWE-agent prompt/workflow → Figure 10 的 agent-level length/pass-rate statistics → Figure 1 的 Mamba/Pythia finetuning 曲线。该对象承担失败模式和实验设置背景，不直接比较最终模型。
- **优点**：双 panel 把环境生成负担（长度）与任务结果（pass rate）并列；左侧三种长度统计和右侧 pass-rate 曲线都用函数数作为共同 x 轴。
- **缺陷**：caption 的 median 与 legend 的 Average 不一致；原图为 raster，页面缩放后小刻度和 legend 细字不如矢量图稳定；pass-rate 分母、trajectory 过滤比例和 uncertainty 缺失。
- **可复用模式**：用共享复杂度 x 轴配对「生成轨迹成本」与「成功率」panel，并在 caption 明确 statistic（mean/median）、评测分母和过滤规则。
- **证据定位**：p.26 上部，bbox 约 `[108, 64, 504, 148]`；依据 `rendered_observation`。

## 跨对象系统判断

- **视觉叙事**：Figure 1 先把三种 coding trajectory 与 length-generalization 结果绑定；Figure 2 把 pointer memory 的局部动作与 addition 曲线绑定；Table 1 将 synthetic task 结果压成统一外推语法；Figure 3 扩展到自然语言；Figure 4–10 依次展开任务构造、seed robustness、baseline、训练配置和 agent setup。主线围绕「有限内部状态 → 外部工具接口 → 轨迹学习 → 长度外推」推进。
- **Caption 系统**：正文 Figure 1/2 的 caption 相对完整，提供 setup、编码和结论；Figure 3 caption 过短。附录 Figure 6/7 的 caption 具有较多设置细节，Figure 8/9 依赖前置段落，Figure 10 的 median/average 术语需要修正。Table 1 自带 notation/threshold 定义，Table 2 复用却未重述。
- **表头系统**：两张表统一使用 `Model` 与 `n→m(p%)` 结果语法，横线分隔 SSM/RNN 与 Transformer；Table 2 缩减到 recursive Hanoi 单任务，缺少 algorithm-variant 层级。两表均为黑白 booktabs，粗体承担最佳结果提示。
- **方法—结果—消融链接**：Figure 2/4 是 method interface，Figure 1/3、Table 1、Figure 6 是主比较，Figure 5/7/8/9 是 robustness/ablation，Figure 10 是 agent setup/failure。正文对 Figure 1–3 和 Table 1 的调用直接；Figure 7–10 由 appendix headings/paragraphs 调用。Figure 6 caption 的 pointer/search tool 文案是跨对象最明显的接口不一致。
- **正文—附录链接**：正文 p.7–10 通过 Appendix C/D/E/F 指针把训练超参、tool algorithms、seed sensitivity、ablation、hybrid/RMT 和 coding prompt 后移；附录对象能恢复大部分细节，但 Table 1 best-seed 与 Figure 5 全 seed 之间的聚合边界需要读者主动对照。
- **字体与颜色一致性**：正文使用 Nimbus Roman/Computer Modern；图表使用 DejaVu Sans，轨迹和截图引入 Lucida Console/Aptos/系统字体，符合各自的 chart/code 角色。Figure 2/6 使用固定蓝—橙五模型 palette；Figure 7 使用 standard blue/orange/green；Figure 8/9 使用另一套蓝/橙/绿/红 palette，并在两图间一致。Figure 1/4 的 pastel diagram palette 与定量图 palette 局部独立。多数 quantitative plots 没有颜色以外的语义编码，Figure 2/6/7/8/9 通过 marker 补充区分。

## 最终判断

### 最可复用模式

1. 将 tool trajectory 的局部可执行状态（Figure 1、Figure 2）与共享 x 轴的长度外推曲线配对，读者可以沿「接口—行为—结果」顺序阅读。
2. 用统一 `n→m(p%)` notation 和 `p≥5%` 规则压缩跨任务外推结果，同时在 Table 1 caption 公开聚合阈值。
3. 用 Figure 5 的 seed-wise lines、Figure 7 的 error envelope、Figure 8/9 的 error bars 分别暴露初始化、训练配置和任务混合的不稳定性。
4. 用 Figure 4 的 abstract graph→code 双行结构把 synthetic task 的数据生成规则转成可执行表示。

### 最高价值对象

- Figure 2：同时承担 pointer-memory method interface 和 addition headline，最直接连接理论机制与可见行为。
- Table 1：以统一阈值把 arithmetic/reasoning 外推结果放在同一决策面，便于与 Figure 6 和 Appendix 的细节互证。
- Figure 1：将三种 coding trajectory source 与 Mamba/Pythia 的 system-level 差异绑定，连接 introduction、Section 3.3 和 Appendix E。
- Figure 5：把 Table 1 的 best-seed 汇总还原为 seed heterogeneity，揭示 Hanoi 结论的稳健性边界。

### 失败模式

- 关键实验的分母、seed 聚合与 uncertainty 不一致：Figure 1–3、Table 1 和 Table 2 主要给点结果，Figure 5/7/8/9 才显式展开 variability。
- Table 1 的 best-seed/最大长度摘要会遮蔽完整曲线；Figure 5 才显示 Hanoi 的初始化敏感性。
- Figure 6 caption 对 Logical Graph/Hanoi 的 pointer-based 与 search-based tool 描述前后不一致。
- Figure 7 的 Task 1/Task 2、Figure 8/9 的 weight/error-bar 细节依赖邻近正文，脱离正文后复现困难。
- Figure 10 的 caption 使用 median，左 legend 使用 Average；嵌入 raster 还降低了细刻度的可审计性。

**一句话视觉策略**：论文用「工具轨迹示意 → 统一长度外推比较 → 附录中的 seed/预算/任务构造展开」把外部状态如何解除 SSM 记忆瓶颈转成一条可扫描的视觉证据链，但应统一工具接口文案、统计聚合和 uncertainty 定义。

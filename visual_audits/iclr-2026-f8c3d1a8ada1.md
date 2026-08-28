# Visual audit — `iclr-2026-f8c3d1a8ada1`

## 范围、事实源与对象清单

- **论文**：*Rodrigues Network for Learning Robot Actions*（ICLR 2026；OpenReview forum `IZHk6BXBST`）。
- **PDF 事实源**：`/Users/zimingwang/Developer/GitHub/elite-ml-paper-anatomy-2026/corpus/pdfs/iclr-2026-f8c3d1a8ada1.pdf`。`pdfinfo` 报告 23 个物理页、Letter 612 × 792 pt；PDF 由 `pdfTeX-1.40.26` 生成。正文/参考文献/补充材料都在同一 PDF 中。
- **渲染与逐页检查**：23 页全部用 `pdftoppm -r 200 -png` 渲染为 1700 × 2200 px（实际约 199.9996 dpi），并检查 p.1–23 的正文、参考文献与附录；含对象页又逐页放大复核。`pdftotext -layout` 用于逐字核对 caption/header，`pdffonts` 用于字体对象核对，`pdfimages` 提取的 59 个 PNG 资产用于判断栅格/混合渲染。所有 Figure/Table 均按 PDF 中的实际物理页记录。
- **PDF 对象清单**：6 幅编号 Figure、12 张编号 Table，共 18 个对象；没有 Algorithm、未编号 Figure/Table 或跨页表。Figure 1–5 与 Table 1–3 在主文；Figure 6 与 Table 4–12 在补充材料的附录/消融部分。p.10–13 是参考文献，p.14–23 是 Supplementary Material。
- `readings/iclr-2026-f8c3d1a8ada1.json` 的 visual inventory 数量、标签和页码与 PDF 一致。reading 的 `page_map.layout` 将全 PDF 写作“双栏”；逐页 PDF 检查显示主文 p.1–13 为双栏，而 Supplementary p.14–23 实际切换为单个宽文本栏。下文以 PDF 的实际版式为准。

| PDF 页 | Figure | Table | 模块与职责 |
|---:|---|---|---|
| 1 | Figure 1 | — | 摘要/引言：classical Rodrigues operator → learnable operator → 应用范围 |
| 5 | Figure 2 | — | 方法接口：Rodrigues Block 的三层数据流 |
| 7 | Figure 3、Figure 4 | — | FK 拟合定量收敛与 qualitative link-error 对照 |
| 8 | Figure 5 | Table 1 | Cartesian motion 的轨迹、规模曲线与主数值比较 |
| 9 | — | Table 2、Table 3 | imitation success 与 FreiHAND hand reconstruction 主比较 |
| 16 | — | Table 4、Table 5 | FK/motion training hyperparameters |
| 17 | — | Table 6、Table 7 | imitation training 与各任务规模 |
| 18 | — | Table 8 | hand reconstruction training hyperparameters |
| 19–20 | — | Table 9、Table 10 | FK/motion approximate training time |
| 21 | — | Table 11 | 组件移除消融 |
| 22 | Figure 6 | Table 12 | baseline 参数规模与 Rodrigues hyperparameter sensitivity |

## 公开视觉源获取

自动 `reports/tables/visual_source_inventory.csv` 仍将该论文标为 `no_public_source_found`；`corpus/visual_sources/iclr-2026-f8c3d1a8ada1/` 不存在。随后按 PDF 首页、正文/参考文献、OpenReview/论文页面和 GitHub 进行只读核查：

- PDF 没有 GitHub/project URL，只在 Supplementary p.14 写明代码、数据集和 checkpoint 将在接收后发布；reading 给出的官方 PDF 和 OpenReview forum 也没有作者代码链接。OpenReview API 的直接请求返回 403，因此不把其作为视觉源证据。
- `gh search repos` 以完整标题和方法名命中 [mzhmxzh/RodriguesNetwork](https://github.com/mzhmxzh/RodriguesNetwork)。仓库描述为 `[ICLR 2026 Oral] Rodrigues Network for Learning Robot Actions`，README 自称 official repo，`main` 当前提交为 `d867464c146ac1e1449c36f67dc5718fa109a801`（`open source`）。标题、会议和方法名构成与本 PDF 的直接身份关联。
- 仓库树没有论文排版、静态结果图或表格生成文件：没有 `figure*`、`table*`、`plot*` 结果脚本、`.ipynb`、`.tex`、`.tikz`、`.pgf`、`.svg` 或导出的 PNG/PDF 图表。它提供的 `tests/plotly/` 脚本是可复用的机器人/轨迹可视化源，因此记作 **`partial_visual_source`**，而不是 exact source。
- 可复用的视觉相关文件为：`tests/plotly/FK/visualize_dataset.py` 和 `tests/plotly/FK/visualize_model.py`（Plotly，LEAP hand 的 FK/预测与 robot mesh overlay，分别使用 `lightblue`/`lightgreen`）；`tests/plotly/Motion/visualize_dataset.py`、`tests/plotly/Motion/visualize_saved_dataset.py`、`tests/plotly/Motion/visualize_model.py`（Plotly，按帧从 RGB `(173,216,230)` 插值到 `(144,238,144)`，可显示 16-frame trajectory、observed/predicted overlay，并隐藏 3D axes）；以及 `tests/plotly/visualize_robot_model.py`（Plotly robot mesh）。这些源能支持 Figure 4/5 的定性几何和轨迹语义，但不能逐字复现 PDF 的 Figure 1/2 diagram、Figure 3/6 统计图、表格、字体排版或误差编码。
- 未拉取权重、数据集、checkpoint 或完整仓库；JSON 只记录上述轻量源文件和树证据。公开源状态因此是“部分视觉源”：定性 robot/trajectory renderer 可查，所有正式图表的最终 PDF 仍是事实源。

## 全文视觉风格

- **版式与分栏**：主文 p.1–13 是 ICLR 双栏；Figure 1、2、3、4、5 和 Table 1–3 都跨两栏/页宽。补充 p.14–23 是实际单个宽文本栏；Table 4–10、11–12 和 Figure 6 均位于这一宽栏中，不能按 reading 所写的 appendix 双栏解释。
- **字体**：正文和 caption 以 Nimbus Roman No9 L/Times New Roman 类衬线字体为主，数学符号由 Computer Modern 与 Cambria Math 等嵌入字体承担；`pdffonts` 还显示少量 DejaVu Serif/粗体对象。图内统计标签约 6–10 pt，caption/表体约 8–9 pt，标题和 caption 粗体片段约 9–10 pt。图表文字能放大读取，但 Figure 4 的 colorbar 竖排标签和 Figure 5 的小 inset 是主要可读性瓶颈。
- **颜色**：结果图在 Figure 5/6 中复用模型类别：MLP 橙（约 `#F28E2B`）、GCN 红（约 `#E64B35`）、BoT 紫（约 `#7E63B8`）、Transformer 浅蓝（约 `#75AADB`）、Rodrigues 绿（约 `#238B45`）。Figure 3 的 bar panel 使用统一蓝色柱，右侧曲线用该类别色。Figure 4 使用从深蓝/青到黄的 sequential link-error 色阶（约 `#213B9A`、`#2C7FB8`、`#41B6C4`、`#A1D76A`、`#FDE725`）。Figure 1/2 以橙色 classical/Rodrigues 语义、绿色 learnable/feature 语义、紫色/蓝色模块块和灰黑箭头组成概念图调色板。类别主要靠颜色加 legend/位置/文字冗余编码，纯灰度下结果曲线仍可凭 legend 识别，但图中颜色并不完全灰度安全。
- **矢量/栅格**：正文文字、booktabs 表格、Figure 3/6 的坐标与曲线为 PDF vector；Figure 1/2 的结构框和文字混有 robot/hand 图标；Figure 4 的 robot render、Figure 5 的 robot render/小图是 embedded raster 与 vector 标注的混合物。未见整页栅格化。
- **一致性**：caption 均采用“`Figure/Table n:` + 粗体标题片段 + 设置/编码说明”的 LaTeX 语法，表格均为无竖线的 booktabs 风格。模型类别色在三组结果图中保持稳定，主比较→附录消融的阅读链清楚；不过 Figure 1/2 的插图风格、Figure 4 的 pastel error map 与统计图的 Matplotlib 颜色并非一个完全统一的品牌色系。

## 逐对象审计

### Figure 1 — Neural Rodrigues Operator 总览（p.1）

- **版式、类型与职责**：主文、页宽、摘要/引言起始处。三个横向区域为 `Classical Operator`、`Learnable Operator`、`Applications`；左侧展示 robot、Rodrigues’ Rotation Formula、fixed coefficients 与 joint state，中间展示 Neural Rodrigues Operator、message passing、learnable weights 与 joint features，右侧三个虚线应用框为 motion prediction、imitation learning、hand pose estimation。类型为 `conceptual_diagram`、`pipeline`；复杂度 4/5（多语义区、多个小图标和应用缩略图）；用途为 `headline`、`method_interface`、`theory_mechanism`、`experimental_design`。
- **绘图语法与编码**：没有 conventional x/y 轴、网格或 legend。x 方向是 classical → learnable → applications 的阶段顺序，y 方向在 operator 内分别堆叠公式/参数和 message/feature 语义。橙色强调 classical rotation/fixed coefficients，绿色强调 learnable/message passing，灰色/黑色箭头表达信息流，虚线框表达应用分支；direct labels=true，marker=0，约 2 种线型，reference line=0，uncertainty=none，线宽为约 1–1.5 pt 的渲染估计；rendering=mixed。
- **字体与颜色**：图内约 6–12 pt，衬线正文、Computer Modern/Cambria 数学、粗体标题和少量 italic/roman；颜色约 `#F28E2B`、`#63A86B`、`#5B9BD5`、`#A6A6A6`、`#F2F2F2`、`#000000`；颜色与位置、标签和箭头冗余编码，pastel 子类别的灰度区分较弱。
- **数据与统计**：概念接口图，说明固定 Rodrigues 系数如何变成可训练权重、关节角如何推广为抽象特征，以及三个应用域；无样本分母、效果量、重复、不确定性或坐标轴。
- **Caption（PDF 逐字提取，空格规范化；59 词）**：
  > Figure 1: We introduce the Neural Rodrigues Operator, a learnable extension of the classical Rodrigues’ Rotation Formula from robot control, where the original coefficients are replaced with trainable weights and joint angles are generalized to abstract features. Built upon this operator, the Rodrigues Network leverages the kinematic structure of articulated systems to advance a wide range of action-learning tasks.

  动作是 `title`、`setup`、`comparison`、`main_finding`；图内的 `Neural Rodrigues Operator` 和 `Rodrigues Network` 为粗体片段，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`（提出与应用范围被写出，但没有定量结果）。
- **证据关系**：引言的“MLP/Transformer 把动作当作无结构 token”问题 → Eqs. (3)–(8) 的 Rodrigues 重参数化与多通道 operator → Figure 1 的 classical/learnable 对照 → Figure 2 的可堆叠 block → Figures 3–5、Tables 1–3 的 synthetic/robot/hand 结果。该图承担 headline 和方法入口，不替代性能证据。
- **设计优点**：在一幅全宽图中把理论基元、可学习改造和三类应用接成一条叙事；左右 operator 面板具有近似同构结构，箭头、标题和颜色形成冗余线索；应用框让读者预先知道后续实验的覆盖范围。
- **设计缺点**：中间/右侧小字和缩略图在单页缩放下偏小；没有给出通道数、层数或输入输出张量形状，读者仍需回到公式；pastel 颜色在灰度打印时不稳定，应用框的图像内容也不是可量化证据。
- **可复用模式**：用“经典算子 → 可学习算子 → 应用族”的三段式全宽概念桥，配同构 operator 面板、直接标签和下游任务框；若用于复现，应在输出端补充维度、假设和可验证指标。
- **证据**：`p.1 Figure 1`；`rendered_observation`，PDF 字体对象由 `pdffonts` 交叉核对。

### Figure 2 — Rodrigues Block 架构接口（p.5）

- **版式、类型与职责**：主文、页宽。左侧是 robot/scene illustration，右侧从左到右为 `Rodrigues Layer`、`Joint Layer`、`Self-attention Layer` 三个方框；每层显示 `F`、`Θ`、可选 global token `G` 和箭头，标出 update link feature、update joint feature、exchange link feature。类型为 `architecture`、`pipeline`、`conceptual_diagram`；复杂度 4/5；用途为 `method_interface`、`theory_mechanism`。
- **绘图语法与编码**：无轴/网格/legend。x 是 layer 顺序和信息方向，y 是 link/joint/global feature lane；紫色 `F`、橙色 `Θ`、蓝色 `G`、绿色 Rodrigues 运算、黄色 Linear/Multi-Head Attention、黑色箭头编码数据流；direct_labels=true，marker=0，line_styles≈2（实线连接与框线），reference_lines=0，uncertainty=none，线宽约 1–1.5 pt，rendering=mixed。
- **字体与颜色**：图内约 6–11 pt，粗体层标题、regular/roman 衬线和数学符号；代表色约 `#7E63B8`、`#F2A900`、`#70AD47`、`#5B9BD5`、`#F2F2F2`、`#000000`。形状、标签和通道 lane 对颜色有冗余，灰度可恢复大部分顺序但不能稳定区分所有模块色。
- **数据与统计**：方法图而非性能图；显示 joint→link 的多通道 Rodrigues、link→joint 的 joint-specific linear、全 link/global token self-attention 的传递关系，不含样本分母、参数规模、重复或不确定性。
- **Caption（PDF 逐字提取；51 词）**：
  > Figure 2: Rodrigues Block. It comprises three components: a Rodrigues Layer for passing information from joints to links, constructed with our Multi-Channel Neural Rodrigues Operator; a Joint Layer for passing information from links to joints; and a Self-Attention Layer for global information exchange with all the links and the global token.

  动作是 `title`、`setup`、`encoding_key`；`Rodrigues Block` 为粗体标题片段，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Eqs. (9)–(11) 和 §4.1–§4.3 的 component definitions → Figure 2 的层级接口 → D.1–D.4 的任务特化配置 → Table 11 组件移除和 Table 12 超参敏感性。它是方法接口与后续消融的结构锚点。
- **设计优点**：三层顺序、输入/输出 lane 和 global token 同屏，能够解释局部 kinematic message 与全局 attention 如何串联；左侧场景图把抽象 block 绑定到 articulated robot。
- **设计缺点**：箭头密集且每个模块内部字小；没有显示 block 堆叠深度、channel 数或 cross-attention 的 hand 特化，读者仍需查附录；global token 在不同任务是否启用由正文隐含而非图例编码。
- **可复用模式**：以“局部结构传播 → 反向更新 → 全局交换”的固定三框接口组织结构化网络；在图旁明确 `C_J/C_L/B`、可选 token 和任务特化分支，可直接服务复现。
- **证据**：`p.5 Figure 2`；`rendered_observation`。

### Figure 3 — FK 拟合的误差与收敛（p.7）

- **版式、类型与职责**：主文、页宽双面板。左 panel 是五个 backbone 的 MSE bar chart（MLP、GCN、BoT、Transformer、Rodrigues），右 panel 是 MSE 随 10k–100k training iterations 的 log-line chart，含五条方法曲线和半透明波动带。类型为 `bar`、`line`；复杂度 3/5；用途为 `headline`、`main_comparison`。
- **绘图语法与编码**：左 x 为 categorical backbone、右 x 为 linear iteration（合并字段以 `unknown` 表示），y 两 panel 均为 log MSE；有 y 向浅色网格，右 panel legend 位于 upper-right，仅一个 legend 服务两 panel，direct labels=true（左柱顶数值与 panel titles），marker_types=0，line_styles=1，reference_lines=0，hatching=false，uncertainty_display=`multiple`（左侧小 error bar、右侧 band），线宽约 1 pt；rendering=vector，plot grammar provenance=`rendered_estimate`。
- **数据与统计**：左柱从 PDF 读取约为 MLP `6.32e−04`、GCN `5.07e−04`、BoT `5.37e−06`、Transformer `5.26e−06`、Rodrigues `2.82e−07`；右图显示 10k–100k 的 training MSE descent。Figure 3 没有报告 run 数、重复层级或 band/error-bar 的统计定义，故只能将其视作 test-set MSE comparison + training curve，不能从带宽推断标准误或置信区间。
- **Caption（PDF 逐字提取；24 词）**：
  > Figure 3: Fitting forward kinematics with different network backbones (MSE↓). The Rodrigues network achieves significantly lower error (left) with faster convergence during training (right).

  动作是 `title`、`setup`、`comparison`、`main_finding`；标题整句有粗体片段，`headline_bold=true`；`self_contained=true`；`main_finding_stated=true`。
- **证据关系**：§3 的 operator expressivity 主张 → §5.1 LEAP hand FK setup → Figure 3 的跨 backbone accuracy/convergence → Table 1/Figure 5 的 motion generalization → Table 11 对 Rodrigues/Joint/Self-attention 的组件机制核验。
- **设计优点**：同一 Figure 同时覆盖终点误差和训练动态，log y 让数量级差异可见；方法颜色、legend 和柱顶数值使 Rodrigues 的优势快速可定位；曲线 band 表达了视觉上的重复波动。
- **设计缺点**：左右 panel 的 x 语义不同却没有在 caption 中明确“左为 categorical、右为 iteration”；band/error bar 未定义重复单位；左柱全部用同一蓝色，方法对照仍需阅读 x 标签，且数值标注在缩放后较小。
- **可复用模式**：用“终点 bar + 收敛 line”成对回答表达能力和优化速度；将重复单位、误差定义和共同 y 量纲写入 caption，并对不同 x 语义使用明确 panel 标题。
- **证据**：`p.7 Figure 3`；`rendered_observation` + `pdf_object`。

### Figure 4 — FK 的 link-wise qualitative error（p.7）

- **版式、类型与职责**：主文、页宽横向 montage。六个并排面板为 MLP、GCN、BoT、Transformer、Rodrigues、Ground Truth；每个面板是同一 LEAP hand configuration 的 17-link robot render，右侧独立竖直 colorbar 标为 fitting error。类型为 `qualitative_grid`、`image_montage`；复杂度 4/5（6 个 render + per-link color encoding）；用途为 `main_comparison`、`qualitative_evidence`、`failure`。
- **绘图语法与编码**：无 x/y 轴、网格或 legend；x 是模型/ground-truth 顺序，y 是 17-link hand geometry；link 颜色是误差大小，颜色越深表示误差越大，Ground Truth 作为无误差参照，direct_labels=true，marker/line/hatch/reference/uncertainty 均为 0/none，rendering=mixed（嵌入 render + vector labels/colorbar）。
- **字体与颜色**：模型标签约 7–9 pt，caption 为衬线粗体标题+regular 正文；error colorbar 约由深蓝 `#213B9A`、青 `#2C7FB8`、青绿 `#41B6C4`、浅绿 `#A1D76A` 至黄 `#FDE725` 组成；sequential 色阶直接映射 link-wise MSE，位置和模型名提供部分冗余，灰度下误差等级不稳定。
- **数据与统计**：单个 example configuration 的 per-link predicted pose 与 GT 对照，不是全测试集聚合；正文指出 baseline 在 fingertips 处积累误差、Rodrigues 接近 GT，但图面没有颜色数值、样本分母、重复或不确定性。
- **Caption（PDF 逐字提取；26 词）**：
  > Figure 4: Visualization of forward kinematics prediction on an example configuration. Errors are plotted on each link with color scales, with darker colors indicating larger errors.

  动作是 `title`、`setup`、`encoding_key`；标题片段粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Figure 3 的全局 MSE → Figure 4 的 link/fingertip failure localization → 正文对 GCN artifacts 与 Rodrigues minimal error 的解释 → Table 1/Figure 5 的 motion evidence。该图承担 qualitative evidence 和 failure localization。
- **设计优点**：固定配置、统一视角和 Ground Truth 末列使 spatial error pattern 易于比较；颜色直接落在 link geometry 上，比单个 aggregate MSE 更能显示 fingertips 这一局部失败模式。
- **设计缺点**：单一 configuration 容易被误读为总体表现；竖直 colorbar 字小且没有清楚给出绝对数值范围，颜色依赖较强；六个 hand render 在页宽下较小，无法同时看清局部 link 和标签。
- **可复用模式**：在定量 aggregate 图之后，以固定样本的 model×geometry montage 做误差定位；应附带样本选择规则、colorbar 数值范围和跨样本统计，避免把例子当总体结论。
- **证据**：`p.7 Figure 4`；`rendered_observation`，`pdfimages` 显示主体 render 为栅格资产。

### Figure 5 — Cartesian motion trajectory 与规模曲线（p.8）

- **版式、类型与职责**：主文、页宽双面板复合图。左 panel 上层展示 Frames 0–7 observed 与 Frames 8–15 predicted 的 UR5 末端位置，下面五个小 inset 分别显示 MLP/GCN/BoT/Transformer/Rodrigues 的 trajectory 与 GT 虚线；右 panel 是 Test error vs trainset size 的 log-line chart（10³–10⁶）。类型为 `line`、`image_montage`、`qualitative_grid`；复杂度 4/5；用途为 `main_comparison`、`qualitative_evidence`、`robustness`。
- **绘图语法与编码**：复合图的 x 语义为左侧 frame index/轨迹时间、右侧 trainset size log（字段以 `log` 记录 quantitative panel），y 右侧为 log Test MSE；右 panel 有 x/y 浅色网格，legend 位于 upper-right，左侧 inset 用方法名直接标注而非共享 legend；direct_labels=true，marker_types=1，line_styles≈1（轨迹实线/GT 虚线），reference_lines≈5（每个模型 inset 的 GT 水平/轨迹参考），uncertainty=none，线宽约 1 pt；rendering=mixed。
- **数据与统计**：左侧是 8 帧观测、8 帧预测的 single example，红点为 end-effector、B-spline 连接各模型轨迹；右侧比较 `10^3`、`10^4`、`10^5`、`10^6` training pairs 的 test MSE。公开 Plotly 源的颜色梯度与三维轨迹语义可复用，但不包含该 PDF 的静态 five-inset 排版；图面无误差带、run count 或聚合定义。
- **Caption（PDF 逐字提取；9 词）**：
  > Figure 5: Results for motion prediction in Cartesian space.

  图内 subcaption `(a) Trajectory visualization. We visualize the trajectories of the end-point (marked in red) predicted by each model from the top-down view, interpolated with B-spline curves.` 与 `(b) Testset performance (MSE↓) under different amounts of training data.` 补充了 setup/encoding。caption 动作是 `title`、`setup`、`encoding_key`、`comparison`；标题片段粗体，`headline_bold=true`；合并 subcaption 后 `self_contained=true`；`main_finding_stated=false`。
- **证据关系**：§5.1 的 6-DoF UR5、16-frame Cartesian interpolation/IK → Figure 5a 的 observed/predicted trajectory → Table 1 的 10⁵ 主比较 → Figure 5b 的数据规模鲁棒性 → Appendix Tables 5/10 的训练与成本边界。
- **设计优点**：把定性轨迹、模型间局部曲线和 trainset scaling 放在同一对象，直接把“桥接 Cartesian/joint space”的机制主张连到结果；公开 Plotly source 还提供 observed/predicted geometric overlay 的复用起点。
- **设计缺点**：左侧五个 inset 很小，单图同时有 frame、trajectory、GT 和 model 语义，阅读顺序依赖 subcaption；右侧没有 uncertainty 或 sample count；不同模型颜色依赖 legend，灰度打印时易混淆。
- **可复用模式**：用上层时序/几何示例解释下层的 aggregate scaling curve；保留 observed→predicted 的时间分界，并把训练集规模、测试分母和重复单位写到图注。
- **证据**：`p.8 Figure 5`；`rendered_observation`；公开仓库 `tests/plotly/Motion/visualize_model.py` 和 `visualize_dataset.py` 为 `source_exact` 的相关轨迹 renderer，但不是 PDF figure layout。

### Figure 6 — baseline 参数规模消融（p.22）

- **版式、类型与职责**：附录 E.2、Supplementary 单宽栏、两个并排 vector line charts：`Train MSE vs model parameters` 与 `Test MSE vs model parameters`，x 为 1M/3M/10M/30M，五类方法曲线；绿色虚线标出 Rodrigues (3M) 的 1.93e−06 和 2.56e−06。类型为 `line`；复杂度 3/5；用途为 `robustness`、`main_comparison`、`efficiency_cost`。
- **绘图语法与编码**：x 为参数档位 categorical，y 为 log MSE；两个 panel 均有浅色 x/y 网格，legend 在 lower-left，每个 panel 都重复方法 legend（不是跨 panel 的单一共享 legend），direct_labels=true（绿色 reference 数值），marker_types=1，line_styles=2（solid method curves + dashed Rodrigues reference），reference_lines=2（每 panel 1 条），uncertainty=none，线宽约 1–1.2 pt；rendering=vector。
- **数据与统计**：比较四个 baseline 在约 1M/3M/10M/30M 的配置与固定 3M Rodrigues；正文解释 MLP/GCN 的 test error 在大模型上上升、BoT/Transformer 饱和，而 Rodrigues reference 始终较低。图面为 configuration-level train/test MSE point curves，无重复或不确定性。
- **Caption（PDF 逐字提取；17 词）**：
  > Figure 6: Comparing our method to different baseline configurations in motion prediction with trainset size = 10^5.

  动作是 `title`、`setup`、`comparison`；标题片段粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：主文 3M parameter fairness claim → Figure 6 的 baseline capacity/tuning alternative → Table 12 的 Rodrigues channel/depth sensitivity → Table 10 的 motion runtime。该图承担 robustness 与 efficiency-context，验证主结果不是单一 capacity 点。
- **设计优点**：同一 x 档位并列 train/test panel，过拟合与饱和形状一眼可见；固定绿色 reference 将 3M Rodrigues 与多种 baseline capacity 放进同一视觉坐标。
- **设计缺点**：图例在两 panel 重复，占用可视空间；x 标签是离散档位而非显式参数连续尺度，caption 未说明各 baseline 的每个配置如何调参；reference 线没有误差范围，不能判断近邻差异的重复稳定性。
- **可复用模式**：用 train/test 成对 scaling plot 检验容量替代解释；将固定方法 reference、调参规则和每档参数实际值写入 caption/附表，避免把视觉优越性归因于未披露配置。
- **证据**：`p.22 Figure 6`；`rendered_observation`。

### Table 1 — Cartesian motion 主比较（p.8）

- **版式、表头与职责**：主文页宽，6 列、5 个数据行、单层表头：Backbone、ErrorT (mm)、ErrorR (°)、Errorθ (°)、MSE (1e−6)、Train MSE (1e−6)。行是 MLP、GCN、BoT、Transformer、Rodrigues；用途为 `headline`、`main_comparison`。booktabs 风格、无竖线；Rodrigues 行粗体，其他单元格不着色。
- **统计与精度**：训练集为 `10^5` motion trajectories；ErrorT/ ErrorR/ Errorθ 是测试集几何误差，MSE 与 Train MSE 分别是测试/训练 MSE，全部 lower-is-better。数值通常保留两位小数，并以 `mean ±` 形式呈现。Rodrigues 为 1.21 ±0.17 mm、0.16 ±0.04°、0.06 ±0.00°、2.56 ±0.39 ×10⁻⁶、1.93 ±0.34 ×10⁻⁶；最强 baseline 的 test MSE 是 Transformer 12.86 ±1.25 ×10⁻⁶。PDF 和正文没有定义这些 ± 的重复单位；没有 seed、区间或显著性列。
- **Caption/header（12 词）**：
  > Table 1: Motion prediction in Cartesian space with trainset size = 10^5.

  `title`、`setup`；标题片段粗体，`headline_bold=true`；header 单层、指标方向/单位写在 header 中但 repeat/aggregation 未写；`self_contained=false`（Error 指标定义在 Appendix C.2）。`main_finding_stated=false`。
- **证据关系**：Figure 5 的 trajectory/scaling → Table 1 的固定 10⁵ 主比较 → Appendix C.2 的 metric definition、Table 5 training setup 与 Table 10 runtime → Figure 6/Table 11 的 robustness/ablation。
- **设计优点**：几何误差、测试误差、训练误差放在同一决策面，且模型参数量在正文说明为约 3M；粗体 Rodrigues 行和统一精度便于扫描。
- **设计缺点**：± 没有统计定义，训练/测试列的分母和 checkpoint 规则需要查附录；ErrorT/R/θ 缩写虽然有单位但没有在表内展开；单页宽横向密集。
- **可复用模式**：主比较表可保留“任务几何误差 + test/train loss”并列，但应在 header/caption 写清 aggregation、重复单位、checkpoint 和 lower-is-better 方向。
- **证据**：`p.8 Table 1`；`rendered_observation` + `pdf_object`。

### Table 2 — ManiSkill imitation success（p.9）

- **版式、表头与职责**：主文页宽，7 列、3 个数据行、单层表头：Method、PushCube、PickCube、StackCube、PegInsertionSide、PlugCharger、Average。用途为 `headline`、`main_comparison`；booktabs 无竖线，最佳单元格粗体：Transformer-DP、UNet-DP、Rodrigues-DP 三行。
- **统计与精度**：simulated success rate，五个 ManiSkill task；正文说明每任务 100 evaluation rollouts，5 random seeds，任务单元格报告 mean ± standard deviation，Average 列只给均值。Rodrigues-DP 平均 0.61，UNet-DP 0.58，Transformer-DP 0.44；PlugCharger Rodrigues 0.10 低于 UNet 0.13，PushCube 近饱和 1.00。小数统一两位；没有 seed-level values、失败类型或 task 分母列。
- **Caption/header（12 词）**：
  > Table 2: Baseline comparisons on the imitation learning benchmark. Simulated success rate.

  `title`、`setup`、`comparison`；caption 标题粗体，`headline_bold=true`；header 给出 task 分组但没有显式百分比/rollout/seed 信息；`self_contained=false`；`main_finding_stated=false`。
- **证据关系**：固定 Diffusion Policy outer framework 与 17M 参数公平比较 → Table 2 的五任务结果 → 正文 task-dependent benefits/failure 解释 → Appendix Table 7 的 demo/iteration 与 Table 6 training hyperparameters。该表承担 headline 但也揭示 PlugCharger 的任务异质性。
- **设计优点**：任务列横向对齐，平均值压缩为一个快速入口；粗体最佳值能迅速看到 PickCube/StackCube 等收益，同时表格保持黑白可打印。
- **设计缺点**：Average 没有 ±，读者不能判断跨任务平均的不确定性；任务名长且缺少 rollout/seed header；PushCube 饱和与接触动力学失败需依赖正文，表本身没有 failure/cost 列。
- **可复用模式**：采用 task×backbone 主表并保留 overall mean，但在表头写 `mean ± SD, 5 seeds, n=100 rollouts`，并单独标注接触/传感器缺口，避免把 average 当成普遍收益。
- **证据**：`p.9 Table 2`；`rendered_observation`。

### Table 3 — FreiHAND hand reconstruction 主比较（p.9）

- **版式、表头与职责**：主文页宽，5 列、11 个数据行、单层表头：Method、PA-MPJPE↓、PA-MPVPE↓、F@5↑、F@15↑。用途为 `headline`、`main_comparison`；booktabs/部分横线将早期基线、HaMeR 两行和 Ours 分组，Ours 行及其最佳指标粗体。
- **统计与精度**：FreiHAND standard protocol；PA-MPVPE 与 PA-MPJPE 单位为 mm，F@5/F@15 为 mesh/joint accuracy 指标，箭头直接给出方向。前两列一位小数，后两列三位小数，故列间精度为 mixed；没有均值/不确定性、样本分母或重复。Ours 为 5.9、5.6、0.793、0.991；HaMeR published 为 6.0/5.7/0.785/0.990，HaMeR (Reproduced) 为 6.2/5.9/0.774/0.989。MobRecon 的 PA-MPJPE 5.7 低于 Ours，故“state-of-the-art”必须限定为多数指标/整体表面，而不是所有单项。
- **Caption/header（30 词）**：
  > Table 3: Baseline comparisons on the FreiHAND dataset. We use the standard protocol and report metrics on 3D joint and 3D mesh accuracy. PA-MPVPE and PA-MPJPE numbers are in mm.

  `title`、`setup`、`encoding_key`、`abbreviation_definition`；caption 标题粗体，`headline_bold=true`；`self_contained=false`（standard protocol 与指标细节在正文/HaMeR 中）；`main_finding_stated=false`。
- **证据关系**：Figure 1 hand pose application → §5.3 HaMeR replacement claim → Table 3 的 published/reproduced baseline 对照 → Appendix A/C.4/D.4 的 MANO、数据集、训练细节与 parameter count。它把“超越机器人”落到 hand quantitative evidence，但不提供视觉 qualitative sample。
- **设计优点**：把 published 与 reproduced HaMeR 并列，减少单一复现基线误读；箭头和单位明确，横线区分参考组与 Ours，F 指标的小数精度稳定。
- **设计缺点**：没有 parameter-count、数据集混合或 uncertainty 列；“previous state-of-the-art”容易被单列 MobRecon 5.7 PA-MPJPE 反驳；引用嵌入 Method 单元格后横向扫描变慢。
- **可复用模式**：保留 published/reproduced 两类强基线和指标方向箭头；当方法只在部分指标占优时，caption 直接限定 claim，并将参数/训练协议作为 companion row 或附表。
- **证据**：`p.9 Table 3`；`rendered_observation` + `pdf_object`。

### Table 4 — FK fitting training hyperparameters（p.16）

- **版式、表头与职责**：Supplementary C.1 的单宽栏，6 列的三组 `Parameter name / Value` pair，2 行数据；用途为 `reproduction`。booktabs（顶部/底部和 header rule）、无竖线、无 cell highlight。
- **数据与精度**：训练 iterations 100,000；Optimizer Adam；learning rate 0.0003；Batch size 1024；Validate every 500 iterations；Weight decay 0。混合整数/字符串/小数，`decimal_precision=null`；没有不确定性。
- **Caption/header（9 词）**：
  > Table 4: Training hyperparameters for forward kinematics fitting experiment.

  `title`、`setup`；标题粗体，`headline_bold=true`；header 单层但重复 pair label，`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Figure 3 FK 收敛 → Table 4 的 optimizer/schedule → Appendix C.1 数据采样和 D.1 baseline architecture → Table 9 runtime。它只承担 reproduction，不是结果比较。
- **设计优点**：三组 key-value 并排节省附录空间，核心训练开关完整；无竖线的 booktabs 仍能通过 pair 对齐。
- **设计缺点**：第三组 header 在 PDF 中显示为单数 `Parameter`，重复表头需要读者自行分组；learning rate/weight decay 没有科学计数法统一格式，也没有 hardware/seed。
- **可复用模式**：对小型超参集合使用成对 key-value 宽表；应同时给出随机性、硬件和 checkpoint selection，保证“可复现”不只等于 optimizer 列。
- **证据**：`p.16 Table 4`；`rendered_observation`。

### Table 5 — Cartesian motion training hyperparameters（p.16）

- **版式、表头与职责**：Supplementary C.2 单宽栏，6 列三组 pair，3 行数据；用途为 `reproduction`、`experimental_design`。booktabs、无竖线/颜色。
- **数据与精度**：Training iterations 100,000；Optimizer Adam；learning rate 0.0001；Batch size 1024；Validate every 500 iterations；Weight decay 0；Input frames 8；Output frames 8；DoFs 6。数值类型混合，`decimal_precision=null`，无 uncertainty。
- **Caption/header（11 词）**：
  > Table 5: Training hyperparameters for motion prediction in Cartesian space experiment.

  `title`、`setup`；标题粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Figure 5 的 observed/predicted 8+8 frames → Table 5 的 schedule/DoFs → Appendix C.2 的 6-DoF UR5 pose interpolation、validation/test split 与 metric definitions → Table 10 runtime。
- **设计优点**：Input/Output frames、DoFs 与训练参数同表，能复现 Figure 5 的时序设定；成对排版紧凑。
- **设计缺点**：训练集规模 `10^3–10^6`、validation/test 10⁴ 和固定 checkpoint 规则不在表内；`Parameter name` 重复 header 使横向关系稍弱。
- **可复用模式**：把模型输入输出时间窗与优化器同屏，但把 dataset size、split 和 evaluation checkpoint 也列为独立 pair。
- **证据**：`p.16 Table 5`；`rendered_observation`。

### Table 6 — imitation training hyperparameters（p.17）

- **版式、表头与职责**：Supplementary C.3 单宽栏，6 列三组 pair，2 行；用途为 `reproduction`、`experimental_design`。booktabs，无竖线/颜色。
- **数据与精度**：Optimizer AdamW；learning rate 0.0001；Weight decay 1e−6；LR scheduler Cosine scheduler；Batch size 1024；Episode steps 200。整数、小数和字符串混排，`decimal_precision=null`；无 uncertainty。
- **Caption/header（14 词）**：
  > Table 6: Training hyperparameters for imitation learning experiment (following Chi et al. (2023)’s settings).

  `title`、`setup`、`comparison`；标题粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Table 2 五任务 success → Table 6 的 DP optimizer/scheduler/batch → Table 7 task-specific iteration/demo → Appendix D.3 的 17M backbone implementation。它把公平比较的外层训练条件变成可复现接口。
- **设计优点**：直接标示 following Chi et al. settings，能把改动限定在 denoising backbone；weight decay、scheduler、episode steps 都可定位。
- **设计缺点**：EMA、warm-up 500 steps 和 decay 0.75 只在正文段落，不在表内；没有 random seed 和 rollout count，读者无法仅凭表重建统计协议。
- **可复用模式**：在 baseline replacement 实验中将固定 outer framework 的所有训练开关集中，并把外部 protocol 与本论文改动分列。
- **证据**：`p.17 Table 6`；`rendered_observation`。

### Table 7 — task-level demonstrations 与 iterations（p.17）

- **版式、表头与职责**：Supplementary C.3 单宽栏，6 列、2 行：Task name + 五个 ManiSkill tasks；数据行 Demo trajectories、Training iterations。用途为 `dataset`、`experimental_design`、`reproduction`。booktabs，无竖线/高亮。
- **数据与精度**：PushCube/PickCube/StackCube/PegInsertionSide/PlugCharger demos 为 100/100/100/500/500；iterations 为 30k/30k/60k/100k/300k；整数/`k` 混排，`decimal_precision=null`，无 uncertainty。
- **Caption/header（14 词）**：
  > Table 7: Demo trajectories and training iterations for each task in imitation learning experiment.

  `title`、`setup`；标题粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Table 2 task success → Table 7 demo budget/iteration budget → Table 6 optimizer 与正文 100 rollout/5 seed 协议。它是 task heterogeneity 与 reproduction 的支撑表。
- **设计优点**：五任务横向一览，demo/compute budget 对齐，读者能看出 PlugCharger/PegInsertionSide 的训练预算差异。
- **设计缺点**：没有每条 trajectory 的 episode steps（正文才写 200）、scene randomization 或 evaluation rollout 列；`k` 与绝对数混用，对精确预算不如统一整数直观。
- **可复用模式**：任务作为列、数据/训练预算作为行适合小型 benchmark；增加成功 rollout、传感器和 episode length 行可闭合因果比较。
- **证据**：`p.17 Table 7`；`rendered_observation`。

### Table 8 — hand reconstruction training hyperparameters（p.18）

- **版式、表头与职责**：Supplementary C.4 单宽栏，6 列三组 pair，2 行；用途为 `reproduction`。booktabs，无竖线/颜色。
- **数据与精度**：Training iterations 1,000,000；Optimizer AdamW；learning rate 1e−5；Batch size 64；Validate every 1,000 iterations；Weight decay 1e−4。混合类型，`decimal_precision=null`，无 uncertainty。
- **Caption/header（9 词）**：
  > Table 8: Training hyperparameters for 3D hand reconstruction experiment.

  `title`、`setup`；标题粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Table 3 FreiHAND metrics → C.4 的十数据集/256×256/58 MANO 设定与 D.4 的 ViT+RodriNet → Table 8 training budget。该表承担 hand reproduction。
- **设计优点**：把极长训练预算、validation interval 和 optimizer 在一个紧凑表中固定下来；与其它超参表样式一致。
- **设计缺点**：训练约 7 天、GPU、EMA/augmentation 等成本或实现细节不在表内；表内没有 256×256、58 MANO outputs 等输入输出信息。
- **可复用模式**：将步数、validation、weight decay 和 batch 同屏；对视觉任务另加 resolution、label protocol 和 hardware pair。
- **证据**：`p.18 Table 8`；`rendered_observation`。

### Table 9 — FK training time（p.19）

- **版式、表头与职责**：Supplementary D.1 单宽栏，6 列（Method + MLP/GCN/Transformer/BoT/Rodrigues (ours)），1 个 `Time` 数据行；用途为 `efficiency_cost`、`reproduction`。booktabs，无竖线/高亮。
- **数据与精度**：单张 Quadro RTX 6000、100,000 training iterations 的 approximate wall-clock：MLP 17min、GCN 1h 50min、Transformer 2h 20min、BoT 2h 20min、Rodrigues 1h 18min。字符串时间粒度不统一（分钟/小时），`decimal_precision=null`；无重复或 uncertainty。
- **Caption/header（12 词，PDF 无句末句号）**：
  > Table 9: Approximate training time of different methods for fitting forward kinematics

  `title`、`setup`、`comparison`；标题粗体，`headline_bold=true`；`self_contained=false`（GPU 与 100k context 在正文）；`main_finding_stated=false`。
- **证据关系**：D.1 parameter count/FK architecture → Table 9 cost → Figure 3 convergence and Table 4 schedule。它把“Rodrigues 表达能力”与训练时间边界接起来。
- **设计优点**：不同 backbone 成本集中在同一行，Rodrigues 与 Transformer/BoT 的 trade-off 可快速读出。
- **设计缺点**：approximate time 没有硬件利用率、seed、warm-up 或重复；时间字符串不统一，且缺少参数量列，不能仅凭本表判断效率。
- **可复用模式**：成本表应同时给 wall-clock、hardware、iteration budget、parameter count 和重复范围，并统一时间单位。
- **证据**：`p.19 Table 9`；`rendered_observation`。

### Table 10 — motion training time（p.20）

- **版式、表头与职责**：Supplementary D.2 单宽栏，6 列同 Table 9，1 个 `Time` 行；用途为 `efficiency_cost`、`reproduction`。booktabs，无竖线/高亮。
- **数据与精度**：同为单张 Quadro RTX 6000、100,000 iterations；MLP 27min、GCN 1h 12min、Transformer 1h 20min、BoT 1h 20min、Rodrigues 2h 22min。approximate string time，`decimal_precision=null`；无 uncertainty。
- **Caption/header（12 词，PDF 无句末句号）**：
  > Table 10: Approximate training time of different methods for motion prediction experiment

  `title`、`setup`、`comparison`；标题粗体，`headline_bold=true`；`self_contained=false`；`main_finding_stated=false`。
- **证据关系**：Figure 5/Table 1 的 motion quality → Table 10 的 runtime cost → Appendix F CUDA acceleration（PyTorch >100h vs CUDA ≈15h 的大配置）。它明确 Rodrigues 在 motion toy task 上质量—时间 trade-off。
- **设计优点**：与 Table 9 同结构，能跨 FK/motion 复用表头；motion 的 2h22 cost 没有被 headline accuracy 隐藏。
- **设计缺点**：无速度单位统一、参数规模/吞吐/显存和 run-to-run variation；单行结构无法解释为什么完整 Rodrigues motion 比简单 MLP 慢。
- **可复用模式**：成对报告相同 hardware/iteration 的 task runtime，并在旁边给 parameter count、batch、吞吐和加速实现状态。
- **证据**：`p.20 Table 10`；`rendered_observation`。

### Table 11 — component-removal ablation（p.21）

- **版式、表头与职责**：Supplementary E.1 单宽栏，6 列：R Layer、J Layer、S Layer、Params (M)、Train MSE (1e−6)、Test MSE (1e−6)；4 个配置行，checkmark 表示保留组件，空白表示移除。用途为 `ablation`、`mechanism`、`main_comparison`；booktabs 顶/底规则，无竖线；默认行和最优/关键数值粗体。
- **统计与精度**：Default `3.04 / 1.93 ±0.34 / 2.56 ±0.39`；remove S `1.44 / 1.94 ±0.26 / 2.33 ±0.26`；remove J `3.01 / 2.33 ±0.56 / 2.80 ±0.62`；remove R `1.69 / 5.57 ±0.55 / 6.19 ±0.57`，MSE 单位为 ×10⁻⁶。Params/MSE 多为两位小数；MSE 的 ± 重复单位未定义，没有 seed/区间或显著性。
- **Caption/header（44 词）**：
  > Table 11: Ablation studies for motion prediction in Cartesian space with trainset size = 10^5. We remove the Rodrigues Layer (R Layer), Joint Layer (J Layer), or Self-attention Layer (S Layer) respectively from the original Rodrigues Network, and evaluate the MSE on train/test sets.

  `title`、`setup`、`encoding_key`、`comparison`、`abbreviation_definition`；标题粗体，`headline_bold=true`；`self_contained=true`；`main_finding_stated=false`。
- **证据关系**：Figure 2 三组件接口 → Table 11 的逐一移除 → E.1 对 R/J/S 作用与 parameter share 的解释 → Figure 6/Table 12 的 capacity/sensitivity controls。它是机制消融的主要闭环。
- **设计优点**：checkmark/blank 将结构干预显式化，Params 与 train/test MSE 并列，能同时观察 capacity 和性能；正文结论可直接回指每一行。
- **设计缺点**：没有无组件/多组件交互、随机种子和测试分母；remove-S test 略低于 default，却仍保留 default 的理由需读正文；空白 cell 在低质量输出中可能与缺失值混淆。
- **可复用模式**：用 component indicator matrix + capacity + train/test metrics 组成最小机制消融；明确“空白=removed”、重复单位和保留默认的决策规则。
- **证据**：`p.21 Table 11`；`rendered_observation`。

### Table 12 — Rodrigues hyperparameter sensitivity（p.22）

- **版式、表头与职责**：Supplementary E.3 单宽栏，7 列：Variation、C_J、C_L、B、Params (M)、Train MSE (1e−6)、Test MSE (1e−6)；7 个数据行，Default、Joint channels (2/8)、Link channels (4/16)、Num blocks (6/24)。用途为 `ablation`、`robustness`、`efficiency_cost`；booktabs/partial group rules，无竖线/颜色。
- **统计与精度**：Default 4/8/12 → 3.04、1.93、2.56；C_J=2/8 → 2.43/4.26 参数、2.18/1.32 train、3.00/1.96 test；C_L=4/16 → 1.19/8.73、3.64/1.51、4.35/2.18；B=6/24 → 1.55/6.03、2.24/3.47、2.76/4.15。数值主要两位小数，无 ±/重复/uncertainty；变体组用横线分隔但没有 group header。
- **Caption/header（20 词）**：
  > Table 12: Hyperparameter sensitivity analysis for the Rodrigues Network on motion prediction in Cartesian space with trainset size = 10^5.

  `title`、`setup`、`comparison`；标题粗体，`headline_bold=true`；header 单层且用数学下标 `C_J/C_L`，`self_contained=false`（Default/variant 解释在 E.3）；`main_finding_stated=false`。
- **证据关系**：Figure 6 的 baseline capacity scaling → Table 12 的 Rodrigues 内部 channel/depth variation → E.3 对 C_J/C_L 增大与 B=24 退化的解释 → Table 11 的 component removal。它承担 robustness/tuning boundary。
- **设计优点**：把三种超参轴、参数量和 train/test MSE 放在一个窄表中；组间横线让 joint/link/block 变化可分辨，默认配置作为锚点。
- **设计缺点**：空白 cell 没有显式写“unchanged”，单层 header 缺少变体分组标签；只有点估计，无法判断“reasonable range”的重复稳定性；正文“up to 4×”与实际每个方向的变化仍需读者计算。
- **可复用模式**：以 Default + 单因素 halving/doubling rows 做敏感性矩阵，并把 unchanged/variation group 显式编码；同时报告 seed/uncertainty 和优化失败条件。
- **证据**：`p.22 Table 12`；`rendered_observation`。

## 跨对象证据系统

- **视觉叙事**：Figure 1 先把 classical formula 变成 learnable operator，Figure 2 固定 Rodrigues/Joint/Self-attention 的接口；Figure 3–5 依次覆盖 FK expressivity、link-wise error、Cartesian motion quality/scaling；Tables 1–3 将 motion、imitation、hand 三类 headline 结果集中；Tables 4–10 把训练条件和 runtime 下沉到附录；Figure 6、Tables 11–12 回应 baseline capacity、组件必要性和超参敏感性。因此叙事链是“结构 prior → 方法接口 → synthetic/realized results → cost/robustness boundaries”。
- **Caption 系统**：所有 caption 以 Figure/Table label 加粗标题片段开头，随后给 setup、比较对象或编码；Figure 3/4 的 title 直接写主要 visual claim，Figure 5 依赖 subcaption 补充 encoding。主要缺口是 ±/band 的重复单位、sample denominator 和部分缩写/指标定义经常留在正文或附录。
- **表头系统**：结果表采用单层表头，指标方向和单位写在 Error/MSE/F@ columns；超参/成本表复用 6-column key-value 或 Method×backbone 横向结构。主表 header 没有统一的 seed、n、parameter count 或 cost 列；附录表把训练设定拆开提供了 reproduction 支撑，但跨表链接依赖正文。
- **方法—结果—消融链接**：Figure 2 的三组件在 Figure 3/5 的方法 backbone 中实例化；Table 1 是 Cartesian main result；Table 11 逐项移除验证 R/J/S，Table 12 改变 C_J/C_L/B，Figure 6 改变 baseline 参数规模。这个闭环能支持“Rodrigues Layer 是关键结构”这一机制解释，但 remove-S test 略降和 runtime 较高是重要边界。
- **主文—附录链接**：正文 §5.1–§5.3 显式指向 C.1/C.2/C.3/A/D.1–D.4；Table 4–10 提供主结果的训练、任务预算、runtime 和 hand protocol；E.1–E.3 的 Table 11/12 与 Figure 6 是主文 3M comparison 的稳健性补充；F p.23 说明 CUDA 大配置加速。PDF 实际单栏 appendix 使这些表更宽、更易读，但 reading 的“双栏”描述不准确。
- **字体一致性**：caption/table 的衬线和数学字体稳定，图内统计标签偏 sans/DejaVu/Times 混合；小字号与 Figure 5 inset 是共同可读性瓶颈。
- **颜色一致性**：MLP/GCN/BoT/Transformer/Rodrigues 的类别色在 Figure 5/6 和 Figure 3 右 panel 可追踪，Figure 4 的 sequential error map 另有独立语义；Figure 1/2 颜色更多服务模块角色而非模型类别。颜色有文字、位置和线型冗余，但未提供 hatching/marker 级灰度保障。

## 最终判断

- **最可复用模式**：
  1. 以全宽 Figure 1 的“classical → learnable → applications”概念桥和 Figure 2 的三层 block 接口先固定机制语言，再用 Figure 3 的 bar+convergence pair、Figure 5 的 trajectory+scaling pair 填入结果。
  2. 结果图跨对象固定 MLP/GCN/BoT/Transformer/Rodrigues 色义，并让方法名、位置、legend、实/虚线共同承担类别编码。
  3. 用 Table 11 的组件 indicator + 参数量 + train/test metrics 连接结构消融，用 Figure 6/Table 12 处理 baseline capacity 与内部 hyperparameter 的替代解释。
  4. 将训练超参、任务预算和 runtime 拆到统一的附录 key-value/cost 表，为主表提供可复现和成本边界。
- **最高价值对象**：Figure 2（方法接口）；Figure 3（终点误差与训练动态）；Table 1（Cartesian 主决策面）；Table 2（五任务异质性）；Table 11（机制消融）；Figure 6（capacity/tuning robustness）。Figure 4 的 link-wise montage 对解释 fingertips failure 特别有价值，但它只是一例。
- **失败模式**：
  1. 结果表/曲线中的 `±`、半透明 band 和 success average 没有统一的重复单位、样本分母或 aggregation definition。
  2. Figure 4 的单例 qualitative evidence 与 Table 3 的“state-of-the-art”措辞容易超出逐指标证据边界（MobRecon 的 PA-MPJPE 更低）。
  3. Figure 5 inset、Figure 4 colorbar、Table 3 引用嵌入和超参表重复 header 在缩放后增加阅读成本；颜色对灰度打印的冗余仍不足。
  4. Tables 9–10 只给 approximate wall-clock，缺少 parameter/throughput/显存和重复；Figure 6 的 reference line 也没有不确定性。
  5. 公共仓库有 Plotly robot/trajectory renderer，但没有 PDF 静态 figure/table source；复现完整排版和 Figure 1/2/3/6 数值仍需从 PDF 重建。
- **一句话视觉策略**：用 kinematics-aware operator 的概念桥和三层 architecture 固定方法接口，再用跨任务主表、终点/收敛成对图、定性 link error、容量/组件消融和附录成本表形成“机制—性能—边界—复现”的闭环。

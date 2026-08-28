# 视觉审计：icml-2026-b8bfc5f3f2ec

## 审计范围与事实源

本轮只处理这一篇论文。PDF 是 Figure/Table 清单、页码、caption、表头和视觉事实源；已完整读取物理页 1–26，包含正文、p.10 的 Impact Statement/Acknowledgment/References 混合页、References p.10–12、Appendix A–H p.13–26。
页面按至少 200 dpi 渲染到 `/tmp/icml-b8-pages-200.VOAvTs/page-01.png` 至 `page-26.png`，并结合 PDF 内嵌对象检查；`pdfimages -list` 显示 Figure raster 对象有效分辨率均高于约 180 dpi。PDF 清单为 18 Figures 与 9 Tables，修正了自动草稿曾记录的 15 Figures 与 6 Tables。

## 源核查

论文正文 p.2 明确链接作者仓库 `jeakwon/ai-engram`；GitHub README 的论文标题与 arXiv 2606.14997 对齐。已用认证 gh 查看 main 分支递归树和 README；树在提交 `e9efaf39544bf0df322cea566d9f2b902f33b19c` 下包含六个 paper-named figure notebooks。三个 notebook 被本地 compact source 保留，另外三个因文件较大只以 GitHub 树为证。

本审计将 source acquisition 定为 `partial_visual_source`。公开 notebook 覆盖 CIFAR-10、MNIST、CIFAR-100、ImageNet-1k 和 CelebA 的部分图形族；没有找到 paper TeX、table generator、CKA/W-Norm/概念图的精确绘图源。`fig_llm_tofu.ipynb` 生成的 Overall–EM 诊断散点不是 PDF 对象，因此不冒充 Figure 9 的精确源。

## 对象清单核对

正文对象为 Figure 1–9 与 Table 1–4；附录对象为 Figure 10–18 与 Table 5–9。p.10–12 References 无对象；p.13–26 的附录对象均已逐页检查。所有对象的设计、plot grammar、caption/header、数据统计和 evidence relation 均在下列记录中填写。

## Figures

### Figure 1  p.1  introduction

版式与类型  single_column；conceptual_diagram, pipeline；purpose 为 headline, method_interface, experimental_design；complexity 4/5，1 panel，series None，legend 0，annotations 14，marks 24。
设计与视觉编码  概念图没有样本、单位、聚合、分母或不确定性；它把目标/参考输入、内部状态以及注入/切除操作并置。 target/reference、null/learned state 与四种 criteria 的角色 输入图片、神经元、参数矩阵与分层权重块
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 2；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 1. Illustration of neuroscience criteria for AI engram. The engram μ_c^+ of target concept c is identified as the causal substrate satisfying: i) Specificity: selective encoding of target experience X_c^+ relative to reference X_c^-; ii) Reactivation: consistent reproduction of learned internal representations Z_c^+; iii) Sufficiency: memory induction via injection of μ_c^+ into the null state μ_null; iv) Necessity: memory elimination via surgical ablation of μ_c^+ from the learned state μ_all.` Caption words 71；moves title, setup, encoding_key；headline bold True；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 8 色，#F9DA78, #0C1E79, #4A5492, #E5BB9A, #F2D3B3, #908EA9, #F6E7C9, #D1CED3；grayscale safe False。Introduction 的 distributed and entangled memory gap → 四条 neuroscience criteria → Figure 1 接口 → Table 1 形式化约束与 Figures 2–3 的 estimator/decomposition。
优点  四条标准与后续的 observed/intervened state 一一对应。；四格、箭头和参数块形成位置与颜色冗余，阅读方向明确。
弱点  右列图中文字较小，缩放后公式和图片标签成本较高。；颜色承担多种状态语义，灰度阅读主要依赖位置与文字。
可复用模式  用四格条件图固定概念接口，再接参数分解与后续定量证据。

### Figure 2  p.4  method

版式与类型  single_column；architecture, pipeline；purpose 为 method_interface, theory_mechanism；complexity 3/5，1 panel，series None，legend 0，annotations 12，marks 20。
设计与视觉编码  单次 forward pass 累积 X+ 与 X− covariance；图面不提供样本量、数值矩阵、误差或重复实验。 X+、Σ+ 与 W+ 的绿色，X−、Σ− 的蓝色，网络与算子底色的灰紫色 输入堆叠、网络层、covariance 小矩阵与公式块
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 2；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 2. Mechanics of the Engram Method. We compute the Engram weights as W^{+(l)} = W^{(l)} P^{+(l)}, where the projection matrix P^{+(l)} = Σ^{+(l)} (Σ^{+(l)} + Σ^{−(l)})† acts as a surgical filter, where covariances are accumulated during a single forward pass.` Caption words 41；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 8 色，#9299A8, #A7DBB9, #DEF3E4, #506277, #AFE4C3, #C3C5D2, #ACDDBC, #95BEA4；grayscale safe False。Table 1 的四条约束 → Figure 2 的 covariance surgical filter → Eq. (3)–(4) → Figures 4–6 的因果验证。
优点  把抽象投影公式连接到可执行的 network-layer 流程。；虚线统计路径与实线权重路径区分 extraction 与 application。
弱点  公式较密，projection 的伪逆含义仍需正文解释。；单列图较窄，多个小矩阵在页面缩放后难以读取。
可复用模式  用输入、统计量、投影和输出四段式管线解释 closed-form estimator。

### Figure 3  p.5  method

版式与类型  single_column；architecture, conceptual_diagram, pipeline；purpose 为 method_interface, theory_mechanism；complexity 4/5，1 panel，series None，legend 0，annotations 16，marks 26。
设计与视觉编码  概念性分解图；唯一的量化语句是 2^n−1 状态数，未给出数据样本、误差或分布。 A/B/C concept covariance 与对应 W_A^+/W_B^+/W_C^+ 的颜色配对 输入/协方差/权重矩阵小图块
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 1；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 3. Illustration of Engrammatic Decomposition. Linear additivity of spectral subspaces enables the zero-shot synthesis of 2^n − 1 unique memory states from n extracted engrams, mastering the combinatorial explosion of unlearning scenarios (see Appendix F).` Caption words 36；moves title, setup, main_finding, appendix_pointer；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 8 色，#9BBEDB, #F1DFA5, #E99694, #938185, #F4F2E3, #564A4D, #EBA8A5, #F1E6C8；grayscale safe False。Eq. (6) 的 additive covariance decomposition → Figure 3 的多概念接口 → Eq. (7) → Figures 8、12、13 与 Figure 18 的组合状态证据。
优点  把一次统计收集如何支持多概念组合直接画出来。；颜色在 concept covariance 与 engram 输出之间保持配对。
弱点  公式、矩阵与注释密集，单列下需要较高分辨率。；2^n−1 是结构性计数而非实验测量，图面未将两者视觉区分。
可复用模式  用并排的 extraction 与 composition 模块解释可组合的线性结构。

### Figure 4  p.5  results

版式与类型  single_column；heatmap, matrix；purpose 为 headline, main_comparison, qualitative_evidence；complexity 3/5，1 panel，series None，legend 0，annotations 100，marks 100。
设计与视觉编码  每个单元格是一个 target-class accuracy；10×10 class/edit 组合，颜色范围 0–1，未显示重复或误差。 Blues 连续色阶编码 accuracy，白色对角表示目标类接近零 None
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers 0；line styles 0；reference lines 0；uncertainty none；provenance mixed。
caption/header  `Figure 4. Surgical Precision on CIFAR-10 (ResNet-18). The diagonal drop in accuracy confirms that ablating a specific engram selectively erases the target concept, while the off-diagonal stability indicates that reference classes remain intact.` Caption words 33；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  sequential，约 5 色，#F7FBFF, #C6DBEF, #6BAED6, #2171B5, #08306B；grayscale safe True。Figure 3 的单概念分解 → CIFAR-10 surgical erasure claim → Table 2 的 ToW/DA/NMI 对比与 Appendix Figures 11–13 的规模扩展。
优点  对角线与 off-diagonal 形成强视觉对照，目标/保留语义直观。；数字标注让颜色模式可被精确复核；本地图源 notebook 使用 Blues、vmin=0、vmax=1 与 300 dpi。
弱点  x 轴旋转标签密集，类别增加时可读性快速下降。；单一蓝色在低分辨率或色觉差异下区分小差异有限。
可复用模式  用方阵对角线表达 selective erasure，固定 x 为 intervention、y 为 evaluated class。

### Figure 5  p.6  results

版式与类型  single_column；image_montage, qualitative_grid, heatmap；purpose 为 main_comparison, qualitative_evidence；complexity 3/5，2 panel，series None，legend 0，annotations 100，marks 120。
设计与视觉编码  左侧是 MNIST ConvAE 的 ground-truth/ablation reconstruction 样本，右侧按类别汇总 test-set MSE；没有误差或重复定义。 左侧图像灰度表示形态，右侧 Blues 强度表示 MSE/性能值 digit image tiles 与 heatmap cells
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 5. Selective Erasure in ConvAE (MNIST). Ablating target engrams (μ − μ^+) selectively impairs reconstruction (Left), as confirmed by the specific increase in test-set MSE (Right).` Caption words 27；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 5 色，#000000, #FFFFFF, #F7FBFF, #6BAED6, #08306B；grayscale safe True。Figure 4 的监督分类精度 → Figure 5 的无显式标签生成重建 → Figure 7–8 的 CelebA semantic edits。
优点  定性图像与定量热图互相校验 selective erasure。；左右面板语义明确，目标数字的重建破坏很容易定位。
弱点  图注未定义每一列的完整样本选择与 MSE 分母。；小图块和旋转 tick 在单列宽度下对细节复核不友好。
可复用模式  将真实/重建样本与同条件的逐类热图配对，避免只用视觉例子支撑因果结论。

### Figure 6  p.6  results

版式与类型  single_column；scatter；purpose 为 main_comparison, mechanism；complexity 3/5，1 panel，series 11，legend 11，annotations 11，marks None。
设计与视觉编码  散点比较 original/retrained 两个 CKA 关系；方法点云和参考对角线，没有 error bar、置信区间或重复聚合说明。 方法类别的离散颜色 不同 unlearning method 的 marker
plot grammar  rendering raster；x linear；y linear；grid both；legend True（lower right）；direct labels False；markers 11；line styles 2；reference lines 1；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 6. CKA similarity of the original (x-axis) versus the retrained (y-axis) models; ideal unlearning appears toward top-left.` Caption words 18；moves title, setup, comparison, main_finding；headline bold False；self-contained False；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  categorical，约 11 色，#348ABD, #E1812C, #FFBF00, #CF6DAA, #55A868, #5A9EC9, #E15759, #4C4C4C, #000000, #999999, #777777；grayscale safe False。Table 2 的输出/表示指标 → Figure 6 的 representation proximity diagnostic → Appendix Figure 10 的 CIFAR-100 复现。
优点  top-left 目标区由坐标和 y=x 同时定义，方向容易解释。；颜色与 marker 双编码方法，避免仅靠颜色识别。
弱点  图注未解释每个 marker、点数和 seed 聚合方式。；11 项 legend 占据绘图区，点云重叠时比较细节受限。
可复用模式  用二维相似度坐标固定“接近 retrain、远离 original”的目标区，并用 shape/color 冗余编码方法。

### Figure 7  p.7  results

版式与类型  single_column；image_montage, qualitative_grid；purpose 为 qualitative_evidence, mechanism；complexity 5/5，4 panel，series None，legend 0，annotations 20，marks None。
设计与视觉编码  四个 CelebA 属性各以多张人脸示例呈现编辑轨迹；无数值聚合、分母或不确定性。 自然脸部图像变化与绿色 α 文字 人物图像 tiles
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 7. Semantic Specificity Control in WAE (CelebA). Ablating attribute-specific engrams (μ − μ_c^+) removes fine-grained target features (e.g., eyeglasses, bangs) while strictly preserving facial identity. The slider (μ − αμ_c^+) demonstrates the linear compositionality of identified engrams, allowing for fine-grained, continuous manipulation of semantic intensity without retraining.` Caption words 48；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 2 色，#5DBE7A, #000000；grayscale safe False。Figure 5 的生成式 selective reconstruction → Figure 7 的 scalar engram control → Figure 15 的更大属性轨迹与 Figure 8 的 vector arithmetic。
优点  同一人物跨 α 配对，身份保留与属性变化同时可见。；α 序列与属性行直接标注，省去外置 legend。
弱点  高密度人脸小图在 PDF 缩放后难以判断细微身份变化。；caption 没有说明样本数、选择标准或 α 的方向约定以外的重建细节。
可复用模式  固定样本身份并横向扫描单一 edit strength，让语义连续性成为可视证据。

### Figure 8  p.7  results

版式与类型  single_column；image_montage, qualitative_grid, conceptual_diagram；purpose 为 qualitative_evidence, theory_mechanism；complexity 4/5，3 panel，series None，legend 0，annotations 20，marks None。
设计与视觉编码  按属性组合展示图像重建状态；结果是定性样本，没有样本量、聚合或不确定性。 人脸图像与中央概念节点的 pastel colors 样本 tiles、concept nodes 与箭头
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 2；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 8. Engram Arithmetics Examples showing bidirectional arithmetic operation for reconstruction with identified engrams of μ_β^+ (Glasses) and μ_γ^+ (Goatee). GT, Ground Truth.` Caption words 23；moves title, setup, encoding_key, abbreviation_definition；headline bold True；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 6 色，#E99694, #9BBEDB, #F1DFA5, #938185, #000000, #FFFFFF；grayscale safe False。Figure 3 的 linear additivity → Figure 8 的 bidirectional attribute arithmetic → Figure 18 的 n-concept state space。
优点  中央路径把多张图像状态与向量运算联系起来。；加减箭头和 GT 标签使操作方向可追踪。
弱点  组合节点与图像列较密，读者需要正文映射 μ_A/μ_B。；定性例子未报告系统化成功率或失败案例。
可复用模式  用中央 composition graph 连接左右对照样本，展示加法与减法的双向可逆感。

### Figure 9  p.9  results

版式与类型  single_column；heatmap, matrix；purpose 为 mechanism, headline；complexity 3/5，1 panel，series None，legend 0，annotations 20，marks 112。
设计与视觉编码  16 个 transformer layers 加 LM head 的 layer-type matrix；颜色表示 ||W^+||_F/||W||_F 的相对范数，未报告重复或误差。 紫到黄连续色阶编码 relative engram weight norm None
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 9. Relative Engram Weight Norm as a Proxy for Causal Memory Traces. We show the identified relative weight norm of the engram weights over original weight in Llama-3.2-1B for Tofu dataset. The heatmap reveals that the changes are predominantly concentrated in the Query and Key of self-attention and Gate of MLP. With this relative norm, we applied surgical strength in TOFU unlearning process.` Caption words 64；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  sequential，约 6 色，#0C1E79, #4A5492, #908EA9, #E5BB9A, #F9DA78, #FFFFFF；grayscale safe False。Figure 6 的 CKA proximity → Figure 9 的 weight-space localization → Appendix Table 8 layer-type ablation 与 Table 3 adaptive α。
优点  把 LLM 层级定位从文字 claim 变成可扫描的矩阵。；Q/K/Gate 的暖色区域与下游 ablation 形成结构性对应。
弱点  colorbar 的 norm 定义仍需要正文公式，图注没有单位。；layer labels 和 LM head 文字小，色阶对相近值的区分有限。
可复用模式  用 layer-type × depth 热图定位结构性变化，再由消融表验证颜色模式的因果含义。

### Figure 10  p.16  appendix

版式与类型  single_column；scatter；purpose 为 robustness, main_comparison；complexity 3/5，1 panel，series 11，legend 11，annotations None，marks None。
设计与视觉编码  CIFAR-100 的方法级 CKA 散点；坐标约 0.55–1.00，无误差或 seed 聚合定义。 方法类别离散颜色 method markers
plot grammar  rendering raster；x linear；y linear；grid both；legend True（lower right）；direct labels False；markers 11；line styles 2；reference lines 1；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 10. CKA similarity of the original (x-axis) versus the retrained (y-axis) models for CIFAR-100.` Caption words 15；moves title, setup, comparison；headline bold False；self-contained False；main finding False。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  categorical，约 11 色，#348ABD, #E1812C, #FFBF00, #CF6DAA, #55A868, #5A9EC9, #E15759, #4C4C4C, #000000, #999999, #777777；grayscale safe False。Figure 6 的 CIFAR-10 CKA diagnostic → Figure 10 的 CIFAR-100 appendix replication；与 Table 2 主结果互补。
优点  沿用 Figure 6 grammar，跨数据集比较成本低。；y=x 参考线明确 top-left 的 unlearning target。
弱点  caption 没有定义 method symbols、点数或 aggregation。；appendix 单列 legend 与点云重叠，难以读取小差异。
可复用模式  把同一诊断图语法复制到第二数据集，专门验证主图结论的迁移。

### Figure 11  p.16  appendix

版式与类型  single_column；heatmap, matrix；purpose 为 robustness, main_comparison；complexity 3/5，1 panel，series None，legend 0，annotations 100，marks 100。
设计与视觉编码  10×10 class/edit accuracy matrix；对角线数值约接近零、off-diagonal 接近一，未报告不确定性。local notebook exact source uses figsize 6×4.5 in、Blues、vmin/vmax 0/1、300 dpi。 Blues accuracy 0–1，white diagonal is target drop None
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance mixed。
caption/header  `Figure 11. Class-wise unlearning performance on MNIST 3-layer MLP We evaluate the Engram Method by unlearning each of the 10 classes individually. The heatmap illustrates that the accuracy of the target class (white diagonal) drops to near zero, while the performance on the remaining 99 classes (dark blue off-diagonal) is perfectly preserved, showcasing the method’s ability to handle high-dimensional class sets without collateral interference.` Caption words 64；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  sequential，约 5 色，#F7FBFF, #C6DBEF, #6BAED6, #2171B5, #08306B；grayscale safe True。Figure 4 的 ResNet-18 CIFAR-10 pattern → Figure 11 的 MLP appendix scale check → Figures 12–13 的 20/100 类扩展。
优点  同一 heatmap grammar 支持跨架构和类别数对照。；单元格数值与对角线语义同时可见，验证目标类选择性。
弱点  99 类表述与图上 10 类示例存在叙述张力，caption 未解释该计数边界。；旋转列标签和小数字在单列尺寸下拥挤。
可复用模式  固定 intervention columns 与 evaluated-class rows，使用 white diagonal/dark off-diagonal 作为跨实验视觉协议。

### Figure 12  p.17  appendix

版式与类型  page_width；heatmap, matrix；purpose 为 robustness, main_comparison；complexity 5/5，1 panel，series None，legend 0，annotations None，marks 2500。
设计与视觉编码  Grouped ImageNet-1k class-wise accuracy matrix；每个 group 含 20 classes，图上以约 50 groups 展开，未显示误差或重复。 Blues group accuracy，white diagonal target group drop None
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 12. Grouped class-wise unlearning performance on ImageNet-1k with ViT We show 20-class grouped-wise unlearning result. Each row represents a model trained to unlearn a specific group of classes. The white diagonal elements indicate near-zero accuracy for the target forgotten groups, while the dark blue off-diagonal regions demonstrate that the accuracy for other classes is preserved, confirming the surgical precision of the method.` Caption words 63；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  sequential，约 5 色，#F7FBFF, #C6DBEF, #6BAED6, #2171B5, #08306B；grayscale safe True。Figure 3 的 2^n−1 combinatorial motivation → Figure 12 的 1k-class scalability → Figure 13 CIFAR-100 dense classwise check。
优点  页宽布局为密集 group labels 留出必要空间。；白色对角与深蓝 off-diagonal 在大矩阵中保持结构可见。
弱点  50×50 级别矩阵文字极小，逐 group 数值难以核验。；caption 未说明 group 构造和每个 cell 的聚合分母。
可复用模式  对大类集合使用 page-width heatmap，只保留结构性 diagonal/off-diagonal pattern。

### Figure 13  p.18  appendix

版式与类型  page_width；heatmap, matrix；purpose 为 robustness, main_comparison；complexity 5/5，1 panel，series None，legend 0，annotations None，marks 10000。
设计与视觉编码  100×100 class/edit accuracy matrix；白色 diagonal 表示目标类接近零，off-diagonal 为保留类 accuracy，未显示误差。 Blues accuracy 0–1 None
plot grammar  rendering raster；x categorical；y categorical；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 13. Class-wise unlearning performance on CIFAR-100 in ResNet-18. Each row i represents a model specifically updated to unlearn class i using the Engram Method. The prominent white diagonal indicates that the accuracy for the target forgotten class drops to near zero, while the consistently dark blue off-diagonal regions demonstrate that the knowledge of all other 99 classes remains intact. This highlights the method’s ability to perform class-specific erasure with minimal collateral damage to unrelated categories.` Caption words 76；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  sequential，约 5 色，#F7FBFF, #C6DBEF, #6BAED6, #2171B5, #08306B；grayscale safe True。Figure 4/11 的 diagonal erasure protocol → Figure 13 的 CIFAR-100 scale result → Table 2 classwise aggregate and Figure 14 overlap failure boundary。
优点  页宽矩阵让 100 类的整体结构仍然可见。；颜色和行列顺序对齐，目标类与对应 edit 一眼可定位。
弱点  高密度 tick labels 几乎不能逐项阅读。；只显示颜色而无数值标注，细微 collateral change 难以量化。
可复用模式  用页宽方阵承载大类规模，依赖整体 diagonal/off-diagonal pattern 而非逐格文本。

### Figure 14  p.19  appendix

版式与类型  page_width；bar, line；purpose 为 robustness, failure, mechanism；complexity 4/5，2 panel，series 3，legend 0，annotations 8，marks 8。
设计与视觉编码  Panel (a) 汇总 same/different-superclass pair 的 mean accuracy drop；panel (b) 按 cosine-similarity bins 汇总 drop，并显示 error bars。caption 未定义 error bar 的统计类型。 red same-superclass/overlap 与 blue different-superclass/low overlap bar in (a), circular markers in (b)
plot grammar  rendering raster；x categorical；y linear；grid none；legend False（None）；direct labels True；markers 1；line styles 2；reference lines 1；uncertainty error_bar；provenance rendered_estimate。
caption/header  `Figure 14. Graceful degradation under semantic overlap on CIFAR-100 (ResNet-18). (a) Mean test-set accuracy drop on reference classes after ablating the target engram, split by same-superclass (high feature overlap) versus different-superclass (low overlap) pairs. Same-superclass pairs show only a 0.80 percentage-point mean degradation; different-superclass pairs are effectively unaffected. (b) Within a superclass, accuracy drop varies smoothly and monotonically with cosine similarity between class-conditional input representations, with no discontinuous collapse. These results empirically confirm that the soft-projection operator P^+ accommodates partial concept overlap.` Caption words 82；moves title, setup, encoding_key, comparison, uncertainty_definition, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 4 色，#B2182B, #2166AC, #777777, #FFFFFF；grayscale safe False。Figure 13 的大规模 collateral-preservation claim → Figure 14 的 semantic-overlap failure boundary → Section 6.3 soft projection mechanism。
优点  把“非零重叠时平滑退化”从定性说法转为分组柱和趋势线。；零线、panel labels 与 error bars 共同表达方向和不确定性。
弱点  不同 panel 的 x 轴单位和聚合层级不统一，跨 panel 数值比较不应直接进行；panel (b) 的 Cosine Distance 轴与 caption 的 cosine similarity 用词不一致。；error bar 定义缺失，0.80 pp 也缺少样本数和分母。
可复用模式  用分组摘要加相似度趋势同时展示平均影响和 overlap-conditioned gradient。

### Figure 15  p.20  appendix

版式与类型  page_width；image_montage, qualitative_grid；purpose 为 robustness, qualitative_evidence；complexity 5/5，4 panel，series None，legend 0，annotations 32，marks None。
设计与视觉编码  四个属性各有七个 α 条件和 GT 重建；图面是定性轨迹，没有聚合、不确定性或自动属性分数。 natural face image appearance and green α labels face image tiles
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 0；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 15. Semantic attribute control on CelebA (WAE). For each attribute (Goatee, Glasses, Hat, Bangs), we apply continuous engram-based editing μ − αμ_c^+ with α ∈ {−2/3, −1/3, 0, 1/3, 2/3, 1, 4/3}. Increasing α progressively removes the target attribute while preserving facial identity; negative α amplifies the attribute. The smooth, monotonic interpolation across α values demonstrates that the identified engram defines a stable, linearizable trajectory in weight space for semantic manipulation without retraining. GT: ground truth reconstruction at α = 0.` Caption words 82；moves title, setup, encoding_key, main_finding, abbreviation_definition；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  not_applicable，约 0 色，无独立调色板；grayscale safe False。Figure 7 的四属性主文样例 → Figure 15 的 appendix expanded grid → Figure 8 arithmetic composition。
优点  统一 α grid 让属性增强/消除方向可直接比较。；多行属性和固定人物配对强化 identity-preservation claim。
弱点  页宽图片数量大，细微属性变化需要放大查看。；caption 没有说明每行样本数、seed 或图像选择。
可复用模式  固定 α 列表和属性行，使用同一版式扩展定性编辑证据。

### Figure 16  p.21  appendix

版式与类型  single_column；conceptual_diagram, architecture；purpose 为 theory_mechanism, method_interface；complexity 2/5，1 panel，series None，legend 0，annotations 12，marks 8。
设计与视觉编码  算子示意图，无经验数据、单位、样本、聚合或不确定性。 green engram blocks, blue/grey original blocks, purple projector blocks block matrices and column vectors
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 1；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 16. Global Engram Operator. Block-diagonal projector P acting on layer-wise weights μ.` Caption words 13；moves title, encoding_key；headline bold False；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 5 色，#A7DBB9, #506277, #C3C5D2, #E6B8D7, #FFFFFF；grayscale safe False。Eq. (5) global linear operation → Figure 16 block-diagonal construction → Figure 9 layer localization and Table 8 targeted layer ablation。
优点  将逐层 projector 组合成一个全局对象，补足 Figure 2 的局部视角。；块结构与公式符号一一对应。
弱点  示意块不表示真实矩阵维度或数值稀疏度。；单列尺寸使 P block labels 较小。
可复用模式  用 block-diagonal operator 将 layer-wise extraction 统一为 global map。

### Figure 17  p.24  appendix

版式与类型  single_column；conceptual_diagram, network；purpose 为 theory_mechanism, method_interface；complexity 3/5，1 panel，series None，legend 0，annotations 14，marks 12。
设计与视觉编码  四个 compositional states 的概念状态图；箭头类型表达 acquire/eliminate，未提供实验频次或概率。 pastel A/B overlap regions and state blocks state circles/overlap diagrams
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 2；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 17. Transitions between fundamental memory states in compositional learning. For a concept C consisting of sub-concepts {A,B}, we identify four compositional memory states: (i) the knowledge vacuum μ_0; (ii) isolated states μ_A,μ_B for individual concepts; and (iii) the composite state μ_AB for their superposition. Solid and dotted arrows represent acquisition (+) and elimination (−) processes, respectively. Our framework posits a commutative manifold where the integration of A and B reaches a consistent equilibrium regardless of the learning sequence.` Caption words 79；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 6 色，#E99694, #9BBEDB, #938185, #F1DFA5, #666666, #FFFFFF；grayscale safe False。Figure 3 的 additive subspaces → Figure 17 的 fundamental state transition hypothesis → Figure 18 的 n-concept hypercube 与 Table 9 instantiation test。
优点  状态、操作方向和复合关系在一张图中闭合。；solid/dotted 双线型即使颜色消失也保留操作语义。
弱点  commutative manifold 是假设性结构，图面不显示路径实验或反例。；重叠圆与小型公式在单列中较密。
可复用模式  用 square state graph 表示 acquisition/elimination 的可交换路径，并显式标注 vacuum。

### Figure 18  p.25  appendix

版式与类型  single_column；network, conceptual_diagram；purpose 为 theory_mechanism, headline；complexity 4/5，2 panel，series None，legend 0，annotations 20，marks 16。
设计与视觉编码  概念状态空间示意；2^n 与 2^n−1 是结构性计数，图面没有实验样本或不确定性。 pastel concept membership and state nodes nodes, cube vertices and connecting edges
plot grammar  rendering raster；x none；y none；grid none；legend False（None）；direct labels True；markers None；line styles 1；reference lines 0；uncertainty none；provenance rendered_estimate。
caption/header  `Figure 18. Combinatorial State Space. For n concepts, the memory manifold consists of 2^n discrete nodes. Excluding the trivial starting state (Vacuum), there are 2^n − 1 active knowledge states that a user might wish to reach (or unlearn to). Our Engrammatic Decomposition allows for zero-shot traversal between any two nodes in this hypercube via simple arithmetic.` Caption words 57；moves title, setup, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math, Calibri，约 5.98–11.0 pt，mixed。
颜色与证据关系  mixed，约 6 色，#E99694, #9BBEDB, #F1DFA5, #938185, #564A4D, #FFFFFF；grayscale safe False。Figure 3 的 2^n−1 decomposition claim → Figure 18 combinatorial state-space summary → Appendix G Table 9 checks a concrete instantiation consequence。
优点  n=2 square 与 n=3 cube 将抽象指数增长变成可见拓扑。；Vacuum 排除和 active-state count 直接标注。
弱点  只展示 n=2/3，其他 n 依赖 ellipsis 和公式推断。；节点文字和边在单列中较小，路径方向不总是显式箭头。
可复用模式  用低维 hypercube 示例解释指数状态空间，再以公式概括任意 n。

## Tables

### Table 1  p.3  method

版式与表头  single_column；method_interface, theory_mechanism；4 data rows，3 columns，2 header levels，2 row groups，precision None，rules partial_grid。
caption/header  `Table 1. Operationalizing Engrammatic Axioms as Optimization Constraints. By contrasting observed states with intervened states, we establish formal linear-algebraic constraints from four neuroscience engram criteria: i) Specificity (X^±, target vs. ref.), ii) Reactivation (Z̄^{±}_{0,1}, internal representation), iii) Sufficiency (‡, gain-of-function) and iv) Necessity (†, loss-of-function).` Caption words 45；moves title, setup, encoding_key, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Observed and intervened states for Target X+ and Ref. X−; baseline t=0 and learned t=1 equations use W0/W1, Z, † and ‡. No empirical uncertainty. Highlighting italic, cell_color；uncertainty none reported。
证据关系  Figure 1 criteria → Table 1 constraints → Figure 2 covariance estimator and Eq. (2) objective.
优点  Two-level header separates target from baseline/learned states.；Observed/intervened grey row bands make causal contrast explicit.
弱点  Equation-heavy cells are small and require notation from body.；Target column and state groupings may be confused at narrow width.
可复用模式  Use a two-level state table to turn conceptual criteria into auditable algebraic constraints.

### Table 2  p.6  results

版式与表头  single_column；main_comparison, robustness；18 data rows，4 columns，2 header levels，2 row groups，precision 3，rules booktabs。
caption/header  `Table 2. Class-wise unlearning comparison on CIFAR-10/100. We report ToW(↑), DA(↑), and NMI(↓). Values in parentheses indicate the gap with the retrain models. Best values are bolded, and second-best values are underlined. Shaded rows indicate our proposed method and α_best is the best α from grid search.` Caption words 47；moves title, setup, encoding_key, comparison；headline bold False；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Two 9-row blocks for CIFAR-10 ResNet-18 and CIFAR-100 ResNet-50; columns Method, ToW↑, DA↑, NMI↓ with three decimals. Main Engram rows are shaded. Highlighting bold, underline, cell_color, best_second_best；uncertainty Parenthesized values are gaps to retrain, not uncertainty intervals; no seed aggregation or error bars are shown.。
证据关系  Figure 4/5 causal examples → Table 2 aggregate class-wise comparison → Figure 6 CKA and Appendix Figures 10–14.
优点  Same metrics and direction arrows across both dataset blocks.；Parenthetical retrain gaps expose the comparison baseline compactly.
弱点  Two architectures are stacked without an explicit visual divider beyond rules and headers.；Parentheses can be mistaken for uncertainty, although caption defines them as retrain gaps.
可复用模式  Repeat a compact metric block across datasets while keeping one shared method vocabulary.

### Table 3  p.8  results

版式与表头  single_column；main_comparison, efficiency_cost；12 data rows，6 columns，1 header levels，3 row groups，precision 4，rules booktabs。
caption/header  `Table 3. Evaluation results on Llama3.2-1B with TOFU dataset. The top two rows are baselines. Best values among the methods are bolded, and second-best values are underlined. α = 0.6 denotes uniform α across layers, and α_W-Norm denotes adaptive α obtained by rescaling the weight norm ratio ||W^+||/||W|| to [0,1]. EM: Exact Memorization, FQ: log_10 Forget Quality.` Caption words 57；moves title, setup, encoding_key, comparison, abbreviation_definition；headline bold False；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows Init Fine., Retain, eight gradient-based methods, and two Engram variants; columns Method, Mem.↑, Util.↑, Priv.↑, EM↓, FQ↑. Values use four decimals. Highlighting bold, underline, cell_color, best_second_best；uncertainty No uncertainty display; each metric is a single reported score. ↑/↓ directions are embedded in headers.。
证据关系  Figure 9 W-Norm localization → Table 3 LLM benchmark → Table 4 closed-form comparison and Appendix Table 6 metric breakdown.
优点  Compactly puts memorization, utility, privacy and EM/FQ on one decision surface.；Shaded Engram rows and direction arrows make the proposed variants searchable.
弱点  Method names and metric abbreviations are compressed.；Single scores hide seed variation and metric construction until Appendix E.2.
可复用模式  Use one multi-axis score table for the main LLM result, then unpack metrics in an appendix table.

### Table 4  p.9  results

版式与表头  single_column；main_comparison, efficiency_cost；3 data rows，6 columns，1 header levels，1 row groups，precision 3，rules booktabs。
caption/header  `Table 4. Comparison with closed-form editing baselines on TOFU (Llama-3.2-1B, forget10). Engram, UCE, and Task Arithmetic are all gradient-free closed-form methods. Despite this shared paradigm, Engram outperforms both baselines across all metrics except utility. See Appendix E.5 for algebraic correspondence, hyperparameter sweeps, and screening results.` Caption words 45；moves title, setup, comparison, main_finding, appendix_pointer；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Three method rows and six columns Method, Overall↑, Mem.↑, Util.↑, Priv.↑, EM↓; values use three decimals. Highlighting bold；uncertainty No uncertainty or interval; one score per method and metric.。
证据关系  Table 3 main LLM result → Table 4 isolates gradient-free closed-form competitors → Appendix E.5 correspondence and sweeps.
优点  All relevant outcome dimensions fit in a single narrow comparison.；Caption states the comparison paradigm and the one utility exception.
弱点  Three rows make statistical robustness impossible to infer.；No explicit shading separates proposed method from baselines.
可复用模式  Use a small closed-form baseline table when the comparison set and metric directions are stable.

### Table 5  p.15  appendix

版式与表头  single_column；experimental_design, reproduction；7 data rows，2 columns，1 header levels，1 row groups，precision None，rules booktabs。
caption/header  `Table 5. Hyperparameter search spaces for each unlearning method.` Caption words 9；moves title, setup；headline bold False；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows Fine-tune, l1-Sparse, NegGrad, NegGrad+, SalUn, Random Label, Engram; columns Method and Hyperparameters (LR / Epochs / Others). Lists LR grid, γ/β/sparsity and Engram α grid. Highlighting none；uncertainty No uncertainty; this is a search-space specification rather than an outcome table.。
证据关系  Main Table 2 selected α_best values → Table 5 records the search space → Appendix B.4.1 evaluation protocol.
优点  Makes tuning degrees of freedom auditable.；Shared “as above” LR notation avoids repeating a long grid.
弱点  “As above” requires carrying context across rows.；Search-space table does not report selected values or sensitivity.
可复用模式  Record search spaces in a compact two-column appendix table, with metric outcomes kept separate.

### Table 6  p.22  appendix

版式与表头  page_width；main_comparison, robustness；12 data rows，16 columns，2 header levels，3 row groups，precision 4，rules booktabs。
caption/header  `Table 6. Detailed breakdown of unlearning performance on the TOFU dataset (Forget10). The Overall score is the harmonic mean of Memorization, Utility, and Privacy scores. Memorization, Utility, and Privacy scores are harmonic means of their respective sub-metrics (denoted in the columns below them). ↑ indicates higher is better, and ↓ indicates lower is better. Best values (excluding baselines) are bolded.` Caption words 60；moves title, setup, encoding_key, comparison；headline bold False；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows Init Fine., Retain, eight methods and two Engram variants; 16 columns grouped as Overall, Memorization (Score/EM/ES/PP/TR), Utility (Score/MU/FF), Privacy (Score/SLOSS/SZLIB/SMIN-K/SMIN-K++) and FQ. Four decimals. Highlighting bold；uncertainty No interval or error display; the table reports deterministic aggregate scores and submetrics. EM/FQ directions are explicit.。
证据关系  Table 3 summary metrics → Table 6 expands harmonic-mean components → Appendix E.2 defines metrics and the safe hmean.
优点  Hierarchical headers expose how Overall is assembled.；Page-width placement is necessary for 16 columns and preserves metric groups.
弱点  Very small text and many vertical separators slow row scanning.；FQ on a different numerical scale sits beside bounded scores without a visual scale cue.
可复用模式  Use grouped multi-level headers to expose an aggregate metric’s construction without duplicating rows.

### Table 7  p.23  appendix

版式与表头  single_column；efficiency_cost, main_comparison；11 data rows，4 columns，1 header levels，3 row groups，precision None，rules booktabs。
caption/header  `Table 7. Compute and memory profile for gradient-based unlearning vs. Engram on Llama-3.2-1B (TOFU forget10). Gradient-based estimates assume 10 epochs of training (e.g., AltPO/NPO/SimNPO); Engram requires a single forward pass plus a closed-form solve. P = 1.24 × 10^9 parameters; activations estimated at batch size 2, sequence length 256.` Caption words 49；moves title, setup, encoding_key, comparison；headline bold True；self-contained True；main finding False。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows cover forward/backward/SVD/total FLOPs, weights/gradients/optimizer/activations/covariance/total memory and wall time; columns Resource, Gradient-based, Engram, Ratio. Highlighting bold；uncertainty Approximate quantities use ~ and “negl.”; no variance or hardware replication is shown.。
证据关系  Table 4 compute frontier claim → Table 7 decomposes FLOPs/memory/time → Section 7 compute–accuracy frontier.
优点  Rows align resource categories and ratio in one scan.；Approximation symbols distinguish estimates from exact model scores.
弱点  Gradient-based and Engram columns mix units across row groups.；A100 and batch/sequence assumptions are only in caption.
可复用模式  Group compute, memory and wall time under a shared resource table with explicit assumptions.

### Table 8  p.24  appendix

版式与表头  single_column；ablation, mechanism；4 data rows，6 columns，1 header levels，1 row groups，precision 3，rules booktabs。
caption/header  `Table 8. Layer-type ablation on TOFU (Llama-3.2-1B, forget10). We selectively extract engrams from different projection layer subsets to isolate the contribution of each layer type. Q/K + Gate alone matches the all-layer Overall score, while removing Q/K/Gate collapses unlearning performance to near-baseline, empirically confirming the W-Norm localization pattern (Fig. 9). The Utility column shows that excluding Q/K/Gate preserves general capability (0.968) at the cost of completely failing to unlearn—indicating that these layers are precisely where the target memory resides.` Caption words 79；moves title, setup, encoding_key, comparison, main_finding；headline bold True；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows All linear projections, Q/K only, Q/K + Gate, No Q/K/Gate; columns Targeted Layers, Overall↑, Mem.↑, Util.↑, Priv.↑, EM↓; three decimals. Highlighting bold；uncertainty No uncertainty; each targeted-layer subset has one score per metric.。
证据关系  Figure 9 W-Norm heatmap → Table 8 causal layer ablation → Table 3 α_W-Norm and Section E.6 findings.
优点  Directly tests the localization hypothesis with a small controlled row set.；Utility and unlearning metrics show the collateral/forgetting tradeoff.
弱点  Only four subsets cannot localize individual Q versus K versus Gate contributions.；Single scores lack seed or class-level spread.
可复用模式  Follow a localization heatmap with a targeted subset ablation table that includes both forgetting and utility.

### Table 9  p.26  appendix

版式与表头  single_column；ablation, theory_mechanism；2 data rows，3 columns，1 header levels，1 row groups，precision 3，rules booktabs。
caption/header  `Table 9. Effect of the instantiation choice on TOFU (Llama-3.2-1B, forget10). The tabula rasa instantiation decouples the layer-wise sub-problems and solves all layers in parallel. Naive substitution of the fine-tuning delta without sequential V^* optimization accumulates per-layer error.` Caption words 38；moves title, setup, comparison, main_finding；headline bold False；self-contained True；main finding True。Typography Nimbus Roman No9 L, Computer Modern math，body/header 6.83/7.0 pt，header bold。
数据与高亮  Rows ΔW = W_ft − W_pt (naive) and ΔW = W_ft (tabula rasa, ours); columns Instantiation, Overall↑, EM↓; three decimals. Highlighting bold；uncertainty No uncertainty; two instantiation choices each report one Overall and EM score.。
证据关系  Appendix G three-state derivation → Table 9 empirical naive-substitution failure → Table 7 single-pass efficiency rationale.
优点  Small table isolates the structural choice rather than burying it in a large baseline table.；Bold ours row makes the causal contrast visible.
弱点  Two rows do not expose per-layer error accumulation directly.；Caption supplies the mechanism, while table has no diagnostic per-layer values.
可复用模式  Pair a structural derivation with a two-row counterfactual instantiation test.

## 跨对象系统

visual_narrative  Figure 1 先把 specificity/reactivation/sufficiency/necessity 画成概念接口，Table 1 把接口变成约束，Figures 2–3 给出 covariance filter 与组合分解，Figures 4–8 依次提供分类、生成、CKA 与 semantic arithmetic 证据，Figure 9 把机制定位到 LLM 层级；附录 Figures 10–18 和 Tables 5–9 扩展架构规模、重叠失败、成本、层消融与状态空间。
caption_system  caption 多以 italic Figure/Table label 开头，主文结论型标题常粗体；设置、编码、比较和主发现覆盖不均，Figure 6/10 与若干 appendix tables 缺少粗体标题或 self-contained method key。
table_header_system  表格使用小号 Nimbus/Computer Modern、booktabs 横线、↑/↓ 指标方向和少量分组表头；Table 6 以二级 grouped header 展开 Overall 的 harmonic-mean 组成，Table 2/3 用 shaded Engram rows 标示提出方法。
method_result_ablation_link  Table 1→Figure 2→Figure 3 构成 method spine；Figure 4/5/6/7/8 与 Table 2/3/4 承担主结果；Figure 9→Table 8 是最清晰的 localization-to-causal-ablation 链路，Table 9 验证 tabula-rasa instantiation。
main_appendix_link  主文 Figures 4/5/6/7/8/9 分别在 Appendix Figures 10–15、Table 6–8 中扩展到 CIFAR-100、MNIST、ImageNet、CelebA、metric breakdown、cost 与 layer subsets；Figures 16–18 把 global operator 与组合状态假设形式化。
typography_consistency  正文和 caption 主要是 Nimbus Roman No9 L/Computer Modern math，图内 raster 标签偏 sans-serif；整体统一但图内字号、caption headline bold 与 appendix 表格字号不完全一致。
color_consistency  Blues heatmap 在 classwise accuracy 上稳定复用，Engram rows 使用浅灰底，diagram pastel colors 随概念变化；CKA 方法色与 semantic montage 颜色不构成跨对象统一 legend。

## 最终判断

最可复用模式
- 用 intervention×evaluated-unit 方阵的 white diagonal/dark off-diagonal grammar 表达 selective erasure，并跨架构扩展。
- 将机制热图（Figure 9）与 targeted subset ablation（Table 8）配对，区分相关定位和因果验证。
- 对定性编辑固定样本身份与 α 列表，以横向 montage 展示连续或组合状态，再用 caption 明确操作方向。
- 用 page-width grouped header table 展开 aggregate score 的组成，并保留 ↑/↓、成本和假设。

最高价值对象  Figure 2, Figure 4, Figure 9, Figure 14, Table 3, Table 6, Table 8

失败模式
- 图注和表注的 headline bold、自包含程度及方法符号定义不一致，Figure 6/10 与 Table 2/3/5/6/9 尤明显。
- 高密度 heatmap、qualitative montage 和 16-column Table 6 在单页缩放后难以逐格复核。
- 单一分数或无 uncertainty display 的表格承担较强跨 seed/类别结论，caption 很少交代分母、重复和 error-bar 定义。
- Figure 12/13/15 的大规模对象依赖整体模式，缺少可复核的数值切片或失败案例。

一句话视觉策略  论文以 closed-form memory isolation 为主线，用概念管线固定 operator 接口，用 diagonal heatmap、CKA、semantic montage 和层定位/消融表逐步把“可组合且局部”的 engram claim 推到多架构与 LLM 规模。

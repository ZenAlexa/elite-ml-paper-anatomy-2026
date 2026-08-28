# InfoTok 视觉审计

- **paper_id**：`iclr-2026-3c7fde53bdb5`
- **论文**：InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression
- **PDF 事实源**：`corpus/pdfs/iclr-2026-3c7fde53bdb5.pdf`，已完整读取物理页 1–23（正文、参考文献、Supplementary Material、Appendix A–E）。所有含视觉对象的页面均以 200 dpi 渲染（letter 页面 1700×2200 像素）；先按渲染页复核，再用 `pdfimages`、`pdffonts` 与 `pdftohtml -xml` 核对对象和字体。
- **正文/附录边界**：正文页 1–10；参考文献页 11–13；补充材料页 14–23。正文中的 Algorithm 1（p. 4）是算法块，不计入 Figure/Table；没有把它误报为视觉对象。

## 1. PDF 对象清单核对

以 PDF 实际渲染为对象清单事实源，共有 **6 幅 Figure、6 张 Table**：

| PDF 标签 | 页 | 模块 | 视觉核对 |
|---|---:|---|---|
| Figure 1 | 2 | method | 双栏方法流程图，含两行示例视频 |
| Table 1 | 7 | results | 双数据集主比较表 |
| Figure 2 | 7 | results | 四行方法 × 三组场景的重建图网格 |
| Figure 3 | 8 | ablation | 原图与三个压缩率的重建网格 |
| Figure 4 | 8 | results | 六个质量曲线面板加一个 NFE 柱状面板 |
| Table 2 | 9 | ablation | ELBO router 与 Optimal 搜索的三档预算比较 |
| Table 3 | 9 | ablation | 左右两个消融子表 |
| Figure 5 | 15 | appendix A | 狗视频六帧的 Original/InfoTok/Token Mask/Token Usage 网格 |
| Figure 6 | 16 | appendix A | 工作空间视频四帧的同构网格 |
| Table 4 | 22 | appendix C | compressor、quantizer、Cosmos 配置 |
| Table 5 | 23 | appendix D | 256×256 与 360p 多宽高比比较 |
| Table 6 | 23 | appendix D | NFE 与单视频推理延迟 |

页 1、3–6、10–14、17–21 逐页检查后，没有额外 Figure/Table；页 14 是补充目录，页 17–21 是证明，故不把公式、定理、Algorithm 1 或目录当作图表。Figure 3/4 在同一物理页，Table 5/6 在同一物理页，均按 PDF 标签分别记录。

## 2. 视觉源检索

审计前先检查 `reports/tables/visual_source_inventory.csv` 与 `corpus/visual_sources/iclr-2026-3c7fde53bdb5/`。inventory 的旧行将该论文记为 `repository_without_visual_source`，本地视觉源目录为空；这不是 PDF 对象清单，也不能覆盖之后公开的仓库内容。

随后只读使用 `gh` 核查论文首页明确的 project URL（`https://research.nvidia.com/labs/dir/infotok/`）对应的作者仓库及严格标题候选：

- **可信仓库**：[`YWolfeee/InfoTok`](https://github.com/YWolfeee/InfoTok)。`gh repo view` 的 description 为 `Codebase for InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression`；README 一级标题与论文题目严格一致，并链接同一 NVIDIA InfoTok 网站。递归 tree 直接列出 `assets/infotok-header.png`、`assets/compare_length.png`、`assets/infotok-table.png` 与 `assets/1747309095480157_compare.gif`。
- **已验证的公共渲染资产**：`assets/infotok-header.png` 与 Figure 1 的流程/示例组合相符；`assets/compare_length.png` 与 Figure 3 的四行压缩率网格相符；`assets/infotok-table.png` 与 Table 1 的数值、行列和粗体布局相符；`assets/1747309095480157_compare.gif` 与 Figure 5 的棕白猫/Token Mask/Token Usage 序列相符。它们是公开渲染资产，不是论文 LaTeX 或绘图参数源，因此只能把对应视觉内容记为 `rendered_asset`，不能把字体、线宽或数据生成过程宣称为 `source_exact`。
- README 还嵌入两个 Panda-70M GIF；渲染内容为人物/户外片段，不对应本 PDF 的 Figure 2 或 Figure 6，未计入本文视觉源。`gh search code` 对 `savefig`/`matplotlib` 只命中 `cosmos_predict1/diffusion/training/utils/inference_long_video.py` 的通用 tensor 调试可视化；对 seaborn、plotly、TikZ、Figure 4 均无论文绘图源命中。仓库没有 PDF 的 `.tex`、`.tikz`、`.pgf` 或 Figure 4 的绘图脚本。
- inventory 中的 [`ZLKong/Awesome-Collection-Token-Reduction`](https://github.com/ZLKong/Awesome-Collection-Token-Reduction) 与 [`lavinal712/Awesome-Visual-Tokenizers`](https://github.com/lavinal712/Awesome-Visual-Tokenizers) 分别是主题集合仓库；`gh repo view` 的标题/description 不指向该论文视觉生成，未采用其文件。

因此本审计的 `source_acquisition.status` 为 `partial_visual_source`：Figure 1、Figure 3、Table 1 和 Figure 5 有作者仓库中的对应渲染资产；Figure 2、Figure 4、Figure 6、Table 2–6 没有经验证的绘图/LaTeX 源。

## 3. 全局视觉系统

- **字体**：PDF 正文、caption 和表格使用嵌入的 Nimbus Roman No9 L（regular/medium），数学符号来自 Computer Modern 的 CMR/CMMI/CMSY；表格主体约 6–7 pt，表头约 6–7 pt，caption 约 8.7 pt。图内 raster 标签是 Helvetica/Arial-like sans-serif 的估计，字号约 6–11 pt；Figure 4 图像内坐标和图例字号约 6–9 pt。caption 的字体家族/对象可由 `pdffonts` 与 XML 确认，图内字号只能由 200 dpi 渲染估计。
- **颜色**：Figure 4 的像素主色可从嵌入 raster 读到红 `#DB4437`（ElasticTok）、绿 `#0F9D58`（InfoTok）、蓝 `#4285F4`（InfoTok-Flex），配浅灰虚线网格；Figure 1 的主色为蓝 `#5384ED`、亮绿 `#85B737`、深绿 `#58A65D`、紫 `#634FA2`、灰 `#AEAEAE`、深蓝描边 `#112735`。Appendix mask 使用黑/白二值，usage 使用绿柱。自然视频本身的颜色不承担定量编码。
- **渲染**：`pdfimages -list` 显示所有六幅 Figure 主要由嵌入 RGB raster（Figure 4 的七个面板也是 raster）构成；表格文字和规则为 PDF 文本/线对象。全篇没有误把 raster 图当作可编辑 vector source。
- **统计表达**：Table 1–3、Table 5–6 和 Figure 4 都是点估计或确定性流程的显示，没有 seed、重复数、误差条、区间或显著性程序。Figure 4 caption 的 “significantly” 没有对应不确定性编码。图表因此适合比较方向和机制例证，不足以表达跨运行变异。

## 4. 逐对象审计

### Figure 1（p. 2，method，正文）

- **几何与类型**：双栏近页宽；上部是从 Input Video → Encoder → Embeddings → Router/Adaptive Compressor → Quantize/De-quantize → Adaptive De-compressor → Decoder 的横向回路，下部是两行各 8 帧的小型重建示例。类型为 `architecture`、`pipeline`、`conceptual_diagram`、`qualitative_grid`，复杂度 4（跨栏、多组件、两组示例）。白底、圆角 embedding/token 容器和大量留白让阅读顺序从左到右再回到 decoder。
- **绘图语法**：无 x/y 轴、网格或 conventional legend；实线黑箭头是数据流，方块/梯形是组件，立方体是 embedding/token，文本直接标注阶段。颜色语义为绿=encoder/decoder/downstream applications，紫=router，蓝=adaptive compressor/de-compressor，灰=quantize/de-quantize，浅绿=embeddings；没有不确定性、marker 或 hatching，箭头线约 1 pt（渲染估计）。
- **字体与颜色**：图内 sans-serif raster 标签约 8–12 pt，组件名 regular/medium，`N_x`、`x` 等数学字形与 caption 的 CMR/Nimbus 混合；图内主色为 `#5384ED`、`#85B737`、`#58A65D`、`#634FA2`、`#AEAEAE`、`#112735`。颜色与形状、文字双重编码，黑白打印仍可按箭头和标签理解，但组件颜色本身不完全灰度等价。
- **数据与证据关系**：图中两行示例写有 `Error: 0.0267 / Compression Rate (Measured by BPP16): 0.4004` 与 `Error: 0.0438 / ...: 0.6168`；caption 将其概括为稳定 dog 约 0.40、动态 cat-fighting 约 0.62。它是机制接口示意与方法预览，不是数据集汇总。它把引言的“信息复杂度→可变长度”连接到 §3.1 router、§3.2 compressor，并由 Appendix A 的 Figures 5–6 展开 mask 细节。
- **caption**：`Figure 1: Overall framework of InfoTok, an information-theoretic adaptive video tokenizer. An encoder maps video x into fixed-length embeddings, from which a router estimates the number of tokens N_x based on information complexity (section 3.1). An adaptive compressor encodes the embeddings to N_x tokens (section 3.2). For reconstruction, the tokens are decompressed to fixed-length embeddings and decoded back into video. InfoTok tokenizes based on video complexity: e.g., the stable dog video is compressed more (0.40) than the dynamic cat-fighting video (0.62). Illustration details can be found in Appendix A.`（约 94 词；说明 setup、encoding key、比较与附录指针；脱离正文基本自足，直接说明按复杂度分配 token，但不呈现统计主结论。）
- **优点**：把新增 router/compressor 放在既有 tokenizer 的 encoder/decoder 两侧，路径和逆路径一眼对应；颜色和组件形状形成冗余编码；示例率把抽象接口连接到具体视频复杂度。
- **缺陷**：组件标签和下方示例的字体/比例不完全统一；下方示例的数值未定义误差分母、样本选择或统计聚合；跨栏图压缩了正文页 2 的连续阅读空间；公开仓库只有渲染资产，没有可复用的 diagram source。
- **可复用范式**：用“输入→固定表征→资源路由→自适应压缩→量化→逆变换→下游/重建”的双向单图，并在同一图底部放两类复杂度对照，而不是把模块图与动机例子拆成互不相连的图。

### Table 1（p. 7，results，正文）

- **几何与结构**：跨双栏、10 列、9 个数据行、两层表头；TokenBench-256x256 和 DAVIS-256x256 各跨四个指标列。数据行按 fixed baselines、BPP16=0.81 adaptive、BPP16=0.56 adaptive 分为 3 组（每组 3 行），规则为 booktabs 风格的顶线、组间线和底线，无竖线。
- **字体与高亮**：表格主体约 6.7 pt Nimbus Roman No9 L regular；表头约 6.7 pt regular，数学上下标来自 CMR/CMSY；固定 baseline 三行使用灰色 `#7F7F7F`，各组显示最好值用粗体，未使用底色、下划线或箭头。caption 约 8.7 pt regular。
- **表头/精度/不确定性**：`Compression (BPP16 ↓)`、PSNR↑、SSIM↑、LPIPS↓、FVD↓ 明确方向和单位；BPP/PSNR 两位小数，SSIM/LPIPS 三位，FVD 整数，列内精度一致但跨指标不同。没有 mean±SD、区间、重复数或失败值。
- **数据与证据关系**：在 TokenBench 与 DAVIS 两个 256×256 分区上比较 Open-MAGVIT2-UCF、OmniTokenizer、Cosmos-DV、ElasticTok、InfoTok-Flex、InfoTok；自适应方法在 0.81/0.56 两档与 ElasticTok 对齐。表支持“同预算重建质量”和“低预算仍优于 ElasticTok”的主结果，直接承接 §4.1–4.2；没有把 downstream utility 混入表内。
- **caption**：`Table 1: Evaluation of fixed-length and adaptive tokenizers on TokenBench and DAVIS. We compare InfoTok with ElasticTok at two compression levels (0.81, 0.56) by setting our compression rates to theirs.`（约 32 词；title、setup、comparison 齐全，表头补充方向；不直接写主发现。）
- **优点**：将两数据集、四指标和两预算放在同一决策面；组间线和粗体把 baseline、同预算比较分开；`BPP16` 的方向箭头减少读者查正文的成本。
- **缺陷**：灰色 baseline 与黑色方法行在小字号下对比偏弱；无离散度导致表内差异无法区分运行噪声；0.81 与 0.56 组的“最好”是逐指标高亮而非预先定义的综合准则；公开仓库仅有 raster table asset，无生成器。
- **可复用范式**：用跨数据集的分组表固定预算，再将压缩率、失真/感知质量和方向箭头置于同一表头；按预算分块并在块内逐指标高亮，不用额外的综合分数。

### Figure 2（p. 7，results，正文）

- **几何与类型**：双栏近页宽的 4×9 图像网格（四个方法行 × 三组场景 × 每组 3 帧），垂直虚线分隔 climbing/close-up/road 场景。类型为 `qualitative_grid`、`image_montage`，复杂度 4；行标签 `Original`、`Cosmos-DV`、`ElasticTok`、`InfoTok-Flex` 直接给出比较 key。
- **绘图语法**：无轴、网格或 conventional legend；行名与每组三帧是直接标签，虚线只编码场景分块。图像内在颜色为自然视频，指标行使用黑色文字并用红色强调 ElasticTok 的 compression-rate 数字；无 marker、线型数据系列、hatching、参考线或不确定性。
- **字体与颜色**：栅格内标签/指标约 6–8 pt sans-serif bold/regular，caption 为 Nimbus Roman 约 8.7 pt；主色是自然 RGB，辅以 `#000000`、`#FFFFFF`、深蓝 `#112438` 虚线和约 `#E33E31` 红字。红色不是唯一识别依据，因为行名和数值文字提供冗余；自然图像灰度化后可读但质量色彩本身不可比较。
- **数据与证据关系**：每个场景展示 Original、Cosmos-DV、ElasticTok、InfoTok-Flex 的重建；可见指标文字给 Original/Cosmos-DV/ElasticTok 三行的 PSNR 和 BPP16（左组 28.97/1.00、27.09/0.93、27.89/0.52；中组 34.12/1.00、28.74/0.48、32.98/0.44；右组 32.85/1.00、26.85/0.43、33.08/0.40），InfoTok-Flex 行没有对应的逐格数值标签。它是 representative qualitative evidence，与 Table 1 的 aggregate PSNR/BPP16 主比较相呼应，但不能替代全数据统计。
- **caption**：`Figure 2: Reconstructions examples of video with different complexities using different tokenizers. InfoTok-Flex can achieve similar PSNR with much higher compression (compared to Cosmos-DV), and similar compression rates with better PSNR (compared to ElasticTok).`（约 34 词；setup、comparison、main finding 齐全，脱离正文可理解。）
- **优点**：场景分块和方法行使同一阅读方向，读者可同时看空间质量和压缩率；以三种内容难度支撑“按复杂度适配”的视觉直觉。
- **缺陷**：InfoTok-Flex 行缺少同位置的 PSNR/BPP16 标签，比较需要回查上方行或 Table 1；只有三组代表性场景且无抽样规则/人评；自然图像和红字混合使图例语义依赖 caption；没有公共绘图源。
- **可复用范式**：定性网格保留 Original 行、固定场景列和统一方法行，并给每个方法行同格式的质量/预算标注；若数字不适合放在每格，应在 caption 或旁侧小表补全，而不留一行空缺。

### Figure 3（p. 8，ablation，正文）

- **几何与类型**：双栏近页宽 4×9 网格（Original、Rate=0.81、Rate=0.56、Rate=0.31 四行；三个场景组，每组 3 帧），虚线分隔场景。类型为 `qualitative_grid`、`image_montage`，复杂度 4；无坐标轴、图例或数值曲线。
- **绘图语法**：`Rate=...` 是行 direct label；每个已标注行的下方有 `PSNR` 与 `Compression Rate (Measured by BPP16)`，无 marker/线型/hatching/参考线/不确定性。全部是 raster，边界和文字来自嵌入图像。
- **字体与颜色**：图内约 6–8 pt sans-serif，caption Nimbus Roman 约 8.7 pt；黑/白文字和自然视频颜色为主，场景分隔使用 `#112438` 深蓝虚线。黑白 mask/数值文字形成冗余，图像内容的颜色没有统计语义。
- **数据与证据关系**：同一视频逐步降低预算，图内可见 Original 的 PSNR/rate 为 28.24/.75、34.87/.63、33.15/.57；Rate=.81 为 27.89/.52、32.98/.44、33.08/.40；Rate=.56 为 25.86/.35、30.33/.25、26.53/.23；最低 Rate=.31 行没有同位置 PSNR/rate 标签。Figure 3 是“结构先保留、细节后消失”的预算敏感性消融，连接 §4.3 与 Figure 4 的连续 rate 曲线；它展示单视频 failure boundary，不是样本级统计。
- **caption**：`Figure 3: Reconstructions examples of video by InfoTok-Flex with different compression rates.`（约 12 词；title/setup，未说明行标签、指标或主发现，脱离正文自足性低。）
- **优点**：用固定场景和单一模型隔离压缩率变化；视觉上能看到低预算时细节消失而整体轮廓保留；公开仓库有对应 `assets/compare_length.png` 渲染资产。
- **缺陷**：最低预算行缺指标注释；只有一个视频和三个场景，无法表示跨内容异质性；caption 没有定义 `Rate` 与 BPP16 的关系；无不确定性、采样规则或生成源。
- **可复用范式**：对同一视频固定帧/场景，按从高到低预算排列，并保持行标签、质量标签和图像尺寸完全一致；把视觉退化边界作为消融的一部分而不是单独的装饰图。

### Figure 4（p. 8，results，正文）

- **几何与类型**：双栏 2×3 质量曲线加右侧纵向 NFE 柱状图，共 7 个面板（a–g），复杂度 4。每个曲线面板以 BPP16 为 x，分别画 TokenBench 的 PSNR/LPIPS/FVD 和 DAVIS 的 PSNR/LPIPS/FVD；g 为三柱 `InfoTok-Flex`、`InfoTok`、`ElasticTok`。
- **完整绘图语法**：全部为嵌入 raster；x/y 均 linear，x 有 0.4/0.6/0.8/1.0 等刻度，y 为各 metric 的 linear 数值；网格为 x+y 浅灰虚线。三条曲线使用圆 marker、红实线/绿虚线/蓝实线，曲线面板内重复放三项 legend；g 无 conventional legend，x 类别和柱顶 `1.00/1.00/11.00` 为 direct labels。无 hatching、参考线、error bar、band、ellipse 或 distribution；估计线宽约 2 pt。像素主色精确读到 `#DB4437`、`#0F9D58`、`#4285F4`，但没有源脚本。
- **数据与证据关系**：曲线用 BPP16 对应 PSNR↑、LPIPS↓、FVD↓，绿色/蓝色在较低 BPP16 通常保持更好质量；g 显示 additional NFEs/standard NFEs 为 Flex=1.00、InfoTok=1.00、ElasticTok=11.00。它把 Table 1 的两点预算扩成连续 rate–quality frontier，并把 §4.2 的搜索成本主张放到同一图；曲线仍未给重复/离散度。
- **caption**：`Figure 4: Video tokenization performance of InfoTok-Flex, InfoTok, and ElasticTok on TokenBench (a-c) and DAVIS (d-f). Quality metrics are plotted against BPP16 (bits per 16 pixels). Tokenization efficiency measured in the Number of Function Evaluations overhead (additional NFEs / standard NFEs ↓) is shown in (g). InfoTok-Flex and InfoTok achieve superior reconstruction quality with smaller BPP16 levels. Additionally, InfoTok is significantly more efficient than ElasticTok, which requires searching to meet thresholds.`（约 69 词；title、setup、encoding、comparison、main finding 齐全，caption 自足；“significantly”没有误差编码支持。）
- **优点**：六个质量面板共享 x 语义，g 面板将质量收益和推理成本放在同一对象内；颜色、圆 marker 和一条虚线共同提供部分系列区分；点位置让 rate–quality 关系比 Table 1 更直观。
- **缺陷**：每个小面板重复大 legend，侵占绘图区；红/蓝均实线且均圆 marker，灰度和色觉缺陷下区分弱；x 轴方向用向下箭头表达“低 BPP 更好”但曲线仍从低到高排列；无 uncertainty，caption 的显著性词超出显示证据；没有经验证的 plot script。
- **可复用范式**：以共享 BPP16 x 轴组织“质量 frontier + inference-overhead”面板，固定方法颜色/线型/marker；生产版应改用一次共享 legend、颜色之外的线型/marker 冗余，并在 caption 明确重复与不确定性定义。

### Table 2（p. 9，ablation，正文）

- **几何与结构**：跨双栏、10 列、6 个数据行（3 个压缩率 × 2 个 inference method）、两层表头；TokenBench 与 DAVIS 各四指标，按 BPP16=0.81/0.56/0.31 分 3 个 row group，booktabs 顶/组间/底线，无竖线。
- **字体与表头**：主体约 6.7 pt Nimbus Roman regular，表头约 6.7 pt，caption 约 8.7 pt；列名明确 `Compression (BPP16 ↓)`、`Inference Method`、PSNR↑/SSIM↑/LPIPS↓/FVD↓。BPP/PSNR 两位、SSIM/LPIPS 三位、FVD 整数；无粗体、下划线、底色或箭头高亮。
- **数据与证据关系**：InfoTok-Flex 与 exhaustive `Optimal` 在三档预算和两个数据集上逐点比较；`Optimal` 是对该 router 的严格上界，指标接近（例如 0.56 TokenBench PSNR 29.30/29.39、FVD 71/74；DAVIS PSNR 24.84/24.93、FVD 581/601）。它检验 ELBO router 接近 near-oracle 的机制主张，连接 Theorem 3.1、§4.3 和 Figure 4；不测量真实 log-likelihood 或 entropy bound。
- **caption**：`Table 2: Ablation on InfoTok versus an optimal search-based strategy to determine the token lengths. “Optimal” is a strict upper bound of our method, yet their performance is extremely close.`（约 30 词；title、setup、upper-bound 解释和 main finding 齐全，自足。）
- **优点**：把 oracle/搜索基线和三个预算放在一个严格对齐的表中；caption 解释 `Optimal` 的证据地位，避免把上界误读成可部署模型。
- **缺陷**：没有说明 exhaustive search 的运行成本、可行 token 网格以外的误差或重复统计；“接近”没有预先定义距离；低预算行的指标下降与 router 误差混在同一表中；没有源文件。
- **可复用范式**：在同一表中同时放可部署路由与严格 oracle，并显式写出 oracle 的上界地位；预算作为 row group，跨数据集列保持完全相同。

### Table 3（p. 9，ablation，正文）

- **几何与结构**：双栏宽度的左右并置复合表。左子表为 5 列（Compressor、PSNR、SSIM、LPIPS、FVD）×3 行；右子表为 4 列（Architecture、Adaptive Mechanism、PSNR、FVD）×4 行。主表记录最大 4 行、复合 9 列语义、两侧各 1 层表头；顶/底线和少量组间规则为 partial-grid/booktabs 混合的极简规则。左侧 R2L/Jump/Ours，右侧 Cosmos 两行及 ElasticTok Backbone/Vision Transformer 两行。
- **字体/高亮**：主体约 6.7 pt Nimbus Roman，表头约 6.7 pt；`Ours` 和 ELBO 行的关键数值用粗体，未使用底色/下划线；左右列的数字精度按指标一致（PSNR 两位、SSIM/LPIPS 三位、FVD 整数）。
- **数据与证据关系**：左侧固定 TokenBench 平均 BPP16=0.56，比较 R2L、spatial Jump 与 ELBO-mask compressor；Ours 的 PSNR/SSIM/FVD 为 29.30/0.857/71，但 Jump 的 LPIPS 0.173 略优于 Ours 0.179。右侧在 Cosmos 和纯 ViT/ElasticTok backbone 上比较 Uniform (ElasticTok) 与 ELBO (InfoTok)，同时改变机制和部分 architecture。它把 §3.2 的 compressor 设计和整套 adaptive mechanism 消融连接到 Table 1 主结果。
- **caption**：`Table 3: Ablation results on TokenBench with an average BPP16 = 0.56. (Left) Ablation on adaptive compressors. (Right) Ablation on different variants of adaptive mechanisms across architectures.`（约 27 词；title、预算、左右表语义齐全；不直接写发现，但可独立读表。）
- **优点**：一页内按“组件→整体机制/架构”递进，左侧提供单变量 compressor 对照，右侧补充跨 architecture 适用性；粗体只强化显示的最佳 PSNR/SSIM/FVD。
- **缺陷**：右侧同时改变 architecture 与 mechanism，不能当作单变量机制估计；复合表的左右表头和行数不对称；Jump 的 LPIPS 反例使“全面优于”不成立；没有不确定性或源码。
- **可复用范式**：把组件消融与整套机制消融并置，但在 caption/正文明确哪些是同 backbone 对照、哪些同时改变架构；保留逐指标结果以暴露 trade-off。

### Figure 5（p. 15，appendix A，附录）

- **几何与类型**：整页近页宽 raster，6 行时间帧（0、60、120、180、240、258）×4 列（Original、InfoTok、Token Mask、Token Usage）。类型为 `qualitative_grid`、`image_montage`、`bar`，复杂度 5；行首黑底 Frame label，最右列为每帧单个绿色 usage bar。
- **绘图语法**：无 x/y 轴、网格或 conventional legend；列标题和 Frame 号是 direct labels。Token Mask 以白=保留、黑=mask 的二值编码，usage bar 以高度/绿色填充表达保留比例并以文字标值；无误差/参考线/hatching/marker，bar 线宽不适用。全部是 raster。
- **字体与颜色**：图内深色条上的 sans-serif 白字约 7–9 pt，Frame label medium/bold；caption 为 Nimbus Roman 约 8.7 pt。像素主色为 `#000000`、`#1C1C1C`、`#FFFFFF`、usage 绿 `#31A752`，自然视频保留 RGB；黑白 mask、百分比文字和列名对绿色形成冗余，灰度打印仍能读数。
- **数据与证据关系**：狗视频各帧 usage 为 38%、35%、60%、41%、29%、30%；caption 把静止地面、镜头转向另一只狗、再次稳定与 mask 地面区域串成“按信息复杂度分配 token”的机制例。它扩展 Figure 1 的简化示例，连接 §3.2 的 token mask 与 Appendix A 说明；仍是一个定性序列，不是总体分布。
- **caption**：`Figure 5: The video starts with a brown dog sleeping on the ground. The video is stable and more than 60% of tokens are masked without harming the reproduction quality. Later on, the camera shifts toward another white dog, during which the token length increases to 60% to encode new information. As the camera stabilizes again and focuses on the face of the white dog, the token length reduces back to 30%, and much of the ground area is masked out (because they can be easily inferred from surrounding areas).`（约 90 词；setup、encoding key、main finding 齐全，自足。）
- **优点**：同一时序中同时给原图、重建、mask 与数值 usage，能直接看到空间 mask 与视频运动的对应；百分比标签使绿色柱无需标尺也可复核；仓库有对应狗序列的 `1747309095480157_compare.gif`。
- **缺陷**：只有 6 个抽帧且无选择规则；“不损害质量”没有同步 PSNR/感知指标；黑白 mask 的像素含义需要读段首文字；超宽整页图在 PDF 缩放下细节较难读；GIF 是伴随渲染资产而非生成参数源。
- **可复用范式**：对时间序列固定抽帧，按 Original→reconstruction→mask→usage 四列组织；用百分比文字配单色 bar，避免把空间 mask 和定量率混在同一色标里。

### Figure 6（p. 16，appendix A，附录）

- **几何与类型**：整页 raster，4 行时间帧（0、20、40、60）×4 列 Original/InfoTok/Token Mask/Token Usage，类型为 `qualitative_grid`、`image_montage`、`bar`，复杂度 4。场景是动态工作空间/手部任务，mask 主要保留中心和运动边缘，外围变黑。
- **绘图语法**：无轴、网格、legend 或不确定性；列名和 Frame 号 direct label；白/黑 mask 编码保留/删除，右侧绿色单柱及百分比为每帧 usage。无 marker、线型、hatching、参考线，raster 渲染。
- **字体与颜色**：图内约 7–9 pt sans-serif 白字，caption Nimbus Roman 约 8.7 pt；`#000000`/`#1C1C1C`/`#FFFFFF`/`#31A752` 与自然视频 RGB。列名、黑白 mask 和数值文字提供冗余，灰度下仍可判读。
- **数据与证据关系**：usage 依次为 65%、50%、29%、17%；caption 将相机/人物运动变缓、手部任务聚焦、外围背景可由前帧推断连接到 token usage 下降。它是 Figure 5 的另一场景复制，支撑机制的 qualitative generality，但不提供跨视频统计或下游任务证据；本仓库资产中没有与该工作空间静态组合严格匹配的公开源。
- **caption**：`Figure 6: The video begins with a wide shot of a workspace. The camera is highly dynamic as the person moves, requiring a higher token usage of 65% to capture the rapidly changing environment. As the person stabilizes their position and focuses their hands on the task at the center of the frame, the token usage progressively drops to 50% and then 29%. By the end of the sequence, as the background remains static and the movements become more predictable, the token usage further reduces to 17%. Large portions of the peripheral workshop area are masked out, as the model recognizes they contain redundant information that can be inferred from previous frames.`（约 112 词；setup、encoding、main finding 齐全，自足。）
- **优点**：比 Figure 5 更明确地给出动态→稳定的 token usage 轨迹，并以 mask 的外围区域提供空间解释；四帧版面密度比六帧版更容易逐行读。
- **缺陷**：仍是单视频代表性例，没有运动复杂度标尺、误差或抽样方案；右栏绿色 bar 没有 y 轴，读者只能依赖百分比文字；没有验证过的 Figure 6 源文件。
- **可复用范式**：复制 Figure 5 的四列接口到第二种内容场景，用不同时间点检验同一机制，并明确把定性例证与 aggregate benchmark 分开。

### Table 4（p. 22，appendix C，附录）

- **几何与结构**：居中、近双栏宽度的 3 列表，17 个数据行（不含 4 个粗体 section group 行），1 层字段表头，4 个 row group：Adaptive Compressor/De-compressor、Quantizer、Based Tokenizer: Cosmos、Total parameter size。规则为 booktabs 顶/组间/底线，无竖线；InfoTok-Flex 未提供的配置以 `-` 表示。
- **字体/高亮/精度**：body/header 约 8.7 pt Nimbus Roman No9 L regular/medium；section group 与表头粗体；数学 β、2^16 等用 CMMI/CMSY/CMR；无底色、下划线或 best/second-best。数值为整数、列表、百分比和模型名混合，不能指定单一 decimal precision；没有不确定性。
- **表头/数据与证据关系**：三列为 Hyperparameter、InfoTok-β、InfoTok-Flex。表中给出 compressor 深度 8、attention head 32、hidden 256/512、2D RoPE、FSQ embedding 6、codebook 64000 (2^16)、Cosmos 3D Causal CNN、(4,8,8) 压缩和 123M 总参数。它为 §3.2/§4.1 的模型复现接口提供 appendix detail，连接 Figure 1 的 compressor/decompressor 模块，但不报告训练结果或方差。
- **caption**：`Table 4: Architecture Configuration.`（约 4 词；仅 title，表头和正文才能补足语境，非自足，未写主发现。）
- **优点**：按模块分组，把新增 adaptive 部分与复用的 Cosmos base tokenizer 分开；缺失的 Flex 配置显式写 `-`，避免伪造参数。
- **缺陷**：section group 行被计入视觉节奏但没有单独的语义列；`InfoTok-β` 和 `InfoTok-Flex` 的 `-` 很多，未解释哪些参数共享；caption 没说明单位、缺失值或总参数分解；没有源码生成表。
- **可复用范式**：复现型架构表用 section group + 共享列，显式展示新增参数比例和 base tokenizer 组成；对未实例化配置用 em dash，并在 caption 解释。

### Table 5（p. 23，appendix D，附录）

- **几何与结构**：与 Table 6 左右并置；本子表单栏宽、5 列、4 个数据行、1 层表头、2 个 resolution row group（256×256 与 360p 三种 aspect ratio），booktabs 顶/底线，无竖线。列为 Model、Resolution、BPP16、PSNR、FVD。
- **字体/精度/不确定性**：主体和表头约 6 pt Nimbus Roman（XML 的 9 px 字号对应约 6 pt），表头 medium/bold；BPP16/PSNR 两位小数，FVD 整数，跨列为 mixed precision；无高亮、区间或失败值。
- **数据与证据关系**：Cosmos Arch 与 Cosmos Arch + InfoTok 在 256×256 和 360p (1:1, 4:3, 16:9) 各占一对，低 BPP16=0.56 对照 1.00；360p 对的 PSNR/FVD 为 30.55/56 对 31.13/27。它回应 §4.1/Appendix D 的 resolution generalization 主张，但只是同一 TokenBench 家族上的点估计，不证明等质量。
- **caption**：`Table 5: Comparison of Cosmos Arch with and without InfoTok across resolutions on TokenBench.`（约 14 词；title/setup，表头足以解释列，但不直接写结论。）
- **优点**：用相同 architecture 和两种 resolution/宽高比呈现适用性边界；把 BPP16 与质量列放在同一小表中，便于看 trade-off。
- **缺陷**：360p 行把三个 aspect ratio 合并在一个单元，无法审查各宽高比的差异；没有 SSIM/LPIPS 或方差；caption 没有说明低预算不是等质量比较；无公共表生成源。
- **可复用范式**：附录 robustness 表用同 backbone 的 with/without 行配 resolution 与资源率，让泛化和质量代价同时可见；对合并 aspect ratio 应增加逐比行或注明聚合方式。

### Table 6（p. 23，appendix D，附录）

- **几何与结构**：与 Table 5 右侧并置、单栏宽、3 列、4 个数据行、1 层表头、无 row group，booktabs 顶/底线。列为 Method、NFEs、Inference Latency per video。
- **字体/精度/不确定性**：body/header 约 6 pt Nimbus Roman，表头 medium/bold；NFEs 为整数，latency 为两位小数加 `s`，跨列 mixed precision；无 bold、颜色、区间或重复统计。
- **数据与证据关系**：Cosmos=1/0.61 s，Cosmos + InfoTok mechanism=2/1.23 s，Cosmos + ElasticTok mechanism=12/13.45 s，ElasticTok=12/42.75 s。条件是单 RTX A5000、33 帧、256×256、BPP16=0.56（正文 Appendix D 文字说明），用于量化 Figure 4g 的 NFE efficiency 以及搜索机制成本，不支持跨硬件/批大小泛化。
- **caption**：`Table 6: Inference latency comparison across different methods.`（约 8 词；仅 title，不说明 GPU、clip shape、BPP16 或 latency 单位，非自足。）
- **优点**：把 mechanism-only 与 full ElasticTok 分开，避免只给一个模糊 baseline；NFEs 与 wall-clock latency 并列，能区分算法次数和实际时间。
- **缺陷**：单硬件单 clip 的一次 point measurement，没有重复/分位数；caption 未写条件和单位；Cosmos + ElasticTok mechanism 与 full ElasticTok 的差异可能包含额外 pipeline 开销；没有源文件。
- **可复用范式**：延迟表同时报告 NFE 和 wall-clock，并列出 mechanism-only 与 full pipeline；caption 应固定硬件、输入形状、预算、重复统计和单位。

## 5. 跨对象系统判断

- **视觉叙事**：Figure 1 把 source-coding 机制画成路由/压缩接口；Table 1 与 Figure 2 收回同预算 aggregate/qualitative 结果；Figure 4 扩展到连续 rate–quality 与 NFE；Table 2–3 做 oracle、compressor 和整体 mechanism 消融；Figures 5–6 把 mask/usage 机制落到时序例；Tables 4–6 把架构、分辨率和延迟放入附录。主文→附录链条完整，但证明和复现实验条件依赖跨页跳读。
- **caption 系统**：Figure captions 多为“对象标题 + 设置 + 比较/机制 + 结论”，Figure 3 和 Tables 4/6 最短；Table 1–3 明确预算/分组，Table 4/6 的 caption 没有单位或条件。Figure 4 使用 “significantly” 而未配 uncertainty，属于 caption–encoding 不一致。
- **表头系统**：主表统一用箭头表达 metric 方向、数据集跨列和 BPP16 预算；消融表复用同一四指标词汇；附录表转为架构/分辨率/NFE 语义。表头字体与规则一致，但小表字号极小，Table 3 左右复合结构需要正文解释。
- **method–result–ablation**：Figure 1 → Table 1/Figure 2 → Figure 4 → Table 2/3 → Figures 5/6 的顺序逐步从接口、收益、效率、机制到定性边界；Table 3 的 architecture 右表同时改变 backbone 和 mechanism，需把“泛化”与“单变量因果”区分。
- **main–appendix**：正文保留最重要 pipeline、主表、rate curve、router/compressor 消融；Appendix A 详述 mask，C 给配置，D 给 resolution/latency。Figure 1 caption 明确指向 Appendix A，但正文结果仍依赖附录条件解释。
- **typography consistency**：PDF 文本对象统一 Nimbus Roman/Computer Modern 家族；raster 内部使用 sans-serif 标签，字号和字重的跨图一致性只能估计，Table 5/6 的 6 pt 级别明显小于主 caption。
- **color consistency**：Figure 1 使用模块色，Figure 4 固定红/绿/蓝方法色，Appendix usage 固定绿色；Figure 2/3 的红色只强调部分数字、mask 使用黑白，方法颜色并未贯穿所有对象，因此跨图跟踪方法时主要依赖行/图例文本而非颜色。

## 6. 最终判断

- **最可复用模式**：
  1. 把自适应资源分配画成正向/逆向闭环，并在同图给出复杂度对照。
  2. 用同一 BPP16 预算在跨数据集表、定性网格和连续 rate–quality 曲线中重复主比较。
  3. 以 oracle router、组件 compressor、整体 mechanism 三层消融分别回答“接近最优”“哪一部件有效”“是否跨架构”。
  4. 用 Original/重建/mask/usage 四列时序网格把定量路由规则与空间证据对齐。
- **最高价值对象**：Figure 4（把质量 frontier 与 NFE 成本合并）、Table 1（同预算跨数据集决策面）、Table 2（严格 oracle 上界）、Figure 5（机制 mask 与 token usage 的可视对应）。
- **主要失败模式**：公开视觉源只有渲染资产而无 plot/LaTeX 参数；Figure 2/3 的最后一行缺逐格质量标签；Figure 4 重复 legend、红蓝线型冗余不足；Figures 5–6 和 Table 5–6 是代表性/单硬件点测量却没有不确定性；Table 4/6 caption 没有完整条件和单位。
- **一句话视觉策略**：InfoTok 用“复杂度路由闭环 → 同预算质量表/曲线 → oracle 与组件消融 → 时序 mask 例证 → 附录配置与延迟”把信息论机制转成可读的质量、效率和复现证据，但仍以 raster 与代表性点估计为主。

# InfoTok 深读备忘

- **论文** — InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression
- **ID / 来源**：`iclr-2026-3c7fde53bdb5`；ICLR 2026 Oral；实际读取官方 proceedings PDF（物理页 1–23）。
- **版面边界**：正文为物理页 1–10；`References` 为页 11–13；同一 PDF 内的 `Supplementary Material` 为页 14–23。正文为双栏；Figure 1、Table 1、Figures 3–4 与 Table 2 跨栏或占据大面积，压缩了相邻段落的连续阅读空间。附录第 14 页是目录，第 15–16 页为整页定性图，第 17–21 页主要是证明。

## 1. 单一主线与页级结构

论文把「视频信息密度不均」转写为 source coding 问题：固定长度或训练时与样本无关的长度采样都不能按样本概率分配码长；因而以负对数似然近似为依据，把每个视频的长度交给 ELBO router，再由 transformer adaptive compressor 在视频内部保留信息量较高的 token。理论给出理想条件下的码长界，实验在视频重建、同预算比较、oracle router 消融和推理次数上回收该链条。[PDF p. 2, §1; “content-dependent compression”] [PDF p. 5, §3.1; “Nx should be proportional”]

| 物理页 | 内容与语义模块 | 版面观察 |
|---|---|---|
| 1 | 题目、Abstract、Introduction 开始 | 摘要居中窄栏；引言双栏起笔。 |
| 2 | Figure 1；Introduction 续 | Figure 1 横跨双栏，承担方法预览。 |
| 3 | Introduction 收束；§2.1、§2.2、Theorem 2.1 | 贡献列表后立即进入形式化定义。 |
| 4 | §2.2、Algorithm 1、§2.3、Theorem 2.2 | 算法与解释并排，定理位于页底。 |
| 5 | §2.3 收束；§3.1、Eqs. (3)–(4)、Theorem 3.1 | 从反例/下界转为可训练 router。 |
| 6 | §3.1 Flex、§3.2、§4/§4.1 开始 | 方法结束即交代实验范围与裁剪条件。 |
| 7 | Table 1、Figure 2、§4.1 | 主比较表和定性重建例同页。 |
| 8 | Figure 3、Figure 4、§4.2 | 结果曲线与 NFE 柱状图先于文字解释。 |
| 9 | Table 2、Table 3、§4.3、§5 开始 | router、compressor、整体机制消融同页。 |
| 10 | §5 续；§6 Discussions & Limitations；§7 Conclusion | related work 后置；限制紧接结论前。 |
| 11–13 | Ethics、Reproducibility、References | 没有 acknowledgements。 |
| 14–23 | Supplementary Material | A 定性例、B 证明、C 细节、D 补充实验、E LLM 使用说明。 |

### 相对篇幅（逐页人工估计）

以正文叙述性文字约 5,344 词为分母，排除公式、表格单元格、参考文献和大部分图注：Abstract 152（2.8%）、Introduction 775（14.5%）、Related Work 333（6.2%）、Method 1,530（28.6%）、Theory 430（8.1%）、Experimental Design 655（12.3%）、Results 440（8.2%）、Ablation 540（10.1%）、Conclusion 99（1.9%）、Limitations 390（7.3%）。补充材料约 3,406 个抽取词、10 个物理页，页数与正文相同；三页参考文献与 ethics/reproducibility 归为其他内容。由于论文把定理陈述嵌在方法段内，Method 与 Theory 是按语义切分而非按连续页面切分。

## 2. 摘要：逐句功能与承诺

| # | 词数 | 功能 | 句子及作用 |
|---|---:|---|---|
| 1 | 13 | object_scope | 将离散视频 tokenization 定位为长视频处理的基础。 |
| 2 | 32 | problem_gap | 固定压缩率面对可变信息密度，会冗余或丢失信息。 |
| 3 | 17 | core_idea | 从 Shannon 信息论引出 InfoTok。 |
| 4 | 27 | theory + method | 承诺证明 data-agnostic training 的次优性，并给出 ELBO algorithm。 |
| 5 | 13 | method | 给出 transformer-based adaptive compressor。 |
| 6 | 26 | quantitative_result + qualitative_result | 承诺 SOTA、20% token 节省与 2.3× compression rate。 |
| 7 | 24 | qualitative_result + impact_claim | 将按信息丰富度分配 token 上升为未来研究启发。 |

功能顺序是「必要性 → 失败机制 → 理论框架 → 实现 → 数字结果 → 影响」。最强的可检验承诺先是理论（第 4 句），后是数字（第 6 句）；摘要未给出 limitation。第 6 句的 `20%` 与 `2.3×` 没有说明数据集、指标或比较基线，正文才将其拆为 Cosmos/ElasticTok 与不同 BPP16 设置。[PDF p. 1, Abstract; “saving 20% tokens”]

## 3. 引言的论证推进

1. **context**：视觉 foundation model 与长视频把 token 数推到百万级，提出可扩展表示的压力。[PDF p. 1, §1; “millions of tokens”]
2. **context / setup**：用 encoder–quantizer–decoder 和重建损失解释 tokenizer 本质上也是 compressor。[PDF p. 1, §1; “tokenizers are essentially compressors”]
3. **failure_of_prior_work**：把固定率和 ElasticTok 式启发式 flexible tokenization 放在同一问题下，前者对所有视频同率，后者训练 data-agnostic、推理需要 trial-and-error 搜索。[PDF p. 2, §1; “identical compression rate”]
4. **problem**：用单独的斜体问题句锁定「理论理想 tokenizer 如何定义与训练」。[PDF p. 2, §1; “theoretically ideal discrete video tokenizer”]
5. **theory_preview**：以 source coding 把所需长度接到内容频率，预告 fixed 与 data-agnostic adaptive 的预期长度会偏离最优。[PDF p. 2, §1; “near-optimal compression rate”]
6. **method_preview**：router 用 ELBO 指定长度，adaptive compressor 处理可变长度，并由 Figure 1 给出 pipeline。[PDF p. 2, §1; “ELBO of the negative log-likelihood”]
7. **result_preview**：给出约 50% token、2.3× rate 和 11× NFE 的更强数字预告。[PDF p. 3, §1; “save approximately 50% tokens”]
8. **contribution_list**：三个 bullet 分别对应 bias theorem、InfoTok 组件与实证优越性；与摘要重复核心结论，但将理论、系统和证据分开。前两个是可证伪的，第三个未在列表中给数字或边界。[PDF p. 3, §1; “main contributions”]

链条为 `context → compression setup → fixed/heuristic failure → ideal-question → source-coding insight → router+compressor → measured payoff → contributions`。引言的结果预告比摘要更具体，但把「50%」与摘要的「20%」放在不同比较语境，读者需要到 Table 1/4 区分。

## 4. 相关工作

相关工作是独立的 §5，后置在全部主实验和消融之后，占正文约 6.2%。它有两个引用簇：

- **Discrete Tokenization**：VQ-VAE/VQGAN、FSQ/LFQ、TiTok/FlowMo/SelfTok，再到 OmniTokenizer、Open-MAGVIT2、Cosmos；比较维度是量化方式、1D 表示、diffusion decoder 与 image/video 域。[PDF pp. 9–10, §5; “Discrete Tokenization”]
- **Adaptive Representation**：Nested Dropout、Matryoshka、CAT、ALIT、One-D-Piece、ElasticTok、FlexTok；比较维度是连续/离散 token、图像/视频，以及随机 masking 的启发式训练。最后一句用「objective functions are biased by definition」创建 InfoTok 的缺口。[PDF p. 10, §5; “random masking”]

它主要采用 taxonomy 加 nearest-neighbor contrast，而非逐篇方法复述。ElasticTok 不只在此处定位：引言将其作为 heuristic 反例，§4 将其作为同预算和 NFE baseline，§4.3 作为 router/compressor 对照，故引用在后文继续承担论证作用。[PDF p. 2, §1; “trial-and-error length selection”] [PDF p. 9, §4.3; “Uniform (ElasticTok)”]

## 5. 方法与信息论机制

### 5.1 形式化对象与组件

- **输入/输出**：视频 `x ∈ {0,…,255}^{T×H×W×3}`；fixed tokenizer 以 `E_φ` 得连续 latent、`Q` 得离散 `z`、`D_θ` 重建 `x̂`。Eq. (1) 是 fixed-tokenizer reconstruction NLL，VAE 假设下可转为 pixel-space MSE。[PDF p. 3, §2.1; “Lrecon(T)”]
- **目标问题**：fixed `N=c·THW` 对给定长度与分辨率不随样本变；而样本时空复杂度与频率不均。Theorem 2.1 重述 source-coding 下 `E[Nx]` 的熵下界，并给出 adaptive code 可在一 token 内逼近该下界。[PDF p. 3, §2.2; “HC(D) + 1”]
- **adaptive tokenizer**：在既有 `T` 上添加 router `r(Nx|x)` 与 compressor `Mψ`；compressor 将 `h` 变成 `Nx` 长的 `h′`，量化/反量化后由 inverse compressor 恢复 fixed-length latent。Algorithm 1 将这一训练流水线写成 11 行；循环不变量是同一 `Nx` 同时供压缩与解压使用，最终优化 Eq. (2) 的 adaptive reconstruction loss。[PDF p. 4, §2.2; “Adaptive Tokenizer Training”]
- **反例机制**：对 uniform router，模型必须在不同信息级别同时重建，但 loss 不奖励更短的期望长度；Theorem 2.2 构造数据分布，使最优训练后的 oracle length 仍可比 entropy length 大任意常数倍。四样本 `{2^-1,2^-2,2^-3,2^-3}` 例把最优码长 `1,2,3,3` 与均为 2 的结果并列。[PDF pp. 4–5, §2.3; “could be arbitrarily large”]

### 5.2 ELBO router 与 compressor

1. **长度规则**：由于理想长度为 `-log p(x)` 而真似然不可算，Eq. (3) 用 `ELBO(x)` 作下界近似；Eq. (4) 以 `β·ELBO(x)/E[ELBO(x)]` 的 delta router 指定 `Nx`。两者通常为负，因此较负的 ELBO 对应较长 token 序列。`β` 是每 token 承载信息量/平均预算的控制量。[PDF p. 5, §3.1; “ELBO(x) ≤ log p(x)”]
2. **理论保证**：Theorem 3.1 在 `β ≥ -E[ELBO(x)]` 且 tokenizer 达到 reconstruction-loss 全局最小的条件下，给出 `E[Nx] ≤ H_C(D)+β-E[-log p(x)]`。它保证的是条件式码长上界，不是对实际 benchmark 或 true likelihood 的直接测量。[PDF p. 5, §3.1; “if the tokenizer manages to minimize”]
3. **Flex**：InfoTok-Flex 在训练时从多个 `β` 中采样，让一个 compressor 覆盖不同预算；实践中以 reconstruction error 代替完整 ELBO，理由是 KL term 被称为与重建误差近似成比例，而非在本文数据上做了校准检验。[PDF p. 6, §3.1; “approximately proportional”]
4. **视频内 token 选择**：先保留 per-token log-likelihood 最低（信息量最高）的 `Nx` 个位置；mask 随 `z` 存储，作者报告约 5% token-length overhead。end-to-end loss 让 transformer 将被 mask 的信息迁到保留位置。[PDF p. 6, §3.2; “minimal overhead of approximately 5%”]
5. **实例化**：复用 Cosmos 的 3D-CNN encoder/decoder；新增 transformer compressor/decompressor。主文称八层、block-causal attention 与 FSQ，附录给出 123M 总参数、18M（14.6%）adaptive 模块、2D RoPE 等配置。[PDF p. 7, §4.1; “eight-layer transformer”] [PDF p. 22, Table 4; “Total parameter size”]

方法推进可概括为：`setup_notation → source-coding derive → define router/compressor → contrast uniform router → ELBO surrogate → theorem guarantee → Flex instantiation → likelihood-mask mechanism → experiment connection`。

### 5.3 定理和证明的证据边界

| 项目 | 假设与结论 | 证明/作用 | 与实证的对应 |
|---|---|---|---|
| Theorem 2.1 | 完全重建、codebook size `C`；码长期望不小于 `H_C(D)`，并存在 `<H_C(D)+1` 的 adaptive code。 | 主文是 Shannon theorem 的 restatement，没有本文证明；是因果链的理想基线。 | 不直接估计 `p(x)` 或 entropy；只启发 router。 |
| Theorem 2.2 | uniform `r(·|x)`、足够大的 `N`、最小化 Eq. (2)；存在分布使 oracle 期望长度 ≥ `κH_C(D)`。 | Appendix B.1（物理页 17–21）把 generate-then-mask tokenizer 化为 C-ary tree，再以 lifting argument 构造反证。 | Table 1/3 将 ElasticTok 当实用 uniform-router 对照，但不测量 theorem 的构造分布或比值。 |
| Theorem 3.1 | Eq. (4) router、`β ≥ -E[ELBO]`、达到全局 reconstruction 最小。 | Appendix B.2（物理页 21）用 `ELBO≤log p(x)` 和 Huffman tree 写出上界；属于条件 guarantee。 | Table 2 对比 exhaustive `Optimal` router，是近似机制检查，但不是对 true bound 的实证验证。 |

主文可见 display 公式块估计为 9 个，其中编号公式为 (1)–(4) 共 4 个；附录证明再有约 18 个 display 公式块，编号 Eq. (5) 只有 1 个。证明不是装饰：B.1 支撑「uniform bias」，B.2 支撑「near-optimal」；但两个正式界的关键条件（完全/最优重建、可用 ELBO gap）未由结果部分逐一验证。[PDF p. 21, §B.2; “Hoffman tree can encode”]

## 6. 实验设计与复现粒度

- **目标与顺序**：§4 先设定重建 benchmark、度量、base tokenizer、baseline 和预算对齐；§4.2 给主比较与 NFE；§4.3 依次检验 router、compressor、整套 mechanism、预算变化。该顺序与引言的系统/效率主张相配，但没有预注册式的 research-question 或 hypothesis 列表。[PDF pp. 6–9, §4; “Experimental Settings”]
- **数据**：TokenBench 是 500 个高分辨率长视频，来源含 BDD100K、EgoExo-4D、BridgeData V2、Panda-70M；DAVIS 使用 Test-Dev 2019 的 30 sequences。[PDF pp. 22–23, §C.3; “500 high-resolution”]
- **可比性控制**：为匹配仅接受 square 256px 的 ElasticTok，两个数据集只取 256px partition 并随机裁剪为正方形；作者明确说这使 baseline result 不能与 ElasticTok 原论文直接比较。此控制解决本文内部的输入形状一致性，但不等于外部复现对齐。[PDF p. 6, §4.1; “not directly comparable”]
- **指标与分母**：PSNR、SSIM、LPIPS、FVD 评估重建；BPP16 是每 16 pixels 的 bits，公式使用 token 数、视频 `THW` 和 codebook size。论文报告 dataset-level point estimate；页内没有 seed、重复次数、variance/error bar、confidence interval、hypothesis test、multiple-comparison 或 bootstrap 说明。[PDF p. 7, §4.1; “four metrics”]
- **baseline**：fixed 为 Open-MAGVIT2、OmniTokenizer、Cosmos；adaptive 为 ElasticTok。ElasticTok 以 loss threshold 而非平均压缩率控制，因此作者以相同 BPP16 对齐。[PDF p. 7, §4.1; “align our methods”]
- **训练与实现**：Cosmos training data、256px resized videos；AdamW，`1e-4→1e-5` cosine decay，batch size 1、33-frame clips、`2e5` steps、32 H100（4 nodes）、每模型约四天。附录还给 EMA ELBO、最小长度 `Nmax/16`、Table 4 配置及 clip-wise inference。[PDF pp. 21–22, §C; “32 H100 GPUs”]
- **可复现来源**：主文把完整设置指向 §4.1/Appendix C，并称匿名代码在 supplementary material；本次已验证 PDF 内没有可执行代码本体。[PDF p. 11, Reproducibility Statement; “anonymous code”]

## 7. 结果、统计与图表

### 主结果

| 主张 | 证据与数值 | 比较/统计处理 | 不利或替代解释 |
|---|---|---|---|
| 同 BPP16 下优于 ElasticTok | Table 1 在 0.81：InfoTok vs ElasticTok，TokenBench PSNR `30.08 vs 28.26`、FVD `49 vs 141`；DAVIS PSNR `25.79 vs 24.69`、FVD `408 vs 754`。 | 两数据集的 point estimate；无 seed/误差表达。 | 这是重建质量而非 downstream utility。 |
| 低预算仍保留较高质量 | Table 1 在 0.56：InfoTok TokenBench `29.27/0.854/0.176/70`，ElasticTok `27.34/0.813/0.276/194`（PSNR/SSIM/LPIPS/FVD）；DAVIS 为 `24.52/0.738/0.277/540` vs `23.76/0.714/0.356/930`。 | 相同 BPP16 的跨模型比较。 | 与 Cosmos 的 1.00 BPP16 相比，低 BPP 的 InfoTok 不是所有指标都相同或更好，故「without loss」依赖具体比较对象/指标。 |
| 可用更低率取得近似质量，并少做搜索 | Figure 4 绘制 BPP16–PSNR/LPIPS/FVD 曲线；作者举例相近质量时 2.3× rate，NFE overhead 的 ElasticTok 柱为 `11.06`，InfoTok/Flex 均 `1.00`。 | 曲线没有 point count、error band 或 test；NFE 是确定性流程成本。 | 2.3× 是曲线例示，非每个数据集/指标的普遍比值。 |
| 视觉质量随预算退化 | Figures 2–3 给原图/重建例；作者称低 token 时保留 overall structure、失去 fine detail。 | 代表性图像，无抽样规则或人类评测。 | 不能由少量帧判断全部视频/语义任务。 |
| 分辨率与延迟补充结果 | Table 5：360p 不同 aspect ratio 下，Cosmos+InfoTok at 0.56 BPP16 为 PSNR `30.55`、FVD `56`，full Cosmos at 1.00 为 `31.13`、`27`。Table 6：33×256² 单 RTX A5000，InfoTok mechanism `2` NFE、`1.23s`；ElasticTok mechanism `12`、`13.45s`，full ElasticTok `42.75s`。 | 单一硬件/单一 clip shape 的 point measurement。 | Table 5 支持不同 resolution 下仍可运行的压缩趋势，不证明等质量；延迟的 hardware generality 未测试。 |

所有主表注释自足性中等：Table 1 写明指标方向、数据集与 BPP16；Table 2 写明 `Optimal` 是 strict upper bound；Table 3 把 compressor 与 architecture 消融并排。Figures 3–4 的 caption 说明任务、坐标和 NFE 分母，未说明曲线是否含重复实验或置信表达。[PDF p. 8, Figure 4; “additional NFEs / standard NFEs”]

### 消融

消融主体约一页正文，含 Table 2、Table 3 与关联的 Figure 3：

1. **router / oracle**：对每视频枚举 `BPP16∈{1/16,…,1}`，再在全数据上求约束平均率的 optimal strategy。0.56 时 InfoTok-Flex/Optimal 的 TokenBench PSNR `29.30/29.39`、FVD `71/74`，DAVIS `24.84/24.93`、FVD `581/601`；这支持 ELBO routing 接近该 oracle，但并未测到 entropy bound。[PDF p. 9, Table 2; “strict upper bound”]
2. **compressor**：同为 TokenBench 0.56 BPP16，R2L/Jump/Ours 的 PSNR 为 `27.43/28.07/29.30`，FVD 为 `137/84/71`。Jump 的 LPIPS `0.173` 略低于 Ours 的 `0.179`，故「better reconstruction quality」不是四个指标的逐项支配。[PDF p. 9, Table 3; “Ablation on adaptive compressors”]
3. **整套 mechanism 与架构**：Cosmos 上 uniform/ELBO 为 PSNR `27.35/29.30`、FVD `152/71`；ElasticTok backbone uniform 为 `27.21/198`，Vision Transformer+ELBO 为 `28.64/114`。该设计改变了 adaptive mechanism，也改变了后一个 backbone，因此后组更适合作为跨架构适用性证据，而非严格单变量机制估计。[PDF p. 9, Table 3; “different variants”]
4. **预算敏感性**：Figure 3 在 `0.81, 0.56, 0.31` BPP16 展示同一视频；作者解释结构先保留、细节后消失。这是定性失败/退化边界，不是样本异质性统计。[PDF p. 9, §4.3; “fine-grained details becoming invisible”]

## 8. 限制、负面信息与呈现策略

### 作者明确的限制

- **额外计算**：ELBO router 需要一次额外 decoder pass；作者建议未来从 encoder latent 直接估计复杂度。[PDF p. 10, §6; “one additional decoder pass”]
- **任务范围**：只测 reconstruction fidelity，未测 video generation 或 action understanding，原因是资源消耗；因此对 downstream performance/efficiency 的影响仍是 future work。[PDF p. 10, §6; “beyond our current scope”]
- **数据与公平性**：256px square crop 是为匹配 ElasticTok，且基线不可与其原论文直接比较。[PDF p. 6, §4.1; “not directly comparable”]
- **理论–实践间隙**：Theorem 3.1 需要最小化 reconstruction loss 和 ELBO 条件；主文仅称 large-scale tokenizer 的 ELBO「believed」接近 likelihood，未展示 gap calibration。[PDF p. 6, §3.1; “believed to be close enough”]
- **伦理**：指出 deepfake、misinformation 与 privacy 风险，但没有部署缓解方案或评估。[PDF p. 11, Ethics Statement; “deceptive content”]
- **统计报告缺口**：Table 1–3 和 Figure 4 未呈现 seed、离散度、区间或显著性处理；这是 PDF 中缺失的报告信息，而非作者明确承认的 limitation。[PDF pp. 7–9, Tables 1–3; “PSNR↑”]

### 不利信息如何出现

没有文本证据可将任何选择称为作者的隐藏或操控策略；以下只记录可验证的呈现边界。

- 256px 裁剪与 baseline 不能直接横比的 caveat 在 §4.1 主文、主表之前出现，而非仅放在附录。[PDF p. 6, §4.1; “fair comparisons”]
- Table 1 自身暴露跨指标异质性：将 InfoTok `0.56` 与 ElasticTok `0.81` 比时，DAVIS 的 PSNR/SSIM 为 `24.52/0.738`，低于 `24.69/0.752`，但 LPIPS/FVD 更好；§4.2 的「outperform」没有给出如何在指标冲突时排序的规则。[PDF pp. 7–8, Table 1; “outperform ElasticTok”]
- 主要曲线和表格为单点或无误差带呈现；因没有 seed/replicate 描述，读者不能从版面判断结果变异。这是信息缺口，不推断意图。[PDF pp. 7–9, Figures 4 and Tables 1–3; “NFE Overhead”]
- Figures 2、3、5、6 都是代表性视频/帧，PDF 未说明其抽样规则；其代表性应保持未判定。[PDF pp. 7–8, 15–16, Figures 2–3 and 5–6; “Reconstructions examples”]

## 9. 附录职责

| 一级模块 | 页数 | 分类 | 内容与正文调用 |
|---|---:|---|---|
| Supplementary contents | 14 | other | 提供主文与附录目录；无独立结论。 |
| A Illustration of Adaptive Tokenization | 15–16 | qualitative_example | 两段视频的原图、InfoTok、mask、token usage；主文 Figure 1 caption 明说详图在 Appendix A。 |
| B Proofs | 17–21 | proof | B.1 将 uniform-router loss 化为 tree 并完成 Theorem 2.2；B.2 推导 Theorem 3.1。主文两处分别说 proof deferred to B。 |
| C Experimental Details | 21–23 | implementation_detail | Table 4、训练数据/资源、EMA length selection、pruning、clip-wise inference、dataset details；主文 §3.2/§4 提示更多 training/inference/resource details 在 C。 |
| D Additional Experiment Results | 23 | robustness | Table 5 多分辨率、Table 6 延迟；主文 §4.1 调用 resolution，§4.3 调用 latency details。 |
| E Use of Large Language Models | 23 | other | 仅说明用 LLM 润色 grammar/fluency；主文无调用。 |

附录以页数计为正文的 1.0×。它把形式证明、hyperparameter、compute、精确 inference pipeline 和 supplementary robustness 移出正文，换来主文较快的「理论→框架→表/图」节奏；代价是读者必须跳至 B 才能审查正式保证，跳至 C/D 才能复现实验或评估速度/分辨率主张。正文仍保留了决策性对象：Eq. (4)、Theorem 3.1 statement、Algorithm 1、Table 1、Figure 4、Table 2–3。

## 10. 用词与修辞

- **高频论证域**：`tokenization/tokenizer/tokens`、`router`、`ELBO`、`adaptive compressor`、`token sequence`、`compression rate`、`reconstruction quality`、`ElasticTok`。这些词主要来自真实机制与比较对象；模板引言并未主导其出现。
- **高频 n-gram**：`adaptive tokenization`、`adaptive compressor`、`compression rate`、`token sequence`、`information theory`、`ELBO-based router`、`reconstruction quality`、`evidence lower bound`。`I NFOT OK` 在 PDF 文本抽取中被错误拆开，故不能把 `nfot` 当词频结论。
- **主张动词**：按主文抽取的短语，`we propose` 3 次（pp. 2, 3, 5），`we prove` 2 次（pp. 2–3），`we show` 1 次（p. 3），`we find` 1 次（p. 6）；没有精确 `we demonstrate` 或 `we observe`。无主语的 `Empirical results demonstrate` 与 `These findings demonstrate` 另承担结果语气。[PDF p. 1, Abstract; “Empirical results demonstrate”]
- **限定/对比/因果词**：`approximately`、`could`、`believed`、`if`、`while`、`however`、`in contrast`、`therefore`、`remarkably`、`notably`。强语气集中在 `rigorously prove`、`guarantees`、`state-of-the-art`、`superiority`、`significantly`；弱语气集中在 ELBO closeness、跨模态推广和未来工作。对 30 句显式评价句作人工编码，强主张 19、限定/弱主张 11，约 `1.7:1`；这不是汇总器的原始 token 计数。

## 11. 闭环判断与可迁移规则

| 引言主张 | 方法/理论回应 | 证据回应 | 结论回应 | 状态 |
|---|---|---|---|---|
| fixed/data-agnostic rates 有效率偏差 | Theorems 2.1–2.2、tree proof | ElasticTok 主比较和 Table 3 uniform 对照 | 复述 fixed-rate suboptimality | **partially_closed**：理论是理想化/构造性，未测 true entropy ratio。 |
| ELBO router 接近理想长度 | Eqs. (3)–(4)、Theorem 3.1、B.2 | Table 2 对 exhaustive Optimal 接近 | 复述 dynamic length | **partially_closed**：oracle ablation 支持机制，但不验证全局最小/ELBO gap。 |
| compressor 以较少 token 保持重建 | mask + transformer mechanism | Table 1、Figures 2–4、Table 3 | 复述显著优势 | **closed（限于重建 benchmark）**。 |
| Flex 覆盖多种 budget | sampled `β` 的 single compressor | Figure 4 蓝/绿线、Table 1 | 结论未单独展开 | **closed（限于图示 rate 范围）**。 |
| 不同 resolution 可适用 | 2D RoPE、resolution-agnostic framework | Table 5 TokenBench 360p/aspect ratio | §6 只作泛化讨论 | **partially_closed**：只测一个补充 setting。 |
| audio/3D 与 downstream model 的广泛影响 | VAE-compatible 的概念类推 | 没有 audio/3D/generation/action experiment | 作为 future direction | **not_testable_here**。 |

**最有效的写作模式**：先用 source-coding 的不可忽略差异把「adaptive」从功能偏好变为可定义的长度分配问题；随后给可部署的 ELBO proxy；再用同预算主表、曲线/NFE 与 oracle/component ablation 分别检验效益、效率与机制。

**最大缺口**：理论保证的条件（true likelihood proxy、loss 达到最小、`β` 条件）没有与实际训练诊断逐一对齐；实证只覆盖裁剪后的 reconstruction 数据，且不报告不确定性，也不测试 downstream utility。

**可迁移规则**：当资源长度应随样本难度而变时，把理论上的每样本资源准则落实为可在已有模型上计算的 router；主结果必须同时有同预算比较、oracle/near-oracle 检查与组件消融。

**适用边界**：该规则依赖 proxy 与真实信息/任务价值有足够一致性，并要求 resource-saving 不损害真正 downstream target。若 reconstruction ELBO 与下游语义、感知质量或安全目标错位，本文的码长论证不能单独推出部署收益。

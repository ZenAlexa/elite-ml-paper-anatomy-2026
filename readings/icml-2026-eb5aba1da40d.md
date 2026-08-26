# Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models

## 文献与读取边界

- **论文**：John Cooper、Ilias Diakonikolas、Mingchen Ma、Frederic Sala，*Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models*。
- **样本标签**：ICML 2026；目录同时标记为 `oral` 与 `spotlight`。
- **实际读取版本**：`corpus/preprints/icml-2026-eb5aba1da40d.pdf`，29 个 PDF 物理页；本备忘以该份 arXiv v1 预印本为准，`source_kind=verified_preprint`。
- **读取范围**：正文、References、Supplementary Material 均逐页阅读。正文最后一句位于 PDF p. 12 的 References 标题之前；Supplementary Material 从 PDF p. 15 开始。

## 页级地图与版面

| PDF 页 | 位置与内容 | 语义模块 | 版面证据 |
|---|---|---|---|
| 1 | 标题、Abstract、Introduction 前三段 | abstract、introduction | 双栏正文；标题跨栏；Abstract 位于页首正文区，Introduction 紧接其后。 |
| 2 | Figure 1、Introduction 后三段、Section 2 起始 | introduction、other | Figure 1 跨两栏放在页首，约占上方四分之一；其后恢复双栏。 |
| 3 | Section 2 余部、Section 3 与 Definition 3.1 | other、theory | 两栏密集定义；唯一居中的 attention softmax 显示式位于上半页。 |
| 4 | Sections 3.1、3.2，Assumptions 3.2/3.6、Theorems 3.3/3.7、Lemma 3.5 | theory | 定理和假设排在连续段落内，未独立占页。 |
| 5 | Figure 2、Section 4 总体构造 | method | Figure 2 跨栏置顶；下方用三个未编号矩阵／映射显示块建立 SSM 到 Transformer 的接口。 |
| 6 | Figure 3、Definition 4.1、Theorems 4.2/4.3 | method、theory | Figure 3 跨栏置顶，随后给出 Selective Copy 的界定、下界和构造保证。 |
| 7 | Definition 4.4、Theorems 4.5/4.6、Section 5 与 5.1 | method、theory、experimental_design | 从第二个构造直接切换到 C1–C3 经验主张。 |
| 8 | Figure 4、Section 5.2 开始 | experimental_design、results | Figure 4 用折线、阴影带和嵌入式数表同屏呈现参数扫描。 |
| 9 | Figure 5、Associative Recall with Decoding、MKAR、NH 的设计与部分结果 | experimental_design、results | Figure 5 置顶；任务定义和解释占余下两栏。 |
| 10 | Figure 6、MKAR/NH 结果、Section 5.3、Length Generalization 设计 | experimental_design、results | Figure 6 同样组合折线、阴影带和数表。 |
| 11 | Figure 7、Table 1、OOD Generalization、Section 6 开始 | results、conclusion | 两个主要经验对象纵向排列；Conclusion 在页末开始。 |
| 12 | Figure 8、Conclusion 结尾、References 起始 | results、conclusion、other | Figure 8 位于页首；Conclusion 后半段和 References 共用该物理页。 |
| 13–14 | References 续页 | other | 纯参考文献双栏页；无 acknowledgement。 |
| 15 | Supplementary 导言、A Related Works、B Complete Preliminaries 开始 | appendix、related_work | 附录继续使用双栏，A 与 B 同页。 |
| 16–17 | Table 2、补充定义、Section C 与 C.1 | appendix | Table 2 是符号表；随后进入密集证明。 |
| 18–19 | C.2/C.3 与 D.1 | appendix | C.2 和 D.1 在 p. 19 同页衔接。 |
| 20–21 | D.2，Selective Copy 构造证明 | appendix | 多个大矩阵和 attention 权重显示块压缩可读文字面积。 |
| 22–25 | D.3、D.4、D.5 | appendix | D.4 的 Associative Recall 构造跨四页；p. 25 以 Figure 9 和实现讨论结束。 |
| 26–29 | E.1、E.2、Figures 10–16 | appendix、ablation | 参数、词表、head、state dimension、window 的补充扫描主要集中在此段。 |

**页面计数口径。**正文实际覆盖 p. 1–12，其中 p. 12 为 Conclusion 与 References 的混合页；因此记录 `main_pages=12`、`reference_pages=3`（p. 12–14）和 `appendix_pages=15`（p. 15–29）。自动测量把正文末页暂定为 p. 11，遗漏了 p. 12 顶部的 Conclusion 延续，见本备忘的「测量分歧」。

**模块字数口径。**机器草稿给出正文 5,674 个词、附录 6,640 个词。模块估计沿用该正文总量，并把 p. 12 的 Conclusion 片段留在正文；Related Works 和 E.2 的消融只在附录出现，故不计入正文份额。双栏排版贯穿全文。Figure 1–3 以构造流程图建立读者心智模型，Figure 4–8 以结果曲线占据主要决策位置；长证明和补充扫描均转入附录。

## 摘要逐句编码

| 句 | 词数 | 功能 | 限定、数字与承接 |
|---|---:|---|---|
| 1 | 25 | `object_scope` | 将 Hybrid 定义为 Transformer 与 state-space model layer 的组合，并把目标并列为 expressivity 与 computational efficiency。 |
| 2 | 25 | `problem_gap` | 使用 “lack a basic understanding” 指出机制和适用情境未知；承接研究动机。 |
| 3 | 16 | `object_scope` | 把对象收束到 “a broad family of core synthetic tasks”。 |
| 4 | 15 | `theory` | 声称在该任务族中证明 non-hybrid 的 fundamental limitations。 |
| 5 | 23 | `theory` | 明确二元代价：large number of parameters 或 large working memory。 |
| 6 | 37 | `method`、`theory`、`impact_claim` | 限定为 Selective Copying 与 Associative Recall；给出 small size、working memory、provably solve。 |
| 7 | 8 | `qualitative_result` | 经验评估验证理论发现。 |
| 8 | 26 | `experimental_setup`、`quantitative_result` | 对象从 constructed 扩到 learned hybrid；比较非混合模型，数字为 up to `6×` parameters。 |
| 9 | 15 | `qualitative_result`、`impact_claim` | 追加 length generalization 与 OOD robustness。 |

摘要的推进是 `object_scope → problem_gap → scope → theory → resource tradeoff → constructive method/theory → validation → quantitative learned-model result → generalization impact`。它报告实验结果，包含 `6×` 参数比较，并提及理论；没有摘要内 limitation 句。最强的可量化经验主张落在倒数第二句，随后用泛化与 OOD 结果扩大意义范围（PDF p. 1, Abstract；锚点 `up to 6× as many parameters`）。

## 引言的论证推进

以下比例以去除标题、Figure 1 caption 和作者脚注后的六个引言段落为分母，合计约 740 个英文词。

| 段 | 页 | 约词数与占比 | 主动作 | 上段留下的问题 | 本段回答与下一钩子 |
|---|---:|---:|---|---|---|
| 1 | 1 | 84，11.4% | `context` | 长序列 Transformer 的推理复杂度。 | 将 Mamba 定为效率候选，并指出 throughput 与 performance 的权衡。 |
| 2 | 1 | 109，14.7% | `problem` | 能否同时取得两类资源优势。 | 给出 hybrid 的产业规模与 Nemotron-H 例子，转向其机理。 |
| 3 | 1 | 122，16.5% | `missing_insight`、`core_idea` | 已有经验成功缺少可解释条件。 | 提出 function-composition tasks 与纯模型限制，钩向具体度量。 |
| 4 | 2 | 198，26.8% | `theory_preview`、`method_preview` | 何种任务暴露两种瓶颈。 | 用 injectivity 与 local sensitivity 导出两个纯模型下界，再给出两个构造任务。 |
| 5 | 2 | 147，19.9% | `result_preview` | 构造是否反映 learned model。 | 预告 MKAR、NH、`6×`、约 `10%` 长度差距与超过 `15%` OOD 差距。 |
| 6 | 2 | 80，10.8% | `roadmap` | 贡献如何落到章节。 | 按 Section 2–5 指向 notation、限制、构造和实验。 |

引言没有项目符号形式的 contribution list。第 4、5 段承担等价职责。前者给出条件化的理论主张和两项构造，后者给出可证伪的经验数字。它与摘要重复 Hybrid 的资源优势叙事，同时新增了两个充分条件、四项任务和具体比较尺度（PDF p. 2, Introduction；锚点 `injectivity condition`）。

## 相关工作

相关工作没有放入正文独立章节，集中在 Supplementary Section A。正文只在 Introduction、理论动机和实验解释中穿插引用，A 节本身约 546 个英文词，占附录 p. 15 的大部分文字区。

| 段 | 引用簇与比较维度 | 动作编码 | 与本文的关系 |
|---|---|---|---|
| A.1 | Elman、LSTM、HiPPO、S4/S4D、Mamba；维度为 SSM 的状态演化与长序列效率 | `taxonomy`、`credit_or_foundation` | 给出 SSM 历史和现代结构基础。 |
| A.2 | Transformer-XL、Hungry Hungry Hippos、Zoology、Jamba、Samba、BabyLM；维度为 recurrent/SSM 与 attention 的混合及经验性能 | `taxonomy`、`gap_creation` | 承认相近经验发现，再定位「何种任务要求混合」的理论缺口。 |
| A.3 | Merrill、Peng、Chen、Yehudai、Jelassi、Zhan；维度为 computational/communication complexity 与受控 synthetic tasks | `taxonomy`、`nearest_neighbor_contrast`、`limitation_of_prior` | 将本文与 pure-model 理论、copy/recall 任务和 sparse-attention 扩展区分开。 |

A 节通过按模型族、经验 Hybrid、表达力与效率三层分类避免复述 Section 4 的构造。Jelassi、Arora、Gu and Dao、Park 等引用在正文再次承担定义、动机或结果解释；A 节没有将每篇相关工作重新逐项比较（PDF p. 15, Section A；锚点 `fundamental tradeoffs ... remain poorly understood`）。

## 方法与理论

### 形式化对象与机制链

论文以 sequence-to-sequence token prediction 为外层接口。输入为长度 `L` 的 token 序列 `x`，任务写作 `F(u(x), v(x))`。`u` 是局部、可内容寻址的必要上下文，`v` 是从长上下文取得的控制变量，输出是目标空间 `Y` 中的 token 或序列（PDF p. 3, Definition 3.1；锚点 `M(x) = F(u(x), v(x))`）。

资源分为 input-independent memory，即模型参数量，和 input-dependent memory，即推理时保存输入与中间状态的 working memory（PDF p. 3, Memory Budget；锚点 `input-dependent memory`）。纯 SSM 的状态负责长期压缩，sliding-window Transformer 的窗口负责读取范围。Hybrid 的顺序构造让 SSM 先产出 `u` 与 `v` 的压缩表示，再让 Transformer 执行内容寻址的 `F`（PDF p. 5, Section 4；锚点 `summarizes the information from the long context`）。

| 组件 | 解决的前文问题 | 机制与证据 |
|---|---|---|
| `u(x), v(x), F` 分解 | 需要把「长上下文控制」与「局部 lookup」分开。 | Definition 3.1 把两者置入同一 function composition（PDF p. 3）。 |
| SSM encoder | Transformer 若自行寻找控制变量会需要大窗口。 | 组合 `SSM_u` 和 `SSM_v`，在末端输出 `u(x)` 与 `v(x)`（PDF p. 5；锚点 `maps x to a sequence`）。 |
| attention layer | SSM 若独立完成可内容寻址映射会需要大状态。 | 令 query 从 `v` 来、key/value 从 `u` 来，使 `TF∘SSM` 实现 `F`（PDF p. 5；锚点 `exactly F(u, v)`）。 |
| Selective Copy 具体构造 | 最近 number token 指定一个相对位置。 | Mamba 保留最近 number，attention 依此回看 `N` 个位置（PDF p. 6, Figure 3）。 |
| Associative Recall with Decoding 构造 | bit subsequence 先解码为 word token，再检索其最后一次出现后的 token。 | Mamba 累积 bit encoding；两层 attention 先取得相邻 token，再以 decoded token 检索（PDF pp. 22–24, D.4）。 |

方法动作序列为：`setup_notation → state_problem → derive SSM limit → derive Transformer limit → explain_mechanism → define_component → instantiate_selective_copy → connect_to_prediction → instantiate_associative_recall → connect_to_experiment`。Section 5 的 C1–C3 直接把构造有效性、learned hybrid 与扩展分布三层命题接入实验（PDF p. 7；锚点 `We empirically validate three claims`）。

### 理论结果与证明位置

| 对象 | 主文页 | 前提与结论 | 证明页 | 角色与经验对应 |
|---|---:|---|---|---|
| Definition 3.1 | 3 | 定义 function-composition task `F(u(x),v(x))`。 | 不适用 | 核心问题表达。 |
| Assumption 3.2 | 4 | `G(u)` 对一组控制变量的输出为 injection。 | 前提 | 支撑 SSM 信息下界。 |
| Theorem 3.3 | 4 | 在 Assumption 3.2 下，成功纯 SSM 的状态位数和下界为 `Ω(m log|V| - q log|Y|)`。 | C.2，18–19 | `guarantee`；对应 Selective Copy 与 Associative Recall 的纯 SSM 难度。 |
| Lemma 3.5 | 4 | 多层 SSM 可并入单层，合成状态空间不超过各层状态空间乘积。 | C.1，17–18 | `core_chain`；把多层情形化为单层信息论证明。 |
| Assumption 3.6 | 4 | 输出对相距 `R` 的前缀差异仍敏感。 | 前提 | 支撑窗口下界。 |
| Theorem 3.7 | 4 | 成功 sliding-window Transformer 需满足总窗口 `ΣW_i ≥ R`。 | C.3，19 | `guarantee`；对应长上下文控制变量。 |
| Theorem 4.2 | 6 | Selective Copy 上，纯 SSM 要求 `N log M` 状态信息，纯 Transformer 要求 `Ω(L)` 窗口。 | D.1，19 | `core_chain`；把一般下界实例化。 |
| Theorem 4.3 | 6 | 两层 Mamba + attention Hybrid 对所有 Selective Copy 输入求解，`d=O(max(log|V|,log L))`。 | D.2，20–21 | `core_chain`；C1 的构造对象。 |
| Theorem 4.5 | 7 | Associative Recall with Decoding 上，纯 SSM 为 `Ω(W log W)`，纯 Transformer 为 `Ω(L)`。 | D.3，22 | `core_chain`；第二个实例化下界。 |
| Theorem 4.6 | 7 | 三层 Mamba + 两层 attention 对均匀输入以 99% 成功率求解 Associative Recall with Decoding。 | D.4，22–25 | `core_chain`；第二个构造对象。 |

主文有 6 个 Theorem、1 个 Lemma、2 个 Assumption、5 个 Definition；没有 Proposition 或 Corollary 标题。完整证明置于 C.1–C.3 与 D.1–D.4。附录还出现 Claim D.3、D.4、D.7，分别验证 Mamba 的 Selective Copy 状态、其 attention 读出，以及 bit decoding 的 Mamba 状态（PDF pp. 20–24）。

按可见数学显示块人工计数，正文有 6 个，附录有 34 个，总计 40 个；多个对齐矩阵按一个显示块计。PDF 视觉扫描未见括号式 equation tag。自动测量草稿的 `numbered_equations_provisional=2` 不能代表所有未编号显示式，因此不将其用作显示式总数。

### 图、表与算法的理论职责

- **Figure 1**：用 question、key info、function composition 和 answer 的卡通流程把抽象 `u/v/F` 拆解放在 Introduction 的任务动机位置（PDF p. 2；锚点 `Example function composition task`）。
- **Figure 2**：给出 `SSM → TF` 的通用管线，紫色为控制参数、红色为完整任务输出（PDF p. 5；锚点 `represented in purple`）。
- **Figure 3**：将 Selective Copy 的最近 number token、相对距离和被复制 token 逐层画出（PDF p. 6；锚点 `most recent number token`）。
- **伪代码／algorithm block**：未出现。构造由 Definition、权重矩阵和附录证明表达，读者需要在公式级别还原步骤（PDF pp. 3–7、20–24，版面观察）。

## 实验设计

### 研究问题与对应安排

| 研究命题 | 设置 | 证据对象 |
|---|---|---|
| C1 | 显式实现 Theorems 4.3 与 4.6 的构造。 | Section 5.1 报告两者在最后位置完成各自任务；实现细节在 D.5。 |
| C2 | 训练 `TF-TF`、`SSM-SSM`、`TF-SSM`、`SSM-TF`，在 Selective Copy 与 Associative Recall with Decoding 比较。 | Figures 4–5。 |
| C3 | 在 MKAR、NH、长度分布外和 bit-proportion OOD 上比较 learned models。 | Figures 6–8 与 Table 1。 |

模型使用 GPTNeoX attention layer 与 Mamba SSM layer，RoPE positional encoding、causal windowed attention、单 attention head 和 Mamba state-dimension expansion 1；除特别说明外均为 seq-to-seq，accuracy 统计所有 valid tokens（PDF p. 8, Experiment Details；锚点 `accuracy is measured over all valid tokens`）。层顺序从左到右读取，`SSM-TF` 是先 SSM 后 Transformer 的目标 Hybrid（PDF p. 8；锚点 `layers are read left-to-right`）。

Appendix E.1 补足训练细节：AdamW、100 warm-up steps、线性衰减 learning rate、最大 learning rate 从 `1e-4` 到 `1e+0` 的十倍网格、训练至收敛，并以 loss plateau 后通常超过四倍计算量继续训练。每个实验运行 11 次，图中报告均值及 10th/90th percentiles error bars（PDF p. 25, E.1；锚点 `Experiments were ran 11 times`）。

| 任务 | 主要设计参数 | 控制与边界 |
|---|---|---|
| Selective Copy | input length 100；number tokens 5–10；词表 26；默认 token dimension 12。 | 小模型至约 10,000 parameters；不同 architecture 用 token dimension 控制近似参数规模。 |
| Associative Recall with Decoding | bit sequence length 5；word vocabulary `2^5=32` 外加 bits；dimension 24–768；三层模型。 | 两层模型在该设置下未学到任务，论文据此采用三层。 |
| MKAR | query length 2；词表 8；context length 100。 | 词表小到足以使目标 pair 在 context 中出现。 |
| Needle in a Haystack | 词表 100，加两个 marker tokens。 | 用 full-context attention 的结果检视除 function-composition 理论外的 learnability。 |
| Length generalization | 约 100M parameters；训练长度 20–50，测试更长长度。 | 将 Hybrid 与 `T_rope`、`mamba` 放在同一任务比较。 |
| OOD bit proportions | 12-layer models；训练 bit proportion 从 0.05 至 0.9；测试比例固定 0.2。 | Table 1 列 architecture 的 evaluation accuracy。 |

可复现信息在软件、优化器、学习率 sweep、部分任务参数和重复运行层级上较明确。明确 random seed 值、训练／评估样本数、硬件型号、wall-clock budget、代码仓库的固定 revision、数据泄漏控制与预注册失败阈值均未在 PDF 中给出。正文承认 Mamba layer 含更多 parameters，因此不同 architecture 的参数扫描范围并不完全相同（PDF p. 25, E.1；锚点 `Mamba layers contained more parameters`）。

## 结果、统计与可视化

| 结果 | 量化值与比较 | 统计处理和可视化 | 作者解释与不利解释 |
|---|---|---|---|
| 显式构造 C1 | 两个构造在 context 最后位置完成目标任务；正文未给数值准确率。 | 作为 Section 5.1 的实现验证；D.5 给 embedding/output 示意。 | 证明和实现共同支持构造正确性，实际运行量级未在主文表格中列出。 |
| Selective Copy | `SSM-TF` 在约 2,000 parameters 达 0.999；`TF-TF` 0.352、`SSM-SSM` 0.305、`TF-SSM` 0.433。约 12,000 parameters 时纯模型约 0.9。 | Figure 4：accuracy 对 parameter count 折线、阴影带与嵌入数表；11 次均值及 p10/p90 区间规则来自 E.1。 | 支持先 SSM 后 attention 的顺序；reverse Hybrid 接近纯模型。 |
| Associative Recall with Decoding | Figure 5 caption 记载 Hybrid 是唯一到 0.5 accuracy 的架构；纯模型在测试尺度未超过 0.4。 | Figure 5：accuracy 对 parameter count；三层设置，规模接近 1M。 | 构造需要三层，层数与其他小任务不同，跨任务参数比较须保留该条件。 |
| MKAR | Figure 6 数表中 `SSM-TF` 在约 6,000 与 12,000 parameters 均为 0.990/0.989；纯 TF 在约 12,000 为 0.668。文本称 60% accuracy 时参数需求约少 `6×`。 | Figure 6：折线、阴影带、数表。 | SSM 表现低；Hybrid 和 Transformer 在规模增加后都能做任务。 |
| Needle in a Haystack | Figure 7 显示 `SSM-TF` 和 `SSM-SSM` 以较少参数达到接近 1.0，Transformer 仍低。 | Figure 7：同一 parameter sweep。 | 作者明说该分离机制未由 function-composition 直接刻画，留作 future work。 |
| Length generalization | 训练短序列时，Hybrid 与 Transformer 的短长度差距约 2%，长长度差距约 10%。 | Figure 8：character accuracy 对 evaluation length；三条曲线。 | 结果符合 Hybrid 较慢性能下降的叙述，任务仍为 synthetic Associative Recall with Decoding。 |
| OOD generalization | 测试 bit proportion 0.2 时，Hybrid 在 train proportions 0.1、0.3、0.5、0.8 领先；0.05 与 TF 同为 0.47，0.9 时 SSM 0.86 高于 Hybrid 0.80。 | Table 1：6 个训练比例的 point accuracy；表内没有 dispersion 列。 | 正文用 “for almost all training distributions” 限定 Hybrid 优势，表中的两个非严格领先点与此措辞一致。 |

统计单位是 seq-to-seq 的 valid token accuracy，Figures 4–8 的重复运行聚合为均值并以 10th/90th percentiles 表示分布范围。论文没有报告 hypothesis test、p value、bootstrap、Bayesian analysis、回归或多重比较程序；Table 1 的单元格也没有明示不确定性。图注能说明任务、横轴、比较架构和主要结论；E.1 才说明 error bars 的具体含义（PDF p. 25；锚点 `10 and 90 percentiles as error bars`）。

## 消融、负面结果与自我设限

主文没有独立 ablation 小节，正文 ablation 面积为 0。附录 E.2 约四页，承担了参数和机制边界的消融职责。

| 对象 | 类型 | 位置 | 可识别结果 |
|---|---|---:|---|
| Figure 11 | 词表规模敏感性 | 27 | Selective Copy 将词表扩至 200、1000；作者称行为没有显著改变。 |
| Figure 12 | head 数与 Mamba state dimension | 27 | head 超过 1 时小模型表现很差；增加 state 不呈清晰单调改善。 |
| Figure 13 | 对抗数据分布 | 28 | 一半末 token 为 number，另一半 last number 很早出现；Hybrid 仍领先，SSM 在此分布更容易。 |
| Figure 14 | context window sensitivity | 28 | 更大 window 下 Transformer 变差，Hybrid 也常与 Transformer 持平；作者归因 learnability。 |
| Figures 15–16 | MKAR window、head、state dimension | 29 | window 增大时 Transformer 退化；head/state sweep 出现先降后升和非单调行为。 |

限制的明确位置如下：

- **scope / generality**：Conclusion 将理论局限为 synthetic tasks 与 restricted Transformer attention mechanisms，并把 real function-composition datasets 和 naturalistic long-context workloads 留为未来方向（PDF p. 12；锚点 `focus on synthetic tasks`）。
- **causality**：NH 的分离机制 “not directly characterized by function-composition”，因此未把该结果提升为现有理论的机制验证（PDF p. 10；锚点 `left to future work`）。
- **optimization**：E.2 多次将 head、state 和大 window 的异常曲线解释为 tiny-scale optimization issues；这是对 learned performance 与 expressivity guarantee 区分的直接陈述（PDF pp. 27–28；锚点 `learnability issues rather than expressivity ones`）。
- **baseline / metric**：Mamba 与 Transformer 的参数构成不同，正文只能做到 token dimension 驱动的近似参数匹配；实验并未提供同等 FLOPs、latency 或 memory 的完整测量（PDF p. 8 与 p. 25）。

不利信息的呈现方式以可验证事实为准。论文在主文 p. 10 主动写出 NH 的机制空缺，在 p. 12 直接列出合成任务与 attention 范围，在 p. 27–28 把较大 window 下的 learnability 退化配图展示。完整证明、训练 sweep 和额外扫描转入附录，并有 Section C–E 的正文调用；这种位置安排降低主文长度，同时使读者必须翻至附录才能复核证明细节和误差条规则。Table 1 没有 dispersion，表格本身不能显示运行间波动，这是版面事实，不推断作者动机。

## 结论与主张闭环

Conclusion 是一个跨 p. 11–12 的单段收束。它依次重述 function-composition 的两个步骤、SSM 与 sliding-window Transformer 的限制、Selective Copy 和 Associative Recall 的构造，以及 learned-model 的长度与分布外结果；末句给出限制和未来方向。结论没有新数字（PDF p. 12, Section 6；锚点 `Limitations include our focus on synthetic tasks`）。

| 引言主张 | 方法与理论回应 | 设计与结果回应 | 结论与附录回应 | 闭合状态 |
|---|---|---|---|---|
| 纯 SSM 的 state 与纯 Transformer 的 window 形成互补瓶颈 | Definition 3.1、Assumptions 3.2/3.6、Theorems 3.3/3.7 | 以 Selective Copy、Associative Recall 构造具体实例 | C.1–C.3 给证明；Conclusion 重述限定 | `closed`，条件化于给定假设与 sliding window。 |
| Hybrid 可以在 Selective Copy 同时改善资源规模 | Theorems 4.2/4.3，Mamba 先编码、attention 再读取 | Figure 4 在约 2k 参数显示 0.999 | D.1/D.2 给下界和构造证明 | `closed`，理论命题闭合；learned 数值只覆盖测试设置。 |
| Hybrid 可以在 Associative Recall with Decoding 取得相应分离 | Theorems 4.5/4.6，三层构造 | Figure 5 的 learned Hybrid 超过 0.5，纯模型未超 0.4 | D.3/D.4 给证明 | `partially_closed`，经验规模与三层条件限制外推。 |
| learned Hybrid 在更多 synthetic tasks 仍有优势 | Section 5.2 的 architecture sweep | Figures 6–7 | E.1/E.2 给参数扫描 | `partially_closed`，MKAR 与 NH 的机制地位不同。 |
| Hybrid 的长度和 OOD 泛化更强 | 没有相应一般定理 | Figure 8、Table 1 | Conclusion 回收，E.1 给重复规则 | `partially_closed`，任务、模型和 OOD 构造都很特定。 |
| 这些分离解释现实长上下文任务 | 引言把 function composition 称为自然任务模型 | 没有真实数据集或 naturalistic workload 评估 | Conclusion 将 real datasets 列为未来工作 | `open`。 |

## 附录职责

Supplementary Material 为 15 个物理页，正文含 Conclusion 的范围为 12 页，长度比约为 1.25。它保留理论可核查性和训练细节，同时使正文把定义、结果和限制集中在决策路径上。

| 附录模块 | 页 | 分类 | 内容、对象数与正文调用 |
|---|---:|---|---|
| A Related Works | 15 | `other` | 3 个引用簇；正文没有单独 A 节调用，Introduction 已先用少量相关引用定位。 |
| B Complete Preliminaries and Notations | 15–17 | `extended_method` | Table 2、Transformer/SSM/Mamba、encoder/decoder、embedding 定义；p. 2 明确将 complete list defer 至 Section B。 |
| C Omitted Proofs in Section 3 | 17–19 | `proof` | C.1 Lemma 3.5、C.2 Theorem 3.3、C.3 Theorem 3.7；主文 pp. 4 明确调用 C.1–C.3。 |
| D Omitted Proofs in Section 4 | 19–25 | `proof` | D.1–D.4 覆盖 Theorems 4.2、4.3、4.5、4.6；主文 pp. 6–7 逐项调用。 |
| D.5 Construction Implementations | 25–26 | `implementation_detail` | Figures 9–10 展示两种构造的 embedding/input-output；p. 7 的 Section 5.1 调用 D.5。 |
| E.1 Expressivity Experiments | 25–26 | `reproducibility` | AdamW、warm-up、learning rate sweep、11 runs、token/vocabulary/layer 细节；p. 8 调用 Appendix E。 |
| E.2 Additional Experiments | 26–29 | `ablation` | Figures 11–16 的词表、head、state、对抗分布、window 扫描；主文不逐项调用。 |

正文在 Definition、Theorem、Figure 4–8 和 Table 1 保留了作出主张所需的最小对象。证明的每一步、矩阵权重、实现 embedding、训练 sweep 与额外敏感性扫描依赖附录。理论主张需要 C/D 才能检查推导；经验主张的 error bar 和超参数解释需要 E 才能完整复现。正文对核心结论自足，证明与复现审计并不自足。

## 用词与修辞

原始 token 频率由汇总脚本统一计算。人工语境编码显示，正文高频实词由 `hybrid`、`pure`、`SSM`、`Transformer`、`task`、`memory`、`function composition`、`construct` 与 `performance` 驱动；这些词在定义、下界、构造和结果段均承担实际论证角色，并非模板性堆叠。

| 结构 | 主文次数 | 所在模块与作用 |
|---|---:|---|
| `we show` | 2 | p. 7 构造可得小参数 Hybrid；p. 10 指向 Figure 7。 |
| `we find` | 1 | p. 2 汇总 `6×` 任务结果。 |
| `we demonstrate` | 1 | p. 7 将 C1–C3 接到实践设置。 |
| `we propose` | 0 | 未出现。 |
| `we observe` | 2 | p. 2 预告 OOD/长度；p. 9 解释三层结果。 |
| `we prove` | 1 | p. 2 预告两个资源限制。 |
| `we construct` | 3 | Abstract、Introduction、Section 3 的理论构造语境。 |
| `we study` | 3 | Abstract、Introduction、Section 3 的对象限定。 |
| `we validate` | 1 | p. 2 从理论过渡到经验。 |

对 Abstract 与 Introduction 的 30 个直接 claim-bearing sentences 作人工编码，17 句为无条件或强动词陈述，13 句带 `can`、`typically`、`at the tested scales`、`around`、`sometimes` 或任务范围限定，强主张与限定主张的比约为 1.31:1。限定语主要落在 learned-model 的规模、OOD 和实际迁移处；定理主张则以 Assumption 和 architecture scope 限定。该比例是写作编码，不是论文报告的统计量。

## 最终判断

**单一主线。**长上下文序列任务可分成控制变量提取和受控内容检索。纯 SSM 在后者受状态容量约束，sliding-window Transformer 在前者受窗口约束；按 `SSM → attention` 排列的 Hybrid 可把两种资源责任分配给不同层。该因果链先用条件化下界固定，再以两个构造和 learned synthetic experiments 追踪。

**正文保留的决策内容。**正文保留任务分解、两类假设、六个主要 Theorem 的陈述、两个构造图、C1–C3、Figures 4–8、Table 1 和 p. 12 的限制。读者可在不进入附录的情况下判断论文的理论前提、比较对象、主要趋势与外推边界。

**附录迁移与代价。**证明、权重矩阵、符号表、训练 sweep、重复规则、词表／head／state／window 扫描移入 p. 15–29。迁移没有抹去主文的核心证据，但使定理验证和实验复现依赖 C–E。

**最有效的模式。**Figure 2–3 将抽象分解压缩为层间信息流，随后 Theorems 4.2–4.6 把资源不等式与两个可视化任务对齐，Figures 4–8 再将同一层顺序带到 learned models。图、定理和实验的排序与主线一致。

**最大缺口与读者成本。**理论覆盖 injectivity、local sensitivity 和 sliding-window Transformer。真实 function-composition data、全注意力或 external memory 的理论地位未被实测。Table 1 缺少运行间分散度，部分 learned 结果还受层数、参数组成和小尺度优化影响；这些条件限制结论的可迁移范围。

**可迁移规则。**当一个架构主张「兼具两种资源优势」时，先构造能把两种资源瓶颈分离的任务，再把下界、显式构造、learned training 和分布外检查排列为同一条证据链。

**适用边界。**该规则适用于能写成控制变量加局部检索的任务，并要求对 pure baseline 的 memory/parameter 口径、attention 形式和分布假设做出明确限定。若目标任务的性能由优化、数据分布或外部记忆主导，单靠该 function-composition 理论不能给出机制解释。

## 测量分歧与文本内交叉核对

1. `preprint_auto_metrics.csv` 将正文末页暂定为 p. 11；PDF p. 12 顶部仍为 Section 6 Conclusion，References 在同页下方开始。本文按实际内容记录 main range 为 p. 1–12，References 为 p. 12–14。
2. 自动草稿的 `numbered_equations_provisional=2` 与 PDF 的可见数学排版口径不同。人工以居中的／独立的显示块计得正文 6、附录 34；视觉扫描未见括号式 equation tag。
3. Theorem 4.6 在主文 p. 7 的句子写作 “solve the selective copying task”，其标题、Definition 4.4 上下文和 Appendix Theorem D.6 都指向 Associative Recall with Decoding。该处按版面原文记录为内部标签不一致，不改写其结论对象。
4. p. 20 的 Claim D.3 是 Selective Copy 的 Mamba 输出保证；p. 21 页首却印为 “Proof of Claim D.7”，而段内符号仍是 Selective Copy 的 `N` 和 `n_i`。p. 23 的 Claim D.7 才是 bit decoding 保证，因此 p. 21 的 proof label 与前后对象不一致。

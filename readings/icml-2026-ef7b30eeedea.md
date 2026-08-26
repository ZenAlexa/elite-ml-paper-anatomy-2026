# 深读备忘：Rational Transductors

## 读取范围与身份

- **论文**：*Rational Transductors*，Mehryar Mohri；ICML 2026，目录标记为 `oral|spotlight`。
- **实际读取版本。** `corpus/preprints/icml-2026-ef7b30eeedea.pdf`，49 个 PDF 物理页，arXiv 2602.07599v1。
- **来源元数据。** `source_kind=verified_preprint`，`source_url=https://arxiv.org/pdf/2602.07599`。OpenReview forum <https://openreview.net/forum?id=uEZpyELNuB>。
- **文档边界**：p.1–2 为目录；p.3 为摘要并开始正文；p.3–42 为摘要、正文与结论；p.43–45 为 acknowledgments 和 references；Appendix A 在 p.46–47，Appendix B 在 p.48–49。PDF 中没有独立 supplementary 文件或独立 limitations 节。
- **阅读方法**：以下判断以该 PDF 的物理页、章节与图表/公式编号为锚点。篇幅数字为版面与提取文本的近似值，不把图、公式或目录排版误当成连续散文。

## 逐页地图、模块映射与版面

|物理页|内容与语义模块|版面/阅读面积|估计文字与证据|
|---|---|---|---|
|p.1–2|目录；`other`|单栏目录占满两页，正文被放在目录之后。|约 1,035 个提取词；目录列出 1–8 节与 A–B 附录。|
|p.3|Abstract；Introduction 起始|双栏；摘要约占上半页，随后进入问题背景。|摘要 6 句；引言第一段提出 Transformer 的 state-tracking 缺口。|
|p.3–5|1 Introduction；其中含内嵌 Related Work|双栏；Figure 1 在 p.5 跨栏，占上半页左右，压缩了 Related Work 与 roadmap 的连续阅读。|引言与嵌入式相关工作合计约 1,440 个提取词。|
|p.6–12|2 Rational Features Framework；`method`|双栏；Figure 2、3、4 分别给出 sidecar、Universal 与 wide/deep 对照。|约 3,185 个提取词；Eq. (1)–(9)。|
|p.12–13|3 Motivation: Why Rational Features?；`other`|双栏；p.13 顶部先放 Table 1。|约 900 个词的动机段，突出 state tracking、time invariance 与 parallel scan。|
|p.13–24|4 Expressivity and Complexity；`theory`|双栏、高公式密度；Table 1、Figure 5、Figure 6 跨栏或占大块版面。|约 6,165 个提取词；Lemma 4、Theorem 5–18、Corollary 19 与 Eq. (10)–(22)。|
|p.25–33|5 Theoretical Analysis of Learning；`theory`|双栏、公式与 proof 交替；p.33 下部转入第 6 节。|约 4,750 个提取词；Theorem 20–30 与 Eq. (23)–(48)。|
|p.33–35|6 Concrete Training Recipe；`experimental_design`|双栏；没有伪代码框，训练过程用 prose 与 Eq. (49)–(51) 表达。|约 1,300 个提取词；parallel scan、spectral control、near-identity initialization。|
|p.35–41|7 Empirical Validation；`experimental_design` 与 `results`|双栏；Figure 7–11 各占约半页到一页，主文以图注承载大量配置与结果。|约 2,900 个提取词；四项 synthetic task。|
|p.42|8 Conclusion；`conclusion`|双栏，纯文字。|约 418 个提取词；回收三类「completeness」，以 large-scale pre-training 收束。|
|p.43–45|Acknowledgments、References；`other`|双栏参考文献；p.43 顶部是简短致谢。|约 47 条参考文献，覆盖 WFA、形式语言、circuit complexity、Transformer/SSM。|
|p.46–47|Appendix A；`appendix`|双栏；定义、Eq. (52) 和 Fliess theorem 的背景材料。|约 786 个提取词；正文 p.5 roadmap 明确调用 Section A。|
|p.48–49|Appendix B；`appendix`|双栏；Table 2 占 p.48 中部，p.49 只留下结尾一句。|约 452 个提取词；四项任务的 hyperparameter 与 5-seed 稳定性说明。|

**版面判断。** 正文采用紧凑双栏 letter 页面；图 1–6 为蓝/绿/橙色的结构图或理论图，图 7–11 为带图例的曲线/柱图，均依赖 caption 完整交代任务。主要图跨两栏，公式密集段落以长 proof 切割阅读流。p.5 的 Figure 1、p.11 的 Figure 4、p.15 的 Figure 5、p.23 的 Figure 6 使用大面积空白和跨栏图形，承担概念停顿；p.36–41 的实验页以单一主图加短结果段落推进。文中无 Algorithm 或 pseudocode 环境。[p.5, Figure 1；p.11, Figure 4；p.23, Figure 6；p.36–41, Figure 7–11；layout observation]

### 12 个固定语义模块

下表的 `main share` 对 p.3–42 的语义切片估算；分散出现的 limitations 会与来源段落重叠，因此这些比例不用于相加。

|模块|状态|估计词数 / main share|图/表/算法/显示公式|映射说明|
|---|---:|---:|---:|---|
|`abstract`|observed|约 204 / 0.01|0/0/0/0|p.3，6 句。|
|`introduction`|observed|约 725 / 0.04|0/0/0/0|p.3–5，扣除 Related Work 后的背景、问题、方案与 roadmap。|
|`related_work`|observed|约 700 / 0.04|0/0/0/0|p.4–5 的内嵌 `Related Work`，没有独立二级节。|
|`method`|observed|约 3,185 / 0.16|4/0/0/11|p.6–12，WFA、parameterization、deep injection 与 stack 对照。|
|`theory`|observed|约 10,525 / 0.54|2/1/0/45|p.13–33 的 expressivity 与 learning theory。|
|`experimental_design`|observed|约 1,250 / 0.06|0/0/0/3|p.33–35 的 recipe，加 p.36–41 各 task setup。|
|`results`|observed|约 2,250 / 0.12|5/0/0/0|p.36–41，Figure 7–11。|
|`ablation`|not_present|0 / 0|0/0/0/0|没有 component removal、head routing、超参数敏感性或机制替代检验。|
|`conclusion`|observed|约 418 / 0.02|0/0/0/0|p.42。|
|`limitations`|observed|约 480 / 0.02|0/0/0/0|分布在 Table 1、§4、§5.3、§7.5 与 conclusion，未形成独立节。|
|`appendix`|observed|约 1,238 / null|0/1/0/1|p.46–49，A 为理论背景，B 为实验设置与稳定性。|
|`other`|observed|约 2,141 / null|0/0/0/0|目录、动机、acknowledgments、references。|

## 摘要：逐句功能与承接

|句|功能|限定、数字、比较与承接|
|---|---|---|
|1|`object_scope`、`problem_gap`|将对象限定为 standard Transformers，缺口是 rigid sequential logic 与 state tracking。[p.3, Abstract, “struggle with rigid sequential logic”]|
|2|`theory`、`problem_gap`、`scope_boundary`|以 AC0/TC0 解释缺口；条件是没有 intermediate chain-of-thought，措辞为 “often fail”。它把经验问题挂到 circuit-class 前提上。[p.3, Abstract, “limited to AC0 … or TC0”]|
|3|`core_idea`、`method`|提出 dual-stream Rational Transductors，将 Transformer 接上由 WFA 导出的 matrix-valued recurrence。[p.3, Abstract, “dual-stream architecture”]|
|4|`method`、`theory`、`impact_claim`|以 Deep Rational Injection 引入状态；主张覆盖 all Regular Languages、NC1-complete Boolean Formula Evaluation、Parity/Modular Counting，并给出 `O(L + log T)`。[p.3, Abstract, “Deep Rational Injection”; `O(L + log T)`]|
|5|`theory`、`method`、`limitation`|把学习理论拆成 Random Rational Features 的 universal basis 与 learned Differentiable Rational Features 的 compactness 必要性；限制隐含在随机方案的效率缺口。[p.3, Abstract, “representational compactness gap”]|
|6|`qualitative_result`、`impact_claim`|以理论和实证共同收束「Regular Gap」与 length generalization；比较对象为 standard Transformers 与 traditional RNNs，没有摘要级数字。[p.3, Abstract, “solve the ‘Regular Gap’”]|

功能顺序为**问题 → 复杂性前提 → 体系结构 → 形式能力与效率 → 学习理论 → 经验含义**。摘要把最强的范围性主张放在第 4 句，把实验结论放在末句；它没有给出实验数据、seed 数、具体任务长度或 error expression。其理论与经验结论均以抽象层次出现，细节移到 §4–7 与 Appendix B。[p.3, Abstract]

## 引言与相关工作：论证推进

### 引言动作链

1. **`context`**：Transformer 已成为序列建模标准，attention 处理长程 semantic dependencies。[p.3, §1, “de facto standard”]
2. **`problem` + `failure_of_prior_work`**：把 rigid logic、state tracking、unbounded sequential dependencies 定为缺口，并用 AC0/TC0、C-RASP 接上理论理由。[p.3, §1, “well-documented blind spot”]
3. **`failure_of_prior_work`**：RNN/SSM 带回 latent state，却面对 expressivity、interleaving 或 sequential bottleneck 的取舍。[p.3, §1, “structural trade-off”]
4. **`core_idea`**：将 Attention/Recurrence 的二分设为错误问题，提出 WFA 支持的 dual stream。[p.4, §1, “false one”]
5. **`method_preview`**：Rational Feature Head 以线性 matrix multiplication 演化；parallel scan 与 WFA transparency 给出两个直接理由。[p.4, §1, “two decisive advantages”]
6. **`theory_preview`**：Random Rational Features 解释初始化，learned regime 回应 compactness，并预告 spectral parameterization。[p.4, §1, “exponentially inefficient”]
7. **`contribution_list`**：三组 Related Work 段落把 sidecar 与 SSM、Transformer expressivity、spectral automata learning 对齐。[p.4–5, §1, “Related Work”]
8. **`roadmap`**：逐节映射 architecture、motivation、expressivity、learning、recipe、experiments、appendix。[p.5, §1, “Paper Organization”]

这条链的未解问题依次是「attention 为什么失败」「已有 recurrence 为什么不够」「线性 WFA 为什么足够」「如何学习且保持稳定」「是否在合成任务上出现相应行为」。每一步都留出下一步的钩子。引言没有单列编号贡献；它以两项“decisive advantages”、学习理论段和 Related Work 三个 bullet 承担贡献清单。清单包含可证伪的语言/复杂度与效率主张，未在引言报告实验数字，也没有独立 limitations bullet。[p.4–5, §1]

### 内嵌 Related Work 的功能

Related Work 约占引言的一半，置于 p.4 下半到 p.5 中段；它没有重复 WFA 定义，改用比较维度组织：

- **SSM/Linear RNN 簇**：S4、Mamba、RWKV、DeltaNet、Kimi Linear；差别是 input-driven sidecar 预计算状态，文章将其与 deep/interleaved SSM 的 layer-wise dependency 对照。[p.4–5, §1, “State Space Models (SSMs) and Linear RNNs”]
- **Transformer expressivity 簇**：Hahn、Merrill and Sabharwal 的 AC0/TC0 上界为 Parity/NC1 的 constructive extension 设立缺口。[p.5, §1, “Expressivity of Transformers”]
- **Spectral automata learning 簇**：Balle and Mohri 的 WFA learning 被表述为迁入 deep-learning optimization loop 的基础。[p.5, §1, “Spectral Learning of Automata”]

前两簇在 §4 的 circuit/language 论证和 §7 的 Transformer/SSM 范围说明中再次承担论证作用；第三簇在 §5.3 Hankel-Rademacher 讨论中被再次调用。相关工作并未给出 nearest-neighbor 的参数、benchmark 或实验复现表；比较主要来自架构依赖与理论类别。[p.5, §1；p.32, §5.3；p.36, §7.1]

## 方法、公式与理论链

### 最小逻辑单元与段落动作

`setup_notation → define_component → explain_mechanism → define_component → define_component → contrast_alternative → define_component → derive → contrast_alternative → summarize`

- **WFA state**：`A=(Σ,d,α,{Mσ})`，输入 token 选择 transition，`h_t=M_{x_t}h_{t-1}`，中间向量而非 classical final weight `β` 是注入对象。它把「显式 state tracking」变成可用 feature sequence。[p.6, §2.1–2.2, Eq. (1)]
- **结构化 transition family**：DPLR 对 fading/mixing；Cayley orthogonal 对 conservation/counting；shared basis 降低参数；direct sum 形成 Universal Transductor 的 orthogonal/stochastic parallel heads。[p.7–9, §2.3, Eq. (2)–(4)]
- **Deep Rational Injection**：各 Transformer layer 用独立 `W_proj^(l)` 接收同一 `h_t`，避免只在 input injection 时让 backbone 保存精确状态；Eq. (5)–(6) 把对应关系写为每层的加性注入。[p.9–10, §2.4, Eq. (5)–(6)]
- **wide sidecar 的设计选择**：线性 stack 可合并为单一较宽 WFA；若在层间加入 nonlinearity，tensor-product state 带来更紧凑的表达，却把 scan 串行化为 `O(L log T)`。文章选择 input-driven single head 的平行路径。[p.10–12, §2.5, Proposition 1; Theorem 3]
- **训练 recipe**：forward 与 reverse affine recurrence 分别以 parallel scan 完成；Scaled Cayley 与 explicit spectral normalization 处理 conservation/decay；near-identity initialization 将学习从 remember 转为选择性 forget。[p.34–35, §6.1–6.3, Eq. (49)–(51)]

方法没有 Algorithm 环境、输入输出框、循环层级或可执行伪代码。正文解释到状态方程、矩阵族、训练复杂度与初始化的粒度；kernel 实现只说 CUDA/Triton、Kogge-Stone-style scan 和小维度 `d≤32`，没有给 kernel、代码地址、API、测试样本数或训练日志。[p.34, §6.1, “CUDA or Triton”；p.48, Appendix B]

### 公式与理论库存

- **公式量**：物理页中编号公式连续为 Eq. (1)–(52)，共 52 个。另有约 8 个未编号的 display block（shared-basis sum、块矩阵、图中/证明中的矩阵等），故显示公式约 60 块；method 为 Eq. (1)–(9)，理论为 Eq. (10)–(48)，recipe 为 Eq. (49)–(51)，Appendix A 为 Eq. (52)。[p.6, Eq. (1)；p.35, Eq. (51)；p.46, Eq. (52)]
- **命名结果**：主文有 Proposition 1、8、9、15、17，Lemma 4，Theorem 2–7、10–11、13、16、18、20–21、24–30，Corollary 14、19、23；Appendix A 有 Theorem 32。合计 30 个命名 theorem/lemma/proposition/corollary。Definition 12、31 不计入该数。[p.10–33, named statements；p.46, Theorem 32]
- **核心因果链**：Lemma 4 先将 sinusoidal/RoPE 编码写成 WFA；Theorem 5–7 用 explicit automata 构造 Parity、Modulo-k 与 base-b evaluation；Theorem 13 将整机归结为 `F_TF ∘ T_Rat`；Theorem 16–19 给出 PNC1/AC0 sandwich；Theorem 20–30 处理随机特征、compactness、梯度、泛化与 Lipschitz stability。[p.14–16, Lemma 4 and Theorem 5–7；p.20–24, Theorem 13 and 16–19；p.25–33, Theorem 20–30]
- **经验对应**：Theorem 6 对应 Modulo-5 与 length generalization；Theorem 7 对应 Base-2 evaluation；parallel scan 的主张对应 isolated mixer latency；Universal/stochastic discussion 对应 long-integer addition。Random-feature universality、Krohn-Rhodes completeness、W-MSO characterization 没有对应的 direct empirical study。[p.36–41, §7.1–7.5]

### 理论结果的边界

多数结果带有明确前提，包括 fixed depth、无 auxiliary memory/chain-of-thought、exact 或 bounded-precision arithmetic、fixed model parameters、结构化的 spectral constraint，或 contractive `γ<1`。Theorem 27 自己指出 `γ=1` 的 unitary regime 不能使用其 `1/(1-γ)` 误差界，只能依赖 transition 的 algebraic exactness 与足够硬件精度。

Table 1 将「all Context-Free Languages」列为两类模型都不具备的能力。§4.2 随后讨论某些 Context-Free languages 在无限域上可通过 quantitative embedding 被「recognize」，并限定 robust learning 需要 high precision 和特定 inductive biases。两处需要一起读取，后者不能扩展成一般 Context-Free 保证。[p.13, Table 1；p.17, “Recognition of Context-Free Languages”；p.31, “Remark: The Unitary Regime”]

## 实验设计、结果与统计

### 设计事实与复现粒度

|项目|已给出事实|缺口|
|---|---|---|
|研究问题|明确检验两项：Rational Transductors 是否解决 NC1/Regular Gap，是否对未见长度保持 time invariance。[p.35, §7, “two key claims”]|没有预注册、功效分析或正式 failure criterion。|
|任务|Modulo-5 Counting、Modulo length generalization、Long-Integer Addition、Base-2 Integer Evaluation，均为 synthetic。[p.36, §7.1；p.39–41, §7.4–7.5]|没有自然语言、代码、真实长文或公开数据集评测。|
|比较模型|Transformer 在四项任务出现；LSTM 出现在 Base-2；Sequential RNN 和 attention mixer 用于延迟图；SSM 只有理论范围讨论。[p.36, §7.1；p.38–41, §7.3–7.5]|没有 S4/Mamba/RWKV 的实际结果，且没有 component-matched head ablation。|
|训练与硬件|PyTorch、single NVIDIA T4 or A100、AdamW/Adam；Table 2 给出 d、layers、batch size、learning rate、steps、loss、precision。[p.48, Appendix B, Table 2]|未给 source repository、commit、数据生成器、完整 seed 列表、评测样本数或原始结果。|
|对照条件|Modulo 的 RT 与 Transformer 约 25k 参数；length task两者 2 layer/4 heads；addition 同为 2 layer/32 hidden/4 heads。[p.36–40, §7.1–7.4]|PE 设置同时随模型变化：RT 关闭 positional encoding，Transformer 使用 learned/relative positional encoding；它是目标 inductive-bias 设计，也使结论属于该整体配置。|
|重复与不确定性|所有 synthetic experiments 说重复 `N=5` seeds；Fig. 7 写 SD `<0.01%` omitted，Fig. 8 说 shaded region 来自 5 runs，Appendix B 给 addition `<0.05%` 与 Base-2 `<1.0×10^-10`。[p.36–37, Figure 7–8 captions；p.48, Appendix B.2]|无 confidence interval、显著性检验、多重比较、bootstrap、effect-size 分析或每项 test denominator。|

聚合单位主要是 sequence-level accuracy、每长度曲线、single-batch (`B=1`) mixer latency 和 MSE；seed 是显式重复层级。延迟实验说明为 A100、warm-up 后 20–100 trials 的平均值，测试范围 `T=128` 到 `32,768`，但图中没有可复算的点表或离散量。图注可单独理解任务与结论，缺少完整统计设计时仍无法恢复 raw variability。[p.38, §7.3, “20–100 trials”；p.39, Figure 9]

### 主结果库存

|主张|证据对象与数值|比较与统计处理|不利解释及正文处理|
|---|---|---|---|
|Modulo-5 的 cyclic state|Figure 7：RT 在测试长度至 500 维持 100%，Transformer 在更长序列接近 20% random chance；5 seeds，SD `<0.01%` 被省略。[p.36, Figure 7]|约 25k 参数的 2-layer Transformer；准确率曲线。|该设置关闭 RT 的 PE 并使用 orthogonal Cayley，结果支持的是此 inductive-bias package；文中没有 learned-matrix recovery 或 component deletion 来直接验证「学到 cyclic permutation」。|
|长度泛化|Figure 8：仅以 `L_train=40` 训练，RT 在 `L_test=1000` 仍为 99% 以上；Transformer 约为 20%。[p.37–38, Figure 8 and Results]|5 runs，shaded SD 在图尺度上不可见。|覆盖的是 Modulo-5 一项任务；结论没有在自然序列或其他 regular-language family 上交叉验证。|
|平行效率|Figure 9：Rational mixer 在 `T>512` 超过 sequential RNN，并至 `T=32k` 维持吞吐；attention 在极长长度出现 quadratic wall。[p.39, Figure 9]|B=1，A100，20–100 warm trials；比较对象只是 sequence-mixing layers。|文中明确隔离 shared feed-forward blocks，因此不能把图直接读成完整训练/推理系统端到端速度。|
|long-integer addition|Figure 10：Transformer 在 `L=100` 为 0%，Universal RT 至 `L=1000` 为 100%。[p.40, Figure 10]|sequence-level exact-match accuracy；训练长度 `U[10,40]`，stochastic head。|该图没有分离 orthogonal 与 stochastic head，也没有测量「autonomously route」的实际 routing 行为。|
|base-2 quantitative precision|Figure 11：RT MSE `≈5.9×10^-9`，LSTM/Transformer `≈8.4×10^-2`；训练 `L=64`、Float64。[p.41, Figure 11]|MSE，Appendix B 给出 5-run SD `<1.0×10^-10`。|p.41 明示 `L>53` 的 IEEE-754 significand 边界；归因于 finite precision 与优化误差，未做长度外推曲线。|

**消融与负面结果。** 没有独立 ablation section，也没有删除 Deep Rational Injection、替换矩阵族、改变 state dimension、PE/control 或将 Random 与 Differentiable Rational Features 配对的实验。存在的负面信息是 Transformer 的长度外 failure、LSTM/Transformer 的 Base-2 failure、unitary precision caveat 与 isolated runtime scope；它们不是对 RT 组件识别的消融。[p.35, §7 heading；p.38, §7.3；p.41, §7.5]

**不利信息的呈现。** Figure 7 的 caption 明示「standard deviations are negligible (<0.01%) and omitted for clarity」，Figure 8 的 caption 明示阴影存在但「invisible at this scale」。这两处是可验证的 error-expression 选择，不能单凭该版面推定呈现意图。正文没有足够证据支持「隐藏异质性」「弱基线」或「未来工作化」等作者动机归因。[p.36, Figure 7；p.37, Figure 8]

## Limitations、结论与闭环

### 分散限制

1. **模型/理论范围**：全语言层面仍没有 unbounded stack；Table 1 把所有 Context-Free languages 标为不可得。[p.13, Table 1]
2. **算术与精度**：诸多 expressivity 结论依赖 exact/bounded-precision abstraction；Base-2 在 `L>53` 直接面对 Float64 mantissa 边界。[p.13, §4 Theoretical Setup；p.41, §7.5]
3. **稳定性条件。** `γ<1` 的 contractive bounds 与 `γ=1` 的 infinite-memory regime 使用不同保证机制。[p.31, §5.3, “Remark: The Unitary Regime”]
4. **随机特征的紧凑性**：Theorem 20 的 finite-horizon universal basis 要求 `d≥|X^L|`；Proposition 22 把 learned 与 random 的资源差异设为核心理由。[p.25–29, §5.1]
5. **实证范围**：四项任务都是小模型 synthetic probes；结论将 large-scale pre-training 写为下一步。[p.35, §7；p.42, §8, “natural next step”]
6. **比较范围**：论文把 RT 当作更广 Linear RNN/SSM 的理论 proxy，却未实测 Mamba/SSM；效率图也只测 mixer。[p.36, §7.1, “minimal theoretical proxy”；p.38, §7.3]
7. **文档结构**：没有标题为 `Limitations` 的章节、ethics/broader-impact analysis 或 deployment evaluation。[p.42–45, end of main body and references；layout observation]

### 结论编码与贡献闭环

结论依次回收问题、线性 recurrence 方法、Krohn-Rhodes/FO–W-MSO/稳定性三组理论、length generalization 的实证意义、Universal Transductor 的角色，再以大规模预训练作为 future work。它没有新的数字。值得核验的范围变化在于：p.42 用「tasks like parity and modular addition」总结经验，而 §7 的图表是 Modulo-5、其长度泛化、long addition、Base-2；没有单独 Parity 实验图。`like` 可以是类别性写法，故不把它判作错误；若把它读为已展示的 Parity run，则该经验闭环为 `open`。[p.42, §8；p.36–41, §7.1–7.5]

|引言/摘要主张|方法/理论回应|实证/结论回应|闭环|
|---|---|---|---|
|WFA sidecar 让 Transformer 获得 state tracking|Eq. (1)–(6)、Figure 2、Theorem 13 明确给出状态与组合形式。|Figure 7、8、10、11 与 §8 回收。|`closed`，在所述 architecture 定义内。|
|可越过 Parity/Modulo 的 attention-only expressivity gap|Theorem 5、6、16–19 给出构造、下界与 PNC1 上界。|Modulo-5 有实证；独立 Parity run 未出现。|`partially_closed`。|
|维持 `O(L + log T)` parallel depth|Eq. (1)、Figure 4、Eq. (49) 与 §6 推导 scan。|Figure 9 仅为 B=1 isolated mixer latency。|`partially_closed`。|
|Random Rational Features 是有效 universal basis|Theorem 20–21 给出有限 horizon 与 RKHS 条件；Proposition 22 给出 compactness gap。|没有 random-feature width/accuracy 曲线。|`closed` 作为条件化理论结果；经验效率未检验。|
|Universal head 会 autonomously select 合适 dynamics|Figure 3、direct sum 及 Krohn-Rhodes 叙述定义了候选机制。|Long addition 说「effectively routing to the Stochastic component」，没有 routing measurement 或 head ablation。|`partially_closed`。|
|长长度 robustness 可推广至实用 sequence modeling|§5.3 的 contractive/exactness 条件给出限定。|实验是四个 synthetic setting；结论把大规模预训练留作 future work。|`open` 对真实任务/大规模主张。|

## 附录、参考文献与包装职责

Appendix A 不是逐 theorem 的详细 proof appendix；它提供 Rational Power Series、linear representation、Fliess theorem、Hankel rank、图解释的背景。主文通过 p.5 的 roadmap 将其定位为基础理论，实际核心 theorem 的 proof 多在正文就地给出。Appendix B 承担 Table 2 的 task hyperparameters、optimizer/hardware、near-identity stability 与 5-seed 摘要；p.35 和 Figure 7 caption 均将完整实验设置调用到 Appendix B。[p.5, §1, “Section A reviews foundational theory”；p.35, §7；p.46–49, Appendix A–B]

因此，正文保留了设计选择、核心构造、复杂度链和所有 headline plots；可复现的 batch size、learning rate、steps、precision、部分 variance 留在 Appendix B。附录没有提供 code、data generator、raw measurements、test denominators、ablation、head-routing diagnostics 或大规模任务。A+B 共 4 页，相对于 p.3–42 的 40 页正文约为十分之一，正文在没有 Appendix B 时无法重建完整训练配置，但仍能读出任务、模型类别、主要数值与比较方向。[p.36–41, §7；p.48, Table 2]

参考文献跨 p.43–45，包含经典 automata/circuit 基础（Schützenberger、Fliess、Krohn–Rhodes、Barrington、Smolensky）、WFA learning/rational kernels，以及 Transformer/SSM 论文。它们被用于构造性与复杂性论证，而非仅在 Related Work 出现一次。[p.43–45, References；p.14–24, §4]

## 用词、修辞与可迁移规则

以 p.3–42 的提取正文为定位材料，排除 references；公式碎片和图表 caption 仍可能残留，所以以下频率只用来识别论证动作。`we prove` 5 次、`we show` 3 次、`we introduce` 4 次、`we argue` 3 次、`we propose` 2 次、`we note` 8 次、`we validate` 1 次。高频实词/短语围绕 `Rational Transductor(s)`、`rational features`、`standard Transformers`、`state tracking`、`length generalization`、`parallel scan`、`regular languages`、`expressivity`。其来源主要是领域名词与实际的理论/实验转场，未见纯模板口号。

强主张常用 `strictly`、`exact`、`guarantee`、`solve`、`complete`，集中在摘要、§4–5、Figure 7–11 与 §8。弱化语气集中在 `often`、`can`、`may`、`assuming`、`we note`，用于 attention 前提、软注意力、精度与实现边界。按段落级主断言作人工粗编码，强断言与有条件断言约为三比一。

最有效的修辞模式如下。先给一个小型 WFA 图或显式 matrix construction，再给 theorem/circuit class，最后放与该构造同形的 synthetic task。Figure 5 → Theorem 5/6 → Figure 7/8 是最清楚的一条链。[p.15–16, Figure 5 and Theorem 5–6；p.36–38, Figure 7–8]

**单一主线。** 将 input-driven 的 WFA recurrence 作为可并行 state co-processor，并把状态逐层注入 Transformer；这补上文章所称 attention 缺失的 cyclic/state-tracking inductive bias，在保留 parallel scan 的条件下解释 Regular Gap 与合成长度泛化。[p.6–10, §2；p.13–24, §4；p.36–41, §7]

**可迁移规则。** 对同时包含形式主张和经验主张的架构论文，把每个 headline capability 组织为「可执行构造/方程 → 带前提的 theorem → 匹配的任务、baseline、metric 和 uncertainty」；把容量、精度、benchmark scope 和端到端成本放在同一闭环里。该规则适用于可明确写出机制和可控制任务的工作；当目标是开放域能力、训练动态或部署效用时，synthetic construction 不能替代真实任务、消融与端到端测量。[p.25–35, §5–6；p.38, §7.3；p.42, §8]

## 自动测量核对

- 自动草稿把 appendix start 暂定为 p.44；实际 p.43–45 都是 references，Appendix A 明确从 p.46 开始。[p.43, “References”；p.46, “A Theoretical Background”]
- 自动草稿给出 53 个编号公式；实读到 Eq. (1)–(52) 连续结束于 Appendix A 的 Eq. (52)，故采用 52。[p.35, Eq. (51)；p.46, Eq. (52)]
- 自动的 main-end p.42 与物理正文结束一致；references、appendix 不计入 p.3–42 main-body 地图。[p.42, §8；p.43, References]

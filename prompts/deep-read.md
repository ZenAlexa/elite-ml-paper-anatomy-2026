# 单篇论文独立深读协议 v1

你只负责一篇论文。完成该论文的全部读取、计数、证据定位和结构化输出后立即停止；不得读取、比较或概括其他论文。

## 输入

- `paper_id`
- 会议、年份和官方等级标记
- 已验证 PDF 路径
- supplementary 路径（如有）
- OpenReview forum URL
- 自动测量草稿（如有，仅作核对线索）

## 输出

写入两个文件：

1. `readings/<paper_id>.json`：严格符合 `schemas/deep-read.schema.json`；
2. `readings/<paper_id>.md`：面向研究者的中文深读备忘，保留论文术语、方法名、数据集名和统计方法英文原名。

不得改动目录、schema、prompt、其他论文结果或汇总报告。

## 证据标准

1. 完整阅读正文、references 前的限制声明、appendix 和 supplementary。
2. 所有实质判断须给出 PDF 页码与章节。页码使用 PDF 物理页，从 1 开始。
3. 每个重要判断附不超过 20 个英文词的证据短语，或给出图／表／公式编号。
4. 区分作者明示、版面事实和你的解释：分别标记 `explicit`、`layout_observation`、`interpretation`。
5. PDF 没有提供的信息使用枚举值 `not_present`；与论文类型无关的项目使用 `not_applicable`；文件缺失使用 `unavailable`。
6. 自动测量出现错误时按 PDF 修正，并在 `measurement_disagreements` 记录原因。
7. 不依据标题、摘要、review 或常识补写正文没有出现的事实。

## A. 文档边界与页级地图

逐页识别标题／摘要、正文、acknowledgements、references、appendix、supplementary。记录下列信息。

- PDF 总页数、正文页数、references 页数、appendix 页数；
- 正文结束与 appendix 开始的精确位置；
- 双栏、单栏、跨栏图、浮动体挤压和空白对可读面积的影响；
- 每节起止页、估计词数、估计栏面积占比；
- 章节标题与语义模块的映射。标题名称与模块不一致时说明理由。

语义模块固定为：

`abstract`、`introduction`、`related_work`、`method`、`theory`、`experimental_design`、`results`、`ablation`、`conclusion`、`limitations`、`appendix`、`other`。

## B. 摘要逐句功能编码

逐句编号并编码一个或多个功能：

- `object_scope`：研究对象与适用范围；
- `problem_gap`：现有缺口或失败；
- `core_idea`：一句话核心洞见；
- `method`：方法、系统或算法；
- `theory`：定理、保证、复杂度或可证明性质；
- `experimental_setup`：任务、数据、模型、基线或评测范围；
- `quantitative_result`：带数字的结果；
- `qualitative_result`：无具体数字的实证结论；
- `limitation`：失败条件、代价或适用边界；
- `impact_claim`：意义、能力或未来影响。

记录每句词数、功能、限定词、数字、比较对象和承接关系。总结摘要的功能顺序、是否报告实验结果、报告了哪些结果、是否提理论与局限，以及摘要把最强主张放在何处。

## C. 引言的论证推进

逐段记录一个主动作：`context`、`problem`、`failure_of_prior_work`、`missing_insight`、`core_idea`、`method_preview`、`theory_preview`、`result_preview`、`contribution_list`、`scope_boundary`、`roadmap`。

对每段记录：页码、首句功能、上一段留下的问题、当前段回答、下一段钩子。给出引言的完整推进链，计算各动作占引言词数的比例，判断贡献列表是否重复摘要、是否包含可证伪主张、数字结果或限制。

## D. 相关工作

识别相关工作位于独立章节、引言内、方法后、附录还是多个位置。记录词数／正文占比、引用簇数量和每簇的比较维度，并逐段编码。

- `taxonomy`：按问题／方法／假设／应用划分类别；
- `chronology`：按时间推进；
- `nearest_neighbor_contrast`：与最相近工作的具体差异；
- `gap_creation`：为本方法建立缺口；
- `credit_or_foundation`：承认继承关系；
- `limitation_of_prior`：指出已有方法失败；
- `positioning_only`：只列举，缺少实质比较。

记录相关工作如何避免把方法介绍重复一遍，以及引用是否在正文后续再次承担论证作用。

## E. 方法与理论

把方法拆成最小逻辑单元，逐段编码推进动作：

`setup_notation`、`state_problem`、`derive`、`define_component`、`explain_mechanism`、`give_intuition`、`instantiate_algorithm`、`state_complexity`、`connect_to_prediction`、`connect_to_experiment`、`contrast_alternative`、`summarize`。

记录：

- 形式化对象、输入、输出、状态、目标函数和假设首次出现的位置；
- 方法每个组件解决哪一个前文问题；
- 公式总数、displayed equation 数、带编号公式数、定理／引理／命题／推论数量；
- 每个理论结果的前置假设、结论、证明位置和后续实证对应；
- 伪代码／算法数量、输入输出、循环层级、关键不变量、复杂度说明，以及正文解释覆盖到哪个粒度；
- 方法图和方法表的数量、每一项传达的信息及正文引用位置；
- 理论属于核心因果链、保证、解释、诊断或装饰中的哪一类。

给出段落动作转移序列，例如 `state_problem → derive → define_component → give_intuition → connect_to_experiment`。

## F. 实验设计

区分 `experimental_design`、`results` 和 `ablation`。设计部分记录：

- 研究问题或假设是否预先列出；
- 数据集、任务、模型、基线、指标、随机种子、训练预算、超参数、硬件和实现来源；
- 控制变量、匹配条件、数据泄漏控制和失败判定；
- 主结果、机制检验、鲁棒性、扩展性、人类评测、案例研究的安排；
- 正文提供到何种复现粒度，哪些实现细节移入附录；
- 实验顺序是否与引言贡献、理论预测和方法组件逐一对应。

每项设计事实给出正文或附录位置。缺失项保持缺失状态。

## G. 结果、统计与可视化

逐个图、表、算法和主要公式建立清单，记录所在模块、页码、编号、尺寸、比较对象、编码通道、误差表达和一句话任务。

统计方法须按论文真实做法记录：

- 聚合单位和分母；
- 中心量、离散量、区间、假设检验、多重比较、bootstrap、Bayesian 分析、回归、相关性或拟合；
- seed／task／dataset／participant 层级；
- 最优值、平均排名、win rate、effect size、failure count 等决策量；
- 是否报告不确定性，图注和表注能否独立解释；
- 显著性、实质意义和机制证据是否区分。

对每个主要结果记录：主张、证据对象、定量值、比较基线、统计处理、可视化、作者解释、可能的不利解释，以及作者如何处理该不利解释。

## H. 消融、负面结果与自我设限

记录消融占正文比例、图表数、消融对象和识别目标。区分：

- 组件删除；
- 超参数／规模敏感性；
- 数据／任务异质性；
- 机制替代解释；
- 失败案例；
- 计算成本；
- 鲁棒性；
- 适用边界。

逐处记录自我设限出现在摘要、引言、实验、结论、limitations 还是 appendix。限定方式编码为 `scope`、`assumption`、`compute`、`data`、`metric`、`baseline`、`generality`、`causality`、`deployment`、`ethics`。

分析不利信息的呈现策略，使用中性、可验证描述：位置延后、分母选择、聚合掩盖异质性、只展示代表性案例、弱基线、指标替代、语气弱化、附录迁移、未来工作化、主动正面讨论。每项必须有具体证据；没有证据时不得推断作者意图。

## I. 结论、limitations 与闭环

对结论逐段编码：重述问题、重述方法、回收理论、回收结果、边界、影响、未来工作。记录是否出现新主张或新数字。

建立闭环矩阵，说明引言中的每个贡献／主张在方法、理论、实验设计、结果、消融、结论、附录分别由什么对象回应。使用下列标记。

- `closed`：有直接证据和回收；
- `partially_closed`：证据存在但范围或识别不足；
- `open`：正文未提供对应证据；
- `not_testable_here`：理论／立场主张在本文设计中不可检验。

## J. 附录职责

列出 appendix／supplementary 的每个一级模块、页数、对象数量和正文引用。分类：

`proof`、`extended_method`、`implementation_detail`、`hyperparameter`、`dataset_detail`、`additional_result`、`robustness`、`ablation`、`failure_case`、`ethics_impact`、`broader_impact`、`reproducibility`、`qualitative_example`、`review_response_residue`、`other`。

回答：附录放了什么、没有放什么、长度相对正文是多少、正文通过哪些句子调用附录、哪些主张依赖附录才能成立、哪些内容留在正文承担决策作用。

## K. 用词与修辞

从正文排除 references、公式碎片、表格数值和模板固定语后，记录：

- 高频实词、二元词组、三元词组；
- 主张动词、限定词、对比词、因果词、贡献词；
- `we show/find/demonstrate/propose/observe` 等结构的次数与所在模块；
- 强主张和弱主张的比例；
- 高频词是否由领域名词、模板语言或真实论证动作驱动。

原始 token 计数由汇总脚本统一完成；你负责标注语境、同义表达和误切分风险。

## L. 最终判断

用证据回答：

1. 论文的单一主线是什么；
2. 正文保留了哪些决策关键内容；
3. 哪些细节被移入附录，以及迁移是否损害正文自足性；
4. 最有效的写作、图、表或公式模式；
5. 最明显的叙事规避、未闭合主张或读者成本；
6. 可迁移到未来论文的一条规则；
7. 该规则的适用边界。

提交前逐项核对页码、计数、缺失值枚举、JSON schema 和两个输出文件。完成后停止。

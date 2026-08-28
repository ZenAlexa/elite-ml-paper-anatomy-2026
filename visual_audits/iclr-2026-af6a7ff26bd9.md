# Visual Audit: iclr-2026-af6a7ff26bd9

## 审计范围与清单对账
本轮只审计 `paper_id=iclr-2026-af6a7ff26bd9`（*P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling*）。PDF `corpus/pdfs/iclr-2026-af6a7ff26bd9.pdf` 是 Figure/Table 清单事实源：29 个 physical Letter pages，正文 pp.1–10，acknowledgments/references pp.11–13，附录 pp.14–29；逐页核对得到正文 Figure 1–4、Table 1–5，附录 Figure 5–15、Table 6–15。附录 p.22 的 Algorithm 1 已读但不是 Figure/Table，按 schema 不另计。
PDF 全 29 页先以 200 dpi 渲染（`/tmp/iclr_af6_render200/page-01.png`–`page-29.png`，1700×2200，超过要求的 180 dpi），再用 contacts 和逐对象 page render 检查布局、字体、颜色、plot grammar、caption/header、统计表达与 evidence relation。PDF p.1–29 均检查以确认 references/appendix 无漏计对象。
本审计沿用此前同论文 Markdown 草稿所需字段，但以 PDF 当前渲染逐对象复核；下面的颜色、图内字号、线宽和 raster/vector 判断在未有精确绘图源时标为 rendered estimate，不冒充 source-exact。

|对象|PDF 页|模块|布局|
|---|---:|---|---|
|Figure 1|2|introduction|main / page_width|
|Figure 2|4|method|main / page_width|
|Figure 3|9|prototype_analysis|main / page_width|
|Figure 4|10|prototype_analysis|main / page_width|
|Figure 5|15|prototype_analysis|appendix / page_width|
|Figure 6|16|qualitative_analysis|appendix / page_width|
|Figure 7|17|qualitative_analysis|appendix / page_width|
|Figure 8|18|prototype_analysis|appendix / page_width|
|Figure 9|23|prompt_templates|appendix / page_width|
|Figure 10|24|prompt_templates|appendix / page_width|
|Figure 11|25|prompt_templates|appendix / page_width|
|Figure 12|26|prompt_templates|appendix / page_width|
|Figure 13|27|prompt_templates|appendix / page_width|
|Figure 14|28|prompt_templates|appendix / page_width|
|Figure 15|29|prompt_templates|appendix / page_width|
|Table 1|8|results|main / page_width|
|Table 2|8|ablation|main / single_column|
|Table 3|8|persona_comparison|main / single_column|
|Table 4|9|scaling_analysis|main / single_column|
|Table 5|10|ood_generalization|main / single_column|
|Table 6|14|preliminary_persona|appendix / page_width|
|Table 7|15|reward_settings|appendix / single_column|
|Table 8|16|prototype_distribution|appendix / page_width|
|Table 9|16|prototype_distribution|appendix / page_width|
|Table 10|17|macro_accuracy|appendix / page_width|
|Table 11|19|efficiency|appendix / single_column|
|Table 12|20|feedback_sensitivity|appendix / page_width|
|Table 13|20|prototype_sensitivity|appendix / page_width|
|Table 14|21|policy_training|appendix / single_column|
|Table 15|21|policy_training|appendix / page_width|

清单对账结论：Figure 1–15、Table 1–15 的标签和页码与 PDF 一致；Algorithm 1（p.22）仅保留在范围说明中。

## 源核查与来源角色
- **PDF/reading**：本地已验证 PDF 为对象事实源；reading JSON/MD 的 visual_inventory、caption 与正文/附录叙事逐项回读。PDF 首页链接 OpenReview `https://openreview.net/forum?id=hXNApWLBZG`、proceedings `https://proceedings.iclr.cc/paper_files/paper/2026/file/73bda9a20f6f9f6074ce822e76f126bb-Paper-Conference.pdf` 和作者仓库 `https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/Character-GenRM`。
- **source inventory/local visual source**：`reports/tables/visual_source_inventory.csv` 对该 paper 已标记 `partial_visual_source`，自动候选为 `Tongyi-ConvAI/Qwen-Character`；`corpus/visual_sources/iclr-2026-af6a7ff26bd9/` 存在但为空，本轮不修改 inventory。
- **GitHub**：已用 `gh auth status`、`gh repo view`/tree、`unicli search` 与 `agent-reach doctor --json` 核查作者仓库；当前 main commit 为 `be552f7a1a063304311fb8f28e10d47d815a9ac4`。`assets/workflow.png`、`training.png`、`evaluation_chain.png` 分别与 PDF Figure 1、Figure 2(a)、Figure 2(b) 视觉匹配，故 source role 为 `rendered_asset`、证据标为 source_exact；`comparative_results.png`/`scaling_generalization.png` 仅是 README release visuals，未冒充 PDF Table/Figure exact source。
- **源码边界**：读取 `inference/PROMPTS.py`、`prototype_learning/scaling_with_proto.py`、`proto_knn_scaler.py` 与 README；它们支持 prompt/prototype semantics，却没有 Figure 3–15 或 Table 1–15 的完整 generator、TeX/TikZ、导出数据和可重现 exact plot/table pipeline。因此 source status 维持 `partial_visual_source`。

## 全文视觉风格
- **字体/版式**：PDF `pdffonts` 显示 Nimbus Roman No9 L、Computer Modern math、NimbusMonL-Regu，并嵌有 CambriaMath/TimesNewRoman/Calibri/DengXian/SegoePrint-like raster text；正文/附录均为双栏 Letter shell，caption 置于对象下方，表格多为 booktabs/minimal。
- **颜色**：workflow 使用浅蓝/浅橙/浅灰 block；定量图使用蓝/橙 series；cluster/user 图用蓝 shared 与红 individual；prompt cards 使用深蓝 header。表格依靠黑白、粗体、下划线和破折号。颜色有文字/位置/形状冗余，但 cluster 和 prompt raster 在灰度/缩印下仍存在识别负担。
- **统计边界**：主 Tables 1–4 明示 5-run mean±standard error；Table 5 与大量 appendix tables/figures 不在对象内给 denominator 或 spread。Table 14 的 mean/SE/95% CI 与 Table 15 raw runs 属于 appendix policy analysis，按论文结构记录，不外推为主文统计。

## Figure 逐对象审计
### Figure 1 (p.2 / introduction)
- **布局/类型/职责**：`main`，`page_width`；types=`pipeline, architecture, conceptual_diagram`；purpose=`headline, method_interface, theory_mechanism`；complexity=5/5（panels=1，series=None，legend_items=0，annotations≈28，marks≈30）。
- **Caption（PDF 原文）**：*Figure 1: Workflow of P-GenRM. P-GenRM infers a scenario-specific user persona and preference analysis from hybrid preference signals, generates dynamic scoring rubrics, and assesses candidate responses accordingly. At test-time, P-GenRM can aggregate multiple individual-level scoring schemes and incorporate similar users’ preferences to improve scoring accuracy and generalization.*（47 words；moves=`title, setup, encoding_key, main_finding`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 5.5–10 pt（median 7.2）；weight=`regular, bold`；style=`roman, italic`；provenance=`mixed`，confidence=`high`。
- **Color**：mode=`mixed`，约 6 colors，HEX=`#F2F2F2, #D9EAF7, #F6E7CB, #F4B183, #70AD47, #3778B2`；浅灰/浅蓝/浅橙块区分输入、用户或 prototype、persona/rubric 与 scoring chain；蓝/绿箭头和直接文字补充流程含义。 grayscale_safe=True，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/3；refs=0；hatching=False；uncertainty=`none`；line_width=1.0 pt；provenance=`mixed`。
- **Encodings**：`{"x": "从混合 preference signals 到 response ranking 的左到右流程", "y": null, "color": "user/profile、prototype、persona、rubric 和 scoring/evaluation chain 的浅色模块", "shape": "rounded boxes, user icons, document/cards and arrows", "line": "solid directed arrows with feedback/test-time branches", "facet": "offline preference/prototype preparation versus test-time individual/prototype scaling", "text": "P-GenRM, persona, scoring rubric, candidate response and aggregation labels"}`
- **Data/statistics**：概念 pipeline；没有坐标、样本聚合或不确定性。图中 offline prototype/user construction、scenario-specific persona/rubric generation、candidate scoring 和 test-time individual/prototype aggregation 是接口示意，而非 measured marks。
- **Evidence relation**：Introduction 的 sparse/noisy/scenario-varying preference problem → Figure 1 给出 persona–rubric–judge 主线 → Tables 1–4 将各阶段映射到 benchmark、ablation、persona 和 scaling results。
- **设计优点：
  - 把离线 preference modeling、动态 persona/rubric 与测试时 scaling 串成单一左到右路径。
  - 同一图同时展示 individual 与 prototype 级别的 aggregation，直接对应方法的可扩展性主张。
  - 颜色、模块形状和箭头共同表达阶段，不依赖复杂图例。
- **设计弱点：
  - “improve scoring accuracy and generalization”是 caption finding，但图内没有实验数字或不确定性。
  - 流程框中文字较小，离线/测试时边界和多个反馈箭头在双栏缩放后需要细读。
  - prototype 与 individual 的视觉差异主要依赖小标签，灰度打印中层次变弱。
- **可复用模式**：用离线信号→persona/rubric→candidate judgment→test-time aggregation 的阶段化流程图建立全文视觉索引，并把定量结论留给相邻结果表。
- **Evidence**：p.2；basis=`source_exact`；Figure 1。

### Figure 2 (p.4 / method)
- **布局/类型/职责**：`main`，`page_width`；types=`pipeline, architecture, conceptual_diagram`；purpose=`method_interface, experimental_design, theory_mechanism`；complexity=5/5（panels=2，series=None，legend_items=0，annotations≈26，marks≈34）。
- **Caption（PDF 原文）**：*Figure 2: (a) The three-stage training framework of P-GenRM (b) An illustration of the personalized evaluation chain, showing how preference modeling and derived scoring schemes lead to interpretable, criterion-weighted judgments for responses.*（32 words；moves=`title, setup, encoding_key`；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 5.5–9.5 pt（median 7.0）；weight=`regular, bold`；style=`roman, italic`；provenance=`mixed`，confidence=`high`。
- **Color**：mode=`mixed`，约 6 colors，HEX=`#F2F2F2, #D9EAF7, #F6E7CB, #F4B183, #70AD47, #3778B2`；浅灰/浅蓝/浅橙块区分输入、用户或 prototype、persona/rubric 与 scoring chain；蓝/绿箭头和直接文字补充流程含义。 grayscale_safe=True，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/3；refs=0；hatching=False；uncertainty=`none`；line_width=1.0 pt；provenance=`mixed`。
- **Encodings**：`{"x": "(a) training stage order; (b) evaluation chain order", "y": null, "color": "training/data/persona/rubric/scoring blocks and blue-green directed arrows", "shape": "stage boxes, persona/rubric cards, candidate-response cards and score outputs", "line": "solid arrows, nested boxes and stage separators", "facet": "(a) three-stage training framework versus (b) personalized evaluation chain", "text": "stage names, preference signals, criteria/weights, score and explanation"}`
- **Data/statistics**：双 panel conceptual diagram：(a) 展示 P-GenRM 的三阶段 training framework；(b) 展示从 preference modeling、persona/rubric derivation 到 criterion-weighted judgment 的 evaluation chain。无坐标、样本数或 uncertainty，文字和箭头是结构编码。
- **Evidence relation**：Figure 1 的 end-to-end workflow → Figure 2 分解 training 与 evaluation interfaces → Tables 1–3 测量训练后的 reward model 与 persona induction，Figures 6–7 展示生成的 qualitative rubrics。
- **设计优点：
  - (a)/(b) 用同一视觉语言把训练管线和推理时评价链并置。
  - 把“criterion-weighted”从抽象主张变成 rubric/score cards 和箭头关系。
  - panel 标题、模块内文本和流程方向形成多重可读线索。
- **设计弱点：
  - 两个 panel 都没有标出输入规模、loss/step 或 score aggregation 的数值。
  - 训练框架与 evaluation chain 的共享色彩使两者边界依赖 panel 字母和小标题。
  - 大量小文本和嵌套卡片在 page-width 缩放后信息密度高。
- **可复用模式**：将 training stages 与 personalized evaluation chain 置于同一页宽图中，用同构卡片和箭头连接方法接口与解释性输出。
- **Evidence**：p.4；basis=`source_exact`；Figure 2。

### Figure 3 (p.9 / prototype_analysis)
- **布局/类型/职责**：`main`，`page_width`；types=`line, bar`；purpose=`experimental_design, robustness, main_comparison`；complexity=4/5（panels=2，series=4，legend_items=2，annotations≈8，marks≈25）。
- **Caption（PDF 原文）**：*Figure 3: Determination of prototype numbers and their effect on scaling performance. Left: retained variance ratio as a function of the number of singular vectors on Chatbot Arena and PRISM. Right: performance of P-GenRM with different prototype numbers.*（38 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 5.5–9.0 pt（median 7.0）；weight=`regular, bold`；style=`roman, italic`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`categorical`，约 4 colors，HEX=`#2F75B5, #ED7D31, #4472C4, #A5A5A5`；蓝、橙和灰色区分数据集、prototype 数量或统计曲线；坐标、panel 位置和直接标签提供颜色以外的线索。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`categorical/linear`；grid=`both`；legend=`True`（placement=panel-local upper area，shared=False）；direct_labels=True；markers/line_styles=2/2；refs=0；hatching=False；uncertainty=`none`；line_width=1.0 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": "left: number of singular vectors; right: prototype count {0,25,50,100,125}", "y": "left: retained variance ratio; right: Chatbot Arena/PRISM performance", "color": "dataset and performance series (blue/orange)", "shape": "points/lines for retained variance and scaling curves", "line": "solid line segments joining ordered prototype settings", "facet": "left variance-selection plot and right performance-vs-prototypes plot", "text": "dataset labels, prototype counts, retained variance and accuracy values"}`
- **Data/statistics**：左 panel 是 retained variance ratio 随 singular vectors 的曲线；右 panel 是 prototype count 0/25/50/100/125 对 Chatbot Arena 与 PRISM performance 的影响。点估计无误差带；正文给出 50 prototypes 的选择理由，约 50 处达到 74.30/67.54，100/125 后趋于 plateau 或轻微下降。
- **Evidence relation**：Section 5.3 的 prototype-number selection → Figure 3 将 PCA/variance 与 test-time scaling 置于同一对象 → Table 4 给出各 Ind/Pro 组合，Tables 8–9 给出 prototype sample/accuracy distribution。
- **设计优点：
  - 左侧选择依据与右侧性能响应共享 prototype 轴语义，支持一个明确的设计决策。
  - 两条数据集曲线、panel labels 和直接 x tick 使趋势可扫描。
  - 图与正文的 50-prototype decision 以及 Appendix Tables 8–9 形成可追踪链路。
- **设计弱点：
  - 左右 panel 的 y 量纲不同，caption 没有说明右侧是否共享 y-axis 或误差定义。
  - 曲线点数少且没有 seed/spread，plateau 与下降的稳定性无法从图中判断。
  - 颜色是 dataset/metric 的主要区分手段，灰度和小字号下 legend 负担较高。
- **可复用模式**：把容量/表示选择曲线与 downstream performance 曲线并置，明确选点理由，并在附录用分布统计表补足稳定性。
- **Evidence**：p.9；basis=`rendered_observation`；Figure 3。

### Figure 4 (p.10 / prototype_analysis)
- **布局/类型/职责**：`main`，`page_width`；types=`scatter, qualitative_grid, other`；purpose=`qualitative_evidence, theory_mechanism, method_interface`；complexity=4/5（panels=2，series=None，legend_items=0，annotations≈18，marks≈45）。
- **Caption（PDF 原文）**：*Figure 4: Visualization of User–prototype distributions and representative preference patterns. Blue highlights show shared intra-group preferences, red highlights show individual diversity. Distinct clusters capture inter-group heterogeneity, validating prototype-based modeling.*（29 words；moves=`title, setup, encoding_key, main_finding`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 5.0–9.0 pt（median 6.8）；weight=`regular, bold`；style=`roman, italic`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 5 colors，HEX=`#2F75B5, #C00000, #A5A5A5, #70AD47, #FFC000`；蓝色高亮 shared intra-group preference，红色高亮 individual variation；中性灰与其他散点/文字构成群组和文本层。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": "2-D user–prototype layout (coordinates not labelled)", "y": "2-D proximity to prototypes (coordinates not labelled)", "color": "blue shared preference phrases, red individual-diversity phrases and neutral clusters", "shape": "prototype labels (P36/P46/P15/P49/P40/P8/P2/P7) and user/cluster marks", "line": "none; spatial proximity and text connectors imply grouping", "facet": "cluster distribution at left and representative preference text at right", "text": "prototype IDs and highlighted preference phrases"}`
- **Data/statistics**：定性 scatter/cluster visualization 与右侧 preference-pattern text panels；prototype IDs 和 cluster proximity 是结构编码。没有坐标单位、样本数、聚类指标或 uncertainty；blue shared 与 red individual highlights 只支持机制解释，不是 aggregate accuracy。
- **Evidence relation**：Section 5.3 的 user–prototype case study → Figure 4 说明 intra-group commonality、individual variation 与 inter-group heterogeneity → Table 4 scaling combinations、Figures 6–8 的 persona/cluster examples。
- **设计优点：
  - 空间聚类和文本例子并置，使 prototype grouping 与 preference semantics 互相解释。
  - 蓝/红高亮与 cluster labels 对“shared vs individual”提供直接视觉 key。
  - caption 明示 inter-group heterogeneity，避免把点云当作未解释的 embedding plot。
- **设计弱点：
  - 坐标轴、sample count 和 cluster assignment rule 均未编码，视觉距离不能独立支撑 clustering validity。
  - 右侧长文本占据大量面积且字号小，个别 phrases 在缩印后难以追踪。
  - 蓝红语义在灰度和色觉差异下不稳，虽有文字位置冗余但仍依赖颜色高亮。
- **可复用模式**：用 embedding/cluster scatter 配合代表性文本卡片，把群组结构与可解释 preference pattern 同页呈现，并把聚类可靠性留给定量附录。
- **Evidence**：p.10；basis=`rendered_observation`；Figure 4。

### Figure 5 (p.15 / prototype_analysis)
- **布局/类型/职责**：`appendix`，`page_width`；types=`bar, line`；purpose=`main_comparison, robustness, experimental_design`；complexity=4/5（panels=1，series=2，legend_items=0，annotations≈7，marks≈52）。
- **Caption（PDF 原文）**：*Figure 5: The number of samples assigned to each prototype and the corresponding performance of P-GenRM across them.*（18 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 5.0–8.5 pt（median 6.6）；weight=`regular, bold`；style=`roman, italic`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 2 colors，HEX=`#1F77B4, #E53935`；蓝柱表示每个 prototype 的样本数，红线表示对应准确率；左右 y-axis 标签和数据位置重复编码。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`categorical/unknown`；grid=`y`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=1/1；refs=0；hatching=False；uncertainty=`none`；line_width=1.0 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": "prototype IDs ordered by assigned-sample count", "y": "left: number of assigned samples; right: prototype-level accuracy", "color": "blue bars for sample count and red line for accuracy", "shape": "rectangular bars and circular/line points", "line": "red accuracy trajectory across prototypes", "facet": null, "text": "prototype IDs, left/right axis labels and accuracy/sample values"}`
- **Data/statistics**：双 y-axis bar+line chart；50 prototype bins 的 sample count 从约 930、904、410、352、266 下降到约 18，红线展示各 prototype accuracy（约 0.58–0.75）。这是 distribution/heterogeneity view，无 error bars、样本级分布或准确率置信信息。
- **Evidence relation**：Appendix A.11 的 sample requirement 与 Figure 3 的 prototype count choice → Figure 5 展示 fixed 50 prototypes 内的 load imbalance/accuracy → Tables 8–9 以 summary statistics 检查同一对象。
- **设计优点：
  - 双轴将 prototype load 与 performance 同时展示，能看出不均衡样本量并不自动等价于 accuracy。
  - 按样本量排序比原始 prototype ID 更利于识别长尾。
  - 图和 Tables 8–9 共享 prototype-level view，便于从视觉分布回到统计摘要。
- **设计弱点：
  - 双轴提高解读风险，caption 没有解释哪条 y-axis 对应哪个量或 prototype order。
  - accuracy 线可能把离散 prototypes 误读为连续趋势，且无样本权重/误差。
  - 52 个 x 类别或密集标签在 appendix page-width 下非常拥挤。
- **可复用模式**：在同一 prototype index 上叠加容量柱和质量线，先按负载排序，再用表格报告长尾和 accuracy 分布；双轴必须配清晰 axis key。
- **Evidence**：p.15；basis=`rendered_observation`；Figure 5。

### Figure 6 (p.16 / qualitative_analysis)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, qualitative_grid, other`；purpose=`qualitative_evidence, method_interface`；complexity=4/5（panels=1，series=None，legend_items=0，annotations≈20，marks≈None）。
- **Caption（PDF 原文）**：*Figure 6: A single user’s preference analysis under music recommendation setting*（11 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 5.0–9.0 pt（median 6.4）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue section headers and pale card backgrounds", "shape": "prompt/response text blocks and rubric rows", "line": "card borders and indentation lines", "facet": "query, inferred persona, preference analysis and weighted rubric sections", "text": "Can you recommend music?, persona prose, criteria names and weights"}`
- **Data/statistics**：单用户 qualitative prompt card；query 为 “Can you recommend music?”；内容显示 inferred persona/preferences 与 rubric：Helpfulness/Specificity 30、Factuality/Correctness 20、Fluency/Clarity 15、Creativity/Depth 10、Diversity/Breadth 10、Values Alignment/Openness 10、Safety/Tone 5。没有样本汇总或统计量。
- **Evidence relation**：正文说 Figures 6–7 展示 non-cherry-picked user 的 scenario-varying preference → Figure 6 给 music setting 的可解释 persona/rubric example → Figure 2(b) evaluation chain 与 Figure 9–11 prompt templates 提供 implementation context。
- **设计优点：
  - 把 scenario-specific persona、rubric criteria 与 weights 放在一张可读的 prompt card 中。
  - 权重合计 100 的结构使 scoring scheme 具备可审计的内部约束。
  - 蓝 header、分层文本和 criteria rows 在无坐标对象中提供清晰阅读顺序。
- **设计弱点：
  - 单一用户案例不能估计总体 preference fidelity 或代表性，caption 也未注明 user sampling rule。
  - 大段文字和多级 criteria 在 PDF appendix 缩放下难以逐词核对。
  - 缺少 query response、judge output 或 before/after comparison，无法独立验证 rubric 的效用。
- **可复用模式**：用可复用的 scenario→persona→weighted rubric card 展示 qualitative mechanism，但要把单例严格标为 case study 并配 aggregate evidence。
- **Evidence**：p.16；basis=`rendered_observation`；Figure 6。

### Figure 7 (p.17 / qualitative_analysis)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, qualitative_grid, other`；purpose=`qualitative_evidence, method_interface`；complexity=4/5（panels=1，series=None，legend_items=0，annotations≈20，marks≈None）。
- **Caption（PDF 原文）**：*Figure 7: A single user’s preference analysis under serious discussion setting*（11 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 5.0–9.0 pt（median 6.4）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue headers, pale cards and black/gray prose", "shape": "question, persona, criterion and rubric text blocks", "line": "card borders and indentation", "facet": "serious-discussion query, inferred persona and weighted criteria", "text": "moral-responsibility query, persona descriptors, criteria and weights"}`
- **Data/statistics**：单用户 serious discussion qualitative prompt card；query 为 “Are people really responsible for their immoral actions?”；rubric weights 为 Helpfulness/Depth 30、Factuality/Nuance 25、Fluency/Clarity 20、Philosophical Engagement/Openness 15、Values Alignment/Tone 5、Safety 5。无 aggregate/statistical layer。
- **Evidence relation**：与 Figure 6 形成跨场景 case pair → Figure 7 显示同一 pipeline 可生成不同 rubric emphasis → Figure 2、Tables 3/6 和 prompt source 支持 adaptive persona interpretation。
- **设计优点：
  - 与 Figure 6 共用 card grammar，跨场景差异来自 query 和 criterion weights 而非装饰。
  - 直接展示 Depth/Nuance/Philosophical Engagement 等 broader preference space，响应论文的 interpretability claim。
  - 层级标题和权重数字保留了从问题到评分标准的推理路径。
- **设计弱点：
  - 仍是一个用户的定性样例，不能替代用户群体上的 calibration 或 generalization。
  - caption 不说明是否与 Figure 6 使用同一 user/history，跨图比较存在选择不确定性。
  - 长文本和弱对比背景容易在小字号下丢失 criterion boundaries。
- **可复用模式**：用同构 qualitative cards 对比不同 scenario 的 dynamic rubric；在 caption 或表格中明确 user/history selection 与量化验证。
- **Evidence**：p.17；basis=`rendered_observation`；Figure 7。

### Figure 8 (p.18 / prototype_analysis)
- **布局/类型/职责**：`appendix`，`page_width`；types=`scatter, qualitative_grid, other`；purpose=`qualitative_evidence, theory_mechanism, robustness`；complexity=5/5（panels=2，series=None，legend_items=0，annotations≈26，marks≈70）。
- **Caption（PDF 原文）**：*Figure 8: Visualization of user–prototype distributions and representative preference patterns. Each cluster corresponds to a learned prototype, around which users with similar preferences are grouped. (1) Within the same cluster, users share common preferences (highlighted in blue), yet also exhibit subtle variations and diversity (highlighted in red). (2) Across different clusters, users demonstrate clearly distinct preference tendencies, underscoring the effectiveness of prototype-based modeling for capturing both intra-group commonality and inter-group heterogeneity.*（71 words；moves=`title, setup, encoding_key, main_finding`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math, NimbusMonL-Regu, Cambria Math`；约 4.8–8.8 pt（median 6.5）；weight=`regular, bold`；style=`roman, italic`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 5 colors，HEX=`#2F75B5, #C00000, #A5A5A5, #70AD47, #FFC000`；蓝色高亮 shared intra-group preference，红色高亮 individual variation；中性灰与其他散点/文字构成群组和文本层。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`mixed`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": "2-D user/prototype layout with unlabeled embedding coordinates", "y": "2-D embedding proximity with unlabeled units", "color": "blue shared statements, red individual variations, neutral cluster points", "shape": "prototype labels, user dots and text callout blocks", "line": "none; visual proximity defines cluster membership", "facet": "scatter/cluster distribution and representative preference-pattern panels", "text": "P# prototype IDs and blue/red highlighted preference phrases"}`
- **Data/statistics**：Figure 4 的扩展版 qualitative cluster visualization；多个 learned prototypes（如 P36、P46、P15、P49、P40、P8、P2、P7、P37、P6、P34、P47、P27、P1、P17、P13、P5）周围放置用户，旁侧文本分 shared/individual preferences。无坐标、聚类质量、sample denominator 或 uncertainty。
- **Evidence relation**：Appendix A.8 具体化正文 Figure 4 的 case study → Figure 8 扩展 prototype coverage 与 preference heterogeneity → Figure 5/8–9 以及 Tables 8–9 提供 prototype load/accuracy 语境。
- **设计优点：
  - 比正文 Figure 4 覆盖更多 prototypes，能显示 cluster-level heterogeneity 的范围。
  - blue/red text highlighting 将 shared commonality 与 individual diversity 从点云中解释出来。
  - caption 以 numbered (1)/(2) 组织 within- 与 across-cluster reading order。
- **设计弱点：
  - embedding coordinates 和 cluster algorithm 未定义，读者不能从图独立复现 grouping。
  - 对象同时包含密集 scatter 与长文本，视觉层次和字号在附录 page-width 下紧张。
  - qualitative examples 的选择和 prevalence 未报告，不能单独支撑 prototype accuracy claim。
- **可复用模式**：以扩展 cluster map + representative text cards 作为可解释性审计对象，同时将 sampling、cluster metric 与 aggregate accuracy 放在邻接表格。
- **Evidence**：p.18；basis=`rendered_observation`；Figure 8。

### Figure 9 (p.23 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈12，marks≈None）。
- **Caption（PDF 原文）**：*Figure 9: Prompt of Explicit Preference Synthesis.*（7 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue prompt title bar, black text on light card", "shape": "code-like prompt blocks", "line": "border/indentation separators", "facet": null, "text": "instruction, input placeholders and synthesis output requirements"}`
- **Data/statistics**：prompt screenshot/template，展示 Explicit Preference Synthesis 的 system/user instruction 和 input/output placeholders；没有 measured observations、sample counts、uncertainty 或 plot axes。
- **Evidence relation**：Appendix prompt inventory → Figure 9 defines explicit preference synthesis before Figures 10–12 的 scoring/rubric prompts → Figure 1/2 的 persona and preference-signal stages。
- **设计优点：
  - 把 prompt content 当作方法接口而非装饰截图，便于读者定位输入/输出约束。
  - 统一 blue header/card grammar 与 Figures 10–15，形成可检索的 template family。
- **设计弱点：
  - 代码字体、换行和小字号依赖 raster rendering，复制/复用困难。
  - caption 只给标题，不说明变量替换规则、模型、版本或 exact prompt source。
  - 缺少 prompt ablation or example output，不能由图判断其对结果的增量。
- **可复用模式**：用统一 prompt-card family 展示阶段化 instruction templates，须在源仓库保留可复制文本和版本绑定。
- **Evidence**：p.23；basis=`rendered_observation`；Figure 9。

### Figure 10 (p.24 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈13，marks≈None）。
- **Caption（PDF 原文）**：*Figure 10: Prompt of Persona-guided Scoring Induction.*（7 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue section header, light prompt body, dark text", "shape": "instruction paragraphs, persona/rubric placeholders and output block", "line": "card borders/indentation", "facet": null, "text": "persona induction instruction, user history and scoring criteria fields"}`
- **Data/statistics**：prompt template 展示 Persona-guided Scoring Induction 的 prompt structure：history/preference signals → inferred persona → scoring rubric/criteria output。无坐标、数据 marks 或 uncertainty。
- **Evidence relation**：Figure 2(b) personalized evaluation chain 的 persona stage → Figure 10 给出可执行的 induction interface → Table 3 对比 adaptive PSI 与 static SMe，Figures 6–7 展示其 qualitative outputs。
- **设计优点：
  - 把 adaptive persona induction 的输入和输出槽位分开，直接对应论文的 dynamic-persona claim。
  - 与其他 prompt figures 共用布局，便于逐阶段核查。
- **设计弱点：
  - 模板截图没有显示实际输入长度、历史条数、模型或解码设置。
  - caption 不提供 exact variable names/version，难以用截图复现。
  - 模板本身没有效能量化，必须由 Table 3 等结果承接。
- **可复用模式**：用 prompt interface card 显示动态 persona 的数据流和输出约束，旁边绑定 adaptive-vs-static experiment。
- **Evidence**：p.24；basis=`rendered_observation`；Figure 10。

### Figure 11 (p.25 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈12，marks≈None）。
- **Caption（PDF 原文）**：*Figure 11: Prompt of Criteria-based Scoring Enhancement.*（7 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue title bar and light code/text card", "shape": "criteria instructions, score dimensions and output fields", "line": "card border/indentation", "facet": null, "text": "criterion definitions, user-specific weights and scoring response format"}`
- **Data/statistics**：prompt template 展示 Criteria-based Scoring Enhancement：把 inferred persona/preference dimensions 转成 criterion-level scoring instructions。无定量坐标或统计编码。
- **Evidence relation**：Figure 2(b) rubric/criterion branch → Figure 11 细化 scoring enhancement prompt → Tables 1–4 的 personalized evaluation outcomes 和 Figure 6/7 rubric cases。
- **设计优点：
  - 把“criteria-based”从概念词转为明确的 field/instruction block。
  - 卡片层次维持与 Figures 9–10/12–15 的家族一致性。
- **设计弱点：
  - 没有列出完整的 field schema、权重归一化或输入/输出示例。
  - raster prompt text 的可复制性和字号较弱。
  - caption 没有说明该模板是否作为所有 benchmark 的固定 prompt。
- **可复用模式**：将 rubric generation 和 criterion scoring 作为可替换 prompt stage，保持字段顺序稳定并把模板版本记录到源代码。
- **Evidence**：p.25；basis=`rendered_observation`；Figure 11。

### Figure 12 (p.26 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈12，marks≈None）。
- **Caption（PDF 原文）**：*Figure 12: Prompt of LLM-as-a-Judge + Output Style Requirements.*（9 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue header and neutral prompt body", "shape": "judge instruction block and output-style constraints", "line": "card border/indentation", "facet": null, "text": "LLM-as-a-Judge instruction, output style/system requirements and response format"}`
- **Data/statistics**：prompt screenshot/template，将 LLM-as-a-Judge 与 Output Style Requirements 组合；是 prompt implementation artifact，不含 benchmark values、sample size 或 uncertainty。
- **Evidence relation**：Table 6 的 OSR preference-indicator ablation → Figure 12 给出 OSR prompt mechanism → Figure 9–11 和 Table 6 的 combined Persona/OSR/SDim condition。
- **设计优点：
  - 直接对应 Table 6 的 OSR abbreviation，能把 prompt-level treatment 与 ablation row 对齐。
  - 统一 card layout 让多个 judge prompt 的差异集中在标题/文本。
- **设计弱点：
  - caption 不定义 output style 的 exact constraint 或 judge parser。
  - 截图只展示 template，不展示 generated judgment validity/failure rate。
  - 小号等宽/衬线混排和长行在附录阅读中可能产生换行歧义。
- **可复用模式**：将 prompt intervention 与对应 ablation condition 一一命名，并同时记录 parser、model 与 output validation。
- **Evidence**：p.26；basis=`rendered_observation`；Figure 12。

### Figure 13 (p.27 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈12，marks≈None）。
- **Caption（PDF 原文）**：*Figure 13: Prompt of LLM-as-a-Judge + Self-Description.*（7 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue header, light body, dark prompt text", "shape": "self-description field and judge instruction blocks", "line": "card border/indentation", "facet": null, "text": "self-description input, judge prompt and output-format requirements"}`
- **Data/statistics**：prompt template 将 LLM-as-a-Judge 与 Self-Description（SD）结合；只记录 prompt structure，不含被试数量、accuracy 或 replicate spread。
- **Evidence relation**：Table 6 的 +SD condition → Figure 13 给出 self-description treatment → Figure 6/7 的 inferred preference cases 与 Figure 14 的 demographic alternative。
- **设计优点：
  - 清楚标出 self-description 是 user-provided signal，和 persona induction 的来源不同。
  - 与 Figure 12 同构，减少读者在 prompt family 中寻找差异的成本。
- **设计弱点：
  - caption 没有说明 self-description 的长度、原文来源或隐私处理。
  - 模板截屏无法验证实际填充内容是否标准化。
  - 缺少 comparison output，单靠图片不能解释 Table 6 的差异。
- **可复用模式**：用同一 judge shell 仅替换 user signal channel，以 prompt-level controlled comparison 支撑 preference-indicator ablation。
- **Evidence**：p.27；basis=`rendered_observation`；Figure 13。

### Figure 14 (p.28 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈12，marks≈None）。
- **Caption（PDF 原文）**：*Figure 14: Prompt of LLM-as-a-Judge + Basic Demographic Information.*（9 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue header and neutral demographic/prompt fields", "shape": "demographic input fields and judge instruction card", "line": "card border/indentation", "facet": null, "text": "age/gender/employment/education and other demographic placeholders"}`
- **Data/statistics**：prompt template 将 basic demographic information 注入 LLM-as-a-Judge；字段包括 age、gender、employment、education、English proficiency、marital status、religion、ethnicity 和 location 等。无统计 marks 或 uncertainty。
- **Evidence relation**：Table 6 的 +BDI condition → Figure 14 明示 demographic signal channel → 对比 Figure 13 self-description、Figure 15 choice attributes 和 combined indicator row。
- **设计优点：
  - 字段清单使 BDI 的输入范围可见，避免把 demographic condition 与 persona 混为一谈。
  - 同一 prompt shell 便于和其他 indicator 条件做结构对照。
- **设计弱点：
  - 敏感字段虽可见但没有说明缺失值/编码、采样比例或 privacy handling。
  - caption 只给标题，无法知道 demographic 信息在实际评测中如何合成。
  - 无 output example 或 accuracy linkage，模板证据需依靠 Table 6。
- **可复用模式**：将不同 user signal channel 设计为同构 prompt cards，并在结果表中对齐 exact condition names 与 data-handling rules。
- **Evidence**：p.28；basis=`rendered_observation`；Figure 14。

### Figure 15 (p.29 / prompt_templates)
- **布局/类型/职责**：`appendix`，`page_width`；types=`screenshot, other`；purpose=`method_interface, experimental_design`；complexity=3/5（panels=1，series=None，legend_items=0，annotations≈13，marks≈None）。
- **Caption（PDF 原文）**：*Figure 15: Prompt of LLM-as-a-judge +Choice Attributes.*（7 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Times New Roman, Calibri, DengXian, Segoe Print, Nimbus Roman No9 L`；约 4.8–8.5 pt（median 6.2）；weight=`regular, bold`；style=`roman, italic, monospace`；provenance=`rendered_estimate`，confidence=`medium`。
- **Color**：mode=`mixed`，约 4 colors，HEX=`#3778B2, #F2F2F2, #FFFFFF, #1F4E79`；深蓝 header 和边框组织 prompt 卡片，浅灰/白色承载代码和解释文字，深色文字与层次线提供结构冗余。 grayscale_safe=False，redundant=True，provenance=`rendered_estimate`。
- **Plot grammar**：rendering=`raster`；x/y=`none/none`；grid=`none`；legend=`False`（placement=None，shared=False）；direct_labels=True；markers/line_styles=0/0；refs=0；hatching=False；uncertainty=`none`；line_width=0.8 pt；provenance=`rendered_estimate`。
- **Encodings**：`{"x": null, "y": null, "color": "blue title/header and light prompt body", "shape": "choice-attribute JSON-like fields and judge instruction", "line": "card border/indentation", "facet": null, "text": "user-defined scoring dimensions, weights and judge output format"}`
- **Data/statistics**：prompt template 展示 LLM-as-a-Judge + Choice Attributes（caption 保留原文的 “+Choice” 紧写法）；内容包含 user-defined scoring dimensions/weights 和 judge response format。无数据分布或 uncertainty。
- **Evidence relation**：Table 6 的 +SDim condition 将 choice attributes 作为 preference indicator → Figure 15 给出字段层模板 → Figures 6–7 的 weighted rubric 与 Table 6 combined condition 完成解释链。
- **设计优点：
  - Choice attributes 的维度/权重字段直接对应正文的 SDim abbreviation 和 example JSON。
  - prompt family 的一致 header、indentation 和 card border 适合快速逐阶段核查。
- **设计弱点：
  - caption 的大小写和空格本身不稳定（LLM-as-a-judge +Choice），且不解释 weight normalization。
  - 模板截图没有说明 dimensions 的来源、可选范围或 parser 约束。
  - 没有直接把该 prompt 与 accuracy delta 绑定，必须回到 Table 6。
- **可复用模式**：用结构化 attribute/weight fields 将用户偏好变成可消费的 scoring input，旁边配 ablation 结果和输入 schema。
- **Evidence**：p.29；basis=`rendered_observation`；Figure 15。

## Table 逐对象审计
### Table 1 (p.8 / results)
- **布局/职责**：`main`，`page_width`；purpose=`headline, main_comparison, robustness`。
- **Caption（PDF 原文）**：*Table 1: Results on PersonalRewardBench. P-GenRM outperforms all baselines on both datasets and model scales, while Test-time User-based Scaling brings further gains. Best and second-best results are marked in bold and underline. Ind and Pro denote the Individual and Prototype level scaling, respectively. Results are reported as “mean ± standard error” over 5 independent runs.*（55 words；moves=`title, setup, comparison, encoding_key, uncertainty_definition, main_finding`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.0/7.5 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=14，columns=5，header_levels=2，row_groups=4，decimal_precision=2，rules=`booktabs`，highlighting=`bold, underline, best_second_best`。
- **Uncertainty**：每个结果为 5 次独立运行的 mean ± standard error；caption 明确定义 spread 和 run count，但没有说明每个 dataset 的 test denominator。
- **Header/data/statistics**：5 columns：base model/method 与 Chatbot Arena-Personalized、PRISM-Personalized 的四个 model-scale columns；14 个 data rows，按 In-Context Judge、Finetuned Reward Model、Existing Personalized Reward Model、Personalized Generative Reward Model 四组排列。P-GenRM 8B/70B 为 72.68±1.85/73.42±1.74 与 65.32±0.56/66.21±0.76；Ind-8,Pro-4 和 Ind-16,Pro-8 在 8B 进一步到 74.30/67.54 与 75.92/68.06。
- **Evidence relation**：Introduction 的 benchmark claim → Table 1 是主 headline comparison → Table 2/3 分解 components/persona；Table 4 展开 test-time scaling strategies，Table 5 检查 cold-start generalization。
- **设计优点：
  - 多级 header 同时保留 dataset、personalization 和 base-model scale。
  - section row groups 和 bold/underline best rules 让长 baseline list 仍可扫描。
  - caption 把 mean±SE、run count、Ind/Pro 语义和主要 finding 集中写出。
- **设计弱点：
  - 14 data rows 加 4 个 metric columns 使字体很小，长 method names 与 section headers 挤压可读性。
  - 不同 rows 的 missing em-dash（scaling 仅在 8B）需要读者理解其不适用而非缺失。
  - mean±SE 没有逐列 sample denominator，跨 benchmark 比较仍依赖正文。
- **可复用模式**：用多级 dataset×scale 表头、语义 row groups 和明确 best/second-best 规则构成主结果 decision surface，并在附录展开稀疏条件。
- **Evidence**：p.8；basis=`rendered_observation`；Table 1。

### Table 2 (p.8 / ablation)
- **布局/职责**：`main`，`single_column`；purpose=`ablation, main_comparison`。
- **Caption（PDF 原文）**：*Table 2: Ablation studies of P-GenRM components: CL (Curriculum Learning), PR (Process Reward), OR (Outcome Reward). Results are reported as “mean ± standard error” over 5 independent runs.*（28 words；moves=`title, setup, abbreviation_definition, uncertainty_definition`；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.0/7.5 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=6，columns=3，header_levels=1，row_groups=1，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：6 rows 均为 5-run mean ± standard error；caption 定义 run count，但没有说是否复用 Table 1 的 test split。
- **Header/data/statistics**：Method + Chatbot Arena + PRISM 三列；P-GenRM baseline 与 w/o CL、w/o CL,PR、w/o CL,OR、w/o CL,RL、w/o CL,RL,SFT 五个 ablation rows。完整方法 72.68/65.32，去掉 RL/SFT 降至 56.37/52.04。
- **Evidence relation**：Table 1 headline → Table 2 isolates Curriculum Learning、Process/Outcome Reward、RL/SFT contributions → Table 3 tests adaptive persona as a separate design axis。
- **设计优点：
  - 三列结构清晰，组件缩写直接放入 method labels。
  - 单一 baseline-to-ablation ordering 让 performance drops 易于逐行追踪。
  - caption 明确 mean±SE 和 component definitions。
- **设计弱点：
  - 多个 nested ablations 需要读者理解 w/o CL,RL,SFT 的 cumulative semantics。
  - 没有 delta column，组件影响需要心算。
  - caption 没有说明具体 benchmark split、model scale 或 denominator。
- **可复用模式**：以完整模型为第一行，按可解释的组件删除路径排列消融，并在 caption 中定义缩写与 replicate unit。
- **Evidence**：p.8；basis=`rendered_observation`；Table 2。

### Table 3 (p.8 / persona_comparison)
- **布局/职责**：`main`，`single_column`；purpose=`main_comparison, robustness`。
- **Caption（PDF 原文）**：*Table 3: Comparison of adaptive (PSI, Persona-guided Scoring Induction) and static (SMe, SynthesizeMe) persona methods across base models. Results are reported as “mean ± standard error” over 5 independent runs.*（30 words；moves=`title, setup, comparison, abbreviation_definition, uncertainty_definition`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.0/7.5 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=6，columns=3，header_levels=1，row_groups=2，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：6 data rows，均为 5-run mean ± standard error；caption 定义 PSI/SMe 与 run count。
- **Header/data/statistics**：Qwen3-8B、Qwen3-8B+SMe、Qwen3-8B+PSI、o3、o3+SMe、o3+PSI 六行，列为 model/method、Chatbot Arena、PRISM。PSI 在 Qwen3-8B 达 64.22/58.01，在 o3 达 69.14/63.87。
- **Evidence relation**：正文 adaptive-vs-static persona argument → Table 3 controls base model and compares SMe/PSI → Figure 6–7 qualitative persona outputs and Table 1 P-GenRM results。
- **设计优点：
  - 按 base model 分组，adaptive/static contrast 在每组内直接可见。
  - PSI rows 的 method names 与 caption abbreviation 完整对齐。
  - bold/values 和 mean±SE 让跨 base-model comparison 可审计。
- **设计弱点：
  - 同一表混合 Qwen3 与 o3 的 scale/closed model 差异，缺少 compute/context metadata。
  - 只有 absolute accuracy，未提供 paired delta 或 significance/reproducibility detail。
  - section/group boundaries主要靠 row order，视觉上不如显式 horizontal rule。
- **可复用模式**：在固定 base-model block 内对照 adaptive 与 static persona，保持指标和 uncertainty 语法相同。
- **Evidence**：p.8；basis=`rendered_observation`；Table 3。

### Table 4 (p.9 / scaling_analysis)
- **布局/职责**：`main`，`single_column`；purpose=`main_comparison, robustness, efficiency_cost`。
- **Caption（PDF 原文）**：*Table 4: Comparison of different scaling strategies on Chatbot Arena and PRISM benchmarks, where Ind, Pro denotes the Individual and Prototype level scaling, respectively. Results are reported as “mean ± standard error” over 5 independent runs.*（36 words；moves=`title, setup, comparison, abbreviation_definition, uncertainty_definition`；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.0/7.5 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=12，columns=3，header_levels=1，row_groups=2，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：12 rows，5 independent runs 的 mean ± standard error；caption 定义 Ind/Pro 和 run count。
- **Header/data/statistics**：Model + Chatbot Arena + PRISM 三列；o3/o3+PSI 两个 proprietary rows，加 P-GenRM-8B baseline 与 9 个 Ind/Pro configurations。Ind-16,Pro-8 为 75.92±1.70/68.06±0.69；Ind-0,Pro-8 下降到 66.90/57.65。
- **Evidence relation**：Figure 3 prototype-count selection → Table 4 是 test-time user-based scaling strategy sweep → Table 1 只保留 best scaling rows，Tables 11–13 补 latency/pair/prototype sensitivity。
- **设计优点：
  - 同一 metric columns 支持完整 Ind/Pro sweep 与 proprietary reference。
  - row order 从 no scaling 到 individual/prototype combinations，读者可见 scaling frontier 与异常 configuration。
  - caption 定义 abbreviations and uncertainty。
- **设计弱点：
  - 12 rows 的 method strings 很长，single-column width 下数值紧密。
  - 表没有 inference-time cost，accuracy-only reading 会漏掉 scaling trade-off。
  - 把 o3/o3+PSI 与 P-GenRM mixing 在同一 row group 中，group distinction 依赖小 header。
- **可复用模式**：以稳定 metric columns 扫描 individual/prototype allocation，并把 best configuration 与 latency table 交叉绑定。
- **Evidence**：p.9；basis=`rendered_observation`；Table 4。

### Table 5 (p.10 / ood_generalization)
- **布局/职责**：`main`，`single_column`；purpose=`main_comparison, robustness`。
- **Caption（PDF 原文）**：*Table 5: Performances with cold-start settings measured by Spearman’s rank correlation on LaMP-QA (↑ = better). Arts = Arts & Entertainment, Pers. = Personal Life & Development, Soc. = Society & Culture, Avg. = Average.*（35 words；moves=`title, setup, comparison, encoding_key, abbreviation_definition`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.0/7.5 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=7，columns=5，header_levels=1，row_groups=1，decimal_precision=3，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：Spearman correlations are single point estimates with no run spread, sample denominator or uncertainty column；↑ 明示 higher is better。
- **Header/data/statistics**：Reward Model + Arts + Pers. + Soc. + Avg. 五列，7 rows（Qwen3 8B/32B/235B-A22B, LLaMA3.1 8B/70B, SynthMe-8B, P-GenRM-8B+Ind-8,Pro-4）。P-GenRM Avg=.638，优于其它 listed baselines。
- **Evidence relation**：Section 5.4 unseen-user cold-start claim → Table 5 将 sparse feedback generalization 分解到 LaMP-QA domains → Table 1 main PersonalRewardBench 与 Appendix prompt/evaluation protocol 限定 ground-truth construction。
- **设计优点：
  - domain columns 和 Avg. 使跨类别 pattern 易于扫描。
  - caption 定义 shortened dataset names 和 metric direction。
  - 最后一行把 P-GenRM scaling configuration 与 baseline ranking 对齐。
- **设计弱点：
  - caption 未说明 synthetic LLM judge ground truth 的 construction、sample size 或 independent runs。
  - Avg. 可能掩盖 domain heterogeneity，且没有 delta/uncertainty。
  - Reward Model 名称长，single-column table 在 appendix-like page bottom 偏密。
- **可复用模式**：把 OOD cold-start 结果按任务域拆列并保留 Avg.，同时在 caption 中定义方向和缩写，旁边公开 ground-truth protocol。
- **Evidence**：p.10；basis=`rendered_observation`；Table 5。

### Table 6 (p.14 / preliminary_persona)
- **布局/职责**：`appendix`，`page_width`；purpose=`ablation, main_comparison, experimental_design`。
- **Caption（PDF 原文）**：*Table 6: Accuracy(%) of LLM-as-a-Judge with different types of user preference indicators.*（12 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=7，columns=3，header_levels=1，row_groups=1，decimal_precision=0，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：accuracy 是 single 15% PRISM test subset 上 over 5 independent runs 的 mean（正文说明），但 table caption 不写 run count 或 uncertainty；表格只给 point ACC。
- **Header/data/statistics**：Condition、Description、ACC(%) 三列；N-CoT、+Persona、+SD、+OSR、+BDI、+SDim、+Persona,OSR,SDim 七行，最后 combined condition 为 66.17。
- **Evidence relation**：Appendix A.2 的 preference-indicator experiment → Table 6 quantifies Figures 12–15 prompt conditions → combined Persona/OSR/SDim supports the method’s persona/rubric chain but is preliminary rather than benchmark headline。
- **设计优点：
  - Description column makes each indicator operational definition self-contained enough to map to prompt figures。
  - 最后 combined row shows composition rather than only one-factor ablation。
  - point ACC and bold maxima are readable without color。
- **设计弱点：
  - caption omits five-run aggregation, test subset proportion and judge model，需读正文。
  - description paragraphs make table very tall and shrink ACC column’s visual salience。
  - no spread or per-condition sample count means 0.2–1.8 pp differences are not stability evidence。
- **可复用模式**：把 prompt/user-signal variants放在“condition–description–metric”三列，并以 combined row 明示 composition；统计 protocol 应移入 caption。
- **Evidence**：p.14；basis=`rendered_observation`；Table 6。

### Table 7 (p.15 / reward_settings)
- **布局/职责**：`appendix`，`single_column`；purpose=`ablation, robustness`。
- **Caption（PDF 原文）**：*Table 7: Performance changes of the model after reinforcement learning under different α-β settings*（14 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=4，columns=3，header_levels=1，row_groups=1，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：α–β settings 的 Chatbot Arena/PRISM values 是 point estimates，无 uncertainty；caption 没有 run count。
- **Header/data/statistics**：αβ setting、Chatbot Arena、PRISM 三列，4 rows：(0.5,1)=71.07/63.82，(0.5,0.5)=70.65/63.33，(1,0)=69.05/60.94，(0,1)=70.22/62.70。
- **Evidence relation**：Appendix A.3 reward-weight discussion → Table 7 tests process/outcome reward balance → Table 2 CL/PR/OR ablation and main Table 1 P-GenRM result。
- **设计优点：
  - 小型 parameter sweep 易读，两个 benchmark columns 保持固定。
  - α/β settings 直接作为 row labels，避免另加 legend。
- **设计弱点：
  - caption 未定义 α 与 β 分别对应哪类 reward，也未报告 training budget。
  - 无 uncertainty、seed 或 selection rule，不能判定 settings 差异稳定。
  - performance changes 的 “changes” 没有 baseline/delta column，实际展示的是 absolute scores。
- **可复用模式**：用 compact hyperparameter sweep 表展示 reward mixing 的双轴结果，同时明确 parameter semantics、baseline 和 replicate。
- **Evidence**：p.15；basis=`rendered_observation`；Table 7。

### Table 8 (p.16 / prototype_distribution)
- **布局/职责**：`appendix`，`page_width`；purpose=`dataset, robustness`。
- **Caption（PDF 原文）**：*Table 8: Distribution of user groups in the PRISM dataset*（10 words；moves=`title, setup`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=1，columns=7，header_levels=1，row_groups=1，decimal_precision=1，rules=`minimal`，highlighting=`none`。
- **Uncertainty**：一行 summary statistics，无 uncertainty；Min/Max/Mean/Median/percentiles 不是 repeated-run estimates。
- **Header/data/statistics**：Num of samples row；7 columns 为 statistic name、Min、Max、Mean、Median、25th pct、75th pct。样本数范围 18–930，mean 154.8，median 105，IQR 63–176。
- **Evidence relation**：Figure 5 prototype load bars → Table 8 summarizes PRISM user-group sample distribution → Table 9 prototype-level accuracy distribution and Figure 3/5 scaling choice。
- **设计优点：
  - 一行统计表把 long-tailed group-size fact 直接暴露出来。
  - 同时报告 median/IQR 与 mean/min/max，避免只用均值掩盖长尾。
- **设计弱点：
  - caption 未说明 unit 是 user samples 还是 preference pairs，也未注明 total groups。
  - 单行宽表的 header abbreviations 在缩印后需要回读。
  - 没有 histogram/quantile plot，无法看到内部分布形状。
- **可复用模式**：用 min/max/mean/median/percentiles 的横向 summary 为 prototype-load 图提供可复查的分母背景。
- **Evidence**：p.16；basis=`rendered_observation`；Table 8。

### Table 9 (p.16 / prototype_distribution)
- **布局/职责**：`appendix`，`page_width`；purpose=`robustness, main_comparison`。
- **Caption（PDF 原文）**：*Table 9: Stable performance of P-GenRM across prototypes*（8 words；moves=`title, main_finding`；headline_bold=False；self_contained=False；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=1，columns=7，header_levels=1，row_groups=1，decimal_precision=4，rules=`minimal`，highlighting=`none`。
- **Uncertainty**：Prototype-level accuracy summary is deterministic aggregate (Macro .6521, Min .5806, Max .7508, Median .6500, Std .0401, IQR .0544) with no uncertainty over resampling/runs。
- **Header/data/statistics**：Prototype-level Acc row；7 columns 为 statistic、Macro、Min、Max、Median、Std、IQR。以 distribution summary 支撑“stable across prototypes”，不是 per-prototype raw table。
- **Evidence relation**：Figure 5 red accuracy line 与 Figure 3 prototype number study → Table 9 summarizes prototype-level stability → Table 4 scaling sweep and Table 8 group-size distribution give complementary explanations。
- **设计优点：
  - Std/IQR 与 extrema 同时报告，较单一 mean 更能检验 stability。
  - 与 Figure 5 的 prototype-level accuracy view 直接配对。
- **设计弱点：
  - 标题和 caption 的 “stable” 是方向性结论，但没有 confidence/replicate definition。
  - 一行 aggregate hides which prototype IDs are outliers；应与 raw distribution or figure link explicit。
  - Macro/Std 的计算单位与 class weighting 未定义。
- **可复用模式**：当图展示许多 group-level outcomes 时，附一行 Macro/Min/Max/Median/Std/IQR summary，但要公开 aggregation unit。
- **Evidence**：p.16；basis=`rendered_observation`；Table 9。

### Table 10 (p.17 / macro_accuracy)
- **布局/职责**：`appendix`，`page_width`；purpose=`main_comparison, robustness`。
- **Caption（PDF 原文）**：*Table 10: P-GenRM outperforms baselines methods using macro-accuracy as the metric*（11 words；moves=`title, comparison, main_finding`；headline_bold=False；self_contained=False；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=1，columns=7，header_levels=1，row_groups=1，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：Macro accuracy values include ± spread in each cell（如 P-GenRM-8B 65.21±.64），但 caption 不定义 spread、runs 或 dataset unit。
- **Header/data/statistics**：一行 macro acc，7 columns：row label plus Llama3.1-8B 56.24±.78、Llama3.1-70B 58.27±.76、o3 63.33±.68、Fine-tuned BT-70B 60.64±.84、SynthesizeMe70B 61.51±.73、P-GenRM-8B 65.21±.64。
- **Evidence relation**：Appendix macro-accuracy robustness claim → Table 10 changes aggregation from main benchmark accuracy to per-user/group macro accuracy → Table 1 headline and Figure 4/8 prototype heterogeneity contextualize why macro metric matters。
- **设计优点：
  - Single-row wide comparison makes method ranking immediate。
  - Retains several baseline families and an uncertainty token per cell。
- **设计弱点：
  - “baselines methods” caption grammar aside, metric denominator and spread are unspecified。
  - Horizontal six-model scan is dense; no model family grouping or direction arrow。
  - one-row layout hides per-user variance and can overstate uniform superiority。
- **可复用模式**：用 wide single-row metric panel快速报告 alternative aggregation metric，并同时给各 model 的 spread 与 exact denominator。
- **Evidence**：p.17；basis=`rendered_observation`；Table 10。

### Table 11 (p.19 / efficiency)
- **布局/职责**：`appendix`，`single_column`；purpose=`efficiency_cost, main_comparison`。
- **Caption（PDF 原文）**：*Table 11: Inference time comparison between P-GenRM with test-time user-based scaling and base-line methods.*（14 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=8，columns=3，header_levels=1，row_groups=1，decimal_precision=0，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：Inference time 是 single wall-clock measurement/setting；没有 repeated-run spread、hardware utilization 或 cost normalization。
- **Header/data/statistics**：Model、Inference Time (Wall-clock)、Performance 三列；8 rows 从 LLaMA3.1-8B/70B+PSI、SynthesizeMe+FT RM 8B/70B、o3+PSI、P-GenRM-8B 到 +Ind-8,Pro-4、+Ind-16,Pro-8。P-GenRM base 00:14:16/72.68，Ind-16,Pro-8 00:23:05/75.92。
- **Evidence relation**：正文 limited inference-time increase claim → Table 11 binds performance to wall-clock cost → Table 4 accuracy strategy sweep and Tables 12–13 pair/prototype sensitivities。
- **设计优点：
  - 同表给 runtime 与 performance，避免 scaling gains 脱离成本。
  - rows 含 prior baselines 与 multiple P-GenRM scaling levels，能看 marginal latency。
- **设计弱点：
  - hardware、batch size、parallelism、requests and timing protocol absent from caption。
  - wall-clock string 不提供 per-request normalization，跨 model scale 的比较可能不对称。
  - performance uncertainty missing despite neighboring result tables using mean±SE。
- **可复用模式**：把 latency 与 quality 放入同一 decision table，明确 wall-clock protocol、hardware 和 normalization。
- **Evidence**：p.19；basis=`rendered_observation`；Table 11。

### Table 12 (p.20 / feedback_sensitivity)
- **布局/职责**：`appendix`，`page_width`；purpose=`robustness, ablation`。
- **Caption（PDF 原文）**：*Table 12: P-GenRM’s performance with different numbers of preference pairs*（10 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=1，columns=5，header_levels=1，row_groups=1，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：1/2/3/4 preference-pair accuracy values为 59.78±2.66、64.62±2.07、72.68±1.85、72.50±1.64；± 未在 caption 定义，正文语境为 independent runs。
- **Header/data/statistics**：一行 table，Preference Pairs + 1、2、3、4 四个 columns；accuracy 随 pairs 增至 3 提升，4 略降。
- **Evidence relation**：Sparse preference motivation → Table 12 tests user-history budget → Figure 1 hybrid signals and Tables 1/5 show benchmark/cold-start endpoints。
- **设计优点：
  - 横向 budget sweep 让 feedback-efficiency curve 易于扫描。
  - 保留 uncertainty token，能看 3 vs 4 pairs 的差距相对 spread。
- **设计弱点：
  - 单行不显示 model/dataset/configuration；需正文解码。
  - ± provenance、run count 和 pair sampling rule 未写入 caption。
  - 只有四个 budget points，无法确定 non-monotonicity 是否稳定。
- **可复用模式**：以一行小表展示 scarce-feedback budget sweep，caption 应固定 model、split、run aggregation 和 pair sampling。
- **Evidence**：p.20；basis=`rendered_observation`；Table 12。

### Table 13 (p.20 / prototype_sensitivity)
- **布局/职责**：`appendix`，`page_width`；purpose=`robustness, main_comparison`。
- **Caption（PDF 原文）**：*Table 13: P-GenRM-8B performance under different numbers of prototypes with (Ind-8, Pro-4) setting*（13 words；moves=`title, setup, comparison, abbreviation_definition`；headline_bold=False；self_contained=False；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=2，columns=6，header_levels=1，row_groups=1，decimal_precision=2，rules=`booktabs`，highlighting=`bold`。
- **Uncertainty**：Chatbot Arena/PRISM values over prototype counts include mean±standard error；caption 没有重述 5-run protocol。
- **Header/data/statistics**：two rows (Chatbot Arena, PRISM) × columns # Prototypes {0,25,50,100,125} plus row label；values mirror Figure 3 right: 72.68→74.30→73.45 and 65.32→67.54→67.19 pattern。
- **Evidence relation**：Figure 3 plot → Table 13 gives exact prototype-count values under fixed Ind-8,Pro-4 → Tables 8–9 explain load/stability and Table 4 gives allocation alternatives。
- **设计优点：
  - Exact values complement visual plateau and make 50-prototype choice reproducible。
  - fixed Ind-8,Pro-4 condition prevents prototype count from being confounded with individual scaling。
- **设计弱点：
  - caption 未写 mean±SE/run count、dataset split 或 prototype construction。
  - two-row table cannot show distribution across prototypes or latency。
  - prototype count 0 baseline semantics needs surrounding text。
- **可复用模式**：将核心 design sweep 的 exact values 作为二维 table 与 plot 配对，固定其它 scaling dimensions。
- **Evidence**：p.20；basis=`rendered_observation`；Table 13。

### Table 14 (p.21 / policy_training)
- **布局/职责**：`appendix`，`single_column`；purpose=`main_comparison, robustness`。
- **Caption（PDF 原文）**：*Table 14: Comparisons of policy models’ performance over 5 independent runs*（11 words；moves=`title, setup, comparison, uncertainty_definition`；headline_bold=False；self_contained=True；main_finding_stated=True）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=6，columns=4，header_levels=1，row_groups=1，decimal_precision=3，rules=`booktabs`，highlighting=`none`。
- **Uncertainty**：Mean、SE 和 95% CI 均显式列出，统计对象是 policy model performance over 5 independent runs；属于 appendix analysis。
- **Header/data/statistics**：Policy Model、Mean、SE、95% CI 四列；6 rows：Llama3.1-8B-Instruct 2.954 [2.939,2.969]，Qwen2.5-7B 2.970 [2.952,2.988]，Llama3.1-70B 3.156 [3.138,3.174]，Qwen2.5-72B 3.214 [3.192,3.228]，DPO 3.316 [3.303,3.329]，GRPO 3.354 [3.334,3.374]。
- **Evidence relation**：Section 5.5 policy training claim → Table 14 summarizes 5-run policy model means and CI → Table 15 exposes raw judge-by-run values and DPO/GRPO provenance。
- **设计优点：
  - Mean/SE/CI columns make aggregation and uncertainty explicit。
  - policy model rows are stable and ordered from base to tuned variants。
- **设计弱点：
  - model names are long and interval notation is cramped in single-column width。
  - CI method, score scale and judge aggregation are not stated in caption。
  - only summary means hide judge-specific disagreement that Table 15 reveals。
- **可复用模式**：Use a compact policy-model summary with explicit mean/SE/interval columns, then expose raw per-run judge values in a wide appendix table.
- **Evidence**：p.21；basis=`rendered_observation`；Table 14。

### Table 15 (p.21 / policy_training)
- **布局/职责**：`appendix`，`page_width`；purpose=`reproduction, robustness`。
- **Caption（PDF 原文）**：*Table 15: Full per-run results of policy models’ performances over 5 independent runs*（13 words；moves=`title, setup, comparison`；headline_bold=False；self_contained=True；main_finding_stated=False）。
- **Typography**：family=`Nimbus Roman No9 L, Computer Modern math`；body/header≈7.2/7.8 pt；header_weight=`bold`；provenance=`pdf_object`，confidence=`high`。
- **Header/structure**：rows=6，columns=16，header_levels=2，row_groups=1，decimal_precision=3，rules=`minimal`，highlighting=`none`。
- **Uncertainty**：Raw per-run scores over 5 runs are shown for each policy model and each of three judges (GPT-4o, Claude-sonnet-4, Gemini-2.5-pro)；no derived uncertainty inside table。
- **Header/data/statistics**：16 columns：Policy Model + three judge blocks × five runs；6 policy rows corresponding to Table 14. Wide repeated-run layout preserves raw values used for summary means/SE/CI。
- **Evidence relation**：Table 14 summary → Table 15 raw judge/run expansion → Section 5.5 DPO/GRPO policy-training claim；raw table bounds any cross-judge aggregation。
- **设计优点：
  - Raw runs make Table 14 summary auditable and expose judge heterogeneity。
  - two-level judge×run header keeps repeated measures aligned。
  - no color needed; whitespace and separators indicate blocks。
- **设计弱点：
  - 16 columns are very dense and require horizontal scanning at appendix width。
  - caption does not state score range, randomization or exact aggregation from judges to policy score。
  - row labels and judge names compete with 15 numeric columns, increasing transcription risk。
- **可复用模式**：Keep a raw-run wide table beside a summary table whenever model/policy claims aggregate across judges and runs; preserve exact block headers and computation mapping。
- **Evidence**：p.21；basis=`rendered_observation`；Table 15。

## 跨对象系统判断
- **Visual narrative**：Figure 1 建立 sparse/noisy/scenario-varying preference→persona/rubric→judgment→test-time scaling 主线；Figure 2 分解 training/evaluation chain；Figure 3–5 将 prototype number、user-group load 与 performance stability 变成选择证据；Figure 6–8 给跨场景 persona 和 cluster qualitative evidence；Figure 9–15 公开 prompt interfaces。Tables 1–5 是 benchmark/ablation/persona/scaling/OOD headline，Tables 6–15 补 prompt-indicator、reward、prototype、latency、policy training 和 raw-run 边界。
- **Caption system**：Figure/Table captions 统一使用 “Figure/Table n:” 加标题；正文 Figure 1/3/4 和 Table 1 带 finding 或 comparison，附录 prompt figures 多为标题-only，qualitative captions 很少给 sampling/denominator。Table 1–4 明确 mean±standard error over 5 runs，Table 5/6/7/8–15 的 uncertainty、ground-truth 或 aggregation 说明更多依赖正文。
- **Table header system**：主结果表使用 dataset×model-scale 多级表头（Table 1），消融/策略表使用 method/condition + 两个 benchmark columns（Tables 2–4），OOD 使用 domain columns + Avg.（Table 5）。附录以 Condition–Description–ACC、alpha/beta、prototype summary、runtime/performance、judge×run blocks 组织；Table 14/15 用 summary-to-raw 两层证据。
- **Method/result/ablation**：Figure 2 的 training/evaluation chain 解释 P-GenRM pipeline；Tables 1–4 测量完整模型、CL/PR/OR/RL 消融、adaptive PSI 与 Ind/Pro scaling；Figures 3–5/8 和 Tables 8–9/13 检查 prototype capacity/load/stability；Figures 9–15、Table 6 将 prompt indicators 映射到 persona/rubric outcomes。
- **Main/appendix link**：正文 Figures 3–4 指向 Appendix Figure 5/8 与 Tables 8–9/13 的 prototype details；正文 Tables 1–5 的 OOD、scaling 和 policy claims 由 Appendix Tables 6–15 的 prompt, reward, latency, policy summary/raw runs 补证。附录 qualitative/prompt objects 展示机制与输入接口，但不能独立取代正文 aggregate results。
- **Typography**：PDF 字体对象以 Nimbus Roman No9 L、Computer Modern math、NimbusMonL-Regu 等为主；正文表格约 7.0–7.5 pt，附录约 7.2–7.8 pt，图内标签/代码文字约 5–9 pt rendered estimate。Figure 1/2 source assets 与 PDF shell 混合，prompt screenshots 的 Times/Calibri/DengXian-like glyphs 不应当被误报为 exact source font。
- **Color**：浅色 pipeline blocks、蓝/橙定量 series、蓝 shared/红 individual highlights 和深蓝 prompt headers 构成局部语义；表格不依赖颜色。直接文本、cluster labels、axis roles、card hierarchy 和 bold/underline 提供一定冗余，但 cluster/prompt screenshots 的颜色与 raster text 在灰度/缩印中仍有风险。

## 最终判断
- **最可复用模式：
  - Figure 1/2 把 preference signal、persona、rubric、judge 和 test-time scaling 组成可追踪的 workflow/evaluation-chain pair。
  - Figure 3 与 Table 13 以 prototype-count plot+exact-value table 支撑一个容量选择；Figure 5、Tables 8–9 再给 group-load/stability boundary。
  - Table 1 的 dataset×model-scale 多级表头和 section row groups 适合跨 baseline、scale 与 scaling level 的主结果比较。
  - Figure 6/7、Figure 4/8 用 scenario/persona card 与 cluster/text pair 让 qualitative interpretability 连接到 rubric/prompt mechanism。
  - Table 14 summary + Table 15 raw judge/run expansion 是 policy-model aggregate claim 的可审计配对。
- **最高价值对象：
  - Figure 1
  - Figure 2
  - Table 1
  - Figure 3 + Table 13
  - Figure 4/8 + Tables 8–9
- **失败模式：
  - 多数 qualitative/prompt figures 是单例或模板截图，没有 sampling rule、prevalence、parser/version 或 outcome linkage。
  - 主结果表虽常给 5-run mean±SE，但 Table 5–13 大量对象缺 denominator、spread provenance、hardware/cost 或 ground-truth construction。
  - dual-axis Figure 5、unlabeled cluster coordinates Figure 4/8 和 prompt card raster text 在缩印/灰度下增加解读负担。
  - prototype-count/accuracy 的 plateau 与 stability claim 依赖少量 summary rows，未展示 raw per-prototype uncertainty 或 latency jointly。
  - 作者仓库提供 Figure 1/2 exact raster assets 和实现/提示词，但没有全套 PDF Figure/Table generators；不能把 README release visuals 当作 exact export。
- **一句话视觉策略：**论文用 preference→persona/rubric→judge→test-time scaling 的 workflow 贯穿正文结果、prototype capacity/stability 图表和附录 prompt/qualitative cards，解释性路径清晰，但统计分母、单例选择、cost/uncertainty 与完整 source binding 仍是主要缺口。

## 交付验证
- 只修改 `visual_audits/iclr-2026-af6a7ff26bd9.md` 与原子发布的 `.json`；没有改 reading、inventory、schema、prompt、PDF、源码或其他论文审计文件。
- 目标 JSON 通过 schema、Figure/Table 数量、标签和页码断言；全 29 页已以 200 dpi 渲染并逐页/逐对象检查。

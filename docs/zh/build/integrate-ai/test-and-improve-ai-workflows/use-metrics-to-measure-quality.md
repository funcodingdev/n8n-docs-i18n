---
title: 基于 metric 的 evaluation
description: >-
  使用基于 metric 的 evaluation，持续衡量、评分并改进生产中 AI 工作流的性能。
contentType: howto
nodeTitle: 使用 metric 衡量质量
originalFilePath: advanced-ai/evaluations/metric-based-evaluations.md
originalUrl: 'https://docs.n8n.io/advanced-ai/evaluations/metric-based-evaluations'
url: >-
  https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality
layout:
  description:
    visible: false
---

# 基于 metric 的 evaluation <a href="#metric-based-evaluations" id="metric-based-evaluations"></a>


{% hint style="info" %}
**适用于 Pro 和 Enterprise 计划**

基于 metric 的 evaluation 适用于 Pro 和 Enterprise 计划。已注册社区用户和 Starter 计划用户也可以在单个工作流中使用。
{% endhint %}

### 什么是基于 metric 的 evaluation？ <a href="#what-are-metric-based-evaluations" id="what-are-metric-based-evaluations"></a>

当工作流准备部署后，你通常会希望用比[构建阶段](run-quick-evaluations.md)更多的示例来测试它。

例如，当生产执行开始暴露边界场景时，你会希望将它们添加到测试数据集中，确保这些场景被覆盖。

对于从生产数据构建的大型数据集，只靠目测结果很难了解性能。相反，你必须衡量性能。基于 metric 的 evaluation 可以为每次测试运行分配一个或多个分数，你可以将它们与之前的运行进行比较。单个分数会汇总起来，用于衡量整个数据集上的性能。

此功能允许你运行会计算 metric 的 evaluation，跟踪这些 metric 在不同运行之间如何变化，并深入分析变化原因。

Metric 可以是确定性函数（例如两个字符串之间的距离），也可以使用 AI 计算。Metric 通常涉及检查输出与*参考输出*（也称为 ground truth）之间的差距。为此，数据集必须包含该参考输出。不过，有些 evaluation 不需要此参考输出（例如检查文本的情绪或毒性）。

## 工作方式 <a href="#how-it-works" id="how-it-works"></a>

{% hint style="info" %}
**Google Sheets credential**

Evaluation 使用 data table 或 Google Sheets 存储测试数据集。要使用 Google Sheets 作为数据集来源，请配置 [Google Sheets credential](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/google)。
{% endhint %}

1. 设置[轻量 evaluation](run-quick-evaluations.md)
2. 向工作流添加 metric
3. 运行 evaluation 并查看结果

### 1. 设置轻量 evaluation <a href="#1-set-up-light-evaluation" id="1-set-up-light-evaluation"></a>

按照[设置说明](run-quick-evaluations.md)创建数据集，并将其连接到工作流，将输出写回数据集。

以下步骤使用轻量 evaluation 文档中的同一个支持工单分类工作流：

![轻量 evaluation 工作流](../../.gitbook/assets/light-evaluation-workflow.png)

### 2. 向工作流添加 metric <a href="#2-add-metrics-to-workflow" id="2-add-metrics-to-workflow"></a>

Metric 是用于给工作流输出评分的维度。它们通常会将实际工作流输出与参考输出进行比较。使用 AI 计算 metric 很常见，不过有时只使用代码也可行。在 n8n 中，metric 始终是数字。

你需要在工作流已经产生输出之后，添加用于计算 metric 的逻辑。可以将 metric 使用的任何参考输出作为数据集中的一列。这能确保它们在工作流中可用，因为 evaluation trigger 会输出它们。

使用 **Set Metrics** 操作计算：

* **Correctness (AI-based)**：回答含义是否与提供的参考答案一致。使用 1 到 5 的评分，5 表示最好。
* **Helpfulness (AI-based)**：响应是否回答了给定查询。使用 1 到 5 的评分，5 表示最好。
* **String Similarity**：回答与参考答案有多接近，按字符逐个衡量（编辑距离）。返回 0 到 1 之间的分数。
* **Categorization**：回答是否与参考答案完全匹配。匹配时返回 1，否则返回 0。
* **Tools Used**：执行是否使用了 tool。返回 0 到 1 之间的分数。

你也可以添加自定义 metric。只需在工作流中计算 metric，然后将它们映射到 Evaluation 节点。使用 **Set Metrics** 操作，并选择 **Custom Metrics** 作为 Metric。随后可以设置要返回的 metric 名称和值。

例如：

* [RAG document relevance](https://n8n.io/workflows/4273)：使用 vector database 时，检索到的文档是否与问题相关。

计算 metric 可能增加延迟和成本，因此你可能只想在运行 evaluation 时执行它，并在生产执行时避免它。你可以将 metric 逻辑放在 [`check if evaluating` 操作](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.evaluation#check-if-evaluating)之后来实现。

![Check if evaluating 节点](../../.gitbook/assets/check-if-evaluating.png)

### 3. 运行 evaluation 并查看结果 <a href="#3-run-evaluation-and-view-results" id="3-run-evaluation-and-view-results"></a>

切换到工作流的 **Evaluations** 选项卡，并点击 **Run Test** 按钮。Evaluation 会开始运行。运行结束后，它会显示每个 metric 的汇总分数。

点击测试运行行可以查看每个测试用例的结果。点击单个测试用例会在新标签页中打开产生该结果的 execution。

#### 并行运行测试用例 <a href="#run-test-cases-in-parallel" id="run-test-cases-in-parallel"></a>

在支持并发的计划中，**Run Test** 是一个拆分按钮。右侧插入符号会打开一个带滑块的弹出框，用于控制同时运行多少个测试用例。

<figure>
<img src="../../.gitbook/assets/run-test-concurrency.png" alt="">
<figcaption>并发弹出框，其中滑块设置为 3，最大为 5 个并行测试用例。</figcaption>
</figure>

默认最大值取决于你的计划：

| 计划 | 最大并行测试用例数 |
| :--- | :-------------------------- |
| Community / Pro | 1（顺序执行） |
| Business | 3 |
| Enterprise | 5 |

当最大值为 `1` 时，插入符号和弹出框会隐藏，**Run Test** 是普通按钮，运行会按顺序执行，与早期版本相同。

无论计划层级如何，自托管实例都可以使用 [`N8N_CONCURRENCY_EVALUATION_LIMIT`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions) 环境变量覆盖最大值。

{% hint style="info" %}
**LLM 速率限制**

更高并发会加快 evaluation 运行速度，但也会增加触发上游 LLM 速率限制的概率。如果看到速率限制错误，请降低滑块数值。
{% endhint %}

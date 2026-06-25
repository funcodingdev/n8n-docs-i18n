---
title: 轻量 evaluation
description: >-
  在开发期间使用轻量 evaluation，通过检查已知测试用例的执行结果来构建可靠的 LLM 工作流。
contentType: howto
nodeTitle: 运行快速 evaluation
originalFilePath: advanced-ai/evaluations/light-evaluations.md
originalUrl: 'https://docs.n8n.io/advanced-ai/evaluations/light-evaluations'
url: >-
  https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/run-quick-evaluations
layout:
  description:
    visible: false
---

# 轻量 evaluation <a href="#light-evaluations" id="light-evaluations"></a>


{% hint style="info" %}
**适用于已注册社区计划和付费计划**

轻量 evaluation 对已注册社区用户和所有付费计划可用。
{% endhint %}

## 什么是轻量 evaluation？ <a href="#what-are-light-evaluations" id="what-are-light-evaluations"></a>

构建工作流时，你通常希望用少量示例测试它，了解其表现并进行改进。在工作流开发的这个阶段，逐个查看每个示例的工作流输出通常已经足够。设置更[正式的评分或 metric](use-metrics-to-measure-quality.md) 所带来的收益，尚不足以抵消额外投入。

轻量 evaluation 允许你将测试数据集中的示例逐个通过工作流运行，并将输出写回数据集。然后你可以并排检查这些输出，并将它们与预期输出（如果有）进行视觉比较。

## 工作方式 <a href="#how-it-works" id="how-it-works"></a>

{% hint style="info" %}
**Google Sheets credential**

Evaluation 使用 data table 或 Google Sheets 存储测试数据集。要使用 Google Sheets 作为数据集来源，请配置 [Google Sheets credential](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/credentials/google)。
{% endhint %}

轻量 evaluation 在工作流的 `Editor` 选项卡中进行，不过你会在 `Evaluations` 选项卡中找到设置说明。

步骤：

1. 创建数据集
2. 将数据集连接到工作流
3. 将工作流输出写回数据集
4. 运行 evaluation

下面的说明会使用一个示例工作流，它会为传入的支持工单分配类别和优先级。

![AI 工作流示例](../../.gitbook/assets/example-ai-workflow.png)

### 1. 创建数据集 <a href="#1-create-a-dataset" id="1-create-a-dataset"></a>

创建一个 data table 或 Google Sheet，为工作流准备少量示例。你的数据集应包含以下列：

- 工作流输入
- （可选）预期或正确的工作流输出
- 实际输出

将实际输出列留空，因为你会在 evaluation 期间填充它们。

<figure>
<img src="../../.gitbook/assets/sample-dataset.png" alt="">
<figcaption>支持工单分类工作流的<a href="https://docs.google.com/spreadsheets/d/1uuPS5cHtSNZ6HNLOi75A2m8nVWZrdBZ_Ivf58osDAS8/edit?gid=294497137#gid=294497137">示例数据集</a>。</figcaption>
</figure>

### 2. 将数据集连接到工作流 <a href="#2-wire-the-dataset-up-to-your-workflow" id="2-wire-the-dataset-up-to-your-workflow"></a>

#### 插入 evaluation trigger 以拉取数据集 <a href="#insert-an-evaluation-trigger-to-pull-in-your-dataset" id="insert-an-evaluation-trigger-to-pull-in-your-dataset"></a>

每次 [evaluation trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.evaluationtrigger) 运行时，都会输出一个 item，代表数据集中的一行。

点击 evaluation trigger 左侧的 `Evaluate all` 按钮，会按顺序多次运行你的工作流，数据集中的每一行运行一次。这是 evaluation trigger 的特殊行为。

连接 trigger 时，你通常只想运行一次。可以通过以下任一方式做到：

- 将 trigger 的 `Max rows to process` 设置为 1
- 点击 trigger 上的 `Execute node` 按钮（而不是 `Evaluate all` 按钮）

#### 将 trigger 连接到工作流 <a href="#wire-the-trigger-up-to-your-workflow" id="wire-the-trigger-up-to-your-workflow"></a>

现在可以将 evaluation trigger 连接到工作流的其余部分，并引用它输出的数据。至少，你需要在工作流后续部分使用数据集的输入列。

如果工作流中有多个 trigger，你需要[将它们的分支合并在一起](fix-common-issues.md#combining-multiple-triggers)。

<figure>
<img src="../../.gitbook/assets/connecting-evaluation-trigger.png" alt="">
<figcaption>已添加并连接 evaluation trigger 的支持工单分类工作流。</figcaption>
</figure>

### 3. 将工作流输出写回数据集 <a href="#3-write-workflow-outputs-back-to-dataset" id="3-write-workflow-outputs-back-to-dataset"></a>

要在 evaluation 运行时填充数据集的输出列：

- 插入 [evaluation node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.evaluation) 的 `Set outputs` action
- 在工作流已经产生你要评估的输出之后，将它连接到工作流
- 在节点参数中，将工作流输出映射到正确的数据集列

<figure>
<img src="../../.gitbook/assets/connecting-set-outputs-node.png" alt="">
<figcaption>已添加并连接 `set outputs` 节点的支持工单分类工作流。</figcaption>
</figure>

### 4. 运行 evaluation <a href="#4-run-evaluation" id="4-run-evaluation"></a>

点击 evaluation trigger 左侧的 **Execute workflow** 按钮。工作流会多次执行，数据集中的每一行执行一次：

![Execute workflow 按钮](../../.gitbook/assets/execute-workflow-button.png)

在 data table 或 Google Sheet 中检查每次执行的输出。如有需要，可以使用工作流的 `executions` 选项卡检查执行详情。

当数据集增长到超过少量示例时，可以考虑使用 [metric-based evaluation](use-metrics-to-measure-quality.md)，从数值角度查看性能。另请参阅[提示和常见问题](fix-common-issues.md)。

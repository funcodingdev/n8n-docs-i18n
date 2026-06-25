---
description: 查看和筛选当前在画布中打开的工作流的所有 execution。
contentType: howto
nodeTitle: View executions for a single workflow
originalFilePath: workflows/executions/single-workflow-executions.md
originalUrl: 'https://docs.n8n.io/workflows/executions/single-workflow-executions'
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/view-executions-for-a-single-workflow
layout:
  description:
    visible: false
---

# 工作流级 execution 列表 <a href="#workflow-level-executions-list" id="workflow-level-executions-list"></a>

工作流中的 **Executions** 列表会显示该工作流的所有 execution。

{% hint style="info" %}
**已删除的工作流**

删除工作流时，n8n 也会删除其 execution 历史。这意味着你无法查看已删除工作流的 execution。
{% endhint %}

{% hint style="info" %}
**Execution history 和 workflow history**

不要将 execution 列表与 [Workflow history](../../manage-workflows/view-change-history.md) 混淆。

Execution 是工作流运行记录。通过 executions 列表，你可以查看当前工作流版本过去的运行。你可以将先前 execution 复制到编辑器中，在当前工作流里[调试并重新运行过去的 execution](debug-executions.md)。

Workflow history 是工作流的先前版本，例如包含不同 node 或不同参数设置的版本。
{% endhint %}


## 查看单个工作流的 execution <a href="#view-executions-for-a-single-workflow" id="view-executions-for-a-single-workflow"></a>

在工作流中，选择顶部菜单中的 **Executions** 标签。你可以预览该工作流的所有 execution。

## 筛选 execution <a href="#filter-executions" id="filter-executions"></a>

你可以筛选 executions 列表。

1. 在工作流中，选择 **Executions**。
2. Select **Filters**.
3. 输入筛选条件。你可以按以下字段筛选：
	* **Status**：从 **Failed**、**Running**、**Success** 或 **Waiting** 中选择。
	* **Execution start**：查看在给定时间内开始的 execution。
	* **Saved custom data**：这是你在工作流中使用 Code node 创建的数据。输入 key 和 value 进行筛选。有关添加自定义数据的信息，请参阅[自定义 execution 数据](customize-executions-data.md)。

		{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/hEbJHXcEBce6m2wEE65f/" %}


## 重试失败的工作流 <a href="#retry-failed-workflows" id="retry-failed-workflows"></a>

如果工作流 execution 失败，你可以重试该 execution。如需重试失败的工作流：

1. 打开 **Executions** 列表。
2. 对于要重试的工作流 execution，选择 **Refresh** <img src="../../../../build/.gitbook/assets/refresh.png" alt="Refresh icon" data-size="line">。
{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/yD2T5eTeZvZaPRV8P7MJ/" %}

---
contentType: howto
nodeTitle: View all executions
originalFilePath: workflows/executions/all-executions.md
originalUrl: https://docs.n8n.io/workflows/executions/all-executions
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/view-all-executions
description: 查看和筛选所有工作流的全部 execution。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 查看所有 execution

如需查看 n8n 实例中的 **all executions**，进入 **Overview** 页面，然后点击 Executions 标签。这会显示你有权访问的工作流中的所有 execution。

如果你的 n8n 实例支持 **projects**，你也可以在有权访问的 project 中查看 executions 标签。这只会显示指定 project 内工作流的 execution。

{% hint style="info" %}
**已删除的工作流**

删除工作流时，n8n 也会删除其 execution 历史。这意味着你无法查看已删除工作流的 execution。
{% endhint %}

## 筛选 execution <a href="#filter-executions" id="filter-executions"></a>

你可以筛选 executions 列表：

1. 在 **Overview** 页面或特定 **project** 中选择 **Executions** 标签，打开列表。
2. 选择 **Filters**。
3. 输入筛选条件。你可以按以下字段筛选：
   * **Workflows**：选择所有工作流，或选择特定工作流名称。
   * **Status**：从 **Failed**、**Running**、**Success** 或 **Waiting** 中选择。
   * **Execution start**：查看在给定时间内开始的 execution。
   * **Saved custom data**：这是你在工作流中使用 Code node 创建的数据。输入 key 和 value 进行筛选。有关添加自定义数据的信息，请参阅[自定义 execution 数据](customize-executions-data.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/hEbJHXcEBce6m2wEE65f/" %}

## 重试失败的工作流 <a href="#retry-failed-workflows" id="retry-failed-workflows"></a>

如果工作流 execution 失败，你可以重试该 execution。如需重试失败的工作流：

1. 在 **Overview** 页面或特定 **project** 中选择 **Executions** 标签，打开列表。
2. 在要重试的 execution 上，选择 **Retry execution** <img src="../../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options menu icon" data-size="line">。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/yD2T5eTeZvZaPRV8P7MJ/" %}

## 将先前 execution 的数据加载到当前工作流 <a href="#load-data-from-previous-executions-into-your-current-workflow" id="load-data-from-previous-executions-into-your-current-workflow"></a>

你可以将先前工作流的数据重新加载到画布中。更多信息请参阅[调试 execution](debug-executions.md)。

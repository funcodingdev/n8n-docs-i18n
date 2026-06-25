---
contentType: howto
title: 调试并重新运行过去的 execution
description: >-
  如何将 execution 数据复制到当前工作流中，以调试之前的 execution。
nodeTitle: Debug executions
originalFilePath: workflows/executions/debug.md
originalUrl: 'https://docs.n8n.io/workflows/executions/debug'
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/debug-executions
layout:
  description:
    visible: false
---

# 调试并重新运行过去的 execution <a href="#debug-and-re-run-past-executions" id="debug-and-re-run-past-executions"></a>

{% hint style="info" %}
**功能可用性**

适用于 n8n Cloud 和已注册的 Community 计划。
{% endhint %}

你可以将先前 execution 中的数据加载到当前工作流中。这对于调试失败的 production execution 数据很有用：你可以查看失败的 execution，修改工作流以修复问题，然后使用先前的 execution 数据重新运行。

## 加载数据 <a href="#load-data" id="load-data"></a>

如需加载先前 execution 的数据：

1. 在工作流中，选择 **Executions** 标签，查看 **Executions** 列表。
1. 选择要调试的 execution。n8n 会根据工作流成功或失败显示不同选项：
	* 对于失败的 execution：选择 **Debug in editor**。
	* 对于成功的 execution：选择 **Copy to editor**。
1. n8n 会将 execution 数据复制到当前工作流，并在工作流的第一个 node 中[固定数据](../../work-with-data/pin-and-mock-data.md)。

{% hint style="info" %}
**检查保存哪些 execution**

**Executions** 列表中可用的 execution 取决于你的[工作流设置](../../manage-workflows/configure-workflow-settings.md)。
{% endhint %}

---
contentType: howto
description: 如何处理执行错误。
nodeTitle: Handle errors gracefully
originalFilePath: flow-logic/error-handling.md
originalUrl: 'https://docs.n8n.io/flow-logic/error-handling'
url: 'https://docs.n8n.io/build/flow-logic/handle-errors-gracefully'
layout:
  description:
    visible: false
---

# 错误处理 <a href="#error-handling" id="error-handling"></a>

设计流程逻辑时，建议考虑潜在错误，并设置能优雅处理这些错误的方法。通过 error workflow，你可以控制 n8n 在工作流执行失败时如何响应。

{% hint style="info" %}
**调查错误**

要调查失败的执行，你可以：

* 查看你的 [Executions](../understand-workflows/understand-executions/README.md)，可以查看[单个工作流](../understand-workflows/understand-executions/view-executions-for-a-single-workflow.md)，也可以查看[你有权访问的所有工作流](../understand-workflows/understand-executions/view-all-executions.md)。你可以将[上一次执行的数据加载](../understand-workflows/understand-executions/debug-executions.md)到当前工作流中。
* 启用 [Log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems)。
{% endhint %}

## 创建并设置 error workflow <a href="#create-and-set-an-error-workflow" id="create-and-set-an-error-workflow"></a>

对于每个工作流，你都可以在 **Workflow Settings** 中设置 error workflow。它会在执行失败时运行。这意味着，例如当工作流执行出错时，你可以发送电子邮件或 Slack 告警。error workflow 必须以 [Error Trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.errortrigger) 开头。

你可以为多个工作流使用同一个 error workflow。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/odStQfuU7M0KPowwye9k/" %}

## 错误数据 <a href="#error-data" id="error-data"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/rAiMowL1bA7C4GcH8FyS/" %}

## 使用 Stop And Error 造成工作流执行失败 <a href="#cause-a-workflow-execution-failure-using-stop-and-error" id="cause-a-workflow-execution-failure-using-stop-and-error"></a>

创建并设置 error workflow 后，n8n 会在执行失败时运行它。通常，这类失败来自节点设置错误，或工作流耗尽内存等情况。

你可以将 [Stop And Error](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.stopanderror) 节点添加到工作流中，在你选择的条件下强制执行失败，并触发 error workflow。

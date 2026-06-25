---
title: 'Manual、partial 和 production executions'
description: 'Manual、partial 和 automatic workflow executions 的区别。'
contentType: explanation
nodeTitle: Types of executions
originalFilePath: workflows/executions/manual-partial-and-production-executions.md
originalUrl: >-
  https://docs.n8n.io/workflows/executions/manual-partial-and-production-executions
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/types-of-executions
layout:
  description:
    visible: false
---

# Manual、partial 和 production executions <a href="#manual-partial-and-production-executions" id="manual-partial-and-production-executions"></a>

n8n 手动执行工作流（点击 **Execute Workflow** 按钮）和自动执行工作流（工作流处于 **Active** 状态，并由事件或 schedule 触发）的方式存在一些重要区别。

## Manual executions <a href="#manual-executions" id="manual-executions"></a>

Manual execution 允许你直接从画布[^1]运行工作流，以测试工作流逻辑。这类 execution 是“ad-hoc”的：只有当你手动选择 **Execute workflow** 按钮时才会运行。

Manual execution 允许你在构建过程中迭代测试、跟随流程逻辑并查看数据转换，从而让构建工作流更容易。你可以通过提供不同输入 item 和修改 node options，测试条件分支、数据格式变更和循环行为。

{% hint style="info" %}
**固定 execution 数据**

执行 manual execution 时，你可以使用 [data pinning](../../work-with-data/pin-and-mock-data.md) “pin” 或“冻结”某个 node 的输出数据。你也可以选择编辑已固定的数据。

在后续运行中，n8n 不会执行已固定的 node，而是会替换为已固定数据，并继续按流程逻辑执行。这允许你在不处理可变数据或不重复查询外部服务的情况下进行迭代。Production execution 会忽略所有已固定数据。
{% endhint %}

## Partial executions <a href="#partial-executions" id="partial-executions"></a>

在 **Editor** 标签中点击工作流底部的 **Execute workflow** 按钮，会手动运行整个工作流。你也可以执行 partial execution，只运行工作流中的特定步骤。Partial execution 是一种只运行工作流 node 子集的 manual execution。

如需执行 partial execution，选择一个 node，打开其详情视图，然后选择 **Execute step**。这会执行该特定 node，以及填充其输入数据所需的任何前置 node。构建时，你也可以临时禁用工作流链中的特定 node，以避免与这些服务交互。

在更新特定 node 的逻辑时，partial execution 尤其有用，因为它允许你使用相同输入数据重新执行该 node。

### 排查 partial execution 问题 <a href="#troubleshooting-partial-executions" id="troubleshooting-partial-executions"></a>

运行 partial execution 时，可能遇到的一些常见问题包括：


> The destination node is not connected to any trigger. Partial executions need a trigger.


当你尝试在工作流未连接 trigger 的情况下执行 partial execution 时，会出现此错误消息。Manual execution（包括 partial execution）会尽可能模拟 production execution。其中一部分要求是需要 trigger node 来描述工作流逻辑应在何时执行。

如需规避此问题，请将 trigger node 连接到包含你要执行 node 的工作流。多数情况下，[manual trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger) 是最简单的选择。

> Please execute the whole workflow, rather than just the node. (Existing execution data is too large.)

在包含大量分支的工作流上执行 partial execution 时，可能会出现此错误。Partial execution 会以 full execution 不需要的方式向 n8n 后端发送数据和工作流逻辑。当工作流超过这些消息允许的最大大小时，就会发生此错误。

如需规避此问题，可考虑在运行 partial execution 时使用 [limit node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.limit) 限制 node 输出。工作流按预期运行后，你可以在启用 production execution 前禁用或删除 limit node。

## Production executions <a href="#production-executions" id="production-executions"></a>

当触发事件或 schedule 自动运行工作流时，就会发生 production execution。在[付费计划](https://n8n.io/pricing/)中，production execution 会计入你的 execution 配额。关于哪些会计数、哪些不会计数，详情请参阅 [Execution 如何计入配额](README.md#how-executions-count-towards-quotas)。

如需配置 production execution，必须连接一个 [trigger node](#user-content-fn-2)[^2]（除 [manual trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger) 外的任意 trigger 都可以），并将工作流开关切换为 **Active**。发布后，只要触发条件发生，工作流就会自动执行。

Production execution 的执行流不会像 manual execution 那样显示在工作流的 Editor 标签中。相反，你可以根据[工作流设置](../../manage-workflows/configure-workflow-settings.md)，在工作流的 **Executions** 标签中查看 execution。你可以从那里使用 [debug in editor 功能](debug-executions.md)探索和排查问题。

[^1]: 画布是 n8n 编辑器 UI 中用于构建工作流的主要界面。你可以在画布上添加并连接 node 来组成工作流。
[^2]: Trigger node 是一种特殊 node，负责根据特定条件执行工作流。所有生产工作流都至少需要一个 trigger，用于确定工作流应在何时运行。

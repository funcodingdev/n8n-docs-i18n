---
description: 用于处理 n8n metadata 的方法。
contentType: reference
hide:
  - toc
nodeTitle: n8n metadata
originalFilePath: code/builtin/n8n-metadata.md
originalUrl: 'https://docs.n8n.io/code/builtin/n8n-metadata'
url: 'https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts/n8n-metadata'
layout:
  description:
    visible: false
---

# n8n metadata <a href="#n8n-metadata" id="n8n-metadata"></a>

用于处理 n8n metadata 的方法。

包括：

* 访问自托管 n8n 的 n8n 环境变量。
* workflow、execution 和 node 的 metadata。
* 关于实例[变量](../define-custom-variables.md)和 [External secrets](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/use-external-secret-stores) 的信息。

{% hint style="info" %}
**Python 支持**

你可以在 Code node 中使用 Python。它不能在 expression 中使用。
{% endhint %}
{% tabs %}
{% tab title="JavaScript" %}
| 方法 | 描述 | 可在 Code node 中使用？ |
| ------ | ----------- | :-------------------------: |
| `$env` | 包含 n8n 实例配置[环境变量](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables)。 | ✅ |
| `$execution.customData` | 设置和获取自定义 execution data。更多信息请参阅 [Custom executions data](../../understand-workflows/understand-executions/customize-executions-data.md)。 | ✅ |
| `$execution.id` | 当前 workflow execution 的唯一 ID。 | ✅ |
| `$execution.mode` | execution 是自动触发，还是通过手动运行 workflow 触发。可选值为 `test` 和 `production`。 | ✅ |
| `$execution.resumeUrl` | 用于恢复等待在 [Wait node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait) 上的 workflow 的 webhook URL。 | ✅ |
| `$getWorkflowStaticData(type)` | 查看[示例](../cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。测试 workflow 时 static data 不会持久化。workflow 必须处于 active 状态，并由 trigger 或 webhook 调用，才能保存 static data。它可用于访问 static workflow data。 | ✅ |
| `$("<node-name>").isExecuted` | 检查某个 node 是否已经执行。 | ✅ |
| `$itemIndex` | item 列表中某个 item 的索引。 | ❌ |
| `$nodeVersion` | 获取当前 node 的版本。 | ✅ |
| `$prevNode.name` | 当前输入来源 node 的名称。使用 Merge node 时，请注意 `$prevNode` 始终使用第一个输入连接器。 | ✅ |
| `$prevNode.outputIndex` | 当前输入来源的输出连接器索引。当上一个 node 有多个输出时使用它（例如 If 或 Switch node）。使用 Merge node 时，请注意 `$prevNode` 始终使用第一个输入连接器。 | ✅ |
| `$prevNode.runIndex` | 生成当前输入的上一个 node 的运行。使用 Merge node 时，请注意 `$prevNode` 始终使用第一个输入连接器。 | ✅ |
| `$runIndex` | n8n 执行当前 node 的次数。以 0 为基数（第一次运行是 0，第二次是 1，依此类推）。 | ✅ |
| `$secrets` | 包含关于你的 [External secrets](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/use-external-secret-stores) 设置的信息。 | ❌ |
| `$vars` | 包含 active environment 中可用的[变量](../define-custom-variables.md)。 | ✅ |
| `$version` | node 版本。 | ❌ |
| `$workflow.active` | workflow 是否 active（true）或非 active（false）。 | ✅ |
| `$workflow.id` | workflow ID。 | ✅ |
| `$workflow.name` | workflow 名称。 | ✅ |
{% endtab %}

{% tab title="Python (native)" %}
| 方法 | 描述 |
| ------ | ----------- |
| `_items` | 包含 "Run once for all items" 模式下的输入 item。 |
| `_item` | 包含 "Run once for each item" 模式下正在迭代的 item。 |
{% endtab %}

{% tab title="Python (Pyodide, deprecated)" %}
| 方法 | 描述 |
| ------ | ----------- |
| `_env` | 包含 n8n 实例配置[环境变量](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables)。 |
| `_execution.customData` | 设置和获取自定义 execution data。更多信息请参阅 [Custom executions data](../../understand-workflows/understand-executions/customize-executions-data.md)。 |
| `_execution.id` | 当前 workflow execution 的唯一 ID。 |
| `_execution.mode` | execution 是自动触发，还是通过手动运行 workflow 触发。可选值为 `test` 和 `production`。 |
| `_execution.resumeUrl` | 用于恢复等待在 [Wait node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait) 上的 workflow 的 webhook URL。 |
| `_getWorkflowStaticData(type)` | 查看[示例](../cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata.md)。测试 workflow 时 static data 不会持久化。workflow 必须处于 active 状态，并由 trigger 或 webhook 调用，才能保存 static data。它可用于访问 static workflow data。 |
| `_("<node-name>").isExecuted` | 检查某个 node 是否已经执行。 |
| `_nodeVersion` | 获取当前 node 的版本。 | ✅ |
| `_prevNode.name` | 当前输入来源 node 的名称。使用 Merge node 时，请注意 `_prevNode` 始终使用第一个输入连接器。 |
| `_prevNode.outputIndex` | 当前输入来源的输出连接器索引。当上一个 node 有多个输出时使用它（例如 If 或 Switch node）。使用 Merge node 时，请注意 `_prevNode` 始终使用第一个输入连接器。 |
| `_prevNode.runIndex` | 生成当前输入的上一个 node 的运行。使用 Merge node 时，请注意 `_prevNode` 始终使用第一个输入连接器。 |
| `_runIndex` | n8n 执行当前 node 的次数。以 0 为基数（第一次运行是 0，第二次是 1，依此类推）。 |
| `_secrets` | 包含关于你的 [External secrets](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/use-external-secret-stores) 设置的信息。 |
| `_vars` | 包含 active environment 中可用的[变量](../define-custom-variables.md)。 |
| `_workflow.active` | workflow 是否 active（true）或非 active（false）。 |
| `_workflow.id` | workflow ID。 |
| `_workflow.name` | workflow 名称。 |
{% endtab %}
{% endtabs %}

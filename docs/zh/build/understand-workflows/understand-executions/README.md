---
description: Execution 是工作流的一次运行。
contentType: overview
nodeTitle: Understand executions
originalFilePath: workflows/executions/index.md
originalUrl: 'https://docs.n8n.io/workflows/executions'
url: 'https://docs.n8n.io/build/understand-workflows/understand-executions'
layout:
  description:
    visible: false
---

# Executions <a href="#executions" id="executions"></a>

Execution 是工作流的一次运行。

## Execution 模式 <a href="#execution-modes" id="execution-modes"></a>

Execution 有两种模式：

* **Manual:** 点击 **Execute Workflow** 手动运行工作流。通过手动运行进行测试时，保持工作流未发布。
* **Production:** 生产工作流会自动运行。发布某个工作流版本即可将其投入生产。

## Execution 如何计入配额 <a href="#how-executions-count-towards-quotas" id="how-executions-count-towards-quotas"></a>

无论是 Cloud 还是自托管，[付费计划](https://n8n.io/pricing/)都有 execution 限额。只有 production execution 会计入此配额。这类 execution 由 trigger、schedule 或 polling 自动启动。无论实例环境是开发还是生产，此区别都适用。

### 按 trigger 类型计算 execution <a href="#execution-count-by-trigger-type" id="execution-count-by-trigger-type"></a>

Execution 的计算方式取决于所使用的 trigger node 类型：

* **Schedule Trigger nodes:** 每当 node 触发一次，就计为一次 execution，无论结果如何。
* **Polling nodes（例如 Google Drive Trigger）：** 只有在发现新数据时才计为一次 execution。没有返回结果的轮询不会计为 execution。
* **Webhook Trigger nodes:** 每个激活 trigger 的入站请求都会计为一次 execution。这包括 body 为空的请求（例如 `{}`）。在工作流启动前失败的格式错误请求不会计为 execution。

### 不计入配额的 trigger 和运行 <a href="#triggers-and-runs-that-dont-count" id="triggers-and-runs-that-dont-count"></a>

以下内容不会计入 execution 配额：

* **Manual executions:** 在构建或测试时从编辑器运行工作流。
* **Sub-workflow executions:** 当工作流使用 Execute Sub-workflow node 调用另一个工作流时，只计算父级（顶层）execution。
* **Error workflow executions:** 作为 [error workflow](../../flow-logic/handle-errors-gracefully.md) 设置的工作流运行。
* **未返回数据的 poll:** Polling trigger 只有在发现新数据时才计数。
* **格式错误或被拒绝的请求:** 在工作流启动前失败的 Webhook 请求。

## Execution 列表 <a href="#execution-lists" id="execution-lists"></a>

n8n 提供两个 execution 列表：

* [Workflow-level executions](view-executions-for-a-single-workflow.md)：此 execution 列表显示单个工作流的 execution。
* [All executions](view-all-executions.md)：此列表显示所有工作流的全部 execution。

n8n 支持[向 execution 添加自定义数据](customize-executions-data.md)。

## Execution 数据遮盖 <a href="#execution-data-redaction" id="execution-data-redaction"></a>

你可以遮盖 execution 数据以保护敏感信息。遮盖会隐藏工作流 execution 的输入和输出数据，同时保留状态、时间和 node 名称等 execution 元数据。详情请参阅 [Execution data redaction](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data)。

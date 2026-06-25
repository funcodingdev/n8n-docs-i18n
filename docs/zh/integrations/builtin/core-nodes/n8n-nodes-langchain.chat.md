---
title: Chat node documentation
description: >-
  了解如何在 n8n 中使用 Chat node。按照技术文档将 Chat node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Chat node documentation
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-langchain.chat.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat'
layout:
  description:
    visible: false
---

# Chat node <a href="#chat-node" id="chat-node"></a>

将 Chat node 与 [Chat Trigger](n8n-nodes-base.compression/n8n-nodes-base.compression.md) node 一起使用，可向 chat 发送消息，并可选择等待用户响应。这支持 chat workflow 中的 human-in-the-loop（HITL）用例，让你可以在单次 execution 中进行多轮 chat 交互。Chat node 也可以作为 AI Agent 的 tool 使用。

{% hint style="info" %}
**Chat Trigger node**

Chat node 要求 workflow 中存在 [Chat Trigger](n8n-nodes-base.compression/n8n-nodes-base.compression.md) node，并且 [Response Mode](n8n-nodes-base.compression/n8n-nodes-base.compression.md#response-mode) 设置为 'Using Response Nodes'。
{% endhint %}

{% hint style="warning" %}
**不支持 Embedded mode**

当 Chat Trigger node 设置为 **Embedded** mode 时，不支持 Chat node。在 Embedded mode 中，请改用 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) node。
{% endhint %}

{% hint style="info" %}
**以前的版本**

在以前的版本中，此 node 名为 "Respond to Chat"，并使用单个 "Wait for User Reply" 切换项。该功能已重组为两个不同 action，并增加了更多 response type。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

使用以下参数配置此 node。

### Operation <a href="#operation" id="operation"></a>

Chat node 支持以下操作：

* **Send Message**：向 chat 发送消息。发送后 workflow execution 会立即继续。
* **Send and Wait for Response**：向 chat 发送消息并等待用户响应。此操作会暂停 workflow execution，直到用户提交响应。

选择 **Send and Wait for Response** 会启用[等待响应](#waiting-for-a-response)中讨论的其他参数和选项。

### Message <a href="#message" id="message"></a>

要发送到 chat 的消息。两个操作都可使用此参数。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些 **Options** 进一步细化 node 行为。

### Add Memory Input Connection <a href="#add-memory-input-connection" id="add-memory-input-connection"></a>

选择是否要将 Chat node 中的消息提交到连接的 memory。Agent 或 chain [root node](../cluster-nodes/root-nodes/README.md) 与 Chat node 之间使用共享 memory，会为这些消息附加相同的 session key，并让你捕获完整的消息历史。

## 等待响应 <a href="#waiting-for-a-response" id="waiting-for-a-response"></a>

选择 **Send and Wait for Response** 操作后，你可以发送消息并暂停 workflow execution，直到有人响应。这支持在单次 execution 中实现多轮对话和审批 workflow。

### Response Type <a href="#response-type" id="response-type"></a>

你可以在以下 response 类型之间选择：

* **Free Text**：用户可以在 chat 中输入任意响应。这与之前的 "Wait for User Reply" 选项行为相同。
* **Approval**：用户可以使用消息中的 inline button 批准或拒绝。你也可以选择允许用户输入自定义响应。

根据所选类型的不同，可用参数和选项也不同。

### Free Text 参数和选项 <a href="#free-text-parameters-and-options" id="free-text-parameters-and-options"></a>

使用 Free Text response type 时，用户可以输入任意消息作为响应。

**用例：**
- 开放式问题
- 收集详细反馈
- 请求特定信息

**选项：**
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。可以是时间间隔，也可以是具体的时钟时间。

### Approval 参数和选项 <a href="#approval-parameters-and-options" id="approval-parameters-and-options"></a>

使用 Approval response type 时，消息会显示用户可点击的 inline button，用于批准或拒绝。此 response type 遵循 n8n 中其他 human-in-the-loop（HITL）node 的相同模式。

**用例：**
- 简单的是/否决策
- 审批 workflow
- 确认

使用 Approval response type 时，以下参数可用：

* **Type of Approval**：是只显示批准按钮，还是同时显示批准和拒绝按钮。
    - **Approve Only**：显示单个批准按钮
    - **Approve and Disapprove**：显示两个按钮（默认）

* **Approve Button Label**：批准按钮上显示的文本。默认值：`Approve`

* **Disapprove Button Label**：拒绝按钮上显示的文本（仅当 Type of Approval 为 "Approve and Disapprove" 时显示）。默认值：`Disapprove`

* **Block User Input**：是否阻止用户输入自定义消息（启用），或允许用户输入响应（禁用，默认）。
    - 当 **disabled**（默认）时：用户可以点击按钮或输入自定义消息。输入的消息会被视为带自定义消息的拒绝。
    - 当 **enabled** 时：用户只能使用按钮交互。

Approval response type 还提供以下选项：

* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。可以是时间间隔，也可以是具体的时钟时间。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

有关设置 chat interface 的信息，请参阅 [Chat Trigger](n8n-nodes-base.compression/n8n-nodes-base.compression.md) node 文档。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Chat node 文档集成模板](https://n8n.io/integrations/chat)或[搜索所有模板](https://n8n.io/workflows/)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

- 当 Chat Trigger node 的 **Mode** 设置为 **Embedded** 时，不支持 Chat node。在 Embedded mode 中，Chat Trigger node 只提供 **Respond to Webhook** 作为 response mode。请改用 [Respond to Webhook](n8n-nodes-base.respondtowebhook.md) node。
- Chat node 作为 subagent 的 tool 使用时无法工作。
- Chat node 在 subworkflow 中使用时无法工作。这包括在被 AI Agent 用作 tool 的 subworkflow 中使用。
- 请确保 Chat Trigger node 的 Response Mode 设置为 "Using Response Nodes"，以便 Chat node 正常工作。

有关 Chat Trigger node 的常见问题，请参阅 [Common Chat Trigger Node Issues](n8n-nodes-base.compression/common-issues.md)。

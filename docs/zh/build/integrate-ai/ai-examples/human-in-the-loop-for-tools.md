---
title: AI tool 调用中的人在环路
description: >-
  了解如何在 n8n 中要求 AI Agent 执行特定 tool 前先获得人工审批。
contentType: explanation
nodeTitle: tool 的人在环路
originalFilePath: advanced-ai/human-in-the-loop-tools.md
originalUrl: 'https://docs.n8n.io/advanced-ai/human-in-the-loop-tools'
url: 'https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools'
layout:
  description:
    visible: false
---

# AI tool 调用中的人在环路 <a href="#human-in-the-loop-for-ai-tool-calls" id="human-in-the-loop-for-ai-tool-calls"></a>

你可以要求 AI Agent 在执行特定 tool 之前先获得人工审批。当 tool 需要人工审核时，工作流会暂停，并等待人工执行以下操作之一：

- **Approve**：tool 使用 AI 指定的输入执行。
- **Deny**：操作被取消且不会运行。

此功能允许你选择性监督 AI 工作流中的 tool 使用，从而更容易对风险更高的 tool 施加额外审核，例如发送消息、修改记录或删除数据。

## 何时使用人工审核 <a href="#when-to-use-human-review" id="when-to-use-human-review"></a>

人在环路 (HITL) 审核适用于以下场景：

- **tool 执行不可逆操作**：删除数据、发送外部通信或进行购买。
- **存在合规要求**：受监管行业可能要求某些自动化操作必须经过人工审批。
- **涉及高价值决策**：对业务有重大影响的操作适合加入人工监督。
- **你正在建立对 AI 工作流的信任**：一开始启用人工审核，随着信心提升再减少监督。

HITL 可以应用到连接到 AI Agent 节点的所有 tool，也可以只应用到选定的单个 tool。相比一般的输出门控，它提供了更精细的控制。

## 工作方式 <a href="#how-it-works" id="how-it-works"></a>

1. AI Agent 判断自己需要使用一个已启用人工审核的 tool。
2. 工作流暂停，并通过你配置的渠道发送审批请求（例如 Slack、Telegram 或 n8n Chat 界面）。
3. 人工审核者收到请求，请求中会展示 AI 想使用哪个 tool，以及使用哪些参数。
4. 审核者批准或拒绝该请求。
5. 如果批准，tool 会使用 AI 指定的输入执行；如果拒绝，操作会被取消，AI 也会收到拒绝通知。

{% hint style="info" %}
**不同审批渠道**

审核步骤可以通过不同于主交互的渠道发生。例如，你可以让用户通过 n8n Chat 界面与 AI agent 交互，但将审批请求路由到 Slack 中的特定人员。
{% endhint %}

## 为 tool 设置人工审核 <a href="#setting-up-human-review-for-tools" id="setting-up-human-review-for-tools"></a>

### 第 1 步：打开 Tools Panel <a href="#step-1-open-the-tools-panel" id="step-1-open-the-tools-panel"></a>

在工作流中，点击 AI Agent 节点上的 **Tools** 连接器，打开 Tools Panel。

### 第 2 步：添加人工审核步骤 <a href="#step-2-add-a-human-review-step" id="step-2-add-a-human-review-step"></a>

1. 在 Tools Panel 中找到 **Human review** 部分。
2. 从可用选项中选择你偏好的审批渠道。
3. 使用适当的 credential 和设置配置审批渠道。

### 第 3 步：将 tool 连接到审核步骤 <a href="#step-3-connect-tools-to-the-review-step" id="step-3-connect-tools-to-the-review-step"></a>

1. 将需要审批的 tool 添加到人工审核步骤的 tool 连接器。
2. 像往常一样配置每个 tool。



## 可用审批渠道 <a href="#available-approval-channels" id="available-approval-channels"></a>

你可以使用以下任一服务作为人工审核渠道：

| 渠道 | 说明 |
|---------|-------------|
| [Chat](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-langchain.chat) | n8n 内置聊天界面 |
| [Slack](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.slack) | 将审批请求发送到 Slack channel 或私信 |
| [Discord](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.discord) | 将审批请求发送到 Discord channel |
| [Telegram](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.telegram) | 通过 Telegram 发送审批请求 |
| [Microsoft Teams](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.microsoftteams) | 将审批请求发送到 Teams channel 或聊天 |
| [Gmail](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.gmail) | 通过电子邮件发送审批请求 |
| [WhatsApp Business Cloud](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.whatsapp) | 通过 WhatsApp 发送审批请求 |
| [Google Chat](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.googlechat) | 将审批请求发送到 Google Chat |
| [Microsoft Outlook](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.microsoftoutlook) | 通过 Outlook 邮件发送审批请求 |

## 在人工审核 tool 中使用 expression <a href="#using-expressions-in-human-review-tools" id="using-expressions-in-human-review-tools"></a>

### `$tool` 变量 <a href="#the-dollartool-variable" id="the-dollartool-variable"></a>

配置人工审核步骤时，你可以使用 `$tool` 变量为审核者构建消息，提供 AI 正在尝试执行什么操作的上下文。该变量有两个属性：

| 属性 | 说明 |
|----------|-------------|
| `$tool.name` | AI Agent 正在尝试调用的 tool 名称。这是在 n8n 画布上显示的节点名称。 |
| `$tool.parameters` | AI Agent 在 tool 调用中尝试使用的参数。这包括 tool 输入 schema 中配置了 `$fromAI()` expression 的任何字段。 |

**消息配置示例：**

```
The AI wants to use {{ $tool.name }} with the following parameters:
{{ JSON.stringify($tool.parameters, null, 2) }}
```

这有助于审核者在批准或拒绝请求之前，准确理解 AI 正在尝试执行什么操作。

### 在人工审核 tool 中使用 `$fromAI()` <a href="#using-dollarfromai-in-human-review-tools" id="using-dollarfromai-in-human-review-tools"></a>

[`$fromAI()` 函数](use-ai-for-parameters.md) 可用于连接到人工审核步骤的 tool。这意味着 AI 可以动态指定 tool 参数，而人工审核者看到并审批的正是这些由 AI 决定的值。

## System prompt 最佳实践 <a href="#system-prompt-best-practices" id="system-prompt-best-practices"></a>

为了让 AI Agent 正确解读和处理被拒绝的 tool 调用尝试，请在 system prompt 中包含人工审核设置的信息。

{% hint style="warning" %}
**需要配置 system prompt**

请确保在 system prompt 中包含 tool 设置和人工审核步骤。这有助于 AI 理解哪些 tool 需要审批，以及在 tool 调用被拒绝时如何得体地响应。
{% endhint %}

可以考虑包含：

- 哪些 tool 需要人工审批
- 审批被拒绝时会发生什么
- AI 应如何响应拒绝（例如告知用户、建议替代方案或要求澄清）



## Chaining 和 subagent <a href="#chaining-and-subagents" id="chaining-and-subagents"></a>

当你将一个 AI Agent 作为另一个 AI Agent 的 tool 使用时，subagent 中的人工审核步骤可以正常工作。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

- [AI Agent node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
- [Tools Agent](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)
- [AI 中的 tool 是什么？](../understand-ai-components/how-tools-work.md)
- [让 AI 使用 $fromAI() 指定 tool 参数](use-ai-for-parameters.md)

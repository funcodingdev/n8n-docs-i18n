---
title: Microsoft Agent 365 Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Microsoft Agent 365 Trigger node。按照技术文档将
  Microsoft Agent 365 Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Root nodes
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger
url: 'https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.microsoftagent365trigger'
layout:
  description:
    visible: false
---

# Microsoft Agent 365 Trigger node <a href="#microsoft-agent-365-trigger-node" id="microsoft-agent-365-trigger-node"></a>

{% hint style="warning" %}
**早期预览**

这是使用 Microsoft Agent 365 和 n8n 构建 agents 的早期预览。你需要加入 [Frontier preview program](https://adoption.microsoft.com/copilot/frontier-program/) 才能提前访问 Microsoft Agent 365。
{% endhint %}

使用 Microsoft Agent 365 Trigger node 接收来自 Microsoft Agent 365 的消息，并使用 AI 驱动的 agent 能力进行响应。此 node 允许 n8n 作为 Agent 365 agents 的后端。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/microsoftagent365.md)找到此 node 的身份验证信息。
{% endhint %}

## Node 连接器 <a href="#node-connectors" id="node-connectors"></a>

Microsoft Agent 365 Trigger node 可以连接到以下 sub-nodes：

- **Model**：连接语言 model（Chat model sub-node）来处理传入消息。
- **Memory**：连接 memory sub-node 来维护对话上下文。单个 n8n workflow 会驱动 Microsoft 侧的多个 Agent 实例，因此多个用户会与同一个 workflow 交互。请谨慎选择 session ID key，将对话限定到单个 Agent 实例，并防止对话历史在不同实例之间串扰。
- **Tool**：连接 tool sub-nodes，为你的 agent 提供额外能力。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Enable Microsoft Work IQ Tools for A365 <a href="#enable-microsoft-work-iq-tools-for-a365" id="enable-microsoft-work-iq-tools-for-a365"></a>

切换此选项可让你的 agent 通过 Model Context Protocol（MCP）访问 Microsoft 365 tools。默认值：Off。

启用后，请选择以下之一：

- **All**：启用所有可用的 Microsoft MCP tools
- **Selected**：从列表中选择特定 tools：
	- Calendar
	- Mail
	- SharePoint
	- Teams
	- Word
	- 更多

## 入门 <a href="#getting-started" id="getting-started"></a>

我们建议按照以下资源设置 Agent 365 集成：

1. [Microsoft Agent 365 developer documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)：用于构建 Microsoft Agent 365 agents 的官方文档
2. [Agent 365 CLI Documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/agent-365-cli)：用于在 Azure 上部署和管理 Agent 365 应用程序的跨平台命令行工具

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Agent 365 developer documentation](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

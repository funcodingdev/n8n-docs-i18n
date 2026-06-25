---
title: AI Agent node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent node。按照技术文档将 AI Agent node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: n8n-nodes-langchain.agent
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent
layout:
  description:
    visible: false
---

# AI Agent node <a href="#ai-agent-node" id="ai-agent-node"></a>

[AI agent](#user-content-fn-1)[^1] 是一种自主系统，它接收数据、做出理性决策，并在其环境中采取行动以实现特定目标。AI agent 的环境是 agent 可以访问、但不属于 agent 自身的一切。此 agent 使用外部 tools[^2] 和 API 执行动作并检索信息。它可以理解不同 tool 的能力，并根据任务决定使用哪个 tool。

{% hint style="info" %}
**连接 tool**

你必须至少将一个 tool [sub-node](../../sub-nodes/README.md) 连接到 AI Agent node。
{% endhint %}

{% hint style="info" %}
**Agent 类型**

在版本 1.82.0 之前，AI Agent 有一个设置，可作为不同 agent 类型工作。该设置现已移除，所有 AI Agent node 都作为 `Tools Agent` 工作，这也是此前推荐且最常用的设置。如果你在 workflow 或模板中使用较旧版本的 AI Agent，只要它们设置为 `Tools Agent`，更新后的 node 应会继续按预期运行。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.agent 集成模板](https://n8n.io/integrations/agent)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 关于 agents 的文档](https://js.langchain.com/docs/concepts/agents/)。

刚接触 AI Agents？请阅读 [n8n blog 的 AI agents 介绍](https://blog.n8n.io/ai-agents/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议的解决步骤，请参阅[常见问题](common-issues.md)。

[^1]: AI agent 是一种人工智能系统，能够响应请求、做出决策，并为用户执行现实世界中的任务。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^2]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

---
title: Simple Memory node 文档
description: >-
  了解如何在 n8n 中使用 Simple Memory node。按照技术文档将 Simple Memory node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-langchain.memorybufferwindow
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow
layout:
  description:
    visible: false
---

# Simple Memory node <a href="#simple-memory-node" id="simple-memory-node"></a>

使用 Simple Memory node 在 workflow 中持久化[^1] chat history。

在本页中，你可以找到 Simple Memory node 支持的 operations 列表，以及更多相关资源链接。

{% hint style="warning" %}
**如果 n8n 以 queue mode 运行，请不要使用此 node**

如果你的 n8n instance 使用 [queue mode](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/enable-queue-mode)，此 node 无法在 active production workflow 中工作。这是因为 n8n 无法保证每次调用 Simple Memory 都会进入同一个 worker。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

配置以下参数来配置此 node：

* **Session Key**：输入用于在 workflow data 中存储 memory 的 key。
* **Context Window Length**：输入要作为 context 考虑的前序 interactions 数量。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.memorybufferwindow 集成模板](https://n8n.io/integrations/window-buffer-memory)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain Buffer Window Memory 文档](https://v03.api.js.langchain.com/classes/langchain.memory.BufferWindowMemory.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或故障以及建议解决方案，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 语境中，memory 允许 AI tools 在 interactions 之间持久化 message context。例如，这允许你与 AI agents 进行持续对话，而无需在每条 message 中提交 ongoing context。在 n8n 中，AI agent nodes 可以使用 memory，但 AI chains 不能。

---
title: MongoDB Chat Memory node 文档
description: >-
  了解如何在 n8n 中使用 MongoDB Chat Memory node。按照技术文档将 MongoDB Chat
  Memory node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: MongoDB Chat Memory node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymongochat
layout:
  description:
    visible: false
---

# MongoDB Chat Memory node <a href="#mongodb-chat-memory-node" id="mongodb-chat-memory-node"></a>

使用 MongoDB Chat Memory node 将 MongoDB 用作存储 chat history 的 memory[^1] server。

在本页中，你可以找到 MongoDB Chat Memory node 支持的 operations 列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/mongodb.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Session Key**：输入用于在 workflow data 中存储 memory 的 key。
* **Collection Name**：输入用于存储 chat history 的 collection 名称。如果 collection 不存在，系统会创建它。
* **Database Name**：输入用于存储 chat history 的 database 名称。如果未提供，则使用 credentials 中的 database。
* **Context Window Length**：输入要作为 context 考虑的前序 interactions 数量。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain MongoDB Chat Message History 文档](https://js.langchain.com/docs/integrations/memory/mongodb)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 单一 memory instance <a href="#single-memory-instance" id="single-memory-instance"></a>

如果你向 workflow 添加多个 MongoDB Chat Memory node，默认情况下所有 nodes 都会访问同一个 memory instance。在执行会覆盖现有 memory contents 的破坏性 actions 时请谨慎，例如 [Chat Memory Manager](./n8n-nodes-langchain.memorymanager.md) node 中的 override all messages operation。如果想在 workflow 中使用多个 memory instance，请在不同 memory nodes 中设置不同 session IDs。

[^1]: 在 AI 语境中，memory 允许 AI tools 在 interactions 之间持久化 message context。例如，这允许你与 AI agents 进行持续对话，而无需在每条 message 中提交 ongoing context。在 n8n 中，AI agent nodes 可以使用 memory，但 AI chains 不能。

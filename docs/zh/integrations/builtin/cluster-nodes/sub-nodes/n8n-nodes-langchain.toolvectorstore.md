---
title: Vector Store Question Answer Tool node 文档
description: >-
  了解如何在 n8n 中使用 Vector Store Question Answer Tool node。按照技术文档将 Vector
  Store Question Answer Tool node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Vector Store Question Answer Tool node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore
layout:
  description:
    visible: false
---

# Vector Store Question Answer Tool node <a href="#vector-store-question-answer-tool-node" id="vector-store-question-answer-tool-node"></a>

Vector Store Question Answer node 是一个 tool[^1]，允许 agent[^2] 基于来自 [vector store](#user-content-fn-3)[^3] 的 chunks 汇总结果并回答问题。

在本页中，你可以找到 Vector Store Question Answer node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**示例和模板**

有关帮助你开始使用的 usage examples 和 templates，请参阅 n8n 的 [Vector Store Question Answer Tool integrations](https://n8n.io/integrations/vector-store-tool/) 页面。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Description of Data <a href="#description-of-data" id="description-of-data"></a>

输入 vector store 中 data 的 description。

### Limit <a href="#limit" id="limit"></a>

要返回的最大 results 数量。

## n8n 如何填充 tool description <a href="#how-n8n-populates-the-tool-description" id="how-n8n-populates-the-tool-description"></a>

n8n 使用 node name（选择名称即可编辑）和 **Description of Data** 参数，通过以下格式为 AI agents 填充 tool description：

> Useful for when you need to answer questions about [node name]. Whenever you need information about [Description of Data], you should ALWAYS use this. Input should be a fully formed question.

node name 中的 spaces 会在 tool description 中转换为 underscores。

{% hint style="warning" %}
**避免在 node names 中使用 special characters**

在 node name 中使用 special characters 会导致 agent 运行时报错：

![model errors from special characters](../../../.gitbook/assets/name-characters-error.png)

node names 只能使用 alphanumeric characters、spaces、dashes 和 underscores。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

在 n8n 网站查看 [example workflows 和 related content](https://n8n.io/integrations/vector-store-tool/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: 在 AI 语境中，tool 是一种附加 resource，AI 在响应 request 时可以引用它来获取特定 information 或 functionality。AI model 可以使用 tool 与 external systems 交互，或完成具体、聚焦的 tasks。
[^2]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。
[^3]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。

---
title: Reranker Cohere
description: >-
  了解如何在 n8n 中使用 Reranker Cohere node。按照技术文档将 Cohere reranking
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Reranker Cohere
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere
layout:
  description:
    visible: false
---

# Reranker Cohere <a href="#reranker-cohere" id="reranker-cohere"></a>

Reranker Cohere node 允许你对来自 [vector store](#user-content-fn-2)[^2] 的结果 chunks 进行 rerank[^1]。你可以将此 node 连接到 vector store。

reranker 会按相关性从高到低，重新排序从 vector store 中针对给定 query 检索到的 documents 列表。

在本页中，你可以找到 Reranker Cohere node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/cohere.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Model <a href="#model" id="model"></a>

选择要使用的 reranking model。你可以在 [Cohere model 文档](https://docs.cohere.com/docs/models#rerank)中了解更多可用 models。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Reranker Cohere 集成模板](https://n8n.io/integrations/reranker-cohere)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Reranking 是一种优化 candidate documents 列表顺序的技术，用于提升 search results 的相关性。Retrieval-Augmented Generation（RAG）和其他应用会使用 reranking，为 generation 或 downstream tasks 优先选择最相关的信息。
[^2]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。

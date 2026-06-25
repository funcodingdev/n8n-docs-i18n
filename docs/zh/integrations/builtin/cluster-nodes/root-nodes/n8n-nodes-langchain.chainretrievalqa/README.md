---
title: Question and Answer Chain node 文档
description: >-
  了解如何在 n8n 中使用 Question and Answer Chain node。按照技术文档将
  Question and Answer Chain node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-langchain.chainretrievalqa
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa
layout:
  description:
    visible: false
---

# Question and Answer Chain node <a href="#question-and-answer-chain-node" id="question-and-answer-chain-node"></a>

使用 Question and Answer Chain node 将 [vector store](#user-content-fn-1)[^1] 用作 retriever。

在本页中，你可以找到 Question and Answer Chain node 的 node 参数，以及更多相关资源链接。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Query <a href="#query" id="query"></a>

你想提出的问题。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.chainretrievalqa 集成模板](https://n8n.io/integrations/retrieval-qanda-chain)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 LangChain 如何将 vector store 用作 retriever 的示例，请参阅 [LangChain 关于 retrieval chains 的文档](https://js.langchain.com/docs/tutorials/rag/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议的解决步骤，请参阅[常见问题](common-issues.md)。

[^1]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。

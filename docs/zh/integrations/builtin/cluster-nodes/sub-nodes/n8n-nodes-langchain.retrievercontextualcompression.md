---
title: Contextual Compression Retriever node 文档
description: >-
  了解如何在 n8n 中使用 Contextual Compression Retriever node。按照技术文档将 Contextual
  Compression Retriever node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Contextual Compression Retriever node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrievercontextualcompression
layout:
  description:
    visible: false
---

# Contextual Compression Retriever node <a href="#contextual-compression-retriever-node" id="contextual-compression-retriever-node"></a>

Contextual Compression Retriever node 会考虑 query 的 context，从而改进 [vector store](#user-content-fn-1)[^1] document similarity searches 返回的 answers。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Contextual Compression Retriever node 文档集成模板](https://n8n.io/integrations/contextual-compression-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain contextual compression retriever 文档](https://js.langchain.com/docs/how_to/contextual_compression/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。

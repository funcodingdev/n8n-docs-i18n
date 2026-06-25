---
title: 什么是 vector database？
description: >-
  理解 vector database。了解 n8n 如何提供 vector database，以及与其配合使用的关键组件，包括 embedding、retriever 和 document loader。
contentType: explanation
nodeTitle: Store and search data with vectors
originalFilePath: advanced-ai/examples/understand-vector-databases.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/understand-vector-databases'
url: >-
  https://docs.n8n.io/build/integrate-ai/understand-ai-components/store-and-search-data-with-vectors
layout:
  description:
    visible: false
---

# 什么是 vector database？ <a href="#what-are-vector-databases" id="what-are-vector-databases"></a>

Vector database 会将信息存储为数字：

> Vector database 是一种将数据存储为高维 vector 的数据库，这些 vector 是特征或属性的数学表示。（[来源](https://learn.microsoft.com/en-us/semantic-kernel/memories/vector-db)）

这可以实现快速且准确的相似性搜索。使用 vector database 时，你不必使用传统数据库 query，而是可以基于语义和上下文含义搜索相关数据。

## 一个简化示例 <a href="#a-simplified-example" id="a-simplified-example"></a>

Vector database 可以存储句子 "n8n is a source-available automation tool that you can self-host"，但它不是将其作为文本存储，而是存储一个表示其特征的维度数组（0 到 1 之间的数字）。这并不意味着把句子中的每个字母转换为数字。相反，vector database 中的 vector 会描述这个句子。

假设在一个 vector store 中，`0.1` 表示 `automation tool`，`0.2` 表示 `source available`，`0.3` 表示 `can be self-hosted`。你可能得到以下 vector：

| 句子 | Vector（维度数组） |
| -------- | ------ |
| n8n is a source-available automation tool that you can self-host | [0.1, 0.2, 0.3] |
| Zapier is an automation tool | [0.1] |
| Make is an automation tool | [0.1] |
| Confluence is a wiki tool that you can self-host | [0.3] |

{% hint style="info" %}
**这个示例非常简化**

实践中，vector 要复杂得多。一个 vector 的维度数量可以从几十到几千不等。维度与单一特征之间并不是一对一关系，因此不能把单个维度直接翻译为单个概念。这个示例提供的是近似的心智模型，而不是真正的技术理解。
{% endhint %}


## 展示相似性搜索的能力 <a href="#demonstrating-the-power-of-similarity-search" id="demonstrating-the-power-of-similarity-search"></a>

Qdrant 提供 [vector search demo](https://qdrant.tech/demo/)，帮助用户理解 vector database 的能力。[food discovery demo](https://food-discovery.qdrant.tech/) 展示了 vector store 如何基于视觉相似性匹配图片。

> 此 demo 使用 Delivery Service 的数据。用户可以喜欢或不喜欢某道菜的照片，app 会基于外观推荐更相似的餐食。也可以选择查看配送范围内餐厅的结果。（[来源](https://qdrant.tech/demo/)）

完整技术细节请参阅 [Qdrant demo-food-discovery GitHub repository](https://github.com/qdrant/demo-food-discovery)。

## Embedding、retriever、text splitter 和 document loader <a href="#embeddings-retrievers-text-splitters-and-document-loaders" id="embeddings-retrievers-text-splitters-and-document-loaders"></a>

Vector database 需要其他 tool 才能工作：

- Document loader 和 text splitter：document loader 会拉取 document 和数据，并准备将它们用于 embedding[^1]。Document loader 可以使用 text splitter 将 document 拆分为 chunk。
- Embedding：这些 tool 会将数据（文本、图片等）转换为 vector，并从 vector 转回原始数据。请注意，n8n 仅支持 text embedding。
- Retriever：retriever 从 vector database 获取 document。你需要将它们与 embedding 配对，才能把 vector 转回数据。

[^1]: Embedding 是使用 vector 表示数据的数值形式。AI 通过在多个维度上映射值来解释复杂数据和关系。Vector database 或 vector store 是专为存储和访问 embedding 设计的数据库。

---
title: MongoDB Atlas Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: MongoDB Atlas Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoremongodbatlas
description: >-
  了解如何在 n8n 中使用 MongoDB Atlas Vector Store node。按照技术文档将
  MongoDB Atlas Vector Store node 集成到你的 workflow 中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# MongoDB Atlas Vector Store

MongoDB Atlas Vector Search 是 MongoDB Atlas 的一项功能，允许用户存储和查询 vector embeddings。使用此 node 与 MongoDB Atlas collections 中的 Vector Search indexes 交互。你可以插入 documents、检索 documents，并在 chains 中使用 vector store，或将其作为 agents 的 tool。

在本页中，你可以找到 MongoDB Atlas Vector Store node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/mongodb.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此 node 之前，请在你的 MongoDB Atlas collection 中创建 [Vector Search index](https://www.mongodb.com/docs/atlas/atlas-vector-search/vector-search-type/)。按以下步骤创建：

1. 登录 [MongoDB Atlas dashboard](https://cloud.mongodb.com/)。
2. 选择你的 organization 和 project。
3. 找到 "Search & Vector Search" 部分。
4. 选择你的 cluster 并点击 "Go to search"。
5. 点击 "Create Search Index"。
6. 选择 "Vector Search" 模式，并使用 visual 或 JSON editors。例如：

    ```json
    {
      "fields": [
        {
          "type": "vector",
          "path": "<field-name>",
          "numDimensions": 1536, // any other value
          "similarity": "<similarity-function>"
        }
      ]
    }
    ```
7. 根据你的 embedding model 调整 "dimensions" 值（例如，OpenAI 的 `text-embedding-small-3` 使用 `1536`）。
8. 命名你的 index 并创建。

请务必记录以下值，它们在配置 node 时必需：

* Collection name
* Vector index name
* Field names for embeddings and metadata

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 MongoDB Atlas Vector Store node：

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 MongoDB Atlas Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 MongoDB Atlas Vector Store 放在普通连接流程中，不使用 agent。

你可以在[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)的场景 1 中看到示例（该模板使用 Supabase Vector Store，但模式相同）。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 MongoDB Atlas Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> MongoDB Atlas Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 MongoDB Atlas Vector Store node 一起使用，从 MongoDB Atlas Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)（链接示例使用 Pinecone，但模式相同）如下：Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> MongoDB Atlas Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 MongoDB Atlas Vector Store node 回答问题。此模式不是将 MongoDB Atlas Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

在这种情况下，[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)（链接示例使用 In-Memory Vector Store，但模式相同）如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> In-Memory Vector store。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/eiIkcF23uZ2A8BkFVQM5/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Mongo Collection**：输入要使用的 MongoDB collection 名称。
* **Vector Index Name**：输入 MongoDB Atlas collection 中 Vector Search index 的名称。
* **Embedding Field**：输入 documents 中包含 vector embeddings 的字段名称。
* **Metadata Field**：输入 documents 中包含文本 metadata 的字段名称。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Mongo Collection**：输入要使用的 MongoDB collection 名称。
* **Vector Index Name**：输入 MongoDB Atlas collection 中 Vector Search index 的名称。
* **Embedding Field**：输入 documents 中包含 vector embeddings 的字段名称。
* **Metadata Field**：输入 documents 中包含文本 metadata 的字段名称。

### Retrieve Documents 参数（As Vector Store for Chain/Tool） <a href="#retrieve-documents-parameters-as-vector-store-for-chaintool" id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Mongo Collection**：输入要使用的 MongoDB collection 名称。
* **Vector Index Name**：输入 MongoDB Atlas collection 中 Vector Search index 的名称。
* **Embedding Field**：输入 documents 中包含 vector embeddings 的字段名称。
* **Metadata Field**：输入 documents 中包含文本 metadata 的字段名称。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Mongo Collection**：输入要使用的 MongoDB collection 名称。
* **Vector Index Name**：输入 MongoDB Atlas collection 中 Vector Search index 的名称。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Options <a href="#options" id="options"></a>

* **Metadata Filter**：根据 metadata 过滤结果。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MongoDB Atlas Vector Store node 文档集成模板](https://n8n.io/integrations/mongodb-atlas-vector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

请参阅：

* [LangChain 的 MongoDB Atlas Vector Search 文档](https://js.langchain.com/docs/integrations/vectorstores/mongodb_atlas)，了解该服务的更多信息。
* [MongoDB Atlas Vector Search 文档](https://www.mongodb.com/docs/atlas/atlas-vector-search/)，了解 MongoDB Atlas Vector Search 的更多信息。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/dN5Se1JVH7wYGtmN4n0v/" %}

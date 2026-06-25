---
title: Chroma Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Chroma Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorechroma
description: >-
  了解如何在 n8n 中使用 Chroma Vector Store node。按照技术文档将 Chroma Vector
  Store node 集成到你的 workflow 中。
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

# Chroma Vector Store

使用 Chroma node 将你的 Chroma 数据库作为 [vector store](#user-content-fn-1)[^1] 进行交互。你可以将 documents 插入 vector database、从 vector database 获取 documents、检索 documents 并提供给连接到 chain[^2] 的 retriever，或作为 tool[^4] 直接连接到 agent[^3]。

在本页中，你可以找到 Chroma node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/chroma.md)找到此 node 的身份验证信息。
{% endhint %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 Chroma Vector Store node。

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 Chroma Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 Chroma Vector Store 放在普通连接流程中，不使用 agent。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 Chroma Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> Chroma Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 Chroma Vector Store node 一起使用，从 Chroma Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

连接流程示例如下：

Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> Chroma Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 Chroma Vector Store node 回答问题。此模式不是将 Chroma Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

在这种情况下，连接流程如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> Chroma Vector store。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Operation Mode <a href="#operation-mode" id="operation-mode"></a>

此 Vector Store node 有四种模式：**Get Many**、**Insert Documents**、**Retrieve Documents (As Vector Store for Chain/Tool)** 和 **Retrieve Documents (As Tool for AI Agent)**。你选择的模式会决定 node 可执行的操作，以及可用的输入和输出。

#### Get Many <a href="#get-many" id="get-many"></a>

在此模式下，你可以通过提供 prompt 从 vector database 检索多个 documents。prompt 会被嵌入并用于相似度搜索。node 会返回与 prompt 最相似的 documents 及其相似度分数。如果你想检索相似 documents 列表，并将其作为额外上下文传递给 agent，此模式很有用。

#### Insert Documents <a href="#insert-documents" id="insert-documents"></a>

使用 Insert Documents 模式将新 documents 插入 vector database。

#### Retrieve Documents (as Vector Store for Chain/Tool) <a href="#retrieve-documents-as-vector-store-for-chaintool" id="retrieve-documents-as-vector-store-for-chaintool"></a>

将 Retrieve Documents (As Vector Store for Chain/Tool) 模式与 vector-store retriever 一起使用，从 vector database 检索 documents，并将其提供给连接到 chain 的 retriever。在此模式下，你必须将 node 连接到 retriever node 或 root node。

#### Retrieve Documents (as Tool for AI Agent) <a href="#retrieve-documents-as-tool-for-ai-agent" id="retrieve-documents-as-tool-for-ai-agent"></a>

使用 Retrieve Documents (As Tool for AI Agent) 模式，在回答查询时将 vector store 用作 tool 资源。生成响应时，如果 vector store 的名称和描述与问题详情匹配，agent 会使用该 vector store。

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

启用 reranking[^5]。如果启用此选项，你必须将 reranking node 连接到 vector store。该 node 随后会对查询结果重新排序。你可以将此选项与 `Get Many`、`Retrieve Documents (As Vector Store for Chain/Tool)` 和 `Retrieve Documents (As Tool for AI Agent)` 模式一起使用。

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Chroma collection name**：从已获取的 collections 列表中选择你的 collection。
* **Prompt**：输入搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `5` 可获取最匹配的五个结果。

此 Operation Mode 包含一个 **Node option**：Metadata Filter。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Chroma collection name**：从已获取的 collections 列表中选择你的 collection。

### Retrieve Documents (As Vector Store for Chain/Tool) 参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Chroma collection name**：从已获取的 collections 列表中选择你的 collection。

此 Operation Mode 包含一个 **Node option**：Metadata Filter。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Chroma collection name**：从已获取的 collections 列表中选择你的 collection。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `5` 可获取最匹配的五个结果。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Metadata Filter <a href="#metadata-filter" id="metadata-filter"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/9OWZ8hSpVqky4D4xRnYP/" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Chroma 文档](https://js.langchain.com/oss/javascript/integrations/vectorstores/chroma)。

查看 n8n 的 [Advanced AI](../../../../../advanced-ai/index.md) 文档。

[^1]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。
[^2]: AI chains 允许你通过一系列组件调用与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久 memory，因此不能用它们引用之前的上下文（请为此使用 AI agents）。
[^3]: AI agents 是能够响应请求、做出决策并为用户执行现实世界任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^4]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。
[^5]: Reranking 是一种用于优化候选 document 列表排序的技术，可提高搜索结果的相关性。Retrieval-Augmented Generation（RAG）和其他应用会使用 reranking 优先选择对生成或下游任务最相关的信息。

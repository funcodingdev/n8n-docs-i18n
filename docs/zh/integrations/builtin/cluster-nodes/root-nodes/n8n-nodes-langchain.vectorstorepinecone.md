---
title: Pinecone Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Pinecone Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone
description: >-
  了解如何在 n8n 中使用 Pinecone Vector Store node。按照技术文档将 Pinecone
  Vector Store node 集成到你的 workflow 中。
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

# Pinecone Vector Store

使用 Pinecone node 将你的 Pinecone 数据库作为 [vector store](#user-content-fn-1)[^1] 进行交互。你可以将 documents 插入 vector database、从 vector database 获取 documents、检索 documents 并提供给连接到 chain[^2] 的 retriever，或作为 tool[^4] 直接连接到 agent[^3]。你也可以通过 ID 更新 vector database 中的 item。

在本页中，你可以找到 Pinecone node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/pinecone.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 Pinecone Vector Store node。

### 作为普通 node 插入、更新和检索 documents <a href="#use-as-a-regular-node-to-insert-update-and-retrieve-documents" id="use-as-a-regular-node-to-insert-update-and-retrieve-documents"></a>

你可以将 Pinecone Vector Store 作为普通 node 使用，用于插入、更新或获取 documents。此模式会将 Pinecone Vector Store 放在普通连接流程中，不使用 agent。

你可以在[此模板](https://n8n.io/workflows/2165-chat-with-pdf-docs-using-ai-quoting-sources/)的场景 1 中看到示例。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 Pinecone Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> Pinecone Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 Pinecone Vector Store node 一起使用，从 Pinecone Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)如下：Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> Pinecone Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 Pinecone Vector Store node 回答问题。此模式不是将 Pinecone Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

在这种情况下，[连接流程](https://n8n.io/workflows/2705-chat-with-github-api-documentation-rag-powered-chatbot-with-pinecone-and-openai/)如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> Pinecone Vector store。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Operation Mode <a href="#operation-mode" id="operation-mode"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/5aeZAt5P1m2YndTmiFTG/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Pinecone Index**：选择或输入要使用的 Pinecone Index。
* **Prompt**：输入你的搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Pinecone Index**：选择或输入要使用的 Pinecone Index。

### Retrieve Documents (As Vector Store for Chain/Tool) 参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Pinecone Index**：选择或输入要使用的 Pinecone Index。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Pinecone Index**：选择或输入要使用的 Pinecone Index。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### **Update Documents** 参数 <a href="#parameters-for-update-documents" id="parameters-for-update-documents"></a>

* ID

## Node 选项 <a href="#node-options" id="node-options"></a>

### Pinecone Namespace <a href="#pinecone-namespace" id="pinecone-namespace"></a>

用于在 index 中存储数据的另一种隔离选项。

### Metadata Filter <a href="#metadata-filter" id="metadata-filter"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/9OWZ8hSpVqky4D4xRnYP/" %}

### Clear Namespace <a href="#clear-namespace" id="clear-namespace"></a>

在 **Insert Documents** 模式中可用。在插入新数据之前删除 namespace 中的所有数据。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Pinecone Vector Store node 文档集成模板](https://n8n.io/integrations/pinecone-vector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Pinecone 文档](https://js.langchain.com/docs/integrations/vectorstores/pinecone/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

### 查找你的 Pinecone index 和 namespace <a href="#find-your-pinecone-index-and-namespace" id="find-your-pinecone-index-and-namespace"></a>

你的 Pinecone index 和 namespace 可在 Pinecone 账户中找到。

![Screenshot of a Pinecone account, with the Pinecone index labelled](../../../.gitbook/assets/pinecone-index-namespace.png)

[^1]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。
[^2]: AI chains 允许你通过一系列组件调用与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久 memory，因此不能用它们引用之前的上下文（请为此使用 AI agents）。
[^3]: AI agents 是能够响应请求、做出决策并为用户执行现实世界任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^4]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

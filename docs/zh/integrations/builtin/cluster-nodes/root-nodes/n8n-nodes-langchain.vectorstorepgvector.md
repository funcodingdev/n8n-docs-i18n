---
title: PGVector Vector Store node 文档
priority: medium
nodeTitle: PGVector Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepgvector
description: >-
  了解如何在 n8n 中使用 PGVector Vector Store node。按照技术文档将 PGVector
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

# PGVector Vector Store

PGVector 是 Postgresql 的一个扩展。使用此 node 与 Postgresql 数据库中的 PGVector tables 交互。你可以将 documents 插入 vector table、从 vector table 获取 documents、检索 documents 并提供给连接到 chain[^1] 的 retriever，或作为 tool[^3] 直接连接到 agent[^2]。

在本页中，你可以找到 PGVector node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/postgres.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 PGVector Vector Store node。

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 PGVector Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 PGVector Vector Store 放在普通连接流程中，不使用 agent。

你可以在[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)的场景 1 中看到示例（该模板使用 Supabase Vector Store，但模式相同）。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 PGVector Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> PGVector Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 PGVector Vector Store node 一起使用，从 PGVector Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)（链接示例使用 Pinecone，但模式相同）如下：Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> PGVector Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 PGVector Vector Store node 回答问题。此模式不是将 PGVector Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

在这种情况下，[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)（链接示例使用 Simple Vector Store，但模式相同）如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> Simple Vector store。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/eiIkcF23uZ2A8BkFVQM5/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Table name**：输入要查询的表名称。
* **Prompt**：输入你的搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Table name**：输入要查询的表名称。

### Retrieve Documents 参数（As Vector Store for Chain/Tool） <a href="#retrieve-documents-parameters-as-vector-store-for-chaintool" id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Table name**：输入要查询的表名称。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Table Name**：输入要使用的 PGVector table。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Collection <a href="#collection" id="collection"></a>

这是一种在 PGVector 中分隔 datasets 的方式。它会创建独立的表和列，用于跟踪 vector 属于哪个 collection。

* **Use Collection**：选择是否使用 collection（开启或关闭）。
* **Collection Name**：输入你想使用的 collection 名称。
* **Collection Table Name**：输入用于存储 collection 信息的表名称。

### Column Names <a href="#column-names" id="column-names"></a>

以下选项指定用于存储 vectors 和相应信息的列名：

* **ID Column Name**
* **Vector Column Name**
* **Content Column Name**
* **Metadata Column Name**

### Metadata Filter <a href="#metadata-filter" id="metadata-filter"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/9OWZ8hSpVqky4D4xRnYP/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 PGVector Vector Store node 文档集成模板](https://n8n.io/integrations/postgres-pgvector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 PGVector 文档](https://js.langchain.com/docs/integrations/vectorstores/pgvector)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/dN5Se1JVH7wYGtmN4n0v/" %}

[^1]: AI chains 允许你通过一系列组件调用与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久 memory，因此不能用它们引用之前的上下文（请为此使用 AI agents）。
[^2]: AI agents 是能够响应请求、做出决策并为用户执行现实世界任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^3]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

---
title: Redis Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Redis Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreredis
description: >-
  了解如何在 n8n 中使用 Redis Vector Store node。按照技术文档将 Redis Vector
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

# Redis Vector Store

使用 Redis Vector Store node 将你的 Redis 数据库作为 [vector store](#user-content-fn-1)[^1] 进行交互。你可以将 documents 插入 vector database、从 vector database 获取 documents、使用连接到 chain[^2] 的 retriever 检索 documents，或直接连接到 agent[^3] 并作为 tool[^4] 使用。

在本页中，你可以找到 Redis Vector Store node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/redis.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此 node 之前，你需要一个启用了 [Redis Query Engine](https://redis.io/docs/latest/develop/ai/search-and-query/?utm_source=n8n\&utm_medium=docs) 的 Redis 数据库。使用以下之一：

* **Redis Open Source（v8.0 及更高版本）**：默认包含 Redis Query Engine
* [**Redis Cloud**](https://cloud.redis.io/?utm_source=n8n\&utm_medium=docs)：全托管服务
* [**Redis Software**](https://redis.io/software/?utm_source=n8n\&utm_medium=docs)：自托管部署

{% hint style="info" %}
**如果你没有 index，将创建一个新 index。**

只有当你想使用自定义 index schema 或复用现有 index 时，才需要提前创建自己的 indices。否则，你可以跳过此步骤，让 node 根据你指定的选项为你创建新 index。
{% endhint %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 Redis Vector Store node：

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 Redis Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 Redis Vector Store 放在普通连接流程中，不使用 agent。

你可以在[此模板](https://n8n.io/workflows/10887-reduce-llm-costs-with-semantic-caching-using-redis-vector-store-and-huggingface/)中看到示例，其中 semantic cache 存储在 Redis 中，并在 workflow 开始时使用 Redis Vector Store node 检索。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 Redis Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool[^4] 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> Redis Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 Redis Vector Store node 一起使用，从 Redis Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)（链接示例使用 Pinecone，但模式相同）如下：Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> Redis Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 Redis Vector Store node 回答问题。此模式不是将 Redis Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

此[模板](https://n8n.io/workflows/10837-chat-with-github-issues-using-openai-and-redis-vector-search/)展示了如何将 Vector Store Question Answer Tool 与 Redis Vector Store node 一起使用。在这种情况下，连接流程如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> Redis Vector store。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/eiIkcF23uZ2A8BkFVQM5/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Redis Index**：输入要使用的 Redis vector search index 名称。也可以从列表中选择现有 index。
* **Prompt**：输入搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

此 Operation Mode 包含一个 **Node option**：[Metadata Filter](n8n-nodes-langchain.vectorstoreredis.md#metadata-filter)。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Redis Index**：输入要使用的 Redis vector search index 名称。也可以从列表中选择现有 index。

### Retrieve Documents (As Vector Store for Chain/Tool) 参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Redis Index**：输入要使用的 Redis vector search index 名称。也可以从列表中选择现有 index。

此 Operation Mode 包含一个 **Node option**：[Metadata Filter](n8n-nodes-langchain.vectorstoreredis.md#metadata-filter)。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Redis Index**：输入要使用的 Redis vector search index 名称。也可以从列表中选择现有 index。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Include Metadata <a href="#include-metadata" id="include-metadata"></a>

是否包含 document metadata。

你可以将此选项与 [Get Many](n8n-nodes-langchain.vectorstoreredis.md#get-many-parameters) 和 [Retrieve Documents (As Tool for AI Agent)](n8n-nodes-langchain.vectorstoreredis.md#retrieve-documents-as-tool-for-ai-agent-parameters) 模式一起使用。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Metadata Filter <a href="#metadata-filter" id="metadata-filter"></a>

Metadata filters 可用于 [Get Many](n8n-nodes-langchain.vectorstoreredis.md#get-many-parameters)、[Retrieve Documents (As Vector Store for Chain/Tool)](n8n-nodes-langchain.vectorstoreredis.md#retrieve-documents-as-vector-store-for-chaintool-parameters) 和 [Retrieve Documents (As Tool for AI Agent)](n8n-nodes-langchain.vectorstoreredis.md#retrieve-documents-as-tool-for-ai-agent-parameters) operation modes。这是一个 `OR` 查询。如果你指定多个 metadata filter 字段，至少其中一个必须匹配。插入数据时，metadata 由 document loader 设置。有关加载 documents 的更多信息，请参阅 [Default Data Loader](../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。

### Redis Configuration Options <a href="#redis-configuration-options" id="redis-configuration-options"></a>

适用于所有 operation modes：

* **Metadata Key**：输入 Redis hash 中 metadata 字段的 key（默认：`metadata`）。
* **Key Prefix**：输入用于存储 documents 的 key prefix（默认：`doc:`）。
* **Content Key**：输入 Redis hash 中 content 字段的 key（默认：`content`）。
* **Embedding Key**：输入 Redis hash 中 embedding 字段的 key（默认：`embedding`）。

### Insert Options <a href="#insert-options" id="insert-options"></a>

适用于 [Insert Documents](n8n-nodes-langchain.vectorstoreredis.md#insert-documents-parameters) operation mode：

* **Overwrite Documents**：选择是否覆盖现有 documents（开启或关闭）。也会删除 index。
* **Time-to-Live**：输入 documents 的存活时间，单位秒。不会使 index 过期。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Redis Vector Store node 文档集成模板](https://n8n.io/integrations/redis-vector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

请参阅：

* [Redis Vector Search 文档](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/)，了解 Redis vector 能力的更多信息。
* [RediSearch 文档](https://redis.io/docs/latest/develop/interact/search-and-query/)，了解 RediSearch 的更多信息。
* [LangChain 的 Redis Vector Store 文档](https://js.langchain.com/docs/integrations/vectorstores/redis)，了解该服务的更多信息。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/dN5Se1JVH7wYGtmN4n0v/" %}

[^1]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。
[^2]: AI chains 允许你通过一系列组件调用与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久 memory，因此不能用它们引用之前的上下文（请为此使用 AI agents）。
[^3]: AI agents 是能够响应请求、做出决策并为用户执行现实世界任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^4]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

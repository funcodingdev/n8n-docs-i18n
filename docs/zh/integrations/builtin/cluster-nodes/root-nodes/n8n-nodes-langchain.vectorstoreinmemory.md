---
title: Simple Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Simple Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory
description: >-
  了解如何在 n8n 中使用 Simple Vector Store node。按照技术文档将 Simple Vector
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

# Simple Vector Store

使用 Simple Vector Store node 在 n8n 的 app 内 memory 中存储和检索 embeddings[^1]。

在本页中，你可以找到 Simple Vector Store node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

{% hint style="info" %}
**此 node 不同于 AI memory nodes**

这里描述的 simple vector storage 不同于 [Simple Memory](../sub-nodes/n8n-nodes-langchain.memorybufferwindow/) 等 AI memory nodes。

此 node 会在 app memory 中创建一个 [vector database](#user-content-fn-2)[^2]。
{% endhint %}

## 数据安全限制 <a href="#data-safety-limitations" id="data-safety-limitations"></a>

使用 Simple Vector Store node 之前，务必了解它的限制和工作方式。

{% hint style="warning" %}
n8n 建议仅将 Simple Vector store 用于开发用途。
{% endhint %}

### Vector store 数据不是持久的 <a href="#vector-store-data-isnt-persistent" id="vector-store-data-isnt-persistent"></a>

此 node 仅在 memory 中存储数据。n8n 重启时，所有数据都会丢失；在低 memory 条件下，数据也可能被清除。

### 所有实例用户都可以访问 vector store 数据 <a href="#all-instance-users-can-access-vector-store-data" id="all-instance-users-can-access-vector-store-data"></a>

Simple Vector Store node 的 memory keys 是全局的，不限定到单个 workflow。

这意味着，该实例的所有用户都可以通过添加 Simple Vector Store node 并选择 memory key 来访问 vector store 数据，无论原始 workflow 设置了什么访问控制。使用 Simple Vector Store node 摄取数据时，请注意不要暴露敏感信息。

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 Simple Vector Store node。

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 Simple Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 Simple Vector Store 放在普通连接流程中，不使用 agent。

你可以在[此模板](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)的第 2 步中看到示例。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 Simple Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool[^3] 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> Simple Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 Simple Vector Store node 一起使用，从 Simple Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

[连接流程示例](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)（链接示例使用 Pinecone，但模式相同）如下：Question and Answer Chain（Retriever connector）-> Vector Store Retriever（Vector Store connector）-> Simple Vector Store。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 Simple Vector Store node 回答问题。此模式不是将 Simple Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

在这种情况下，[连接流程](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)如下：AI agent（tools connector）-> Vector Store Question Answer Tool（Vector Store connector）-> Simple Vector store。

## Memory 管理 <a href="#memory-management" id="memory-management"></a>

Simple Vector Store 实现了 memory management，以防止过量 memory 使用：

* 当 memory 压力增加时，自动清理旧 vector stores
* 移除在可配置时长内未被访问的 inactive stores

### 配置选项 <a href="#configuration-options" id="configuration-options"></a>

你可以使用以下环境变量控制 memory 使用：

| Variable | Type | Default | Description |
| --- | --- | --- | --- |
| `N8N_VECTOR_STORE_MAX_MEMORY` | Number | -1 | 所有 vector stores 合计允许使用的最大 memory，单位 MB（-1 表示禁用限制）。 |
| `N8N_VECTOR_STORE_TTL_HOURS` | Number | -1 | store 在不活跃多少小时后被移除（-1 表示禁用 TTL）。 |

在 n8n Cloud 上，这些值分别预设为 100MB（约 8,000 个 documents，取决于 document 大小和 metadata）和 7 天。对于 self-hosted 实例，这两个值默认都是 -1（无 memory 限制或基于时间的清理）。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/eiIkcF23uZ2A8BkFVQM5/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Memory Key**：选择或创建包含你想查询的 vector memory 的 key。
* **Prompt**：输入搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Memory Key**：选择或创建你想用于存储 vector memory 的 key。
* **Clear Store**：使用此参数控制在插入数据之前，是否为此 workflow 清空给定 memory key 的 vector store（开启）。

### Retrieve Documents (As Vector Store for Chain/Tool) 参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Memory Key**：选择或创建包含你想查询的 vector memory 的 key。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Memory Key**：选择或创建包含你想查询的 vector memory 的 key。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Simple Vector Store node 文档集成模板](https://n8n.io/integrations/in-memory-vector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChains 的 Memory Vector Store 文档](https://js.langchain.com/docs/integrations/vectorstores/memory/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Embeddings 是使用 vectors 表示数据的数值表示。AI 使用它们通过在多个维度上映射值来解释复杂数据和关系。Vector databases 或 vector stores 是专为存储和访问 embeddings 而设计的数据库。
[^2]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。
[^3]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

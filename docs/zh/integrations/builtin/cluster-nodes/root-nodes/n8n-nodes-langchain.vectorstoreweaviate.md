---
title: Weaviate Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Weaviate Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate
description: >-
  了解如何在 n8n 中使用 Weaviate Vector Store node。按照技术文档将 Weaviate
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

# Weaviate Vector Store

使用 Weaviate node 将你的 Weaviate collection 作为 [vector store](#user-content-fn-1)[^1] 进行交互。你可以将 documents 插入 vector database，或从 vector database 检索 documents。你也可以检索 documents 并提供给连接到 chain[^2] 的 retriever，或将此 node 直接连接到 agent[^3] 并作为 tool[^4] 使用。在本页中，你可以找到 Weaviate node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/weaviate.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

你可以按以下模式使用 Weaviate Vector Store node。

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

你可以将 Weaviate Vector Store 作为普通 node 使用，用于插入或获取 documents。此模式会将 Weaviate Vector Store 放在普通连接流程中，不使用 agent。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

你可以将 Weaviate Vector Store node 直接连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，以便在回答查询时将 vector store 用作资源。

此处的连接为：AI agent（tools connector）-> Weaviate Vector Store node。

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

你可以将 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) node 与 Weaviate Vector Store node 一起使用，从 Weaviate Vector Store node 获取 documents。这通常与 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) node 一起使用，用于从 vector store 获取与给定 chat input 匹配的 documents。

### 使用 Vector Store Question Answer Tool 回答问题 <a href="#use-the-vector-store-question-answer-tool-to-answer-questions" id="use-the-vector-store-question-answer-tool-to-answer-questions"></a>

另一种模式使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总结果，并基于 Weaviate Vector Store node 回答问题。此模式不是将 Weaviate Vector Store 直接作为 tool 连接，而是使用专为汇总 vector store 中数据而设计的 tool。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% hint style="info" %}
**Multitenancy**

你可以将同一 collection 中的数据拆分到相互隔离的 tenants（例如不同客户）。为此，插入和检索 objects 时都必须始终提供 [Tenant Name](n8n-nodes-langchain.vectorstoreweaviate.md#tenant-name)。请在 [Weaviate 文档中阅读更多关于 multi tenancy 的内容](https://docs.weaviate.io/weaviate/manage-collections/multi-tenancy)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/eiIkcF23uZ2A8BkFVQM5/" %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Weaviate Collection**：输入要使用的 Weaviate collection 名称。
* **Prompt**：输入搜索查询。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Weaviate Collection**：输入要使用的 Weaviate collection 名称。
* **Embedding Batch Size**：单个 batch 中要 embed 的 documents 数量。默认值为 200 个 documents。

### Retrieve Documents (As Vector Store for Chain/Tool) 参数 <a href="#retrieve-documents-as-vector-store-for-chaintool-parameters" id="retrieve-documents-as-vector-store-for-chaintool-parameters"></a>

* **Weaviate Collection**：输入要使用的 Weaviate collection 名称。

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Weaviate Collection**：vector store 的名称。
* **Description**：向 LLM 说明此 tool 的作用。良好且具体的描述可以让 LLM 更经常生成预期结果。
* **Weaviate Collection**：输入要使用的 Weaviate collection 名称。
* **Limit**：输入要从 vector store 检索多少个结果。例如，将其设置为 `10` 可获取最匹配的十个结果。

### Include Metadata <a href="#include-metadata" id="include-metadata"></a>

是否包含 document metadata。

你可以将此选项与 [Get Many](n8n-nodes-langchain.vectorstoreweaviate.md#get-many) 和 [Retrieve Documents (As Tool for AI Agent)](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent-parameters) 模式一起使用。

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

### Search Filters <a href="#search-filters" id="search-filters"></a>

适用于 [Get Many](n8n-nodes-langchain.vectorstoreweaviate.md#get-many)、[Retrieve Documents (As Vector Store for Chain/Tool)](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-vector-store-for-chaintool) 和 [Retrieve Documents (As Tool for AI Agent)](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent) operation modes。

搜索数据时，使用此选项匹配与 documents 关联的 metadata。你可以在 [Weaviate 的 conditional filters 文档](https://docs.weaviate.io/weaviate/api/graphql/filters)中了解更多 operators 和 query structure。

你可以将 `AND` 和 `OR` 与不同 operators 一起使用。Operators 不区分大小写：

```json
{
  "OR": [
    {
        "path": ["source"],
        "operator": "Equal",
        "valueString": "source1"
    },
    {
        "path": ["source"],
        "operator": "Equal",
        "valueString": "source1"
    }
  ]
}
```

支持的 operators：

| Operator | Required Field(s) | Description |
| --- | --- | --- |
| `'equal'` | `valueString` 或 `valueNumber` | 检查 property 是否等于给定字符串或数字。 |
| `'like'` | `valueString` | 检查 string property 是否匹配某个 pattern（例如 substring match）。 |
| `'containsAny'` | `valueTextArray` (string\[]) | 检查 property 是否包含给定值中的**任意**一个。 |
| `'containsAll'` | `valueTextArray` (string\[]) | 检查 property 是否包含给定值中的**全部**。 |
| `'greaterThan'` | `valueNumber` | 检查 property value 是否大于给定数字。 |
| `'lessThan'` | `valueNumber` | 检查 property value 是否小于给定数字。 |
| `'isNull'` | `valueBoolean` (true/false) | 检查 property 是否为 null。([必须在 ingestion 前启用](https://docs.weaviate.io/weaviate/manage-collections/collection-operations#set-inverted-index-parameters)) |
| `'withinGeoRange'` | `valueGeoCoordinates`（包含 geolocation data 的 object） | 按与地理坐标的距离过滤。 |

插入数据时，document loader 会设置 metadata。有关加载 documents 的更多信息，请参阅 [Default Data Loader](../sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md)。

### Metadata Keys <a href="#metadata-keys" id="metadata-keys"></a>

你可以定义希望 Weaviate 在查询中返回哪些 metadata keys。这可以减少网络负载，因为你只会获取已定义的 properties。默认情况下会返回 server 中的所有 properties。

适用于 [Get Many](n8n-nodes-langchain.vectorstoreweaviate.md#get-many)、[Retrieve Documents (As Vector Store for Chain/Tool)](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-vector-store-for-chaintool) 和 [Retrieve Documents (As Tool for AI Agent)](n8n-nodes-langchain.vectorstoreweaviate.md#retrieve-documents-as-tool-for-ai-agent) operation modes。

### Hybrid: Query Text <a href="#hybrid-query-text" id="hybrid-query-text"></a>

提供 query text，用于将 vector search 与 keyword/text search 结合。

### Hybrid: Explain Score <a href="#hybrid-explain-score" id="hybrid-explain-score"></a>

是否显示 hybrid 和 vector search 说明之间融合后的 score。

### Hybrid: Fusion Type <a href="#hybrid-fusion-type" id="hybrid-fusion-type"></a>

选择用于结合 vector 和 keyword search 结果的 fusion type。[了解更多 fusion algorithms](https://weaviate.io/learn/knowledgecards/fusion-algorithm)。

选项：

* **Relative Score**：使用 relative score fusion
* **Ranked**：使用 ranked fusion

### Hybrid: Auto Cut Limit <a href="#hybrid-auto-cut-limit" id="hybrid-auto-cut-limit"></a>

通过检测 score 的突然跳变来限制结果组。[了解更多 autocut](https://docs.weaviate.io/weaviate/api/graphql/additional-operators#autocut)。

### Hybrid: Alpha <a href="#hybrid-alpha" id="hybrid-alpha"></a>

更改 keyword 和 vector 组件的相对权重。1.0 = 纯 vector，0.0 = 纯 keyword。默认值为 0.5。[了解更多 alpha parameter](https://weaviate.io/learn/knowledgecards/alpha-parameter)。

### Hybrid: Query Properties <a href="#hybrid-query-properties" id="hybrid-query-properties"></a>

输入逗号分隔的 properties 列表，可包含可选权重值，例如 "question^2,answer"。[了解更多如何设置 property values 权重](https://docs.weaviate.io/weaviate/search/hybrid#set-weights-on-property-values)。

### Hybrid: Max Vector Distance <a href="#hybrid-max-vector-distance" id="hybrid-max-vector-distance"></a>

设置 vector search 组件允许的最大距离。

### Tenant Name <a href="#tenant-name" id="tenant-name"></a>

用于存储或检索 documents 的特定 tenant。[了解更多 multi-tenancy](https://weaviate.io/learn/knowledgecards/multi-tenancy)。

{% hint style="info" %}
**必须在创建时启用**

你必须在首次 ingestion 时传入 tenant name，才能为 collection 启用 multitenancy。创建后无法启用或禁用 multitenancy。
{% endhint %}

### Text Key <a href="#text-key" id="text-key"></a>

document 中包含 embedded text 的 key。

### Skip Init Checks <a href="#skip-init-checks" id="skip-init-checks"></a>

实例化 client 时是否[跳过初始化检查](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#initial-connection-checks)。

### Init Timeout <a href="#init-timeout" id="init-timeout"></a>

初始检查期间等待多久后[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)，单位秒。

### Insert Timeout <a href="#insert-timeout" id="insert-timeout"></a>

插入期间等待多久后[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)，单位秒。

### Query Timeout <a href="#query-timeout" id="query-timeout"></a>

查询期间等待多久后[超时](https://docs.weaviate.io/weaviate/client-libraries/typescript/notes-best-practices#timeout-values)，单位秒。

### GRPC Proxy <a href="#grpc-proxy" id="grpc-proxy"></a>

用于 gRPC requests 的 proxy。

### Clear Data <a href="#clear-data" id="clear-data"></a>

适用于 [Insert Documents](n8n-nodes-langchain.vectorstoreweaviate.md#insert-documents) operation mode。

是否在插入新数据之前清空 collection 或 tenant。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Weaviate Vector Store node 文档集成模板](https://n8n.io/integrations/weaviate-vector-store)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Weaviate 文档](https://js.langchain.com/docs/integrations/vectorstores/weaviate/)。

有关 self hosted Weaviate Cluster，请参阅 [Weaviate Installation](https://docs.weaviate.io/deploy)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: vector store 或 vector database 会存储信息的数学表示。它可与 embeddings 和 retrievers 一起使用，创建一个 AI 在回答问题时可以访问的数据库。
[^2]: AI chains 允许你通过一系列组件调用与大型语言模型（LLM）和其他资源交互。n8n 中的 AI chains 不使用持久 memory，因此不能用它们引用之前的上下文（请为此使用 AI agents）。
[^3]: AI agents 是能够响应请求、做出决策并为用户执行现实世界任务的人工智能系统。它们使用大型语言模型（LLM）解释用户输入，并根据可用的信息和资源决定如何最好地处理请求。
[^4]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

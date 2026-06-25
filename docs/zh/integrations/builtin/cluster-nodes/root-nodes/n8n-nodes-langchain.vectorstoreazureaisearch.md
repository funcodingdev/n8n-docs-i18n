---
title: Azure AI Search Vector Store node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Azure AI Search Vector Store node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreazureaisearch
description: >-
  了解如何在 n8n 中使用 Azure AI Search Vector Store node。按照技术文档将 Azure
  AI Search Vector Store node 集成到你的 workflow 中。
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

# Azure AI Search Vector Store

Azure AI Search（以前称为 Azure Cognitive Search）是一项云搜索服务，为 RAG 和语义搜索应用提供 vector search 能力。使用此 node 存储、检索和查询 vector embeddings，以及它们的内容和 metadata。

在本页中，你可以找到 Azure AI Search Vector Store node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/azureaisearch.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

使用此 node 之前，你需要：

1. 一个 [Azure subscription](https://azure.microsoft.com)
2. 一个 [Azure AI Search service](https://learn.microsoft.com/azure/search/search-create-service-portal)
3. 已配置 API key 身份验证（写操作使用 admin key，只读操作使用 query key）

    设置说明请参阅 [credentials 文档](../../credentials/azureaisearch.md)。

### Index 配置 <a href="#index-configuration" id="index-configuration"></a>

如果 index 不存在，node 会自动创建。自动创建时，node 会配置：

* 根据你的 embeddings model 设置合适维度的 vector fields
* 使用 cosine metric 的 HNSW algorithm，用于高效相似度搜索
* 用于过滤和检索的 content 与 metadata fields

你也可以在 Azure Portal 中预先创建自定义配置的 indexes。示例 schema：

```json
{
  "name": "n8n-vectorstore",
  "fields": [
    {
      "name": "id",
      "type": "Edm.String",
      "key": true,
      "filterable": true
    },
    {
      "name": "content",
      "type": "Edm.String",
      "searchable": true
    },
    {
      "name": "content_vector",
      "type": "Collection(Edm.Single)",
      "searchable": true,
      "vectorSearchDimensions": 1536,
      "vectorSearchProfileName": "n8n-vector-profile"
    },
    {
      "name": "metadata",
      "type": "Edm.String",
      "filterable": true
    }
  ],
  "vectorSearch": {
    "profiles": [
      {
        "name": "n8n-vector-profile",
        "algorithm": "n8n-vector-algorithm"
      }
    ],
    "algorithms": [
      {
        "name": "n8n-vector-algorithm",
        "kind": "hnsw",
        "hnswParameters": {
          "metric": "cosine",
          "m": 4,
          "efConstruction": 400,
          "efSearch": 500
        }
      }
    ]
  }
}
```

{% hint style="info" %}
**Vector dimensions**

`vectorSearchDimensions` 值必须与你的 embeddings model 输出匹配。
{% endhint %}

## Node 使用模式 <a href="#node-usage-patterns" id="node-usage-patterns"></a>

### 作为普通 node 插入和检索 documents <a href="#use-as-a-regular-node-to-insert-and-retrieve-documents" id="use-as-a-regular-node-to-insert-and-retrieve-documents"></a>

直接在 workflow 中使用此 node 插入或检索 documents，而不使用 agent。请参阅[此模板](https://n8n.io/workflows/2621-ai-agent-to-chat-with-files-in-supabase-storage/)中的示例模式（使用 Supabase，但模式相同）。

### 作为 tool 直接连接到 AI agent <a href="#connect-directly-to-an-ai-agent-as-a-tool" id="connect-directly-to-an-ai-agent-as-a-tool"></a>

连接到 [AI agent](n8n-nodes-langchain.agent/) 的 tool 连接器，将 vector store 用作可搜索知识库：

AI agent（tools connector）-> Azure AI Search Vector Store node

### 使用 retriever 获取 documents <a href="#use-a-retriever-to-fetch-documents" id="use-a-retriever-to-fetch-documents"></a>

与 [Vector Store Retriever](../sub-nodes/n8n-nodes-langchain.retrievervectorstore.md) 和 [Question and Answer Chain](n8n-nodes-langchain.chainretrievalqa/) 一起使用，用于 retrieval-augmented generation：

Question and Answer Chain（Retriever）-> Vector Store Retriever（Vector Store）-> Azure AI Search Vector Store

请参阅[此示例 workflow](https://n8n.io/workflows/1960-ask-questions-about-a-pdf-using-ai/)。

### 使用 Vector Store Question Answer Tool <a href="#use-the-vector-store-question-answer-tool" id="use-the-vector-store-question-answer-tool"></a>

使用 [Vector Store Question Answer Tool](../sub-nodes/n8n-nodes-langchain.toolvectorstore.md) 汇总并回答问题：

AI agent（tools）-> Vector Store Question Answer Tool（Vector Store）-> Azure AI Search Vector Store

请参阅[此示例](https://n8n.io/workflows/2465-building-your-first-whatsapp-chatbot/)。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/5aeZAt5P1m2YndTmiFTG/" %}

### Rerank Results <a href="#rerank-results" id="rerank-results"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/KcxcfJWhy81cjCSzO4vQ/" %}

{% hint style="info" %}
**Azure AI Search semantic reranking**

当你在具有 semantic configuration 的情况下使用 **Semantic Hybrid** query mode 时，Azure AI Search 提供内置 [semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview)。要使用它：

1. 在 Options 中将 **Query Mode** 设置为 **Semantic Hybrid**
2. 将 **Semantic Configuration** 设置为你的 configuration name（未指定时默认为 `semantic-search-config`）

内置 semantic reranker 使用 machine learning models 改进相关性。你可以在 semantic reranking 之后串接额外的 reranking node，以进一步优化。

只有当你的 index 定义了 semantic configuration 时，[Semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 才可用。
{% endhint %}

### Get Many 参数 <a href="#get-many-parameters" id="get-many-parameters"></a>

* **Endpoint**：你的 Azure AI Search endpoint（格式：`https://your-service.search.windows.net`）
* **Index Name**：要查询的 index
* **Limit**：要返回的最大 documents 数量（默认：4）

### Insert Documents 参数 <a href="#insert-documents-parameters" id="insert-documents-parameters"></a>

* **Endpoint**：你的 Azure AI Search endpoint
* **Index Name**：要使用的 index（如果不存在会自动创建）
* **Batch Size**：每批上传到 Azure AI Search 的 documents 数量。请根据 document 大小和你的 service tier 限制进行调整。此项只控制 upload batching，embedding generation batching 在 embedding nodes 中配置。

### Update Documents 参数 <a href="#update-documents-parameters" id="update-documents-parameters"></a>

* **Endpoint**：你的 Azure AI Search endpoint
* **Index Name**：要更新的 index

### Retrieve Documents 参数（As Vector Store for Chain/Tool） <a href="#retrieve-documents-parameters-as-vector-store-for-chaintool" id="retrieve-documents-parameters-as-vector-store-for-chaintool"></a>

* **Endpoint**：你的 Azure AI Search endpoint
* **Index Name**：要查询的 index

### Retrieve Documents (As Tool for AI Agent) 参数 <a href="#retrieve-documents-as-tool-for-ai-agent-parameters" id="retrieve-documents-as-tool-for-ai-agent-parameters"></a>

* **Name**：显示给 LLM 的 tool 名称
* **Description**：向 LLM 说明此 tool 的作用。请写得具体，以帮助 LLM 判断何时使用此 tool。
* **Endpoint**：你的 Azure AI Search endpoint
* **Index Name**：要查询的 index
* **Limit**：要检索的最大结果数（例如 `10` 表示十个最佳匹配）

## Node 选项 <a href="#node-options" id="node-options"></a>

### Options <a href="#options" id="options"></a>

* **Filter**：[OData filter expression](https://learn.microsoft.com/azure/search/search-query-odata-filter)，用于按 document fields 或 metadata 过滤结果。请参阅下面的 filter 示例。
* **Query Mode**：要使用的搜索策略：
  * **Vector**：仅使用 embeddings 进行相似度搜索
  * **Keyword**：使用 BM25 ranking 进行全文搜索
  * **Hybrid**（默认）：结合 vector 和 keyword search，并使用 Reciprocal Rank Fusion（RRF）
  * **Semantic Hybrid**：带有 [semantic reranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 的 hybrid search，用于改进相关性
* **Semantic Configuration**：用于 [semantic ranking](https://learn.microsoft.com/azure/search/semantic-search-overview) 的 semantic configuration 名称。如果未指定，默认为 `semantic-search-config`。只有当你预先创建了带自定义 semantic configuration name 的 index 时，才需要此项。

{% hint style="info" %}
**Query mode 选择**

使用 **Vector** 进行语义相似度搜索，使用 **Keyword** 进行精确词匹配，使用 **Hybrid** 获得平衡结果，或在你的 index 中配置了 semantic search 时使用 **Semantic Hybrid** 获取最高相关性。
{% endhint %}

### OData filter 示例 <a href="#odata-filter-examples" id="odata-filter-examples"></a>

Azure AI Search 使用 [OData syntax](https://learn.microsoft.com/azure/search/search-query-odata-filter) 进行过滤。Metadata fields 使用 `metadata/fieldName` 格式访问。

**按 document ID 过滤：**

```
id eq '3da6491a-f930-4a4e-9471-c05dcd450ba0'
```

**按 metadata field 过滤：**

```
metadata/source eq 'user-guide'
```

**复杂 AND filter：**

```
metadata/category eq 'technology' and metadata/author eq 'John'
```

**复杂 OR filter：**

```
metadata/source eq 'user-guide' or metadata/rating ge 4
```

**数值比较：**

```
metadata/rating ge 4 and metadata/rating lt 10
```

**使用 NOT 的字符串匹配：**

```
metadata/category eq 'technology' and metadata/title ne 'Deprecated'
```

**支持的 OData operators：**

* Comparison：`eq`、`ne`、`gt`、`ge`、`lt`、`le`
* Logical：`and`、`or`、`not`
* String functions：`startswith()`、`endswith()`、`contains()`
* Collection functions：`any()`、`all()`

{% hint style="info" %}
**Filter 格式**

Filters 适用于所有 query modes（Vector、Keyword、Hybrid、Semantic Hybrid）和所有 operation modes（retrieve、load、retrieve-as-tool）。
{% endhint %}

## Azure AI Search 特定功能 <a href="#azure-ai-search-specific-features" id="azure-ai-search-specific-features"></a>

### 使用 RRF 的 Hybrid search <a href="#hybrid-search-with-rrf" id="hybrid-search-with-rrf"></a>

Azure AI Search 的 hybrid search 使用 Reciprocal Rank Fusion 合并 vector 和 keyword 结果，相比单独使用任一方法可提供更好的准确性。

### [Semantic ranking](https://learn.microsoft.com/azure/search/semantic-search-overview) <a href="#semantic-rankinghttpslearnmicrosoftcomazuresearchsemantic-search-overview" id="semantic-rankinghttpslearnmicrosoftcomazuresearchsemantic-search-overview"></a>

Semantic Hybrid 模式会应用 machine learning models，根据对查询的语义理解重新排序结果。这需要你的 index 中存在 semantic configuration。

### OData filters <a href="#odata-filters" id="odata-filters"></a>

使用 OData syntax 在 vector search 执行前按 document fields 或 metadata 过滤。当你需要来自特定来源或具有特定属性的结果时，这会提高性能和精度。

### HNSW algorithm <a href="#hnsw-algorithm" id="hnsw-algorithm"></a>

Azure AI Search 使用 Hierarchical Navigable Small World（HNSW）graphs 进行 approximate nearest neighbor search，以可配置的 accuracy/speed 取舍提供大规模快速检索。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Index 问题 <a href="#index-issues" id="index-issues"></a>

**Index not found**：确认 index name 正确（区分大小写）且存在于你的 Azure AI Search service 中。如果使用自动创建，请检查 index 是否已成功创建。

**Vector dimension mismatch**：确保 embedding model dimensions 与 index vector field dimensions 匹配。检查 index schema 以确认 `vectorSearchDimensions` 设置。

**Document insert failures**：

* 验证写入权限（需要 admin API key）
* 检查 document fields 是否与你的 index schema 匹配
* 确保 documents 中提供了必需字段
* 如果处理大型 document sets 时遇到超时，请检查 batch size 设置

### Filter 问题 <a href="#filter-issues" id="filter-issues"></a>

**Filter not working**：

* 验证 OData syntax 是否正确
* 确保 metadata fields 使用 `metadata/` 前缀：`metadata/source eq 'value'`
* 检查 filtered fields 是否在你的 index schema 中标记为 `filterable`
* 在使用复杂 expressions 前，先用简单 filters（`id eq 'value'`）测试

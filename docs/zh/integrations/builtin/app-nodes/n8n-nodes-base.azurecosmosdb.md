---
title: Azure Cosmos DB node documentation
description: >-
  了解如何在 n8n 中使用 Azure Cosmos DB node。按照技术文档将 Azure Cosmos DB node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Azure Cosmos DB node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurecosmosdb
layout:
  description:
    visible: false
---

# Azure Cosmos DB node <a href="#azure-cosmos-db-node" id="azure-cosmos-db-node"></a>

使用 Azure Cosmos DB node 自动化 Azure Cosmos DB 中的工作，并将 Azure Cosmos DB 与其他应用集成。n8n 内置支持大量 Azure Cosmos DB 功能，包括创建、获取、更新和删除 container 与 item。

在本页中，你可以找到 Azure Cosmos DB node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/azurecosmosdb.md)找到此 node 的身份验证信息。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Container**:
	* **Create**
	* **Delete**
	* **Get**
	* **Get Many**
* **Item**:
	* **Create**
	* **Delete**
	* **Get**
	* **Get Many**
	* **Execute Query**
	* **Update**

## Item: Execute Query <a href="#item-execute-query" id="item-execute-query"></a>

对 container 执行 NoSQL SQL query，并返回匹配的 item。

### 参数 <a href="#parameters" id="parameters"></a>

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| **Container** | 是 | 要对其运行 query 的 container。从列表中选择，或直接输入 container ID。 |
| **Query** | 是 | 要执行的 SQL query。使用 `$1`、`$2`、`$3` 等作为 query 参数的位置 placeholder。n8n 在向 Azure Cosmos DB 发送请求前，会自动将这些转换为 `@Param1`、`@Param2`、`@Param3`。例如：`SELECT * FROM c WHERE c.status = $1 AND c.startDate = $2`。 |
| **Simplify** | 否 | 启用后（默认），会从返回的 item 中移除内部 Cosmos DB metadata 字段（以 `_` 开头的字段）。禁用后可接收完整 raw API response。 |

### 选项 <a href="#options" id="options"></a>

展开 **Options** 配置 query 参数。

| 选项 | 说明 |
| --- | --- |
| **Query Parameters** | 以逗号分隔的字符串值列表，会按位置映射到 query 中的 `$1`、`$2` 等。**所有值始终会作为字符串发送。** 可将其用于简单文本筛选，例如名称或状态值。示例：`active,2024`。 |
| **Query Parameters (JSON)** | JSON 数组值，会按位置映射到 query 中的 `$1`、`$2` 等。保留原生类型：number、boolean、`null`，以及带前导零的字符串。当类型精度很重要时，请使用此选项替代 **Query Parameters**。示例：`[1737062400000, "01234", true, null]`。 |

{% hint style="info" %}
**在 Query Parameters 和 Query Parameters (JSON) 之间选择**

Azure Cosmos DB 执行类型敏感的比较。像
`WHERE c.startDate = $1` 这样的筛选，如果数据库中的 `startDate` 存储为 number
但参数以字符串到达，则不会返回结果。

- 当所有筛选值都是文本（名称、状态、标识符）时，使用 **Query Parameters**。
- 当需要按 number、boolean、`null` 或必须保持字符串形式的数字开头字符串（例如 `"01234"` 这样的邮政编码）筛选时，使用 **Query Parameters (JSON)**。

**限制：** JavaScript 的 JSON parser 无法以完整精度表示大于
`Number.MAX_SAFE_INTEGER`（`9007199254740991`）的整数。使用 **Query Parameters (JSON)** 时，超过此限制的值可能会丢失精度。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Azure Cosmos DB node 文档集成模板](https://n8n.io/integrations/azure-cosmos-db)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure Cosmos DB 文档](https://learn.microsoft.com/en-us/rest/api/cosmos-db/)。


{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

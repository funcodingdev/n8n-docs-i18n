---
title: Azure Cosmos DB credentials
description: >-
  Azure Cosmos DB credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Azure Cosmos DB。
contentType:
  - integration
  - reference
nodeTitle: Azure Cosmos DB credentials
originalFilePath: integrations/builtin/credentials/azurecosmosdb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/azurecosmosdb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/azurecosmosdb'
layout:
  description:
    visible: false
---

# Azure Cosmos DB credentials <a href="#azure-cosmos-db-credentials" id="azure-cosmos-db-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Azure Cosmos DB](../app-nodes/n8n-nodes-base.azurecosmosdb.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Azure](https://azure.microsoft.com) subscription。
* 创建一个 [Azure Cosmos DB account](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-manage-database-account)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API Key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure Cosmos DB 的 API 文档](https://learn.microsoft.com/en-us/rest/api/cosmos-db/)。

## 使用 API Key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

* **Account**：你的 Azure Cosmos DB account 名称。
* **Key**：Azure Cosmos DB account 的 key。在 Azure portal 中为你的 Azure Cosmos DB 选择 **Overview** > **Keys**。你可以使用两个 account keys 中的任意一个。
* **Database**：要连接的 Azure Cosmos DB database 名称。

有关更详细的步骤，请参阅 [Get your primary key | Microsoft](https://learn.microsoft.com/en-us/previous-versions/azure/cosmos-db/how-to-obtain-keys?tabs=azure-portal)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Azure Cosmos DB credentials 的已知常见错误和问题。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fXYywkPyzPTxeGOEnYgb/" %}

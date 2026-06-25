---
title: Azure Storage node documentation
description: >-
  了解如何在 n8n 中使用 Azure Storage node。按照技术文档将 Azure Storage node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Azure Storage node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.azurestorage.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.azurestorage'
layout:
  description:
    visible: false
---

# Azure Storage node <a href="#azure-storage-node" id="azure-storage-node"></a>

Azure Storage node 内置支持大量功能，包括创建、获取和删除 blob 与 container。使用此 node 自动化 Azure Storage 服务内的工作，或将其与 workflow 中的其他服务集成。

在本页中，你可以找到 Azure Storage node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/azurestorage.md)找到此 node 的身份验证信息。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* **Blob**
	* **Create blob**：创建新 blob 或替换现有 blob。
	* **Delete blob**：删除现有 blob。
	* **Get blob**：检索特定 blob 的数据。
	* **Get many blobs**：检索 blob 列表。
* **Container**
	* **Create container**：创建新 container。
	* **Delete container**：删除现有 container。
	* **Get container**：检索特定 container 的数据。
	* **Get many containers**：检索 container 列表。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Azure Storage node 文档集成模板](https://n8n.io/integrations/azure-storage)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Microsoft Azure Storage 文档](https://learn.microsoft.com/en-us/rest/api/storageservices/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

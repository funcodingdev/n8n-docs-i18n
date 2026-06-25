---
title: Microsoft SharePoint node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft SharePoint node。按照技术文档将 Microsoft SharePoint
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Microsoft SharePoint node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftsharepoint
layout:
  description:
    visible: false
---

# Microsoft SharePoint node <a href="#microsoft-sharepoint-node" id="microsoft-sharepoint-node"></a>

使用 Microsoft SharePoint node 自动化 Microsoft SharePoint 中的工作，并将 Microsoft SharePoint 与其他应用集成。n8n 内置支持大量 Microsoft SharePoint 功能，包括下载、上传和更新文件，管理 list 中的 item，以及获取 list 和 list item。

在本页中，你可以找到 Microsoft SharePoint node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/microsoft.md)找到此 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **File**:
    * Download：下载文件。
    * Update：更新文件。
    * Upload：上传现有文件。
* **Item**:
    * Create：在现有 list 中创建 item。
    * Create or Update：创建新 item；如果当前 item 已存在，则更新它（upsert）。
    * Delete：从 list 中删除 item。
    * Get：从 list 中检索 item。
    * Get Many：获取 list 中的特定 item，或列出多个 item。
    * Update：更新现有 list 中的 item。
* **List**:
    * Get：检索单个 list 的详细信息。
    * Get Many：检索 list 列表。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft SharePoint node 文档集成模板](https://n8n.io/integrations/microsoft-sharepoint)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Microsoft SharePoint 文档](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service)。

---
title: Microsoft OneDrive node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft OneDrive node。按照技术文档将 Microsoft OneDrive node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft OneDrive node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftonedrive
layout:
  description:
    visible: false
---

# Microsoft OneDrive node <a href="#microsoft-onedrive-node" id="microsoft-onedrive-node"></a>

使用 Microsoft OneDrive node 自动化 Microsoft OneDrive 中的工作，并将 Microsoft OneDrive 与其他应用集成。n8n 内置支持大量 Microsoft OneDrive 功能，包括创建、更新、删除和获取文件与文件夹。

在本页中，你可以找到 Microsoft OneDrive node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

此 node 支持两种身份验证选项：

- **Microsoft Drive OAuth2 API**：Microsoft OneDrive 专用 OAuth2 credential（默认）。
- **Microsoft OAuth2 API**：可在其他 Microsoft node 中复用的通用 Microsoft Graph credential。选择此选项时，请确保 credential 已被授予此 node 所需的 scope（例如 `Files.ReadWrite.All`）。

有关设置身份验证的指导，请参阅 [Microsoft credentials](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用 government cloud tenant（US Government、US Government DOD 或 China），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* File
    * 复制文件
    * 删除文件
    * 下载文件
    * 获取文件
    * 重命名文件
    * 搜索文件
    * 共享文件
    * 上传最大 4MB 的文件
* Folder
    * 创建文件夹
    * 删除文件夹
    * 获取子项（获取文件夹内的 item）
    * 重命名文件夹
    * 搜索文件夹
    * 共享文件夹

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft OneDrive node 文档集成模板](https://n8n.io/integrations/microsoft-onedrive)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Microsoft OneDrive API 文档](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)。

## 查找文件夹 ID <a href="#find-the-folder-id" id="find-the-folder-id"></a>

要对文件夹执行操作，你需要提供 ID。你可以通过以下方式找到它：

* 在文件夹 URL 中查找
* 使用 node 搜索它。如果使用 MS 365（OneDrive 在底层使用 SharePoint），你需要这样做：
    1. 选择 **Resource** > **Folder**。
    2. 选择 **Operation** > **Search**。
    3. 在 **Query** 中输入文件夹名称。
    4. 选择 **Execute step**。n8n 会运行查询并返回文件夹相关数据，其中包括包含文件夹 ID 的 `id` 字段。

---
title: Google Drive File and Folder operations
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Drive File and Folder operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations
description: >-
  n8n 中 Google Drive node 的 File and Folder 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# File and Folder operations

使用此操作在 Google Drive 中搜索文件和文件夹。有关 Google Drive node 本身的更多信息，请参阅 [Google Drive](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Search files and folders <a href="#search-files-and-folders" id="search-files-and-folders"></a>

使用此操作在 drive 中搜索文件和文件夹。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **File/Folder**。
* **Operation**：选择 **Search**。
* **Search Method**：选择搜索方式：
  * **Search File/Folder Name**：在 **Search Query** 中填写要搜索的文件或文件夹名称。也会返回与查询部分匹配的文件和文件夹。
  * **Advanced Search**：填写 **Query String**，使用 [Google query string syntax](https://developers.google.com/drive/api/guides/search-files) 搜索文件和文件夹。
* **Return All**：选择是返回所有结果，还是只返回给定限制内的结果。
* **Limit**：禁用 **Return All** 时要返回的最大 item 数。
* **Filter**：选择是否限制搜索范围：
  * **Drive**：要搜索的 drive。默认使用你的个人 "My Drive"。选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
    * 访问浏览器中的共享 drive 并复制 URL 的最后一段，即可找到 `driveId`：`https://drive.google.com/drive/u/1/folders/driveId`。
  * **Folder**：要搜索的文件夹。选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。
    * 访问浏览器中的共享文件夹并复制 URL 的最后一段，即可找到 `folderId`：`https://drive.google.com/drive/u/1/folders/folderId`。
  * **What to Search**：搜索 **Files and Folders**、**Files** 还是 **Folders**。
  * **Include Trashed Items**：是否同时返回 Drive 回收站中的 item。

### Options <a href="#options" id="options"></a>

* **Fields**：选择要返回的字段。可以是以下一个或多个字段：**\[All]**、**explicitlyTrashed**、**exportLinks**、**hasThumbnail**、**iconLink**、**ID**、**Kind**、**mimeType**、**Name**、**Permissions**、**Shared**、**Spaces**、**Starred**、**thumbnailLink**、**Trashed**、**Version** 或 **webViewLink**。

有关更多信息，请参阅 [Method: files.list | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/list) API 文档。

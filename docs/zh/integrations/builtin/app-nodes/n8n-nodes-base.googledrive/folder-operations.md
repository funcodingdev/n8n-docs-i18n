---
title: Google Drive Folder operations
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Drive Folder operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations
description: >-
  n8n 中 Google Drive node 的 Folder 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Folder operations

使用此操作在 Google Drive 中创建、删除和共享文件夹。有关 Google Drive node 本身的更多信息，请参阅 [Google Drive](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Create a folder <a href="#create-a-folder" id="create-a-folder"></a>

使用此操作在 drive 中创建新文件夹。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Folder**。
* **Operation**：选择 **Create**。
* **Folder Name**：新文件夹使用的名称。
* **Parent Drive**：选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
* **Parent Folder**：选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。

访问浏览器中的共享 drive 或文件夹并复制 URL 的最后一段，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### Options <a href="#options" id="options"></a>

* **Simplify Output**：选择是否返回简化版响应，而不是包含所有字段。
* **Folder Color**：文件夹颜色，使用 RGB 十六进制字符串。

有关更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。

## Delete a folder <a href="#delete-a-folder" id="delete-a-folder"></a>

使用此操作从 drive 删除文件夹。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Folder**。
* **Operation**：选择 **Delete**。
* **Folder**：选择要删除的文件夹。
  * 选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。
  * 你可以在 Google Drive 文件夹 URL 中找到 `folderId`：`https://drive.google.com/drive/u/0/folders/folderID`。

### Options <a href="#options" id="options"></a>

* **Delete Permanently**：选择是立即永久删除文件夹，还是将其移至回收站。

有关更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。

## Share a folder <a href="#share-a-folder" id="share-a-folder"></a>

使用此操作为文件夹添加共享权限。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Folder**。
* **Operation**：选择 **Share**。
* **Folder**：选择要共享的文件夹。
  * 选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。
  * 你可以在 Google Drive 文件夹 URL 中找到 `folderId`：`https://drive.google.com/drive/u/0/folders/folderID`。
* **Permissions**：要添加到文件夹的权限：
  * **Role**：选择用户可对文件夹执行的操作。可以是 **Commenter**、**File Organizer**、**Organizer**、**Owner**、**Reader**、**Writer** 之一。
  * **Type**：选择新权限的范围：
    * **User**：向特定用户授予权限，通过输入其 **Email Address** 定义。
    * **Group**：向特定群组授予权限，通过输入其 **Email Address** 定义。
    * **Domain**：向完整域授予权限，通过 **Domain** 定义。
    * **Anyone**：向任何人授予权限。可以选择 **Allow File Discovery**，使文件可通过搜索发现。

### Options <a href="#options" id="options"></a>

* **Email Message**：要包含在通知邮件中的纯文本自定义消息。
* **Move to New Owners Root**：在共享非共享 drive 中的 item 时尝试转移所有权可用。启用后，会将文件夹移动到新所有者的 My Drive 根文件夹。
* **Send Notification Email**：共享给用户或群组时是否发送通知邮件。
* **Transfer Ownership**：是否将所有权转移给指定用户，并将当前所有者降级为 writer 权限。
* **Use Domain Admin Access**：是否以域管理员身份执行此操作。

有关更多信息，请参阅 [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files) API 文档。

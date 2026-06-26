---
title: Google Drive File operations
description: >-
  n8n 中 Google Drive node 的 File 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Drive File operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations
layout:
  description:
    visible: false
---

# Google Drive File operations <a href="#google-drive-file-operations" id="google-drive-file-operations"></a>

使用此操作在 Google Drive 中创建、删除、变更和管理文件。有关 Google Drive node 本身的更多信息，请参阅 [Google Drive](README.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Copy a file <a href="#copy-a-file" id="copy-a-file"></a>

使用此操作将文件复制到 drive。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Copy**。
- **File**：选择要复制的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。
- **File Name**：新文件副本使用的名称。
- **Copy In The Same Folder**：选择是否将文件复制到同一文件夹。如果禁用，请设置以下内容：
	- **Parent Drive**：选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
	- **Parent Folder**：选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。
	- 访问浏览器中的共享 drive 或文件夹并复制 URL 的最后一段，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### Options <a href="#options" id="options"></a>

- **Copy Requires Writer Permissions**：选择是否允许 reader 和 commenter 复制、打印或下载新文件。
- **Description**：文件的简短描述。

有关更多信息，请参阅 [Method: files.copy | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/copy) API 文档。

## Create from text <a href="#create-from-text" id="create-from-text"></a>

使用此操作根据提供的文本在 drive 中创建新文件。

输入以下参数：
- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Create From Text**。
- **File Content**：输入用于创建新文件的文件内容。
- **File Name**：新文件使用的名称。
- **Parent Drive**：选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
- **Parent Folder**：选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。

访问浏览器中的共享 drive 或文件夹并复制 URL 的最后一段，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### Options <a href="#options" id="options"></a>

- **APP Properties**：一组任意键值对，对发起请求的应用私有。
- **Properties**：一组任意键值对，对所有应用可见。
- **Keep Revision Forever**：选择是否在新的 head revision 中设置 `keepForever` 字段。此选项仅适用于包含二进制内容的文件。最多可保留 200 个 revision，之后必须删除已固定的 revision。


- **OCR Language**：一个 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码，用于帮助 OCR 在导入期间解释内容。


- **Use Content As Indexable Text**：选择是否将上传内容标记为可索引文本。
- **Convert to Google Document**：选择是否创建 Google Document，而不是默认 `.txt` 格式。要使用此功能，必须在 [Google API Console](https://console.cloud.google.com/apis/library/docs.googleapis.com) 中启用 Google Docs API。

有关更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。

## Delete a file <a href="#delete-a-file" id="delete-a-file"></a>

使用此操作从 drive 删除文件。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Delete**。
- **File**：选择要删除的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。

### Options <a href="#options" id="options"></a>

- **Delete Permanently**：选择是立即永久删除文件，还是将其移至回收站。

有关更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。

## Download a file <a href="#download-a-file" id="download-a-file"></a>

使用此操作从 drive 下载文件。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Download**。
- **File**：选择要下载的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。

### Options <a href="#options" id="options"></a>

- **Put Output File in Field**：选择用于放置二进制文件内容的字段名称，使后续 node 可以使用该内容。
- **Google File Conversion**：下载 Google 文件时选择要导出的格式：
	* **Google Docs**：下载 Google Docs 文件时选择使用的导出格式：**HTML**、**MS Word Document**、**Open Office Document**、**PDF**、**Rich Text (rtf)** 或 **Text (txt)**。
	* **Google Drawings**：下载 Google Drawing 文件时选择使用的导出格式：**JPEG**、**PDF**、**PNG** 或 **SVG**。
	* **Google Slides**：下载 Google Slides 文件时选择使用的导出格式：**MS PowerPoint**、**OpenOffice Presentation** 或 **PDF**。
	* **Google Sheets**：下载 Google Sheets 文件时选择使用的导出格式：**CSV**、**MS Excel**、**Open Office Sheet** 或 **PDF**。
- **File Name**：下载文件使用的名称。

有关更多信息，请参阅 [Method: files.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/get) API 文档。

## Move a file <a href="#move-a-file" id="move-a-file"></a>

使用此操作将文件移动到 drive 中的其他位置。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Move**。
- **File**：选择要移动的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。
- **Parent Drive**：选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
- **Parent Folder**：选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。

访问浏览器中的共享 drive 或文件夹并复制 URL 的最后一段，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

有关更多信息，请参阅 [Method: parents.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/parents/insert) API 文档。

## Share a file <a href="#share-a-file" id="share-a-file"></a>

使用此操作为文件添加共享权限。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Share**。
- **File**：选择要共享的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。
- **Permissions**：要添加到文件的权限：
	- **Role**：选择用户可对文件执行的操作。可以是 **Commenter**、**File Organizer**、**Organizer**、**Owner**、**Reader**、**Writer** 之一。
	- **Type**：选择新权限的范围：
		- **User**：向特定用户授予权限，通过输入其 **Email Address** 定义。
		- **Group**：向特定群组授予权限，通过输入其 **Email Address** 定义。
		- **Domain**：向完整域授予权限，通过 **Domain** 定义。
		- **Anyone**：向任何人授予权限。可以选择 **Allow File Discovery**，使文件可通过搜索发现。

### Options <a href="#options" id="options"></a>

- **Email Message**：要包含在通知邮件中的纯文本自定义消息。

- **Move to New Owners Root**：共享不在共享 drive 中的 item 并尝试转移所有权时可用。启用后，会将文件移动到新所有者的 My Drive 根文件夹。

- **Send Notification Email**：共享给用户或群组时是否发送通知邮件。
- **Transfer Ownership**：是否将所有权转移给指定用户，并将当前所有者降级为 writer 权限。
- **Use Domain Admin Access**：是否以域管理员身份执行此操作。

有关更多信息，请参阅 [REST Resources: files | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files) API 文档。

## Update a file <a href="#update-a-file" id="update-a-file"></a>

使用此操作更新文件。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Update**。
- **File to Update**：选择要更新的文件。
    - 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入文件 URL，或选择 **By ID** 输入 `fileId`。
    - 你可以在可共享的 Google Drive 文件 URL 中找到 `fileId`：`https://docs.google.com/document/d/fileId/edit#gid=0`。在 Google Drive 中，选择 **Share > Copy link** 获取可共享文件 URL。
- **Change File Content**：选择是否发送新的二进制数据来替换现有文件内容。启用后，请填写以下内容：
	- **Input Data Field Name**：包含要使用的二进制文件数据的输入字段名称。
- **New Updated File Name**：如果要更新文件名，则填写文件的新名称。

### Options <a href="#options" id="options"></a>

- **APP Properties**：一组任意键值对，对发起请求的应用私有。
- **Properties**：一组任意键值对，对所有应用可见。
- **Keep Revision Forever**：选择是否在新的 head revision 中设置 `keepForever` 字段。此选项仅适用于包含二进制内容的文件。最多可保留 200 个 revision，之后必须删除已固定的 revision。


- **OCR Language**：一个 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码，用于帮助 OCR 在导入期间解释内容。


- **Use Content As Indexable Text**：选择是否将上传内容标记为可索引文本。
- **Move to Trash**：是否将文件移至回收站。仅文件所有者可以执行。
- **Return Fields**：返回文件相关的元数据字段。可以是以下一个或多个字段：**[All]**、**explicitlyTrashed**、**exportLinks**、**hasThumbnail**、**iconLink**、**ID**、**Kind**、**mimeType**、**Name**、**Permissions**、**Shared**、**Spaces**、**Starred**、**thumbnailLink**、**Trashed**、**Version** 或 **webViewLink**。

有关更多信息，请参阅 [Method: files.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/update) API 文档。

## Upload a file <a href="#upload-a-file" id="upload-a-file"></a>

使用此操作上传文件。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/README.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Upload**。
- **Input Data Field Name**：包含要使用的二进制文件数据的输入字段名称。
- **File Name**：新文件使用的名称。
- **Parent Drive**：选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
- **Parent Folder**：选择 **From list** 可从下拉列表中选择文件夹，选择 **By URL** 可输入文件夹 URL，或选择 **By ID** 输入 `folderId`。

访问浏览器中的共享 drive 或文件夹并复制 URL 的最后一段，即可找到 `driveId` 和 `folderID`：`https://drive.google.com/drive/u/1/folders/driveId`。

### Options <a href="#options" id="options"></a>

- **APP Properties**：一组任意键值对，对发起请求的应用私有。
- **Properties**：一组任意键值对，对所有应用可见。
- **Keep Revision Forever**：选择是否在新的 head revision 中设置 `keepForever` 字段。此选项仅适用于包含二进制内容的文件。最多可保留 200 个 revision，之后必须删除已固定的 revision。


- **OCR Language**：一个 [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) 语言代码，用于帮助 OCR 在导入期间解释内容。


- **Use Content As Indexable Text**：选择是否将上传内容标记为可索引文本。
- **Simplify Output**：选择是否返回简化版响应，而不是包含所有字段。

有关更多信息，请参阅 [Method: files.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/insert) API 文档。

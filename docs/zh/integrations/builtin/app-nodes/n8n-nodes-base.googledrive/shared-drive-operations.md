---
title: Google Drive Shared Drive operations
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Drive Shared Drive operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations
description: >-
  n8n 中 Google Drive node 的 Shared Drive 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Shared Drive operations

使用此操作在 Google Drive 中创建、删除、获取和更新共享 drive。有关 Google Drive node 本身的更多信息，请参阅 [Google Drive](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Create a shared drive <a href="#create-a-shared-drive" id="create-a-shared-drive"></a>

使用此操作创建新的共享 drive。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Shared Drive**。
* **Operation**：选择 **Create**。
* **Name**：新共享 drive 使用的名称。

### Options <a href="#options" id="options"></a>

* **Capabilities**：要为新共享 drive 设置的能力（更多详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)）：
  * **Can Add Children**：当前用户是否可以向此共享 drive 中的文件夹添加子项。
  * **Can Change Copy Requires Writer Permission Restriction**：当前用户是否可以更改此共享 drive 上的 `copyRequiresWriterPermission` 限制。
  * **Can Change Domain Users Only Restriction**：当前用户是否可以更改此共享 drive 上的 `domainUsersOnly` 限制。
  * **Can Change Drive Background**：当前用户是否可以更改此共享 drive 的背景。
  * **Can Change Drive Members Only Restriction**：当前用户是否可以更改此共享 drive 上的 `driveMembersOnly` 限制。
  * **Can Comment**：当前用户是否可以评论此共享 drive 中的文件。
  * **Can Copy**：当前用户是否可以复制此共享 drive 中的文件。
  * **Can Delete Children**：当前用户是否可以从此共享 drive 的文件夹中删除子项。
  * **Can Delete Drive**：当前用户是否可以删除此共享 drive。如果共享 drive 中仍有未在回收站中的 item，此操作仍可能失败。
  * **Can Download**：当前用户是否可以从此共享 drive 下载文件。
  * **Can Edit**：当前用户是否可以编辑此共享 drive 中的文件。
  * **Can List Children**：当前用户是否可以列出此共享 drive 中文件夹的子项。
  * **Can Manage Members**：当前用户是否可以添加、移除或更改此共享 drive 成员的角色。
  * **Can Read Revisions**：当前用户是否可以读取此共享 drive 中文件的 revisions 资源。
  * **Can Rename Drive**：当前用户是否可以重命名此共享 drive。
  * **Can Share**：当前用户是否可以共享此共享 drive 中的文件或文件夹。
  * **Can Trash Children**：当前用户是否可以将此共享 drive 中文件夹的子项移至回收站。
* **Color RGB**：此共享 drive 的颜色，使用 RGB 十六进制字符串。
* **Hidden**：是否在默认视图中隐藏此共享 drive。
* **Restrictions**：要添加到此共享 drive 的限制（更多详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)）：
  * **Admin Managed Restrictions**：启用后，此处的限制会将此共享 drive 内任何文件中同名字段覆盖为 true。
  * **Copy Requires Writer Permission**：是否对 reader 和 commenter 禁用复制、打印或下载此共享 drive 内文件的选项。
  * **Domain Users Only**：是否将对此共享 drive 及其内部 item 的访问限制为此共享 drive 所属域的用户。
  * **Drive Members Only**：是否将对此共享 drive 内 item 的访问限制为其成员。

有关更多信息，请参阅 [Method: drives.insert | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/insert) API 文档。

## Delete a shared drive <a href="#delete-a-shared-drive" id="delete-a-shared-drive"></a>

使用此操作删除共享 drive。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Shared Drive**。
* **Operation**：选择 **Delete**。
* **Shared Drive**：选择要删除的共享 drive。
  * 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
  * 你可以在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

有关更多信息，请参阅 [Method: drives.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/delete) API 文档。

## Get a shared drive <a href="#get-a-shared-drive" id="get-a-shared-drive"></a>

使用此操作获取共享 drive。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Shared Drive**。
* **Operation**：选择 **Get**。
* **Shared Drive**：选择要获取的共享 drive。
  * 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
  * 你可以在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### Options <a href="#options" id="options"></a>

* **Use Domain Admin Access**：是否以域管理员身份发出请求。启用后，如果请求者是共享 drive 所属域的管理员，则授予请求者访问权限。

有关更多信息，请参阅 [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get) API 文档。

## Get many shared drives <a href="#get-many-shared-drives" id="get-many-shared-drives"></a>

使用此操作获取多个共享 drive。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Shared Drive**。
* **Operation**：选择 **Get Many**。
* **Return All**：选择是返回所有结果，还是只返回给定限制内的结果。
* **Limit**：禁用 **Return All** 时要返回的最大 item 数。
* **Shared Drive**：选择要获取的共享 drive。
  * 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
  * 你可以在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### Options <a href="#options" id="options"></a>

* **Query**：用于搜索共享 drive 的查询字符串。更多信息请参阅 [Search for shared drives | Google Drive](https://developers.google.com/drive/api/guides/search-shareddrives)。
* **Use Domain Admin Access**：是否以域管理员身份发出请求。启用后，如果请求者是共享 drive 所属域的管理员，则授予请求者访问权限。

有关更多信息，请参阅 [Method: drives.get | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/get) API 文档。

## Update a shared drive <a href="#update-a-shared-drive" id="update-a-shared-drive"></a>

使用此操作更新共享 drive。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Drive credentials](../../credentials/google/)。
* **Resource**：选择 **Shared Drive**。
* **Operation**：选择 **Update**。
* **Shared Drive**：选择要更新的共享 drive。
  * 选择 **From list** 可从下拉列表中选择 drive，选择 **By URL** 可输入 drive URL，或选择 **By ID** 输入 `driveId`。
  * 你可以在共享 Google Drive 的 URL 中找到 `driveId`：`https://drive.google.com/drive/u/0/folders/driveID`。

### Update Fields <a href="#update-fields" id="update-fields"></a>

* **Color RGB**：此共享 drive 的颜色，使用 RGB 十六进制字符串。
* **Name**：共享 drive 更新后的名称。
* **Restrictions**：此共享 drive 的限制（更多详情请参阅 [REST Resources: drives | Google Drive](https://developers.google.com/drive/api/reference/rest/v3/drives)）：
  * **Admin Managed Restrictions**：启用后，此处的限制会将此共享 drive 内任何文件中同名字段覆盖为 true。
  * **Copy Requires Writer Permission**：是否对 reader 和 commenter 禁用复制、打印或下载此共享 drive 内文件的选项。
  * **Domain Users Only**：是否将对此共享 drive 及其内部 item 的访问限制为此共享 drive 所属域的用户。
  * **Drive Members Only**：是否将对此共享 drive 内 item 的访问限制为其成员。

有关更多信息，请参阅 [Method: drives.update | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/drives/update) API 文档。

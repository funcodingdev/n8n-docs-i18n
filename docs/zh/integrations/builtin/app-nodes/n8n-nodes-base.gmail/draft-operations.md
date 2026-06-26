---
title: Gmail node Draft Operations documentation
description: >-
  了解如何在 n8n 中使用 Gmail node 的 Draft Operations。按照技术文档，
  将 Draft Operations 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Gmail node Draft Operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations
layout:
  description:
    visible: false
---

# Gmail node Draft Operations <a href="#gmail-node-draft-operations" id="gmail-node-draft-operations"></a>

使用 Draft operations 在 Gmail 中创建、删除、获取单个 draft 或列出 drafts。有关 Gmail node 本身的更多信息，请参考 [Gmail node](README.md)。

## Create a draft <a href="#create-a-draft" id="create-a-draft"></a>

使用此 operation 创建新的 draft。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Draft**。
* **Operation**：选择 **Create**。
* **Subject**：输入 subject line。
* 选择 **Email Type**。可选择 **Text** 或 **HTML**。
* **Message**：输入 email message body。

### Create draft options <a href="#create-draft-options" id="create-draft-options"></a>

使用这些 options 进一步调整 node 行为：

* **Attachments**：选择 **Add Attachment** 添加附件。输入 **Attachment Field Name (in Input)**，用于标识 input node 中哪个字段包含附件。
    * 如有多个 properties，请输入逗号分隔列表。
* **BCC**：输入一个或多个 blind copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**：输入一个或多个 carbon copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **From Alias Name or ID**：选择发送 draft 使用的 alias。此字段会根据你在参数中选择的 credential 填充。
* **Send Replies To**：输入 email address，设置为 reply-to address。
* **Thread ID**：如果你希望此 draft 附加到某个 thread，请输入该 thread 的 ID。
* **To Email**：输入一个或多个 recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。

更多信息请参考 [Gmail API Method: users.drafts.create](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/create) 文档。

## Delete a draft <a href="#delete-a-draft" id="delete-a-draft"></a>

使用此 operation 删除 draft。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Draft**。
* **Operation**：选择 **Delete**。
* **Draft ID**：输入你想删除的 draft ID。

更多信息请参考 [Gmail API Method: users.drafts.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/delete) 文档。

## Get a draft <a href="#get-a-draft" id="get-a-draft"></a>

使用此 operation 获取单个 draft。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Draft**。
* **Operation**：选择 **Get**。
* **Draft ID**：输入你想获取信息的 draft ID。

### Get draft options <a href="#get-draft-options" id="get-draft-options"></a>

使用这些 options 进一步调整 node 行为：

* **Attachment Prefix**：输入 binary property 名称的 prefix，node 会将所有 attachments 写入该 binary property。n8n 会在 prefix 后添加从 `0` 开始的 index。例如，如果你输入 `attachment_` 作为 prefix，第一个 attachment 会保存到 `attachment_0`。
* **Download Attachments**：选择 node 是否下载 draft 的 attachments（打开）或不下载（关闭）。

更多信息请参考 [Gmail API Method: users.drafts.get](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/get) 文档。


## Get Many drafts <a href="#get-many-drafts" id="get-many-drafts"></a>


使用此 operation 获取两个或更多 drafts。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Draft**。
* **Operation**：选择 **Get Many**。
* **Return All**：选择 node 是返回全部 drafts（打开），还是最多返回设定 limit 数量（关闭）。
* **Limit**：输入要返回的最大 drafts 数量。仅在关闭 **Return All** 时使用。


### Get Many drafts options <a href="#get-many-drafts-options" id="get-many-drafts-options"></a>


使用这些 options 进一步调整 node 行为：

* **Attachment Prefix**：输入 binary property 名称的 prefix，node 会将所有 attachments 写入该 binary property。n8n 会在 prefix 后添加从 `0` 开始的 index。例如，如果你输入 `attachment_` 作为 prefix，第一个 attachment 会保存到 `attachment_0`。
* **Download Attachments**：选择 node 是否下载 draft 的 attachments（打开）或不下载（关闭）。
* **Include Spam and Trash**：选择 node 是否获取 Spam 和 Trash folders 中的 drafts（打开）或不获取（关闭）。

更多信息请参考 [Gmail API Method: users.drafts.list](https://developers.google.com/gmail/api/reference/rest/v1/users.drafts/list) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见 errors 或 issues 及建议解决步骤，请参考 [常见问题](common-issues.md)。

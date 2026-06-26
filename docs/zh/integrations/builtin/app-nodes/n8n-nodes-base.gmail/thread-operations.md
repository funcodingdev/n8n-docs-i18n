---
title: Gmail node Thread Operations documentation
description: >-
  了解如何在 n8n 中使用 Gmail node 的 Thread Operations。按照技术文档，
  将 Thread Operations 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Gmail node Thread Operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations
layout:
  description:
    visible: false
---

# Gmail node Thread Operations <a href="#gmail-node-thread-operations" id="gmail-node-thread-operations"></a>

使用 Thread operations 删除、reply、trash、untrash、添加/移除 labels、获取单个 thread 或列出 threads。有关 Gmail node 本身的更多信息，请参考 [Gmail node](README.md)。

## Add Label to a thread <a href="#add-label-to-a-thread" id="add-label-to-a-thread"></a>

使用此 operation 向 thread 添加 label。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Add Label**。
* **Thread ID**：输入你想添加 label 的 thread ID。
* **Label Names or IDs**：选择要应用的 Label names，或输入 expression 指定 IDs。dropdown 会根据你选择的 **Credential** 填充。


更多信息请参考 [Gmail API Method: users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify) 文档。


## Delete a thread <a href="#delete-a-thread" id="delete-a-thread"></a>

使用此 operation 立即且永久删除 thread 及其所有 messages。

{% hint style="info" %}
**永久删除**

此 operation 无法撤销。对于可恢复的删除，请改用 [Trash operation](#trash-a-thread)。
{% endhint %}

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Delete**。
* **Thread ID**：输入你想删除的 thread ID。

更多信息请参考 [Gmail API Method: users.threads.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/delete) 文档。

## Get a thread <a href="#get-a-thread" id="get-a-thread"></a>

使用此 operation 获取单个 thread。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Get**。
* **Thread ID**：输入你想检索的 thread ID。
* **Simplify**：选择返回简化版 response（打开）还是 raw data（关闭）。默认为打开。
    * 这相当于将 API call 的 `format` 设置为 `metadata`，会返回 email message IDs、labels 和 email headers，包括 From、To、CC、BCC 和 Subject。

### Get thread options <a href="#get-thread-options" id="get-thread-options"></a>

使用这些 options 进一步调整 node 行为：

* **Return Only Messages**：选择是否只返回 thread messages（打开）。

更多信息请参考 [Gmail API Method: users.threads.get](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/get) 文档。


## Get Many threads <a href="#get-many-threads" id="get-many-threads"></a>


使用此 operation 获取两个或更多 threads。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Get Many**。
* **Return All**：选择 node 是返回全部 threads（打开），还是最多返回设定 limit 数量（关闭）。
* **Limit**：输入要返回的最大 threads 数量。仅在关闭 **Return All** 时使用。


### Get Many threads filters <a href="#get-many-threads-filters" id="get-many-threads-filters"></a>


使用这些 filters 进一步调整 node 行为：

* **Include Spam and Trash**：选择 node 是否获取 Spam 和 Trash folders 中的 threads（打开）或不获取（关闭）。
* **Label Names or IDs**：只返回已添加所选 labels 的 threads。选择要应用的 Label names，或输入 expression 指定 IDs。dropdown 会根据你选择的 **Credential** 填充。
* **Search**：输入 Gmail search refine filters，例如 `from:`，用于过滤返回的 threads。更多信息请参考 [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en)。
* **Read Status**：选择接收 **Unread and read emails**、**Unread emails only**（默认）或 **Read emails only**。
* **Received After**：只返回指定日期和时间之后收到的 emails。使用 date picker 选择日期和时间，或输入 expression 以 ISO format string 或 milliseconds timestamp 设置日期。有关 string 格式的更多信息，请参考 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Received Before**：只返回指定日期和时间之前收到的 emails。使用 date picker 选择日期和时间，或输入 expression 以 ISO format string 或 milliseconds timestamp 设置日期。有关 string 格式的更多信息，请参考 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。

更多信息请参考 [Gmail API Method: users.threads.list](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/list) 文档。

## Remove label from a thread <a href="#remove-label-from-a-thread" id="remove-label-from-a-thread"></a>

使用此 operation 从 thread 移除 label。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Remove Label**。
* **Thread ID**：输入你想从中移除 label 的 thread ID。
* **Label Names or IDs**：选择要移除的 Label names，或输入 expression 指定它们的 IDs。dropdown 会根据你选择的 **Credential** 填充。


更多信息请参考 [Gmail API Method: users.threads.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/modify) 文档。


## Reply to a message <a href="#reply-to-a-message" id="reply-to-a-message"></a>

使用此 operation reply to a message。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Reply**。
* **Thread ID**：输入你想 reply 的 thread ID。
* **Message Snippet or ID**：选择你想 reply 的 Message，或输入 expression 指定其 ID。dropdown 会根据你选择的 **Credential** 填充。
* 选择 **Email Type**。可选择 **Text** 或 **HTML**。
* **Message**：输入 email message body。

### Reply options <a href="#reply-options" id="reply-options"></a>

使用这些 options 进一步调整 node 行为：

* **Attachments**：选择 **Add Attachment** 添加附件。输入 **Attachment Field Name (in Input)**，用于标识 input node 中哪个字段包含附件。
    * 如有多个 properties，请输入逗号分隔列表。
* **BCC**：输入一个或多个 blind copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**：输入一个或多个 carbon copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**：输入你希望在 recipients email 中显示的 sender 名称。
* **Reply to Sender Only**：选择 reply all（关闭）还是只 reply 给 sender（打开）。

更多信息请参考 [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) 文档。

## Trash a thread <a href="#trash-a-thread" id="trash-a-thread"></a>

使用此 operation 将 thread 及其所有 messages 移到 trash。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Trash**。
* **Thread ID**：输入你想移动到 trash 的 thread ID。

更多信息请参考 [Gmail API Method: users.threads.trash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/trash) 文档。

## Untrash a thread <a href="#untrash-a-thread" id="untrash-a-thread"></a>

使用此 operation 从 trash 恢复 thread 及其所有 messages。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Thread**。
* **Operation**：选择 **Untrash**。
* **Thread ID**：输入你想从 trash 恢复的 thread ID。

更多信息请参考 [Gmail API Method: users.threads.untrash](https://developers.google.com/gmail/api/reference/rest/v1/users.threads/untrash) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见 errors 或 issues 及建议解决步骤，请参考 [常见问题](common-issues.md)。

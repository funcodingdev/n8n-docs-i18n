---
title: Gmail node Message Operations documentation
description: >-
  了解如何在 n8n 中使用 Gmail node 的 Message Operations。按照技术文档，
  将 Message Operations 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Gmail node Message Operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations
layout:
  description:
    visible: false
---

# Gmail node Message Operations <a href="#gmail-node-message-operations" id="gmail-node-message-operations"></a>

使用 Message operations 在 Gmail 中发送、回复、删除、标记已读或未读、添加 label、移除 label、获取单个 message 或获取 messages 列表。有关 Gmail node 本身的更多信息，请参考 [Gmail node](README.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

## Add Label to a message <a href="#add-label-to-a-message" id="add-label-to-a-message"></a>

使用此 operation 向 message 添加一个或多个 labels。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Add Label**。
* **Message ID**：输入你想添加 label 的 message ID。
* **Label Names or IDs**：选择要添加的 Label names，或输入 expression 指定 IDs。dropdown 会根据你选择的 **Credential** 填充。


更多信息请参考 [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) 文档。


## Delete a message <a href="#delete-a-message" id="delete-a-message"></a>

使用此 operation 立即且永久删除 message。

{% hint style="info" %}
**永久删除**

此 operation 无法撤销。对于可恢复的删除，请改用 [Thread Trash operation](thread-operations.md#trash-a-thread)。
{% endhint %}

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Delete**。
* **Message ID**：输入你想删除的 message ID。

更多信息请参考 [Gmail API Method: users.messages.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete) 文档。

## Get a message <a href="#get-a-message" id="get-a-message"></a>

使用此 operation 获取单个 message。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Get**。
* **Message ID**：输入你想检索的 message ID。
* **Simplify**：选择返回简化版 response（打开）还是 raw data（关闭）。默认为打开。
    * 这相当于将 API call 的 `format` 设置为 `metadata`，会返回 email message IDs、labels 和 email headers，包括 From、To、CC、BCC 和 Subject。

更多信息请参考 [Gmail API Method: users.messages.get](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/get) 文档。


## Get Many messages <a href="#get-many-messages" id="get-many-messages"></a>


使用此 operation 获取两个或更多 messages。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Get Many**。
* **Return All**：选择 node 是返回全部 messages（打开），还是最多返回设定 limit 数量（关闭）。
* **Limit**：输入要返回的最大 messages 数量。仅在关闭 **Return All** 时使用。
* **Simplify**：选择返回简化版 response（打开）还是 raw data（关闭）。默认为打开。
    * 这相当于将 API call 的 `format` 设置为 `metadata`，会返回 email message IDs、labels 和 email headers，包括 From、To、CC、BCC 和 Subject。


### Get Many messages filters <a href="#get-many-messages-filters" id="get-many-messages-filters"></a>


使用这些 filters 进一步调整 node 行为：

* **Include Spam and Trash**：选择 node 是否获取 Spam 和 Trash folders 中的 messages（打开）或不获取（关闭）。
* **Label Names or IDs**：只返回已添加所选 labels 的 messages。选择要应用的 Label names，或输入 expression 指定 IDs。dropdown 会根据你选择的 **Credential** 填充。
* **Search**：输入 Gmail search refine filters，例如 `from:`，用于过滤返回的 messages。更多信息请参考 [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en)。
* **Read Status**：选择接收 **Unread and read emails**、**Unread emails only**（默认）或 **Read emails only**。
* **Received After**：只返回指定日期和时间之后收到的 emails。使用 date picker 选择日期和时间，或输入 expression 以 ISO format string 或 milliseconds timestamp 设置日期。有关 string 格式的更多信息，请参考 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Received Before**：只返回指定日期和时间之前收到的 emails。使用 date picker 选择日期和时间，或输入 expression 以 ISO format string 或 milliseconds timestamp 设置日期。有关 string 格式的更多信息，请参考 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)。
* **Sender**：输入 email 或 sender name 的一部分，只返回来自该 sender 的 messages。

更多信息请参考 [Gmail API Method: users.messages.list](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/list) 文档。

## Mark as Read <a href="#mark-as-read" id="mark-as-read"></a>

使用此 operation 将 message 标记为已读。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Mark as Read**。
* **Message ID**：输入你想标记为已读的 message ID。


更多信息请参考 [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) 文档。


## Mark as Unread <a href="#mark-as-unread" id="mark-as-unread"></a>

使用此 operation 将 message 标记为未读。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Mark as Unread**。
* **Message ID**：输入你想标记为未读的 message ID。


更多信息请参考 [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) 文档。


## Remove Label from a message <a href="#remove-label-from-a-message" id="remove-label-from-a-message"></a>

使用此 operation 从 message 移除一个或多个 labels。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Remove Label**。
* **Message ID**：输入你想从中移除 label 的 message ID。
* **Label Names or IDs**：选择要移除的 Label names，或输入 expression 指定 IDs。dropdown 会根据你选择的 **Credential** 填充。


更多信息请参考 [Gmail API Method: users.messages.modify](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/modify) 文档。


## Reply to a message <a href="#reply-to-a-message" id="reply-to-a-message"></a>

使用此 operation 以 reply 形式发送 message 到现有 message。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Reply**。
* **Message ID**：输入你想 reply 的 message ID。
* 选择 **Email Type**。可选择 **Text** 或 **HTML**。
* **Message**：输入 email message body。

### Reply options <a href="#reply-options" id="reply-options"></a>

使用这些 options 进一步调整 node 行为：

* **Append n8n attribution**：默认情况下，node 会在 email 末尾追加 `This email was sent automatically with n8n`。要移除此 statement，请关闭此 option。
* **Attachments**：选择 **Add Attachment** 添加附件。输入 **Attachment Field Name (in Input)**，用于标识 input node 中哪个字段包含附件。
    * 如有多个 properties，请输入逗号分隔列表。
* **BCC**：输入一个或多个 blind copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**：输入一个或多个 carbon copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**：输入你希望在 recipients email 中显示的 sender 名称。
* **Reply to Sender Only**：选择 reply all（关闭）还是只 reply 给 sender（打开）。

更多信息请参考 [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) 文档。

## Send a message <a href="#send-a-message" id="send-a-message"></a>

使用此 operation 发送 message。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send**。
* **To**：输入你想发送 email 到的 email address。
* **Subject**：输入 subject line。
* 选择 **Email Type**。可选择 **Text** 或 **HTML**。
* **Message**：输入 email message body。

### Send options <a href="#send-options" id="send-options"></a>

使用这些 options 进一步调整 node 行为：

* **Append n8n attribution**：默认情况下，node 会在 email 末尾追加 `This email was sent automatically with n8n`。要移除此 statement，请关闭此 option。
* **Attachments**：选择 **Add Attachment** 添加附件。输入 **Attachment Field Name (in Input)**，用于标识 input node 中哪个字段包含附件。
    * 如有多个 properties，请输入逗号分隔列表。
* **BCC**：输入一个或多个 blind copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **CC**：输入一个或多个 carbon copy recipients 的 email addresses。多个 email addresses 用逗号分隔，例如 `jay@gatsby.com, jon@smith.com`。
* **Sender Name**：输入你希望在 recipients email 中显示的 sender 名称。
* **Send Replies To**：输入 email address，设置为 reply-to address。
* **Reply to Sender Only**：选择 reply all（关闭）还是只 reply 给 sender（打开）。

更多信息请参考 [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) 文档。

## Send a message and wait for approval <a href="#send-a-message-and-wait-for-approval" id="send-a-message-and-wait-for-approval"></a>

使用此 operation 发送 message，并等待 recipient 批准后再继续 workflow execution。

{% hint style="info" %}
**复杂审批请使用 Wait**

**Send and Wait for Approval** operation 非常适合简单 approval processes。对于更复杂的 approvals，请考虑使用 [Wait node](../../core-nodes/n8n-nodes-base.wait.md)。
{% endhint %}

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send and Wait for Approval**。
* **To**：输入你想发送 email 到的 email address。
* **Subject**：输入 subject line。
* **Message**：输入 email message body。

### Send and wait for approval options <a href="#send-and-wait-for-approval-options" id="send-and-wait-for-approval-options"></a>

使用这些 options 进一步调整 node 行为：

* **Type of Approval**：选择 **Approve Only**（默认）仅包含 approval button，或选择 **Approve and Disapprove** 同时包含 disapproval option。
* **Approve Button Label**：approval button 使用的 label（默认为 **Approve**）。
* **Approve Button Style**：approval button 样式使用 **Primary**（默认）还是 **Secondary**。
* **Disapprove Button Label**：disapproval button 使用的 label（默认为 **Decline**）。仅当你将 **Type of Approval** 设置为 **Approve and Disapprove** 时可见。
* **Disapprove Button Style**：disapproval button 样式使用 **Primary** 还是 **Secondary**（默认）。仅当你将 **Type of Approval** 设置为 **Approve and Disapprove** 时可见。

更多信息请参考 [Gmail API Method: users.messages.send](https://developers.google.com/gmail/api/reference/rest/v1/users.messages/send) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见 errors 或 issues 及建议解决步骤，请参考 [常见问题](common-issues.md)。

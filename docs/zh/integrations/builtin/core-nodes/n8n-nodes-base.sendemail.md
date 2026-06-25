---
title: Send Email
contentType:
  - integration
  - reference
priority: high
nodeTitle: Send Email
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sendemail
description: >-
  n8n 中 Send Email node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
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

# Send Email

Send Email node 使用 SMTP email server 发送 email。

{% hint style="info" %}
**Credential**

你可以在[这里](../credentials/send-email/)找到此 node 的身份验证信息。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

使用以下参数配置此 node。

### Credential to connect with <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建此 node 要使用的 [SMTP account credential](../credentials/send-email/)。

### Operation <a href="#operation" id="operation"></a>

Send Email node 支持以下操作：

* **Send**：发送 email。
* **Send and Wait for Response**：发送 email，并等待接收者响应。此操作会暂停 workflow 执行，直到用户提交响应。

选择 **Send and Wait for Response** 会启用[等待响应](n8n-nodes-base.sendemail.md#waiting-for-a-response)中讨论的参数和选项。

### From Email <a href="#from-email" id="from-email"></a>

输入你希望用于发送 email 的 email 地址。你也可以使用此格式包含名称：`Name Name <email@sample.com>`，例如：`Nathan Doe <nate@n8n.io>`。

### To Email <a href="#to-email" id="to-email"></a>

输入要发送 email 的目标 email 地址。你也可以使用此格式包含名称：`Name Name <email@sample.com>`，例如：`Nathan Doe <nate@n8n.io>`。使用逗号分隔多个 email 地址：`first@sample.com, "Name" <second@sample.com>`。

{% hint style="info" %}
**Email 格式**

此 email 格式也适用于 CC 和 BCC 字段。
{% endhint %}

### Subject <a href="#subject" id="subject"></a>

输入 email 的主题行。

### Email Format <a href="#email-format" id="email-format"></a>

选择发送 email 的格式。使用 **Send** 操作时，此参数可用。可选值包括：

* **Text**：以纯文本格式发送 email。
* **HTML**：以 HTML 格式发送 email。
* **Both**：同时以两种格式发送 email。如果选择此选项，email 接收者的客户端会决定显示哪种格式。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些 **Options** 进一步细化 node 的行为。

### Append n8n Attribution <a href="#append-n8n-attribution" id="append-n8n-attribution"></a>

设置是否在 email 末尾包含 `This email was sent automatically with n8n` 短语（开启），或不包含（关闭）。

### Attachments <a href="#attachments" id="attachments"></a>

输入包含要作为附件添加的数据的二进制属性名称。使用此选项的一些提示：

* 使用 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) node 或 [HTTP Request](n8n-nodes-base.httprequest/) node 将文件上传到你的 workflow。
* 输入以逗号分隔的二进制属性列表，以添加多个附件。
* 在 email message 正文中引用嵌入图片或其他内容，例如 `<img src="cid:image_1">`。

### CC Email <a href="#cc-email" id="cc-email"></a>

输入 `cc:` 字段的 email 地址。

### BCC Email <a href="#bcc-email" id="bcc-email"></a>

输入 `bcc:` 字段的 email 地址。

### Ignore SSL Issues <a href="#ignore-ssl-issues" id="ignore-ssl-issues"></a>

设置 n8n 是否应忽略 TLS/SSL 证书验证失败（开启），或强制执行验证（关闭）。

### Reply To <a href="#reply-to" id="reply-to"></a>

输入 Reply To 字段的 email 地址。

## 等待响应 <a href="#waiting-for-a-response" id="waiting-for-a-response"></a>

选择 **Send and Wait for a Response** 操作后，你可以发送 email message，并暂停 workflow 执行，直到某人确认操作或提供更多信息。

### Response Type <a href="#response-type" id="response-type"></a>

你可以在以下等待和批准操作类型之间选择：

* **Approval**：用户可以在 message 内批准或拒绝。
* **Free Text**：用户可以通过表单提交响应。
* **Custom Form**：用户可以通过自定义表单提交响应。

根据所选类型的不同，可用选项也不同。

### Approval 参数和选项 <a href="#approval-parameters-and-options" id="approval-parameters-and-options"></a>

使用 Approval response type 时，以下选项可用：

* **Type of Approval**：是只显示批准按钮，还是同时显示批准和拒绝按钮。
* **Button Label**：批准或拒绝按钮的标签。默认选择分别是批准和拒绝操作的 `Approve` 与 `Decline`。
* **Button Style**：按钮样式（primary 或 secondary）。

此 mode 还提供以下选项：

* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。可以是时间间隔，也可以是具体的时钟时间。
* **Append n8n Attribution**：设置是否在 email 末尾包含 `This email was sent automatically with n8n` 短语（开启），或不包含（关闭）。

### Free Text 参数和选项 <a href="#free-text-parameters-and-options" id="free-text-parameters-and-options"></a>

使用 Free Text response type 时，以下选项可用：

* **Message Button Label**：message 按钮使用的标签。默认选择是 `Respond`。
* **Response Form Title**：用户提供响应的表单标题。
* **Response Form Description**：用户提供响应的表单说明。
* **Response Form Button Label**：表单上用于提交响应的按钮标签。默认选择是 `Submit`。
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。可以是时间间隔，也可以是具体的时钟时间。
* **Append n8n Attribution**：设置是否在 email 末尾包含 `This email was sent automatically with n8n` 短语（开启），或不包含（关闭）。

### Custom Form 参数和选项 <a href="#custom-form-parameters-and-options" id="custom-form-parameters-and-options"></a>

使用 Custom Form response type 时，你可以使用想要的字段和选项构建表单。

你可以使用 [n8n Form trigger 的表单元素](n8n-nodes-base.formtrigger.md#form-elements)中列出的设置自定义每个表单元素。要添加更多字段，请选择 **Add Form Element** 按钮。

以下选项也可用：

* **Message Button Label**：message 按钮使用的标签。默认选择是 `Respond`。
* **Response Form Title**：用户提供响应的表单标题。
* **Response Form Description**：用户提供响应的表单说明。
* **Response Form Button Label**：表单上用于提交响应的按钮标签。默认选择是 `Submit`。
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。可以是时间间隔，也可以是具体的时钟时间。
* **Append n8n Attribution**：设置是否在 email 末尾包含 `This email was sent automatically with n8n` 短语（开启），或不包含（关闭）。

## 限制 <a href="#limitations" id="limitations"></a>

Send Email (SMTP) node 不支持设置 `In-Reply-To` 和 `References` 等 email threading 所需的 header。因此，每封 email 都会被视为新的 conversation，而不是显示在同一个 thread 中。

* **Workaround**：使用 Gmail node 的 **Reply to a message** 操作，或使用支持自定义 header 的 custom node。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Send Email 集成模板](https://n8n.io/integrations/send-email)或[搜索所有模板](https://n8n.io/workflows/)

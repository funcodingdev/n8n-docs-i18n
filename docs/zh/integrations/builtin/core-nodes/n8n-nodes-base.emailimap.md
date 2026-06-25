---
title: Email Trigger (IMAP) node 文档
description: >-
  了解如何在 n8n 中使用 Email Trigger (IMAP) Trigger node。按照技术
  文档将 Email Trigger (IMAP) Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Email Trigger (IMAP) node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.emailimap'
layout:
  description:
    visible: false
---

# Email Trigger (IMAP) node <a href="#email-trigger-imap-node" id="email-trigger-imap-node"></a>

使用 IMAP Email node 可以通过 IMAP 邮件服务器接收电子邮件。此 node 是 trigger node。

{% hint style="info" %}
**Credential**

你可以在[这里](../credentials/imap/README.md)找到该 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

- 接收电子邮件

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置该 node。

### Credential to connect with <a href="#credential-to-connect-with" id="credential-to-connect-with"></a>

选择或创建用于连接服务器的 [IMAP credential](../credentials/imap/README.md)。

### Mailbox Name <a href="#mailbox-name" id="mailbox-name"></a>

输入你想从中接收邮件的 mailbox。

### Action <a href="#action" id="action"></a>

选择当 n8n 收到邮件时，是否要将该邮件标记为已读。**None** 会让它保持未读状态。**Mark as Read** 会将其标记为已读。

### Download Attachments <a href="#download-attachments" id="download-attachments"></a>

此开关控制是否下载电子邮件附件（开启）或不下载（关闭）。由于这会增加处理量，请仅在必要时设置。

### Format <a href="#format" id="format"></a>

从以下选项中选择要返回的消息格式：

* **RAW**：此格式会返回完整的电子邮件消息数据，body 内容以 base64url 编码字符串形式位于 raw 字段中。它不使用 payload 字段。
* **Resolved**：此格式会返回完整邮件，其中所有数据都已解析，附件保存为二进制数据。
* **Simple**：此格式会返回完整邮件。如果你想收集内联附件，请不要使用它。

## Node 选项 <a href="#node-options" id="node-options"></a>

你可以使用这些 **Options** 进一步配置该 node。

### Custom Email Rules <a href="#custom-email-rules" id="custom-email-rules"></a>

输入自定义邮件获取规则，以决定该 node 获取哪些邮件。

更多信息请参阅 [node-imap 的 search function criteria](https://github.com/mscdex/node-imap)。

### Force Reconnect Every Minutes <a href="#force-reconnect-every-minutes" id="force-reconnect-every-minutes"></a>

设置强制重新连接的分钟间隔。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Email Trigger (IMAP) node 集成模板](https://n8n.io/integrations/email-trigger-imap)或[搜索所有模板](https://n8n.io/workflows/)

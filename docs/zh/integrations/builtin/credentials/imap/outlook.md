---
title: Outlook.com
description: >-
  Outlook.com IMAP credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Outlook.com IMAP 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Outlook.com
originalFilePath: integrations/builtin/credentials/imap/outlook.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/imap/outlook'
url: 'https://docs.n8n.io/integrations/builtin/credentials/imap/outlook'
layout:
  description:
    visible: false
---

{% hint style="warning" %}
**Microsoft 已移除 Outlook.com IMAP 的 Basic Auth**

Microsoft 已弃用 Exchange Online 和 Outlook.com 中 IMAP 的 Basic Authentication。因此，IMAP node **无法连接到 Outlook.com 或 Microsoft 365 accounts**。App passwords 不能绕过此限制。

**请改用 [Microsoft Outlook node](../../app-nodes/n8n-nodes-base.microsoftoutlook.md)。** 它使用 OAuth 2.0，这是 Microsoft 现在对 mail access 的要求。

更多信息请参考 [Microsoft's deprecation notice](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)。
{% endhint %}


# Outlook.com IMAP credentials <a href="#outlookcom-imap-credentials" id="outlookcom-imap-credentials"></a>

由于 Microsoft 已弃用 Basic Authentication，n8n 不再支持 Outlook.com 和 Microsoft 365 accounts 的 IMAP access。你无法使用 IMAP（无论是常规 password 还是 app password）连接到 Outlook.com 或 Microsoft 365 accounts。

要替代用于 incoming email 的 IMAP triggers，请使用支持 Message Received event 的 [Microsoft Outlook Trigger node](../../trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)。

对于常规 Microsoft Outlook 自动化，请使用 [Microsoft Outlook node](../../app-nodes/n8n-nodes-base.microsoftoutlook.md)，它会使用 Microsoft 要求的 OAuth 2.0。

更多信息请参考 [Microsoft's deprecation notice](https://learn.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/deprecation-of-basic-authentication-exchange-online#what-we-are-changing)。

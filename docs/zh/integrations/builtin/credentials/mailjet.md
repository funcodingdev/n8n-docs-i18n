---
title: Mailjet credentials
description: >-
  Mailjet credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mailjet 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Mailjet credentials
originalFilePath: integrations/builtin/credentials/mailjet.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mailjet'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mailjet'
layout:
  description:
    visible: false
---

# Mailjet credentials <a href="#mailjet-credentials" id="mailjet-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mailjet](../app-nodes/n8n-nodes-base.mailjet.md)
- [Mailjet Trigger](../trigger-nodes/n8n-nodes-base.mailjettrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mailjet](https://www.mailjet.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Email API key：用于 Mailjet 的 Email API
- SMS token：用于 Mailjet 的 SMS API

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关每个服务的更多信息，请参考 [Mailjet's Email API documentation](https://dev.mailjet.com/email/guides/) 和 [Mailjet's SMS API documentation](https://dev.mailjet.com/sms/reference/send-message/)。

## 使用 Email API key <a href="#using-email-api-key" id="using-email-api-key"></a>

要配置此 credential，你需要：

- **API Key**：在 Mailjet [API Key Management](https://app.mailjet.com/signin) 页面查看和生成 API keys。
- **Secret Key**：在 Mailjet [API Key Management](https://app.mailjet.com/signin) 页面查看你的 API Secret Keys。
- _可选：_ 选择是否对使用此 credential 发起的调用使用 **Sandbox Mode**。开启后，所有 API calls 都会使用 Sandbox mode：API 仍会验证 payloads，但不会实际发送消息。这对于排查 payload error messages 很有用，且不会真正发送消息。更多信息请参考 Mailjet 的 [Sandbox Mode documentation](https://dev.mailjet.com/email/guides/send-api-v31/#sandbox-mode)。

对于此 credential，你可以使用以下任一项：

- Mailjet 的 primary API key 和 secret key
- subaccount API key 和 secret key

创建更多 API keys 的详细说明请参考 Mailjet 的 [How to create a subaccount (or additional API key) documentation](https://documentation.mailjet.com/hc/en-us/articles/360042561974-How-to-create-a-subaccount-or-additional-API-Key)。有关 Mailjet subaccounts 以及何时使用它们的更多信息，请参考 [What are subaccounts and how does it help me?](https://documentation.mailjet.com/hc/en-us/articles/360042561854-What-are-subaccounts-and-how-does-it-help-me) 页面。

## 使用 SMS Token <a href="#using-sms-token" id="using-sms-token"></a>

要配置此 credential，你需要：

- access **Token**：从 Mailjet 的 [SMS Dashboard](https://app.mailjet.com/sms) 生成新 token。

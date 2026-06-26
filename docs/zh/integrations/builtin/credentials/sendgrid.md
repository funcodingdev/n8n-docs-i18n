---
title: SendGrid credentials
description: >-
  SendGrid credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SendGrid 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: SendGrid credentials
originalFilePath: integrations/builtin/credentials/sendgrid.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/sendgrid'
url: 'https://docs.n8n.io/integrations/builtin/credentials/sendgrid'
layout:
  description:
    visible: false
---

# SendGrid credentials <a href="#sendgrid-credentials" id="sendgrid-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SendGrid](../app-nodes/n8n-nodes-base.sendgrid.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SendGrid's API documentation](https://www.twilio.com/docs/sendgrid/api-reference)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [SendGrid](https://sendgrid.com) 账号，以及：

- 一个 **API Key**

要创建 API key：

1. 在 Twilio SendGrid app 中，前往 **Settings >** [**API Keys**](https://app.sendgrid.com/settings/api_keys)。
2. 选择 **Create API Key**。
3. 为你的 API key 输入一个 **Name**，例如 `n8n integration`。
4. 选择 **Full Access**。
5. 选择 **Create & View**。
6. 复制 key，并将其输入到你的 n8n credential 中。

更多信息请参考 [Create API Keys](https://www.twilio.com/docs/sendgrid/api-reference/api-keys/create-api-keys)。

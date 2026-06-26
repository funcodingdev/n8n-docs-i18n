---
title: MailerLite credentials
description: >-
  MailerLite credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MailerLite 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: MailerLite credentials
originalFilePath: integrations/builtin/credentials/mailerlite.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mailerlite'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mailerlite'
layout:
  description:
    visible: false
---

# MailerLite credentials <a href="#mailerlite-credentials" id="mailerlite-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [MailerLite](../app-nodes/n8n-nodes-base.mailerlite.md)
- [MailerLite Trigger](../trigger-nodes/n8n-nodes-base.mailerlitetrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MailerLite](https://www.mailerlite.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MailerLite's API documentation](https://developers.mailerlite.com/docs/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：从 **Integrations** 菜单生成 API key。更详细说明请参考 [API Authentication documentation](https://developers.mailerlite.com/docs/#authentication)。

如果 API key 用于 MailerLite Classic account，而不是较新的 MailerLite experience，请启用 **Classic API** toggle。

{% hint style="info" %}
大多数新的 MailerLite accounts 和所有免费 accounts 都应禁用 **Classic API** toggle。你可以了解[自己正在使用哪个 MailerLite 版本](https://www.mailerlite.com/help/which-version-of-mailerlite-am-i-using)，并在 [MailerLite FAQ](https://www.mailerlite.com/help/new-mailerlite-faq) 中了解两者之间的更多差异。
{% endhint %}

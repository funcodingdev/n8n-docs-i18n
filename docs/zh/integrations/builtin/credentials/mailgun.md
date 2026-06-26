---
title: Mailgun credentials
description: >-
  Mailgun credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mailgun 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Mailgun credentials
originalFilePath: integrations/builtin/credentials/mailgun.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mailgun'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mailgun'
layout:
  description:
    visible: false
---

# Mailgun credentials <a href="#mailgun-credentials" id="mailgun-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mailgun](../app-nodes/n8n-nodes-base.mailgun.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Mailgun](https://www.mailgun.com/) 账号。
- 在 Mailgun 中[添加并验证 domain](https://help.mailgun.com/hc/en-us/articles/360026833053-Domain-Verification-Setup-Guide)，或使用提供的 sandbox domain 进行测试。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mailgun's API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Domain**：如果你的 Mailgun account 位于欧洲，请选择 **api.eu.mailgun.net**；否则选择 **api.mailgun.net**。更多信息请参考 [Mailgun Base URLs](https://documentation.mailgun.com/docs/mailgun/api-reference/api-overview#base-url)。
- **Email Domain**：输入你正在使用的 email sending domain。如果你有多个 sending domains，更多信息请参考[使用多个 email domains](#working-with-multiple-email-domains)。
- **API Key**：在 **Settings > API Keys** 中查看你的 API key。更详细说明请参考 [Mailgun's API Authentication documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/mg-auth)。

## 使用多个 email domains <a href="#working-with-multiple-email-domains" id="working-with-multiple-email-domains"></a>

如果你的 Mailgun account 包含多个 sending domains，请为正在使用的每个 email domain 创建单独的 credential。

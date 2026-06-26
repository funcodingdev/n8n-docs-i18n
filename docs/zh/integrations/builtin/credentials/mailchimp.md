---
title: Mailchimp credentials
description: >-
  Mailchimp credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mailchimp 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Mailchimp credentials
originalFilePath: integrations/builtin/credentials/mailchimp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mailchimp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mailchimp'
layout:
  description:
    visible: false
---

# Mailchimp credentials <a href="#mailchimp-credentials" id="mailchimp-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mailchimp](../app-nodes/n8n-nodes-base.mailchimp.md)
- [Mailchimp Trigger](../trigger-nodes/n8n-nodes-base.mailchimptrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Mailchimp](https://www.mailchimp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OAuth2

有关应使用哪种方式，请参考[选择身份验证方式](#selecting-an-authentication-method)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mailchimp's API documentation](https://mailchimp.com/developer/marketing/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：在 Mailchimp 账号的 [API keys section](https://us1.admin.mailchimp.com/account/api/) 生成 API key。更详细说明请参考 [Mailchimp 生成 API key 文档](https://mailchimp.com/developer/marketing/guides/quick-start/#generate-your-api-key)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从头配置 OAuth2，请[注册 application](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#register-your-application)。更多信息请参考 [Mailchimp OAuth2 documentation](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/)。

## 选择身份验证方式 <a href="#selecting-an-authentication-method" id="selecting-an-authentication-method"></a>

如果你只访问自己 Mailchimp account 的数据，Mailchimp 建议使用 API key：

> 如果你编写的代码将_你的_ application 数据与_你的_ Mailchimp account 数据紧密耦合，请使用 API key。如果你需要访问_其他人_的 Mailchimp account 数据，应使用 OAuth 2（[source](https://mailchimp.com/developer/marketing/guides/access-user-data-oauth-2/#when-not-to-use-oauth-2)）

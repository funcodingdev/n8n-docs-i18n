---
title: PayPal credentials
description: >-
  PayPal credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  PayPal 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: PayPal credentials
originalFilePath: integrations/builtin/credentials/paypal.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/paypal'
url: 'https://docs.n8n.io/integrations/builtin/credentials/paypal'
layout:
  description:
    visible: false
---

# PayPal credentials <a href="#paypal-credentials" id="paypal-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [PayPal](../app-nodes/n8n-nodes-base.paypal.md)
- [PayPal Trigger](../trigger-nodes/n8n-nodes-base.paypaltrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [PayPal developer](https://developer.paypal.com/home) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API client and secret

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Paypal's API documentation](https://developer.paypal.com/api/rest/)。

## 使用 API client and secret <a href="#using-api-client-and-secret" id="using-api-client-and-secret"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：创建 app 时生成。
- 一个 **Secret**：创建 app 时生成。
- 一个 **Environment**：选择 **Live** 或 **Sandbox**。

要生成 **Client ID** 和 **Secret**，请登录你的 Paypal [developer dashboard](https://developer.paypal.com/dashboard/)。选择 **Apps & Credentials > Rest API apps > Create app**。更多信息请参考 [Get client ID and client secret](https://developer.paypal.com/api/rest/#link-getclientidandclientsecret)。

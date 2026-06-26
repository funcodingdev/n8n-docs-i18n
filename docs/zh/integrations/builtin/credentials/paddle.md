---
title: Paddle credentials
description: >-
  Paddle credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Paddle 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Paddle credentials
originalFilePath: integrations/builtin/credentials/paddle.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/paddle'
url: 'https://docs.n8n.io/integrations/builtin/credentials/paddle'
layout:
  description:
    visible: false
---

# Paddle credentials <a href="#paddle-credentials" id="paddle-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Paddle](../app-nodes/n8n-nodes-base.paddle.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Paddle](https://paddle.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token (Classic)

{% hint style="warning" %}
**Paddle Classic API**

此 credential 适用于 Paddle Classic 的 API。如果你是在 2023 年 8 月之后加入 Paddle，则使用的是 [Paddle Billing API](https://developer.paddle.com/api-reference/overview)，此 credential 可能不适用于你。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Paddle Classic's API documentation](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference)。

## 使用 API access token (Classic) <a href="#using-api-access-token-classic" id="using-api-access-token-classic"></a>

要配置此 credential，你需要：

- 一个 **Vendor Auth Code**：生成 API key 时创建。
- 一个 **Vendor ID**：生成 API key 时显示。
- **Use Sandbox Environment API**：启用后，使用此 credential 的 nodes 会命中 Sandbox API endpoint，而不是 live API endpoint。

要生成 auth code 并查看 Vendor ID，请前往 **Paddle > Developer Tools > Authentication > Generate Auth Code**。选择 **Reveal Auth Code** 显示 Auth Code。更多信息请参考 [API Authentication](https://developer.paddle.com/api-reference/about/authentication)。

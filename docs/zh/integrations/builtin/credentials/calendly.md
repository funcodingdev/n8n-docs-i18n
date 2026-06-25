---
title: Calendly credentials
description: >-
  Calendly credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Calendly。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Calendly credentials
originalFilePath: integrations/builtin/credentials/calendly.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/calendly'
url: 'https://docs.n8n.io/integrations/builtin/credentials/calendly'
layout:
  description:
    visible: false
---

# Calendly credentials <a href="#calendly-credentials" id="calendly-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Calendly Trigger](../trigger-nodes/n8n-nodes-base.calendlytrigger.md)

{% hint style="warning" %}
**支持的 Calendly plans**

Calendly Trigger node 依赖 Calendly webhooks。Calendly 只在付费 plans 中提供 webhooks 访问权限。
{% endhint %}

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Personal Access Token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Calendly 的 API 文档](https://developer.calendly.com/getting-started)。

## 使用 Personal Access Token <a href="#using-personal-access-token" id="using-personal-access-token"></a>

要配置此 credential，你需要一个 [Calendly](https://www.calendly.com/) 账号，以及：

- 一个 **Personal Access Token**

获取 access token：

1. 前往 Calendly [**Integrations & apps**](https://calendly.com/integrations) 页面。
2. 选择 [**API & Webhooks**](https://calendly.com/integrations/api_webhooks)。
3. 在 **Your Personal Access Tokens** 中，选择 **Generate new token**。
4. 输入 access token 的 **Name**，例如 `n8n integration`。
5. 选择 **Create token**。
6. 选择 **Copy token**，并将其输入到 n8n credential 中。

有关更多信息，请参阅 [Calendly API authentication 文档](https://developer.calendly.com/how-to-authenticate-with-personal-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Calendly developer](https://developer.calendly.com) 账号，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

要获取二者，请在 Calendly 中创建新的 OAuth app：

1. 登录 Calendly developer portal，并前往 [**My apps**](https://developer.calendly.com/console/apps)。
1. 选择 **Create new app**。
1. 输入 **Name of app**，例如 `n8n integration`。
2. 在 **Kind of app** 中，选择 **Web**。
3. 在 **Environment type** 中，选择与你使用方式对应的环境，即 **Sandbox** 或 **Production**。
    - Calendly 建议开发时从 **Sandbox** 开始，并在准备上线时为 **Production** 创建第二个 application。
4. 从 n8n 复制 **OAuth Redirect URL**，并在 OAuth app 中将其输入为 **Redirect URI**。
5. 选择 **Save & Continue**。app 详情会显示出来。
5. 复制 **Client ID**，并将其输入为 n8n **Client ID**。
6. 复制 **Client secret**，并将其输入为 n8n **Client Secret**。
1. 在 n8n 中选择 **Connect my account**，并按照屏幕提示完成 credential 授权。

有关更多信息，请参阅 [Registering your application with Calendly](https://developer.calendly.com/create-a-developer-account)。

{% hint style="info" %}
**本地 OAuth2 测试**

使用 tunnel（例如 ngrok 或 Cloudflare Tunnel）测试 OAuth2 时，请通过你作为 **OAuth Redirect URL** 使用的同一个 public URL 打开 n8n。否则，OAuth callback 可能失败，因为 n8n session cookie 属于不同 host。
{% endhint %}

---
title: X (formerly Twitter) credentials
description: >-
  X credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 X 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: X (formerly Twitter) credentials
originalFilePath: integrations/builtin/credentials/twitter.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/twitter'
url: 'https://docs.n8n.io/integrations/builtin/credentials/twitter'
layout:
  description:
    visible: false
---

# X (formerly Twitter) credentials <a href="#x-formerly-twitter-credentials" id="x-formerly-twitter-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [X (formerly Twitter)](../app-nodes/n8n-nodes-base.twitter.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [X developer](https://developer.x.com/en) 账号。
- 创建一个 [Twitter app](https://developer.x.com/en/docs/apps)，或使用注册 developer portal 时默认创建的 project 和 app。有关 app 配置的更多细节，请参考下方每种支持的身份验证方式。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

{% hint style="info" %}
**弃用警告**

n8n 曾支持一种 **OAuth** 身份验证方式，该方式使用 X 的 [OAuth 1.0a](https://developer.x.com/en/docs/authentication/oauth-1-0a) 身份验证方式。n8n 在 n8n version [0.236.0](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/0.x#n8n02360) 发布 X node V2 时弃用了此方式。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [X's API documentation](https://developer.x.com/en/docs/twitter-api)。有关向该服务进行身份验证的更多信息，请参考 [X's API authentication documentation](https://developer.x.com/en/docs/authentication/overview)。

有关 app-only authentication 的更多信息，请参考 [Application-only Authentication](https://developer.twitter.com/en/docs/authentication/oauth-2-0/application-only)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

如果你使用 n8n version 0.236.0 或更高版本，请使用此方式。

要配置此 credential，你需要：

- 一个 **Client ID**
- 一个 **Client Secret**

要生成你的 Client ID 和 Client Secret：

1. 在 Twitter [developer portal](https://developer.x.com/en/portal/dashboard) 中打开你的 project。
2. 在 project 的 **Overview** tab 上，找到 **Apps** 部分并选择 **Add App**。
3. 为你的 app 指定 **Name** 并选择 **Next**。
1. 前往 **App Settings**。
4. 在 **User authentication settings** 中，选择 **Set Up**。
1. 设置 **App permissions**。如果要使用 n8n X node 的所有功能，请选择 **Read and write and Direct message**。
5. 在 **Type of app** 部分，选择 **Web App, Automated App or Bot**。
1. 在 n8n 中，复制 **OAuth Redirect URL**。
7. 在你的 X app 中，找到 **App Info** 部分，并将该 URL 粘贴为 **Callback URI / Redirect URL**。
7. 添加 **Website URL**。
8. 保存更改。
1. 复制 X 中显示的 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential 中的对应字段。

有关使用此身份验证方式的更多信息，请参考 X 的 [OAuth 2.0 Authentication documentation](https://developer.x.com/en/docs/authentication/oauth-2-0)。

{% hint style="info" %}
**X rate limits**

此 credential 使用 OAuth 2.0 Bearer Token 身份验证方式，因此你会受到 app rate limits 约束。更多信息请参考下方 [X rate limits](#x-rate-limits)。
{% endhint %}

## X rate limits <a href="#x-rate-limits" id="x-rate-limits"></a>

X 会根据你的 developer access plan level，按 endpoint 设置基于时间的 rate limits。X 会独立计算 app rate limits 和 user rate limits。有关 access plan level rate limits 以及避免触发限制的指导，请参考 [Rate limits](https://developer.x.com/en/docs/twitter-api/rate-limits)。

使用以下指导计算 rate limits：

- 如果你使用已弃用的 OAuth 方式，则适用 user rate limits。每组 users' access tokens 在每个 time window 中都有一个限制。
- 如果你正在[使用 OAuth2](#using-oauth2)，则适用 app rate limits。你的 app 发出的 requests 在每个 time window 中都有一个限制。

X 会独立计算 user rate limits 和 app rate limits。

有关这些 rate limit types 的更多信息，请参考 X 的 [Rate limits and authentication methods](https://developer.x.com/en/docs/twitter-api/rate-limits#auth)。

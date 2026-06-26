---
title: Sentry.io credentials
description: >-
  Sentry.io credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Sentry.io 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Sentry.io credentials
originalFilePath: integrations/builtin/credentials/sentryio.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/sentryio'
url: 'https://docs.n8n.io/integrations/builtin/credentials/sentryio'
layout:
  description:
    visible: false
---

# Sentry.io credentials <a href="#sentryio-credentials" id="sentryio-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Sentry.io](../app-nodes/n8n-nodes-base.sentryio.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Sentry.io](https://sentry.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2
- Server API token：用于 [self-hosted Sentry](https://develop.sentry.dev/self-hosted/)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Sentry.io's API documentation](https://docs.sentry.io/api/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 API **Token**：在 **Account > Settings > User Auth Tokens** 中生成 [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)。更多信息请参考 [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零开始配置 OAuth2，请使用以下设置[创建 integration](https://docs.sentry.io/organization/integrations/integration-platform/#creating-an-integration)：

- 复制 n8n **OAuth Callback URL**，并将其添加为 **Authorized Redirect URI**。
- 复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential 中。

有关创建 integration 的更多信息，请参考 [Public integrations](https://docs.sentry.io/organization/integrations/integration-platform/public-integration/)。

## 使用 Server API token <a href="#using-server-api-token" id="using-server-api-token"></a>

要配置此 credential，你需要：

- 一个 API **Token**：在 **Account > Settings > User Auth Tokens** 中生成 [**User Auth Token**](https://sentry.io/settings/account/api/auth-tokens/)。更多信息请参考 [User Auth Tokens](https://docs.sentry.io/account/auth-tokens/#user-auth-tokens)。
- 你的 self-hosted Sentry 实例的 **URL**。

---
title: Strava credentials
description: >-
  Strava credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Strava 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Strava credentials
originalFilePath: integrations/builtin/credentials/strava.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/strava'
url: 'https://docs.n8n.io/integrations/builtin/credentials/strava'
layout:
  description:
    visible: false
---

# Strava credentials <a href="#strava-credentials" id="strava-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Strava](../app-nodes/n8n-nodes-base.strava.md)
- [Strava Trigger](../trigger-nodes/n8n-nodes-base.stravatrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Strava](https://strava.com) 账号。
- 在 [**Settings > API**](https://www.strava.com/settings/api) 中创建一个 Strava application。更多信息请参考 [使用 OAuth2](#using-oauth2)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Strava's API documentation](https://developers.strava.com/docs/reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：在你[创建 Strava app](https://developers.strava.com/docs/getting-started/#account) 时生成。
- 一个 **Client Secret**：在你[创建 Strava app](https://developers.strava.com/docs/getting-started/#account) 时生成。

为你的 Strava app 使用以下设置：

- 在 n8n 中复制 **OAuth Callback URL**。将此 URL 粘贴到你的 Strava app 的 **Authorization Callback Domain** 中。
- 从 **Authorization Callback Domain** 中移除 protocol（`https://` 或 `http://`）和 relative URL（`/oauth2/callback` 或 `/rest/oauth2-credential/callback`）。例如，如果 OAuth Redirect URL 原本是 `https://oauth.n8n.cloud/oauth2/callback`，则 **Authorization Callback Domain** 应为 `oauth.n8n.cloud`。
- 从你的 app 复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential。

有关 Strava OAuth flow 的更多信息，请参考 [Authentication](https://developers.strava.com/docs/authentication/)。

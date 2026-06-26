---
title: Zoom credentials
description: >-
  Zoom credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zoom 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zoom credentials
originalFilePath: integrations/builtin/credentials/zoom.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zoom'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zoom'
layout:
  description:
    visible: false
---

# Zoom credentials <a href="#zoom-credentials" id="zoom-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Zoom](../app-nodes/n8n-nodes-base.zoom.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zoom](https://zoom.us/) 账号。你的账号必须拥有以下 permissions 之一：

- Account owner
- Account admin
- Zoom for developers role

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API JWT token
- OAuth2

{% hint style="warning" %}
**API JWT token 弃用**

Zoom 已在 2023 年 6 月移除对 JWT access tokens 的支持。所有新的 credentials 都必须使用 OAuth2。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zoom's API documentation](https://developers.zoom.us/docs/api/)。

## 使用 API JWT token <a href="#using-api-jwt-token" id="using-api-jwt-token"></a>

此身份验证方式已被 Zoom 完全弃用。不要使用它创建新的 credentials。

要配置此 credential，你需要：

- 一个 **JWT token**：要创建 JWT token，请在 [Zoom App Marketplace](https://marketplace.zoom.us/) 中创建新的 JWT app。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：在 Zoom App Marketplace 创建 OAuth app 时生成。
- 一个 **Client Secret**：创建 OAuth app 时生成。

要生成你的 **Client ID** 和 **Client Secret**，请[创建 OAuth app](https://developers.zoom.us/docs/integrations/create/)。

为你的 OAuth app 使用以下设置：

- 为 **Select how the app is managed** 选择 **User-managed app**。
- 从 n8n 复制 **OAuth Callback URL**，并在 Zoom 中将其输入为 **OAuth Redirect URL**。
- 如果你的 n8n credential 显示 **Whitelist URL**，也将该 URL 输入为 **OAuth Redirect URL**。
- 输入你计划使用的 scopes 对应的 **Scopes**。要使用 [Zoom](../app-nodes/n8n-nodes-base.zoom.md) node 的全部功能，请选择：
    - `meeting:read`
    - `meeting:write`
    - 有关 meeting scopes 的更多信息，请参考 [OAuth scopes | Meeting scopes](https://developers.zoom.us/docs/integrations/oauth-scopes/#meeting-scopes)。
- 复制 Zoom app 中提供的 **Client ID** 和 **Client Secret**，并将它们输入到你的 n8n credential。

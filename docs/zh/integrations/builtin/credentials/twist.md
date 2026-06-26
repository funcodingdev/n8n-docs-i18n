---
title: Twist credentials
description: >-
  Twist credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Twist 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Twist credentials
originalFilePath: integrations/builtin/credentials/twist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/twist'
url: 'https://docs.n8n.io/integrations/builtin/credentials/twist'
layout:
  description:
    visible: false
---

# Twist credentials <a href="#twist-credentials" id="twist-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Twist](../app-nodes/n8n-nodes-base.twist.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Twist](https://twist.com/) 账号。
- [创建 general integration](https://twist.com/app_console/create_app)，并配置有效的 OAuth Redirect URL。更多信息请参考 [使用 OAuth2](#using-oauth2)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关向该服务进行身份验证的更多信息，请参考 [Twist's API documentation](https://developer.twist.com/v3/#authorization)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>
要配置此 credential，你需要：

- 一个 **Client ID**：创建 general integration 后生成。
- 一个 **Client Secret**：创建 general integration 后生成。

要生成你的 Client ID 和 Client Secret，请[创建 general integration](https://twist.com/app_console/create_app)。

为你的 integration 的 **OAuth Authentication** 使用以下设置：

- 从 n8n 复制 **OAuth Redirect URL**，并将其作为 **OAuth 2 redirect URL** 输入到 Twist。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>self-hosted n8n 的 OAuth Redirect URL</strong></p><p>Twist 不接受 <code>localhost</code> Redirect URL。Redirect URL 应是你 domain 中的 URL，例如：<code>https://mytemplatemaker.example.com/gr_callback</code>。如果你的 n8n <strong>OAuth Redirect URL</strong> 包含 localhost，请参考下方 <a href="#local-environment-redirect-url">Local environment redirect URL</a>，生成 Twist 允许的 URL。</p></div>

- 选择 **Update OAuth settings** 保存这些更改。
- 从 Twist 复制 **Client ID** 和 **Client Secret**，并将它们输入到 n8n 中的相应字段。

### Local environment redirect URL <a href="#local-environment-redirect-url" id="local-environment-redirect-url"></a>

Twist 不接受 localhost callback URL。以下步骤可让你为 local environment 配置 OAuth credentials：

1. 使用 [ngrok](https://ngrok.com/) 将本地运行在 port `5678` 的 server 暴露到互联网。在 terminal 中运行以下命令：
```sh
ngrok http 5678
```
2. 在新的 terminal 中运行以下命令。将 `<YOUR-NGROK-URL>` 替换为上一步获得的 URL。
```sh
export WEBHOOK_URL=<YOUR-NGROK-URL>
```
3. 在 Twist 中将生成的 URL 用作你的 **OAuth 2 redirect URL**。

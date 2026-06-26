---
title: Zendesk credentials
description: >-
  Zendesk credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zendesk 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zendesk credentials
originalFilePath: integrations/builtin/credentials/zendesk.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zendesk'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zendesk'
layout:
  description:
    visible: false
---

# Zendesk credentials <a href="#zendesk-credentials" id="zendesk-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Zendesk](../app-nodes/n8n-nodes-base.zendesk.md)
- [Zendesk Trigger](../trigger-nodes/n8n-nodes-base.zendesktrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Zendesk](https://zendesk.com/) 账号。
- 对于 API token authentication，请在 Admin Center 的 **Apps and integrations > APIs > Zendesk APIs** 下启用 API token access。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zendesk's API documentation](https://developer.zendesk.com/api-reference/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 你的 **Subdomain**：Zendesk subdomain 是 URL 中位于 `https://` 和 `.zendesk.com` 之间的部分。例如，如果 Zendesk URL 是 `https://n8n-example.zendesk.com/agent/dashboard`，则 subdomain 是 `n8n-example`。
- 一个 **Email** address：输入用于登录 Zendesk 的 email address。
- 一个 **API Token**：在 **Apps and integrations > APIs > Zendesk API** 中生成 API token。更多信息请参考 [API token](https://developer.zendesk.com/api-reference/introduction/security-and-auth/#api-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：创建新 OAuth client 时生成。
- 一个 **Client Secret**：创建新 OAuth client 时生成。
- 你的 **Subdomain**：Zendesk subdomain 是 URL 中位于 `https://` 和 `.zendesk.com` 之间的部分。例如，如果 Zendesk URL 是 `https://n8n-example.zendesk.com/agent/dashboard`，则 subdomain 是 `n8n-example`。

要创建新的 OAuth client，请前往 **Apps and integrations > APIs > Zendesk API > OAuth Clients**。

使用以下设置：

- 从 n8n 复制 **OAuth Redirect URL**，并将其作为 **Redirect URL** 输入到 OAuth client。
- 复制 Zendesk client 的 **Unique identifier**，并将其作为 n8n **Client ID** 输入。
- 从 Zendesk 复制 **Secret**，并将其作为 n8n **Client Secret** 输入。

更多信息请参考 [Registering your application with Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845965210-Using-OAuth-authentication-with-your-application#topic_s21_lfs_qk)。

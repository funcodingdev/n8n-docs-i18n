---
title: monday.com credentials
description: >-
  monday.com credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 monday.com 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: monday.com credentials
originalFilePath: integrations/builtin/credentials/mondaycom.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mondaycom'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mondaycom'
layout:
  description:
    visible: false
---

# monday.com credentials <a href="#mondaycom-credentials" id="mondaycom-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [monday.com](../app-nodes/n8n-nodes-base.mondaycom.md)

{% hint style="info" %}
**最低版本要求**

monday.com node 需要 n8n version 1.22.6 或更高版本。
{% endhint %}

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关对该服务进行身份验证的更多信息，请参考 [monday.com's API documentation](https://developer.monday.com/api-reference/docs/basics)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要一个 [monday.com](https://monday.com/) 账号，以及：

- 一个 API **Token V2**

获取 token：

1. 在你的 monday.com account 中，选择右上角的 profile picture。
2. 选择 **Developers**。Developer Center 会在新 tab 中打开。
3. 在 Developer Center 中，选择 **My Access Tokens > Show**。
4. 复制你的 personal token，并在 n8n credential 中将其输入为 **Token V2**。

更多信息请参考 [monday.com API Authentication](https://developer.monday.com/api-reference/docs/authentication)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [monday.com](https://monday.com/) 账号，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

要生成这两个字段，请注册一个新的 monday.com application：

1. 在你的 monday.com account 中，选择右上角的 profile picture。
2. 选择 **Developers**。Developer Center 会在新 tab 中打开。
3. 在 Developer Center 中，选择 **Build app**。app details 会打开。
4. 为你的 app 输入一个 **Name**，例如 `n8n integration`。
5. 复制 **Client ID**，并将其输入到你的 n8n credential 中。
6. **Show** **Client Secret**，复制它，并将其输入到你的 n8n credential 中。
7. 在左侧菜单中，选择 **OAuth**。
8. 对于 **Scopes**，选择 `boards:write` 和 `boards:read`。
9. 选择 **Save Scopes**。
10. 选择 **Redirect URLs** tab。
11. 从 n8n 复制 **OAuth Redirect URL**，并将其输入为 **Redirect URL**。
12. 在 monday.com 中 **Save** 你的更改。
13. 在 n8n 中，选择 **Connect my account** 完成设置。

有关创建 apps 的更多信息，请参考 [Create an app](https://developer.monday.com/apps/docs/create-an-app)。

有关可用 scopes 和设置 Redirect URL 的更多信息，请参考 [OAuth and permissions](https://developer.monday.com/apps/docs/oauth)。

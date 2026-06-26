---
title: Typeform credentials
description: >-
  Typeform credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Typeform 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Typeform credentials
originalFilePath: integrations/builtin/credentials/typeform.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/typeform'
url: 'https://docs.n8n.io/integrations/builtin/credentials/typeform'
layout:
  description:
    visible: false
---

# Typeform credentials <a href="#typeform-credentials" id="typeform-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Typeform Trigger](../trigger-nodes/n8n-nodes-base.typeformtrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Typeform's API documentation](https://www.typeform.com/developers/get-started/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要一个 [Typeform](https://typeform.com/) 账号，以及：

- 一个 personal **Access Token**

要获取你的 personal access token：

1. 登录你的 Typeform account。
2. 选择右上角的 profile avatar，并前往 **Account > Your settings >** [**Personal Tokens**](https://admin.typeform.com/user/tokens)。
3. 选择 **Generate a new token**。
4. 为你的 token 指定 **Name**，例如 `n8n integration`。
5. 对于 **Scopes**，选择 **Custom scopes**。选择以下 scopes：
    - Forms: Read
    - Webhooks: Read, Write
6. 选择 **Generate token**。
7. 复制 token，并将其输入到你的 n8n credential。

更多信息请参考 Typeform 的 [Personal access token documentation](https://www.typeform.com/developers/get-started/personal-access-token/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Typeform](https://typeform.com/) 账号，以及：

- 一个 **Client ID**：注册 app 时生成。
- 一个 **Client Secret**：注册 app 时生成。

要获取你的 Client ID 和 Client Secret，请注册一个新的 Typeform app：

1. 登录你的 Typeform account。
2. 在左上角，选择你的 organization 下拉菜单，并选择 **Developer apps**。
3. 选择 **Register a new app**。
4. 输入有意义的 **App Name**，例如 `n8n OAuth2 integration`。
5. 将你的 n8n base URL 输入为 **App website**，例如 `https://n8n-sample.app.n8n.cloud/`。
6. 从 n8n 复制 **OAuth Redirect URL**。在 Typeform 中将其输入为 **Redirect URI(s)**。
7. 选择 **Register app**。
8. 复制 **Client Secret**，并将其输入到你的 n8n credential。
9. 在 Typeform 中，选择 **Got it** 关闭 Client Secret modal。
10. **Developer apps** panel 会显示你的新 app。复制 **Client ID**，并将其输入到你的 n8n credential。
10. 在 n8n 中输入 **Client ID** 和 **Client Secret** 后，选择 **Connect my account**，并按照屏幕提示完成 app 授权。

更多信息请参考 [Create applications that integrate with Typeform's APIs](https://www.typeform.com/developers/get-started/applications/#1-create-an-application-in-the-typeform-admin-panel)。

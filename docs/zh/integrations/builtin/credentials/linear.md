---
title: Linear credentials
description: >-
  Linear credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Linear 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Linear credentials
originalFilePath: integrations/builtin/credentials/linear.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/linear'
url: 'https://docs.n8n.io/integrations/builtin/credentials/linear'
layout:
  description:
    visible: false
---

# Linear credentials <a href="#linear-credentials" id="linear-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Linear Trigger](../trigger-nodes/n8n-nodes-base.lineartrigger.md)
* [Linear](../app-nodes/n8n-nodes-base.linear.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Linear](https://linear.app/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Linear's API documentation](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：


- Personal **API Key**：在你的 [**Settings** > **Security & access**](https://linear.app/n8n/settings/account/security) 中创建专用 personal API key。更多信息请参考 [Linear Personal API keys documentation](https://linear.app/developers/graphql#personal-api-keys)。


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- **Client ID**：创建新的 OAuth2 application 时生成。
- **Client Secret**：创建新的 OAuth2 application 时生成。
- 选择 **Actor**：actor 定义 OAuth2 application 应如何创建 issues、comments 和其他更改。选项包括：
    - **User**（Linear 默认值）：application 以授权用户身份创建 resources。如果你希望每个用户自行身份验证，请使用此选项。
    - **Application**：application 以自身身份创建 resources。如果只有一个用户（例如 admin）授权 application，请使用此选项。
- 要将此 credential 与 [Linear Trigger](../trigger-nodes/n8n-nodes-base.lineartrigger.md) node 一起使用，必须启用 **Include Admin Scope** toggle。

更详细说明和解释请参考 [Linear OAuth2 Authentication documentation](https://developers.linear.app/docs/oauth/authentication)。在 Linear OAuth2 application 中，将 n8n **OAuth Redirect URL** 用作 **Redirect callback URL**。

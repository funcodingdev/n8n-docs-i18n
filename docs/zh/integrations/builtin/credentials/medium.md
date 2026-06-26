---
title: Medium credentials
description: >-
  Medium credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Medium 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Medium credentials
originalFilePath: integrations/builtin/credentials/medium.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/medium'
url: 'https://docs.n8n.io/integrations/builtin/credentials/medium'
layout:
  description:
    visible: false
---

# Medium credentials <a href="#medium-credentials" id="medium-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Medium](../app-nodes/n8n-nodes-base.medium.md)

{% hint style="warning" %}
**Medium API 不再受支持**

Medium 已停止支持 Medium API。这些 credentials 仍会显示在 n8n 中，但你无法再使用它们配置新的 integrations。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 在 [Medium](https://www.medium.com/) 上创建账号。
- 对于 OAuth2，请发送 email 到 [yourfriends@medium.com](mailto:yourfriends@medium.com) 请求 credentials 访问权限。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Medium's API documentation](https://github.com/Medium/medium-api-docs)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- API **Access Token**：在 **Settings >** [**Security and apps**](https://medium.com/me/settings/security) **> Integration tokens** 中生成 token。使用它生成的 integration token 作为 n8n **Access Token**。

更多信息请参考 Medium API 的 [Self-issued access tokens documentation](https://github.com/Medium/medium-api-docs?tab=readme-ov-file#21-self-issued-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- **Client ID**
- **Client Secret**

要生成 **Client ID** 和 **Client Secret**，你需要有权访问 **Developers** 菜单。然后在其中创建新的 application 来生成 Client ID 和 Secret。

为新的 application 使用以下设置：

- 选择 **OAuth 2** 作为 **Authorization Protocol**
- 从 n8n 复制 **OAuth Callback URL**，并在 Medium 中将其用作 **Callback URL**。

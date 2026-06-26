---
title: QuickBooks credentials
description: >-
  QuickBooks credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 QuickBooks 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: QuickBooks credentials
originalFilePath: integrations/builtin/credentials/quickbooks.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/quickbooks'
url: 'https://docs.n8n.io/integrations/builtin/credentials/quickbooks'
layout:
  description:
    visible: false
---

# QuickBooks credentials <a href="#quickbooks-credentials" id="quickbooks-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [QuickBooks](../app-nodes/n8n-nodes-base.quickbooks.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Intuit developer](https://developer.intuit.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Intuit's API documentation](https://developer.intuit.com/app/developer/qbo/docs/develop)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：创建 app 时生成。
- 一个 **Client Secret**：创建 app 时生成。
- 一个 **Environment**：选择此 credential 应访问 **Production** 还是 **Sandbox** environment。

要生成你的 **Client ID** 和 **Client Secret**，请[创建一个 app](https://developer.intuit.com/app/developer/qbo/docs/get-started/start-developing-your-app#create-an-app)。

创建 app 时使用这些设置：

- 为你的 app 选择合适的 scopes。更多信息请参考 [Learn about scopes](https://developer.intuit.com/app/developer/qbo/docs/learn/scopes)。
- 在 app 的 **Development > Keys & OAuth** section 中，将 n8n 的 **OAuth Redirect URL** 输入为 **Redirect URI**。
- 从 app 的 **Development > Keys & OAuth** section 复制 **Client ID** 和 **Client Secret**，输入到 n8n 中。更多信息请参考 [Get the Client ID and Client Secret for your app](https://developer.intuit.com/app/developer/qbo/docs/get-started/get-client-id-and-client-secret)。

有关完整流程的更多信息，请参考 Intuit 的 [Set up OAuth 2.0 documentation](https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0)。

{% hint style="info" %}
**Environment selection**

如果你从头创建新 app，请先使用 **Sandbox** environment。Production apps 需要满足 Intuit 的所有要求。更多信息请参考 Intuit 的 [Publish your app documentation](https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app)。
{% endhint %}

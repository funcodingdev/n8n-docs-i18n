---
title: Facebook Lead Ads credentials
description: >-
  Facebook Lead Ads credentials 文档。使用这些 credentials 在 n8n 这个
  workflow automation platform 中验证 Facebook Lead Ads。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Facebook Lead Ads credentials
originalFilePath: integrations/builtin/credentials/facebookleadads.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/facebookleadads'
url: 'https://docs.n8n.io/integrations/builtin/credentials/facebookleadads'
layout:
  description:
    visible: false
---

# Facebook Lead Ads credentials <a href="#facebook-lead-ads-credentials" id="facebook-lead-ads-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Facebook Lead Ads trigger](../trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Facebook Lead Ads 文档](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/)。

可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/facebook-lead-ads-trigger/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

要获取二者，请[创建 Meta app](https://developers.facebook.com/docs/development/create-an-app)，并使用 Facebook Login product 或 Facebook Login for Business product。

要使用 **Facebook Login for Business** 创建 app 并设置 credential：

1. 前往 Meta Developer [App Dashboard](https://developers.facebook.com/apps)，并选择 **Create App**。
2. 如果你有 business portfolio 且准备将 app 连接到它，请选择该 business portfolio。如果没有 business portfolio，或尚未准备好连接，请选择 **I don’t want to connect a business portfolio yet**，然后选择 **Next**。会打开 **Use cases** 页面。
3. 选择 **Other**，然后选择 **Next**。
4. 选择 **Business** 和 **Next**。
5. 完成必要信息：
    * 添加 **App name**。
    * 添加 **App contact email**。
    * 这里也可以连接到 business portfolio 或跳过。
1. 选择 **Create app**。会打开 **Add products to your app** 页面。
1. 选择 **Facebook Login for Business**。该 product 的 **Settings** 页面会打开。
1. 从 n8n credential 复制 **OAuth Redirect URL**。
1. 在 Meta app settings 的 **Client OAuth settings** 中，将该 URL 粘贴为 **Valid OAuth Redirect URIs**。
1. 从左侧菜单选择 **App settings > Basic**。
1. 复制 **App ID**，并在 n8n credential 中将其输入为 **Client ID**。
1. 复制 **App Secret**，并在 n8n credential 中将其输入为 **Client Secret**。

你的 credential 现在应该能成功连接，但在使用 [Facebook Lead Ads trigger](../trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md) 前，还需要完成将 Meta app 切换为 live 的步骤。你需要做的概要如下：

1. 在 Meta app 中，从左侧菜单选择 **App settings > Basic**。
1. 输入 **Privacy Policy URL**。（将 app 切换为 "Live" 时必需。）
1. 选择 **Save changes**。
1. 在页面顶部，将 **App Mode** 从 **Development** 切换为 **Live**。
1. Facebook Login for Business 需要 `public_profile` 的 Advanced Access。要添加它，请前往 **App Review > Permissions and Features**。
1. 搜索 `public_profile` 并选择 **Request advanced access**。
1. 完成 [business verification](https://www.facebook.com/business/tools/meta-verified-for-business/) 步骤。
1. 使用 [Lead Ads Testing Tool](https://developers.facebook.com/tools/lead-ads-testing) 触发一些 demo form submissions，并测试你的 workflow。

有关创建 app、Privacy Policy URL 等必填字段以及添加 products 的更多信息，请参阅 Meta 的 [Create an app](https://developers.facebook.com/docs/development/create-an-app) 文档。

有关 app modes 以及切换到 **Live** mode 的更多信息，请参阅 [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes) 和 [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types)。

---
title: Facebook Graph API credentials
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Facebook Graph API credentials
originalFilePath: integrations/builtin/credentials/facebookgraph.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/facebookgraph
url: https://docs.n8n.io/integrations/builtin/credentials/facebookgraph
description: >-
  Facebook Graph API credentials 文档。使用这些 credentials 在 n8n 这个
  workflow automation platform 中验证 Facebook Graph API。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Facebook Graph API credentials

你可以使用这些 credentials 验证以下 nodes：

* [Facebook Graph API](../app-nodes/n8n-nodes-base.facebookgraphapi.md)

{% hint style="info" %}
**Facebook Trigger credentials**

如果你想为 [Facebook Trigger](../trigger-nodes/n8n-nodes-base.facebooktrigger/) node 创建 credentials，请按照 [Facebook App credentials](facebookapp.md) 文档中的说明操作。
{% endhint %}

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* App access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Meta Graph API 文档](https://developers.facebook.com/docs/graph-api/overview)。

## 使用 app access token <a href="#using-app-access-token" id="using-app-access-token"></a>

要配置此 credential，你需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

* app **Access Token**

设置 credential 有两个步骤：

1. 使用你需要访问的 products [创建 Meta app](facebookgraph.md#create-a-meta-app)。
2. 为该 app [生成 App Access Token](facebookgraph.md#generate-an-app-access-token)。

请参阅下方每个步骤的详细说明。

### 创建 Meta app <a href="#create-a-meta-app" id="create-a-meta-app"></a>

创建 Meta app：

1. 前往 Meta Developer [App Dashboard](https://developers.facebook.com/apps)，并选择 **Create App**。
2. 如果你有 business portfolio 且准备将 app 连接到它，请选择该 business portfolio。如果没有 business portfolio，或尚未准备好连接，请选择 **I don’t want to connect a business portfolio yet**，然后选择 **Next**。会打开 **Use cases** 页面。
3. 选择与你希望如何使用 Facebook Graph API 相匹配的 **Use case**。例如，对于 Meta **Business** suite 中的 products（如 Messenger、Instagram、WhatsApp、Marketing API、App Events、Audience Network、Commerce API、Fundraisers、Jobs、Threat Exchange 和 Webhooks），选择 **Other**，然后选择 **Next**。
4. 选择 **Business** 和 **Next**。
5. 完成必要信息：
   * 添加 **App name**。
   * 添加 **App contact email**。
   * 这里也可以连接到 business portfolio 或跳过。
6. 选择 **Create app**。
7. 会打开 **Add products to your app** 页面。
8. 从左侧菜单选择 **App settings > Basic**。
9. 输入 **Privacy Policy URL**。（将 app 切换为 "Live" 时必需。）
10. 选择 **Save changes**。
11. 在页面顶部，将 **App Mode** 从 **Development** 切换为 **Live**。
12. 在左侧菜单中选择 **Add Product**。
13. 会出现 **Add products to your app** 页面。选择适合你的 app 的 products 并进行配置。

有关创建 app、Privacy Policy URL 等必填字段以及添加 products 的更多信息，请参阅 Meta 的 [Create an app](https://developers.facebook.com/docs/development/create-an-app) 文档。

有关 app modes 以及切换到 **Live** mode 的更多信息，请参阅 [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes) 和 [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types)。

### 生成 App Access Token <a href="#generate-an-app-access-token" id="generate-an-app-access-token"></a>

接下来，创建用于 n8n credential 和你所选 products 的 app access token：

1. 在单独的标签页或窗口中，打开 [Graph API explorer](https://developers.facebook.com/tools/explorer/)。
2. 在 **Access Token** 区域中，选择你刚创建的 **Meta App**。
3. 在 **User or Page** 中，选择 **Get App Token**。
4. 选择 **Generate Access Token**。
5. 页面会提示你登录并授权。按照屏幕提示操作。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>App 不可用</strong></p><p>你可能会收到 app 不可用的警告。将 app 切换为 live 后，可能需要等待几分钟才能生成 access token。</p></div>
6. 复制 token，并在 n8n credential 中将其输入为 **Access Token**。

有关生成 token 的更多信息，请参阅 Meta 的 [Your First Request](https://developers.facebook.com/docs/graph-api/get-started#get-started) 说明。

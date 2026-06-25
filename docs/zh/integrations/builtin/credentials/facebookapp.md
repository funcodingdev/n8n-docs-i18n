---
title: Facebook App credentials
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Facebook App credentials
originalFilePath: integrations/builtin/credentials/facebookapp.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/facebookapp
url: https://docs.n8n.io/integrations/builtin/credentials/facebookapp
description: >-
  Facebook App credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Facebook App。
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

# Facebook App credentials

你可以使用这些 credentials 验证以下 nodes：

* [Facebook Trigger](../trigger-nodes/n8n-nodes-base.facebooktrigger/)

{% hint style="info" %}
**Facebook Graph API credentials**

如果你想为 [Facebook Graph API](../app-nodes/n8n-nodes-base.facebookgraphapi.md) node 创建 credentials，请按照 [Facebook Graph API credentials](facebookgraph.md) 文档中的说明操作。
{% endhint %}

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* App access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Meta Graph API 文档](https://developers.facebook.com/docs/graph-api/overview)。

## 使用 app access token <a href="#using-app-access-token" id="using-app-access-token"></a>

要配置此 credential，你需要一个 [Meta for Developers](https://developers.facebook.com/) 账号，以及：

* app **Access Token**
* 可选的 **App Secret**：用于验证 payload 的完整性和来源。

设置 credential 有五个步骤：

1. 使用 Webhooks product [创建 Meta app](facebookapp.md#create-a-meta-app)。
2. 为该 app [生成 App Access Token](facebookapp.md#generate-an-app-access-token)。
3. [配置 Facebook trigger](facebookapp.md#configure-the-facebook-trigger)。
4. 可选：[添加 app secret](facebookapp.md#optional-add-an-app-secret)。
5. [App Review](facebookapp.md#app-review)：仅当 app users 在 app 本身没有 roles 时才需要。如果你创建 app 仅供内部使用，则不需要。

请参阅下方每个步骤的详细说明。

### 创建 Meta app <a href="#create-a-meta-app" id="create-a-meta-app"></a>

创建 Meta app：

1. 前往 Meta Developer [App Dashboard](https://developers.facebook.com/apps)，并选择 **Create App**。
2. 如果你有 business portfolio 且准备将 app 连接到它，请选择该 business portfolio。如果没有 business portfolio，或尚未准备好连接，请选择 **I don’t want to connect a business portfolio yet**，然后选择 **Next**。会打开 **Use cases** 页面。
3. 选择 **Other**，然后选择 **Next**。
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
13. 会出现 **Add products to your app** 页面。选择 **Webhooks**。
14. **Webhooks** product 会打开。

有关创建 app、Privacy Policy URL 等必填字段以及添加 products 的更多信息，请参阅 Meta 的 [Create an app](https://developers.facebook.com/docs/development/create-an-app) 文档。

有关 app modes 以及切换到 **Live** mode 的更多信息，请参阅 [App Modes](https://developers.facebook.com/docs/development/build-and-test/app-modes) 和 [Publish | App Types](https://developers.facebook.com/docs/development/release#app-types)。

### 生成 App Access Token <a href="#generate-an-app-access-token" id="generate-an-app-access-token"></a>

接下来，创建供 n8n credential 和 Webhooks product 使用的 app access token：

1. 在单独的标签页或窗口中，打开 [Graph API explorer](https://developers.facebook.com/tools/explorer/)。
2. 在 **Access Token** 区域中，选择你刚创建的 **Meta App**。
3. 在 **User or Page** 中，选择 **Get App Token**。
4. 选择 **Generate Access Token**。
5. 页面会提示你登录并授权。按照屏幕提示操作。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>App 不可用</strong></p><p>你可能会收到 app 不可用的警告。将 app 切换为 live 后，可能需要等待几分钟才能生成 access token。</p></div>
6. 复制 token，并在 n8n credential 中将其输入为 **Access Token**。也请把此 token 保存到其他地方，因为 Webhooks 配置也会用到它。
7. 保存你的 n8n credential。

有关生成 token 的更多信息，请参阅 Meta 的 [Your First Request](https://developers.facebook.com/docs/graph-api/get-started#get-started) 说明。

### 配置 Facebook Trigger <a href="#configure-the-facebook-trigger" id="configure-the-facebook-trigger"></a>

现在你已有 token，可以配置 Facebook Trigger node：

1. 在 Meta app 中，从顶部导航栏复制 **App ID**。
2. 在 n8n 中，打开 Facebook Trigger node。
3. 将 **App ID** 粘贴到 **APP ID** 字段。
4. 选择 **Execute step**，将 trigger 切换到 listening mode。
5. 返回 Meta app 的 **Webhooks** product 配置所在的标签页或窗口。
6. **Subscribe** 你想接收 Facebook Trigger notifications 的 objects。对于每个 subscription：
   1. 从 n8n 复制 **Webhook URL**，并在 Meta App 中将其输入为 **Callback URL**。
   2. 将上方复制的 **Access Token** 输入为 **Verify token**。
   3. 选择 **Verify and save**。（如果 n8n trigger 没有在 listening，此步骤会失败。）
   4. 一些 webhook subscriptions（例如 **User**）会提示你订阅单独 events。订阅你感兴趣的 events。
   5. 你可以从 Meta 发送一些 **Test** events 来确认是否正常。如果发送 test event，请在 n8n 中验证是否收到。

有关更多信息，请参阅 [Facebook Trigger node](../trigger-nodes/n8n-nodes-base.facebooktrigger/) 文档。

### 可选：添加 App Secret <a href="#optional-add-an-app-secret" id="optional-add-an-app-secret"></a>

为了增强安全性，Meta 建议添加 **App Secret**。这会使用 `appsecret_proof` 参数签名所有 API calls。app secret proof 是 access token 的 sha256 hash，使用 app secret 作为 key。

生成 App Secret：

1. 在 Meta 中查看 app 时，从左侧菜单选择 **App settings > Basic**。
2. 选择 **App secret** 字段旁边的 **Show**。
3. 页面会提示你重新输入 Facebook account credentials。完成后，Meta 会显示 App Secret。
4. 选中并复制它，然后在 n8n credential 中将其粘贴为 **App Secret**。
5. **Save** 你的 n8n credential。

有关更多信息，请参阅 [App Secret 文档](https://developers.facebook.com/docs/facebook-login/security#appsecret)。

### App review <a href="#app-review" id="app-review"></a>

App Review 需要 Business Verification。

如果 app 将被以下用户使用，则必须通过 App Review：

* 在 app 本身没有 role 的用户。
* 在已认领该 app 的 Business 中没有 role 的用户。

如果你的 app users 只有在 app 本身拥有 role 的 users，则不需要 App Review。

作为 App Review 流程的一部分，你可能需要为 webhook subscriptions 请求 advanced access。

有关更多信息，请参阅 Meta 的 [App Review](https://developers.facebook.com/docs/resp-plat-initiatives/app-review) 和 [Advanced Access](https://developers.facebook.com/docs/graph-api/overview/access-levels#advanced-access) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### Unverified apps 限制 <a href="#unverified-apps-limit" id="unverified-apps-limit"></a>

Facebook 只允许你最多在 15 个尚未关联到 Meta Verified Business Account 的 apps 上拥有 developer 或 administrator role。

如果你超过该限制，请参阅 [Limitations | Create an app](https://developers.facebook.com/docs/development/create-an-app#limitations)。

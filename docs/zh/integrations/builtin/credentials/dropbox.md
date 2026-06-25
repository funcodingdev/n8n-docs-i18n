---
title: Dropbox credentials
description: >-
  Dropbox credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Dropbox。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Dropbox credentials
originalFilePath: integrations/builtin/credentials/dropbox.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/dropbox'
url: 'https://docs.n8n.io/integrations/builtin/credentials/dropbox'
layout:
  description:
    visible: false
---

# Dropbox credentials <a href="#dropbox-credentials" id="dropbox-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token：Dropbox 推荐将此方法用于通过你的 user account 进行测试，以及授予有限数量的 users 访问权限。
- OAuth2：Dropbox 推荐将此方法用于生产环境，或用于超过 50 个 users 的测试。

{% hint style="info" %}
**App 复用**

你可以通过在 n8n 中使用同一个 app 创建新的 OAuth2 credential，将 app 从 API access token 迁移到 OAuth2。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Dropbox Developer 文档](https://www.dropbox.com/developers/documentation)。

## 使用 access token <a href="#using-access-token" id="using-access-token"></a>

要配置此 credential，你需要一个 [Dropbox](https://www.dropbox.com/developers) developer 账号，以及：

- 一个 **Access Token**：创建 Dropbox app 后生成。
- 一个 **App Access Type**

要设置 credential，请创建 Dropbox app：

1. 在 Dropbox developer portal 中打开 [App Console](https://www.dropbox.com/developers/apps)。
2. 选择 **Create app**。
3. 在 **Choose an API** 中，选择 **Scoped access**。
4. 在 **Choose the type of access you need** 中，选择最符合你使用 [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md) node 的选项：
    - **App Folder** 授予对专门为你的 app 创建的单个 folder 的访问权限。
    - **Full Dropbox** 授予对你的 user Dropbox 中所有 files 和 folders 的访问权限。
    - 有关更多信息，请参阅 [DBX Platform developer guide](https://www.dropbox.com/developers/reference/developer-guide)。
5. 在 **Name your app** 中，输入 app 名称，例如 `n8n integration`。
6. 勾选复选框，同意 **Dropbox API Terms and Conditions**。
7. 选择 **Create app**。app 的 **Settings** 会打开。
8. 在 **OAuth 2** 区域中，在 **Generated access token** 中选择 **Generate**。
9. 复制 access token，并在 n8n credential 中将其输入为 **Access Token**。
10. 在 n8n 中，选择与你为 app 选择的相同 **App Access Type**。

有关更多信息，请参阅 [Dropbox App Console Settings 文档](https://www.dropbox.com/developers/reference/getting-started)。

{% hint style="warning" %}
**User 限制**

在 **Settings** 选项卡中，即使使用 access token 方法，你也可以向 app 添加其他 users。一旦 app 关联了 50 个 Dropbox users，你将有两周时间申请并获得 production status approval；否则 Dropbox 会冻结 app，阻止其关联更多 users。
{% endhint %}

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

Cloud users 需要选择 **App Access Type**：

- **App Folder** 授予对专门为你的 app 创建的单个 folder 的访问权限。
- **Full Dropbox** 授予对你的 user Dropbox 中所有 files 和 folders 的访问权限。
- 有关更多信息，请参阅 [DBX Platform developer guide](https://www.dropbox.com/developers/reference/developer-guide)。

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要手动配置 OAuth2：

1. 在 Dropbox developer portal 中打开 [App Console](https://www.dropbox.com/developers/apps)。
2. 选择 **Create app**。
3. 在 **Choose an API** 中，选择 **Scoped access**。
4. 在 **Choose the type of access you need** 中，选择最符合你使用 [Dropbox](../app-nodes/n8n-nodes-base.dropbox.md) node 的选项：
    - **App Folder** 授予对专门为你的 app 创建的单个 folder 的访问权限。
    - **Full Dropbox** 授予对你的 user Dropbox 中所有 files 和 folders 的访问权限。
    - 有关更多信息，请参阅 [DBX Platform developer guide](https://www.dropbox.com/developers/reference/developer-guide)。
5. 在 **Name your app** 中，输入 app 名称，例如 `n8n integration`。
6. 勾选复选框，同意 **Dropbox API Terms and Conditions**。
7. 选择 **Create app**。app 的 **Settings** 会打开。
8. 复制 **App key**，并在 n8n credential 中将其输入为 **Client ID**。
9. 复制 **Secret**，并在 n8n credential 中将其输入为 **Client Secret**。
10. 在 n8n 中复制 **OAuth Redirect URL**，并将其输入到 Dropbox **Redirect URIs**。
11. 在 n8n 中，选择与你为 app 选择的相同 **App Access Type**。

有关更多信息，请参阅 [Dropbox Implementing OAuth 文档](https://developers.dropbox.com/oauth-guide#implementing-oauth)中的说明。

对于 internal tools 和 limited usage，你可以保持 app private。但如果你想让 app 被超过 50 个 users 使用，或者想分发它，则需要完成 Dropbox 的 production approval process。有关更多信息，请参阅 [DBX Platform developer guide](https://www.dropbox.com/developers/reference/developer-guide) 中的 **Production Approval**。

{% hint style="warning" %}
**User 限制**

在 **Settings** 选项卡中，你可以向 app 添加其他 users。一旦 app 关联了 50 个 Dropbox users，你将有两周时间申请并获得 production status approval；否则 Dropbox 会冻结 app，阻止其关联更多 users。
{% endhint %}

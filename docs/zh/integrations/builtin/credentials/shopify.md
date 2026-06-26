---
title: Shopify credentials
description: >-
  Shopify credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Shopify 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Shopify credentials
originalFilePath: integrations/builtin/credentials/shopify.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/shopify'
url: 'https://docs.n8n.io/integrations/builtin/credentials/shopify'
layout:
  description:
    visible: false
---

# Shopify credentials <a href="#shopify-credentials" id="shopify-credentials"></a>

你可以使用这些 credentials 通过 Shopify 对以下 nodes 进行身份验证。

- [Shopify](../app-nodes/n8n-nodes-base.shopify.md)
- [Shopify Trigger](../trigger-nodes/n8n-nodes-base.shopifytrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token（推荐）：用于 private apps/单店铺使用。常规 admins 可以创建。
- OAuth2：用于 public apps。必须由 partner accounts 创建。
- API key：已弃用。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Shopify's authentication documentation](https://shopify.dev/docs/apps/auth)。

## 使用 access token <a href="#using-access-token" id="using-access-token"></a>

要配置此 credential，你需要一个 [Shopify](https://shopify.com/) admin account，以及：

- 你的 **Shop Subdomain**
- 一个 **Access Token**：创建 custom app 时生成。
- 一个 **APP Secret Key**：创建 custom app 时生成。

要设置 credential，你需要创建并安装一个 custom app：

1. 输入你的 **Shop Subdomain**。
    - 你的 subdomain 位于 URL 中：`https://<subdomain>.myshopify.com`。例如，如果完整 URL 是 `https://n8n.myshopify.com`，则 Shop Subdomain 是 `n8n`。
2. 在 Shopify 中，前往 **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps)。
3. 选择 **Develop apps**。
4. 选择 **Create a custom app**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>没有看到这个选项？</strong></p><p>如果你没有看到这个选项，你的 store 可能还没有启用 custom app development。更多信息请参考 <a href="#enable-custom-app-development">启用 custom app development</a>。</p></div>

5. 在 modal window 中，输入 **App name**。
6. 选择一个 **App developer**。app developer 可以是 store owner，也可以是任何拥有 **Develop apps** permission 的账号。
7. 选择 **Create app**。
8. 选择 **Select scopes**。在 **Admin API access scopes** 部分，选择你的 app 需要的 API scopes。
    - 要使用 [Shopify](../app-nodes/n8n-nodes-base.shopify.md) node 的全部功能，请添加 `read_orders`、`write_orders`、`read_products` 和 `write_products` scopes。
    - 有关可用 scopes 的更多信息，请参考 [Shopify API Access Scopes](https://shopify.dev/docs/api/usage/access-scopes)。
9. 选择 **Save**。
10. 选择 **Install app**。
11. 在 modal window 中，选择 **Install app**。
12. 打开 app 的 **API Credentials** 部分。
13. 复制 **Admin API Access Token**。在你的 n8n credential 中将其输入为 **Access Token**。
14. 复制 **API Secret Key**。在你的 n8n credential 中将其输入为 **APP Secret Key**。

有关这些步骤的更多信息，请参考 [Creating a custom app](https://help.shopify.com/en/manual/apps/app-types/custom-apps) 和 [Generate access tokens for custom apps in the Shopify admin](https://shopify.dev/docs/apps/build/authentication-authorization/access-token-types/generate-app-access-tokens-admin)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Shopify partner](https://www.shopify.com/partners) account，以及：

- 一个 **Client ID**：创建 custom app 时生成。
- 一个 **Client Secret**：创建 custom app 时生成。
- 你的 **Shop Subdomain**

要设置 credential，你需要创建并安装一个 custom app：

{% hint style="info" %}
**Custom app development**

Shopify 提供用于创建新 apps 的 templates。以下说明只覆盖设置 n8n credential 所必需的元素。有关构建 apps 以及使用 app templates 的更多信息，请参考 Shopify 的 [Build dev docs](https://shopify.dev/docs/apps/build)。
{% endhint %}

1. 打开你的 [Shopify Partner dashboard](https://partners.shopify.com/)。
2. 从左侧导航选择 **Apps**。
3. 选择 **Create app**。
4. 在 **Use Shopify Partners** 部分，输入 **App name**。
6. 选择 **Create app**。
7. 当 app details 打开后，复制 **Client ID**。将其输入到你的 n8n credential 中。
8. 复制 **Client Secret**。将其输入到你的 n8n credential 中。
9. 在左侧菜单中，选择 **Configuration**。
10. 在 n8n 中，复制 **OAuth Redirect URL**，并将其粘贴到 **URLs** 部分的 **Allowed redirection URL(s)** 中。
10. 在 **URLs** 部分，为你的 app 输入 **App URL**。这里输入的 host 需要与 **Allowed redirection URL(s)** 的 host 匹配，例如你的 n8n 实例的 base URL。
8. 选择 **Save and release**。
1. 从左侧菜单选择 **Overview**。此时，你可以选择将 app 安装到你的某个 store 来 **Test your app**，也可以选择 **Choose distribution** 将其公开分发。
1. 在 n8n 中，输入你安装该 app 的 store 的 **Shop Subdomain**，无论它是用于测试还是用于分发。
    - 你的 subdomain 位于 URL 中：`https://<subdomain>.myshopify.com`。例如，如果完整 URL 是 `https://n8n.myshopify.com`，则 Shop Subdomain 是 `n8n`。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

{% hint style="warning" %}
**方法已弃用**

Shopify 不再生成带 password 的 API keys。请改用 [Access token](#using-access-token) 方式。
{% endhint %}

要配置此 credential，你需要：

- 一个 **API Key**
- 一个 **Password**
- 你的 **Shop Subdomain**：你的 subdomain 位于 URL 中：`https://<subdomain>.myshopify.com`。例如，如果完整 URL 是 `https://n8n.myshopify.com`，则 Shop Subdomain 是 `n8n`。
- _可选：_ 一个 **Shared Secret**

## 常见问题 <a href="#common-issues" id="common-issues"></a>

下面列出一些设置 Shopify credential 时的常见问题，以及解决或排查步骤。

### 启用 custom app development <a href="#enable-custom-app-development" id="enable-custom-app-development"></a>

如果你没有看到 **Create a custom app** 选项，说明还没有人为你的 store 启用 custom app development。

要启用 custom app development，你必须以 store owner 身份登录，或以拥有 **Enable app development** permission 的用户身份登录：

1. 在 Shopify 中，前往 **Admin > Settings >** [**Apps and sales channels**](https://admin.shopify.com/settings/apps)。
2. 选择 **Develop apps**。
3. 选择 **Allow custom app development**。
4. 阅读 warning 和提供的信息，然后选择 **Allow custom app development**。

### Forbidden credentials error <a href="#forbidden-credentials-error" id="forbidden-credentials-error"></a>


如果你在测试 credentials 时收到 **Couldn't connect with these settings / Forbidden - perhaps check your credentials** 警告，这可能是因为 app 的 [access scope](https://shopify.dev/docs/api/usage/access-scopes) 依赖关系。例如，`read_orders` scope 也需要 `read_products` scope。请检查已分配的 scopes，以及你尝试完成的 action。

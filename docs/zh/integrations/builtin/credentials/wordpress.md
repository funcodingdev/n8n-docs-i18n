---
title: WordPress credentials
description: >-
  WordPress credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 WordPress 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: WordPress credentials
originalFilePath: integrations/builtin/credentials/wordpress.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/wordpress'
url: 'https://docs.n8n.io/integrations/builtin/credentials/wordpress'
layout:
  description:
    visible: false
---

# WordPress credentials <a href="#wordpress-credentials" id="wordpress-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [WordPress](../app-nodes/n8n-nodes-base.wordpress.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- **Basic auth**：创建一个 [WordPress](https://wordpress.com/) 账号，或在 server 上部署 WordPress。
- **OAuth2**：创建一个可访问 [developer portal](https://developer.wordpress.com/apps/) 的 [WordPress.com](https://wordpress.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [WordPress's API documentation](https://developer.wordpress.com/docs/api/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 你的 WordPress **Username**
- 一个 WordPress application **Password**
- 你的 **WordPress URL**
- 决定是否 **Ignore SSL Issues**

使用此 credential 包含三个步骤：

1. [启用 two-step authentication](#enable-two-step-authentication)。
2. [创建 application password](#create-an-application-password)。
3. [设置 credential](#set-up-the-credential)。

请参考下方每个步骤的详细说明。

### 启用 two-step authentication <a href="#enable-two-step-authentication" id="enable-two-step-authentication"></a>

要生成 application password，你必须先在 WordPress 中启用 Two-Step Authentication。如果已经完成，请[跳到下一节](#create-an-application-password)。

1. 打开你的 WordPress [profile](https://wordpress.com/me)。
2. 从左侧菜单选择 **Security**。
3. 选择 **Two-Step Authentication**。**Two-Step Authentication** 页面会打开。
4. 如果尚未启用 Two-Step Authentication，你必须启用它。
5. 选择使用 authenticator app 或 SMS codes 启用，并按照屏幕提示操作。

详细说明请参考 WordPress 的 [Enable Two-Step Authentication](https://wordpress.com/support/security/two-step-authentication/)。

### 创建 application password <a href="#create-an-application-password" id="create-an-application-password"></a>

启用 Two-Step Authentication 后，你现在可以生成 application password：

1. 从 WordPress **Security >** [**Two-Step Authentication**](https://wordpress.com/me/security/two-step) 页面，在 **Application passwords** 部分选择 **+ Add new application password**。
2. 输入 **Application name**，例如 `n8n integration`。
3. 选择 **Generate Password**。
4. 复制它生成的 password。你将在 n8n credential 中使用它。

### 设置 credential <a href="#set-up-the-credential" id="set-up-the-credential"></a>

1. 在你的 n8n credential 中输入 WordPress **Username**。
2. 将上方复制的 application password 作为 **Password** 输入到 n8n credential。
3. 将你的 WordPress site URL 输入为 **WordPress URL**。
4. 可选：使用 **Ignore SSL Issues** 选择是否希望 n8n credential 在 SSL certificate validation 失败时仍继续连接（打开），或遵守 SSL certificate validation（关闭）。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**仅限 WordPress.com**

OAuth2 authentication 仅适用于 WordPress.com-hosted sites。对于 self-hosted WordPress，请改用 basic auth。
{% endhint %}

要配置此 credential，你需要：

- 一个 **Client ID**：创建 WordPress.com developer application 时生成。
- 一个 **Client Secret**：创建 WordPress.com developer application 时生成。
- 你的 **WordPress.com Site**：你的 `.wordpress.com` subdomain 或 custom domain（例如 `myblog.wordpress.com` 或 `myblog.com`）。

创建此 credential 包含两个步骤：

1. [创建 developer application](#create-a-developer-application)。
2. [设置 OAuth2 credential](#set-up-the-oauth2-credential)。

### 创建 developer application <a href="#create-a-developer-application" id="create-a-developer-application"></a>

1. 前往你的 WordPress.com [developer applications](https://developer.wordpress.com/apps/) 页面。
2. 选择 **Create New Application**。
3. 为你的 application 输入 **Name**，例如 `n8n integration`。
4. 从 n8n 的 **OAuth2 (WordPress.com)** credential screen 复制 **OAuth Redirect URL**。将其粘贴到 WordPress 的 **Redirect URLs** 字段。
5. 根据你的 application 需要，填写 **Description**、**Website URL** 和其他字段。
6. 选择 **Create** 保存 application。
7. 返回你的 WordPress.com [developer applications](https://developer.wordpress.com/apps/) 页面，并点击刚刚创建的 integration。
8. 复制 **Client ID** 和 **Client Secret**。

### 设置 OAuth2 credential <a href="#set-up-the-oauth2-credential" id="set-up-the-oauth2-credential"></a>

1. 在 n8n **OAuth2 (WordPress.com)** credential screen 中，粘贴上一步的 **Client ID** 和 **Client Secret**。
2. 在 **WordPress.com Site** 字段中输入你的 WordPress.com site identifier，例如 `myblog.wordpress.com`。
3. 点击 **Connect to WordPress**。

更多信息请参考 WordPress 的 [OAuth2 authentication documentation](https://developer.wordpress.com/docs/oauth2/)。

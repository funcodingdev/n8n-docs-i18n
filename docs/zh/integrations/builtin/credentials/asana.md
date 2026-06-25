---
title: Asana credentials
description: >-
  Asana credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Asana。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Asana credentials
originalFilePath: integrations/builtin/credentials/asana.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/asana'
url: 'https://docs.n8n.io/integrations/builtin/credentials/asana'
layout:
  description:
    visible: false
---

# Asana credentials <a href="#asana-credentials" id="asana-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Asana](../app-nodes/n8n-nodes-base.asana.md)
- [Asana Trigger](../trigger-nodes/n8n-nodes-base.asanatrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [Asana Developer Guides](https://developers.asana.com/docs/overview)。

## 使用 Access token <a href="#using-access-token" id="using-access-token"></a>

要配置此 credential，你需要一个 [Asana](https://asana.com/) 账号，以及：

- 一个 Personal **Access Token** (PAT)

获取 PAT：

1. 打开 Asana [developer console](https://app.asana.com/0/my-apps)。
2. 在 **Personal access tokens** 区域中，选择 **Create new token**。
3. 输入 **Token name**，例如 `n8n integration`。
4. 勾选复选框，同意 **Asana API terms**。
5. 选择 **Create token**。
6. 复制 token，并在 n8n credential 中将其输入为 **Access Token**。

有关更多信息，请参阅 [Asana Quick start guide](https://developers.asana.com/docs/quick-start#setup)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Asana](https://asana.com/) 账号。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要注册一个 application 来设置 OAuth：

1. 打开 Asana [developer console](https://app.asana.com/0/my-apps)。
2. 在 **My apps** 区域中，选择 **Create new app**。
3. 为你的 application 输入 **App name**，例如 `n8n integration`。
4. 选择 app 的用途。
5. 勾选复选框，同意 **Asana API terms**。
6. 选择 **Create app**。页面会打开该 app 的 **Basic Information**。
7. 从左侧菜单选择 **OAuth**。
8. 在 n8n 中复制 **OAuth Redirect URL**。
9. 在 Asana 中，选择 **Add redirect URL** 并输入你从 n8n 复制的 URL。
7. 从 Asana 复制 **Client ID**，并将其输入到 n8n credential 中。
8. 从 Asana 复制 **Client Secret**，并将其输入到 n8n credential 中。

有关更多信息，请参阅 [Asana OAuth register an application 文档](https://developers.asana.com/docs/oauth#register-an-application)。

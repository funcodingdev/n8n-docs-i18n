---
title: Todoist credentials
description: >-
  Todoist credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Todoist 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Todoist credentials
originalFilePath: integrations/builtin/credentials/todoist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/todoist'
url: 'https://docs.n8n.io/integrations/builtin/credentials/todoist'
layout:
  description:
    visible: false
---

# Todoist credentials <a href="#todoist-credentials" id="todoist-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Todoist](../app-nodes/n8n-nodes-base.todoist.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Todoist's REST API documentation](https://developer.todoist.com/rest/v2/#overview)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Todoist](https://todoist.com/) 账号，以及：

- 一个 **API Key**

要获取你的 **API Key**：

1. 在 Todoist 中，打开你的 [**Integration settings**](https://todoist.com/prefs/integrations)。
2. 选择 **Developer** tab。
3. 复制你的 **API token**，并将其作为 **API Key** 输入到你的 n8n credential 中。

更多信息请参考 [Find your API token](https://todoist.com/help/articles/find-your-api-token-Jpzx9IIlB)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你正在 [self-hosting](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，你需要一个 [Todoist](https://todoist.com/) 账号，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

通过创建 application 获取二者：

1. 打开 Todoist [App Management Console](https://developer.todoist.com/appconsole.html)。
2. 选择 **Create a new app**。
3. 为你的 app 输入 **App name**，例如 `n8n integration`。
4. 选择 **Create app**。
5. 复制 n8n **OAuth Redirect URL**，并将其作为 **OAuth redirect URL** 输入到 Todoist。
6. 从 Todoist 复制 **Client ID**，并将其输入到你的 n8n credential。
7. 从 Todoist 复制 **Client Secret**，并将其输入到你的 n8n credential。
8. 根据你的使用场景，配置 Todoist app 的其余部分。

更多信息请参考 Todoist [Authorization Guide](https://developer.todoist.com/guides/#authorization)。

---
title: Rocket.Chat credentials
description: >-
  Rocket.Chat credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Rocket.Chat 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Rocket.Chat credentials
originalFilePath: integrations/builtin/credentials/rocketchat.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/rocketchat'
url: 'https://docs.n8n.io/integrations/builtin/credentials/rocketchat'
layout:
  description:
    visible: false
---

# Rocket.Chat credentials <a href="#rocketchat-credentials" id="rocketchat-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Rocket.Chat](../app-nodes/n8n-nodes-base.rocketchat.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Rocket.Chat](https://rocket.chat/) 账号。
- 你的 account 必须具有 `create-personal-access-tokens` permission，才能生成 personal access tokens。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Rocket.Chat's API documentation](https://developer.rocket.chat/reference/api/rest-api)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 你的 **User ID**：生成 access token 时显示。
- 一个 **Auth Key**：你的 personal access token。要生成 access token，请前往你的 **avatar > Account > Personal Access Tokens**。复制 token，并将其作为 n8n **Auth Key** 添加。
- 你的 Rocket.Chat **Domain**：也称为 default URL 或 workspace URL。

更多信息请参考 [Personal Access Tokens](https://docs.rocket.chat/docs/manage-your-account-settings#personal-access-tokens)。

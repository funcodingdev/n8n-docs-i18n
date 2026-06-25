---
title: Ghost credentials
description: >-
  Ghost credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Ghost。
contentType:
  - integration
  - reference
nodeTitle: Ghost credentials
originalFilePath: integrations/builtin/credentials/ghost.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/ghost'
url: 'https://docs.n8n.io/integrations/builtin/credentials/ghost'
layout:
  description:
    visible: false
---

# Ghost credentials <a href="#ghost-credentials" id="ghost-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Ghost](../app-nodes/n8n-nodes-base.ghost.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Ghost](https://ghost.org/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Admin API key
- Content API key

这些 keys 通过相同步骤生成，但 authorization flows 和 key format 不同，因此 n8n 会分别存储 credentials。Content API 使用 API key；Admin API 使用 API key 生成用于身份验证的 token。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 Admin API service 的更多信息，请参阅 Ghost 的 [Admin API 文档](https://ghost.org/docs/admin-api/)。有关 Content API service 的更多信息，请参阅 Ghost 的 [Content API 文档](https://ghost.org/docs/content-api/)。

## 使用 Admin API key <a href="#using-admin-api-key" id="using-admin-api-key"></a>

要配置此 credential，你需要：

- Ghost admin domain 的 **URL**。你的 [admin domain](https://ghost.org/docs/admin-api/#base-url) 可以不同于 main domain，并且可能包含 subdirectory。所有 Ghost(Pro) blogs 都有一个 `*.ghost.io` domain 作为 admin domain，并且需要 https。
- 一个 **API Key**：要生成新的 API key，请创建一个新的 Custom Integration。有关更详细的说明，请参阅 [Ghost Admin API Token Authentication Key 文档](https://ghost.org/docs/admin-api/#token-authentication)。复制 **Admin API Key**，并在 Ghost Admin n8n credential 中将其用作 **API Key**。

## 使用 Content API key <a href="#using-content-api-key" id="using-content-api-key"></a>

要配置此 credential，你需要：

- Ghost admin domain 的 **URL**。你的 [admin domain](https://ghost.org/docs/content-api/#url) 可以不同于 main domain，并且可能包含 subdirectory。所有 Ghost(Pro) blogs 都有一个 `*.ghost.io` domain 作为 admin domain，并且需要 https。
- 一个 **API Key**：要生成新的 API key，请创建一个新的 Custom Integration。有关更详细的说明，请参阅 [Ghost Content API Key 文档](https://ghost.org/docs/content-api/#key)。复制 **Content API Key**，并在 Ghost Content n8n credential 中将其用作 **API Key**。

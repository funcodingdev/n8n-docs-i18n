---
title: Gotify credentials
description: >-
  Gotify credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Gotify 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Gotify credentials
originalFilePath: integrations/builtin/credentials/gotify.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/gotify'
url: 'https://docs.n8n.io/integrations/builtin/credentials/gotify'
layout:
  description:
    visible: false
---

# Gotify credentials <a href="#gotify-credentials" id="gotify-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Gotify](../app-nodes/n8n-nodes-base.gotify.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在你的服务器上安装 [Gotify](https://gotify.net/docs/install)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Gotify's API documentation](https://gotify.net/api-docs)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- **App API Token**：仅当你要使用此 credential 创建消息时才需要。要生成 App API token，请从 **Apps** 菜单创建 application。更多信息请参考 [Gotify's Push messages documentation](https://gotify.net/docs/pushmsg)。
- **Client API Token**：创建消息以外的所有 actions 都需要，例如删除或检索消息。要生成 Client API token，请从 **Clients** 菜单创建 client。
- Gotify host 的 **URL**

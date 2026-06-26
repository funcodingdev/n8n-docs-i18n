---
title: Pushbullet credentials
description: >-
  Pushbullet credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Pushbullet 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Pushbullet credentials
originalFilePath: integrations/builtin/credentials/pushbullet.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/pushbullet'
url: 'https://docs.n8n.io/integrations/builtin/credentials/pushbullet'
layout:
  description:
    visible: false
---

# Pushbullet credentials <a href="#pushbullet-credentials" id="pushbullet-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Pushbullet](../app-nodes/n8n-nodes-base.pushbullet.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Pushbullet](https://www.pushbullet.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Pushbullet's API documentation](https://docs.pushbullet.com/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：创建 Pushbullet app（也称为 OAuth client）时生成。
- 一个 **Client Secret**：创建 Pushbullet app（也称为 OAuth client）时生成。

要生成 **Client ID** 和 **Client Secret**，请前往 [create client](https://www.pushbullet.com/create-client) page。从 n8n 复制 **OAuth Redirect URL**，并将它作为 app/client 的 **redirect_uri** 添加。在你的 n8n credential 中使用 OAuth Client 的 **client_id** 和 **client_secret**。

更多信息请参考 Pushbullet 的 [OAuth2 Guide](https://docs.pushbullet.com/#oauth2)。

{% hint style="info" %}
**Pushbullet OAuth test link**

Pushbullet 会在上面描述的 client 创建流程中提供 test link。此 link 与 n8n 不兼容。要验证身份验证是否有效，请使用 n8n 中的 **Connect my account** button。
{% endhint %}

---
title: Raindrop credentials
description: >-
  Raindrop credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Raindrop 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Raindrop credentials
originalFilePath: integrations/builtin/credentials/raindrop.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/raindrop'
url: 'https://docs.n8n.io/integrations/builtin/credentials/raindrop'
layout:
  description:
    visible: false
---

# Raindrop credentials <a href="#raindrop-credentials" id="raindrop-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Raindrop](../app-nodes/n8n-nodes-base.raindrop.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Raindrop](https://raindrop.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Raindrop's API documentation](https://developer.raindrop.io/)。

## 使用 OAuth <a href="#using-oauth" id="using-oauth"></a>

要配置此 credential，你需要：

- 一个 **Client ID**
- 一个 **Client Secret**

通过创建 Raindrop app 生成二者。

要创建 app，请前往 **Settings >** [**Integrations**](https://app.raindrop.io/settings/integrations)，并在 **For Developers** section 中选择 **+ Create new app**。

为你的 app 使用这些设置：

- 从 n8n 复制 **OAuth Redirect URL**，并将其作为 **Redirect URI** 添加到你的 app。
- 从 Raindrop app 复制 **Client ID** 和 **Client Secret**，并将它们输入到你的 n8n credential 中。

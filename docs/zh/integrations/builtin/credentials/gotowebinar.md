---
title: GoToWebinar credentials
description: >-
  GoToWebinar credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  GoToWebinar 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: GoToWebinar credentials
originalFilePath: integrations/builtin/credentials/gotowebinar.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/gotowebinar'
url: 'https://docs.n8n.io/integrations/builtin/credentials/gotowebinar'
layout:
  description:
    visible: false
---

# GoTo Webinar credentials <a href="#goto-webinar-credentials" id="goto-webinar-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [GoToWebinar](../app-nodes/n8n-nodes-base.gotowebinar.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个拥有 [Developer Center](https://developer.goto.com/) 访问权限的 [GoToWebinar](https://www.goto.com/webinar) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关如何对该服务进行身份验证的更多信息，请参考 [GoToWebinar's API documentation](https://developer.goto.com/GoToWebinarV2)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- **Client ID**：创建 OAuth client 后提供
- **Client Secret**：创建 OAuth client 后提供

创建 OAuth client 的详细说明请参考[创建 OAuth client 文档](https://developer.goto.com/guides/Get%20Started/02_HOW_createClient/)。从 n8n 复制 **OAuth Callback URL**，并在 OAuth client 中将其用作 **Redirect URI**。完成 client 设置后会提供 Client ID 和 Client secret。

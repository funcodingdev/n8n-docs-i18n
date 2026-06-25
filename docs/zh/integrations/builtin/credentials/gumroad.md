---
title: Gumroad credentials
description: >-
  Gumroad credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Gumroad 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Gumroad credentials
originalFilePath: integrations/builtin/credentials/gumroad.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/gumroad'
url: 'https://docs.n8n.io/integrations/builtin/credentials/gumroad'
layout:
  description:
    visible: false
---

# Gumroad credentials <a href="#gumroad-credentials" id="gumroad-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Gumroad Trigger](../trigger-nodes/n8n-nodes-base.gumroadtrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Gumroad](https://gumroad.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Gumroad's API documentation](https://app.gumroad.com/api)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- API **Access Token**：创建 application 以生成 access token。关于创建新 application 并生成 access token 的详细说明，请参考 [Gumroad 为 API 创建 application 文档](https://gumroad.com/help/article/280-create-application-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你是[自托管 n8n](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)，你需要：

- **OAuth Redirect URL**
- **Client ID**
- **Client Secret**

要获取这些信息，请创建一个 Gumroad application：

1. 在 Gumroad 中，进入 **Settings > Advanced**。详细说明请参考 [Gumroad 为 API 创建 application 文档](https://gumroad.com/help/article/280-create-application-api)。
2. 从你的 n8n credential 复制 **OAuth Redirect URL**，并在 Gumroad 创建 application 时将它作为 **Redirect URI** 输入。
3. 创建 application。Gumroad 会生成 **Application ID** 和 **Application Secret**。
4. 复制 **Application ID**，并将其粘贴到 n8n credential 的 **Client ID** 中。
5. 复制 **Application Secret**，并将其粘贴到 n8n credential 的 **Client Secret** 中。
6. 如需请求默认 `view_sales` 之外的 scopes，请在 n8n credential 中启用 **Custom Scopes** 并输入所需 scopes。否则保持关闭。

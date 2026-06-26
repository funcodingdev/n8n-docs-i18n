---
title: Webflow credentials
description: >-
  Webflow credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Webflow 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Webflow credentials
originalFilePath: integrations/builtin/credentials/webflow.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/webflow'
url: 'https://docs.n8n.io/integrations/builtin/credentials/webflow'
layout:
  description:
    visible: false
---

# Webflow credentials <a href="#webflow-credentials" id="webflow-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Webflow](../app-nodes/n8n-nodes-base.webflow.md)
- [Webflow Trigger](../trigger-nodes/n8n-nodes-base.webflowtrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Webflow](https://webflow.com/) 账号。
- [创建 site](https://developers.webflow.com/data/reference/structure-1#sites)：仅 API access token 身份验证需要。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Webflow's API documentation](https://developers.webflow.com/data/reference/rest-introduction)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 Site **Access Token**：Access tokens 是 site-specific 的。前往你的 site 的 **Site Settings > Apps & integrations > API access**，并选择 **Generate API token**。更多信息请参考 [Get a Site Token](https://developers.webflow.com/data/v1.0.0/docs/get-a-site-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零开始配置 OAuth2，请在你的 workspace 中[注册 application](https://developers.webflow.com/data/docs/register-an-app)。

为你的 application 使用以下设置：

- 从 n8n 复制 **OAuth callback URL**，并将其作为 **Redirect URI** 添加到你的 application 中。
- 创建 application 后，复制 **Client ID** 和 **Client Secret**，并将它们输入到你的 n8n credential。
- 如果你使用的是 Webflow Data API V1（已弃用），请启用 **Legacy** toggle。否则保持关闭。

有关 Webflow OAuth web flow 的更多信息，请参考 [OAuth](https://developers.webflow.com/data/reference/oauth-app)。

---
title: Auth0 Management credentials
description: >-
  Auth0 Management credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Auth0 Management。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Auth0 Management credentials
originalFilePath: integrations/builtin/credentials/auth0management.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/auth0management'
url: 'https://docs.n8n.io/integrations/builtin/credentials/auth0management'
layout:
  description:
    visible: false
---

# Auth0 Management credentials <a href="#auth0-management-credentials" id="auth0-management-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Auth0](https://auth0.com) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API client secret

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Auth0 Management 文档](https://auth0.com/docs/api/management/v2)。

这是一个仅 credential 的 node。请参阅 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。可在 n8n 网站查看[示例 workflows 和相关内容](https://n8n.io/integrations/auth0-management-api/)。

## 使用 API client secret <a href="#using-api-client-secret" id="using-api-client-secret"></a>

要配置此 credential，你需要：

- 一个 Auth0 **Domain**
- 一个 **Client ID**
- 一个 **Client Secret**

有关从 application 的 **Settings** 选项卡获取 Client ID 和 Client Secret 的说明，请参阅 [Auth0 Management API Get Access Tokens 文档](https://auth0.com/docs/secure/tokens/access-tokens/get-access-tokens)。

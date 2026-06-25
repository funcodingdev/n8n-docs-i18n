---
title: Bitly credentials
description: >-
  Bitly credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Bitly。
contentType:
  - integration
  - reference
nodeTitle: Bitly credentials
originalFilePath: integrations/builtin/credentials/bitly.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/bitly'
url: 'https://docs.n8n.io/integrations/builtin/credentials/bitly'
layout:
  description:
    visible: false
---

# Bitly credentials <a href="#bitly-credentials" id="bitly-credentials"></a>

你可以使用这些 credentials 验证以下 node：

- [Bitly](../app-nodes/n8n-nodes-base.bitly.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Bitly](https://www.bitly.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Bitly 的 API 文档](https://dev.bitly.com/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **Access Token**：登录后，访问 [Settings > Developer Settings > API](https://app.bitly.com/settings/api/) 生成 Access Token。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零配置 OAuth2，或需要了解 OAuth web flow 中发生的细节，请参阅 [Bitly API Authentication 文档](https://dev.bitly.com/docs/getting-started/authentication/) 获取更多信息。

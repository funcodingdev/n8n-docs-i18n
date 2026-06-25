---
title: Eventbrite credentials
description: >-
  Eventbrite credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Eventbrite。
contentType:
  - integration
  - reference
nodeTitle: Eventbrite credentials
originalFilePath: integrations/builtin/credentials/eventbrite.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/eventbrite'
url: 'https://docs.n8n.io/integrations/builtin/credentials/eventbrite'
layout:
  description:
    visible: false
---

# Eventbrite credentials <a href="#eventbrite-credentials" id="eventbrite-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Eventbrite Trigger](../trigger-nodes/n8n-nodes-base.eventbritetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Eventbrite](https://www.eventbrite.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API private key
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Eventbrite 的 API 文档](https://www.eventbrite.com/platform/api)。

## 使用 API private key <a href="#using-api-private-key" id="using-api-private-key"></a>

要配置此 credential，你需要：

- 一个 **Private Key**：有关生成 Private Token 的详细步骤，请参阅 [Eventbrite API Authentication Get a Private Token 文档](https://www.eventbrite.com/platform/api#/introduction/authentication/1.-get-a-private-token)。在 n8n credential 中将此 private token 用作 **Private Key**。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零配置 OAuth2，或需要了解 OAuth web flow 中发生的细节，请参阅 [Eventbrite API authentication For App Partners 文档](https://www.eventbrite.com/platform/api#/introduction/authentication/2.-(for-app-partners)-authorize-your-users)中的说明来设置 OAuth。

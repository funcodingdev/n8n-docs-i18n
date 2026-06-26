---
title: Postmark credentials
description: >-
  Postmark credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Postmark 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Postmark credentials
originalFilePath: integrations/builtin/credentials/postmark.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/postmark'
url: 'https://docs.n8n.io/integrations/builtin/credentials/postmark'
layout:
  description:
    visible: false
---

# Postmark credentials <a href="#postmark-credentials" id="postmark-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Postmark Trigger](../trigger-nodes/n8n-nodes-base.postmarktrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 Postmark server 上创建一个 [Postmark](https://postmarkapp.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Postmark's API documentation](https://postmarkapp.com/developer/api/overview)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **Server API Token**：Server API token 可由 Account Owners、Account Admins，以及在 server 上拥有 Server Admin privileges 的 users 访问。请从 Postmark server 下的 [**API Tokens**](https://account.postmarkapp.com/api_tokens) tab 获取。更多信息请参考 [API Authentication](https://postmarkapp.com/developer/api/overview#authentication)。

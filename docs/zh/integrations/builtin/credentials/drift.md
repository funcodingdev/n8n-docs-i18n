---
title: Drift credentials
description: >-
  Drift credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Drift。
contentType:
  - integration
  - reference
nodeTitle: Drift credentials
originalFilePath: integrations/builtin/credentials/drift.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/drift'
url: 'https://docs.n8n.io/integrations/builtin/credentials/drift'
layout:
  description:
    visible: false
---

# Drift credentials <a href="#drift-credentials" id="drift-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Drift](../app-nodes/n8n-nodes-base.drift.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Drift](https://www.drift.com/) 账号。
- [创建 Drift app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API personal access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Drift 的 API 文档](https://devdocs.drift.com/docs/using-drift-apis)。

## 使用 API personal access token <a href="#using-api-personal-access-token" id="using-api-personal-access-token"></a>

要配置此 credential，你需要：

- 一个 **Personal Access Token**：要获取 token，请[创建 Drift app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-)。[安装 app](https://devdocs.drift.com/docs/quick-start#3-install-it-to-your-drift-account-) 以生成 OAuth Access token。将其作为 **Personal Access Token** 添加到 n8n credential 中。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零配置 OAuth2，或需要了解 OAuth web flow 中发生的细节，请参阅 [Drift Authentication and Scopes 文档](https://devdocs.drift.com/docs/authentication-and-scopes)中的说明，为你的 app 设置 OAuth。

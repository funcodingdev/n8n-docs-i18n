---
title: npm credentials
description: >-
  npm credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  npm 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: npm credentials
originalFilePath: integrations/builtin/credentials/npm.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/npm'
url: 'https://docs.n8n.io/integrations/builtin/credentials/npm'
layout:
  description:
    visible: false
---

# npm credentials <a href="#npm-credentials" id="npm-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [npm](../app-nodes/n8n-nodes-base.npm.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [npm](https://www.npmjs.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [npm's external integrations documentation](https://docs.npmjs.com/integrations/integrating-npm-with-external-services)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 **Access Token**：从你的 profile menu 中选择 **Access Tokens** 来创建 access token。更详细的说明请参考 [npm's Creating and viewing access tokens documentation](https://docs.npmjs.com/creating-and-viewing-access-tokens)。
- 一个 **Registry URL**：如果你使用 custom npm registry，请将 **Registry URL** 更新为该 custom registry。否则，保留 public registry value。

---
title: Matrix credentials
description: >-
  Matrix credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Matrix 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Matrix credentials
originalFilePath: integrations/builtin/credentials/matrix.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/matrix'
url: 'https://docs.n8n.io/integrations/builtin/credentials/matrix'
layout:
  description:
    visible: false
---

# Matrix credentials <a href="#matrix-credentials" id="matrix-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Matrix](../app-nodes/n8n-nodes-base.matrix.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 [Matrix](https://matrix.org/) server 上创建账号。更多信息请参考[创建账号](https://matrix.org/docs/chat_basics/matrix-for-im/#creating-a-matrix-account)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Matrix Specification](https://spec.matrix.org/latest/)。

请参考你用于访问 Matrix server 的具体 client 的文档。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- **Access Token**：此 token 与你用于登录 Matrix 的账号绑定。
- **Homeserver URL**：这是你创建账号时输入的 [homeserver](https://matrix.org/docs/matrix-concepts/elements-of-matrix/#homeserver) URL。n8n 会预填充 matrix.org 自己的 server；如果你使用的是托管在其他位置的 server，请调整此值。

获取这些详情的说明会因你用于访问 server 的 client 而异。**Access Token** 和 **Homeserver URL** 最常见的位置是 **Settings > Help & About > Advanced**，但更多详情请参考你的 client 文档。

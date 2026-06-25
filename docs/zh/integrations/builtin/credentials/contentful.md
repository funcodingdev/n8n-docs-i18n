---
title: Contentful credentials
description: >-
  Contentful credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Contentful。
contentType:
  - integration
  - reference
nodeTitle: Contentful credentials
originalFilePath: integrations/builtin/credentials/contentful.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/contentful'
url: 'https://docs.n8n.io/integrations/builtin/credentials/contentful'
layout:
  description:
    visible: false
---

# Contentful credentials <a href="#contentful-credentials" id="contentful-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Contentful](../app-nodes/n8n-nodes-base.contentful.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Contentful](https://www.contentful.com/) 账号。
- 创建一个 [Contentful space](https://www.contentful.com/help/getting-started/contentful-101/#step-2-create-a-space)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Contentful 的 API 文档](https://www.contentful.com/developers/docs/references/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 你的 Contentful **Space ID**：Space ID 会在你生成 tokens 时显示；你也可以参阅 [Contentful Find space ID 文档](https://www.contentful.com/help/spaces/find-space-id/) 查看 Space ID。
- 一个 **Content Delivery API Access Token**：如果你想使用 [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/)，则需要此项。如果不打算使用此 API，请留空。
- 一个 **Content Preview API Access Token**：如果你想使用 [Content Preview API](https://www.contentful.com/developers/docs/references/content-preview-api/)，则需要此项。如果不打算使用此 API，请留空。

在 Contentful 的 **Settings > API keys** 中查看和生成 access tokens。Contentful 会为 Content Delivery API 和 Content Preview API 生成同一个 key 的 tokens。有关详细说明，请参阅 [Contentful API authentication 文档](https://www.contentful.com/developers/docs/references/authentication/)。

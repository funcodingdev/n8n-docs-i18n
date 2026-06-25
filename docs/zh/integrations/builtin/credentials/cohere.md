---
title: Cohere credentials
description: >-
  Cohere credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Cohere。
contentType:
  - integration
  - reference
nodeTitle: Cohere credentials
originalFilePath: integrations/builtin/credentials/cohere.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cohere'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cohere'
layout:
  description:
    visible: false
---

# Cohere credentials <a href="#cohere-credentials" id="cohere-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Cohere](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md)
* [Cohere Chat](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatcohere.md)
* [Reranker Cohere](../cluster-nodes/sub-nodes/n8n-nodes-langchain.rerankercohere.md)
* [Embeddings Cohere](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingscohere.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Cohere account](https://cohere.com/)。

你需要一个具备以下访问权限的账号：

- 对于 Trial API，你需要 User 或 Owner permissions。
- 对于 Production API，你需要 Owner permissions。

有关更多信息，请参阅 [Cohere Teams and Roles 文档](https://docs.cohere.com/reference/teams-and-roles)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cohere 的文档](https://docs.cohere.com/reference/about)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：要生成 Cohere API key，请前往 Cohere dashboard 的 [API Keys 区域](https://dashboard.cohere.com/api-keys)。

---
title: Pinecone credentials
description: >-
  Pinecone credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Pinecone 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Pinecone credentials
originalFilePath: integrations/builtin/credentials/pinecone.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/pinecone'
url: 'https://docs.n8n.io/integrations/builtin/credentials/pinecone'
layout:
  description:
    visible: false
---

# Pinecone credentials <a href="#pinecone-credentials" id="pinecone-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Pinecone Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstorepinecone.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Pinecone's documentation](https://docs.pinecone.io/reference/api/introduction)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Pinecone](https://www.pinecone.io/) 账号，以及：

- 一个 **API Key**

获取 API key：

1. 打开你的 [Pinecone console](https://app.pinecone.io/organizations/-/projects)。
2. 选择你想为其创建 API key 的 project。如果你没有任何现有 projects，请先创建一个。更多信息请参考 Pinecone 的 [Quickstart](https://docs.pinecone.io/guides/get-started/quickstart)。
3. 前往 **API Keys**。
4. 复制那里显示的 API Key，并将其输入到你的 n8n credential 中。

更多信息请参考 Pinecone API [Authentication documentation](https://docs.pinecone.io/guides/get-started/authentication)。

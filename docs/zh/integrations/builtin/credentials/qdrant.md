---
title: Qdrant credentials
description: >-
  Qdrant credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Qdrant 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Qdrant credentials
originalFilePath: integrations/builtin/credentials/qdrant.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/qdrant'
url: 'https://docs.n8n.io/integrations/builtin/credentials/qdrant'
layout:
  description:
    visible: false
---

# Qdrant credentials <a href="#qdrant-credentials" id="qdrant-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Qdrant Vector Store](../cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

更多信息请参考 [Qdrant's documentation](https://qdrant.tech/documentation/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Qdrant cluster](https://qdrant.tech/documentation/cloud/create-cluster/)，以及：

- 一个 **API Key**
- 你的 **Qdrant URL**

设置步骤：

1. 前往 [Cloud Dashboard](https://qdrant.to/cloud)。
2. 选择 **Access Management** 以显示可用 API keys（或前往 **Cluster detail** page 的 **API Keys** section）。
3. 选择 **Create**。
4. 在 dropdown 中选择你希望该 key 有权访问的 cluster。
5. 选择 **OK**。
6. 复制 API Key，并将其输入到你的 n8n credential 中。
7. 在 **Qdrant URL** 中输入你的 Qdrant cluster URL。更多信息请参考 [Qdrant Web UI](https://qdrant.tech/documentation/interfaces/web-ui/)。

有关创建和使用 API keys 的更多信息，请参考 [Qdrant's authentication documentation](https://qdrant.tech/documentation/cloud/authentication/)。

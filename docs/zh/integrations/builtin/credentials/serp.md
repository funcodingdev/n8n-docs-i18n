---
title: Serp credentials
description: >-
  Serp credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Serp 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Serp credentials
originalFilePath: integrations/builtin/credentials/serp.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/serp'
url: 'https://docs.n8n.io/integrations/builtin/credentials/serp'
layout:
  description:
    visible: false
---

# Serp credentials <a href="#serp-credentials" id="serp-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Serp](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [SerpApi](https://serpapi.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Serp's API documentation](https://serpapi.com/search-api)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

要获取你的 API key：

1. 前往 **Your Account >** [**API Key**](https://serpapi.com/manage-api-key)。
2. 复制 **Your Private API Key**，并将其作为 **API Key** 输入到你的 n8n credential 中。

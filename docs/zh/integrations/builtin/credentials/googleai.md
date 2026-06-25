---
title: Google Gemini(PaLM) credentials
description: >-
  Google Gemini(PaLM) credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Google Gemini 和 Google PaLM AI nodes 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Gemini(PaLM) credentials
originalFilePath: integrations/builtin/credentials/googleai.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/googleai'
url: 'https://docs.n8n.io/integrations/builtin/credentials/googleai'
layout:
  description:
    visible: false
---

# Google Gemini(PaLM) credentials <a href="#google-geminipalm-credentials" id="google-geminipalm-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Embeddings Google Gemini](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglegemini.md)
* [Google Gemini](../app-nodes/n8n-nodes-langchain.googlegemini.md)
* [Google Gemini Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini.md)
* [Embeddings Google PaLM](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Google Cloud](https://cloud.google.com/) 账号。
* 创建一个 [Google Cloud Platform project](https://developers.google.com/workspace/marketplace/create-gcp-project)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Gemini(PaLM) API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Google's Gemini API documentation](https://ai.google.dev/gemini-api/docs)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 Gemini(PaLM) API key <a href="#using-geminipalm-api-key" id="using-geminipalm-api-key"></a>

要配置此 credential，你需要：

- API **Host** URL：PaLM 和 Gemini 都使用默认的 `https://generativelanguage.googleapis.com`。
- **API Key**：在 [Google AI Studio](https://aistudio.google.com/apikey) 中创建 key。

{% hint style="warning" %}
**不支持自定义 hosts**

相关 nodes 尚不支持 API host 的自定义 hosts 或代理，必须使用 `https://generativelanguage.googleapis.com`。
{% endhint %}

创建 API key：

1. 前往 Google AI Studio 的 API Key 页面：[https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)。
2. 选择 **Create API Key**。
3. 你可以选择 **Create API key in new project**，也可以搜索已有 Google Cloud 项目并选择 **Create API key in existing project**。
4. 复制生成的 API key，并将它添加到你的 n8n credential。

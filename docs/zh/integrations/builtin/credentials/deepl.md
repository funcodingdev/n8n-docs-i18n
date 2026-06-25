---
title: DeepL credentials
description: >-
  DeepL credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 DeepL。
contentType:
  - integration
  - reference
nodeTitle: DeepL credentials
originalFilePath: integrations/builtin/credentials/deepl.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/deepl'
url: 'https://docs.n8n.io/integrations/builtin/credentials/deepl'
layout:
  description:
    visible: false
---

# DeepL credentials <a href="#deepl-credentials" id="deepl-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [DeepL](../app-nodes/n8n-nodes-base.deepl.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [DeepL developer](https://www.deepl.com/pro-api) 账号。n8n 同时支持 Free 和 Pro API Plans。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DeepL 的 API 文档](https://developers.deepl.com/docs)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关获取 API key 的更多信息，请参阅 [DeepL Authentication 文档](https://developers.deepl.com/docs/getting-started/auth#authentication)。
- 识别你使用的 **API Plan**。DeepL 为每个 plan 使用不同的 API endpoints，因此请确保选择正确的 plan：
    - Pro Plan
    - Free Plan

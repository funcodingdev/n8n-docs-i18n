---
title: Jina AI credentials
description: >-
  Jina AI credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Jina AI 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Jina AI credentials
originalFilePath: integrations/builtin/credentials/jinaai.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/jinaai'
url: 'https://docs.n8n.io/integrations/builtin/credentials/jinaai'
layout:
  description:
    visible: false
---

# Jina AI credentials <a href="#jina-ai-credentials" id="jina-ai-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Jina AI](../app-nodes/n8n-nodes-base.jinaai.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Jina AI's reader API documentation](https://r.jina.ai/docs) 和 [Jina AI's search API documentation](https://s.jina.ai/docs)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

* **API key**：Jina AI API key。你可以无需创建账号，通过以下步骤获取免费 API key：
	1. 访问 [Jina AI website](https://jina.ai/)。
	2. 在页面上选择 **API**。
	3. 在 API app widget 中选择 **API KEY & BILLING**。
	4. 复制标记为 "This is your unique key. Store it securely!" 的 key。

Jina AI API keys 开始时包含 1000 万个可用于非商业用途的免费 tokens。要为 key 充值或进行商业使用，请在 **API** widget 的 **API KEY & BILLING** 标签页中向下滚动，并选择最适合你需求的充值选项。

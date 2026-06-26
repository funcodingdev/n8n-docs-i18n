---
title: OpenRouter credentials
description: >-
  OpenRouter credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 OpenRouter 进行身份验证。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenRouter credentials
originalFilePath: integrations/builtin/credentials/openrouter.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/openrouter'
url: 'https://docs.n8n.io/integrations/builtin/credentials/openrouter'
layout:
  description:
    visible: false
---

# OpenRouter credentials <a href="#openrouter-credentials" id="openrouter-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Chat OpenRouter](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [OpenRouter](https://openrouter.ai/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [OpenRouter's API documentation](https://openrouter.ai/docs/quick-start)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

生成 API Key：

1. 登录你的 OpenRouter account，或[创建](https://openrouter.ai/)一个 account。
2. 打开你的 [API keys](https://openrouter.ai/keys) page。
3. 选择 **Create new secret key** 创建 API key，可选择为 key 命名。
4. 复制你的 key，并在 n8n 中将其添加为 **API Key**。

更多信息请参考 [OpenRouter Quick Start](https://openrouter.ai/docs/quick-start) page。

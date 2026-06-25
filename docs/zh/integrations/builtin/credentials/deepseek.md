---
title: DeepSeek credentials
description: >-
  DeepSeek credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Deepseek。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: DeepSeek credentials
originalFilePath: integrations/builtin/credentials/deepseek.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/deepseek'
url: 'https://docs.n8n.io/integrations/builtin/credentials/deepseek'
layout:
  description:
    visible: false
---

# DeepSeek credentials <a href="#deepseek-credentials" id="deepseek-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Chat DeepSeek](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatdeepseek.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [DeepSeek](https://platform.deepseek.com/sign_up) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DeepSeek 的 API 文档](https://api-docs.deepseek.com/api/deepseek-api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

生成 API Key：

1. 登录你的 DeepSeek 账号，或[创建](https://platform.deepseek.com/sign_up)一个账号。
2. 打开 [API keys](https://platform.deepseek.com/api_keys) 页面。
3. 选择 **Create new secret key** 创建 API key，可选择为 key 命名。
4. 复制你的 key，并在 n8n 中将其添加为 **API Key**。

有关更多信息，请参阅 [Your First API Call](https://api-docs.deepseek.com/) 页面。

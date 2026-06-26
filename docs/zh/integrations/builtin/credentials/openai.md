---
title: OpenAI credentials
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI credentials
originalFilePath: integrations/builtin/credentials/openai.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/openai
url: https://docs.n8n.io/integrations/builtin/credentials/openai
description: >-
  OpenAI credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  OpenAI 进行身份验证。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# OpenAI credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [OpenAI](../app-nodes/n8n-nodes-langchain.openai/)
* [Chat OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/)
* [Embeddings OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md)
* [LM OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [OpenAI](https://platform.openai.com/signup/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [OpenAI's API documentation](https://platform.openai.com/docs/introduction)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

* 一个 **API Key**
* 一个 **Organization ID**：如果你属于多个 organizations，则需要填写；否则留空。

生成 API Key：

1. 登录你的 OpenAI account，或[创建](https://platform.openai.com/signup/)一个 account。
2. 打开你的 [API keys](https://platform.openai.com/api-keys) page。
3. 选择 **Create new secret key** 创建 API key，可选择为 key 命名。
4. 复制你的 key，并在 n8n 中将其添加为 **API Key**。

更多信息请参考 [API Quickstart Account Setup documentation](https://platform.openai.com/docs/quickstart/account-setup)。

查找 Organization ID：

1. 前往你的 [Organization Settings](https://platform.openai.com/account/organization) page。
2. 复制你的 Organization ID，并在 n8n 中将其添加为 **Organization ID**。

更多信息请参考 [Setting up your organization](https://platform.openai.com/docs/guides/production-best-practices/setting-up-your-organization)。请注意，使用 Organization ID 发起的 API requests 会计入该 organization 的 subscription quota。

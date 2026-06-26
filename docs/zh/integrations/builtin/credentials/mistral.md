---
title: Mistral Cloud credentials
description: >-
  Mistral Cloud credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Mistral Cloud 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Mistral Cloud credentials
originalFilePath: integrations/builtin/credentials/mistral.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mistral'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mistral'
layout:
  description:
    visible: false
---

# Mistral Cloud credentials <a href="#mistral-cloud-credentials" id="mistral-cloud-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Mistral AI](../app-nodes/n8n-nodes-base.mistralai.md)
* [Mistral Cloud](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmistralcloud.md)
* [Embeddings Mistral Cloud](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Mistral](https://mistral.ai/) La Plateforme 账号。
- 你必须在 **Workspace >** [**Billing**](https://admin.mistral.ai/organization/billing) 中添加付款信息并激活付款，才能启用 API keys。更多信息请参考 [Account setup](https://docs.mistral.ai/getting-started/quickstart/#account-setup)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些 APIs 的更多信息，请参考 [Mistral's API documentation](https://docs.mistral.ai/api/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**

向你的 Mistral Cloud account 添加付款信息后：

1. 登录你的 [Mistral account](https://console.mistral.ai/home)。
2. 前往 **API Keys** 页面。
3. 选择 **Create new key**。
4. 复制 API key，并将其输入到你的 n8n credential 中。

更多信息请参考 [Account setup](https://docs.mistral.ai/getting-started/quickstart/#account-setup)。

{% hint style="info" %}
**需要付费账号**

Mistral 要求你添加付款信息并激活付款，才能使用 API keys。更多信息请参考上面的[前提条件](#prerequisites)部分。
{% endhint %}

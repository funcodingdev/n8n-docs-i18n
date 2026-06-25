---
title: Groq credentials
description: >-
  Groq credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Groq 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Groq credentials
originalFilePath: integrations/builtin/credentials/groq.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/groq'
url: 'https://docs.n8n.io/integrations/builtin/credentials/groq'
layout:
  description:
    visible: false
---

# Groq credentials <a href="#groq-credentials" id="groq-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Groq Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Groq](https://groq.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Groq's documentation](https://console.groq.com/docs/quickstart)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**

获取 API key：

1. 前往 Groq console 的 [API Keys](https://console.groq.com/keys) 页面。
2. 选择 **Create API Key**。
3. 输入 key 的 **display name**，例如 `n8n integration`，然后选择 **Submit**。
4. 复制该 key，并将它粘贴到你的 n8n credential 中。

更多信息请参考 [Groq's API Keys documentation](https://console.groq.com/docs/quickstart)。

{% hint style="info" %}
**Groq API keys**

Groq 会将 API keys 绑定到组织，而不是用户。
{% endhint %}

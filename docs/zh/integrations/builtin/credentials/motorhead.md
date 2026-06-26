---
title: Motorhead credentials
description: >-
  Motorhead credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Motorhead 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Motorhead credentials
originalFilePath: integrations/builtin/credentials/motorhead.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/motorhead'
url: 'https://docs.n8n.io/integrations/builtin/credentials/motorhead'
layout:
  description:
    visible: false
---

# Motorhead credentials <a href="#motorhead-credentials" id="motorhead-credentials"></a>

{% hint style="warning" %}
**已弃用**

Motorhead project 已不再维护。[Motorhead node](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md) 已弃用，并会在未来版本中移除。
{% endhint %}

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Motorhead](../cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Motorhead's API documentation](https://docs.getmetal.io/rest-api/introduction)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Motorhead](https://www.metal.ai/) 账号，以及：

- 你的 **Host** URL
- 一个 **API Key**
- 一个 **Client ID**

设置时，你需要生成一个 API key：

1. 如果你 self-hosting Motorhead，请更新 **Host** URL，使其与你的 Motorhead URL 匹配。
2. 在 Motorhead 中，前往 **Settings > Organization**。
3. 在 **API Keys** section 中，选择 **Create**。
4. 为你的 API Key 输入一个 **Name**，例如 `n8n integration`。
5. 选择 **Generate**。
6. 复制 **apiKey**，并将其输入到你的 n8n credential 中。
7. 返回 API key 列表。
8. 复制该 key 的 **clientID**，并在你的 n8n credential 中将其输入为 **Client ID**。

更多信息请参考 [Generate an API key](https://docs.getmetal.io/guides/misc-get-keys)。

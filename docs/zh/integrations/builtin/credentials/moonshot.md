---
title: Moonshot credentials
description: >-
  Moonshot credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Moonshot 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Moonshot credentials
originalFilePath: integrations/builtin/credentials/moonshot.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/moonshot'
url: 'https://docs.n8n.io/integrations/builtin/credentials/moonshot'
layout:
  description:
    visible: false
---

# Moonshot credentials <a href="#moonshot-credentials" id="moonshot-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Moonshot Kimi](../app-nodes/n8n-nodes-langchain.moonshot.md)
* [Moonshot Kimi Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Kimi API Platform account](https://platform.kimi.ai/)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Moonshot's documentation](https://platform.kimi.ai/docs/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [Kimi API Platform](https://platform.kimi.ai/) 账号和一个 API key：

1. 在 [Kimi API Platform console](https://platform.kimi.ai/console/api-keys) 中，选择 **API Keys**。
2. 选择 **Create API Key**。
3. 输入 API key 的 **name** 和 **project**。
4. 复制 API key，并将其输入到你的 n8n credential 中。

---
title: MiniMax credentials
description: >-
  MiniMax credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  MiniMax 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: MiniMax credentials
originalFilePath: integrations/builtin/credentials/minimax.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/minimax'
url: 'https://docs.n8n.io/integrations/builtin/credentials/minimax'
layout:
  description:
    visible: false
---

# MiniMax credentials <a href="#minimax-credentials" id="minimax-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [MiniMax](../app-nodes/n8n-nodes-langchain.minimax.md)
* [MiniMax Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [MiniMax](https://platform.minimax.io/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [MiniMax's API documentation](https://platform.minimax.io/docs/guides/models-intro)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Region**：根据你的 MiniMax account 选择 **International** 或 **China**。
- 一个 **API Key**

获取 API key：

1. 登录你的 [MiniMax account](https://platform.minimax.io/)。
2. 前往 **Account** > **API Keys**。
3. 选择 **Create API Key**。
4. 复制 key，并将其输入到你的 n8n credential 中。

---
title: Lemonade credentials
description: >-
  Lemonade credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Lemonade 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Lemonade credentials
originalFilePath: integrations/builtin/credentials/lemonade.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/lemonade'
url: 'https://docs.n8n.io/integrations/builtin/credentials/lemonade'
layout:
  description:
    visible: false
---
# Lemonade credentials <a href="#lemonade-credentials" id="lemonade-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Lemonade Chat Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md)
* [Lemonade Model](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md)
* [Embeddings Lemonade](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingslemonade.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

Lemonade 在本地运行 AI inference。这些 nodes 会直接连接到在你的机器或网络中运行的 Lemonade server process。请先[安装并运行 Lemonade server](https://lemonade-server.ai/install_options.html)，再在 n8n 中创建 credentials。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Lemonade server connection

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Lemonade's documentation](https://lemonade-server.ai/docs/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 配置 Lemonade server connection <a href="#configuring-lemonade-server-connection" id="configuring-lemonade-server-connection"></a>

要配置此 credential，你需要：

- **Base URL**：你的 Lemonade server URL，包括 API path。本地安装的默认值是 `http://localhost:8000/api/v1`。如果你在 Docker 中运行 n8n，请改用 `http://host.docker.internal:8000/api/v1`。如果 Lemonade server 位于远程机器，请将 `localhost` 替换为 server address。
- **API key**（可选）：用于 Lemonade server authentication 的可选 API key。默认 Lemonade installation 不需要此项。

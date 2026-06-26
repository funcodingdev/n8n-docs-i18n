---
title: Ollama credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Ollama credentials
originalFilePath: integrations/builtin/credentials/ollama.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/ollama
url: https://docs.n8n.io/integrations/builtin/credentials/ollama
description: >-
  Ollama credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Ollama 进行身份验证。
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

# Ollama credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Ollama](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/)
* [Chat Ollama](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/)
* [Embeddings Ollama](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsollama.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建并运行一个带一个 user 的 [Ollama](https://ollama.com/) instance。更多信息请参考 Ollama [Quick Start](https://github.com/ollama/ollama/blob/main/README.md#quickstart)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Instance URL

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Ollama's API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 使用 instance URL <a href="#using-instance-url" id="using-instance-url"></a>

要配置此 credential，你需要：

* 你的 Ollama instance 或 remote authenticated Ollama instances 的 **Base URL**。
* （可选）如果连接到 remote authenticated proxy，则需要用于 Bearer token authentication 的 **API Key**。

默认 **Base URL** 是 `http://localhost:11434`，但如果你已设置 `OLLAMA_HOST` environment variable，请输入该值。如果连接到本地 n8n server 时遇到问题，请尝试使用 `127.0.0.1` 而不是 `localhost`。

如果你通过 authenticated proxy services（例如 [Open WebUI](https://docs.openwebui.com/getting-started/api-endpoints/#-ollama-api-proxy-support)）连接到 Ollama，则必须包含 API key。如果不需要身份验证，请将此字段留空。提供 API key 时，它会作为 Bearer token 发送到 Ollama API request 的 `Authorization` header 中。

更多信息请参考 [How do I configure Ollama server?](https://github.com/ollama/ollama/blob/main/docs/faq.mdx#how-do-i-configure-ollama-server)。

### Ollama 和 self-hosted n8n <a href="#ollama-and-self-hosted-n8n" id="ollama-and-self-hosted-n8n"></a>

如果你在同一台机器上 self-hosting n8n 和 Ollama，但它们运行在不同 containers 中，可能会遇到连接问题。

对于这种设置，请通过设置 `OLLAMA_ORIGINS` variable 或将 `OLLAMA_HOST` 调整为另一个 container 可访问的 address，为 n8n 打开一个特定 port 以便与 Ollama 通信。

更多信息请参考 Ollama 的 [How can I allow additional web origins to access Ollama?](https://docs.ollama.com/faq#how-can-i-allow-additional-web-origins-to-access-ollama)。

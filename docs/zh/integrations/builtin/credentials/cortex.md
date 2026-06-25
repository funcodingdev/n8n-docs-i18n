---
title: Cortex credentials
description: >-
  Cortex credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Cortex。
contentType:
  - integration
  - reference
nodeTitle: Cortex credentials
originalFilePath: integrations/builtin/credentials/cortex.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cortex'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cortex'
layout:
  description:
    visible: false
---

# Cortex credentials <a href="#cortex-credentials" id="cortex-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Cortex](../app-nodes/n8n-nodes-base.cortex.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

在你的 server 上安装 [Cortex](https://docs.strangebee.com/cortex/installation-and-configuration/)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cortex 的 API 文档](https://docs.strangebee.com/cortex/api/api-guide/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关生成 API keys 的详细说明，请参阅 [Cortex API Authentication 文档](https://docs.strangebee.com/cortex/api/api-guide/#authentication)。
- 你的 **Cortex Instance** 的 URL/Server Address（默认为 `http://<your_server_address>:9001/`）

---
title: Freshservice credentials
description: >-
  Freshservice credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Freshservice。
contentType:
  - integration
  - reference
nodeTitle: Freshservice credentials
originalFilePath: integrations/builtin/credentials/freshservice.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/freshservice'
url: 'https://docs.n8n.io/integrations/builtin/credentials/freshservice'
layout:
  description:
    visible: false
---

# Freshservice credentials <a href="#freshservice-credentials" id="freshservice-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Freshservice](../app-nodes/n8n-nodes-base.freshservice.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Freshservice](https://freshservice.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Freshservice 的 API 文档](https://api.freshservice.com/v2/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关获取 API key 的详细说明，请参阅 [Freshservice API authentication 文档](https://api.freshservice.com/v2/#authentication)。
- 你的 Freshservice **Domain**：使用 Freshservice 账号的 subdomain。这是 URL 的一部分，例如 `https://<subdomain>.freshservice.com`。因此，如果你通过 `https://n8n.freshservice.com` 访问 Freshservice，请输入 `n8n` 作为 **Domain**。

---
title: Freshdesk credentials
description: >-
  Freshdesk credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Freshdesk。
contentType:
  - integration
  - reference
nodeTitle: Freshdesk credentials
originalFilePath: integrations/builtin/credentials/freshdesk.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/freshdesk'
url: 'https://docs.n8n.io/integrations/builtin/credentials/freshdesk'
layout:
  description:
    visible: false
---

# Freshdesk credentials <a href="#freshdesk-credentials" id="freshdesk-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Freshdesk](../app-nodes/n8n-nodes-base.freshdesk.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Freshdesk](https://freshdesk.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Freshdesk 的 API 文档](https://developers.freshdesk.com/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关获取 API key 的详细说明，请参阅 [Freshdesk API authentication 文档](https://developers.freshdesk.com/api/#authentication)。
- Freshdesk **Domain**：使用 Freshdesk 账号的 subdomain。这是 URL 的一部分，例如 `https://<subdomain>.freshdesk.com`。因此，如果你通过 `https://n8n.freshdesk.com` 访问 Freshdesk，请输入 `n8n` 作为 **Domain**。

---
title: Freshworks CRM credentials
description: >-
  Freshworks CRM credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Freshworks CRM。
contentType:
  - integration
  - reference
nodeTitle: Freshworks CRM credentials
originalFilePath: integrations/builtin/credentials/freshworkscrm.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/freshworkscrm'
url: 'https://docs.n8n.io/integrations/builtin/credentials/freshworkscrm'
layout:
  description:
    visible: false
---

# Freshworks CRM credentials <a href="#freshworks-crm-credentials" id="freshworks-crm-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Freshworks CRM](../app-nodes/n8n-nodes-base.freshworkscrm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Freshworks CRM](https://www.freshworks.com/freshsales-crm/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Freshworks CRM 的 API 文档](https://developers.freshworks.com/crm/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关获取 API key 的详细说明，请参阅 [Freshworks CRM API authentication 文档](https://developers.freshworks.com/crm/api/#authentication)。
- 你的 Freshworks CRM **Domain**：使用 Freshworks CRM 账号的 subdomain。这是 URL 的一部分，例如 `https://<subdomain>.myfreshworks.com`。因此，如果你通过 `https://n8n.myfreshworks.com` 访问 Freshworks CRM，请输入 `n8n` 作为 **Domain**。

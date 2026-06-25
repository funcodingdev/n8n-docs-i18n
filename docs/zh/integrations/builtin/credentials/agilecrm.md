---
title: Agile CRM credentials
description: >-
  Agile CRM credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Agile CRM。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Agile CRM credentials
originalFilePath: integrations/builtin/credentials/agilecrm.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/agilecrm'
url: 'https://docs.n8n.io/integrations/builtin/credentials/agilecrm'
layout:
  description:
    visible: false
---

# Agile CRM credentials <a href="#agile-crm-credentials" id="agile-crm-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Agile CRM](../app-nodes/n8n-nodes-base.agilecrm.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Agile CRM](https://www.agilecrm.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用该服务的更多信息，请参阅 [Agile CRM API 文档](https://www.agilecrm.com/api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 在 AgileCRM 注册的 **Email Address**
- REST **API Key**：通过 **Admin Settings > Developers & API >** [**REST API key**](https://github.com/agilecrm/rest-api?tab=readme-ov-file#api-key) 访问你的 Agile CRM API key。
- Agile CRM **Subdomain**（例如 `n8n`）

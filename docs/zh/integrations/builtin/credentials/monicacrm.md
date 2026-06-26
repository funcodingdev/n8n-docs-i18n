---
title: Monica CRM credentials
description: >-
  Monica CRM credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Monica CRM 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Monica CRM credentials
originalFilePath: integrations/builtin/credentials/monicacrm.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/monicacrm'
url: 'https://docs.n8n.io/integrations/builtin/credentials/monicacrm'
layout:
  description:
    visible: false
---

# Monica CRM credentials <a href="#monica-crm-credentials" id="monica-crm-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Monica CRM](../app-nodes/n8n-nodes-base.monicacrm.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

注册一个 [Monica CRM](https://www.monicahq.com/) 账号，或 self-host 一个 instance。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Monica's API documentation](https://www.monicahq.com/api)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 你的 **Environment**：
    - 如果你通过 Monica 访问 Monica instance，请选择 **Cloud-Hosted**。
    - 如果你已在自己的 server 上 self-hosted Monica，请选择 **Self-Hosted**。请提供你的 **Self-Hosted Domain**。
- 一个 **API Token**：在 **Settings > API** 中生成 token。

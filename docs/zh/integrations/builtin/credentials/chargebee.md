---
title: Chargebee credentials
description: >-
  Chargebee credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Chargebee。
contentType:
  - integration
  - reference
nodeTitle: Chargebee credentials
originalFilePath: integrations/builtin/credentials/chargebee.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/chargebee'
url: 'https://docs.n8n.io/integrations/builtin/credentials/chargebee'
layout:
  description:
    visible: false
---

# Chargebee credentials <a href="#chargebee-credentials" id="chargebee-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Chargebee](../app-nodes/n8n-nodes-base.chargebee.md)
- [Chargebee Trigger](../trigger-nodes/n8n-nodes-base.chargebeetrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Chargebee](https://www.chargebee.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Chargebee 的 API 文档](https://apidocs.chargebee.com/docs/api/)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Account Name**：这是你的 Chargebee Site Name 或 subdomain。例如，如果 `https://n8n.chargebee.com` 是完整 site name，则 Account Name 是 `n8n`。
- 一个 **API Key**：有关如何生成 API key 的步骤，请参阅 [Chargebee Creating an API key 文档](https://www.chargebee.com/docs/api_keys.html#creating-an-api-key)。

有关进一步说明，请参阅其更通用的 [API authentication 文档](https://apidocs.chargebee.com/docs/api/auth?lang=curl)。

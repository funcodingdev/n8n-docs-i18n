---
title: ConvertKit credentials
description: >-
  ConvertKit credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 ConvertKit。
contentType:
  - integration
  - reference
nodeTitle: ConvertKit credentials
originalFilePath: integrations/builtin/credentials/convertkit.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/convertkit'
url: 'https://docs.n8n.io/integrations/builtin/credentials/convertkit'
layout:
  description:
    visible: false
---

# ConvertKit credentials <a href="#convertkit-credentials" id="convertkit-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [ConvertKit](../app-nodes/n8n-nodes-base.convertkit.md)
- [ConvertKit Trigger](../trigger-nodes/n8n-nodes-base.convertkittrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [ConvertKit](https://convertkit.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ConvertKit 的 API 文档](https://developers.convertkit.com/#overview)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Secret**：在 [**Account Settings > Advanced**](https://app.convertkit.com/account_settings/advanced_settings) 中访问你的 ConvertKit API key。在 n8n 中将此 key 添加为 **API Secret**。

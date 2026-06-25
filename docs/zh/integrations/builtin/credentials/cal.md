---
title: Cal.com credentials
description: >-
  Cal.com credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Cal.com。
contentType:
  - integration
  - reference
nodeTitle: Cal.com credentials
originalFilePath: integrations/builtin/credentials/cal.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/cal'
url: 'https://docs.n8n.io/integrations/builtin/credentials/cal'
layout:
  description:
    visible: false
---

# Cal.com credentials <a href="#calcom-credentials" id="calcom-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Cal.com Trigger](../trigger-nodes/n8n-nodes-base.caltrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Cal.com](https://www.cal.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Cal.com 的 API 文档](https://cal.com/docs/enterprise-features/api#api-server-specifications)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：有关如何生成新 API key 的信息，请参阅 [Cal API Quick Start 文档](https://cal.com/docs/enterprise-features/api/quick-start)。
- 一个 **Host**：如果你使用 Cal.com 的 cloud version，请将 Host 保留为 `https://api.cal.com`。如果你 self-host Cal.com，请输入你的 Cal.com instance 的 **Host**。

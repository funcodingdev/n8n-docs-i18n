---
title: Onfleet credentials
description: >-
  Onfleet credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Onfleet 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Onfleet credentials
originalFilePath: integrations/builtin/credentials/onfleet.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/onfleet'
url: 'https://docs.n8n.io/integrations/builtin/credentials/onfleet'
layout:
  description:
    visible: false
---

# Onfleet credentials <a href="#onfleet-credentials" id="onfleet-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Onfleet](../app-nodes/n8n-nodes-base.onfleet.md)
- [Onfleet Trigger](../trigger-nodes/n8n-nodes-base.onfleettrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Onfleet](https://onfleet.com/) administrator account。

# 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Onfleet's API documentation](https://docs.onfleet.com/reference/introduction)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API key**：要创建 API key，请登录你的 organization administrator account。选择 **Settings > API & Webhooks**，然后选择 **+** 创建一个新的 key。更多信息请参考 Onfleet 的 [Creating an API key documentation](https://support.onfleet.com/hc/en-us/articles/360045763292-API)。

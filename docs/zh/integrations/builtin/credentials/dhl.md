---
title: DHL credentials
description: >-
  DHL credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 DHL。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: DHL credentials
originalFilePath: integrations/builtin/credentials/dhl.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/dhl'
url: 'https://docs.n8n.io/integrations/builtin/credentials/dhl'
layout:
  description:
    visible: false
---

# DHL credentials <a href="#dhl-credentials" id="dhl-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [DHL](../app-nodes/n8n-nodes-base.dhl.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [DHL Developer 文档](https://support-developer.dhl.com/support/home)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要一个 [DHL Developer](https://developer.dhl.com/user/register) 账号，以及：

- 一个 **API Key**

要获取 API key，请创建一个 app：

1. 在 DHL Developer portal 中，选择 user 图标打开你的 [User Apps](https://developer.dhl.com/user/apps)。
2. 选择 **+ Create App**。
3. 输入 **App name**，例如 `n8n integration`。
4. 输入 **Machine name**，例如 `n8n_integration`。
4. 在 **SELECT APIs** 中，选择 **Shipment Tracking - Unified**。该 API 会添加到 **Add API to app** 区域。
5. 在 **Add API to app** 区域中，选择 **Shipment Tracking - Unified** API 旁边的 **+**。
6. 选择 **Create App**。**Apps** 页面会打开，并显示你刚创建的 app。
7. 选择刚创建的 app 查看其详情。
8. 选择 **API Key** 旁边的 **Show key**。
9. 复制 **API Key**，并将其输入到 n8n credential 中。

有关更多信息，请参阅 [How to create an app?](https://support-developer.dhl.com/support/solutions/articles/47001177011-how-to-create-an-app-)。

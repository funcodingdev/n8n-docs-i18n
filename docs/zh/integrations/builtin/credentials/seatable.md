---
title: SeaTable credentials
description: >-
  SeaTable credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 SeaTable 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: SeaTable credentials
originalFilePath: integrations/builtin/credentials/seatable.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/seatable'
url: 'https://docs.n8n.io/integrations/builtin/credentials/seatable'
layout:
  description:
    visible: false
---

# SeaTable credentials <a href="#seatable-credentials" id="seatable-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [SeaTable](../app-nodes/n8n-nodes-base.seatable.md)
- [SeaTable Trigger](../trigger-nodes/n8n-nodes-base.seatabletrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

在 cloud 或 self-hosted SeaTable server 上创建一个 [SeaTable](https://seatable.io/en/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [SeaTable's API documentation](https://api.seatable.io)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **Environment**：选择与你的 SeaTable 实例匹配的环境：
    - **Cloud-Hosted**
    - **Self-Hosted**
- 一个 **API Token (of a Base)**：在 SeaTable 中从 base options > **Advanced > API Token** 生成 **Base-Token**。
    - 为你的 token 使用 **Read-Write** permission。
    - 更多信息请参考 [Creating an API token](https://seatable.io/en/docs/seatable-api/erzeugen-eines-api-tokens/)。
- 一个 **Timezone**：选择你的 SeaTable server 所在时区。

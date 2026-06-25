---
title: Autopilot credentials
description: >-
  Autopilot credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Autopilot。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Autopilot credentials
originalFilePath: integrations/builtin/credentials/autopilot.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/autopilot'
url: 'https://docs.n8n.io/integrations/builtin/credentials/autopilot'
layout:
  description:
    visible: false
---

# Autopilot credentials <a href="#autopilot-credentials" id="autopilot-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Autopilot](../app-nodes/n8n-nodes-base.autopilot.md)
- [Autopilot Trigger](../trigger-nodes/n8n-nodes-base.autopilottrigger.md)

{% hint style="warning" %}
**Autopilot 品牌变更**

Autopilot 已变为 Ortto。Autopilot credentials 和 nodes 仅兼容 Autopilot，不兼容新的 Ortto API。
{% endhint %}

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Autopilot](https://app.autopilothq.com) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Autopilot 的 API 文档](https://autopilot.docs.apiary.io/#)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- 一个 **API Key**：在 **Settings > Autopilot API** 中生成 API key。有关更多信息，请参阅 [Autopilot API authentication](https://autopilot.docs.apiary.io/#reference/authentication)。

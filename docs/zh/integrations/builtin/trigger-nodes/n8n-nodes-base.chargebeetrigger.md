---
title: Chargebee Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Chargebee Trigger node。按照技术文档将 Chargebee Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Chargebee Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.chargebeetrigger
layout:
  description:
    visible: false
---

# Chargebee Trigger node <a href="#chargebee-trigger-node" id="chargebee-trigger-node"></a>

[Chargebee](https://www.chargebee.com/) 是面向基于订阅的 SaaS 和电商企业的计费平台。Chargebee 与支付网关集成，让你可以自动化定期收款，并处理发票、税务、会计、email 通知、SaaS Metrics 和客户管理。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/chargebee.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Chargebee Trigger integrations](https://n8n.io/integrations/chargebee-trigger/) 页面。
{% endhint %}

## 在 Chargebee 中添加 webhook URL <a href="#add-webhook-url-in-chargebee" id="add-webhook-url-in-chargebee"></a>

要在 Chargebee 中添加 Webhook URL：

1. 打开你的 Chargebee dashboard。
2. 前往 **Settings** > **Configure Chargebee**。
4. 向下滚动并选择 **Webhooks**。
5. 选择 **Add Webhook** 按钮。
6. 输入 **Webhook Name** 和 **Webhook URL**。
7. 选择 **创建**。

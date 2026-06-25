---
title: Wise Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Wise Trigger node。按照技术文档将 Wise Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Wise Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.wisetrigger
layout:
  description:
    visible: false
---

# Wise Trigger node <a href="#wise-trigger-node" id="wise-trigger-node"></a>

[Wise](https://wise.com) 可让你以低成本向海外转账、通过国际账户详情收款，并在手机上跟踪交易。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/wise.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Wise Trigger integrations](https://n8n.io/integrations/wise-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

- 每当 balance account 入账时触发
- 每当 balance account 入账或出账时触发
- 每当 transfer 的 active cases 列表更新时触发
- 每当 transfer 状态更新时触发

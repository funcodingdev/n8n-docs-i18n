---
title: Customer.io Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Customer.io Trigger node。按照技术文档将 Customer.io Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Customer.io Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.customeriotrigger
layout:
  description:
    visible: false
---

# Customer.io Trigger node <a href="#customerio-trigger-node" id="customerio-trigger-node"></a>

[Customer.io](https://customer.io/) 允许用户使用网站数据向选定客户 segment 发送 newsletter。你可以发送定向 email、push notification 和 SMS，以降低流失、建立更强关系并推动订阅。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/customerio.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Customer.io Trigger integrations](https://n8n.io/integrations/customerio-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 客户
    * 已订阅
    * 取消订阅
* Email
    * 已退信
    * 已点击
    * 已转化
    * 已送达
    * 已起草
    * 失败
    * 已打开
    * 已发送
    * 已标记为 spam
* Push
    * 已尝试
    * 已退信
    * 已点击
    * 已送达
    * 已起草
    * 失败
    * 已打开
    * 已发送
* Slack
    * 已尝试
    * 已点击
    * 已起草
    * 失败
    * 已发送
* SMS
    * 已尝试
    * 已退信
    * 已点击
    * 已送达
    * 已起草
    * 失败
    * 已发送

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Customer.io 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.customerio.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/customerio-trigger/)。

有关其 API 的详细信息，请参阅 [Customer.io 的文档](https://docs.customer.io/api/)。

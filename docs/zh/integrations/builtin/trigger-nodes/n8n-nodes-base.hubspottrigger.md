---
title: HubSpot Trigger node 文档
description: >-
  了解如何在 n8n 中使用 HubSpot Trigger node。按照技术文档将 HubSpot Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: HubSpot Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.hubspottrigger
layout:
  description:
    visible: false
---

# HubSpot Trigger node <a href="#hubspot-trigger-node" id="hubspot-trigger-node"></a>

[HubSpot](https://www.hubspot.com/) 提供社交媒体营销、内容管理、网页分析、landing page、客户支持和搜索引擎优化工具。

{% hint style="warning" %}
**Webhooks 限制**

如果你激活第二个 trigger，前一个 trigger 会停止工作。这是因为 trigger 激活时会向 HubSpot 注册新的 webhook。HubSpot 一次只允许一个 webhook。
{% endhint %}

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/hubspot.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [HubSpot Trigger integrations](https://n8n.io/integrations/hubspot-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 公司
	* 已创建
	* 已删除
	* 属性已更改
* 联系人
	* 已创建
	* 已删除
	* 隐私删除
	* 属性已更改
* 对话
	* 已创建
	* 已删除
	* 新消息
	* 隐私删除
	* 属性已更改
* 交易
	* 已创建
	* 已删除
	* 属性已更改
* 工单
	* 已创建
	* 已删除
	* 属性已更改

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 HubSpot 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.hubspot.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/hubspot-trigger/)。

有关其 API 的详细信息，请参阅 [HubSpot 的文档](https://developers.hubspot.com/docs/api/overview)。

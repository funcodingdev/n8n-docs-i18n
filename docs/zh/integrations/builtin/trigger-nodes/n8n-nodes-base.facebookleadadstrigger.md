---
title: Facebook Lead Ads Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Facebook Lead Ads Trigger node。按照技术文档将 Facebook Lead Ads Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Facebook Lead Ads Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.facebookleadadstrigger
layout:
  description:
    visible: false
---

# Facebook Lead Ads Trigger node <a href="#facebook-lead-ads-trigger-node" id="facebook-lead-ads-trigger-node"></a>

使用 Facebook Lead Ads Trigger node 响应 [Facebook Lead Ads](https://www.facebook.com/business/ads/lead-ads/) 中的事件，并将 Facebook Lead Ads 与其他应用集成。n8n 内置支持响应新的 lead。

在本页中，你可以找到 Facebook Lead Ads Trigger node 可以响应的事件列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/facebookleadads.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Facebook Lead Ads Trigger integrations](https://n8n.io/integrations/facebook-lead-ads-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 新 lead

## 相关资源 <a href="#related-resources" id="related-resources"></a>

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/facebook-lead-ads-trigger/)。

有关其 API 的详细信息，请参阅 [Facebook Lead Ads 的文档](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Facebook Lead Ads Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### Workflow 只能在测试或生产中二选一工作 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

Facebook Lead Ads 只允许你为每个 app 注册一个 webhook。这意味着每次你从测试 URL 切换到生产 URL（反之亦然）时，Facebook Lead Ads 都会覆盖已注册的 webhook URL。

如果你尝试测试一个同时在生产中启用的 workflow，可能会遇到此问题。Facebook Lead Ads 只会向两个 webhook URL 中的一个发送事件，因此另一个永远不会收到事件通知。

要绕过此问题，可以在测试时停用 workflow：

{% hint style="warning" %}
**会停止生产流量**

此 workaround 会在测试期间临时停用你的生产 workflow。停用期间，你的 workflow 将不再接收生产流量。
{% endhint %}

1. 前往你的 workflow 页面。
2. 从 workflow 设置下拉菜单中点击 **取消发布**，临时停用 workflow。
3. 使用测试 webhook URL 测试 workflow。
4. 测试完成后，点击 **发布**。生产 webhook URL 应恢复工作。

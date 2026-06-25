---
title: WhatsApp Trigger node 文档
contentType:
  - integration
  - reference
priority: high
nodeTitle: WhatsApp Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger
description: >-
  了解如何在 n8n 中使用 WhatsApp Trigger node。按照技术文档将 WhatsApp
  Trigger node 集成到你的 workflow 中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# WhatsApp Trigger

使用 WhatsApp Trigger node 响应 WhatsApp 中的事件，并将 WhatsApp 与其他应用程序集成。n8n 内置支持多种 WhatsApp 事件，包括 account、message 和 phone number 事件。

在本页中，你可以找到 WhatsApp Trigger node 可响应的事件列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/whatsapp.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [WhatsApp integrations](https://n8n.io/integrations/whatsapp-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* Account 审核更新
* Account 更新
* Business capability 更新
* Message template 质量更新
* Message template 状态更新
* Messages
* Phone number 名称更新
* Phone number 质量更新
* Security
* Template category 更新

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 WhatsApp 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.whatsapp/)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/whatsapp-trigger/)。

有关其 API 的详细信息，请参阅 [WhatsApp 的文档](https://developers.facebook.com/docs/whatsapp/cloud-api)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 WhatsApp Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### Workflow 只在测试或生产环境中工作 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

WhatsApp 只允许你为每个 app 注册一个 webhook。这意味着，每次你从测试 URL 切换到生产 URL（反之亦然）时，WhatsApp 都会覆盖已注册的 webhook URL。

如果你尝试测试一个也在生产环境中处于激活状态的 workflow，可能会遇到此问题。WhatsApp 只会向两个 webhook URL 中的一个发送事件，因此另一个永远不会收到事件通知。

要绕过此问题，你可以在测试时停用 workflow：

{% hint style="warning" %}
**暂停生产流量**

此规避方法会临时停用你的生产 workflow 以便测试。停用期间，你的 workflow 将不再接收生产流量。
{% endhint %}

1. 前往你的 workflow 页面。
2. 切换顶部面板中的 **Active** 开关，临时停用 workflow。
3. 使用测试 webhook URL 测试你的 workflow。
4. 测试完成后，切换 **Inactive** 开关以重新启用 workflow。生产 webhook URL 应恢复工作。

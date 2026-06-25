---
title: Pushcut Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Pushcut Trigger node。按照技术文档将 Pushcut Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Pushcut Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.pushcuttrigger
layout:
  description:
    visible: false
---

# Pushcut Trigger node <a href="#pushcut-trigger-node" id="pushcut-trigger-node"></a>

[Pushcut](https://pushcut.io) 是一款 iOS app，可让你创建智能通知来启动快捷指令、URL 和在线自动化。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/pushcut.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Pushcut Trigger integrations](https://n8n.io/integrations/pushcut-trigger/) 页面。
{% endhint %}

## 配置 Pushcut action <a href="#configure-a-pushcut-action" id="configure-a-pushcut-action"></a>

按照以下步骤，使用你的 Pushcut app 配置 Pushcut Trigger node。

1. 在你的 Pushcut app 中，从 **Notifications** 屏幕选择一个通知。
2. 选择 **Add Action** 按钮。
3. 在 **Label** 字段中输入 action 名称。
4. 选择 **Server** 标签页。
5. 选择 **Integration** 标签页。
6. 选择 **Integration Trigger**。
7. 在 n8n 中，输入 action 名称并选择 **Execute step**。
8. 在 Pushcut app 的 **Select Integration Trigger** 屏幕下选择此 action。
9. 选择右上角的 **Done** 保存 action。

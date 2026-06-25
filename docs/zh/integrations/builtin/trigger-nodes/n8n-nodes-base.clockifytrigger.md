---
title: Clockify Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Clockify Trigger node。按照技术文档将 Clockify Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Clockify Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clockifytrigger
layout:
  description:
    visible: false
---

# Clockify Trigger node <a href="#clockify-trigger-node" id="clockify-trigger-node"></a>

[Clockify](https://clockify.me/) 是一款免费的时间跟踪和工时表应用，用于跨项目跟踪工作时间。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/clockify.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Clockify Trigger integrations](https://n8n.io/integrations/clockify-trigger/) 页面。
{% endhint %}

此 node 使用 workflow 时区设置来指定 time entry 开始时间的范围。如果你希望此 trigger node 检索正确的 time entry，请在 [Workflow Settings](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/configure-workflow-settings) 中配置时区。

---
title: KoboToolbox Trigger node 文档
description: >-
  了解如何在 n8n 中使用 KoboToolbox Trigger node。按照技术文档将 KoboToolbox Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: KoboToolbox Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.kobotoolboxtrigger
layout:
  description:
    visible: false
---

# KoboToolbox Trigger node <a href="#kobotoolbox-trigger-node" id="kobotoolbox-trigger-node"></a>

[KoboToolbox](https://www.kobotoolbox.org/) 是一款现场调查和数据收集工具，用于设计可在移动设备离线填写的交互式表单。它既提供免费云方案，也提供自托管版本。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/kobotoolbox.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [KoboToolbox Trigger integrations](https://n8n.io/integrations/kobotoolbox-trigger/) 页面。
{% endhint %}

此 node 会在指定表单有新提交时启动 workflow。trigger node 会处理 hook 的创建/删除，因此你不需要在 KoboToolbox 中进行任何设置。

它的工作方式与 [KoboToolbox](../app-nodes/n8n-nodes-base.kobotoolbox.md) node 中的 Get Submission 操作相同，包括支持相同的重新格式化选项。

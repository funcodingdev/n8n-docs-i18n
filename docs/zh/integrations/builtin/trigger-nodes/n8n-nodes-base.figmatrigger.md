---
title: Figma Trigger (Beta) node 文档
description: >-
  了解如何在 n8n 中使用 Figma Trigger node。按照技术文档将 Figma Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Figma Trigger (Beta) node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.figmatrigger
layout:
  description:
    visible: false
---

# Figma Trigger (Beta) node <a href="#figma-trigger-beta-node" id="figma-trigger-beta-node"></a>

[Figma](https://www.figma.com/) 是一款主要基于 Web 的原型设计工具，并通过 macOS 和 Windows 桌面应用提供更多离线功能。

{% hint style="warning" %}
**支持的 Figma 计划**

Figma 的免费 "Starter" 计划不支持 webhook。你的团队需要使用 "Professional" 计划才能使用此 node。
{% endhint %}

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/figma.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Figma Trigger integrations](https://n8n.io/integrations/figma-trigger-beta/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

- **文件已评论**：当有人评论文件时触发。
- **文件已删除**：当有人删除单个文件时触发，但删除包含所有文件的整个文件夹时不会触发。
- **文件已更新**：当有人保存或删除文件时触发。在做出更改后 30 秒内关闭文件会产生一次保存。
- **文件版本已更新**：当有人在文件的版本历史中创建命名版本时触发。
- **Library 已发布**：当有人发布 library 文件时触发。

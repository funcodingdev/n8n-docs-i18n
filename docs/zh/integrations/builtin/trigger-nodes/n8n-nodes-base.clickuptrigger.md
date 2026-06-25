---
title: ClickUp Trigger node 文档
description: >-
  了解如何在 n8n 中使用 ClickUp Trigger node。按照技术文档将 ClickUp Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: ClickUp Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.clickuptrigger
layout:
  description:
    visible: false
---

# ClickUp Trigger node <a href="#clickup-trigger-node" id="clickup-trigger-node"></a>

[ClickUp](https://clickup.com/) 是一款基于云的协作和项目管理工具，适用于各种规模和行业的企业。其功能包括沟通和协作工具、任务分配和状态、alert 以及任务工具栏。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/clickup.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [ClickUp Trigger integrations](https://n8n.io/integrations/clickup-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 关键结果
    * 已创建
    * 已删除
    * 已更新
* 列表
    * 已创建
    * 已删除
    * 已更新
* 空间
    * 已创建
    * 已删除
    * 已更新
* 任务
    * 负责人已更新
    * 评论
      * 已发布
      * 已更新
    * 已创建
    * 已删除
    * 截止日期已更新
    * 已移动
    * 状态已更新
    * Tag 已更新
    * 时间预估已更新
    * 跟踪时间已更新
    * 已更新

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 ClickUp 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.clickup.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/clickup-trigger/)。

有关其 API 的详细信息，请参阅 [ClickUp 的文档](https://developer.clickup.com/docs/authentication)。

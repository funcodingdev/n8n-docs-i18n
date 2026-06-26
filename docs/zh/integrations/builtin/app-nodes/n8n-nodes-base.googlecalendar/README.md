---
title: Google Calendar node documentation
description: >-
  了解如何在 n8n 中使用 Google Calendar node。按照技术文档将 Google
  Calendar node 集成到你的工作流中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-base.googlecalendar
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar
layout:
  description:
    visible: false
---

# Google Calendar node <a href="#google-calendar-node" id="google-calendar-node"></a>

使用 Google Calendar node 自动化 Google Calendar 中的工作，并将 Google Calendar 与其他应用集成。n8n 内置支持大量 Google Calendar 功能，包括添加、获取、删除和更新日历事件。

在本页中，你可以找到 Google Calendar node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [Google Calendar credentials](../../credentials/google/README.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Operations 操作 <a href="#operations" id="operations"></a>

* **Calendar**
    * [**Availability**](calendar-operations.md#availability)：检查日历中某个时间段是否可用
* **Event**
    * [**Create**](event-operations.md#create)：向日历添加事件
    * [**Delete**](event-operations.md#delete)：删除事件
    * [**Get**](event-operations.md#get)：获取事件
    * [**Get Many**](event-operations.md#get-many)：从日历中获取所有事件
    * [**Update**](event-operations.md#update)：更新事件

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.googlecalendar 集成模板](https://n8n.io/integrations/google-calendar) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Google Calendar 提供了一个 trigger node。你可以在[这里](../../trigger-nodes/n8n-nodes-base.googlecalendartrigger.md)找到该 trigger node 的文档。

有关该服务的更多信息，请参阅 [Google Calendar 文档](https://developers.google.com/calendar/api/v3/reference)。

在 n8n 网站上查看[示例工作流和相关内容](https://n8n.io/integrations/google-calendar/)。

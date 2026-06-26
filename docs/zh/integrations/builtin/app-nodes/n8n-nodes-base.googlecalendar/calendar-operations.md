---
title: Google Calendar Calendar operations
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Calendar Calendar operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations
description: >-
  n8n 中 Google Calendar node 的 Calendar 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Calendar operations

使用此操作检查 Google Calendar 中某个日历的可用性。有关 Google Calendar node 本身的更多信息，请参阅 [Google Calendar](./)。

## Availability <a href="#availability" id="availability"></a>

使用此操作检查日历中某个时间段是否可用。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Calendar**。
* **Operation**：选择 **Availability**。
* **Calendar**：选择要检查的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Start Time**：要检查的时间段开始时间。默认使用一个求值为当前时间的表达式（`{{ $now }}`）。
* **End Time**：要检查的时间段结束时间。默认使用一个求值为一小时后的表达式（`{{ $now.plus(1, 'hour') }}`）。

### Options <a href="#options" id="options"></a>

* **Output Format**：选择可用性信息的格式：
  * **Availability**：返回给定时间段是否已有重叠事件。
  * **Booked Slots**：返回已预订的时间段。
  * **RAW**：返回 API 的原始数据。
* **Timezone**：响应中使用的时区。默认使用 n8n 时区。

有关更多信息，请参阅 [Freebusy: query | Google Calendar](https://developers.google.com/calendar/api/v3/reference/freebusy/query) API 文档。

---
title: Google Calendar Event operations
contentType:
  - integration
  - reference
priority: high
nodeTitle: Google Calendar Event operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations
description: >-
  n8n 中 Google Calendar node 的 Event 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Event operations

使用这些操作在 Google Calendar 中创建、删除、获取和更新事件。有关 Google Calendar node 本身的更多信息，请参阅 [Google Calendar](./)。

## Create <a href="#create" id="create"></a>

使用此操作向 Google Calendar 添加事件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Event**。
* **Operation**：选择 **Create**。
* **Calendar**：选择要添加事件的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Start Time**：事件的开始时间。默认使用一个求值为当前时间的表达式（`{{ $now }}`）。
* **End Time**：事件的结束时间。默认使用一个求值为一小时后的表达式（`{{ $now.plus(1, 'hour') }}`）。
* **Use Default Reminders**：是否根据日历配置为事件启用默认提醒。

### Options <a href="#options" id="options"></a>

* **All Day**：事件是否为全天事件。
* **Attendees**：要邀请参加事件的与会者。
* **Color Name or ID**：事件颜色。从列表中选择，或使用表达式指定 ID。
* **Conference Data**：创建会议链接（Hangouts、Meet 等）并将其附加到事件。
* **Description**：事件描述。
* **Guests Can Invite Others**：组织者以外的与会者是否可以邀请其他人参加事件。
* **Guests Can Modify**：组织者以外的与会者是否可以修改事件。
* **Guests Can See Other Guests**：组织者以外的与会者是否可以看到事件的其他与会者。
* **ID**：事件的不透明标识符。
* **Location**：事件的地理位置，使用自由格式文本。
* **Max Attendees**：响应中包含的最大与会者数量。如果与会者数量超过指定数量，则只返回参与者。
* **Repeat Frequency**：重复事件的重复间隔。
* **Repeat How Many Times?**：为重复事件创建的实例数量。
* **Repeat Until**：重复事件应停止的日期。
* **RRULE**：重复规则。设置后会忽略 Repeat Frequency、Repeat How Many Times 和 Repeat Until 参数。
* **Send Updates**：是否发送有关新事件创建的通知。
* **Show Me As**：事件是否占用日历上的时间。
* **Summary**：事件标题。

有关更多信息，请参阅 [Events: insert | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/insert) API 文档。

## Delete <a href="#delete" id="delete"></a>

使用此操作从 Google Calendar 删除事件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Event**。
* **Operation**：选择 **Delete**。
* **Calendar**：选择要从中删除事件的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Event ID**：要删除的事件 ID。

### Options <a href="#options" id="options"></a>

* **Send Updates**：是否发送有关事件删除的通知。

有关更多信息，请参阅 [Events: delete | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/delete) API 文档。

## Get <a href="#get" id="get"></a>

使用此操作从 Google Calendar 获取事件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Event**。
* **Operation**：选择 **Get**。
* **Calendar**：选择要从中获取事件的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Event ID**：要获取的事件 ID。

### Options <a href="#options" id="options"></a>

* **Max Attendees**：响应中包含的最大与会者数量。如果与会者数量超过指定数量，则只返回参与者。
* **Return Next Instance of Recurrent Event**：是否返回重复事件的下一个实例，而不是事件本身。
* **Timezone**：响应中使用的时区。默认使用 n8n 时区。

有关更多信息，请参阅 [Events: get | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/get) API 文档。

## Get Many <a href="#get-many" id="get-many"></a>

使用此操作从 Google Calendar 获取多个事件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Event**。
* **Operation**：选择 **Get Many**。
* **Calendar**：选择要从中获取事件的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Return All**：是返回所有结果，还是只返回给定限制内的结果。
* **Limit**：（未选择 "Return All" 时）要返回的最大结果数。
* **After**：获取在此时间之后发生的事件。事件至少有一部分必须在此时间之后。默认使用一个求值为当前时间的表达式（`{{ $now }}`）。将字段切换为 "fixed" 可从日期小组件中选择日期。
* **Before**：获取在此时间之前发生的事件。事件至少有一部分必须在此时间之前。默认使用一个求值为当前时间加一周的表达式（`{{ $now.plus({ week: 1 }) }}`）。将字段切换为 "fixed" 可从日期小组件中选择日期。

### Options <a href="#options" id="options"></a>

* **Fields**：指定要返回的字段。默认返回 Google 预定义的一组常用字段。使用 "\*" 可返回所有字段。你可以在 [Google Calendar 关于使用部分资源的文档](https://developers.google.com/calendar/api/guides/performance#partial)中了解更多信息。
* **iCalUID**：指定要包含在响应中的事件 ID（iCalendar 格式）。
* **Max Attendees**：响应中包含的最大与会者数量。如果与会者数量超过指定数量，则只返回参与者。
* **Order By**：响应中事件使用的排序方式。
* **Query**：用于查找匹配事件的自由文本搜索词。该搜索会搜索除扩展属性以外的所有字段。
* **Recurring Event Handling**：如何处理重复事件：
  * **All Occurrences**：返回指定时间范围内重复事件的所有实例。
  * **First Occurrence**：返回指定时间范围内重复事件的第一个事件。
  * **Next Occurrence**：返回指定时间范围内重复事件的下一个实例。
* **Show Deleted**：是否在结果中包含已删除事件（状态等于 "cancelled"）。
* **Show Hidden Invitations**：是否在结果中包含隐藏邀请。
* **Timezone**：响应中使用的时区。默认使用 n8n 时区。
* **Updated Min**：事件最后修改时间的下限（作为 [RFC 3339 timestamp](https://datatracker.ietf.org/doc/html/rfc3339)）

有关更多信息，请参阅 [Events: list | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/list) API 文档。

## Update <a href="#update" id="update"></a>

使用此操作更新 Google Calendar 中的事件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Calendar credentials](../../credentials/google/)。
* **Resource**：选择 **Event**。
* **Operation**：选择 **Update**。
* **Calendar**：选择要添加事件的日历。选择 **From list** 可从下拉列表中选择标题，或选择 **By ID** 输入日历 ID。
* **Event ID**：要更新的事件 ID。
* **Modify**：对于重复事件，选择是更新重复事件，还是更新重复事件的特定实例。
* **Use Default Reminders**：是否根据日历配置为事件启用默认提醒。
* **Update Fields**：要更新的事件字段：
  * **All Day**：事件是否为全天事件。
  * **Attendees**：要邀请参加事件的与会者。你可以选择添加与会者，也可以替换现有与会者列表。
  * **Color Name or ID**：事件颜色。从列表中选择，或使用表达式指定 ID。
  * **Description**：事件描述。
  * **End**：事件结束时间。
  * **Guests Can Invite Others**：组织者以外的与会者是否可以邀请其他人参加事件。
  * **Guests Can Modify**：组织者以外的与会者是否可以更改事件。
  * **Guests Can See Other Guests**：组织者以外的与会者是否可以看到事件的其他与会者。
  * **ID**：事件的不透明标识符。
  * **Location**：事件的地理位置，使用自由格式文本。
  * **Max Attendees**：响应中包含的最大与会者数量。如果与会者数量超过指定数量，则只返回参与者。
  * **Repeat Frequency**：重复事件的重复间隔。
  * **Repeat How Many Times?**：为重复事件创建的实例数量。
  * **Repeat Until**：重复事件应停止的日期。
  * **RRULE**：重复规则。设置后会忽略 Repeat Frequency、Repeat How Many Times 和 Repeat Until 参数。
  * **Send Updates**：是否发送有关新事件创建的通知。
  * **Show Me As**：事件是否占用日历上的时间。
  * **Start**：事件开始时间。
  * **Summary**：事件标题。
  * **Visibility**：事件可见性：
    * **Confidential**：事件是私密的。此值用于兼容。
    * **Default**：使用日历上事件的默认可见性。
    * **Public**：事件是公开的，日历的所有读取者都可以看到事件详情。
    * **Private**：事件是私密的，只有事件与会者可以查看事件详情。

有关更多信息，请参阅 [Events: update | Google Calendar](https://developers.google.com/calendar/api/v3/reference/events/update) API 文档。

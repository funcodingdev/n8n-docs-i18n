---
title: Date & Time
description: >-
  n8n 中 Date & Time node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Date & Time
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.datetime.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datetime'
layout:
  description:
    visible: false
---

# Date & Time <a href="#date-and-time" id="date-and-time"></a>

Date & Time node 用于处理日期和时间数据，并将其转换为不同格式。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ttmJg4aaEfjB4LyKpCzt/" %}

{% hint style="info" %}
**其他 node 中的日期和时间**

你可以在 Code node 中处理日期和时间，也可以在任何 node 的 expression 中处理。n8n 支持 Luxon，以便在 JavaScript 中处理日期和时间。更多信息请参阅 [Date and time with Luxon](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/handle-special-data-types/work-with-dates-and-times)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Add to a Date**：向某个日期添加指定时长。
* **Extract Part of a Date**：提取日期的一部分，例如年、月或日。
* **Format a Date**：使用预设选项或自定义 expression，将日期格式转换为新格式。
* **Get Current Date**：获取当前日期，并选择是否包含当前时间。适用于触发其他流程和条件逻辑。
* **Get Time Between Dates**：计算两个日期之间以特定单位表示的时间量。
* **Round a Date**：将日期向上或向下取整到你选择的最近单位，例如月、日或小时。
* **Subtract From a Date**：从某个日期减去指定时长。

请参阅下面各节，了解每个操作特有的参数和选项。

## Add to a Date <a href="#add-to-a-date" id="add-to-a-date"></a>

使用这些参数配置该操作：

* **Date to Add To**：输入要更改的日期。
* **Time Unit to Add**：为 **Duration** 参数选择时间单位。
* **Duration**：输入要添加到日期的时间单位数量。
* **Output Field Name**：输入用于输出新日期的字段名称。

### Add to a Date 选项 <a href="#add-to-a-date-options" id="add-to-a-date-options"></a>

此操作有一个选项：**Include Input Fields**。如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。

## Extract Part of a Date <a href="#extract-part-of-a-date" id="extract-part-of-a-date"></a>

使用这些参数配置该操作：

* **Date**：输入要取整或提取部分内容的日期。
* **Part**：选择要提取的日期部分。可选：
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
* **Output Field Name**：输入用于输出所提取日期部分的字段名称。

### Extract Part of a Date 选项 <a href="#extract-part-of-a-date-options" id="extract-part-of-a-date-options"></a>

此操作有一个选项：**Include Input Fields**。如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。

## Format a Date <a href="#format-a-date" id="format-a-date"></a>

使用这些参数配置该操作：

* **Date**：输入要格式化的日期。
* **Format**：选择要把日期转换成的格式。可选：
    * **Custom Format**：使用 Luxon 的[特殊 token](https://moment.github.io/luxon/#/formatting?id=table-of-tokens) 输入自定义格式。Token 区分大小写。
    * **MM/DD/YYYY**：对于 `4 September 1986`，会将日期格式化为 `09/04/1986`。
    * **YYYY/MM/DD**：对于 `4 September 1986`，会将日期格式化为 `1986/09/04`。
    * **MMMM DD YYYY**：对于 `4 September 1986`，会将日期格式化为 `September 04 1986`。
    * **MM-DD-YYYY**：对于 `4 September 1986`，会将日期格式化为 `09-04-1986`。
    * **YYYY-MM-DD**：对于 `4 September 1986`，会将日期格式化为 `1986-09-04`。
* **Output Field Name**：输入用于输出格式化后日期的字段名称。

### Format a Date 选项 <a href="#format-a-date-options" id="format-a-date-options"></a>

此操作包含这些选项：

* **Include Input Fields**：如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。
* **From Date Format**：如果该 node 无法正确识别 **Date** 格式，请在这里输入该 **Date** 的格式，以便 node 正确处理它。使用 Luxon 的[特殊 token](https://moment.github.io/luxon/#/formatting?id=table-of-tokens) 输入格式。Token 区分大小写
* **Use Workflow Timezone**：选择使用输入的时区（关闭）还是 workflow 的时区（开启）。

## Get Current Date <a href="#get-current-date" id="get-current-date"></a>

使用这些参数配置该操作：

* **Include Current Time**：选择是否包含当前时间（开启），或将时间设置为午夜（关闭）。
* **Output Field Name**：输入用于输出当前日期的字段名称。

### Get Current Date 选项 <a href="#get-current-date-options" id="get-current-date-options"></a>

此操作包含这些选项：

* **Include Input Fields**：如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。
* **Timezone**：设置要使用的时区。如果留空，该 node 会使用 n8n 实例的时区。

{% hint style="info" %}
**+00:00 timezone**

+00:00 时区请使用 `GMT`。
{% endhint %}

## Get Time Between Dates <a href="#get-time-between-dates" id="get-time-between-dates"></a>

使用这些参数配置该操作：

* **Start Date**：输入你想比较的较早日期。
* **End Date**：输入你想比较的较晚日期。
* **Units**：选择要计算二者之间时间差的单位。可以包含多个单位。可选：
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
    * **Millisecond**
* **Output Field Name**：输入用于输出计算后时间差的字段名称。

### Get Time Between Dates 选项 <a href="#get-time-between-dates-options" id="get-time-between-dates-options"></a>

Get Time Between Dates 操作包含 **Include Input Fields** 选项，以及 **Output as ISO String** 选项。如果关闭此选项，你选择的每个单位都会返回自己的时间差计算，例如：

    timeDifference
    years : 1
    months : 3
    days : 13

如果开启 **Output as ISO String** 选项，该 node 会将输出格式化为单个 ISO duration 字符串，例如：`P1Y3M13D`。

ISO duration format 会以 `P<n>Y<n>M<n>DT<n>H<n>M<n>S` 形式显示格式。`<n>` 是其后单位对应的数字。

* P = period（duration）。所有 ISO duration 字符串都以它开头。
* Y = years
* M = months
* W = weeks
* D = days
* T = 日期和时间之间的分隔符，用于避免 month 和 minute 混淆
* H = hours
* M = minutes
* S = seconds

Milliseconds 没有自己的单位，而是表示为 decimal seconds。例如，2.1 milliseconds 是 `0.0021S`。

## Round a Date <a href="#round-a-date" id="round-a-date"></a>

使用这些参数配置该操作：

* **Date**：输入你想取整的日期。
* **Mode**：选择 **Round Down** 还是 **Round Up**。
* **To Nearest**：选择要取整到的单位。可选：
    * **Year**
    * **Month**
    * **Week**
    * **Day**
    * **Hour**
    * **Minute**
    * **Second**
* **Output Field Name**：输入用于输出取整后日期的字段名称。

### Round a Date 选项 <a href="#round-a-date-options" id="round-a-date-options"></a>

此操作有一个选项：**Include Input Fields**。如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。

## Subtract From a Date <a href="#subtract-from-a-date" id="subtract-from-a-date"></a>

使用这些参数配置该操作：

* **Date to Subtract From**：输入要从中减去时长的日期。
* **Time Unit to Subtract**：选择要从 **Duration** 数量中减去的单位。
* **Duration**：输入要从 **Date to Subtract From** 中减去的时间单位数量。
* **Output Field Name**：输入用于输出取整后日期的字段名称。

### Subtract From a Date 选项 <a href="#subtract-from-a-date-options" id="subtract-from-a-date-options"></a>

此操作有一个选项：**Include Input Fields**。如果希望在输出中包含所有输入字段，请开启此选项。如果关闭，则只输出 **Output Field Name** 及其内容。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Date & Time 集成模板](https://n8n.io/integrations/date-and-time)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

Date & Time node 使用 [Luxon](https://moment.github.io/luxon)。你也可以在 [Code](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/using-the-code-node) node 和 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 中使用 Luxon。更多信息请参阅 [Date and time with Luxon](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/handle-special-data-types/work-with-dates-and-times)。

### 支持的日期格式 <a href="#supported-date-formats" id="supported-date-formats"></a>

n8n 支持 Luxon [支持的所有日期格式](https://moment.github.io/luxon/#/formatting?id=table-of-tokens)。Token 区分大小写。

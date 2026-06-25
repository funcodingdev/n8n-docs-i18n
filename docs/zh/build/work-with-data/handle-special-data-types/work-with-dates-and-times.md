---
title: 使用 Luxon 处理日期和时间
description: 在 n8n 中使用 Luxon 处理日期和时间。
contentType: howto
nodeTitle: Work with dates and times
originalFilePath: data/specific-data-types/luxon.md
originalUrl: 'https://docs.n8n.io/data/specific-data-types/luxon'
url: >-
  https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-dates-and-times
layout:
  description:
    visible: false
---

# 使用 Luxon 处理日期和时间 <a href="#date-and-time-with-luxon" id="date-and-time-with-luxon"></a>

[Luxon](https://github.com/moment/luxon/) 是一个 JavaScript 库，可让日期和时间处理更容易。有关 Luxon 用法的完整详情，请参阅 [Luxon 文档](https://moment.github.io/luxon/#/?id=luxon)。

n8n 在 node 之间以字符串形式传递日期，因此你需要解析它们。Luxon 可以简化这一过程。

{% hint style="info" %}
**Python 支持**

Luxon 是 JavaScript 库。使用 Code node 中的 Python 时，n8n 创建的两个便捷[变量](#get-the-current-datetime-or-date)可用，但功能有限：

* 你不能对这些变量执行 Luxon 操作。例如，Python 中没有 `$today.minus(...)` 的等价写法。
* 通用 Luxon 功能（例如[将日期字符串转换为 Luxon](#convert-date-string-to-luxon)）不适用于 Python 用户。
{% endhint %}

## n8n 中的日期和时间行为 <a href="#date-and-time-behavior-in-n8n" id="date-and-time-behavior-in-n8n"></a>

请注意以下事项：

* 在工作流中，n8n 会在 node 之间将日期和时间转换为字符串。对来自其他 node 的日期和时间执行计算时，需要记住这一点。
* 在 n8n 中，推荐使用 Luxon 的 `DateTime()`。使用原生 JavaScript 的 `Date()` 无法配合某些 n8n 功能。例如，它不遵守 [Workflow-specific Time Zone](https://docs.n8n.io/workflows/settings/#timezone)。
* 在原生 JavaScript 中，你可以用 `new Date('2019-06-23')` 将字符串转换为日期。在 Luxon 中，你必须使用明确声明格式的函数，例如 `DateTime.fromISO('2019-06-23')` 或 `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`。

## 在 n8n 中设置 timezone <a href="#setting-the-timezone-in-n8n" id="setting-the-timezone-in-n8n"></a>

Luxon 使用 n8n timezone。这个值可以是：

* 默认值：`America/New York`
* n8n 实例的自定义 timezone，通过 `GENERIC_TIMEZONE` 环境变量设置。
* 单个工作流的自定义 timezone，在工作流设置中配置。

## 常见任务 <a href="#common-tasks" id="common-tasks"></a>

本节提供一些常见操作示例。更多示例和详细指南请参阅 [Luxon 自身文档](https://moment.github.io/luxon/#/?id=luxon)。

### 获取当前 datetime 或 date <a href="#get-the-current-datetime-or-date" id="get-the-current-datetime-or-date"></a>

使用 `$now` 和 `$today` Luxon 对象获取当前时间或日期：

* `now`：包含当前 timestamp 的 Luxon 对象。等价于 `DateTime.now()`。
* `today`：包含当前 timestamp 并向下取整到当天的 Luxon 对象。等价于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`。

请注意，这些变量在转换为字符串时可能返回不同的时间格式：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```javascript
{{$now}}
// n8n displays the ISO formatted timestamp
// For example 2022-03-09T14:02:37.065+00:00
{{"Today's date is " + $now}}
// n8n displays "Today's date is <unix timestamp>"
// For example "Today's date is 1646834498755"
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```javascript
$now
// n8n displays <ISO formatted timestamp>
// For example 2022-03-09T14:00:25.058+00:00
let rightNow = "Today's date is " + $now
// n8n displays "Today's date is <unix timestamp>"
// For example "Today's date is 1646834498755"
```
{% endtab %}

{% tab title="Code node (Python)" %}
```python
_now
# n8n displays <ISO formatted timestamp>
# For example 2022-03-09T14:00:25.058+00:00
rightNow = "Today's date is " + str(_now)
# n8n displays "Today's date is <unix timestamp>"
# For example "Today's date is 1646834498755"
```
{% endtab %}
{% endtabs %}

n8n 提供内置便捷函数，用于支持 expression 中的日期数据转换。更多信息请参阅 [Expression reference](../transform-data/expression-reference/README.md)。

### 将 JavaScript 日期转换为 Luxon <a href="#convert-javascript-dates-to-luxon" id="convert-javascript-dates-to-luxon"></a>

如需将原生 JavaScript 日期转换为 Luxon 日期：

* 在 expression 中，使用 `.toDateTime()` 方法。例如 `{{ (new Date()).toDateTime() }}`。
* 在 Code node 中，使用 `DateTime.fromJSDate()`。例如 `let luxondate = DateTime.fromJSDate(new Date())`。

### 将日期字符串转换为 Luxon <a href="#convert-date-string-to-luxon" id="convert-date-string-to-luxon"></a>

你可以将日期字符串和其他日期格式转换为 Luxon DateTime 对象。你可以从标准格式转换，也可以从任意字符串转换。

{% hint style="info" %}
**Luxon DateTime 与 JavaScript Date 的区别**

在原生 JavaScript 中，你可以用 `new Date('2019-06-23')` 将字符串转换为日期。在 Luxon 中，你必须使用明确声明格式的函数，例如 `DateTime.fromISO('2019-06-23')` 或 `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`。
{% endhint %}
#### 如果日期采用受支持的标准技术格式： <a href="#if-you-have-a-date-in-a-supported-standard-technical-format" id="if-you-have-a-date-in-a-supported-standard-technical-format"></a>

大多数日期使用 `fromISO()`。这会从 ISO 8601 字符串创建 Luxon DateTime。例如：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{DateTime.fromISO('2019-06-23T00:00:00.00')}}
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let luxonDateTime = DateTime.fromISO('2019-06-23T00:00:00.00')
```
{% endtab %}
{% endtabs %}

Luxon API 文档提供了有关 [fromISO](https://moment.github.io/luxon/api-docs/index.html#datetimefromiso) 的更多信息。

Luxon 提供函数用于处理多种格式的转换。详情请参阅 Luxon 的 [Parsing technical formats](https://moment.github.io/luxon/#/parsing?id=parsing-technical-formats) 指南。

#### 如果日期字符串不使用标准格式： <a href="#if-you-have-a-date-as-a-string-that-doesnt-use-a-standard-format" id="if-you-have-a-date-as-a-string-that-doesnt-use-a-standard-format"></a>

使用 Luxon 的 [Ad-hoc parsing](https://moment.github.io/luxon/#/parsing?id=ad-hoc-parsing)。为此，请使用 `fromFormat()` 函数，提供字符串和一组描述格式的 [tokens](https://moment.github.io/luxon/#/parsing?id=table-of-tokens)。

例如，n8n 的创立日期为 2019 年 6 月 23 日，格式为 `23-06-2019`。你想将其转换为 Luxon 对象：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")}}
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let newFormat = DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")
```
{% endtab %}
{% endtabs %}

使用 ad-hoc parsing 时，请注意 Luxon 关于 [Limitations](https://moment.github.io/luxon/#/parsing?id=limitations) 的警告。如果看到意外结果，请尝试其 [Debugging](https://moment.github.io/luxon/#/parsing?id=debugging) 指南。

### 获取距今天 n 天的日期 <a href="#get-n-days-from-today" id="get-n-days-from-today"></a>

获取今天之前或之后若干天的日期。

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
例如，你想设置一个字段，让它始终显示当前日期前七天的日期。

在 expressions editor 中输入：


``` js
{{$today.minus({days: 7})}}
```

在 2019 年 6 月 23 日，此表达式返回 `[Object: "2019-06-16T00:00:00.000+00:00"]`。

此示例为方便起见使用 n8n 自定义变量 `$today`。它等价于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`。
{% endtab %}

{% tab title="Code node (JavaScript)" %}
例如，你想要一个包含当前日期前七天日期的变量。

在代码编辑器中输入：

``` js
let sevenDaysAgo = $today.minus({days: 7})
```

在 2019 年 6 月 23 日，此代码返回 `[Object: "2019-06-16T00:00:00.000+00:00"]`。

此示例为方便起见使用 n8n 自定义变量 `$today`。它等价于 `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`。
{% endtab %}
{% endtabs %}

更多详细信息和示例请参阅：

* Luxon's [guide to math](https://moment.github.io/luxon/#/math)
* Their API documentation on [DateTime plus](https://moment.github.io/luxon/api-docs/index.html#datetimeplus) and [DateTime minus](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)

### 创建人类可读日期 <a href="#create-human-readable-dates" id="create-human-readable-dates"></a>

在[获取距今天 n 天的日期](#get-n-days-from-today)中，示例获取当前日期前七天的日期，并以 `[Object: "yyyy-mm-dd-T00:00:00.000+00:00"]`（expression 中）或 `yyyy-mm-dd-T00:00:00.000+00:00`（Code node 中）返回。要让它更易读，可以使用 Luxon 的格式化函数。

例如，你想让包含日期的字段格式化为 DD/MM/YYYY，使其在 2019 年 6 月 23 日返回 `23/06/2019`。

此 expression 获取今天前七天的日期，并将其转换为 DD/MM/YYYY 格式。

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$today.minus({days: 7}).toLocaleString()}}
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString()
```
{% endtab %}
{% endtabs %}

你可以更改格式。例如：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})}}
```

在 2019 年 6 月 23 日，此表达式返回 "16 June 2019"。
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})
```

在 2019 年 6 月 23 日，此代码返回 "16 June 2019"。
{% endtab %}
{% endtabs %}

更多信息请参阅 Luxon 的 [toLocaleString (strings for humans)](https://moment.github.io/luxon/#/formatting?id=tolocalestring-strings-for-humans) 指南。


### 获取两个日期之间的时间 <a href="#get-the-time-between-two-dates" id="get-the-time-between-two-dates"></a>

如需获取两个日期之间的时间，请使用 Luxon 的 diffs 功能。它会用一个日期减去另一个日期，并返回 duration。

例如，获取两个日期之间相差的月数：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()}}
```

这会返回 `[Object: {"months":1}]`。
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let monthsBetweenDates = DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()
```

这会返回 `{"months":1}`。
{% endtab %}
{% endtabs %}

更多信息请参阅 Luxon 的 [Diffs](https://moment.github.io/luxon/#/math?id=diffs)。

### 较长示例：距离圣诞节还有多少天？ <a href="#a-longer-example-how-many-days-to-christmas" id="a-longer-example-how-many-days-to-christmas"></a>

此示例组合了多个 Luxon 功能，使用 JMESPath，并进行一些基础字符串操作。

场景：你想要一个到 12 月 25 日的倒计时。它每天都应该告诉你距离圣诞节还剩多少天。你不想为下一年更新它，它需要无缝适用于每一年。

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{"There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!"}}
```

这会输出 `"There are <number of days> days to Christmas!"`。例如，在 3 月 9 日，它会输出 "There are 291 days to Christmas!"。

该 expression 的详细说明：

* `{{`：表示 expression 开始。
* `"There are "`：字符串。
* `+`：用于连接两个字符串。
* `$today.diff()`：这类似于[获取两个日期之间的时间](#get-the-time-between-two-dates)中的示例，但使用 n8n 自定义 `$today` 变量。
* `DateTime.fromISO($today.year + '-12-25'), 'days'`：此部分使用 `$today.year` 获取当前年份，将其与月份和日期一起转换为 ISO 字符串，然后获取整个 ISO 字符串并将其转换为 Luxon DateTime 数据结构。它还告诉 Luxon 你希望 duration 以天为单位。
* `toObject()` 将 diff() 的结果转换为更可用的对象。此时，expression 返回 `[Object: {"days":-<number-of-days>}]`。例如，在 3 月 9 日，返回 `[Object: {"days":-291}]`。
* `.days` 使用 JMESPath 语法只从对象中检索天数。有关在 n8n 中使用 JMESPath 的更多信息，请参阅我们的 [JMESpath](query-json-data.md) 文档。这会得到距离圣诞节的天数，是一个负数。
* `.toString().substring(1)` 将数字转换为字符串并移除 `-`。
* `+ " days to Christmas!"`：另一个字符串，使用 `+` 将它连接到前一个字符串。
* `}}`：表示 expression 结束。
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let daysToChristmas = "There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!";
```

这会输出 `"There are <number of days> days to Christmas!"`。例如，在 3 月 9 日，它会输出 "There are 291 days to Christmas!"。

该代码的详细说明：

* `"There are "`：字符串。
* `+`：用于连接两个字符串。
* `$today.diff()`：这类似于[获取两个日期之间的时间](#get-the-time-between-two-dates)中的示例，但使用 n8n 自定义 `$today` 变量。
* `DateTime.fromISO($today.year + '-12-25'), 'days'`：此部分使用 `$today.year` 获取当前年份，将其与月份和日期一起转换为 ISO 字符串，然后获取整个 ISO 字符串并将其转换为 Luxon DateTime 数据结构。它还告诉 Luxon 你希望 duration 以天为单位。
* `toObject()` 将 diff() 的结果转换为更可用的对象。此时，expression 返回 `[Object: {"days":-<number-of-days>}]`。例如，在 3 月 9 日，返回 `[Object: {"days":-291}]`。
* `.days` 使用 JMESPath 语法只从对象中检索天数。有关在 n8n 中使用 JMESPath 的更多信息，请参阅我们的 [JMESpath](query-json-data.md) 文档。这会得到距离圣诞节的天数，是一个负数。
* `.toString().substring(1)` 将数字转换为字符串并移除 `-`。
* `+ " days to Christmas!"`：另一个字符串，使用 `+` 将它连接到前一个字符串。
{% endtab %}
{% endtabs %}

---
nodeTitle: Datetime
originalFilePath: data/expression-reference/datetime.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/datetime'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/datetime
layout:
  description:
    visible: false
---
# DateTime <a href="#datetime" id="datetime"></a>

## _`DateTime`_.**`day`** <a href="#datetimeday" id="datetimeday"></a>

**描述：** 月中的日期（1-31）

**语法：** _`DateTime`_.day

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.day //=> 30
  ```

## _`DateTime`_.**`diffTo()`** <a href="#datetimediffto" id="datetimediffto"></a>

**描述：** 返回两个 DateTime 之间的差值，单位为给定 unit

**语法：** _`DateTime`_.diffTo(otherDateTime, unit)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `otherDateTime ` (String|DateTime) - 要从基础 DateTime 中减去的时刻。可以是 ISO 日期字符串或 Luxon DateTime。
  * `unit ` (String|Array<String>) - 可选 - 返回结果使用的单位或单位数组。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt1 = "2024-03-30T18:49:07.234".toDateTime()
  dt1.diffTo('2025-01-01', 'days') //=> 276.21
  ```

  ```javascript
  // dt1 = "2024-03-30T18:49:07.234".toDateTime()
  // dt2 = "2025-01-01T00:00:00.000".toDateTime()
  dt1.diffTo(dt2, ['months', 'days']) //=> {'months':, 'days':}
  ```

  ```javascript
  Note: should support both day and days, etc.
  ```

## _`DateTime`_.**`diffToNow()`** <a href="#datetimedifftonow" id="datetimedifftonow"></a>

**描述：** 返回当前时刻与该 DateTime 之间的差值，单位为给定 unit。如需文本表示，请改用 <code>toRelative()</code>。

**语法：** _`DateTime`_.diffToNow(unit)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `unit ` (String|Array<String>) - 可选 - 返回结果使用的单位或单位数组。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>。

**示例：**

  ```javascript
  // dt = "2023-03-30T18:49:07.234".toDateTime()
  dt.diffToNow('days') //=> 371.9
  ```

  ```javascript
  // dt = "2023-03-30T18:49:07.234".toDateTime()
  dt.diffToNow(['months', 'days']) //=> {"months":12, "days":5.9}
  ```

  ```javascript
  Note: should support both day and days, etc.
  ```

## _`DateTime`_.**`endOf()`** <a href="#datetimeendof" id="datetimeendof"></a>

**描述：** 将 DateTime 向上舍入到其某个单位的末尾，例如月末

**语法：** _`DateTime`_.endOf(unit, opts)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `unit ` (String) - 要舍入到末尾的单位。可以是 <code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。
  * `opts ` (Object) - 可选 - 包含会影响输出的选项的 Object。可用属性：
<code>useLocaleWeeks</code> (boolean)：计算一周起点时是否使用 locale。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-03-20T18:49".toDateTime()
  dt.endOf('month') //=> 2024-03-31T23:59
  ```

## _`DateTime`_.**`equals()`** <a href="#datetimeequals" id="datetimeequals"></a>

**描述：** 如果两个 DateTime 表示完全相同的时刻且位于同一时区，则返回 <code>true</code>。如需不那么严格的比较，请使用 <code>hasSame()</code>。

**语法：** _`DateTime`_.equals(other)

**返回：** Boolean

**类型：** Luxon

**参数：**

  * `other ` (DateTime) - 要比较的另一个 DateTime

**示例：**

  ```javascript
  // dt1 = "2024-03-20T18:49+01:00".toDateTime()
  // dt2 = "2024-03-20T19:49+02:00".toDateTime()
  dt1.equals(dt2) //=> false
  ```

## _`DateTime`_.**`extract()`** <a href="#datetimeextract" id="datetimeextract"></a>

**描述：** 提取日期或时间的一部分，例如月份，并以数字形式返回。如需提取文本名称，请参阅 <code>format()</code>。

**语法：** _`DateTime`_.extract(unit?)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `unit` (String) - 可选 - 要返回的日期或时间部分。可选值：<code>year</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code>

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.extract('month') //=> 3
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.extract('hour') //=> 18
  ```

## _`DateTime`_.**`format()`** <a href="#datetimeformat" id="datetimeformat"></a>

**描述：** 使用指定格式将 DateTime 转换为字符串。<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式化指南</a>。对于常见格式，<code>toLocaleString()</code> 可能更简单。

**语法：** _`DateTime`_.format(fmt)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `fmt` (String) - 要返回字符串所使用的<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式</a>

**示例：**

  ```javascript
  // dt = "2024-04-30T18:49".toDateTime()
  dt.format('dd/LL/yyyy') //=> '30/04/2024'
  ```

  ```javascript
  // dt = "2024-04-30T18:49".toDateTime()
  dt.format('dd LLL yy') //=> '30 Apr 24'
  dt.setLocale('fr').format('dd LLL yyyy') //=> '30 avr. 2024'
  dt.format("HH 'hours and' mm 'minutes'") //=> '18 hours and 49 minutes'
  ```

## _`DateTime`_.**`hasSame()`** <a href="#datetimehassame" id="datetimehassame"></a>

**描述：** 如果两个 DateTime 在指定单位上相同，则返回 <code>true</code>。会忽略时区（只比较本地时间），因此必要时请先使用 <code>toUTC()</code>。

**语法：** _`DateTime`_.hasSame(otherDateTime, unit)

**返回：** Boolean

**类型：** Luxon

**参数：**

  * `otherDateTime ` (DateTime) - 要比较的另一个 DateTime
  * `unit ` (String) - 要检查相同程度的时间单位。可选值为 <code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。

**示例：**

  ```javascript
  // dt1 = "2024-03-20".toDateTime()
  // dt2 = "2024-03-18".toDateTime()
  dt1.hasSame(dt2, 'month') //=> true
  ```

  ```javascript
  // dt1 = "1982-03-20".toDateTime()
  // dt2 = "2024-03-18".toDateTime()
  dt1.hasSame(dt2, 'month') //=> false
  ```

## _`DateTime`_.**`hour`** <a href="#datetimehour" id="datetimehour"></a>

**描述：** 一天中的小时（0-23）

**语法：** _`DateTime`_.hour

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.hour //=> 18
  ```

## _`DateTime`_.**`isBetween()`** <a href="#datetimeisbetween" id="datetimeisbetween"></a>

**描述：** 如果 DateTime 位于指定的两个时刻之间，则返回 <code>true</code>

**语法：** _`DateTime`_.isBetween(date1, date2)

**返回：** Boolean

**来源：** 自定义 n8n 功能

**参数：**

  * `date1` (String|DateTime) - 基础 DateTime 必须晚于的时刻。可以是 ISO 日期字符串或 Luxon DateTime。
  * `date2` (String|DateTime) - 基础 DateTime 必须早于的时刻。可以是 ISO 日期字符串或 Luxon DateTime。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.isBetween('2020-06-01', '2025-06-01') //=> true
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.isBetween('2020', $now) //=> true
  ```

## _`DateTime`_.**`isInDST`** <a href="#datetimeisindst" id="datetimeisindst"></a>

**描述：** DateTime 是否处于夏令时

**语法：** _`DateTime`_.isInDST

**返回：** Boolean

**类型：** Luxon

## _`DateTime`_.**`locale`** <a href="#datetimelocale" id="datetimelocale"></a>

**描述：** DateTime 的 locale，例如 'en-GB'。格式化 DateTime 时会使用该 locale。

**语法：** _`DateTime`_.locale

**返回：** String

**类型：** Luxon

**示例：**

  ```javascript
  $now.locale //=> 'en-US'
  ```

## _`DateTime`_.**`millisecond`** <a href="#datetimemillisecond" id="datetimemillisecond"></a>

**描述：** 秒中的毫秒（0-999）

**语法：** _`DateTime`_.millisecond

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49:07.234".toDateTime()
  dt.millisecond //=> 234
  ```

## _`DateTime`_.**`minus()`** <a href="#datetimeminus" id="datetimeminus"></a>

**描述：** 从 DateTime 中减去给定的一段时间

**语法：** _`DateTime`_.minus(n, unit?)

**返回：** DateTime

**来源：** 自定义 n8n 功能

**参数：**

  * `n` (Number|Object) - 要减去的单位数量。也可以使用 Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration</a> object 一次减去多个单位。
  * `unit` (String) - 可选 - 数字的单位。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minus(7, 'days') //=> 2024-04-23T18:49
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minus(4, 'years') //=> 2020-04-30T18:49
  ```

## _`DateTime`_.**`minute`** <a href="#datetimeminute" id="datetimeminute"></a>

**描述：** 小时中的分钟（0-59）

**语法：** _`DateTime`_.minute

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.minute //=> 49
  ```

## _`DateTime`_.**`month`** <a href="#datetimemonth" id="datetimemonth"></a>

**描述：** 月份（1-12）

**语法：** _`DateTime`_.month

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.month //=> 3
  ```

## _`DateTime`_.**`monthLong`** <a href="#datetimemonthlong" id="datetimemonthlong"></a>

**描述：** 文本形式的完整月份名称，例如 'October'。如果未指定 locale，则默认使用系统 locale。

**语法：** _`DateTime`_.monthLong

**返回：** String

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.monthLong //=> 'March'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').monthLong //=> 'März'
  ```

## _`DateTime`_.**`monthShort`** <a href="#datetimemonthshort" id="datetimemonthshort"></a>

**描述：** 文本形式的月份缩写，例如 'Oct'。如果未指定 locale，则默认使用系统 locale。

**语法：** _`DateTime`_.monthShort

**返回：** String

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.monthShort //=> 'Mar'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').monthShort //=> 'Mär'
  ```

## _`DateTime`_.**`plus()`** <a href="#datetimeplus" id="datetimeplus"></a>

**描述：** 向 DateTime 添加给定的一段时间

**语法：** _`DateTime`_.plus(n, unit?)

**返回：** DateTime

**来源：** 自定义 n8n 功能

**参数：**

  * `n` (Number|Object) - 要添加的单位数量。也可以使用 Luxon <a href=”https://moment.github.io/luxon/api-docs/index.html#duration”>Duration</a> object 一次添加多个单位。
  * `unit` (String) - 可选 - 数字的单位。可选值：<code>years</code>、<code>months</code>、<code>weeks</code>、<code>days</code>、<code>hours</code>、<code>minutes</code>、<code>seconds</code>、<code>milliseconds</code>

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.plus(7, 'days') //=> 2024-04-06T18:49
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.plus(4, 'years') //=> 2028-04-30T18:49
  ```

## _`DateTime`_.**`quarter`** <a href="#datetimequarter" id="datetimequarter"></a>

**描述：** 年中的季度（1-4）

**语法：** _`DateTime`_.quarter

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.quarter //=> 1
  ```

## _`DateTime`_.**`second`** <a href="#datetimesecond" id="datetimesecond"></a>

**描述：** 分钟中的秒（0-59）

**语法：** _`DateTime`_.second

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49:07.234".toDateTime()
  dt.second //=> 7
  ```

## _`DateTime`_.**`set()`** <a href="#datetimeset" id="datetimeset"></a>

**描述：** 为 DateTime 的指定单位分配新值。若要舍入 DateTime，另请参阅 <code>startOf()</code> 和 <code>endOf()</code>。

**语法：** _`DateTime`_.set(values)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `values ` (Object) - 包含要设置的单位和对应赋值的对象。可用 key 为 <code>year</code>、<code>month</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 和 <code>millsecond</code>。

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.set({year:1982, month:10}) //=> 1982-10-20T18:49
  ```

## _`DateTime`_.**`setLocale()`** <a href="#datetimesetlocale" id="datetimesetlocale"></a>

**描述：** 设置 locale，它决定 DateTime 的语言和格式。在生成 DateTime 的文本表示时很有用，例如配合 <code>format()</code> 或 <code>toLocaleString()</code>。

**语法：** _`DateTime`_.setLocale(locale)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `locale ` (String) - 要指定的 locale，例如英国英语使用 ‘en-GB’，巴西葡萄牙语使用 ‘pt-BR’。<a href=”https://www.localeplanet.com/icu/”>列表</a>（非官方）

**示例：**

  ```javascript
  $now.setLocale('de-DE').toLocaleString({'dateStyle':'long'}) //=> 5. Oktober 2024
  ```

  ```javascript
  $now.setLocale('fr-FR').toLocaleString({'dateStyle':'long'}) //=> 5 octobre 2024
  ```

## _`DateTime`_.**`setZone()`** <a href="#datetimesetzone" id="datetimesetzone"></a>

**描述：** 将 DateTime 转换为给定时区。除非在 options 中指定，否则 DateTime 仍表示同一时刻。另请参阅 <code>toLocal()</code> 和 <code>toUTC()</code>。

**语法：** _`DateTime`_.setZone(zone, opts)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `zone ` (String) - 可选 - zone 标识符，格式可以是 ‘America/New_York’、'UTC+3'，也可以是字符串 'local' 或 'utc'
  * `opts ` (Object) - 可选 - 会影响输出的选项。可用属性：
<code>keepCalendarTime</code> (boolean)：是否保持时间不变，只改变 offset。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.setZone('America/Buenos_aires') //=> 2023-12-31T19:00:00.000-03:00
  ```

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.setZone('UTC+7') //=> 2024-01-01T05:00:00.000+07:00
  ```

## _`DateTime`_.**`startOf()`** <a href="#datetimestartof" id="datetimestartof"></a>

**描述：** 将 DateTime 向下舍入到其某个单位的开头，例如月初

**语法：** _`DateTime`_.startOf(unit, opts)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `unit ` (String) - 要舍入到开头的单位。可选值为 <code>year</code>、<code>quarter</code>、<code>month</code>、<code>week</code>、<code>day</code>、<code>hour</code>、<code>minute</code>、<code>second</code> 或 <code>millisecond</code>。
  * `opts ` (Object) - 可选 - 包含会影响输出的选项的 Object。可用属性：
<code>useLocaleWeeks</code> (boolean)：计算一周起点时是否使用 locale。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-03-20T18:49".toDateTime()
  dt.startOf('month') //=> 2024-03-01T00:00
  ```

## _`DateTime`_.**`toISO()`** <a href="#datetimetoiso" id="datetimetoiso"></a>

**描述：** 返回符合 ISO 8601 的 DateTime 字符串表示

**语法：** _`DateTime`_.toISO(opts)

**返回：** String

**类型：** Luxon

**参数：**

  * `opts ` (Object) - 可选 - 配置选项。更多信息请参阅 <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimetoiso”>Luxon docs</a>。

**示例：**

  ```javascript
  $now.toISO() //=> 2024-04-05T18:44:55.525+02:00
  ```

## _`DateTime`_.**`toLocal()`** <a href="#datetimetolocal" id="datetimetolocal"></a>

**描述：** 将 DateTime 转换为 workflow 的本地时区。除非在参数中指定，否则 DateTime 仍表示同一时刻。可在 workflow 设置中设置 workflow 时区。

**语法：** _`DateTime`_.toLocal()

**返回：** DateTime

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000Z".toDateTime()
  dt.toLocal() //=> 2024-01-01T01:00:00.000+01:00, if time zone is Europe/Berlin
  ```

## _`DateTime`_.**`toLocaleString()`** <a href="#datetimetolocalestring" id="datetimetolocalestring"></a>

**描述：** 返回表示该 DateTime 的本地化字符串，即使用与其 locale 对应的语言和格式。如果未指定，则默认使用系统 locale。

**语法：** _`DateTime`_.toLocaleString(formatOpts)

**返回：** String

**类型：** Luxon

**参数：**

  * `formatOpts ` (Object) - 可选 - 渲染配置选项。完整列表请参阅 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat#parameters”>Intl.DateTimeFormat</a>。默认渲染短日期。

**示例：**

  ```javascript
  $now.toLocaleString() //=> '4/30/2024'
  $now.toLocaleString({'dateStyle':'medium', 'timeStyle':'short'}) //=> 'Apr 30, 2024, 10:00 PM'
  // (if in US English locale)
  ```

  ```javascript
  $now.setLocale('de-DE').toLocaleString() //=> '30.4.2024'
  ```

  ```javascript
  $now.toLocaleString({'dateStyle':'short'}) //=> '4/30/2024'
  $now.toLocaleString({'dateStyle':'medium'}) //=> 'Apr 30, 2024'
  $now.toLocaleString({'dateStyle':'long'}) //=> 'April 30, 2024'
  $now.toLocaleString({'dateStyle':'full'}) //=> 'Tuesday, April 30, 2024'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'year':'numeric', 'month':'numeric', 'day':'numeric'}) //=> '4/30/2024'
  $now.toLocaleString({'year':'2-digit', 'month':'2-digit', 'day':'2-digit'}) //=> '04/30/24'
  $now.toLocaleString({'month':'short', 'weekday':'short', 'day':'numeric'}) //=> 'Tue, Apr 30'
  $now.toLocaleString({'month':'long', 'weekday':'long', 'day':'numeric'}) //=> 'Tuesday, April 30'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'timeStyle':'short'}) //=> '10:00 PM'
  $now.toLocaleString({'timeStyle':'medium'}) //=> '10:00:58 PM'
  $now.toLocaleString({'timeStyle':'long'}) //=> '10:00:58 PM GMT+2'
  $now.toLocaleString({'timeStyle':'full'}) //=> '10:00:58 PM Central European Summer Time'
  // (if in US English locale)
  ```

  ```javascript
  $now.toLocaleString({'hour':'numeric', 'minute':'numeric', hourCycle:'h24'}) //=> '22:00'
  $now.toLocaleString({'hour':'2-digit', 'minute':'2-digit', hourCycle:'h12'}) //=> '10:00 PM'
  // (if in US English locale)
  ```

## _`DateTime`_.**`toMillis()`** <a href="#datetimetomillis" id="datetimetomillis"></a>

**描述：** 返回以毫秒为单位的 Unix 时间戳（自 1970 年 1 月 1 日以来经过的毫秒数）

**语法：** _`DateTime`_.toMillis()

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  $now.toMillis() //=> 1712334324677
  ```

## _`DateTime`_.**`toRelative()`** <a href="#datetimetorelative" id="datetimetorelative"></a>

**描述：** 返回相对于现在的时间文本表示，例如 ‘in two days’。默认向下舍入。

**语法：** _`DateTime`_.toRelative(options)

**返回：** String

**类型：** Luxon

**参数：**

  * `options ` (Object) - 可选 - 会影响输出的选项。可用属性：
<code>unit</code> = 默认使用的单位（<code>years</code>、<code>months</code>、<code>days</code> 等）。
<code>locale</code> = 要使用的语言和格式（例如 <code>de</code>、<code>fr</code>）

**示例：**

  ```javascript
  $now.plus(1, 'day').toRelative() //=> "in 1 day"
  ```

  ```javascript
  $now.plus(1, 'day').toRelative({unit:'hours'}) //=> "in 24 hours"
  ```

  ```javascript
  $now.plus(1, 'day').toRelative({locale:'es'}) //=> "dentro de 1 día"
  ```

## _`DateTime`_.**`toSeconds()`** <a href="#datetimetoseconds" id="datetimetoseconds"></a>

**描述：** 返回以秒为单位的 Unix 时间戳（自 1970 年 1 月 1 日以来经过的秒数）

**语法：** _`DateTime`_.toSeconds()

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  $now.toSeconds() //=> 1712334442.372
  ```

## _`DateTime`_.**`toString()`** <a href="#datetimetostring" id="datetimetostring"></a>

**描述：** 返回 DateTime 的字符串表示。类似于 <code>toISO()</code>。如需更多格式化选项，请参阅 <code>format()</code> 或 <code>toLocaleString()</code>。

**语法：** _`DateTime`_.toString()

**返回：** string

**类型：** Luxon

**示例：**

  ```javascript
  $now.toString() //=> 2024-04-05T18:44:55.525+02:00
  ```

## _`DateTime`_.**`toUTC()`** <a href="#datetimetoutc" id="datetimetoutc"></a>

**描述：** 将 DateTime 转换为 UTC 时区。除非在参数中指定，否则 DateTime 仍表示同一时刻。使用 <code>setZone()</code> 可转换为其他时区。

**语法：** _`DateTime`_.toUTC(offset, opts)

**返回：** DateTime

**类型：** Luxon

**参数：**

  * `offset ` (Number) - 可选 - 相对于 UTC 的分钟偏移量
  * `opts ` (Object) - 可选 - 包含会影响输出的选项的 Object。可用属性：
<code>keepCalendarTime</code> (boolean)：是否保持时间不变，只改变 offset。默认为 false。

**示例：**

  ```javascript
  // dt = "2024-01-01T00:00:00.000+02:00".toDateTime()
  dt.toUTC() //=> 2023-12-31T22:00:00.000Z
  ```

## _`DateTime`_.**`weekday`** <a href="#datetimeweekday" id="datetimeweekday"></a>

**描述：** 一周中的日期。1 是星期一，7 是星期日。

**语法：** _`DateTime`_.weekday

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekday //=> 6
  ```

## _`DateTime`_.**`weekdayLong`** <a href="#datetimeweekdaylong" id="datetimeweekdaylong"></a>

**描述：** 文本形式的完整星期名称，例如 'Wednesday'。如果未指定 locale，则默认使用系统 locale。

**语法：** _`DateTime`_.weekdayLong

**返回：** String

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekdayLong //=> 'Saturday'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('de-DE').weekdayLong //=> 'Samstag'
  ```

## _`DateTime`_.**`weekdayShort`** <a href="#datetimeweekdayshort" id="datetimeweekdayshort"></a>

**描述：** 文本形式的星期缩写，例如 'Wed'。如果未指定 locale，则默认使用系统 locale。

**语法：** _`DateTime`_.weekdayShort

**返回：** String

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekdayShort //=> 'Sat'
  ```

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.setLocale('fr-FR').weekdayShort //=> 'sam.'
  ```

## _`DateTime`_.**`weekNumber`** <a href="#datetimeweeknumber" id="datetimeweeknumber"></a>

**描述：** 年中的周数（大约 1-52）

**语法：** _`DateTime`_.weekNumber

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.weekNumber //=> 13
  ```

## _`DateTime`_.**`year`** <a href="#datetimeyear" id="datetimeyear"></a>

**描述：** 年份

**语法：** _`DateTime`_.year

**返回：** Number

**类型：** Luxon

**示例：**

  ```javascript
  // dt = "2024-03-30T18:49".toDateTime()
  dt.year //=> 2024
  ```

## _`DateTime`_.**`zone`** <a href="#datetimezone" id="datetimezone"></a>

**描述：** 与 DateTime 关联的时区

**语法：** _`DateTime`_.zone

**返回：** Object

**类型：** Luxon

**示例：**

  ```javascript
  $now.zone //=> {"zoneName": "Europe/Berlin", "valid": true}
  ```

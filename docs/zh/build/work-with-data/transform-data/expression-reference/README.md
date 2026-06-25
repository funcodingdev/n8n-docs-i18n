---
nodeTitle: Expression reference
originalFilePath: data/expression-reference/index.md
originalUrl: 'https://docs.n8n.io/data/expression-reference'
url: 'https://docs.n8n.io/build/work-with-data/transform-data/expression-reference'
layout:
  description:
    visible: false
---
# Expression 参考 <a href="#expression-reference" id="expression-reference"></a>

下面是一些常用 expression。更完整的列表见下方。

| 类别 | Expression | 描述 |
|---|---|---|
| 访问当前输入 item 数据 | `$json` | 当前 item 的 JSON 数据 |
| | `$json.fieldName` | 当前 item 的字段 |
| | `$binary` | 当前 item 的 binary 数据 |
| 访问前一个 node 的数据 | `$("NodeName").first()` | node 中的第一个 item |
| | `$("NodeName").item` | node 的关联 item。更多信息请参阅 [Item linking](../../reference-data/link-data-items/README.md)。 |
| | `$("NodeName").all()` | node 中的所有 item |
| | `$("NodeName").last()` | node 中的最后一个 item |
| 日期/时间 | `$now` | 当前日期和时间 |
| | `$today` | 今天的日期 |
| | `$now.toFormat("yyyy-MM-dd")` | 将当前日期格式化为字符串 |
| 条件 | `$if(condition, "true", "false")` | 条件为 true 或 false 时返回相应值的辅助函数 |
| | `condition ? true : false` | 三元运算符：条件为 true 时返回一个值，为 false 时返回另一个值 |
| | `$ifEmpty(value, defaultValue)` | 辅助函数接收两个参数，检查第一个参数是否为空，然后返回该参数（如果不为空）或第二个参数（如果第一个参数为空）。如果第一个参数是 `undefined`、`null`、空字符串 `''`、`value.length` 返回 `false` 的数组，或 `Object.keys(value).length` 返回 `false` 的对象，则视为空 |
| String 方法 | `text.toUpperCase()` | 转换为大写 |
| | `text.toLowerCase()` | 转换为小写 |
| | `text.includes("foo")` | 检查文本是否包含搜索词 |
| | `text.extractEmail()` | 从文本中提取 email |
| Array 方法 | `array.length` | 获取数组长度 |
| | `array.join(", ")` | 使用逗号作为分隔符连接数组元素 |
| | `array.filter(x => x <= 20)` | 根据过滤条件筛选数组 item |
| | `array.map(x => x.id)` | 转换数组中的 item |

浏览下方表格，可按数据类型查找作用于该类型的方法。点击方法名称可阅读详细文档。

## Array <a href="#array" id="array"></a>

* [_`Array`_.**`append(elem1, elem2?, ..., elemN?)`**](array.md#arrayappend)

    将新元素添加到数组末尾。类似于 <code>push()</code>，但会返回修改后的数组。建议改用 spread syntax（见示例）。

* [_`Array`_.**`average()`**](array.md#arrayaverage)

    返回数组中数字的平均值。如果存在非数字，则抛出错误。

* [_`Array`_.**`chunk(length)`**](array.md#arraychunk)

    将数组拆分为子数组组成的数组，每个子数组具有给定长度

* [_`Array`_.**`compact()`**](array.md#arraycompact)

    从数组中移除所有空值。<code>null</code>、<code>""</code> 和 <code>undefined</code> 视为空。

* [_`Array`_.**`concat(array2, array3?, ... arrayN?)`**](array.md#arrayconcat)

    将一个或多个数组连接到基础数组末尾

* [_`Array`_.**`difference(otherArray)`**](array.md#arraydifference)

    比较两个数组。返回基础数组中存在、但 <code>otherArray</code> 中不存在的所有元素。

* [_`Array`_.**`filter(function(element, index?, array?), thisValue?)`**](array.md#arrayfilter)

    返回只包含满足条件元素的数组。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。

* [_`Array`_.**`find(function(element, index?, array?), thisValue?)`**](array.md#arrayfind)

    返回数组中第一个满足所提供条件的元素。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。如果找不到匹配项，则返回 <code>undefined</code>。

如果你需要所有匹配元素，请使用 <code>filter()</code>。

* [_`Array`_.**`first()`**](array.md#arrayfirst)

    返回数组的第一个元素

* [_`Array`_.**`includes(element, start?)`**](array.md#arrayincludes)

    如果数组包含指定元素，则返回 <code>true</code>

* [_`Array`_.**`indexOf(element, start?)`**](array.md#arrayindexof)

    返回数组中第一个匹配元素的位置；如果未找到该元素，则返回 -1。位置从 0 开始。

* [_`Array`_.**`intersection(otherArray)`**](array.md#arrayintersection)

    比较两个数组。返回基础数组和另一个数组中都存在的所有元素。

* [_`Array`_.**`isEmpty()`**](array.md#arrayisempty)

    如果数组没有元素或为 <code>null</code>，则返回 <code>true</code>

* [_`Array`_.**`isNotEmpty()`**](array.md#arrayisnotempty)

    如果数组至少有一个元素，则返回 <code>true</code>

* [_`Array`_.**`join(separator?)`**](array.md#arrayjoin)

    将数组的所有元素合并为单个字符串，可选地在每个元素之间加入分隔符。

与 <code>split()</code> 相反。

* [_`Array`_.**`last()`**](array.md#arraylast)

    返回数组的最后一个元素

* [_`Array`_.**`length`**](array.md#arraylength)

    数组中的元素数量

* [_`Array`_.**`map(function(element, index?, array?), thisValue?)`**](array.md#arraymap)

    通过对原数组每个元素应用函数来创建新数组

* [_`Array`_.**`max()`**](array.md#arraymax)

    返回数组中的最大数字。如果存在非数字，则抛出错误。

* [_`Array`_.**`min()`**](array.md#arraymin)

    返回数组中的最小数字。如果存在非数字，则抛出错误。

* [_`Array`_.**`pluck(fieldName1?, fieldName2?, …)`**](array.md#arraypluck)

    返回一个数组，包含数组中每个 Object 的给定字段值。会忽略不是 Object 的数组元素，或没有与所提供字段名匹配 key 的元素。

* [_`Array`_.**`randomItem()`**](array.md#arrayrandomitem)

    从数组中返回一个随机选择的元素

* [_`Array`_.**`reduce(function(prevResult, currentElem, currentIndex?, array?), initResult)`**](array.md#arrayreduce)

    通过对每个元素应用函数，将数组归约为单个值。该函数会将当前元素与前面元素归约得到的结果合并，生成新的结果。

* [_`Array`_.**`removeDuplicates(keys?)`**](array.md#arrayremoveduplicates)

    从数组中移除所有重复出现的元素

* [_`Array`_.**`renameKeys(from, to)`**](array.md#arrayrenamekeys)

    更改数组中所有 Object 的匹配 key（字段名）。通过添加额外参数可重命名多个 key，即 <code>from1, to1, from2, to2, ...</code>。

* [_`Array`_.**`reverse()`**](array.md#arrayreverse)

    反转数组中元素的顺序

* [_`Array`_.**`slice(start, end)`**](array.md#arrayslice)

    返回数组的一部分，从 <code>start</code> 索引开始，到 <code>end</code> 索引之前结束（不包含 <code>end</code>）。索引从 0 开始。

* [_`Array`_.**`smartJoin(keyField, nameField)`**](array.md#arraysmartjoin)

    从 Object 数组创建单个 Object。数组中的每个 Object 为返回的 Object 提供一个字段。数组中的每个 Object 都必须包含一个作为 key 名称的字段和一个作为值的字段。

* [_`Array`_.**`sort(compareFunction(a, b)?)`**](array.md#arraysort)

    重新排序数组元素。按字母顺序排序字符串时不需要参数。排序数字或 Object 时，请参阅示例。

* [_`Array`_.**`sum()`**](array.md#arraysum)

    返回数组中所有数字的总和。如果存在非数字，则抛出错误。

* [_`Array`_.**`toJsonString()`**](array.md#arraytojsonstring)

    将数组转换为 JSON 字符串。等同于 JavaScript 的 <code>JSON.stringify()</code>。

* [_`Array`_.**`toSpliced(start, deleteCount, elem1, ....., elemN)`**](array.md#arraytospliced)

    在给定位置添加和/或移除数组元素。

另请参阅 <code>slice()</code> 和 <code>append()</code>。

* [_`Array`_.**`toString()`**](array.md#arraytostring)

    将数组转换为字符串，值之间用逗号分隔。若要使用其他分隔符，请改用 <code>join()</code>。

* [_`Array`_.**`union(otherArray)`**](array.md#arrayunion)

    连接两个数组，然后移除所有重复项

* [_`Array`_.**`unique()`**](array.md#arrayunique)

    从数组中移除所有重复元素


## BinaryFile <a href="#binaryfile" id="binaryfile"></a>

* [`binaryFile`.**`directory`**](binaryfile.md#binaryfiledirectory)

    文件存储所在目录的路径。适合区分位于不同目录但名称相同的文件。如果 n8n 配置为将文件存储在数据库中，则不会设置。

* [`binaryFile`.**`fileExtension`**](binaryfile.md#binaryfilefileextension)

    附加到文件名后的后缀（例如 <code>txt</code>）

* [`binaryFile`.**`fileName`**](binaryfile.md#binaryfilefilename)

    文件名称，包含扩展名

* [`binaryFile`.**`fileSize`**](binaryfile.md#binaryfilefilesize)

    表示文件大小的字符串

* [`binaryFile`.**`fileType`**](binaryfile.md#binaryfilefiletype)

    表示文件类型的字符串，例如 <code>image</code>。对应 MIME 类型的第一部分。

* [`binaryFile`.**`id`**](binaryfile.md#binaryfileid)

    文件的唯一 ID。当文件存储在磁盘或 S3 等存储服务中时，用于识别文件。

* [`binaryFile`.**`mimeType`**](binaryfile.md#binaryfilemimetype)

    表示文件内容格式的字符串，例如 <code>image/jpeg</code>


## Boolean <a href="#boolean" id="boolean"></a>

* [_`Boolean`_.**`isEmpty()`**](boolean.md#booleanisempty)

    对所有 boolean 返回 <code>false</code>。对 <code>null</code> 返回 <code>true</code>。

* [_`Boolean`_.**`toNumber()`**](boolean.md#booleantonumber)

    将 <code>true</code> 转换为 1，将 <code>false</code> 转换为 0

* [_`Boolean`_.**`toString()`**](boolean.md#booleantostring)

    将 <code>true</code> 转换为字符串 ‘true’，将 <code>false</code> 转换为字符串 ‘false’


## CustomData <a href="#customdata" id="customdata"></a>

* [`$execution.customData`.**`get(key)`**](customdata.md#executioncustomdataget)

    返回存储在给定 key 下的自定义 execution data。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

* [`$execution.customData`.**`getAll()`**](customdata.md#executioncustomdatagetall)

    返回当前 execution 中已设置的所有自定义 data 键值对。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

* [`$execution.customData`.**`set(key, value)`**](customdata.md#executioncustomdataset)

    将自定义 execution data 存储在指定 key 下。可用它按这些数据轻松筛选 execution。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

* [`$execution.customData`.**`setAll(obj)`**](customdata.md#executioncustomdatasetall)

    为 execution 设置多个自定义 data 键值对。可用它按这些数据轻松筛选 execution。<a href="/workflows/executions/custom-executions-data/">更多信息</a>


## Date <a href="#date" id="date"></a>

* [_`Date`_.**`toDateTime()`**](date.md#datetodatetime)

    将 JavaScript Date 转换为 Luxon DateTime。DateTime 包含相同信息，但更易操作。


## DateTime <a href="#datetime" id="datetime"></a>

* [_`DateTime`_.**`day`**](datetime.md#datetimeday)

    月中的日期（1-31）

* [_`DateTime`_.**`diffTo(otherDateTime, unit)`**](datetime.md#datetimediffto)

    返回两个 DateTime 之间的差值，单位为给定 unit

* [_`DateTime`_.**`diffToNow(unit)`**](datetime.md#datetimedifftonow)

    返回当前时刻与该 DateTime 之间的差值，单位为给定 unit。如需文本表示，请改用 <code>toRelative()</code>。

* [_`DateTime`_.**`endOf(unit, opts)`**](datetime.md#datetimeendof)

    将 DateTime 向上舍入到其某个单位的末尾，例如月末

* [_`DateTime`_.**`equals(other)`**](datetime.md#datetimeequals)

    如果两个 DateTime 表示完全相同的时刻且位于同一时区，则返回 <code>true</code>。如需不那么严格的比较，请使用 <code>hasSame()</code>。

* [_`DateTime`_.**`extract(unit?)`**](datetime.md#datetimeextract)

    提取日期或时间的一部分，例如月份，并以数字形式返回。如需提取文本名称，请参阅 <code>format()</code>。

* [_`DateTime`_.**`format(fmt)`**](datetime.md#datetimeformat)

    使用指定格式将 DateTime 转换为字符串。<a href="https://moment.github.io/luxon/#/formatting?id=table-of-tokens">格式化指南</a>。对于常见格式，<code>toLocaleString()</code> 可能更简单。

* [_`DateTime`_.**`hasSame(otherDateTime, unit)`**](datetime.md#datetimehassame)

    如果两个 DateTime 在指定单位上相同，则返回 <code>true</code>。会忽略时区（只比较本地时间），因此必要时请先使用 <code>toUTC()</code>。

* [_`DateTime`_.**`hour`**](datetime.md#datetimehour)

    一天中的小时（0-23）

* [_`DateTime`_.**`isBetween(date1, date2)`**](datetime.md#datetimeisbetween)

    如果 DateTime 位于指定的两个时刻之间，则返回 <code>true</code>

* [_`DateTime`_.**`isInDST`**](datetime.md#datetimeisindst)

    DateTime 是否处于夏令时

* [_`DateTime`_.**`locale`**](datetime.md#datetimelocale)

    DateTime 的 locale，例如 'en-GB'。格式化 DateTime 时会使用该 locale。

* [_`DateTime`_.**`millisecond`**](datetime.md#datetimemillisecond)

    秒中的毫秒（0-999）

* [_`DateTime`_.**`minus(n, unit?)`**](datetime.md#datetimeminus)

    从 DateTime 中减去给定的一段时间

* [_`DateTime`_.**`minute`**](datetime.md#datetimeminute)

    小时中的分钟（0-59）

* [_`DateTime`_.**`month`**](datetime.md#datetimemonth)

    月份（1-12）

* [_`DateTime`_.**`monthLong`**](datetime.md#datetimemonthlong)

    文本形式的完整月份名称，例如 'October'。如果未指定 locale，则默认使用系统 locale。

* [_`DateTime`_.**`monthShort`**](datetime.md#datetimemonthshort)

    文本形式的月份缩写，例如 'Oct'。如果未指定 locale，则默认使用系统 locale。

* [_`DateTime`_.**`plus(n, unit?)`**](datetime.md#datetimeplus)

    向 DateTime 添加给定的一段时间

* [_`DateTime`_.**`quarter`**](datetime.md#datetimequarter)

    年中的季度（1-4）

* [_`DateTime`_.**`second`**](datetime.md#datetimesecond)

    分钟中的秒（0-59）

* [_`DateTime`_.**`set(values)`**](datetime.md#datetimeset)

    为 DateTime 的指定单位分配新值。若要舍入 DateTime，另请参阅 <code>startOf()</code> 和 <code>endOf()</code>。

* [_`DateTime`_.**`setLocale(locale)`**](datetime.md#datetimesetlocale)

    设置 locale，它决定 DateTime 的语言和格式。在生成 DateTime 的文本表示时很有用，例如配合 <code>format()</code> 或 <code>toLocaleString()</code>。

* [_`DateTime`_.**`setZone(zone, opts)`**](datetime.md#datetimesetzone)

    将 DateTime 转换为给定时区。除非在 options 中指定，否则 DateTime 仍表示同一时刻。另请参阅 <code>toLocal()</code> 和 <code>toUTC()</code>。

* [_`DateTime`_.**`startOf(unit, opts)`**](datetime.md#datetimestartof)

    将 DateTime 向下舍入到其某个单位的开头，例如月初

* [_`DateTime`_.**`toISO(opts)`**](datetime.md#datetimetoiso)

    返回符合 ISO 8601 的 DateTime 字符串表示

* [_`DateTime`_.**`toLocal()`**](datetime.md#datetimetolocal)

    将 DateTime 转换为 workflow 的本地时区。除非在参数中指定，否则 DateTime 仍表示同一时刻。可在 workflow 设置中设置 workflow 时区。

* [_`DateTime`_.**`toLocaleString(formatOpts)`**](datetime.md#datetimetolocalestring)

    返回表示该 DateTime 的本地化字符串，即使用与其 locale 对应的语言和格式。如果未指定，则默认使用系统 locale。

* [_`DateTime`_.**`toMillis()`**](datetime.md#datetimetomillis)

    返回以毫秒为单位的 Unix 时间戳（自 1970 年 1 月 1 日以来经过的毫秒数）

* [_`DateTime`_.**`toRelative(options)`**](datetime.md#datetimetorelative)

    返回相对于现在的时间文本表示，例如 ‘in two days’。默认向下舍入。

* [_`DateTime`_.**`toSeconds()`**](datetime.md#datetimetoseconds)

    返回以秒为单位的 Unix 时间戳（自 1970 年 1 月 1 日以来经过的秒数）

* [_`DateTime`_.**`toString()`**](datetime.md#datetimetostring)

    返回 DateTime 的字符串表示。类似于 <code>toISO()</code>。如需更多格式化选项，请参阅 <code>format()</code> 或 <code>toLocaleString()</code>。

* [_`DateTime`_.**`toUTC(offset, opts)`**](datetime.md#datetimetoutc)

    将 DateTime 转换为 UTC 时区。除非在参数中指定，否则 DateTime 仍表示同一时刻。使用 <code>setZone()</code> 可转换为其他时区。

* [_`DateTime`_.**`weekday`**](datetime.md#datetimeweekday)

    一周中的日期。1 是星期一，7 是星期日。

* [_`DateTime`_.**`weekdayLong`**](datetime.md#datetimeweekdaylong)

    文本形式的完整星期名称，例如 'Wednesday'。如果未指定 locale，则默认使用系统 locale。

* [_`DateTime`_.**`weekdayShort`**](datetime.md#datetimeweekdayshort)

    文本形式的星期缩写，例如 'Wed'。如果未指定 locale，则默认使用系统 locale。

* [_`DateTime`_.**`weekNumber`**](datetime.md#datetimeweeknumber)

    年中的周数（大约 1-52）

* [_`DateTime`_.**`year`**](datetime.md#datetimeyear)

    年份

* [_`DateTime`_.**`zone`**](datetime.md#datetimezone)

    与 DateTime 关联的时区


## ExecData <a href="#execdata" id="execdata"></a>

* [`$exec`.**`customData`**](execdata.md#execcustomdata)

    设置和获取自定义 execution data（例如用于筛选 execution）。也可以使用 ‘Execution Data’ node 完成。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

* [`$exec`.**`id`**](execdata.md#execid)

    当前 workflow execution 的 ID

* [`$exec`.**`mode`**](execdata.md#execmode)

    可以是 3 个值之一：<code>test</code>（表示 execution 是通过点击 n8n 中的按钮触发的）或 <code>production</code>（表示 execution 是自动触发的）。运行 workflow 测试时使用 <code>evaluation</code>。

* [`$exec`.**`resumeFormUrl`**](execdata.md#execresumeformurl)

    访问由 <a href="/integrations/builtin/core-nodes/n8n-nodes-base.wait/">’Wait’ node</a> 生成的表单的 URL。

* [`$exec`.**`resumeUrl`**](execdata.md#execresumeurl)

    用于恢复等待在 <a href="/integrations/builtin/core-nodes/n8n-nodes-base.wait/">’Wait’ node</a> 上的 workflow 的 webhook URL。


## HTTPResponse <a href="#httpresponse" id="httpresponse"></a>

* [`$response`.**`body`**](httpresponse.md#responsebody)

    上一次 HTTP 调用中 response 对象的 body。仅在 ‘HTTP Request’ node 中可用

* [`$response`.**`headers`**](httpresponse.md#responseheaders)

    上一次 HTTP 调用返回的 headers。仅在 ‘HTTP Request’ node 中可用。

* [`$response`.**`statusCode`**](httpresponse.md#responsestatuscode)

    上一次 HTTP 调用返回的 HTTP 状态码。仅在 ‘HTTP Request’ node 中可用。

* [`$response`.**`statusMessage`**](httpresponse.md#responsestatusmessage)

    关于 request 状态的可选消息。仅在 ‘HTTP Request’ node 中可用。


## Item <a href="#item" id="item"></a>

* [`$item`.**`binary`**](item.md#itembinary)

    返回该 item 包含的所有 binary 数据

* [`$item`.**`json`**](item.md#itemjson)

    返回该 item 包含的 JSON 数据。<a href="/data/data-structure/">更多信息</a>


## NodeInputData <a href="#nodeinputdata" id="nodeinputdata"></a>

* [`$input`.**`all(branchIndex?, runIndex?)`**](nodeinputdata.md#inputall)

    返回当前 node 的输入 item 数组

* [`$input`.**`first(branchIndex?, runIndex?)`**](nodeinputdata.md#inputfirst)

    返回当前 node 的第一个输入 item

* [`$input`.**`item`**](nodeinputdata.md#inputitem)

    返回当前正在处理的输入 item

* [`$input`.**`last(branchIndex?, runIndex?)`**](nodeinputdata.md#inputlast)

    返回当前 node 的最后一个输入 item

* [`$input`.**`params`**](nodeinputdata.md#inputparams)

    当前 node 的配置设置。这些是你在配置 node 时在 node 内填写的参数（例如它的操作）。


## NodeOutputData <a href="#nodeoutputdata" id="nodeoutputdata"></a>

* [`$()`.**`all(branchIndex?, runIndex?)`**](nodeoutputdata.md#all)

    返回该 node 的输出 item 数组

* [`$()`.**`first(branchIndex?, runIndex?)`**](nodeoutputdata.md#first)

    返回该 node 输出的第一个 item

* [`$()`.**`isExecuted`**](nodeoutputdata.md#isexecuted)

    如果该 node 已执行，则为 <code>true</code>；否则为 <code>false</code>

* [`$()`.**`item`**](nodeoutputdata.md#item)

    返回匹配的 item，即用于在当前 node 中生成当前 item 的那个 item。<a href="/data/data-mapping/data-item-linking/">更多信息</a>

* [`$()`.**`itemMatching(currentItemIndex?)`**](nodeoutputdata.md#itemmatching)

    返回匹配的 item，即用于在当前 node 中生成指定索引 item 的那个 item。<a href="/data/data-mapping/data-item-linking/">更多信息</a>

* [`$()`.**`last(branchIndex?, runIndex?)`**](nodeoutputdata.md#last)

    返回该 node 输出的最后一个 item

* [`$()`.**`params`**](nodeoutputdata.md#params)

    给定 node 的配置设置。这些是你在 node UI 中填写的参数（例如它的操作）。


## Number <a href="#number" id="number"></a>

* [_`Number`_.**`abs()`**](number.md#numberabs)

    返回数字的绝对值，也就是移除任何负号

* [_`Number`_.**`ceil()`**](number.md#numberceil)

    将数字向上舍入到下一个整数

* [_`Number`_.**`floor()`**](number.md#numberfloor)

    将数字向下舍入到最接近的整数

* [_`Number`_.**`format(locale?, options?)`**](number.md#numberformat)

    返回表示该数字的格式化字符串。适合按特定语言或货币格式化。等同于 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat”><code>Intl.NumberFormat()</code></a>。

* [_`Number`_.**`isEmpty()`**](number.md#numberisempty)

    对所有数字返回 <code>false</code>。对 <code>null</code> 返回 <code>true</code>。

* [_`Number`_.**`isEven()`**](number.md#numberiseven)

    如果数字是偶数，则返回 <code>true</code>。如果数字不是整数，则抛出错误。

* [_`Number`_.**`isInteger()`**](number.md#numberisinteger)

    如果数字是整数，则返回 <code>true</code>

* [_`Number`_.**`isOdd()`**](number.md#numberisodd)

    如果数字是奇数，则返回 <code>true</code>。如果数字不是整数，则抛出错误。

* [_`Number`_.**`round(decimalPlaces?)`**](number.md#numberround)

    返回舍入到最接近整数的数字（或舍入到指定小数位数）

* [_`Number`_.**`toBoolean()`**](number.md#numbertoboolean)

    将数字转换为 boolean 值。<code>0</code> 会变为 <code>false</code>；其他所有值会变为 <code>true</code>。

* [_`Number`_.**`toDateTime(format?)`**](number.md#numbertodatetime)

    将数值时间戳转换为 DateTime。如果时间戳不是毫秒格式，必须指定时间戳格式。使用 n8n 中的时区（或 workflow 设置中的时区）。

* [_`Number`_.**`toLocaleString(locales?, options?)`**](number.md#numbertolocalestring)

    返回表示该数字的本地化字符串，即使用与其 locale 对应的语言和格式。如果未指定，则默认使用系统 locale。

* [_`Number`_.**`toString(radix?)`**](number.md#numbertostring)

    将数字转换为简单的文本表示。如需更多格式化选项，请参阅 <code>toLocaleString()</code>。


## Object <a href="#object" id="object"></a>

* [_`Object`_.**`compact()`**](object.md#objectcompact)

    移除所有值为空的字段，即值为 <code>null</code> 或 <code>""</code> 的字段

* [_`Object`_.**`hasField(name)`**](object.md#objecthasfield)

    如果存在名为 <code>name</code> 的字段，则返回 <code>true</code>。只检查顶层 key。比较区分大小写。

* [_`Object`_.**`isEmpty()`**](object.md#objectisempty)

    如果 Object 没有设置任何 key（字段）或为 <code>null</code>，则返回 <code>true</code>

* [_`Object`_.**`isNotEmpty()`**](object.md#objectisnotempty)

    如果 Object 至少设置了一个 key（字段），则返回 <code>true</code>

* [_`Object`_.**`keepFieldsContaining(value)`**](object.md#objectkeepfieldscontaining)

    移除值没有至少部分匹配给定 <code>value</code> 的字段。比较区分大小写。非字符串字段始终会被移除。

* [_`Object`_.**`keys()`**](object.md#objectkeys)

    返回包含该对象所有字段名（key）的数组。等同于 JavaScript 的 <code>Object.keys(obj)</code>。

* [_`Object`_.**`merge(otherObject)`**](object.md#objectmerge)

    将两个 Object 合并为一个。如果两个 Object 中存在同一个 key（字段名），会使用第一个（基础）Object 中的值。

* [_`Object`_.**`removeField(key)`**](object.md#objectremovefield)

    从 Object 中移除一个字段。等同于 JavaScript 的 <code>delete</code>。

* [_`Object`_.**`removeFieldsContaining(value)`**](object.md#objectremovefieldscontaining)

    移除值至少部分匹配给定 <code>value</code> 的 key（字段）。比较区分大小写。非字符串字段始终会被保留。

* [_`Object`_.**`toJsonString()`**](object.md#objecttojsonstring)

    将 Object 转换为 JSON 字符串。类似于 JavaScript 的 <code>JSON.stringify()</code>。

* [_`Object`_.**`urlEncode()`**](object.md#objecturlencode)

    根据 Object 的 key 和 value 生成 URL 参数字符串。仅支持顶层 key。

* [_`Object`_.**`values()`**](object.md#objectvalues)

    返回包含该 Object 所有字段值的数组。等同于 JavaScript 的 <code>Object.values(obj)</code>。


## PrevNodeData <a href="#prevnodedata" id="prevnodedata"></a>

* [**`name`**](prevnodedata.md#name)

    当前输入来源 node 的名称。

如果有多个输入连接器（例如在 ‘Merge’ node 中），始终使用当前 node 的第一个输入连接器。

* [**`outputIndex`**](prevnodedata.md#outputindex)

    当前输入来源的输出连接器索引。当上一个 node 有多个输出时使用它（例如 ‘If’ 或 ‘Switch’ node）。

如果有多个输入连接器（例如在 ‘Merge’ node 中），始终使用当前 node 的第一个输入连接器。

* [**`runIndex`**](prevnodedata.md#runindex)

    生成当前输入的上一个 node 的运行。

如果有多个输入连接器（例如在 ‘Merge’ node 中），始终使用当前 node 的第一个输入连接器。


## Root <a href="#root" id="root"></a>

* [**`$(nodeName)`**](root.md#)

    返回指定 node 的数据

* [**`$binary`**](root.md#binary)

    返回当前 item 上当前 node 的所有 binary 输入数据。<code>$input.item.binary</code> 的简写。

* [**`$execution`**](root.md#execution)

    检索或设置当前 execution 的元数据

* [**`$fromAI(key, description?, type?, defaultValue?)`**](root.md#fromai)

    当 node 参数的值应由大语言模型提供时使用。为获得更好的结果，建议提供描述。

* [**`$if(condition, valueIfTrue, valueIfFalse)`**](root.md#if)

    根据 <code>condition</code> 返回两个值中的一个。类似于 JavaScript 中的 <code>?</code> 运算符。

* [**`$ifEmpty(value, valueIfEmpty)`**](root.md#ifempty)

    如果第一个参数不为空，则返回第一个参数；否则返回第二个参数。以下值会被视为空：<code>””</code>、<code>[]</code>、<code>{}</code>、<code>null</code>、<code>undefined</code>

* [**`$input`**](root.md#input)

    当前 node 的输入数据

* [**`$itemIndex`**](root.md#itemindex)

    当前正在处理的 item 在输入 item 列表中的位置

* [**`$jmespath(obj, expression)`**](root.md#jmespath)

    使用 <a href=”/code/cookbook/jmespath/”>JMESPath</a> expression 从对象（或对象数组）中提取数据。适合查询复杂的嵌套对象。如果 expression 无效，则返回 <code>undefined</code>。

* [**`$json`**](root.md#json)

    返回当前 item 上当前 node 的 JSON 输入数据。<code>$input.item.json</code> 的简写。<a href="/data/data-structure/">更多信息</a>

* [**`$max(num1, num2, …, numN)`**](root.md#max)

    返回给定数字中的最大值

* [**`$min(num1, num2, …, numN)`**](root.md#min)

    返回给定数字中的最小值

* [**`$nodeVersion`**](root.md#nodeversion)

    当前 node 的版本（显示在 node 设置面板底部）

* [**`$now`**](root.md#now)

    表示当前时刻的 DateTime。

使用 workflow 的时区（可在 workflow 设置中更改）。

* [**`$pageCount`**](root.md#pagecount)

    node 已获取的结果页数。仅在 ‘HTTP Request’ node 中可用。

* [**`$parameter`**](root.md#parameter)

    当前 node 的配置设置。这些是你在 node UI 中填写的参数（例如它的操作）。

* [**`$prevNode`**](root.md#prevnode)

    提供当前输入来源的 node 信息。

在 ‘Merge’ node 中，始终使用第一个输入连接器。

* [**`$request`**](root.md#request)

    node 上次运行期间发送的 request 对象。仅在 ‘HTTP Request’ node 中可用。

* [**`$response`**](root.md#response)

    上一次 HTTP 调用返回的 response。仅在 ‘HTTP Request’ node 中可用。

* [**`$runIndex`**](root.md#runindex)

    当前 node execution 的当前运行索引。从 0 开始。

* [**`$secrets`**](root.md#secrets)

    如果已配置，表示来自<a href="/external-secrets/">外部 secrets vault</a> 的 secrets。Secret 值永远不会向用户显示。仅在 credential 字段中可用。

* [**`$today`**](root.md#today)

    表示当前日期起始午夜时刻的 DateTime。

使用实例的时区（除非在 workflow 设置中覆盖）。

* [**`$vars`**](root.md#vars)

    workflow 可用的<a href="/code/variables/">变量</a>

* [**`$workflow`**](root.md#workflow)

    当前 workflow 的信息


## String <a href="#string" id="string"></a>

* [_`String`_.**`base64Encode()`**](string.md#stringbase64decode)

    将纯文本转换为 base64 编码字符串

* [_`String`_.**`base64Encode()`**](string.md#stringbase64encode)

    将 base64 编码字符串转换为纯文本

* [_`String`_.**`concat(string1, string2?, ..., stringN?)`**](string.md#stringconcat)

    将一个或多个字符串连接到基础字符串末尾。也可以使用 <code>+</code> 运算符（见示例）。

* [_`String`_.**`extractDomain()`**](string.md#stringextractdomain)

    如果字符串是 email 地址或 URL，则返回其 domain（如果未找到则返回 <code>undefined</code>）。

如果字符串还包含其他内容，请尝试先使用 <code>extractEmail()</code> 或 <code>extractUrl()</code>。

* [_`String`_.**`extractEmail()`**](string.md#stringextractemail)

    提取字符串中找到的第一个 email。如果没有找到，则返回 <code>undefined</code>。

* [_`String`_.**`extractUrl()`**](string.md#stringextracturl)

    提取字符串中找到的第一个 URL。如果没有找到，则返回 <code>undefined</code>。只识别完整 URL，例如以 <code>http</code> 开头的 URL。

* [_`String`_.**`extractUrlPath()`**](string.md#stringextracturlpath)

    返回 URL 中 domain 后面的部分；如果未找到 URL，则返回 <code>undefined</code>。

如果字符串还包含其他内容，请尝试先使用 <code>extractUrl()</code>。

* [_`String`_.**`hash(algo?)`**](string.md#stringhash)

    返回使用给定算法哈希后的字符串。如果未指定，则默认使用 md5。

* [_`String`_.**`includes(searchString, start?)`**](string.md#stringincludes)

    如果字符串包含 <code>searchString</code>，则返回 <code>true</code>。区分大小写。

* [_`String`_.**`indexOf(searchString, start?)`**](string.md#stringindexof)

    返回 <code>searchString</code> 在基础字符串中首次出现的索引（位置）；如果未找到，则返回 -1。区分大小写。

* [_`String`_.**`isDomain()`**](string.md#stringisdomain)

    如果字符串是 domain，则返回 <code>true</code>

* [_`String`_.**`isEmail()`**](string.md#stringisemail)

    如果字符串是 email，则返回 <code>true</code>

* [_`String`_.**`isEmpty()`**](string.md#stringisempty)

    如果字符串没有字符或为 <code>null</code>，则返回 <code>true</code>

* [_`String`_.**`isNotEmpty()`**](string.md#stringisnotempty)

    如果字符串至少有一个字符，则返回 <code>true</code>

* [_`String`_.**`isNumeric()`**](string.md#stringisnumeric)

    如果字符串表示一个数字，则返回 <code>true</code>

* [_`String`_.**`isUrl()`**](string.md#stringisurl)

    如果字符串是有效 URL，则返回 <code>true</code>

* [_`String`_.**`length`**](string.md#stringlength)

    字符串中的字符数量

* [_`String`_.**`match(regexp)`**](string.md#stringmatch)

    用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>匹配字符串。返回包含第一个匹配项的数组；如果正则表达式设置了 <code>g</code> flag，则返回所有匹配项。如果没有找到匹配项，则返回 <code>null</code>。

如果只是检查文本是否存在，请考虑改用 <code>includes()</code>。

* [_`String`_.**`parseJson()`**](string.md#stringparsejson)

    返回该字符串表示的 JavaScript Object 或值；如果字符串不是有效 JSON，则返回 <code>undefined</code>。不支持单引号 JSON。

* [_`String`_.**`quote(mark?)`**](string.md#stringquote)

    用引号包裹字符串，并转义字符串中已有的任何引号。适合构建 JSON、SQL 等内容。

* [_`String`_.**`removeMarkdown()`**](string.md#stringremovemarkdown)

    移除字符串中的所有 Markdown 格式。也会移除 HTML 标签。

* [_`String`_.**`removeTags()`**](string.md#stringremovetags)

    从字符串中移除标签，例如 HTML 或 XML

* [_`String`_.**`replace(pattern, replacement)`**](string.md#stringreplace)

    返回一个字符串，其中第一次出现的 <code>pattern</code> 被替换为 <code>replacement</code>。

要替换所有出现位置，请改用 <code>replaceAll()</code>。

* [_`String`_.**`replaceAll(pattern, replacement)`**](string.md#stringreplaceall)

    返回一个字符串，其中所有出现的 <code>pattern</code> 都被替换为 <code>replacement</code>

* [_`String`_.**`replaceSpecialChars()`**](string.md#stringreplacespecialchars)

    将字符串中的特殊字符替换为最接近的 ASCII 字符

* [_`String`_.**`search(regexp)`**](string.md#stringsearch)

    返回某个 pattern 在字符串中首次出现的索引（位置）；如果未找到，则返回 -1。pattern 使用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>指定。若要改用文本，请参阅 <code>indexOf()</code>。

* [_`String`_.**`slice(start, end?)`**](string.md#stringslice)

    提取字符串中给定位置的片段。如需更高级的提取，请参阅 <code>match()</code>。

* [_`String`_.**`split(separator?, limit?)`**](string.md#stringsplit)

    将字符串拆分为子字符串数组。每次拆分都在 <code>separator</code> 处进行，输出中不包含 separator。

与对数组使用 <code>join()</code> 相反。

* [_`String`_.**`startsWith(searchString, start?)`**](string.md#stringstartswith)

    如果字符串以 <code>searchString</code> 开头，则返回 <code>true</code>。区分大小写。

* [_`String`_.**`substring(start, end?)`**](string.md#stringsubstring)

    提取字符串中给定位置的片段。如需更高级的提取，请参阅 <code>match()</code>。

* [_`String`_.**`toBoolean()`**](string.md#stringtoboolean)

    将字符串转换为 boolean 值。<code>0</code>、<code>false</code> 和 <code>no</code> 会解析为 <code>false</code>，其他所有值解析为 <code>true</code>。不区分大小写。

* [_`String`_.**`toDateTime()`**](string.md#stringtodatetime)

    将字符串转换为 DateTime。适合进一步转换。支持的字符串格式包括 ISO 8601、HTTP、RFC2822、SQL 和以毫秒为单位的 Unix 时间戳。

如需解析其他格式，请使用 <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimefromformat”> <code>DateTime.fromFormat()</code></a>。

* [_`String`_.**`toJsonString()`**](string.md#stringtojsonstring)

    准备将字符串插入 JSON 对象。会转义任何引号和特殊字符（例如换行符），并用引号包裹字符串。

等同于 JavaScript 的 <code>JSON.stringify()</code>。

* [_`String`_.**`toLowerCase()`**](string.md#stringtolowercase)

    将字符串中的所有字母转换为小写

* [_`String`_.**`toNumber()`**](string.md#stringtonumber)

    将表示数字的字符串转换为数字。如果字符串不是以有效数字开头，则抛出错误。

* [_`String`_.**`toSentenceCase()`**](string.md#stringtosentencecase)

    将字符串的大小写更改为句子大小写。每个句子的首字母大写，其余字母小写。

* [_`String`_.**`toSnakeCase()`**](string.md#stringtosnakecase)

    将字符串格式更改为 snake case。空格和连字符会替换为 <code>_</code>，符号会被移除，所有字母会变为小写。

* [_`String`_.**`toTitleCase()`**](string.md#stringtotitlecase)

    将字符串的大小写更改为 title case。每个单词的首字母大写，其余字母保持不变。短介词和连词不会大写（例如 ‘a’、‘the’）。

* [_`String`_.**`toUpperCase()`**](string.md#stringtouppercase)

    将字符串中的所有字母转换为大写

* [_`String`_.**`trim()`**](string.md#stringtrim)

    移除字符串两端的空白。空白包括换行符、tab、空格等。

* [_`String`_.**`urlDecode(allChars?)`**](string.md#stringurldecode)

    解码 URL 编码字符串。将形式为 <code>%XX</code> 的所有字符码替换为对应字符。

* [_`String`_.**`urlEncode(allChars?)`**](string.md#stringurlencode)

    对字符串进行编码，使其可用于 URL。空格和特殊字符会被替换为 <code>%XX</code> 形式的编码。


## WorkflowData <a href="#workflowdata" id="workflowdata"></a>

* [`$workflow`.**`active`**](workflowdata.md#workflowactive)

    workflow 是否处于 active 状态

* [`$workflow`.**`id`**](workflowdata.md#workflowid)

    workflow ID。也可以在 workflow 的 URL 中找到。

* [`$workflow`.**`name`**](workflowdata.md#workflowname)

    workflow 名称，显示在编辑器顶部

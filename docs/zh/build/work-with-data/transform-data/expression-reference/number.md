---
nodeTitle: Number
originalFilePath: data/expression-reference/number.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/number'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/number
layout:
  description:
    visible: false
---
# Number <a href="#number" id="number"></a>

## _`Number`_.**`abs()`** <a href="#numberabs" id="numberabs"></a>

**描述：** 返回数字的绝对值，也就是移除任何负号

**语法：** _`Number`_.abs()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // x = -1.7
  x.abs() //=> 1.7
  ```

## _`Number`_.**`ceil()`** <a href="#numberceil" id="numberceil"></a>

**描述：** 将数字向上舍入到下一个整数

**语法：** _`Number`_.ceil()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // x = 1.234
  x.ceil() //=> 2
  ```

## _`Number`_.**`floor()`** <a href="#numberfloor" id="numberfloor"></a>

**描述：** 将数字向下舍入到最接近的整数

**语法：** _`Number`_.floor()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // x = 1.234
  x.floor() //=> 1
  ```

## _`Number`_.**`format()`** <a href="#numberformat" id="numberformat"></a>

**描述：** 返回表示该数字的格式化字符串。适合按特定语言或货币格式化。等同于 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat”><code>Intl.NumberFormat()</code></a>。

**语法：** _`Number`_.format(locale?, options?)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `locale` (String) - 可选 - 用于格式化数字的 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl#locales_argument”>locale tag</a>，例如 <code>fr-FR</code>、<code>en-GB</code>、<code>pr-BR</code>
  * `options` (Object) - 可选 - 数字格式化的配置选项。<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat" target="_blank">更多信息</a>

**示例：**

  ```javascript
  // number = 123456.789;
  number.format('de-DE') //=> 123.456,789
  ```

  ```javascript
  // number = 123456.789;
  number.format('de-DE', {'style': 'currency', 'currency': 'EUR'}) //=> 123.456,79 €
  ```

## _`Number`_.**`isEmpty()`** <a href="#numberisempty" id="numberisempty"></a>

**描述：** 对所有数字返回 <code>false</code>。对 <code>null</code> 返回 <code>true</code>。

**语法：** _`Number`_.isEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // num = 10
  num.isEmpty() // => false
  ```

  ```javascript
  // num = 0
  num.isEmpty() // => false
  ```

  ```javascript
  // num = null
  num.isEmpty() // => true
  ```

## _`Number`_.**`isEven()`** <a href="#numberiseven" id="numberiseven"></a>

**描述：** 如果数字是偶数，则返回 <code>true</code>。如果数字不是整数，则抛出错误。

**语法：** _`Number`_.isEven()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // number = 33
  number.isEven() //=> false
  ```

## _`Number`_.**`isInteger()`** <a href="#numberisinteger" id="numberisinteger"></a>

**描述：** 如果数字是整数，则返回 <code>true</code>

**语法：** _`Number`_.isInteger()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // number = 4
  number.isInteger() //=> true
  ```

  ```javascript
  // number = 4.12
  number.isInteger() //=> false
  ```

## _`Number`_.**`isOdd()`** <a href="#numberisodd" id="numberisodd"></a>

**描述：** 如果数字是奇数，则返回 <code>true</code>。如果数字不是整数，则抛出错误。

**语法：** _`Number`_.isOdd()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // number = 33
  number.isOdd() //=> true
  ```

## _`Number`_.**`round()`** <a href="#numberround" id="numberround"></a>

**描述：** 返回舍入到最接近整数的数字（或舍入到指定小数位数）

**语法：** _`Number`_.round(decimalPlaces?)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `decimalPlaces` (Number) - 可选 - 要舍入到的小数位数

**示例：**

  ```javascript
  // number = 1.256
  number.round() //=> 1
  ```

  ```javascript
  // number = 1.256
  number.round(1) //=> 1.3
  number.round(2) //=> 1.26
  ```

## _`Number`_.**`toBoolean()`** <a href="#numbertoboolean" id="numbertoboolean"></a>

**描述：** 将数字转换为 boolean 值。<code>0</code> 会变为 <code>false</code>；其他所有值会变为 <code>true</code>。

**语法：** _`Number`_.toBoolean()

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // number = 12
  number.toBoolean() //=> true
  ```

  ```javascript
  // number = 0
  number.toBoolean() //=> false
  ```

## _`Number`_.**`toDateTime()`** <a href="#numbertodatetime" id="numbertodatetime"></a>

**描述：** 将数值时间戳转换为 DateTime。如果时间戳不是毫秒格式，必须指定时间戳格式。使用 n8n 中的时区（或 workflow 设置中的时区）。

**语法：** _`Number`_.toDateTime(format?)

**返回：** DateTime

**来源：** 自定义 n8n 功能

**参数：**

  * `format` (String) - 可选 - 要转换的时间戳类型。可选值为 <code>ms</code>（Unix 毫秒时间戳）、<code>s</code>（Unix 秒时间戳）或 <code>excel</code>（自 1900 年以来的天数）。

**示例：**

  ```javascript
  // ts = 1708695471
  ts.toDateTime('s') //=> 2024-02-23T14:37:51+01:00
  ```

  ```javascript
  // ts = 1708695471000
  ts.toDateTime('ms') //=> 2024-02-23T14:37:51+01:00
  ```

  ```javascript
  // ts = 45345
  ts.toDateTime('excel') //=> 2024-02-23T01:00:00+01:00
  ```

## _`Number`_.**`toLocaleString()`** <a href="#numbertolocalestring" id="numbertolocalestring"></a>

**描述：** 返回表示该数字的本地化字符串，即使用与其 locale 对应的语言和格式。如果未指定，则默认使用系统 locale。

**语法：** _`Number`_.toLocaleString(locales?, options?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `locales` (String|Array<String>) - 可选 - 要指定的 locale，例如英国英语使用 ‘en-GB’，巴西葡萄牙语使用 ‘pt-BR’。请参阅<a href=”https://www.localeplanet.com/icu/”>完整列表</a>（非官方）。也接受 locale 数组。如果未指定，则默认使用系统 locale。
  * `options` (Object) - 可选 - 包含<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat#parameters”>格式化选项</a>的对象

**示例：**

  ```javascript
  // num = 500000.125
  num.toLocaleString() //=> '500,000.125' (if in US English locale)
  ```

  ```javascript
  // num = 500000.125
  num.toLocaleString('fr-FR') //=> '500 000,125'
  ```

  ```javascript
  // num = 500000.125
  num.toLocaleString('fr-FR', {style:'currency', currency:'EUR'}) //=> '500 000,13 €'
  ```

## _`Number`_.**`toString()`** <a href="#numbertostring" id="numbertostring"></a>

**描述：** 将数字转换为简单的文本表示。如需更多格式化选项，请参阅 <code>toLocaleString()</code>。

**语法：** _`Number`_.toString(radix?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `radix` (Number) - 可选 - 要使用的进制。必须是 2 到 36 之间的整数。例如 <code>2</code> 进制是二进制，<code>16</code> 进制是十六进制。

**示例：**

  ```javascript
  // num = 500000.125
  num.toString() //=> '500000.125'
  ```

  ```javascript
  // num = 500000.125
  num.toString(16) //=> '7a120.2'
  ```

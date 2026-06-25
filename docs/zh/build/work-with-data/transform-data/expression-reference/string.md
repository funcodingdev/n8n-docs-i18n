---
nodeTitle: String
originalFilePath: data/expression-reference/string.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/string'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/string
layout:
  description:
    visible: false
---
# String <a href="#string" id="string"></a>

## _`String`_.**`base64Decode()`** <a href="#stringbase64decode" id="stringbase64decode"></a>

**描述：** 将纯文本转换为 base64 编码字符串

**语法：** _`String`_.base64Encode()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "aGVsbG8=".base64Decode() //=> "hello"
  ```

## _`String`_.**`base64Encode()`** <a href="#stringbase64encode" id="stringbase64encode"></a>

**描述：** 将 base64 编码字符串转换为纯文本

**语法：** _`String`_.base64Encode()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "hello".base64Encode() //=> "aGVsbG8="
  ```

## _`String`_.**`concat()`** <a href="#stringconcat" id="stringconcat"></a>

**描述：** 将一个或多个字符串连接到基础字符串末尾。也可以使用 <code>+</code> 运算符（见示例）。

**语法：** _`String`_.concat(string1, string2?, ..., stringN?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `string1` (String) - 要追加的第一个字符串
  * `string2` (String) - 可选 - 要追加的第二个字符串
  * `stringN` (String) - 可选 - 要追加的第 N 个字符串

**示例：**

  ```javascript
  'sea'.concat('food') //=> 'seafood'
  'sea' + 'food' //=> 'seafood'
  ```

  ```javascript
  'work'.concat('a', 'holic') //=> 'workaholic'
  ```

## _`String`_.**`extractDomain()`** <a href="#stringextractdomain" id="stringextractdomain"></a>

**描述：** 如果字符串是 email 地址或 URL，则返回其 domain（如果未找到则返回 <code>undefined</code>）。

如果字符串还包含其他内容，请尝试先使用 <code>extractEmail()</code> 或 <code>extractUrl()</code>。

**语法：** _`String`_.extractDomain()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "me@example.com".extractDomain() //=> 'example.com'
  ```

  ```javascript
  "http://n8n.io/workflows".extractDomain() //=> 'n8n.io'
  ```

  ```javascript
  "It's me@example.com".extractEmail().extractDomain() //=> 'example.com'
  ```

## _`String`_.**`extractEmail()`** <a href="#stringextractemail" id="stringextractemail"></a>

**描述：** 提取字符串中找到的第一个 email。如果没有找到，则返回 <code>undefined</code>。

**语法：** _`String`_.extractEmail()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "My email is me@example.com".extractEmail() //=> 'me@example.com'
  ```

## _`String`_.**`extractUrl()`** <a href="#stringextracturl" id="stringextracturl"></a>

**描述：** 提取字符串中找到的第一个 URL。如果没有找到，则返回 <code>undefined</code>。只识别完整 URL，例如以 <code>http</code> 开头的 URL。

**语法：** _`String`_.extractUrl()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "Check out http://n8n.io".extractUrl() //=> 'http://n8n.io'
  ```

## _`String`_.**`extractUrlPath()`** <a href="#stringextracturlpath" id="stringextracturlpath"></a>

**描述：** 返回 URL 中 domain 后面的部分；如果未找到 URL，则返回 <code>undefined</code>。

如果字符串还包含其他内容，请尝试先使用 <code>extractUrl()</code>。

**语法：** _`String`_.extractUrlPath()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "http://n8n.io/workflows".extractUrlPath() //=> '/workflows'
  ```

  ```javascript
  "Check out http://n8n.io/workflows".extractUrl().extractUrlPath() //=> '/workflows'
  ```

## _`String`_.**`hash()`** <a href="#stringhash" id="stringhash"></a>

**描述：** 返回使用给定算法哈希后的字符串。如果未指定，则默认使用 md5。

**语法：** _`String`_.hash(algo?)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `algo` (String) - 可选 - 要使用的哈希算法。可选值为 <code>md5</code>、<code>base64</code>、<code>sha1</code>、<code>sha224</code>、<code>sha256</code>、<code>sha384</code>、<code>sha512</code>、<code>sha3</code>、<code>ripemd160</code>

**示例：**

  ```javascript
  "hello".hash() //=> '5d41402abc4b2a76b9719d911017c592'
  ```

## _`String`_.**`includes()`** <a href="#stringincludes" id="stringincludes"></a>

**描述：** 如果字符串包含 <code>searchString</code>，则返回 <code>true</code>。区分大小写。

**语法：** _`String`_.includes(searchString, start?)

**返回：** Boolean

**来源：** JavaScript 函数

**参数：**

  * `searchString` (String) - 要搜索的文本
  * `start` (Number) - 可选 - 开始搜索的位置（索引）

**示例：**

  ```javascript
  'team'.includes('tea') //=> true
  'team'.includes('i') //=> false
  ```

  ```javascript
  // Returns false if the case doesn't match, so consider using .toLowerCase() first
  'team'.includes('Tea') //=> false
  'Team'.toLowerCase().includes('tea') //=> true
  ```

## _`String`_.**`indexOf()`** <a href="#stringindexof" id="stringindexof"></a>

**描述：** 返回 <code>searchString</code> 在基础字符串中首次出现的索引（位置）；如果未找到，则返回 -1。区分大小写。

**语法：** _`String`_.indexOf(searchString, start?)

**返回：** Number

**来源：** JavaScript 函数

**参数：**

  * `searchString` (String) - 要搜索的文本
  * `start` (Number) - 可选 - 开始搜索的位置（索引）

**示例：**

  ```javascript
  'steam'.indexOf('tea') //=> 1
  'steam'.indexOf('i') //=> -1
  ```

  ```javascript
  // Returns -1 if the case doesn't match, so consider using .toLowerCase() first
  'STEAM'.indexOf('tea') //=> -1
  'STEAM'.toLowerCase().indexOf('tea') //=> 1
  ```

## _`String`_.**`isDomain()`** <a href="#stringisdomain" id="stringisdomain"></a>

**描述：** 如果字符串是 domain，则返回 <code>true</code>

**语法：** _`String`_.isDomain()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "n8n.io".isDomain() //=> true
  ```

  ```javascript
  "http://n8n.io".isDomain() //=> false
  ```

  ```javascript
  "hello".isDomain() //=> false
  ```

## _`String`_.**`isEmail()`** <a href="#stringisemail" id="stringisemail"></a>

**描述：** 如果字符串是 email，则返回 <code>true</code>

**语法：** _`String`_.isEmail()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "me@example.com".isEmail() //=> true
  ```

  ```javascript
  "It's me@example.com".isEmail() //=> false
  ```

  ```javascript
  "hello".isEmail() //=> false
  ```

## _`String`_.**`isEmpty()`** <a href="#stringisempty" id="stringisempty"></a>

**描述：** 如果字符串没有字符或为 <code>null</code>，则返回 <code>true</code>

**语法：** _`String`_.isEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "".isEmpty() // => true
  ```

  ```javascript
  "hello".isEmpty() // => false
  ```

## _`String`_.**`isNotEmpty()`** <a href="#stringisnotempty" id="stringisnotempty"></a>

**描述：** 如果字符串至少有一个字符，则返回 <code>true</code>

**语法：** _`String`_.isNotEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "hello".isNotEmpty() // => true
  ```

  ```javascript
  "".isNotEmpty() // => false
  ```

## _`String`_.**`isNumeric()`** <a href="#stringisnumeric" id="stringisnumeric"></a>

**描述：** 如果字符串表示一个数字，则返回 <code>true</code>

**语法：** _`String`_.isNumeric()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "1.2234".isNumeric() // true
  ```

  ```javascript
  "hello".isNumeric() // false
  ```

  ```javascript
  "123E23".isNumeric() // true
  ```

## _`String`_.**`isUrl()`** <a href="#stringisurl" id="stringisurl"></a>

**描述：** 如果字符串是有效 URL，则返回 <code>true</code>

**语法：** _`String`_.isUrl()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "https://n8n.io".isUrl() //=> true
  ```

  ```javascript
  "n8n.io".isUrl() //=> false
  ```

  ```javascript
  "hello".isUrl() //=> false
  ```

## _`String`_.**`length`** <a href="#stringlength" id="stringlength"></a>

**描述：** 字符串中的字符数量

**语法：** _`String`_.length

**返回：** Number

**来源：** JavaScript 函数

**示例：**

  ```javascript
  "hello".length //=> 5
  ```

## _`String`_.**`match()`** <a href="#stringmatch" id="stringmatch"></a>

**描述：** 用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>匹配字符串。返回包含第一个匹配项的数组；如果正则表达式设置了 <code>g</code> flag，则返回所有匹配项。如果没有找到匹配项，则返回 <code>null</code>。

如果只是检查文本是否存在，请考虑改用 <code>includes()</code>。

**语法：** _`String`_.match(regexp)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `regexp` (RegExp) - 包含要查找 pattern 的<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>。如果存在 <code>g</code> flag，会查找多个匹配项（见示例）。

**示例：**

  ```javascript
  // Match all words starting with 'r'
  "rock and roll".match(/r[^ ]*/g) //=> ['rock', 'roll']
  ```

  ```javascript
  // Match first word starting with 'r' (no 'g' flag)
  "rock and roll".match(/r[^ ]*/) //=> ['rock']
  ```

  ```javascript
  // For case-insensitive, add 'i' flag
  "ROCK and roll".match(/r[^ ]*/ig) //=> ['ROCK', 'roll']
  ```

## _`String`_.**`parseJson()`** <a href="#stringparsejson" id="stringparsejson"></a>

**描述：** 返回该字符串表示的 JavaScript Object 或值；如果字符串不是有效 JSON，则返回 <code>undefined</code>。不支持单引号 JSON。

**语法：** _`String`_.parseJson()

**返回：** any

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  '{"name":"Nathan"}'.parseJson() //=> {"name":"Nathan"}
  ```

  ```javascript
  "{'name':'Nathan'}".parseJson() //=> undefined
  ```

  ```javascript
  'hello'.parseJson() //=> undefined
  ```

## _`String`_.**`quote()`** <a href="#stringquote" id="stringquote"></a>

**描述：** 用引号包裹字符串，并转义字符串中已有的任何引号。适合构建 JSON、SQL 等内容。

**语法：** _`String`_.quote(mark?)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `mark` (String) - 可选 - 要使用的引号类型

**示例：**

  ```javascript
  'Nathan says "hi"'.quote() //=> '"Nathan says \"hi\""'
  ```

## _`String`_.**`removeMarkdown()`** <a href="#stringremovemarkdown" id="stringremovemarkdown"></a>

**描述：** 移除字符串中的所有 Markdown 格式。也会移除 HTML 标签。

**语法：** _`String`_.removeMarkdown()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "*bold*, [link]()".removeMarkdown() //=> "bold, link"
  ```

## _`String`_.**`removeTags()`** <a href="#stringremovetags" id="stringremovetags"></a>

**描述：** 从字符串中移除标签，例如 HTML 或 XML

**语法：** _`String`_.removeTags()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "<b>bold</b>, <a>link</a>".removeTags() //=> "bold, link"
  ```

## _`String`_.**`replace()`** <a href="#stringreplace" id="stringreplace"></a>

**描述：** 返回一个字符串，其中第一次出现的 <code>pattern</code> 被替换为 <code>replacement</code>。

要替换所有出现位置，请改用 <code>replaceAll()</code>。

**语法：** _`String`_.replace(pattern, replacement)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `pattern` (String|RegExp) - 要在字符串中替换的 pattern。可以是要匹配的字符串，也可以是<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>。
  * `replacement` (String) - 用于替换的新文本

**示例：**

  ```javascript
  'Red or blue or green'.replace('or', 'and') //=> 'Red and blue or green'
  ```

  ```javascript
  // A global, case-insensitive replacement:
  let text = "Mr Blue has a blue house and a blue car";
  let result = text.replace(/blue/gi, "red");
  ```

  ```javascript
  // A function to return the replacement text:
  let text = "Mr Blue has a blue house and a blue car";
  let result = text.replace(/blue|house|car/i, function (x) {
    return x.toUpperCase();
  });
  ```

## _`String`_.**`replaceAll()`** <a href="#stringreplaceall" id="stringreplaceall"></a>

**描述：** 返回一个字符串，其中所有出现的 <code>pattern</code> 都被替换为 <code>replacement</code>

**语法：** _`String`_.replaceAll(pattern, replacement)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `pattern` (String|RegExp) - 要在字符串中替换的 pattern。可以是要匹配的字符串，也可以是<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>。
  * `replacement` (String|function) - 用于替换的新文本。可以是字符串，也可以是返回字符串的函数（见示例）。

**示例：**

  ```javascript
  'Red or blue or green'.replace('or', 'and') //=> 'Red and blue and green'
  ```

  ```javascript
  // Uppercase any occurrences of 'blue' or 'car'
  // (You must include the 'g' flag when using a regex)

  // text = 'Mr Blue has a blue car'
  text.replaceAll(/blue|car/gi, x => x.toUpperCase()) //=> 'Mr BLUE has a BLUE CAR'

  // Or with traditional function notation:
  text.replaceAll(/blue|car/gi, function(x){return x.toUpperCase()}) //=> 'Mr BLUE has a BLUE CAR'
  ```

## _`String`_.**`replaceSpecialChars()`** <a href="#stringreplacespecialchars" id="stringreplacespecialchars"></a>

**描述：** 将字符串中的特殊字符替换为最接近的 ASCII 字符

**语法：** _`String`_.replaceSpecialChars()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "déjà".replaceSpecialChars() //=> "deja"
  ```

## _`String`_.**`search()`** <a href="#stringsearch" id="stringsearch"></a>

**描述：** 返回某个 pattern 在字符串中首次出现的索引（位置）；如果未找到，则返回 -1。pattern 使用<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>指定。若要改用文本，请参阅 <code>indexOf()</code>。

**语法：** _`String`_.search(regexp)

**返回：** Number

**来源：** JavaScript 函数

**参数：**

  * `regexp` (RegExp) - 包含要查找 pattern 的<a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions”>正则表达式</a>

**示例：**

  ```javascript
  // Pos of first word starting with 'n'
  "Neat n8n node".search(/n[^ ]*/) //=> 5
  ```

  ```javascript
  // Case-insensitive match with 'i'
  // Pos of first word starting with 'n' or 'N'
  "Neat n8n node".search(/n[^ ]*/i) //=> 0
  ```

## _`String`_.**`slice()`** <a href="#stringslice" id="stringslice"></a>

**描述：** 提取字符串中给定位置的片段。如需更高级的提取，请参阅 <code>match()</code>。

**语法：** _`String`_.slice(start, end?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `start` (Number) - 开始位置。位置从 0 开始。负数从字符串末尾开始倒数。
  * `end` (String) - 可选 - 选择到的位置。不包含 end 位置的字符。负数从字符串末尾开始选择。如果省略，则提取到字符串末尾。

**示例：**

  ```javascript
  'Hello from n8n'.slice(0, 5) //=> 'Hello'
  ```

  ```javascript
  'Hello from n8n'.slice(6) //=> 'from n8n'
  ```

  ```javascript
  'Hello from n8n'.slice(-3) //=> 'n8n'
  ```

## _`String`_.**`split()`** <a href="#stringsplit" id="stringsplit"></a>

**描述：** 将字符串拆分为子字符串数组。每次拆分都在 <code>separator</code> 处进行，输出中不包含 separator。

与对数组使用 <code>join()</code> 相反。

**语法：** _`String`_.split(separator?, limit?)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `separator` (String) - 可选 - 用于拆分的字符串（或正则表达式）。如果省略，则返回包含原字符串的数组。
  * `limit` (Number) - 可选 - 要返回的最大数组元素数。如果省略，则返回所有元素。

**示例：**

  ```javascript
  "wind,fire,water".split(",") //=> ['wind', 'fire', 'water']
  ```

  ```javascript
  "me and you and her".split("and") //=> ['me ', ' you ', ' her']
  ```

  ```javascript
  // Split one or more of space, comma and '?' using a regular expression
  "me? you, and her".split(/[ ,?]+/) //=> ['me', 'you', 'and', 'her']
  ```

## _`String`_.**`startsWith()`** <a href="#stringstartswith" id="stringstartswith"></a>

**描述：** 如果字符串以 <code>searchString</code> 开头，则返回 <code>true</code>。区分大小写。

**语法：** _`String`_.startsWith(searchString, start?)

**返回：** Boolean

**来源：** JavaScript 函数

**参数：**

  * `searchString` (String) - 要与基础字符串开头比较的文本
  * `start` (Number) - 可选 - 开始搜索的位置（索引）

**示例：**

  ```javascript
  'team'.startsWith('tea') //=> true
  'team'.startsWith('Tea') //=> false
  ```

  ```javascript
  // Returns false if the case doesn't match, so consider using .toLowerCase() first
  'Team'.toLowerCase().startsWith('tea') //=> true
  ```

## _`String`_.**`substring()`** <a href="#stringsubstring" id="stringsubstring"></a>

**描述：** 提取字符串中给定位置的片段。如需更高级的提取，请参阅 <code>match()</code>。

**语法：** _`String`_.substring(start, end?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `start` (Number) - 开始位置。位置从 0 开始。
  * `end` (String) - 可选 - 选择到的位置。不包含 end 位置的字符。如果省略，则提取到字符串末尾。

**示例：**

  ```javascript
  'Hello from n8n'.substring(0, 5) //=> 'Hello'
  ```

  ```javascript
  'Hello from n8n'.substring(6) //=> 'from n8n'
  ```

## _`String`_.**`toBoolean()`** <a href="#stringtoboolean" id="stringtoboolean"></a>

**描述：** 将字符串转换为 boolean 值。<code>0</code>、<code>false</code> 和 <code>no</code> 会解析为 <code>false</code>，其他所有值解析为 <code>true</code>。不区分大小写。

**语法：** _`String`_.toBoolean()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "true".toBoolean() //=> true
  ```

  ```javascript
  "false".toBoolean() //=> false
  ```

  ```javascript
  "0".toBoolean() //=> false
  ```

  ```javascript
  "hello".toBoolean() //=> true
  ```

## _`String`_.**`toDateTime()`** <a href="#stringtodatetime" id="stringtodatetime"></a>

**描述：** 将字符串转换为 DateTime。适合进一步转换。支持的字符串格式包括 ISO 8601、HTTP、RFC2822、SQL 和以毫秒为单位的 Unix 时间戳。

如需解析其他格式，请使用 <a href=”https://moment.github.io/luxon/api-docs/index.html#datetimefromformat”> <code>DateTime.fromFormat()</code></a>。

**语法：** _`String`_.toDateTime()

**返回：** DateTime

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "2024-03-29T18:06:31.798+01:00".toDateTime()
  ```

  ```javascript
  "Fri, 29 Mar 2024 18:08:01 +0100".toDateTime()
  ```

  ```javascript
  "20240329".toDateTime()
  ```

  ```javascript
  "1711732132990".toDateTime()
  ```

## _`String`_.**`toJsonString()`** <a href="#stringtojsonstring" id="stringtojsonstring"></a>

**描述：** 准备将字符串插入 JSON 对象。会转义任何引号和特殊字符（例如换行符），并用引号包裹字符串。

等同于 JavaScript 的 <code>JSON.stringify()</code>。

**语法：** _`String`_.toJsonString()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // str = 'The "best" colours: red\nbrown'
  str.toJsonString() //=> '"The \\"best\\" colours: red\\nbrown"'
  ```

## _`String`_.**`toLowerCase()`** <a href="#stringtolowercase" id="stringtolowercase"></a>

**描述：** 将字符串中的所有字母转换为小写

**语法：** _`String`_.toLowerCase()

**返回：** String

**来源：** JavaScript 函数

**示例：**

  ```javascript
  "I'm SHOUTing".toLowerCase() //=> "i'm shouting"
  ```

## _`String`_.**`toNumber()`** <a href="#stringtonumber" id="stringtonumber"></a>

**描述：** 将表示数字的字符串转换为数字。如果字符串不是以有效数字开头，则抛出错误。

**语法：** _`String`_.toNumber()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "123".toNumber() //=> 123
  ```

  ```javascript
  "1.23E10".toNumber() //=> 12300000000
  ```

## _`String`_.**`toSentenceCase()`** <a href="#stringtosentencecase" id="stringtosentencecase"></a>

**描述：** 将字符串的大小写更改为句子大小写。每个句子的首字母大写，其余字母小写。

**语法：** _`String`_.toSentenceCase()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "quick! brown FOX".toSentenceCase() //=> "Quick! Brown fox"
  ```

## _`String`_.**`toSnakeCase()`** <a href="#stringtosnakecase" id="stringtosnakecase"></a>

**描述：** 将字符串格式更改为 snake case。空格和连字符会替换为 <code>_</code>，符号会被移除，所有字母会变为小写。

**语法：** _`String`_.toSnakeCase()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "quick brown $FOX".toSnakeCase() //=> "quick_brown_fox"
  ```

## _`String`_.**`toTitleCase()`** <a href="#stringtotitlecase" id="stringtotitlecase"></a>

**描述：** 将字符串的大小写更改为 title case。每个单词的首字母大写，其余字母保持不变。短介词和连词不会大写（例如 ‘a’、‘the’）。

**语法：** _`String`_.toTitleCase()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  "quick a brown FOX".toTitleCase() //=> "Quick a Brown Fox"
  ```

## _`String`_.**`toUpperCase()`** <a href="#stringtouppercase" id="stringtouppercase"></a>

**描述：** 将字符串中的所有字母转换为大写

**语法：** _`String`_.toUpperCase()

**来源：** JavaScript 函数

**示例：**

  ```javascript
  "I'm not angry".toUpperCase() //=> "I'M NOT ANGRY"
  ```

## _`String`_.**`trim()`** <a href="#stringtrim" id="stringtrim"></a>

**描述：** 移除字符串两端的空白。空白包括换行符、tab、空格等。

**语法：** _`String`_.trim()

**返回：** String

**来源：** JavaScript 函数

**示例：**

  ```javascript
  '   lonely   '.trim() //=> 'lonely'
  ```

## _`String`_.**`urlDecode()`** <a href="#stringurldecode" id="stringurldecode"></a>

**描述：** 解码 URL 编码字符串。将形式为 <code>%XX</code> 的所有字符码替换为对应字符。

**语法：** _`String`_.urlDecode(allChars?)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `allChars` (Boolean) - 可选 - 是否解码属于 URI 语法一部分的字符（例如 <code>=</code>、<code>?</code>）

**示例：**

  ```javascript
  "name%3DNathan%20Automat".urlDecode() //=> "name=Nathan Automat"
  ```

  ```javascript
  "name%3DNathan%20Automat".urlDecode(true) //=> "name%3DNathan Automat"
  ```

## _`String`_.**`urlEncode()`** <a href="#stringurlencode" id="stringurlencode"></a>

**描述：** 对字符串进行编码，使其可用于 URL。空格和特殊字符会被替换为 <code>%XX</code> 形式的编码。

**语法：** _`String`_.urlEncode(allChars?)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `allChars` (Boolean) - 可选 - 是否编码属于 URI 语法一部分的字符（例如 <code>=</code>、<code>?</code>）

**示例：**

  ```javascript
  "name=Nathan Automat".urlEncode() //=> "name%3DNathan%20Automat"
  ```

  ```javascript
  "name=Nathan Automat".urlEncode(true) //=> "name=Nathan%20Automat"
  ```

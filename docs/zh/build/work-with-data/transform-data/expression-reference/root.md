---
nodeTitle: Root
originalFilePath: data/expression-reference/root.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/root'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/root
layout:
  description:
    visible: false
---
# Root <a href="#root" id="root"></a>

## **`$()`** <a href="#dollar" id="dollar"></a>

**描述：** 返回指定 node 的数据

**语法：** $(nodeName)

**返回：** NodeData

**来源：** 自定义 n8n 功能

**参数：**

  * `nodeName` (String) - 要检索其数据的 node 名称

## **`$binary`** <a href="#dollarbinary" id="dollarbinary"></a>

**描述：** 返回当前 item 上当前 node 的所有 binary 输入数据。<code>$input.item.binary</code> 的简写。

**语法：** **`$binary`**

**返回：** Array<BinaryFile>

**来源：** 自定义 n8n 功能

## **`$execution`** <a href="#dollarexecution" id="dollarexecution"></a>

**描述：** 检索或设置当前 execution 的元数据

**语法：** **`$execution`**

**返回：** ExecData

**来源：** 自定义 n8n 功能

## **`$fromAI()`** <a href="#dollarfromai" id="dollarfromai"></a>

**描述：** 当 node 参数的值应由大语言模型提供时使用。为获得更好的结果，建议提供描述。

**语法：** $fromAI(key, description?, type?, defaultValue?)

**返回：** any

**来源：** 自定义 n8n 功能

**参数：**

  * `key` (String) - 要获取的字段名称。只能包含字母、数字、下划线和连字符。
  * `description` (String) - 可选 - 用于为模型提供更多上下文，明确它应该返回什么
  * `type` (String) - 可选 - 要返回的值类型。可选值为 <code>string</code>、<code>number</code>、<code>boolean</code>、<code>json</code>、<code>date</code>、<code>datetime</code>。默认为 <code>string</code>。
  * `defaultValue` (any) - 可选 - 如果模型没有返回该 key，则使用这个值

**示例：**

  ```javascript
  // Ask the model to provide a name, and use it here
  $fromAI('name')
  ```

  ```javascript
  // Ask the model to provide the age of the person (as a number with a default value of 18), and use it here
  $fromAI('age', 'The age of the person', 'number', 18)
  ```

  ```javascript
  // Ask the model to provide a boolean signifying whether the person is a student (with default value false), and use it here
  $fromAI('isStudent', 'Is the person a student', 'boolean', false)
  ```

## **`$if()`** <a href="#dollarif" id="dollarif"></a>

**描述：** 根据 <code>condition</code> 返回两个值中的一个。类似于 JavaScript 中的 <code>?</code> 运算符。

**语法：** $if(condition, valueIfTrue, valueIfFalse)

**返回：** any

**来源：** 自定义 n8n 功能

**参数：**

  * `condition` (Boolean) - 要执行的检查。应求值为 <code>true</code> 或 <code>false</code>
  * `valueIfTrue` (any) - 条件为 true 时返回的值
  * `valueIfFalse` (any) - 条件为 false 时返回的值

**示例：**

  ```javascript
  // Return "Good day" if time is before 5pm, otherwise "Good evening"
  $if($now.hour < 17, "Good day", "Good evening")
  ```

  ```javascript
  // $if() calls can be combined:
  // Return "Good morning" if time is before 10am, "Good day" it's before 5pm, otherwise "Good evening"
  $if($now.hour < 10, "Good morning", $if($now.hour < 17, "Good day", "Good evening"))
  ```

## **`$ifEmpty()`** <a href="#dollarifempty" id="dollarifempty"></a>

**描述：** 如果第一个参数不为空，则返回第一个参数；否则返回第二个参数。以下值会被视为空：<code>””</code>、<code>[]</code>、<code>{}</code>、<code>null</code>、<code>undefined</code>

**语法：** $ifEmpty(value, valueIfEmpty)

**返回：** any

**来源：** 自定义 n8n 功能

**参数：**

  * `value` (any) - 若该值不为空，则返回它
  * `valueIfEmpty` (any) - 当 <code>value</code> 为空时返回的值

**示例：**

  ```javascript
  "Hi " + $ifEmpty(name, "there") // e.g. "Hi Nathan" or "Hi there"
  ```

## **`$input`** <a href="#dollarinput" id="dollarinput"></a>

**描述：** 当前 node 的输入数据

**语法：** **`$input`**

**返回：** NodeData

**来源：** 自定义 n8n 功能

## **`$itemIndex`** <a href="#dollaritemindex" id="dollaritemindex"></a>

**描述：** 当前正在处理的 item 在输入 item 列表中的位置

**语法：** **`$itemIndex`**

**返回：** Number

**来源：** 自定义 n8n 功能

## **`$jmespath()`** <a href="#dollarjmespath" id="dollarjmespath"></a>

**描述：** 使用 <a href=”/code/cookbook/jmespath/”>JMESPath</a> expression 从对象（或对象数组）中提取数据。适合查询复杂的嵌套对象。如果 expression 无效，则返回 <code>undefined</code>。

**语法：** $jmespath(obj, expression)

**返回：** any

**来源：** 自定义 n8n 功能

**参数：**

  * `obj` (Object|Array) - 要从中检索数据的 Object 或 Object 数组
  * `expression` (String) - 一个 <a href=”https://jmespath.org/examples.html”>JMESPath expression</a>，定义要从对象中检索的数据

**示例：**

  ```javascript
  data = {
    "people": [
      {
        "age": 20,
        "other": "foo",
        "name": "Bob"
      },
      {
        "age": 25,
        "other": "bar",
        "name": "Fred"
      },
      {
        "age": 30,
        "other": "baz",
        "name": "George"
      }
    ]
  }

  // Get all names, in an array
  {{ $jmespath(data, '[*].name') }} //=> ["Bob", "Fred", "George"]

  // Get the names and ages of everyone under 20
  $jmespath(data, '[?age > `20`].[name, age]') //=> [ ["Fred",25], ["George",30] ]

  // Get the name of the first person under 20
  $jmespath($json.people, '[?age > `20`].name | [0]') //=> Fred
  ```

  ```javascript
  data = {
      "reservations": [
        {
          "id": 1,
          "guests": [
            {
              "name": "Nathan",
              "requirements": {
                "room": "double",
                "meal": "vegetarian"
              }
            },
            {
              "name": "Meg",
              "requirements": {
                "room": "single"
              }
            }
          ]
        },
        {
          "id": 2,
          "guests": [
            {
              "name": "Lex",
              "requirements": {
                "room": "double"
              }
            }
          ]
        }
      ]
    }

  // Get the names of all the guests in each reservation that require a double room
  $jmespath(data, 'reservations[].guests[?requirements.room==`double`].name')
  ```

## **`$json`** <a href="#dollarjson" id="dollarjson"></a>

**描述：** 返回当前 item 上当前 node 的 JSON 输入数据。<code>$input.item.json</code> 的简写。<a href="/data/data-structure/">更多信息</a>

**语法：** **`$json`**

**返回：** Object

**来源：** 自定义 n8n 功能

## **`$max()`** <a href="#dollarmax" id="dollarmax"></a>

**描述：** 返回给定数字中的最大值

**语法：** $max(num1, num2, …, numN)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `num1` (Number) - 要比较的第一个数字
  * `num2` (Number) - 要比较的第二个数字

## **`$min()`** <a href="#dollarmin" id="dollarmin"></a>

**描述：** 返回给定数字中的最小值

**语法：** $min(num1, num2, …, numN)

**返回：** Number

**来源：** 自定义 n8n 功能

**参数：**

  * `num1` (Number) - 要比较的第一个数字
  * `num2` (Number) - 要比较的第二个数字

## **`$nodeVersion`** <a href="#dollarnodeversion" id="dollarnodeversion"></a>

**描述：** 当前 node 的版本（显示在 node 设置面板底部）

**语法：** **`$nodeVersion`**

**返回：** String

**来源：** 自定义 n8n 功能

## **`$now`** <a href="#dollarnow" id="dollarnow"></a>

**描述：** 表示当前时刻的 DateTime。

使用 workflow 的时区（可在 workflow 设置中更改）。

**语法：** **`$now`**

**返回：** DateTime

**来源：** 自定义 n8n 功能

## **`$pageCount`** <a href="#dollarpagecount" id="dollarpagecount"></a>

**描述：** node 已获取的结果页数。仅在 ‘HTTP Request’ node 中可用。

**语法：** **`$pageCount`**

**返回：** Number

**来源：** 自定义 n8n 功能

## **`$parameter`** <a href="#dollarparameter" id="dollarparameter"></a>

**描述：** 当前 node 的配置设置。这些是你在 node UI 中填写的参数（例如它的操作）。

**语法：** **`$parameter`**

**返回：** NodeParams

**来源：** 自定义 n8n 功能

## **`$prevNode`** <a href="#dollarprevnode" id="dollarprevnode"></a>

**描述：** 提供当前输入来源的 node 信息。

在 ‘Merge’ node 中，始终使用第一个输入连接器。

**语法：** **`$prevNode`**

**返回：** PrevNodeData

**来源：** 自定义 n8n 功能

## **`$request`** <a href="#dollarrequest" id="dollarrequest"></a>

**描述：** node 上次运行期间发送的 request 对象。仅在 ‘HTTP Request’ node 中可用。

**语法：** **`$request`**

**返回：** Object

**来源：** 自定义 n8n 功能

## **`$response`** <a href="#dollarresponse" id="dollarresponse"></a>

**描述：** 上一次 HTTP 调用返回的 response。仅在 ‘HTTP Request’ node 中可用。

**语法：** **`$response`**

**返回：** HTTPResponse

**来源：** 自定义 n8n 功能

## **`$runIndex`** <a href="#dollarrunindex" id="dollarrunindex"></a>

**描述：** 当前 node execution 的当前运行索引。从 0 开始。

**语法：** **`$runIndex`**

**返回：** Number

**来源：** 自定义 n8n 功能

## **`$secrets`** <a href="#dollarsecrets" id="dollarsecrets"></a>

**描述：** 如果已配置，表示来自<a href="/external-secrets/">外部 secrets vault</a> 的 secrets。Secret 值永远不会向用户显示。仅在 credential 字段中可用。

**语法：** **`$secrets`**

**返回：** Object

**来源：** 自定义 n8n 功能

## **`$today`** <a href="#dollartoday" id="dollartoday"></a>

**描述：** 表示当前日期起始午夜时刻的 DateTime。

使用实例的时区（除非在 workflow 设置中覆盖）。

**语法：** **`$today`**

**返回：** DateTime

**来源：** 自定义 n8n 功能

## **`$vars`** <a href="#dollarvars" id="dollarvars"></a>

**描述：** workflow 可用的<a href="/code/variables/">变量</a>

**语法：** **`$vars`**

**返回：** Object

**来源：** 自定义 n8n 功能

## **`$workflow`** <a href="#dollarworkflow" id="dollarworkflow"></a>

**描述：** 当前 workflow 的信息

**语法：** **`$workflow`**

**返回：** WorkflowData

**来源：** 自定义 n8n 功能

---
nodeTitle: Customdata
originalFilePath: data/expression-reference/customdata.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/customdata'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/customdata
layout:
  description:
    visible: false
---
# CustomData <a href="#customdata" id="customdata"></a>

## `$execution.customData`.**`get()`** <a href="#dollarexecutioncustomdataget" id="dollarexecutioncustomdataget"></a>

**描述：** 返回存储在给定 key 下的自定义 execution 数据。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

**语法：** `$execution.customData`.get(key)

**返回：** String

**来源：** 自定义 n8n 功能

**参数：**

  * `key` (String) - 存储数据的 key（标识符）

**示例：**

  ```javascript
  // Get the user's email (which was previously stored)
  $execution.customData.get("user_email") //=> "me@example.com"
  ```

## `$execution.customData`.**`getAll()`** <a href="#dollarexecutioncustomdatagetall" id="dollarexecutioncustomdatagetall"></a>

**描述：** 返回当前 execution 中已设置的所有自定义数据键值对。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

**语法：** `$execution.customData`.getAll()

**返回：** Object

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  $execution.customData.getAll() //=> {"user_email": "me@example.com", "id": 1234}
  ```

## `$execution.customData`.**`set()`** <a href="#dollarexecutioncustomdataset" id="dollarexecutioncustomdataset"></a>

**描述：** 将自定义 execution 数据存储在指定 key 下。使用它可以方便地按此数据筛选 execution。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

**语法：** `$execution.customData`.set(key, value)

**来源：** 自定义 n8n 功能

**参数：**

  * `key` (String) - 存储数据的 key（标识符）
  * `value` (String) - 要存储的数据

**示例：**

  ```javascript
  // Store the user's email, to easily retrieve all execs related to that user later
  $execution.customData.set("user_email", "me@example.com")
  ```

## `$execution.customData`.**`setAll()`** <a href="#dollarexecutioncustomdatasetall" id="dollarexecutioncustomdatasetall"></a>

**描述：** 为 execution 设置多个自定义数据键值对。使用它可以方便地按此数据筛选 execution。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

**语法：** `$execution.customData`.setAll(obj)

**来源：** 自定义 n8n 功能

**参数：**

  * `obj` (Object) - 包含要设置数据键值对的 JavaScript 对象

**示例：**

  ```javascript
  $execution.customData.setAll({"user_email": "me@example.com", "id": 1234})
  ```

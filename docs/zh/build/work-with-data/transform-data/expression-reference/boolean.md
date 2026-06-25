---
nodeTitle: Boolean
originalFilePath: data/expression-reference/boolean.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/boolean'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/boolean
layout:
  description:
    visible: false
---
# Boolean <a href="#boolean" id="boolean"></a>

## _`Boolean`_.**`isEmpty()`** <a href="#booleanisempty" id="booleanisempty"></a>

**描述：** 对所有 boolean 返回 <code>false</code>。对 <code>null</code> 返回 <code>true</code>。

**语法：** _`Boolean`_.isEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // bool = true
  bool.isEmpty() // => false
  ```

  ```javascript
  // bool = false
  bool.isEmpty() // => false
  ```

  ```javascript
  // bool = null
  bool.isEmpty() // => true
  ```

## _`Boolean`_.**`toNumber()`** <a href="#booleantonumber" id="booleantonumber"></a>

**描述：** 将 <code>true</code> 转换为 1，将 <code>false</code> 转换为 0

**语法：** _`Boolean`_.toNumber()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  true.toNumber() //=> 1
  ```

  ```javascript
  false.toNumber() //=> 0
  ```

## _`Boolean`_.**`toString()`** <a href="#booleantostring" id="booleantostring"></a>

**描述：** 将 <code>true</code> 转换为字符串 ‘true’，将 <code>false</code> 转换为字符串 ‘false’

**语法：** _`Boolean`_.toString()

**返回：** String

**来源：** JavaScript 函数

**示例：**

  ```javascript
  // bool = true
  bool.toString() //=> 'true'
  ```

  ```javascript
  // bool = false
  bool.toString() //=> 'false'
  ```

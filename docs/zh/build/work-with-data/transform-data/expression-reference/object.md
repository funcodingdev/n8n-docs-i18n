---
nodeTitle: Object
originalFilePath: data/expression-reference/object.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/object'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/object
layout:
  description:
    visible: false
---
# Object <a href="#object" id="object"></a>

## _`Object`_.**`compact()`** <a href="#objectcompact" id="objectcompact"></a>

**描述：** 移除所有值为空的字段，即值为 <code>null</code> 或 <code>""</code> 的字段

**语法：** _`Object`_.compact()

**返回：** Object

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'x':null, 'y':2, 'z':''}
  obj.compact() //=> {'y':2}
  ```

## _`Object`_.**`hasField()`** <a href="#objecthasfield" id="objecthasfield"></a>

**描述：** 如果存在名为 <code>name</code> 的字段，则返回 <code>true</code>。只检查顶层 key。比较区分大小写。

**语法：** _`Object`_.hasField(name)

**返回：** Boolean

**来源：** 自定义 n8n 功能

**参数：**

  * `name` (String) - 要搜索的 key 名称

**示例：**

  ```javascript
  // obj = {'name':'Nathan', 'age':42}
  obj.hasField('name') //=> true
  ```

  ```javascript
  // obj = {'name':'Nathan', 'age':42}
  obj.hasField('Name') //=> false
  obj.hasField('inventedField') //=> false
  ```

## _`Object`_.**`isEmpty()`** <a href="#objectisempty" id="objectisempty"></a>

**描述：** 如果 Object 没有设置任何 key（字段）或为 <code>null</code>，则返回 <code>true</code>

**语法：** _`Object`_.isEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name': 'Nathan'}
  obj.isEmpty() //=> false
  ```

  ```javascript
  // obj = {}
  obj.isEmpty() //=> true
  ```

## _`Object`_.**`isNotEmpty()`** <a href="#objectisnotempty" id="objectisnotempty"></a>

**描述：** 如果 Object 至少设置了一个 key（字段），则返回 <code>true</code>

**语法：** _`Object`_.isNotEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name': 'Nathan'}
  obj.isNotEmpty() //=> true
  ```

  ```javascript
  // obj = {}
  obj.isNotEmpty() //=> false
  ```

## _`Object`_.**`keepFieldsContaining()`** <a href="#objectkeepfieldscontaining" id="objectkeepfieldscontaining"></a>

**描述：** 移除值没有至少部分匹配给定 <code>value</code> 的字段。比较区分大小写。非字符串字段始终会被移除。

**语法：** _`Object`_.keepFieldsContaining(value)

**返回：** Object

**来源：** 自定义 n8n 功能

**参数：**

  * `value` (String) - 值必须包含该文本才会被保留

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
  obj.keepFieldsContaining('Nathan') //=> {'name': 'Mr Nathan'}
  ```

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42 }
  obj.keepFieldsContaining('nathan') //=> {}
  obj.keepFieldsContaining('han') //=> {'name': 'Mr Nathan', 'city':'hanoi'}
  ```

## _`Object`_.**`keys()`** <a href="#objectkeys" id="objectkeys"></a>

**描述：** 返回包含该对象所有字段名（key）的数组。等同于 JavaScript 的 <code>Object.keys(obj)</code>。

**语法：** _`Object`_.keys()

**返回：** Array<String>

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', age: 42 }
  obj.keys() //=> ['name', 'age']
  ```

## _`Object`_.**`merge()`** <a href="#objectmerge" id="objectmerge"></a>

**描述：** 将两个 Object 合并为一个。如果两个 Object 中存在同一个 key（字段名），会使用第一个（基础）Object 中的值。

**语法：** _`Object`_.merge(otherObject)

**返回：** Object

**来源：** 自定义 n8n 功能

**参数：**

  * `otherObject` (Object) - 要与基础 Object 合并的 Object。

**示例：**

  ```javascript
  // obj1 = {'name':'Nathan', 'age': 42}
  // obj2 = {'name':'Jan', 'city': 'hanoi'}
  obj1.merge(obj2) //=> {'name':'Jan', 'city': 'hanoi', 'age':42}
  ```

## _`Object`_.**`removeField()`** <a href="#objectremovefield" id="objectremovefield"></a>

**描述：** 从 Object 中移除一个字段。等同于 JavaScript 的 <code>delete</code>。

**语法：** _`Object`_.removeField(key)

**返回：** Object

**来源：** 自定义 n8n 功能

**参数：**

  * `key` (String) - 要移除的字段名称

**示例：**

  ```javascript
  // obj = {'name':'Nathan', 'city':'hanoi'}
  obj.removeField('name') //=> {'city':'hanoi'}
  ```

## _`Object`_.**`removeFieldsContaining()`** <a href="#objectremovefieldscontaining" id="objectremovefieldscontaining"></a>

**描述：** 移除值至少部分匹配给定 <code>value</code> 的 key（字段）。比较区分大小写。非字符串字段始终会被保留。

**语法：** _`Object`_.removeFieldsContaining(value)

**返回：** Object

**来源：** 自定义 n8n 功能

**参数：**

  * `value` (String) - 值必须包含该文本才会被移除

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  obj.removeFieldsContaining('Nathan') //=> {'city':'hanoi', age: 42}
  ```

  ```javascript
  // obj = {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  obj.removeFieldsContaining('han') //=> {age: 42}
  obj.removeFieldsContaining('nathan') //=> {'name': 'Mr Nathan', 'city':'hanoi', age: 42}
  ```

## _`Object`_.**`toJsonString()`** <a href="#objecttojsonstring" id="objecttojsonstring"></a>

**描述：** 将 Object 转换为 JSON 字符串。类似于 JavaScript 的 <code>JSON.stringify()</code>。

**语法：** _`Object`_.toJsonString()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name':'Nathan', age:42}
  obj.toJsonString() //=> '{"name":"Nathan","age":42}'

  ```

## _`Object`_.**`urlEncode()`** <a href="#objecturlencode" id="objecturlencode"></a>

**描述：** 根据 Object 的 key 和 value 生成 URL 参数字符串。仅支持顶层 key。

**语法：** _`Object`_.urlEncode()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name':'Mr Nathan', 'city':'hanoi'}
  obj.urlEncode() //=> 'name=Mr+Nathan&city=hanoi'
  ```

## _`Object`_.**`values()`** <a href="#objectvalues" id="objectvalues"></a>

**描述：** 返回包含该 Object 所有字段值的数组。等同于 JavaScript 的 <code>Object.values(obj)</code>。

**语法：** _`Object`_.values()

**返回：** Array<String>

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = {'name': 'Mr Nathan', age: 42 }
  obj.values() //=> ['Mr Nathan', 42]
  ```

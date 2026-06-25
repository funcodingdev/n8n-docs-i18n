---
nodeTitle: Array
originalFilePath: data/expression-reference/array.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/array'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/array
layout:
  description:
    visible: false
---
# Array <a href="#array" id="array"></a>

## _`Array`_.**`append()`** <a href="#arrayappend" id="arrayappend"></a>

**描述：** 将新元素添加到数组末尾。类似于 <code>push()</code>，但会返回修改后的数组。建议改用 spread syntax（见示例）。

**语法：** _`Array`_.append(elem1, elem2?, ..., elemN?)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `elem1` (any) - 要追加的第一个元素
  * `elem2` (any) - 可选 - 要追加的第二个元素
  * `elemN` (any) - 可选 - 要追加的第 N 个元素

**示例：**

  ```javascript
  // arr = ['forget', 'me']
  arr.append('not') //=> arr = ['forget', 'me', 'not']
  ```

  ```javascript
  // arr = [9, 0, 2]
  arr.append(1, 0) //=> [9, 0, 2, 1, 0]

  // Consider using spread syntax instead
  [...arr, 1, 0]  //=> [9, 0, 2, 1, 0]
  ```

## _`Array`_.**`average()`** <a href="#arrayaverage" id="arrayaverage"></a>

**描述：** 返回数组中数字的平均值。如果存在非数字，则抛出错误。

**语法：** _`Array`_.average()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = [12, 1, 5]
  arr.average() //=> 6
  ```

## _`Array`_.**`chunk()`** <a href="#arraychunk" id="arraychunk"></a>

**描述：** 将数组拆分为子数组组成的数组，每个子数组具有给定长度

**语法：** _`Array`_.chunk(length)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `length` (Number) - 每个 chunk 中的元素数量

**示例：**

  ```javascript
  // arr = [1, 2, 3, 4, 5, 6]
  arr.chunk(2) //=> [ [1,2], [3,4], [5,6] ]
  ```

## _`Array`_.**`compact()`** <a href="#arraycompact" id="arraycompact"></a>

**描述：** 从数组中移除所有空值。<code>null</code>、<code>""</code> 和 <code>undefined</code> 视为空。

**语法：** _`Array`_.compact()

**返回：** Array

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = [2, null, 1, ""]
  arr.compact() //=> [2, 1]
  ```

## _`Array`_.**`concat()`** <a href="#arrayconcat" id="arrayconcat"></a>

**描述：** 将一个或多个数组连接到基础数组末尾

**语法：** _`Array`_.concat(array2, array3?, ... arrayN?)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `array2` (Array) - 要连接到基础数组末尾的第一个数组
  * `array3` (Array) - 可选 - 要连接到基础数组末尾的第二个数组
  * `arrayN` (Array) - 可选 - 要连接到基础数组末尾的第 N 个数组

**示例：**

  ```javascript
  // arr1 = ['Nathan', 'Jan']
  arr1.concat(['Steve', 'Bill']) // ['Nathan', 'Jan', 'Steve', 'Bill']
  ```

  ```javascript
  // arr1 = [5, 4]
  // arr2 = [100, 101]
  // arr3 = ['a', 'b']
  arr1.concat(arr2, arr3) // [5, 4, 100, 101, 'a', 'b']
  ```

## _`Array`_.**`difference()`** <a href="#arraydifference" id="arraydifference"></a>

**描述：** 比较两个数组。返回基础数组中存在、但 <code>otherArray</code> 中不存在的所有元素。

**语法：** _`Array`_.difference(otherArray)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `otherArray` (Array) - 要与基础数组比较的数组

**示例：**

  ```javascript
  // arr = [1, 2, 3]
  arr.difference([2, 3]) //=> [1]
  ```

## _`Array`_.**`filter()`** <a href="#arrayfilter" id="arrayfilter"></a>

**描述：** 返回只包含满足条件元素的数组。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。

**语法：** _`Array`_.filter(function(element, index?, array?), thisValue?)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `function()` (function) - 对每个数组元素运行的函数。如果返回 <code>true</code>，该元素会被保留。可考虑使用 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions”>arrow function notation</a> 节省空间。
  * `element` (any) - 当前元素的值
  * `index` (Number) - 可选 - 当前元素在数组中的位置（从 0 开始）
  * `array` (Array) - 可选 - 正在处理的数组。很少需要。
  * `thisValue` (any) - 可选 - 作为函数 <code>this</code> 值传入的值。很少需要。

**示例：**

  ```javascript
  // Keep ages over 18 (using arrow function notation):
  // ages = [12, 33, 16, 40]
  ages.filter(age => (age > 18)) //=> [33, 40]
  ```

  ```javascript
  // Keep names under 5 letters long (using arrow function notation):
  // names = ['Nathan', 'Bob', 'Sebastian']
  ages.filter(age => (age.length < 5)) //=> ["Bob"]

  // Or using traditional function notation:
  ages.filter(function(age){return age.length < 5}) //=> ["Bob"]
  ```

  ```javascript
  // Keep numbers at odd indexes
  // nums = [1, 7, 3, 10, 5]
  ages.filter((num, index) => {return index%2 != 0}) //=> [7, 10]
  ```

## _`Array`_.**`find()`** <a href="#arrayfind" id="arrayfind"></a>

**描述：** 返回数组中第一个满足所提供条件的元素。条件是一个返回 <code>true</code> 或 <code>false</code> 的函数。如果找不到匹配项，则返回 <code>undefined</code>。

如果你需要所有匹配元素，请使用 <code>filter()</code>。

**语法：** _`Array`_.find(function(element, index?, array?), thisValue?)

**返回：** any

**来源：** JavaScript 函数

**参数：**

  * `function()` (function) - 对每个数组元素运行的函数。一旦它返回 <code>true</code>，就会返回该元素。可考虑使用 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions”>arrow function notation</a> 节省空间。
  * `element` (any) - 当前元素的值
  * `index` (Number) - 可选 - 当前元素在数组中的位置（从 0 开始）
  * `array` (Array) - 可选 - 当前元素所在的数组。很少需要。
  * `thisValue` (any) - 可选 - 作为函数 <code>this</code> 值传入的值。很少需要。

**示例：**

  ```javascript
  // Find first age over 18 (using arrow function notation):
  // ages = [12, 33, 16, 40]
  ages.find(age => (age > 18)) //=> 33
  ```

  ```javascript
  // Find first name under 5 letters long (using arrow function notation):
  // names = ['Nathan', 'Bob', 'Sebastian']
  ages.find(age => (age.length < 5)) //=> 'Bob'

  // Or using traditional function notation:
  ages.find(function(age){return age.length < 5}) //=> 'Bob'
  ```

## _`Array`_.**`first()`** <a href="#arrayfirst" id="arrayfirst"></a>

**描述：** 返回数组的第一个元素

**语法：** _`Array`_.first()

**返回：** any

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'fox']
  arr.first() //=> 'quick'
  ```

## _`Array`_.**`includes()`** <a href="#arrayincludes" id="arrayincludes"></a>

**描述：** 如果数组包含指定元素，则返回 <code>true</code>

**语法：** _`Array`_.includes(element, start?)

**返回：** Boolean

**来源：** JavaScript 函数

**参数：**

  * `element` (any) - 要在数组中搜索的值
  * `start` (Number) - 可选 - 开始搜索的索引

**示例：**

  ```javascript
  // names = ["Bob", "Bill", "Nat"];
  names.includes("Nat") //=> true
  names.includes("Nathan") //=> false
  ```

## _`Array`_.**`indexOf()`** <a href="#arrayindexof" id="arrayindexof"></a>

**描述：** 返回数组中第一个匹配元素的位置；如果未找到该元素，则返回 -1。位置从 0 开始。

**语法：** _`Array`_.indexOf(element, start?)

**返回：** Number

**来源：** JavaScript 函数

**参数：**

  * `element` (any) - 要查找的值
  * `start` (Number) - 可选 - 开始搜索的索引

**示例：**

  ```javascript
  // names = ["Bob", "Bill", "Nat"];
  names.indexOf("Nat") //=> 2
  ```

  ```javascript
  // names = ["Bob", "Bill", "Nat"];
  names.indexOf("Nathan") //=> -1
  ```

## _`Array`_.**`intersection()`** <a href="#arrayintersection" id="arrayintersection"></a>

**描述：** 比较两个数组。返回基础数组和另一个数组中都存在的所有元素。

**语法：** _`Array`_.intersection(otherArray)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `otherArray` (Array) - 要与基础数组比较的数组

**示例：**

  ```javascript
  // arr = [1, 2]
  arr.intersection([2, 3]) //=> [2]
  ```

## _`Array`_.**`isEmpty()`** <a href="#arrayisempty" id="arrayisempty"></a>

**描述：** 如果数组没有元素或为 <code>null</code>，则返回 <code>true</code>

**语法：** _`Array`_.isEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = []
  arr.isEmpty() //=> true
  ```

  ```javascript
  // arr = ['quick', 'brown', 'fox']
  arr.isEmpty() //=> false
  ```

## _`Array`_.**`isNotEmpty()`** <a href="#arrayisnotempty" id="arrayisnotempty"></a>

**描述：** 如果数组至少有一个元素，则返回 <code>true</code>

**语法：** _`Array`_.isNotEmpty()

**返回：** Boolean

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'fox']
  arr.isNotEmpty() //=> true
  ```

  ```javascript
  // arr = []
  arr.isNotEmpty() //=> false
  ```

## _`Array`_.**`join()`** <a href="#arrayjoin" id="arrayjoin"></a>

**描述：** 将数组的所有元素合并为单个字符串，可选地在每个元素之间加入分隔符。

与 <code>split()</code> 相反。

**语法：** _`Array`_.join(separator?)

**返回：** String

**来源：** JavaScript 函数

**参数：**

  * `separator` (String) - 可选 - 插入到每个元素之间的字符

**示例：**

  ```javascript
  // arr = ['Wind', 'Water', 'Fire']
  a.join(" + ") //=> 'Wind + Water + Fire'
  ```

  ```javascript
  // arr = ['Wind', 'Water', 'Fire']
  a.join() //=> 'Wind,Water,Fire'
  a.join("") //=> 'WindWaterFire'
  ```

## _`Array`_.**`last()`** <a href="#arraylast" id="arraylast"></a>

**描述：** 返回数组的最后一个元素

**语法：** _`Array`_.last()

**返回：** any

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'fox']
  arr.last() //=> 'fox'

  ```

## _`Array`_.**`length`** <a href="#arraylength" id="arraylength"></a>

**描述：** 数组中的元素数量

**语法：** _`Array`_.length

**返回：** Number

**来源：** JavaScript 函数

**示例：**

  ```javascript
  // names = ["Bob", "Bill", "Nat"];
  names.length //=> 3
  ```

## _`Array`_.**`map()`** <a href="#arraymap" id="arraymap"></a>

**描述：** 通过对原数组每个元素应用函数来创建新数组

**语法：** _`Array`_.map(function(element, index?, array?), thisValue?)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `function()` (function) - 对每个数组元素运行的函数。在新数组中，该函数的输出会取代原元素。可考虑使用 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions”>arrow function notation</a> 节省空间。
  * `element` (any) - 当前元素的值
  * `index` (Number) - 可选 - 当前元素在数组中的位置（从 0 开始）
  * `array` (Array) - 可选 - 当前元素所在的数组。很少需要。
  * `thisValue` (any) - 可选 - 作为函数 <code>this</code> 值传入的值。很少需要。

**示例：**

  ```javascript
  // Double all numbers (using arrow function notation):
  // nums = [12, 33, 16]
  nums.map(num => num*2) //=> [24, 66, 32]
  ```

  ```javascript
  // Convert elements to uppercase (using arrow function notation):
  // words = ['hello', 'old', 'chap']
  words.map(word => word.toUpperCase()) //=> ['HELLO', 'OLD', 'CHAP']]

  // Or using traditional function notation:
  words.map(function(word){return word.toUpperCase()}) //=> ['HELLO', 'OLD', 'CHAP']]
  ```

## _`Array`_.**`max()`** <a href="#arraymax" id="arraymax"></a>

**描述：** 返回数组中的最大数字。如果存在非数字，则抛出错误。

**语法：** _`Array`_.max()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = [1, 12, 5]
  arr.max() //=> 12

  ```

## _`Array`_.**`min()`** <a href="#arraymin" id="arraymin"></a>

**描述：** 返回数组中的最小数字。如果存在非数字，则抛出错误。

**语法：** _`Array`_.min()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = [12, 1, 5]
  arr.min() //=> 1
  ```

## _`Array`_.**`pluck()`** <a href="#arraypluck" id="arraypluck"></a>

**描述：** 返回一个数组，包含数组中每个 Object 的给定字段值。会忽略不是 Object 的数组元素，或没有与所提供字段名匹配 key 的元素。

**语法：** _`Array`_.pluck(fieldName1?, fieldName2?, …)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `fieldName1` (String) - 可选 - 要检索其值的第一个 key
  * `fieldName2` (String) - 可选 - 要检索其值的第二个 key

**示例：**

  ```javascript
  // arr = [{'name':'Nathan','age':42},{'name':'Jan','city':'Berlin'}]
  arr.pluck('name') //=> ["Nathan", "Jan"]
  ```

  ```javascript
  // arr = [{'name':'Nathan','age':42},{'name':'Jan','city':'Berlin'}]
  arr.pluck('age') //=> [42]
  ```

## _`Array`_.**`randomItem()`** <a href="#arrayrandomitem" id="arrayrandomitem"></a>

**描述：** 从数组中返回一个随机选择的元素

**语法：** _`Array`_.randomItem()

**返回：** any

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'fox']
  arr.randomItem() //=> 'brown'
  arr.randomItem() //=> 'quick'
  ```

## _`Array`_.**`reduce()`** <a href="#arrayreduce" id="arrayreduce"></a>

**描述：** 通过对每个元素应用函数，将数组归约为单个值。该函数会将当前元素与前面元素归约得到的结果合并，生成新的结果。

**语法：** _`Array`_.reduce(function(prevResult, currentElem, currentIndex?, array?), initResult)

**来源：** JavaScript 函数

**参数：**

  * `function()` (function) - 对每个数组元素运行的函数。接收累积结果和当前元素，并返回新的累积结果。可考虑使用 <a href=”https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions”>arrow function notation</a> 节省空间。
  * `prevResult` (any) - 对前面元素应用函数后得到的累积结果。处理第一个元素时，它会被设置为 <code>initResult</code>（如果未指定，则为第一个数组元素）。
  * `currentElem` (any) - 数组中当前正在处理的值
  * `currentIndex` (Number) - 可选 - 当前元素在数组中的位置（从 0 开始）
  * `array` (Array) - 可选 - 正在处理的数组。很少需要。
  * `initResult` (any) - 可选 - prevResult 的初始值，用于在第一个数组元素上调用函数。如果未指定，它会被设置为第一个数组元素，并且第一次函数调用会从第二个数组元素开始，而不是第一个。

**示例：**

  ```javascript
  // Sum numbers (using arrow function notation):
  // nums = [12, 33, 16]
  nums.reduce((result, num) => (result+num), 0) //=> 61
  ```

  ```javascript
  // Join letters and uppercase (using arrow function notation):
  // chars = ['a', 'b', 'c']
  chars.reduce((result, char) => (result+char.toUpperCase()), '') //=> 'ABC'

  // Or using traditional function notation:
  chars.reduce(function(result, char){return result+char.toUpperCase()}, '') //=> 'ABC'
  ```

## _`Array`_.**`removeDuplicates()`** <a href="#arrayremoveduplicates" id="arrayremoveduplicates"></a>

**描述：** 从数组中移除所有重复出现的元素

**语法：** _`Array`_.removeDuplicates(keys?)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `keys` (String) - 可选 - 用于 Object 数组。一个 key，或用逗号分隔的 key 列表，用于限制检查范围。如果省略，则检查所有 key。

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'quick']
  arr.removeDuplicates() //=> ['quick', 'brown']
  ```

## _`Array`_.**`renameKeys()`** <a href="#arrayrenamekeys" id="arrayrenamekeys"></a>

**描述：** 更改数组中所有 Object 的匹配 key（字段名）。通过添加额外参数可重命名多个 key，即 <code>from1, to1, from2, to2, ...</code>。

**语法：** _`Array`_.renameKeys(from, to)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `from` (String) - 要重命名的 key
  * `to` (String) - 新的 key 名称

**示例：**

  ```javascript
  // arr = [{'name':'bob'},{'name':'meg'}]
  arr.renameKeys('name', 'x') //=> [{"x": "bob"},{"x": "meg"}]]
  ```

## _`Array`_.**`reverse()`** <a href="#arrayreverse" id="arrayreverse"></a>

**描述：** 反转数组中元素的顺序

**语法：** _`Array`_.reverse()

**返回：** Array

**来源：** JavaScript 函数

**示例：**

  ```javascript
  // arr = ['dog', 'bites', 'man']
  arr.reverse() //=> ['man', 'bites', 'dog']
  ```

## _`Array`_.**`slice()`** <a href="#arrayslice" id="arrayslice"></a>

**描述：** 返回数组的一部分，从 <code>start</code> 索引开始，到 <code>end</code> 索引之前结束（不包含 <code>end</code>）。索引从 0 开始。

**语法：** _`Array`_.slice(start, end)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `start` (Number) - 可选 - 开始位置。位置从 0 开始。负数从数组末尾开始倒数。
  * `end` (Number) - 可选 - 选择到的位置。不包含 end 位置的元素。负数从数组末尾开始选择。如果省略，则提取到数组末尾。

**示例：**

  ```javascript
  // arr = [1, 2, 3, 4, 5]
  arr.slice(2, 4) //=> [3, 4]
  ```

  ```javascript
  // arr = [1, 2, 3, 4, 5]
  arr.slice(2) //=> [3, 4, 5]
  ```

  ```javascript
  // arr = [1, 2, 3, 4, 5]
  arr.slice(-2) //=> [4, 5]
  ```

## _`Array`_.**`smartJoin()`** <a href="#arraysmartjoin" id="arraysmartjoin"></a>

**描述：** 从 Object 数组创建单个 Object。数组中的每个 Object 为返回的 Object 提供一个字段。数组中的每个 Object 都必须包含一个作为 key 名称的字段和一个作为值的字段。

**语法：** _`Array`_.smartJoin(keyField, nameField)

**返回：** Object

**来源：** 自定义 n8n 功能

**参数：**

  * `keyField` (String) - 每个 Object 中包含 key 名称的字段
  * `nameField` (String) - 每个 Object 中包含值的字段

**示例：**

  ```javascript
  // arr => [{'field':'age','value':2},{'field':'city','value':'Berlin'}]
  arr.smartJoin('field','value') //=> {"age": 2, "city": "Berlin"}
  ```

## _`Array`_.**`sort()`** <a href="#arraysort" id="arraysort"></a>

**描述：** 重新排序数组元素。按字母顺序排序字符串时不需要参数。排序数字或 Object 时，请参阅示例。

**语法：** _`Array`_.sort(compareFunction(a, b)?)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `compareFunction` (function) - 可选 - 用于比较两个数组元素并返回数字的函数，该数字表示哪个元素排在前面：
<b>Return < 0</b>：<code>a</code> 排在 <code>b</code> 前面
<b>Return 0</b>：<code>a</code> 和 <code>b</code> 相等（顺序不变）
<b>Return > 0</b>：<code>b</code> 排在 <code>a</code> 前面

如果未指定函数，会将所有值转换为字符串并比较其字符编码。
  * `a` (any) - 函数中要比较的第一个元素
  * `b` (any) - 函数中要比较的第二个元素

**示例：**

  ```javascript
  // No need for a param when sorting strings
  // arr = ['d', 'a', 'c', 'b']
  arr.sort() //=> ['a', 'b', 'c', 'd']
  ```

  ```javascript
  // To sort numbers, you must use a function
  // arr = [4, 2, 1, 3]
  arr.sort((a, b) => (a - b)) //=> [1, 2, 3, 4]

  // Or using traditional function notation:
  arr.sort(function(a, b){return a - b}) //=> [1, 2, 3, 4]
  ```

  ```javascript
  // Sort in reverse alphabetical order
  // arr = ['d', 'a', 'c', 'b']
  arr.sort((a, b) => b.localeCompare(a)) //=> ['d', 'c', 'b', 'a']
  ```

  ```javascript
  // Sort array of objects by a property
  // arr = [{name:'Zak'}, {name:'Abe'}, {name:'Bob'}]
  arr.sort((a, b) => a.name.localeCompare(b.name)) //=> [{name:'Abe'}, {name:'Bob'}, {name:'Zak'}]
  ```

## _`Array`_.**`sum()`** <a href="#arraysum" id="arraysum"></a>

**描述：** 返回数组中所有数字的总和。如果存在非数字，则抛出错误。

**语法：** _`Array`_.sum()

**返回：** Number

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = [12, 1, 5]
  arr.sum() //=> 18
  ```

## _`Array`_.**`toJsonString()`** <a href="#arraytojsonstring" id="arraytojsonstring"></a>

**描述：** 将数组转换为 JSON 字符串。等同于 JavaScript 的 <code>JSON.stringify()</code>。

**语法：** _`Array`_.toJsonString()

**返回：** String

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // obj = ['quick', 'brown', 'fox']
  obj.toJsonString() //=> '["quick","brown","fox"]'
  ```

## _`Array`_.**`toSpliced()`** <a href="#arraytospliced" id="arraytospliced"></a>

**描述：** 在给定位置添加和/或移除数组元素。

另请参阅 <code>slice()</code> 和 <code>append()</code>。

**语法：** _`Array`_.toSpliced(start, deleteCount, elem1, ....., elemN)

**返回：** Array

**来源：** JavaScript 函数

**参数：**

  * `start` (Number) - 要添加或移除元素的索引（位置）。新元素会插入到该索引处元素之前。负索引从数组末尾开始倒数。
  * `deleteCount` (Number) - 可选 - 要移除的元素数量。如果省略，则移除从 <code>start</code> 索引开始的所有元素。
  * `elem1` (any) - 可选 - 要添加的第一个新元素
  * `elem2` (any) - 可选 - 要添加的第二个新元素
  * `elemN` (any) - 可选 - 要添加的第 N 个新元素

**示例：**

  ```javascript
  // Insert element at index 1
  // months = ['Jan', 'Mar']
  months.toSpliced(1, 0, "Feb") // ['Jan', 'Feb', 'Mar']
  ```

  ```javascript
  // Delete 2 elements starting at index 1
  // arr = ["don't", "make", "me", "do", "this"]
  arr.toSpliced(1, 2) // ["don't", "do", "this"]
  ```

  ```javascript
  // Replace 2 elements starting at index 1
  // arr = ["don't", "be", "evil"]
  arr.toSpliced(1, 2, 'eat', 'slugs') // ["don't", "eat", "slugs"]
  ```

## _`Array`_.**`toString()`** <a href="#arraytostring" id="arraytostring"></a>

**描述：** 将数组转换为字符串，值之间用逗号分隔。若要使用其他分隔符，请改用 <code>join()</code>。

**语法：** _`Array`_.toString()

**返回：** String

**来源：** JavaScript 函数

**示例：**

  ```javascript
  // words = ['make', 'my', 'day']
  words.toString() //=> 'make,my,day'
  ```

## _`Array`_.**`union()`** <a href="#arrayunion" id="arrayunion"></a>

**描述：** 连接两个数组，然后移除所有重复项

**语法：** _`Array`_.union(otherArray)

**返回：** Array

**来源：** 自定义 n8n 功能

**参数：**

  * `otherArray` (Array) - 要与基础数组合并取并集的数组

**示例：**

  ```javascript
  // arr = [1, 2]
  arr.union([2, 3]) //=> [1, 2, 3]

  ```

## _`Array`_.**`unique()`** <a href="#arrayunique" id="arrayunique"></a>

**描述：** 从数组中移除所有重复元素

**语法：** _`Array`_.unique()

**返回：** Array

**来源：** 自定义 n8n 功能

**示例：**

  ```javascript
  // arr = ['quick', 'brown', 'quick']
  arr.unique() //=> ['quick', 'brown']
  ```

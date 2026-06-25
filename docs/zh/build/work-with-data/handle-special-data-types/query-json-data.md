---
title: 使用 JMESPath 查询 JSON
description: >-
  n8n 支持 JMESPath 库，用于简化 JSON 格式数据处理。
contentType: howto
nodeTitle: Query JSON data
originalFilePath: data/specific-data-types/jmespath.md
originalUrl: 'https://docs.n8n.io/data/specific-data-types/jmespath'
url: >-
  https://docs.n8n.io/build/work-with-data/handle-special-data-types/query-json-data
layout:
  description:
    visible: false
---

# 使用 JMESPath 查询 JSON <a href="#query-json-with-jmespath" id="query-json-with-jmespath"></a>

[JMESPath](https://jmespath.org/) 是一种 JSON 查询语言，可用于从 JSON 文档中提取和转换元素。有关 JMESPath 用法的完整详情，请参阅 [JMESPath documentation](https://jmespath.org/tutorial.html)。


## `jmespath()` 方法 <a href="#the-jmespath-method" id="the-jmespath-method"></a>

n8n 提供自定义方法 `jmespath()`。使用此方法可以通过 JMESPath 查询语言搜索 JSON 对象。

基本语法如下：

{% tabs %}
{% tab title="JavaScript" %}
```js
$jmespath(object, searchString)
```
{% endtab %}

{% tab title="Python" %}
```python
_jmespath(object, searchString)
```
{% endtab %}
{% endtabs %}

为了帮助理解此方法的作用，下面是等价的较长 JavaScript 写法：


```js
var jmespath = require('jmespath');
jmespath.search(object, searchString);
```

{% hint style="info" %}
**Expressions 必须是单行**

较长代码示例不能在 Expressions 中工作，因为 expression 必须是单行。
{% endhint %}

`object` 是 JSON 对象，例如前序 node 的输出。`searchString` 是用 JMESPath 查询语言编写的 expression。[JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification) 提供了支持的 expression 列表，其 [Tutorial](https://jmespath.org/tutorial.html) 和 [Examples](https://jmespath.org/examples.html) 提供了交互式示例。

{% hint style="warning" %}
**Search 参数顺序**

[JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification) 中的示例遵循 `search(searchString, object)` 模式。n8n 使用的 [JMESPath JavaScript library](https://github.com/jmespath/jmespath.js/) 则支持 `search(object, searchString)`。这意味着使用 JMESPath 文档中的示例时，你可能需要更改 search 函数参数的顺序。
{% endhint %}

## 常见任务 <a href="#common-tasks" id="common-tasks"></a>

本节提供一些常见操作示例。更多示例和详细指南可在 [JMESPath 自身文档](https://jmespath.org/tutorial.html)中查看。

尝试这些示例时，需要将 Code node 的 **Mode** 设置为 **Run Once for Each Item**。

### 使用 projection 将 JMESPath expression 应用于元素集合 <a href="#apply-a-jmespath-expression-to-a-collection-of-elements-with-projections" id="apply-a-jmespath-expression-to-a-collection-of-elements-with-projections"></a>

来自 [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections)：

> Projections 是 JMESPath 的关键功能之一。可用它将 expression 应用于元素集合。JMESPath 支持五种 projection：
>
> * List Projections
> * Slice Projections
> * Object Projections
> * Flatten Projections
> * Filter Projections

以下示例展示 list、slice 和 object projections 的基本用法。有关每种 projection 类型的详细解释和更多示例，请参阅 [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections)。

给定来自 webhook node 的以下 JSON：


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


检索所有人的 first name [list](https://jmespath.org/tutorial.html#list-and-slice-projections)：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$jmespath($json.body.people, "[*].first" )}}
// Returns ["James", "Jacob", "Jayden"]
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let firstNames = $jmespath($json.body.people, "[*].first" )
return {firstNames};
/* Returns:
[
	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code node (Python)" %}
```python
firstNames = _jmespath(_json.body.people, "[*].first" )
return {"firstNames":firstNames}
"""
Returns:
[
	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

获取 first name 的 [slice](https://jmespath.org/tutorial.html#list-and-slice-projections)：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$jmespath($json.body.people, "[:2].first")}}
// Returns ["James", "Jacob"]
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let firstTwoNames = $jmespath($json.body.people, "[:2].first");
return {firstTwoNames};
/* Returns:
[
	{
		"firstNames": [
			"James",
			"Jacob",
			"Jayden"
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code node (Python)" %}
```python
firstTwoNames = _jmespath(_json.body.people, "[:2].first" )
return {"firstTwoNames":firstTwoNames}
"""
Returns:
[
	{
		"firstTwoNames": [
		"James",
		"Jacob"
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

使用 [object projections](https://jmespath.org/tutorial.html#object-projections) 获取 dogs 年龄列表：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$jmespath($json.body.dogs, "*.age")}}
// Returns [7,5]
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let dogsAges = $jmespath($json.body.dogs, "*.age");
return {dogsAges};
/* Returns:
[
	{
		"dogsAges": [
			7,
			5
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code node (Python)" %}
```python
dogsAges = _jmespath(_json.body.dogs, "*.age")
return {"dogsAges": dogsAges}
"""
Returns:
[
	{
		"dogsAges": [
			7,
			5
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

### 选择多个元素并创建新 list 或 object <a href="#select-multiple-elements-and-create-a-new-list-or-object" id="select-multiple-elements-and-create-a-new-list-or-object"></a>

使用 [Multiselect](https://jmespath.org/tutorial.html#multiselect) 从 JSON object 中选择元素，并将它们组合为新的 list 或 object。

给定来自 webhook node 的以下 JSON：


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


使用 multiselect list 获取 first 和 last name，并创建包含两个 name 的新 list：

{% tabs %}
{% tab title="Expressions (JavaScript)" %}
```js
{{$jmespath($json.body.people, "[].[first, last]")}}
// Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]
```
{% endtab %}

{% tab title="Code node (JavaScript)" %}
```js
let newList = $jmespath($json.body.people, "[].[first, last]");
return {newList};
/* Returns:
[
	{
		"newList": [
			[
				"James",
				"Green"
			],
			[
				"Jacob",
				"Jones"
			],
			[
				"Jayden",
				"Smith"
			]
		]
	}
]
*/
```
{% endtab %}

{% tab title="Code node (Python)" %}
```python
newList = _jmespath(_json.body.people, "[].[first, last]")
return {"newList":newList}
"""
Returns:
[
	{
		"newList": [
			[
				"James",
				"Green"
			],
			[
				"Jacob",
				"Jones"
			],
			[
				"Jayden",
				"Smith"
			]
		]
	}
]
"""
```
{% endtab %}
{% endtabs %}

### Expression 中 arrow function 的替代方案 <a href="#an-alternative-to-arrow-functions-in-expressions" id="an-alternative-to-arrow-functions-in-expressions"></a>

例如，通过从 Code node 返回以下代码生成一些输入数据：

```js
return[
  {
    "json": {
      "num_categories": "0",
      "num_products": "45",
      "category_id": 5529735,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "HP",
      "description": "",
      "image": ""
    }
  },
  {
    "json": {
      "num_categories": "0",
      "num_products": "86",
      "category_id": 5529740,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "Lenovo",
      "description": "",
      "image": ""
    }
  }
]
```

你可以执行类似“查找名称为 Lenovo 的 item，并告诉我它们的 category ID”的搜索。

```js
{{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}
```

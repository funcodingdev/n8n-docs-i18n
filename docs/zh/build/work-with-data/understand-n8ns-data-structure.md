---
contentType: explanation
nodeTitle: Understand n8n's data structure
originalFilePath: data/data-structure.md
originalUrl: 'https://docs.n8n.io/data/data-structure'
url: 'https://docs.n8n.io/build/work-with-data/understand-n8ns-data-structure'
layout:
  description:
    visible: false
---

# n8n 如何组织数据 <a href="#how-n8n-structures-data" id="how-n8n-structures-data"></a>

理解 n8n 如何组织数据并在 node 之间传递数据，是构建工作流的基础。本指南同时介绍数据结构格式，以及数据如何流经工作流。

## 数据结构 <a href="#data-structure" id="data-structure"></a>

在 n8n 中，node 之间传递的所有数据都是对象数组。其结构如下：

```json
[
	{
		// For most data:
		// Wrap each item in another object, with the key 'json'
		"json": {
			// Example data
			"apple": "beets",
			"carrot": {
				"dill": 1
			}
		},
		// For binary data:
		// Wrap each item in another object, with the key 'binary'
		"binary": {
			// Example data
			"apple-picture": {
				"data": "....", // Base64 encoded binary data (required)
				"mimeType": "image/png", // Best practice to set if possible (optional)
				"fileExtension": "png", // Best practice to set if possible (optional)
				"fileName": "example.png", // Best practice to set if possible (optional)
			}
		}
	},
]
```

{% hint style="info" %}
**省略 `json` key 和数组语法**

从 0.166.0 起，使用 Function node 或 Code node 时，如果缺少 `json` key，n8n 会自动添加。如果需要，它也会自动将 item 包装到数组（`[]`）中。只有使用 Function 或 Code node 时才会这样。构建自己的 node 时，你仍必须确保 node 返回带有 `json` key 的数据。
{% endhint %}

## 数据如何在 node 内流动 <a href="#how-data-flows-within-nodes" id="how-data-flows-within-nodes"></a>

在工作流中连接 node 后，数据会自动从一个 node 传递到下一个 node。

Node 会自动处理多个 item。当 node 收到 data item 数组时，它会逐个处理每个 item，并对每个 item 执行已配置的操作。

例如，如果你将 Trello node 设置为 `Create-Card`，并创建一个 expression，使用传入数据中名为 `name-input-value` 的属性设置 `Name`，该 node 会为每个 item 创建一张卡片，并始终选择当前 item 的 `name-input-value`。

例如，以下输入会创建两张卡片。一张名为 `test1`，另一张名为 `test2`：

```json
[
	{
		"name-input-value": "test1"
	},
	{
		"name-input-value": "test2"
	}
]
```

## 理解拖放映射的内容 <a href="#understand-what-youre-mapping-with-drag-and-drop" id="understand-what-youre-mapping-with-drag-and-drop"></a>

Data mapping 会映射字段路径，并加载字段值。例如，给定以下数据：

```js
[
	{
		"fruit": "apples",
		"color": "green"
	}
]
```

你可以将 **fruit** 从 **INPUT** 拖放到要使用其值的字段中，从而映射 `fruit`。这会创建一个 expression：`{{ $json.fruit }}`。当 node 遍历输入 item 时，该字段的值会变成每个 item 的 `fruit` 值。

## 理解嵌套数据 <a href="#understand-nested-data" id="understand-nested-data"></a>

给定以下数据：

```js
[
  {
    "name": "First item",
    "nested": {
      "example-number-field": 1,
      "example-string-field": "apples"
    }
  },
  {
    "name": "Second item",
    "nested": {
      "example-number-field": 2,
      "example-string-field": "oranges"
    }
  }
]
```

n8n 会以如下表格形式显示它：

!["INPUT 面板中表格的截图。它包含一个名为 nested 的顶级字段。该字段包含嵌套数据，并以粗体显示。"](../../../build/.gitbook/assets/nested-data.png)

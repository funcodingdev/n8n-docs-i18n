---
contentType: explanation
nodeTitle: Expressions for data transformation
originalFilePath: data/expressions-for-transformation.md
originalUrl: 'https://docs.n8n.io/data/expressions-for-transformation'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expressions-for-data-transformation
layout:
  description:
    visible: false
---

# 用于数据转换的 expressions <a href="#expressions-for-data-transformation" id="expressions-for-data-transformation"></a>

在 n8n 中，任何支持 expression 的地方都可以使用 expression transformation functions。

不过，如果你的主要目标是使用 expression 转换数据，而不执行其他操作，请使用 **Edit Fields (Set)** node。此 node 专为数据转换设计，提供清晰界面以：

* 添加基于 expression 值的新字段
* 使用 transformation functions 修改现有字段值
* 删除或重命名字段

这会将数据转换与业务逻辑分离，让工作流保持有序，更易理解和维护。

**最佳实践**：不要在多个 node 的多个参数中添加复杂 expression，而是先使用 Edit Fields 准备数据，然后将转换后的数据传递给后续 node。

![在 UI 中创建 expressions](../../../../build/.gitbook/assets/expressionDot.gif)

更多信息和示例请参阅 [Expression reference](expression-reference/README.md)。

### 示例：从 webhook body 获取数据 <a href="#example-get-data-from-webhook-body" id="example-get-data-from-webhook-body"></a>

考虑以下场景：你有一个 webhook trigger，它通过 webhook body 接收数据。你想提取其中一部分数据供工作流使用。

你的 webhook 数据类似如下：


```json
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "name": "Jim",
      "age": 30,
      "city": "New York"
    }
  }
]
```


在工作流的下一个 node 中，你只想获取 `city` 的值。可以使用以下 expression：


```js
{{$json.body.city}}
```

此 expression：

1. 使用 n8n 自定义 `$json` 变量访问传入的 JSON 格式数据。
2. 找到 `city` 的值（在此示例中为 "New York"）。请注意，此示例使用 JMESPath 语法查询 JSON 数据。你也可以将此 expression 写成 `{{$json['body']['city']}}`。

### 在 credential 中使用 expressions <a href="#using-expressions-in-credentials" id="using-expressions-in-credentials"></a>

你也可以在 credential 字段中使用 expression。当你使用 expression 引用数据时（例如 `{{$json.body.city}}` 或 `{{ $('Webhook').item.json.headers.authorization }}`），n8n 会在当前 workflow execution 的上下文中计算该 expression。

这意味着：

- Credential 中的 expression 可以访问当前 execution 上下文中可用的数据，包括来自前序 node 的数据。
- 每次 workflow execution 都有自己的数据上下文。
- Expression 会按 execution 计算，因此不同 execution 不共享数据。

例如，如果 webhook node 收到 access token，而你在 credential 字段中使用 expression 引用它，该值会使用该特定工作流运行的 execution 数据解析。

## 示例：将较长 JavaScript 写成 expression <a href="#example-writing-longer-javascript-as-expressions" id="example-writing-longer-javascript-as-expressions"></a>

你可以在 expression 中执行变量赋值或多条语句，但需要使用立即调用函数表达式（IIFE）的语法包装代码。

以下代码使用 Luxon 日期时间库计算两个日期之间相差的月数。我们同时用 expression 的花括号和 IIFE 语法包裹代码。

```js
{{(()=>{
  let end = DateTime.fromISO('2017-03-13');
  let start = DateTime.fromISO('2017-02-13');
  let diffInMonths = end.diff(start, 'months');
  return diffInMonths.toObject();
})()}}
```

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是一些与 [expressions](../expressions-versus-data-nodes.md) 相关的常见错误和问题，以及解决或排查步骤。

### item 0 中的 'JSON Output' 包含无效 JSON <a href="#the-json-output-in-item-0-contains-invalid-json" id="the-json-output-in-item-0-contains-invalid-json"></a>

当你使用 JSON 模式但没有提供有效 JSON 对象时，会发生此错误。根据 JSON 对象的问题不同，该错误有时会显示为 `The 'JSON Output' in item 0 does not contain a valid JSON object`。

如需解决此问题，请确保提供的代码是有效 JSON：

- 使用 [JSON validator](https://jsonlint.com/) 检查 JSON。
- 检查 JSON 对象没有引用未定义的输入数据。如果传入数据不总是包含相同字段，可能会发生这种情况。

### 无法为 expression 获取数据 <a href="#cant-get-data-for-expression" id="cant-get-data-for-expression"></a>

当 n8n 无法检索 expression 引用的数据时，会发生此错误。通常，这是因为前序 node 尚未运行。

此错误的另一个变体可能显示为 `Referenced node is unexecuted`。在这种情况下，完整错误文本会按以下格式告诉你未执行的具体 node：

> An expression references the node '&lt;node-name&gt;', but it hasn't been executed yet. Either change the expression, or re-wire your workflow to make sure that node executes first.

开始排查时，请先测试工作流直到该命名 node。

对于使用 JavaScript 或其他自定义代码的 node，你可以在尝试使用前序 node 的值之前，通过以下方式检查它是否已执行：

```javascript
$("<node-name>").isExecuted
```

例如，以下 JSON 引用了输入数据的参数。如果你在未将此步骤连接到另一个 node 的情况下测试它，就会显示此错误：

```javascript
{
  "my_field_1": {{ $input.params }}
}
```

### 无效语法 <a href="#invalid-syntax" id="invalid-syntax"></a>

当你使用存在语法错误的 expression 时，会发生此错误。

例如，以下 JSON 中的 expression 包含末尾句点，会导致无效语法错误：

```jsx
{
  "my_field_1": "value",
  "my_field_2": {{ $('If').item.json. }}
}
```

如需解决此错误，请检查 [expression 语法](../expressions-versus-data-nodes.md)，确保它符合预期格式。

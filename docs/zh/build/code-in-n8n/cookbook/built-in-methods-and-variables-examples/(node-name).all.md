---
contentType: reference
nodeTitle: (node-name).all
originalFilePath: code/cookbook/builtin/all.md
originalUrl: 'https://docs.n8n.io/code/cookbook/builtin/all'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/(node-name).all
layout:
  description:
    visible: false
---

# `("<node-name>").all(branchIndex?: number, runIndex?: number)` <a href="#lessnode-namegreaterallbranchindex-number-runindex-number" id="lessnode-namegreaterallbranchindex-number-runindex-number"></a>

这会让你访问当前 node 或父 node 的所有 item。如果不提供任何参数，它会返回当前 node 的所有 item。

## 获取 item <a href="#getting-items" id="getting-items"></a>

{% tabs %}
{% tab title="JavaScript" %}
```js
// Returns all the items of the given node and current run
let allItems = $("<node-name>").all();

// Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
let allItems = $("IF").all();

// Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
let allItems = $("IF").all(0, $runIndex);

// Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
let allItems = $("IF").all(1, 0);
```
{% endtab %}

{% tab title="Python" %}
```python
# Returns all the items of the given node and current run
allItems = _("<node-name>").all();

# Returns all items the node "IF" outputs (index: 0 which is Output "true" of its most recent run)
allItems = _("IF").all();

# Returns all items the node "IF" outputs (index: 0 which is Output "true" of the same run as current node)
allItems = _("IF").all(0, _runIndex);

# Returns all items the node "IF" outputs (index: 1 which is Output "false" of run 0 which is the first run)
allItems = _("IF").all(1, 0);
```
{% endtab %}
{% endtabs %}

## 访问 item 数据 <a href="#accessing-item-data" id="accessing-item-data"></a>

获取前一个 node 输出的所有 item，并记录它们包含的数据：

{% tabs %}
{% tab title="JavaScript" %}
```typescript
previousNodeData = $("<node-name>").all();
for(let i=0; i<previousNodeData.length; i++) {
	console.log(previousNodeData[i].json);
}
```
{% endtab %}

{% tab title="Python" %}
```python
previousNodeData = _("<node-name>").all();
for item in previousNodeData:
	# item is of type <class 'pyodide.ffi.JsProxy'>
	# You need to convert it to a Dict
	itemDict = item.json.to_py()
	print(itemDict)
```
{% endtab %}
{% endtabs %}

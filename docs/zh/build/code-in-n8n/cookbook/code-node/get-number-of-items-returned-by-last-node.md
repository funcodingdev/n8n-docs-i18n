---
contentType: howto
nodeTitle: Get number of items returned by last node
originalFilePath: code/cookbook/code-node/number-items-last-node.md
originalUrl: 'https://docs.n8n.io/code/cookbook/code-node/number-items-last-node'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/code-node/get-number-of-items-returned-by-last-node
layout:
  description:
    visible: false
---

# 获取前一个 node 返回的 item 数量 <a href="#get-number-of-items-returned-by-the-previous-node" id="get-number-of-items-returned-by-the-previous-node"></a>

要获取前一个 node 返回的 item 数量：

{% tabs %}
{% tab title="JavaScript" %}
```js
if (Object.keys(items[0].json).length === 0) {
return [
	{
		json: {
			results: 0,
		}
	}
]
}
return [
	{
		json: {
			results: items.length,
		}
	}
];
```

输出将类似如下内容。

```json
[
	{
		"results": 8
	}
]
```
{% endtab %}

{% tab title="Python" %}
```python
if len(items[0].json) == 0:
	return [
		{
			"json": {
				"results": 0,
			}
		}
	]
else:
	return [
		{
			"json": {
				"results": items.length,
			}
		}
	]
```
输出将类似如下内容。

```json
[
	{
		"results": 8
	}
]
```
{% endtab %}
{% endtabs %}

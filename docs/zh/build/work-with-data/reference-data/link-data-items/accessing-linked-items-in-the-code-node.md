---
description: 如何使用 `("<node-name>").itemMatching(currentNodeinputIndex)`
contentType: howto
nodeTitle: Accessing linked items in the Code node
originalFilePath: data/data-mapping/itemmatching.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/itemmatching'
url: >-
  https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/accessing-linked-items-in-the-code-node
layout:
  description:
    visible: false
---

# 在 Code node 中访问 linked item <a href="#accessing-linked-items-in-the-code-node" id="accessing-linked-items-in-the-code-node"></a>

Node 输入数据中的每个 item 都会链接回前序 node 中用于生成它的 item。如果你需要从比直接前序 node 更早的位置检索 linked item，这会很有用。

如需访问工作流中更早位置的 linked item，请使用 `("<node-name>").itemMatching(currentNodeinputIndex)`。


例如，考虑一个执行以下操作的工作流：

1. Customer Datastore node 生成示例数据：
	```json
	[
		{
			"id": "23423532",
			"name": "Jay Gatsby",
			"email": "gatsby@west-egg.com",
			"notes": "Keeps asking about a green light??",
			"country": "US",
			"created": "1925-04-10"
		},
		{
			"id": "23423533",
			"name": "José Arcadio Buendía",
			"email": "jab@macondo.co",
			"notes": "Lots of people named after him. Very confusing",
			"country": "CO",
			"created": "1967-05-05"
		},
		...
    ]
	```
2. Edit Fields node 简化这些数据：
	```json
	[
		{
			"name": "Jay Gatsby"
		},
		{
			"name": "José Arcadio Buendía"
		},
        ...
	]
	```
3. Code node 将 email 地址恢复到正确的人：
	```json
	[
		{
			"name": "Jay Gatsby",
			"restoreEmail": "gatsby@west-egg.com"
		},
		{
			"name": "José Arcadio Buendía",
			"restoreEmail": "jab@macondo.co"
		},
		...
	]
	```

Code node 使用以下代码完成此操作：

{% tabs %}
{% tab title="JavaScript" %}
```js
for(let i=0; i<$input.all().length; i++) {
	$input.all()[i].json.restoreEmail = $('Customer Datastore (n8n training)').itemMatching(i).json.email;
}
return $input.all();
```
{% endtab %}

{% tab title="Python" %}
```python
for i,item in enumerate(_input.all()):
	_input.all()[i].json.restoreEmail = _('Customer Datastore (n8n training)').itemMatching(i).json.email

return _input.all();
```
{% endtab %}
{% endtabs %}

你可以从 [n8n website | itemMatching usage example](https://n8n.io/workflows/1966-itemmatching-usage-example/) 查看并下载示例工作流。

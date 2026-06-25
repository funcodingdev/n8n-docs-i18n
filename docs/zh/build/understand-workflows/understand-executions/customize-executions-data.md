---
description: >-
  使用 Code node 向工作流 execution 添加自定义数据，然后可按这些数据筛选 execution。
contentType: howto
nodeTitle: Customize executions data
originalFilePath: workflows/executions/custom-executions-data.md
originalUrl: 'https://docs.n8n.io/workflows/executions/custom-executions-data'
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/customize-executions-data
layout:
  description:
    visible: false
---

# 自定义 execution 数据 <a href="#custom-executions-data" id="custom-executions-data"></a>

你可以使用 Code node 或 [Execution Data node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executiondata) 为工作流设置自定义数据。n8n 会随每次 execution 记录这些数据。随后，你可以在筛选 execution 列表时使用这些数据，也可以在工作流中使用 Code node 获取这些数据。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/hEbJHXcEBce6m2wEE65f/" %}

## 使用 Code node 设置和访问自定义数据 <a href="#set-and-access-custom-data-using-the-code-node" id="set-and-access-custom-data-using-the-code-node"></a>

本节介绍如何使用 Code node 设置和访问数据。关于如何使用 Execution Data node 设置数据，请参阅 [Execution Data node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executiondata)。你不能使用 Execution Data node 获取自定义数据。

### 设置自定义 execution 数据 <a href="#set-custom-executions-data" id="set-custom-executions-data"></a>

设置一条额外数据：

{% tabs %}
{% tab title="JavaScript" %}
```js
$execution.customData.set("key", "value");
```
{% endtab %}

{% tab title="Python" %}
```python
_execution.customData.set("key", "value");
```
{% endtab %}
{% endtabs %}

设置所有额外数据。这会覆盖当前 execution 的整个自定义数据对象：

{% tabs %}
{% tab title="JavaScript" %}
```js
$execution.customData.setAll({"key1": "value1", "key2": "value2"})
```
{% endtab %}

{% tab title="Python" %}
```python
_execution.customData.setAll({"key1": "value1", "key2": "value2"})
```
{% endtab %}
{% endtabs %}

存在以下限制：

* 它们必须是字符串
* `key` 最大长度为 50 个字符
* `value` 最大长度为 255 个字符
* n8n 最多支持 10 条自定义数据

### 在 execution 期间访问自定义数据对象 <a href="#access-the-custom-data-object-during-execution" id="access-the-custom-data-object-during-execution"></a>

你可以在 execution 期间获取自定义数据对象，或获取其中的某个特定值：


{% tabs %}
{% tab title="JavaScript" %}
```js
// Access the current state of the object during the execution
const customData = $execution.customData.getAll();

// Access a specific value set during this execution
const customData = $execution.customData.get("key");
```
{% endtab %}

{% tab title="Python" %}
```python
# Access the current state of the object during the execution
customData = _execution.customData.getAll();

# Access a specific value set during this execution
customData = _execution.customData.get("key");
```
{% endtab %}
{% endtabs %}

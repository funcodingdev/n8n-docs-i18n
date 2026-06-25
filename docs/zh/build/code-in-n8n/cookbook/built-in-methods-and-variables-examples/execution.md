---
contentType: reference
nodeTitle: execution
originalFilePath: code/cookbook/builtin/execution.md
originalUrl: 'https://docs.n8n.io/code/cookbook/builtin/execution'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/execution
layout:
  description:
    visible: false
---

# `execution` <a href="#execution" id="execution"></a>

## `execution.id` <a href="#executionid" id="executionid"></a>

包含当前 workflow execution 的唯一 ID。

{% tabs %}
{% tab title="JavaScript" %}
```js
let executionId = $execution.id;
```
{% endtab %}

{% tab title="Python" %}
```python
executionId = _execution.id
```
{% endtab %}
{% endtabs %}

## `execution.resumeUrl` <a href="#executionresumeurl" id="executionresumeurl"></a>

用于恢复[等待中](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait) workflow 的 webhook URL。

更多信息请参阅 [Wait > On webhook call](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait#on-webhook-call) 文档。

`execution.resumeUrl` 可用于包含 Wait node、且有一个 node 等待 webhook response 的 workflow。

## `execution.customData` <a href="#executioncustomdata" id="executioncustomdata"></a>

这只在 Code node 中可用。

{% tabs %}
{% tab title="JavaScript" %}
```js
// Set a single piece of custom execution data
$execution.customData.set("key", "value");

// Set the custom execution data object
$execution.customData.setAll({"key1": "value1", "key2": "value2"})

// Access the current state of the object during the execution
var customData = $execution.customData.getAll()

// Access a specific value set during this execution
var customData = $execution.customData.get("key")
```
{% endtab %}

{% tab title="Python" %}
```python
# Set a single piece of custom execution data
_execution.customData.set("key", "value");

# Set the custom execution data object
_execution.customData.setAll({"key1": "value1", "key2": "value2"})

# Access the current state of the object during the execution
customData = _execution.customData.getAll()

# Access a specific value set during this execution
customData = _execution.customData.get("key")
```
{% endtab %}
{% endtabs %}

更多信息请参阅 [Custom executions data](../../../understand-workflows/understand-executions/customize-executions-data.md)。

---

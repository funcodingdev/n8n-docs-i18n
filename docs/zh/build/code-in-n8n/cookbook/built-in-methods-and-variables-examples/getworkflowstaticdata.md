---
tags:
  - static data
  - global variables
hide:
  - tags
contentType: reference
nodeTitle: getWorkflowStaticData
originalFilePath: code/cookbook/builtin/get-workflow-static-data.md
originalUrl: 'https://docs.n8n.io/code/cookbook/builtin/get-workflow-static-data'
url: >-
  https://docs.n8n.io/build/code-in-n8n/cookbook/built-in-methods-and-variables-examples/getworkflowstaticdata
layout:
  description:
    visible: false
---

# `getWorkflowStaticData(type)` <a href="#getworkflowstaticdatatype" id="getworkflowstaticdatatype"></a>

这会让你访问 static workflow data。

{% hint style="info" %}
**实验性功能**

- 测试 workflow 时 static data 不可用。workflow 必须处于 active 状态，并由 trigger[^1] 或 webhook 调用，才能保存 static data。
- 在高频 workflow execution 下，此功能可能表现不稳定。
{% endhint %}
你可以直接在 workflow 中保存数据。这类数据应保持较小。

例如：你可以保存从 RSS feed 或数据库处理的最后一个 item 的时间戳。它始终会返回一个 object。随后可读取、删除或设置该 object 上的 property。当 workflow execution 成功时，n8n 会自动检查数据是否已更改，并在必要时保存。

static data 有两种类型：global 和 node。Global static data 在整个 workflow 中相同。workflow 中的每个 node 都可以访问它。node static data 对该 node 是唯一的。只有设置它的 node 可以再次检索它。

global data 示例：

{% tabs %}
{% tab title="JavaScript" %}
```javascript
// Get the global workflow static data
const workflowStaticData = $getWorkflowStaticData('global');

// Access its data
const lastExecution = workflowStaticData.lastExecution;

// Update its data
workflowStaticData.lastExecution = new Date().getTime();

// Delete data
delete workflowStaticData.lastExecution;
```
{% endtab %}

{% tab title="Python" %}
```python
# Get the global workflow static data
workflowStaticData = _getWorkflowStaticData('global')

# Access its data
lastExecution = workflowStaticData.lastExecution

# Update its data
workflowStaticData.lastExecution = new Date().getTime()

# Delete data
delete workflowStaticData.lastExecution
```
{% endtab %}
{% endtabs %}

node data 示例：

{% tabs %}
{% tab title="JavaScript" %}
```js
// Get the static data of the node
const nodeStaticData = $getWorkflowStaticData('node');

// Access its data
const lastExecution = nodeStaticData.lastExecution;

// Update its data
nodeStaticData.lastExecution = new Date().getTime();

// Delete data
delete nodeStaticData.lastExecution;
```
{% endtab %}

{% tab title="Python" %}
```python
# Get the static data of the node
nodeStaticData = _getWorkflowStaticData('node')

# Access its data
lastExecution = nodeStaticData.lastExecution

# Update its data
nodeStaticData.lastExecution = new Date().getTime()

# Delete data
delete nodeStaticData.lastExecution
```
{% endtab %}
{% endtabs %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/2538" %}

[^1]: Trigger node 是一种特殊 node，负责在响应特定条件时执行 workflow。所有 production workflow 都至少需要一个 trigger，以确定 workflow 应在何时运行。

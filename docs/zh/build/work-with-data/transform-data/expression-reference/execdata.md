---
nodeTitle: Execdata
originalFilePath: data/expression-reference/execdata.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/execdata'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/execdata
layout:
  description:
    visible: false
---
# ExecData <a href="#execdata" id="execdata"></a>

## `$exec`.**`customData`** <a href="#dollarexeccustomdata" id="dollarexeccustomdata"></a>

**描述：** 设置和获取自定义 execution 数据（例如用于筛选 execution）。你也可以使用 ‘Execution Data’ node 完成此操作。<a href="/workflows/executions/custom-executions-data/">更多信息</a>

**语法：** `$exec`.`$exec`.**`customData`**

**返回：** CustomData

**来源：** 自定义 n8n 功能

## `$exec`.**`id`** <a href="#dollarexecid" id="dollarexecid"></a>

**描述：** 当前 workflow execution 的 ID

**语法：** `$exec`.`$exec`.**`id`**

**返回：** String

**来源：** 自定义 n8n 功能

## `$exec`.**`mode`** <a href="#dollarexecmode" id="dollarexecmode"></a>

**描述：** 可以是 3 个值之一：<code>test</code>（表示 execution 是通过点击 n8n 中的按钮触发的）或 <code>production</code>（表示 execution 是自动触发的）。运行工作流测试时使用 <code>evaluation</code>。

**语法：** `$exec`.`$exec`.**`mode`**

**返回：** String

**来源：** 自定义 n8n 功能

## `$exec`.**`resumeFormUrl`** <a href="#dollarexecresumeformurl" id="dollarexecresumeformurl"></a>

**描述：** 用于访问 <a href="/integrations/builtin/core-nodes/n8n-nodes-base.wait/">’Wait’ node</a> 生成表单的 URL。

**语法：** `$exec`.`$exec`.**`resumeFormUrl`**

**返回：** String

**来源：** 自定义 n8n 功能

## `$exec`.**`resumeUrl`** <a href="#dollarexecresumeurl" id="dollarexecresumeurl"></a>

**描述：** 用于调用并恢复正在 <a href="/integrations/builtin/core-nodes/n8n-nodes-base.wait/">’Wait’ node</a> 等待的工作流的 webhook URL。

**语法：** `$exec`.`$exec`.**`resumeUrl`**

**返回：** String

**来源：** 自定义 n8n 功能

---
title: Execution Data
description: >-
  n8n 中 Execution Data node 的文档。n8n 是一个 workflow 自动化
  平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Execution Data
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executiondata
layout:
  description:
    visible: false
---

# Execution Data <a href="#execution-data" id="execution-data"></a>

使用此 node 可以保存 workflow execution 的 metadata。之后你可以在 **Executions** 列表中按这些数据搜索。

你可以在 workflow execution 期间使用 Code node 检索自定义 execution data。更多信息请参阅 [Custom executions data](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/customize-executions-data)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/hEbJHXcEBce6m2wEE65f/" %}

## 操作 <a href="#operations" id="operations"></a>

* 保存 Execution Data 以供搜索

## 要保存的数据 <a href="#data-to-save" id="data-to-save"></a>

为你想保存的每个 metadata key/value pair 添加一个 **Saved Field**。

## 限制 <a href="#limitations" id="limitations"></a>

Execution Data node 存储 execution metadata 时有以下限制：

* `key`：限制为 50 个字符
* `value`：限制为 512 个字符

如果 `key` 或 `value` 超出上述限制，n8n 会截断到最大长度，并输出一条日志。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execution Data 集成模板](https://n8n.io/integrations/execution-data)或[搜索所有模板](https://n8n.io/workflows/)

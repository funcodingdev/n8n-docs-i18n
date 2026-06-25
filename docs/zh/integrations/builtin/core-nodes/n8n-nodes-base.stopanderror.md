---
title: Stop And Error
description: >-
  n8n 中 Stop And Error node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Stop And Error
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror
layout:
  description:
    visible: false
---

# Stop And Error <a href="#stop-and-error" id="stop-and-error"></a>

使用 Stop And Error node 显示自定义错误消息、在特定条件下让 execution 失败，并将自定义错误信息发送到 error workflow。

## 操作 <a href="#operations" id="operations"></a>

* Error Message
* Error Object

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

两个操作都包含一个 node 参数：**Error Type**。使用此参数选择要抛出的错误类型。在两个操作之间选择：**Error Message** 和 **Error Object**。

其他参数取决于你选择的操作。

### Error Message 参数 <a href="#error-message-parameters" id="error-message-parameters"></a>

Error Message Error Type 会添加一个参数：**Error Message** 字段。输入要抛出的消息。

### Error Object 参数 <a href="#error-object-parameters" id="error-object-parameters"></a>

Error Object Error Type 会添加一个参数：**Error Object**。输入包含要抛出的错误属性的 JSON 对象。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Stop And Error 集成模板](https://n8n.io/integrations/stop-and-error)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

你可以将 Stop And Error node 与 [Error trigger](n8n-nodes-base.errortrigger.md) node 一起使用。

阅读更多关于 n8n workflow 中 [Error workflow](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/handle-errors-gracefully) 的内容。

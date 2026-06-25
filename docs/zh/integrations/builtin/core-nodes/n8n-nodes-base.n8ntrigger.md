---
title: n8n Trigger node 文档
description: >-
  了解如何在 n8n 中使用 n8n Trigger node。按照技术文档将
  n8n Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: n8n Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.n8ntrigger'
layout:
  description:
    visible: false
---

# n8n Trigger node <a href="#n8n-trigger-node" id="n8n-trigger-node"></a>

当包含此 node 的 workflow 更新或发布，或 n8n instance 启动或重启时，n8n Trigger node 会触发。此 node 只响应其所在 workflow 中的事件；其他 workflow 的更改不会触发它。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

该 node 只包含一个参数，用于标识应触发它的 **Events**。可选择这些事件：

- **Published Workflow Updated**：如果选择此事件，当包含此 node 的 workflow 更新时，该 node 会触发。其他 workflow 的更改不会触发此 node。
- **Instance started**：如果选择此事件，当 n8n instance 启动或重启时，该 node 会触发。
- **Workflow Published**：如果选择此事件，当包含此 node 的 workflow 发布时，该 node 会触发。发布其他 workflow 不会触发此 node。

你可以选择其中一个或多个事件。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n Trigger node 集成模板](https://n8n.io/integrations/n8n-trigger)或[搜索所有模板](https://n8n.io/workflows/)

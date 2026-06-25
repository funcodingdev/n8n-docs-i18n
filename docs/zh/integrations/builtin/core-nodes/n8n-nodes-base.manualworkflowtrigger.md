---
title: Manual Trigger node 文档
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Manual Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger
description: >-
  了解如何在 n8n 中使用 Manual Trigger node。按照技术文档将
  Manual Trigger node 集成到你的 workflow 中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Manual Trigger

如果你想通过选择 **Execute Workflow** 来启动 workflow，并且不希望 workflow 有任何自动运行选项，请使用此 node。

Workflow 始终需要 trigger 或起点。大多数 workflow 以 trigger node 开始，响应外部事件触发，或由 [Schedule Trigger](n8n-nodes-base.scheduletrigger/) 按设定计划触发。

Manual Trigger node 充当那些没有自动 trigger 的 workflow 的 workflow trigger。

在以下场景中使用此 trigger：

* 在添加某种自动 trigger 之前测试 workflow。
* 当你不希望 workflow 自动运行时。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Manual Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### 一个 workflow 中只允许有一个 'Manual Trigger' node <a href="#only-one-manual-trigger-node-is-allowed-in-a-workflow" id="only-one-manual-trigger-node-is-allowed-in-a-workflow"></a>

如果你尝试向已经包含 Manual Trigger node 的 workflow 添加 Manual Trigger node，会显示此错误。

移除现有的 Manual Trigger，或编辑 workflow，将该 trigger 连接到不同的 node。

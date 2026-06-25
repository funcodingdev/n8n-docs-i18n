---
title: Workflow Trigger node documentation
description: >-
  了解如何在 n8n 中使用 Workflow Trigger node。按照技术文档将 Workflow Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Workflow Trigger node documentation
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.workflowtrigger
layout:
  description:
    visible: false
---

# Workflow Trigger node <a href="#workflow-trigger-node" id="workflow-trigger-node"></a>

当 workflow 更新或激活时，Workflow Trigger node 会被触发。

{% hint style="warning" %}
**已弃用**

n8n 已弃用 Workflow Trigger node，并将其功能迁移到 [n8n Trigger node](n8n-nodes-base.n8ntrigger.md)。
{% endhint %}

{% hint style="info" %}
**请注意**

如果想在某个 workflow 中使用 Workflow Trigger node，请将该 node 添加到该 workflow。你不需要创建单独的 workflow。
{% endhint %}

Workflow Trigger node 会针对添加它的 workflow 触发。你可以使用 Workflow Trigger node 触发 workflow，以通知 workflow 状态。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

此 node 包含一个参数，用于识别应触发它的 **Events**。可从这些事件中选择：

- **Active Workflow Updated**：如果选择此事件，当此 workflow 更新时，该 node 会触发。
- **Workflow Activated**：如果选择此事件，当此 workflow 激活时，该 node 会触发。

你可以选择其中一个或两个事件。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Workflow Trigger node 文档集成模板](https://n8n.io/integrations/workflow-trigger)或[搜索所有模板](https://n8n.io/workflows/)

---
title: Activation Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Activation Trigger node。按照技术文档将
  Activation Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Activation Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.activationtrigger
layout:
  description:
    visible: false
---

# Activation Trigger node <a href="#activation-trigger-node" id="activation-trigger-node"></a>

当 n8n 或 workflow 触发某个事件时，Activation Trigger node 会被触发。

{% hint style="warning" %}
n8n 已弃用 Activation Trigger node，并用两个新 node 取代它：[n8n Trigger node](n8n-nodes-base.n8ntrigger.md) 和 [Workflow Trigger node](n8n-nodes-base.workflowtrigger.md)。更多详情，请查看 [breaking changes](https://github.com/n8n-io/n8n/blob/master/packages/cli/BREAKING-CHANGES.md#01170) 页面中的对应条目。
{% endhint %}

{% hint style="info" %}
**请记住**

如果你想在某个 workflow 中使用 Activation Trigger node，请将该 node 添加到这个 workflow 中。你不需要创建单独的 workflow。
{% endhint %}

Activation Trigger node 会针对其所在的 workflow 被触发。你可以使用 Activation Trigger node 触发 workflow，以通知该 workflow 的状态。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

- Events
    - **Activation**：workflow 发布时运行
    - **Start**：n8n 启动或重启时运行
    - **Update**：workflow 处于激活状态并被保存时运行

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Activation Trigger node 集成模板](https://n8n.io/integrations/activation-trigger)或[搜索所有模板](https://n8n.io/workflows/)

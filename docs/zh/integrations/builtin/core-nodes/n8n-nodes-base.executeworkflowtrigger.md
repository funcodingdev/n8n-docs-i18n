---
title: Execute Sub-workflow Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Execute Sub-workflow Trigger node。按照技术
  文档将 Execute Sub-workflow Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Execute Sub-workflow Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger
layout:
  description:
    visible: false
---

# Execute Sub-workflow Trigger node <a href="#execute-sub-workflow-trigger-node" id="execute-sub-workflow-trigger-node"></a>

使用此 node 可以响应另一个 workflow 来启动一个 workflow。它应是 workflow 中的第一个 node。

n8n 允许你从其他 workflow 调用 workflow。如果你想执行以下操作，这会很有用：

* 复用 workflow：例如，你可以有多个 workflow 从不同来源拉取并处理数据，然后让所有这些 workflow 调用一个生成报告的单一 workflow。
* 将大型 workflow 拆分为较小组件。

## 用法 <a href="#usage" id="usage"></a>

此 node 会响应来自 [Execute Sub-workflow](n8n-nodes-base.executeworkflow.md) 或 [Call n8n Workflow Tool](../cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md) node 的调用而运行。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/wlwT5JcWyWTecnDN6aul/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execute Sub-workflow Trigger node 集成模板](https://n8n.io/integrations/execute-workflow-trigger)或[搜索所有模板](https://n8n.io/workflows/)

## 数据如何在 workflow 之间传递 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/edKlUxnfiRMq38CujuFv/" %}

---
title: If
description: >-
  n8n 中 If node 的文档。n8n 是一个 workflow 自动化平台。包含
  使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: critical
tags:
  - if
  - if node
  - If
  - If node
hide:
  - tags
nodeTitle: If
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.if.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if'
layout:
  description:
    visible: false
---

# If <a href="#if" id="if"></a>

使用 If node 可以基于比较操作有条件地拆分 workflow。

## 添加条件 <a href="#add-conditions" id="add-conditions"></a>

为你的 If node 创建比较 **Conditions**。

- 使用数据类型下拉菜单，为条件选择数据类型和比较操作类型。例如，要筛选某个日期之后的日期，请选择 **Date & Time > is after**。
- 条件中要输入的字段和值会根据你选择的数据类型和比较而变化。所有按数据类型划分的比较完整列表，请参阅[可用数据类型比较](#available-data-type-comparisons)。

选择 **Add condition** 可创建更多条件。

### 组合条件 <a href="#combining-conditions" id="combining-conditions"></a>

你可以选择保留数据：

* 当它满足所有条件时：创建两个或更多条件，并在它们之间的下拉菜单中选择 **AND**。
* 当它满足任一条件时：创建两个或更多条件，并在它们之间的下拉菜单中选择 **OR**。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 If 集成模板](https://n8n.io/integrations/if)或[搜索所有模板](https://n8n.io/workflows/)

## 使用 If 和 Merge node 进行分支执行 <a href="#branch-execution-with-if-and-merge-nodes" id="branch-execution-with-if-and-merge-nodes"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/o5sVhTw0cyO5aAAkAVDj/" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关使用条件创建 n8n 中复杂逻辑的更多信息，请参阅[使用条件拆分](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/split-with-conditionals)。

如果需要两个以上的条件输出，请使用 [Switch node](n8n-nodes-base.switch.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/bMMOCQFbQ4YpKDnWQQOg/" %}

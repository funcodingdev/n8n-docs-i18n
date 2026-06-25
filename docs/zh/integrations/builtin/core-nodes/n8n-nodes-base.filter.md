---
title: Filter
description: >-
  n8n 中 Filter node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Filter
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.filter.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.filter'
layout:
  description:
    visible: false
---

# Filter <a href="#filter" id="filter"></a>

根据条件过滤 item。如果 item 满足条件，Filter node 会将其传递给 Filter node 输出中的下一个 node。如果 item 不满足条件，Filter node 会从输出中省略该 item。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

创建过滤比较 **Conditions** 来执行过滤。

- 使用数据类型下拉菜单，为条件选择数据类型和比较操作类型。例如，要筛选某个日期之后的日期，请选择 **Date & Time > is after**。
- 条件中要输入的字段和值会根据你选择的数据类型和比较而变化。所有按数据类型划分的比较完整列表，请参阅[可用数据类型比较](#available-data-type-comparisons)。

选择 **Add condition** 可创建更多条件。

### 组合条件 <a href="#combining-conditions" id="combining-conditions"></a>

你可以选择保留 item：

* 当它们满足所有条件时：创建两个或更多条件，并在它们之间的下拉菜单中选择 **AND**。
* 当它们满足任一条件时：创建两个或更多条件，并在它们之间的下拉菜单中选择 **OR**。

你不能混合创建 AND 和 OR 规则。

## Node 选项 <a href="#node-options" id="node-options"></a>

- **Ignore Case**：是否忽略字母大小写（开启），或区分大小写（关闭）。
- **Less Strict Type Validation**：是否希望 n8n 根据你选择的 operator 尝试转换值类型（开启）或不转换（关闭）。当你的 node 遇到 "wrong type:" 错误时，请开启此选项。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Filter 集成模板](https://n8n.io/integrations/filter)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/bMMOCQFbQ4YpKDnWQQOg/" %}

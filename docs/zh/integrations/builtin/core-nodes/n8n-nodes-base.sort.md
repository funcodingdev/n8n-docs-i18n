---
title: Sort
description: >-
  n8n 中 Sort node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Sort
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.sort.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.sort'
layout:
  description:
    visible: false
---

# Sort <a href="#sort" id="sort"></a>

使用 Sort node 按所需顺序整理 item 列表，或生成随机选择。

{% hint style="info" %}
**数组排序行为**

Sort 操作使用默认 JavaScript 行为：要排序的元素会转换为字符串，然后比较它们的值。更多信息请参阅 [Mozilla 的 Array sort 指南](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)。
{% endhint %}

## Node parameters <a href="#node-parameters" id="node-parameters"></a>

使用 **Type** 参数配置此 node。

使用下拉菜单从这些选项中选择排序输入方式。

### Simple <a href="#simple" id="simple"></a>

使用所选字段执行升序或降序排序。

选择此 **Type** 时：

* 使用 **Add Field To Sort By** 按钮输入 **Field Name**。
* 选择使用 **Ascending** 还是 **Descending** 顺序。

#### Simple 选项 <a href="#simple-options" id="simple-options"></a>

将 **Type** 选为 **Simple** 时，可以选择 **Disable Dot Notation**。默认情况下，n8n 启用 dot notation，以 `parent.child` 格式引用子字段。使用此选项可禁用 dot notation（开启），或继续使用 dot notation（关闭）。

### Random <a href="#random" id="random"></a>

为列表创建随机顺序。

### Code <a href="#code" id="code"></a>

输入自定义 JavaScript 代码执行排序操作。如果简单排序无法满足需求，这是一个合适的选项。

在 **Code** 输入字段中输入自定义 JavaScript 代码。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Sort 集成模板](https://n8n.io/integrations/sort)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/0nvcx1EqJQgGVzUXOOMN/" %}

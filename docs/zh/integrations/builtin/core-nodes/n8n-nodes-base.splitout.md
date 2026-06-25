---
title: Split Out
description: >-
  n8n 中 Split Out node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Split Out
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.splitout.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitout'
layout:
  description:
    visible: false
---

# Split Out <a href="#split-out" id="split-out"></a>

使用 Split Out node 将包含列表的单个数据 item 拆分为多个 item。例如，你有一个客户列表，并希望拆分成每个客户一个 item。

## Node parameters <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置此 node。

### Field to Split Out <a href="#field-to-split-out" id="field-to-split-out"></a>

输入包含列表的字段，该列表会被拆分为单独的 item。

如果处理的是二进制数据输入，请在 expression 中使用 `$binary` 设置要拆分的字段。

### Include <a href="#include" id="include"></a>

选择 n8n 是否以及如何在每个新的单独 item 中保留输入数据中的其他字段。

你可以选择：

* **No Other Fields**：不包含其他字段。
* **All Other Fields**：包含所有其他字段。
* **Selected Other Fields**：仅包含所选字段。
    * **Fields to Include**：输入要包含的字段列表，以逗号分隔。

## Node options <a href="#node-options" id="node-options"></a>

### Disable Dot Notation <a href="#disable-dot-notation" id="disable-dot-notation"></a>

默认情况下，n8n 启用 dot notation，以 `parent.child` 格式引用子字段。使用此选项可禁用 dot notation（开启），或继续使用 dot notation（关闭）。

### Destination Field Name <a href="#destination-field-name" id="destination-field-name"></a>

输入输出中的字段名称，用于存放拆分出的字段内容。

### Include Binary <a href="#include-binary" id="include-binary"></a>

选择是否在新的输出中包含来自输入的二进制数据（开启），或不包含（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Split Out 集成模板](https://n8n.io/integrations/split-out)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/0nvcx1EqJQgGVzUXOOMN/" %}

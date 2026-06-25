---
title: Summarize
description: >-
  n8n 中 Summarize node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Summarize
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.summarize.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.summarize'
layout:
  description:
    visible: false
---

# Summarize <a href="#summarize" id="summarize"></a>

使用 Summarize node 汇总 item，方式类似 Excel 数据透视表。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Fields to Summarize <a href="#fields-to-summarize" id="fields-to-summarize"></a>

使用这些字段定义你希望如何汇总输入数据。

* **Aggregation**：选择要在给定字段上使用的聚合方法。选项包括：
	* **Append**：追加。
		* 如果选择此选项，请决定是否要 **Include Empty Values**。
	* **Average**：计算输入数据的数值平均值。
	* **Concatenate**：将输入数据中的值组合在一起。
		* 如果选择此选项，请决定是否要 **Include Empty Values**。
		* **Separator**：选择要插入到拼接值之间的分隔符。
	* **Count**：统计输入数据中的值总数。
	* **Count Unique**：统计输入数据中唯一值的数量。
	* **Max**：查找输入数据中的最大数值。
	* **Min**：查找输入数据中的最小数值。
	* **Sum**：将输入数据中的数值相加。
* **Field**：输入要执行聚合的字段名称。

### Fields to Split By <a href="#fields-to-split-by" id="fields-to-split-by"></a>

输入要按其拆分汇总结果的输入字段名称（类似 group by 语句）。这样可以基于其他字段中的值获得单独的汇总。

例如，如果输入数据包含 `Sales Rep` 和 `Deal Amount` 列，并且我们正在对 `Deal Amount` 字段执行 **Sum**，则可以按 `Sales Rep` 拆分，以获得每个销售代表的 **Sum** 总计。

要输入多个拆分字段，请输入以逗号分隔的列表。

## Node 选项 <a href="#node-options" id="node-options"></a>

### Continue if Field Not Found <a href="#continue-if-field-not-found" id="continue-if-field-not-found"></a>

默认情况下，如果任何 item 中都不存在 **Field to Summarize**，此 node 会抛出错误。使用此选项可以改为继续并返回单个空 item（开启），或保持默认错误行为（关闭）。

### Disable Dot Notation <a href="#disable-dot-notation" id="disable-dot-notation"></a>

默认情况下，n8n 启用 dot notation，以 `parent.child` 格式引用子字段。使用此选项可禁用 dot notation（开启），或继续使用 dot notation（关闭）。

### Output Format <a href="#output-format" id="output-format"></a>

选择输出格式。如果你正在使用 **Fields to Split By**，建议设置此选项。

* **Each Split in a Separate Item**：使用此选项为每个拆分出的字段生成单独的输出 item。
* **All Splits in a Single Item**：使用此选项生成单个 item，其中列出拆分出的字段。

## 忽略没有有效 group by 字段的 item <a href="#ignore-items-without-valid-fields-to-group-by" id="ignore-items-without-valid-fields-to-group-by"></a>

设置是否忽略不包含 **Fields to Split By** 的输入 item（开启），或不忽略（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Summarize 集成模板](https://n8n.io/integrations/summarize)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/0nvcx1EqJQgGVzUXOOMN/" %}

---
title: Compare Datasets
description: >-
  n8n 中 Compare Datasets node 的文档。n8n 是一个 workflow 自动化
  平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Compare Datasets
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets
layout:
  description:
    visible: false
---

# Compare Datasets <a href="#compare-datasets" id="compare-datasets"></a>

Compare Datasets node 可以帮助你比较两个输入流中的数据。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

1. 决定要比较哪些字段。在 **Input A Field** 中输入你想从输入流 A 使用的字段名。在 **Input B Field** 中输入你想从输入流 B 使用的字段名。
2. **可选**：你可以按多个字段进行比较。选择 **Add Fields to Match** 来设置更多比较。
3. 选择如何处理两个数据集之间的差异。在 **When There Are Differences** 中选择以下选项之一：
	* **Use Input A Version**：将输入流 A 视为事实来源。
	* **Use Input B Version**：将输入流 B 视为事实来源。
	* **Use a Mix of Versions**：为不同字段使用不同输入。
		* 使用 **Prefer** 选择 **Input A Version** 或 **Input B Version** 作为主要事实来源。
		* 在 **For Everything Except** 中输入作为例外的输入字段，以便从另一个输入源取值。要添加多个输入字段，请输入逗号分隔的列表。
	* **Include Both Versions**：在输出中包含两个输入流，这可能会让结构更复杂。
4. 决定是否使用 **Fuzzy Compare**。开启后，在比较字段时会容忍较小的类型差异。例如，数字 3 和字符串 `3` 在开启 **Fuzzy Compare** 时会被视为相同，但关闭时不会被视为相同。

## 理解 item 比较 <a href="#understand-item-comparison" id="understand-item-comparison"></a>

Item 比较是一个两阶段过程：

1. n8n 会检查你选择用于比较的字段值在两个输入中是否匹配。
2. 如果要比较的字段匹配，n8n 接着会比较 item 内的所有字段，以判断这些 item 是相同还是不同。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用 node 的 **Options** 可以细化比较或调整比较行为。

### Fields to Skip Comparing <a href="#fields-to-skip-comparing" id="fields-to-skip-comparing"></a>

输入你想在比较中忽略的字段名称。

例如，如果使用 `person.language` 作为 **Fields to Match** 来比较下面两个数据集，n8n 会返回它们不同。如果将 `person.name` 添加到 **Fields to Skip Comparing**，n8n 会返回它们匹配。

```json
	// Input 1
	[
		{
			"person":
			{
				"name":	"Stefan",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jim",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Hans",
				"language":	"de"
			}
		}
	]
	// Input 2
		[
		{
			"person":
			{
				"name":	"Sara",
				"language":	"de"
			}
		},
		{
			"person":
			{
				"name":	"Jane",
				"language":	"en"
			}
		},
		{
			"person":
			{
				"name":	"Harriet",
				"language":	"de"
			}
		}
	]
```

### Disable Dot Notation <a href="#disable-dot-notation" id="disable-dot-notation"></a>

控制是否禁止在字段名中使用 `parent.child` 引用子字段（开启），或允许这样做（关闭，默认）。

### Multiple Matches <a href="#multiple-matches" id="multiple-matches"></a>

选择如何处理重复数据。默认值是 **Include All Matches**。你可以选择 **Include First Match Only**。

例如，给定这两个数据集：
```json
	// Input 1
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
	// Input 2
	[
		{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "apple",
				"color": "red"
			}
		},
				{
			"fruit": {
				"type": "banana",
				"color": "yellow"
			}
		}
	]
```

n8n 会在 **Same Branch** 标签页中返回三个 item。两个分支中的数据相同。

如果选择 **Include First Match Only**，n8n 会在 **Same Branch** 标签页中返回两个 item。两个分支中的数据相同，但 n8n 只返回匹配的 "apple" item 的第一次出现。


## 理解输出 <a href="#understand-the-output" id="understand-the-output"></a>

共有四种输出选项：

* **In A only Branch**：包含只出现在第一个输入中的数据。
* **Same Branch**：包含两个输入中相同的数据。
* **Different Branch**：包含两个输入之间不同的数据。
* **In B only Branch**：包含只出现在第二个输出中的数据。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Compare Datasets 集成模板](https://n8n.io/integrations/compare-datasets)或[搜索所有模板](https://n8n.io/workflows/)

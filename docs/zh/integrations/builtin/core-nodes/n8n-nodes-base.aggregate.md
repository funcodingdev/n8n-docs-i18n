---
title: Aggregate
description: >-
  n8n 中 Aggregate node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Aggregate
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aggregate'
layout:
  description:
    visible: false
---

# Aggregate <a href="#aggregate" id="aggregate"></a>

使用 Aggregate node 可以将分散的 item，或 item 中的部分内容，组合成单独的 item。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

要开始使用该 node，请选择你想使用的 **Aggregate** 类型：

* [**Individual Fields**](#individual-fields)：分别聚合单个字段。
* [**All Item Data**](#all-item-data)：将所有 item 数据聚合到一个列表中。

### Individual Fields <a href="#individual-fields" id="individual-fields"></a>

* **Input Field Name**：输入要一起聚合的输入数据字段名称。
* **Rename Field**：此开关控制是否在聚合后的输出数据中为字段使用不同名称。开启后可以添加不同的字段名。如果要聚合多个字段，必须提供新的输出字段名。不能让多个字段保持未定义。
	* **Output Field Name**：开启 **Rename Field** 后会显示此字段。输入聚合后输出数据的字段名。

更多配置选项请参阅 [Node 选项](#node-options)。

### All Item Data <a href="#all-item-data" id="all-item-data"></a>

* **Put Output in Field**：输入用于输出数据的字段名称。
* **Include**：选择要包含在输出中的字段。可选项包括：
	* **All fields**：输出包含所有字段的数据，无需更多参数。
	* **Specified Fields**：如果选择此选项，请在 **Fields To Include** 参数中输入逗号分隔的字段列表，表示输出应包含哪些字段的数据。输出只会包含此列表中的字段。
	* **All Fields Except**：如果选择此选项，请在 **Fields To Exclude** 参数中输入逗号分隔的字段列表，表示输出应排除哪些字段的数据。输出会包含不在此列表中的所有字段。

更多配置选项请参阅 [Node 选项](#node-options)。

## Node 选项 <a href="#node-options" id="node-options"></a>

你可以使用这些 **Options** 进一步配置此 node：

* **Disable Dot Notation**：当你选择 **Individual Fields** Aggregate 时，该 node 会显示此开关。它控制是否禁止在字段名中使用 `parent.child` 引用子字段（开启），或允许这样做（关闭，默认）。
* **Merge Lists**：当你选择 **Individual Fields** Aggregate 时，该 node 会显示此开关。如果要聚合的字段是列表，并且你想输出一个单层列表而不是列表的列表，请开启它。
* **Include Binaries**：两种 Aggregate 类型都会显示此开关。如果想在新输出中包含输入里的二进制数据，请开启它。
* **Keep Missing And Null Values**：当你选择 **Individual Fields** Aggregate 时，该 node 会显示此开关。开启后，当输入中存在 null 或缺失值时，会在输出列表中添加一个 null（空）条目。如果关闭，输出会忽略 null 或空值。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Aggregate 集成模板](https://n8n.io/integrations/aggregate)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/0nvcx1EqJQgGVzUXOOMN/" %}

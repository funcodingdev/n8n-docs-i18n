---
title: Merge
description: >-
  n8n 中 Merge node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Merge
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.merge.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.merge'
layout:
  description:
    visible: false
---

# Merge <a href="#merge" id="merge"></a>

使用 Merge node 可以在所有数据流的数据都可用后，合并来自多个数据流的数据。

{% hint style="info" %}
**0.194.0 中的重大变化**

n8n 团队在 n8n 0.194.0 中重做了此 node。本文档反映该 node 的最新版本。如果你使用的是旧版本 n8n，可以在[这里](https://github.com/n8n-io/n8n-docs/blob/4ff688642cc9ee7ca7d00987847bf4e4515da59d/docs/integrations/builtin/core-nodes/n8n-nodes-base.merge.md)找到此文档的旧版本。
{% endhint %}

{% hint style="info" %}
**1.49.0 中的小幅变化**

n8n 1.49.0 引入了添加两个以上输入的选项。旧版本最多只支持两个输入。如果你运行的是旧版本，并且想在这些版本中合并多个输入，请使用 [Code node](https://deploy-preview-2225--n8n-docs.netlify.app/code/code-node/)。

**Mode > SQL Query** 功能也在 n8n 1.49.0 中添加，旧版本不可用。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

你可以通过选择 **Mode** 来指定 Merge node 应如何合并不同数据流中的数据：

### Append <a href="#append" id="append"></a>

保留来自所有输入的数据。选择 **Number of Inputs**，按顺序输出每个输入的 item。该 node 会等待所有已连接输入执行完成。

<figure>
<img src="../../.gitbook/assets/append-diagram.png" alt="">
<figcaption>Append mode inputs and output</figcaption>
</figure>

### Combine <a href="#combine" id="combine"></a>

合并来自两个输入的数据。在 **Combine By** 中选择一个选项，决定希望如何合并输入数据。

#### Matching Fields <a href="#matching-fields" id="matching-fields"></a>

按字段值比较 item。在 **Fields to Match** 中输入要比较的字段。

n8n 默认行为是保留匹配的 item。你可以使用 **Output Type** 设置更改此行为：

* **Keep Matches**：合并匹配的 item。类似 inner join。
* **Keep Non-Matches**：合并不匹配的 item。
* **Keep Everything**：合并匹配的 item，并包含不匹配的 item。类似 outer join。
* **Enrich Input 1**：保留 Input 1 的所有数据，并添加来自 Input 2 的匹配数据。类似 left join。
* **Enrich Input 2**：保留 Input 2 的所有数据，并添加来自 Input 1 的匹配数据。类似 right join。

<figure>
<img src="../../.gitbook/assets/merge-by-field-diagram.png" alt="">
<figcaption>Combine by Matching Fields mode inputs and output</figcaption>
</figure>


#### Position <a href="#position" id="position"></a>

根据顺序合并 item。Input 1 中 index 0 的 item 会与 Input 2 中 index 0 的 item 合并，以此类推。

<figure>
<img src="../../.gitbook/assets/merge-by-position-diagram.png" alt="">
<figcaption>Combine by Position mode inputs and output</figcaption>
</figure>


#### All Possible Combinations <a href="#all-possible-combinations" id="all-possible-combinations"></a>

输出所有可能的 item 组合，同时合并同名字段。

<figure>
<img src="../../.gitbook/assets/multiplex-diagram.png" alt="">
<figcaption>Combine by All Possible Combinations mode inputs and output</figcaption>
</figure>

#### Combine mode 选项 <a href="#combine-mode-options" id="combine-mode-options"></a>

使用 **Mode > Combine** 合并数据时，可以设置这些 **Options**：

* **Clash Handling**：选择当数据流冲突或存在子字段时如何合并。详情请参阅 [Clash handling](#clash-handling)。
* **Fuzzy Compare**：比较字段时是否容忍类型差异（enabled），或不容忍（disabled，默认）。例如，启用后，n8n 会将 `"3"` 和 `3` 视为相同。
* **Disable Dot Notation**：防止在字段名中使用 `parent.child` 访问子字段。
* **Multiple Matches**：选择 n8n 在比较数据流时如何处理多个匹配项。
    * **Include All Matches**：如果存在多个匹配项，则输出多个 item，每个匹配项一个。
    * **Include First Match Only**：每个匹配只保留第一个 item，并丢弃其余多个匹配项。
* **Include Any Unpaired Items**：选择按 position 合并时保留还是丢弃未配对 item。默认行为是排除没有匹配项的 item。

##### Clash Handling <a href="#clash-handling" id="clash-handling"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/VJPiDgC5Bx5FmuGODmCq/" %}

### SQL Query <a href="#sql-query" id="sql-query"></a>

编写自定义 SQL Query 来合并数据。

示例：
```sql
SELECT * FROM input1 LEFT JOIN input2 ON input1.name = input2.id
```

来自前面 node 的数据会作为表可用，你可以在 SQL query 中按顺序使用 input1、input2、input3 等名称引用它们。支持的 SQL statement 完整列表请参阅 [AlaSQL GitHub page](https://github.com/alasql/alasql/wiki/Supported-SQL-statements)。

### Choose Branch <a href="#choose-branch" id="choose-branch"></a>

选择要保留的输入。此选项始终会等待两个输入的数据都可用。你可以选择 **Output**：

* **Input 1 Data**
* **Input 2 Data**
* **A Single, Empty Item**

该 node 会输出所选输入的数据，且不更改它。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Merge 集成模板](https://n8n.io/integrations/merge)或[搜索所有模板](https://n8n.io/workflows/)

## 合并 item 数量不均的数据流 <a href="#merging-data-streams-with-uneven-numbers-of-items" id="merging-data-streams-with-uneven-numbers-of-items"></a>

传入 Merge node 的 Input 1 的 item 会优先。例如，如果 Merge node 在 Input 1 中收到 5 个 item，在 Input 2 中收到 10 个 item，它只会处理 5 个 item。Input 2 中剩余的 5 个 item 不会被处理。

## 使用 If 和 Merge node 进行分支执行 <a href="#branch-execution-with-if-and-merge-nodes" id="branch-execution-with-if-and-merge-nodes"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/o5sVhTw0cyO5aAAkAVDj/" %}


## 试试看：逐步示例 <a href="#try-it-out-a-step-by-step-example" id="try-it-out-a-step-by-step-example"></a>

创建一个带有示例输入数据的 workflow，试用 Merge node。

### 使用 Code node 设置示例数据 <a href="#set-up-sample-data-using-the-code-nodes" id="set-up-sample-data-using-the-code-nodes"></a>

1. 向 canvas 添加一个 Code node，并将它连接到 Start node。
2. 在 **JavaScript Code** 字段中粘贴以下 JavaScript 代码片段：
```js
return [
  {
    json: {
      name: 'Stefan',
      language: 'de',
    }
  },
  {
    json: {
      name: 'Jim',
      language: 'en',
    }
  },
  {
    json: {
      name: 'Hans',
      language: 'de',
    }
  }
];
```
3. 添加第二个 Code node，并将它连接到 Start node。
4. 在 **JavaScript Code** 字段中粘贴以下 JavaScript 代码片段：
```js
return [
	  {
    json: {
      greeting: 'Hello',
      language: 'en',
    }
  },
  {
    json: {
      greeting: 'Hallo',
      language: 'de',
    }
  }
];
```

### 试用不同 merge mode <a href="#try-out-different-merge-modes" id="try-out-different-merge-modes"></a>

添加 Merge node。将第一个 Code node 连接到 **Input 1**，将第二个 Code node 连接到 **Input 2**。运行 workflow，将数据加载到 Merge node 中。

最终 workflow 应如下所示：

{% @n8n-blocks/n8n-workflow-demo content="" url="https://api.n8n.io/workflows/templates/655" %}

现在尝试 **Mode** 中的不同选项，查看它如何影响输出数据。

#### Append <a href="#append" id="append"></a>

选择 **Mode** > **Append**，然后选择 **Execute step**。

表格视图中的输出应如下所示：

| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | de |  |
| Jim | en |  |
| Hans | de |  |
|   | en | Hello |
|   | de | Hallo |


#### Combine by Matching Fields <a href="#combine-by-matching-fields" id="combine-by-matching-fields"></a>

你可以合并这两个数据输入，使每个人都获得其语言对应的正确问候语。

1. 选择 **Mode** > **Combine**。
2. 选择 **Combine by** > **Matching Fields**。
3. 在 **Input 1 Field** 和 **Input 2 Field** 中都输入 `language`。这会告诉 n8n 通过匹配每个数据集中的 `language` 字段值来合并数据。
4. 选择 **Execute step**。

表格视图中的输出应如下所示：


| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | de | Hallo |
| Jim | en | Hello  |
| Hans | de | Hallo |


#### Combine by Position <a href="#combine-by-position" id="combine-by-position"></a>

选择 **Mode** > **Combine**、**Combine by** > **Position**，然后选择 **Execute step**。

表格视图中的输出应如下所示：

| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Jim | de | Hallo  |


##### 保留未配对 item <a href="#keep-unpaired-items" id="keep-unpaired-items"></a>

如果想保留所有 item，请选择 **Add Option** > **Include Any Unpaired Items**，然后开启 **Include Any Unpaired Items**。

表格视图中的输出应如下所示：

| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Jim | de | Hallo  |
| Hans | de |  |


#### Combine by All Possible Combinations <a href="#combine-by-all-possible-combinations" id="combine-by-all-possible-combinations"></a>

选择 **Mode** > **Combine**、**Combine by** > **All Possible Combinations**，然后选择 **Execute step**。

表格视图中的输出应如下所示：

| **name** | **language** | **greeting** |
| --- | --- | --- |
| Stefan | en | Hello |
| Stefan | de | Hallo |
| Jim | en | Hello  |
| Jim | de | Hallo |
| Hans | en | Hello |
| Hans | de | Hallo |

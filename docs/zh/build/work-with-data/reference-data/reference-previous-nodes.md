---
description: >-
  处理当前 node 输入和前序 node 输出的方法。
contentType: reference
nodeTitle: Reference previous nodes
originalFilePath: data/data-mapping/referencing-other-nodes.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/referencing-other-nodes'
url: >-
  https://docs.n8n.io/build/work-with-data/reference-data/reference-previous-nodes
layout:
  description:
    visible: false
---

# 引用前序 node <a href="#referencing-previous-nodes" id="referencing-previous-nodes"></a>

在 n8n 中处理数据时，你经常需要引用当前 node 或工作流中前序 node 的信息。

## 常见引用方式 <a href="#common-ways-of-referencing" id="common-ways-of-referencing"></a>

最常用的数据访问方式是：

- **`$json`**：访问当前输入 item 中的 JSON 数据
- **`$('<node-name>').item.json`**：访问前序 node 中 [linked item](link-data-items/README.md) 的 JSON 数据

## 其他引用方法 <a href="#other-referencing-methods" id="other-referencing-methods"></a>

这些方法既适用于 expression，也适用于 Code node：

| 方法 | 描述 |
| ------ | ----------- |
| `$binary` | 访问当前输入 item 中的 binary 数据 |
| `$input.item` | 当前正在处理的输入 item |
| `$('<node-name>').first()` | 获取指定 node 的第一个 item |
| `$('<node-name>').last()` | 获取指定 node 的最后一个 item |
| `$('<node-name>').all()` | 获取指定 node 的所有 item |

## 当前 node 输入 <a href="#current-node-input" id="current-node-input"></a>

用于处理当前 node 输入的方法。部分方法和变量在 Code node 中不可用。

{% hint style="info" %}
**Python 支持**

你可以在 Code node 中使用 Python。Expression 中不支持 Python。
{% endhint %}
{% tabs %}
{% tab title="JavaScript" %}
| 方法 | 描述 | 在 Code node 中可用？ |
| ------ | ----------- | :-------------------------: |
| `$binary` | `$input.item.binary` 的简写。来自 node 的传入 binary 数据 | ❌ |
| `$input.item` | 当前 node 正在处理的输入 item。有关 paired item 和 item linking 的更多信息，请参阅 [Item linking](link-data-items/README.md)。 | ✅ |
| `$input.all()` | 当前 node 中的所有输入 item。 | ✅ |
| `$input.first()` | 当前 node 中的第一个输入 item。 | ✅ |
| `$input.last()` | 当前 node 中的最后一个输入 item。 | ✅ |
| `$input.params` | 包含前一个 node 查询设置的对象。这包括它运行的 operation、结果限制等数据。 | ✅ |
| `$json` | `$input.item.json` 的简写。来自 node 的传入 JSON 数据。有关 item 结构的信息，请参阅[数据结构](../understand-n8ns-data-structure.md)。 | ✅（以每个 item 运行一次时） |
| `$input.context.noItemsLeft` | Boolean。仅在使用 Loop Over Items node 时可用。提供 node 中正在发生什么的信息。可用它判断 node 是否仍在处理 item。 | ✅ |
{% endtab %}

{% tab title="Python" %}
| 方法 | 描述 |
| ------ | ----------- |
| `_input.item` | 当前 node 正在处理的输入 item。有关 paired item 和 item linking 的更多信息，请参阅 [Item linking](link-data-items/README.md)。 |
| `_input.all()` | 当前 node 中的所有输入 item。 |
| `_input.first()` | 当前 node 中的第一个输入 item。 |
| `_input.last()` | 当前 node 中的最后一个输入 item。 |
| `_input.params` | 包含前一个 node 查询设置的对象。这包括它运行的 operation、结果限制等数据。 |
| `_json` | `_input.item.json` 的简写。来自 node 的传入 JSON 数据。有关 item 结构的信息，请参阅[数据结构](../understand-n8ns-data-structure.md)。当你将 **Mode** 设置为 **Run Once for Each Item** 时可用。 |
| `_input.context.noItemsLeft` | Boolean。仅在使用 Loop Over Items node 时可用。提供 node 中正在发生什么的信息。可用它判断 node 是否仍在处理 item。 |
{% endtab %}
{% endtabs %}

## 其他 node 的输出 <a href="#output-of-other-nodes" id="output-of-other-nodes"></a>

用于处理其他 node 输出的方法。部分方法和变量在 Code node 中不可用。

{% tabs %}
{% tab title="JavaScript" %}
| 方法 | 描述 | 在 Code node 中可用？ |
| ------ | ----------- | :-------------------------: |
| `$("<node-name>").all(branchIndex?, runIndex?)` | 返回指定 node 的所有 item。如果未提供 `branchIndex`，则默认使用将 `node-name` 与你使用 expression 或代码的 node 相连接的输出。 | ✅ |
| `$("<node-name>").first(branchIndex?, runIndex?)` | 指定 node 输出的第一个 item。如果未提供 `branchIndex`，则默认使用将 `node-name` 与你使用 expression 或代码的 node 相连接的输出。 | ✅ |
| `$("<node-name>").last(branchIndex?, runIndex?)` | 指定 node 输出的最后一个 item。如果未提供 `branchIndex`，则默认使用将 `node-name` 与你使用 expression 或代码的 node 相连接的输出。 | ✅ |
| `$("<node-name>").item` | linked item。它是指定 node 中用于生成当前 item 的 item。有关 item linking 的更多信息，请参阅 [Item linking](link-data-items/README.md)。 | ✅ |
| `$("<node-name>").params` | 包含指定 node 查询设置的对象。这包括它运行的 operation、结果限制等数据。 | ✅ |
| `$("<node-name>").context` | Boolean。仅在使用 Loop Over Items node 时可用。提供 node 中正在发生什么的信息。可用它判断 node 是否仍在处理 item。 | ✅ |
| `$("<node-name>").itemMatching(currentNodeInputIndex)` | 如果需要从输入 item 反向追踪，请在 Code node 中使用它替代 `$("<node-name>").item`。 | ✅ |
{% endtab %}
{% endtabs %}

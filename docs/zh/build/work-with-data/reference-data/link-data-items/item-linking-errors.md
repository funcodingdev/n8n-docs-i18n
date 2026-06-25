---
contentType: reference
nodeTitle: Item linking errors
originalFilePath: data/data-mapping/data-item-linking/item-linking-errors.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-errors'
url: >-
  https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/item-linking-errors
layout:
  description:
    visible: false
---

# Item linking errors <a href="#item-linking-errors" id="item-linking-errors"></a>

在 n8n 中，你可以引用任意前序 node 的数据。它不一定是紧邻前一个 node：可以是链条中的任意前序 node。引用更早的 node 时，可以使用 expression 语法 `$(node_name).item`。

<figure markdown>
<img src="../../../../../build/.gitbook/assets/item-linking-multiple-lines.png" alt="">
<figcaption markdown>不同 item 的 thread 图。由于 item linking，你可以使用 `$('Get famous movie actors').item` 获取每部电影的演员。</figcaption>
</figure>

由于前序 node 中可能有多个 item，n8n 需要知道要使用哪一个。使用 `.item` 时，n8n 会在后台为你判断。有关其工作方式的详细信息，请参阅 [Item linking concepts](how-items-link-through-workflows.md)。

如果缺少信息，`.item` 会失败。为了确定要使用哪个 item，n8n 会为每个 item 维护一条向前穿过工作流 node 的 thread。对于给定 item，这条 thread 会告诉 n8n 是前序 node 中的哪些 item 生成了它。为了在给定前序 node 中找到匹配 item，n8n 会沿着这条 thread 回溯，直到到达目标 node。

使用 `.item` 时，n8n 会在以下情况下显示错误：

- thread 断裂
- thread 指向前序 node 中的多个 item（因为不清楚要使用哪一个）

如需解决这些错误，你可以避免使用 `.item`，或修复根本原因。

你可以改用 `.first()`、`.last()` 或 `.all()[index]` 来避免使用 `.item`。这些方法要求你知道目标 item 在目标 node 输出 item 中的位置。有关这些方法的更多详情，请参阅[引用前序 node](../reference-previous-nodes.md)。

根本原因的修复方式取决于具体错误。

### 修复 'Info for expressions missing from previous node' <a href="#fix-for-info-for-expressions-missing-from-previous-node" id="fix-for-info-for-expressions-missing-from-previous-node"></a>

如果看到此错误消息：

> ERROR: Info for expression missing from previous node

链条中有一个 node 没有返回 pairing 信息。解决方案取决于前序 node 的类型：

- Code nodes：确保返回该 node 使用哪些输入 item 生成每个输出 item。更多信息请参阅 [Preserving linking in the Code node](preserving-linking-in-the-code-node.md)。
- Custom 或 community nodes：node 创建者需要更新该 node，使其返回用于生成每个输出 item 的输入 item。更多信息请参阅 [Item linking for node creators](item-linking-for-node-creators.md)。

### 修复 'Multiple matching items for expression' <a href="#fix-for-multiple-matching-items-for-expression" id="fix-for-multiple-matching-items-for-expression"></a>

错误消息如下：

> ERROR: Multiple matching items for expression

有时 n8n 会使用多个 item 创建单个 item。例如 Summarize、Aggregate 和 Merge nodes。这些 node 可以组合来自多个 item 的信息。

当你使用 `.item` 且存在多个可能匹配项时，n8n 不知道该使用哪一个。要解决此问题，你可以：

- 改用 `.first()`、`.last()` 或 `.all()[index]`。有关这些方法的更多详情，请参阅[引用前序 node](../reference-previous-nodes.md)。
- 引用另一个包含相同信息、但没有多个匹配 item 的 node。

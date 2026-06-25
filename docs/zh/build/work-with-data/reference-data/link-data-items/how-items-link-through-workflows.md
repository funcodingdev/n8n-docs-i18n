---
contentType: explanation
nodeTitle: How items link through workflows
originalFilePath: data/data-mapping/data-item-linking/item-linking-concepts.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/data-item-linking/item-linking-concepts'
url: >-
  https://docs.n8n.io/build/work-with-data/reference-data/link-data-items/how-items-link-through-workflows
layout:
  description:
    visible: false
---

# Item 如何在工作流中链接 <a href="#how-items-link-through-workflows" id="how-items-link-through-workflows"></a>

Node 创建的每个输出 item 都包含元数据，用于将它们链接到该 node 用来生成它们的输入 item。这会创建一条 item 链，你可以沿着这条链回溯访问先前 item。这可能较难理解，尤其是在 node 拆分或合并数据时。构建自己的编程式 node，或在某些场景中使用 Code node 时，你需要理解 item linking。

本文档提供此功能的概念概览。使用详情请参阅：

* [Item linking for node creators](item-linking-for-node-creators.md)，了解构建 node 时如何处理 item linking。
* [Preserving linking in the Code node](preserving-linking-in-the-code-node.md)，了解如何在 Code node 中处理 item linking。
* [Item linking errors](item-linking-errors.md)，了解你可能在编辑器 UI 中遇到的错误。

## n8n 的自动 item linking <a href="#n8ns-automatic-item-linking" id="n8ns-automatic-item-linking"></a>

如果 node 没有控制如何将输入 item 链接到输出 item，n8n 会尝试自动推断如何链接这些 item：

* 单个输入、单个输出：输出链接到输入。
* 单个输入、多个输出：所有输出都链接到该输入。
* 多个输入和输出：
	* 如果你保留输入 item，但更改顺序（或移除部分 item 但保留其他 item），n8n 可以自动添加正确的 linked item 信息。
	* 如果输入和输出数量相等，n8n 会按顺序链接 item。这意味着 output-1 链接到 input-1，output-2 链接到 input-2，依此类推。
	* 如果数量不相等，或你创建了全新的 item，n8n 无法自动链接 item。

如果 n8n 无法自动链接 item，而 node 也没有处理 item linking，n8n 会显示错误。更多信息请参阅 [Item linking errors](item-linking-errors.md)。

## Item linking 示例 <a href="#item-linking-example" id="item-linking-example"></a>

![显示多个 item 通过工作流向前回链的 threads 图](../../../../../build/.gitbook/assets/item-linking-multiple-lines.png)

在此示例中，即使 item 顺序发生变化，n8n 仍可以将某个 node 中的 item 向前链接回多个步骤。这意味着按字母顺序对电影排序的 node 可以访问获取著名电影演员的 node 中 linked item 的信息。

访问 linked item 的方式会因使用 UI、expression 还是 Code node 而不同。可查看以下资源：

* [在 UI 中 mapping](../use-the-ui-mapper.md)
* [在 Code node 中保留 linking](preserving-linking-in-the-code-node.md)
* [Item linking errors](item-linking-errors.md)

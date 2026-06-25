---
title: 子工作流转换
description: 选择工作流中的节点，并将它们转换为子工作流。
contentType: howto
nodeTitle: Convert to sub-workflows
originalFilePath: workflows/subworkflow-conversion.md
originalUrl: 'https://docs.n8n.io/workflows/subworkflow-conversion'
url: 'https://docs.n8n.io/build/flow-logic/convert-to-sub-workflows'
layout:
  description:
    visible: false
---

# 子工作流转换 <a href="#sub-workflow-conversion" id="sub-workflow-conversion"></a>

{% hint style="info" %}
**功能可用性**

从 n8n 1.97.0 起，所有方案均可使用。
{% endhint %}

使用子工作流转换，可以将你的工作流重构为可复用的部分。引用其他节点的 expressions 会自动更新，并作为参数添加到 [Execute Workflow Trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger) 节点中。

概念上的一般介绍请参阅[子工作流](break-workflows-into-smaller-parts.md)。

## 为子工作流选择节点 <a href="#selecting-nodes-for-a-sub-workflow" id="selecting-nodes-for-a-sub-workflow"></a>

要将工作流的一部分转换为子工作流，必须在原工作流中选择想要转换的节点。

选择一组有效节点即可。选择范围必须连续，并且与工作流其余部分最多只能通过一个起始节点和一个结束节点连接。选择范围必须满足以下条件：

- 不得包含 trigger nodes。
- 选择范围中只能有一个节点接收来自选择范围*外部*节点的传入连接。
	- 该节点可以有多个传入连接，但只能有一个输入*分支*（这意味着它不能是 [Merge node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.merge) 等节点）。
	- 该节点不能接收来自选择范围内其他节点的传入连接。
- 选择范围中只能有一个节点向选择范围*外部*的节点发出连接。
	- 该节点可以有多个传出连接，但只能有一个输出分支（例如它不能是 [If node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if)）。
	- 该节点不能向选择范围内的其他节点发出连接。
- 选择范围必须包含输入节点和输出节点之间的所有节点。

## 如何将工作流的一部分转换为子工作流 <a href="#how-to-convert-part-of-a-workflow-to-a-sub-workflow" id="how-to-convert-part-of-a-workflow-to-a-sub-workflow"></a>

在画布上选择目标节点。右键点击画布背景，然后选择 **Convert to sub-workflow**。

## 注意事项 <a href="#things-to-keep-in-mind" id="things-to-keep-in-mind"></a>

大多数子工作流转换都能顺利完成，但需要注意以下限制和细节：

* **必须手动设置输入和输出的类型约束**：默认情况下，子工作流输入和输出允许所有类型。你可以在子工作流的 [Execute Sub-workflow Trigger node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger) 和 [Edit Fields (set) node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.set) 中设置期望类型（后者标记为 **Return**，并且仅在子工作流有输出时包含）。
* **对 AI nodes 的支持有限**：处理 AI tools 这类 sub-nodes 时，必须全部选中它们，并且可能需要在转换前复制与其他 AI Agents 共享的节点。
- **使用 v1 执行顺序：** 新工作流会使用 [`v1` 执行顺序](understand-execution-order.md)，不管父工作流的设置是什么。你可以在设置中改回去。
* **`first()`、`last()` 和 `all()` 这类访问函数需要额外注意**：使用这些函数的 expressions 并不总是能干净地转换到子工作流上下文。n8n 可能会转换它们以尽量保留原有功能，但你应检查它们在新上下文中是否按预期工作。<br>

	<div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Sub-node 参数后缀</strong></p><p>n8n 会给这些函数访问的变量名添加 <code>_firstItem</code>、<code>_lastItem</code> 和 <code>_allItems</code> 等后缀。这样有助于保留原表达式的信息，因为 item 顺序在子工作流上下文中可能不同。</p></div>


* **`itemMatching` 函数需要固定索引**：使用 [`itemMatching` function](../work-with-data/reference-data/reference-previous-nodes.md) 时，不能使用表达式作为索引值。必须传入固定数字。

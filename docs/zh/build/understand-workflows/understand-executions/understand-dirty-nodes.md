---
title: Dirty nodes
description: 什么是 dirty node，以及它们如何影响工作流 execution。
contentType: explanation
nodeTitle: Understand dirty nodes
originalFilePath: workflows/executions/dirty-nodes.md
originalUrl: 'https://docs.n8n.io/workflows/executions/dirty-nodes'
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/understand-dirty-nodes
layout:
  description:
    visible: false
---

# Dirty nodes <a href="#dirty-nodes" id="dirty-nodes"></a>

**Dirty node** 是过去曾成功执行，但其输出现在被 n8n 视为陈旧或不可靠的 node。标记为 dirty node 表示如果该 node 再次执行，输出可能会不同。它也可能是 [partial execution](types-of-executions.md#partial-executions) 的起点。

## 如何识别 dirty node 数据 <a href="#how-to-recognize-dirty-node-data" id="how-to-recognize-dirty-node-data"></a>

在工作流编辑器的画布中，你可以通过不同颜色的边框，以及替代先前绿色勾选符号的黄色三角形识别 dirty node。例如：

!["带黄色边框显示的 node 图片"](../../../../build/.gitbook/assets/dirty-node-canvas.png)

在 node 编辑器视图中，输出面板也会显示黄色三角形。将鼠标悬停在三角形上时，会出现 tooltip，显示 n8n 为什么认为这些数据陈旧的更多信息：

!["带黄色边框显示的 node 图片"](../../../../build/.gitbook/assets/dirty-node-editor.png)

## 为什么 n8n 会将 node 标记为 dirty <a href="#why-n8n-marks-nodes-dirty" id="why-n8n-marks-nodes-dirty"></a>

n8n 可能会因为多种原因将 execution 数据标记为陈旧。例如：

- 插入或删除 node：将插入 node 之后的第一个 node 标记为 dirty。
- 修改 node 参数：将被修改的 node 标记为 dirty。
- 添加 connector：将新 connector 的目标 node 标记为 dirty。
- 停用 node：将停用 node 之后的第一个 node 标记为 dirty。

<details>

<summary>n8n 将 node 标记为 dirty 的其他原因</summary>

- 取消固定 node：将被取消固定的 node 标记为 dirty。
- 修改已固定数据：将已固定数据之后的 node 标记为 dirty。
- 如果上述任何操作发生在 loop 内，也会将 loop 的第一个 node 标记为 dirty。

对于 sub-node，在以下情况下，也会标记已执行的父 node（直到并包括 root）：

- 编辑已执行的 sub-node
- 添加新的 sub-node
- 断开或删除 sub-node
- 停用 sub-node
- 启用 sub-node

</details>

<div class="grid cards" markdown>

-   删除工作流中已连接的 node 时：

    !["带黄色边框显示的 node 图片"](../../../../build/.gitbook/assets/dirty-before.png)

-   序列中的下一个 node 会变为 dirty：

    !["带黄色边框显示的 node 图片"](../../../../build/.gitbook/assets/dirty-after.png)

</div>

使用 loop（通过 [Loop over Items](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.splitinbatches) node）时，如果 loop 内的任何 node 是 dirty，loop 的初始 node 也会被视为 dirty：

!["带黄色边框显示的 node 图片"](../../../../build/.gitbook/assets/dirty-loop.png)

## 解决 dirty node <a href="#resolving-dirty-nodes" id="resolving-dirty-nodes"></a>

再次执行 node 会清除其 dirty 状态。你可以通过触发整个工作流手动完成，也可以在单个 node 或其后任意 node 上使用 **Execute step** 运行 [partial execution](types-of-executions.md#partial-executions)。

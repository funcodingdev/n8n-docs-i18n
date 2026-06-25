---
description: 在画布上将相关 node 分组，让大型工作流保持可读。
contentType: howto
nodeTitle: Canvas Groups
originalFilePath: workflows/components/canvas-groups.md
originalUrl: 'https://docs.n8n.io/workflows/components/canvas-groups'
url: >-
  https://docs.n8n.io/build/understand-workflows/workflow-components/canvas-groups
layout:
  description:
    visible: false
---

# Canvas Groups <a href="#canvas-groups" id="canvas-groups"></a>

Canvas Groups 允许你在画布上将相关 node 组织到一个有名称的分组中。你可以把处理工作流某一部分的 node 放入一组，为其命名，并在需要更清爽视图时折叠它。Canvas Group 会随工作流一起保存，因此任何打开该工作流的人都能看到相同结构。你也可以折叠 Canvas Group 以获得更清爽的视图，这是一项保存在浏览器中的个人偏好。

![包含多个已折叠 Canvas Groups 的工作流](../../../../build/.gitbook/assets/canvas-groups-overview.png)

## 创建 Canvas Group <a href="#create-a-canvas-group" id="create-a-canvas-group"></a>

1. 选择要分组的 node。可以拖出选择框框住它们，或按住 `Ctrl/Cmd` 并点击每个 node。
2. 在选区上方的工具栏中选择 **Group nodes** 图标 <img src="../../../../build/.gitbook/assets/group.svg" alt="Group nodes icon" data-size="line">，或按 `Ctrl/Cmd` + `G`。
3. n8n 会创建 Canvas Group，并高亮名称字段，方便你立即输入名称。

只有当选区能组成有效 Canvas Group 时，才能进行分组。规则请参阅[可分组的内容](#what-you-can-group)。

## 命名 Canvas Group <a href="#name-a-canvas-group" id="name-a-canvas-group"></a>

创建 Canvas Group 时，n8n 会自动分配默认名称（例如 “Group 1”）并高亮该名称，你可以立即替换为更具描述性的名称，也可以保留建议名称。稍后如需重命名分组，双击分组名称，编辑文本，然后点击分组外任意位置保存。分组名称不能为空。

## 折叠和展开 Canvas Group <a href="#collapse-and-expand-a-canvas-group" id="collapse-and-expand-a-canvas-group"></a>

折叠 Canvas Group 会隐藏其中的 node，只显示名称。这样可以把大型工作流压缩成更易读的视图。折叠后，它只显示名称，不显示其他内容。

选择折叠或展开图标，可在两种状态之间切换。每次只能折叠或展开一个 Canvas Group。

n8n 会记住你展开了哪些 Canvas Group，并在你重新打开工作流时保持相同视图。该偏好保存在你的浏览器中，因此只对你和你的设备生效。它不会随工作流保存，也不会同步到其他浏览器或其他用户。

## 取消分组 <a href="#ungroup" id="ungroup"></a>

如需将 Canvas Group 拆回独立 node，选择其上方的 **Ungroup** 图标 <img src="../../../../build/.gitbook/assets/ungroup.svg" alt="Ungroup icon" data-size="line">，或按 `Ctrl/Cmd` + `Shift` + `G`。这些 node 会保留在画布上。

## 可分组的内容 <a href="#what-you-can-group" id="what-you-can-group"></a>

并非每个选区都能变成 Canvas Group。选择 node 时，n8n 会检查一些规则，只有全部通过时才会显示 **Group nodes** 图标 <img src="../../../../build/.gitbook/assets/group.svg" alt="Group nodes icon" data-size="line">。如果图标没有出现，请按以下规则检查选区：

- 这些 node 尚未属于另一个 Canvas Group。
- 选区不包含 trigger node。Trigger 用于锚定工作流起点，会保留在 Canvas Group 之外。
- 这些 node 构成一条相连的链。不能把彼此不相邻的 node 加入同一个 Canvas Group。
- Canvas Group 外部的 node 只能通过该组的第一个 node 和最后一个 node 与其连接，不能直接连接到中间的 node。
- AI node 及其 sub-node（chat model、memory 和 tool）必须一起位于同一个 Canvas Group 中。Sub-node connection 不能跨越 Canvas Group 边界。

## 只读工作流中的 Canvas Groups <a href="#canvas-groups-in-read-only-workflows" id="canvas-groups-in-read-only-workflows"></a>

当工作流以只读方式显示时，例如在工作流历史或共享视图中，Canvas Groups 默认会展开，以便你查看完整工作流。

## 键盘快捷键 <a href="#keyboard-shortcuts" id="keyboard-shortcuts"></a>

| 操作 | 快捷键 |
| ------ | -------- |
| 分组选中的 node | `Ctrl/Cmd` + `G` |
| 取消选中 node 的分组 | `Ctrl/Cmd` + `Shift` + `G` |

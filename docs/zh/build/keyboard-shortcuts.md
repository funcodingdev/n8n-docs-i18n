---
tags:
  - Keyboard
  - Move canvas
  - Move nodes
  - Drag and drop
description: n8n 中可用的键盘快捷键。
hide:
  - tags
contentType: reference
nodeTitle: Keyboard shortcuts
originalFilePath: keyboard-shortcuts.md
originalUrl: 'https://docs.n8n.io/keyboard-shortcuts'
url: 'https://docs.n8n.io/build/keyboard-shortcuts'
layout:
  description:
    visible: false
---

# 键盘快捷键和控制方式 <a href="#keyboard-shortcuts-and-controls" id="keyboard-shortcuts-and-controls"></a>

n8n 为部分操作提供键盘快捷键。

## 工作流控制 <a href="#workflow-controls" id="workflow-controls"></a>

 - **Ctrl/Cmd** + **Alt** + **n**：创建新工作流
 - **Ctrl/Cmd** + **o**：打开工作流
 - **Ctrl/Cmd** + **s**：保存当前工作流
 - **Ctrl/Cmd** + **z**：撤销
 - **Ctrl/Cmd** + **shift** + **z**：重做
 - **Ctrl/Cmd** + **Enter**：执行工作流

## 画布 <a href="#canvas" id="canvas"></a>

### 移动画布 <a href="#move-the-canvas" id="move-the-canvas"></a>

 - **Ctrl/Cmd** + **Left Mouse Button** + 拖动：移动节点视图
 - **Ctrl/Cmd** + **Middle mouse button** + 拖动：移动节点视图
 - **Space** + 拖动：移动节点视图
 - **Middle mouse button** + 拖动：移动节点视图
 - 在触摸屏上使用双指：移动节点视图

### 画布缩放 <a href="#canvas-zoom" id="canvas-zoom"></a>

- **+** 或 **=**：放大
- **-** 或 **_**：缩小
- **0**：重置缩放级别
- **1**：缩放以适应工作流
- **Ctrl/Cmd** + **Mouse wheel**：放大/缩小

### 画布上的节点 <a href="#nodes-on-the-canvas" id="nodes-on-the-canvas"></a>

- 在节点上 **Double click**：打开节点详情
- 在 sub-workflow 节点上 **Ctrl/Cmd** + **Double click**：在新标签页中打开 sub-workflow
- **Ctrl/Cmd** + **a**：选择所有节点
- **Ctrl/Cmd** + **v**：粘贴节点
- **Shift** + **s**：添加 sticky note

### 在画布中选中一个或多个节点时 <a href="#with-one-or-more-nodes-selected-in-canvas" id="with-one-or-more-nodes-selected-in-canvas"></a>

 - **ArrowDown**：选择当前节点下方的同级节点
 - **ArrowLeft**：选择当前节点左侧的节点
 - **ArrowRight**：选择当前节点右侧的节点
 - **ArrowUp**：选择当前节点上方的同级节点
 - **Ctrl/Cmd** + **c**：复制
 - **Ctrl/Cmd** + **g**：组合选中的节点
 - **Ctrl/Cmd** + **shift** + **g**：取消组合选中的节点
 - **Ctrl/Cmd** + **x**：剪切
 - **D**：停用
 - **Delete**：删除
 - **Enter**：打开
 - **F2**：重命名
 - **P**：固定节点中的数据。更多信息请参阅 [Data pinning](work-with-data/pin-and-mock-data.md)。
 - **Shift** + **ArrowLeft**：选择当前节点左侧的所有节点
 - **Shift** + **ArrowRight**：选择当前节点右侧的所有节点
 - 在 sub-workflow 节点上 **Ctrl/Cmd** + **Shift** + **o**：在新标签页中打开 sub-workflow

## 节点面板 <a href="#node-panel" id="node-panel"></a>

 - **N**：打开节点面板
 - **Enter**：将选中的节点插入工作流
 - **Escape**：关闭节点面板

### 节点面板分类 <a href="#node-panel-categories" id="node-panel-categories"></a>

- **Enter**：插入节点、折叠/展开分类、打开子分类
- **ArrowRight**：展开分类、打开子分类
- **ArrowLeft**：折叠分类、关闭子分类视图

## 在节点内部 <a href="#within-nodes" id="within-nodes"></a>

- **=**：在空参数输入框中，切换到 expressions[^1] 模式。

## 命令栏 <a href="#command-bar" id="command-bar"></a>

Command Bar 提供贯穿 n8n 的操作和导航快捷入口。使用 **Ctrl/Cmd + K** 打开，或点击画布上的放大镜图标。命令会根据你当前所在视图和权限动态调整。

* **工作流操作：** 添加节点、保存、测试、整理、发布/取消发布、复制、导入/导出、归档、删除
* **资源导航：** 创建和打开工作流、凭据、data tables、projects；访问最近资源
* **执行操作：** 调试、复制、重试、停止或删除 executions
* **通用导航：** 访问 Templates、Variables、Insights、Settings、Help resources 和 Documentation

[^1]: 在 n8n 中，expressions 可以通过执行 JavaScript 代码动态填充节点参数。你不必提供静态值，而是可以使用 n8n expression 语法，基于前置节点、其他工作流或 n8n 环境中的数据定义该值。

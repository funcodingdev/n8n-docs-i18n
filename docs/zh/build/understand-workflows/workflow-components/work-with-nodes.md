---
contentType: howto
nodeTitle: Work with nodes
originalFilePath: workflows/components/nodes.md
originalUrl: https://docs.n8n.io/workflows/components/nodes
url: >-
  https://docs.n8n.io/build/understand-workflows/workflow-components/work-with-nodes
description: >-
  Node 可以是获取数据的入口、处理数据的功能单元，也可以是发送数据的出口。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 使用 node

Node[^1] 是工作流[^2]的关键组成模块。它们可以执行多种操作，包括：

* 启动工作流。
* 获取和发送数据。
* 处理和操作数据。

n8n 提供了一组内置 node，也支持创建你自己的 node。参阅：

* [内置集成](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/node-types)，浏览 node 库。
* [社区 node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/community-nodes/installation-and-management)，了解如何查找和安装社区创建的 node。
* [创建 node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview)，开始构建你自己的 node。

## 向工作流添加 node <a href="#add-a-node-to-your-workflow" id="add-a-node-to-your-workflow"></a>

### 向空工作流添加 node <a href="#add-a-node-to-an-empty-workflow" id="add-a-node-to-an-empty-workflow"></a>

1. 选择 **Add first step**。n8n 会打开 nodes 面板，你可以在其中搜索或浏览 [trigger nodes](#user-content-fn-3)[^3]。
2.  选择要使用的 trigger。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>选择正确的 app event</strong></p><p>如果选择 <strong>On App Event</strong>，n8n 会显示所有受支持服务的列表。使用此列表浏览 n8n 的集成，并在所选服务发生事件时触发工作流。并非所有集成都有 trigger。如需查看哪些集成可用作 trigger，请选择该 node。如果 trigger 可用，你会在可用操作列表顶部看到它。</p><p>例如，下面是 Asana 的 trigger：</p><p><img src="../../../../build/.gitbook/assets/recommended-trigger.png" alt="Asana node 操作列表截图，顶部显示 Recommended 部分" data-size="original"></p></div>

### 向现有工作流添加 node <a href="#add-a-node-to-an-existing-workflow" id="add-a-node-to-an-existing-workflow"></a>

选择 **Add node** <img src="../../../../build/.gitbook/assets/add-node-small (1).png" alt="Add node icon" data-size="line"> connector。n8n 会打开 nodes 面板，你可以在其中搜索或浏览所有 node。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/nqwVeyXZtOyDsX8afllD/" %}

## Node 控件 <a href="#node-controls" id="node-controls"></a>

如需查看 node 控件，将鼠标悬停在画布上的 node 上：

* **Execute step** <img src="../../../../build/.gitbook/assets/play-node.png" alt="Execute step icon" data-size="line">：运行 node。
* **Deactivate** <img src="../../../../build/.gitbook/assets/power-off.png" alt="Deactivate node icon" data-size="line">：停用 node。
* **Delete** <img src="../../../../build/.gitbook/assets/delete-node (1).png" alt="Delete node icon" data-size="line">：删除 node。
* **Node context menu** <img src="../../../../build/.gitbook/assets/node-context-menu (1).png" alt="Node context menu icon" data-size="line">：选择 node 操作。可用操作包括：
  * Open node
  * Execute step
  * Rename node
  * Deactivate node
  * Pin node
  * Copy node
  * Duplicate node
  * Tidy up workflow
  * Convert node to sub-workflow
  * Select all
  * Clear selection
  * Delete node

## Node 设置 <a href="#node-settings" id="node-settings"></a>

**Settings** 标签下的 node 设置允许你控制 node 行为并添加 node 备注。

启用或设置后，它们的作用如下：

* **Always Output Data**：即使 node 在执行期间没有返回数据，也会返回一个空 item。在 IF node 上设置此项时要小心，因为它可能导致无限循环。
* **Execute Once**：node 只执行一次，并使用它收到的第一个 item 的数据。它不会处理额外 item。
* **Retry On Fail**：当 execution 失败时，node 会重新运行，直到成功。
* **On Error**:
  * **Stop Workflow**：发生错误时停止整个工作流，防止继续执行后续 node。
  * **Continue**：尽管发生错误，仍使用最后一份有效数据继续执行到下一个 node。
  * **Continue (using error output)**：继续执行工作流，并将错误信息传递给下一个 node，供后续处理。
* **Custom Span Attributes**：向 node 的 OpenTelemetry span 添加自定义键值属性。键是纯文本，值支持表达式。只有启用 OpenTelemetry tracing 并拥有 Enterprise license 时，才会显示此设置。详情请参阅 [Custom span attributes](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry#custom-span-attributes)。

你可以使用 node notes 为工作流添加文档说明：

* **Notes**：随 node 保存的备注。
* **Display note in flow**：启用后，n8n 会在工作流中将备注显示为副标题。

[^1]: 在 n8n 中，node 是用于组合创建工作流的独立组件。Node 定义工作流应在何时运行，允许你获取、发送和处理数据，可以定义流程控制逻辑，并与外部服务连接。
[^2]: n8n workflow 是一组用于自动化流程的 node。工作流会在触发条件发生时开始执行，并按顺序执行以完成复杂任务。
[^3]: Trigger node 是一种特殊 node，负责根据特定条件执行工作流。所有生产工作流都至少需要一个 trigger，用于确定工作流应在何时运行。

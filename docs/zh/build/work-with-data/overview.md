---
contentType: overview
nodeTitle: Overview
originalFilePath: data/index.md
originalUrl: 'https://docs.n8n.io/data'
url: 'https://docs.n8n.io/build/work-with-data/overview'
layout:
  description:
    visible: false
---

# 概览 <a href="#overview" id="overview"></a>

在 n8n 中，数据会在工作流中从一个 node 流向另一个 node。每个 node 接收数据、处理数据，并将结果传递给下一个 node。理解数据如何在工作流中移动和转换，是构建有效工作流的关键。

## n8n 中的数据如何工作 <a href="#how-data-works-in-n8n" id="how-data-works-in-n8n"></a>

**数据流经 node**：连接 node 后，数据会自动从一个 node 传递到下一个 node。每个 node 会处理传入数据，并根据自身配置输出结果。

**查看每个阶段的数据**：你可以在工作流中的任意位置检查数据：

- **Node details view**：双击任意 node 查看其输入和输出数据。可在 **Schema**、**Table** 和 **JSON** 视图之间切换。Schema 视图只显示第一个 item 的简化结构，Table 和 JSON 会显示完整数据集。
- **Execution logs**：查看过去的工作流运行，了解经过每个 node 的数据。

**引用先前数据**：使用 [data mapping](reference-data/README.md) 引用工作流中前序 node 的数据。你可以：

- 使用 UI 从先前 node 中选择值
- 编写[表达式](expressions-versus-data-nodes.md)动态访问和组合数据
- 按名称引用特定 node 以获取其输出

**转换数据**：n8n 提供多种修改数据的方式：

- 使用专用 transformation nodes（Aggregate、Split Out、Sort 等）
- 直接在 node 参数中编写[表达式](transform-data/expressions-for-data-transformation.md)
- 使用 [Code node](expressions-versus-data-nodes.md#code-node) 编写自定义 JavaScript 或 Python 逻辑
- 使用 [AI Transform node](expressions-versus-data-nodes.md#ai-transform-node) 进行 AI 辅助转换

**理解数据结构**：n8n 在所有 node 中使用[一致的数据结构](understand-n8ns-data-structure.md)，因此数据如何在工作流中流动和转换是可预测的。

## 本节内容 <a href="#in-this-section" id="in-this-section"></a>

* [n8n 如何组织数据](understand-n8ns-data-structure.md)
* [转换数据](transform-data/approaches-for-transforming-data.md)
* [使用代码处理数据](expressions-versus-data-nodes.md#code-node)
* 在工作流开发期间[固定、模拟和编辑数据](pin-and-mock-data.md)
* [引用数据](reference-data/README.md)和 [item linking](reference-data/link-data-items/README.md)：data item 如何相互关联

---
contentType: explanation
nodeTitle: Approaches for transforming data
originalFilePath: data/transforming-data.md
originalUrl: 'https://docs.n8n.io/data/transforming-data'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/approaches-for-transforming-data
layout:
  description:
    visible: false
---

# 转换数据的方式 <a href="#approaches-for-transforming-data" id="approaches-for-transforming-data"></a>

n8n 中的数据转换，是指数据在工作流中流动时对其进行修改、重组或增强。这包括更改数据格式、筛选或聚合值、添加计算字段，以及转换数据结构以适配不同 node。

n8n 使用预定义的[数据结构](../understand-n8ns-data-structure.md)，让所有 node 都能正确处理传入数据。当你的数据不符合此结构，或需要根据 use case 修改数据时，就需要转换数据。

n8n 提供多种数据转换方式：

* [Expressions](../expressions-versus-data-nodes.md#expressions) 允许你使用 n8n 的 expression 语法（`{{ }}`）直接在 node 参数中转换数据。
* [Code node](../expressions-versus-data-nodes.md#code-node) 允许你为复杂转换编写自定义 JavaScript 或 Python。
* [AI Transform node](../expressions-versus-data-nodes.md#ai-transform-node) 会根据自然语言 prompt 生成转换代码。
* 高级转换技巧：对于复杂数据操作，n8n 支持：
   * **三元运算符**：直接在 expression 中使用条件逻辑（`condition ? valueIfTrue : valueIfFalse`）
   * **链式函数**：组合多个转换函数
   * **复杂 expression**：在 expression 语法中使用 JavaScript 方法和运算符
* 用于常见结构转换的专用 transformation nodes：
   * [Aggregate](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.aggregate)：将独立 item 分组到一起
   * [Limit](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.limit)：限制 item 数量
   * [Remove Duplicates](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.removeduplicates)：移除相同 item
   * [Sort](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.sort)：为 item 排序或随机化
   * [Split Out](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.splitout)：将列表拆分为单独 item
   * [Summarize](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.summarize)：像 Excel 数据透视表一样聚合数据

有关这些方式的对比，请参阅 [Expressions 与 data nodes 对比](../expressions-versus-data-nodes.md)。

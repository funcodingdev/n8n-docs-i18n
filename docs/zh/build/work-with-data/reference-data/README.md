---
contentType: overview
nodeTitle: Reference data
originalFilePath: data/data-mapping/index.md
originalUrl: 'https://docs.n8n.io/data/data-mapping'
url: 'https://docs.n8n.io/build/work-with-data/reference-data'
layout:
  description:
    visible: false
---

# 引用数据 <a href="#referencing-data" id="referencing-data"></a>

引用数据，也称 data mapping，指访问工作流中前序 node 的信息。这允许你将早期步骤的输出用作后续 node 的输入，从而创建能在多个操作间传递数据的动态工作流。

引用数据时，你不会更改数据。你只是指向已经存在的值，以便在 node 参数、expression 或自定义代码中使用它们。

如果你想更改正在引用的数据，请参阅[转换数据](../transform-data/approaches-for-transforming-data.md)。

## 如何引用数据 <a href="#how-to-reference-data" id="how-to-reference-data"></a>

引用数据的主要方式是使用 [expressions](../expressions-versus-data-nodes.md#expressions)。你可以在参数字段中输入 expression，也可以在 UI 中从 Input 面板拖放字段来创建 expression。Expression 会通过 [item linking](link-data-items/README.md) 自动确定要使用的正确 item。

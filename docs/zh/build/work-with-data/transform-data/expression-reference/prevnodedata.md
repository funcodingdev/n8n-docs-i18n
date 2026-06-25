---
nodeTitle: Prevnodedata
originalFilePath: data/expression-reference/prevnodedata.md
originalUrl: 'https://docs.n8n.io/data/expression-reference/prevnodedata'
url: >-
  https://docs.n8n.io/build/work-with-data/transform-data/expression-reference/prevnodedata
layout:
  description:
    visible: false
---
# PrevNodeData <a href="#prevnodedata" id="prevnodedata"></a>

## **`name`** <a href="#name" id="name"></a>

**描述：** 当前输入来源 node 的名称。

如果当前 node 有多个输入 connector，则始终使用第一个输入 connector（例如在 ‘Merge’ node 中）。

**语法：** **`name`**

**返回：** String

**来源：** 自定义 n8n 功能

## **`outputIndex`** <a href="#outputindex" id="outputindex"></a>

**描述：** 当前输入来源输出 connector 的索引。当前序 node 有多个输出时使用它（例如 ‘If’ 或 ‘Switch’ node）。

如果当前 node 有多个输入 connector，则始终使用第一个输入 connector（例如在 ‘Merge’ node 中）。

**语法：** **`outputIndex`**

**返回：** Number

**来源：** 自定义 n8n 功能

## **`runIndex`** <a href="#runindex" id="runindex"></a>

**描述：** 生成当前输入的前序 node 运行次数。

如果当前 node 有多个输入 connector，则始终使用第一个输入 connector（例如在 ‘Merge’ node 中）。

**语法：** **`runIndex`**

**返回：** Number

**来源：** 自定义 n8n 功能

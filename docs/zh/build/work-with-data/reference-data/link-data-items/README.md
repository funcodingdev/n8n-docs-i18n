---
contentType: overview
nodeTitle: Link data items
originalFilePath: data/data-mapping/data-item-linking/index.md
originalUrl: 'https://docs.n8n.io/data/data-mapping/data-item-linking'
url: 'https://docs.n8n.io/build/work-with-data/reference-data/link-data-items'
layout:
  description:
    visible: false
---

# 链接 data item <a href="#linking-data-items" id="linking-data-items"></a>

Item 是一条单独的数据。Node 接收一个或多个 item，对它们执行操作，并输出新的 item。每个 item 都会链接回生成它的前序 node 中的 item。

通常这会自动工作。如果你处于以下情况，则需要详细理解此行为：

* 使用 Code node 处理输入和输出数据的复杂行为。
* 构建偏编程式的 node。

本节提供：

* [Item linking concepts](how-items-link-through-workflows.md) 的概念概览。
* [Item linking for node creators](item-linking-for-node-creators.md) 相关信息。
* 为需要在使用 Code node 时[处理数据路径](preserving-linking-in-the-code-node.md)、从前序 node 检索 item 数据并链接 item 的最终用户提供支持。
* 排查[错误](item-linking-errors.md)的指导。

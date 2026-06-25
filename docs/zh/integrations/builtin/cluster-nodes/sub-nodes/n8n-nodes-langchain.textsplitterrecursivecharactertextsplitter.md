---
title: Recursive Character Text Splitter node 文档
description: >-
  了解如何在 n8n 中使用 Recursive Character Text Splitter node。按照技术文档将 Recursive
  Character Text Splitter node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Recursive Character Text Splitter node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter
layout:
  description:
    visible: false
---

# Recursive Character Text Splitter node <a href="#recursive-character-text-splitter-node" id="recursive-character-text-splitter-node"></a>

Recursive Character Text Splitter node 会递归拆分 document data，尽可能长时间地保持 paragraphs、sentences 和 words 在一起。

在本页中，你可以找到 Recursive Character Text Splitter node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Chunk Size**：输入每个 chunk 中的 characters 数量。
* **Chunk Overlap**：输入 chunks 之间要保留多少 overlap。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Recursive Character Text Splitter node 文档集成模板](https://n8n.io/integrations/recursive-character-text-splitter)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain text splitter 文档](https://js.langchain.com/docs/concepts/text_splitters)和 [LangChain recursively split by character 文档](https://v03.api.js.langchain.com/classes/langchain.text_splitter.RecursiveCharacterTextSplitter.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

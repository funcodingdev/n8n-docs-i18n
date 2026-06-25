---
title: Token Splitter node 文档
description: >-
  了解如何在 n8n 中使用 Token Splitter node。按照技术文档将 Token Splitter node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Token Splitter node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.textsplittertokensplitter
layout:
  description:
    visible: false
---

# Token Splitter node <a href="#token-splitter-node" id="token-splitter-node"></a>

Token Splitter node 会先将 raw text string 转换为 BPE tokens，再将这些 tokens 拆分为 chunks，并把单个 chunk 中的 tokens 转回 text。

在本页中，你可以找到 Token Splitter node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Chunk Size**：输入每个 chunk 中的 characters 数量。
* **Chunk Overlap**：输入 chunks 之间要保留多少 overlap。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Token Splitter node 文档集成模板](https://n8n.io/integrations/token-splitter)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain token 文档](https://js.langchain.com/docs/concepts/tokens/)和 [LangChain text splitter 文档](https://js.langchain.com/docs/concepts/text_splitters/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

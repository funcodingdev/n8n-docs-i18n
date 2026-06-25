---
title: Summarization Chain node 文档
description: >-
  了解如何在 n8n 中使用 Summarize Chain node。按照技术文档将 Summarize Chain
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Summarization Chain node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization
layout:
  description:
    visible: false
---

# Summarization Chain node <a href="#summarization-chain-node" id="summarization-chain-node"></a>

使用 Summarization Chain node 汇总多个文档。

在本页中，你可以找到 Summarization Chain node 的 node 参数，以及更多相关资源链接。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

在 **Data to Summarize** 中选择需要汇总的数据类型。你选择的数据类型会决定其他 node 参数。

* **Use Node Input (JSON)** 和 **Use Node Input (Binary)**：汇总 workflow 中传入 node 的数据。
	* 你可以配置 **Chunking Strategy**：选择用于定义数据 chunk 大小的策略。
		* 如果选择 **Simple (Define Below)**，则可以设置 **Characters Per Chunk** 和 **Chunk Overlap (Characters)**。
		* 如果想连接提供更多配置选项的 splitter sub-node，请选择 **Advanced**。
* **Use Document Loader**：汇总由 document loader sub-node 提供的数据。

## Node 选项 <a href="#node-options" id="node-options"></a>

你可以配置汇总方法和 prompts。选择 **Add Option** > **Summarization Method and Prompts**。

**Summarization Method** 中的选项：

* **Map Reduce**：这是推荐选项。请在 LangChain 文档中了解更多关于 [Map Reduce](https://js.langchain.com/v0.1/docs/modules/chains/document/map_reduce/) 的信息。
* **Refine**：请在 LangChain 文档中了解更多关于 [Refine](https://js.langchain.com/v0.1/docs/modules/chains/document/refine/) 的信息。
* **Stuff**：请在 LangChain 文档中了解更多关于 [Stuff](https://js.langchain.com/v0.1/docs/modules/chains/document/stuff/) 的信息。

你可以自定义 **Individual Summary Prompts** 和 **Final Prompt to Combine**。node 中提供了示例。你必须包含 `"{text}"` 占位符。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Summarization Chain node 文档集成模板](https://n8n.io/integrations/summarization-chain)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 关于 summarization 的文档](https://js.langchain.com/docs/tutorials/summarization/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

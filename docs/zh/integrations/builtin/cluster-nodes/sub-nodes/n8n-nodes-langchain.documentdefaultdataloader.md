---
title: Default Data Loader node 文档
description: >-
  了解如何在 n8n 中使用 Default Data Loader node。按照技术文档将 Default Data
  Loader node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Default Data Loader node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader
layout:
  description:
    visible: false
---

# Default Data Loader node <a href="#default-data-loader-node" id="default-data-loader-node"></a>

使用 Default Data Loader node 加载 binary data files 或 JSON data，用于 [vector stores](#user-content-fn-1)[^1] 或 summarization。

在本页中，你可以找到 Default Data Loader node 支持的参数列表，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text Splitting**：选择：
	* **Simple**：使用 [Recursive Character Text Splitter](n8n-nodes-langchain.textsplitterrecursivecharactertextsplitter.md)，chunk size 为 1000，overlap 为 200。
	* **Custom**：允许你连接所选的 text splitter。
* **Type of Data**：选择 **Binary** 或 **JSON**。
* **Mode**：选择：
	* **Load All Input Data**：使用该 node 的所有 input data。
	* **Load Specific Data**：使用 [expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 定义要加载的数据。你可以添加文本，也可以添加 expressions。这意味着你可以用文本和 expressions 的组合创建自定义 document。
* **Data Format**：当你将 **Type of Data** 设置为 **Binary** 时显示。选择 binary data 的文件 MIME type。如果希望 n8n 自动设置 data format，请设为 **Automatically Detect by MIME Type**。如果你设置了特定 data format，而传入文件的 MIME type 不匹配，node 会报错。如果使用 **Automatically Detect by MIME Type**，但 node 无法将文件 MIME type 匹配到支持的 data format，则会回退到 text format。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Metadata**：设置 document 在 vector store 中应附带的 metadata。使用 vector store nodes 检索数据时，这就是通过 **Metadata Filter** 选项匹配的内容。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Default Data Loader node 文档集成模板](https://n8n.io/integrations/default-data-loader)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7MPhMVJM8wcmiOf5zn2m/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。

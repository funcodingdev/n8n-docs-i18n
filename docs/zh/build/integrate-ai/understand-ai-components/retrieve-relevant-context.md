---
title: n8n 中的 RAG
description: >-
  使用检索增强生成 (RAG)，你可以让模型访问特定上下文资源，帮助生成相关回答。了解它的工作方式以及如何在 n8n 中使用 RAG。
contentType: overview
nodeTitle: 检索相关上下文
originalFilePath: advanced-ai/rag-in-n8n.md
originalUrl: 'https://docs.n8n.io/advanced-ai/rag-in-n8n'
url: >-
  https://docs.n8n.io/build/integrate-ai/understand-ai-components/retrieve-relevant-context
layout:
  description:
    visible: false
---




# n8n 中的 RAG <a href="#rag-in-n8n" id="rag-in-n8n"></a>

## 什么是 RAG <a href="#what-is-rag" id="what-is-rag"></a>

[检索增强生成 (RAG)](#user-content-fn-1)[^1] 是一种通过将语言模型与外部数据源结合来改进 AI 回答的技术。RAG 系统不会只依赖模型内部训练数据，而是检索相关文档，让回答基于[^2]最新、特定领域或专有知识。RAG 工作流通常依赖 vector store 来高效管理和搜索这些外部数据。

## 什么是 vector store？ <a href="#what-is-a-vector-store" id="what-is-a-vector-store"></a>

[Vector store](#user-content-fn-3)[^3] 是一种专门用于存储和搜索高维向量的数据库：这些向量是文本、图片或其他数据的数值表示。上传文档时，vector store 会将文档拆分为 chunk，并使用 [embedding model](#user-content-fn-4)[^4] 将每个 chunk 转换为向量。

你可以使用相似度搜索来查询这些向量。相似度搜索会基于*语义含义*而不是关键词匹配来构建结果。这让 vector store 成为 RAG 以及其他需要在大量知识中检索和推理的 AI 系统的强大基础。

## 如何在 n8n 中使用 RAG <a href="#how-to-use-rag-in-n8n" id="how-to-use-rag-in-n8n"></a>

{% hint style="info" %}
**从 RAG 模板开始**

👉 使用 [RAG Starter Template](https://n8n.io/workflows/5010-rag-starter-template-using-simple-vector-stores-form-trigger-and-openai) 在 n8n 中试用 RAG。该模板包含两个现成工作流：一个用于上传文件，另一个用于查询文件。
{% endhint %}

### 将数据插入 vector store <a href="#inserting-data-into-your-vector-store" id="inserting-data-into-your-vector-store"></a>

在 agent 可以访问自定义知识之前，你需要将这些数据上传到 vector store：

1. 添加获取源数据所需的节点。
2. 插入 **Vector Store** 节点（例如 [Simple Vector Store](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreinmemory)），并选择 **Insert Documents** 操作。
3. 选择 **embedding model**，它会将文本转换为 vector embedding。关于[选择合适 embedding model](#how-do-i-choose-the-right-embedding-model) 的更多信息，请查看 FAQ。
4. 添加 [Default Data Loader](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.documentdefaultdataloader) 节点，它会将内容拆分为 chunk。你可以使用默认设置，也可以定义自己的 chunking 策略：
	* **Character Text Splitter：** 按字符长度拆分。
	* **Recursive Character Text Splitter：** 按 Markdown、HTML、代码块或简单字符递归拆分（推荐用于大多数场景）。
	* **Token Text Splitter：** 按 token 数量拆分。
5. （可选）为每个 chunk 添加 **metadata**，以丰富上下文，并允许后续更好地过滤。

### 查询数据 <a href="#querying-your-data" id="querying-your-data"></a>

你可以通过两种主要方式查询数据：使用 agent，或直接通过节点查询。

### 使用 agent <a href="#using-agents" id="using-agents"></a>

1. 向工作流添加一个 [agent](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)。
2. 将 vector store 作为 **tool** 添加，并为它提供 **description**，帮助 agent 理解什么时候使用它：
	* 设置 **limit**，定义要返回多少个 chunk。
	* 启用 **Include Metadata**，为每个 chunk 提供额外上下文。
3. 添加与你插入数据时使用的同一个 **embedding model**。

{% hint style="info" %}
**专业提示**

为了节省昂贵模型的 token，你可以先使用 [Vector Store Question Answer tool](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolvectorstore) 检索相关数据，然后再将结果传递给 Agent。要查看这一做法的实际效果，请查看[此模板](https://n8n.io/workflows/5011-save-costs-in-rag-workflows-using-the-qanda-tool-with-multiple-models)。
{% endhint %}

### 直接使用节点 <a href="#using-the-node-directly" id="using-the-node-directly"></a>

1. 将 vector store 节点添加到画布，并选择 **Get Many** 操作。
2. 输入查询或提示词：
	* 设置 **limit**，指定要返回多少个 chunk。
	* 如有需要，启用 **Include Metadata**。

## FAQ <a href="#faqs" id="faqs"></a>


### 如何选择合适的 embedding model？ <a href="#how-do-i-choose-the-right-embedding-model" id="how-do-i-choose-the-right-embedding-model"></a>


合适的 embedding model 会因场景而异。

通常，较小的模型（例如 `text-embedding-ada-002`）速度更快、成本更低，因此适合短文档、通用文档或轻量级 RAG 工作流。较大的模型（例如 `text-embedding-3-large`）提供更好的语义理解能力，最适合长文档、复杂主题或准确性至关重要的场景。


### 哪种文本拆分方式最适合我的场景？ <a href="#what-is-the-best-text-splitting-for-my-use-case" id="what-is-the-best-text-splitting-for-my-use-case"></a>


这同样很大程度上取决于你的数据：

* 小 chunk（例如 200 到 500 个 token）适合细粒度检索。
* 大 chunk 可能携带更多上下文，但也可能变得稀释或引入噪声。

使用合适的 overlap 大小，对 AI 理解 chunk 上下文很重要。这也是为什么使用 Markdown 或 Code Block 拆分通常能让 chunk 质量更好的原因。

另一个好方法是为 chunk 添加更多上下文（例如说明该 chunk 来自哪个文档）。如需进一步了解，可以查看 [Anthropic 的这篇优秀文章](https://www.anthropic.com/news/contextual-retrieval)。

[^1]: 检索增强生成（Retrieval-augmented generation，RAG）是一种让 LLM 访问外部来源中新信息的技术，用于改进 AI 回答。RAG 系统会检索相关文档，让回答基于最新、特定领域或专有知识，以补充模型原始训练数据。RAG 系统通常依赖 vector store 来高效管理和搜索这些外部数据。
[^2]: 在 AI 中，特别是在检索增强生成 (RAG) 语境中，groundedness 和 ungroundedness 衡量的是模型回答准确反映源信息的程度。模型使用源文档生成 grounded response，而 ungrounded response 则包含没有这些来源支持的猜测或幻觉。
[^3]: Vector store 或 vector database 用于存储信息的数学表示。它与 embedding 和 retriever 搭配使用，创建 AI 在回答问题时可访问的数据库。
[^4]: Embedding 是使用向量表示数据的数值表示。AI 使用它们通过在许多维度上映射值来理解复杂数据和关系。Vector database 或 vector store 是专门用于存储和访问 embedding 的数据库。

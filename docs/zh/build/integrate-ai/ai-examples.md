---
contentType: overview
title: 高级 AI 示例和概念
description: 使用 n8n 构建 AI 功能的 workflow 示例和使用场景。
hide:
  - toc
nodeTitle: AI examples
originalFilePath: advanced-ai/examples/introduction.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/introduction'
url: 'https://docs.n8n.io/build/integrate-ai/ai-examples'
layout:
  description:
    visible: false
---

# 高级 AI 示例和概念 <a href="#advanced-ai-examples-and-concepts" id="advanced-ai-examples-and-concepts"></a>

本节解释重要的 AI 概念，并提供突出这些概念的 workflow template，同时包含说明和配置指南。这些示例覆盖常见使用场景，并展示 n8n 中高级 AI 的不同功能。

<div class="grid cards" markdown>

-   __Agent 和 chain__

	了解 AI 中的 agent[^1] 和 chain[^2]，并通过示例 workflow 探索关键差异。

	[→ AI 中的 chain 是什么？](understand-ai-components/what-chains-do.md)
    [→ AI 中的 agent 是什么？](understand-ai-components/what-agents-do.md)
	[→ 演示 agent 和 chain 的关键差异](understand-ai-components/agents-vs-chains.md)

-   __调用 n8n Workflow Tool__

    了解 AI 中的 tool[^3]，然后探索使用 n8n workflow 作为自定义 tool 的示例，为你的 AI workflow 提供更多数据访问能力。

	[→ AI 中的 tool 是什么？](understand-ai-components/how-tools-work.md)
    [→ 与 Google Sheets 对话](ai-examples/use-google-sheets-as-a-data-source.md)
	[→ 调用 API 获取数据](ai-examples/call-apis.md)
	[→ 设置人工 fallback](ai-examples/set-a-human-fallback-for-ai-workflows.md)
	[→ 让 AI 使用 `$fromAI()` 指定 tool 参数](ai-examples/use-ai-for-parameters.md)

-   __Vector database__

    了解 AI 中的 [vector database](#user-content-fn-4)[^4]，以及 embedding[^5] 和 retriever 等相关概念。

	[→ 什么是 vector database？](understand-ai-components/store-and-search-data-with-vectors.md)
    [→ 从网站填充 Pinecone vector database](ai-examples/use-website-content.md)

-   __Memory__

    了解 AI 中的 memory[^6]。

	[→ AI 中的 memory 是什么？](understand-ai-components/how-memory-works.md)

-   __AI workflow template__

	你可以在 n8n 网站上浏览 AI template，包括社区贡献内容。

    [→ 浏览所有 AI template](https://n8n.io/workflows/?categories=25)



</div>

[^1]: AI agent 是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）解释用户输入，并根据可用信息和资源决定如何最好地处理请求。
[^2]: AI chain 允许你按顺序调用组件，与大语言模型（LLM）和其他资源交互。n8n 中的 AI chain 不使用持久 memory，因此不能用它们引用之前的上下文（这种场景请使用 AI agent）。
[^3]: 在 AI 上下文中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成具体、聚焦的任务。
[^4]: Vector store 或 vector database 会存储信息的数学表示。将其与 embedding 和 retriever 配合使用，可以创建 AI 在回答问题时可访问的数据库。
[^5]: Embedding 是使用 vector 表示数据的数值形式。AI 通过在多个维度上映射值来解释复杂数据和关系。Vector database 或 vector store 是专为存储和访问 embedding 设计的数据库。
[^6]: 在 AI 上下文中，memory 允许 AI tool 在交互之间持久保留消息上下文。例如，这让你可以与 AI agent 进行连续对话，而不需要每条消息都提交持续上下文。在 n8n 中，AI agent node 可以使用 memory，但 AI chain 不能。

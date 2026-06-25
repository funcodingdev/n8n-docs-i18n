---
title: AI 中的 chain 是什么？
description: 理解 AI 上下文中的 chain。了解 n8n 中的 chain。
contentType: explanation
nodeTitle: What chains do
originalFilePath: advanced-ai/examples/understand-chains.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/understand-chains'
url: 'https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-chains-do'
layout:
  description:
    visible: false
---

# AI 中的 chain 是什么？ <a href="#whats-a-chain-in-ai" id="whats-a-chain-in-ai"></a>

Chain[^1] 将不同 AI 组件组合起来，创建一个连贯系统。它们会在组件之间建立一系列调用。这些组件可以包括 model 和 memory[^2]（但请注意，在 n8n 中 chain 不能使用 memory）。


## n8n 中的 chain <a href="#chains-in-n8n" id="chains-in-n8n"></a>

n8n 提供三个 chain node：

* [Basic LLM Chain](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm)：用于与 LLM 交互，不包含任何额外组件。
* [Question and Answer Chain](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa)：可以使用 retriever 连接到 [vector store](#user-content-fn-3)[^3]，也可以使用 Workflow Retriever node 连接到 n8n workflow。如果你想创建支持针对特定文档提问的 workflow，请使用它。
* [Summarization Chain](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainsummarization)：接收输入并返回摘要。

n8n 中的 chain 与 LangChain 等其他工具中的 chain 有一个重要区别：所有 chain node 都不支持 memory。这意味着它们不能记住之前的用户 query。如果你用 LangChain 编写 AI 应用，可以为应用提供 memory。在 n8n 中，如果你需要 workflow 支持 memory，请使用 agent。如果你希望用户能够与你的 app 进行自然、持续的对话，这一点很关键。

[^1]: AI chain 允许你按顺序调用组件，与大语言模型（LLM）和其他资源交互。n8n 中的 AI chain 不使用持久 memory，因此不能用它们引用之前的上下文（这种场景请使用 AI agent）。
[^2]: 在 AI 上下文中，memory 允许 AI tool 在交互之间持久保留消息上下文。例如，这让你可以与 AI agent 进行连续对话，而不需要每条消息都提交持续上下文。在 n8n 中，AI agent node 可以使用 memory，但 AI chain 不能。
[^3]: Vector store 或 vector database 会存储信息的数学表示。将其与 embedding 和 retriever 配合使用，可以创建 AI 在回答问题时可访问的数据库。

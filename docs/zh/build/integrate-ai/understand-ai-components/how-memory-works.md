---
title: AI 中的 memory 是什么？
description: >-
  理解 AI 上下文中的 memory。了解 n8n 中 memory 的特别之处。
contentType: explanation
nodeTitle: How memory works
originalFilePath: advanced-ai/examples/understand-memory.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/understand-memory'
url: >-
  https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-memory-works
layout:
  description:
    visible: false
---

# AI 中的 memory 是什么？ <a href="#whats-memory-in-ai" id="whats-memory-in-ai"></a>

Memory 是 AI chat service 的关键部分。Memory[^1] 会保留之前消息的历史，让你能够与 AI 持续对话，而不是每次交互都从头开始。

## n8n 中的 AI memory <a href="#ai-memory-in-n8n" id="ai-memory-in-n8n"></a>

要向 AI workflow 添加 memory，你可以使用：

* [Simple Memory](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)：为当前 session 存储可自定义长度的 chat history。这是最容易上手的方式。
* n8n 提供 node 支持的某个 memory service。这些包括：
	* [Motorhead](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymotorhead)
	* [Redis Chat Memory](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryredischat)
	* [Postgres Chat Memory](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorypostgreschat)
	* [Xata](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryxata)
	* [Zep](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep)

如果你需要在 workflow 中执行高级 AI memory 管理，请使用 [Chat Memory Manager](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager) node。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ipTfg43EHN14P930L6JP/" %}

[^1]: 在 AI 上下文中，memory 允许 AI tool 在交互之间持久保留消息上下文。例如，这让你可以与 AI agent 进行连续对话，而不需要每条消息都提交持续上下文。在 n8n 中，AI agent node 可以使用 memory，但 AI chain 不能。

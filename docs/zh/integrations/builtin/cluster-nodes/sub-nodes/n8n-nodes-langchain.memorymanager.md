---
title: Chat Memory Manager node 文档
description: >-
  了解如何在 n8n 中使用 Chat Memory Manager node。按照技术文档将 Chat Memory
  Manager node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Chat Memory Manager node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorymanager
layout:
  description:
    visible: false
---

# Chat Memory Manager node <a href="#chat-memory-manager-node" id="chat-memory-manager-node"></a>

Chat Memory Manager node 用于管理 workflows 中的 chat message memories[^1]。使用此 node 在 in-memory [vector store](#user-content-fn-2)[^2] 中加载、插入和删除 chat messages。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ipTfg43EHN14P930L6JP/" %}

在本页中，你可以找到 Chat Memory Manager node 支持的 operations 列表，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Operation Mode**：在 **Get Many Messages**、**Insert Messages** 和 **Delete Messages** operations 之间选择。
* **Insert Mode**：在 **Insert Messages** mode 中可用。可选择：
    * **Insert Messages**：在现有 messages 旁插入 messages。
    * **Override All Messages**：替换当前 memory。
* **Delete Mode**：在 **Delete Messages** mode 中可用。可选择：
    * **Last N**：删除最后 N 条 messages。
    * **All Messages**：从 memory 中删除 messages。
* **Chat Messages**：在 **Insert Messages** mode 中可用。定义要插入 memory 的 chat messages，包括：
	* **Type Name or ID**：设置 message type。选择以下之一：
		* **AI**：用于来自 AI 的 messages。
		* **System**：添加一条包含 AI instructions 的 message。
		* **User**：用于来自 user 的 messages。此 message type 在其他 AI tools 和 guides 中有时称为 'human' message。
	* **Message**：输入 message contents。
	* **Hide Message in Chat**：选择 n8n 是否应在 chat UI 中向 user 显示该 message（关闭）或不显示（开启）。
* **Messages Count**：当你选择 **Last N** 时，在 **Delete Messages** mode 中可用。输入要删除的最新 messages 数量。
* **Simplify Output**：在 **Get Many Messages** mode 中可用。开启后会简化 output，只包含 sender（AI、user 或 system）和 text。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Chat Memory Manager node 文档集成模板](https://n8n.io/integrations/chat-memory-manager)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain Memory 文档](https://langchain-ai.github.io/langgraphjs/concepts/memory/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: 在 AI 语境中，memory 允许 AI tools 在 interactions 之间持久化 message context。例如，这允许你与 AI agents 进行持续对话，而无需在每条 message 中提交 ongoing context。在 n8n 中，AI agent nodes 可以使用 memory，但 AI chains 不能。
[^2]: Vector store，也称 vector database，用于存储信息的数学表示。将它与 embeddings 和 retrievers 一起使用，可以创建一个 AI 回答问题时能够访问的 database。

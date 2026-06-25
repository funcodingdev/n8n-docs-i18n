---
title: AI Agent Tool node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent Tool node。按照技术文档将 AI Agent Tool node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: AI Agent Tool node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent
layout:
  description:
    visible: false
---

# AI Agent Tool node <a href="#ai-agent-tool-node" id="ai-agent-tool-node"></a>

AI Agent Tool node 允许 workflow 中 root-level agent[^1] 将其他 agents 作为 tools 调用，从而简化 multi-agent orchestration。

[primary agent](../root-nodes/n8n-nodes-langchain.agent/tools-agent.md) 可以监督并将工作委派给专注于不同 tasks 和 knowledge 的 AI Agent Tool nodes。这允许你在单个 workflow 中使用多个 agents，而无需处理 sub-workflows 所需的 context 和 variables 管理复杂性。你可以将 AI Agent Tool nodes 嵌套成多层，以支持更复杂的 multi-tiered use cases。

在本页中，你可以找到 AI Agent Tool node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 AI Agent Tool node：

* **Description**：向 LLM 描述此 agent 的目的和职责范围。清晰具体的 description 会告诉 parent agent 何时将 tasks 委派给此 agent 处理。
* **Prompt (User Message)**：给 LLM 的 prompt，用于说明要执行哪些 actions，以及要返回哪些 information。
* **Require Specific Output Format**：是否要求 node 使用特定 output format。开启后，n8n 会提示你连接 [main agent page](../root-nodes/n8n-nodes-langchain.agent/tools-agent.md#require-specific-output-format) 中描述的 output parsers 之一。
* **Enable Fallback Model**：是否启用 fallback model。启用后，n8n 会提示你连接 backup chat model，以便在 primary model 失败或不可用时使用。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 AI Agent Tool node 的行为：

* **System Message**：conversation 开始前发送给 agent 的 message。
* **Max Iterations**：model 在停止前为生成 response 可运行的最大次数。
* **Return Intermediate Steps**：是否在最终 output 中包含 agent 执行过的 intermediate steps。
* **Automatically Passthrough Binary Images**：是否应自动将 binary images 作为 image type messages 传递给 agent。
* **Batch Processing**：是否启用以下 batch processing options 来进行 rate limiting：
	* **Batch Size**：并行处理的 items 数量。这有助于 rate limiting，但可能影响 log output ordering。
	* **Delay Between Batches**：batches 之间等待的毫秒数。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AI Agent Tool node 文档集成模板](https://n8n.io/integrations/ai-agent-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 使用 `$fromAI()` 的 tool 动态参数 <a href="#dynamic-parameters-for-tools-with-dollarfromai" id="dynamic-parameters-for-tools-with-dollarfromai"></a>

要了解如何为 app node tools 动态填充参数，请参阅[让 AI 使用 `$fromAI()` 指定 tool 参数](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/ai-examples/use-ai-for-parameters)。

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

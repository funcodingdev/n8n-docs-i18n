---
title: AI 中的 agent 是什么？
description: 理解 AI 上下文中的 agent。了解 n8n 如何提供 agent。
contentType: explanation
nodeTitle: What agents do
originalFilePath: advanced-ai/examples/understand-agents.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/understand-agents'
url: 'https://docs.n8n.io/build/integrate-ai/understand-ai-components/what-agents-do'
layout:
  description:
    visible: false
---

# AI 中的 agent 是什么？ <a href="#whats-an-agent-in-ai" id="whats-an-agent-in-ai"></a>

可以把 agent[^1] 理解为一个知道如何做决策的 [chain](what-chains-do.md)。chain 会按预先确定的顺序调用不同 AI 组件，而 agent 会使用 language model 决定要采取哪些 action。

Agent 是 AI 中承担决策者角色的部分。它们可以与其他 agent 和 tool[^2] 交互。当你向 agent 发送 query 时，它会尝试选择最合适的 tool 来回答。Agent 会适应你的具体 query，也会受配置其行为的 prompt 影响。

## n8n 中的 agent <a href="#agents-in-n8n" id="agents-in-n8n"></a>

n8n 提供一个 Agent node，它可以根据你选择的设置作为不同类型的 agent 工作。可用 agent 类型的详细信息请参阅 [Agent node documentation](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)。

当你执行包含 agent 的 workflow 时，agent 会运行多次。例如，它可能先进行初始设置，然后运行一次以调用 tool，再运行一次以评估 tool response 并回复用户。

[^1]: AI agent 是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）解释用户输入，并根据可用信息和资源决定如何最好地处理请求。
[^2]: 在 AI 上下文中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成具体、聚焦的任务。

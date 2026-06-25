---
title: AI 中的 tool 是什么？
description: >-
  理解 AI 上下文中的 tool。了解 n8n 中 tool 的特别之处。
contentType: explanation
nodeTitle: How tools work
originalFilePath: advanced-ai/examples/understand-tools.md
originalUrl: 'https://docs.n8n.io/advanced-ai/examples/understand-tools'
url: 'https://docs.n8n.io/build/integrate-ai/understand-ai-components/how-tools-work'
layout:
  description:
    visible: false
---

# AI 中的 tool 是什么？ <a href="#whats-a-tool-in-ai" id="whats-a-tool-in-ai"></a>

在 AI 中，"tool" 有特定含义。Tool 类似附加组件，AI 可以使用它访问额外上下文或资源。

还有几种表达方式：

> Tool 是 agent 可用于与世界交互的接口（[来源](https://langchain-ai.github.io/langgraphjs/how-tos/tool-calling/)）



> 可以把这些 tool 理解为你的 AI model 能够调用的函数（[来源](https://www.udemy.com/course/chatgpt-and-langchain-the-complete-developers-masterclass/)）

## n8n 中的 AI tool <a href="#ai-tools-in-n8n" id="ai-tools-in-n8n"></a>

n8n 提供可连接到 [AI agent](#user-content-fn-2)[^2] 的 tool sub-node[^1]。除了提供 [Wikipedia](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwikipedia) 和 [SerpAPI](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolserpapi) 等常用 tool，n8n 还提供三个特别强大的 tool：

* [Call n8n Workflow Tool](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow)：用它将任意 n8n workflow 加载为 tool。
* [Custom Code Tool](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode)：编写 agent 可运行的代码。
* [HTTP Request Tool](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolhttprequest.md)：发起调用以获取网站或 API 数据。

接下来的三个示例重点展示 Call n8n Workflow Tool：

- [与 Google Sheets 对话](../ai-examples/use-google-sheets-as-a-data-source.md)
- [调用 API 获取数据](../ai-examples/call-apis.md)
- [设置人工 fallback](../ai-examples/set-a-human-fallback-for-ai-workflows.md)

你还可以了解如何[使用 `$fromAI()` 函数让 AI 动态指定 tool 参数](../ai-examples/use-ai-for-parameters.md)。

[^1]: n8n cluster node 由一个或多个连接到 root node 的 sub-node 组成。Sub-node 会扩展 root node 的功能，提供对特定 service 或 resource 的访问，或提供特定类型的专用处理，例如 calculator 功能。
[^2]: AI agent 是能够响应请求、做出决策并为用户执行现实任务的人工智能系统。它们使用大语言模型（LLM）解释用户输入，并根据可用信息和资源决定如何最好地处理请求。

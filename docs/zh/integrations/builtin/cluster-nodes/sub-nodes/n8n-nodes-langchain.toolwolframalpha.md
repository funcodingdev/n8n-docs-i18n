---
title: Wolfram|Alpha tool node 文档
description: >-
  了解如何在 n8n 中使用 Wolfram|Alpha tool node。按照技术文档将 Wolfram|Alpha
  tool node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Wolfram|Alpha tool node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolwolframalpha
layout:
  description:
    visible: false
---

# Wolfram|Alpha tool node <a href="#wolframoralpha-tool-node" id="wolframoralpha-tool-node"></a>

使用 Wolfram|Alpha tool node 将你的 agents[^1] 和 chains[^2] 连接到 Wolfram|Alpha computational intelligence engine。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/wolframalpha.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Wolfram|Alpha tool node 文档集成模板](https://n8n.io/integrations/wolframoralpha)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Wolfram|Alpha 文档](https://products.wolframalpha.com/api)。你还可以查看 [LangChain 关于 WolframAlpha Tool 的文档](https://js.langchain.com/docs/integrations/tools/wolframalpha/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。
[^2]: AI chains 允许你通过对 components 的一系列调用与 large language models（LLMs）和其他 resources 交互。n8n 中的 AI chains 不使用 persistent memory，因此不能用它们引用 previous context（请使用 AI agents 实现此目的）。

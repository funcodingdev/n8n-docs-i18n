---
title: Anthropic Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Anthropic Chat Model node。按照技术文档将 Anthropic Chat
  Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Anthropic Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatanthropic
layout:
  description:
    visible: false
---

# Anthropic Chat Model node <a href="#anthropic-chat-model-node" id="anthropic-chat-model-node"></a>

使用 Anthropic Chat Model node 将 Anthropic 的 Claude 系列 chat models 与 conversational agents[^1] 配合使用。

在本页中，你可以找到 Anthropic Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/anthropic.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择生成 completion 的 model。可选择：
	* **Claude**
	* **Claude Instant**

在 [Anthropic model 文档](https://docs.anthropic.com/claude/reference/selecting-a-model)中了解更多。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Anthropic Chat Model node 文档集成模板](https://n8n.io/integrations/anthropic-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Anthropic 文档](https://js.langchain.com/docs/integrations/chat/anthropic/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

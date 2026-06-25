---
title: Ollama Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Ollama Chat Model node。按照技术文档将 Ollama Chat Model
  node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-langchain.lmchatollama
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama
layout:
  description:
    visible: false
---

# Ollama Chat Model node <a href="#ollama-chat-model-node" id="ollama-chat-model-node"></a>

Ollama Chat Model node 允许你将本地 Llama 2 models 与 conversational agents[^1] 配合使用。

在本页中，你可以找到 Ollama Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../../credentials/ollama.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择生成 completion 的 model。可选择：
	* **Llama2**
	* **Llama2 13B**
	* **Llama2 70B**
	* **Llama2 Uncensored**

有关可用 models 的更多信息，请参阅 Ollama [Models Library 文档](https://ollama.com/library)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.lmchatollama 集成模板](https://n8n.io/integrations/ollama-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Ollama Chat Model 文档](https://js.langchain.com/docs/integrations/chat/ollama/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或故障以及建议解决方案，请参阅[常见问题](common-issues.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/dN5Se1JVH7wYGtmN4n0v/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

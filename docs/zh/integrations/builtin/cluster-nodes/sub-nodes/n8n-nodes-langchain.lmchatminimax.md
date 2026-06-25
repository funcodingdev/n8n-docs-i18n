---
title: MiniMax Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 MiniMax Chat Model node。按照技术文档将 MiniMax Chat
  Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: MiniMax Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatminimax
layout:
  description:
    visible: false
---

# MiniMax Chat Model node <a href="#minimax-chat-model-node" id="minimax-chat-model-node"></a>

使用 MiniMax Chat Model node 将 MiniMax 的 chat models 与 conversational agents[^1] 配合使用。

在本页中，你可以找到 MiniMax Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/minimax.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择生成 completion 的 model。可用 models 请参阅 [MiniMax model 文档](https://platform.minimax.io/docs/guides/models-intro)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Hide Thinking**：开启时（默认），node 会从 model response 中剥离 `<think>` tags。关闭此项可在 output 中包含 model 的 reasoning。
* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Timeout**：输入最大 request time，单位为毫秒。
* **Max Retries**：输入 retry request 的最大次数。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MiniMax Chat Model node 文档集成模板](https://n8n.io/integrations/minimax-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [MiniMax 文档](https://platform.minimax.io/docs/guides/models-intro)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

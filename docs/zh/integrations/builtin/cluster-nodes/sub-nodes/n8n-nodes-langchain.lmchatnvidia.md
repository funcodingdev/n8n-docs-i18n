---
title: NVIDIA Nemotron Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 NVIDIA Nemotron Chat Model node。按照技术文档将 NVIDIA
  Nemotron Chat Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: NVIDIA Nemotron Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatnvidia
layout:
  description:
    visible: false
---

# NVIDIA Nemotron Chat Model node <a href="#nvidia-nemotron-chat-model-node" id="nvidia-nemotron-chat-model-node"></a>

使用 NVIDIA Nemotron Chat Model node 将 [NVIDIA Nemotron](https://build.nvidia.com/models) models 与 conversational agents[^1] 配合使用。此 node 可与托管在 [build.nvidia.com](https://build.nvidia.com/) 上的 Nemotron models 配合使用，也可与 self-hosted NVIDIA Inference Microservices（NIM）配合使用。

在本页中，你可以找到 NVIDIA Nemotron Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/nvidia.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Model <a href="#model" id="model"></a>

选择用于生成 completion 的 Nemotron model。

n8n 会从你的 credential 中配置的 endpoint 动态加载 Nemotron models。如果 n8n 无法访问 endpoint，它会回退到一组精选的常见 Nemotron model IDs。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项进一步调整 node 的行为。

### Frequency Penalty <a href="#frequency-penalty" id="frequency-penalty"></a>

使用此选项控制 model 重复自身的概率。较高值会降低 model 重复自身的概率。

### Maximum Number of Tokens <a href="#maximum-number-of-tokens" id="maximum-number-of-tokens"></a>

输入使用的最大 tokens 数量，用于设置 completion length。使用 `-1` 表示 model 默认值。

### Response Format <a href="#response-format" id="response-format"></a>

选择 **Text** 或 **JSON**。**JSON** 可确保 model 返回有效 JSON。选择 **JSON** 时，请在 chain 或 agent 的 prompt 中包含 `json` 这个词。

### Presence Penalty <a href="#presence-penalty" id="presence-penalty"></a>

使用此选项控制 model 谈论新主题的概率。较高值会增加 model 谈论新主题的概率。

### Sampling Temperature <a href="#sampling-temperature" id="sampling-temperature"></a>

使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。

### Timeout <a href="#timeout" id="timeout"></a>

输入最大 request time，单位为毫秒。

### Max Retries <a href="#max-retries" id="max-retries"></a>

输入 retry request 的最大次数。

### Top P <a href="#top-p" id="top-p"></a>

使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 NVIDIA Nemotron Chat Model node 文档集成模板](https://n8n.io/integrations/nvidia-nemotron-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 Nemotron models 列表，请参阅 [NVIDIA build catalogue](https://build.nvidia.com/models)；有关 self-hosting 指南，请参阅 [NIM 文档](https://docs.nvidia.com/nim/)。由于 NVIDIA API 与 OpenAI-spec compatible，你可以参阅 [LangChain 的 OpenAI 文档](https://js.langchain.com/docs/integrations/chat/openai/)了解 underlying client 的更多信息。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

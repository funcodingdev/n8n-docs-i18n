---
title: OpenRouter Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 OpenRouter Chat Model node。按照技术文档将 OpenRouter Chat
  Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: OpenRouter Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter
layout:
  description:
    visible: false
---

# OpenRouter Chat Model node <a href="#openrouter-chat-model-node" id="openrouter-chat-model-node"></a>

使用 OpenRouter Chat Model node 将 OpenRouter 的 chat models 与 conversational agents 配合使用。

在本页中，你可以找到 OpenRouter Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/openrouter.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Model <a href="#model" id="model"></a>

选择用于生成 completion 的 model。

n8n 会从 OpenRouter 动态加载 models，你只会看到你的账号可用的 models。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项进一步调整 node 的行为。

### Frequency Penalty <a href="#frequency-penalty" id="frequency-penalty"></a>

使用此选项控制 model 重复自身的概率。较高值会降低 model 重复自身的概率。

### Maximum Number of Tokens <a href="#maximum-number-of-tokens" id="maximum-number-of-tokens"></a>

输入使用的最大 tokens 数量，用于设置 completion length。

### Response Format <a href="#response-format" id="response-format"></a>

选择 **Text** 或 **JSON**。**JSON** 可确保 model 返回有效 JSON。

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

[浏览 OpenRouter Chat Model node 文档集成模板](https://n8n.io/integrations/openrouter-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

由于 OpenRouter 与 OpenAI API-compatible，你可以参阅 [LangChain 的 OpenAI 文档](https://js.langchain.com/docs/integrations/chat/openai/)了解该服务的更多信息。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

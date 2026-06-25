---
title: xAI Grok Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 xAI Grok Chat Model node。按照技术文档将 xAI Grok Chat
  Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: xAI Grok Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatxaigrok
layout:
  description:
    visible: false
---

# xAI Grok Chat Model node <a href="#xai-grok-chat-model-node" id="xai-grok-chat-model-node"></a>

使用 xAI Grok Chat Model node 访问 xAI Grok 的 large language models，用于 conversational AI 和 text generation tasks。

在本页中，你可以找到 xAI Grok Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/xai.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 completion 的 model。n8n 会从 xAI Grok API 动态加载可用 models。在 [xAI Grok model 文档](https://docs.x.ai/docs/models)中了解更多。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Frequency Penalty**：使用此选项控制 model 重复自身的概率。较高值会降低 model 重复自身的概率。
* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。大多数 models 的 context length 为 2048 tokens，最新 models 支持最多 32,768 tokens。
* **Response Format**：选择 **Text** 或 **JSON**。**JSON** 可确保 model 返回有效 JSON。
* **Presence Penalty**：使用此选项控制 model 谈论新主题的概率。较高值会增加 model 谈论新主题的概率。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Timeout**：输入最大 request time，单位为毫秒。
* **Max Retries**：输入 retry request 的最大次数。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 xAI Grok Chat Model node 文档集成模板](https://n8n.io/integrations/xai-grok-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [xAI Grok API 文档](https://docs.x.ai/docs/api-reference)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

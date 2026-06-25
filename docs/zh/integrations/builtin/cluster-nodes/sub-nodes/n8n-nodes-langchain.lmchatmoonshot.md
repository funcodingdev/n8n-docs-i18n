---
title: Moonshot Kimi Chat Model node
contentType:
  - integration
  - reference
nodeTitle: Moonshot Kimi Chat Model node
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatmoonshot
description: >-
  将 Moonshot Kimi Chat Model 集成到 n8n workflows 中，为 AI chains 生成 chat
  responses。常见用途包括生成 conversational replies、与 LangChain-style workflows 集成、以及
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Moonshot Kimi Chat Model node

使用 Moonshot Kimi Chat Model node 向 Kimi chat API 发送 chat requests，并生成 conversational responses。当你需要在 workflow 中使用 AI chat model 时可使用此 node。例如，你可以驱动 assistants、构建 multi-step AI chains，或使用可调 sampling 和 token settings 生成 model-driven content。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/moonshot.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Operations <a href="#operations" id="operations"></a>

### Generate chat response <a href="#generate-chat-response" id="generate-chat-response"></a>

向所选 Kimi model 发送 chat request，并返回 model response。

**Parameters**

* **Model**（type: options，field: `model`）：生成 completion 的 model。默认值：`kimi-k2.5`。在 [Moonshot Kimi Chat API docs](https://platform.kimi.ai/docs/api/chat) 了解更多。

**Options**

* **Frequency Penalty**（type: number，field: `frequencyPenalty`）：正值会根据新 tokens 的既有频率进行惩罚，让 model 更少重复。默认值：`0`。
* **Maximum number of tokens**（type: number，field: `maxTokens`）：completion 中要生成的最大 tokens 数量。值为 -1 时使用 model 默认值。token limit 取决于所选 model。默认值：`-1`。
* **Response format**（type: options，field: `responseFormat`）：model response 的格式。默认值：`text`。
* **Presence penalty**（type: number，field: `presencePenalty`）：正值会根据新 tokens 是否已出现在当前文本中进行惩罚，提高 model 谈论新主题的可能性。默认值：`0`。
* **Sampling temperature**（type: number，field: `temperature`）：控制随机性。较低值会让 outputs 随机性更低；接近零时 model 更确定。默认值：`0.7`。
* **Timeout**（type: number，field: `timeout`）：request 可耗费的最长时间，单位为毫秒。默认值：360000（六分钟）。
* **Max retries**（type: number，field: `maxRetries`）：失败 requests 的最大 retries 次数。默认值：two。
* **Top P**（type: number，field: `topP`）：控制多样性的 nucleus sampling 参数。值为 zero point five 表示 model 会考虑一半按 likelihood 加权的 options。建议修改 **Top P** 或 **Sampling Temperature**，不要同时修改两者。默认值：`1`。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Moonshot Kimi Chat Model node 集成模板](https://n8n.io/integrations/moonshot-kimi-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务和可用 model options 的更多信息，请参阅 [Moonshot Kimi Chat Model 文档](https://platform.kimi.ai/docs/api/chat)。

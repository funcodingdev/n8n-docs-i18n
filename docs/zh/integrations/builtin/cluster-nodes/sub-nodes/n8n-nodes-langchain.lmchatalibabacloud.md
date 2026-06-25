---
title: Alibaba Cloud Chat Model node 文档
contentType:
  - integration
  - reference
nodeTitle: Alibaba Cloud Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatalibabacloud
description: >-
  Alibaba Cloud Chat Model node 会向 Alibaba Cloud 的 conversational models
  发送 prompts（用于高级 AI chains）。本页说明如何在 n8n workflows 中配置此 node，并覆盖常见用法
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

# Alibaba Cloud Chat Model

Alibaba Cloud Chat Model node 会向 Alibaba Cloud 的 conversational models 发送 chat prompts，用于高级 AI chains 和 LangChain integrations。使用它生成 conversational responses、将 model outputs 集成到 workflows 中，或使用自定义 sampling、retry 和 timeout 设置运行 prompts。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/alibaba.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Operations <a href="#operations" id="operations"></a>

### Generate chat response <a href="#generate-chat-response" id="generate-chat-response"></a>

从所选 Alibaba Cloud model 生成 chat-style response。

**Parameters**

* **Model**（type: _options_，field: `model`）：生成 completion 的 model。在 Alibaba Cloud 了解更多可用 models：[Alibaba Cloud Model Studio — Models](https://www.alibabacloud.com/help/en/model-studio/getting-started/models)。

**Options**

* **Frequency Penalty**（type: _number_，field: `frequencyPenalty`）：正值会根据新 tokens 到目前为止出现的频率进行惩罚，降低 model 逐字重复同一行的可能性。默认值：`0`。
* **Maximum Number of Tokens**（type: _number_，field: `maxTokens`）：completion 中要生成的最大 tokens 数量。限制取决于所选 model。值为 minus one 时使用 model 的默认限制。默认值：`-1`。
* **Response Format**（type: _options_，field: `responseFormat`）：node 返回的 output format，例如 plain text 或 structured formats。默认值：text。
* **Presence Penalty**（type: _number_，field: `presencePenalty`）：正值会根据新 tokens 是否已出现在当前文本中进行惩罚，提高 model 讨论新主题的可能性。默认值：`0`。
* **Sampling Temperature**（type: _number_，field: `temperature`）：控制随机性。较低值会让 output 随机性更低，接近零时更确定。默认值：`0.7`。
* **Timeout**（type: _number_，field: `timeout`）：request 被中止前允许的最长时间（毫秒）。默认值：`360000`。
* **Max Retries**（type: _number_，field: `maxRetries`）：失败 requests 的最大 retry attempts 数量。默认值：`2`。
* **Top P**（type: _number_，field: `topP`）：控制多样性的 nucleus sampling 参数。0.5 表示只考虑一半的 probability mass。调整 **Top P** 或 **Sampling Temperature**，但不要同时调整两者。默认值：`1`。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Alibaba Cloud Chat Model node 文档集成模板](https://n8n.io/integrations/alibaba-cloud-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关可用 models 及其能力的更多信息，请参阅 [Alibaba Cloud Model Studio — Models](https://www.alibabacloud.com/help/en/model-studio/getting-started/models)。

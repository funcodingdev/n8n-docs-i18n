---
title: Lemonade Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Lemonade Chat Model node。按照技术文档将 Lemonade Chat
  Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Lemonade Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatlemonade
layout:
  description:
    visible: false
---

# Lemonade Chat Model node <a href="#lemonade-chat-model-node" id="lemonade-chat-model-node"></a>

使用 Lemonade Chat Model node 在 n8n 中运行由 Lemonade server 管理、支持 chat 的 language models。此 node 作为 LangChain-compatible chat model root node，适用于 chat-style workloads。它允许你选择托管在 Lemonade server 上的 model，并使用常见 sampling 和 decoding options 控制生成行为。

在本页中，你可以找到 node 参数列表，以及用于细化生成效果的可用 options。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/lemonade.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Model <a href="#model" id="model"></a>

用于生成 completion 的 model。Models 通过 Lemonade server 加载和管理。此参数必填。选择 Lemonade server 提供的 model name，例如 `"gpt-4"` 这类 model alias，或 Lemonade 暴露的任何 custom model name。

Models 由 Lemonade server 提供；如果你没有看到预期 model，请检查 Lemonade server configuration 和 credentials。

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项进一步调整 node 的行为。

### Sampling Temperature <a href="#sampling-temperature" id="sampling-temperature"></a>

控制生成文本的随机性。较低值会让 output 更聚焦且更确定，较高值会让 output 更多样且更随机。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | 0.7 |

### Top P <a href="#top-p" id="top-p"></a>

控制 model 在生成文本时可选择哪些词。较低值会逐步移除可能性最低的 options，因此 model 只能从更小、更高置信度的候选池中选择。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | 1 |

### Frequency Penalty <a href="#frequency-penalty" id="frequency-penalty"></a>

调整对已出现在生成文本中的 tokens 的惩罚。正值会减少重复，负值会鼓励重复。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | 0 |

### Presence Penalty <a href="#presence-penalty" id="presence-penalty"></a>

根据 tokens 到目前为止是否出现在生成文本中调整惩罚。正值会惩罚已出现的 tokens，从而鼓励多样性。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | 0 |

### Max Tokens to Generate <a href="#max-tokens-to-generate" id="max-tokens-to-generate"></a>

要生成的最大 tokens 数量。设为 -1 表示不限制。设置为较大值时请谨慎，因为这可能导致很长的 outputs。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | -1 |

### Stop Sequences <a href="#stop-sequences" id="stop-sequences"></a>

以逗号分隔的 sequences 列表，model 会在这些位置停止生成文本。使用此项为 responses 定义明确的 termination strings。

| Property | Value |
|----------|-------|
| Type | string |
| Required | no |
| Default | "" |

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Lemonade Chat Model node 文档集成模板](https://n8n.io/integrations/lemonade-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Lemonade Server 文档](https://lemonade-server.ai/docs/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

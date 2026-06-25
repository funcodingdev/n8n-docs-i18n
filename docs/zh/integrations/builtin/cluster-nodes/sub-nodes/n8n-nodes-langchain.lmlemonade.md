---
title: Lemonade Model node 文档
description: >-
  了解如何在 n8n 中使用 Lemonade Model node。按照技术文档将 Lemonade Model node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Lemonade Model node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmlemonade
layout:
  description:
    visible: false
---

# Lemonade Model node <a href="#lemonade-model-node" id="lemonade-model-node"></a>

使用 Lemonade Model node 通过 Lemonade server 托管和管理的 language models 生成 text completions。此 node 是简单的 LangChain-compatible language model root node，适合 n8n workflows 中的 text completion tasks。

在本页中，你可以找到 Lemonade Model node 支持的 operations 列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/lemonade.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置此 node。

### Model <a href="#model" id="model"></a>

用于生成 completion 的 model。Models 通过 Lemonade server 加载和管理；请从 node 提供的列表中选择要使用的 model。

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

要生成的最大 tokens 数量。设为 -1 表示不限制。设置为较大值时请谨慎，因为这可能导致非常长的 outputs。

| Property | Value |
|----------|-------|
| Type | number |
| Required | no |
| Default | -1 |

### Stop Sequences <a href="#stop-sequences" id="stop-sequences"></a>

以逗号分隔的 sequences 列表，model 会在这些位置停止生成文本。

| Property | Value |
|----------|-------|
| Type | string |
| Required | no |
| Default | "" |

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Lemonade Model node 文档集成模板](https://n8n.io/integrations/lemonade-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Lemonade Server 文档](https://lemonade-server.ai/docs/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

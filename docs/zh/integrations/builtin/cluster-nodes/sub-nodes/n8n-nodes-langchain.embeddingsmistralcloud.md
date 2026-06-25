---
title: Embeddings Mistral Cloud node 文档
description: >-
  了解如何在 n8n 中使用 Embeddings Mistral Cloud node。按照技术文档将 Embeddings
  Mistral Cloud node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Embeddings Mistral Cloud node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsmistralcloud
layout:
  description:
    visible: false
---

# Embeddings Mistral Cloud node <a href="#embeddings-mistral-cloud-node" id="embeddings-mistral-cloud-node"></a>

使用 Embeddings Mistral Cloud node 为给定文本生成 embeddings[^1]。

在本页中，你可以找到 Embeddings Mistral Cloud node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/mistral.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 embedding 的 model。

在 [Mistral 的 models 文档](https://docs.mistral.ai/platform/pricing/)中了解更多可用 models。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Batch Size**：输入每个 request 中要发送的最大 documents 数量。
* **Strip New Lines**：选择是否从 input text 中移除换行字符（开启）或不移除（关闭）。n8n 默认启用此项。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Embeddings Mistral Cloud node 文档集成模板](https://n8n.io/integrations/embeddings-mistral-cloud)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Mistral embeddings 文档](https://js.langchain.com/docs/integrations/text_embedding/mistralai)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Embeddings 是使用 vectors 表示数据的数值表示。AI 使用它们通过在多个维度上映射 values 来解释复杂数据和关系。Vector databases，也称 vector stores，是为存储和访问 embeddings 而设计的 databases。

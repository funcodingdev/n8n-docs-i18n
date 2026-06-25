---
title: Embeddings OpenAI node 文档
description: >-
  了解如何在 n8n 中使用 Embeddings OpenAI node。按照技术文档将 Embeddings OpenAI
  node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Embeddings OpenAI node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsopenai
layout:
  description:
    visible: false
---

# Embeddings OpenAI node <a href="#embeddings-openai-node" id="embeddings-openai-node"></a>

使用 Embeddings OpenAI node 为给定文本生成 embeddings[^1]。

在本页中，你可以找到 Embeddings OpenAI node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/openai.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}


## Node 选项 <a href="#node-options" id="node-options"></a>

* **Model**：选择用于生成 embeddings 的 model。
* **Base URL**：输入发送 request 的 URL。如果你使用 self-hosted OpenAI-like model，请使用此项。
* **Batch Size**：输入每个 request 中要发送的最大 documents 数量。
* **Strip New Lines**：选择是否从 input text 中移除换行字符（开启）或不移除（关闭）。n8n 默认启用此项。
* **Timeout**：输入 request 可耗费的最长时间，单位为秒。设为 `-1` 表示不超时。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Embeddings OpenAI node 文档集成模板](https://n8n.io/integrations/embeddings-openai)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 OpenAI embeddings 文档](https://js.langchain.com/docs/integrations/text_embedding/openai/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Embeddings 是使用 vectors 表示数据的数值表示。AI 使用它们通过在多个维度上映射 values 来解释复杂数据和关系。Vector databases，也称 vector stores，是为存储和访问 embeddings 而设计的 databases。

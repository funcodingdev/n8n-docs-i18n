---
title: Embeddings Google PaLM node 文档
description: >-
  了解如何在 n8n 中使用 Embeddings Google PaLM node。按照技术文档将 Embeddings
  Google PaLM node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Embeddings Google PaLM node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsgooglepalm
layout:
  description:
    visible: false
---

# Embeddings Google PaLM node <a href="#embeddings-google-palm-node" id="embeddings-google-palm-node"></a>

使用 Embeddings Google PaLM node 为给定文本生成 embeddings[^1]。

在本页中，你可以找到 Embeddings Google PaLM node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/googleai.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 embedding 的 model。

n8n 会从 Google PaLM API 动态加载 models，你只会看到你的账号可用的 models。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Embeddings Google PaLM node 文档集成模板](https://n8n.io/integrations/embeddings-google-palm)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Google PaLM embeddings 文档](https://js.langchain.com/v0.2/docs/integrations/text_embedding/google_palm/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Embeddings 是使用 vectors 表示数据的数值表示。AI 使用它们通过在多个维度上映射 values 来解释复杂数据和关系。Vector databases，也称 vector stores，是为存储和访问 embeddings 而设计的 databases。

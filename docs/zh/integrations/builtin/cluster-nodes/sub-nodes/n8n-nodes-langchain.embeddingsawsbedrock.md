---
title: Embeddings AWS Bedrock node 文档
description: >-
  了解如何在 n8n 中使用 Embeddings AWS Bedrock node。按照技术文档将 Embeddings
  AWS Bedrock node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Embeddings AWS Bedrock node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsawsbedrock
layout:
  description:
    visible: false
---

# Embeddings AWS Bedrock node <a href="#embeddings-aws-bedrock-node" id="embeddings-aws-bedrock-node"></a>

使用 Embeddings AWS Bedrock node 为给定文本生成 embeddings[^1]。

在本页中，你可以找到 Embeddings AWS Bedrock node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/aws.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**：选择身份验证方法：
    * **AWS (IAM)**：使用 IAM access key。选择一个 **AWS** credential。
    * **AWS (Assume Role)**：临时 assume 一个 IAM role。选择一个 **AWS (Assume Role)** credential。
* **Model**：选择用于生成 embedding 的 model。如果下拉列表为空，你的 IAM role 可能没有 `bedrock:ListFoundationModels` 权限。将字段切换到 **Expression** 模式，并直接输入 model ID。

在 [Amazon Bedrock 文档](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)中了解更多可用 models。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Embeddings AWS Bedrock node 文档集成模板](https://n8n.io/integrations/embeddings-aws-bedrock)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 AWS Bedrock 的更多信息，请参阅 [LangChain 的 AWS Bedrock embeddings 文档](https://js.langchain.com/docs/integrations/platforms/aws/#text-embedding-models)和 [AWS Bedrock 文档](https://docs.aws.amazon.com/bedrock/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: Embeddings 是使用 vectors 表示数据的数值表示。AI 使用它们通过在多个维度上映射 values 来解释复杂数据和关系。Vector databases，也称 vector stores，是为存储和访问 embeddings 而设计的 databases。

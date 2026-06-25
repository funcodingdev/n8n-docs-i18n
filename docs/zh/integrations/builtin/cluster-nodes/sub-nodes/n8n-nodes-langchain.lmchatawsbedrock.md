---
title: AWS Bedrock Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 AWS Bedrock Chat Model node。按照技术文档将 AWS Bedrock
  Chat Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: AWS Bedrock Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatawsbedrock
layout:
  description:
    visible: false
---

# AWS Bedrock Chat Model node <a href="#aws-bedrock-chat-model-node" id="aws-bedrock-chat-model-node"></a>

AWS Bedrock Chat Model node 允许你使用 AWS Bedrock platform 上的 LLM models。

在本页中，你可以找到 AWS Bedrock Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/aws.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Authentication**：选择身份验证方法：
    * **AWS (IAM)**：使用 IAM access key。选择一个 **AWS** credential。
    * **AWS (Assume Role)**：临时 assume 一个 IAM role。选择一个 **AWS (Assume Role)** credential。
* **Model**：选择生成 completion 的 model。

在 [Amazon Bedrock model 文档](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)中了解更多可用 models。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。

## Proxy limitations <a href="#proxy-limitations" id="proxy-limitations"></a>

此 node 不支持 [`NO_PROXY` environment variable](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/deployment)。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AWS Bedrock Chat Model node 文档集成模板](https://n8n.io/integrations/aws-bedrock-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 AWS Bedrock Chat Model 文档](https://js.langchain.com/docs/integrations/chat/bedrock/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

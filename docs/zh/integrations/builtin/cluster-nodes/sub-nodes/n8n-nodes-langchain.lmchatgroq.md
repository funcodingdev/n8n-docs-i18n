---
title: Groq Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Groq Chat Model node。按照技术文档将 Groq Chat Model
  node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Groq Chat Model node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgroq
layout:
  description:
    visible: false
---

# Groq Chat Model node <a href="#groq-chat-model-node" id="groq-chat-model-node"></a>

使用 Groq Chat Model node 访问 Groq 的 large language models，用于 conversational AI 和 text generation tasks。

在本页中，你可以找到 Groq Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/groq.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 completion 的 model。n8n 会从 Groq API 动态加载可用 models。在 [Groq model 文档](https://console.groq.com/docs/models)中了解更多。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Groq Chat Model node 文档集成模板](https://n8n.io/integrations/groq-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Groq API 文档](https://console.groq.com/docs/quickstart)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

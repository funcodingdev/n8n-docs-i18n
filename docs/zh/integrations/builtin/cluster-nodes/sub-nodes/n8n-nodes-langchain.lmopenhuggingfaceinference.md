---
title: Hugging Face Inference Model node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Hugging Face Inference Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmopenhuggingfaceinference
description: >-
  了解如何在 n8n 中使用 Hugging Face Inference Model node。按照技术文档将 Hugging
  Face Inference Model node 集成到你的 workflows 中。
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

# Hugging Face Inference Model

使用 Hugging Face Inference Model node 来使用 Hugging Face 的 models。

在本页中，你可以找到 Hugging Face Inference Model node 的 node 参数，以及更多相关资源链接。

此 node 缺少 tools support，因此不能与 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/) node 配合使用。请改为将它连接到 [Basic LLM Chain](../root-nodes/n8n-nodes-langchain.chainllm.md) node。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/huggingface.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择用于生成 completion 的 model。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Custom Inference Endpoint**：输入 custom inference endpoint URL。
* **Frequency Penalty**：使用此选项控制 model 重复自身的概率。较高值会降低 model 重复自身的概率。
* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Presence Penalty**：使用此选项控制 model 谈论新主题的概率。较高值会增加 model 谈论新主题的概率。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Hugging Face Inference Model node 文档集成模板](https://n8n.io/integrations/hugging-face-inference-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Hugging Face Inference Model 文档](https://js.langchain.com/docs/integrations/llms/huggingface_inference/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

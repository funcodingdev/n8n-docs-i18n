---
title: Cohere Model node 文档
contentType:
  - integration
  - reference
nodeTitle: Cohere Model node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmcohere
description: >-
  了解如何在 n8n 中使用 Cohere Model node。按照技术文档将 Cohere Model node
  集成到你的 workflows 中。
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

# Cohere Model

使用 Cohere Model node 来使用 Cohere 的 models。

在本页中，你可以找到 Cohere Model node 的 node 参数，以及更多相关资源链接。

此 node 缺少 tools support，因此不能与 [AI Agent](../root-nodes/n8n-nodes-langchain.agent/) node 配合使用。请改为将它连接到 [Basic LLM Chain](../root-nodes/n8n-nodes-langchain.chainllm.md) node。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/cohere.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Cohere Model node 文档集成模板](https://n8n.io/integrations/cohere-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Cohere 文档](https://js.langchain.com/docs/integrations/llms/cohere/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

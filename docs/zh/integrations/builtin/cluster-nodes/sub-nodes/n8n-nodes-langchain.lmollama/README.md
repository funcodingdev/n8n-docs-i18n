---
title: Ollama Model node 文档
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-langchain.lmollama
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama
description: >-
  了解如何在 n8n 中使用 Ollama Model node。按照技术文档将 Ollama Model node
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

# Ollama Model

Ollama Model node 允许你使用本地 Llama 2 models。

在本页中，你可以找到 Ollama Model node 的 node 参数，以及更多相关资源链接。

此 node 缺少 tools support，因此不能与 [AI Agent](../../root-nodes/n8n-nodes-langchain.agent/) node 配合使用。请改为将它连接到 [Basic LLM Chain](../../root-nodes/n8n-nodes-langchain.chainllm.md) node。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../../credentials/ollama.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Model**：选择生成 completion 的 model。可选择：
  * **Llama2**
  * **Llama2 13B**
  * **Llama2 70B**
  * **Llama2 Uncensored**

有关可用 models 的更多信息，请参阅 Ollama [Models Library 文档](https://ollama.com/library)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.lmollama 集成模板](https://n8n.io/integrations/ollama-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Ollama 文档](https://js.langchain.com/docs/integrations/llms/ollama/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或故障以及建议解决方案，请参阅[常见问题](common-issues.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/dN5Se1JVH7wYGtmN4n0v/" %}

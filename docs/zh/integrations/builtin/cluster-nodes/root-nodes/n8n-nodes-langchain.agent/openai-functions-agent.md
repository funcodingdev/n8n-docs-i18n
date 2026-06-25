---
title: OpenAI Functions Agent node 文档
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Functions Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/openai-functions-agent
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 OpenAI Functions Agent。按照技术文档将
  OpenAI Functions Agent 集成到你的 workflow 中。
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

# OpenAI Functions Agent

使用 OpenAI Functions Agent node 来使用 [OpenAI functions model](https://platform.openai.com/docs/guides/function-calling)。这些 model 会检测何时应调用函数，并返回应传递给该函数的输入。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/cHtfs3gewkhPbGP31rjc/" %}

{% hint style="info" %}
**需要 OpenAI Chat Model**

你必须将 [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/) 与此 agent 一起使用。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 OpenAI Functions Agent。

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 OpenAI Functions Agent node 的行为：

### System Message <a href="#system-message" id="system-message"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ci5NMdJiVoyT9dtdTE9w/" %}

### Max Iterations <a href="#max-iterations" id="max-iterations"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/8UflrA3Nx8LD5bKQn8Xc/" %}

### Return Intermediate Steps <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/skA96E8hAnMMKG7c4Lta/" %}

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](./#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。

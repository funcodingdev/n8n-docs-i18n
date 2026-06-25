---
title: Google Vertex Chat Model node 文档
description: >-
  了解如何在 n8n 中使用 Google Vertex Chat Model node。按照技术文档将 Google Vertex
  Chat Model node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
nodeTitle: Google Vertex Chat Model node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglevertex
layout:
  description:
    visible: false
---

# Google Vertex Chat Model node <a href="#google-vertex-chat-model-node" id="google-vertex-chat-model-node"></a>

使用 Google Vertex AI Chat Model node 将 Google 的 Vertex AI chat models 与 conversational agents[^1] 配合使用。

在本页中，你可以找到 Google Vertex AI Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/google/service-account.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Project ID**：选择要使用的 Google Cloud account 中的 project ID。n8n 会从 Google Cloud account 动态加载 projects，但你也可以手动输入。
* **Model Name**：选择用于生成 completion 的 model 名称，例如 `gemini-1.5-flash-001`、`gemini-1.5-pro-001` 等。可用 models 列表请参阅 [Google models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Maximum Number of Tokens**：输入使用的最大 tokens 数量，用于设置 completion length。
* **Sampling Temperature**：使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。
* **Thinking Budget**：控制 thinking models 的 reasoning tokens。设为 `0` 可禁用 automatic thinking。设为 `-1` 表示 dynamic thinking。留空表示 auto mode。
* **Top K**：输入 model 用于生成下一个 token 的 token choices 数量。
* **Top P**：使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。
* **Safety Settings**：Gemini 支持可调整的 safety settings。有关可用 filters 和 levels 的信息，请参阅 Google 的 [Gemini API safety settings](https://ai.google.dev/docs/safety_setting_gemini)。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Google Vertex Chat Model node 文档集成模板](https://n8n.io/integrations/google-vertex-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 Google Vertex AI 文档](https://js.langchain.com/docs/integrations/chat/google_vertex_ai/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

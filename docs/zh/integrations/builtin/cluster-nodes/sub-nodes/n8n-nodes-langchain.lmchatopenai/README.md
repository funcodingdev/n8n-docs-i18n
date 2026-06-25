---
title: OpenAI Chat Model node 文档
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-langchain.lmchatopenai
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai
description: >-
  了解如何在 n8n 中使用 OpenAI Chat Model node。按照技术文档将 OpenAI Chat Model
  node 集成到你的 workflows 中。
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

# OpenAI Chat Model

使用 OpenAI Chat Model node 将 OpenAI 的 chat models 与 conversational agents[^1] 配合使用。

在本页中，你可以找到 OpenAI Chat Model node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../../credentials/openai.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Model <a href="#model" id="model"></a>

选择用于生成 completion 的 model。

n8n 会从 OpenAI 动态加载 models，你只会看到你的账号可用的 models。

### Use Responses API <a href="#use-responses-api" id="use-responses-api"></a>

OpenAI 提供两个 endpoint，用于从 model 生成 output：

* **Chat Completions**：Chat Completions API endpoint 会根据构成对话的 messages 列表生成 model response。该 API 要求用户手动处理 conversation state，例如添加 [Simple Memory](../n8n-nodes-langchain.memorybufferwindow/) subnode。对于新项目，OpenAI 建议使用 Responses API。
* **Responses**：Responses API 是 agentic loop，允许 model 在一次 API request 期间调用多个 built-in tools。它还支持通过传入 `conversation_id` 来持久化 conversations。

如果希望 model 使用 Responses API 生成 output，请开启 **Use Responses API**。否则，OpenAI Chat Model node 默认使用 Chat Completions API。

有关 [Chat Completions 和 Responses APIs 的对比](https://platform.openai.com/docs/guides/migrate-to-responses)，请参阅 OpenAI 文档。

### Built-in Tools <a href="#built-in-tools" id="built-in-tools"></a>

OpenAI Responses API 提供一系列 [built-in tools](https://platform.openai.com/docs/guides/tools)，用于增强 model response。如果希望 model 可以访问以下 built-in tools，请开启 **Use Responses API**：

* **Web Search**：允许 models 在生成 response 前搜索 web，获取最新信息。
* **File Search**：允许 models 在生成 response 前搜索你之前上传的文件 knowledgebase，以查找相关信息。更多信息请参阅 [OpenAI 文档](https://platform.openai.com/docs/guides/tools-file-search)。
* **Code Interpreter**：允许 models 在 sandboxed environment 中编写并运行 Python code。

{% hint style="info" %}
**与 AI Agent node 配合使用**

Built-in tools 仅在 OpenAI Chat Model node 与 AI Agent node 组合使用时受支持。例如，与 Basic LLM Chain node 组合使用 OpenAI Chat Model node 时，built-in tools 不可用。
{% endhint %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项进一步调整 node 的行为。无论是否使用 Responses API 生成 model output，以下 options 都可用。

### Frequency Penalty <a href="#frequency-penalty" id="frequency-penalty"></a>

使用此选项控制 model 重复自身的概率。较高值会降低 model 重复自身的概率。

### Maximum Number of Tokens <a href="#maximum-number-of-tokens" id="maximum-number-of-tokens"></a>

输入使用的最大 tokens 数量，用于设置 completion length。

### Presence Penalty <a href="#presence-penalty" id="presence-penalty"></a>

使用此选项控制 model 谈论新主题的概率。较高值会增加 model 谈论新主题的概率。

### Sampling Temperature <a href="#sampling-temperature" id="sampling-temperature"></a>

使用此选项控制 sampling process 的随机性。较高 temperature 会产生更多样的 sampling，但也会增加 hallucinations 风险。

### Timeout <a href="#timeout" id="timeout"></a>

输入最大 request time，单位为毫秒。

### Max Retries <a href="#max-retries" id="max-retries"></a>

输入 retry request 的最大次数。

### Top P <a href="#top-p" id="top-p"></a>

使用此选项设置 completion 应使用的 probability。使用较低值可忽略可能性较低的 options。

## 额外 node 选项（仅 Responses API） <a href="#additional-node-options-responses-api-only" id="additional-node-options-responses-api-only"></a>

开启 **Use Responses API** 时，以下额外 options 可用。

### Conversation ID <a href="#conversation-id" id="conversation-id"></a>

此 response 所属的 conversation。此 response 完成后，该 response 的 input items 和 output items 会自动添加到此 conversation。

### Prompt Cache Key <a href="#prompt-cache-key" id="prompt-cache-key"></a>

使用此 key 缓存相似 requests，以优化 cache hit rates。

### Safety Identifier <a href="#safety-identifier" id="safety-identifier"></a>

应用 identifier 来跟踪可能违反 usage policies 的 users。

### Service Tier <a href="#service-tier" id="service-tier"></a>

选择适合需求的 service tier：Auto、Flex、Default 或 Priority。

### Metadata <a href="#metadata" id="metadata"></a>

一组用于存储 structured information 的 key-value pairs。你最多可以向一个 object 附加 16 个 pairs，这对于添加 custom data 很有用，这些 custom data 可被 API 或 dashboard 用于搜索。

### Top Logprobs <a href="#top-logprobs" id="top-logprobs"></a>

定义 0 到 20 之间的 integer，指定在每个 token position 返回最可能 tokens 的数量，每个 token 都带有关联的 log probability。

### Output Format <a href="#output-format" id="output-format"></a>

选择 response format：Text、JSON Schema 或 JSON Object。如果你希望接收 JSON 格式的数据，建议使用 JSON Schema。

### Prompt <a href="#prompt" id="prompt"></a>

配置填入 unique ID、version 和 substitutable variables 的 prompt。Prompts 通过 OpenAI dashboard 配置。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-langchain.lmchatopenai 集成模板](https://n8n.io/integrations/openai-chat-model)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 的 OpenAI 文档](https://js.langchain.com/docs/integrations/chat/openai/)。

有关参数的更多信息，请参阅 [OpenAI 文档](https://platform.openai.com/docs/api-reference/responses/create)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或故障以及建议解决方案，请参阅[常见问题](common-issues.md)。

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

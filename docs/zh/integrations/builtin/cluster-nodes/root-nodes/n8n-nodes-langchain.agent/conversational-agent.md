---
title: Conversational AI Agent node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 Conversational Agent。按照技术文档将
  Conversational Agent 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Conversational AI Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/conversational-agent
layout:
  description:
    visible: false
---

# Conversational AI Agent node <a href="#conversational-ai-agent-node" id="conversational-ai-agent-node"></a>

{% hint style="info" %}
**功能已移除**

n8n 已在 2025 年 2 月移除此功能。
{% endhint %}

Conversational Agent 可以进行类似人类的对话。它可以维护上下文、理解用户意图，并提供相关答案。此 agent 通常用于构建聊天机器人、虚拟助手和客户支持系统。

Conversational Agent 会在 system prompt 中描述 tools[^1]，并解析 JSON 响应用于 tool calls。如果你偏好的 AI model 不支持 tool calling，或者你正在处理更简单的交互，此 agent 是一个通用选项。它更灵活，但准确性可能低于 [Tools Agent](tools-agent.md)。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](README.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/cHtfs3gewkhPbGP31rjc/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Conversational Agent。

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 Conversational Agent node 的行为：

### Human Message <a href="#human-message" id="human-message"></a>

告诉 agent 它可以使用哪些 tools，并为用户输入添加上下文。

你必须包含这些 expressions 和变量：

* `{tools}`：一个 LangChain expression，提供你已连接到 Agent 的 tools 字符串。请说明谁应使用这些 tools，以及应如何使用。
* `{format_instructions}`：一个 LangChain expression，提供你已连接的 output parser node 中的 schema 或格式。由于这些说明本身就是上下文，因此无需再为此 expression 提供上下文。
* `{{input}}`：一个 LangChain 变量，包含用户的 prompt。此变量会填充为 **Prompt** 参数的值。请提供上下文，说明这是用户输入。

下面是这些字符串的一种用法示例：

示例：

```
TOOLS
------
Assistant 可以要求用户使用 tools 来查找可能有助于回答用户原始问题的信息。用户可以使用的 tools 如下：

{tools}

{format_instructions}

USER'S INPUT
--------------------
以下是用户输入（请记住，只能以 markdown code snippet 形式返回包含单个 action 的 JSON blob，不能返回其他内容）：

{{input}}
```

### System Message <a href="#system-message" id="system-message"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ci5NMdJiVoyT9dtdTE9w/" %}

### Max Iterations <a href="#max-iterations" id="max-iterations"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/8UflrA3Nx8LD5bKQn8Xc/" %}

### Return Intermediate Steps <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/skA96E8hAnMMKG7c4Lta/" %}

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。

[^1]: 在 AI 语境中，tool 是一种附加资源，AI 在响应请求时可以引用它来获取特定信息或功能。AI model 可以使用 tool 与外部系统交互，或完成特定且聚焦的任务。

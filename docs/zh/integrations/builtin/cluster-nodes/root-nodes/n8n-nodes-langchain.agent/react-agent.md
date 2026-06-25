---
title: ReAct AI Agent node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 ReAct Agent。按照技术文档将 ReAct
  Agent 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: ReAct AI Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/react-agent
layout:
  description:
    visible: false
---

# ReAct AI Agent node <a href="#react-ai-agent-node" id="react-ai-agent-node"></a>

{% hint style="info" %}
**功能已移除**

n8n 已在 2025 年 2 月移除此功能。
{% endhint %}

ReAct Agent node 实现 [ReAct](https://react-lm.github.io/) 逻辑。ReAct（reasoning and acting）将 chain-of-thought prompting 的推理能力与行动计划生成结合在一起。

ReAct Agent 会围绕给定任务进行推理，确定必要动作，然后执行这些动作。它会遵循推理和行动的循环，直到完成任务。ReAct agent 可以将复杂任务拆解为更小的子任务，对它们排序，并逐一执行。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](README.md)。

{% hint style="info" %}
**无 memory**

ReAct agent 不支持 memory sub-node。这意味着它无法回忆之前的 prompts，也无法模拟持续对话。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 ReAct Agent。

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项在对话开始时创建要发送给 agent 的消息。消息类型取决于你使用的 model：

* **Chat models**：这些 model 具有三个交互组件（AI、system 和 human）的概念。它们可以接收 system messages 和 human messages（prompts）。
* **Instruct models**：这些 model 没有独立的 AI、system 和 human 组件概念。它们接收一整段文本，即 instruct message。

### Human Message Template <a href="#human-message-template" id="human-message-template"></a>

使用此选项扩展用户 prompt。这是一种让 agent 在一次迭代到下一次迭代之间传递信息的方式。

可用的 LangChain expressions：

* `{input}`：包含用户 prompt。
* `{agent_scratchpad}`：用于在下一次迭代中记住的信息。

### Prefix Message <a href="#prefix-message" id="prefix-message"></a>

输入要在对话开始时添加到 tools 列表前面的文本。你无需添加 tools 列表。LangChain 会自动添加 tools 列表。

### Suffix Message for Chat Model <a href="#suffix-message-for-chat-model" id="suffix-message-for-chat-model"></a>

当 agent 使用 chat model 时，添加要在对话开始时附加到 tools 列表之后的文本。你无需添加 tools 列表。LangChain 会自动添加 tools 列表。

### Suffix Message for Regular Model <a href="#suffix-message-for-regular-model" id="suffix-message-for-regular-model"></a>

当 agent 使用 regular/instruct model 时，添加要在对话开始时附加到 tools 列表之后的文本。你无需添加 tools 列表。LangChain 会自动添加 tools 列表。

### Return Intermediate Steps <a href="#return-intermediate-steps" id="return-intermediate-steps"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/skA96E8hAnMMKG7c4Lta/" %}

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关更多信息，请参阅 LangChain 的 [ReAct Agents](https://js.langchain.com/docs/concepts/agents/) 文档。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。

---
title: Plan and Execute AI Agent node 文档
description: >-
  了解如何在 n8n 中使用 AI Agent node 的 Plan and Execute Agent。按照技术文档将
  Plan and Execute Agent 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Plan and Execute AI Agent node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/plan-execute-agent
layout:
  description:
    visible: false
---

# Plan and Execute Agent node <a href="#plan-and-execute-agent-node" id="plan-and-execute-agent-node"></a>

Plan and Execute Agent 类似 [ReAct agent](react-agent.md)，但更侧重规划。它会先创建用于解决给定任务的高层计划，然后逐步执行该计划。此 agent 最适合需要结构化方法和细致规划的任务。

有关 AI Agent node 本身的更多信息，请参阅 [AI Agent](README.md)。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置 Plan and Execute Agent。

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Node 选项 <a href="#node-options" id="node-options"></a>

使用这些选项细化 Plan and Execute Agent node 的行为：

### Human Message Template <a href="#human-message-template" id="human-message-template"></a>

输入 n8n 在每次 step 执行期间发送给 agent 的消息。

可用的 LangChain expressions：

* `{previous_steps}`：包含 agent 已完成的前序 step 信息。
* `{current_step}`：包含当前 step 的信息。
* `{agent_scratchpad}`：用于在下一次迭代中记住的信息。

### Tracing Metadata <a href="#tracing-metadata" id="tracing-metadata"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/GAsqtB1RVGEDrT5PMMLl/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

请参阅主 AI Agent node 的[模板和示例](README.md#templates-and-examples)部分。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或疑问以及建议的解决方案，请参阅[常见问题](common-issues.md)。

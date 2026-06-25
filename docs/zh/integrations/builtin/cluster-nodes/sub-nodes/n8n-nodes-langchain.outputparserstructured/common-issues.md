---
title: Structured Output Parser node 常见问题
contentType:
  - integration
  - reference
priority: high
nodeTitle: Structured Output Parser node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues
description: >-
  n8n workflow automation platform 中 Structured Output Parser node 的常见问题与疑问文档。包含问题详情和建议解决方案。
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

# 常见问题

这里列出 [Structured Output Parser node](./) 的一些常见错误和问题，以及解决或排查它们的步骤。

## 处理参数 <a href="#processing-parameters" id="processing-parameters"></a>

Structured Output Parser node 是 sub-node[^1]。使用 expressions 处理多个 items 时，sub-nodes 的行为与其他 nodes 不同。

大多数 nodes，包括 [root nodes](#user-content-fn-2)[^2]，都会接收任意数量的 items 作为 input，处理这些 items，并输出结果。你可以使用 expressions 引用 input items，node 会依次为每个 item 解析 expression。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 会依次解析为每个 name。

在 sub-nodes 中，expression 始终解析为第一个 item。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 始终解析为第一个 name。

## 将 structured output parser node 添加到 AI nodes <a href="#adding-the-structured-output-parser-node-to-ai-nodes" id="adding-the-structured-output-parser-node-to-ai-nodes"></a>

你可以将 output parser nodes 附加到部分 [AI root nodes](../../root-nodes/)。

要将 Structured Output Parser 添加到 node，请在你想要格式化的 AI root node 中启用 **Require Specific Output Format** 选项。启用该选项后，会显示一个新的 **output parser** attachment point。点击 **output parser** attachment point，即可将 Structured Output Parser node 添加到该 node。

## 使用 structured output parser 格式化 intermediary steps <a href="#using-the-structured-output-parser-to-format-intermediary-steps" id="using-the-structured-output-parser-to-format-intermediary-steps"></a>

Structured Output Parser node 会结构化 AI agents 的最终 output。它并不用于结构化传递给其他 AI tools 或 stages 的 intermediary output。

如果要为 intermediary output 请求特定格式，请在 **AI Agent** 的 **System Message** 中包含 response structure。该 message 可以包含 schema 或 example response，供 agent 用作结果模板。

## 结构化 agents 的 output <a href="#structuring-output-from-agents" id="structuring-output-from-agents"></a>

在使用 [agents](../../root-nodes/n8n-nodes-langchain.agent/) 时，structured output parsing 通常不可靠。

如果你的 workflow 使用 agents，n8n 建议使用单独的 [LLM-chain](../../root-nodes/n8n-nodes-langchain.chainllm.md) 接收 agent 输出的数据并解析它。相比直接在 agent workflow 中解析，这会带来更好、更一致的结果。

[^1]: n8n cluster nodes 由一个或多个连接到 root node 的 sub nodes 组成。Sub nodes 扩展 root node 的功能，提供对特定 services 或 resources 的访问，或提供特定类型的专用处理，例如 calculator functionality。
[^2]: 每个 n8n cluster node 都包含一个定义 cluster 主要功能的 root node。一个或多个 sub nodes 会附加到 root node，以扩展其功能。

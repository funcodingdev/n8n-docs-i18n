---
title: OpenAI Chat Model node 常见问题
description: >-
  n8n workflow automation platform 中 OpenAI Chat Model node 的常见问题与疑问文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: OpenAI Chat Model node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues
layout:
  description:
    visible: false
---

# OpenAI Chat Model node 常见问题 <a href="#openai-chat-model-node-common-issues" id="openai-chat-model-node-common-issues"></a>

这里列出 [OpenAI Chat Model node](README.md) 的一些常见错误和问题，以及解决或排查它们的步骤。

## 处理参数 <a href="#processing-parameters" id="processing-parameters"></a>

OpenAI Chat Model node 是 sub-node[^1]。使用 expressions 处理多个 items 时，sub-nodes 的行为与其他 nodes 不同。

大多数 nodes，包括 [root nodes](#user-content-fn-2)[^2]，都会接收任意数量的 items 作为 input，处理这些 items，并输出结果。你可以使用 expressions 引用 input items，node 会依次为每个 item 解析 expression。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 会依次解析为每个 name。

在 sub-nodes 中，expression 始终解析为第一个 item。例如，给定包含五个 name values 的 input，expression `{{ $json.name }}` 始终解析为第一个 name。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/wqdQXLzKrIsqxA7CuhxT/" %}

[^1]: n8n cluster nodes 由一个或多个连接到 root node 的 sub nodes 组成。Sub nodes 扩展 root node 的功能，提供对特定 services 或 resources 的访问，或提供特定类型的专用处理，例如 calculator functionality。
[^2]: 每个 n8n cluster node 都包含一个定义 cluster 主要功能的 root node。一个或多个 sub nodes 会附加到 root node，以扩展其功能。

---
title: 流式响应
contentType: howto
nodeTitle: Stream real-time responses
originalFilePath: workflows/streaming.md
originalUrl: https://docs.n8n.io/workflows/streaming
url: >-
  https://docs.n8n.io/build/understand-workflows/understand-executions/stream-real-time-responses
description: 构建带有流式响应的工作流
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

# 流式传输实时响应

{% hint style="info" %}
**功能可用性**

适用于所有计划。
{% endhint %}

流式响应允许你在 AI Agent node 生成数据时，将数据实时返回给用户。这对聊天机器人很有用，因为你可以在答案生成过程中展示给用户，从而提供更好的体验。

你可以使用以下任一方式启用 streaming：

* The [Chat Trigger](/broken/spaces/BKcbOzIWja8NfqKDcqHc/pages/ufgV9cVbZYhO7UuKUvU1)
* The [Webhook node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.webhook)

在这两种情况下，都要将 node 的 **Response Mode** 设置为 **Streaming**。

## 配置 node 以支持 streaming <a href="#configure-nodes-for-streaming" id="configure-nodes-for-streaming"></a>

如需流式传输数据，需要向工作流添加支持 streaming output 的 node。并非所有 node 都支持此功能。

1. 选择支持 streaming 的 node，例如：
   * [AI agent](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)
   * [Respond to Webhook](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.respondtowebhook)
2. 你可以在这些 node 的 options 中禁用 streaming。默认情况下，只要被执行 trigger 的 `Response Mode` 设置为 `Streaming response`，它们就会流式传输数据。

## 重要信息 <a href="#important-information" id="important-information"></a>

配置流式响应时，请注意以下细节：

* **Trigger**：trigger node 必须支持 streaming，并已配置 streaming。否则，工作流会按照 response mode 设置运行。
* **Node configuration**：即使 trigger 已启用 streaming，也至少需要配置一个 node 来流式传输数据。否则，工作流不会发送任何数据。

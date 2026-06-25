---
title: Trello Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Trello Trigger node。按照技术文档将 Trello Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Trello Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.trellotrigger
layout:
  description:
    visible: false
---

# Trello Trigger node <a href="#trello-trigger-node" id="trello-trigger-node"></a>

[Trello](https://trello.com/) 是一个基于 Web 的看板式列表应用，隶属于 Atlassian。用户可以创建包含不同列的任务看板，并在列之间移动任务。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/trello.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Trello Trigger integrations](https://n8n.io/integrations/trello-trigger/) 页面。
{% endhint %}

## 查找 Model ID <a href="#find-the-model-id" id="find-the-model-id"></a>

model ID 是 Trello 中任意 model 的 ID。根据使用场景，它可以是 User ID、List ID 等。

在此具体示例中，List ID 就是 Model ID：

1. 打开包含该列表的 Trello board。
2. 如果该列表没有任何 card，请向列表添加一张 card。
3. 打开该 card，在 URL 末尾添加 `.json`，然后按 Enter。
4. 在 JSON 文件中，你会看到名为 `idList` 的字段。
5. 复制 `idList` 并将其粘贴到 n8n 的 **Model ID** 字段中。

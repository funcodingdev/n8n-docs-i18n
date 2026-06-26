---
title: Gmail node documentation
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-base.gmail
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail
description: >-
  了解如何在 n8n 中使用 Gmail node。按照技术文档，将 Gmail node
  集成到你的 workflows 中。
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

# Gmail

使用 Gmail node 自动化 Gmail 中的工作，并将 Gmail 与其他 applications 集成。n8n 内置支持大量 Gmail 功能，包括创建、更新、删除和获取 drafts、messages、labels、threads。

在本页中，你会看到 Gmail node 支持的 operations 列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关设置身份验证的指导，请参考 [Google credentials](../../credentials/google/)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Operations 操作 <a href="#operations" id="operations"></a>

* **Draft**
  * [**Create**](draft-operations.md#create-a-draft) draft
  * [**Delete**](draft-operations.md#delete-a-draft) draft
  * [**Get**](draft-operations.md#get-a-draft) draft
  * [**Get Many**](draft-operations.md#get-many-drafts) drafts
* **Label**
  * [**Create**](label-operations.md#create-a-label) label
  * [**Delete**](label-operations.md#delete-a-label) label
  * [**Get**](label-operations.md#get-a-label) label
  * [**Get Many**](label-operations.md#get-many-labels) labels
* **Message**
  * [**Add Label**](message-operations.md#add-label-to-a-message) 到 message
  * [**Delete**](message-operations.md#delete-a-message) message
  * [**Get**](message-operations.md#get-a-message) message
  * [**Get Many**](message-operations.md#get-many-messages) messages
  * [**Mark as Read**](message-operations.md#mark-as-read)
  * [**Mark as Unread**](message-operations.md#mark-as-unread)
  * [**Remove Label**](message-operations.md#remove-label-from-a-message) from message
  * [**Reply**](message-operations.md#reply-to-a-message) to message
  * [**Send**](message-operations.md#send-a-message) message
* **Thread**
  * [**Add Label**](thread-operations.md#add-label-to-a-thread) 到 thread
  * [**Delete**](thread-operations.md#delete-a-thread) thread
  * [**Get**](thread-operations.md#get-a-thread) thread
  * [**Get Many**](thread-operations.md#get-many-threads) threads
  * [**Remove Label**](thread-operations.md#remove-label-from-a-thread) from thread
  * [**Reply**](thread-operations.md#reply-to-a-message) to message
  * [**Trash**](thread-operations.md#trash-a-thread) thread
  * [**Untrash**](thread-operations.md#untrash-a-thread) thread

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-base.gmail integration templates](https://n8n.io/integrations/gmail) 或[搜索全部 templates](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此 node 集成的 API 的详细信息，请参考 Google 的 [Gmail API documentation](https://developers.google.com/gmail/api)。

n8n 为 Gmail 提供 trigger node。你可以在[这里](../../trigger-nodes/n8n-nodes-base.gmailtrigger/)找到 trigger node 文档。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见 errors 或 issues 及建议解决步骤，请参考 [常见问题](common-issues.md)。

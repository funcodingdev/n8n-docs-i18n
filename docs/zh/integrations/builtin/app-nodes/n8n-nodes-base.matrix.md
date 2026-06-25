---
title: Matrix node documentation
description: >-
  了解如何在 n8n 中使用 Matrix node。按照技术文档将 Matrix node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Matrix node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.matrix.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.matrix'
layout:
  description:
    visible: false
---

# Matrix node <a href="#matrix-node" id="matrix-node"></a>

使用 Matrix node 自动化 Matrix 中的工作，并将 Matrix 与其他应用集成。n8n 内置支持大量 Matrix 功能，包括获取当前 user 的 account 信息、向 room 发送 media 和 message，以及获取 room member 和 message。

在本页中，你可以找到 Matrix node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Matrix credentials](../credentials/matrix.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Account
    * 获取当前 user 的 account 信息
* Event
    * 按 ID 获取单个 event
* Media
    * 向 chat room 发送 media
* Message
    * 向 room 发送 message
    * 获取 room 中的所有 message
* Room
    * 使用指定设置创建新 chat room
    * 邀请 user 加入 room
    * 加入新 room
    * 将 user 踢出 room
    * 离开 room
* Room Member
    * 获取所有 member

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Matrix node 文档集成模板](https://n8n.io/integrations/matrix)或[搜索所有模板](https://n8n.io/workflows/)

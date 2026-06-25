---
title: Trello node documentation
description: >-
  了解如何在 n8n 中使用 Trello node。按照技术文档将 Trello node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Trello node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.trello.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.trello'
layout:
  description:
    visible: false
---

# Trello node <a href="#trello-node" id="trello-node"></a>

使用 Trello node 自动化 Trello 中的工作，并将 Trello 与其他应用集成。n8n 内置支持大量 Trello 功能，包括创建和更新 card，以及添加和移除 member。

在本页中，你可以找到 Trello node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Trello credentials](../credentials/trello.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Attachment
    * 为 card 创建新 attachment
    * 删除 attachment
    * 获取 attachment 数据
    * 返回 card 的所有 attachment
* Board
    * 创建新 board
    * 删除 board
    * 获取 board 数据
    * 更新 board
* Board Member
    * 添加
    * 获取全部
    * 邀请
    * 移除
* Card
    * 创建新 card
    * 删除 card
    * 获取 card 数据
    * 更新 card
* Card Comment
    * 在 card 上创建 comment
    * 从 card 删除 comment
    * 更新 card 上的 comment
* Checklist
    * 创建 checklist item
    * 创建新 checklist
    * 删除 checklist
    * 删除 checklist item
    * 获取 checklist 数据
    * 返回 card 的所有 checklist
    * 获取 card 上的特定 checklist
    * 获取 card 上已完成的 checklist item
    * 更新 card 上 checklist 中的 item
* Label
    * 向 card 添加 label。
    * 创建新 label
    * 删除 label
    * 获取 label 数据
    * 返回 board 的所有 label
    * 从 card 移除 label。
    * 更新 label。
* List
    * 归档/取消归档 list
    * 创建新 list
    * 获取 list 数据
    * 获取所有 list
    * 获取 list 中的所有 card
    * 更新 list

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Trello node 文档集成模板](https://n8n.io/integrations/trello)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 查找 List ID <a href="#find-the-list-id" id="find-the-list-id"></a>

1. 打开包含该 list 的 Trello board。
2. 如果该 list 没有任何 card，请向 list 添加一个 card。
3. 打开 card，在 URL 末尾添加 `.json`，然后按 Enter。
4. 在 JSON 文件中，你会看到名为 `idList` 的字段。
5. 复制 `idList` 字段的内容，并将其粘贴到 n8n 的 ***List ID** 字段中。

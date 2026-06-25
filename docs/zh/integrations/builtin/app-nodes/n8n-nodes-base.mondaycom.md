---
title: monday.com node documentation
description: >-
  了解如何在 n8n 中使用 monday.com node。按照技术文档将 monday.com node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: monday.com node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mondaycom.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mondaycom'
layout:
  description:
    visible: false
---

# monday.com node <a href="#mondaycom-node" id="mondaycom-node"></a>

使用 monday.com node 自动化 monday.com 中的工作，并将 monday.com 与其他应用集成。n8n 内置支持大量 monday.com 功能，包括创建新 board，以及在 board 上添加、删除和获取 item。

在本页中，你可以找到 monday.com node 支持的操作列表，以及更多资源链接。

{% hint style="warning" %}
**最低要求版本**

此 node 要求 n8n 版本为 1.22.6 或更高。
{% endhint %}

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [monday.com credentials](../credentials/mondaycom.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Board
    * 归档 board
    * 创建新 board
    * 获取 board
    * 获取所有 board
* Board Column
    * 创建新 column
    * 获取所有 column
* Board Group
    * 删除 board 中的 group
    * 在 board 中创建 group
    * 获取 board 中的 group 列表
* Board Item
    * 向 item 添加 update。
    * 更改 board item 的 column value
    * 更改 board item 的多个 column value
    * 在 board 的 group 中创建 item
    * 删除 item
    * 获取 item
    * 获取所有 item
    * 按 column value 获取 item
    * 将 item 移动到 group

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 monday.com node 文档集成模板](https://n8n.io/integrations/mondaycom)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

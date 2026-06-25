---
title: Google Books node documentation
description: >-
  了解如何在 n8n 中使用 Google Books node。按照技术文档将 Google Books node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Google Books node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks'
layout:
  description:
    visible: false
---

# Google Books node <a href="#google-books-node" id="google-books-node"></a>

使用 Google Books node 自动化 Google Books 中的工作，并将 Google Books 与其他应用集成。n8n 内置支持大量 Google Books 功能，包括为指定 user 检索特定 bookshelf resource、向 bookshelf 添加 volume，以及获取 volume。

在本页中，你可以找到 Google Books node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Google credentials](../credentials/google/README.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Bookshelf
    * 为指定 user 检索特定 bookshelf resource
    * 获取指定 user 的所有公共 bookshelf resource
* Bookshelf Volume
    * 向 bookshelf 添加 volume
    * 清空 bookshelf 中的所有 volume
    * 获取指定 user 在特定 bookshelf 中的所有 volume
    * 在 bookshelf 内移动 volume
    * 从 bookshelf 中移除 volume
* Volume
    * 基于 ID 获取 volume resource
    * 获取按 query 过滤的所有 volume

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Google Books node 文档集成模板](https://n8n.io/integrations/google-books)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

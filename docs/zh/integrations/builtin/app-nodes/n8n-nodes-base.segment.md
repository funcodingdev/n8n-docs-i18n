---
title: Segment node documentation
description: >-
  了解如何在 n8n 中使用 Segment node。按照技术文档将 Segment node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Segment node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.segment.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.segment'
layout:
  description:
    visible: false
---

# Segment node <a href="#segment-node" id="segment-node"></a>

使用 Segment node 自动化 Segment 中的工作，并将 Segment 与其他应用集成。n8n 内置支持大量 Segment 功能，包括将 user 添加到 group、创建 identity，以及跟踪 activity。

在本页中，你可以找到 Segment node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Segment credentials](../credentials/segment.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Group
    * 将 user 添加到 group
* Identify
    * 创建 identity
* Track
    * 记录 user 执行的操作。每个操作都会触发一个 event，该 event 也可以带有关联 property。
    * 记录你网站上的 page view，以及有关所查看页面的可选额外信息。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Segment node 文档集成模板](https://n8n.io/integrations/segment)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

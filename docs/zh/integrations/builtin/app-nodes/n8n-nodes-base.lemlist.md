---
title: Lemlist node documentation
description: >-
  了解如何在 n8n 中使用 Lemlist node。按照技术文档将 Lemlist node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Lemlist node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.lemlist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.lemlist'
layout:
  description:
    visible: false
---

# Lemlist node <a href="#lemlist-node" id="lemlist-node"></a>

使用 Lemlist node 自动化 Lemlist 中的工作，并将 Lemlist 与其他应用集成。n8n 内置支持大量 Lemlist 功能，包括获取 activity、team 和 campaign，以及创建、更新和删除 lead。

在本页中，你可以找到 Lemlist node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Lemlist credentials](../credentials/lemlist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Activity
    * Get Many：获取多个 activity
* Campaign
    * Get Many：获取多个 campaign
    * Get Stats：获取 campaign stats
* Enrichment
    * Get：获取之前完成的 enrichment
    * Enrich Lead：使用 email 或 LinkedIn URL 丰富 lead
    * Enrich Person：使用 email 或 LinkedIn URL 丰富 person
* Lead
    * Create：创建新 lead
    * Delete：删除现有 lead
    * Get：获取现有 lead
    * Unsubscribe：取消订阅现有 lead
* Team
    * Get：获取现有 team
    * Get Credits：获取现有 team 的 credit
* Unsubscribe
    * Add：将 email 添加到 unsubscribe list
    * Delete：从 unsubscribe list 中删除 email
    * Get Many：获取多个已取消订阅的 email

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Lemlist node 文档集成模板](https://n8n.io/integrations/lemlist)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

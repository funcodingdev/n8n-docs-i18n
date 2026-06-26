---
title: Supabase node documentation
description: >-
  了解如何在 n8n 中使用 Supabase node。按照技术文档将 Supabase node 集成到你的工作流中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-base.supabase
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.supabase/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.supabase'
layout:
  description:
    visible: false
---

# Supabase node <a href="#supabase-node" id="supabase-node"></a>

使用 Supabase node 自动化 Supabase 中的工作，并将 Supabase 与其他应用集成。n8n 内置支持大量 Supabase 功能，包括创建、删除和获取行。

在本页中，你可以找到 Supabase node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [Supabase credentials](../../credentials/supabase.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Operations 操作 <a href="#operations" id="operations"></a>

* Row
    * Create a new row
    * Delete a row
    * Get a row
    * Get all rows
    * Update a row

## 使用自定义 schema <a href="#using-custom-schemas" id="using-custom-schemas"></a>

默认情况下，Supabase node 只获取 `public` schema。要获取[自定义 schema](https://supabase.com/docs/guides/api/using-custom-schemas)，请启用 **Use Custom Schema**。

在新的 **Schema** 字段中，提供 Supabase node 应使用的自定义 schema。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.supabase 集成模板](https://n8n.io/integrations/supabase) 或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

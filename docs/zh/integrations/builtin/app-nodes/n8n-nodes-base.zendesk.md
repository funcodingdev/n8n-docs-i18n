---
title: Zendesk node 文档
description: >-
  了解如何在 n8n 中使用 Zendesk node。按照技术文档将 Zendesk node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Zendesk node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.zendesk.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.zendesk'
layout:
  description:
    visible: false
---

# Zendesk node <a href="#zendesk-node" id="zendesk-node"></a>

使用 Zendesk node 自动化 Zendesk 中的工作，并将 Zendesk 与其他应用集成。n8n 内置支持大量 Zendesk 功能，包括创建和删除 ticket、用户与组织。

在本页中，你可以找到 Zendesk node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Zendesk credentials](../credentials/zendesk.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* 工单
    * 创建工单
    * 删除工单
    * 获取工单
    * 获取所有工单
    * 恢复已暂停的工单
    * 更新工单
* 工单字段
    * 获取工单字段
    * 获取所有系统和自定义工单字段
* 用户
    * 创建用户
    * 删除用户
    * 获取用户
    * 获取所有用户
    * 获取用户的组织
    * 获取与用户相关的数据
    * 搜索用户
    * 更新用户
* 组织
    * 创建组织
    * 删除组织
    * 统计组织
    * 获取组织
    * 获取所有组织
    * 获取与组织相关的数据
    * 更新组织

{% hint style="warning" %}
**Tag 替换行为**

使用 Zendesk node 的“更新工单”操作并指定 `Tag Names or IDs` 字段时，ticket 上的整个 tag 列表**会被替换**。由于 Zendesk API 默认处理 tag 更新的方式，未包含在更新中的任何 tag 都会从 ticket 中移除。

**为避免意外移除 tag：**

- 先检索 ticket 的 tag，并在更新前将它们与你的新 tag 合并。
- 或者，使用 HTTP Request node 和 Zendesk 的 `additional_tags` 属性来添加 tag，而不移除现有 tag。
- 你也可以调用 ticket 的 `/tags` endpoint 来添加 tag，而不替换现有 tag（[Zendesk tags endpoint documentation](https://developer.zendesk.com/api-reference/ticketing/ticket-management/tags/)）。

详情请参阅官方文档：[Adding tags to tickets without overwriting existing tags](https://developer.zendesk.com/documentation/ticketing/managing-tickets/adding-tags-to-tickets-without-overwriting-existing-tags/)。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Zendesk node 文档集成模板](https://n8n.io/integrations/zendesk)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

---
title: Salesforce node documentation
description: >-
  了解如何在 n8n 中使用 Salesforce node。按照技术文档将 Salesforce node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Salesforce node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.salesforce.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.salesforce'
layout:
  description:
    visible: false
---

# Salesforce node <a href="#salesforce-node" id="salesforce-node"></a>

使用 Salesforce node 自动化 Salesforce 中的工作，并将 Salesforce 与其他应用集成。n8n 内置支持大量 Salesforce 功能，包括创建、更新、删除和获取 account、attachment、case 与 lead，以及上传 document。

在本页中，你可以找到 Salesforce node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Salesforce credentials](../credentials/salesforce.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Account
    * 向 account 添加 note
    * 创建 account
    * 创建新 account；如果当前 account 已存在，则更新它（upsert）
    * 获取 account
    * 获取所有 account
    * 返回 account metadata 概览。
    * 删除 account
    * 更新 account
* Attachment
    * 创建 attachment
    * 删除 attachment
    * 获取 attachment
    * 获取所有 attachment
    * 返回 attachment metadata 概览。
    * 更新 attachment
* Case
    * 向 case 添加 comment
    * 创建 case
    * 获取 case
    * 获取所有 case
    * 返回 case metadata 概览
    * 删除 case
    * 更新 case
* Contact
    * 将 lead 添加到 campaign
    * 向 contact 添加 note
    * 创建 contact
    * 创建新 contact；如果当前 contact 已存在，则更新它（upsert）
    * 删除 contact
    * 获取 contact
    * 返回 contact metadata 概览
    * 获取所有 contact
    * 更新 contact
* Custom Object
    * 创建 custom object record
    * 创建新 record；如果当前 record 已存在，则更新它（upsert）
    * 获取 custom object record
    * 获取所有 custom object record
    * 删除 custom object record
    * 更新 custom object record
* Document
    * 上传 document
* Flow
    * 获取所有 flow
    * 调用 flow
* Lead
    * 将 lead 添加到 campaign
    * 向 lead 添加 note
    * 创建 lead
    * 创建新 lead；如果当前 lead 已存在，则更新它（upsert）
    * 删除 lead
    * 获取 lead
    * 获取所有 lead
    * 返回 Lead metadata 概览
    * 更新 lead
* Opportunity
    * 向 opportunity 添加 note
    * 创建 opportunity
    * 创建新 opportunity；如果当前 opportunity 已存在，则更新它（upsert）
    * 删除 opportunity
    * 获取 opportunity
    * 获取所有 opportunity
    * 返回 opportunity metadata 概览
    * 更新 opportunity
* Search
    * 执行 SOQL query，并在单个 response 中返回所有结果
* Task
    * 创建 task
    * 删除 task
    * 获取 task
    * 获取所有 task
    * 返回 task metadata 概览
    * 更新 task
* User
    * 获取 user
    * 获取所有 user

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Salesforce node 文档集成模板](https://n8n.io/integrations/salesforce)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 使用 Salesforce custom fields <a href="#working-with-salesforce-custom-fields" id="working-with-salesforce-custom-fields"></a>

要向 request 添加 custom field：

1. 选择 **Additional Fields** > **Add Field**。
2. 在下拉菜单中选择 **Custom Fields**。

然后你就可以查找并添加 custom field。

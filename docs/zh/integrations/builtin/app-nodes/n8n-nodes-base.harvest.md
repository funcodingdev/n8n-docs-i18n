---
title: Harvest node documentation
description: >-
  了解如何在 n8n 中使用 Harvest node。按照技术文档将 Harvest node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Harvest node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.harvest.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.harvest'
layout:
  description:
    visible: false
---

# Harvest node <a href="#harvest-node" id="harvest-node"></a>

使用 Harvest node 自动化 Harvest 中的工作，并将 Harvest 与其他应用集成。n8n 内置支持大量 Harvest 功能，包括创建、更新、删除和获取 client、contact、invoice、task、expense、user 与 project。

在本页中，你可以找到 Harvest node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Harvest credentials](../credentials/harvest.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Client
    * 创建 client
    * 删除 client
    * 获取 client 数据
    * 获取所有 client 的数据
    * 更新 client
* Company
    * 检索当前已验证 user 的 company
* Contact
    * 创建 contact
    * 删除 contact
    * 获取 contact 数据
    * 获取所有 contact 的数据
    * 更新 contact
* Estimate
    * 创建 estimate
    * 删除 estimate
    * 获取 estimate 数据
    * 获取所有 estimate 的数据
    * 更新 estimate
* Expense
    * 获取 expense 数据
    * 获取所有 expense 的数据
    * 创建 expense
    * 更新 expense
    * 删除 expense
* Invoice
    * 获取 invoice 数据
    * 获取所有 invoice 的数据
    * 创建 invoice
    * 更新 invoice
    * 删除 invoice
* Project
    * 创建 project
    * 删除 project
    * 获取 project 数据
    * 获取所有 project 的数据
    * 更新 project
* Task
    * 创建 task
    * 删除 task
    * 获取 task 数据
    * 获取所有 task 的数据
    * 更新 task
* Time Entries
    * 使用 duration 创建 time entry
    * 使用 start time 和 end time 创建 time entry
    * 删除 time entry
    * 删除 time entry 的 external reference。
    * 获取 time entry 数据
    * 获取所有 time entry 的数据
    * 重新启动 time entry
    * 停止 time entry
    * 更新 time entry
* User
    * 创建 user
    * 删除 user
    * 获取 user 数据
    * 获取所有 user 的数据
    * 获取已验证 user 的数据
    * 更新 user

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Harvest node 文档集成模板](https://n8n.io/integrations/harvest)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

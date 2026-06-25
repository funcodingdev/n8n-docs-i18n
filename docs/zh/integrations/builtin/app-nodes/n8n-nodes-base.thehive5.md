---
title: TheHive 5 node documentation
description: >-
  了解如何在 n8n 中使用 TheHive 5 node。按照技术文档将 TheHive 5 node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: TheHive 5 node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.thehive5.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive5'
layout:
  description:
    visible: false
---

# TheHive 5 node <a href="#thehive-5-node" id="thehive-5-node"></a>

使用 TheHive 5 node 自动化 TheHive 中的工作，并将 TheHive 与其他应用集成。n8n 内置支持大量 TheHive 功能，包括创建 alert，统计 task log、case 和 observable。

在本页中，你可以找到 TheHive node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**TheHive 和 TheHive 5**

n8n 为 TheHive 提供两个 node。如果你想使用 TheHive 版本 5 API，请使用此 node（TheHive 5）。如果想使用版本 3 或 4，请使用 [TheHive](n8n-nodes-base.thehive.md)。
{% endhint %}
{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [TheHive credentials](../credentials/thehive5.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Alert
    * 创建
    * 删除
    * 执行 Responder
    * 获取
    * 合并到 Case
    * 提升为 Case
    * 搜索
    * 更新
    * 更新 Status
* Case
    * 添加 Attachment
    * 创建
    * 删除 Attachment
    * 删除 Case
    * 执行 Responder
    * 获取
    * 获取 Attachment
    * 获取 Timeline
    * 搜索
    * 更新
* Comment
    * 创建
    * 删除
    * 搜索
    * 更新
* Observable
    * 创建
    * 删除
    * 执行 Analyzer
    * 执行 Responder
    * 获取
    * 搜索
    * 更新
* Page
    * 创建
    * 删除
    * 搜索
    * 更新
* Query
    * 执行 Query
* Task
    * 创建
    * 删除
    * 执行 Responder
    * 获取
    * 搜索
    * 更新
* Task Log
    * 添加 Attachment
    * 创建
    * 删除
    * 删除 Attachment
    * 执行 Responder
    * 获取
    * 搜索

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 TheHive 5 node 文档集成模板](https://n8n.io/integrations/thehive-5)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 提供 trigger node。你可以在[这里](../trigger-nodes/n8n-nodes-base.thehive5trigger.md)找到 trigger node 文档。

有关此服务的更多信息，请参阅 TheHive [文档](https://docs.strangebee.com/)。

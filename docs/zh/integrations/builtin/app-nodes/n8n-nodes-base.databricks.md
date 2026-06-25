---
title: Databricks node documentation
description: >-
  了解如何在 n8n 中使用 Databricks node。按照技术文档将 Databricks node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Databricks node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.databricks.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.databricks'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.databricks'
layout:
  description:
    visible: false
---

# Databricks node <a href="#databricks-node" id="databricks-node"></a>

使用 Databricks node 自动化 Databricks 中的工作，并将 Databricks 与其他应用集成。n8n 内置支持大量 Databricks 功能，包括执行 SQL query、管理 Unity Catalog 对象、查询 ML model serving endpoint，以及处理 vector search index。

在本页中，你可以找到 Databricks node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Databricks credentials](../credentials/databricks.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Databricks SQL
    * 执行 Query
* File
    * 创建 Directory
    * 删除 Directory
    * 删除 File
    * 下载 File
    * 获取 File Metadata
    * 列出 Directory
    * 上传 File
* Genie
    * 创建 Conversation Message
    * 执行 Message SQL Query
    * 获取 Conversation Message
    * 获取 Genie Space
    * 获取 Query Results
    * 启动 Conversation
* Model Serving
    * 查询 Endpoint
* Unity Catalog
    * 创建 Catalog
    * 创建 Function
    * 创建 Volume
    * 删除 Catalog
    * 删除 Function
    * 删除 Volume
    * 获取 Catalog
    * 获取 Function
    * 获取 Table
    * 获取 Volume
    * 列出 Catalog
    * 列出 Function
    * 列出 Table
    * 列出 Volume
    * 更新 Catalog
* Vector Search
    * 创建 Index
    * 获取 Index
    * 列出 Index
    * 查询 Index

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Databricks node 文档集成模板](https://n8n.io/integrations/databricks)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关 Databricks API 的详细信息，请参阅 [Databricks REST API 文档](https://docs.databricks.com/api/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

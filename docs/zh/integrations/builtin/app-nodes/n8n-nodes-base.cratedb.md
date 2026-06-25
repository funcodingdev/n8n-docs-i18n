---
title: CrateDB node documentation
description: >-
  了解如何在 n8n 中使用 CrateDB node。按照技术文档将 CrateDB node 集成到你的 workflow
  中。
contentType:
  - integration
  - reference
nodeTitle: CrateDB node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.cratedb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.cratedb'
layout:
  description:
    visible: false
---

# CrateDB node <a href="#cratedb-node" id="cratedb-node"></a>

使用 CrateDB node 自动化 CrateDB 中的工作，并将 CrateDB 与其他应用集成。n8n 内置支持大量 CrateDB 功能，包括在数据库中执行、插入和更新 row。

在本页中，你可以找到 CrateDB node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [CrateDB credentials](../credentials/cratedb.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 执行 SQL query
* 在数据库中插入 row
* 在数据库中更新 row

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 CrateDB node 文档集成模板](https://n8n.io/integrations/cratedb)或[搜索所有模板](https://n8n.io/workflows/)

## Node 参考 <a href="#node-reference" id="node-reference"></a>

### 指定 column 的数据类型 <a href="#specify-a-columns-data-type" id="specify-a-columns-data-type"></a>

要指定 column 的数据类型，请在 column 名称后追加 `:type`，其中 `type` 是你希望该 column 使用的数据类型。例如，如果你想为 **id** column 指定 `int` 类型，并为 **name** column 指定 `text` 类型，可以在 **Columns** 字段中使用以下片段：`id:int,name:text`。

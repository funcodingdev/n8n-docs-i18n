---
title: TimescaleDB node documentation
description: >-
  了解如何在 n8n 中使用 TimescaleDB node。按照技术文档将 TimescaleDB node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: TimescaleDB node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.timescaledb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.timescaledb'
layout:
  description:
    visible: false
---

# TimescaleDB node <a href="#timescaledb-node" id="timescaledb-node"></a>

使用 TimescaleDB node 自动化 TimescaleDB 中的工作，并将 TimescaleDB 与其他应用集成。n8n 内置支持大量 TimescaleDB 功能，包括执行 SQL query，以及向数据库插入和更新 row。

在本页中，你可以找到 TimescaleDB node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [TimescaleDB credentials](../credentials/timescaledb.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 执行 SQL query
* 向数据库中插入 row
* 更新数据库中的 row

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 TimescaleDB node 文档集成模板](https://n8n.io/integrations/timescaledb)或[搜索所有模板](https://n8n.io/workflows/)

## 指定 column 的数据类型 <a href="#specify-a-columns-data-type" id="specify-a-columns-data-type"></a>

要指定 column 的数据类型，请在 column name 后追加 `:type`，其中 `type` 是你希望该 column 使用的数据类型。例如，如果你想为 **id** column 指定 `int` 类型，并为 **name** column 指定 `text` 类型，可以在 **Columns** 字段中使用以下片段：`id:int,name:text`。

---
title: Grist node documentation
description: >-
  了解如何在 n8n 中使用 Grist node。按照技术文档将 Grist node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Grist node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.grist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grist'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.grist'
layout:
  description:
    visible: false
---

# Grist node <a href="#grist-node" id="grist-node"></a>

使用 Grist node 自动化 Grist 中的工作，并将 Grist 与其他应用集成。n8n 内置支持大量 Grist 功能，包括在 table 中创建、更新、删除和读取 row。

在本页中，你可以找到 Grist node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Grist credentials](../credentials/grist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 在 table 中创建 row
* 从 table 中删除 row
* 从 table 中读取 row
* 更新 table 中的 row

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Grist node 文档集成模板](https://n8n.io/integrations/grist)或[搜索所有模板](https://n8n.io/workflows/)

## 获取 Row ID <a href="#get-the-row-id" id="get-the-row-id"></a>

要更新或删除特定 record，你需要 Row ID。获取 Row ID 有两种方式：

**在 Grist 中创建 Row ID column**

在你的 Grist table 中创建一个新 column，公式为 `$id`。

**使用 Get All 操作**

**Get All** 操作会返回每条 record 的 Row ID 及其字段。

你可以用表达式 `{{$("GristNodeName").item.json.id}}` 获取它。

## 使用 Get All 操作时过滤 record <a href="#filter-records-when-using-the-get-all-operation" id="filter-records-when-using-the-get-all-operation"></a>

- 选择 **Add Option**，并从下拉列表中选择 **Filter**。
- 你可以为任意数量的 column 添加 filter。结果只会包含匹配所有 column 的 record。
- 对于每个 column，你可以输入任意数量的值，并用逗号分隔。结果会包含匹配该 column 任意值的 record。

---
title: Airtable node documentation
description: >-
  了解如何在 n8n 中使用 Airtable node。按照技术文档将 Airtable node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: n8n-nodes-base.airtable
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtable'
layout:
  description:
    visible: false
---

# Airtable node <a href="#airtable-node" id="airtable-node"></a>

使用 Airtable node 自动化 Airtable 中的工作，并将 Airtable 与其他应用集成。n8n 内置支持大量 Airtable 功能，包括创建、读取、列出、更新和删除 table。

在本页中，你可以找到 Airtable node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Airtable credentials](../../credentials/airtable.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Append the data to a table
* Delete data from a table
* List data from a table
* Read data from a table
* Update data in a table

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 n8n-nodes-base.airtable 集成模板](https://n8n.io/integrations/airtable)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Airtable 提供了 trigger node。你可以在[这里](../../trigger-nodes/n8n-nodes-base.airtabletrigger.md)查看 trigger node 文档。

有关该服务的更多信息，请参阅 [Airtable 文档](https://airtable.com/developers/web/api/introduction)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}


## Node 参考 <a href="#node-reference" id="node-reference"></a>

### 获取 Record ID <a href="#get-the-record-id" id="get-the-record-id"></a>

要获取特定 record 的数据，你需要 Record ID。获取 Record ID 有两种方式。

### 在 Airtable 中创建 Record ID 列 <a href="#create-a-record-id-column-in-airtable" id="create-a-record-id-column-in-airtable"></a>

要在 table 中创建 `Record ID` 列，请参阅这篇[文章](https://support.airtable.com/docs/finding-airtable-ids)。然后你可以在 Airtable node 中使用此 Record ID。

### 使用 List 操作 <a href="#use-the-list-operation" id="use-the-list-operation"></a>

要获取 record 的 Record ID，可以使用 Airtable node 的 **List** 操作。此操作会返回 Record ID 以及字段。然后你可以在 Airtable node 中使用此 Record ID。

### 使用 List 操作时过滤 record <a href="#filter-records-when-using-the-list-operation" id="filter-records-when-using-the-list-operation"></a>

要从 Airtable base 过滤 record，请使用 **Filter By Formula** 选项。例如，如果你想返回属于组织 `n8n` 的所有用户，请按照以下步骤操作：

1. 从 **Operation** 下拉列表中选择 'List'。
2. 分别在 **Base ID** 和 **Table** 字段中输入 base ID 和 table 名称。
3. 点击 **Add Option**，并从下拉列表中选择 'Filter By Formula'。
4. 在 **Filter By Formula** 字段中输入以下公式：`{Organization}='n8n'`。

类似地，如果你想返回不属于组织 `n8n` 的所有用户，请使用以下公式：`NOT({Organization}='n8n')`。

参阅 Airtable [文档](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference)，了解更多关于公式的信息。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议的解决步骤，请参阅[常见问题](common-issues.md)。

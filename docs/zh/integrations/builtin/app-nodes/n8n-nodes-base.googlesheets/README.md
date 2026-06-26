---
title: Google Sheets
description: >-
  n8n 中 Google Sheets node 的文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: n8n-nodes-base.googlesheets
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets'
layout:
  description:
    visible: false
---

# Google Sheets <a href="#google-sheets" id="google-sheets"></a>

使用 Google Sheets node 自动化 Google Sheets 中的工作，并将 Google Sheets 与其他应用集成。n8n 内置支持大量 Google Sheets 功能，包括创建、更新、删除、追加、移除和获取文档。

在本页中，你可以找到 Google Sheets node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [Google Sheets credentials](../../credentials/google/README.md)。
{% endhint %}

## Operations 操作 <a href="#operations" id="operations"></a>

* **Document**
    * [**Create**](document-operations.md#create-a-spreadsheet) 电子表格。
	* [**Delete**](document-operations.md#delete-a-spreadsheet) 电子表格。
* **Sheet Within Document**
	* [**Append or Update Row**](sheet-operations.md#append-or-update-row)：追加新行；如果该行已存在，则更新当前行。
	* [**Append Row**](sheet-operations.md#append-row)：创建新行。
	* [**Clear**](sheet-operations.md#clear-a-sheet) sheet 中的所有数据。
	* [**Create**](sheet-operations.md#create-a-new-sheet) 新 sheet。
	* [**Delete**](sheet-operations.md#delete-a-sheet) sheet。
	* [**Delete Rows or Columns**](sheet-operations.md#delete-rows-or-columns)：从 sheet 中删除列和行。
	* [**Get Row(s)**](sheet-operations.md#get-rows)：读取 sheet 中的所有行。
	* [**Update Row**](sheet-operations.md#update-row)：更新 sheet 中的一行。


## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.googlesheets 集成模板](https://n8n.io/integrations/google-sheets) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Google Sheet 的 API 文档](https://developers.google.com/sheets/api)。



## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或错误以及建议解决方案，请参阅[常见问题](common-issues.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

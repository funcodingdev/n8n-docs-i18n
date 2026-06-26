---
title: Google Sheets Document operations
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Google Sheets Document operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations
description: >-
  n8n 中 Google Sheets node 的 Document 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Document operations

使用此操作从 Google Sheets 创建或删除 Google 电子表格。有关 Google Sheets node 本身的更多信息，请参阅 [Google Sheets](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Create a spreadsheet <a href="#create-a-spreadsheet" id="create-a-spreadsheet"></a>

使用此操作创建新的电子表格。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Document**。
* **Operation**：选择 **Create**。
* **Title**：输入要创建的新电子表格标题。
* **Sheets**：添加要在电子表格中创建的 sheet 的 **Title(s)**。

### Options <a href="#options" id="options"></a>

* **Locale**：输入电子表格的 locale。此设置会影响函数、日期和货币等格式细节。使用以下格式之一：
  * `en` (639-1)
  * `fil`（如果不存在 639-1 格式，则使用 639-2）
  * `en_US`（ISO 语言和国家/地区组合）。
  * 有关语言和国家/地区代码，请参阅 [List of ISO 639 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) 和 [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes)。请注意，Google 不支持所有 locale/语言。
* **Recalculation Interval**：输入电子表格函数所需的重新计算间隔。这会影响 `NOW`、`TODAY`、`RAND` 和 `RANDBETWEEN` 的更新频率。选择 **On Change** 可在电子表格发生更改时重新计算，选择 **Minute** 可每分钟重新计算，选择 **Hour** 可每小时重新计算。有关这些选项的更多信息，请参阅 [Set a spreadsheet’s location & calculation settings](https://support.google.com/docs/answer/58515)。

有关更多信息，请参阅 [Method: spreadsheets.create | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create) API 文档。

## Delete a spreadsheet <a href="#delete-a-spreadsheet" id="delete-a-spreadsheet"></a>

使用此操作删除已有电子表格。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Document**。
* **Operation**：选择 **Delete**。
* **Document**：选择要删除的电子表格。
  * 选择 **From list** 可从下拉列表中选择标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。

有关更多信息，请参阅 [Method: files.delete | Google Drive](https://developers.google.com/drive/api/reference/rest/v2/files/delete) API 文档。

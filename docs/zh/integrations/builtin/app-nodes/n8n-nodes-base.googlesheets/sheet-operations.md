---
title: Google Sheets Sheet Within Document operations
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Google Sheets Sheet Within Document operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations
description: >-
  n8n 中 Google Sheets node 的 Sheet 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Sheet Within Document operations

使用此操作从 Google Sheets 创建、更新、清空或删除 Google 电子表格中的 sheet。有关 Google Sheets node 本身的更多信息，请参阅 [Google Sheets](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Append or Update Row <a href="#append-or-update-row" id="append-or-update-row"></a>

使用此操作更新已有行；如果 sheet 中没有找到匹配条目，则在数据末尾添加新行。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Append or Update Row**。
* **Document**：选择包含要追加或更新行的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要追加或更新行的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 标题。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**：
  * **Map Each Column Manually**：为每一列输入 **Values to Send**。
  * **Map Automatically**：n8n 会自动查找与 Google Sheets 中列匹配的传入数据。在此模式下，请确保传入数据字段与 Google Sheets 中的列相同。（如有需要，请在此 node 之前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md) node 更改它们。）
  * **Nothing**：不映射任何数据。

### Options <a href="#options" id="options"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/5qCFLvqGg2hlBEeEqCwp/" %}

有关更多信息，请参阅 [Method: spreadsheets.values.update | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update) API 文档。

## Append Row <a href="#append-row" id="append-row"></a>

使用此操作在 sheet 数据末尾追加新行。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Append Row**。
* **Document**：选择包含要追加行的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要追加行的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 标题。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**：
  * **Map Each Column Manually**：查找要更新的行时，选择 **Column to Match On**。为每一列输入 **Values to Send**。
  * **Map Automatically**：n8n 会自动查找与 Google Sheets 中列匹配的传入数据。在此模式下，请确保传入数据字段与 Google Sheets 中的列相同。（如有需要，请在此 node 之前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md) node 更改它们。）
  * **Nothing**：不映射任何数据。

### Options <a href="#options" id="options"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/5qCFLvqGg2hlBEeEqCwp/" %}

有关更多信息，请参阅 [Method: spreadsheets.values.append | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/append) API 文档。

## Clear a sheet <a href="#clear-a-sheet" id="clear-a-sheet"></a>

使用此操作清空 sheet 中的所有数据。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Clear**。
* **Document**：选择包含要清空数据的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要清空数据的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 标题。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Clear**：选择要从 sheet 中清空的数据。
  * **Whole Sheet**：清空整个 sheet 的数据。开启 **Keep First Row** 可保留 sheet 的第一行。
  * **Specific Rows**：清空指定行的数据。还需输入：
    * **Start Row Number**：输入要清空的第一行行号。
    * **Number of Rows to Delete**：输入要清空的行数。`1` 只会清空 **Start Row Number** 中的那一行数据。
  * **Specific Columns**：清空指定列的数据。还需输入：
    * **Start Column**：使用字母表示法输入要清空的第一列。
    * **Number of Columns to Delete**：输入要清空的列数。`1` 只会清空 **Start Column** 中的数据。
  * **Specific Range**：使用 [A1 notation](https://developers.google.com/sheets/api/guides/concepts#cell) 输入要清空数据的表格范围。

有关更多信息，请参阅 [Method: spreadsheets.values.clear | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/clear) API 文档。

## Create a new sheet <a href="#create-a-new-sheet" id="create-a-new-sheet"></a>

使用此操作创建新 sheet。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Create**。
* **Document**：选择要在其中创建新 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Title**：输入新 sheet 的标题。

### Options <a href="#options" id="options"></a>

* **Hidden**：开启此选项可在 UI 中隐藏该 sheet。
* **Right To Left**：开启此选项可使用 RTL sheet，而不是 LTR sheet。
* **Sheet ID**：输入 sheet 的 ID。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Sheet Index**：默认情况下，新 sheet 是电子表格中的最后一个 sheet。要覆盖此行为，请输入希望新 sheet 使用的索引。当你在给定索引处添加 sheet 时，Google 会递增后续所有 sheet 的索引。有关更多信息，请参阅 [Sheets | SheetProperties](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets#SheetProperties) 文档。
* **Tab Color**：输入十六进制颜色代码，或使用颜色选择器设置 UI 中标签页的颜色。

有关更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Delete a sheet <a href="#delete-a-sheet" id="delete-a-sheet"></a>

使用此操作永久删除 sheet。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Delete**。
* **Document**：选择包含要删除的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要删除的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 名称。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。

有关更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Delete Rows or Columns <a href="#delete-rows-or-columns" id="delete-rows-or-columns"></a>

使用此操作删除 sheet 中的行或列。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Delete Rows or Columns**。
* **Document**：选择包含要从中删除行或列的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要在其中删除行或列的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 名称。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Start Row Number** 或 **Start Column**：输入开始删除的行号或列字母。
* **Number of Rows to Delete** 或 **Number of Columns to delete**：输入要删除的行数或列数。

有关更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Get Row(s) <a href="#get-rows" id="get-rows"></a>

使用此操作从 sheet 中读取一行或多行。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Get Row(s)**。
* **Document**：选择包含要从中获取行的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要从中读取行的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 名称。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Filters**：默认情况下，node 会返回 sheet 中的所有行。设置 filter 可返回有限的一组结果：
  * **Column**：选择 sheet 中要搜索的列。
  * **Value**：输入要搜索的单元格值。你可以将输入数据参数拖到这里。如果 filter 匹配多行，n8n 会返回第一个结果。如果你想返回所有匹配行：
    1. 在 **Options** 下，选择 **Add Option** > **When Filter Has Multiple Matches**。
    2. 将 **When Filter Has Multiple Matches** 更改为 **Return All Matches**。

### Options <a href="#options" id="options"></a>

* **Data Location on Sheet**：使用此选项指定数据范围。默认情况下，n8n 会自动检测范围，直到 sheet 中的最后一行。
* **Output Formatting**：使用此选项选择 n8n 如何格式化 Google Sheets 返回的数据。
  * **General Formatting**：
    * **Values (unformatted)**（默认）：n8n 会移除货币符号和其他特殊格式。数据类型保持为 number。
    * **Values (formatted)**：n8n 会按 Google Sheets 中显示的样子显示值（例如保留逗号或货币符号），并将数据类型从 number 转换为 string。
    * **Formulas**：n8n 返回公式。它不会计算公式输出。例如，如果单元格 B2 的公式为 `=A2`，n8n 会以文本形式返回 B2 的值 `=A2`。有关更多信息，请参阅 [About date & time values | Google Sheets](https://developers.google.com/sheets/api/guides/formats#about_date_time_values)。
  * **Date Formatting**：有关更多信息，请参阅 [DateTimeRenderOption | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption)。
    * **Formatted Text**（默认）：按 Google Sheets 中显示的样子返回，具体取决于电子表格 locale。例如 `01/01/2024`。
    * **Serial Number**：自 1899 年 12 月 30 日以来的天数。
  * **When Filter Has Multiple Matches**：设置为 **Return All Matches** 可获取多个匹配项。默认只返回第一个结果。

{% hint style="info" %}
**First row**

n8n 会将 Google Sheet 中的第一行视为标题行，读取所有行时不会返回它。如果要读取第一行，请使用 **Options** 设置 **Data Location on Sheet**。
{% endhint %}

有关更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

## Update Row <a href="#update-row" id="update-row"></a>

使用此操作更新 sheet 中的已有行。此操作只更新已有行。如果在 sheet 中没有找到匹配条目时要追加行，请改用 **Append or Update Row** operation。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Google Sheets credentials](../../credentials/google/)。
* **Resource**：选择 **Sheet Within Document**。
* **Operation**：选择 **Update Row**。
* **Document**：选择包含要更新的 sheet 的电子表格。
  * 选择 **From list** 可从下拉列表中选择电子表格标题，选择 **By URL** 可输入电子表格 URL，或选择 **By ID** 输入 `spreadsheetId`。
  * 你可以在 Google Sheets URL 中找到 `spreadsheetId`：`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`。
* **Sheet**：选择要更新的 sheet。
  * 选择 **From list** 可从下拉列表中选择 sheet 标题，选择 **By URL** 可输入 sheet URL，选择 **By ID** 可输入 `sheetId`，或选择 **By Name** 输入 sheet 标题。
  * 你可以在 Google Sheets URL 中找到 `sheetId`：`https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=sheetId`。
* **Mapping Column Mode**：
  * **Map Each Column Manually**：为每一列输入 **Values to Send**。
  * **Map Automatically**：n8n 会自动查找与 Google Sheets 中列匹配的传入数据。在此模式下，请确保传入数据字段与 Google Sheets 中的列相同。（如有需要，请在此 node 之前使用 [Edit Fields](../../core-nodes/n8n-nodes-base.set.md) node 更改它们。）
  * **Nothing**：不映射任何数据。

### Options <a href="#options" id="options"></a>

* **Cell Format**：使用此选项选择如何格式化单元格中的数据。有关更多信息，请参阅 [Google Sheets API | CellFormat](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells#CellFormat)。
  * **Let Google Sheets format**（默认）：n8n 会根据 Google Sheets 的默认设置格式化单元格中的文本和数字。
  * **Let n8n format**：sheet 中的新单元格将具有与 n8n 提供的输入数据相同的数据类型。
* **Data Location on Sheet**：当你需要指定 sheet 上的数据范围位置时，使用此选项。
  * **Header Row**：指定包含列标题的行索引。
  * **First Data Row**：指定实际数据开始的行索引。

有关更多信息，请参阅 [Method: spreadsheets.batchUpdate | Google Sheets](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/batchUpdate) API 文档。

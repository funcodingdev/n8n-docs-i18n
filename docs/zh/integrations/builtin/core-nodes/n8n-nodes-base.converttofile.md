---
title: Convert to File
description: >-
  n8n 中 Convert to File node 的文档。n8n 是一个 workflow 自动化
  平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Convert to File
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.converttofile.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile
layout:
  description:
    visible: false
---

# Convert to File <a href="#convert-to-file" id="convert-to-file"></a>

使用 Convert to File node 可以接收输入数据，并将其作为文件输出。它会把输入的 JSON 数据转换为二进制格式。

{% hint style="info" %}
**Extract From File**

要从文件中提取数据并转换为 JSON，请使用 [Extract from File](n8n-nodes-base.extractfromfile.md) node。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Convert to CSV**](#convert-to-csv)
* [**Convert to HTML**](#convert-to-html)
* [**Convert to ICS**](#convert-to-ics)
* [**Convert to JSON**](#convert-to-json)
* [**Convert to ODS**](#convert-to-ods)
* [**Convert to RTF**](#convert-to-rtf)
* [**Convert to Text File**](#convert-to-text-file)
* [**Convert to XLS**](#convert-to-xls)
* [**Convert to XLSX**](#convert-to-xlsx)
* [**Move Base64 String to File**](#move-base64-string-to-file)

Node 参数和选项取决于你选择的操作。

### Convert to CSV <a href="#convert-to-csv" id="convert-to-csv"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to CSV 选项 <a href="#convert-to-csv-options" id="convert-to-csv-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* 如果文件第一行包含表头名称，请开启 **Header Row** 选项。

### Convert to HTML <a href="#convert-to-html" id="convert-to-html"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to HTML 选项 <a href="#convert-to-html-options" id="convert-to-html-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* 如果文件第一行包含表头名称，请开启 **Header Row** 选项。

### Convert to ICS <a href="#convert-to-ics" id="convert-to-ics"></a>

* **Put Output File in Field**。输入输出数据中用于包含该文件的字段名称。
* **Event Title**：输入事件标题。
* **Start**：输入事件开始的日期和时间。全天事件会忽略时间。
* **End**：输入事件结束的日期和时间。全天事件会忽略时间。如果未设置，该 node 会使用开始日期。
* **All Day**：选择该事件是否为全天事件（开启）或不是全天事件（关闭）。

#### Convert to ICS 选项 <a href="#convert-to-ics-options" id="convert-to-ics-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Attendees**：使用此选项向事件添加参与者。为每个参与者添加：
	* **Name**
	* **Email**
	* **RSVP**：选择参与者是否需要确认出席（开启）或不需要确认（关闭）。
* **Busy Status**：使用此选项为 Outlook 等 Microsoft 应用设置忙碌状态。可选：
	* **Busy**
	* **Tentative**
* **Calendar Name**：对于 Apple 和 Microsoft 日历，请输入该事件的[日历名称](https://learn.microsoft.com/en-us/openspecs/exchange_server_protocols/ms-oxcical/1da58449-b97e-46bd-b018-a1ce576f3e6d)。
*  **Description**：输入事件描述。
* **Geolocation**：输入事件位置的 **Latitude** 和 **Longitude**。
* **Location**：输入事件预期的场地/位置。
* **Recurrence Rule**：输入用于定义事件重复模式的规则（RRULE）。可使用 [iCalendar.org RRULE Tool](https://icalendar.org/rrule-tool.html) 生成规则。
* **Organizer**：输入组织者的 **Name** 和 **Email**。
* **Sequence**：如果你要发送具有相同通用唯一 ID（UID）的事件更新，请输入修订序列号。
* **Status**：设置事件状态。可选：
	* **Confirmed**
	* **Cancelled**
	* **Tentative**
* **UID**：输入事件的通用唯一 ID（UID）。UID 应全局唯一。如果未输入，该 node 会自动生成 UID。
* **URL**：输入与事件关联的 URL。
* **Use Workflow Timezone**：选择使用 UTC 时区（关闭）还是 workflow 的时区（开启）。在 [Workflow Settings](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/configure-workflow-settings) 中设置 workflow 的时区。

### Convert to JSON <a href="#convert-to-json" id="convert-to-json"></a>

根据你的需求，从以下选项中选择最合适的输出 **Mode**：

* **All Items to One File**：将所有输入 item 发送到单个文件。
* **Each Item to Separate File**：为每个输入 item 创建一个文件。

#### Convert to JSON 选项 <a href="#convert-to-json-options" id="convert-to-json-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Format**：选择是否格式化 JSON 以便更易阅读（开启）或不格式化（关闭）。
* **Encoding**：选择用于编码数据的字符集。默认值为 **utf8**。

### Convert to ODS <a href="#convert-to-ods" id="convert-to-ods"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to ODS 选项 <a href="#convert-to-ods-options" id="convert-to-ods-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Compression**：选择是否压缩并减小文件输出大小。
* **Header Row**：如果文件第一行包含表头名称，请开启。
* **Sheet Name**：输入要在电子表格中创建的 Sheet Name。

### Convert to RTF <a href="#convert-to-rtf" id="convert-to-rtf"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to RFT 选项 <a href="#convert-to-rft-options" id="convert-to-rft-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* 如果文件第一行包含表头名称，请开启 **Header Row** 选项。

### Convert to Text File <a href="#convert-to-text-file" id="convert-to-text-file"></a>

输入包含要转换为文件的字符串的 **Text Input Field** 名称。深层字段请使用点表示法，例如 `level1.level2.currentKey`。

#### Convert to Text File 选项 <a href="#convert-to-text-file-options" id="convert-to-text-file-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Encoding**：选择用于编码数据的字符集。默认值为 **utf8**。

### Convert to XLS <a href="#convert-to-xls" id="convert-to-xls"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to XLS 选项 <a href="#convert-to-xls-options" id="convert-to-xls-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Header Row**：如果文件第一行包含表头名称，请开启。
* **Sheet Name**：输入要在电子表格中创建的 Sheet Name。

### Convert to XLSX <a href="#convert-to-xlsx" id="convert-to-xlsx"></a>

使用 **Put Output File in Field** 参数配置该操作。输入输出数据中用于包含该文件的字段名称。

#### Convert to XLSX 选项 <a href="#convert-to-xlsx-options" id="convert-to-xlsx-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **Compression**：选择是否压缩并减小文件输出大小。
* **Header Row**：如果文件第一行包含表头名称，请开启。
* **Sheet Name**：输入要在电子表格中创建的 Sheet Name。

### Move Base64 String to File <a href="#move-base64-string-to-file" id="move-base64-string-to-file"></a>

输入包含要转换为文件的 Base64 字符串的 **Base64 Input Field** 名称。深层字段请使用点表示法，例如 `level1.level2.currentKey`。

#### Move Base64 String to File 选项 <a href="#move-base64-string-to-file-options" id="move-base64-string-to-file-options"></a>

你还可以使用这些 **Options** 配置该操作：

* **File Name**：输入生成的输出文件名称。
* **MIME Type**：输入输出文件的 MIME type。常见 MIME type 及其对应文件扩展名列表请参阅 [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Convert to File 集成模板](https://n8n.io/integrations/convert-to-file)或[搜索所有模板](https://n8n.io/workflows/)

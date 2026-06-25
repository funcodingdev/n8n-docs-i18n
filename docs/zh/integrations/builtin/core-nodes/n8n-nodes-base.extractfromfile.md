---
title: Extract From File
description: >-
  n8n 中 Extract From File node 的文档。n8n 是一个 workflow 自动化
  平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Extract From File
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile
layout:
  description:
    visible: false
---

# Extract From File <a href="#extract-from-file" id="extract-from-file"></a>

n8n workflow 中的常见模式是接收文件，文件可以来自 [HTTP Request node][]（用于从网站获取文件）、[Webhook Node][]（用于从其他位置发送到你的 workflow 的文件），也可以来自本地来源。以这种方式获得的数据通常是二进制格式，例如电子表格或 PDF。

Extract From File node 会从二进制格式文件中提取数据并转换为 JSON，之后 workflow 的其余部分就可以轻松处理这些数据。要将 JSON 转回二进制文件类型，请参阅 [Convert to File](n8n-nodes-base.converttofile.md) node。

## 操作 <a href="#operations" id="operations"></a>

使用 **Operations** 下拉菜单选择要从哪种源文件格式中提取数据。

- **Extract From CSV**："Comma Separated Values" 文件类型常用于表格数据。
- **Extract From HTML**：从标准网页 HTML 格式文件中提取字段。
- **Extract From JSON**：从二进制文件中提取 JSON 数据。
- **Extract From ICS**：从 iCalendar 格式文件中提取字段。
- **Extract From ODS**：从 ODS 电子表格文件中提取字段。
- **Extract From PDF**：从 Portable Document Format 文件中提取字段。
- **Extract From RTF**：从 Rich Text Format 文件中提取字段。
- **Extract From Text File**：从标准文本文件格式中提取字段。
- **Extract From XLS**：从 Microsoft Excel 文件（旧格式）中提取字段。
- **Extract From XLSX**：从 Microsoft Excel 文件中提取字段。
- **Move File to Base64 String**：将二进制数据转换为适合文本处理的 [base64][] 格式。

## 示例 workflow <a href="#example-workflow" id="example-workflow"></a>

在此示例中，Webhook node 用于触发 workflow。当 CSV 文件被发送到 webhook 地址时，文件数据会输出并由 Extract From File node 接收。

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22name%22%3A%20%22Extract%20from%20file%20example%22%2C%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22httpMethod%22%3A%20%22POST%22%2C%0A%20%20%20%20%20%20%20%20%22path%22%3A%20%2206696ea7-9dc7-464a-873b-3feb095b0874%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22rawBody%22%3A%20true%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.webhook%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-380%2C%0A%20%20%20%20%20%20%20%20-80%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22dfbd51af-6050-47c5-a26c-74cba77f65f7%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Webhook%22%2C%0A%20%20%20%20%20%20%22webhookId%22%3A%20%2206696ea7-9dc7-464a-873b-3feb095b0874%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%22headerRow%22%3A%20false%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.extractFromFile%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20-160%2C%0A%20%20%20%20%20%20%20%20-80%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%221b1e4643-8269-402b-83af-dfd90fd6a0b5%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Extract%20from%20File%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22Webhook%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Extract%20from%20File%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22active%22%3A%20true%2C%0A%20%20%22settings%22%3A%20%7B%0A%20%20%20%20%22executionOrder%22%3A%20%22v1%22%0A%20%20%7D%2C%0A%20%20%22versionId%22%3A%20%22dd2bf7f1-692a-41a8-9c2e-7931de57fa13%22%2C%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%221060f46e51fc7902c377ab29d7cbfb87696ddf6b3c5c27cbbb65c3cb36e21baf%22%0A%20%20%7D%2C%0A%20%20%22id%22%3A%20%229i3iDZf5MpjlJ2sh%22%2C%0A%20%20%22tags%22%3A%20%5B%5D%0A%7D" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/core-nodes/n8n-nodes-base.extractfromfile/webhook-example.json" %}

设置为以 'Extract from CSV' 运行后，该 node 会将数据输出为一系列 JSON 'row' 对象：

```
{
  "row": {
  "0": "apple",
  "1": "1",
  "2": "2",
  "3": "3"
  }
  ...
```

{% hint style="info" %}
**使用 webhook 接收文件**

选择 Webhook Node 的 **Add Options** 按钮并选择 **Raw body**，然后启用该设置，让该 node 输出后续 node 期望接收的二进制文件。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Input Binary Field <a href="#input-binary-field" id="input-binary-field"></a>

输入 node 输入数据中包含二进制文件的字段名称。默认值是 'data'。

### Destination Output Field <a href="#destination-output-field" id="destination-output-field"></a>

输入 node 输出中用于包含提取数据的字段名称。

此参数仅适用于以下操作：

- Extract From JSON
- Extract From ICS
- Extract From Text File
- Move File to Base64 String

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Extract From File 集成模板](https://n8n.io/integrations/extract-from-file)或[搜索所有模板](https://n8n.io/workflows/)

[HTTP Request Node]: /integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md
[Webhook Node]: /integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md
[base64]: https://datatracker.ietf.org/doc/html/rfc4648#section-4

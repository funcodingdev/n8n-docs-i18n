---
title: HTML
description: >-
  n8n 中 HTML node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: HTML
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.html.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.html'
layout:
  description:
    visible: false
---

# HTML <a href="#html" id="html"></a>

HTML node 提供一些操作，帮助你在 n8n 中处理 HTML。

{% hint style="info" %}
**HTML Extract node**

从 0.213.0 版本开始，HTML node 取代了 HTML Extract node。如果你使用的是旧版本 n8n，仍然可以查看 [HTML Extract node 文档](https://github.com/n8n-io/n8n-docs/blob/86fe33b681621e618e3adcab9a27e8605dbc23ad/docs/integrations/builtin/core-nodes/n8n-nodes-base.htmlextract.md)。
{% endhint %}
{% hint style="warning" %}
**Cross-site scripting**

使用 HTML node 生成 HTML template 时，可能引入 [XSS（cross-site scripting）](https://owasp.org/www-community/attacks/xss/)。这是一种安全风险。请谨慎处理不可信输入。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Generate HTML template**](#generate-html-template)：使用此操作创建 HTML template。它允许你从 workflow 中获取数据，并将其作为 HTML 输出。
* [**Extract HTML content**](#extract-html-content)：从 HTML 格式来源中提取内容。来源可以是 JSON 或二进制文件（`.html`）。
* [**Convert to HTML Table**](#convert-to-html-table)：将内容转换为 HTML table。

Node 参数和选项取决于你选择的操作。有关配置每个操作的更多详情，请参阅下面各节。

## Generate HTML template <a href="#generate-html-template" id="generate-html-template"></a>

创建 HTML template。它允许你从 workflow 中获取数据，并将其作为 HTML 输出。

你可以包含：

* 标准 HTML
* `<style>` 标签中的 CSS。
* `<script>` 标签中的 JavaScript。n8n 不会执行 JavaScript。
* 用 `{{}}` 包裹的 expression。

你可以在 template 中使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes)，包括 n8n 的[内置方法和变量](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/use-built-in-shortcuts)。

## Extract HTML Content <a href="#extract-html-content" id="extract-html-content"></a>

从 HTML 格式来源中提取内容。来源可以是 JSON 或二进制文件（`.html`）。

使用以下参数：

### Source Data <a href="#source-data" id="source-data"></a>

选择 HTML 内容的来源类型。可选：

* **JSON**：如果选择此 source data，请输入 **JSON Property**：包含要提取 HTML 的输入名称。该属性可以包含字符串或字符串数组。
* **Binary**：如果选择此 source data，请输入 **Input Binary Field**：包含要提取 HTML 的输入名称。该属性可以包含字符串或字符串数组。

### Extraction Values <a href="#extraction-values" id="extraction-values"></a>

- **Key**：输入用于保存提取值的 key。
- **CSS Selector**：输入要搜索的 CSS selector。
- **Return Value**：选择要返回的数据类型。可选：
	- **Attribute**：返回元素上的属性值，例如 `class`。
		- 如果选择此选项，请输入要返回其值的 **Attribute** 名称。
	- **HTML**：返回该元素包含的 HTML。
	- **Text**：返回该元素的文本内容。
		- 如果选择此选项，还可以在 **Skip Selectors** 中输入逗号分隔的 selector 列表，以跳过这些 selector。
	- **Value**：返回 input、select 或 text area 的值。
- **Return Array**：选择将多个提取值作为数组返回（开启），还是作为单个字符串返回（关闭）。

### Extract HTML Content 选项 <a href="#extract-html-content-options" id="extract-html-content-options"></a>

你还可以使用这些选项配置此操作：

* **Trim Values**：控制是否移除值开头和结尾的所有空格与换行（开启），或保留它们（关闭）。
* **Clean Up Text**：控制是否移除前导空白、尾随空白和换行，并将多个连续空白压缩为单个空格（开启），或保持原样（关闭）。

## Convert to HTML Table <a href="#convert-to-html-table" id="convert-to-html-table"></a>

此操作期望接收来自另一个 node 的数据。它没有参数。它包含以下选项：

* **Capitalize Headers**：控制是否将表格 header 首字母大写（开启），或不处理（关闭）。
* **Custom Styling**：控制是否使用自定义样式（开启）或不使用（关闭）。
* **Caption**：输入要添加到表格的 caption。
* **Table Attributes**：输入要应用到 `<table>` 的任何属性，例如 style 属性。
* **Header Attributes**：输入要应用到表格 header `<th>` 的任何属性。
* **Row Attributes**：输入要应用到表格 row `<tr>` 的任何属性。
* **Cell Attributes**：输入要应用到表格 cell `<td>` 的任何属性。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 HTML 集成模板](https://n8n.io/integrations/html)或[搜索所有模板](https://n8n.io/workflows/)

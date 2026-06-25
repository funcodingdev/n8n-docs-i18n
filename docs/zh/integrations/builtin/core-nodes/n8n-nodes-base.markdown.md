---
title: Markdown
description: >-
  n8n 中 Markdown node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Markdown
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.markdown.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.markdown'
layout:
  description:
    visible: false
---

# Markdown <a href="#markdown" id="markdown"></a>

Markdown node 可在 Markdown 和 HTML 格式之间转换。

## 操作 <a href="#operations" id="operations"></a>

此 node 的操作是 **Modes**：

* **Markdown to HTML**：使用此 mode 将 Markdown 转换为 HTML。
* **HTML to Markdown**：使用此 mode 将 HTML 转换为 Markdown。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **HTML** 或 **Markdown**：输入要转换的数据。字段名称会根据你选择的 **Mode** 变化。
* **Destination Key**：输入要放置输出的字段。使用点来指定嵌套字段，例如 `level1.level2.newKey`。

## Node 选项 <a href="#node-options" id="node-options"></a>

Node 的 **Options** 取决于所选 **Mode**。

{% hint style="info" %}
**测试这些选项**

部分选项相互依赖或可能相互影响。建议测试选项，确认效果符合预期。
{% endhint %}

### Markdown to HTML 选项 <a href="#markdown-to-html-options" id="markdown-to-html-options"></a>

| Option | Description | Default |
| ------ | ----------- | ------- |
| **Add Blank To Links** | 是否在新窗口中打开链接（enabled）或不打开（disabled）。 | Disabled |
| **Automatic Linking To URLs** | 是否自动链接 URL（enabled）或不自动链接（disabled）。如果启用，n8n 会将其识别为 URL 的任何字符串转换为链接。 | Disabled |
| **Backslash Escapes HTML Tags** | 是否允许用反斜杠转义 HTML 标签（enabled）或不允许（disabled）。启用后，n8n 会转义前面带有 `\` 的任何 `<` 或 `>`。例如，`\<div\>` 会渲染为 `&lt;div&gt;`。 | Disabled |
| **Complete HTML Document** | 是否输出完整 HTML document（enabled）或 HTML fragment（disabled）。完整 HTML document 包含 `<DOCTYPE HTML>` 声明、`<html>` 和 `<body>` 标签，以及 `<head>` 元素。 | Disabled |
| **Customized Header ID** | 是否支持自定义 heading ID（enabled）或不支持（disabled）。启用后，可以在 heading 文本后使用 `{header ID here}` 添加自定义 heading ID。 | Disabled |
| **Emoji Support** | 是否支持 emoji（enabled）或不支持（disabled）。 | Disabled. |
| **Encode Emails** | 是否将 ASCII 字符 email 转换为等价 decimal entities（enabled）或不转换（disabled）。 | Enabled |
| **Exclude Trailing Punctuation From URLs** | 是否从自动链接的 URL 中排除尾随标点（enabled）或不排除（disabled）。与 **Automatic Linking To URLs** 一起使用。 | Disabled |
| **GitHub Code Blocks** | 是否启用 GitHub Flavored Markdown code block（enabled）或不启用（disabled）。 | Enabled |
| **GitHub Compatible Header IDs** | 是否生成 GitHub Flavored Markdown heading ID（enabled）或不生成（disabled）。GitHub Flavored Markdown 会用 `-` 替换空格，并移除非字母数字字符来生成 heading ID。 | Disabled |
| **GitHub Mention Link** | 更改与 **GitHub Mentions** 一起使用的链接。 | Disabled |
| **GitHub Mentions** | 是否支持用 `@` 标记 GitHub 用户（enabled）或不支持（disabled）。启用后，n8n 会将 `@name` 替换为 `https://github.com/name`。 | Disabled |
| **GitHub Task Lists** | 是否支持 GitHub Flavored Markdown task list（enabled）或不支持（disabled）。 | Disabled |
| **Header Level Start** | 数字。设置 header 的起始级别。例如，将此字段改为 `2` 会让 n8n 将 `#` 视为 `<h2>`，将 `##` 视为 `<h3>`，以此类推。 | 1 |
| **Mandatory Space Before Header** | 是否要求 `#` 与 heading 文本之间必须有空格（enabled）或不要求（disabled）。启用后，n8n 会按字面渲染写作 `##Some header text` 的 heading，而不会将其转换为 heading 元素。 | Disabled |
| **Middle Word Asterisks** | n8n 是否应将单词中的星号视为 Markdown（disabled），或将其渲染为字面星号（enabled）。 | Disabled |
| **Middle Word Underscores** | n8n 是否应将单词中的下划线视为 Markdown（disabled），或将其渲染为字面下划线（enabled）。 | Disabled |
| **No Header ID** | 禁用自动生成 header ID（enabled）。 | Disabled |
| **Parse Image Dimensions** | 支持在 Markdown 语法中设置最大图片尺寸（enabled）。 | Disabled |
| **Prefix Header ID** | 定义要添加到 header ID 的前缀。 | None |
| **Raw Header ID** | 是否从 header ID（包括前缀）中移除空格、`'` 和 `"`，并用 `-` 替换它们（enabled）或不处理（disabled）。 | Disabled |
| **Raw Prefix Header ID** | 是否阻止 n8n 修改 header 前缀（enabled）或不阻止（disabled）。 | Disabled |
| **Simple Line Breaks** | 是否在行末没有两个空格时也创建换行（enabled）或不创建（disabled）。 | Disabled |
| **Smart Indentation Fix** | 是否尝试智能修复与缩进 code block 中 ES6 template string 相关的缩进问题（enabled）或不修复（disabled）。 | Disabled |
| **Spaces Indented Sublists** | 是否移除子列表必须缩进四个空格的要求（enabled）或不移除（disabled）。 | Disabled |
| **Split Adjacent Blockquotes** | 是否拆分相邻 blockquote block（enabled）或不拆分（disabled）。如果不启用，n8n 会将单独行上以 `>` 开头的 quote 视为一个 blockquote，即使中间有空行分隔。 | Disabled |
| **Strikethrough** | 是否支持删除线语法（enabled）或不支持（disabled）。启用后，可以使用包围单词或短语的 `~~` 添加 ~~strikethrough~~ 效果。 | Disabled |
| **Tables Header ID** | 是否向 table header 标签添加 ID（enabled）或不添加（disabled）。 | Disabled |
| **Tables Support** | 是否支持 table（enabled）或不支持（disabled）。 | Disabled |

### HTML to Markdown 选项 <a href="#html-to-markdown-options" id="html-to-markdown-options"></a>

| Option | Description | Default |
| ------ | ----------- | ------- |
| **Bullet Marker** | 指定用于 unordered list 的字符。 | * |
| **Code Block Fence** | 指定用于 code block 的字符。 | ``` |
| **Emphasis Delimiter** | 指定 `<em>` 字符。 | _ |
| **Global Escape Pattern** | 覆盖默认字符转义设置。你可能应改用 Text Replacement Pattern。 | None |
| **Ignored Elements** | 忽略给定 HTML 元素及其子元素。 | None |
| **Keep Images With Data** | 是否保留带 data 的图片（enabled）或不保留（disabled）。支持最大 1MB 的文件。 | Disabled |
| **Line Start Escape Pattern** | 覆盖默认字符转义设置。你可能应改用 Text Replacement Pattern。 | None |
| **Max Consecutive New Lines** | 数字。指定允许的最大连续新行数。 | 3 |
| **Place URLs At The Bottom** | 是否将 URL 放在页面底部，并使用 link reference definition 格式化（enabled）或不这样做（disabled）。 | Disabled |
| **Strong Delimiter** | 指定 `<strong>` 的字符。 | ** |
| **Style For Code Block** | 指定 code block 的样式。选项为 **Fence** 和 **Indented**。 | Fence |
| **Text Replacement Pattern** | 使用 regex 定义文本替换 pattern。 | None |
| **Treat As Blocks** | 指定要作为 block 处理的 HTML 元素（前后加空行）。 | None |

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Markdown 集成模板](https://n8n.io/integrations/markdown)或[搜索所有模板](https://n8n.io/workflows/)

## Parser <a href="#parsers" id="parsers"></a>

n8n 使用以下 parser：

* 从 HTML 转换为 Markdown：[node-html-markdown](https://www.npmjs.com/package/node-html-markdown)。
* 从 Markdown 转换为 HTML：[Showdown](https://www.npmjs.com/package/showdown)。某些选项允许你使用 [GitHub Flavored Markdown](https://github.github.com/gfm/) 扩展 Markdown。

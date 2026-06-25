---
title: XML
description: >-
  n8n 中 XML node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: XML
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.xml.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.xml'
layout:
  description:
    visible: false
---

# XML <a href="#xml" id="xml"></a>

使用 XML node 在 XML 与其他数据之间进行转换。

{% hint style="info" %}
**二进制文件**

如果 XML 位于二进制文件中，请先使用 [Extract from File](n8n-nodes-base.extractfromfile.md) node 将其转换为文本。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

- **Mode**：数据应从哪种格式转换，以及转换为哪种格式。
	- **JSON to XML**：将数据从 JSON 转换为 XML。
    - **XML to JSON**：将数据从 XML 转换为 JSON。
- **Property Name**：输入包含要转换数据的属性名称。

## Node 选项 <a href="#node-options" id="node-options"></a>

无论选择哪种 **Mode**，以下选项都可用：

- **Attribute Key**：输入用于访问 attribute 的前缀。默认值为 `$`。
- **Character Key**：输入用于访问字符内容的前缀。默认值为 `_`。

所有其他选项取决于所选 **Mode**。

### JSON to XML 选项 <a href="#json-to-xml-options" id="json-to-xml-options"></a>

只有当你选择 **JSON to XML** 作为 **Mode** 时，才会显示这些选项：

- **Allow Surrogate Chars**：设置是否允许使用 Unicode surrogate blocks 中的字符（开启），或不允许（关闭）。
- **Cdata**：设置是否在需要时将文本 node 包裹在 `<![CDATA[ ... ]]>` 中而不是转义（开启），或不这样做（关闭）。
    * 开启此选项不会在不需要时添加 `<![CDATA[ ... ]]>`。
- **Headless**：设置是否省略 XML header（开启），或包含它（关闭）。
- **Root Name**：输入要使用的根元素名称。

### XML to JSON 选项 <a href="#xml-to-json-options" id="xml-to-json-options"></a>

只有当你选择 **XML to JSON** 作为 **Mode** 时，才会显示这些选项：

- **Explicit Array**：设置是否将子 node 放入数组（开启），或仅在有多个子 node 时创建数组（关闭）。
- **Explicit Root**：设置是否在结果对象中获取根 node（开启），或不获取（关闭）。
- **Ignore Attributes**：设置是否忽略所有 XML attribute 并只创建文本 node（开启），或不忽略（关闭）。
- **Merge Attributes**：设置是否将 attribute 和子元素合并为父级属性（开启），或将 attribute 作为子 attribute 对象的 key（关闭）。如果 **Ignore Attribute** 已开启，此选项会被忽略。
- **Normalize**：设置是否修剪文本 node 内部的空白（开启），或不修剪（关闭）。
- **Normalize Tags**：设置是否将所有标签名称标准化为小写（开启），或保持标签名称原样（关闭）。
- **Trim**：设置是否修剪文本 node 开头和结尾的空白（开启），或保留空白原样（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 XML 集成模板](https://n8n.io/integrations/xml)或[搜索所有模板](https://n8n.io/workflows/)

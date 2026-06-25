---
title: Information Extractor node 文档
description: >-
  了解如何在 n8n 中使用 Information Extractor node。按照技术文档将
  Information Extractor node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Information Extractor node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor
layout:
  description:
    visible: false
---

# Information Extractor node <a href="#information-extractor-node" id="information-extractor-node"></a>

使用 Information Extractor node 从传入数据中提取结构化信息。

在本页中，你可以找到 Information Extractor node 的 node 参数，以及更多相关资源链接。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text** 定义要从中提取信息的输入文本。这通常是引用输入 items 中某个字段的 expression。例如，如果输入来自 chat trigger，可以是 `{{ $json.chatInput }}`；如果前一个 node 是 Extract from PDF，可以是 `{{ $json.text }}`。
* 使用 **Schema Type** 选择你希望如何描述期望的输出数据格式。你可以选择：
    * **From Attribute Descriptions**：此选项允许你通过指定属性列表及其描述来定义 schema。
    * **Generate From JSON Example**：输入一个 JSON object 示例以自动生成 schema。node 使用 object property 的类型和名称，并忽略实际值。n8n 从 JSON 示例生成 schemas 时，会将每个字段都视为必填。
    * **Define using JSON Schema**：手动输入 JSON schema。如需创建有效 JSON schema 的帮助，请阅读 JSON Schema [指南和示例](https://json-schema.org/learn/miscellaneous-examples)。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **System Prompt Template**：使用此选项更改信息提取所使用的 system prompt。n8n 会自动向 prompt 追加格式规范说明。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

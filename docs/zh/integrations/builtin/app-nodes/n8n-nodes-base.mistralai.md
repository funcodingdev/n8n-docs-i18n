---
title: MistralAI node documentation
description: >-
  了解如何在 n8n 中使用 Mistral AI node。按照技术文档将 Mistral AI node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
nodeTitle: MistralAI node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mistralai.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mistralai'
layout:
  description:
    visible: false
---

# Mistral AI node <a href="#mistral-ai-node" id="mistral-ai-node"></a>

使用 Mistral AI node 自动化 Mistral AI 中的工作，并将 Mistral AI 与其他应用集成。n8n 内置支持使用多种模型、文件类型和输入方式提取文本。

在本页中，你可以找到 Mistral AI node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/mistral.md)找到此 node 的身份验证信息。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Resource**：Mistral AI 要操作的资源。当前实现支持 "Document" 资源。
* **Operation**：要执行的操作：
    * **Extract Text**：使用光学字符识别（OCR）从文档或图像中提取文本。
* **Model**：给定操作要使用的模型。当前版本要求使用 `mistral-ocr-latest` 模型。
* **Document Type**：要处理的文档格式。可以是 "Document" 或 "Image"。
* **Input Type**：文档的输入方式：
    * **Binary Data**：以二进制字段形式将文档传给此 node。
    * **URL**：从给定 URL 获取文档。
* **Input Binary Field**：使用 "Binary Data" 输入类型时，定义包含文件的输入二进制字段名称。
* **URL**：使用 "URL" 输入类型时，要处理的文档或图像的 URL。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Enable Batch Processing**：是否在同一个 API 调用中处理多个文档。通过合并请求，这可能会降低成本。
* **Batch Size**：使用 "Enable Batch Processing" 时，设置每批要处理的最大文档数。
* **Delete Files After Processing**：使用 "Enable Batch Processing" 时，是否在处理完成后从 Mistral Cloud 删除文件。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 MistralAI node 文档集成模板](https://n8n.io/integrations/mistral-ai)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Mistral AI 文档](https://docs.mistral.ai/api/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

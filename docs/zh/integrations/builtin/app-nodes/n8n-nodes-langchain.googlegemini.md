---
title: Google Gemini node 文档
description: >-
  了解如何在 n8n 中使用 Google Gemini node。按照技术文档将 Google Gemini node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Google Gemini node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.googlegemini
layout:
  description:
    visible: false
---

# Google Gemini node <a href="#google-gemini-node" id="google-gemini-node"></a>

使用 Google Gemini node 自动化 Google Gemini 中的工作，并将 Google Gemini 与其他应用集成。n8n 内置支持大量 Google Gemini 功能，包括处理音频、视频、图片、文档和文件，用于分析、生成和转写。

在本页中，你可以找到 Google Gemini node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/googleai.md)找到此 node 的身份验证信息。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* 音频：
	* 分析音频：接收音频并回答有关音频的问题。
	* 转写录音：将音频转写为文本。
* 文档：
	* 分析文档：接收文档并回答有关文档的问题。
* 文件搜索：
	* 创建文件搜索存储：为 RAG（Retrieval Augmented Generation）创建新的文件搜索存储
	* 删除文件搜索存储：删除文件搜索存储
	* 列出文件搜索存储：列出用户拥有的所有文件搜索存储
	* 上传到文件搜索存储：将文件上传到用于 RAG（Retrieval Augmented Generation）的文件搜索存储
* 图片：
	* 分析图片：接收图片并回答有关图片的问题。
	* 生成图片：根据文本 prompt 创建图片。
	* 编辑图片：上传一张或多张图片，并基于 prompt 应用编辑
* 媒体文件：
	* 上传媒体文件：将文件上传到 Google Gemini API，供之后使用。
* 文本：
	* 向模型发送消息：使用 Google Gemini 模型创建补全。
* 视频：
	* 分析视频：接收视频并回答有关视频的问题。
	* 生成视频：根据文本 prompt 创建视频。
	* 下载视频：使用 URL 从 Google Gemini API 下载生成的视频。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Google Gemini node 文档集成模板](https://n8n.io/integrations/google-gemini)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>


有关此服务的更多信息，请参阅 [Google Gemini 的文档](https://ai.google.dev/gemini-api/docs)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

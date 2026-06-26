---
title: OpenAI File operations
description: >-
  n8n 中 OpenAI node 的 File 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI File operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations
layout:
  description:
    visible: false
---

# OpenAI File operations <a href="#openai-file-operations" id="openai-file-operations"></a>

使用此操作在 OpenAI 中创建、删除、列出、发送消息或更新 file。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

## Delete a File <a href="#delete-a-file" id="delete-a-file"></a>

使用此操作从服务器删除 file。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Delete a File**。
- **File**：输入此操作要使用的 file ID，或从下拉列表中选择 file name。

有关更多信息，请参阅 [Delete file | OpenAI](https://platform.openai.com/docs/api-reference/files/delete) 文档。

## List Files <a href="#list-files" id="list-files"></a>

使用此操作列出属于用户 organization 的 file。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **List Files**。

### Options <a href="#options" id="options"></a>

- **Purpose**：使用此选项只返回具有给定 purpose 的 file。使用 **Assistants** 只返回与 Assistants 和 Message operations 相关的 file。使用 **Fine-Tune** 返回与 [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning) 相关的 file。

有关更多信息，请参阅 [List files | OpenAI](https://platform.openai.com/docs/api-reference/files/list) 文档。

## Upload a File <a href="#upload-a-file" id="upload-a-file"></a>

使用此操作上传 file。它可用于多种操作。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **File**。
- **Operation**：选择 **Upload a File**。
- **Input Data Field Name**：默认为 `data`。输入包含 file 的 binary property 名称。单个 file 最大可为 512 MB，或 Assistants 使用时最多 200 万 token。

### Options <a href="#options" id="options"></a>

- **Purpose**：输入上传 file 的预期 purpose。对与 Assistants 和 Message operations 关联的 file 使用 **Assistants**。对 [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning) 使用 **Fine-Tune**。

有关更多信息，请参阅 [Upload file | OpenAI](https://platform.openai.com/docs/api-reference/files/create) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

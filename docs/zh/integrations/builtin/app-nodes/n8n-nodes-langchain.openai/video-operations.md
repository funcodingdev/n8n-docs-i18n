---
title: OpenAI Video operations
description: >-
  n8n 中 OpenAI node 的 Video 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Video operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations
layout:
  description:
    visible: false
---

# OpenAI Video operations <a href="#openai-video-operations" id="openai-video-operations"></a>

使用此操作在 OpenAI 中生成 video。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

## Generate Video <a href="#generate-video" id="generate-video"></a>

使用此操作根据文本 prompt 生成 video。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Video**。
- **Operation**：选择 **Generate Video**。
- **Model**：选择要用于生成 video 的 model。目前支持 `sora-2` 和 `sora-2-pro`。
- **Prompt**：用于生成 video 的 prompt。
- **Seconds**：clip 时长，单位为秒（最多 25 秒）。
- **Size**：输出分辨率，格式为 width x height。1024x1792 和 1792x1024 仅受 Sora 2 Pro 支持。

### Options <a href="#options" id="options"></a>

- **Reference**：用于指导生成的可选 image reference。必须以 binary item 传入。
- **Wait Timeout**：等待 video 生成的时间，单位为秒。默认为 300。
- **Output Field Name**：用于放置二进制文件数据的输出字段名称。默认为 `data`。

有关更多信息，请参阅 [Video Generation | OpenAI](https://platform.openai.com/docs/guides/video-generation)。

---
title: OpenAI Image operations
description: >-
  n8n 中 OpenAI node 的 Image 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Image operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations
layout:
  description:
    visible: false
---

# OpenAI Image operations <a href="#openai-image-operations" id="openai-image-operations"></a>

使用此操作在 OpenAI 中分析或生成 image。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

## Analyze Image <a href="#analyze-image" id="analyze-image"></a>

使用此操作接收 image 并回答有关它们的问题。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Image**。
- **Operation**：选择 **Analayze Image**。
- **Model**：选择要用于分析 image 的 model。
- **Text Input**：询问有关 image 的问题。
- **Input Type**：选择希望如何输入 image。选项包括：
    - **Image URL(s)**：输入要分析的 image 的 **URL(s)**。可用逗号分隔列表添加多个 URL。
    - **Binary File(s)**：在 **Input Data Field Name** 中输入包含 image 的 binary property 名称。

### Options <a href="#options" id="options"></a>

- **Detail**：指定 response time 与 token usage 之间的平衡。
- **Length of Description (Max Tokens)**：默认为 300。更少 token 会产生更短、细节更少的 image 描述。

有关更多信息，请参阅 [Images | OpenAI](https://platform.openai.com/docs/api-reference/images) 文档。

## Generate an Image <a href="#generate-an-image" id="generate-an-image"></a>

使用此操作根据文本 prompt 创建 image。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Image**。
- **Operation**：选择 **Generate an Image**。
- **Model**：选择要用于生成 image 的 model。
- **Prompt**：输入所需 image 的文本描述。`dall-e-2` 的最大长度为 1000 个字符，`dall-e-3` 的最大长度为 4000 个字符。

### Options <a href="#options" id="options"></a>

- **Quality**：生成 image 的质量。**HD** 会创建细节更精细且整体一致性更高的 image。此选项仅支持 `dall-e-3`。否则请选择 **Standard**。
- **Resolution**：选择生成 image 的分辨率。对 `dall-e-2` 选择 **1024x1024**。对 `dall-e-3` model 选择 **1024x1024**、**1792x1024** 或 **1024x1792** 之一。
- **Style**：选择生成 image 的风格。此选项仅支持 `dall-e-3`。
    - **Natural**：用于生成更自然的 image。
    - **Vivid**：用于生成 hyper-real 和 dramatic image。
- **Respond with image URL(s)**：是否返回 image URL(s)，而不是 binary file(s)。
- **Put Output in Field**：默认为 `data`。输入用于放置二进制文件数据的输出字段名称。仅在关闭 **Respond with image URL(s)** 时可用。

有关更多信息，请参阅 [Create image | OpenAI](https://platform.openai.com/docs/api-reference/images/create) 文档。

## Edit an Image <a href="#edit-an-image" id="edit-an-image"></a>

使用此操作根据文本 prompt 编辑 image。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Image**。
- **Operation**：选择 **Edit Image**。
- **Model**：选择要用于生成 image 的 model。支持 `dall-e-2` 和 `gpt-image-1`。
- **Prompt**：输入对输入 image 进行所需编辑的文本描述。
- **Image(s)**：添加一个或多个 binary field，用于将 image 与 prompt 一起提供。每个 image 应为小于 50MB 的 png、webp 或 jpg 文件。最多可提供 16 张 image。
- **Number of Images**：要生成的 image 数量。必须介于 1 到 10 之间。
- **Size**：生成 image 的大小和尺寸（px）。
- **Quality**：将生成 image 的质量（auto、low、medium、high、standard）。仅支持 `gpt-image-1`。
- **Output Format**：返回生成 image 的格式（png、webp 或 jpg）。仅支持 gpt-image-1。
- **Output Compression**：生成 image 的压缩级别（0-100%）。仅支持 `gpt-image-1` 的 webp 或 jpeg 输出格式。

### Options <a href="#options" id="options"></a>
- **Background**：允许设置生成 image 的背景透明度。仅支持 `gpt-image-1`。
- **Input Fidelity**：控制 model 为匹配输入 image 的风格和特征所投入的 effort。仅支持 `gpt-image-1`。
- **Image Mask**：包含 image 的 binary property 名称。第二张 image 的完全透明区域（例如 alpha 为零的位置）会显示应编辑 image 的位置。如果提供了多张 image，mask 会应用到第一张 image 上。必须是有效 PNG 文件，小于 4MB，并且尺寸与 image 相同。
- **User**：代表最终用户的唯一标识符，可帮助 OpenAI 监控和检测滥用。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

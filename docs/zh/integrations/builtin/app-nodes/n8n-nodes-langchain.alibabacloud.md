---
title: Alibaba Cloud Model Studio node 文档
contentType:
  - integration
  - reference
nodeTitle: Alibaba Cloud Model Studio node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.alibabacloud
description: >-
  通过 Model Studio 与 Alibaba Cloud Qwen 模型交互。本页说明如何在 n8n workflow 中使用此 node
  生成文本补全、分析或生成图片，以及根据文本创建视频
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Alibaba Cloud Model Studio

Alibaba Cloud Model Studio node 允许你从 n8n 调用 Alibaba Cloud Qwen 模型（文本、视觉和媒体模型）。可用它生成补全、分析或创建图片，以及从文本或图片生成短视频。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/alibaba.md)找到此 node 的身份验证信息。
{% endhint %}

## 资源和操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

* **Text**：向模型发送消息，创建文本补全和类似 agent 的响应。
* **Image**：使用视觉语言模型分析图片，或根据 prompt 生成图片。
* **Video**：从文本或一张/多张图片生成短视频。

### 向模型发送消息 <a href="#message-a-model" id="message-a-model"></a>

使用 Qwen 模型创建补全。

**参数**

* **Model**（类型：options，字段：`modelId`）：用于生成的模型（例如 Qwen3.5 Flash、Qwen3 Max）。
* **Messages**（类型：fixedCollection，字段：`messages`）：组成对话的一条或多条消息。
  * 消息值：
    * **Content**（类型：string，字段：`content`）：消息内容。
    * **Role**（类型：options，字段：`role`）：消息发送者的角色（User 或 Assistant）。
* **Simplify Output**（类型：boolean，字段：`simplify`）：返回简化版响应，而不是完整的原始 API 输出。

**选项**

* **Enable Search**（类型：boolean，字段：`enableSearch`）：启用网页搜索以获取最新信息。
* **Max Tokens**（类型：number，字段：`maxTokens`）：要生成的最大 token 数。
* **Max Tools Iterations**（类型：number，字段：`maxToolsIterations`）：停止前允许的最大 tool 调用迭代次数。设为 0 表示不限制。
* **Repetition Penalty**（类型：number，字段：`repetitionPenalty`）：token 重复惩罚。值越高，重复越少。
* **Seed**（类型：number，字段：`seed`）：用于可复现输出的随机种子。
* **Stop Sequences**（类型：string，字段：`stop`）：以逗号分隔的序列列表，API 遇到这些序列时会停止生成。
* **System Message**（类型：string，字段：`system`）：给模型的系统指令。
* **Temperature**（类型：number，字段：`temperature`）：控制随机性。值越低，输出越确定。
* **Top K**（类型：number，字段：`topK`）：将采样池限制为 top K 个 token。
* **Top P**（类型：number，字段：`topP`）：核采样参数。

### 分析图片 <a href="#analyze-image" id="analyze-image"></a>

以图片作为输入，并向视觉语言模型提问。

**参数**

* **Model**（类型：options，字段：`modelId`）：要使用的视觉语言模型（例如 Qwen-VL Flash）。
* **Input Type**（类型：options，字段：`inputType`）：提供图片的方式（URL 或二进制数据）。
* **Image URL**（类型：string，字段：`imageUrl`）：要分析的图片 URL（使用 URL 输入时必填）。
* **Input Data Field Name**（类型：string，字段：`binaryPropertyName`）：使用二进制输入时，从中读取图片的二进制字段名。
* **Question**（类型：string，字段：`question`）：关于图片的问题或指令。
* **Simplify Output**（类型：boolean，字段：`simplify`）：返回简化版响应。

**选项**

* **Temperature**（类型：number，字段：`temperature`）：控制视觉模型的随机性。
* **Max Tokens**（类型：number，字段：`maxTokens`）：视觉模型输出的最大 token 数。

### 生成图片 <a href="#generate-an-image" id="generate-an-image"></a>

根据文本 prompt 创建图片。

**参数**

* **Model**（类型：options，字段：`modelId`）：要使用的图片生成模型（例如 Z-Image Turbo）。
* **Prompt**（类型：string，字段：`prompt`）：描述要生成图片的文本 prompt。
* **Download Image**（类型：boolean，字段：`downloadImage`）：为 true 时，将生成的图片下载为二进制数据；否则只返回 URL。

**选项**

* **Size**（类型：options，字段：`size`）：生成图片的尺寸（例如 102&#x34;_&#x31;024、166&#x34;_&#x39;28）。
* **Prompt Extend**（类型：boolean，字段：`promptExtend`）：自动扩展并增强 prompt。

### 从文本生成视频 <a href="#generate-video-from-text" id="generate-video-from-text"></a>

根据文本 prompt 生成短视频。

**参数**

* **Model**（类型：options，字段：`modelId`）：要使用的 text-to-video 模型（例如 Wan 2.6 Text-to-Video）。
* **Prompt**（类型：string，字段：`prompt`）：用于生成视频的文本 prompt。
* **Resolution**（类型：options，字段：`resolution`）：分辨率档位（720P 或 1080P）。
* **Duration (Seconds)**（类型：number，字段：`duration`）：生成视频的时长，单位秒（2-15）。
* **Shot Type**（类型：options，字段：`shotType`）：Single 或 Multi（多镜头叙事）。
* **Download Video**（类型：boolean，字段：`downloadVideo`）：为 true 时，将生成的视频下载为二进制数据；否则只返回 URL。
* **Simplify Output**（类型：boolean，字段：`simplify`）：返回简化版响应。

**选项**

* **Prompt Extend**（类型：boolean，字段：`promptExtend`）：自动扩展并增强 prompt。
* **Audio**（类型：boolean，字段：`audio`）：是否为视频生成音频。
* **Audio Input Type**（类型：options，字段：`audioInputType`）：启用 **Audio** 选项时必须指定。它定义如何提供音频：通过音频 URL 或二进制文件。
* **Audio URL**（类型：string，字段：`audioUrl`）：当 **Audio Input Type** 设置为 URL 时必须指定。定义要使用的音频文件 URL。
* **Audio Data Field Name**（类型：string，字段：`audioBinaryPropertyName`）：当 **Audio Input Type** 设置为 **Binary File** 时必须指定。定义音频输入的二进制字段名。

### 从图片生成视频 <a href="#generate-video-from-image" id="generate-video-from-image"></a>

使用 Wan 模型从一张或多张图片生成视频。

**参数**

* **Model**（类型：options，字段：`modelId`）：要使用的 image-to-video 模型（例如 Wan 2.6 Image-to-Video Flash）。
* **Input Type**（类型：options，字段：`inputType`）：定义如何提供图片：通过图片 URL 或二进制文件。
* **Image URL**（类型：string，字段：`imgUrl`）：用于生成视频的首帧图片 URL。
* **Input Data Field Name**（类型：string，字段：`binaryPropertyName`）：使用二进制输入时，从中读取图片的二进制字段名。
* **Prompt**（类型：string，字段：`prompt`）：可选文本，用于描述期望的内容和视觉特征。
* **Resolution**（类型：options，字段：`resolution`）：分辨率档位（720P 或 1080P）。
* **Duration (Seconds)**（类型：number，字段：`duration`）：时长，单位秒（2-15）。
* **Shot Type**（类型：options，字段：`shotType`）：Single 或多镜头叙事。
* **Download Video**（类型：boolean，字段：`downloadVideo`）：为 true 时，将生成的视频下载为二进制数据；否则只返回 URL。
* **Simplify Output**（类型：boolean，字段：`simplify`）：返回简化版响应。

**选项**

* **Prompt Extend**（类型：boolean，字段：`promptExtend`）：自动扩展并增强 prompt。
* **Audio**（类型：boolean，字段：`audio`）：是否为视频生成音频。
* **Audio Input Type**（类型：options，字段：`audioInputType`）：定义如何提供音频：通过音频 URL 或二进制文件。
* **Audio URL**（类型：string，字段：`audioUrl`）：当 **Audio Input Type** 设置为 URL 时，要使用的音频文件 URL。
* **Audio Data Field Name**（类型：string，字段：`audioBinaryPropertyName`）：当 **Audio Input Type** 设置为二进制数据时，音频输入的二进制字段名。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Alibaba Cloud Model Studio node 文档集成模板](https://n8n.io/integrations/alibaba-cloud-model-studio)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关可用模型和 API 行为的更多信息，请参阅 [Alibaba Cloud Model Studio 文档](https://www.alibabacloud.com/product/qwen)。

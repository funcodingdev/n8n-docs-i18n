---
title: OpenAI Audio operations
description: >-
  n8n 中 OpenAI node 的 Audio 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Audio operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations
layout:
  description:
    visible: false
---

# OpenAI Audio operations <a href="#openai-audio-operations" id="openai-audio-operations"></a>

使用此操作在 OpenAI 中生成 audio，或转录、翻译录音。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

## Generate Audio <a href="#generate-audio" id="generate-audio"></a>

使用此操作根据文本 prompt 创建 audio。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Audio**。
- **Operation**：选择 **Generate Audio**。
- **Model**：选择用于生成 audio 的 model。更多信息请参阅 [TTS | OpenAI](https://platform.openai.com/docs/models/tts)。
    - **TTS-1**：用于优化速度。
    - **TTS-1-HD**：用于优化质量。
- **Text Input**：输入要为其生成 audio 的文本。最大长度为 4096 个字符。
- **Voice**：选择生成 audio 时使用的 voice。可在 [Text to speech guide | OpenAI](https://platform.openai.com/docs/guides/text-to-speech/quickstart) 中收听 voice 预览。

### Options <a href="#options" id="options"></a>

- **Response Format**：选择 audio response 的格式。可从 **MP3**（默认）、**OPUS**、**AAC**、**FLAC**、**WAV** 和 **PCM** 中选择。
- **Audio Speed**：输入生成 audio 的速度，取值范围为 `0.25` 到 `4.0`。默认为 `1`。
- **Put Output in Field**：默认为 `data`。输入用于放置二进制文件数据的输出字段名称。

有关更多信息，请参阅 [Create speech | OpenAI](https://platform.openai.com/docs/api-reference/audio/createSpeech) 文档。

## Transcribe a Recording <a href="#transcribe-a-recording" id="transcribe-a-recording"></a>

使用此操作将 audio 转录为文本。OpenAI API 将 audio 文件大小限制为 25 MB。OpenAI 默认使用 `whisper-1` model。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Audio**。
- **Operation**：选择 **Transcribe a Recording**。
- **Input Data Field Name**：默认为 `data`。输入包含 audio 文件的 binary property 名称，文件格式可以是 `.flac`、`.mp3`、`.mp4`、`.mpeg`、`.mpga`、`.m4a`、`.ogg`、`.wav` 或 `.webm`。

### Options <a href="#options" id="options"></a>

- **Language of the Audio File**：输入输入 audio 的语言，使用 [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)。使用此选项可提高准确性并降低延迟。
- **Output Randomness (Temperature)**：默认为 `1.0`。调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 0.7）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。

有关更多信息，请参阅 [Create transcription | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription) 文档。

## Translate a Recording <a href="#translate-a-recording" id="translate-a-recording"></a>

使用此操作将 audio 翻译为英文。OpenAI API 将 audio 文件大小限制为 25 MB。OpenAI 默认使用 `whisper-1` model。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Audio**。
- **Operation**：选择 **Translate a Recording**。
- **Input Data Field Name**：默认为 `data`。输入包含 audio 文件的 binary property 名称，文件格式可以是 `.flac`、`.mp3`、`.mp4`、`.mpeg`、`.mpga`、`.m4a`、`.ogg`、`.wav` 或 `.webm`。

### Options <a href="#options" id="options"></a>

- **Output Randomness (Temperature)**：默认为 `1.0`。调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 0.7）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。

有关更多信息，请参阅 [Create transcription | OpenAI](https://platform.openai.com/docs/api-reference/audio/createTranscription) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

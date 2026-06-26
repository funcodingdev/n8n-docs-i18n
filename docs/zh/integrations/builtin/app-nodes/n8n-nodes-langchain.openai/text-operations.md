---
title: OpenAI Text operations
description: >-
  n8n 中 OpenAI node 的 Text 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Text operations
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations
layout:
  description:
    visible: false
---

# OpenAI Text operations <a href="#openai-text-operations" id="openai-text-operations"></a>

使用此操作在 OpenAI 中向 model 发送消息，或对文本进行违规分类。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

{% hint style="info" %}
**以前的 node 版本**

n8n 1.117.0 引入支持 OpenAI Responses API 的 OpenAI node V2。它将 'Message a Model' operation 重命名为 'Generate a Chat Completion'，以明确其与 Chat Completions API 的关联，并引入一个单独使用 Responses API 的 'Generate a Model Response' operation。
{% endhint %}

## Generate a Chat Completion <a href="#generate-a-chat-completion" id="generate-a-chat-completion"></a>

使用此操作通过 Chat Completions API 向 OpenAI model 发送 message 或 prompt，并接收 response。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Text**。
- **Operation**：选择 **Generate a Chat Completion**。
- **Model**：选择要使用的 model。如果不确定使用哪个 model，需要高智能时可尝试 `gpt-4o`，需要最快速度和最低成本时可尝试 `gpt-4o-mini`。有关更多信息，请参阅 [Models overview | OpenAI Platform](https://platform.openai.com/docs/models)。
- **Messages**：输入 **Text** prompt，并分配 model 用于生成 response 的 **Role**。有关如何使用这些 role 编写更好 prompt 的更多信息，请参阅 [Prompt engineering | OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)。从以下 role 中选择：
    - **User**：以 user 身份发送 message，并从 model 获取 response。
    - **Assistant**：告诉 model 采用特定语气或个性。
    - **System**：默认没有 system message。你可以在 user message 中定义 instructions，但在 system message 中设置的 instructions 更有效。每个 conversation 可设置多个 system message。使用此项为下一条 user message 设置 model 行为或上下文。
- **Simplify Output**：开启后返回简化版 response，而不是原始数据。
- **Output Content as JSON**：开启后尝试以 JSON 格式返回 response。兼容 `GPT-4 Turbo` 和所有比 `gpt-3.5-turbo-1106` 更新的 `GPT-3.5 Turbo` model。

### Options <a href="#options" id="options"></a>

- **Frequency Penalty**：应用 penalty，降低 model 重复相似行的倾向。范围为 `0.0` 到 `2.0`。
- **Maximum Number of Tokens**：设置 response 的最大 token 数。对于标准英文文本，一个 token 约为四个字符。使用此选项限制输出长度。
- **Number of Completions**：默认为 1。设置希望为每个 prompt 生成的 completion 数量。请谨慎使用，因为设置较高数量会快速消耗 token。
- **Presence Penalty**：应用 penalty，影响 model 讨论新主题的倾向。范围为 `0.0` 到 `2.0`。
- **Output Randomness (Temperature)**：调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 `0.7`）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。默认为 `1.0`。
- **Output Randomness (Top P)**：调整 Top P 设置，以控制 assistant response 的多样性。例如，`0.5` 表示会考虑所有按可能性加权选项中的一半。建议修改此项或 **Output Randomness (Temperature)**，但不要同时修改两者。默认为 `1.0`。

有关更多信息，请参阅 [Chat Completions | OpenAI](https://platform.openai.com/docs/api-reference/chat) 文档。

## Generate a Model Response <a href="#generate-a-model-response" id="generate-a-model-response"></a>

使用此操作通过 Responses API 向 OpenAI model 发送 message 或 prompt，并接收 response。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Text**。
- **Operation**：选择 **Generate a Model Response**。
- **Model**：选择要使用的 model。有关概览，请参阅 [Models overview | OpenAI Platform](https://platform.openai.com/docs/models)。
- **Messages**：从以下 **Message Types** 中选择：
    - **Text**：输入 **Text** prompt，并分配 model 用于生成 response 的 **Role**。有关如何使用这些 role 编写更好 prompt 的更多信息，请参阅 [Prompt engineering | OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)。
    - **Image**：通过 Image URL、File ID（使用 [OpenAI Files API](https://platform.openai.com/docs/api-reference/files)）或从 workflow 中较早 node 传入 binary data 来提供 **Image**。
    - **File**：以受支持格式（当前仅 PDF）提供 **File**，可通过 File URL、File ID（使用 [OpenAI Files API](https://platform.openai.com/docs/api-reference/files)）或从 workflow 中较早 node 传入 binary data。
    - 对任何 message type，都可以从以下 role 中选择：
        - **User**：以 user 身份发送 message，并从 model 获取 response。
        - **Assistant**：告诉 model 采用特定语气或个性。
        - **System**：默认情况下，system message 是 `"You are a helpful assistant"`。你可以在 user message 中定义 instructions，但在 system message 中设置的 instructions 更有效。每个 conversation 只能设置一条 system message。使用此项为下一条 user message 设置 model 行为或上下文。
- **Simplify Output**：开启后返回简化版 response，而不是原始数据。

### Built-in Tools <a href="#built-in-tools" id="built-in-tools"></a>
OpenAI Responses API 提供一系列 [built-in tools](https://platform.openai.com/docs/guides/tools)，用于丰富 model 的 response：

- **Web Search**：允许 model 在生成 response 前搜索 web 以获取最新信息。
- **MCP Servers**：允许 model 连接到远程 MCP server。有关将远程 MCP server 作为 tool 使用的更多信息，请参阅[这里](https://platform.openai.com/docs/guides/tools-connectors-mcp)。
- **File Search**：允许 model 从先前上传的 file 中搜索 knowledgebase，在生成 response 前查找相关信息。有关更多信息，请参阅 [OpenAI documentation](https://platform.openai.com/docs/guides/tools-file-search)。
- **Code Interpreter**：允许 model 在 sandboxed environment 中编写和运行 Python code。

### Options <a href="#options" id="options"></a>

- **Maximum Number of Tokens**：设置 response 的最大 token 数。对于标准英文文本，一个 token 约为四个字符。使用此选项限制输出长度。
- **Output Randomness (Temperature)**：调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 `0.7`）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。默认为 `1.0`。
- **Output Randomness (Top P)**：调整 Top P 设置，以控制 assistant response 的多样性。例如，`0.5` 表示会考虑所有按可能性加权选项中的一半。建议修改此项或 **Output Randomness (Temperature)**，但不要同时修改两者。默认为 `1.0`。
- **Conversation ID**：此 response 所属的 conversation。此 response 的 input item 和 output item 会在 response 完成后自动添加到此 conversation。
- **Previous Response ID**：要从中继续的 previous response ID。不能与 Conversation ID 结合使用。
- **Reasoning**：model 生成 response 时应投入的 reasoning effort 级别。包括返回 model 执行的 reasoning 的 **Summary** 的能力（例如用于调试）。
- **Store**：是否存储生成的 model response，以便之后通过 API 获取。默认为 `true`。
- **Output Format**：是以 **Text**、指定 **JSON Schema** 还是 **JSON Object** 返回 response。
- **Background**：是否在 [background mode](https://platform.openai.com/docs/guides/background) 下运行 model。这允许更可靠地执行长时间运行的任务。

有关更多信息，请参阅 [Responses | OpenAI](https://platform.openai.com/docs/api-reference/responses/create) 文档。

## Classify Text for Violations <a href="#classify-text-for-violations" id="classify-text-for-violations"></a>

使用此操作识别并标记可能有害的内容。OpenAI model 会分析文本，并返回包含以下内容的 response：

- `flagged`：一个 boolean 字段，表示内容是否可能有害。
- `categories`：特定 category 的违规 flag 列表。
- `category_scores`：每个 category 的分数。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Text**。
- **Operation**：选择 **Classify Text for Violations**。
- **Text Input**：输入要分类的文本，以判断其是否违反 moderation policy。
- **Simplify Output**：开启后返回简化版 response，而不是原始数据。

### Options <a href="#options" id="options"></a>

- **Use Stable Model**：开启后使用 model 的 stable version，而不是 latest version；准确率可能略低。

有关更多信息，请参阅 [Moderations | OpenAI](https://platform.openai.com/docs/api-reference/moderations) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

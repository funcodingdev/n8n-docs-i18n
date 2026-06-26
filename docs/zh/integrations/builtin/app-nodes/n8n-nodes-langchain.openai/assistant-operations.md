---
title: OpenAI Assistant operations
description: >-
  n8n 中 OpenAI node 的 Assistant 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Assistant operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations
layout:
  description:
    visible: false
---

# OpenAI Assistant operations <a href="#openai-assistant-operations" id="openai-assistant-operations"></a>

使用此操作在 OpenAI 中创建、删除、列出、发送消息或更新 assistant。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](README.md)。

{% hint style="info" %}
**Assistant operations 在 OpenAI node V2 中已弃用**

n8n 1.117.0 引入 OpenAI node V2，支持 OpenAI Responses API，并移除对[即将弃用的 Assistants API](https://platform.openai.com/docs/assistants/migration) 的支持。
{% endhint %}

## Create an Assistant <a href="#create-an-assistant" id="create-an-assistant"></a>

使用此操作创建新的 assistant。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Assistant**。
- **Operation**：选择 **Create an Assistant**。
- **Model**：选择 assistant 将使用的 model。如果不确定使用哪个 model，需要高智能时可尝试 `gpt-4o`，需要最快速度和最低成本时可尝试 `gpt-4o-mini`。有关更多信息，请参阅 [Models overview | OpenAI Platform](https://platform.openai.com/docs/models)。
- **Name**：输入 assistant 名称。最大长度为 256 个字符。
- **Description**：输入 assistant 描述。最大长度为 512 个字符。
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**：输入 assistant 使用的 system instructions。最大长度为 32,768 个字符。使用此字段指定 model 回复时使用的 persona。
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Code Interpreter**：开启后为 assistant 启用 code interpreter，使其可以在 sandbox 环境中编写和执行代码。对于需要计算、数据分析或任何基于逻辑处理的任务，请启用此 tool。
- **Knowledge Retrieval**：开启后为 assistant 启用 knowledge retrieval，使其可以访问外部来源或连接的知识库。有关更多信息，请参阅 [File Search | OpenAI Platform](https://platform.openai.com/docs/assistants/tools/file-search)。
    - **Files**：选择要上传为外部知识来源的 file。使用 **Upload a File** operation 添加更多 file。

### Options <a href="#options" id="options"></a>

- **Output Randomness (Temperature)**：调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 0.7）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。默认为 `1.0`。
- **Output Randomness (Top P)**：调整 Top P 设置，以控制 assistant response 的多样性。例如，`0.5` 表示会考虑所有按可能性加权选项中的一半。建议修改此项或 **Output Randomness (Temperature)**，但不要同时修改两者。默认为 `1.0`。
- **Fail if Assistant Already Exists**：启用后，如果已存在同名 assistant，此操作会失败。

有关更多信息，请参阅 [Create assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/createAssistant) 文档。

## Delete an Assistant <a href="#delete-an-assistant" id="delete-an-assistant"></a>

使用此操作从你的账户中删除已有 assistant。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Assistant**。
- **Operation**：选择 **Delete an Assistant**。
- **Assistant**：选择要删除的 assistant，可选择 **From list** 或 **By ID**。

有关更多信息，请参阅 [Delete assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/deleteAssistant) 文档。

## List Assistants <a href="#list-assistants" id="list-assistants"></a>

使用此操作获取 organization 中的 assistant 列表。

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Assistant**。
- **Operation**：选择 **List Assistants**。

### Options <a href="#options" id="options"></a>

- **Simplify Output**：开启后返回简化版 response，而不是原始数据。此选项默认启用。

有关更多信息，请参阅 [List assistants | OpenAI](https://platform.openai.com/docs/api-reference/assistants/listAssistants) 文档。

## Message an Assistant <a href="#message-an-assistant" id="message-an-assistant"></a>

使用此操作向 assistant 发送消息并接收 response。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Assistant**。
- **Operation**：选择 **Message an Assistant**。
- **Assistant**：选择要发送消息的 assistant。
- **Prompt**：输入要发送给 assistant 的文本 prompt 或 message。
    - **Connected Chat Trigger Node**：自动使用前一个 node 的 `chatInput` 字段中的输入。
    - **Define Below**：通过输入静态文本或使用表达式引用前置 node 数据来手动定义 prompt。

### Options <a href="#options" id="options"></a>

- **Base URL**：输入 assistant 发出 API request 时应使用的 base URL。此选项适用于将 assistant 指向其他提供 OpenAI-compatible API 的 LLM provider endpoint。
- **Max Retries**：指定 assistant 在失败时应重试操作的次数。
- **Timeout**：设置 assistant 在超时前等待 response 的最大时间，单位为毫秒。使用此选项可防止操作等待过久。
- **Preserve Original Tools**：关闭后移除与 assistant 关联的原始 tool。如果你想在此特定操作中临时移除 tool，请使用此选项。

有关更多信息，请参阅 [Assistants | OpenAI](https://platform.openai.com/docs/api-reference/assistants) 文档。

## Update an Assistant <a href="#update-an-assistant" id="update-an-assistant"></a>

使用此操作更新已有 assistant 的详情。

输入以下参数：

- **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
- **Resource**：选择 **Assistant**。
- **Operation**：选择 **Update an Assistant**。
- **Assistant**：选择要更新的 assistant。

### Options <a href="#options" id="options"></a>

- **Code Interpreter**：开启后为 assistant 启用 code interpreter，使其可以在 sandbox 环境中编写和执行代码。对于需要计算、数据分析或任何基于逻辑处理的任务，请启用此 tool。
- **Description**：输入 assistant 描述。最大长度为 512 个字符。
  ```
  A virtual assistant that helps users with daily tasks, including setting reminders, answering general questions, and providing quick information.
  ```
- **Instructions**：输入 assistant 使用的 system instructions。最大长度为 32,768 个字符。使用此字段指定 model 回复时使用的 persona。
  ```
  Always respond in a friendly and engaging manner. When a user asks a question, provide a concise answer first, followed by a brief explanation or additional context if necessary. If the question is open-ended, offer a suggestion or ask a clarifying question to guide the conversation. Keep the tone positive and supportive, and avoid technical jargon unless specifically requested by the user.
  ```
- **Knowledge Retrieval**：开启后为 assistant 启用 knowledge retrieval，使其可以访问外部来源或连接的知识库。有关更多信息，请参阅 [File Search | OpenAI Platform](https://platform.openai.com/docs/assistants/tools/file-search)。
- **Files**：选择要上传为外部知识来源的 file。使用 [**Upload a File**](file-operations.md#upload-a-file) operation 添加更多 file。请注意，这只会更新 [Code Interpreter](https://platform.openai.com/docs/assistants/tools/code-interpreter) tool，而不会更新 [File Search](https://platform.openai.com/docs/assistants/tools/file-search) tool。
- **Model**：选择 assistant 将使用的 model。如果不确定使用哪个 model，需要高智能时可尝试 `gpt-4o`，需要最快速度和最低成本时可尝试 `gpt-4o-mini`。有关更多信息，请参阅 [Models overview | OpenAI Platform](https://platform.openai.com/docs/models)。
- **Name**：输入 assistant 名称。最大长度为 256 个字符。
- **Remove All Custom Tools (Functions)**：开启后从 assistant 中移除所有 custom tools (functions)。
- **Output Randomness (Temperature)**：调整 response 的随机性。范围为 `0.0`（确定性）到 `1.0`（最大随机性）。建议修改此项或 **Output Randomness (Top P)**，但不要同时修改两者。从中等 temperature（约 0.7）开始，并根据观察到的输出进行调整。如果 response 过于重复或僵硬，请提高 temperature；如果过于混乱或偏离目标，请降低 temperature。默认为 `1.0`。
- **Output Randomness (Top P)**：调整 Top P 设置，以控制 assistant response 的多样性。例如，`0.5` 表示会考虑所有按可能性加权选项中的一半。建议修改此项或 **Output Randomness (Temperature)**，但不要同时修改两者。默认为 `1.0`。

有关更多信息，请参阅 [Modify assistant | OpenAI](https://platform.openai.com/docs/api-reference/assistants/modifyAssistant) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

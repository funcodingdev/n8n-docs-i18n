---
title: OpenAI Conversation operations
contentType:
  - integration
  - reference
priority: critical
nodeTitle: OpenAI Conversation operations
originalFilePath: >-
  integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/conversation-operations
description: >-
  n8n 中 OpenAI node 的 Conversation 操作文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Conversation operations

使用此操作在 OpenAI 中创建、获取、更新或移除 conversation。有关 OpenAI node 本身的更多信息，请参阅 [OpenAI](./)。

## Create a Conversation <a href="#create-a-conversation" id="create-a-conversation"></a>

使用此操作创建新 conversation。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
* **Resource**：选择 **Conversation**。
* **Operation**：选择 **Create a Conversation**。
* **Messages**：发送给 model 的消息输入。带有 `system` role 的消息优先于 `user` role 给出的 instructions。带有 `assistant` role 的消息会被假定为 model 在之前交互中生成的内容。

### Options <a href="#options" id="options"></a>

* **Metadata**：用于存储结构化信息的一组键值对。你最多可以向一个 object 附加 16 对，这对于添加可通过 API 或 dashboard 搜索的自定义数据很有用。

有关更多信息，请参阅 [Conversations | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Get a Conversation <a href="#get-a-conversation" id="get-a-conversation"></a>

使用此操作获取已有 conversation。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
* **Resource**：选择 **Conversation**。
* **Operation**：选择 **Get Conversation**。
* **Conversation ID**：要获取的 conversation ID。

有关更多信息，请参阅 [Conversations | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Remove a Conversation <a href="#remove-a-conversation" id="remove-a-conversation"></a>

使用此操作移除已有 conversation。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
* **Resource**：选择 **Conversation**。
* **Operation**：选择 **Remove Conversation**。
* **Conversation ID**：要移除的 conversation ID。

有关更多信息，请参阅 [Conversations | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

## Update a Conversation <a href="#update-a-conversation" id="update-a-conversation"></a>

使用此操作更新已有 conversation。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [OpenAI credential](../../credentials/openai.md)。
* **Resource**：选择 **Conversation**。
* **Operation**：选择 **Update a Conversation**。
* **Conversation ID**：要更新的 conversation ID。

### Options <a href="#options" id="options"></a>

* **Metadata**：用于存储结构化信息的一组键值对。你最多可以向一个 object 附加 16 对，这对于添加可通过 API 或 dashboard 搜索的自定义数据很有用。

有关更多信息，请参阅 [Conversations | OpenAI](https://platform.openai.com/docs/api-reference/conversations/create) 文档。

---
title: Moonshot Kimi node 文档
contentType:
  - integration
  - reference
nodeTitle: Moonshot Kimi node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.moonshot
description: >-
  Moonshot Kimi node 允许你从 n8n 与 Moonshot Kimi AI 模型交互。本文档说明如何向模型发送消息、附加图片，以及使用
  node 的操作分析图片
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

# Moonshot Kimi

Moonshot Kimi node 将 n8n workflow 连接到 Moonshot Kimi AI 模型。可用它发送 prompt 并接收模型响应、向消息附加图片，或使用图片分析模型分析图片。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/moonshot.md)找到此 node 的身份验证信息。
{% endhint %}

## 资源和操作 <a href="#resources-and-operations" id="resources-and-operations"></a>

* **分析图片**：分析图片并回答有关图片的问题。
* **向模型发送消息**：向 Moonshot Kimi 模型发送基于文本的消息并接收响应（支持附件、系统消息，以及 thinking mode 和 web search 等高级选项）。

### 分析图片 <a href="#analyze-image" id="analyze-image"></a>

分析图片并回答有关图片的问题。

**参数**

* **Model**（类型：resourceLocator，字段：`modelId`）：选择用于分析的 Moonshot Kimi 模型。
* **Text Input**（类型：string，字段：`text`）：随图片一起发送的 prompt 或问题。默认值：`What's in this image?`
* **Input Data Field Name(s)**（类型：string，字段：`binaryPropertyName`）：包含图片的二进制字段名称。提供多个字段时，用逗号分隔。默认值：`data`
* **Simplify Output**（类型：boolean，字段：`simplify`）：启用时，node 返回简化版响应，而不是完整的原始 API 响应。默认值：`true`

**选项**

* **Maximum Number of Tokens**（类型：number，字段：`maxTokens`）：较少 token 会生成更短、更不详细的图片描述。默认值：`1024`

### 向模型发送消息 <a href="#message-a-model" id="message-a-model"></a>

向 Moonshot Kimi 模型发送一条或多条消息，并接收它的响应。支持基于角色的消息（user/assistant）、附件、系统消息和高级生成选项。

**参数**

* **Model**（类型：resourceLocator，字段：`modelId`）：选择要发送消息的 Moonshot Kimi 模型。
* **Messages**（类型：fixedCollection，字段：`messages`）：组成对话 prompt 的一条或多条消息。
  * content（类型：string）：消息的文本内容。（显示名称：Prompt）
  * role（类型：options）：消息角色，例如 `user` 或 `assistant`，用于指导模型应如何响应。
* **Add Attachments**（类型：boolean，字段：`addAttachments`）：是否向消息附加图片。默认值：`false`
* **Attachment Input Data Field Name(s)**（类型：string，字段：`binaryPropertyName`）：包含要附加图片的二进制字段名称。多个字段用逗号分隔。默认值：`data`
* **Simplify Output**（类型：boolean，字段：`simplify`）：启用时，node 返回简化版响应，而不是原始 API 输出。默认值：`true`

**选项**

* **Frequency Penalty**（类型：number，字段：`frequencyPenalty`）：正值会惩罚文本中已出现的 token，从而减少重复。默认值：`0`
* **Include Merged Response**（类型：boolean，字段：`includeMergedResponse`）：包含一个合并模型响应中所有文本部分的单一输出字符串。默认值：`false`
* **Maximum Number of Tokens**（类型：number，字段：`maxTokens`）：补全要生成的最大 token 数。默认值：`1024`
* **Max Tool Calls Iterations**（类型：number，字段：`maxToolsIterations`）：LLM 停止前运行的最大 tool 迭代循环数。一次迭代可能包含多个 tool call。设为 `0` 表示不限制。默认值：`15`
* **Output Randomness (Temperature)**（类型：number，字段：`temperature`）：控制输出随机性。值越低，输出越确定。默认值：`0.7`
* **Output Randomness (Top P)**（类型：number，字段：`topP`）：采样时要考虑的 token 最大累积概率。默认值：`1`
* **Presence Penalty**（类型：number，字段：`presencePenalty`）：正值会根据 token 是否已出现在当前文本中进行惩罚，鼓励引入新话题。默认值：`0`
* **Response Format**（类型：options，字段：`responseFormat`）：返回响应的格式，例如 `text`。
* **System Message**（类型：string，字段：`system`）：指导模型整体行为和语气的系统级指令。
* **Thinking Mode**（类型：boolean，字段：`thinkingMode`）：启用时，模型会以 chain-of-thought 风格包含推理步骤。不能与 **Web Search** 一起使用。默认值：`false`
* **Web Search**（类型：boolean，字段：`webSearch`）：启用时，模型会执行内置网页搜索以获取最新信息。不能与 **Thinking Mode** 一起使用。默认值：`false`

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Moonshot Kimi node 文档集成模板](https://n8n.io/integrations/moonshot-kimi)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Moonshot Kimi 文档](https://platform.kimi.ai/docs/overview)。

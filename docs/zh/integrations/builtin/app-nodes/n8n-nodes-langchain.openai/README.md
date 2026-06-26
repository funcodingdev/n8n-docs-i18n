---
title: OpenAI node documentation
description: >-
  了解如何在 n8n 中使用 OpenAI node。按照技术文档将 OpenAI node 集成到你的工作流中。
contentType:
  - integration
  - reference
priority: critical
search:
  boost: 3
nodeTitle: n8n-nodes-langchain.openai
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai'
layout:
  description:
    visible: false
---

# OpenAI node <a href="#openai-node" id="openai-node"></a>

使用 OpenAI node 自动化 OpenAI 中的工作，并将 OpenAI 与其他应用集成。n8n 内置支持大量 OpenAI 功能，包括创建 image 和 assistant，以及与 model 聊天。

在本页中，你可以找到 OpenAI node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**以前的 node 版本**

OpenAI node 从 1.29.0 版本开始取代 OpenAI assistant node。
n8n 1.117.0 引入 OpenAI node V2，支持 OpenAI Responses API，并移除对[即将弃用的 Assistants API](https://platform.openai.com/docs/assistants/migration) 的支持。
{% endhint %}

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [OpenAI credentials](../../credentials/openai.md)。
{% endhint %}

## Operations 操作 <a href="#operations" id="operations"></a>

- **Text**
	- [**Generate a Chat Completion**](text-operations.md#generate-a-chat-completion)
	- [**Generate a Model Response**](text-operations.md#generate-a-model-response)
	- [**Classify Text for Violations**](text-operations.md#classify-text-for-violations)
- **Image**
	- [**Analyze Image**](image-operations.md#analyze-image)
	- [**Generate an Image**](image-operations.md#generate-an-image)
	- [**Edit an Image**](image-operations.md#edit-an-image)
- **Audio**
	- [**Generate Audio**](audio-operations.md#generate-audio)
	- [**Transcribe a Recording**](audio-operations.md#transcribe-a-recording)
	- [**Translate a Recording**](audio-operations.md#translate-a-recording)
- **File**
	- [**Delete a File**](file-operations.md#delete-a-file)
	- [**List Files**](file-operations.md#list-files)
	- [**Upload a File**](file-operations.md#upload-a-file)
- **Video**
	- [**Generate a Video**](video-operations.md#generate-video)
- **Conversation**
	- [**Create a Conversation**](conversation-operations.md#create-a-conversation)
	- [**Get a Conversation**](conversation-operations.md#get-a-conversation)
	- [**Update a Conversation**](conversation-operations.md#update-a-conversation)
	- [**Remove a Conversation**](conversation-operations.md#remove-a-conversation)


## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-langchain.openai 集成模板](https://n8n.io/integrations/openai) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [OpenAI 文档](https://beta.openai.com/docs/introduction)。

有关 assistant 工作方式的更多信息，请参阅 [OpenAI assistants 文档](https://platform.openai.com/docs/assistants/how-it-works/objects)。

有关处理 rate limit 的帮助，请参阅 [Handling rate limits](../../handle-rate-limits.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 将 tool 与 OpenAI assistant 一起使用 <a href="#using-tools-with-openai-assistants" id="using-tools-with-openai-assistants"></a>

某些操作允许你连接 tool。[Tools](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/understand-ai-components/how-tools-work) 就像你的 AI 可以用来访问额外上下文或资源的 addon。

选择 **Tools** connector 可浏览可用 tool 并添加它们。

添加 tool connection 后，OpenAI node 会成为 [root node](#user-content-fn-1)[^1]，使它可以与 tool sub-nodes[^3] 组成 [cluster node](#user-content-fn-2)[^2]。有关 cluster node 和 root node 的更多信息，请参阅 [Node types](../../node-types.md#cluster-nodes)。

### 支持 tool connector 的操作 <a href="#operations-that-support-tool-connectors" id="operations-that-support-tool-connectors"></a>

- **Text**
	- [**Generate a Chat Completion**](text-operations.md#generate-a-chat-completion)
	- [**Generate a Model Response**](text-operations.md#generate-a-model-response)

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见问题或错误以及建议解决方案，请参阅[常见问题](common-issues.md)。

[^1]: 每个 n8n cluster node 都包含一个 root node，用于定义 cluster 的主要功能。一个或多个 sub node 会附加到 root node，以扩展其功能。
[^2]: 在 n8n 中，cluster node 是一组协同工作、在 workflow 中提供功能的 node。它们由一个 root node 和一个或多个扩展 node 功能的 sub node 组成。
[^3]: n8n cluster node 由一个或多个连接到 root node 的 sub node 组成。Sub node 会扩展 root node 的功能，提供对特定服务或资源的访问，或提供特定类型的专用处理，例如 calculator 功能。

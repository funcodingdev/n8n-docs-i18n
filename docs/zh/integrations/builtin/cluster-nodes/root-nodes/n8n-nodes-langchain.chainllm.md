---
title: Basic LLM Chain node 文档
description: >-
  了解如何在 n8n 中使用 Basic LLM Chain node。按照技术文档将 Basic LLM Chain
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Basic LLM Chain node documentation
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm
layout:
  description:
    visible: false
---

# Basic LLM Chain node <a href="#basic-llm-chain-node" id="basic-llm-chain-node"></a>

使用 Basic LLM Chain node 设置 model 将使用的 prompt，并可为响应设置可选 parser。

在本页中，你可以找到 Basic LLM Chain node 的 node 参数，以及更多相关资源链接。

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Basic LLM Chain integrations](https://n8n.io/integrations/basic-llm-chain/) 页面。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Prompt <a href="#prompt" id="prompt"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Ss9Y6clfLTwlXMx69w6E/" %}

### Require Specific Output Format <a href="#require-specific-output-format" id="require-specific-output-format"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/IsHMhvgDA3Ok5qdqnHnJ/" %}

## Chat Messages <a href="#chat-messages" id="chat-messages"></a>

使用 chat model 时，使用 **Chat Messages** 设置消息。

如果你没有连接 chat model，n8n 会忽略这些选项。选择你希望 node 使用的 **Type Name or ID**：

#### AI <a href="#ai" id="ai"></a>

在 **Message** 字段中输入一个预期响应示例。model 会尝试在其消息中以相同方式响应。

#### System <a href="#system" id="system"></a>

输入要与用户输入一起包含的 system **Message**，以帮助指导 model 应执行什么操作。

将此选项用于定义语气等场景，例如：`Always respond talking like a pirate`。

#### User <a href="#user" id="user"></a>

输入一个用户输入示例。将它与 AI 选项一起使用，可以帮助改善 agent 的输出。两者一起使用时，会为 model 提供输入示例和预期响应（**AI Message**）以供遵循。

选择以下输入类型之一：

* **Text**：输入一个文本 **Message** 作为用户输入示例。
* **Image (Binary)**：选择前一个 node 中的 binary input。输入 **Image Data Field Name**，以标识前一个 node 中哪个 binary 字段包含图片数据。
* **Image (URL)**：使用此选项从 URL 输入图片。输入 **Image URL**。

对于两种 **Image** 类型，请选择 **Image Details** 来控制 model 如何处理图片并生成其文本理解。可选项包括：

* **Auto**：model 使用 auto 设置，该设置会查看图片输入大小，并决定应使用 Low 还是 High 设置。
* **Low**：model 接收低分辨率 512px x 512px 版本的图片，并用 65 token 的预算表示图片。这允许 API 更快返回响应并消耗更少输入 token。将此选项用于不需要高细节的用例。
* **High**：model 可以访问低分辨率图片，然后根据输入图片大小创建 512px 方形的详细裁剪。每个详细裁剪使用两倍 token 预算（65 tokens），总计 129 tokens。将此选项用于需要高细节的用例。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Basic LLM Chain node 文档集成模板](https://n8n.io/integrations/basic-llm-chain)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain 关于 Basic LLM Chains 的文档](https://js.langchain.com/docs/tutorials/llm_chain/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Basic LLM Chain node 的一些常见错误和问题，以及解决或排查步骤。

### No prompt specified error <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

当 **Prompt** 为空或无效时，会显示此错误。

你可能会在以下两种场景之一看到此错误：

1. 当你将 **Prompt** 设置为 **Define below**，但未在 **Text** 字段中输入任何内容时。
    * 要解决此问题，请在 **Text** 字段中输入有效 prompt。
2. 当你将 **Prompt** 设置为 **Connected Chat Trigger Node**，且传入数据没有名为 `chatInput` 的字段时。
    * node 期望存在 `chatInput` 字段。如果前一个 node 没有此字段，请添加 [Edit Fields (Set)](../../core-nodes/n8n-nodes-base.set.md) node，将传入字段名称编辑为 `chatInput`。

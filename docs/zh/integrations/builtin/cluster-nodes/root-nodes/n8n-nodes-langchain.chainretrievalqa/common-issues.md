---
title: Question and Answer Chain node 常见问题
contentType:
  - integration
  - reference
priority: high
nodeTitle: Question and Answer Chain node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues
description: >-
  n8n 中 Question and Answer Chain node 的常见问题和疑问文档，n8n 是一个 workflow 自动化平台。包含问题详情和建议解决方案。
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

# 常见问题

以下是 [Question and Answer Chain node](./) 的一些常见错误和问题，以及解决或排查步骤。

## No prompt specified error <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

当 **Prompt** 为空或无效时，会显示此错误。

你可能会在以下两种场景之一看到此错误：

1. 当你将 **Prompt** 设置为 **Define below**，且 **Text** 中的 expression 未生成值时。
   * 要解决此问题，请在 **Text** 字段中输入有效 prompt。
   * 确保所有 expressions 都引用有效字段，并解析为有效输入，而不是 null。
2. 当你将 **Prompt** 设置为 **Connected Chat Trigger Node**，且传入数据包含 null 值时。
   * 要解决此问题，请确保输入包含 `chatInput` 字段。添加 [Edit Fields (Set)](../../../core-nodes/n8n-nodes-base.set.md) node，将传入字段名称编辑为 `chatInput`。
   * 从输入 node 的 `chatInput` 字段中移除所有 null 值。

## A Retriever sub-node must be connected error <a href="#a-retriever-sub-node-must-be-connected-error" id="a-retriever-sub-node-must-be-connected-error"></a>

当 n8n 尝试在未连接 Retriever 的情况下执行 node 时，会显示此错误。

要解决此问题，请在 node 打开时点击屏幕底部的 + Retriever 按钮，或在 node 未打开时点击 Retriever + 连接器。然后 n8n 会打开可供选择的 Retrievers 列表。

## 无法生成更长响应 <a href="#cant-produce-longer-responses" id="cant-produce-longer-responses"></a>

如果你需要生成比 Question and Answer Chain node 默认输出更长的响应，可以尝试以下一种或多种方法：

* **连接更详细的 model**：有些 AI models 生成的结果比其他 model 更简短。将 model 换成具有更大 context window 和更详细输出的 model，可以增加响应字数。
* **增加最大 token 数**：许多 model node（例如 [OpenAI Chat Model](../../sub-nodes/n8n-nodes-langchain.lmchatopenai/#maximum-number-of-tokens)）包含 **Maximum Number of Tokens** 选项。你可以设置此项以增加 model 可用于生成响应的最大 token 数。
* **分阶段构建更长响应**：对于更详细的答案，你可能希望使用多种 AI node 分阶段构建回复。你可以使用 AI 将单个问题拆分为多个 prompts，并为每个 prompt 创建响应。然后再组合这些响应形成最终回复。虽然细节不同，但你可以在这个[使用 AI 根据少量关键词撰写 WordPress 文章的模板](https://n8n.io/workflows/2187-write-a-wordpress-post-with-ai-starting-from-a-few-keywords/)中看到这一通用思路的良好示例。

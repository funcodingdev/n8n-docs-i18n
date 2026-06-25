---
title: AI Agent node 常见问题
contentType:
  - integration
  - reference
priority: critical
nodeTitle: AI Agent node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues
description: >-
  n8n 中 AI Agent node 的常见问题和疑问文档，n8n 是一个 workflow 自动化平台。包含问题详情和建议解决方案。
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

以下是 [AI Agent node](./) 的一些常见错误和问题，以及解决或排查步骤。

## Internal error: 400 Invalid value for 'content' <a href="#internal-error-400-invalid-value-for-content" id="internal-error-400-invalid-value-for-content"></a>

完整错误消息可能如下所示：

```
Internal error
Error: 400 Invalid value for 'content': expected a string, got null.
<stack-trace>
```

如果 **Prompt** 输入包含 null 值，可能会发生此错误。

你可能会在以下两种场景之一看到此错误：

1. 当你将 **Prompt** 设置为 **Define below**，且 **Text** 中的 expression 未生成值时。
   * 要解决此问题，请确保你的 expressions 引用了有效字段，并且它们会解析为有效输入，而不是 null。
2. 当你将 **Prompt** 设置为 **Connected Chat Trigger Node**，且传入数据包含 null 值时。
   * 要解决此问题，请从输入 node 的 `chatInput` 字段中移除所有 null 值。

## Error in sub-node Simple Memory <a href="#error-in-sub-node-simple-memory" id="error-in-sub-node-simple-memory"></a>

当 n8n 在 [Simple Memory](../../sub-nodes/n8n-nodes-langchain.memorybufferwindow/) sub-node 中遇到问题时，会显示此错误。

最常见的情况是，你的 workflow 或复制的 workflow 模板使用了较旧版本的 Simple Memory node（以前称为 "Window Buffer Memory"）。

尝试从 workflow 中移除 Simple Memory node 并重新添加，这将确保你使用的是该 node 的最新版本。

## A Chat Model sub-node must be connected error <a href="#a-chat-model-sub-node-must-be-connected-error" id="a-chat-model-sub-node-must-be-connected-error"></a>

当 n8n 尝试在未连接 Chat Model 的情况下执行 node 时，会显示此错误。

要解决此问题，请在 node 打开时点击屏幕底部的 + Chat Model 按钮，或在 node 关闭时点击 Chat Model + 连接器。然后 n8n 会打开可供选择的 Chat Models 列表。

## No prompt specified error <a href="#no-prompt-specified-error" id="no-prompt-specified-error"></a>

当 agent 期望自动从前一个 node 获取 prompt 时，会发生此错误。通常，这发生在你使用 [Chat Trigger Node](../../../core-nodes/n8n-nodes-base.compression/n8n-nodes-base.compression.md) 时。

要解决此问题，请找到 AI Agent node 的 **Prompt** 参数，并将其从 **Connected Chat Trigger Node** 改为 **Define below**。这样你就可以通过引用其他 node 的输出数据或添加静态文本，手动构建 prompt。

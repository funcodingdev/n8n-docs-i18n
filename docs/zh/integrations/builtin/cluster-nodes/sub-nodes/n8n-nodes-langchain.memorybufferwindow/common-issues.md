---
title: Simple Memory node 常见问题
description: >-
  n8n workflow automation platform 中 Simple Memory node 的常见问题与疑问文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Simple Memory node common issues
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues
layout:
  description:
    visible: false
---

# Simple Memory node 常见问题 <a href="#simple-memory-node-common-issues" id="simple-memory-node-common-issues"></a>

这里列出 [Simple Memory node](README.md) 的一些常见错误和问题，以及解决或排查它们的步骤。

## 单一 memory instance <a href="#single-memory-instance" id="single-memory-instance"></a>

如果你向 workflow 添加多个 Simple Memory node，默认情况下所有 nodes 都会访问同一个 memory instance。在执行会覆盖现有 memory contents 的破坏性 actions 时请谨慎，例如 [Chat Memory Manager](../n8n-nodes-langchain.memorymanager.md) node 中的 override all messages operation。如果想在 workflow 中使用多个 memory instance，请在不同 memory nodes 中设置不同 session IDs。

## 管理 Session ID <a href="#managing-the-session-id" id="managing-the-session-id"></a>

大多数情况下，`sessionId` 会自动从 **On Chat Message** trigger 获取。但你可能会遇到包含 `No sessionId` 短语的错误。

如果遇到此错误，请先检查 Chat trigger 的 output，确保其中包含 `sessionId`。

如果你没有使用 **On Chat Message** trigger，则需要手动管理 sessions。

出于测试目的，你可以使用类似 `my_test_session` 的 static key。如果采用这种方式，请务必在发布 workflow 前设置适当的 session management，以避免 live environment 中的潜在问题。

---
title: Zep node 文档
description: >-
  了解如何在 n8n 中使用 Zep node。按照技术文档将 Zep node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Zep node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memoryzep
layout:
  description:
    visible: false
---

# Zep node <a href="#zep-node" id="zep-node"></a>

{% hint style="warning" %}
**Deprecated**

此 node 已弃用，并会在未来版本中移除。
{% endhint %}

使用 Zep node 将 Zep 用作 memory[^1] server。

在本页中，你可以找到 Zep node 支持的 operations 列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../../credentials/zep.md)找到此 node 的身份验证信息。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Session ID**：输入用于在 workflow data 中存储 memory 的 ID。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Zep node 文档集成模板](https://n8n.io/integrations/zep)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain Zep 文档](https://js.langchain.com/docs/integrations/memory/zep_memory)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

## 单一 memory instance <a href="#single-memory-instance" id="single-memory-instance"></a>

如果你向 workflow 添加多个 Zep node，默认情况下所有 nodes 都会访问同一个 memory instance。在执行会覆盖现有 memory contents 的破坏性 actions 时请谨慎，例如 [Chat Memory Manager](./n8n-nodes-langchain.memorymanager.md) node 中的 override all messages operation。如果想在 workflow 中使用多个 memory instance，请在不同 memory nodes 中设置不同 session IDs。

[^1]: 在 AI 语境中，memory 允许 AI tools 在 interactions 之间持久化 message context。例如，这允许你与 AI agents 进行持续对话，而无需在每条 message 中提交 ongoing context。在 n8n 中，AI agent nodes 可以使用 memory，但 AI chains 不能。

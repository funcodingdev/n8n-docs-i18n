---
title: Workflow Retriever node 文档
description: >-
  了解如何在 n8n 中使用 Workflow Retriever node。按照技术文档将 Workflow Retriever
  node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Workflow Retriever node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.retrieverworkflow
layout:
  description:
    visible: false
---

# Workflow Retriever node <a href="#workflow-retriever-node" id="workflow-retriever-node"></a>

使用 Workflow Retriever node 从 n8n workflow 检索数据，供 Retrieval QA Chain 或另一个 Retriever node 使用。

在本页中，你可以找到 Workflow Retriever node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Source <a href="#source" id="source"></a>

告诉 n8n 要调用哪个 workflow。你可以选择：

* **Database** 并输入 workflow ID。
* **Parameter** 并复制完整的 [workflow JSON](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/export-and-import)。

### Workflow values <a href="#workflow-values" id="workflow-values"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/i66Pv0lYL7QjJ9F9tZUj/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Workflow Retriever node 文档集成模板](https://n8n.io/integrations/workflow-retriever)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [LangChain general retriever 文档](https://js.langchain.com/docs/concepts/retrievers/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

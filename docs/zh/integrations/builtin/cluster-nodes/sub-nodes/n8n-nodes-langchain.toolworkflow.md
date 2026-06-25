---
title: Call n8n Workflow Tool node 文档
description: >-
  了解如何在 n8n 中使用 Call n8n Workflow Tool node。按照技术文档将 Call n8n
  Workflow Tool node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Call n8n Workflow Tool node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow
layout:
  description:
    visible: false
---

# Call n8n Workflow Tool node <a href="#call-n8n-workflow-tool-node" id="call-n8n-workflow-tool-node"></a>

Call n8n Workflow Tool node 是一个 tool[^1]，允许 agent[^2] 运行另一个 n8n workflow 并获取其 output data。

在本页中，你可以找到 Call n8n Workflow Tool node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Description <a href="#description" id="description"></a>

输入 custom code description。这会告诉 agent 何时使用此 tool。例如：

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Source <a href="#source" id="source"></a>

告诉 n8n 要调用哪个 workflow。你可以选择：

* **Database**：从列表选择 workflow 或输入 workflow ID。
* **Define Below**：复制完整的 [workflow JSON](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/export-and-import)。

### Workflow Inputs <a href="#workflow-inputs" id="workflow-inputs"></a>

当使用 **Database** 作为 workflow source 时，选择 sub-workflow（并在 sub-workflow 中定义 **Workflow Input Schema**）后，你可以定义 **Workflow Inputs**。

选择 **Refresh** button，从 sub-workflow 拉取 input fields。

你可以使用以下任意组合来定义 workflow input values：

* 提供 fixed values
* 使用 expressions 引用当前 workflow 的 data
* 选择字段右侧的 AI button，[让 AI model 指定参数](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/ai-examples/use-ai-for-parameters)
* 在 expressions 中使用 [`$fromAI()` function](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/ai-examples/use-ai-for-parameters#use-the-fromai-function)，控制 model 填入 data 的方式，并将 AI-generated input 与其他 custom input 混合

要引用当前 workflow 的 data，请将 input panel 中的 fields 拖到已选择 Expressions mode 的 field 中。

要开始使用 `$fromAI()` function，请选择字段右侧的 "Let the model define this parameter" button，然后使用框上的 **X** 恢复为 user-defined values。该 field 会变为 expression field，并预填 `$fromAI()` expression。从这里开始，你可以自定义 expression，添加其他 static 或 dynamic content，或调整 `$fromAI()` function parameters。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Call n8n Workflow Tool node 文档集成模板](https://n8n.io/integrations/workflow-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: 在 AI 语境中，tool 是一种附加 resource，AI 在响应 request 时可以引用它来获取特定 information 或 functionality。AI model 可以使用 tool 与 external systems 交互，或完成具体、聚焦的 tasks。
[^2]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

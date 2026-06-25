---
title: Custom Code Tool node 文档
description: >-
  了解如何在 n8n 中使用 Custom Code Tool node。按照技术文档将 Custom Code Tool
  node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Custom Code Tool node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolcode
layout:
  description:
    visible: false
---

# Custom Code Tool node <a href="#custom-code-tool-node" id="custom-code-tool-node"></a>

使用 Custom Code Tool node 编写 agent[^1] 可运行的 code。

在本页中，你可以找到 Custom Code Tool node 的 node 参数，以及更多相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Description <a href="#description" id="description"></a>

为你的 custom code 添加 description。这会告诉 agent 何时使用此 tool。例如：

> Call this tool to get a random color. The input should be a string with comma separated names of colors to exclude.

### Language <a href="#language" id="language"></a>

你可以使用 JavaScript 或 Python。

### JavaScript / Python box <a href="#javascript-python-box" id="javascript-python-box"></a>

在这里编写 code。

你可以使用 `query` 访问 tool input。例如，要接收 input string 并将其转为小写：

```js
let myString = query;
return myString.toLowerCase();
```

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Custom Code Tool node 文档集成模板](https://n8n.io/integrations/code-tool)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

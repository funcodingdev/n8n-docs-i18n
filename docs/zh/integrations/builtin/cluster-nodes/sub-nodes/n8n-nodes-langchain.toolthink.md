---
title: Think Tool node 文档
description: >-
  了解如何在 n8n 中使用 Think Tool node。按照技术文档将 Tool Think node 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Think Tool node documentation
originalFilePath: integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolthink
layout:
  description:
    visible: false
---

# Think Tool node <a href="#think-tool-node" id="think-tool-node"></a>

Think Tool node 是一个 tool[^1]，会邀请 agent[^2] 在回答前进行思考。本质上，它允许 agent 在给出 answer 之前通过自言自语反思 question。对于需要审慎 response 的复杂 queries，这尤其有用。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Think Tool node 文档集成模板](https://n8n.io/integrations/think-tool)，或[搜索所有模板](https://n8n.io/workflows/)

### Prompting 示例 <a href="#prompting-example" id="prompting-example"></a>

例如，假设你询问 agent：

> *Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?*

agent 会使用 tool 进行思考：

> *We have the following information: 1. Jack is looking at Anne. 2. Anne is looking at George. 3. Jack is married. 4. George is not married. 5. We don't know if Anne is married or not.*

> *We need to determine if a married person is looking at an unmarried person. Let's consider both cases for Anne:*

> *Case 1: Anne is married.*

> - *If Anne is married, then she (married) is looking at George (unmarried). In this case, a married person (Anne) is looking at an unmarried person (George).*

> *Case 2: Anne is unmarried.*

> - *If Anne is unmarried, then Jack (married) is looking at Anne (unmarried). In this case, a married person (Jack) is looking at an unmarried person (Anne).*

> *In both scenarios, we find that a married person is looking at an unmarried person. Therefore, the answer to the question is yes.*

然后再提供 answer：

> *Yes, a married person is looking at an unmarried person. In both possible scenarios regarding Anne's marital status, we find that a married individual (either Jack or Anne) is looking at an unmarried individual (either George or Anne).*

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Yl56nEscwQQAbBUeWfvp/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

[^1]: 在 AI 语境中，tool 是一种附加 resource，AI 在响应 request 时可以引用它来获取特定 information 或 functionality。AI model 可以使用 tool 与 external systems 交互，或完成具体、聚焦的 tasks。
[^2]: AI agents 是能够响应请求、做出决策并为用户执行真实世界任务的人工智能系统。它们使用 large language models（LLMs）解释用户输入，并根据已有的信息和资源决定如何最好地处理请求。

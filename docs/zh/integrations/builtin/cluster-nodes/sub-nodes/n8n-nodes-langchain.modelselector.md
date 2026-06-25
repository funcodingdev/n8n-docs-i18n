---
title: Model Selector
description: >-
  了解如何在 n8n 中使用 Model Selector node。按照技术文档将 Model Selector node
  集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Model Selector
originalFilePath: >-
  integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.modelselector
layout:
  description:
    visible: false
---

# Model Selector <a href="#model-selector" id="model-selector"></a>

Model Selector node 会在 workflow execution 期间，根据一组已定义的 conditions，动态选择已连接 language models 中的一个。这允许你为 error handling 实现 fallback mechanisms，或为特定 tasks 选择最合适的 model。

本页介绍 Model Selector node 的 node 参数，并包含相关资源链接。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/X6JM1Mgg5iwvZLDpGEB0/" %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Number of Inputs <a href="#number-of-inputs" id="number-of-inputs"></a>

指定可用于附加 language models 的 input connections 数量。

### Rules <a href="#rules" id="rules"></a>

每条 rule 定义当特定 conditions 匹配时要使用的 model。

Model Selector node 会从第一个 input 开始按顺序评估 rules，并在找到匹配项后立即停止评估。这意味着如果多条 rules 都会匹配，n8n 只会使用第一条匹配 rule 定义的 model。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Model Selector 集成模板](https://n8n.io/integrations/model-selector)，或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

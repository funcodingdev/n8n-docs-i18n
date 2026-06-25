---
title: Sentiment Analysis node 文档
description: >-
  了解如何在 n8n 中使用 Sentiment Analysis node。按照技术文档将 Sentiment
  Analysis node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Sentiment Analysis node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis
layout:
  description:
    visible: false
---

# Sentiment Analysis node <a href="#sentiment-analysis-node" id="sentiment-analysis-node"></a>

使用 Sentiment Analysis node 分析传入文本数据的情感。

语言 model 会使用 node 选项中的 [**Sentiment Categories**](#node-options) 来判断每个 item 的情感。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Text to Analyze** 定义用于情感分析的输入文本。这是一个引用输入 items 中某个字段的 expression。例如，如果输入来自 chat 或 message 来源，可以是
`{{ $json.chatInput }}`。默认情况下，它期望存在 `text` 字段。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Sentiment Categories**：定义你希望将输入分类到哪些类别。
    * 默认类别为 `Positive, Neutral, Negative`。你可以自定义这些类别以适配特定用例，例如使用 `Very Positive, Positive, Neutral, Negative, Very Negative` 进行更细粒度的分析。
* **Include Detailed Results**：开启后，此选项会在输出中包含情感强度和置信度分数。请注意，这些分数是语言 model 生成的估计值，是粗略指标而非精确测量。
* **System Prompt Template**：使用此选项更改情感分析所使用的 system prompt。它使用 `{categories}` 占位符表示类别。
* **Enable Auto-Fixing**：启用后，node 会自动修复 model 输出，确保其匹配预期格式。实现方式是将 schema 解析错误发送给 LLM，并要求它修复错误。

## 使用说明 <a href="#usage-notes" id="usage-notes"></a>

### Model Temperature 设置 <a href="#model-temperature-setting" id="model-temperature-setting"></a>

强烈建议将连接的语言 model 的 temperature 设置为 0 或接近 0 的值。这有助于确保结果尽可能确定，在多次运行中提供更一致、更可靠的情感分析。

### 语言注意事项 <a href="#language-considerations" id="language-considerations"></a>

node 的表现可能因输入文本语言而异。

为获得最佳结果，请确保你选择的语言 model 支持输入语言。

### 处理大量文本 <a href="#processing-large-volumes" id="processing-large-volumes"></a>

分析大量文本时，请考虑将输入拆分为更小的 chunks，以优化处理时间和资源使用。

### 迭代优化 <a href="#iterative-refinement" id="iterative-refinement"></a>

对于复杂的情感分析任务，你可能需要迭代优化 system prompt 和 categories，以达到期望结果。

## 使用示例 <a href="#example-usage" id="example-usage"></a>

### 基础情感分析 <a href="#basic-sentiment-analysis" id="basic-sentiment-analysis"></a>

1. 将数据源（例如 RSS Feed、HTTP Request）连接到 Sentiment Analysis node。
2. 将 "Text to Analyze" 字段设置为相关 item property（例如，针对 blog post 内容使用 `{{ $json.content }}`）。
3. 保留默认情感类别。
4. 将 node 输出连接到不同路径，以分别处理 positive、neutral 和 negative 情感。

### 自定义类别分析 <a href="#custom-category-analysis" id="custom-category-analysis"></a>

1. 将 **Sentiment Categories** 更改为 `Excited, Happy, Neutral, Disappointed, Angry`。
2. 调整你的 workflow 以处理这五个输出类别。
3. 使用此设置通过更细腻的情绪类别分析客户反馈。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

---
title: AI Transform
contentType:
  - integration
  - reference
nodeTitle: AI Transform
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.aitransform.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.aitransform
description: >-
  n8n 中 AI Transform node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
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

# AI Transform

使用 AI Transform node 可以根据你的提示词生成代码片段。AI 具备上下文感知能力，能够理解 workflow 中的 node 及其数据类型。

{% hint style="info" %}
**功能可用性**

仅在 [Cloud plans](../../../../manage-cloud/overview.md) 中可用。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Instructions <a href="#instructions" id="instructions"></a>

输入给 AI 的提示词，然后点击 **Generate code** 按钮，自动填充 **Transformation Code**。例如，你可以指定希望如何处理或分类数据。更多信息请参阅[编写良好提示词](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/get-coding-help-from-ai#writing-good-prompts)。

提示词应使用简单英文，并少于 500 个字符。

### Transformation Code <a href="#transformation-code" id="transformation-code"></a>

该 node 生成的代码片段是只读的。要编辑这段代码，请调整 **Instructions** 中的提示词，或将其复制粘贴到 [Code](n8n-nodes-base.code/) node 中。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 AI Transform 集成模板](https://n8n.io/integrations/ai-transform)或[搜索所有模板](https://n8n.io/workflows/)

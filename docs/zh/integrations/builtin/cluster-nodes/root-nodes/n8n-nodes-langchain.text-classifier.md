---
title: Text Classifier node 文档
description: >-
  了解如何在 n8n 中使用 Text Classifier node。按照技术文档将 Text Classifier
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Text Classifier node documentation
originalFilePath: >-
  integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier
layout:
  description:
    visible: false
---

# Text Classifier node <a href="#text-classifier-node" id="text-classifier-node"></a>

使用 Text Classifier node 对传入数据进行分类。使用参数中提供的类别（见下文），每个 item 都会传给 model，以判断其类别。

在本页中，你可以找到 Text Classifier node 的 node 参数，以及更多相关资源链接。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

* **Input Prompt** 定义要分类的输入。这通常是引用输入 items 中某个字段的 expression。例如，如果输入来自 chat trigger，可以是 `{{ $json.chatInput }}`。默认情况下，它引用 `text` 字段。
* **Categories**：添加你希望将输入分类到的类别。类别包含名称和描述。使用描述告诉 model 该类别的含义。如果含义不明显，这一点很重要。你可以添加任意数量的类别。

## Node 选项 <a href="#node-options" id="node-options"></a>

* **Allow Multiple Classes To Be True**：你可以配置 classifier 始终为每个 item 输出单个 class（关闭），或允许 model 选择多个 classes（开启）。
* **When No Clear Match**：定义当 model 无法为 item 找到合适匹配项时会发生什么。有两个选项：
	- **Discard Item**（默认）：如果 node 未检测到任何类别，则丢弃该 item。
	- **Output on Extra, 'Other' Branch**：创建一个名为 **Other** 的独立输出分支。当 node 未检测到任何类别时，会在此分支输出 items。
* **System Prompt Template**：使用此选项更改分类所使用的 system prompt。它使用 `{categories}` 占位符表示类别。

* **Enable Auto-Fixing**：启用后，node 会自动修复 model 输出，确保其匹配预期格式。实现方式是将 schema 解析错误发送给 LLM，并要求它修复错误。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

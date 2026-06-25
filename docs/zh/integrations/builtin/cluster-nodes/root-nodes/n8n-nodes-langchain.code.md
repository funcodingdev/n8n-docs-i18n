---
title: LangChain Code node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: LangChain Code node documentation
originalFilePath: integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code
url: >-
  https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code
description: >-
  了解如何在 n8n 中使用 LangChain Code node。按照技术文档将 LangChain Code
  node 集成到你的 workflow 中。
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

# LangChain Code

使用 LangChain Code node 导入 LangChain。这意味着，如果你需要某项 n8n 尚未创建 node 的功能，仍然可以使用它。通过配置 LangChain Code node 连接器，你可以将其用作普通 node、root node 或 sub-node。

在本页中，你可以找到 node 参数、配置 node 的指导，以及更多相关资源链接。

{% hint style="warning" %}
**因安全问题已弃用**

此 node 存在严重安全问题，使用并不安全。它已弃用，并从 nodes panel 中隐藏。请避免在 workflow 中使用它。
{% endhint %}

{% hint style="info" %}
**Cloud 中不可用**

此 node 仅在 self-hosted n8n 中可用。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Add Code <a href="#add-code" id="add-code"></a>

添加你的自定义代码。选择 **Execute** 或 **Supply Data** 模式。你只能使用一种模式。

与 [Code node](../../core-nodes/n8n-nodes-base.code/) 不同，LangChain Code node 不支持 Python。

* **Execute**：像使用 n8n 自带的 Code node 一样使用 LangChain Code node。它会从 workflow 获取输入数据，处理数据，并将其作为 node 输出返回。此模式需要 main input 和 output。你必须在 **Inputs** 和 **Outputs** 中创建这些连接。
* **Supply Data**：将 LangChain Code node 用作 sub-node，向 root node 发送数据。它使用 main 之外的输出。

默认情况下，你无法在此 node 中加载 built-in 或 external modules。Self-hosted 用户可以[启用 built-in 和 external modules](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration)。

### Inputs <a href="#inputs" id="inputs"></a>

选择输入类型。

main input 是所有 n8n workflow 中都有的普通连接器。如果你在 node 中设置了 main input 和 output，则必须使用 **Execute** code。

### Outputs <a href="#outputs" id="outputs"></a>

选择输出类型。

main output 是所有 n8n workflow 中都有的普通连接器。如果你在 node 中设置了 main input 和 output，则必须使用 **Execute** code。

## Node 输入和输出配置 <a href="#node-inputs-and-outputs-configuration" id="node-inputs-and-outputs-configuration"></a>

通过配置 LangChain Code node 连接器（inputs 和 outputs），你可以将其用作 app node、root node 或 sub-node。

![Screenshot of a workflow with four LangChain nodes, configured as different node types](../../../.gitbook/assets/create-node-types.png)

| Node type | Inputs | Outputs | Code mode |
| --- | --- | --- | --- |
| App node。类似 [Code node](../../core-nodes/n8n-nodes-base.code/)。 | Main | Main | Execute |
| Root node | Main；至少一个其他类型 | Main | Execute |
| Sub-node | - | main 之外的类型。必须匹配你想连接到的 input type。 | Supply Data |
| 带 sub-nodes 的 sub-node | main 之外的类型 | main 之外的类型。必须匹配你想连接到的 input type。 | Supply Data |

## 内置方法 <a href="#built-in-methods" id="built-in-methods"></a>

n8n 提供这些方法，让你更容易在 LangChain Code node 中执行常见任务。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/iIcw3xaOoa9HryGmR8dX/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 LangChain Code node 文档集成模板](https://n8n.io/integrations/langchain-code)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/mjXhKRIw98UJ5hk9LWBl/" %}

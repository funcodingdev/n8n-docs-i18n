---
description: n8n 的内置自定义方法和变量。
contentType: overview
nodeTitle: Use built-in shortcuts
originalFilePath: code/builtin/overview.md
originalUrl: 'https://docs.n8n.io/code/builtin/overview'
url: 'https://docs.n8n.io/build/code-in-n8n/use-built-in-shortcuts'
layout:
  description:
    visible: false
---

# 内置方法和变量 <a href="#built-in-methods-and-variables" id="built-in-methods-and-variables"></a>

n8n 提供内置方法和变量，用于处理数据和访问 n8n 数据。本节提供可在 expression[^1] 中使用的方法和变量参考，并附带简短说明。

{% hint style="info" %}
**Expressions editor 和 Code node 中的可用性**

有些方法和变量在 Code node 中不可用。这些内容不会出现在文档中。

所有数据转换函数仅在 expressions editor 中可用。
{% endhint %}


[Cookbook](README.md) 包含一些常见任务的示例，包括部分[仅 Code node 可用](cookbook/code-node/README.md)的函数。

[^1]: 在 n8n 中，expression 允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n expression 语法，通过前序 node、其他 workflow 或 n8n 环境中的数据来定义值。

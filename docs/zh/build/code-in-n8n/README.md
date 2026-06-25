---
title: n8n 中的代码文档和指南
description: >-
  访问关于在 n8n 中使用代码和 expression 的文档与指南，以及其他开发者资源。
contentType: overview
hide:
  - feedback
  - kapaButton
nodeTitle: Code in n8n
originalFilePath: code/index.md
originalUrl: 'https://docs.n8n.io/code'
url: 'https://docs.n8n.io/build/'
layout:
  description:
    visible: false
---

# n8n 中的代码 <a href="#code-in-n8n" id="code-in-n8n"></a>

n8n 是低代码工具。这意味着你可以在不写代码的情况下完成很多事情，然后在需要时添加代码。

## workflow 中的代码 <a href="#code-in-your-workflows" id="code-in-your-workflows"></a>

在 workflow 中，有两个地方可以使用代码：

<div class="grid-cards-vertical cards" markdown>

- __Expression__

	使用 expression[^1] 在 node 中转换[数据](../work-with-data/overview.md)。你可以在 expression 中使用 JavaScript，也可以使用 n8n 的[内置方法和变量](use-built-in-shortcuts.md)。

	[→ Expression](../work-with-data/expressions-versus-data-nodes.md)

- __Code node__

	使用 Code node 将 JavaScript 或 Python 添加到 workflow 中。

	[→ Code node](using-the-code-node.md)

</div>


## 其他技术资源 <a href="#other-technical-resources" id="other-technical-resources"></a>

以下功能与技术用户相关。

### 技术 node <a href="#technical-nodes" id="technical-nodes"></a>

n8n 提供 core node，可简化添加关键功能的过程，例如 API 请求、webhook、调度和文件处理。

<div class="grid-cards-vertical cards" markdown>

- __编写后端__

	[HTTP Request](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.httprequest)、[Webhook](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.webhook) 和 [Code](using-the-code-node.md) node 可帮助你发起 API 调用、响应 webhook，并在 workflow 中编写任意 JavaScript。

	可用它完成类似[创建 API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint/) 的工作。

	[→ Core nodes](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes)

- __表达复杂逻辑__

	你可以使用 [If](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if)、[Switch](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.switch) 和 [Merge](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.merge) 等 node 构建复杂流程。

	[→ 流程逻辑](../flow-logic/README.md)

</div>

### 其他开发者资源 <a href="#other-developer-resources" id="other-developer-resources"></a>

<div class="grid-cards-vertical cards" markdown>

- __n8n API__

	n8n 提供 API，你可以用编程方式执行许多与 GUI 中相同的任务。workflow 中也有一个 [n8n API node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.n8n) 可用于访问 API。

	[→ API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)

- __自托管__

	你可以自托管 n8n。这会让你的数据留在自己的基础设施中。

	[→ 托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)

- __构建自己的 node__

	你可以构建自定义 node，将它们安装到自己的 n8n 实例，并发布到 [npm](https://www.npmjs.com/)。

	[→ 创建 node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview)

</div>

[^1]: 在 n8n 中，expression 允许你通过执行 JavaScript 代码动态填充 node 参数。你不必提供静态值，而是可以使用 n8n expression 语法，通过前序 node、其他 workflow 或 n8n 环境中的数据来定义值。

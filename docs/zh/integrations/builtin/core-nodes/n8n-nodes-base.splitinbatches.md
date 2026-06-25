---
title: Loop Over Items (Split in Batches)
description: >-
  n8n 中 Loop Over Items node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Loop Over Items (Split in Batches)
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches
layout:
  description:
    visible: false
---

# Loop Over Items <a href="#loop-over-items" id="loop-over-items"></a>

Loop Over Items node 可帮助你在需要时循环处理数据。

此 node 会保存原始传入数据，并在每次迭代时通过 **loop** 输出返回预定义数量的数据。

当 node 执行完成时，它会合并所有已处理的数据，并通过 **done** 输出返回。

## 何时使用 Loop Over Items node <a href="#when-to-use-the-loop-over-items-node" id="when-to-use-the-loop-over-items-node"></a>

默认情况下，n8n node 的设计目标是处理输入 item 列表（也有一些例外，下方会详细说明）。根据你想实现的目标，workflow 中通常不需要 Loop Over Items node。你可以在 [n8n 中的循环](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/loop)页面了解 n8n 如何处理多个 item。

以下链接重点介绍了一些适合使用 Loop Over Items node 的场景：

* [循环直到所有 item 都处理完](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/loop#loop-until-all-items-are-processed)：说明 Loop Over Items node 与普通 item 处理有何不同，以及何时可能需要加入此 node。
* [Node 例外](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/loop#node-exceptions)：概述可能需要使用 Loop Over Items node 手动构建循环逻辑的特定场景和 node。
* [避免 rate limiting](../handle-rate-limits.md)：演示如何对 API 请求分批，以避免其他服务的速率限制。

## Node parameters <a href="#node-parameters" id="node-parameters"></a>

### Batch Size <a href="#batch-size" id="batch-size"></a>

输入每次调用要返回的 item 数量。

## Node options <a href="#node-options" id="node-options"></a>

### Reset <a href="#reset" id="reset"></a>

启用后，此 node 会在每次循环时使用当前输入数据重新初始化并重置。当你希望 Loop Over Items node 将传入数据视为一组新数据，而不是前面 item 的延续时，请使用此项。

例如，当你预先不知道需要查询多少页时，可以将启用 reset 选项的 Loop Over Items node 与 [If node](n8n-nodes-base.if.md) 一起使用，查询分页服务。循环会一次查询一页、执行所需处理，并递增页码。循环 reset 可确保循环将每次迭代识别为一组新数据。If node 会评估退出条件，以决定是否执行下一次迭代。

{% hint style="warning" %}
**包含有效的终止条件**

对于上面示例这样的 workflow，为循环包含有效的终止条件非常关键。如果终止条件永远不匹配，workflow 执行会卡在无限循环中。
{% endhint %}

启用后，你可以将参数表示方式从 **Fixed** 切换为 **Expression** 来调整 reset 条件。expression 的求值结果决定此 node 何时重置 item 处理。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Loop Over Items (Split in Batches) 集成模板](https://n8n.io/integrations/split-in-batches)或[搜索所有模板](https://n8n.io/workflows/)

### 从两个不同来源读取 RSS feed <a href="#read-rss-feed-from-two-different-sources" id="read-rss-feed-from-two-different-sources"></a>

此 workflow 允许你使用 Loop Over Items node 从两个不同来源读取 RSS feed。workflow 中需要 Loop Over Items node，因为 RSS Feed Read node 只处理它接收到的第一个 item。你也可以在 n8n.io 上找到该 [workflow](https://n8n.io/workflows/687-read-rss-feed-from-two-different-sources/)。

该示例会逐步说明如何构建 workflow，但假设你已经熟悉 n8n。要构建第一个 workflow，包括学习如何向 workflow 添加 node，请参阅 [Try it out](/try-it-out/index.md)。

最终 workflow 如下所示：

{% @n8n-blocks/n8n-workflow-demo content="%7B%0A%20%20%22nodes%22%3A%20%5B%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.manualTrigger%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%200%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22e6e1cfe6-eff1-48bd-b21c-6ba83d4244d9%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22jsCode%22%3A%20%22return%20%5B%5Cn%5Ct%7B%5Cn%5Ct%5Ctjson%3A%20%7B%5Cn%5Ct%5Ct%5Cturl%3A%20%27https%3A%2F%2Fmedium.com%2Ffeed%2Fn8n-io%27%2C%5Cn%5Ct%5Ct%7D%5Cn%5Ct%7D%2C%5Cn%5Ct%7B%5Cn%5Ct%5Ctjson%3A%20%7B%5Cn%5Ct%5Ct%5Cturl%3A%20%27https%3A%2F%2Fdev.to%2Ffeed%2Fn8n%27%2C%5Cn%5Ct%5Ct%7D%5Cn%5Ct%7D%5Cn%5D%3B%22%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.code%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%202%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20220%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22137f1128-45b6-4bc4-a9fb-8660baa652a9%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Code%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.splitInBatches%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%203%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20440%2C%0A%20%20%20%20%20%20%20%200%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%223449a953-49c2-4a36-ba3d-cbc0573f3f6c%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22Loop%20Over%20Items%22%0A%20%20%20%20%7D%2C%0A%20%20%20%20%7B%0A%20%20%20%20%20%20%22parameters%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%22url%22%3A%20%22%3D%7B%7B%20%24json.url%20%7D%7D%22%2C%0A%20%20%20%20%20%20%20%20%22options%22%3A%20%7B%7D%0A%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%22type%22%3A%20%22n8n-nodes-base.rssFeedRead%22%2C%0A%20%20%20%20%20%20%22typeVersion%22%3A%201.1%2C%0A%20%20%20%20%20%20%22position%22%3A%20%5B%0A%20%20%20%20%20%20%20%20660%2C%0A%20%20%20%20%20%20%20%20100%0A%20%20%20%20%20%20%5D%2C%0A%20%20%20%20%20%20%22id%22%3A%20%22cc2e59d7-0a9b-4640-8052-d8f7f8d8c9fe%22%2C%0A%20%20%20%20%20%20%22name%22%3A%20%22RSS%20Read%22%0A%20%20%20%20%7D%0A%20%20%5D%2C%0A%20%20%22connections%22%3A%20%7B%0A%20%20%20%20%22When%20clicking%20%E2%80%98Execute%20workflow%E2%80%99%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Code%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Code%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Loop%20Over%20Items%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22Loop%20Over%20Items%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%5D%2C%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22RSS%20Read%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%2C%0A%20%20%20%20%22RSS%20Read%22%3A%20%7B%0A%20%20%20%20%20%20%22main%22%3A%20%5B%0A%20%20%20%20%20%20%20%20%5B%0A%20%20%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%22node%22%3A%20%22Loop%20Over%20Items%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22main%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%22index%22%3A%200%0A%20%20%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20%20%20%5D%0A%20%20%20%20%20%20%5D%0A%20%20%20%20%7D%0A%20%20%7D%2C%0A%20%20%22pinData%22%3A%20%7B%7D%2C%0A%20%20%22meta%22%3A%20%7B%0A%20%20%20%20%22instanceId%22%3A%20%22cb484ba7b742928a2048bf8829668bed5b5ad9787579adea888f05980292a4a7%22%0A%20%20%7D%0A%7D%0A" url="https://raw.githubusercontent.com/n8n-io/n8n-docs/refs/heads/main/docs/_workflows/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches/rss-feed-example.json" %}

复制上面的 workflow 文件并粘贴到你的 instance 中，或按照以下步骤手动构建：

1. 添加 manual trigger。
2. 添加 Code node。
3. 将此代码复制到 Code node 中：
	```js
	return [
		{
			json: {
				url: 'https://medium.com/feed/n8n-io',
			}
		},
		{
			json: {
				url: 'https://dev.to/feed/n8n',
			}
		}
	];
	```
4. 添加 Loop Over Items node。
5. 配置 Loop Over Items：在 **Batch Size** 字段中将批大小设置为 `1`。
6. 添加 RSS Feed Read node。
7. 选择 **Execute Workflow**。这会运行 workflow，将数据加载到 RSS Feed Read node 中。
8. 配置 RSS Feed Read：将输入中的 `url` 映射到 **URL** 字段。你可以从 **INPUT** 面板拖放完成，也可以使用此 expression：`{{ $json.url }}`。
9. 选择 **Execute Workflow** 运行 workflow 并查看结果数据。

### 检查 node 是否已处理所有 item <a href="#check-that-the-node-has-processed-all-items" id="check-that-the-node-has-processed-all-items"></a>

要检查此 node 是否仍有 item 需要处理，请使用以下 expression：`{{$("Loop Over Items").context["noItemsLeft"]}}`。此 expression 返回布尔值。如果此 node 仍有数据需要处理，该 expression 返回 `false`，否则返回 `true`。

### 获取 node 当前运行索引 <a href="#get-the-current-running-index-of-the-node" id="get-the-current-running-index-of-the-node"></a>

要获取此 node 的当前运行索引，请使用以下 expression：`{{$("Loop Over Items").context["currentRunIndex"];}}`。

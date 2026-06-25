---
contentType: howto
nodeTitle: Loop
originalFilePath: flow-logic/looping.md
originalUrl: 'https://docs.n8n.io/flow-logic/looping'
url: 'https://docs.n8n.io/build/flow-logic/loop'
layout:
  description:
    visible: false
---

# n8n 中的循环 <a href="#looping-in-n8n" id="looping-in-n8n"></a>

当你想处理多个 items，或重复执行某个动作时，循环很有用，例如给通讯录里的每个联系人发送消息。n8n 会自动处理这种重复处理，这意味着你不需要专门在工作流中构建循环。不过，[某些节点](#node-exceptions)例外。

## 在 n8n 中使用循环 <a href="#using-loops-in-n8n" id="using-loops-in-n8n"></a>

n8n 节点可以接收任意数量的 items 作为输入，处理这些 items，并输出结果。你可以把每个 item 理解为一个单独的数据点，或节点输出表中的一行。

![Customer Datastore 节点输出](../../../build/.gitbook/assets/customer_datastore_node.png)

节点通常会针对每个 item 运行一次。例如，如果你想把 Customer Datastore 节点中客户的姓名和备注作为 Slack 消息发送，你会：

1. 将 Slack 节点连接到 Customer Datastore 节点。
2. 配置参数。
3. 执行节点。

你会收到五条消息：每个 item 一条。

这就是你无需显式地将节点连接成循环，也能处理多个 items 的方式。

### 只执行节点一次 <a href="#executing-nodes-once" id="executing-nodes-once"></a>

在不希望节点处理所有接收 items 的情况下，例如只给第一个客户发送 Slack 消息，可以在该节点的 **Settings** 选项卡中开启 **Execute Once** 参数。这个设置适用于传入数据包含多个 items，而你只想处理第一个 item 的场景。


## 创建循环 <a href="#creating-loops" id="creating-loops"></a>

n8n 通常会自动迭代所有传入 items。不过，在某些场景中，你必须创建循环来遍历所有 items。不会自动遍历所有传入 items 的节点列表，请参阅 [Node exceptions](#node-exceptions)。

### 循环直到满足条件 <a href="#loop-until-a-condition-is-met" id="loop-until-a-condition-is-met"></a>

要在 n8n 工作流中创建循环，可以将一个节点的输出连接到前面某个节点的输入。添加 [IF](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 节点，用于检查何时停止循环。

下面是一个使用 `IF` 节点实现循环的[示例工作流](https://n8n.io/workflows/1130)：

![示例工作流的编辑器 UI 视图](../../../build/.gitbook/assets/example_workflow.png)

### 循环直到所有 items 都处理完 <a href="#loop-until-all-items-are-processed" id="loop-until-all-items-are-processed"></a>

当你想循环直到处理完所有 items 时，请使用 [Loop Over Items](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.splitinbatches) 节点。要逐个处理每个 item，请将 **Batch Size** 设置为 `1`。

你可以将数据按组分批，并处理这些批次。处理大量传入数据时，或你想处理返回 items 中的特定分组时，这种方式有助于避免 API 速率限制。

Loop Over Items 节点会在所有传入 items 被拆分成批次并传给工作流中的下一个节点后停止执行，因此不需要再添加 IF 节点来停止循环。

## 节点例外 <a href="#node-exceptions" id="node-exceptions"></a>

以下节点和操作需要你在工作流中设计循环：

* [CrateDB](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.cratedb) 对 `insert` 和 `update` 只执行一次。
* [Code](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) node 在 **Run Once for All Items** 模式下：根据输入的代码片段处理所有 items。
* [Execute Workflow](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflow) node 在 **Run Once for All Items** 模式下。
* [HTTP Request](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.httprequest)：必须自行处理分页。如果 API 调用返回分页结果，必须创建循环以一次获取一页。
* [Microsoft SQL](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.microsoftsql) 对 `insert`、`update` 和 `delete` 只执行一次。
* [MongoDB](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.mongodb) 对 `insert` 和 `update` 只执行一次。
* [QuestDB](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.questdb) 对 `insert` 只执行一次。
* [Redis](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.redis)：
	* Info：无论传入数据中有多少 items，此操作都只执行一次。
* [RSS Read](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.rssfeedread) 对请求的 URL 只执行一次。
* [TimescaleDB](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/app-nodes/n8n-nodes-base.timescaledb) 对 `insert` 和 `update` 只执行一次。

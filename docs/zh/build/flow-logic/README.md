---
title: 流程逻辑
description: 如何在 n8n 工作流中表达逻辑。
contentType: overview
nodeTitle: Flow logic
originalFilePath: flow-logic/index.md
originalUrl: 'https://docs.n8n.io/flow-logic'
url: 'https://docs.n8n.io/build/'
layout:
  description:
    visible: false
---

# 流程逻辑 <a href="#flow-logic" id="flow-logic"></a>

n8n 允许你在工作流中表达复杂逻辑。

## 相关章节 <a href="#related-sections" id="related-sections"></a>

你需要对 n8n 中的[数据](../work-with-data/overview.md)有一些了解，包括[数据结构](../work-with-data/understand-n8ns-data-structure.md)和[节点内的数据流](../work-with-data/understand-n8ns-data-structure.md#how-data-flows-within-nodes)。

构建逻辑时，你会使用 n8n 的 [Core nodes](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes)，包括：

* 分支：[IF](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 和 [Switch](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.switch)。
* 合并：[Merge](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.merge)、[Compare Datasets](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.comparedatasets) 和 [Code](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code)。
* 循环：[IF](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 和 [Loop Over Items](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.splitinbatches)。
* 等待：[Wait](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait)。
* 创建子工作流：[Execute Workflow](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflow) 和 [Execute Workflow Trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger)。
* 错误处理：[Stop And Error](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.stopanderror) 和 [Error Trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.errortrigger)。

---
description: 使用 If 和 Switch 将工作流拆分成多条路径
contentType: howto
nodeTitle: Split with conditionals
originalFilePath: flow-logic/splitting.md
originalUrl: 'https://docs.n8n.io/flow-logic/splitting'
url: 'https://docs.n8n.io/build/flow-logic/split-with-conditionals'
layout:
  description:
    visible: false
---

# 使用条件节点拆分工作流 <a href="#splitting-workflows-with-conditional-nodes" id="splitting-workflows-with-conditional-nodes"></a>

拆分使用 [IF](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 或 [Switch](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.switch) 节点。它会将单分支工作流变成多分支工作流。这是在 n8n 中表达复杂逻辑的关键部分。

比较以下两个工作流：

!["表示两个工作流的图示。一个有三个步骤，并按线性流程运行：用户提交 bug，然后工作流给支持团队发邮件。第二个工作流以相同方式开始，但会根据用户是否将问题标记为紧急而拆分，然后又根据用户的支持方案再次拆分。"](../../../build/.gitbook/assets/single-multi-branch-workflow.png)

这就是 n8n 中拆分和条件节点的能力。

用法详情请参阅 [IF](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.if) 或 [Switch](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.switch) 文档。

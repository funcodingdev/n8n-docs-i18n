---
title: 多分支工作流中的执行顺序
description: n8n 如何决定多分支工作流中的节点执行顺序。
contentType: explanation
nodeTitle: Understand execution order
originalFilePath: flow-logic/execution-order.md
originalUrl: 'https://docs.n8n.io/flow-logic/execution-order'
url: 'https://docs.n8n.io/build/flow-logic/understand-execution-order'
layout:
  description:
    visible: false
---

# 多分支工作流中的执行顺序 <a href="#execution-order-in-multi-branch-workflows" id="execution-order-in-multi-branch-workflows"></a>

n8n 的节点执行顺序取决于你使用的 n8n 版本：

* 对于 1.0 版本之前创建的工作流：n8n 会先执行每个分支的第一个节点，再执行每个分支的第二个节点，以此类推。
* 对于 1.0 及以上版本创建的工作流：n8n 会依次执行每个分支，完成一个分支后再开始另一个分支。n8n 会根据分支在画布[^1]上的位置排序，从最上方到最下方执行。如果两个分支高度相同，则先执行最左侧的分支。

你可以在[工作流设置](../manage-workflows/configure-workflow-settings.md)中更改执行顺序。

[^1]: Canvas 是 n8n editor UI 中构建工作流的主界面。你可以在 canvas 上添加并连接节点来编排工作流。

---
title: 提示和常见问题
description: >-
  了解如何设置特定用例，并处理 workflow evaluation 中的常见问题。
contentType: reference
nodeTitle: 修复常见问题
originalFilePath: advanced-ai/evaluations/tips-and-common-issues.md
originalUrl: 'https://docs.n8n.io/advanced-ai/evaluations/tips-and-common-issues'
url: >-
  https://docs.n8n.io/build/integrate-ai/test-and-improve-ai-workflows/fix-common-issues
layout:
  description:
    visible: false
---

# 提示和常见问题 <a href="#tips-and-common-issues" id="tips-and-common-issues"></a>

## 合并多个 trigger <a href="#combining-multiple-triggers" id="combining-multiple-triggers"></a>

如果工作流中已经有另一个 trigger，你就会有两个潜在起点：该 trigger 和 [evaluation trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.evaluationtrigger)。为了确保无论哪个 trigger 执行，工作流都按预期工作，你需要将这些分支合并在一起。

<figure>
<img src="../../.gitbook/assets/merging-trigger-branches.png" alt="">
<figcaption>将两个 trigger 分支合并在一起的逻辑，使它们具有相同的数据格式，并且可以从单个节点引用。</figcaption>
</figure>

操作步骤：

1. **获取另一个 trigger 的数据格式**：
	* 执行另一个 trigger。
    * 打开它，并进入输出面板的 JSON 视图。
    * 点击右侧的 **copy** 按钮。
2. **重新整理 evaluation trigger 数据以匹配格式**：
    * 在 evaluation trigger 后插入一个 [Edit Fields (Set) node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.set)，并将它们连接起来。
    * 将其模式改为 **JSON**。
    * 将数据粘贴到 `JSON` 字段中，移除第一行和最后一行的 `[` 和 `]`。
    * 将字段类型切换为 **Expression**。
    * 从输入面板拖拽 trigger 数据，将其映射进来。
    * 对于字符串，请确保替换整个值（包括引号），并在 expression 末尾添加 `.toJsonString()`。
3. **使用 `No-op` 节点合并分支**：插入一个 [No-op node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.noop)，并将另一个 trigger 和 Set 节点都连接到它。`No-op` 节点只会输出它收到的任何输入。
4. **在工作流其余部分引用 `No-op` 节点输出**：由于两条路径都会以相同格式流经此节点，你可以确定输入数据始终存在。

## 避免 evaluation 破坏聊天 <a href="#avoiding-evaluation-breaking-the-chat" id="avoiding-evaluation-breaking-the-chat"></a>

n8n 的内部聊天会读取工作流中最后执行节点的输出数据。添加带有 [`set outputs` 操作](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.evaluation#set-outputs)的 evaluation 节点后，这些数据可能不是预期格式，甚至可能不包含聊天响应。

![添加第二个输出分支](../../.gitbook/assets/add-second-output-branch.png)

解决方法是从 agent 额外添加一个分支。在 n8n 中，[下方分支会更晚执行](../../flow-logic/understand-execution-order.md)，这意味着你附加到此分支的任何节点都会最后执行。这里可以使用 no-op 节点，因为它只需要透传 agent 输出。

## 计算 metric 时访问 tool 数据 <a href="#accessing-tool-data-when-calculating-metrics" id="accessing-tool-data-when-calculating-metrics"></a>

有时你需要知道 agent 已执行的 sub-node 中发生了什么，例如检查它是否执行了某个 tool。你不能用 expression 直接引用这些节点，但可以在 agent 中启用 **Return intermediate steps** 选项。这会添加一个名为 `intermediateSteps` 的额外输出字段，供后续节点使用：

![启用 return intermediate steps](../../.gitbook/assets/enable-return-intermediate-steps.png)

## 同一工作流中的多个 evaluation <a href="#multiple-evaluations-in-the-same-workflow" id="multiple-evaluations-in-the-same-workflow"></a>

每个工作流只能设置一个 evaluation。换句话说，每个工作流只能有一个 evaluation trigger。

即便如此，你仍然可以将工作流的不同部分放入 [sub-workflow](../../flow-logic/break-workflows-into-smaller-parts.md)，然后分别评估每个 sub-workflow，从而用不同 evaluation 测试工作流的不同部分。

## 处理不一致结果 <a href="#dealing-with-inconsistent-results" id="dealing-with-inconsistent-results"></a>

Metric 经常会有噪声：对完全相同的工作流运行多次 evaluation 时，它们可能不同。这是因为工作流本身可能返回不同结果，或者任何基于 LLM 的 metric 都可能存在自然波动。

你可以通过复制数据集中的行来补偿这一点，让每一行在数据集中出现多次。由于这意味着每个输入实际上会运行多次，因此可以平滑掉一些波动。

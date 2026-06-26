---
contentType: explanation
nodeTitle: Understand concurrency
originalFilePath: manage-cloud/concurrency.md
originalUrl: 'https://docs.n8n.io/manage-cloud/concurrency'
url: 'https://docs.n8n.io/deploy/use-n8n-cloud/understand-concurrency'
layout:
  description:
    visible: false
---

# Cloud 并发 <a href="#cloud-concurrency" id="cloud-concurrency"></a>

{% hint style="info" %}
**仅适用于 n8n Cloud**

本文讨论 n8n Cloud 中的并发。阅读[自托管 n8n 并发控制](../host-n8n/configure-n8n/scaling/control-concurrency.md)，了解并发如何在自托管 n8n 实例中工作。
{% endhint %}

过多 concurrent executions 可能导致性能下降和无响应。为防止这种情况并提升实例稳定性，n8n 会在 regular mode 下为 production executions 设置 concurrency limits。

超过限制的 executions 会排队等待后续处理。这些 executions 会保留在队列中，直到释放 concurrency capacity，然后按 FIFO 顺序处理。

## 并发限制 <a href="#concurrency-limits" id="concurrency-limits"></a>

n8n 会根据 Cloud 实例的 plan 限制 concurrent executions 数量。详情请参阅 [Pricing](https://n8n.io/pricing/)。

你可以在项目或 workflow 的 executions tab 顶部查看 active executions 数量以及你的 plan 的 concurrency limit。

## 详细信息 <a href="#details" id="details"></a>

关于并发，还需要记住一些其他细节：

- Concurrency control 只适用于 production executions：即由 webhook 或 trigger node 启动的 executions。它不适用于其他类型，例如 manual executions、sub-workflow executions 或 error executions。
- [Test evaluations](#user-content-fn-1)[^1] 不计入 production concurrency limits。它们使用单独的按 plan 划分的限制，用于控制单次 test run 中可并行运行多少 test cases：Community 和 Pro 为 1（顺序执行），Business 为 3，Enterprise 为 5。你可以在 **Run Test** popover 中调整某次运行的值。详情请参阅 [Metric-based evaluations](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality#run-test-cases-in-parallel)。
- 你无法重试 queued executions。取消或删除 queued execution 也会将它从队列中移除。
- 实例启动时，n8n 会在 concurrency limit 范围内恢复 queued executions，并将其余 executions 重新入队。

## 与 queue mode 对比 <a href="#comparison-to-queue-mode" id="comparison-to-queue-mode"></a>

{% hint style="info" %}
**功能可用性**

Queue mode 可用于 Cloud Enterprise plans。要启用它，请[联系 n8n](https://n8n-community.typeform.com/to/y9X2YuGa)。
{% endhint %}

queue mode 中的 concurrency 与 regular mode 中的 concurrency 是不同机制。在 queue mode 中，concurrency settings 决定每个 worker 可以并行运行多少 jobs。在 regular mode 中，concurrency limits 适用于整个实例。

[^1]: 在 n8n 中，evaluation 允许你标记和整理 execution history，并将其与新的 executions 进行比较。你可以用它了解 workflow 在你不断修改时的表现。它在开发以 AI 为中心的 workflows 时尤其有用。

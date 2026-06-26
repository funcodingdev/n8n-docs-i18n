---
contentType: explanation
nodeTitle: Control concurrency
originalFilePath: hosting/scaling/concurrency-control.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/concurrency-control'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/control-concurrency'
layout:
  description:
    visible: false
---

# Self-hosted concurrency control <a href="#self-hosted-concurrency-control" id="self-hosted-concurrency-control"></a>

{% hint style="info" %}
**仅适用于 self-hosted n8n**

本文档适用于 self-hosted concurrency control。请阅读 [Cloud concurrency](../../../use-n8n-cloud/understand-concurrency.md)，了解 n8n Cloud accounts 中 concurrency 如何工作。
{% endhint %}

在 regular mode 中，n8n 不限制可同时运行多少个 production executions。这可能导致过多 concurrent executions 冲击 event loop，引发性能下降和无响应。

为防止这种情况，你可以为 regular mode 中的 production executions 设置 concurrency limit。用它来控制 production executions 的并发运行数量，并将超过限制的 concurrent production executions 排队。这些 executions 会留在 queue 中，直到 concurrency capacity 释放，然后按 FIFO 顺序处理。

Concurrency control 默认禁用。要启用它：

```sh
export N8N_CONCURRENCY_PRODUCTION_LIMIT=20
```

注意：

- Concurrency control 只适用于 production executions：由 webhook 或 trigger[^1] node 启动的 executions。它不适用于其他类型，例如 manual executions、sub-workflow executions、error executions，或从 CLI 启动的 executions。
- 不能 retry queued executions。取消或删除 queued execution 也会将其从 queue 中移除。
- 实例启动时，n8n 会恢复不超过 concurrency limit 的 queued executions，并将其余部分重新入队。
- 要监控 concurrency control，请查看 logs，关注 executions 被添加到 queue 和被释放的记录。在未来版本中，n8n 会在 UI 中显示 concurrency control。

启用 concurrency control 后，你可以在 project 或 workflow 的 executions tab 顶部查看 active executions 数量和配置的 limit。

## 与 queue mode 对比 <a href="#comparison-to-queue-mode" id="comparison-to-queue-mode"></a>

在 queue mode 中，你可以使用 [`--concurrency` flag](enable-queue-mode.md#configure-worker-concurrency) 控制 worker 可并发运行多少 jobs。

queue mode 中的 concurrency control 与 regular mode 中的 concurrency control 是不同机制，但环境变量 `N8N_CONCURRENCY_PRODUCTION_LIMIT` 同时控制二者。在 queue mode 中，如果该变量设置为非 `-1` 的值，n8n 会从该变量获取 limit；否则回退到 `--concurrency` flag 或其默认值。

## Evaluation concurrency <a href="#evaluation-concurrency" id="evaluation-concurrency"></a>

Evaluation 测试运行使用与 production executions 不同的独立 concurrency limit。默认情况下，该 limit 遵循实例的 license tier（Community/Pro 为 1，Business 为 3，Enterprise 为 5）。可通过 [`N8N_CONCURRENCY_EVALUATION_LIMIT`](../basic-configuration/use-environment-variables/executions.md) 覆盖。关于 UI 中 slider 的行为，请参考 [Metric-based evaluations](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality#run-test-cases-in-parallel)。

[^1]: Trigger node 是负责在满足特定条件时执行 workflow 的特殊 node。所有 production workflows 都至少需要一个 trigger 来决定 workflow 何时运行。

---
title: Enable Prometheus metrics
description: 启用 Prometheus metrics endpoint。
contentType: howto
nodeTitle: Enable Prometheus metrics
originalFilePath: hosting/configuration/configuration-examples/prometheus.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/prometheus'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics
layout:
  description:
    visible: false
---

# 启用 Prometheus metrics <a href="#enable-prometheus-metrics" id="enable-prometheus-metrics"></a>

为了收集和暴露 metrics，n8n 使用 [prom-client](https://www.npmjs.com/package/prom-client) library。

`/metrics` endpoint 默认禁用，但可以使用 `N8N_METRICS` 环境变量启用。

{% hint style="warning" %}
**不要公开暴露 metrics endpoint**

只向消耗 Prometheus data 的内部服务暴露 `/metrics` endpoint。不要让它可从 public internet 访问，因为它可能泄露关于 n8n instance 的敏感运营数据。
{% endhint %}

```bash
export N8N_METRICS=true
```

有关配置应暴露哪些 metrics 和 labels，请参阅对应的 [Environment Variables](../use-environment-variables/endpoints.md)（`N8N_METRICS_INCLUDE_*`）。

`main` 和 `worker` instances 都可以暴露 metrics。

有关将 Grafana 连接到 Prometheus 以可视化 n8n metrics 的指导，请参阅 [Grafana](../../../keep-n8n-running/visualize-metrics-with-grafana.md)。

## Queue metrics <a href="#queue-metrics" id="queue-metrics"></a>

要启用 queue metrics，请将 `N8N_METRICS_INCLUDE_QUEUE_METRICS` env var 设置为 `true`。你可以使用 `N8N_METRICS_QUEUE_METRICS_INTERVAL` 调整 refresh rate。

n8n 从 Bull 收集这些 metrics，并在 main instances 上暴露它们。在 multi-main setups 上聚合查询时，可以使用 `instance_role_leader` gauge 识别 leader；leader main 设为 `1`，否则设为 `0`。

```
# HELP n8n_scaling_mode_queue_jobs_active Current number of jobs being processed across all workers in scaling mode. <a href="#help-n8nscalingmodequeuejobsactive-current-number-of-jobs-being-processed-across-all-workers-in-scaling-mode" id="help-n8nscalingmodequeuejobsactive-current-number-of-jobs-being-processed-across-all-workers-in-scaling-mode"></a>
# TYPE n8n_scaling_mode_queue_jobs_active gauge <a href="#type-n8nscalingmodequeuejobsactive-gauge" id="type-n8nscalingmodequeuejobsactive-gauge"></a>
n8n_scaling_mode_queue_jobs_active 0

# HELP n8n_scaling_mode_queue_jobs_completed Total number of jobs completed across all workers in scaling mode since instance start. <a href="#help-n8nscalingmodequeuejobscompleted-total-number-of-jobs-completed-across-all-workers-in-scaling-mode-since-instance-start" id="help-n8nscalingmodequeuejobscompleted-total-number-of-jobs-completed-across-all-workers-in-scaling-mode-since-instance-start"></a>
# TYPE n8n_scaling_mode_queue_jobs_completed counter <a href="#type-n8nscalingmodequeuejobscompleted-counter" id="type-n8nscalingmodequeuejobscompleted-counter"></a>
n8n_scaling_mode_queue_jobs_completed 0

# HELP n8n_scaling_mode_queue_jobs_failed Total number of jobs failed across all workers in scaling mode since instance start. <a href="#help-n8nscalingmodequeuejobsfailed-total-number-of-jobs-failed-across-all-workers-in-scaling-mode-since-instance-start" id="help-n8nscalingmodequeuejobsfailed-total-number-of-jobs-failed-across-all-workers-in-scaling-mode-since-instance-start"></a>
# TYPE n8n_scaling_mode_queue_jobs_failed counter <a href="#type-n8nscalingmodequeuejobsfailed-counter" id="type-n8nscalingmodequeuejobsfailed-counter"></a>
n8n_scaling_mode_queue_jobs_failed 0

# HELP n8n_scaling_mode_queue_jobs_waiting Current number of enqueued jobs waiting for pickup in scaling mode. <a href="#help-n8nscalingmodequeuejobswaiting-current-number-of-enqueued-jobs-waiting-for-pickup-in-scaling-mode" id="help-n8nscalingmodequeuejobswaiting-current-number-of-enqueued-jobs-waiting-for-pickup-in-scaling-mode"></a>
# TYPE n8n_scaling_mode_queue_jobs_waiting gauge <a href="#type-n8nscalingmodequeuejobswaiting-gauge" id="type-n8nscalingmodequeuejobswaiting-gauge"></a>
n8n_scaling_mode_queue_jobs_waiting 0
```

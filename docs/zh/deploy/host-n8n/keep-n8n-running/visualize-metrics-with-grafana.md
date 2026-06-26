---
contentType: howto
nodeTitle: Visualize metrics with Grafana
originalFilePath: hosting/logging-monitoring/grafana.md
originalUrl: 'https://docs.n8n.io/hosting/logging-monitoring/grafana'
url: >-
  https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/visualize-metrics-with-grafana
layout:
  description:
    visible: false
---

# Grafana <a href="#grafana" id="grafana"></a>

在 n8n 中启用 Prometheus metrics endpoint，然后通过 Prometheus instance 连接 Grafana，以 visualize 你的 n8n data。继续本指南前，请先参考 [Enable Prometheus metrics](../configure-n8n/basic-configuration/configuration-examples/enable-prometheus-metrics.md)。

{% hint style="info" %}
**功能可用性**

`/metrics` endpoint 在 n8n Cloud 上不可用。
{% endhint %}

## 可复用 dashboard templates <a href="#reusable-dashboard-templates" id="reusable-dashboard-templates"></a>

为 n8n instance 启用 Prometheus metrics 后，你会想构建 dashboards 来 observe 它们。

n8n 在这个 GitHub project 中为多个 supported prometheus metrics 发布了 reusable grafana dashboards：
[n8n-observability](https://github.com/n8n-io/n8n-observability)

## 配置 Prometheus scrape n8n <a href="#configure-prometheus-to-scrape-n8n" id="configure-prometheus-to-scrape-n8n"></a>

Prometheus 会按 schedule scrape n8n 的 `/metrics` endpoint 并存储 data。Grafana 随后 query Prometheus 来显示这些 data。

在你的 `prometheus.yml` 中添加一个指向 n8n instance 的 scrape job：

```yaml
scrape_configs:
  - job_name: n8n
    static_configs:
      - targets:
          - <n8n-host>:<n8n-port>
    metrics_path: /metrics
```

将 `<n8n-host>` 和 `<n8n-port>` 替换为你的 n8n instance address。n8n 默认 port 是 `5678`。

编辑后，reload 或 restart Prometheus 以应用更改。

## 将 Prometheus 添加为 Grafana data source <a href="#add-prometheus-as-a-grafana-data-source" id="add-prometheus-as-a-grafana-data-source"></a>

1. 在 Grafana 中，前往 **Connections** > **Data sources**。
2. 选择 **Add new data source**。
3. 选择 **Prometheus**。
4. 将 **Prometheus server URL** 设置为你的 Prometheus instance address，例如 `http://prometheus:9090`。
5. 选择 **Save & test**。

Grafana 会用 success message 确认 connection。

## Webhook observability <a href="#webhook-observability" id="webhook-observability"></a>

从 n8n version 2.28.0 起可用。

n8n 会为每次 webhook call 暴露 `n8n_webhook_request_duration_seconds` histogram。启用这些 environment variables 来收集它：

| Variable | Default | Description |
|----------|---------|-------------|
| `N8N_METRICS_INCLUDE_WEBHOOK_METRICS` | `false` | 暴露 `n8n_webhook_request_duration_seconds` histogram。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_INFO` | `false` | 暴露用于 human-readable workflow names 的 `n8n_workflow_info` gauge。请参阅 [Workflow name lookup](#workflow-name-lookup)。 |

你可以在 n8n-observability project 中找到这个 histogram 的 [ready-to-use dashboard](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-webhook-executions)。

### Metric 跟踪什么 <a href="#what-the-metric-tracks" id="what-the-metric-tracks"></a>

`n8n_webhook_request_duration_seconds` 是 Prometheus histogram。对于每个 webhook call，n8n 会记录 request 耗时（从 "request received" 到 "response sent"）。该 metric 为每个 label combination 暴露三个 series：

| Series | Description |
|--------|-------------|
| `_bucket{le="<bound>"}` | 在 `<bound>` 秒内完成的 requests 累计数量。 |
| `_sum` | 所有 requests 花费的总秒数。 |
| `_count` | Requests 总数。 |

每个 series 都携带这些 labels：

| Label | Example | Description |
|-------|---------|-------------|
| `method` | `GET` | Incoming request 的 HTTP method。 |
| `status_code` | `200` | n8n 返回的 HTTP status code。 |
| `webhook_path` | `294febd8-...` | 标识 webhook endpoint 的 UUID path。 |
| `workflow_id` | `KhcGg7EmAMoa7Bmv` | webhook 所属 workflow 的 ID。 |

### Dashboard ideas <a href="#dashboard-ideas" id="dashboard-ideas"></a>

| Panel | PromQL |
|-------|--------|
| 每个 workflow 的 request rate | `sum by (workflow_id) (rate(n8n_webhook_request_duration_seconds_count[5m]))` |
| 所有 webhooks 的 p95 latency | `histogram_quantile(0.95, sum by (le) (rate(n8n_webhook_request_duration_seconds_bucket[5m])))` |
| 每个 workflow 的 p95 latency | `histogram_quantile(0.95, sum by (le, workflow_id) (rate(n8n_webhook_request_duration_seconds_bucket[5m])))` |
| Error rate（non-2xx） | `sum by (workflow_id) (rate(n8n_webhook_request_duration_seconds_count{status_code!="2.."}[5m]))` |
| Average request duration | `rate(n8n_webhook_request_duration_seconds_sum[5m]) / rate(n8n_webhook_request_duration_seconds_count[5m])` |

## Form submission observability <a href="#form-submission-observability" id="form-submission-observability"></a>

从 n8n version 2.28.0 起可用。

n8n 会为每次 form submission 暴露 `n8n_form_submission_duration_seconds` histogram。启用这些 environment variables 来收集它：

| Variable | Default | Description |
|----------|---------|-------------|
| `N8N_METRICS_INCLUDE_FORM_METRICS` | `false` | 暴露 `n8n_form_submission_duration_seconds` histogram。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_INFO` | `false` | 暴露用于 human-readable workflow names 的 `n8n_workflow_info` gauge。请参阅 [Workflow name lookup](#workflow-name-lookup)。 |

你可以在 n8n-observability project 中找到这个 histogram 的 [ready-to-use dashboard](https://github.com/n8n-io/n8n-observability/tree/main/dashboards/grafana/n8n-form-executions)。

### Metric 跟踪什么 <a href="#what-the-metric-tracks" id="what-the-metric-tracks"></a>

`n8n_form_submission_duration_seconds` 是 Prometheus histogram。对于每次 form submission，n8n 会记录从 "user pressing submit" 到 "user getting feedback on form submission" 的耗时。该 metric 为每个 label combination 暴露三个 series：

| Series | Description |
|--------|-------------|
| `_bucket{le="<bound>"}` | 在 `<bound>` 秒内完成的 submissions 累计数量。 |
| `_sum` | 处理所有 submissions 花费的总秒数。 |
| `_count` | Submissions 总数。 |

每个 series 都携带这些 labels：

| Label | Example | Description |
|-------|---------|-------------|
| `status_code` | `200` | n8n 返回的 HTTP status code。 |
| `form_path` | `b395d2e2-...` | 标识 form endpoint 的 UUID path。 |
| `workflow_id` | `qTzTyGlEROwSuVlY` | form 所属 workflow 的 ID。 |

{% hint style="info" %}
**无 method label**

Form submissions 不包含 `method` label，因为 n8n 只通过 `POST` 接收 form data。
{% endhint %}

### Dashboard ideas <a href="#dashboard-ideas" id="dashboard-ideas"></a>

| Panel | PromQL |
|-------|--------|
| 每个 workflow 的 submission rate | `sum by (workflow_id) (rate(n8n_form_submission_duration_seconds_count[5m]))` |
| 所有 forms 的 p95 processing time | `histogram_quantile(0.95, sum by (le) (rate(n8n_form_submission_duration_seconds_bucket[5m])))` |
| 每个 workflow 的 p95 processing time | `histogram_quantile(0.95, sum by (le, workflow_id) (rate(n8n_form_submission_duration_seconds_bucket[5m])))` |
| Error rate（non-2xx） | `sum by (workflow_id) (rate(n8n_form_submission_duration_seconds_count{status_code!="2.."}[5m]))` |
| Average processing duration | `rate(n8n_form_submission_duration_seconds_sum[5m]) / rate(n8n_form_submission_duration_seconds_count[5m])` |

## Workflow name lookup <a href="#workflow-name-lookup" id="workflow-name-lookup"></a>

从 n8n version 2.28.0 起可用。

启用 `N8N_METRICS_INCLUDE_WORKFLOW_INFO` 后，n8n 会为每个 workflow 暴露一个 gauge：

```
n8n_workflow_info{workflow_id="VaQPuPmx9tPpo6BX",workflow_name="My workflow"} 1
```

通过 `workflow_id` 将它 join 到任何其他 n8n metric 上，可以在 Grafana panels 中把 opaque IDs 替换为 human-readable names。例如，要按 workflow name 显示 webhook request rate：

```promql
sum by (workflow_name) (
  rate(n8n_webhook_request_duration_seconds_count[5m])
  * on(workflow_id) group_left(workflow_name)
  n8n_workflow_info
)
```

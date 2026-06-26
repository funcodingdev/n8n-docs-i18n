---
description: 获取 health check metrics
contentType: howto
nodeTitle: Monitor n8n
originalFilePath: hosting/logging-monitoring/monitoring.md
originalUrl: 'https://docs.n8n.io/hosting/logging-monitoring/monitoring'
url: 'https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/monitor-n8n'
layout:
  description:
    visible: false
---

# Monitoring <a href="#monitoring" id="monitoring"></a>

你可以调用三个 API endpoints 来检查 instance status：`/healthz`、`healthz/readiness` 和 `/metrics`。

## healthz 和 healthz/readiness <a href="#healthz-and-healthzreadiness" id="healthz-and-healthzreadiness"></a>

`/healthz` endpoint 返回标准 HTTP status code。200 表示 instance 可访问。它不表示 DB status。Self-hosted 和 Cloud users 都可以使用。

访问 endpoint：

```
<your-instance-url>/healthz
```

`/healthz/readiness` endpoint 与 `/healthz` endpoint 类似，但只有当 DB 已连接且已 migrated，因此 instance 准备好接收 traffic 时，它才会返回 HTTP status code 200。

访问 endpoint：

```
<your-instance-url>/healthz/readiness
```

{% hint style="info" %}
**自定义 health check endpoints**

你可以使用 [`N8N_ENDPOINT_HEALTH`](../configure-n8n/basic-configuration/use-environment-variables/endpoints.md) environment variable 自定义 health check endpoint path。
{% endhint %}

## metrics <a href="#metrics" id="metrics"></a>

`/metrics` endpoint 提供关于 instance 当前 status 的更详细信息。

访问 endpoint：

```
<your-instance-url>/metrics
```

{% hint style="info" %}
**功能可用性**

`/metrics` endpoint 在 n8n Cloud 上不可用。
{% endhint %}

## 为 self-hosted n8n 启用 metrics 和 health checks <a href="#enable-metrics-and-health-checks-for-self-hosted-n8n" id="enable-metrics-and-health-checks-for-self-hosted-n8n"></a>

`/metrics` endpoint 默认禁用。主 n8n server 上始终启用 health endpoint。对于 [queue mode](../configure-n8n/scaling/enable-queue-mode.md) 中的 worker servers，health endpoint 默认禁用。

要启用它们，请配置你的 n8n instance：

```shell
# metrics <a href="#metrics" id="metrics"></a>
N8N_METRICS=true
# healthz <a href="#healthz" id="healthz"></a>
QUEUE_HEALTH_CHECK_ACTIVE=true
```

有关如何使用 environment variables 配置 instance 的更多信息，请参考 [Configuration methods](../configure-n8n/basic-configuration.md)。

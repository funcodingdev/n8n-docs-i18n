---
contentType: howto
nodeTitle: Enable queue mode
originalFilePath: hosting/scaling/queue-mode.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/queue-mode'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode'
layout:
  description:
    visible: false
---

# Queue mode <a href="#queue-mode" id="queue-mode"></a>

你可以根据需求以不同模式运行 n8n。queue mode 提供最佳可扩展性。

{% hint style="info" %}
**Binary data 存储**

n8n 不支持在 queue mode 中使用 filesystem binary data storage。如果你的 workflows 需要在 queue mode 中持久化 binary data，可以使用 [S3 external storage](use-external-storage.md)。
{% endhint %}

## 工作原理 <a href="#how-it-works" id="how-it-works"></a>

以 queue mode 运行时，你会设置多个 n8n instances，其中一个 main instance 接收 workflow information（例如 triggers），worker instances 负责执行。

每个 worker 都是自己的 Node.js instance，以 `main` mode 运行，但由于高 IOPS（input-output operations per second），可以处理多个同时进行的 workflow executions。

通过使用 worker instances 并以 queue mode 运行，你可以根据 workload 需要横向扩展 n8n（添加 workers）或缩减 n8n（移除 workers）。

流程如下：

1. main n8n instance 处理 timers 和 webhook calls，生成（但不运行）workflow execution。
1. 它将 execution ID 传递给 message broker [Redis](#start-redis)，Redis 维护 pending executions 的 queue，并允许下一个可用 worker 获取它们。
1. pool 中的某个 worker 从 Redis 获取 message。
1. worker 使用 execution ID 从 database 获取 workflow information。
1. 完成 workflow execution 后，worker：
	- 将结果写入 database。
	- 向 Redis 发布消息，说明 execution 已完成。
1. Redis 通知 main instance。

!["Diagram showing the flow of data between the main n8n instance, Redis, the n8n workers, and the n8n database"](../../../.gitbook/assets/queue-mode-flow.png)

## 配置 workers <a href="#configuring-workers" id="configuring-workers"></a>

Workers 是实际执行工作的 n8n instances。它们从 main n8n process 接收必须执行的 workflows 信息，执行 workflows，并在每次 execution 完成后更新状态。

{% hint style="info" %}
**Per-process event log files**

如果你的 workers 共享可写 filesystem，请为每个 worker process 提供唯一 event log path。详情请参考 [Per-process event log files](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems#per-process-event-log-files)。
{% endhint %}

### 设置 encryption key <a href="#set-encryption-key" id="set-encryption-key"></a>

n8n 首次启动时会自动生成 encryption key。你也可以按需使用[环境变量](../basic-configuration/use-environment-variables/README.md)提供自己的 custom key。

main n8n instance 的 encryption key 必须与所有 worker 和 webhooks processor nodes 共享，以确保这些 worker nodes 能访问 database 中存储的 credentials。

请在每个 worker node 的[配置文件](../basic-configuration.md)中设置 encryption key，或设置对应环境变量：

```bash
export N8N_ENCRYPTION_KEY=<main_instance_encryption_key>
```

### 设置 executions mode <a href="#set-executions-mode" id="set-executions-mode"></a>

{% hint style="info" %}
**Database 注意事项**

n8n 建议使用 Postgres 13+。不建议在 SQLite database 上将 execution mode 设为 `queue` 来运行 n8n。
{% endhint %}

在 main instance 和任何 workers 上，使用以下命令将环境变量 `EXECUTIONS_MODE` 设为 `queue`。

```bash
export EXECUTIONS_MODE=queue
```

或者，你可以在[配置文件](../basic-configuration/use-environment-variables/README.md)中将 `executions.mode` 设为 `queue`。

### 启动 Redis <a href="#start-redis" id="start-redis"></a>

{% hint style="info" %}
**在单独机器上运行 Redis**

你可以在单独机器上运行 Redis，只需确保 n8n instance 可以访问它。
{% endhint %}

要在 Docker container 中运行 Redis，请按以下说明操作：

运行以下命令启动 Redis instance：

```
docker run --name some-redis -p 6379:6379  -d redis
```

默认情况下，Redis 在 `localhost` 的 `6379` port 上运行，且没有 password。根据你的 Redis configuration，为 main n8n process 设置以下配置。这些配置允许 n8n 与 Redis 交互。

| Using configuration file | Using environment variables | Description |
| ------ | ------ | ----- |
| `queue.bull.redis.host:localhost` | `QUEUE_BULL_REDIS_HOST=localhost` | 默认情况下，Redis 在 `localhost` 上运行。 |
| `queue.bull.redis.port:6379` | `QUEUE_BULL_REDIS_PORT=6379` | 默认 port 为 `6379`。如果 Redis 运行在不同 port，请配置此值。 |

你也可以设置以下可选配置：

| Using configuration file | Using environment variables | Description |
| ------ | ------ | ----- |
| `queue.bull.redis.username:USERNAME` | `QUEUE_BULL_REDIS_USERNAME` | 默认情况下，Redis 不要求 username。如果你使用特定 user，请配置此变量。 |
| `queue.bull.redis.password:PASSWORD` | `QUEUE_BULL_REDIS_PASSWORD` | 默认情况下，Redis 不要求 password。如果你使用 password，请配置此变量。 |
| `queue.bull.redis.db:0` | `QUEUE_BULL_REDIS_DB` | 默认值为 `0`。如果更改此值，请更新配置。 |
| `queue.bull.redis.timeoutThreshold:10000ms` | `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | 告诉 n8n 如果 Redis 不可用，在退出前应等待多久。默认值为 `10000`（ms）。 |
| `queue.bull.gracefulShutdownTimeout:30` | `N8N_GRACEFUL_SHUTDOWN_TIMEOUT` | graceful shutdown timeout，用于让 workers 在终止进程前完成正在执行的 jobs。默认值为 `30` 秒。 |

现在你可以启动 n8n instance，它会连接到 Redis instance。

### 启动 workers <a href="#start-workers" id="start-workers"></a>

你需要启动 worker processes，让 n8n 执行 workflows。如果你想在单独机器上托管 workers，请在该机器上安装 n8n，并确保它连接到 Redis instance 和 n8n database。

从根目录运行以下命令启动 worker processes：

```
./packages/cli/bin/n8n worker
```

如果使用 Docker，请使用以下命令：

```
docker run --name n8n-queue -p 5679:5678 docker.n8n.io/n8nio/n8n worker
```

你可以设置多个 worker processes。确保所有 worker processes 都能访问 Redis 和 n8n database。

#### Worker 服务 <a href="#worker-server" id="worker-server"></a>

每个 worker process 都会运行一个 server，并暴露可选 endpoints：

- `/healthz`：如果启用 `QUEUE_HEALTH_CHECK_ACTIVE` 环境变量，返回 worker 是否已启动
- `/healthz/readiness`：如果启用 `QUEUE_HEALTH_CHECK_ACTIVE` 环境变量，返回 worker 的 DB 和 Redis connections 是否 ready
- [credentials overwrite endpoint](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/credential-overwrites)
- [`/metrics`](../basic-configuration/configuration-examples/enable-prometheus-metrics.md)

{% hint style="info" %}
**自定义 health check endpoints**

你可以使用 [`N8N_ENDPOINT_HEALTH`](../basic-configuration/use-environment-variables/endpoints.md) 环境变量自定义 health check endpoint path。
{% endhint %}

#### 查看正在运行的 workers <a href="#view-running-workers" id="view-running-workers"></a>

{% hint style="info" %}
**功能可用性**

* Self-hosted Enterprise plans 可用。
* 如果你想在 Cloud Enterprise 上访问此功能，请[联系 n8n](https://n8n-community.typeform.com/to/y9X2YuGa)。
{% endhint %}

你可以在 n8n 中选择 **Settings** > **Workers**，查看正在运行的 workers 及其 performance metrics。

## 使用 queues 运行 n8n <a href="#running-n8n-with-queues" id="running-n8n-with-queues"></a>

使用 queues 运行 n8n 时，所有 production workflow executions 都由 worker processes 处理。对于 webhooks，这意味着 HTTP request 会由 main/webhook process 接收，但实际 workflow execution 会传递给 worker，这可能增加一些 overhead 和 latency。

Redis 充当 message broker，database 持久化数据，因此二者都必须可访问。不支持在 SQLite 上以这种设置运行 distributed system。

{% hint style="info" %}
**迁移数据**

如果你想将数据从一个 database 迁移到另一个 database，可以使用 Export 和 Import commands。请参考 [CLI commands for n8n](../use-the-command-line.md#export-workflows-and-credentials) 文档，了解如何使用这些 commands。
{% endhint %}

## Webhook processors <a href="#webhook-processors" id="webhook-processors"></a>

{% hint style="info" %}
**注意**

Webhook processes 依赖 Redis，也需要设置 `EXECUTIONS_MODE` 环境变量。请按照上面的[配置 workers](#configuring-workers) 小节设置 webhook processor nodes。
{% endhint %}

Webhook processors 是 n8n 的另一层 scaling。配置 webhook processor 是可选的，它允许你扩展 incoming webhook requests。

这种方式让 n8n 能够处理大量 parallel requests。你只需要相应地添加更多 webhook processes 和 workers。webhook process 会在同一 port（默认：`5678`）监听 requests。请在 containers 或单独机器中运行这些 processes，并使用 load balancing system 相应地路由 requests。

n8n 不建议将 main process 加入 load balancer pool。如果将 main process 加入 pool，它会接收 requests，并可能承受 heavy load。这会导致编辑、查看和与 n8n UI 交互时性能下降。

你可以从根目录执行以下命令启动 webhook processor：

```
./packages/cli/bin/n8n webhook
```

如果使用 Docker，请使用以下命令：

```
docker run --name n8n-queue -p 5679:5678 -e "EXECUTIONS_MODE=queue" docker.n8n.io/n8nio/n8n webhook
```

### 配置 webhook URL <a href="#configure-webhook-url" id="configure-webhook-url"></a>

要配置 webhook URL，请在运行 main n8n instance 的机器上执行以下命令：

```bash
export WEBHOOK_URL=https://your-webhook-url.com
```

你也可以在配置文件中设置此值。

### 配置 load balancer <a href="#configure-load-balancer" id="configure-load-balancer"></a>

使用多个 webhook processes 时，你需要一个 load balancer 来路由 requests。如果 n8n instance 和 webhooks 使用相同 domain name，可以按以下方式设置 load balancer 路由 requests：

- 将 webhook triggers 重定向到 webhook servers pool。需要考虑的 paths：
  - `/webhook/*`：Webhook trigger node endpoints
  - `/webhook-waiting/*`：执行 "send and wait" 操作的 nodes 使用的 Human-in-the-loop webhook endpoints（例如 Slack node）。
- 所有其他 paths（n8n internal API、editor 的 static files 等）都应路由到 main process

**注意：** manual workflow executions 的默认 URL 是 `/webhook-test/*`。请确保这些 URLs 路由到 main process。

你可以在配置文件 `endpoints.webhook` 中更改此 path，或使用 `N8N_ENDPOINT_WEBHOOK` 环境变量。如果更改了这些值，请相应更新 load balancer。

### 禁用 main process 中的 webhook processing（可选） <a href="#disable-webhook-processing-in-the-main-process-optional" id="disable-webhook-processing-in-the-main-process-optional"></a>

你已经有 webhook processors 来执行 workflows。你可以禁用 main process 中的 webhook processing。这会确保所有 webhook executions 都在 webhook processors 中执行。在配置文件中将 `endpoints.disableProductionWebhooksOnMainProcess` 设为 `true`，让 n8n 不在 main process 上处理 webhook requests。

或者，你可以使用以下命令：

```bash
export N8N_DISABLE_PRODUCTION_MAIN_PROCESS=true
```

在 main process 中禁用 webhook process 时，请运行 main process，但不要将它添加到 load balancer 的 webhook pool。

## 配置 worker concurrency <a href="#configure-worker-concurrency" id="configure-worker-concurrency"></a>

你可以使用 `concurrency` flag 定义 worker 可并行运行的 jobs 数量。默认值为 `10`。要修改它：

```bash
n8n worker --concurrency=5
```

## Concurrency 和 scaling 建议 <a href="#concurrency-and-scaling-recommendations" id="concurrency-and-scaling-recommendations"></a>

n8n 建议为 worker instances 将 concurrency 设置为 5 或更高。大量 workers 配合较低 concurrency values 可能耗尽 database connection pool，导致处理延迟和失败。

## Multi-main setup <a href="#multi-main-setup" id="multi-main-setup"></a>

{% hint style="info" %}
**功能可用性**

* Self-hosted Enterprise plans 可用。
{% endhint %}

在 queue mode 中，你可以运行多个 `main` process 以实现 high availability。

在 single-mode setup 中，`main` process 执行两组 tasks：

- **regular tasks**，例如运行 API、提供 UI，以及监听 webhooks；
- **at-most-once tasks**，例如运行 non-HTTP triggers（timers、pollers，以及 RabbitMQ 和 IMAP 等 persistent connections），并 pruning executions 和 binary data。

在 multi-main setup 中，有两类 `main` processes：

- **followers**，运行 **regular tasks**；
- **leader**，同时运行 **regular tasks 和 at-most-once tasks**。

### Leader 指定 <a href="#leader-designation" id="leader-designation"></a>

在 multi-main setup 中，所有 main instances 都会以对用户透明的方式处理 leadership process。如果当前 leader 不可用，例如因为崩溃或 event loop 过于繁忙，其他 followers 可以接管。如果之前的 leader 再次恢复响应，它会变成 follower。

### 配置 multi-main setup <a href="#configuring-multi-main-setup" id="configuring-multi-main-setup"></a>

要以 multi-main setup 部署 n8n，请确保：

- 所有 `main` processes 都以 queue mode 运行，并已连接到 Postgres 和 Redis。
- 所有 `main` 和 `worker` processes 都运行相同版本的 n8n。
- 所有 `main` processes 都已将环境变量 `N8N_MULTI_MAIN_SETUP_ENABLED` 设为 `true`。
- 所有 `main` processes 都在启用 session persistence（sticky sessions）的 load balancer 后运行。

如有需要，可以调整 leader key options：

| Using configuration file | Using environment variables | Description |
| ------ | ------ | ----- |
| `multiMainSetup.ttl:10` | `N8N_MULTI_MAIN_SETUP_KEY_TTL=10` | multi-main setup 中 leader key 的 time to live，单位为秒。 |
| `multiMainSetup.interval:3` | `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL=3` | multi-main setup 中 leader check 的间隔，单位为秒。 |

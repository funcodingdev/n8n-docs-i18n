---
title: Queue mode environment variables
description: >-
  用于在 self-hosted n8n 实例上配置 queue mode 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Queue mode
originalFilePath: hosting/configuration/environment-variables/queue-mode.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/queue-mode'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/queue-mode
layout:
  description:
    visible: false
---

# Queue mode 环境变量 <a href="#queue-mode-environment-variables" id="queue-mode-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

你可以根据需求以不同模式运行 n8n。Queue mode 提供最佳可扩展性。更多信息请参考 [Queue mode](../../scaling/enable-queue-mode.md)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS` | Boolean | `false` | 如果希望 manual executions 在 worker 而不是 main 上运行，请设为 `true`。 |
| `QUEUE_BULL_PREFIX` | String | - | 用于所有 queue keys 的前缀。 |
| `QUEUE_BULL_REDIS_DB` | Number | `0` | 使用的 Redis database。 |
| `QUEUE_BULL_REDIS_HOST` | String | `localhost` | Redis host。 |
| `QUEUE_BULL_REDIS_PORT` | Number | `6379` | 使用的 Redis port。 |
| `QUEUE_BULL_REDIS_USERNAME` | String | - | Redis username（需要 Redis 6 或更高版本）。为了兼容 Redis < 6，请不要定义它。 |
| `QUEUE_BULL_REDIS_PASSWORD` | String | - | Redis password。 |
| `QUEUE_BULL_REDIS_TIMEOUT_THRESHOLD` | Number | `10000` | Redis timeout threshold（ms）。 |
| `QUEUE_BULL_REDIS_CLUSTER_NODES` | String | - | 需要一个以逗号分隔的 Redis Cluster nodes 列表，格式为 `host:port`，供 Redis client 初始连接。如果以 queue mode（`EXECUTIONS_MODE = queue`）运行，设置此变量会创建 Redis Cluster client 而不是 Redis client，并且 n8n 会忽略 `QUEUE_BULL_REDIS_HOST` 和 `QUEUE_BULL_REDIS_PORT`。 |
| `QUEUE_BULL_REDIS_TLS` | Boolean | `false` | 在 Redis connections 上启用 TLS。 |
| `QUEUE_BULL_REDIS_DUALSTACK` | Boolean | `false` | 在 Redis connections 上启用 dual-stack support（IPv4 和 IPv6）。 |
| `QUEUE_WORKER_TIMEOUT` (**deprecated**) | Number | `30` | **Deprecated** 请改用 `N8N_GRACEFUL_SHUTDOWN_TIMEOUT`。

shutdown 时，n8n 在退出 worker process 前应等待 running executions 多久，单位为秒。 |
| `QUEUE_HEALTH_CHECK_ACTIVE` | Boolean | `false` | 是否启用 health checks：`true` 表示启用，`false` 表示禁用。 |
| `QUEUE_HEALTH_CHECK_PORT` | Number | 5678 | 提供 health checks 的 port。如果使用默认 port 启动 worker server 时遇到 port conflict error，请修改此项。 |
| `QUEUE_WORKER_LOCK_DURATION` | Number | `60000` | worker 处理 message 的 lease period 时长，单位为 ms。 |
| `QUEUE_WORKER_LOCK_RENEW_TIME` | Number | `10000` | worker 续期 lease time 的频率，单位为 ms。 |
| `QUEUE_WORKER_STALLED_INTERVAL` | Number | `30000` | worker 检查 stalled jobs 的频率（使用 0 表示永不检查）。 |
| `QUEUE_WORKER_MAX_STALLED_COUNT` | Number | `1` | stalled job 被重新处理的最大次数。 |

## Multi-main setup <a href="#multi-main-setup" id="multi-main-setup"></a>

详情请参考 [Configuring multi-main setup](../../scaling/enable-queue-mode.md#configuring-multi-main-setup)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_MULTI_MAIN_SETUP_ENABLED` | Boolean | `false` | 是否为 queue mode 启用 multi-main setup（需要 license）。 |
| `N8N_MULTI_MAIN_SETUP_KEY_TTL` | Number | `10` | multi-main setup 中 leader key 的 time to live，单位为秒。 |
| `N8N_MULTI_MAIN_SETUP_CHECK_INTERVAL` | Number | `3` | multi-main setup 中 leader check 的间隔，单位为秒。 |

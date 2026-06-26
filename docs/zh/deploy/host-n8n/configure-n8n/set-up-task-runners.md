---
title: Task runners
contentType: howto
nodeTitle: Set up task runners
originalFilePath: hosting/configuration/task-runners.md
originalUrl: https://docs.n8n.io/hosting/configuration/task-runners
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/set-up-task-runners
description: >-
  如何配置 task runners，使用内部或外部 runner processes 执行 tasks。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 设置 task runners

Task runners 是一种通用机制，用于以安全且高性能的方式执行 tasks。它们用于在 [Code node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 中执行用户提供的 JavaScript 和 Python code。

本文档说明 task runners 的工作方式以及如何配置它们。

{% hint style="warning" %}
**生产环境不建议使用 internal mode**

在生产环境中使用 internal mode 可能带来安全风险。对于生产部署，请使用 [external mode](set-up-task-runners.md#external-mode)，以确保 n8n 和 task runner processes 之间有适当隔离。其他安全措施请参阅 [Hardening task runners](security/harden-task-runners.md)。
{% endhint %}

## 工作方式 <a href="#how-it-works" id="how-it-works"></a>

Task runner feature 由以下组件组成：一个或多个 task runners、一个 task broker 和一个 task requester。

![Task runner overview](<../../.gitbook/assets/task-runner-concept (1).png>)

Task runners 使用 websocket connection 连接到 task broker。Task requester 向 broker 提交 task request，可用的 task runner 可以接收它并执行。

Runner 执行 task，并将结果提交给 task requester。Task broker 协调 runner 和 requester 之间的通信。

n8n instance（main 和 worker）充当 broker。在此情况下，Code node 是 task requester。

## Task runner modes <a href="#task-runner-modes" id="task-runner-modes"></a>

你可以以两种不同模式使用 task runners：internal 和 external。

### Internal mode <a href="#internal-mode" id="internal-mode"></a>

在 internal mode 中，n8n instance 将 task runner 作为 child process 启动。n8n process 会监控并管理 task runner 的 lifecycle。task runner process 与 n8n 共享相同的 `uid` 和 `gid`。生产环境 **不** 推荐这种方式。

### External mode <a href="#external-mode" id="external-mode"></a>

在 external mode 中，[launcher application](https://github.com/n8n-io/task-runner-launcher) 会按需启动 task runners 并管理它们的 lifecycle。通常，这意味着你在 n8n 旁边添加一个运行 [`n8nio/runners`](https://hub.docker.com/r/n8nio/runners) image 的 sidecar container，其中包含 launcher、JS task runner 和 Python task runner。此 sidecar container 独立于 n8n instance。

![Task runner deployed as a side-car container](../../.gitbook/assets/task-runner-external-mode.png)

使用 [Queue mode](scaling/enable-queue-mode.md) 时，每个 worker 都需要有自己的 task runners sidecar container。

此外，如果 [`OFFLOAD_MANUAL_EXECUTIONS_TO_WORKERS=false`](basic-configuration/use-environment-variables/queue-mode.md#queue-mode-environment-variables)，那么 main instance 将运行 manual executions，因此也需要自己的 task runners sidecar container。请注意，不建议在生产环境中禁用 offloading 来运行 n8n。

## 设置 external mode <a href="#setting-up-external-mode" id="setting-up-external-mode"></a>

在 external mode 中，你在 n8n 旁边以 sidecar container 运行 `n8nio/runners` image。下面提供一个 docker compose 作为参考。请记住，`n8nio/runners` image version 必须与 `n8nio/n8n` image 一致，并且 n8n version 必须 >=1.111.0。

```yaml
services:
  n8n:
    image: n8nio/n8n:1.111.0
    container_name: n8n-main
    environment:
      - N8N_RUNNERS_ENABLED=true
      - N8N_RUNNERS_MODE=external
      - N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0
      - N8N_RUNNERS_AUTH_TOKEN=your-secret-here
      - N8N_NATIVE_PYTHON_RUNNER=true
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
    # etc.

  task-runners:
    image: n8nio/runners:1.111.0
    container_name: n8n-runners
    environment:
      - N8N_RUNNERS_TASK_BROKER_URI=http://n8n-main:5679
      - N8N_RUNNERS_AUTH_TOKEN=your-secret-here
      # etc.
    depends_on:
      - n8n

volumes:
  n8n_data:
```

配置有三层：n8n container、runners container，以及 runners container 内的 launcher。

### 在 external mode 中配置 n8n container <a href="#configuring-n8n-container-in-external-mode" id="configuring-n8n-container-in-external-mode"></a>

以下是在 external mode 中运行的 n8n container 上可设置的主要环境变量：

| Environment variables | Description |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `N8N_RUNNERS_ENABLED=true` | 启用 task runners。 |
| `N8N_RUNNERS_MODE=external` | 以 external mode 使用 task runners。 |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | task runners 用于连接 broker 的 shared secret。 |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS=0.0.0.0` | 默认情况下，task broker 只监听 localhost。使用多个 containers 时（例如 Docker Compose），它需要能够接受 external connections。 |

完整环境变量列表请参阅 [task runner environment variables](basic-configuration/use-environment-variables/task-runners.md)。

### 在 external mode 中配置 runners container <a href="#configuring-runners-container-in-external-mode" id="configuring-runners-container-in-external-mode"></a>

以下是在 external mode 中运行的 runners container 上可设置的主要环境变量：

| Environment variables | Description |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `N8N_RUNNERS_AUTH_TOKEN=<random secure shared secret>` | task runner 用于连接 broker 的 shared secret。 |
| `N8N_RUNNERS_TASK_BROKER_URI=localhost:5679` | n8n instance 内 task broker server 的地址。 |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT=15` | task runner process 因不活动而关闭前等待的秒数。有新 tasks 要执行时，launcher 会自动重新启动 runner。设置为 `0` 可禁用 automatic shutdown。 |

完整环境变量列表请参阅 [task runner environment variables](basic-configuration/use-environment-variables/task-runners.md)。

### 在 external mode 中配置 runners container 内的 launcher <a href="#configuring-launcher-in-runners-container-in-external-mode" id="configuring-launcher-in-runners-container-in-external-mode"></a>

Launcher 会从 runners container environment 读取环境变量，并执行以下 actions：

* 将 launcher 自身 environment 中的环境变量传递给所有 runners（`allowed-env`）
* 为特定 runners 设置特定环境变量（`env-overrides`）

要传递和设置哪些环境变量，由 runners image 中包含的 [launcher config file](https://github.com/n8n-io/n8n/blob/master/docker/images/runners/n8n-task-runners.json) 定义。此 config file 位于 container 的 `/etc/task-runners.json`。要了解更多 launcher config file 信息，请参阅 [Config file documentation](https://github.com/n8n-io/task-runner-launcher/blob/main/docs/setup.md#config-file)。

默认 launcher configuration file 已锁定，但你可以编辑此文件，例如 allowlist first-party 或 third-party modules。要自定义 launcher configuration file，请挂载到以下路径：

```
path/to/n8n-task-runners.json:/etc/n8n-task-runners.json
```

## 添加额外依赖 <a href="#adding-extra-dependencies" id="adding-extra-dependencies"></a>

### 1. 扩展 `n8nio/runners` image <a href="#id-1-extend-the-n8niorunners-image" id="id-1-extend-the-n8niorunners-image"></a>

你可以扩展 `n8nio/runners` image，为 runners 添加额外依赖。执行此操作需要 `n8nio/runners:1.121.0` 或更高版本。

```dockerfile
FROM n8nio/runners:1.121.0
USER root
RUN cd /opt/runners/task-runner-javascript && pnpm add moment uuid
RUN cd /opt/runners/task-runner-python && uv pip install numpy pandas
COPY n8n-task-runners.json /etc/n8n-task-runners.json
USER runner
```

你还必须 allowlist Code node 可使用的任何 first-party 或 third-party packages。请编辑 configuration file `n8n-task-runners.json`，将 extended image 中的 packages 加入其中。

```json
{
  "task-runners": [
    {
      "runner-type": "javascript",
      "env-overrides": {
        "NODE_FUNCTION_ALLOW_BUILTIN": "crypto",         // <-- allowlist Node.js builtin modules here
        "NODE_FUNCTION_ALLOW_EXTERNAL": "moment,uuid",   // <-- allowlist third-party JS packages here
      }
    },
    {
      "runner-type": "python",
      "env-overrides": {
        "PYTHONPATH": "/opt/runners/task-runner-python",
        "N8N_RUNNERS_STDLIB_ALLOW": "json",              // <-- allowlist Python standard library packages here
        "N8N_RUNNERS_EXTERNAL_ALLOW": "numpy,pandas"     // <-- allowlist third-party Python packages here
      }
    }
  ]
}
```

* `NODE_FUNCTION_ALLOW_BUILTIN`：允许的 node builtin modules，以逗号分隔。
* `NODE_FUNCTION_ALLOW_EXTERNAL`：允许的 JS packages，以逗号分隔。
* `N8N_RUNNERS_STDLIB_ALLOW`：允许的 Python standard library packages，以逗号分隔。
* `N8N_RUNNERS_EXTERNAL_ALLOW`：允许的 Python packages，以逗号分隔。

### 2. 构建自定义 image <a href="#id-2-build-your-custom-image" id="id-2-build-your-custom-image"></a>

例如，从 n8n repository root 执行：

```bash
docker buildx build \
  -f docker/images/runners/Dockerfile \
  -t n8nio/runners:custom \
  .
```

### 3. 运行 image <a href="#id-3-run-the-image" id="id-3-run-the-image"></a>

例如：

```bash
docker run --rm -it \
  -e N8N_RUNNERS_AUTH_TOKEN=test \
  -e N8N_RUNNERS_LAUNCHER_LOG_LEVEL=debug \
  -e N8N_RUNNERS_TASK_BROKER_URI=http://host.docker.internal:5679 \
  -p 5680:5680 \
  n8nio/runners:custom
```

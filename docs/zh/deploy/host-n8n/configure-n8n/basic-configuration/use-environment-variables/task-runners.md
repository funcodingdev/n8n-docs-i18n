---
title: Task runner environment variables
description: 用于为 self-hosted n8n 实例配置 task runners 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Task runners
originalFilePath: hosting/configuration/environment-variables/task-runners.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/task-runners'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/task-runners
layout:
  description:
    visible: false
---

# Task runner 环境变量 <a href="#task-runner-environment-variables" id="task-runner-environment-variables"></a>

{% hint style="info" %}
**基于文件的配置**

与 main n8n image 不同，你不能在 task runner image 中为 secrets 使用基于文件的配置。这意味着添加 `_FILE` 后缀的变量不会被识别。
{% endhint %}

[Task runners](../../set-up-task-runners.md) 执行由 [Code node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) 定义的代码。

## n8n 实例环境变量 <a href="#n8n-instance-environment-variables" id="n8n-instance-environment-variables"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_ENABLED` | Boolean | `false` | 是否启用 task runners。 |
| `N8N_RUNNERS_MODE` | Enum string: `internal`, `external` | `internal` | 如何启动和运行 task runner。`internal` 表示 n8n 会将 task runner 作为 child process 启动。`external` 表示由 external orchestrator 启动 task runner。 |
| `N8N_RUNNERS_AUTH_TOKEN` | String | Random string | task runner 用于向 n8n 认证的 shared secret。使用 `external` mode 时必填。 |
| `N8N_RUNNERS_BROKER_PORT` | Number | `5679` | task broker 监听 task runner connections 的 port。 |
| `N8N_RUNNERS_BROKER_LISTEN_ADDRESS` | String | `127.0.0.1` | task broker 监听的 address。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | task broker 与 task runner 之间通信的最大 payload size，单位为 bytes。 |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | task runner 使用的 `--max-old-space-size` 选项，单位为 MB。默认情况下，Node.js 会根据可用内存设置此项。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | task runner 一次可并发执行的 tasks 数量。 |
| `N8N_RUNNERS_TASK_TIMEOUT` | Number | `300` | task 在 runner 停止并重启它之前可运行的最长时间，单位为秒。该值必须大于 0。 |
| `N8N_RUNNERS_HEARTBEAT_INTERVAL` | Number | `30` | runner 必须向 broker 发送 heartbeat 的间隔，单位为秒。如果 runner 未及时发送 heartbeat，task 会停止且 runner 会重启。该值必须大于 0。 |
| `N8N_RUNNERS_INSECURE_MODE` | Boolean | `false` | 是否在 task runner 中禁用所有安全措施，以兼容依赖 insecure JS features 的 modules。**不建议在生产环境使用。** |
| `N8N_RUNNERS_TASK_REQUEST_TIMEOUT` | Number | `60` | task request 在超时前等待 runner 可用的时长，单位为秒。这可以防止没有可用 runners 时 workflows 无限挂起。必须大于 0。 |

## Task runner launcher 环境变量 <a href="#task-runner-launcher-environment-variables" id="task-runner-launcher-environment-variables"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_LAUNCHER_LOG_LEVEL` | Enum string: `debug`, `info`, `warn`, `error` | `info` | 要显示哪些 log messages。 |
| `N8N_RUNNERS_AUTH_TOKEN` | String | - | 用于向 n8n 认证的 shared secret。 |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | 关闭 idle runner 前等待的秒数。 |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | task broker server（n8n instance）的 URI。 |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | launcher health check server 的 port。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | task broker 与 task runner 之间通信的最大 payload size，单位为 bytes。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | task runner 一次可并发执行的 tasks 数量。 |

## Task runner 环境变量（所有语言） <a href="#task-runner-environment-variables-all-languages" id="task-runner-environment-variables-all-languages"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_GRANT_TOKEN` | String | Random string | runner 用于向 task broker 认证的 token。它由 launcher 自动提供。 |
| `N8N_RUNNERS_AUTO_SHUTDOWN_TIMEOUT` | Number | `15` | 关闭 idle runner 前等待的秒数。 |
| `N8N_RUNNERS_TASK_BROKER_URI` | String | `http://127.0.0.1:5679` | task broker server（n8n instance）的 URI。 |
| `N8N_RUNNERS_LAUNCHER_HEALTH_CHECK_PORT` | Number | `5680` | launcher health check server 的 port。 |
| `N8N_RUNNERS_MAX_PAYLOAD` | Number | `1 073 741 824` | task broker 与 task runner 之间通信的最大 payload size，单位为 bytes。 |
| `N8N_RUNNERS_MAX_CONCURRENCY` | Number | `5` | task runner 一次可并发执行的 tasks 数量。 |

## Task runner 环境变量（JavaScript） <a href="#task-runner-environment-variables-javascript" id="task-runner-environment-variables-javascript"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `NODE_FUNCTION_ALLOW_BUILTIN` | String | - | 允许用户在 Code node 中导入特定 built-in modules。使用 * 可允许全部。n8n 默认禁用模块导入。在 external mode 中，请在 [runners config file](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中将它设为 `env-override`，而不是设为 container environment variable。 |
| `NODE_FUNCTION_ALLOW_EXTERNAL` | String | - | 允许用户在 Code node 中导入特定 external modules（来自 `n8n/node_modules`）。n8n 默认禁用模块导入。在 external mode 中，请在 [runners config file](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中将它设为 `env-override`，而不是设为 container environment variable。 |
| `N8N_RUNNERS_ALLOW_PROTOTYPE_MUTATION` | Boolean | `false` | 是否允许 external libraries 修改 prototype。设为 `true` 可允许依赖 runtime prototype mutation 的 modules（例如 [`puppeteer`](https://pptr.dev/)），代价是放宽安全限制。 |
| `GENERIC_TIMEZONE` | * | `America/New_York` | 与 [n8n instance 配置相同的默认 timezone](timezone-and-localization.md)。 |
| `NODE_OPTIONS` | String | - | Node.js 的 [Options](https://nodejs.org/api/cli.html#node_optionsoptions)。 |
| `N8N_RUNNERS_MAX_OLD_SPACE_SIZE` | String |  | task runner 使用的 `--max-old-space-size` 选项，单位为 MB。默认情况下，Node.js 会根据可用内存设置此项。 |

## Task runner 环境变量（Python） <a href="#task-runner-environment-variables-python" id="task-runner-environment-variables-python"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_RUNNERS_STDLIB_ALLOW` | String | - | 你可以在 Code node 中使用的 Python standard library modules，包括其 submodules。使用 `*` 可允许所有 stdlib modules。n8n 默认禁用所有 Python standard library imports。在 external mode 中，请在 [runners config file](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中将它设为 `env-override`，而不是设为 container environment variable。 |
| `N8N_RUNNERS_EXTERNAL_ALLOW` | String | - | 允许在 Code node 中使用的 third-party Python modules，包括其 submodules。使用 `*` 可允许所有 external modules。n8n 默认禁用所有 third-party Python modules。Third-party Python modules 必须被[包含](../../set-up-task-runners.md#adding-extra-dependencies)到 `n8nio/runners` image 中。在 external mode 中，请在 [runners config file](../../set-up-task-runners.md#configuring-launcher-in-runners-container-in-external-mode)（`/etc/n8n-task-runners.json`）中将它设为 `env-override`，而不是设为 container environment variable。 |
| `N8N_RUNNERS_BUILTINS_DENY` | String | `eval,exec,compile,open,input,breakpoint,getattr,object,type,vars,setattr,delattr,hasattr,dir,memoryview,__build_class__,globals,locals` | 不能在 Code node 中使用的 Python built-ins。设为空字符串可允许所有 built-ins。 |
| `N8N_BLOCK_RUNNER_ENV_ACCESS` | Boolean | `true` | 是否阻止从 Python code tasks 中访问 runner 环境。设为 `false` 可允许所有 Python code node 用户通过 `os.environ` 访问 runner 环境。出于安全原因，默认阻止访问环境变量。 |

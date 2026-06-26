---
title: Configure workflow timeout settings
description: 设置 execution timeouts，以决定 workflows 可以运行多久。
contentType: howto
nodeTitle: Configure workflow timeouts
originalFilePath: hosting/configuration/configuration-examples/execution-timeout.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/execution-timeout
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-workflow-timeouts
layout:
  description:
    visible: false
---

# 配置 workflow timeout settings <a href="#configure-workflow-timeout-settings" id="configure-workflow-timeout-settings"></a>

Workflow 会在此时间后 timeout 并被 canceled（以秒为单位）。如果 workflow 在 main process 中运行，会发生 soft timeout（当前 node 完成后生效）。如果 workflow 在自己的 process 中运行，n8n 会先尝试 soft timeout，然后在等待给定 timeout duration 的五分之一后 kill process。

`EXECUTIONS_TIMEOUT` 默认值为 `-1`。例如，如果你想将 timeout 设置为一小时：

```bash
export EXECUTIONS_TIMEOUT=3600
```

你也可以为每个 workflow 单独设置 maximum execution time（以秒为单位）。例如，如果你想将 maximum execution time 设置为两小时：

```bash
export EXECUTIONS_TIMEOUT_MAX=7200
```
有关这些变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/executions.md)。

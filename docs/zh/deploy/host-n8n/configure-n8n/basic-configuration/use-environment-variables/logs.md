---
title: Logs environment variables
description: 用于配置 logging 和 diagnostic data 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Logs
originalFilePath: hosting/configuration/environment-variables/logs.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/logs'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs
layout:
  description:
    visible: false
---

# Logs 环境变量 <a href="#logs-environment-variables" id="logs-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

本页列出用于设置 debugging logging 的环境变量。详情请参考 [Logging in n8n](../../../keep-n8n-running/set-up-logging.md)。

## n8n logs <a href="#n8n-logs" id="n8n-logs"></a>

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_LOG_LEVEL` | Enum string: `info`, `warn`, `error`, `debug` | `info` | Log output level。详情请参考 [Log levels](../../../keep-n8n-running/set-up-logging.md#log-levels)。 |
| `N8N_LOG_OUTPUT` | Enum string: `console`, `file` | `console` | logs 输出位置。提供多个值时，使用逗号分隔列表。 |
| `N8N_LOG_FORMAT` | Enum string: `text`, `json` | `text` | 要使用的 log format。`text` 打印 human readable messages。`json` 每行打印一个 JSON object，其中包含 message、level、timestamp 和所有 metadata。这对生产监控和 debugging 都很有用。 |
| `N8N_LOG_CRON_ACTIVE_INTERVAL` | Number | `0` | 记录当前 active cron jobs 的间隔，单位为分钟。设为 `0` 可禁用。 |
| `N8N_LOG_FILE_COUNT_MAX` | Number | `100` | 要保留的 log files 最大数量。 |
| `N8N_LOG_FILE_SIZE_MAX` | Number | `16` | 每个 log file 的最大大小，单位为 MB。 |
| `N8N_LOG_FILE_LOCATION` | String | `<n8n-directory-path>/logs/n8n.log` | Log file location。需要将 N8N_LOG_OUTPUT 设为 `file`。 |
| `DB_LOGGING_ENABLED` | Boolean | `false` | 是否启用 database-specific logging。 |
| `DB_LOGGING_OPTIONS` | Enum string: `query`, `error`, `schema`, `warn`, `info`, `log`  | `error` | Database log output level。要启用全部 logging，请指定 `all`。参考 [TypeORM logging options](https://orkhan.gitbook.io/typeorm/docs/docs/advanced-topics/5-logging#logging-options)。 |
| `DB_LOGGING_MAX_EXECUTION_TIME` | Number | `1000` | n8n 记录 warning 前的最大执行时间，单位为毫秒。设为 `0` 可禁用 long running query warning。 |
| `CODE_ENABLE_STDOUT` | Boolean | `false` | 设为 `true` 可将 Code node 中 `console.log` 或 `print` 的 logs 发送到进程 stdout，仅适用于 production executions。 |
| `NO_COLOR` | any | `undefined` | 设为任意值可让 logs 输出不包含 ANSI colors。更多信息请参阅 [no-color.org website](https://no-color.org/)。 |

## 日志流式传输 <a href="#log-streaming" id="log-streaming"></a>

有关此功能的更多信息，请参考 [日志流式传输](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_EVENTBUS_CHECKUNSENTINTERVAL` | Number | `0` | 检查 unsent event messages 的频率，单位为毫秒。在少数情况下可能会重复发送消息。设为 `0` 可禁用。 |
| `N8N_EVENTBUS_LOGWRITER_SYNCFILEACCESS` | Boolean | `false` | 所有 file access 是否在线程内同步发生：`true` 表示同步，`false` 表示不同步。 |
| `N8N_EVENTBUS_LOGWRITER_KEEPLOGCOUNT` | Number | `3` | 要保留的 event log files 数量。 |
| `N8N_EVENTBUS_LOGWRITER_MAXFILESIZEINKB` | Number | `10240` | 开始新 event log file 前，当前文件允许的最大大小，单位为 KB。 |
| `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` | String | `n8nEventLog` | event log file 的 basename。设置 `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` 时会忽略此项。 |
| `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` | String | `''` | event log file 的绝对路径。必须以 `.log` 结尾。设置后会原样使用此路径，并覆盖 `N8N_EVENTBUS_LOGWRITER_LOGBASENAME` 和默认 per-process suffix。当多个进程共享可写 filesystem 时，可用它为每个 n8n process 提供唯一 event log path。详情请参考 [Per-process event log files](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems#per-process-event-log-files)。 |
| `N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE` | Number | `500000` | 恢复期间从单个 event log file 解析的最大行数。当 event log file 包含很多 invalid lines 时，它会限制内存使用。 |

### 通过环境变量管理 log streaming destinations <a href="#manage-log-streaming-destinations-from-environment-variables" id="manage-log-streaming-destinations-from-environment-variables"></a>

将 `N8N_LOG_STREAMING_MANAGED_BY_ENV` 设为 `true`，即可通过环境变量管理 log streaming destinations。关于 activation pattern 的工作方式，请参阅 [Manage instance settings using environment variables](../../manage-settings-using-environment-variables.md)；关于每个 destination 的 JSON 结构，请参阅 [Configure log streaming destinations using environment variables](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems#configure-using-environment-variables)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/JvN9TDUUWTwpWaT83YrH/" %}

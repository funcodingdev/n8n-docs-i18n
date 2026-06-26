---
contentType: howto
nodeTitle: Set up logging
originalFilePath: hosting/logging-monitoring/logging.md
originalUrl: 'https://docs.n8n.io/hosting/logging-monitoring/logging'
url: 'https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/set-up-logging'
layout:
  description:
    visible: false
---

# n8n 中的 Logging <a href="#logging-in-n8n" id="logging-in-n8n"></a>

Logging 是 debugging 的重要功能。n8n 使用 [winston](https://www.npmjs.com/package/winston) logging library。

{% hint style="info" %}
**Log streaming**

n8n Self-hosted Enterprise tier 除本文档描述的 logging options 外，还包含 [Log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems)。
{% endhint %}

## Setup <a href="#setup" id="setup"></a>

要在 n8n 中设置 logging，需要设置以下 environment variables（你也可以在 [configuration file](../configure-n8n/basic-configuration/use-environment-variables/README.md) 中设置这些值）：

| Configuration file 中的 setting | 使用 environment variables | Description |
|-----------------------------------|-----------------------------|-------------|
| n8n.log.level | N8N_LOG_LEVEL | Log output level。可用选项（从最低到最高 level）为 error、warn、info 和 debug。默认值为 `info`。你可以在[这里](#log-levels)了解更多。 |
| n8n.log.output | N8N_LOG_OUTPUT | Log 输出位置。可用选项为 `console` 和 `file`。可以使用多个值，用逗号（`,`）分隔。默认使用 `console`。 |
| n8n.log.file.location | N8N_LOG_FILE_LOCATION | Log file location，仅当 log output 设置为 file 时使用。默认使用 `<n8nFolderPath>/logs/n8n.log`。 |
| n8n.log.file.fileSizeMax | N8N_LOG_FILE_SIZE_MAX | 每个 log file 的最大 size（MB）。默认情况下，n8n 使用 16 MB。 |
| n8n.log.file.fileCountMax | N8N_LOG_FILE_COUNT_MAX | 要保留的 log files 最大数量。默认值为 100。使用 workers 时应设置此值。 |

```bash
# Set the logging level to 'debug' <a href="#set-the-logging-level-to-debug" id="set-the-logging-level-to-debug"></a>
export N8N_LOG_LEVEL=debug

# Set log output to both console and a log file <a href="#set-log-output-to-both-console-and-a-log-file" id="set-log-output-to-both-console-and-a-log-file"></a>
export N8N_LOG_OUTPUT=console,file

# Set a save location for the log file <a href="#set-a-save-location-for-the-log-file" id="set-a-save-location-for-the-log-file"></a>
export N8N_LOG_FILE_LOCATION=/home/jim/n8n/logs/n8n.log

# Set a 50 MB maximum size for each log file <a href="#set-a-50-mb-maximum-size-for-each-log-file" id="set-a-50-mb-maximum-size-for-each-log-file"></a>
export N8N_LOG_FILE_SIZE_MAX=50

# Set 60 as the maximum number of log files to be kept <a href="#set-60-as-the-maximum-number-of-log-files-to-be-kept" id="set-60-as-the-maximum-number-of-log-files-to-be-kept"></a>
export N8N_LOG_FILE_COUNT_MAX=60
```

### Log levels <a href="#log-levels" id="log-levels"></a>

n8n 使用标准 log levels 进行报告：

- `silent`：不输出任何内容
- `error`：只输出 errors，不输出其他内容
- `warn`：输出 errors 和 warning messages
- `info`：包含关于 progress 的有用信息
- `debug`：最 verbose 的输出。n8n 会输出大量信息来帮助你 debug issues。

## Development <a href="#development" id="development"></a>

Development 期间，添加 log messages 是 good practice。它有助于 debug errors。要为 development 配置 logging，请遵循下面的指南。

### Implementation details <a href="#implementation-details" id="implementation-details"></a>

n8n 使用位于 `workflow` package 中的 `LoggerProxy` class。通过传入 `Logger` instance 调用 `LoggerProxy.init()`，会在使用前初始化该 class。

Initialization process 只发生一次。[`start.ts`](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) file 已经为你完成此过程。如果你从头创建 new command，需要初始化 `LoggerProxy` class。

在 `cli` package 中创建 `Logger` implementation 后，可以通过从 exported module 调用 `getInstance` convenience method 获取它。

查看 [start.ts](https://github.com/n8n-io/n8n/blob/master/packages/cli/src/commands/start.ts) file，了解此 process 的工作方式。

### 添加 logs <a href="#adding-logs" id="adding-logs"></a>

在 project 中初始化 `LoggerProxy` class 后，你可以将其 import 到任何其他 file 并添加 logs。

所有 logging levels 都提供 convenience methods，因此可以在需要时使用 `Logger.<logLevel>('<message>', ...meta)` format 添加 new logs，其中 `meta` 表示除 `message` 之外需要的任何 additional properties。

在上面的 example 中，我们使用了[上面](#log-levels)描述的 standard log levels。`message` argument 是 string，`meta` 是 data object。

```js
// You have to import the LoggerProxy. We rename it to Logger to make it easier

import {
	LoggerProxy as Logger
} from 'n8n-workflow';

// Info-level logging of a trigger function, with workflow name and workflow ID as additional metadata properties

Logger.info(`Polling trigger initiated for workflow "${workflow.name}"`, {workflowName: workflow.name, workflowId: workflow.id});
```

创建 new loggers 时，请记住一些有用 standards：

- 尽可能让 log messages 便于人类阅读。例如，始终用引号包裹 names。
- 在 log message 和 metadata 中重复信息（例如上例中的 workflow name）可能很有用，因为 messages 更易搜索，而 metadata 更便于 filtering。
- 在所有 logs 中包含多个 IDs（例如 `executionId`、`workflowId` 和 `sessionId`）。
- 使用 node types 而不是 node names（或两者都用），因为这更一致，也更容易搜索。

## Front-end logs <a href="#front-end-logs" id="front-end-logs"></a>

截至目前，front-end logs 不可用。在 `editor-ui` package 中使用 `Logger` 或 `LoggerProxy` 会产生 errors。此功能将在未来 versions 中实现。

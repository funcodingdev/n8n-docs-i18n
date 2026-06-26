---
description: 将 events 从 n8n stream 到你的 logging tools。
contentType: howto
nodeTitle: Stream logs to external systems
originalFilePath: log-streaming.md
originalUrl: 'https://docs.n8n.io/log-streaming'
url: 'https://docs.n8n.io/administer/observe-and-log/stream-logs-to-external-systems'
layout:
  description:
    visible: false
---

# Log streaming <a href="#log-streaming" id="log-streaming"></a>

{% hint style="info" %}
**功能可用性**

Log Streaming 可用于所有 Enterprise plans。
{% endhint %}

Log streaming 允许你将 events 从 n8n 发送到自己的 logging tools。这让你可以在自己的 alerting 和 logging processes 中管理 n8n monitoring。

## 设置 log streaming <a href="#set-up-log-streaming" id="set-up-log-streaming"></a>

要使用 log streaming，你必须添加 streaming destination。

1. 前往 **Settings** > **Log Streaming**。
2. 选择 **Add new destination**。
3. 选择 destination type。n8n 会打开 **New Event Destination** modal。
4. 在 **New Event Destination** modal 中，输入 event destination 的 configuration information。这些信息取决于你使用的 destination type。
5. 选择 **Events** 来选择要 stream 的 events。
6. 选择 **Save**。

{% hint style="info" %}
**Self-hosted users**

如果你 self-host n8n，可以使用 [Environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs#log-streaming) 配置 additional log streaming behavior。你也可以通过 environment variables 管理 destinations，请参阅 [Configure log streaming destinations using environment variables](#configure-using-environment-variables)。
{% endhint %}

## Per-process event log files <a href="#per-process-event-log-files" id="per-process-event-log-files"></a>

n8n 会在 forward events 到 streaming destinations 前，将每个 emitted event 持久化到 local log file。该 file 会在 restarts 后保留，并让 n8n 重新 emit 尚未 delivered 的 events。

默认情况下，n8n 将 event log 写入 `<n8n-user-folder>/n8nEventLog.log`，并在 worker 或 webhook processor processes 上添加 `-worker` 或 `-webhook-processor` suffix。当单个 n8n process 拥有该 file 时，此默认行为符合预期。

{% hint style="warning" %}
**Shared writable filesystems**

如果多个 n8n processes 共享一个 writable volume，例如基于 NFS 或 EFS shared persistent volume 的 [queue mode](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/enable-queue-mode) workers，它们不得写入同一个 event log file。多个 processes 的 concurrent appends 可能 interleave 或 corrupt file，导致 recovery failures 和 events 丢失。
{% endhint %}

为避免这种情况，请在每个 process 上将 [`N8N_EVENTBUS_LOGWRITER_LOGFULLPATH`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs#log-streaming) 设置为以 `.log` 结尾的唯一 absolute path。n8n 会按原样使用 configured path，并且不会 append process-type suffix，因此你的 orchestrator 负责保证 processes 之间的唯一性。

Companion variable [`N8N_EVENTBUS_LOGWRITER_MAXTOTALMESSAGESPERFILE`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/logs#log-streaming) 会限制 recovery 期间 n8n 从单个 event log file 解析的 lines 数量，因此 corrupted file 不会耗尽 process memory。

Notes：

* 未设置 `N8N_EVENTBUS_LOGWRITER_LOGFULLPATH` 时，默认行为不变。
* 设置该 variable 后，n8n 不会 auto-suffix path。每个 process 必须接收自己的 value。
* 如果 shared `n8nEventLog-worker.log` file 已从 previous deployment 存在，请在 opt in 前手动 quarantine。n8n 不会自动删除 legacy files。

## Events <a href="#events" id="events"></a>

以下 events 可用。你可以在 **Settings** > **Log Streaming** > **Events** 中选择要 stream 的 events。

* Workflow
	* Started
	* Success
	* Failed
	* Cancelled
* Node executions
	* Started
	* Finished
* Audit
	* User login success
	* User login failed
	* User signed up
	* User updated
	* User deleted
	* User invited
	* User invitation accepted
	* User re-invited
	* User email failed
	* User reset requested
	* User reset
	* User credentials created
	* User credentials shared
	* User credentials updated
	* User credentials deleted
	* User API created
	* User API deleted
	* User MFA enabled
	* User MFA disabled
	* User execution deleted
	* Execution data revealed
	* Execution data reveal failed
	* Package installed
	* Package updated
	* Package deleted
	* Workflow created
	* Workflow deleted
	* Workflow updated
	* Workflow archived
	* Workflow unarchived
	* Workflow activated
	* Workflow deactivated
	* Workflow version updated
    * Workflow executed
	* Workflow waiting
	* Workflow resumed
	* Variable created
	* Variable updated
	* Variable deleted
	* External secrets provider settings saved
	* External secrets provider reloaded
	* External secrets connection created
	* External secrets connection updated
	* External secrets connection deleted
	* External secrets connection tested
	* External secrets connection reloaded
	* Personal publishing restricted enabled
	* Personal publishing restricted disabled
	* Personal sharing restricted enabled
	* Personal sharing restricted disabled
	* 2FA enforcement enabled
	* 2FA enforcement disabled
	* Token exchange succeeded
	* Token exchange failed
	* Token exchange embed login
	* Token exchange embed login failed
	* Token exchange identity linked
	* Token exchange user provisioned
	* Token exchange role updated
	* Role mapping roles resolved
	* Role mapping rule created
	* Role mapping rule updated
	* Role mapping rule deleted
	* Role mapping rules bulk deleted
* Worker
	* Started
	* Stopped
* AI node logs
	* Memory get messages
	* Memory added message
	* Output parser parsed
	* Retriever get relevant documents
	* Embeddings embedded document
	* Embeddings embedded query
	* Document processed
	* Text splitter split
	* Tool called
	* Vector store searched
	* LLM generated
	* LLM error
	* Vector store populated
	* Vector store updated
* Runner
	* Task requested
	* Response received
* Queue
	* Job enqueued
	* Job dequeued
	* Job completed
	* Job failed
	* Job stalled

## Destinations <a href="#destinations" id="destinations"></a>

n8n 支持三种 destination types：

* Syslog server
* Generic webhook
* Sentry client

## 使用 environment variables 配置 <a href="#configure-using-environment-variables" id="configure-using-environment-variables"></a>

如果你 self-host n8n，可以使用 environment variables 而不是 UI 管理 log streaming destinations。此功能从 n8n v2.19.0 起可用。将 `N8N_LOG_STREAMING_MANAGED_BY_ENV` 设置为 `true`，并在 `N8N_LOG_STREAMING_DESTINATIONS` 中以 JSON array 提供 destinations。n8n 会在每次 startup 时重新 apply 这些 destinations，并将 **Log Streaming** UI 锁定为 read-only。完整 pattern 请参阅 [Manage instance settings using environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/manage-settings-using-environment-variables)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/JvN9TDUUWTwpWaT83YrH/" %}

### Common fields <a href="#common-fields" id="common-fields"></a>

无论 `type` 如何，每个 destination 都接受这些 fields。

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `"webhook"` \| `"syslog"` \| `"sentry"` | Yes | Destination type。决定适用哪些 type-specific fields。 |
| `label` | string | No | UI 中显示的 display name。 |
| `enabled` | boolean | No | Destination 是否 forward events。 |
| `subscribedEvents` | string[] | No | 要 forward 的 event names 或 group prefixes（例如 `n8n.audit`、`n8n.workflow`）。 |
| `anonymizeAuditMessages` | boolean | No | 从 `n8n.audit.*` events 中 strip sensitive payload data。 |
| `circuitBreaker` | object | No | Failure-protection settings。请参阅 [Circuit breaker](#circuit-breaker)。 |

### Webhook <a href="#webhook" id="webhook"></a>

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `url` | string (URL) | Yes | - | 接收 event payload 的 endpoint。 |
| `method` | `"GET"` \| `"POST"` \| `"PUT"` | No | `"POST"` | Delivery 使用的 HTTP method。 |
| `sendQuery` | boolean | No | `false` | 是否发送 query parameters。 |
| `specifyQuery` | `"keypair"` \| `"json"` | No | `"keypair"` | `sendQuery` 为 `true` 时 query parameters 的 format。 |
| `queryParameters` | `{ parameters: [{ name, value }] }` | No | - | 作为 key/value pairs 的 query parameters。`specifyQuery` 为 `"keypair"` 时使用。 |
| `jsonQuery` | string | No | `""` | 作为 JSON string 的 query parameters。`specifyQuery` 为 `"json"` 时使用。 |
| `sendHeaders` | boolean | No | `false` | 是否发送 headers。 |
| `specifyHeaders` | `"keypair"` \| `"json"` | No | `"keypair"` | `sendHeaders` 为 `true` 时 headers 的 format。 |
| `headerParameters` | `{ parameters: [{ name, value }] }` | No | - | 作为 key/value pairs 的 headers。`specifyHeaders` 为 `"keypair"` 时使用。 |
| `jsonHeaders` | string | No | `""` | 作为 JSON string 的 headers。`specifyHeaders` 为 `"json"` 时使用。 |
| `options` | object | No | `{}` | Connection-level options。请参阅 [Webhook options](#webhook-options)。 |

#### Webhook options <a href="#webhook-options" id="webhook-options"></a>

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `allowUnauthorizedCerts` | boolean | No | `false` | 忽略 SSL certificate validation。 |
| `queryParameterArrays` | `"repeat"` \| `"brackets"` \| `"indices"` | No | `"brackets"` | Query parameters 中使用的 array format。`sendQuery` 为 `true` 时使用。 |
| `redirect` | `{ redirect: { followRedirects, maxRedirects } }` | No | `{ redirect: {} }` | Follow HTTP redirects。`followRedirects` 默认值为 `false`；`maxRedirects` 默认值为 `21`。 |
| `proxy` | `{ proxy: { protocol, host, port } }` | No | `{ proxy: {} }` | HTTP/HTTPS proxy。`protocol` 为 `"https"` 或 `"http"`；`host` 默认值为 `"127.0.0.1"`；`port` 默认值为 `9000`。 |
| `timeout` | integer ≥ 1 (ms) | No | `5000` | Abort 前等待 server 开始 response 的时间。 |
| `socket` | `{ keepAlive, maxSockets, maxFreeSockets }` | No | `{ keepAlive: true, maxSockets: 50, maxFreeSockets: 5 }` | Socket pool configuration。`maxSockets` 和 `maxFreeSockets` 是 integer ≥ 1。 |

```json
[
  {
    "type": "webhook",
    "label": "Audit",
    "subscribedEvents": ["n8n.audit", "n8n.workflow"],
    "anonymizeAuditMessages": true,
    "url": "https://hooks.example.com/n8n",
    "method": "POST",
    "sendHeaders": true,
    "specifyHeaders": "keypair",
    "headerParameters": {
      "parameters": [
        { "name": "Authorization", "value": "Bearer s3cret" }
      ]
    },
    "options": {
      "timeout": 5000,
      "redirect": { "redirect": { "followRedirects": true, "maxRedirects": 5 } }
    }
  }
]
```

### Syslog <a href="#syslog" id="syslog"></a>

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `host` | string | Yes | - | Syslog server hostname 或 IP。 |
| `port` | number | No | `514` | Syslog server port。 |
| `protocol` | `"udp"` \| `"tcp"` \| `"tls"` | No | `"udp"` | Transport protocol。 |
| `tlsCa` | string | When `protocol` is `"tls"` | `""` | TLS connection 使用的 PEM-formatted CA certificate。 |
| `facility` | number | No | `16` | Syslog facility code。Allowed values：`0` (Kernel)、`1` (User)、`3` (System)、`13` (Audit)、`14` (Alert)、`16` 到 `23` (Local0 到 Local7)。 |
| `app_name` | string | No | `"n8n"` | 作为 syslog `APP-NAME` 使用的 value。 |

```json
[
  {
    "type": "syslog",
    "label": "SIEM",
    "subscribedEvents": ["n8n.audit", "n8n.workflow"],
    "host": "syslog.example.com",
    "port": 514,
    "protocol": "tls",
    "tlsCa": "-----BEGIN CERTIFICATE-----\n…\n-----END CERTIFICATE-----",
    "facility": 16,
    "app_name": "n8n"
  }
]
```

### Sentry <a href="#sentry" id="sentry"></a>

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dsn` | string (URL) | Yes | - | Sentry DSN client key。 |

```json
[
  {
    "type": "sentry",
    "label": "Sentry prod",
    "subscribedEvents": ["n8n.workflow"],
    "dsn": "https://public@sentry.example.com/1"
  }
]
```

### Circuit breaker <a href="#circuit-breaker" id="circuit-breaker"></a>

Circuit breaker 会在 repeated failures 后临时停止向 destination delivery，防止给 struggling downstream service 增加 load。所有 destination types 都可使用。

| Field | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `maxFailures` | integer ≥ 1 | No | `5` | 当 `failureWindow` 内 failures 达到此数量时，n8n 停止向 destination 发送 requests。 |
| `failureWindow` | integer ≥ 100 (ms) | No | `60000` | 统计 failures 的 sliding window。较早 failures 会 expire。 |

```json
{ "circuitBreaker": { "maxFailures": 3, "failureWindow": 30000 } }
```

### Complete example <a href="#complete-example" id="complete-example"></a>

```bash
N8N_LOG_STREAMING_MANAGED_BY_ENV=true
N8N_LOG_STREAMING_DESTINATIONS='[
  {
    "type": "webhook",
    "label": "Ops webhook",
    "enabled": true,
    "subscribedEvents": ["n8n.workflow", "n8n.audit"],
    "anonymizeAuditMessages": true,
    "url": "https://hooks.example.com/n8n",
    "method": "POST",
    "sendHeaders": true,
    "specifyHeaders": "keypair",
    "headerParameters": {
      "parameters": [
        { "name": "Authorization", "value": "Bearer s3cret" }
      ]
    },
    "circuitBreaker": { "maxFailures": 5, "failureWindow": 60000 }
  },
  {
    "type": "sentry",
    "label": "Sentry prod",
    "subscribedEvents": ["n8n.workflow"],
    "dsn": "https://public@sentry.example.com/1"
  }
]'
```

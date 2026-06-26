---
title: OpenTelemetry tracing
description: >-
  将 workflow 和 node execution traces 从 n8n 发送到 OpenTelemetry collector。
contentType: howto
nodeTitle: Trace executions with OpenTelemetry
originalFilePath: hosting/logging-monitoring/opentelemetry.md
originalUrl: 'https://docs.n8n.io/hosting/logging-monitoring/opentelemetry'
url: >-
  https://docs.n8n.io/deploy/host-n8n/keep-n8n-running/trace-executions-with-opentelemetry
layout:
  description:
    visible: false
---

# OpenTelemetry tracing <a href="#opentelemetry-tracing" id="opentelemetry-tracing"></a>
{% hint style="warning" %}
**此功能仍在开发中**

- 最初从 2.19.0 起可用
- Open telemetry formatted metrics 即将推出
{% endhint %}

n8n 可以为 workflow 和 node executions 发出 [OpenTelemetry](https://opentelemetry.io/) traces。使用这些 traces 可以 monitor execution latency、debug failures，并在 observability stack 中跨 services 跟踪 requests。

{% hint style="info" %}
**功能可用性**

OpenTelemetry workflow tracing 仅适用于 self-hosted n8n。
{% endhint %}

观看 n8n 中 OpenTelemetry tracing 的 overview：

{% embed url="https://www.youtube.com/embed/xOi8K_-GLRM" %}

## 你会获得什么 <a href="#what-you-get" id="what-you-get"></a>

开启 tracing 后，n8n 会为每次 execution export 两类 spans：

- **`workflow.execute`**：每次 workflow execution 一个 span。它记录 workflow ID、name、version、node count、execution mode、status 和任何 error type。
- **`node.execute`**：每次 node execution 一个 span，嵌套在其 workflow span 中。它记录 node ID、name、type、version，以及 input 和 output items 数量。

每个 span 都包含用于识别 n8n instance 的 resource attributes：

- `service.name`（默认 `n8n`）
- `service.version`（n8n version）
- `n8n.instance.id`
- `n8n.instance.role`（例如 `main`、`worker` 或 `webhook`）

n8n 还会处理 trace context propagation：

- **Inbound**：如果 webhook request 包含 [W3C `traceparent` header](https://www.w3.org/TR/trace-context/)，n8n 会将其用作 workflow span 的 parent。这会把 n8n workflow trace 链接到 upstream caller。
- **Outbound**：HTTP Request nodes（以及使用 n8n HTTP helpers 的其他 nodes）可以向 outbound requests 注入 `traceparent` header。因此支持 W3C trace context 的 downstream services 可以继续该 trace。
- **Sub-workflows**：Sub-workflow 的 span 使用 parent workflow 的 span 作为 parent。
- **Resumed workflows**：当 workflow 在 wait 后 resume 时，new span 会使用 span link 链接回 previous span。

## 在 UI 中启用 tracing <a href="#enable-tracing-in-the-ui" id="enable-tracing-in-the-ui"></a>

{% hint style="info" %}
**从 n8n v2.27.0 起可用**

你需要是 instance owner 或 admin，才能在 UI 中配置 OpenTelemetry。
{% endhint %}

你可以从 **Settings > OpenTelemetry** 配置 tracing，而不是设置 environment variables。n8n 会在无需 restart 的情况下应用更改，并在 [queue mode](../configure-n8n/scaling/enable-queue-mode.md) 中跨 workers 和 webhook processors reload 它们。

配置 tracing：

1. 选择 **Settings > OpenTelemetry**。
1. 打开 **Enable OpenTelemetry**。
1. 在 **Collector connection** 下，输入你的 **OTLP endpoint** 和任何其他 connection details。
1. 在 **Tracing** 下，设置 sampling 和 span options。
1. 选择 **Save settings**。

要检查 n8n 是否可以访问 collector，请在 **Verify configuration** 下选择 **Send test trace**。n8n 会发送单个 test span，并报告 collector 是否接受了它。你可以在保存前或保存后运行它。

每个 field 都映射到一个 environment variable，并显示在 field tooltip 中。完整列表请参阅 [OpenTelemetry environment variables](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)。

{% hint style="info" %}
**Environment variables 优先**

如果你用 environment variable 设置某个 option，n8n 会使用该值，并在 UI 中禁用匹配 field。要从 UI 管理 setting，请不要设置它的 environment variable。n8n restart 时，environment variables 会覆盖保存在 UI 中的值。
{% endhint %}

## 使用 environment variables 启用 tracing <a href="#enable-tracing-with-environment-variables" id="enable-tracing-with-environment-variables"></a>

在每个你想启用 workflow tracing 的 n8n instance（main、workers 和 webhook processors）上设置以下 environment variables：

```bash
export N8N_OTEL_ENABLED=true
export N8N_OTEL_EXPORTER_OTLP_ENDPOINT=http://<your-collector-host>:4318
```

Restart n8n。Instance 会开始通过 OTLP HTTP 使用 Protobuf encoding export spans。

n8n 默认会向 endpoint 追加 `/v1/traces`。请将 `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` 指向 collector 的 base URL，而不是 traces path。

如果你的 collector 需要 authentication，请将 `N8N_OTEL_EXPORTER_OTLP_HEADERS` 设置为以 comma 分隔的 `key=value` pairs：

```bash
export N8N_OTEL_EXPORTER_OTLP_HEADERS="authorization=Bearer <your-token>,x-tenant=acme"

// For added protection - It is recommended to use the `_FILE` postfix if you are putting a token in here:
export N8N_OTEL_EXPORTER_OTLP_HEADERS_FILE=/mnt/otel-headers
```

支持 variables 的完整列表请参考 [OpenTelemetry environment variables](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)。

{% hint style="info" %}
**Queue mode**

在 [queue mode](../configure-n8n/scaling/enable-queue-mode.md) 中，OpenTelemetry variables 必须设置在所有 instances 上。Trace context 会在 instances 之间传播。
{% endhint %}

## Sampling <a href="#sampling" id="sampling"></a>

默认情况下，n8n 会 export 每条 trace。要在繁忙 instances 中减少 volume，请将 `N8N_OTEL_TRACES_SAMPLE_RATE` 设置为 `0` 到 `1` 之间的值：

```bash
# Export 10% of traces <a href="#export-10percent-of-traces" id="export-10percent-of-traces"></a>
export N8N_OTEL_TRACES_SAMPLE_RATE=0.1
```

n8n 使用 trace ID ratio sampler，因此同一 trace ID 在 trace 的所有 spans 中要么完整 sampled，要么完整 dropped。

{% hint style="info" %}
默认情况下，n8n 只为 [production executions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/types-of-executions) 输出 traces。要为所有 workflow executions 输出 traces，请设置 `N8N_OTEL_TRACES_PRODUCTION_ONLY=false`。
{% endhint %}

## 减少 span volume <a href="#reduce-span-volume" id="reduce-span-volume"></a>

Workflow 中的每个 node 都会生成自己的 span。对于包含大量 nodes 的 workflows，这可能产生超过你所需的数据。要只 export workflow-level spans，请设置：

```bash
export N8N_OTEL_TRACES_INCLUDE_NODE_SPANS=false
```

要阻止 n8n 向 outbound HTTP requests 注入 `traceparent` headers，请设置：

```bash
export N8N_OTEL_TRACES_INJECT_OUTBOUND=false
```

## Custom span attributes <a href="#custom-span-attributes" id="custom-span-attributes"></a>

你可以向 project、workflow 和 node spans 添加 custom attributes。n8n 会将每个 custom attribute 作为 OpenTelemetry span attribute export 到你配置的 observability backend。

{% hint style="info" %}
**功能可用性**

Custom span attributes 可用于 Enterprise plans。
{% endhint %}

不要在 attribute values 中包含 secrets、personal data 或其他 sensitive values。

n8n 支持以下 custom attribute levels：

| Level | Configure in | Exported span | Attribute prefix |
| :---- | :----------- | :------------ | :--------------- |
| Project | **Project settings** | `workflow.execute` | `n8n.project.custom.<key>` |
| Workflow | **Workflow settings** | `workflow.execute` | `n8n.workflow.custom.<key>` |
| Node | Node **Settings** tab | `node.execute` | `n8n.node.custom.<key>` |

Project 和 workflow custom span attributes 从 n8n `2.24.0` 起可用。Node custom span attributes 从 n8n `2.22.0` 起可用。

### 添加 project span attributes <a href="#add-project-span-attributes" id="add-project-span-attributes"></a>

添加 project-level span attributes：

1. 打开 project。
1. 选择 **Project settings**。
1. 在 **Custom Span Attributes** 下，添加一个或多个 span attributes。
1. 选择 **Save**。

Project attribute values 使用 plain text。

### 添加 workflow span attributes <a href="#add-workflow-span-attributes" id="add-workflow-span-attributes"></a>

添加 workflow-level span attributes：

1. 打开 workflow。
1. 打开 **Workflow settings**。
1. 在 **Custom Span Attributes** 下，选择 **Configure**。
1. 添加一个或多个 span attributes。
1. 选择 **Save**。

Workflow attribute values 使用 plain text。

### 添加 node span attributes <a href="#add-node-span-attributes" id="add-node-span-attributes"></a>

添加 node-level span attributes：

1. 打开 node，并选择 **Settings** tab。
1. 在 **Custom Span Attributes** 下，选择 **Add Attribute**。
1. 输入 **Key**。Keys 必须是 plain text。
1. 输入 **Value**。Values 可以是 plain text 或 expressions，例如 `={{ $json.environment }}`。

Node attribute values 必须 resolve 为 string、number 或 boolean。

### 在 custom node 中以编程方式添加 attributes <a href="#add-attributes-programmatically-in-a-custom-node" id="add-attributes-programmatically-in-a-custom-node"></a>

如果你正在[构建 custom node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview)，可以从 code 附加 custom key-value pairs。请从 node 的 `execute` method 调用 `setMetadata`：

```typescript
async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
	this.setMetadata({
		tracing: {
			'llm.model': 'gpt-4o',
			'llm.token.input': 1500,
			'llm.token.output': 340,
		},
	});

	return [this.getInputData()];
}
```

n8n 会在 exported span 上为每个 key 加上 `n8n.node.custom.` prefix。Values 必须是 strings、numbers 或 boolean。

此 API 不能从 Code node 使用。它面向希望用 domain-specific data 丰富 spans 的 node authors。

如果 node 在这里设置的 attribute key 也被配置为 [custom node span attribute](#add-node-span-attributes)，programmatic value 会优先。

## 使用 Jaeger 试用 <a href="#try-it-out-with-jaeger" id="try-it-out-with-jaeger"></a>

你可以将 traces 发送到本地 [Jaeger](https://www.jaegertracing.io/) instance，查看实际效果。

1. 将以下内容保存为 `docker-compose.yml`：

```yaml
services:
  jaeger:
    image: jaegertracing/jaeger:latest
    ports:
      - "16686:16686" # UI
      - "4317:4317"   # OTLP gRPC
      - "4318:4318"   # OTLP HTTP
```

2. 启动 Jaeger：

```bash
docker compose up -d
```

3. 启动 n8n，打开 tracing，并指向 Jaeger。Setup details 请参考 [starting n8n](https://github.com/n8n-io/n8n/blob/master/CONTRIBUTING.md)：

```bash
N8N_OTEL_ENABLED=true N8N_OTEL_EXPORTER_OTLP_ENDPOINT=http://127.0.0.1:4318 n8n start
```

5. 运行一个 workflow，然后在 [http://localhost:16686](http://localhost:16686) 打开 Jaeger UI。选择 "n8n" 作为 service，并点击 "Find traces"，查看 n8n 发出的 OpenTelemetry traces。

## Span attributes <a href="#span-attributes" id="span-attributes"></a>

Workflow 和 node spans 包含以下 n8n-specific attributes。

### Workflow span (`workflow.execute`) <a href="#workflow-span-workflowexecute" id="workflow-span-workflowexecute"></a>

| Attribute | Description |
| :-------- | :---------- |
| `n8n.workflow.id` | Workflow ID。 |
| `n8n.workflow.name` | Workflow name。 |
| `n8n.workflow.version_id` | Workflow version ID。 |
| `n8n.workflow.node_count` | Workflow 中的 nodes 数量。 |
| `n8n.project.id` | Project ID。从 n8n `2.23.0` 起可用。 |
| `n8n.execution.id` | Execution ID。 |
| `n8n.execution.mode` | Execution mode（例如 `manual`、`webhook`、`trigger`、`retry`）。 |
| `n8n.execution.status` | Final execution status。 |
| `n8n.execution.is_retry` | 如果 execution 是 retry，则为 `true`。 |
| `n8n.execution.retry_of` | 当 execution 是 retry 时，原始 execution ID。 |
| `n8n.execution.error_type` | Error class name，在 execution 失败时设置。 |
| `n8n.continuation.reason` | Workflow 在 wait 后 resume 时，设置在 span link 上。 |
| `n8n.project.custom.<key>` | 通过 [project-level custom span attributes](#custom-span-attributes) 设置的 custom attributes。 |
| `n8n.workflow.custom.<key>` | 通过 [workflow-level custom span attributes](#custom-span-attributes) 设置的 custom attributes。 |

### Node span (`node.execute`) <a href="#node-span-nodeexecute" id="node-span-nodeexecute"></a>

| Attribute | Description |
| :-------- | :---------- |
| `n8n.node.id` | Node ID。 |
| `n8n.node.name` | Node name。 |
| `n8n.node.type` | Node type（例如 `n8n-nodes-base.httpRequest`）。 |
| `n8n.node.type_version` | Node type version。 |
| `n8n.node.items.input` | Node received 的 input items 数量。 |
| `n8n.node.items.output` | Node produced 的 output items 数量。 |
| `n8n.node.termination_reason` | Node span 未正常完成而结束的原因（例如 `workflow_cancelled`）。 |
| `n8n.node.custom.<key>` | 通过 node settings 中的 [node-level custom span attributes](#custom-span-attributes) 或 custom node code 中的 `metadata.tracing` 设置的 custom attributes。 |

当 node 失败时，n8n 会在 span 上记录一个 `exception` event，并包含标准 OpenTelemetry exception attributes（`exception.type`、`exception.message`、`exception.stacktrace`）。

## 故障排查 <a href="#troubleshooting" id="troubleshooting"></a>

### Backend 中没有出现 traces <a href="#no-traces-appear-in-your-backend" id="no-traces-appear-in-your-backend"></a>

如果 n8n 在 startup 时无法访问 OTLP endpoint，它会记录 error：

```
Failed to connect to OpenTelemetry OTLP endpoint during startup
```

检查：

- `N8N_OTEL_ENABLED` 已设置为 `true`。
- `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` 指向 collector 的 base URL（不是 `/v1/traces` path）。
- Collector 可从 n8n container 或 host 访问。
- 已设置任何必需的 `N8N_OTEL_EXPORTER_OTLP_HEADERS`（例如 authentication tokens）。

n8n 默认以 `warn` level 记录 OpenTelemetry diagnostics。设置 `N8N_LOG_LEVEL=debug` 可查看更多 detail。

### Custom span attributes 缺失 <a href="#custom-span-attributes-are-missing" id="custom-span-attributes-are-missing"></a>

检查：

- 你拥有 Enterprise license。
- 你已将 `N8N_OTEL_ENABLED` 设置为 `true`。
- 对于 node-level span attributes，`N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` 未设置为 `false`。

### Worker traces 缺少 parent context <a href="#worker-traces-are-missing-parent-context" id="worker-traces-are-missing-parent-context"></a>

在 queue mode 中，workers 会从 database 读取 parent trace context。如果你只在 main instance 上设置 OpenTelemetry environment variables，worker spans 不会链接到 parent workflow trace。请在每种 instance type 上设置相同 variables。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

- [OpenTelemetry environment variables](../configure-n8n/basic-configuration/use-environment-variables/opentelemetry.md)
- [W3C Trace Context specification](https://www.w3.org/TR/trace-context/)
- [OpenTelemetry Collector documentation](https://opentelemetry.io/docs/collector/)
- [Logging in n8n](set-up-logging.md)
- [Monitoring](monitor-n8n.md)

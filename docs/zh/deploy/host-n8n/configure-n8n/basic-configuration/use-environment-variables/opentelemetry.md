---
title: OpenTelemetry environment variables
description: >-
  使用环境变量为你的 self-hosted n8n 实例配置 OpenTelemetry tracing。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: OpenTelemetry
originalFilePath: hosting/configuration/environment-variables/opentelemetry.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/opentelemetry'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/opentelemetry
layout:
  description:
    visible: false
---

# OpenTelemetry 环境变量 <a href="#opentelemetry-environment-variables" id="opentelemetry-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

n8n 可以通过 OTLP 将 workflow 和 node execution traces 导出到 OpenTelemetry collector。详情请参考 [OpenTelemetry tracing](../../../keep-n8n-running/trace-executions-with-opentelemetry.md)。

| Variable | Type | Default | Description | 可用版本 |
| :------- | :--- | :------ | :---------- | :------
| `N8N_OTEL_ENABLED` | Boolean | `false` | 是否启用 OpenTelemetry tracing。设为 `false` 时，n8n 不会加载 OpenTelemetry SDK。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_ENDPOINT` | String | `http://localhost:4318` | 用于导出 traces 的 OTLP HTTP endpoint Base URL。n8n 会将 `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` 的值追加到此 URL。 |  2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_TRACING_PATH` | String | `/v1/traces` | 追加到 `N8N_OTEL_EXPORTER_OTLP_ENDPOINT`、用于导出 traces 的 path。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_OTLP_HEADERS` | String | - | 要随每个 OTLP request 作为 HTTP headers 发送的 `key=value` pairs 逗号分隔列表。可用于 authentication tokens 或 tenant headers。例如：`authorization=Bearer <token>,x-tenant=acme`。 | 2.19.0 |
| `N8N_OTEL_EXPORTER_SERVICE_NAME` | String | `n8n` | exported spans 上 `service.name` resource attribute 的值。 | 2.19.0 |
| `N8N_OTEL_TRACES_SAMPLE_RATE` | Number | `1.0` | 要导出的 traces 比例，范围为 `0` 到 `1`。n8n 使用 trace ID ratio sampler，因此同一个 trace 中的所有 spans 要么一起被 sampled，要么一起 dropped。 | 2.19.0 |
| `N8N_OTEL_TRACES_INCLUDE_NODE_SPANS` | Boolean | `true` | 是否为每次 node execution 发出一个 `node.execute` span。设为 `false` 时只导出 workflow-level spans。 | 2.19.0 |
| `N8N_OTEL_TRACES_PRODUCTION_ONLY` | Boolean | `true` | 是否仅为 [production executions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/types-of-executions) 导出 traces。设为 `false` 可为所有 workflow executions 导出 traces。 | 2.25.2 |
| `N8N_OTEL_TRACES_INJECT_OUTBOUND` | Boolean | `true` | 是否将 W3C `traceparent`/`tracesstate` headers 注入由使用 n8n HTTP helpers 的 nodes 发出的 outbound HTTP requests。 | 2.19.0 |
| `N8N_OTEL_STARTUP_CONNECTIVITY_TIMEOUT_MS` | Number | `2000` | 启动时检查 OTLP endpoint 连通性的超时时间，单位为毫秒。如果 endpoint 在此时间内不可达，n8n 会记录 warning。 | 2.19.0 |

---
title: Endpoints environment variables
description: >-
  使用环境变量自定义 self-hosted n8n 实例的应用 API 和 webhook endpoints。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Endpoints
originalFilePath: hosting/configuration/environment-variables/endpoints.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/endpoints'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints
layout:
  description:
    visible: false
---

# Endpoints 环境变量 <a href="#endpoints-environment-variables" id="endpoints-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

本页列出用于自定义 n8n endpoints 的环境变量。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_PAYLOAD_SIZE_MAX` | Number | `16` | 最大 payload 大小，单位为 MiB。默认值为 16 MiB，但可以通过把该变量调高来增加。n8n 实例需要重启才能应用新设置。注意：增加 payload 大小需要更多内存和 CPU 资源，并可能影响性能。请确保你的基础设施能够处理更大的 payload。 |
| `N8N_FORMDATA_FILE_SIZE_MAX` | Number | `200` | form-data webhook payload 中的文件最大 payload 大小，单位为 MiB。 |
| `N8N_METRICS` | Boolean | `false` | 是否启用 `/metrics` endpoint。 |
| `N8N_METRICS_PREFIX` | String | `n8n_` | n8n 特定 metrics 名称的可选前缀。 |
| `N8N_METRICS_INCLUDE_DEFAULT_METRICS` | Boolean | `true` | 是否暴露默认 system 和 node.js metrics。 |
| `N8N_METRICS_INCLUDE_CACHE_METRICS` | Boolean | false | 是否包含 cache hits 和 misses 的 metrics：`true` 表示包含，`false` 表示不包含。 |
| `N8N_METRICS_INCLUDE_MESSAGE_EVENT_BUS_METRICS` | Boolean | `false` | 是否包含 events 的 metrics：`true` 表示包含，`false` 表示不包含。 |
| `N8N_METRICS_INCLUDE_WORKFLOW_ID_LABEL` | Boolean | `false` | 是否在 workflow metrics 上包含 workflow ID label。 |
| `N8N_METRICS_INCLUDE_NODE_TYPE_LABEL` | Boolean | `false` | 是否在 node metrics 上包含 node type label。 |
| `N8N_METRICS_INCLUDE_CREDENTIAL_TYPE_LABEL` | Boolean | `false` | 是否在 credential metrics 上包含 credential type label。 |
| `N8N_METRICS_INCLUDE_API_ENDPOINTS` | Boolean | `false` | 是否暴露 API endpoints 的 metrics。 |
| `N8N_METRICS_INCLUDE_API_PATH_LABEL` | Boolean | `false` | 是否包含 API 调用 path 的 label。 |
| `N8N_METRICS_INCLUDE_API_METHOD_LABEL` | Boolean | `false` | 是否包含 API 调用 HTTP method（GET、POST 等）的 label。 |
| `N8N_METRICS_INCLUDE_API_STATUS_CODE_LABEL` | Boolean | `false` | 是否包含 API 调用 HTTP status code（200、404 等）的 label。 |
| `N8N_METRICS_INCLUDE_QUEUE_METRICS` | Boolean | `false` | 是否包含 scaling mode 中 jobs 的 metrics。 |
| `N8N_METRICS_QUEUE_METRICS_INTERVAL` | Integer | `20` | 更新 queue metrics 的频率，单位为秒。 |
| `N8N_METRICS_INCLUDE_SSRF_METRICS` | Boolean | `false` | 是否包含 SSRF protection checks 的 metrics。 |
| `N8N_METRICS_INCLUDE_DNS_CACHE_METRICS` | Boolean | `false` | 是否包含 DNS cache 的 metrics（目前仅由 SSRF protection 使用）。 |
| `N8N_ENDPOINT_REST` | String | `rest` | REST endpoint 使用的 path。 |
| `N8N_ENDPOINT_WEBHOOK` | String | `webhook` | webhook endpoint 使用的 path。 |
| `N8N_ENDPOINT_WEBHOOK_TEST` | String | `webhook-test` | test-webhook endpoint 使用的 path。 |
| `N8N_ENDPOINT_WEBHOOK_WAIT` | String | `webhook-waiting` | waiting-webhook endpoint 使用的 path。 |
| `N8N_ENDPOINT_HEALTH` | String | `healthz` | health check endpoint 使用的 path。 |
| `WEBHOOK_URL` | String | - | 在 reverse proxy 后运行 n8n 时，用于手动提供 Webhook URL。更多详情请见[这里](../configuration-examples/configure-webhook-urls-with-reverse-proxy.md)。 |
| `N8N_DISABLE_PRODUCTION_MAIN_PROCESS` | Boolean | `false` | 从 main process 禁用 production webhooks。使用 webhook-specific processes 时，这有助于确保没有 HTTP traffic 负载打到 main process。 |

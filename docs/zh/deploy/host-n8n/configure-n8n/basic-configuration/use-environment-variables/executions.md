---
title: Executions environment variables
description: 用于配置 workflow executions 相关设置的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Executions
originalFilePath: hosting/configuration/environment-variables/executions.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/executions'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/executions
layout:
  description:
    visible: false
---

# Executions 环境变量 <a href="#executions-environment-variables" id="executions-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

本页列出用于配置 workflow execution 设置的环境变量。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `EXECUTIONS_MODE` | Enum string: `regular`, `queue` | `regular` | executions 应直接运行还是使用 queue。<br><br>更多详情请参考 [Queue mode](../../scaling/enable-queue-mode.md)。 |
| `EXECUTIONS_TIMEOUT` | Number | `-1` | 为所有 workflows 设置默认超时时间，单位为秒；超时后 n8n 会停止执行。用户可以为单个 workflow 覆盖该值，但不能超过 `EXECUTIONS_TIMEOUT_MAX` 设置的时长。将 `EXECUTIONS_TIMEOUT` 设为 `-1` 可禁用。 |
| `EXECUTIONS_TIMEOUT_MAX` | Number | `3600` | 用户可为单个 workflow 设置的最大执行时间，单位为秒。 |
| `N8N_AI_TIMEOUT_MAX` | Number | `3600000` | 为 AI 和 LLM nodes（如 OpenAI、Anthropic、Mistral 和 Ollama）设置 HTTP request 超时时间，单位为毫秒。它控制 n8n 在超时前等待 AI 服务响应的时间。对较慢的本地 AI 服务或需要更长处理时间的复杂 prompts 很有用。 |
| `EXECUTIONS_DATA_SAVE_ON_ERROR` | Enum string: `all`, `none` | `all` | n8n 是否在出错时保存 execution data。 |
| `EXECUTIONS_DATA_SAVE_ON_SUCCESS` | Enum string: `all`, `none` | `all` | n8n 是否在成功时保存 execution data。 |
| `EXECUTIONS_DATA_SAVE_ON_PROGRESS` | Boolean | `false` | 是否保存每个已执行 node 的进度：`true` 表示保存，`false` 表示不保存。 |
| `EXECUTIONS_DATA_SAVE_MANUAL_EXECUTIONS` | Boolean | `true` | 是否保存手动启动的 executions 数据。 |
| `N8N_EXECUTION_DATA_STORAGE_MODE` | Enum string: `database`, `filesystem`, `s3`, `azure` | `database` | n8n 存储 execution data 的位置。`s3` 和 `azure` 模式需要 Enterprise license。相关存储变量请参考 [External data storage](external-data-storage.md)。 |
| `N8N_STORAGE_PATH` | String | `N8N_USER_FOLDER/storage` | filesystem storage 的 base path。当 `N8N_EXECUTION_DATA_STORAGE_MODE` 为 `filesystem` 时，n8n 会在这里存储 execution data。n8n 也会把该路径用于 filesystem binary data。 |
| `EXECUTIONS_DATA_PRUNE` | Boolean | `true` | 是否滚动删除过去的 executions 数据。 |
| `EXECUTIONS_DATA_MAX_AGE` | Number | `336` | execution 被删除前的保留时长，单位为小时。 |
| `EXECUTIONS_DATA_PRUNE_MAX_COUNT` | Number | `10000` | 数据库中最多保留的 executions 数量。0 表示无限制。 |
| `EXECUTIONS_DATA_HARD_DELETE_BUFFER` | Number | `1` | 已完成 execution data 需要经过多久才会被 hard-delete，单位为小时。默认情况下，此缓冲会排除最近的 executions，因为用户构建 workflow 时可能需要它们。 |
| `EXECUTIONS_DATA_PRUNE_HARD_DELETE_INTERVAL` | Number | `15` | hard-delete execution data 的频率，单位为分钟。 |
| `EXECUTIONS_DATA_PRUNE_SOFT_DELETE_INTERVAL` | Number | `60` | soft-delete execution data 的频率，单位为分钟。 |
| `N8N_CONCURRENCY_PRODUCTION_LIMIT` | Number | `-1` | regular 和 scaling modes 中允许并发运行的最大 production executions 数量。`-1` 表示在 regular mode 中禁用限制。 |
| `N8N_CONCURRENCY_EVALUATION_LIMIT` | Number | License-tier default | 单次 [evaluation](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/integrate-ai/test-and-improve-ai-workflows/use-metrics-to-measure-quality#run-test-cases-in-parallel) 测试运行中可并行执行的最大 test cases 数量。未设置时，该限制遵循 license tier（Community/Pro：1，Business：3，Enterprise：5）。设置此项会覆盖 tier 默认值。 |
| `N8N_WORKFLOW_AUTODEACTIVATION_ENABLED` | Boolean | `false` | workflows 是否会在重复 crashed executions 后自动取消发布。 |
| `N8N_WORKFLOW_AUTODEACTIVATION_MAX_LAST_EXECUTIONS` | Number | `3` | 取消发布 workflow 前允许的 crashed executions 数量。 |

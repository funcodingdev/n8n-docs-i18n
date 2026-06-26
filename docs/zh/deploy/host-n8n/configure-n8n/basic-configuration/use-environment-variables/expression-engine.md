---
title: Expression engine environment variables
description: >-
  为你的 self-hosted n8n 实例配置 expression evaluation engine 及其 V8 isolate pool。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Expression engine
originalFilePath: hosting/configuration/environment-variables/expression-engine.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/expression-engine
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/expression-engine
layout:
  description:
    visible: false
---

# Expression engine 环境变量 <a href="#expression-engine-environment-variables" id="expression-engine-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

[Expressions](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 是 n8n 在运行时求值的 JavaScript snippets，用于动态设置 node parameters。expression engine 是运行该求值过程的组件。本页列出用于配置它的环境变量。

{% hint style="info" %}
**实验性**

`vm` engine 是实验性的。n8n 默认运行 `legacy` engine。除 `N8N_EXPRESSION_ENGINE` 外，下面的变量只有在你将 `N8N_EXPRESSION_ENGINE` 设为 `vm` 时才会生效。
{% endhint %}

| Variable | Type | Default | Description |
| :------- | :--- | :------ | :---------- |
| `N8N_EXPRESSION_ENGINE` | Enum string: `legacy`, `vm` | `legacy` | 要使用的 expression engine。`legacy` 不做隔离直接运行 expressions。`vm` 会在 sandboxed V8 isolate 中运行。`vm` 是实验性的；`legacy` 仍是默认值。 |
| `N8N_EXPRESSION_ENGINE_POOL_SIZE` | Number | `1` | pool 中保持 warm 状态的 V8 isolates 数量。 |
| `N8N_EXPRESSION_ENGINE_MAX_CODE_CACHE_SIZE` | Number | `1024` | 可缓存的 compiled expressions 最大数量。 |
| `N8N_EXPRESSION_ENGINE_TIMEOUT` | Number | `5000` | 每次 expression evaluation 的执行超时时间，单位为毫秒。 |
| `N8N_EXPRESSION_ENGINE_MEMORY_LIMIT` | Number | `128` | 每个 V8 isolate 的内存限制，单位为 MiB。 |
| `N8N_EXPRESSION_ENGINE_IDLE_TIMEOUT` | Number | - | 如果设置，在没有活动达到这么多秒后，将 isolate pool 扩缩到零个 warm isolates。 |

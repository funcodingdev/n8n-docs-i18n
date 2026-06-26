---
title: SSRF protection environment variables
description: 为你的 self-hosted n8n 实例配置 SSRF protection。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: SSRF protection
originalFilePath: hosting/configuration/environment-variables/ssrf-protection.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/ssrf-protection
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/ssrf-protection
layout:
  description:
    visible: false
---

# SSRF protection 环境变量 <a href="#ssrf-protection-environment-variables" id="ssrf-protection-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

这些变量控制对向 user-controllable targets 发起 HTTP requests 的 nodes 的 [SSRF protection](../../security/enable-ssrf-protection.md)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_SSRF_PROTECTION_ENABLED` | Boolean | `false` | 是否为发起 HTTP requests 的 nodes 启用 SSRF protection。 |
| `N8N_SSRF_BLOCKED_IP_RANGES` | String | Standard private/reserved ranges | 要阻止的 CIDR ranges 逗号分隔列表。使用 `default` 可包含 [standard blocked ranges](../../security/enable-ssrf-protection.md#default-blocked-ranges)，也可以和 custom ranges 组合使用（例如：`default,100.0.0.0/8`）。 |
| `N8N_SSRF_ALLOWED_IP_RANGES` | String | - | 要允许的 CIDR ranges 逗号分隔列表。优先级高于 blocked ranges。 |
| `N8N_SSRF_ALLOWED_HOSTNAMES` | String | - | 要允许的 hostname patterns 逗号分隔列表。支持 wildcards（例如：`*.n8n.internal`）。优先级高于 blocked IP ranges。 |
| `N8N_SSRF_DNS_CACHE_MAX_SIZE` | Number | `1048576` | 最大 DNS cache 大小，单位为 bytes。达到限制时使用 LRU eviction。默认值为 1 MB。 |

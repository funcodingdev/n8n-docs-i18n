---
title: SSRF protection
description: >-
  保护你的 self-hosted n8n 实例免受 Server-Side Request Forgery (SSRF) attacks。
contentType: howto
nodeTitle: Enable SSRF protection
originalFilePath: hosting/securing/ssrf-protection.md
originalUrl: 'https://docs.n8n.io/hosting/securing/ssrf-protection'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/enable-ssrf-protection
layout:
  description:
    visible: false
---

# SSRF protection <a href="#ssrf-protection" id="ssrf-protection"></a>

{% hint style="info" %}
**从 2.12.0 起可用**

{% endhint %}

Server-Side Request Forgery (SSRF) attacks 会滥用 workflow nodes，向 internal network resources、cloud metadata endpoints 或不应访问的 localhost services 发起 requests。

{% hint style="warning" %}
SSRF protection 是额外的 application-level defense。你应始终在基础设施上配置 network-level protections（firewalls、security groups、network policies）作为主要防线。n8n 的 SSRF protection 会在这些控制之上增加 defense-in-depth。
{% endhint %}

## 启用 SSRF protection <a href="#enable-ssrf-protection" id="enable-ssrf-protection"></a>

```
N8N_SSRF_PROTECTION_ENABLED=true
```

启用后，n8n 会根据已配置的 blocked 和 allowed ranges，验证来自 user-controllable nodes（例如 HTTP Request node）的所有 outbound HTTP requests。这包括 redirect targets 和 DNS resolution，以防止 DNS rebinding 等绕过技术。

## 默认 blocked ranges <a href="#default-blocked-ranges" id="default-blocked-ranges"></a>

启用 SSRF protection 后，默认会阻止以下 IP ranges：

| Range | Description |
| :---- | :---------- |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | RFC 1918 private addresses |
| `127.0.0.0/8`, `::1/128` | Loopback |
| `169.254.0.0/16`, `fe80::/10` | Link-local |
| `fc00::/7`, `fd00::/8` | IPv6 unique local |
| `0.0.0.0/8`, `192.0.0.0/24`, `192.0.2.0/24`, `198.18.0.0/15`, `198.51.100.0/24`, `203.0.113.0/24` | Reserved/special purpose |

你可以使用 `N8N_SSRF_BLOCKED_IP_RANGES=default,100.0.0.0/8` 扩展此列表。

## 允许访问 internal services <a href="#allow-access-to-internal-services" id="allow-access-to-internal-services"></a>

如果你的 workflows 需要访问合法 internal services，请使用 allowlists。Allowlists 的优先级高于 blocklists，顺序如下：hostname allowlist > IP allowlist > IP blocklist。

按 hostname pattern 允许访问（支持 `*.n8n.internal` 这类 wildcards）：

```
N8N_SSRF_ALLOWED_HOSTNAMES=*.n8n.internal,*.company.local
```

按 IP range 允许访问：

```
N8N_SSRF_ALLOWED_IP_RANGES=10.0.1.0/24,10.0.2.50/32
```

{% hint style="warning" %}
只 allowlist 你控制范围内的 hostnames（internal DNS zones）。Hostname allowlists 会绕过 IP blocklist checks。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

完整配置选项列表请参考 [SSRF protection environment variables](../basic-configuration/use-environment-variables/ssrf-protection.md)。

有关设置环境变量的更多信息，请参考 [Configuration methods](../basic-configuration.md)。

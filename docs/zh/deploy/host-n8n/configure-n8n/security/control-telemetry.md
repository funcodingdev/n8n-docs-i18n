---
title: 退出数据收集
contentType: howto
nodeTitle: Control telemetry
originalFilePath: hosting/securing/telemetry-opt-out.md
originalUrl: https://docs.n8n.io/hosting/securing/telemetry-opt-out
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry
description: 在你的 n8n 实例上退出 data telemetry collection。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 控制 telemetry

n8n 会从 self-hosted n8n installations 收集一些匿名数据。使用以下说明退出 data telemetry collection。

## 收集的数据 <a href="#collected-data" id="collected-data"></a>

有关 n8n 收集的数据详情，请参考 [Privacy | Data collection in self-hosted n8n](https://app.gitbook.com/s/ukPPOMQ6NId4gpAIkPXa/#data-collection-in-self-hosted-n8n)。

## 收集如何工作 <a href="#how-collection-works" id="how-collection-works"></a>

你的 n8n instance 会在生成大多数数据的 events 发生时，将这些数据发送给 n8n。Workflow execution counts 和 instance pulse 会定期发送（每 6 小时一次）。这些数据类型主要属于 n8n telemetry collection。

## 退出数据收集 <a href="#opting-out-of-data-collection" id="opting-out-of-data-collection"></a>

n8n 默认启用 telemetry collection。要禁用它，请配置以下环境变量。

### 退出 telemetry events <a href="#opt-out-of-telemetry-events" id="opt-out-of-telemetry-events"></a>

要退出 telemetry events，请将 `N8N_DIAGNOSTICS_ENABLED` 环境变量设为 false，例如：

```bash
export N8N_DIAGNOSTICS_ENABLED=false
```

### 退出检查 n8n 新版本 <a href="#opt-out-of-checking-for-new-versions-of-n8n" id="opt-out-of-checking-for-new-versions-of-n8n"></a>

要退出检查 n8n 新版本，请将 `N8N_VERSION_NOTIFICATIONS_ENABLED` 环境变量设为 false，例如：

```bash
export N8N_VERSION_NOTIFICATIONS_ENABLED=false
```

## 禁用与 n8n servers 的所有连接 <a href="#disable-all-connection-to-n8n-servers" id="disable-all-connection-to-n8n-servers"></a>

如果你想完全阻止与 n8n servers 的所有通信，请参考 [Isolate n8n](../basic-configuration/configuration-examples/isolate-n8n.md)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些环境变量的更多信息，请参考 [Deployment environment variables](../basic-configuration/use-environment-variables/deployment.md)。

有关设置环境变量的更多信息，请参考 [Configuration](../basic-configuration.md)。

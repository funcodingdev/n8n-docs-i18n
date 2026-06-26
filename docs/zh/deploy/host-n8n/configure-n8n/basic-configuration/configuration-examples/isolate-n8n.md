---
title: Isolate n8n
description: 阻止你的 n8n instance 连接到 n8n servers。
contentType: howto
nodeTitle: Isolate n8n
originalFilePath: hosting/configuration/configuration-examples/isolation.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/isolation'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/isolate-n8n
layout:
  description:
    visible: false
---

# 隔离 n8n <a href="#isolate-n8n" id="isolate-n8n"></a>

默认情况下，自托管 n8n instance 会向 n8n servers 发送数据。它会通知 users 可用 updates、workflow templates 和 diagnostics。

要阻止 n8n instance 连接到 n8n servers，请将这些环境变量设置为 false：

```
N8N_DIAGNOSTICS_ENABLED=false
N8N_VERSION_NOTIFICATIONS_ENABLED=false
N8N_TEMPLATES_ENABLED=false
```

取消设置 n8n diagnostics configuration：

```
EXTERNAL_FRONTEND_HOOKS_URLS=
N8N_DIAGNOSTICS_CONFIG_FRONTEND=
N8N_DIAGNOSTICS_CONFIG_BACKEND=
```

有关这些变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/deployment.md)。

---
title: 禁用 public REST API
description: 禁用 n8n public REST API，防止其他人使用它。
contentType: howto
nodeTitle: Disable the public API
originalFilePath: hosting/securing/disable-public-api.md
originalUrl: 'https://docs.n8n.io/hosting/securing/disable-public-api'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/disable-the-public-api
layout:
  description:
    visible: false
---

# 禁用 public REST API <a href="#disable-the-public-rest-api" id="disable-the-public-rest-api"></a>

[n8n public REST API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api) 允许你以编程方式执行许多与 n8n GUI 中相同的任务。

如果不计划使用此 API，n8n 建议禁用它，以提高 n8n 安装的安全性。

要禁用 [public REST API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)，请将 `N8N_PUBLIC_API_DISABLED` 环境变量设为 `true`，例如：

```bash
export N8N_PUBLIC_API_DISABLED=true
```

## 禁用 API playground <a href="#disable-the-api-playground" id="disable-the-api-playground"></a>

要禁用 [API playground](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api/use-an-api-playground)，请将 `N8N_PUBLIC_API_SWAGGERUI_DISABLED` 环境变量设为 `true`，例如：

```bash
export N8N_PUBLIC_API_SWAGGERUI_DISABLED=true
```

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关这些环境变量的更多信息，请参考 [Deployment environment variables](../basic-configuration/use-environment-variables/deployment.md)。

有关设置环境变量的更多信息，请参考 [Configuration](../basic-configuration.md)。

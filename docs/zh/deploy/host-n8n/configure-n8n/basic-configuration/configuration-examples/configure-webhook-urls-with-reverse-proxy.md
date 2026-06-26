---
title: Configure webhook URLs with reverse proxy
description: 自定义 n8n webhook URLs，以兼容 reverse proxy 设置。
contentType: howto
nodeTitle: Configure webhook URLs with reverse proxy
originalFilePath: hosting/configuration/configuration-examples/webhook-url.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/webhook-url'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy
layout:
  description:
    visible: false
---

# 使用 reverse proxy 配置 n8n webhooks <a href="#configure-n8n-webhooks-with-reverse-proxy" id="configure-n8n-webhooks-with-reverse-proxy"></a>

n8n 通过组合 `N8N_PROTOCOL`、`N8N_HOST` 和 `N8N_PORT` 创建 webhook URL。如果 n8n 在 reverse proxy 后运行，这种方式将不可用。原因是 n8n 内部运行在端口 5678，但 reverse proxy 通过端口 443 将其暴露到 web。

在 reverse proxy 后运行 n8n 时，请务必执行以下操作：

* 使用 `WEBHOOK_URL` 环境变量手动设置 webhook URL，让 n8n 可以在 editor UI 中显示它，并向 external services 注册正确的 webhook URLs。
* 将 `N8N_PROXY_HOPS` 环境变量设置为 `1`。
* 在 request path 上的最后一个 proxy 中，设置以下 headers 以传递初始 request 的信息：
    * [`X-Forwarded-For`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-For)
    * [`X-Forwarded-Host`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-Host)
    * [`X-Forwarded-Proto`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Forwarded-Proto)

```bash
export WEBHOOK_URL=https://n8n.example.com/
export N8N_PROXY_HOPS=1
```
有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/endpoints.md)。

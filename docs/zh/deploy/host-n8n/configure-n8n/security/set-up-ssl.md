---
title: 设置 SSL
description: 为你的 self-hosted n8n 实例设置 SSL。
contentType: howto
nodeTitle: Set up SSL
originalFilePath: hosting/securing/set-up-ssl.md
originalUrl: 'https://docs.n8n.io/hosting/securing/set-up-ssl'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/set-up-ssl'
layout:
  description:
    visible: false
---

# 设置 SSL <a href="#set-up-ssl" id="set-up-ssl"></a>

n8n 有两种支持 TLS/SSL 的方法。

## 使用 reverse proxy（推荐） <a href="#use-a-reverse-proxy-recommended" id="use-a-reverse-proxy-recommended"></a>

在 n8n instance 前使用 [Traefik](https://doc.traefik.io/traefik/) 这类 reverse proxy，或 Network Load Balancer (NLB)。它也应负责 certificate renewals。

更多信息请参考 [Security | Data encryption](https://n8n.io/legal/#security)。

## 直接将 certificates 传入 n8n <a href="#pass-certificates-into-n8n-directly" id="pass-certificates-into-n8n-directly"></a>

你也可以选择直接将 certificates 传入 n8n。为此，请将 `N8N_SSL_CERT` 和 `N8N_SSL_KEY` 环境变量设置为指向你生成的 certificate 和 key file。

你需要确保 certificate 保持续订且为最新状态。

有关这些变量的更多信息，请参考 [Deployment environment variables](../basic-configuration/use-environment-variables/deployment.md)；有关设置环境变量的更多信息，请参考 [Configuration](../basic-configuration.md)。

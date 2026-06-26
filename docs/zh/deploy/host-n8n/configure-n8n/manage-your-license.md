---
title: License key
description: 如何激活 license key。
contentType: howto
nodeTitle: Manage your license
originalFilePath: license-key.md
originalUrl: 'https://docs.n8n.io/license-key'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/manage-your-license'
layout:
  description:
    visible: false
---

# License Key <a href="#license-key" id="license-key"></a>

要启用某些 licensed features，你必须先激活 license。你可以通过 UI 完成，也可以设置环境变量。

## 使用 UI 添加 license key <a href="#add-a-license-key-using-the-ui" id="add-a-license-key-using-the-ui"></a>

在你的 n8n 实例中：

1. 以 **Admin** 或 **Owner** 身份登录。
1. 选择 **Settings** > **Usage and plan**。
1. 选择 **Enter activation key**。
1. 粘贴你的 license key。
1. 选择 **Activate**。

## 使用环境变量添加 license key <a href="#add-a-license-key-using-an-environment-variables" id="add-a-license-key-using-an-environment-variables"></a>

在 n8n configuration 中，将 `N8N_LICENSE_ACTIVATION_KEY` 设置为你的 license key。如果实例已经有 activated license，此变量不会生效。

请参阅 [Environment variables](basic-configuration.md)，了解更多 n8n 配置信息。

## Allowlist license server IP addresses <a href="#allowlist-the-license-server-ip-addresses" id="allowlist-the-license-server-ip-addresses"></a>

n8n 使用 Cloudflare 托管 license server。由于具体 IP addresses 可能变化，你需要 allowlist [Cloudflare IP addresses 的完整范围](https://www.cloudflare.com/ips/)，以确保 n8n 始终可以访问 license server。

---
title: License environment variables
contentType: reference
hide:
  - toc
  - tags
nodeTitle: License
originalFilePath: hosting/configuration/environment-variables/licenses.md
originalUrl: https://docs.n8n.io/hosting/configuration/environment-variables/licenses
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/license
description: >-
  用于配置 n8n license 设置的环境变量，包括隐藏 usage 页面、管理 license 激活和自动续订设置，以及指定 license
  获取所用的 server URL。
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
tags:
  - environment variables
---

# License

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

要启用某些 licensed features，你必须先激活 license。你可以通过 UI 执行，也可以设置环境变量。更多信息请参阅 [license key](../../manage-your-license.md)。

| Variable                                  | Type    | Default                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------------------- | ------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `N8N_HIDE_USAGE_PAGE`                     | boolean | `false`                        | 隐藏 app 中的 usage and plans 页面。                                                                                                                                                                                                                                                                                                                                                                                           |
| `N8N_LICENSE_ACTIVATION_KEY`              | String  | `''`                           | 用于初始化 license 的 activation key。如果 n8n 实例已经激活，则不适用。                                                                                                                                                                                                                                                                                                                                     |
| `N8N_LICENSE_AUTO_RENEW_ENABLED`          | Boolean | `true`                         | <p>启用（true）或禁用（false）license 自动续订。<br>如果禁用，你需要每 10 天手动续订 license：进入 <strong>Settings</strong> > <strong>Usage and plan</strong>，然后按 <code>F5</code>。如果未能续订 license，所有 licensed features 都会被禁用。</p>                                                                                                               |
| `N8N_LICENSE_DETACH_FLOATING_ON_SHUTDOWN` | Boolean | `true`                         | <p>控制实例在关闭时是否将 <a href="https://app.gitbook.com/s/CxSeOtVxqqhfxMSac0AV/key-concept-glossary#entitlement-n8n">floating entitlements</a> 释放回池中。设为 <code>true</code> 可允许其他实例复用 entitlements，设为 <code>false</code> 则保留它们。<br>对于必须始终保持 licensed features 的生产实例，请将此项设为 <code>false</code>。</p> |
| `N8N_LICENSE_SERVER_URL`                  | String  | `https://license.n8n.io/v1`    | 用于获取 license 的 server URL。                                                                                                                                                                                                                                                                                                                                                                                                     |
| `N8N_LICENSE_TENANT_ID`                   | Number  | `1`                            | 与 license 关联的 Tenant ID。仅在 n8n 明确指示时设置此变量。                                                                                                                                                                                                                                                                                                                                      |
| `https_proxy_license_server`              | String  | `https://user:pass@proxy:port` | 用于发起 HTTPS 请求获取 license 的 proxy server URL。此变量名需要使用小写。                                                                                                                                                                                                                                                                                                                                  |

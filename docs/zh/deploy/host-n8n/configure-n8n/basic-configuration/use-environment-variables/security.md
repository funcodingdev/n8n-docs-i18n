---
title: Security environment variables
description: >-
  配置 self-hosted n8n 实例中的 authentication 和环境变量访问。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Security
originalFilePath: hosting/configuration/environment-variables/security.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/security'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security
layout:
  description:
    visible: false
---

# Security 环境变量 <a href="#security-environment-variables" id="security-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_BLOCK_ENV_ACCESS_IN_NODE` | Boolean | `false` | 是否允许用户在 expressions 和 Code node 中访问环境变量：`false` 表示允许，`true` 表示不允许。 |
| `N8N_BLOCK_FILE_ACCESS_TO_N8N_FILES` | Boolean | `true` | 设为 `true` 可阻止访问 `.n8n` 目录和用户定义配置文件中的所有文件。 |
| `N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS` | Boolean | `false` | 设为 `true` 时，会尝试为 settings file 设置 0600 权限，仅允许 owner 读写。 |
| `N8N_RESTRICT_FILE_ACCESS_TO` | String |  | 限制对这些目录中文件的访问。提供多个文件时，使用分号分隔列表（"`;`"）。 |
| `N8N_SECURITY_AUDIT_DAYS_ABANDONED_WORKFLOW` | Number | 90 | 如果 workflow 没有执行，多少天后将其视为 abandoned。 |
|`N8N_CONTENT_SECURITY_POLICY`| String | `{}` | 将 [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) headers 设置为 [helmet.js](https://helmetjs.github.io/#content-security-policy) nested directives object。例如 `{ "frame-ancestors": ["http://localhost:3000"] }` |
| `N8N_SECURE_COOKIE` | Boolean | `true` | 确保 cookies 只通过 HTTPS 发送，从而增强安全性。|
| `N8N_SAMESITE_COOKIE` | Enum string: `strict`, `lax`, `none` | `lax` | 控制 cross-site cookie 行为（[了解更多](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)）：<ul><li>`strict`：仅为 first-party requests 发送。</li><li>`lax`（默认）：随 top-level navigation requests 发送。</li><li>`none`：在所有上下文中发送（需要 HTTPS）。</li></ul> |
| `N8N_GIT_NODE_DISABLE_BARE_REPOS` | Boolean | `false` | 设为 `true` 可阻止 [Git node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.git) 使用 bare repositories，从而增强安全性。 |
| `N8N_GIT_NODE_ENABLE_HOOKS` | Boolean | `false` | 设为 `true` 可允许 [Git node](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.git) 执行 Git hooks。 |

## 使用环境变量配置 security policy <a href="#security-policy-using-environment-variables" id="security-policy-using-environment-variables"></a>

将 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 设为 `true`，即可通过环境变量管理 security policy。关于 activation pattern 的工作方式，请参阅 [Manage instance settings using environment variables](../../manage-settings-using-environment-variables.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/xVIddGVtWAPFZlRYTrwL/" %}

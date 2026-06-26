---
title: 'User management SMTP, and two-factor authentication environment variables'
description: 用于设置 user management 和 emails 的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: User management and 2FA
originalFilePath: hosting/configuration/environment-variables/user-management-smtp-2fa.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/environment-variables/user-management-smtp-2fa
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/user-management-and-2fa
layout:
  description:
    visible: false
---

# User management SMTP 和 two-factor authentication 环境变量 <a href="#user-management-smtp-and-two-factor-authentication-environment-variables" id="user-management-smtp-and-two-factor-authentication-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

有关设置 user management 和 emails 的更多信息，请参考 [User management](../../user-management.md)。

| Variable | Type | Default | Description |
| :------- | :--- | :------ | :---------- |
| `N8N_EMAIL_MODE` | String | `smtp` | 启用 emails。 |
| `N8N_SMTP_HOST` | String | - | _your_SMTP_server_name_ |
| `N8N_SMTP_PORT` | Number | - | _your_SMTP_server_port_ |
| `N8N_SMTP_USER` | String | - | _your_SMTP_username_ |
| `N8N_SMTP_PASS` | String | - | _your_SMTP_password_ |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | String | - | 如果将 2LO 与 service account 一起使用，这是你的 client ID。 |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | String | - | 如果将 2LO 与 service account 一起使用，这是你的 private key。 |
| `N8N_SMTP_SENDER` | String | - | 发件人 email address。你可以选择包含 sender name。包含名称的示例：_n8n `<contact@n8n.com>`_ |
| `N8N_SMTP_SSL` | Boolean | `true` | 是否为 SMTP 使用 SSL：`true` 表示使用，`false` 表示不使用。 |
| `N8N_SMTP_STARTTLS` | Boolean | `true` | 是否为 SMTP 使用 STARTTLS：`true` 表示使用，`false` 表示不使用。 |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | String | - | HTML email template 的完整路径。它会覆盖 invite emails 的默认 template。 |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | String | - | HTML email template 的完整路径。它会覆盖 password reset emails 的默认 template。 |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | - | 覆盖用于通知用户 workflow 已共享的默认 HTML template。请提供 template 的完整路径。 |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | - | 覆盖用于通知用户 credential 已共享的默认 HTML template。请提供 template 的完整路径。 |
| `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED` | String | - | 覆盖用于通知用户 project 已共享的默认 HTML template。请提供 template 的完整路径。 |
| `N8N_USER_MANAGEMENT_JWT_SECRET` | String | - | 设置特定 JWT secret。默认情况下，n8n 会在启动时生成一个。 |
| `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` | Number | 168 | 设置 JWTs 的过期时间，单位为小时。 |
| `N8N_USER_MANAGEMENT_JWT_REFRESH_TIMEOUT_HOURS` | Number | 0 | JWT 过期前多少小时自动刷新。0 表示 `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` 的 25%。-1 表示永不刷新，这会强制用户在 `N8N_USER_MANAGEMENT_JWT_DURATION_HOURS` 定义的周期后重新登录。 |
| `N8N_MFA_ENABLED` | Boolean | `true` | 是否启用 two-factor authentication：`true` 表示启用，`false` 表示禁用。如果现有用户已启用 2FA，n8n 会忽略此项。 |
| `N8N_INVITE_LINKS_EMAIL_ONLY` | Boolean | `false` | 设为 true 时，n8n 只会通过 email 发送 invite links，不会通过 API 暴露它们。此选项通过防止 invite URLs 被程序化访问或被高权限用户访问来增强安全性。 |

## 使用环境变量配置 instance owner <a href="#instance-owner-using-environment-variables" id="instance-owner-using-environment-variables"></a>

将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设为 `true`，即可通过环境变量预配置 instance owner。关于 activation pattern 的工作方式，请参阅 [Manage instance settings using environment variables](../../manage-settings-using-environment-variables.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/75cM0VtFejV1gnDTFOSV/" %}

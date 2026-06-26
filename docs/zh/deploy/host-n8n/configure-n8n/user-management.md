---
description: 配置自托管 n8n 的用户管理
contentType: howto
nodeTitle: User management
originalFilePath: hosting/configuration/user-management-self-hosted.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/user-management-self-hosted'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/user-management'
layout:
  description:
    visible: false
---

# 为用户管理配置自托管 n8n <a href="#configure-self-hosted-n8n-for-user-management" id="configure-self-hosted-n8n-for-user-management"></a>

n8n 中的 user management 允许你邀请其他人到你的 n8n instance 中协作。

本文档说明如何配置 n8n instance 以支持 user management，以及开始邀请 users 的步骤。

有关使用方式的更多信息，请参阅主要的 [User management](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access) 指南，包括：

* [管理 users](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/add-and-remove-users)
* [Account types](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/understand-account-types)
* [Best practices](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/follow-best-practices)

有关 LDAP setup 信息，请参阅 [LDAP](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/connect-ldap)。

有关 SAML setup 信息，请参阅 [SAML](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/use-saml)。

{% hint style="info" %}
**不支持的 user management 方法**

在 1.0 版本中，n8n：
- 移除了对 **basic auth** 和 **JWT** 的支持
- 移除了 `N8N_USER_MANAGEMENT_DISABLED` 环境变量。n8n 的近期版本中不存在受支持的禁用登录界面的方式，包括本地或开发用途。如果你需要为本地开发简化登录，请考虑使用 password manager、设置简单的本地 password，或脚本化标准登录流程。
{% endhint %}
## 设置 <a href="#setup" id="setup"></a>

在 n8n 中设置 user management 有三个阶段：

1. 配置 n8n instance 使用你的 SMTP server。
2. 启动 n8n，并按 app 中的 setup 步骤操作。
3. 邀请 users。

### 第一步：SMTP <a href="#step-one-smtp" id="step-one-smtp"></a>

n8n 建议为 user invites 和 password resets 设置 SMTP server。

{% hint style="info" %}
**自 0.210.1 起可选**

从 0.210.1 版本开始，此步骤是可选的。你可以选择手动复制并发送 invite links，而不是设置 SMTP。请注意，如果跳过此步骤，users 无法 reset passwords。
{% endhint %}
从你的 SMTP provider 获取以下信息：

* Server name
* SMTP username
* SMTP password
* SMTP sender name

要在 n8n 中设置 SMTP，请为你的 n8n instance 配置 SMTP 环境变量。有关如何设置环境变量的信息，请参阅[配置](basic-configuration.md)。

| Variable | Type | Description | Required? |
| -------- | ---- | ----------- | --------- |
| `N8N_EMAIL_MODE` | string | `smtp` | Required |
| `N8N_SMTP_HOST` | string | _your_SMTP_server_name_ | Required |
| `N8N_SMTP_PORT` | number | _your_SMTP_server_port_。默认值为 `465`。| Optional |
| `N8N_SMTP_USER` | string | _your_SMTP_username_ | Optional |
| `N8N_SMTP_PASS` | string | _your_SMTP_password_ | Optional |
| `N8N_SMTP_OAUTH_SERVICE_CLIENT` | string | _your_OAuth_service_client_ | Optional |
| `N8N_SMTP_OAUTH_PRIVATE_KEY` | string | _your_OAuth_private_key_ | Optional |
| `N8N_SMTP_SENDER` | string | Sender email address。你也可以包含 sender name。带名称示例：_n8n `<contact@n8n.com>`_ | Required |
| `N8N_SMTP_SSL` | boolean | 是否对 SMTP 使用 SSL（true）或不使用（false）。默认为 `true`。 | Optional |
| `N8N_UM_EMAIL_TEMPLATES_INVITE` | string | HTML email template 的完整路径。此项会覆盖 invite emails 的默认 template。 | Optional |
| `N8N_UM_EMAIL_TEMPLATES_PWRESET` | string | HTML email template 的完整路径。此项会覆盖 password reset emails 的默认 template。 | Optional |
| `N8N_UM_EMAIL_TEMPLATES_WORKFLOW_SHARED` | String | 覆盖用于通知 users 已共享 credential 的默认 HTML template。请提供 template 的完整路径。 | Optional |
| `N8N_UM_EMAIL_TEMPLATES_CREDENTIALS_SHARED` | String | 覆盖用于通知 users 已共享 credential 的默认 HTML template。请提供 template 的完整路径。 | Optional |
| `N8N_UM_EMAIL_TEMPLATES_PROJECT_SHARED` | String | 覆盖用于通知 users 已共享 project 的默认 HTML template。请提供 template 的完整路径。 | Optional |


如果你的 n8n instance 已在运行，需要重启它才能启用新的 SMTP settings。

{% hint style="info" %}
**更多配置选项**

还有更多配置选项可以作为环境变量使用。列表请参阅 [Environment variables](basic-configuration/use-environment-variables/README.md)。其中包括禁用 tags、workflow templates 和 personalization survey 的选项，如果你不希望 users 看到它们，可以使用这些选项。
{% endhint %}

{% hint style="info" %}
**刚接触 SMTP？**

如果你不熟悉 SMTP，这篇 [SendGrid blog post](https://sendgrid.com/blog/what-is-an-smtp-server/) 提供了简短介绍，而 [Wikipedia 的 Simple Mail Transfer Protocol 文章](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol) 提供了更详细的技术背景。
{% endhint %}

### 第二步：应用内 setup <a href="#step-two-in-app-setup" id="step-two-in-app-setup"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/c0111xcskz1G8PKOQogB/" %}

#### 从环境变量预先 provision instance owner <a href="#pre-provision-the-instance-owner-from-environment-variables" id="pre-provision-the-instance-owner-from-environment-variables"></a>

{% hint style="info" %}
**自 n8n v2.17.0 起可用**


{% endhint %}

你可以从环境变量预先 provision instance owner，而不是走应用内 setup。将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设置为 `true`，并提供 owner details。关于 activation pattern 的工作方式，请参阅[使用环境变量管理实例设置](manage-settings-using-environment-variables.md)。

要在 setup 后更改 owner email，请参阅[更改自托管 n8n 的 instance owner email](change-instance-owner-email.md)。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须是 bcrypt hash**

此变量需要预先 hash 的 bcrypt 值。设置 plaintext password 会导致无法登录。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/75cM0VtFejV1gnDTFOSV/" %}

### 第三步：邀请 users <a href="#step-three-invite-users" id="step-three-invite-users"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/8qoOEjsLz4RnydVBogNy/" %}

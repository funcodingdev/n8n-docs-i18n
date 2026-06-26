---
description: >-
  管理 instance-wide security policies，包括 MFA enforcement 和 personal space controls。
contentType: howto
nodeTitle: Manage security policies
originalFilePath: security-settings.md
originalUrl: 'https://docs.n8n.io/security-settings'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/manage-security-policies
layout:
  description:
    visible: false
---

# 安全设置 <a href="#security-settings" id="security-settings"></a>

{% hint style="info" %}
**功能可用性**

安全设置可用于 Business 和 Enterprise plans。某些设置需要特定 license features。你的 plan 中不可用的设置会显示 **Upgrade** badge。
{% endhint %}

安全设置让你管理 instance-wide security policies。你可以为所有用户强制执行 two-factor authentication，并控制用户可以在 personal spaces 中执行什么操作。

要访问 security settings，请前往 **Settings** > **Security**。

## 强制执行 two-factor authentication <a href="#enforce-two-factor-authentication" id="enforce-two-factor-authentication"></a>

你可以要求实例上的所有用户在使用 email 和 password 登录时设置 two-factor authentication (2FA)。

{% hint style="info" %}
**仅适用于 email 和 password 登录**

2FA enforcement 适用于使用 email 和 password 认证的用户。通过 SSO（SAML 或 OIDC）登录的用户不受此设置影响。
{% endhint %}

要强制执行 2FA：

1. 前往 **Settings** > **Security**。
2. 在 **Enforce two-factor authentication** section 中，打开 toggle switch。

启用此设置后：

- 所有用户必须先设置 2FA，才能继续使用实例。
- 尚未配置 2FA 的用户会在下次 sign-in 时被提示设置。

要停止强制执行 2FA，请关闭 toggle switch。已经设置 2FA 的用户会保留启用状态，但新用户不再需要配置它。

有关单个用户如何设置 2FA 的更多信息，请参考 [Two-factor authentication](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/require-two-factor-auth)。

## 个人空间策略 <a href="#personal-space-policies" id="personal-space-policies"></a>

个人空间策略让 instance admins 控制用户是否可以从其 personal spaces 分享和 publish workflows 与 credentials。

### 分享 workflows 和 credentials <a href="#sharing-workflows-and-credentials" id="sharing-workflows-and-credentials"></a>

控制用户是否可以从其 personal space 与其他 users 或 projects 分享 workflows 和 credentials。

要管理 sharing：

1. 前往 **Settings** > **Security**。
2. 在 **Personal Space** section 中，找到 **Sharing workflows and credentials**。
3. 切换开关以启用或禁用 sharing。

禁用 sharing 后：

- 现有 shares 会保留。该设置只影响新的 sharing actions。
- 当前已分享的 workflows 和 credentials 数量会显示在 toggle 下方。

### 发布 workflows <a href="#publishing-workflows" id="publishing-workflows"></a>

控制用户是否可以从其 personal space publish workflows，使其可用于 execution。

要管理 publishing：

1. 前往 **Settings** > **Security**。
2. 在 **Personal Space** section 中，找到 **Publishing workflows**。
3. 切换开关以启用或禁用 publishing。

禁用 publishing 后：

- 当前已发布的 workflows 会保持 published 状态。该设置只影响新的 publish actions。
- 当前已发布的 personal workflows 数量会显示在 toggle 下方。

## 强制执行 execution data redaction <a href="#enforce-execution-data-redaction" id="enforce-execution-data-redaction"></a>

你可以为实例上的所有 workflows 强制执行 [execution data redaction](redact-execution-data.md)。Enforcement 会设置 instance-wide minimum redaction policy，单个 workflow settings 不能削弱它。

{% hint style="info" %}
**功能可用性**

Data redaction enforcement 可用于 Enterprise Self-hosted 和 Enterprise Cloud plans。

**可用版本：** n8n version 2.26.0
{% endhint %}

要强制执行 data redaction：

1. 前往 **Settings** > **Security**。
2. 在 **Data redaction** section 中，打开 **Enforce data redaction**。
3. 在 **Redact executions** 下选择 enforcement scope：
	- **Production executions (Recommended)**：n8n 会对所有 workflows 中的 production executions 进行 data redaction。
	- **Manual and production executions**：n8n 会对所有 workflows 中的 manual 和 production executions 进行 data redaction。
4. 在 dialog 中确认你的选择。

启用 enforcement 后：

- n8n 会对所选 scope 内所有 workflows 的 execution data 进行 redaction，包括未在自身设置中启用 redaction 的 workflows。
- 用户不能将 workflow-level redaction settings 设置得比强制 scope 更弱。Workflows 仍可以选择更严格的 redaction，例如在仅启用 production enforcement 时也 redact manual executions。
- 新 workflows 会以强制 scope 作为其 redaction policy。

Redaction enforcement 需要带有 data redaction feature 的 Enterprise license。关于 redaction 覆盖哪些内容、revealing data 和权限的详情，请参考 [Execution data redaction](redact-execution-data.md)。

## 使用环境变量配置 security policy <a href="#configure-security-policy-with-environment-variables" id="configure-security-policy-with-environment-variables"></a>

你也可以通过环境变量而不是 UI 管理 security policy settings。从 n8n v2.18.0 起可用。将 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 设为 `true`，并提供下面的变量。关于 activation pattern 的工作方式，请参阅 [Manage instance settings using environment variables](../manage-settings-using-environment-variables.md)。

当 `N8N_SECURITY_POLICY_MANAGED_BY_ENV` 为 `true` 时，本页上的 **Enforce two-factor authentication** 和 **Personal Space** toggles 会变为只读。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/xVIddGVtWAPFZlRYTrwL/" %}

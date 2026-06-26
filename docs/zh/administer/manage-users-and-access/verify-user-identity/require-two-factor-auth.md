---
description: 如何为你的 n8n account 启用 2FA
contentType: howto
nodeTitle: Require two-factor auth
originalFilePath: user-management/two-factor-auth.md
originalUrl: 'https://docs.n8n.io/user-management/two-factor-auth'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/require-two-factor-auth
layout:
  description:
    visible: false
---

# Two-factor authentication (2FA) <a href="#two-factor-authentication-2fa" id="two-factor-authentication-2fa"></a>

Two-factor authentication (2FA) 会在 username 和 password 之上添加第二种 authentication method。这会提升 account security。n8n 支持使用 authenticator app 进行 2FA。

## 启用 2FA <a href="#enable-2fa" id="enable-2fa"></a>

你需要在 phone 上安装 authenticator app。

在 n8n 中启用 2FA：

1. 前往你的 **Settings** > **Personal**。
2. 选择 **Enable 2FA**。n8n 会打开一个带 QR code 的 modal。
3. 在 authenticator app 中扫描 QR code。
4. 在 **Code from authenticator app** 中输入 app 生成的 code。
5. 选择 **Continue**。n8n 会显示 recovery codes。
6. 保存 recovery codes。如果丢失 authenticator，你需要使用这些 codes 恢复 account access。

## 为 instance 禁用 2FA <a href="#disable-2fa-for-your-instance" id="disable-2fa-for-your-instance"></a>

Self-hosted users 可以通过将 `N8N_MFA_ENABLED` 设置为 false，配置 n8n instance 为所有 users 禁用 2FA。请注意，如果 existing users 已启用 2FA，n8n 会忽略此设置。有关使用 environment variables 配置 n8n instance 的更多信息，请参考 [Configuration methods](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration)。

---
title: 将账户注册限制为已验证 email 的用户
description: 要求所有新账户都通过 email 验证。
contentType: howto
nodeTitle: Verify user emails
originalFilePath: hosting/securing/restrict-by-email-verification.md
originalUrl: 'https://docs.n8n.io/hosting/securing/restrict-by-email-verification'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/verify-user-emails'
layout:
  description:
    visible: false
---

# 将账户注册限制为已验证 email 的用户 <a href="#restrict-account-registration-to-email-verified-users" id="restrict-account-registration-to-email-verified-users"></a>

你可以要求所有新账户都通过 email 验证。这可以防止恶意 admins 在未进行 email verification 的情况下注册账户。

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

* 必须设置 SMTP，且 n8n 必须能够发送 emails。

## 如何限制账户注册 <a href="#how-to-restrict-account-registration" id="how-to-restrict-account-registration"></a>

将环境变量 `N8N_INVITE_LINKS_EMAIL_ONLY` 设为 `true`。这会锁定你的实例，使只有 email addresses 已验证的用户才能注册。

关于配置 SMTP 的更多详情，请参阅[设置 SMTP](../user-management.md#step-one-smtp)。

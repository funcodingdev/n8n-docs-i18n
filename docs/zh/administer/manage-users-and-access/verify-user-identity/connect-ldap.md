---
description: 在 n8n 中使用 LDAP。
contentType: howto
nodeTitle: Connect LDAP
originalFilePath: user-management/ldap.md
originalUrl: 'https://docs.n8n.io/user-management/ldap'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/verify-user-identity/connect-ldap
layout:
  description:
    visible: false
---

# Lightweight Directory Access Protocol (LDAP) <a href="#lightweight-directory-access-protocol-ldap" id="lightweight-directory-access-protocol-ldap"></a>

{% hint style="info" %}
**功能可用性**

* 可用于 Self-hosted Business 和 Enterprise，以及 Cloud Enterprise plans。
* 你需要 access n8n instance owner account。
{% endhint %}

本页面说明如何在 n8n 中启用 LDAP。它假设你熟悉 LDAP，并且已有 LDAP server 设置。

LDAP 允许 users 使用其 organization credentials sign in 到 n8n，而不是使用 n8n login。

## 启用 LDAP <a href="#enable-ldap" id="enable-ldap"></a>

1. 以 instance owner 身份登录 n8n。
2. 选择 **Settings** <img src="../../.gitbook/assets/settings.png" alt="Settings icon" data-size="line"> > **LDAP**。
3. 打开 **Enable LDAP Login**。
4. 使用 LDAP server 的 details 填写 fields。
5. 选择 **Test connection** 检查 connection setup，或选择 **Save connection** 创建 connection。

启用 LDAP 后，LDAP server 上的任何人都可以 sign in 到 n8n instance，除非你使用 **User Filter** setting 排除他们。

你仍然可以在 **Settings** > **Users** 页面创建 non-LDAP users（email users）。

## 合并 n8n 和 LDAP accounts <a href="#merging-n8n-and-ldap-accounts" id="merging-n8n-and-ldap-accounts"></a>

如果 n8n 找到 email users 和 LDAP users 的 matching accounts（emails 匹配），该 user 必须使用 LDAP account sign in。n8n instance owner accounts 不受此影响：n8n 永远不会将 owner accounts 转换为 LDAP users。

## n8n 中的 LDAP user accounts <a href="#ldap-user-accounts-in-n8n" id="ldap-user-accounts-in-n8n"></a>

首次 sign in 时，n8n 会为 LDAP user 在 n8n 中创建 user account。

你必须在 LDAP server 上管理 user details，而不是在 n8n 中管理。如果你在 LDAP server 上 update 或 delete user，n8n account 会在下一次 scheduled sync，或该 user 下次尝试 log in 时更新，以先发生者为准。

{% hint style="info" %}
**User deletion**

如果你从 LDAP server 中移除 user，他们会在下一次 sync 时失去 n8n access。
{% endhint %}

## 关闭 LDAP <a href="#turn-ldap-off" id="turn-ldap-off"></a>

关闭 LDAP：

1. 以 instance owner 身份登录 n8n。
2. 选择 **Settings** <img src="../../.gitbook/assets/settings.png" alt="Settings icon" data-size="line"> > **LDAP**。
3. 关闭 **Enable LDAP Login**。

如果关闭 LDAP，n8n 会在现有 LDAP users 下次 login 时将他们转换为 email users。这些 users 必须 reset password。

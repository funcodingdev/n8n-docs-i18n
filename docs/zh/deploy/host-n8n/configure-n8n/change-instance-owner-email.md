---
title: Change the instance owner email for self-hosted n8n
description: >-
  使用 UI 或环境变量更改自托管 n8n 实例的 owner email address。
contentType: howto
nodeTitle: Change instance owner email
originalFilePath: hosting/configuration/change-instance-owner-email.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/change-instance-owner-email'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/change-instance-owner-email'
layout:
  description:
    visible: false
---

# 更改自托管 n8n 的实例 owner email <a href="#change-the-instance-owner-email-for-self-hosted-n8n" id="change-the-instance-owner-email-for-self-hosted-n8n"></a>

你可以从 UI 更改 instance owner email；如果你通过环境变量管理 instance owner，也可以从环境变量更改。

{% hint style="info" %}
**Owner email 必须唯一**

Owner email 不得已经属于该实例上的其他用户。如果你想使用的 email 已被其他用户使用，请先更改或删除该用户，让该 email 可用。
{% endhint %}

更改 owner email 会更新现有 instance owner account。它不会将 ownership 转移给另一个现有用户，也不会合并用户账号。

## 在 UI 中更改 owner email <a href="#change-the-owner-email-in-the-ui" id="change-the-owner-email-in-the-ui"></a>

1. 以 instance owner 身份登录。
2. 前往 **Settings** > **Personal**。
3. 更新 **Email** 字段。
4. 选择 **Save**。

## 使用环境变量更改 owner email <a href="#change-the-owner-email-using-environment-variables" id="change-the-owner-email-using-environment-variables"></a>

如果你使用环境变量管理 instance owner：

1. 将 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 设置为 `true`。
2. 将 `N8N_INSTANCE_OWNER_EMAIL` 设置为新的 owner email。
3. 保持 `N8N_INSTANCE_OWNER_FIRST_NAME`、`N8N_INSTANCE_OWNER_LAST_NAME` 和 `N8N_INSTANCE_OWNER_PASSWORD_HASH` 已设置。
4. 重启 n8n。

当 `N8N_INSTANCE_OWNER_MANAGED_BY_ENV` 为 `true` 时，n8n 会在每次启动时重新应用 owner details。匹配的 UI controls 会变为 read-only。

{% hint style="warning" %}
**`N8N_INSTANCE_OWNER_PASSWORD_HASH` 必须是 bcrypt hash**

此变量需要预先 hash 的 bcrypt 值。设置 plaintext password 会导致无法登录。
{% endhint %}

更多信息请参阅[使用环境变量管理实例设置](manage-settings-using-environment-variables.md#instance-owner)。

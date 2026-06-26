---
title: Mautic credentials
description: >-
  Mautic credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Mautic 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Mautic credentials
originalFilePath: integrations/builtin/credentials/mautic.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/mautic'
url: 'https://docs.n8n.io/integrations/builtin/credentials/mautic'
layout:
  description:
    visible: false
---

# Mautic credentials <a href="#mautic-credentials" id="mautic-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Mautic](../app-nodes/n8n-nodes-base.mautic.md)
- [Mautic Trigger](../trigger-nodes/n8n-nodes-base.mautictrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Mautic's API documentation](https://developer.mautic.org/#rest-api)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

{% hint style="info" %}
**API 已启用**

要设置此 credential，你的 Mautic instance 必须已启用 API。说明请参考[启用 API](#enable-the-api)。
{% endhint %}

要配置此 credential，你需要 [Mautic](https://www.mautic.org/) instance 上的账号，并准备：

- 你的 **URL**
- **Username**
- **Password**

设置步骤：

1. 在 Mautic 中，前往 **Configuration > API Settings**。
2. 如果 **Enable HTTP basic auth?** 设置为 **No**，请将其改为 **Yes** 并保存。更多信息请参考 [API Settings documentation](https://docs.mautic.org/en/5.x/configuration/settings.html#api-settings)。
1. 在 n8n 中，输入 Mautic instance 的 Base **URL**。
2. 输入 Mautic **Username**。
3. 输入 Mautic **Password**。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% hint style="info" %}
**API 已启用**

要设置此 credential，你的 Mautic instance 必须已启用 API。说明请参考[启用 API](#enable-the-api)。
{% endhint %}

要配置此 credential，你需要 [Mautic](https://www.mautic.org/) instance 上的账号，并准备：

- **Client ID**：创建新的 API credentials 时生成。
- **Client Secret**：创建新的 API credentials 时生成。
- 你的 **URL**

设置步骤：

1. 在 Mautic 中，前往 **Configuration > Settings**。
2. 选择 **API Credentials**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>没有 API Credentials 菜单</strong></p><p>如果你在 <strong>Configuration &gt; Settings</strong> 下没有看到 <strong>API Credentials</strong> 选项，请确认已<a href="#enable-the-api">启用 API</a>。如果已经启用 API 但仍看不到该选项，请尝试<a href="https://forum.mautic.org/t/cant-find-api-credentials-menu/10689">手动清理 cache</a>。</p></div>

2. 选择 **Create new client** 选项。
3. 选择 **OAuth 2** 作为 **Authorization Protocol**。
4. 输入 credential 的 **Name**，例如 `n8n integration`。
5. 在 n8n 中复制 **OAuth Callback URL**，并在 Mautic 中将其输入为 **Redirect URI**。
6. 选择 **Apply**。
7. 从 Mautic 复制 **Client ID**，并输入到你的 n8n credential。
8. 从 Mautic 复制 **Client Secret**，并输入到你的 n8n credential。
9. 输入 Mautic instance 的 Base **URL**。

更多信息请参考 [What is Mautic's API?](https://kb.mautic.org/article/what-is-mautic-039%3bs-api.html#mcetoc_1g7n1bgoo0)。

## 启用 API <a href="#enable-the-api" id="enable-the-api"></a>

在你的 Mautic instance 中启用 API：

1. 前往 **Settings > Configuration**。
2. 选择 **API Settings**。
3. 将 **API enabled?** 设置为 **Yes**。
4. **Save** 更改。

更多信息请参考 [How to use the Mautic API](https://kb.mautic.org/article/what-is-mautic-039;s-api.html)。

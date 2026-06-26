---
title: Xero credentials
description: >-
  Xero credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Xero 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Xero credentials
originalFilePath: integrations/builtin/credentials/xero.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/xero'
url: 'https://docs.n8n.io/integrations/builtin/credentials/xero'
layout:
  description:
    visible: false
---

# Xero credentials <a href="#xero-credentials" id="xero-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Xero](../app-nodes/n8n-nodes-base.xero.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Xero](https://www.xero.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zero's API documentation](https://developer.xero.com/documentation/api/accounting/overview)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：为 custom connection 创建新 app 时生成。
- 一个 **Client Secret**：为 custom connection 创建新 app 时生成。

要生成你的 Client ID 和 Client Secret，请在 Xero developer portal [**My Apps**](https://developer.xero.com/app/manage) 中[创建 OAuth2 custom connection app](https://developer.xero.com/documentation/guides/oauth2/custom-connections/)。

为你的 app 使用以下设置：

{% hint style="info" %}
**Xero App Name**

Xero 不支持在 Xero Developer Centre 中创建名称包含 `n8n` 的 app instances。
{% endhint %}

- 选择 **Web app** 作为 **Integration Type**。
- 对于 **Company or Application URL**，输入你的 n8n server 或 reverse proxy address 的 URL。例如对于 cloud users，这是：`https://your-username.app.n8n.cloud/`。
- 从 n8n 复制 **OAuth Redirect URL**，并将其作为 **OAuth 2.0 redirect URI** 添加到你的 app。
- 为你的 app 选择适当的 **scopes**。更多信息请参考 [OAuth2 Scopes](https://developer.xero.com/documentation/guides/oauth2/scopes/)。
    - 要使用 [Xero](../app-nodes/n8n-nodes-base.xero.md) node 的全部功能，请添加 `accounting.contacts` 和 `accounting.transactions` scopes。

更多信息请参考 Xero 的 [OAuth Custom Connections](https://developer.xero.com/documentation/guides/oauth2/custom-connections) 文档。

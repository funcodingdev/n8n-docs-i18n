---
title: Zoho credentials
description: >-
  Zoho credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Zoho 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Zoho credentials
originalFilePath: integrations/builtin/credentials/zoho.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/zoho'
url: 'https://docs.n8n.io/integrations/builtin/credentials/zoho'
layout:
  description:
    visible: false
---

# Zoho credentials <a href="#zoho-credentials" id="zoho-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Zoho CRM](../app-nodes/n8n-nodes-base.zohocrm.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Zoho](https://www.zoho.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Zoho's CRM API documentation](https://www.zoho.com/crm/developer/docs/api/v3/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Access Token URL**：Zoho 提供 region-specific access token URLs。选择最匹配你的 Zoho data center 的 region：
    - **AU**：为 Australia data center 选择此选项。
    - **CN**：为 Canada data center 选择此选项。
    - **EU**：为 European Union data center 选择此选项。
    - **IN**：为 India data center 选择此选项。
    - **US**：为 United States data center 选择此选项。

有关选择 data center 的更多信息，请参考 [Multi DC](https://www.zoho.com/crm/developer/docs/api/v3/multi-dc.html)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从零开始配置 OAuth2，请在 Zoho [注册 application](https://www.zoho.com/accounts/protocol/oauth-setup.html)。

为你的 application 使用以下设置：

- 选择 **Server-based Applications** 作为 **Client Type**。
- 从 n8n 复制 **OAuth Callback URL**，并将其输入到 Zoho **Authorized Redirect URIs** 字段。
- 从 application 复制 **Client ID** 和 **Client Secret**，并将它们输入到你的 n8n credential。

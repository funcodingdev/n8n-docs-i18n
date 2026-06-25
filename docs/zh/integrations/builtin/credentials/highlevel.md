---
title: HighLevel credentials
description: >-
  HighLevel credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  HighLevel 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: HighLevel credentials
originalFilePath: integrations/builtin/credentials/highlevel.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/highlevel'
url: 'https://docs.n8n.io/integrations/builtin/credentials/highlevel'
layout:
  description:
    visible: false
---

# HighLevel credentials <a href="#highlevel-credentials" id="highlevel-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [HighLevel node](../app-nodes/n8n-nodes-base.highlevel.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [HighLevel developer](https://marketplace.gohighlevel.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key：用于 API v1
- OAuth2：用于 API v2

{% hint style="info" %}
**API 1.0 弃用**

HighLevel 已弃用 API v1.0，并且不再维护它。请使用 OAuth2 设置新的 credentials。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [HighLevel's API 2.0 documentation](https://highlevel.stoplight.io/docs/integrations/0443d7d1a4bd0-overview)。

对于使用 API v1.0 的现有 integrations，请参考 [HighLevel's API 1.0 documentation](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **API Key**：获取 API key 的说明请参考 [HighLevel API 1.0 Welcome documentation](https://help.gohighlevel.com/support/solutions/articles/48001060529-highlevel-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- **Client ID**
- **Client Secret**

要生成二者，请在 **My Apps > Create App** 中创建 app。使用以下设置：

1. 将 **Distribution Type** 设置为 **Sub-Account**。
2. 添加这些 **Scopes**：
    - `locations.readonly`
    - `contacts.readonly`
    - `contacts.write`
    - `opportunities.readonly`
    - `opportunities.write`
    - `users.readonly`
3. 从 n8n 复制 **OAuth Redirect URL**，并将它作为 **Redirect URL** 添加到你的 HighLevel app。
4. 从 HighLevel 复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential。
5. 将上方添加的相同 scopes 添加到 n8n credential 中，使用空格分隔。例如：

    ```locations.readonly contacts.readonly contacts.write opportunities.readonly opportunities.write users.readonly```

更多详细信息请参考 HighLevel 的 [API Authorization documentation](https://highlevel.stoplight.io/docs/integrations/a04191c0fabf9-authorization)。有关可用 scopes 的更多信息，请参考 HighLevel 的 [API Scopes documentation](https://highlevel.stoplight.io/docs/integrations/vcctp9t1w8hja-scopes)。

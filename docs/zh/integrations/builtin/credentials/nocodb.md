---
title: NocoDB credentials
description: >-
  NocoDB credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  NocoDB 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: NocoDB credentials
originalFilePath: integrations/builtin/credentials/nocodb.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/nocodb'
url: 'https://docs.n8n.io/integrations/builtin/credentials/nocodb'
layout:
  description:
    visible: false
---

# NocoDB credentials <a href="#nocodb-credentials" id="nocodb-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [NocoDB](../app-nodes/n8n-nodes-base.nocodb.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token（推荐）
- User auth token<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>User auth token 弃用</strong></p><p>NocoDB 已在 v0.205.1 中弃用 user auth tokens。请改用 <a href="#using-api-token">API tokens</a>。</p></div>

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [NocoDB's API documentation](https://data-apis-v2.nocodb.com/)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要一个 [NocoDB](https://www.nocodb.com/) instance，以及：

- 一个 **API Token**
- 你的 database **Host**

生成 API token：

1. 登录 NocoDB，并在左下角 sidebar 中选择 **User menu**。
2. 选择 **Account Settings**。
3. 打开 **Tokens** tab。
4. 选择 **Add new API token**。
5. 为你的 token 输入一个 **Name**，例如 `n8n integration`。
6. 选择 **Save**。
7. 复制 **API Token**，并将其输入到你的 n8n credential 中。
8. 在你的 n8n credential 中输入 NocoDB instance 的 **Host**，例如 `http://localhost:8080`。

更详细的说明请参考 NocoDB [API Tokens documentation](https://docs.nocodb.com/account-settings/api-tokens/)。

## 使用 user auth token <a href="#using-user-auth-token" id="using-user-auth-token"></a>

在 NocoDB 弃用它之前，user auth token 是一种临时 token，用于快速试验 API，有效期为一个 session，直到 user 登出，或最多 10 小时。

{% hint style="info" %}
**User auth token 弃用**

NocoDB 已在 v0.205.1 中弃用 user auth tokens。请改用 [API tokens](#using-api-token)。
{% endhint %}

要配置此 credential，你需要一个 [NocoDB](https://www.nocodb.com/) instance，以及：

- 一个 **User Token**
- 你的 database **Host**

生成 user auth token：

1. 登录 NocoDB，并在左下角 sidebar 中选择 **User menu**。
2. 选择 **Copy Auth token**。
3. 在 n8n 中将该 auth token 输入为 **User Token**。
4. 输入 NocoDB instance 的 **Host**，例如 `http://localhost:8080`。

更多信息请参考 NocoDB [Auth Tokens documentation](https://docs.nocodb.com/account-settings/api-tokens/#auth-tokens)。

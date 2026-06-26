---
title: Strapi credentials
description: >-
  Strapi credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Strapi 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Strapi credentials
originalFilePath: integrations/builtin/credentials/strapi.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/strapi'
url: 'https://docs.n8n.io/integrations/builtin/credentials/strapi'
layout:
  description:
    visible: false
---

# Strapi credentials <a href="#strapi-credentials" id="strapi-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Strapi](../app-nodes/n8n-nodes-base.strapi.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Strapi](https://strapi.io/) admin account，并具备：

- 对现有 Strapi project 的访问权限。
- 该 project 中至少有一个 collection type。
- 该 collection type 中有已发布数据。

更多信息请参考 Strapi developer [Quick Start Guide](https://docs.strapi.io/dev-docs/quick-start)。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API user account：需要拥有适当 content permissions 的 user account。
- API token：需要 admin account。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Strapi's documentation](https://docs.strapi.io/dev-docs/api/rest)。

## 使用 API user account <a href="#using-api-user-account" id="using-api-user-account"></a>

要配置此 credential，你需要：

- user **Email**：必须是 user account，而不是 admin account。请参考下方更详细的说明。
- user **Password**：必须是 user account，而不是 admin account。请参考下方更详细的说明。
- **URL**：使用你的 Strapi server 的 public URL，该 URL 在 `./config/server.js` 中定义为 `url` 参数。Strapi 建议使用 absolute URL。
    - 对于 Strapi Cloud projects，请使用 Cloud project 的 URL，例如：`https://my-strapi-project-name.strapiapp.com`
- **API Version**：选择你希望 calls 使用的 API version。选项包括：
    - **Version 3**
    - **Version 4**

在 Strapi 中，配置包含两个步骤：

1. [配置 role](#configure-a-role)。
2. [创建 user account](#create-a-user-account)。

请参考下方每个步骤的更详细说明。

### 配置 role <a href="#configure-a-role" id="configure-a-role"></a>

要进行 API access，请使用 **Settings > Users & Permissions Plugin** 中的 Users & Permissions Plugin。

有关 plugin 的更多信息，请参考 [Configuring Users & Permissions Plugin](https://docs.strapi.io/user-docs/settings/configuring-users-permissions-plugin-settings)。有关 roles 的更多信息，请参考 [Configuring end-user roles](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles)。

对于 n8n credential，user 必须拥有一个 role，该 role 授予他们对 collection type 的 API permissions。对于 role，你可以：

* 更新默认 **Authenticated** role 以包含所需 permissions，并将 user 分配给该 role。更多信息请参考 [Configuring role's permissions](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#configuring-roles-permissions)。
* 创建一个新 role 以包含所需 permissions，并将 user 分配给该 role。更多信息请参考 [Creating a new role](https://docs.strapi.io/user-docs/users-roles-permissions/configuring-end-users-roles#creating-a-new-role)。

无论选择哪种方式，打开 role 后：

1. 前往 **Permissions** 部分。
2. 打开相关 collection type 的部分。
3. 选择该 role 应拥有的 collection type permissions。选项包括：
    - `create` (POST)
    - `find` 和 `findone` (GET)
    - `update` (PUT)
    - `delete` (DELETE)
4. 对所有相关 collection types 重复以上操作。
5. 保存 role。

有关 permission 选项的更多信息，请参考 [Endpoints](https://docs.strapi.io/dev-docs/api/rest#endpoints)。

### 创建 user account <a href="#create-a-user-account" id="create-a-user-account"></a>

现在你已有适当的 role，请创建一个 end-user account 并将该 role 分配给它：

1. 前往 **Content Manager > Collection Types > User**。
2. 选择 **Add new entry**。
3. 填写 user details。n8n credential 需要这些字段，不过你的 Strapi project 可能有更多自定义必填字段：
    - **Username**：所有 Strapi users 都必填。
    - **Email**：在 Strapi 中输入，并在 n8n credential 中作为 **Email** 使用。
    - **Password**：在 Strapi 中输入，并在 n8n credential 中作为 **Password** 使用。
    - **Role**：选择你在上一步中设置的 role。

更多信息请参考 [Managing end-user accounts](https://docs.strapi.io/user-docs/users-roles-permissions/managing-end-users)。


## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 **API Token**：从 **Settings > Global Settings > API Tokens** 创建 API token。有关更多细节以及重新生成 API tokens 的信息，请参考 Strapi 的 [Creating a new API token documentation](https://docs.strapi.io/user-docs/settings/API-tokens#creating-a-new-api-token)。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>API tokens permission</strong></p><p>如果你在 <strong>Global settings</strong> 中看不到 <strong>API tokens</strong> 选项，说明你的账号没有 <strong>API tokens &gt; Read</strong> permission。</p></div>

- **URL**：使用你的 Strapi server 的 public URL，该 URL 在 `./config/server.js` 中定义为 `url` 参数。Strapi 建议使用 absolute URL。
    - 对于 Strapi Cloud projects，请使用 Cloud project 的 URL，例如：`https://my-strapi-project-name.strapiapp.com`
- **API Version**：选择你希望 calls 使用的 API version。选项包括：
    - **Version 3**
    - **Version 4**

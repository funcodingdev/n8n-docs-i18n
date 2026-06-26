---
title: Pipedrive credentials
description: >-
  Pipedrive credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Pipedrive 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Pipedrive credentials
originalFilePath: integrations/builtin/credentials/pipedrive.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/pipedrive'
url: 'https://docs.n8n.io/integrations/builtin/credentials/pipedrive'
layout:
  description:
    visible: false
---

# Pipedrive credentials <a href="#pipedrive-credentials" id="pipedrive-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Pipedrive](../app-nodes/n8n-nodes-base.pipedrive.md)
- [Pipedrive Trigger](../trigger-nodes/n8n-nodes-base.pipedrivetrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Pipedrive's developer documentation](https://pipedrive.readme.io/docs/getting-started)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要一个 [Pipedrive](https://pipedrive.com/) 账号，以及：

- 一个 **API Token**

获取 API token：

1. 打开你的 [**API Personal Preferences**](https://app.pipedrive.com/settings/api)。
2. 复制 **Your personal API token**，并将其输入到你的 n8n credential 中。

如果你有多个 companies，需要先选择正确的 company：

1. 选择你的 account name，并确保你正在查看正确的 company。
2. 然后选择 **Company Settings**。
2. 选择 **Personal Preferences**。
3. 选择 **API** tab。
4. 复制 **Your personal API token**，并将其输入到你的 n8n credential 中。

更多信息请参考 [How to find the API token](https://pipedrive.readme.io/docs/how-to-find-the-api-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Pipedrive developer sandbox account](https://developers.pipedrive.com/)，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

要获取二者，你需要注册一个新 app：

1. 在右上角选择你的 profile name。
2. 找到 sandbox account 的 company name，并选择 **Developer Hub**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>没有 Developer Hub</strong></p><p>如果你在 account dropdown 中看不到 <strong>Developer Hub</strong>，请注册一个 <a href="https://developers.pipedrive.com/">developer sandbox account</a>。</p></div>

3. 选择 **Create an app**。
4. 选择 **Create public app**。app 的 **Basic info** tab 会打开。
5. 为你的 app 输入 **App name**，例如 `n8n integration`。
6. 从 n8n 复制 **OAuth Redirect URL**，并将其添加为 app 的 **Callback URL**。
7. 选择 **Save**。app 的 **OAuth & access scopes** tab 会打开。
8. 为你的 app 启用合适的 **Scopes**。更多指导请参考下面的 [Pipedrive node scopes](#pipedrive-node-scopes) 和 [Pipedrive Trigger node scopes](#pipedrive-trigger-node-scopes)。
8. 复制 **Client ID**，并将其输入到你的 n8n credential 中。
9. 复制 **Client Secret**，并将其输入到你的 n8n credential 中。

更多信息请参考 [Registering a public app](https://pipedrive.readme.io/docs/marketplace-registering-the-app)。

### Pipedrive node scopes <a href="#pipedrive-node-scopes" id="pipedrive-node-scopes"></a>

你添加到 app 的 scopes 取决于你想在 n8n 中为哪些 node(s) 使用它，以及你想完成哪些 actions。

[Pipedrive](../app-nodes/n8n-nodes-base.pipedrive.md) node 可能需要的 scopes：

| **Object** | **Node action** | **UI scope** | **Actual scope** |
| --- | --- | --- | --- |
| Activity | 获取一个 activity 的数据 <br> 获取所有 activities 的数据 | **Activities: Read only** 或 <br> **Activities: Full Access** | `activities:read` 或 <br> `activities:full` |
| Activity | Create <br> Delete <br> Update | **Activities: Full Access** | `activities:full` |
| Deal | 获取一个 deal 的数据 <br> 获取所有 deals 的数据 <br> Search a deal | **Deals: Read only** 或 <br> **Deals: Full Access** | `deals:read` 或 <br> `deals:full` |
| Deal | Create <br> Delete <br> Duplicate <br> Update | **Deals: Full Access** | `deals:full` |
| Deal Activity | 获取一个 deal 的所有 activities | **Activities: Read only** 或 <br> **Activities: Full Access** | `activities:read` 或 <br> `activities:full` |
| Deal Product | 获取一个 deal 中的所有 products |  **Products: Read Only** 或 <br> **Products: Full Access** | `products:read` 或 <br> `products:full` |
| File | Download <br> 获取一个 file 的数据 | 参考下面的说明 | 参考下面的说明 |
| File | Create <br> Delete | 参考下面的说明 | 参考下面的说明 |
| Lead | 获取一个 lead 的数据 <br> 获取所有 leads 的数据 | **Leads: Read only** 或 <br> **Leads: Full access** | `leads:read` 或 <br> `leads:full` |
| Lead | Create <br> Delete <br> Update | **Leads: Full access** | `leads:full` |
| Note | 获取一个 note 的数据 <br> 获取所有 notes 的数据 | 参考下面的说明 | 参考下面的说明 |
| Note | Create <br> Delete <br> Update | 参考下面的说明 | 参考下面的说明 |
| Organization | 获取一个 organization 的数据 <br> 获取所有 organizations 的数据 <br> Search | **Contacts: Read Only** 或 <br> **Contacts: Full Access** | `contacts:read` 或 <br> `contacts:full` |
| Organization | Create <br> Delete <br> Update | **Contacts: Full Access** | `contacts:full` |
| Person | 获取一个 person 的数据 <br> 获取所有 persons 的数据 <br> Search | **Contacts: Read Only** 或 <br> **Contacts: Full Access** | `contacts:read` 或 <br> `contacts:full` |
| Person | Create <br> Delete <br> Update | **Contacts: Full Access** | `contacts:full` |
| Product | 获取所有 products 的数据 | **Products: Read Only** | `products:read` |

{% hint style="info" %}
**Files 和 Notes**

Files 和 Notes 的 scopes 取决于它们关联的 object：

- Files 与 Deals、Activities 或 Contacts 相关。
- Notes 与 Deals 或 Contacts 相关。

请参考这些 objects 的 scopes。
{% endhint %}

Pipedrive node 还支持 Custom API calls。请为你打算发起的 custom API calls 添加相关 scopes。

更多信息请参考 [Scopes and permissions explanations](https://pipedrive.readme.io/docs/marketplace-scopes-and-permissions-explanations)。

### Pipedrive Trigger node scopes <a href="#pipedrive-trigger-node-scopes" id="pipedrive-trigger-node-scopes"></a>

[Pipedrive Trigger](../trigger-nodes/n8n-nodes-base.pipedrivetrigger.md) node 需要 **Webhooks: Full access** (`webhooks:full`) scope。

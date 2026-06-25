---
title: HubSpot credentials
description: >-
  HubSpot credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  HubSpot 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: HubSpot credentials
originalFilePath: integrations/builtin/credentials/hubspot.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/hubspot'
url: 'https://docs.n8n.io/integrations/builtin/credentials/hubspot'
layout:
  description:
    visible: false
---

# HubSpot credentials <a href="#hubspot-credentials" id="hubspot-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [HubSpot](../app-nodes/n8n-nodes-base.hubspot.md)
- [HubSpot Trigger](../trigger-nodes/n8n-nodes-base.hubspottrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Service key（推荐）：与 [HubSpot](../app-nodes/n8n-nodes-base.hubspot.md) node 一起使用。
- Developer API key：与 [HubSpot Trigger](../trigger-nodes/n8n-nodes-base.hubspottrigger.md) node 一起使用。
- OAuth2：与 [HubSpot](../app-nodes/n8n-nodes-base.hubspot.md) node 一起使用。

{% hint style="warning" %}
**API key 已弃用**

HubSpot 已弃用常规 **API Key** 身份验证方式。该选项仍会出现在 n8n 中，但你应改用上面列出的身份验证方式。如果你已有使用此 API key 方式的 integrations，请参考 HubSpot 的 [Migrate an API key integration to a private app](https://web.archive.org/web/20240106022147/https://developers.hubspot.com/docs/api/migrate-an-api-key-integration-to-a-private-app) 指南并设置 service key。
{% endhint %}

{% hint style="warning" %}
**基于 UI 的 private apps 现在是 legacy**

HubSpot 已将 UI 中创建的 private apps 移入 legacy 状态。如果你正在使用这类 app 的 private app access token，HubSpot 建议改用 service key。更多信息请参考 [HubSpot's Private Apps documentation](https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview)。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [HubSpot's API documentation](https://developers.hubspot.com/docs/api/overview)。[HubSpot Trigger](../trigger-nodes/n8n-nodes-base.hubspottrigger.md) node 使用 Webhooks API；有关该服务的更多信息，请参考 [HubSpot's Webhooks API documentation](https://developers.hubspot.com/docs/api-reference/webhooks-webhooks-v3/guide)。

## 使用 Service Key <a href="#using-service-key" id="using-service-key"></a>

要配置此 credential，你需要一个拥有 super admin access 或 Developer tools access permission 的 [HubSpot](https://www.hubspot.com/) 账号，并准备：

- **Service Key**

生成 service key：

1. 在你的 HubSpot 账号中，进入 **Development** > **Keys** > **Service Keys**。（你也可以在 **Settings** > **Account Management** > **Integrations** > **Service Keys** 下找到 **Service Keys**。）

	![HubSpot Development 菜单中的 Service Keys 页面](../../.gitbook/assets/service_keys_main.png)

2. 选择 **Create service key**。

	![包含 name 和 scopes 字段的 Create Service Key 表单](../../.gitbook/assets/service_keys_create.png)

3. 为你的 key 输入描述性的 **Name**。
4. 选择 **Add new scope**，并选择 integration 需要的 permissions。推荐 scopes 列表请参考 [HubSpot node 所需 scopes](#required-scopes-for-hubspot-node)。
5. 选择 **Update** 确认 scope 选择。
6. 选择 **Create**，然后在对话框中确认。
7. 点击新的 service key 名称进入其详情页，并选择 **Show** 显示你的 key。
8. 使用复制按钮复制 key 值，并将其作为 **App Token** 粘贴到你的 n8n credential。

{% hint style="info" %}
**Service keys 处于 public beta**

Service keys 当前处于 public beta，可能会发生变化。最新信息请参考 [HubSpot's Service Keys documentation](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/account-service-keys)。
{% endhint %}

## 使用 Developer API key <a href="#using-developer-api-key" id="using-developer-api-key"></a>

要配置此 credential，你需要一个 [HubSpot developer](https://developers.hubspot.com/) 账号，并准备：

- **Client ID**：创建 public app 后生成。
- **Client Secret**：创建 public app 后生成。
- **Developer API Key**：从你的 Developer Apps dashboard 生成。
- **App ID**：创建 public app 后生成。

创建 public app 并设置 credential：

1. 登录你的 [HubSpot app developer account](https://developers.hubspot.com/)。
2. 从主导航栏选择 **Apps**。
3. 选择 **Get HubSpot API key**。你可能需要选择 **Show key** 选项。
4. 复制该 key，并在 n8n 中将其填为 **Developer API Key**。
3. 仍在 HubSpot **Apps** 页面，选择 **Create app**。
4. 在 **App Info** 标签页，添加 **App name**、**Description**、**Logo**，以及你想提供的任何 support contact info。遇到此 app 的所有人都会看到这些信息。
5. 打开 **Auth** 标签页。
6. 复制 **App ID** 并输入到 n8n。
6. 复制 **Client ID** 并输入到 n8n。
7. 复制 **Client Secret** 并输入到 n8n。
8. 在 **Scopes** 区域，选择 **Add new scope**。
9. 将 [HubSpot Trigger node 所需 scopes](#required-scopes-for-hubspot-trigger-node) 中列出的所有 scopes 添加到你的 app。
10. 选择 **Update**。
11. 复制 n8n **OAuth Redirect URL**，并将其作为 **Redirect URL** 输入到你的 HubSpot app。
12. 选择 **Create app** 完成 HubSpot app 创建。

 更详细说明请参考 [HubSpot Public Apps documentation](https://developers.hubspot.com/docs/apps/legacy-apps/public-apps/overview)。

### HubSpot Trigger node 所需 scopes <a href="#required-scopes-for-hubspot-trigger-node" id="required-scopes-for-hubspot-trigger-node"></a>

如果你要创建用于 [HubSpot Trigger](../trigger-nodes/n8n-nodes-base.hubspottrigger.md) node 的 app，n8n 建议从这些 scopes 开始：

| **Element** | **Object** | **Permission** | **Scope name** |
| --- | --- | --- | --- |
| n/a | n/a | n/a | `oauth` |
| CRM | Companies | Read | `crm.objects.companies.read` |
| CRM | Companies schemas | Read | `crm.schemas.companies.read` |
| CRM | Contacts | Read | `crm.objects.contacts.read` |
| CRM | Contacts schemas | Read | `crm.schemas.contacts.read` |
| CRM | Deals | Read | `crm.objects.deals.read` |
| CRM | Deals schemas| Read | `crm.schemas.deals.read` |


## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你是[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要通过创建新的 public app 从头配置 OAuth2：

1. 登录你的 [HubSpot app developer account](https://developers.hubspot.com/)。
2. 从主导航栏选择 **Apps**。
3. 选择 **Create app**。
4. 在 **App Info** 标签页，添加 **App name**、**Description**、**Logo**，以及你想提供的任何 support contact info。遇到此 app 的所有人都会看到这些信息。
5. 打开 **Auth** 标签页。
6. 复制 **App ID** 并输入到 n8n。
6. 复制 **Client ID** 并输入到 n8n。
7. 复制 **Client Secret** 并输入到 n8n。
8. 在 **Scopes** 区域，选择 **Add new scope**。
9. 将 [HubSpot node 所需 scopes](#required-scopes-for-hubspot-node) 中列出的所有 scopes 添加到你的 app。
10. 选择 **Update**。
11. 复制 n8n **OAuth Redirect URL**，并将其作为 **Redirect URL** 输入到你的 HubSpot app。
12. 选择 **Create app** 完成 HubSpot app 创建。

更详细说明请参考 [HubSpot Public Apps documentation](https://developers.hubspot.com/docs/apps/legacy-apps/public-apps/overview)。如果你需要了解 OAuth web flow 中发生的更多细节，请参考 [HubSpot Working with OAuth documentation](https://developers.hubspot.com/docs/apps/legacy-apps/authentication/working-with-oauth)。

## HubSpot node 所需 scopes <a href="#required-scopes-for-hubspot-node" id="required-scopes-for-hubspot-node"></a>

如果你要创建用于 [HubSpot](../app-nodes/n8n-nodes-base.hubspot.md) node 的 app，n8n 建议从这些 scopes 开始：

| **Element** | **Object** | **Permission** | **Scope name(s)** |
| --- | --- | --- | --- |
| n/a | n/a | n/a |  `oauth` |
| n/a | n/a | n/a |  `forms` |
| n/a | n/a | n/a |  `tickets` |
| CRM | Companies | Read <br> Write | `crm.objects.companies.read` <br> `crm.objects.companies.write`|
| CRM | Companies schemas | Read | `crm.schemas.companies.read` |
| CRM | Contacts schemas | Read | `crm.schemas.contacts.read` |
| CRM | Contacts | Read <br> Write | `crm.objects.contacts.read` <br> `crm.objects.contacts.write`|
| CRM | Deals | Read <br> Write | `crm.objects.deals.read` <br> `crm.objects.deals.write`|
| CRM | Deals schemas | Read | `crm.schemas.deals.read` |
| CRM | Owners | Read | `crm.objects.owners.read` |
| CRM | Lists | Write | `crm.lists.write` |

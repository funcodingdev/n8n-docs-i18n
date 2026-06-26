---
title: Microsoft Entra ID credentials
description: >-
  Microsoft Entra ID credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Microsoft Entra ID 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft Entra ID credentials
originalFilePath: integrations/builtin/credentials/microsoftentra.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftentra'
url: 'https://docs.n8n.io/integrations/builtin/credentials/microsoftentra'
layout:
  description:
    visible: false
---

# Microsoft Entra ID credentials <a href="#microsoft-entra-id-credentials" id="microsoft-entra-id-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Microsoft Entra ID](../app-nodes/n8n-nodes-base.microsoftentra.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建 Microsoft Entra ID account 或 subscription。
- 如果 user account 由 corporate Microsoft Entra account 管理，administrator account 已为此用户启用 “User can consent to apps accessing company data on their behalf” 选项（请参阅 [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)）。

创建 [Microsoft Azure](https://azure.microsoft.com/) 账号时，Microsoft 会包含 Entra ID free plan。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Microsoft Entra ID's documentation](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

对于自托管用户，从头配置 OAuth2 有两个主要步骤：

1. 在 Microsoft Identity Platform 中[注册 application](#register-an-application)。
2. 为该 application [生成 client secret](#generate-a-client-secret)。

按照下面每一步的详细说明操作。有关 Microsoft OAuth2 web flow 的更多细节，请参考 [Microsoft authentication and authorization basics](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)。

### 注册 application <a href="#register-an-application" id="register-an-application"></a>

在 Microsoft Identity Platform 中注册 application：

1. 打开 [Microsoft Application Registration Portal](https://aka.ms/appregistrations)。
2. 选择 **Register an application**。
3. 输入 app 的 **Name**。
4. 在 **Supported account types** 中，选择 **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**。
5. 在 **Register an application** 中：
    1. 从你的 n8n credential 复制 **OAuth Callback URL**。
    2. 将它粘贴到 **Redirect URI (optional)** 字段。
    3. 选择 **Select a platform** > **Web**。
6. 选择 **Register** 完成 application 创建。
7. 复制 **Application (client) ID**，并在 n8n 中将其粘贴为 **Client ID**。

更多信息请参考[使用 Microsoft Identity Platform 注册 application](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成 client secret <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

创建 application 后，为它生成 client secret：

1. 在 Microsoft application 页面，选择左侧导航中的 **Certificates & secrets**。
1. 在 **Client secrets** 中，选择 **+ New client secret**。
1. 输入 client secret 的 **Description**，例如 `n8n credential`。
1. 选择 **Add**。
1. 复制 **Value** 列中的 **Secret**。
1. 在 n8n 中将其粘贴为 **Client Secret**。
1. 在 n8n 中选择 **Connect my account** 完成连接设置。
1. 登录 Microsoft account，并允许 app 访问你的信息。

有关添加 client secret 的更多信息，请参考 Microsoft 的 [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

### Microsoft Graph API Base URL <a href="#microsoft-graph-api-base-url" id="microsoft-graph-api-base-url"></a>

Microsoft Entra ID credentials 扩展了 Microsoft OAuth2 API credentials，并支持不同的 Microsoft cloud environments。请根据 tenant 的 cloud environment 选择合适的 endpoint：

- **Global**：用于标准 Microsoft 365 tenants（默认）
- **US Government**：用于 Azure US Government (GCC) tenants
- **US Government DOD**：用于 Azure US Government Department of Defense tenants
- **China**：用于由世纪互联运营的 Microsoft 365

{% hint style="warning" %}
**政府云 Authorization URLs**

如果你使用 government cloud tenant，可能还需要更新 credential 中的 **Authorization URL** 和 **Access Token URL** 字段，以使用 government cloud endpoints。例如：
- US Government：使用 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/authorize` 和 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/token`
- 将 `{tenant}` 替换为你的 tenant ID，或对 multi-tenant apps 使用 `common`
{% endhint %}

## 设置自定义 scopes <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Microsoft Entra ID credentials 默认使用以下 scopes：

* [`openid`](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc#the-openid-scope)
* [`offline_access`](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc#the-offline_access-scope)
* [`AccessReview.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#accessreviewreadwriteall)
* [`Directory.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#directoryreadwriteall)
* [`NetworkAccessPolicy.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#networkaccesspolicyreadwriteall)
* [`DelegatedAdminRelationship.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#delegatedadminrelationshipreadwriteall)
* [`EntitlementManagement.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#entitlementmanagementreadwriteall)
* [`User.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#userreadwriteall)
* [`Directory.AccessAsUser.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#directoryaccessasuserall)
* [`Sites.FullControl.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesfullcontrolall)
* [`GroupMember.ReadWrite.All`](https://learn.microsoft.com/en-us/graph/permissions-reference#groupmemberreadwriteall)

要为 credentials 选择不同 scopes，请启用 **Custom Scopes** slider，并编辑 **Enabled Scopes** 列表。请注意，使用更严格的 scopes 时，某些功能可能无法按预期工作。


## 面向组织级 Microsoft integrations 的 delegated access <a href="#delegated-access-for-organisation-wide-microsoft-integrations" id="delegated-access-for-organisation-wide-microsoft-integrations"></a>

本节说明 n8n administrator 如何注册一个带 delegated permissions 的 Entra ID app，一次性授予 admin consent，然后预配置 n8n，让 organisation 中的其他用户无需完成自己的 OAuth app registration，就可以连接 Microsoft services（Outlook、Teams、OneDrive 等）。

### 注册 app <a href="#register-the-app" id="register-the-app"></a>

1. 在 [Microsoft Entra admin centre](https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade/quickStartType~/null/sourceType/Microsoft_AAD_IAM) 中，进入 **App registrations** 并选择 **+ New registration**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>在 <strong>App registrations</strong> 下注册，而不是在 <strong>Enterprise applications</strong> 下注册。</p></div>

2. 为 app 输入有意义的 **Name**，例如 `n8n Outlook`。
3. 在 **Supported account types** 下，选择 **Multiple Entra ID tenants**。
4. 在 **Allow only certain tenants (Preview)** 下，选择 **Manage allowed tenants** 并添加你的 tenant。添加 tenant 后，红色 banner 会消失。
5. 暂时将 **Redirect URI** 留空，然后选择 **Register**。
6. 在 app overview 页面，复制 **Application (client) ID**。稍后会用到它。

### 生成 client secret <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

1. 在 app overview 页面，选择 **Client credentials** 下的 **Add a certificate or secret**。
2. 选择 **+ New client secret**。
3. 输入 **Description**（例如 `n8n token`），并选择符合 organisation credentials policy 的 expiry period。
4. 选择 **Add**。
5. 立即复制 **Value**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>secret value 只会显示一次。复制前不要离开页面，否则之后无法再取回。</p></div>

### 配置 API permissions <a href="#configure-api-permissions" id="configure-api-permissions"></a>

1. 在左侧导航中点击 **API permissions**。
2. 点击 **+ Add a permission** > **Microsoft Graph** > **Delegated permissions**。
3. 在 **Select permissions** 框中，搜索每个所需 scope，并勾选它旁边的复选框。对你想启用的 integrations 所需的所有 scopes 重复此操作。完整列表请参考下方[按 integration 列出的所需 scopes](#required-scopes-by-integration)。
4. 选择 **Add permissions**。

### 添加 redirect URI <a href="#add-the-redirect-uri" id="add-the-redirect-uri"></a>

1. 在 n8n 中，创建一个包含你要配置的 Microsoft integrations 之一的 node 的 workflow（例如 Microsoft Outlook）。
2. 打开 node，并选择 **Set up credential** > **Create new credential**。
3. 为 credential 指定有意义的名称（例如 `admin@yourorg.com`）。
4. 复制 n8n credential 面板中显示的 **OAuth Redirect URL**。
5. 回到 Entra，进入 app overview 页面，并在 **Redirect URIs** 下选择 **Add a redirect URI**。
6. 选择 **+ Add redirect URI**，选择 **Web**，粘贴从 n8n 复制的 URL，然后选择 **Configure**。

### 在 n8n 中授予 admin consent <a href="#grant-admin-consent-in-n8n" id="grant-admin-consent-in-n8n"></a>

1. 在 n8n 中，将前面复制的 **Client ID** 和 **Client Secret** 粘贴到 credential 面板。
2. 选择 **Connect to [service]**（例如 **Connect to Microsoft Outlook**）。
3. 在 sign-in popup 中，勾选 **Consent on behalf of your organization**，然后选择 **Accept**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p>你必须以 admin 身份登录才能授予 organisation-wide consent。Non-admin accounts 会看到需要 admin approval 的提示。</p></div>

4. n8n 中的 success banner 会确认连接可用，并且 consent 已正确授予。

### 为用户预配置 credentials <a href="#pre-configure-credentials-for-users" id="pre-configure-credentials-for-users"></a>

授予 admin consent 后，使用 [credential overwrites](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-credentials/credential-overwrites) 预配置 Client ID 和 Client Secret，让 organisation 中的用户无需自己的 app registration 即可连接。Docker 和 Kubernetes 的设置说明请参考 [Microsoft OAuth credential overwrites configuration guide](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/configuration-examples/pre-configure-microsoft-oauth-credentials)。

### 按 integration 列出的所需 scopes <a href="#required-scopes-by-integration" id="required-scopes-by-integration"></a>

以下 scopes 是截至 2026 年 3 月每个 Microsoft integration 所需的 scopes。在 Entra 中配置 API permissions 时，请为你计划启用的每个 integration 添加对应 scopes。

| Integration | 所需 scopes |
|---|---|
| **Microsoft Dynamics** | `openid`, `offline_access` |
| **Microsoft Entra ID** | `openid`, `offline_access`, `AccessReview.ReadWrite.All`, `Directory.ReadWrite.All`, `NetworkAccessPolicy.ReadWrite.All`, `DelegatedAdminRelationship.ReadWrite.All`, `EntitlementManagement.ReadWrite.All`, `User.ReadWrite.All`, `Directory.AccessAsUser.All`, `Sites.FullControl.All`, `GroupMember.ReadWrite.All` |
| **Microsoft Excel** | `openid`, `offline_access`, `Files.ReadWrite` |
| **Microsoft Graph Security** | `SecurityEvents.ReadWrite.All`, `offline_access` |
| **Microsoft OneDrive** | `openid`, `offline_access`, `Files.ReadWrite.All` |
| **Microsoft Outlook** | `openid`, `offline_access`, `Contacts.Read`, `Contacts.ReadWrite`, `Calendars.Read`, `Calendars.Read.Shared`, `Calendars.ReadWrite`, `Mail.ReadWrite`, `Mail.ReadWrite.Shared`, `Mail.Send`, `Mail.Send.Shared`, `MailboxSettings.Read` |
| **Microsoft SharePoint** | `openid`, `offline_access` |
| **Microsoft Teams** | `openid`, `offline_access`, `User.Read.All`, `Group.ReadWrite.All`, `Chat.ReadWrite`, `ChannelMessage.Read.All` |
| **Microsoft To Do** | `openid`, `offline_access`, `Tasks.ReadWrite` |
| **Additional permissions for triggers** | `Chat.Read.All`, `Team.ReadBasic.All`, `Subscription.Read.All` |

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Microsoft Entra credentials 的已知常见 errors 和 issues。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fXYywkPyzPTxeGOEnYgb/" %}

### Delegated access 设置期间需要管理员批准 <a href="#admin-approval-required-during-delegated-access-setup" id="admin-approval-required-during-delegated-access-setup"></a>

如果用户看到提示需要 admin approval 的页面，说明尚未为 app registration 授予 organisation-wide consent。

要解决此问题，请使用 Entra ID admin account 完成上方[在 n8n 中授予 admin consent](#grant-admin-consent-in-n8n)步骤。

或者，administrator 可以直接在 Entra 中授予 consent，而不经过 n8n，路径为：

**Enterprise applications** > [your app] > **Security** > **Permissions** > **Grant admin consent for [your organisation]**

授予 consent 后，standard users 就可以完成身份验证，而不会遇到 admin approval prompt。

---
title: Microsoft credentials
description: >-
  Microsoft credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Microsoft 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Microsoft credentials
originalFilePath: integrations/builtin/credentials/microsoft.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/microsoft'
url: 'https://docs.n8n.io/integrations/builtin/credentials/microsoft'
layout:
  description:
    visible: false
---

# Microsoft credentials <a href="#microsoft-credentials" id="microsoft-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Microsoft Dynamics CRM](../app-nodes/n8n-nodes-base.microsoftdynamicscrm.md)
- [Microsoft Excel](../app-nodes/n8n-nodes-base.microsoftexcel.md)
- [Microsoft Graph Security](../app-nodes/n8n-nodes-base.microsoftgraphsecurity.md)
- [Microsoft OneDrive](../app-nodes/n8n-nodes-base.microsoftonedrive.md)
- [Microsoft Outlook](../app-nodes/n8n-nodes-base.microsoftoutlook.md)
- [Microsoft Outlook Trigger](../trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md)
- [Microsoft SharePoint](../app-nodes/n8n-nodes-base.microsoftsharepoint.md)
- [Microsoft Teams](../app-nodes/n8n-nodes-base.microsoftteams.md)
- [Microsoft Teams Trigger](../trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md)
- [Microsoft To Do](../app-nodes/n8n-nodes-base.microsofttodo.md)

{% hint style="info" %}
**选择 credential type**

某些 nodes（例如 Microsoft Excel 和 Microsoft OneDrive）允许你在 node-specific credential（例如 **Microsoft Excel OAuth2 API**）和此通用 **Microsoft OAuth2 API** credential 之间选择。通用 credential 可在多个 Microsoft nodes 间复用；使用它时，请确保已授予每个 node 所需的 scopes。不显示此下拉菜单的 nodes 使用各自 node-specific credential。
{% endhint %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Microsoft Azure](https://azure.microsoft.com/) 账号。
- 创建至少一个有权访问相应服务的 user account。
- 如果 corporate Microsoft Entra account 管理该 user account，administrator account 已为此用户启用 “User can consent to apps accessing company data on their behalf” 选项（请参阅 [Microsoft Entra documentation](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent)）。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关每个服务 API 的更多信息，请参考下方链接的 Microsoft API 文档：

- Dynamics CRM: [Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview)
- Excel: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/excel)
- Graph Security: [Graph API](https://learn.microsoft.com/en-us/graph/api/overview)
- OneDrive: [Graph API](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)
- Outlook: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview) 和 [Outlook API](https://learn.microsoft.com/en-us/outlook/rest/reference)
- Teams: [Graph API](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- To Do: [Graph API](https://learn.microsoft.com/en-us/graph/todo-concept-overview)

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

某些 Microsoft services 需要额外的 OAuth2 信息。有关这些服务的更多指导，请参考[服务特定设置](#service-specific-settings)。

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
1. 如果 n8n credential 中显示其他字段，请参考下方[服务特定设置](#service-specific-settings)了解如何完成这些字段。
1. 在 n8n 中选择 **Connect my account** 完成连接设置。
1. 登录 Microsoft account，并允许 app 访问你的信息。

有关添加 client secret 的更多信息，请参考 Microsoft 的 [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

### Microsoft Graph API Base URL <a href="#microsoft-graph-api-base-url" id="microsoft-graph-api-base-url"></a>

Microsoft OAuth2 credential 支持不同的 Microsoft cloud environments。请根据 tenant 的 cloud environment 选择合适的 endpoint：

- **Global**：用于标准 Microsoft 365 tenants（默认）
- **US Government**：用于 Azure US Government (GCC) tenants
- **US Government DOD**：用于 Azure US Government Department of Defense tenants
- **China**：用于由世纪互联运营的 Microsoft 365

此设置适用于所有使用 Microsoft credentials 的 Microsoft Graph API nodes，包括：

- Microsoft Teams
- Microsoft Outlook
- Microsoft Excel
- Microsoft OneDrive
- Microsoft Graph Security
- Microsoft To Do

{% hint style="warning" %}
**政府云 Authorization URLs**

如果你使用 government cloud tenant，可能还需要更新 credential 中的 **Authorization URL** 和 **Access Token URL** 字段，以使用 government cloud endpoints。例如：

- US Government：使用 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/authorize` 和 `https://login.microsoftonline.us/{tenant}/oauth2/v2.0/token`
- 将 `{tenant}` 替换为你的 tenant ID，或对 multi-tenant apps 使用 `common`
{% endhint %}

### 自定义 Scopes <a href="#custom-scopes" id="custom-scopes"></a>

为与以下 Microsoft services 交互定义细粒度 permissions：

* Microsoft Teams
* Microsoft Excel

### 服务特定设置 <a href="#service-specific-settings" id="service-specific-settings"></a>

以下服务需要额外的 OAuth2 信息：

#### Dynamics <a href="#dynamics" id="dynamics"></a>

Dynamics OAuth2 需要你的 Dynamics domain 和 region 信息。按以下额外步骤完成 credential：

1. 输入 Dynamics **Domain**。
2. 选择你所在的 Dynamics data center **Region**。

有关 region 选项和对应 URLs 的更多信息，请参考 [Microsoft Datacenter regions documentation](https://learn.microsoft.com/en-us/power-platform/admin/new-datacenter-regions)。

#### Microsoft (general) <a href="#microsoft-general" id="microsoft-general"></a>

通用 Microsoft OAuth2 还要求你为此 credential 提供以空格分隔的 **Scope** 列表。

可能的 scopes 列表请参考 [Scopes and permissions in the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/scopes-oidc)。

#### Outlook <a href="#outlook" id="outlook"></a>

Outlook OAuth2 支持 credential 访问用户的 primary email inbox 或 shared inbox。默认情况下，credential 会访问用户的 primary email inbox。要更改此行为：

1. 开启 **Use Shared Inbox**。
2. 将目标用户的 UPN 或 ID 输入为 **User Principal Name**。

#### SharePoint <a href="#sharepoint" id="sharepoint"></a>

SharePoint OAuth2 需要你的 SharePoint **Subdomain** 信息。

要完成 credential，请输入 SharePoint URL 中的 **Subdomain** 部分。例如，如果 SharePoint URL 是 `https://tenant123.sharepoint.com`，subdomain 就是 `tenant123`。

SharePoint 需要以下 permissions：

Application permissions：

* `Sites.Read.All`
* `Sites.ReadWrite.All`

Delegated permissions：

* `SearchConfiguration.Read.All`
* `SearchConfiguration.ReadWrite.All`

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Microsoft OAuth2 credentials 的已知常见 errors 和 issues。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fXYywkPyzPTxeGOEnYgb/" %}

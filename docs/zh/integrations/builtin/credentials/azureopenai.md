---
title: Azure OpenAI credentials
description: >-
  Azure OpenAI credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 OpenAI。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Azure OpenAI credentials
originalFilePath: integrations/builtin/credentials/azureopenai.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/azureopenai'
url: 'https://docs.n8n.io/integrations/builtin/credentials/azureopenai'
layout:
  description:
    visible: false
---

# Azure OpenAI credentials <a href="#azure-openai-credentials" id="azure-openai-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Chat Azure OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai.md)
- [Embeddings Azure OpenAI](../cluster-nodes/sub-nodes/n8n-nodes-langchain.embeddingsazureopenai.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- 创建一个 [Azure](https://azure.microsoft.com) subscription。
- 在该 subscription 中具备 Azure OpenAI 访问权限。如果你的 organization 尚未拥有访问权限，可能需要[申请访问](https://aka.ms/oai/access)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API key
- Azure Entra ID (OAuth2)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure OpenAI 的 API 文档](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)。

## 使用 API key <a href="#using-api-key" id="using-api-key"></a>

要配置此 credential，你需要：

- **Resource Name**：你为 resource 指定的 **Name**
- **API key**：**Key 1** 通常可用。部署前可在 **Keys and Endpoint** 中访问。
- credentials 应使用的 **API Version**。有关 Azure OpenAI 中 API 版本控制的更多信息，请参阅 [Azure OpenAI API preview lifecycle 文档](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation)。

要获取上述信息，请[创建并部署一个 Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource)。

{% hint style="info" %}
**Azure OpenAI nodes 的 model name**

部署 resource 后，在使用此 credential 的 Azure OpenAI nodes 中，将 **Deployment name** 用作 model name。
{% endhint %}

## 使用 Azure Entra ID (OAuth2) <a href="#using-azure-entra-id-oauth2" id="using-azure-entra-id-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

对于 self-hosted 用户，从零配置 OAuth2 主要有两个步骤：

1. 在 Microsoft Identity Platform 中[注册一个 application](#register-an-application)。
2. 为该 application [生成 client secret](#generate-a-client-secret)。

按照下面每个步骤的详细说明操作。有关 Microsoft OAuth2 web flow 的更多细节，请参阅 [Microsoft authentication and authorization basics](https://learn.microsoft.com/en-us/graph/auth/auth-concepts)。

### 注册一个 application <a href="#register-an-application" id="register-an-application"></a>

使用 Microsoft Identity Platform 注册 application：

1. 打开 [Microsoft Application Registration Portal](https://aka.ms/appregistrations)。
2. 选择 **Register an application**。
3. 为你的 app 输入 **Name**。
4. 在 **Supported account types** 中，选择 **Accounts in any organizational directory (Any Azure AD directory - Multi-tenant) and personal Microsoft accounts (for example, Skype, Xbox)**。
5. 在 **Register an application** 中：
    1. 从 n8n credential 复制 **OAuth Callback URL**。
    2. 将其粘贴到 **Redirect URI (optional)** 字段。
    3. 选择 **Select a platform** > **Web**。
6. 选择 **Register** 完成 application 创建。
7. 复制 **Application (client) ID**，并在 n8n 中将其粘贴为 **Client ID**。

有关更多信息，请参阅 [Register an application with the Microsoft Identity Platform](https://learn.microsoft.com/en-us/graph/auth-register-app-v2)。

### 生成 client secret <a href="#generate-a-client-secret" id="generate-a-client-secret"></a>

创建 application 后，为它生成 client secret：

1. 在 Microsoft application 页面上，从左侧导航选择 **Certificates & secrets**。
1. 在 **Client secrets** 中，选择 **+ New client secret**。
1. 输入 client secret 的 **Description**，例如 `n8n credential`。
1. 选择 **Add**。
1. 复制 **Value** 列中的 **Secret**。
1. 在 n8n 中将其粘贴为 **Client Secret**。
1. 在 n8n 中选择 **Connect my account** 完成连接设置。
1. 登录你的 Microsoft 账号，并允许 app 访问你的信息。

有关添加 client secret 的更多信息，请参阅 Microsoft 的 [Add credentials](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-credentials)。

## 设置 custom scopes <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Azure Entra ID credentials 默认使用以下 scopes：

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

如需为 credentials 选择不同 scopes，请启用 **Custom Scopes** slider 并编辑 **Enabled Scopes** 列表。请注意，使用更严格的 scopes 时，部分功能可能无法按预期工作。

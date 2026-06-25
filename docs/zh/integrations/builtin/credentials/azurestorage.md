---
title: Azure Storage credentials
description: >-
  Azure Storage credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Azure Storage。
contentType:
  - integration
  - reference
nodeTitle: Azure Storage credentials
originalFilePath: integrations/builtin/credentials/azurestorage.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/azurestorage'
url: 'https://docs.n8n.io/integrations/builtin/credentials/azurestorage'
layout:
  description:
    visible: false
---

# Azure Storage credentials <a href="#azure-storage-credentials" id="azure-storage-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Azure Storage](../app-nodes/n8n-nodes-base.azurestorage.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Azure](https://azure.microsoft.com) subscription。
* 创建一个 [Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2
* Shared Key

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Azure Storage 的 API 文档](https://learn.microsoft.com/en-us/rest/api/storageservices/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

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

## 使用 Shared Key <a href="#using-shared-key" id="using-shared-key"></a>

要配置此 credential，你需要：

* **Account**：你的 Azure Storage account 名称。
* **Key**：Azure Storage account 的 shared key。选择 **Security + networking**，然后选择 **Access keys**。你可以使用两个 account keys 中的任意一个。

有关更详细的步骤，请参阅 [Manage storage account access keys | Microsoft](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage)。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Azure Storage credentials 的已知常见错误和问题。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/fXYywkPyzPTxeGOEnYgb/" %}

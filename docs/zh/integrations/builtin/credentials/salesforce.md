---
title: Salesforce credentials
description: >-
  Salesforce credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Salesforce 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Salesforce credentials
originalFilePath: integrations/builtin/credentials/salesforce.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/salesforce'
url: 'https://docs.n8n.io/integrations/builtin/credentials/salesforce'
layout:
  description:
    visible: false
---

# Salesforce credentials <a href="#salesforce-credentials" id="salesforce-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Salesforce](../app-nodes/n8n-nodes-base.salesforce.md)
- [Salesforce trigger](../trigger-nodes/n8n-nodes-base.salesforcetrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- JWT
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Salesforce's developer documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_intro.htm)。

{% hint style="info" %}
**Salesforce External Client Apps**

Salesforce 正在弃用 Connected Apps，转向 External Client Apps。两种方式都可与 n8n 配合使用。如果你在创建新的 integration，请使用 External Client Apps。现有 Connected Apps 会继续工作。
{% endhint %}

## 使用 JWT <a href="#using-jwt" id="using-jwt"></a>

要配置此 credential，你需要一个 [Salesforce](https://www.salesforce.com/) 账号，以及：

- 你的 **Environment Type**（Production 或 Sandbox）
- 一个 **Client ID**：创建 external client app 或 connected app 时生成。
- 你的 Salesforce **Username**
- 用于 self-signed digital certificate 的 **Private Key**

### 创建 External Client App（推荐） <a href="#create-an-external-client-app-recommended" id="create-an-external-client-app-recommended"></a>

设置时，你首先需要创建 private key 和 certificate，然后创建 external client app：

1. 在 n8n 中，为 connection 选择 **Environment Type**。从 **Production** 或 **Sandbox** 中选择最符合你 environment 的选项。
2. 输入你的 Salesforce **Username**。
3. 登录 Salesforce 中的 org。
4. 你需要一个由 certification authority 签发的 private key 和 certificate。使用你自己的 key/cert，或使用 OpenSSL 创建 key 和 self-signed digital certificate。有关创建自己的 key 和 certificate 的说明，请参考 Salesforce [Create a Private Key and Self-Signed Digital Certificate documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm)。
5. 在 Salesforce 的 **Setup** 中，在 Quick Find box 输入 `App Manager`，然后选择 **App Manager**。
6. 在 App Manager page 上，选择 **New External Client App**。
7. 输入 external client app 必需的 **Basic Info**，包括 **Name** 和 **Contact Email address**。
8. 在 **API (Enable OAuth Settings)** 下，选择 **Enable OAuth**。
9. 在 **Callback URL** box 中，添加 callback URL：`http://localhost:1717/OauthRedirect`（如果 self-hosting，则使用你的 n8n instance URL）。
10. 在 **OAuth Scopes** section 中，选择这些 scopes：
    - **Full access (full)**
    - **Perform requests at any time (refresh_token, offline_access)**
11. 在 **Flow Enablement** section 中，选择 **Enable JWT Bearer Flow**。
12. 选择 **Upload Files**，并上传包含 digital certificate 的 file，例如 `server.crt`。
13. 在 **OAuth Policies** 下，确保以下设置为 **unchecked**：
    - **Require Secret for Web Server Flow**
    - **Require Secret for Refresh Token Flow**
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**
14. 选择 **Save**，然后选择 **Continue**。
15. 复制 **Consumer Key**，并在你的 n8n credential 中将其添加为 **Client ID**。
16. 在 n8n 中将 private key file 的内容输入为 **Private Key**。
    - 使用 n8n 中的 multi-line editor。
    - 以标准 PEM key format 输入 private key：
        ```
        -----BEGIN PRIVATE KEY-----
        KEY DATA GOES HERE
        -----END PRIVATE KEY-----
        ```

更多信息请参考 Salesforce 的 [External Client App Basics](https://help.salesforce.com/s/articleView?id=sf.external_client_app_about.htm&type=5) 文档。

### 创建 Connected App（legacy） <a href="#create-a-connected-app-legacy" id="create-a-connected-app-legacy"></a>

{% hint style="info" %}
**Legacy method**

Salesforce 正在弃用 Connected Apps。新的 integrations 请改用 External Client Apps。
{% endhint %}

设置时，你首先需要创建 private key 和 certificate，然后创建 connected app：

1. 在 n8n 中，为 connection 选择 **Environment Type**。从 **Production** 或 **Sandbox** 中选择最符合你 environment 的选项。
2. 输入你的 Salesforce **Username**。
3. 登录 Salesforce 中的 org。
4. 你需要一个由 certification authority 签发的 private key 和 certificate。使用你自己的 key/cert，或使用 OpenSSL 创建 key 和 self-signed digital certificate。有关创建自己的 key 和 certificate 的说明，请参考 Salesforce [Create a Private Key and Self-Signed Digital Certificate documentation](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm)。
5. 在 Salesforce 的 **Setup** 中，在 Quick Find box 输入 `App Manager`，然后选择 **App Manager**。
6. 在 App Manager page 上，选择 **New Connected App**。
7. 输入 connected app 必需的 **Basic Info**，包括 **Name** 和 **Contact Email address**。更多信息请参考 Salesforce 的 [Configure Basic Connected App Settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5) 文档。
8. 勾选 **Enable OAuth Settings**。
9. 对于 **Callback URL**，输入 `http://localhost:1717/OauthRedirect`。
10. 勾选 **Use digital signatures**。
11. 选择 **Choose File**，并上传包含 digital certificate 的 file，例如 `server.crt`。
12. 添加这些 **OAuth scopes**：
    - **Full access (full)**
    - **Perform requests at any time (refresh_token, offline_access)**
13. 选择 **Save**，然后选择 **Continue**。**Manage Connected Apps** page 应打开到你刚创建的 app。
14. 在 **API (Enable OAuth Settings)** section 中，选择 **Manage Consumer Details**。
15. 复制 **Consumer Key**，并在你的 n8n credential 中将其添加为 **Client ID**。
16. 在 n8n 中将 private key file 的内容输入为 **Private Key**。
    - 使用 n8n 中的 multi-line editor。
    - 以标准 PEM key format 输入 private key：
        ```
        -----BEGIN PRIVATE KEY-----
        KEY DATA GOES HERE
        -----END PRIVATE KEY-----
        ```

这些步骤是 n8n 侧所必需的内容。Salesforce 也建议设置 refresh token policies、session policies 和 OAuth policies：

17. 在 Salesforce 中，选择 **Back to Manage Connected Apps**。
18. 选择 **Manage**。
19. 选择 **Edit Policies**。
20. 检查 **Refresh Token Policy** 字段。Salesforce 建议使用 expire refresh token after 90 days。
21. 在 **Session Policies** section 中，Salesforce 建议将 **Timeout Value** 设置为 15 minutes。
22. 在 **OAuth Policies** section 中，针对 **Permitted Users** 选择 **Admin approved users are pre-authorized for permitted users**，然后选择 **OK**。
23. 选择 **Save**。
24. 选择 **Manage Profiles**，选择预授权使用此 connected app 的 profiles，然后选择 **Save**。
25. 选择 **Manage Permission Sets** 以选择 permission sets。必要时创建 permission sets。

更多信息请参考 Salesforce 的 [Create a Connected App in Your Org](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm) 文档。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Salesforce](https://www.salesforce.com/) 账号。

你需要选择 **Environment Type**。在 **Production** 和 **Sandbox** 之间选择。

### 创建 External Client App（推荐） <a href="#create-an-external-client-app-recommended" id="create-an-external-client-app-recommended"></a>

如果你[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要通过创建 external client app 从头配置 OAuth2：

1. 在 n8n 中，为 connection 选择 **Environment Type**。从 **Production** 或 **Sandbox** 中选择最符合你 environment 的选项。
2. 输入你的 Salesforce **Username**。
3. 登录 Salesforce 中的 org。
4. 在 Salesforce 的 **Setup** 中，在 Quick Find box 输入 `App Manager`，然后选择 **App Manager**。
5. 在 App Manager page 上，选择 **New External Client App**。
6. 输入 external client app 必需的 **Basic Info**，包括 **Name** 和 **Contact Email address**。
7. 在 **API (Enable OAuth Settings)** 下，选择 **Enable OAuth**。
8. 在 **Callback URL** box 中，添加你的 n8n OAuth callback URL（例如 `https://your-n8n-instance.com/rest/oauth2-credential/callback`。对于 n8n Cloud，则为 `https://oauth.n8n.cloud/oauth2/callback`）。
9. 在 **OAuth Scopes** section 中，选择这些 scopes：
    - **Full access (full)**
    - **Perform requests at any time (refresh_token, offline_access)**
10. 在 **Flow Enablement** section 中，选择 **Enable Authorization Code and Credentials Flow**。
11. 在 **OAuth Policies** 下，确保以下设置为 **checked**：
    - **Require Secret for Web Server Flow**
    - **Require Secret for Refresh Token Flow**
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**
12. 选择 **Save**，然后选择 **Continue**。
13. 复制 **Consumer Key**，并在你的 n8n credential 中将其添加为 **Client ID**。
14. 复制 **Consumer Secret**，并在你的 n8n credential 中将其添加为 **Client Secret**。

更多信息请参考 Salesforce 的 [External Client App Basics](https://help.salesforce.com/s/articleView?id=sf.external_client_app_about.htm&type=5) 文档。

### 创建 Connected App（legacy） <a href="#create-a-connected-app-legacy" id="create-a-connected-app-legacy"></a>

{% hint style="info" %}
**Legacy method**

Salesforce 正在弃用 Connected Apps。新的 integrations 请改用 External Client Apps。
{% endhint %}

如果你[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，也可以通过创建 connected app 来配置 OAuth2：

1. 在 n8n 中，为 connection 选择 **Environment Type**。从 **Production** 或 **Sandbox** 中选择最符合你 environment 的选项。
2. 输入你的 Salesforce **Username**。
3. 登录 Salesforce 中的 org。
4. 在 Salesforce 的 **Setup** 中，在 Quick Find box 输入 `App Manager`，然后选择 **App Manager**。
5. 在 App Manager page 上，选择 **New Connected App**。
6. 输入 connected app 必需的 **Basic Info**，包括 **Name** 和 **Contact Email address**。更多信息请参考 Salesforce 的 [Configure Basic Connected App Settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5) 文档。
7. 勾选 **Enable OAuth Settings**。
8. 对于 **Callback URL**，输入 `http://localhost:1717/OauthRedirect`。
9. 添加这些 **OAuth scopes**：
    - **Full access (full)**
    - **Perform requests at any time (refresh_token, offline_access)**
10. 确保以下设置未勾选：
    - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**
    - **Require Secret for Web Server Flow**
    - **Require Secret for Refresh Token Flow**
11. 选择 **Save**，然后选择 **Continue**。**Manage Connected Apps** page 应打开到你刚创建的 app。
12. 在 **API (Enable OAuth Settings)** section 中，选择 **Manage Consumer Details**。
13. 复制 **Consumer Key**，并在你的 n8n credential 中将其添加为 **Client ID**。
14. 复制 **Consumer Secret**，并在你的 n8n credential 中将其添加为 **Client Secret**。

这些步骤是 n8n 侧所必需的内容。Salesforce 也建议设置 refresh token policies 和 session policies：

15. 在 Salesforce 中，选择 **Back to Manage Connected Apps**。
16. 选择 **Manage**。
17. 选择 **Edit Policies**。
18. 检查 **Refresh Token Policy** 字段。Salesforce 建议使用 expire refresh token after 90 days。
19. 在 **Session Policies** section 中，Salesforce 建议将 **Timeout Value** 设置为 15 minutes。

更多信息请参考 Salesforce 的 [Create a Connected App in Your Org](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_connected_app.htm) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### 从 n8n Cloud 使用 Salesforce 身份验证时的连接问题 <a href="#connection-issues-when-authenticating-with-salesforce-from-n8n-cloud" id="connection-issues-when-authenticating-with-salesforce-from-n8n-cloud"></a>

如果你在从 n8n Cloud 使用 Salesforce 身份验证时遇到连接问题，可能需要在 Salesforce user profiles 中启用一个特定 system permission：

1. 在 Salesforce 中，前往 **Setup**。
2. 在 **Quick Find** box 中，搜索 `Profiles`。
3. 选择用于连接到 n8n 的 user 所使用的 profile（例如 System Administrator 或相关 profile）。
4. 点击 **Edit**；如果新的 **Profile** interface 可用，也可以使用它。
5. 找到 **Administrative Permissions** section。
6. 为 **Approve Connected Apps for Non-Admins** 启用 checkbox。根据你的 Salesforce language 或 translation，此 checkbox 也可能显示为 **Approve apps connected not installed**。
7. 点击 **Save**。

即使对于 administrator profiles，此 permission 默认也未启用，必须手动激活。如果没有此 permission，尝试将 n8n 连接到 Salesforce 时可能会遇到 authentication failures。

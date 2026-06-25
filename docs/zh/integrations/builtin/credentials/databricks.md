---
title: Databricks credentials
description: >-
  Databricks credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Databricks。
contentType:
  - integration
  - reference
nodeTitle: Databricks credentials
originalFilePath: integrations/builtin/credentials/databricks.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/databricks'
url: 'https://docs.n8n.io/integrations/builtin/credentials/databricks'
layout:
  description:
    visible: false
---

# Databricks credentials <a href="#databricks-credentials" id="databricks-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Databricks](../app-nodes/n8n-nodes-base.databricks.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

- AWS、Azure 或 GCP 上的一个 [Databricks](https://www.databricks.com/) workspace。
- 一个对你要执行的 operations 具备足够权限的 Databricks user account。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Personal access token
- OAuth2 (service principal)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Databricks authentication 文档](https://docs.databricks.com/aws/en/dev-tools/auth/)。

## 使用 personal access token <a href="#using-a-personal-access-token" id="using-a-personal-access-token"></a>

要配置此 credential，你需要：

- 一个 **Host**：你的 Databricks workspace URL（例如 `https://adb-1234567890123456.7.azuredatabricks.net`）。
- 一个 **Access Token**：在你的 Databricks workspace 中生成的 personal access token。

生成 personal access token：

1. 在 Databricks workspace 中，选择右上角的用户名，然后选择 **Settings**。
2. 选择 **Developer**。
3. 在 **Access tokens** 旁边，选择 **Manage**。
4. 选择 **Generate new token**。
5. 可选输入 **Comment** 以识别该 token，然后选择 **Generate**。
6. 复制 token 并保存在安全位置。关闭此对话框后，你将无法再次查看该 token。
7. 在 n8n credential 中将 token 输入为 **Access Token**。

{% hint style="info" %}
**Token 格式**

Personal access tokens 以 `dapi` 开头，例如 `dapi1234abcd5678efgh`。
{% endhint %}

有关更多信息，请参阅 [Databricks personal access token authentication](https://docs.databricks.com/en/dev-tools/auth/pat.html)。

## 使用 OAuth2 (service principal) <a href="#using-oauth2-service-principal" id="using-oauth2-service-principal"></a>

此方法使用 Databricks service principal 和 OAuth M2M (machine-to-machine) flow。它是 automated workflows 的推荐方式，因为它不需要 user interaction。

要配置此 credential，你需要：

- 一个 **Host**：你的 Databricks workspace URL（例如 `https://adb-1234567890123456.7.azuredatabricks.net`）。
- 一个 **Client ID**：你的 service principal 的 application ID。
- 一个 **Client Secret**：为 service principal 生成的 OAuth secret。

设置此 credential 有两个步骤：

1. [在 Databricks 中创建 service principal 和 OAuth secret](#create-a-service-principal-and-oauth-secret)。
2. [在 n8n 中设置 credential](#set-up-the-oauth2-credential)。

### 创建 service principal 和 OAuth secret <a href="#create-a-service-principal-and-oauth-secret" id="create-a-service-principal-and-oauth-secret"></a>

1. 在 Databricks account console 中，选择 **User management**。
2. 选择 **Service principals**，然后选择 **Add service principal**。
3. 输入 service principal 的名称并选择 **Add**。
4. 打开 service principal，前往 **Configuration** 选项卡，并授予它所需的 workspace entitlements。
5. 前往 **Secrets** 选项卡并选择 **Generate secret**。
6. 设置 secret 的有效天数（最长 730 天），然后选择 **Generate**。
7. 复制显示的 **Secret** 和 **Client ID**（与 application ID 相同）。secret 只会显示一次。

{% hint style="info" %}
**Workspace assignment**

service principal 必须分配给它将访问的 workspace。前往 **Permissions** 选项卡，并授予所需 users 或 groups 管理和使用该 service principal 的访问权限。
{% endhint %}

有关更多信息，请参阅 [Authorize service principal access to Databricks with OAuth](https://docs.databricks.com/en/dev-tools/auth/oauth-m2m.html)。

### 设置 OAuth2 credential <a href="#set-up-the-oauth2-credential" id="set-up-the-oauth2-credential"></a>

在 n8n credential 中：

1. 将 **Authentication** 设置为 **OAuth2**。
2. 将 workspace URL 输入为 **Host**。
3. 输入从 service principal 复制的 **Client ID**。
4. 输入你生成的 **Client Secret**。

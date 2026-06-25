---
title: Jira credentials
description: >-
  Jira credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对 Jira
  进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Jira credentials
originalFilePath: integrations/builtin/credentials/jira.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/jira'
url: 'https://docs.n8n.io/integrations/builtin/credentials/jira'
layout:
  description:
    visible: false
---

# Jira credentials <a href="#jira-credentials" id="jira-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Jira](../app-nodes/n8n-nodes-base.jira.md)
- [Jira Trigger](../trigger-nodes/n8n-nodes-base.jiratrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Jira](https://www.atlassian.com/software/jira) Software Cloud 或 Server 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- [SW Cloud OAuth2](#using-sw-cloud-oauth2)：将此方式与 [Jira Software Cloud](https://www.atlassian.com/software/jira) 配合用于 OAuth2 身份验证。
- [SW Cloud API token](#using-sw-cloud-api-token)：将此方式与 [Jira Software Cloud](https://www.atlassian.com/software/jira) 配合使用。
- [SW Server account](#using-sw-server-account)：将此方式与 [Jira Software Server](https://www.atlassian.com/software/jira/download.) 配合使用。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Jira's API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v2/intro/#about)。

## 使用 SW Cloud OAuth2 <a href="#using-sw-cloud-oauth2" id="using-sw-cloud-oauth2"></a>

要配置此 credential，你需要一个 [Jira Software Cloud](https://www.atlassian.com/software/jira) 账号，并且可以访问 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)。

然后：

1. 打开 [Atlassian Developer Console](https://developer.atlassian.com/console/myapps/)，并选择 **Create** > **OAuth 2.0 integration**。
2. 输入 app 的 **Name** 并同意条款，然后选择 **Create**。
3. 在左侧边栏选择 **Authorization**。
4. 在 **OAuth 2.0 (3LO)** 旁边选择 **Add**。
5. 在 n8n 中复制 **OAuth Redirect URL**。
6. 将该 URL 粘贴到 Atlassian Developer Console 的 **Callback URL** 字段。
7. 选择 **Save changes**。
8. 在左侧边栏选择 **Permissions**，然后在 **Jira API** 旁边选择 **Add**。
9. 选择 **Jira API** > **Edit Scopes** 旁边的 **Configure**。至少启用以下 scopes，然后保存修改：
	- `read:jira-user`
	- `read:jira-work`
	- `write:jira-work`
	- `manage:jira-webhook`
	- `manage:jira-user`
	- `offline_access`
10. 在左侧边栏选择 **Settings**。
11. 复制 **Client ID** 并粘贴到 n8n。
12. 复制 **Secret**，并在 n8n 中将其粘贴为 **Client Secret**。
13. 输入你访问 Jira 的 **Domain**，例如 `https://example.atlassian.net`。
14. 选择 **Connect to Jira SW Cloud**，并按照提示完成 OAuth2 flow。

更多信息请参考 Atlassian 文档中的 [OAuth 2.0 (3LO) apps](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/)。

## 使用 SW Cloud API token <a href="#using-sw-cloud-api-token" id="using-sw-cloud-api-token"></a>

要配置此 credential，你需要一个 [Jira Software Cloud](https://www.atlassian.com/software/jira) 账号。

然后：

1. 登录你的 Atlassian profile > **Security > API tokens** 页面，或使用此[链接](https://id.atlassian.com/manage-profile/security/api-tokens)直接跳转。
2. 选择 **Create API Token**。
3. 输入 token 的 **Name**，例如 `n8n integration`。
4. 设置 **Expires on** 日期，或保留默认日期。
5. 选择 **Create**。
6. 复制 API token。
7. 在 n8n 中，输入与你 Jira 账号关联的 **Email** address。
8. 将复制的 API token 粘贴为你的 **API Token**。
9. 输入你访问 Jira 的 **Domain**，例如 `https://example.atlassian.net`。

更多信息请参考 [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)。

{% hint style="info" %}
**新 tokens**

新的 tokens 可能最多需要一分钟才能生效。如果 credential verification 第一次失败，请等待一分钟再重试。
{% endhint %}

## 使用 SW Server account <a href="#using-sw-server-account" id="using-sw-server-account"></a>

要配置此 credential，你需要一个 [Jira Software Server](https://www.atlassian.com/software/jira/download.) 账号。

然后：

1. 输入与你 Jira 账号关联的 **Email** address。
2. 输入你的 Jira 账号 **Password**。
3. 输入你访问 Jira 的 **Domain**。

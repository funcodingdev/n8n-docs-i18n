---
title: Formstack Trigger credentials
description: >-
  Formstack Trigger credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  automation platform 中验证 Formstack Trigger。
contentType:
  - integration
  - reference
nodeTitle: Formstack Trigger credentials
originalFilePath: integrations/builtin/credentials/formstacktrigger.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/formstacktrigger'
url: 'https://docs.n8n.io/integrations/builtin/credentials/formstacktrigger'
layout:
  description:
    visible: false
---

# Formstack Trigger credentials <a href="#formstack-trigger-credentials" id="formstack-trigger-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Formstack Trigger](../trigger-nodes/n8n-nodes-base.formstacktrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Formstack](https://www.formstack.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Formstack 的 API 文档](https://developers.formstack.com/reference/api-overview)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要：

- 一个 API **Access Token**：要生成 Access Token，请在 Formstack 中使用以下详细信息[创建新 application](https://www.formstack.com/admin/apiKey/main)：
    * **Redirect URI**：对于 cloud n8n instances，输入 `https://oauth.n8n.cloud/oauth2/callback`。
        - 对于 self-hosted n8n instances，请输入 n8n instance 的 OAuth callback URL，格式为 `https://<n8n_url>/rest/oauth2-credential/callback`。例如 `https://localhost:5678/rest/oauth2-credential/callback`。
    * **Platform**：选择 **Website**。

创建 application 后，从 applications 列表复制 access token，或选择 application 查看详情后复制。

有关更详细的说明，请参阅 [Formstack API Authorization 文档](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token)。

{% hint style="info" %}
**Access token 权限**

Formstack 将 access tokens 绑定到 Formstack user。Access tokens 遵循 Formstack（in-app）user permissions。
{% endhint %}

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**
- 一个 **Client Secret**

要生成二者，请在 Formstack 中使用以下详细信息[创建新 application](https://www.formstack.com/admin/apiKey/main)：

- **Redirect URI**：从 n8n credential 复制 **OAuth Redirect URL** 并输入到这里。
    - 对于 self-hosted n8n instances，请输入 n8n instance 的 OAuth callback URL，格式为 `https://<n8n_url>/rest/oauth2-credential/callback`。例如 `https://localhost:5678/rest/oauth2-credential/callback`。
- **Platform**：选择 **Website**。

创建 application 后，从 applications 列表中选择它以查看 **Application Details**。复制 **Client ID** 和 **Client Secret** 并添加到 n8n。二者都添加后，选择 **Connect my account** 按钮开始 OAuth2 flow 和 authorization process。

有关更详细的说明，请参阅 [Formstack API Authorization 文档](https://developers.formstack.com/reference/api-overview#obtaining-an-api-key-oauth2-access-token)。

{% hint style="info" %}
**Access token 权限**

Formstack 将 access tokens 绑定到 Formstack user。Access tokens 遵循 Formstack（in-app）user permissions。
{% endhint %}

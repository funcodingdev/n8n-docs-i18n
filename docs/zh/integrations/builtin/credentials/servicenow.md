---
title: ServiceNow credentials
description: >-
  ServiceNow credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 ServiceNow 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: ServiceNow credentials
originalFilePath: integrations/builtin/credentials/servicenow.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/servicenow'
url: 'https://docs.n8n.io/integrations/builtin/credentials/servicenow'
layout:
  description:
    visible: false
---

# ServiceNow credentials <a href="#servicenow-credentials" id="servicenow-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [ServiceNow](../app-nodes/n8n-nodes-base.servicenow.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [ServiceNow](https://developer.servicenow.com/dev.do#!/reference) developer account。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Basic auth
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [ServiceNow's API documentation](https://developer.servicenow.com/dev.do#!/reference/api/washingtondc/rest/)。

## 使用 basic auth <a href="#using-basic-auth" id="using-basic-auth"></a>

要配置此 credential，你需要：

- 一个 **User** name：输入你的 ServiceNow username。
- 一个 **Password**：输入你的 ServiceNow password。
- 一个 **Subdomain**：你的 servicenow 实例的 subdomain 位于实例 URL 中：`https://<subdomain>.service-now.com/`。例如，如果完整 URL 是 `https://dev99890.service-now.com`，则 subdomain 是 `dev99890`。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**：注册新 app 后生成。
- 一个 **Client Secret**：注册新 app 后生成。
- 一个 **Subdomain**：你的 servicenow 实例的 subdomain 位于实例 URL 中：`https://<subdomain>.service-now.com/`。例如，如果完整 URL 是 `https://dev99890.service-now.com`，则 subdomain 是 `dev99890`。

要生成你的 **Client ID** 和 **Client Secret**，请在 **System OAuth > Application Registry > New > Create an OAuth API endpoint for external clients** 中注册一个新 app。为你的 app 使用以下设置：

- 复制 **Client ID**，并将其添加到你的 n8n credential。
- 输入 **Client Secret**，或留空以自动生成随机 secret。将此 secret 添加到你的 n8n credential。
- 复制 n8n **OAuth Redirect URL**，并将其添加为 **Redirect URL**。

更多信息请参考 [How to setup OAuth2 authentication for RESTMessageV2 integrations](https://www.servicenow.com/community/in-other-news/how-to-setup-oauth2-authentication-for-restmessagev2/ba-p/2271823)。

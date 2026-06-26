---
title: PagerDuty credentials
description: >-
  PagerDuty credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  PagerDuty 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: PagerDuty credentials
originalFilePath: integrations/builtin/credentials/pagerduty.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/pagerduty'
url: 'https://docs.n8n.io/integrations/builtin/credentials/pagerduty'
layout:
  description:
    visible: false
---

# PagerDuty credentials <a href="#pagerduty-credentials" id="pagerduty-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [PagerDuty](../app-nodes/n8n-nodes-base.pagerduty.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [PagerDuty](https://pagerduty.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [PagerDuty's API documentation](https://developer.pagerduty.com/docs/531092d4c6658-rest-api-v2-overview)。

## 使用 API token <a href="#using-api-token" id="using-api-token"></a>

要配置此 credential，你需要：

- 一个 general access **API Token**：要生成 API token，请前往 **Integrations > Developer Tools > API Access Keys > Create New API Key**。更多信息请参考 [Generate a General Access REST API key](https://support.pagerduty.com/docs/api-access-keys#generate-a-general-access-rest-api-key)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你需要从头配置 OAuth2，请[注册一个新的 Pagerduty app](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app)。

注册 app 时使用这些设置：

- 在 **Category** dropdown list 中，选择 **Infrastructure Automation**。
- 在 **Functionality** section 中，选择 **OAuth 2.0**。

**Save** app 后，打开 app details，并[编辑你的 app configuration](https://developer.pagerduty.com/docs/dd91fbd09a1a1-register-an-app#editing-your-app-configuration) 以使用这些设置：

- 在 **OAuth 2.0** section 中，选择 **Add**。
- 从 n8n 复制 **OAuth Callback URL**，并将其粘贴到 **Redirect URL** 字段。
- 从 PagerDuty 复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credentials。
- 从 **Set Permission Scopes** dropdown list 中选择 **Read/Write**。

有关可用 functionality 的更多信息，请参考 [App functionality](https://developer.pagerduty.com/docs/b25fd1b8acb1b-app-functionality) 中的说明。有关 OAuth flow 的更多信息，请参考 PagerDuty [OAuth Functionality documentation](https://developer.pagerduty.com/docs/f59fdbd94ceab-o-auth-functionality)。

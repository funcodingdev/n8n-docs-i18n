---
title: Gong credentials
description: >-
  Gong credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Gong。
contentType:
  - integration
  - reference
nodeTitle: Gong credentials
originalFilePath: integrations/builtin/credentials/gong.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/gong'
url: 'https://docs.n8n.io/integrations/builtin/credentials/gong'
layout:
  description:
    visible: false
---

# Gong credentials <a href="#gong-credentials" id="gong-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

* [Gong](../app-nodes/n8n-nodes-base.gong.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Gong 的 API 文档](https://gong.app.gong.io/settings/api/documentation)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [Gong](https://app.gong.io/welcome/sign-in) 账号，以及：

- 一个 **Access Key**
- 一个 **Access Key Secret**

你可以在 [Gong API Page](https://app.gong.io/company/api) 创建这两项（你必须是 Gong 中的 technical administrator 才能访问此资源）。

有关向该服务进行身份验证的更多信息，请参阅 [Gong 的 API 文档](https://gong.app.gong.io/settings/api/documentation)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Gong](https://app.gong.io/welcome/sign-in) 账号、一个 [Gong developer](https://gong.partnerfleet.app/application_forms/become-a-gong-technology-partner/partner_applications/new) 账号，以及：

* 一个 **Client ID**：创建 Gong Oauth app 时生成。
* 一个 **Client Secret**：创建 Gong Oauth app 时生成。

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要[创建 app](https://help.gong.io/docs/create-an-app-for-gong) 来配置 OAuth2。有关设置 OAuth2 的更多信息，请参阅 [Gong OAuth 文档](https://gong.app.gong.io/settings/api/documentation)。

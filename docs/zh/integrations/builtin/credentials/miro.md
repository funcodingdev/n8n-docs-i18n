---
title: Miro credentials
description: >-
  Miro credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Miro 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Miro credentials
originalFilePath: integrations/builtin/credentials/miro.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/miro'
url: 'https://docs.n8n.io/integrations/builtin/credentials/miro'
layout:
  description:
    visible: false
---

# Miro credentials <a href="#miro-credentials" id="miro-credentials"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/7QbEnpnpOks3Rq0SiMFb/" %}

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Miro](https://miro.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Miro's API documentation](https://developers.miro.com/reference/overview)。

这是一个 credential-only node。请参考 [Custom API operations](../custom-api-actions-for-existing-nodes.md) 了解更多信息。在 n8n 网站上查看[示例 workflows 和相关内容](https://n8n.io/integrations/miro/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Miro](https://miro.com/login/) 账号和 app，以及：

- 一个 **Client ID**：创建新的 OAuth2 application 时生成。
- 一个 **Client Secret**：创建新的 OAuth2 application 时生成。

有关对该服务进行身份验证的更多信息，请参考 [Miro's API documentation](https://developers.miro.com/reference/overview)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，则需要[创建一个 app](https://developers.miro.com/docs/rest-api-build-your-first-hello-world-app) 来配置 OAuth2。有关设置 OAuth2 的更多信息，请参考 [Miro's OAuth documentation](https://developers.miro.com/docs/getting-started-with-oauth)。

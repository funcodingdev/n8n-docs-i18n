---
title: Philips Hue credentials
description: >-
  Philips Hue credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Philips Hue 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Philips Hue credentials
originalFilePath: integrations/builtin/credentials/philipshue.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/philipshue'
url: 'https://docs.n8n.io/integrations/builtin/credentials/philipshue'
layout:
  description:
    visible: false
---

# Philips Hue credentials <a href="#philips-hue-credentials" id="philips-hue-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Philips Hue](../app-nodes/n8n-nodes-base.philipshue.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Philips Hue](https://www.philips-hue.com/en-us) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Philips Hue's CLIP API documentation](https://developers.meethue.com/develop/hue-api-v2/api-reference/)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你使用内置 OAuth connection，则无需输入 **APP ID**。

如果你需要从头配置 OAuth2，你需要一个 [Philips Hue developer](https://developers.meethue.com/) 账号。

在 [Add new Hue Remote API app](https://developers.meethue.com/add-new-hue-remote-api-app/) page 上创建新的 remote app。

为你的 app 使用这些设置：

- 从 n8n 复制 **OAuth Callback URL**，并将其添加为 **Callback URL**。
- 复制 **AppId**、**ClientId** 和 **ClientSecret**，并将它们输入到 n8n 中对应的字段。

---
title: ClickUp credentials
description: >-
  ClickUp credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 ClickUp。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: ClickUp credentials
originalFilePath: integrations/builtin/credentials/clickup.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/clickup'
url: 'https://docs.n8n.io/integrations/builtin/credentials/clickup'
layout:
  description:
    visible: false
---

# ClickUp credentials <a href="#clickup-credentials" id="clickup-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [ClickUp](../app-nodes/n8n-nodes-base.clickup.md)
- [ClickUp Trigger](../trigger-nodes/n8n-nodes-base.clickuptrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [ClickUp 的文档](https://clickup.com/api/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [ClickUp](https://www.clickup.com/) 账号，以及：

- 一个 Personal API **Access Token**

获取 personal API token：

1. 如果你使用 ClickUp 2.0，请选择左下角的头像并选择 **Apps**。如果你使用 ClickUp 3.0，请选择右上角的头像，选择 **Settings**，然后向下滚动并在侧边栏中选择 **Apps**。
2. 在 **API Token** 下，选择 **Generate**。
3. 复制你的 **Personal API token**，并在 n8n credential 中将其输入为 **Access Token**。

有关更多信息，请参阅 [ClickUp Personal Token 文档](https://clickup.com/api/developer-portal/authentication#personal-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要创建一个 OAuth app：

1. 在 ClickUp 中，选择你的头像并选择 **Integrations**。
2. 选择 **ClickUp API**。
3. 选择 **Create an App**。
4. 为你的 app 输入 **Name**。
5. 在 n8n 中复制 **OAuth Redirect URL**。将其作为 ClickUp app 的 **Redirect URL** 输入。
6. 创建 app 后，复制 **client_id** 和 **secret**，并将它们输入到 n8n credential 中。
7. 选择 **Connect my account**，并按照屏幕提示完成 credential 连接。

有关更多信息，请参阅 [ClickUp Oauth flow 文档](https://clickup.com/api/developer-portal/authentication#oauth-flow)。

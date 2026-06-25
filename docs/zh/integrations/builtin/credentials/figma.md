---
title: Figma credentials
description: >-
  Figma credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Figma。
contentType:
  - integration
  - reference
nodeTitle: Figma credentials
originalFilePath: integrations/builtin/credentials/figma.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/figma'
url: 'https://docs.n8n.io/integrations/builtin/credentials/figma'
layout:
  description:
    visible: false
---

# Figma credentials <a href="#figma-credentials" id="figma-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [Figma Trigger (Beta)](../trigger-nodes/n8n-nodes-base.figmatrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Figma](https://www.figma.com/) 账号。你需要 admin 或 owner 级别的账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- Access token
- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Figma 的 API 文档](https://www.figma.com/developers/api)。

## 使用 Access token <a href="#using-access-token" id="using-access-token"></a>

要配置此 credential，你需要：

- 一个 Personal **Access Token** (PAT)：有关生成 Personal **Access Token** 的说明，请参阅 [Figma API Access Tokens 文档](https://www.figma.com/developers/api#access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要一个 [Figma](https://www.figma.com/) 账号。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要注册 application 来设置 OAuth：

1. 打开 Figma [developer apps](https://www.figma.com/developers/apps) 页面。
2. 选择 **Create a new app**。
3. 为你的 app 输入 **Name**，例如 `n8n integration`。
4. 在 n8n 中复制 **OAuth Redirect URL**。
5. 在 Figma 中，选择 **Add a callback** 并输入你从 n8n 复制的 URL。
6. 保存 app。
7. 从 Figma 复制 **Client ID**，并将其输入到 n8n credential 中。
8. 从 Figma 复制 **Client Secret**，并将其输入到 n8n credential 中。

有关更多信息，请参阅 [Figma OAuth 文档](https://www.figma.com/developers/api#oauth2)。

## 设置 custom scopes <a href="#setting-custom-scopes" id="setting-custom-scopes"></a>

Figma OAuth2 credentials 默认使用以下 scopes：

* `webhooks:read`
* `webhooks:write`

如需为 credentials 选择不同 scopes，请启用 **Custom Scopes** slider 并编辑 **Enabled Scopes** 列表。请注意，使用更严格的 scopes 时，部分功能可能无法按预期工作。有关可用 scopes 的完整列表，请参阅 [Figma OAuth scopes](https://developers.figma.com/docs/rest-api/scopes/)。

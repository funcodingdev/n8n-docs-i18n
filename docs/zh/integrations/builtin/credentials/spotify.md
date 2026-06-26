---
title: Spotify credentials
description: >-
  Spotify credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Spotify 进行身份验证。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Spotify credentials
originalFilePath: integrations/builtin/credentials/spotify.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/spotify'
url: 'https://docs.n8n.io/integrations/builtin/credentials/spotify'
layout:
  description:
    visible: false
---

# Spotify credentials <a href="#spotify-credentials" id="spotify-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Spotify](../app-nodes/n8n-nodes-base.spotify.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Spotify's Web API documentation](https://developer.spotify.com/documentation/web-api)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你正在 [self-hosting](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，你需要一个 [Spotify Developer](https://developer.spotify.com/) 账号，以便创建 Spotify app：

1. 打开 [Spotify developer dashboard](https://developer.spotify.com/dashboard)。
2. 选择 **Create an app**。
3. 输入 **App name**，例如 `n8n integration`。
4. 输入 **App description**。
5. 从 n8n 复制 **OAuth Redirect URL**，并将其作为 **Redirect URI** 输入到你的 Spotify app 中。
6. 勾选复选框，同意 Spotify Terms of Service 和 Branding Guidelines。
7. 选择 **Create**。**App overview** 页面会打开。
8. 复制 **Client ID**，并将其输入到你的 n8n credential。
9. 复制 **Client Secret**，并将其输入到你的 n8n credential。
10. 选择 **Connect my account**，并按照屏幕提示完成 credential 授权。

更多信息请参考 [Spotify Apps](https://developer.spotify.com/documentation/web-api/concepts/apps)。

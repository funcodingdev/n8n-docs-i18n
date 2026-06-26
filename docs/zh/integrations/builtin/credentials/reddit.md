---
title: Reddit credentials
description: >-
  Reddit credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Reddit 进行身份验证。
contentType:
  - integration
  - reference
nodeTitle: Reddit credentials
originalFilePath: integrations/builtin/credentials/reddit.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/reddit'
url: 'https://docs.n8n.io/integrations/builtin/credentials/reddit'
layout:
  description:
    visible: false
---

# Reddit credentials <a href="#reddit-credentials" id="reddit-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Reddit](../app-nodes/n8n-nodes-base.reddit.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Reddit](https://reddit.com/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- OAuth2

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Reddit's developer documentation](https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

- 一个 **Client ID**
- 一个 **Client Secret**

{% hint style="warning" %}
**API access requires pre-approval**

Reddit 在 2025 年 11 月关闭了 public data API 的 self-service access。现在，你必须先获得 Reddit 的人工批准，才能创建新的 apps。请查看 Reddit 的 [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)，并通过 [Reddit's Developer Support form](https://support.reddithelp.com/hc/en-us/requests/new?ticket_form_id=14868593862164) 提交 request。
{% endhint %}

获得批准后，创建一个 [third-party app](https://www.reddit.com/prefs/apps)。访问前面的链接，或前往你的 **profile > Settings > Privacy > Third-party app authorizations > are you a developer? create an app**，并使用这些设置：

- 从 n8n 复制 **OAuth Callback URL**，并将其用作 app 的 **redirect uri**。
- app 的 client ID 显示在 app name 下方。复制它，并将其添加为你的 n8n **Client ID**。
- 复制 app 的 **secret**，并将其添加为你的 n8n **Client Secret**。

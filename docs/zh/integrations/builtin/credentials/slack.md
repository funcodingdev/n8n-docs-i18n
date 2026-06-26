---
title: Slack credentials
description: >-
  Slack credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Slack 进行身份验证。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Slack credentials
originalFilePath: integrations/builtin/credentials/slack.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/slack'
url: 'https://docs.n8n.io/integrations/builtin/credentials/slack'
layout:
  description:
    visible: false
---

# Slack credentials <a href="#slack-credentials" id="slack-credentials"></a>

你可以使用这些 credentials 对以下 nodes 进行身份验证：

- [Slack](../app-nodes/n8n-nodes-base.slack.md)
- [Slack Trigger](../trigger-nodes/n8n-nodes-base.slacktrigger.md)

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token：
    - [Slack Trigger](../trigger-nodes/n8n-nodes-base.slacktrigger.md) node 需要此方式。
    - 可用于 [Slack](../app-nodes/n8n-nodes-base.slack.md) node，但不推荐。
- OAuth2：
    - [Slack](../app-nodes/n8n-nodes-base.slack.md) node 的推荐方式。
    - 不适用于 [Slack Trigger](../trigger-nodes/n8n-nodes-base.slacktrigger.md) node。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Slack's API documentation](https://api.slack.com/apis)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [Slack](https://slack.com/) 账号，以及：

- 一个 **Access Token**

要生成 access token，请创建一个 Slack app：

1. 打开你的 [Slack API Apps](https://api.slack.com/apps) 页面。
2. 选择 **Create New App > From scratch**。
3. 输入 **App Name**。
4. 选择你将用于开发 app 的 **Workspace**。
5. 选择 **Create App**。app details 将打开。
6. 在左侧菜单的 **Features** 下，选择 **OAuth & Permissions**。
8. 在 **Scopes** 部分，为你的 app 选择适当的 scopes。推荐 scopes 列表请参考 [Scopes](#scopes)。
9. 添加 scopes 后，回到 **OAuth Tokens** 部分并选择 **Install to Workspace**。你必须是 Slack workspace admin 才能完成此操作。
10. 选择 **Allow**。
12. 复制 **Bot User OAuth Token**，并将其作为 **Access Token** 输入到你的 n8n credential 中。
13. 如果你将此 credential 用于 [Slack Trigger](../trigger-nodes/n8n-nodes-base.slacktrigger.md)，请按照 [Slack Trigger configuration](#slack-trigger-configuration) 中的步骤完成 app 设置。

更多信息请参考 Slack API [Quickstart](https://api.slack.com/quickstart)。

### Slack Trigger configuration <a href="#slack-trigger-configuration" id="slack-trigger-configuration"></a>

要将你的 Slack app 与 [Slack Trigger](../trigger-nodes/n8n-nodes-base.slacktrigger.md) node 配合使用：

1. 在 Slack 中前往 [Your Apps](https://api.slack.com/apps/)，并选择要使用的 app。
2. 前往 **Features** > **Event Subscriptions**。
3. 打开 **Enable Events** 控件。
4. 在 n8n 中复制 **Webhook URL**，并将其作为 **Request URL** 输入到你的 Slack app 中。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Request URL</strong></p><p>Slack 每个 app 只允许一个 request URL。如果你想测试 workflow，需要使用以下方式之一：</p><ul><li>先使用你的 <strong>Test URL</strong> 测试，确认一切正常后，再将 Slack app 改为使用 <strong>Production URL</strong></li><li>使用带 execution logging 的 <strong>Production URL</strong>。</li></ul></div>

5. 验证后，选择要订阅的 bot events。使用 n8n 中的 **Trigger on** 字段过滤这些请求。
    - 要使用列表中没有的 event，请将其添加为 bot event，并在 n8n node 中选择 **Any Event**。

更多信息请参考 [Quickstart | Configuring the app for event listening](https://api.slack.com/quickstart#listening)。

n8n 建议为你的 Slack Trigger 启用 request signature verification，以增强安全性：

1. 在 Slack 中前往 [Your Apps](https://api.slack.com/apps/)，并选择要使用的 app。
2. 前往 **Settings** > **Basic Information**。
3. 复制 **Signing** 的值。
4. 在 n8n 中，将此值粘贴到 credential 的 **Signature Secret** 字段。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你正在 [self-hosting n8n](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)，并且需要从零开始配置 OAuth2，你需要一个 [Slack](https://slack.com/) 账号，以及：

- 一个 **Client ID**
- 一个 **Client Secret**

要同时获取二者，请创建一个 Slack app：

1. 打开你的 [Slack API Apps](https://api.slack.com/apps) 页面。
2. 选择 **Create New App > From scratch**。
3. 输入 **App Name**。
4. 选择你将用于开发 app 的 **Workspace**。
5. 选择 **Create App**。app details 将打开。
6. 在 **Settings > Basic Information** 中，打开 **App Credentials** 部分。
7. 复制 **Client ID** 和 **Client Secret**。将它们粘贴到 n8n 中的对应字段。
6. 在左侧菜单的 **Features** 下，选择 **OAuth & Permissions**。
7. 在 **Redirect URLs** 部分，选择 **Add New Redirect URL**。
8. 从 n8n 复制 **OAuth Callback URL**，并将其作为新的 Redirect URL 输入到 Slack。
9. 选择 **Add**。
10. 选择 **Save URLs**。
11. 在 **Scopes** 部分，为你的 app 选择适当的 scopes。scopes 列表请参考 [Scopes](#scopes)。
13. 添加 scopes 后，回到 **OAuth Tokens** 部分并选择 **Install to Workspace**。你必须是 Slack workspace admin 才能完成此操作。
14. 选择 **Allow**。
15. 此时，你应该可以在 n8n credential 中选择 OAuth 按钮进行连接。

更多信息请参考 Slack API [Quickstart](https://api.slack.com/quickstart)。有关 OAuth flow 本身的更多细节，请参考 Slack [Installing with OAuth](https://api.slack.com/authentication/oauth-v2) 文档。

## Scopes <a href="#scopes" id="scopes"></a>

Scopes 决定 app 拥有哪些 permissions。

* 如果你希望 app 代表授权该 app 的用户执行操作，请在 **User Token Scopes** 部分添加所需 scopes。
* 如果你正在构建 bot，请在 **Bot Token Scopes** 部分添加所需 scopes。

下面是 OAuth credential 需要的 scopes 列表，可作为良好的起点：

| **Scope name**        | **Notes** |
|-----------------------| -- |
| `channels:read`       | |
| `channels:write`      | 不能作为 bot token scope 使用 |
| `channels:history`    | |
| `chat:write`          | |
| `files:read`          | |
| `files:write`         | |
| `groups:read`         | |
| `groups:history`      | |
| `im:read`             | |
| `im:history`          | |
| `mpim:read`           | |
| `mpim:history`        | |
| `reactions:read`      | |
| `reactions:write`     | |
| `stars:read`          | 不能作为 bot token scope 使用 |
| `stars:write`         | 不能作为 bot token scope 使用 |
| `usergroups:read`     | |
| `usergroups:write`    | |
| `users.profile:read`  | |
| `users.profile:write` | 不能作为 bot token scope 使用 |
| `users:read`          | |
| `search:read`         | |

## 常见问题 <a href="#common-issues" id="common-issues"></a>

### Token expired <a href="#token-expired" id="token-expired"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/aLQxqepKmNn7Oz3PDTB7/" %}

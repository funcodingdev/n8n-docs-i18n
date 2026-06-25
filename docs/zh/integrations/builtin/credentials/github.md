---
title: GitHub credentials
description: >-
  GitHub credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 GitHub。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: GitHub credentials
originalFilePath: integrations/builtin/credentials/github.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/github'
url: 'https://docs.n8n.io/integrations/builtin/credentials/github'
layout:
  description:
    visible: false
---

# GitHub credentials <a href="#github-credentials" id="github-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [GitHub](../app-nodes/n8n-nodes-base.github.md)
- [GitHub Trigger](../trigger-nodes/n8n-nodes-base.githubtrigger.md)
- [GitHub Document Loader](../cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)：此 node 不支持 OAuth。

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [GitHub](https://github.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token：此方法可用于任意 GitHub nodes。
- OAuth2：此方法仅用于 [GitHub](../app-nodes/n8n-nodes-base.github.md) 和 [GitHub Trigger](../trigger-nodes/n8n-nodes-base.githubtrigger.md) nodes；不要用于 [GitHub Document Loader](../cluster-nodes/sub-nodes/n8n-nodes-langchain.documentgithubloader.md)。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GitHub 的 API 文档](https://docs.github.com/en/rest)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [GitHub](https://github.com/) 账号。

设置此 credential 有两个步骤：

1. [生成 GitHub personal access token](#generate-personal-access-token)。
2. [设置 credential](#set-up-the-credential)。

请参阅下方各节获取详细说明。

### 生成 personal access token <a href="#generate-personal-access-token" id="generate-personal-access-token"></a>

{% hint style="info" %}
**推荐的 access token 类型**

n8n 建议使用 personal access token (classic)。GitHub fine-grained personal access tokens 仍处于 beta，且无法访问所有 endpoints。
{% endhint %}

生成 personal access token：

1. 如果尚未完成，请使用 GitHub 验证你的 email address。有关更多信息，请参阅 [Verifying your email address](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/verifying-your-email-address)。
2. 打开 GitHub profile [Settings](https://github.com/settings/profile)。
3. 在左侧导航中，选择 [**Developer settings**](https://github.com/settings/apps)。
4. 在左侧导航的 **Personal access tokens** 下，选择 **Tokens (classic)**。
5. 选择 **Generate new token > Generate new token (classic)**。
6. 在 **Note** 字段中为 token 输入描述性名称，例如 `n8n integration`。
7. 选择你希望 token 使用的 **Expiration**，或选择 **No expiration**。
8. 为 token 选择 **Scopes**。对于大多数 n8n GitHub nodes，请添加 `repo` scope。
    - 未分配 scopes 的 token 只能访问 public information。
9. 选择 **Generate token**。
10. 复制 token。

有关更多信息，请参阅 [Creating a personal access token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)。有关 GitHub scopes 的更多信息，请参阅 [Scopes for OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps#available-scopes)。

### 设置 credential <a href="#set-up-the-credential" id="set-up-the-credential"></a>

然后，在 n8n credential 中：

1. 如果你没有使用 GitHub Enterprise Server，请不要更改 **GitHub server** URL。
    - 如果你使用 [GitHub Enterprise Server](https://docs.github.com/en/enterprise-server@3.9/admin/overview/about-github-enterprise-server)，请更新 **GitHub server** 以匹配你的 server URL。
2. 输入你的 GitHub profile 中显示的 **User** name。
3. 输入上方生成的 **Access Token**。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管 n8n](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)，请创建一个新的 GitHub [OAuth app](https://docs.github.com/en/apps/oauth-apps)：

1. 打开 GitHub profile [Settings](https://github.com/settings/profile)。
2. 在左侧导航中，选择 [**Developer settings**](https://github.com/settings/apps)。
3. 在左侧导航中，选择 **OAuth apps**。
4. 选择 **New OAuth App**。
    - 如果你之前未创建过 app，可能会看到 **Register a new application**。请选择它。
5. 输入 **Application name**，例如 `n8n integration`。
6. 输入 app website 的 **Homepage URL**。
7. 如有需要，添加可选的 **Application description**，GitHub 会向 end-users 显示。
8. 从 n8n 复制 **OAuth Redirect URL**，并将其粘贴到 GitHub **Authorization callback URL**。
9. 选择 **Register application**。
10. 复制生成的 **Client ID** 和 **Client Secret**，并将它们添加到 n8n credential 中。

有关 authorization process 的更多信息，请参阅 [GitHub Authorizing OAuth apps 文档](https://docs.github.com/en/apps/oauth-apps/using-oauth-apps/authorizing-oauth-apps)。

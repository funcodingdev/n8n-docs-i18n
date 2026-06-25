---
title: GitLab credentials
description: >-
  GitLab credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 GitLab。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: GitLab credentials
originalFilePath: integrations/builtin/credentials/gitlab.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/credentials/gitlab'
url: 'https://docs.n8n.io/integrations/builtin/credentials/gitlab'
layout:
  description:
    visible: false
---

# GitLab credentials <a href="#gitlab-credentials" id="gitlab-credentials"></a>

你可以使用这些 credentials 验证以下 nodes：

- [GitLab](../app-nodes/n8n-nodes-base.gitlab.md)
- [GitLab Trigger](../trigger-nodes/n8n-nodes-base.gitlabtrigger.md)

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

- API access token
- OAuth2（推荐）

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [GitLab 的 API 文档](https://docs.gitlab.com/ee/api/rest/)。

## 使用 API access token <a href="#using-api-access-token" id="using-api-access-token"></a>

要配置此 credential，你需要一个 [GitLab](https://gitlab.com/) 账号，以及：

- 你的 **GitLab Server** URL
- 一个 **Access Token**

设置 credential：

1. 在 GitLab 中，选择你的 avatar，然后选择 **Edit profile**。
2. 在左侧边栏中，选择 **Access tokens**。
3. 选择 **Add new token**。
4. 为 token 输入 **Name**，例如 `n8n integration`。
5. 输入 token 的 **expiry date**。如果不输入 expiry date，GitLab 会自动将其设置为当前日期 365 天后。
    - token 会在该 expiry date 的 UTC 午夜过期。
6. 选择所需 **Scopes**。对于 [GitLab](../app-nodes/n8n-nodes-base.gitlab.md) node，可使用 `api` scope 轻松授予 node 所有功能的访问权限。也可以参阅 [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)，为你想使用的 functions 选择 scopes。
7. 选择 **Create personal access token**。
8. 复制创建出的 access token，并在 n8n credential 中将其输入为 **Access Token**。
9. 在 n8n credential 中输入你的 **GitLab Server** URL。

有关更多信息，请参阅 GitLab 的 [Create a personal access token 文档](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n) n8n，需要一个 [GitLab](https://gitlab.com/) 账号。然后创建新的 GitLab application：

1. 在 GitLab 中，选择你的 avatar，然后选择 **Edit profile**。
2. 在左侧边栏中，选择 **Applications**。
3. 选择 **Add new application**。
4. 为 application 输入 **Name**，例如 `n8n integration`。
5. 在 n8n 中复制 **OAuth Redirect URL**。将其输入为 GitLab **Redirect URI**。
6. 选择所需 **Scopes**。对于 [GitLab](../app-nodes/n8n-nodes-base.gitlab.md) node，可使用 `api` scope 轻松授予 node 所有功能的访问权限。也可以参阅 [Personal access token scopes](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes)，为你想使用的 functions 选择 scopes。
6. 选择 **Save application**。
7. 复制 **Application ID**，并在 n8n credential 中将其输入为 **Client ID**。
8. 复制 **Secret**，并在 n8n credential 中将其输入为 **Client Secret**。

有关更多信息，请参阅 GitLab 的 [Configure GitLab as an OAuth 2.0 authentication identity provider](https://docs.gitlab.com/ee/integration/oauth_provider.html) 文档。有关 OAuth2 和 GitLab 的更多信息，请参阅 [GitLab OAuth 2.0 identity provider API 文档](https://docs.gitlab.com/ee/api/oauth2.html)。

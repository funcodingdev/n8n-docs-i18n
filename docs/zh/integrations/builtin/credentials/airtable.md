---
title: Airtable credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Airtable credentials
originalFilePath: integrations/builtin/credentials/airtable.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/airtable
url: https://docs.n8n.io/integrations/builtin/credentials/airtable
description: >-
  Airtable credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Airtable。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Airtable credentials

你可以使用这些 credentials 验证以下 nodes：

* [Airtable](../app-nodes/n8n-nodes-base.airtable/)
* [Airtable Trigger](../trigger-nodes/n8n-nodes-base.airtabletrigger.md)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Airtable](https://airtable.com/) 账号。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Personal Access Token (PAT)
* OAuth2

{% hint style="info" %}
**API Key 已弃用**

n8n 过去为 Airtable 提供 API key 身份验证方法。Airtable 已在 2024 年 2 月[完全弃用这些 keys](https://support.airtable.com/v1/docs/airtable-api-deprecation-guidelines)。如果你之前使用 Airtable API credential，请将其替换为 Airtable Personal Access Token 或 Airtable OAuth2 credential。n8n 推荐改用 Personal Access Token。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Airtable 的 API 文档](https://airtable.com/developers/web/api/authentication)。

## 使用 personal access token <a href="#using-personal-access-token" id="using-personal-access-token"></a>

要配置此 credential，你需要：

* 一个 Personal **Access Token** (PAT)

创建 PAT：

1. 前往 Airtable Builder Hub 的 [Personal access tokens](https://airtable.com/create/tokens) 页面。
2. 选择 **+ Create new token**。Airtable 会打开 **Create personal access token** 页面。
3. 为你的 token 输入 **Name**，例如 `n8n credential`。
4. 为 token 添加 **Scopes**。有关更多信息，请参阅 Airtable 的 [Scopes](https://airtable.com/developers/web/api/scopes) 指南。n8n 推荐使用以下 scopes：
   * `data.records:read`
   * `data.records:write`
   * `schema.bases:read`
5. 选择 token 的 **Access**。你可以选择单个 base、多个 bases（即使来自不同 workspace）、你拥有的某个 workspace 中当前和未来的所有 bases，或你拥有的任何 workspace 中的所有 bases，包括未来新增的 base/workspace。
6. 选择 **Create token**。
7. Airtable 会打开一个显示 token 的模态框。复制此 token，并在 n8n credential 中将其输入为 **Access Token**。

有关更多信息，请参阅 Airtable 的 [Find/create PATs 文档](https://support.airtable.com/v1/docs/creating-personal-access-tokens)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/HoGXnGIfupVt81dGox48/" %}

如果你在[自托管 n8n](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n)，你需要：

* 一个 **OAuth Redirect URL**
* 一个 **Client ID**
* 一个 **Client Secret**

要生成这些信息，请注册一个新的 Airtable integration：

1. 打开 Airtable Builder Hub 的 [**OAuth integrations**](https://airtable.com/create/oauth) 页面。
2. 选择 **Register new OAuth integration** 按钮。
3. 为你的 OAuth integration 输入名称。
4. 从 n8n credential 复制 **OAuth Redirect URL**。
5. 在 Airtable 中将该 redirect URL 粘贴为 **OAuth redirect URL**。
6. 选择 **Register integration**。
7. 在下一页，从 Airtable 复制 **Client ID**，并将其粘贴到 n8n credential 的 **Client ID** 中。
8. 在 Airtable 中，选择 **Generate client secret**。
9. 复制 client secret，并将其粘贴到 n8n credential 的 **Client Secret** 中。
10. 在 Airtable 中选择以下 scopes：
    * `data.records:read`
    * `data.records:write`
    * `schema.bases:read`
11. 在 Airtable 中选择 **Save changes**。
12. 在 n8n credential 中选择 **Connect my account**。会打开一个 **Grant access** 模态框。
13. 按照说明操作，并选择你想要使用的 base（或所有 bases）。
14. 选择 **Grant access** 完成连接。

有关注册新 OAuth integration 的步骤，请参阅 [Airtable Register a new integration 文档](https://airtable.com/developers/web/guides/oauth-integrations)。

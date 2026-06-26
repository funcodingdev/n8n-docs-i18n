---
title: Notion credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Notion credentials
originalFilePath: integrations/builtin/credentials/notion.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/notion
url: https://docs.n8n.io/integrations/builtin/credentials/notion
description: >-
  Notion credentials 文档。使用这些 credentials 在 n8n 这个 workflow 自动化平台中对
  Notion 进行身份验证。
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

# Notion credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Notion](../app-nodes/n8n-nodes-base.notion/)
* [Notion Trigger](../trigger-nodes/n8n-nodes-base.notiontrigger.md)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个具有 admin level access 的 [Notion](https://notion.so) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API integration token：用于 internal integrations。
* OAuth2：用于 public integrations。

{% hint style="info" %}
**Integration type**

不确定该使用哪种 integration type？更多信息请参考下面的 [Internal vs. public integrations](notion.md#internal-vs-public-integrations)。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Notion's API documentation](https://developers.notion.com/reference/intro)。

## 使用 API integration token <a href="#using-api-integration-token" id="using-api-integration-token"></a>

要配置此 credential，你需要：

* 一个 **Internal Integration Secret**：创建 Notion integration 后生成。

要生成 integration secret，请[创建 Notion integration](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion)，并从 **Secrets** tab 获取 integration secret：

1. 前往你的 Notion [integration dashboard](https://www.notion.com/my-integrations)。
2. 选择 **+ New integration** button。
3. 为你的 integration 输入一个 **Name**，例如 `n8n integration`。如果需要，也可以添加 **Logo**。
4. 选择 **Submit** 创建你的 integration。
5. 打开 **Capabilities** tab。选择这些 capabilities：
   * `Read content`
   * `Update content`
   * `Insert content`
   * `User information without email addresses`
6. 务必选择 **Save changes**。
7. 选择 **Secrets** tab。
8. 复制 **Internal Integration Token**，并将它作为你的 n8n **Internal Integration Secret** 添加。

有关对该服务进行身份验证的更多信息，请参考 [Internal integration auth flow setup documentation](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up)。

### 与 integration 共享 Notion page(s) <a href="#share-notion-pages-with-the-integration" id="share-notion-pages-with-the-integration"></a>

要让你的 integration 与 Notion 交互，你必须[授予 integration page permission](https://developers.notion.com/docs/create-a-notion-integration#give-your-integration-page-permissions)，允许它与 Notion workspace 中的 page(s) 交互：

1. 访问你的 Notion workspace 中的 page。
2. 选择 page 右上角的 triple dot menu。
3. 在 **Connections** 中，选择 **Connect to**。
4. 使用 search bar 查找并从 dropdown list 中选择你的 integration。

与 integration 共享至少一个 page 后，你就可以开始发起 API requests。如果 page 未共享，发出的任何 API requests 都会返回 error。

更多信息请参考 [Integration permissions](https://developers.notion.com/docs/authorization#integration-permissions)。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

要配置此 credential，你需要：

* 一个 **Client ID**：配置 public integration 后生成。
* 一个 **Client Secret**：配置 public integration 后生成。

你必须[创建 Notion integration](https://developers.notion.com/docs/create-a-notion-integration#create-your-integration-in-notion)，并将其设置为 public distribution：

1. 前往你的 Notion [integration dashboard](https://www.notion.so/my-integrations)。
2. 选择 **+ New integration** button。
3. 为你的 integration 输入一个 **Name**，例如 `n8n integration`。如果需要，也可以添加 **Logo**。
4. 选择 **Submit** 创建你的 integration。
5. 打开 **Capabilities** tab。选择这些 capabilities：
   * `Read content`
   * `Update content`
   * `Insert content`
   * `User information without email addresses`
6. 选择 **Save changes**。
7. 前往 **Distribution** tab。
8. 打开 **Do you want to make this integration public?** control。
9. 在 **Organization Information** section 中输入你的 company name 和 website。
10. 复制 n8n **OAuth Redirect URL**，并将其作为 **Redirect URI** 添加到 Notion integration 的 **OAuth Domain & URLs** section。
11. 前往 **Secrets** tab。
12. 复制 **Client ID** 和 **Client Secret**，并将它们添加到你的 n8n credential。

有关对该服务进行身份验证的更多信息，请参考 Notion 的 [public integration auth flow setup](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up)。

## Internal vs. public integrations <a href="#internal-vs-public-integrations" id="internal-vs-public-integrations"></a>

**Internal** integrations：

* 特定于单个 workspace。
* 仅该 workspace 的 members 可以访问。
* 适合自定义 workspace enhancements。

Internal integrations 使用更简单的身份验证流程（integration secret），发布前无需 security review。

**Public** integrations：

* 可跨多个无关的 Notion workspaces 使用。
* 任何 Notion user 都可以访问，不受其 workspace 限制。
* 适合覆盖更广泛的 use cases。

Public integrations 使用 OAuth 2.0 protocol 进行身份验证。它们在发布前需要通过 Notion security review。

有关这两种 integration types 的更详细说明，请参考 Notion 的 [Internal vs. Public Integrations documentation](https://developers.notion.com/docs/getting-started#internal-vs-public-integrations)。

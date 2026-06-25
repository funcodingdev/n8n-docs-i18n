---
title: Discord credentials
contentType:
  - integration
  - reference
priority: high
nodeTitle: Discord credentials
originalFilePath: integrations/builtin/credentials/discord.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/discord
url: https://docs.n8n.io/integrations/builtin/credentials/discord
description: >-
  Discord credentials 文档。使用这些 credentials 在 n8n 这个 workflow automation
  platform 中验证 Discord。
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

# Discord credentials

你可以使用这些 credentials 验证以下 nodes：

* [Discord](../app-nodes/n8n-nodes-base.discord/)

## 前置条件 <a href="#prerequisites" id="prerequisites"></a>

* 创建一个 [Discord](https://www.discord.com/) 账号。
* 对于 Bot 和 OAuth2 credentials：
  * [设置本地 developer environment](https://discord.com/developers/docs/quick-start/getting-started#step-0-project-setup)。
  * [创建 application 和 bot user](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app)。
* 对于 webhook credentials，请[创建 webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)。

## 支持的身份验证方法 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* Bot
* OAuth2
* Webhook

不确定使用哪种方法？请参阅[选择身份验证方法](discord.md#choose-an-authentication-method)获取更多指导。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Discord Developer 文档](https://discord.com/developers/docs/intro)。

## 使用 bot <a href="#using-bot" id="using-bot"></a>

如果你想使用 bot token 而不是 OAuth2 将 bot 添加到 Discord server，请使用此方法。

要配置此 credential，你需要：

* 一个 **Bot Token**：创建带 bot 的 application 后生成。

创建带 bot 的 application 并生成 **Bot Token**：

1. 如果还没有 app，请在 [developer portal](https://discord.com/developers/applications?new_application=true) 中创建一个 app。
2. 为你的 app 输入 **Name**。
3. 选择 **Create**。
4. 从左侧菜单选择 **Bot**。
5. 在 **Token** 下，选择 **Reset Token** 生成新的 bot token。
6. 复制 token 并添加到 n8n credential 中。
7. 在 **Bot > Privileged Gateway Intents** 中，添加你希望 bot 拥有的 privileged intents。有关 privileged intents 的更多信息，请参阅 [Configuring your bot](https://discord.com/developers/docs/quick-start/getting-started#configuring-your-bot)。
   * n8n 建议启用 **SERVER MEMBERS INTENT: Required for your bot to receive events listed under GUILD\_MEMBERS**。
8. 在 **Installation > Installation Contexts** 中，选择你希望 bot 使用的 installation contexts：
   * 对于安装到 server 的 apps，选择 **Guild Install**。（n8n 用户最常见。）
   * 对于安装到 user 的 apps，选择 **User Install**。（n8n 用户较少见，但可能适合测试。）
   * 有关这些 installation contexts 的更多信息，请参阅 Discord 的 [Choosing installation contexts](https://discord.com/developers/docs/quick-start/getting-started#choosing-installation-contexts) 文档。
9. 在 **Installation > Install Link** 中，如果尚未选择，请选择 **Discord Provided Link**。
10. 仍在 **Installation** 页面中，在 **Default Install Settings** 区域选择 `applications.commands` 和 `bot` scopes。有关这些和其他 scopes 的更多信息，请参阅 Discord 的 [Scopes](https://discord.com/developers/docs/topics/oauth2#shared-resources-oauth2-scopes) 文档。
11. 在 **Bot > Bot Permissions** 页面添加 permissions。有关更多信息，请参阅 Discord 的 [Permissions](https://discord.com/developers/docs/topics/permissions) 文档。n8n 建议为 [Discord](../app-nodes/n8n-nodes-base.discord/) node 选择以下 permissions：
    * Manage Roles
    * Manage Channels
    * Read Messages/View Channels
    * Send Messages
    * Create Public Threads
    * Create Private Threads
    * Send Messages in Threads
    * Send TTS Messages
    * Manage Messages
    * Manage Threads
    * Embed Links
    * Attach Files
    * Read Message History
    * Add Reactions
12. 将 app 添加到你的 server 或 test server：
    1. 前往 **Installation > Install Link** 并复制那里列出的 link。
    2. 将 link 粘贴到浏览器中并按 Enter。
    3. 在 installation prompt 中选择 **Add to server**。
    4. app 添加到 server 后，你会在 member list 中看到它。

这些步骤概述了设置 n8n credential 所需的基本功能。有关创建 app 的更多信息，请参阅 [Discord Creating an App](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app) 指南，尤其是：

* [Fetching your credentials](https://discord.com/developers/docs/quick-start/getting-started#fetching-your-credentials)：用于将 app credentials 放入本地 developer environment。
* [Handling interactivity](https://discord.com/developers/docs/quick-start/getting-started#step-3-handling-interactivity)：用于了解如何为交互式 `/slash` commands 设置 public endpoints。

## 使用 OAuth2 <a href="#using-oauth2" id="using-oauth2"></a>

如果你想使用 OAuth2 flow 将 bot 添加到 Discord servers，请使用此方法；它能简化安装 app 的用户的流程。

要配置此 credential，你需要：

* 一个 **Client ID**
* 一个 **Client Secret**
* 选择将 **Authentication** 发送到 **Header** 还是 **Body**
* 一个 **Bot Token**

有关创建带 bot 的 application 和生成 token 的细节，请按照上方[使用 bot](discord.md#using-bot)中的相同步骤操作。

然后：

1. 复制你生成的 **Bot Token**，并将其添加到 n8n credential 中。
2. 打开 Discord application 中的 **OAuth2** 页面，访问你的 **Client ID** 并生成 **Client Secret**。将它们添加到 n8n credential 中。
3. 从 n8n 复制 **OAuth Redirect URL**，并将其添加到 Discord application 的 **OAuth2 > Redirects** 中。确保保存这些更改。

## 使用 webhook <a href="#using-webhook" id="using-webhook"></a>

要配置此 credential，你需要：

* 一个 **Webhook URL**：创建 webhook 后生成。

要获取 Webhook URL，请创建 webhook 并复制生成的 URL：

1. 打开 Discord **Server Settings**，并打开 **Integrations** 选项卡。
2. 选择 **Create Webhook** 创建新的 webhook。
3. 为 webhook 设置有意义的 **Name**。
4. 选择 **Name** 旁边的 **avatar**，编辑或上传新的 avatar。
5. 在 **CHANNEL** dropdown 中，选择 webhook 应该发布到的 channel。
6. 选择 **Copy Webhook URL** 复制 Webhook URL。将此 URL 输入到 n8n credential 中。

有关更多信息，请参阅 [Discord Making a Webhook 文档](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)。

## 选择身份验证方法 <a href="#choose-an-authentication-method" id="choose-an-authentication-method"></a>

最简单的安装方式是 **webhook**。你可以创建 webhooks，并将其添加到 Discord server 的单个 channel。Webhooks 可以向 channel 发布 messages。它们不需要 bot user 或 authentication。但它们不能监听或响应 user requests 或 commands。如果你需要一种无需交互或反馈即可向 channel 发送 messages 的直接方式，请使用 webhook。

**bot** 是比 webhook 更具交互性的方案。你可以将 bots 添加到 Discord server（在 Discord API 文档中称为 `guild`）或 user accounts。添加到 server 的 bots 可以与 server 所有 channels 中的 users 交互。它们可以管理 channels、发送和检索 messages、检索所有 users 的列表，并更改他们的 roles。如果你需要构建交互式、复杂或多步骤 workflow，请使用 bot。

**OAuth2** 基本上是使用 OAuth2 flow 而不只是 bot token 的 **bot**。和 bots 一样，你可以将它们添加到 Discord server 或 user accounts。这些 credentials 提供与 bots 相同的功能，但可以简化在 server 上安装 bot 的流程。

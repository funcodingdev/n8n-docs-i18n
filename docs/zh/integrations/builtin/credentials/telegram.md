---
title: Telegram credentials
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram credentials
originalFilePath: integrations/builtin/credentials/telegram.md
originalUrl: https://docs.n8n.io/integrations/builtin/credentials/telegram
url: https://docs.n8n.io/integrations/builtin/credentials/telegram
description: >-
  Telegram credentials 文档。使用这些 credentials 在 n8n 这个 workflow
  自动化平台中对 Telegram 进行身份验证。
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

# Telegram credentials

你可以使用这些 credentials 对以下 nodes 进行身份验证：

* [Telegram](../app-nodes/n8n-nodes-base.telegram/)
* [Telegram Trigger](../trigger-nodes/n8n-nodes-base.telegramtrigger/)

## 前提条件 <a href="#prerequisites" id="prerequisites"></a>

创建一个 [Telegram](https://telegram.org/) 账号。

## 支持的身份验证方式 <a href="#supported-authentication-methods" id="supported-authentication-methods"></a>

* API bot access token

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参考 [Telegram's Bot API documentation](https://core.telegram.org/bots/api)。

有关创建和使用 bots 的更多信息，请参考 [Telegram Bot Features](https://core.telegram.org/bots/features) 文档。

## 使用 API bot access token <a href="#using-api-bot-access-token" id="using-api-bot-access-token"></a>

要配置此 credential，你需要：

* 一个 bot **Access Token**

要生成你的 access token：

1. 与 [BotFather](https://telegram.me/BotFather) 开始聊天。
2. 输入 `/newbot` command 创建一个新 bot。
3. BotFather 会要求你为新 bot 提供 name 和 username：
   * **name** 是显示在 contact details 和其他位置的 bot 名称。你稍后可以更改 bot name。
   * **username** 是用于 search、mentions 和 t.me links 的短名称。创建 username 时请遵循以下规则：
     * 长度必须在 5 到 32 个字符之间。
     * 不区分大小写。
     * 只能包含拉丁字符、数字和下划线。
     * 必须以 `bot` 结尾，例如 `tetris_bot` 或 `TetrisBot`。
     * 之后不能更改 username。
4. 复制 BotFather 生成的 bot **token**，并将其作为 n8n 中的 **Access Token** 添加。

更多信息请参考 [BotFather Create a new bot documentation](https://core.telegram.org/bots/features#creating-a-new-bot)。

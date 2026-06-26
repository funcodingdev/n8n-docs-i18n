---
title: Telegram node common issues
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues
description: >-
  n8n 中 Telegram node 的常见问题文档。包含问题详情和建议解决方案。
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

# Common issues

这里列出 [Telegram node](./) 的一些常见错误和问题，以及解决或排查步骤。

## 将 bot 添加到 Telegram channel <a href="#add-a-bot-to-a-telegram-channel" id="add-a-bot-to-a-telegram-channel"></a>

要让 bot 向 channel 发送消息，你必须先将 bot 添加到该 channel。如果尚未将 bot 添加到 channel，你会看到类似如下描述的错误：`Error: Forbidden: bot is not a participant of the channel`。

要将 bot 添加到 channel：

1. 在 Telegram app 中，访问目标 channel 并选择 channel 名称。
2. 将 channel 名称标记为 **public channel**。
3. 选择 **Administrators** > **Add Admin**。
4. 搜索 bot 的 username 并选中它。
5. 选择右上角的勾选标记，将 bot 添加到 channel。

## 获取 Chat ID <a href="#get-the-chat-id" id="get-the-chat-id"></a>

你只能在 public channel 上使用 `@channelusername`。要与 Telegram group 交互，需要该 group 的 Chat ID。

有三种方式可以获取该 ID：

1. 从 Telegram Trigger 获取：在 workflow 中使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node 获取 Chat ID。此 node 可以由不同事件触发，并在执行成功时返回 Chat ID。
2. 从网页浏览器获取：在网页浏览器中打开 Telegram 并打开 group chat。group 的 Chat ID 是字母 "g" 后面的一串数字。在 n8n 中输入 group Chat ID 时，请在前面加上 `-`。
3. 邀请 Telegram 的 [@RawDataBot](https://t.me/RawDataBot) 加入 group：添加后，bot 会输出一个包含 `chat` 对象的 JSON 文件。该对象的 `id` 就是 group Chat ID。然后从 group 中移除 RawDataBot。

## 每秒发送超过 30 条消息 <a href="#send-more-than-30-messages-per-second" id="send-more-than-30-messages-per-second"></a>

Telegram API 有[限制](https://core.telegram.org/bots/faq#broadcasting-to-users)，每秒只能发送 30 条消息。按照以下步骤发送超过 30 条消息：

1. **Loop Over Items node**：使用 [Loop Over Items](../../core-nodes/n8n-nodes-base.splitinbatches.md) node 从数据库中最多获取 30 个 chat ID。
2. **Telegram node**：将 Telegram node 与 Loop Over Items node 连接。使用 **Expression Editor** 从 Loop Over Items node 中选择 Chat ID。
3. **Code node**：将 [Code](../../core-nodes/n8n-nodes-base.code/) node 与 Telegram node 连接。使用 Code node 等待几秒钟，再获取下一批 chat ID。将此 node 与 Loop Over Items node 连接。

你也可以使用这个 [workflow](https://n8n.io/workflows/772)。

## 从已发送消息中移除 n8n 署名 <a href="#remove-the-n8n-attribution-from-sent-messages" id="remove-the-n8n-attribution-from-sent-messages"></a>

如果你使用此 node [发送 Telegram 消息](message-operations.md#send-message)，消息末尾会自动追加 n8n 署名：

> This message was sent automatically with n8n

要移除此署名：

1. 在 node 的 **Additional Fields** 部分中，选择 **Add Field**。
2. 选择 **Append n8n attribution**。
3. 关闭 toggle。

有关更多信息，请参阅 [Send Message additional fields](message-operations.md#send-message-additional-fields)。

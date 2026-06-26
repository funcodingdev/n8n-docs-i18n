---
title: Telegram node documentation
contentType:
  - integration
  - reference
priority: critical
nodeTitle: n8n-nodes-base.telegram
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram
description: >-
  n8n 中 Telegram node 的文档。包含操作和配置详情，并提供示例与凭据相关链接。
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

# Telegram

使用 Telegram node 自动化 [Telegram](https://telegram.org/) 中的工作，并将 Telegram 与其他应用集成。n8n 内置支持大量 Telegram 功能，包括获取文件，以及删除和编辑消息。

在本页中，你可以找到 Telegram node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials 凭据**

有关身份验证设置指南，请参阅 [Telegram credentials](../../credentials/telegram.md)。
{% endhint %}

## Operations 操作 <a href="#operations" id="operations"></a>

* [**Chat** operations](chat-operations.md)
  * [**Get**](chat-operations.md#get-chat) chat 的最新信息。
  * [**Get Administrators**](chat-operations.md#get-administrators)：获取 chat 中所有管理员的列表。
  * [**Get Member**](chat-operations.md#get-chat-member)：获取 chat 成员详情。
  * [**Leave**](chat-operations.md#leave-chat) chat。
  * [**Set Description**](chat-operations.md#set-description) 设置 chat 描述。
  * [**Set Title**](chat-operations.md#set-title) 设置 chat 标题。
* [**Callback** operations](callback-operations.md)
  * [**Answer Query**](callback-operations.md#answer-query)：向 [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards) 发出的 callback query 发送回答。
  * [**Answer Inline Query**](callback-operations.md#answer-inline-query)：向 inline query 发出的 callback query 发送回答。
* [**File** operations](file-operations.md)
  * [**Get File**](file-operations.md#get-file) 从 Telegram 获取文件。
*   [**Message** operations](message-operations.md)<br>

    * [**Delete Chat Message**](message-operations.md#delete-chat-message)。
    * [**Edit Message Text**](message-operations.md#edit-message-text)：编辑已有消息的文本。
    * [**Pin Chat Message**](message-operations.md#pin-chat-message) 到 chat。
    * [**Send Animation**](message-operations.md#send-animation) 到 chat。
      * 用于最大 50 MB、无声音的 GIF 或 H.264/MPEG-4 AVC 视频。
    * [**Send Audio**](message-operations.md#send-audio) 文件到 chat，并在音乐播放器中显示。
    * [**Send Chat Action**](message-operations.md#send-chat-action)：告诉用户 bot 端正在发生某些事情。状态会设置 5 秒或更短时间。
    * [**Send Document**](message-operations.md#send-document) 到 chat。
    * [**Send Location**](message-operations.md#send-location)：向 chat 发送地理位置。
    * [**Send Media Group**](message-operations.md#send-media-group)：发送一组照片和/或视频。
    * [**Send Message**](message-operations.md#send-message) 到 chat。
    * [**Send Photo**](message-operations.md#send-photo) 到 chat。
    * [**Send Sticker**](message-operations.md#send-sticker) 到 chat。
      * 用于静态 .WEBP、动画 .TGS 或视频 .WEBM sticker。
    * [**Send Video**](message-operations.md#send-video) 到 chat。
    * [**Unpin Chat Message**](message-operations.md#unpin-chat-message) 从 chat 取消置顶。

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>将 bot 添加到 channel</strong></p><p>要使用大多数 <strong>Message</strong> operations，你必须将 bot 添加到 channel，使它可以向该 channel 发送消息。更多信息请参阅 <a href="common-issues.md#add-a-bot-to-a-telegram-channel">Common Issues | Add a bot to a Telegram channel</a>。</p></div>

    ## 模板和示例

[浏览 n8n-nodes-base.telegram 集成模板](https://n8n.io/integrations/telegram) 或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Telegram API 文档](https://core.telegram.org/bots/api)。

n8n 为 Telegram 提供了一个 trigger node。更多信息请参阅[这里](../../trigger-nodes/n8n-nodes-base.telegramtrigger/)的 trigger node 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见错误或问题以及建议解决步骤，请参阅[常见问题](common-issues.md)。

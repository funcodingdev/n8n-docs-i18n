---
title: Telegram node Chat operations documentation
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram node Chat operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations
description: >-
  n8n 中 Telegram node 的 Chat 操作文档。包含配置所有 Chat 操作的详情。
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

# Chat operations

使用这些操作获取 chat、成员、管理员相关信息，离开 chat，以及设置 chat 标题和描述。有关 Telegram node 本身的更多信息，请参阅 [Telegram](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Get Chat <a href="#get-chat" id="get-chat"></a>

使用此操作通过 Bot API [getChat](https://core.telegram.org/bots/api#getchat) method 获取 chat 的最新信息。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Get**。
* **Chat ID**：输入目标 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。

有关更多信息，请参阅 Telegram Bot API [getChat](https://core.telegram.org/bots/api#getchat) 文档。

## Get Administrators <a href="#get-administrators" id="get-administrators"></a>

使用此操作通过 Bot API [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators) method 获取 chat 中所有管理员的列表。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Get Administrators**。
* **Chat ID**：输入目标 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。

有关更多信息，请参阅 Telegram Bot API [getChatAdministrators](https://core.telegram.org/bots/api#getchatadministrators) 文档。

## Get Chat Member <a href="#get-chat-member" id="get-chat-member"></a>

使用此操作通过 Bot API [getChatMember](https://core.telegram.org/bots/api#getchatmember) method 获取 chat 成员详情。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Get Member**。
* **Chat ID**：输入目标 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **User ID**：输入要获取其信息的用户的唯一标识符。

有关更多信息，请参阅 Telegram Bot API [getChatMember](https://core.telegram.org/bots/api#getchatmember) 文档。

## Leave Chat <a href="#leave-chat" id="leave-chat"></a>

使用此操作通过 Bot API [leaveChat](https://core.telegram.org/bots/api#leavechat) method 离开 chat。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Leave**。
* **Chat ID**：输入你希望离开的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。

有关更多信息，请参阅 Telegram Bot API [leaveChat](https://core.telegram.org/bots/api#leavechat) 文档。

## Set Description <a href="#set-description" id="set-description"></a>

使用此操作通过 Bot API [setChatDescription](https://core.telegram.org/bots/api#setchatdescription) method 设置 chat 描述。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Set Description**。
* **Chat ID**：输入你希望设置描述的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Description**：输入要为 chat 设置的新描述，最多 255 个字符。

有关更多信息，请参阅 Telegram Bot API [setChatDescription](https://core.telegram.org/bots/api#setchatdescription) 文档。

## Set Title <a href="#set-title" id="set-title"></a>

使用此操作通过 Bot API [setChatTitle](https://core.telegram.org/bots/api#setchattitle) method 设置 chat 标题。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Chat**。
* **Operation**：选择 **Set Title**。
* **Chat ID**：输入你希望设置标题的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Title**：输入要为 chat 设置的新标题，最多 255 个字符。

有关更多信息，请参阅 Telegram Bot API [setChatTitle](https://core.telegram.org/bots/api#setchattitle) 文档。

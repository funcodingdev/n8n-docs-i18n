---
title: Telegram node Callback operations documentation
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram node Callback operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations
description: >-
  n8n 中 Telegram node 的 Callback 操作文档。包含配置所有 Callback 操作的详情。
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

# Callback operations

使用这些操作响应来自 in-line keyboard 或 in-line query 的 callback query。有关 Telegram node 本身的更多信息，请参阅 [Telegram](./)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Answer Query <a href="#answer-query" id="answer-query"></a>

使用此操作通过 Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) method，向 [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards) 发出的 callback query 发送回答。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Callback**。
* **Operation**：选择 **Answer Query**。
* **Query ID**：输入要回答的 query 的唯一标识符。
  * 要将 Query ID 直接传入此 node，请使用在 **Callback Query** 上触发的 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。
* **Results**：输入一个 JSON 序列化的结果数组，用作 query 的回答。有关数组格式的更多信息，请参阅 Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult) 文档。

有关更多信息，请参阅 Telegram Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) 文档。

### Answer Query additional fields <a href="#answer-query-additional-fields" id="answer-query-additional-fields"></a>

使用 **Additional Fields** 进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Cache Time**：输入客户端可缓存 callback query 结果的最长秒数。Telegram 对此 method 默认使用 `0` 秒。
* **Show Alert**：Telegram 可以将回答显示为 chat 屏幕顶部的通知，也可以显示为 alert。选择是保留默认通知显示（关闭），还是将回答显示为 alert（开启）。
* **Text**：如果希望回答显示文本，请在这里输入最多 200 个字符的文本。
* **URL**：输入一个 URL，用户的客户端将打开该 URL。有关更多信息，请参阅 Telegram Bot API [answerCallbackQuery](https://core.telegram.org/bots/api#answercallbackquery) 文档中的 **url** 参数说明。

## Answer Inline Query <a href="#answer-inline-query" id="answer-inline-query"></a>

使用此操作通过 Bot API [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery) method，向 inline query 发出的 callback query 发送回答。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Callback**。
* **Operation**：选择 **Answer Inline Query**。
* **Query ID**：输入要回答的 query 的唯一标识符。
  * 要将 Query ID 直接传入此 node，请使用在 **Inline Query** 上触发的 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。
* **Results**：输入一个 JSON 序列化的结果数组，用作 query 的回答。有关数组格式的更多信息，请参阅 Telegram [InlineQueryResults](https://core.telegram.org/bots/api#inlinequeryresult) 文档。

Telegram 每个 query 最多允许 50 个结果。

有关更多信息，请参阅 Telegram Bot API [answerInlineQuery](https://core.telegram.org/bots/api#answerinlinequery) 文档。

### Answer Inline Query additional fields <a href="#answer-inline-query-additional-fields" id="answer-inline-query-additional-fields"></a>

使用 **Additional Fields** 进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Cache Time**：客户端可缓存 callback query 结果的最长秒数。Telegram 对此 method 默认使用 `300` 秒。
* **Show Alert**：Telegram 可以将回答显示为 chat 屏幕顶部的通知，也可以显示为 alert。选择是保留默认通知显示（关闭），还是将回答显示为 alert（开启）。
* **Text**：如果希望回答显示文本，请在这里输入最多 200 个字符的文本。
* **URL**：输入用户客户端将打开的 URL。

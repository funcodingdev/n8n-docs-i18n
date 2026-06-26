---
title: Telegram node Message operations documentation
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram node Message operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations
description: >-
  n8n 中 Telegram node 的 Message 操作文档。包含配置所有 Message 操作的详情。
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

# Message operations

使用这些操作在 chat 中发送、编辑和删除消息；向 chat 发送文件；以及在 chat 中置顶或取消置顶消息。有关 Telegram node 本身的更多信息，请参阅 [Telegram](./)。

{% hint style="info" %}
**将 bot 添加到 channel**

要使用大多数此类操作，你必须将 bot 添加到 channel，使它可以向该 channel 发送消息。更多信息请参阅 [Common Issues | Add a bot to a Telegram channel](common-issues.md#add-a-bot-to-a-telegram-channel)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

## Delete Chat Message <a href="#delete-chat-message" id="delete-chat-message"></a>

使用此操作通过 Bot API [deleteMessage](https://core.telegram.org/bots/api#deletemessage) method 从 chat 删除消息。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Delete Chat Message**。
* **Chat ID**：输入要从中删除消息的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Message ID**：输入要删除的消息的唯一标识符。

有关更多信息，请参阅 Telegram Bot API [deleteMessage](https://core.telegram.org/bots/api#deletemessage) 文档。

## Edit Message Text <a href="#edit-message-text" id="edit-message-text"></a>

使用此操作通过 Bot API [editMessageText](https://core.telegram.org/bots/api#editmessagetext) method 编辑已有消息的文本。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Edit Message Text**。
* **Chat ID**：输入目标 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Message ID**：输入要编辑的消息的唯一标识符。
* **Reply Markup**：选择是否使用 **Inline Keyboard** 来显示 InlineKeyboardMarkup，或选择 **None** 不使用。这会设置 `reply_markup` 参数。有关更多信息，请参阅 [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) 文档。
* **Text**：输入要将消息编辑为的文本。

有关更多信息，请参阅 Telegram Bot API [editMessageText](https://core.telegram.org/bots/api#editmessagetext) 文档。

### Edit Message Text additional fields <a href="#edit-message-text-additional-fields" id="edit-message-text-additional-fields"></a>

使用 **Additional Fields** 进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Disable WebPage Preview**：选择是否为此消息中的链接启用 link preview（关闭），或禁用 link preview（开启）。这会为 `is_disabled` 设置 `link_preview_options` 参数。有关更多信息，请参阅 [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) 文档。
* **Parse Mode**：选择消息是否使用 **HTML**（默认）、**Markdown (Legacy)** 或 **MarkdownV2** 解析。这会设置 `parse_mode` 参数。

## Pin Chat Message <a href="#pin-chat-message" id="pin-chat-message"></a>

使用此操作通过 Bot API [pinChatMessage](https://core.telegram.org/bots/api#pinchatmessage) method 在 chat 中置顶消息。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Pin Chat Message**。
* **Chat ID**：输入要将消息置顶到的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Message ID**：输入要置顶的消息的唯一标识符。

有关更多信息，请参阅 Telegram Bot API [pinChatMessage](https://core.telegram.org/bots/api#pinchatmessage) 文档。

### Pin Chat Message additional fields <a href="#pin-chat-message-additional-fields" id="pin-chat-message-additional-fields"></a>

使用 **Additional Fields** 进一步细化 node 行为。选择 **Add Field** 可添加以下字段：

* **Disable Notifications**：默认情况下，Telegram 会通知所有 chat 成员该消息已被置顶。如果不想发送这些通知，请开启此控件。它会将 `disable_notification` 参数设置为 `true`。

## Send Animation <a href="#send-animation" id="send-animation"></a>

使用此操作通过 Bot API [sendAnimation](https://core.telegram.org/bots/api#sendanimation) method，向 chat 发送最大 50 MB、无声音的 GIF 或 H.264/MPEG-4 AVC 视频。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Animation**。
* **Chat ID**：输入要发送 animation 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Animation**：如果不使用 **Binary File**，请在这里输入要发送的 animation。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendAnimation](https://core.telegram.org/bots/api#sendanimation) 文档。

### Send Animation additional fields <a href="#send-animation-additional-fields" id="send-animation-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendAnimation method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Caption**：输入 animation 的 caption 文本，最多 1024 个字符。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Duration**：输入 animation 的时长，单位为秒。
* **Height**：输入 animation 的高度。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 Telegram 的 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。
* **Thumbnail**：添加所发送文件的 thumbnail。如果服务器端支持为文件生成 thumbnail，请忽略此字段。thumbnail 应符合以下规格：
  * JPEG 格式
  * 小于 200 KB
  * 宽和高小于 320px。
* **Width**：输入视频剪辑的宽度。

### Send Audio <a href="#send-audio" id="send-audio"></a>

使用此操作通过 Bot API [sendAudio](https://core.telegram.org/bots/api#sendaudio) method，向 chat 发送音频文件并在音乐播放器中显示。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Audio**。
* **Chat ID**：输入要发送 audio 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Audio**：如果不使用 **Binary File**，请在这里输入要发送的 audio。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendAudio](https://core.telegram.org/bots/api#sendaudio) 文档。

### Send Audio additional fields <a href="#send-audio-additional-fields" id="send-audio-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendAudio method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Caption**：输入 audio 的 caption 文本，最多 1024 个字符。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Duration**：输入 audio 的时长，单位为秒。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 Telegram 的 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Performer**：输入 performer 名称。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。
* **Title**：输入 audio track 名称。
* **Thumbnail**：添加所发送文件的 thumbnail。如果服务器端支持为文件生成 thumbnail，请忽略此字段。thumbnail 应符合以下规格：
  * JPEG 格式
  * 小于 200 KB
  * 宽和高小于 320px。

## Send Chat Action <a href="#send-chat-action" id="send-chat-action"></a>

当你需要告知用户 bot 端正在发生某些事情时，使用此操作。它会通过 Bot API [sendChatAction](https://core.telegram.org/bots/api#sendchataction) method 设置状态，持续 5 秒或更短时间。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Chat Action**。
* **Chat ID**：输入要发送 chat action 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Action**：选择要广播 bot 正在执行的动作。这里的选项包括：**Find Location**、**Typing**、**Recording** audio 或 video，以及 **Uploading** file types。

有关更多信息，请参阅 Telegram Bot API [sendChatAction](https://core.telegram.org/bots/api#sendchataction) 文档。

## Send Document <a href="#send-document" id="send-document"></a>

使用此操作通过 Bot API [sendDocument](https://core.telegram.org/bots/api#senddocument) method 向 chat 发送文档。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Document**。
* **Chat ID**：输入要发送 document 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Document**：如果不使用 **Binary File**，请在这里输入要发送的 document。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendDocument](https://core.telegram.org/bots/api#sendchataction) 文档。

### Send Document additional fields <a href="#send-document-additional-fields" id="send-document-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendDocument method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Caption**：输入文件的 caption 文本，最多 1024 个字符。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。
* **Thumbnail**：添加所发送文件的 thumbnail。如果服务器端支持为文件生成 thumbnail，请忽略此字段。thumbnail 应符合以下规格：
  * JPEG 格式
  * 小于 200 KB
  * 宽和高小于 320px。

## Send Location <a href="#send-location" id="send-location"></a>

使用此操作通过 Bot API [sendLocation](https://core.telegram.org/bots/api#sendlocation) method 向 chat 发送地理位置。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Location**。
* **Chat ID**：输入要发送 location 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Latitude**：输入 location 的纬度。
* **Longitude**：输入 location 的经度。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendLocation](https://core.telegram.org/bots/api#sendlocation) 文档。

### Send Location additional fields <a href="#send-location-additional-fields" id="send-location-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendLocation method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。

## Send Media Group <a href="#send-media-group" id="send-media-group"></a>

使用此操作通过 Bot API [sendMediaGroup](https://core.telegram.org/bots/api#sendmediagroup) method 发送一组照片和/或视频。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Media Group**。
* **Chat ID**：输入要发送 media group 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Media**：使用 **Add Media** 向 media group 添加不同媒体类型。对每个 media，选择：
  * **Type**：此 media 的类型。从 **Photo** 和 **Video** 中选择。
  * **Media File**：输入要发送的 media file。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
  * **Additional Fields**：对每个 media file，可选择添加这些字段：
    * **Caption**：输入文件的 caption 文本，最多 1024 个字符。
    * **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。

有关更多信息，请参阅 Telegram Bot API [sendMediaGroup](https://core.telegram.org/bots/api#sendmediagroup) 文档。

### Send Media Group additional fields <a href="#send-media-group-additional-fields" id="send-media-group-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendMediaGroup method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。

## Send Message <a href="#send-message" id="send-message"></a>

使用此操作通过 Bot API [sendMessage](https://core.telegram.org/bots/api#sendmessage) method 向 chat 发送消息。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Message**。
* **Chat ID**：输入要发送消息的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Text**：输入要发送的文本，entities parsing 后最多 4096 个字符。

有关更多信息，请参阅 Telegram Bot API [sendMessage](https://core.telegram.org/bots/api#sendmessage) 文档。

{% hint style="warning" %}
**Send Message 限制**

Telegram 将你每秒可发送的消息数限制为 30 条。如果预计会达到此限制，请参阅 [Send more than 30 messages per second](common-issues.md#send-more-than-30-messages-per-second) 获取建议的解决方法。
{% endhint %}

### Send Message additional fields <a href="#send-message-additional-fields" id="send-message-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendMessage method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Append n8n Attribution**：选择是否在消息末尾包含短语 `This message was sent automatically with n8n`（开启，默认），或不包含（关闭）。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Disable WebPage Preview**：选择是否为此消息中的链接启用 link preview（关闭），或禁用 link preview（开启）。这会为 `is_disabled` 设置 `link_preview_options` 参数。有关更多信息，请参阅 [LinkPreviewOptions](https://core.telegram.org/bots/api#linkpreviewoptions) 文档。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 Telegram 的 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。

## Send and Wait for Response <a href="#send-and-wait-for-response" id="send-and-wait-for-response"></a>

使用此操作通过 Bot API [`sendMessage`](https://core.telegram.org/bots/api#sendmessage) method 向 chat 发送消息，并暂停 workflow 执行，直到用户确认操作。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send and Wait for Response**。
* **Chat ID**：输入要发送消息的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Message**：输入要发送的文本。
* **Response Type**：要使用的 approval 或 response 类型：
  * **Approval**：用户可以在消息内 approve 或 disapprove。
  * **Free Text**：用户可以通过 form 提交 response。
  * **Custom Form**：用户可以通过自定义 form 提交 response。

有关更多信息，请参阅 Telegram Bot API [`sendMessage`](https://core.telegram.org/bots/api#sendmessage) 文档。

{% hint style="warning" %}
**Send Message 限制**

Telegram 将你每秒可发送的消息数限制为 30 条。如果预计会达到此限制，请参阅 [Send more than 30 messages per second](common-issues.md#send-more-than-30-messages-per-second) 获取建议的解决方法。
{% endhint %}

### Send and Wait for Response additional fields <a href="#send-and-wait-for-response-additional-fields" id="send-and-wait-for-response-additional-fields"></a>

Additional fields 取决于你选择的 **Response Type**。

#### Approval <a href="#approval" id="approval"></a>

**Approval** response type 会添加这些选项：

* **Type of Approval**：是只显示 approval button，还是同时显示 approval 和 disapproval button。
* **Button Label**：approval 或 disapproval button 的 label。默认选项分别是 approval action 的 `✅ Approve` 和 disapproval action 的 `❌ Decline`。
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。该时间可以是 interval，也可以是具体 wall time。

#### Free Text <a href="#free-text" id="free-text"></a>

使用 Free Text response type 时，可用以下选项：

* **Message Button Label**：message button 使用的 label。默认选项为 `Respond`。
* **Response Form Title**：用户提供 response 的 form 标题。
* **Response Form Description**：用户提供 response 的 form 描述。
* **Response Form Button Label**：form 上用于提交 response 的 button label。默认选项为 `Submit`。
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。该时间可以是 interval，也可以是具体 wall time。

#### Custom Form <a href="#custom-form" id="custom-form"></a>

使用 Custom Form response type 时，你可以使用所需字段和选项构建 form。

你可以使用 [n8n Form trigger 的 form elements](../../core-nodes/n8n-nodes-base.formtrigger.md#form-elements) 中列出的设置自定义每个 form element。要添加更多字段，请选择 **Add Form Element** button。

以下选项也可用：

* **Message Button Label**：message button 使用的 label。默认选项为 `Respond`。
* **Response Form Title**：用户提供 response 的 form 标题。
* **Response Form Description**：用户提供 response 的 form 描述。
* **Response Form Button Label**：form 上用于提交 response 的 button label。默认选项为 `Submit`。
* **Limit Wait Time**：workflow 是否会在指定时间限制后自动恢复执行。该时间可以是 interval，也可以是具体 wall time。

## Send Photo <a href="#send-photo" id="send-photo"></a>

使用此操作通过 Bot API [sendPhoto](https://core.telegram.org/bots/api#sendphoto) method 向 chat 发送照片。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Photo**。
* **Chat ID**：输入要发送 photo 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Photo**：如果不使用 **Binary File**，请在这里输入要发送的 photo。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendPhoto](https://core.telegram.org/bots/api#sendphoto) 文档。

### Send Photo additional fields <a href="#send-photo-additional-fields" id="send-photo-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendPhoto method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Caption**：输入文件的 caption 文本，最多 1024 个字符。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 Telegram 的 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。

## Send Sticker <a href="#send-sticker" id="send-sticker"></a>

使用此 method 通过 Bot API [sendSticker](https://core.telegram.org/bots/api#sendsticker) 发送静态 .WEBP、动画 .TGS 或视频 .WEBM sticker。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Sticker**。
* **Chat ID**：输入要发送 sticker 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Sticker**：如果不使用 **Binary File**，请在这里输入要发送的 photo。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendSticker](https://core.telegram.org/bots/api#sendsticker) 文档。

### Send Sticker additional fields <a href="#send-sticker-additional-fields" id="send-sticker-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendSticker method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。

## Send Video <a href="#send-video" id="send-video"></a>

使用此操作通过 Bot API [sendVideo](https://core.telegram.org/bots/api#sendvideo) method 向 chat 发送视频。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Send Video**。
* **Chat ID**：输入要发送 video 的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Binary File**：要从 node 本身发送二进制文件，请开启此选项。如果开启此参数，必须输入包含要发送文件的 **Input Binary Field**。
* **Video**：如果不使用 **Binary File**，请在这里输入要发送的 video。传入 `file_id` 可发送 Telegram 服务器上已有的文件（推荐），或传入 HTTP URL 让 Telegram 从互联网获取文件。
* **Reply Markup**：使用此参数设置更多界面选项。有关这些选项和用法的更多信息，请参阅 [Reply Markup parameters](message-operations.md#reply-markup-parameters)。

有关更多信息，请参阅 Telegram Bot API [sendVideo](https://core.telegram.org/bots/api#sendvideo) 文档。

### Send Video additional fields <a href="#send-video-additional-fields" id="send-video-additional-fields"></a>

使用 **Additional Fields** 通过 Telegram sendVideo method 中的可选字段进一步细化 node 行为。选择 **Add Field** 可添加以下任意字段：

* **Caption**：输入 video 的 caption 文本，最多 1024 个字符。
* **Disable Notification**：选择静默发送通知（开启），还是使用标准通知（关闭）。
* **Duration**：输入 video 的时长，单位为秒。
* **Height**：输入 video 的高度。
* **Parse Mode**：输入相关文本使用的 parser。选项包括 **HTML**（默认）、**Markdown (Legacy)**、**MarkdownV2**。有关这些选项的更多信息，请参阅 Telegram 的 [Formatting options](https://core.telegram.org/bots/api#formatting-options)。
* **Reply To Message ID**：如果此消息是回复，请输入被回复消息的 ID。
* **Message Thread ID**：输入目标 message thread（topic）的唯一标识符；仅适用于 forum supergroup。
* **Thumbnail**：添加所发送文件的 thumbnail。如果服务器端支持为文件生成 thumbnail，请忽略此字段。thumbnail 应符合以下规格：
  * JPEG 格式
  * 小于 200 KB
  * 宽和高小于 320px。
* **Width**：输入 video 的宽度。

## Unpin Chat Message <a href="#unpin-chat-message" id="unpin-chat-message"></a>

使用此操作通过 Bot API [unpinChatMessage](https://core.telegram.org/bots/api#unpinchatmessage) method 从 chat 中取消置顶消息。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **Message**。
* **Operation**：选择 **Pin Chat Message**。
* **Chat ID**：输入要从中取消置顶消息的 channel 的 Chat ID 或 username，格式为 `@channelusername`。
  * 要将 Chat ID 直接传入此 node，请使用 [Telegram Trigger](../../trigger-nodes/n8n-nodes-base.telegramtrigger/) node。更多信息请参阅 [Common Issues | Get the Chat ID](common-issues.md#get-the-chat-id)。
* **Message ID**：输入要取消置顶的消息的唯一标识符。

有关更多信息，请参阅 Telegram Bot API [unpinChatMessage](https://core.telegram.org/bots/api#unpinchatmessage) 文档。

## Reply Markup parameters <a href="#reply-markup-parameters" id="reply-markup-parameters"></a>

对于大多数 **Message** **Send** action（例如 Send Animation、Send Audio），使用 **Reply Markup** 参数设置更多界面选项：

* **Force Reply**：Telegram 客户端会像用户已选择 bot 消息并点击 **Reply** 一样，自动向用户显示回复界面。有关此选项的更多指导，请参阅 [Force Reply parameters](message-operations.md#force-reply-parameters)。
* **Inline Keyboard**：在消息旁边显示 inline keyboard。有关此选项的更多指导，请参阅 [Inline Keyboard parameters](message-operations.md#inline-keyboard-parameters)。
* **Reply Keyboard**：显示带回复选项的自定义 keyboard。有关此选项的更多指导，请参阅 [Reply Keyboard parameters](message-operations.md#reply-keyboard-parameters)。
* **Reply Keyboard Remove**：Telegram 客户端会移除当前自定义 keyboard，并显示默认字母 keyboard。有关此选项的更多指导，请参阅 [Reply Keyboard parameters](message-operations.md#reply-keyboard-remove-parameters)。

{% hint style="info" %}
**Telegram Business accounts**

Telegram 会在 channel 中以及代表 Telegram Business account 发送的消息中限制以下选项：

* Force Reply
* Reply Keyboard
* Reply Keyboard Remove
{% endhint %}

### Force Reply parameters <a href="#force-reply-parameters" id="force-reply-parameters"></a>

如果你想创建用户友好的分步界面，同时不牺牲 privacy mode，**Force Reply** 很有用。

如果选择 **Reply Markup > Force Reply**，请从这些 **Force Reply** 参数中选择：

* **Force Reply**：开启后向用户显示回复界面，如上所述。
* **Selective**：如果只想强制以下用户回复，请开启此选项：
  * 消息文本中被 `@mentioned` 的用户。
  * 原始消息的发送者，如果此 Send Animation 消息是对某条消息的回复。

有关更多信息，请参阅 [ForceReply](https://core.telegram.org/bots/api#forcereply)。

### Inline Keyboard parameters <a href="#inline-keyboard-parameters" id="inline-keyboard-parameters"></a>

如果选择 **Reply Markup > Inline Keyboard**，请使用 **Add Button** 选项定义要显示的 inline keyboard button。要向 keyboard 添加更多行，请使用 **Add Keyboard Row**。

有关更多信息，请参阅 [InlineKeyboardMarkup](https://core.telegram.org/bots/api#inlinekeyboardmarkup) 和 [InlineKeyboardButtons](https://core.telegram.org/bots/api#inlinekeyboardbutton)。

### Reply Keyboard parameters <a href="#reply-keyboard-parameters" id="reply-keyboard-parameters"></a>

如果选择 **Reply Markup > Reply Keyboard**，请使用 **Reply Keyboard** 部分定义 Reply Keyboard 中的 button 和 row。

使用 **Reply Keyboard Options** 进一步细化 keyboard 行为：

* **Resize Keyboard**：选择是否请求 Telegram 客户端垂直调整 keyboard 大小以获得最佳适配（开启），或使用与 app 标准 keyboard 相同的高度（关闭）。
* **One Time Keyboard**：选择 Telegram 客户端是否应在用户使用 keyboard 后立即隐藏它（开启），或继续显示它（关闭）。
* **Selective**：如果只想向以下用户显示 keyboard，请开启此选项：
  * 消息文本中被 `@mentioned` 的用户。
  * 原始消息的发送者，如果此 Send Animation 消息是对某条消息的回复。

有关更多信息，请参阅 [ReplyKeyboardMarkup](https://core.telegram.org/bots/api#replykeyboardmarkup)。

### Reply Keyboard Remove parameters <a href="#reply-keyboard-remove-parameters" id="reply-keyboard-remove-parameters"></a>

如果选择 **Reply Markup > Reply Keyboard Remove**，请从这些 **Reply Keyboard Remove** 参数中选择：

* **Remove Keyboard**：选择是否请求 Telegram 客户端移除自定义 keyboard（开启），或保留它（关闭）。
* **Selective**：如果只想为以下用户移除 keyboard，请开启此选项：
  * 消息文本中被 `@mentioned` 的用户。
  * 原始消息的发送者，如果此 Send Animation 消息是对某条消息的回复。

有关更多信息，请参阅 [ReplyKeyboardRemove](https://core.telegram.org/bots/api#replykeyboardremove)。

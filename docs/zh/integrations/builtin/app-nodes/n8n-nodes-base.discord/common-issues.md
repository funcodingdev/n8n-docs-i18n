---
title: Discord node common issues
contentType:
  - integration
  - reference
priority: high
nodeTitle: Discord node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues
description: >-
  n8n 中 Discord node 的常见问题和疑问文档。包含问题详情和建议解决方案。
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

# 常见问题

下面是 [Discord node](./) 的一些常见 errors 和 issues，以及解决或排查步骤。

## 向 embeds 添加额外字段 <a href="#add-extra-fields-to-embeds" id="add-extra-fields-to-embeds"></a>

Discord messages 可以选择包含 embeds。embeds 是一种 rich preview component，可包含 title、description、image、link 等内容。

在 **Message** resource 上使用 **Send** operation 时，Discord node 支持 embeds。选择 **Add Embeds** 可设置额外字段，包括 Description、Author、Title、URL 和 URL Image。

要添加默认未包含的字段，请将 **Input Method** 设为 **Raw JSON**。然后，在 **Value** 参数中添加一个 JSON object，用于定义你想包含的 [field names](https://discord.com/developers/docs/resources/message#embed-object) 和 values。

例如，要包含 `footer` 和 `fields`，而这两个字段无法通过 **Enter Fields** Input Method 使用，你可以使用如下 JSON object：

```json
{
    "author": "My Name",
	"url": "https://discord.js.org",
	"fields": [
		{
			"name": "Regular field title",
			"value": "Some value here"
		}
	],
	"footer": {
		"text": "Some footer text here",
		"icon_url": "https://i.imgur.com/AfFp7pu.png"
	}
}
```

你可以在 [Using Webhooks and Embeds | Discord](https://discord.com/safety/using-webhooks-and-embeds) 中了解更多 embeds 信息。

如果你在使用 Discord node 处理 embeds 时遇到问题，可以使用 [HTTP Request](../../core-nodes/n8n-nodes-base.httprequest/) 搭配现有 Discord credentials，对以下 URL 执行 `POST`：

```
https://discord.com/api/v10/channels/<CHANNEL_ID>/messages
```

在 body 中，将 embed 信息包含在 message content 中，如下所示：

```json
{
	"content": "Test",
	"embeds": [
		{
			"author": "My Name",
			"url": "https://discord.js.org",
			"fields": [
				{
					"name": "Regular field title",
					"value": "Some value here"
				}
			],
			"footer": {
				"text": "Some footer text here",
				"icon_url": "https://i.imgur.com/AfFp7pu.png"
			}
		}
	]
}
```

## Mention users 和 channels <a href="#mention-users-and-channels" id="mention-users-and-channels"></a>

要在 Discord messages 中 mention users 和 channels，你需要按照 [Discord's message formatting guidelines](https://discord.com/developers/docs/reference#message-formatting) 格式化 message。

要 mention user，你需要知道 Discord user 的 user ID。请注意，user ID 与 user 的 display name 不同。同样，要链接到特定 channel，你需要 channel ID。

你可以在 [Discord's documentation on finding User/Server/Message IDs](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID) 中了解如何启用 developer mode 并复制 user 或 channel IDs。

获得 user 或 channel ID 后，你可以使用以下语法格式化 message：

* **User**: `<@USER_ID>`
* **Channel**: `<#CHANNEL_ID>`
* **Role**: `<@&ROLE_ID>`

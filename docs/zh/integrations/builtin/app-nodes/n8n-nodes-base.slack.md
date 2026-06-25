---
title: Slack node documentation
description: >-
  了解如何在 n8n 中使用 Slack node。按照技术文档将 Slack node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Slack node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.slack.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack'
layout:
  description:
    visible: false
---

# Slack node <a href="#slack-node" id="slack-node"></a>

使用 Slack node 自动化 Slack 中的工作，并将 Slack 与其他应用集成。n8n 内置支持大量 Slack 功能，包括创建、归档和关闭 channel，获取 user 和 file，以及删除 message。

在本页中，你可以找到 Slack node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Slack credentials](../credentials/slack.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

## 操作 <a href="#operations" id="operations"></a>

* **Channel**
    * **Archive** channel。
    * **Close** direct message 或 multi-person direct message。
    * **Create** public 或 private channel-based conversation。
    * **Get** channel 相关信息。
    * **Get Many**：获取 Slack 中的 channel 列表。
    * **History**：获取 channel 的 message 和 event 历史。
    * **Invite** user 到 channel。
    * **Join** 现有 channel。
    * **Kick**：从 channel 中移除 user。
    * **Leave** channel。
    * **Member**：列出 channel 的 member。
    * **Open** 或恢复 direct message 或 multi-person direct message。
    * **Rename** channel。
    * **Replies**：获取发布到 channel 的 message thread。
    * **Sets purpose** 设置 channel 的 purpose。
    * **Sets topic** 设置 channel 的 topic。
    * **Unarchive** channel。
* **File**
    * **Get** file。
    * **Get Many**：获取并筛选 team file。
    * **Upload**：创建或上传现有 file。
* **Message**
    * **Delete** message
    * **Get permalink**：获取 message 的 permalink。
    * **Search** message
    * **Send** message
    * **Send and Wait for Response**：发送 message，并在继续前等待接收者响应。
    * **Update** message
* **Reaction**
    * **Add** reaction 到 message。
    * **Get** message 的 reaction。
    * **Remove** message 中的 reaction。
* **Star**
    * **Add** star 到 item。
    * **Delete** 从 item 删除 star。
    * **Get Many**：获取已认证 user 的 star 列表。
* **User**
    * **Get** user 相关信息。
    * **Get Many**：获取 user 列表。
    * **Get User's Profile**。
    * **Get User's Status**。
    * **Update User's Profile**。
* **User Group**
    * **Create** user group。
    * **Disable** user group。
    * **Enable** user group。
    * **Get Many**：获取 user group 列表。
    * **Update** user group。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Slack node 文档集成模板](https://n8n.io/integrations/slack)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Slack 文档](https://api.slack.com/)。

## 必需 scopes <a href="#required-scopes" id="required-scopes"></a>

为你的 [Slack credentials](../credentials/slack.md) 创建 Slack app 后，必须为 Slack app 添加相应 scope，此 node 才能工作。先从 [Scopes | Slack credentials](../credentials/slack.md#scopes) 页面列出的 scope 开始。

如果这些还不够，请使用下表查找你要使用的 resource 和 operation，然后跟随链接到 Slack API 文档，找到正确的 scope。

| **Resource** | **Operation**              | **Slack API method**                                                               |
|--------------|----------------------------|------------------------------------------------------------------------------------|
| Channel      | Archive                    | [conversations.archive](https://api.slack.com/methods/conversations.archive)       |
| Channel      | Close                      | [conversations.close](https://api.slack.com/methods/conversations.close)           |
| Channel      | Create                     | [conversations.create](https://api.slack.com/methods/conversations.create)         |
| Channel      | Get                        | [conversations.info](https://api.slack.com/methods/conversations.info)             |
| Channel      | Get Many                   | [conversations.list](https://api.slack.com/methods/conversations.list)             |
| Channel      | History                    | [conversations.history](https://api.slack.com/methods/conversations.history)       |
| Channel      | Invite                     | [conversations.invite](https://api.slack.com/methods/conversations.invite)         |
| Channel      | Join                       | [conversations.join](https://api.slack.com/methods/conversations.join)             |
| Channel      | Kick                       | [conversations.kick](https://api.slack.com/methods/conversations.kick)             |
| Channel      | Leave                      | [conversations.leave](https://api.slack.com/methods/conversations.leave)           |
| Channel      | Member                     | [conversations.members](https://api.slack.com/methods/conversations.members)       |
| Channel      | Open                       | [conversations.open](https://api.slack.com/methods/conversations.open)             |
| Channel      | Rename                     | [conversations.rename](https://api.slack.com/methods/conversations.rename)         |
| Channel      | Replies                    | [conversations.replies](https://api.slack.com/methods/conversations.replies)       |
| Channel      | Set Purpose                | [conversations.setPurpose](https://api.slack.com/methods/conversations.setPurpose) |
| Channel      | Set Topic                  | [conversations.setTopic](https://api.slack.com/methods/conversations.setTopic)     |
| Channel      | Unarchive                  | [conversations.unarchive](https://api.slack.com/methods/conversations.unarchive)   |
| File         | Get                        | [files.info](https://api.slack.com/methods/files.info)                             |
| File         | Get Many                   | [files.list](https://api.slack.com/methods/files.list)                             |
| File         | Upload                     | [files.upload](https://api.slack.com/methods/files.upload)                         |
| Message      | Delete                     | [chat.delete](https://api.slack.com/methods/chat.delete)                           |
| Message      | Get Permalink              | [chat.getPermalink](https://api.slack.com/methods/chat.getPermalink)               |
| Message      | Search                     | [search.messages](https://api.slack.com/methods/search.messages)                   |
| Message      | Send                       | [chat.postMessage](https://api.slack.com/methods/chat.postMessage)                 |
| Message      | Send and Wait for Response | [chat.postMessage](https://api.slack.com/methods/chat.postMessage)                 |
| Message      | Update                     | [chat.update](https://api.slack.com/methods/chat.update)                           |
| Reaction     | Add                        | [reactions.add](https://api.slack.com/methods/reactions.add)                       |
| Reaction     | Get                        | [reactions.get](https://api.slack.com/methods/reactions.get)                       |
| Reaction     | Remove                     | [reactions.remove](https://api.slack.com/methods/reactions.remove)                 |
| Star         | Add                        | [stars.add](https://api.slack.com/methods/stars.add)                               |
| Star         | Delete                     | [stars.remove](https://api.slack.com/methods/stars.remove)                         |
| Star         | Get Many                   | [stars.list](https://api.slack.com/methods/stars.list)                             |
| User         | Get                        | [users.info](https://api.slack.com/methods/users.info)                             |
| User         | Get Many                   | [users.list](https://api.slack.com/methods/users.list)                             |
| User         | Get User's Profile         | [users.profile.get](https://api.slack.com/methods/users.profile.get)               |
| User         | Get User's Status          | [users.getPresence](https://api.slack.com/methods/users.getPresence)               |
| User         | Update User's Profile      | [users.profile.set](https://api.slack.com/methods/users.profile.set)               |
| User Group   | Create                     | [usergroups.create](https://api.slack.com/methods/usergroups.create)               |
| User Group   | Disable                    | [usergroups.disable](https://api.slack.com/methods/usergroups.disable)             |
| User Group   | Enable                     | [usergroups.enable](https://api.slack.com/methods/usergroups.enable)               |
| User Group   | Get Many                   | [usergroups.list](https://api.slack.com/methods/usergroups.list)                   |
| User Group   | Update                     | [usergroups.update](https://api.slack.com/methods/usergroups.update)               |

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

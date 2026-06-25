---
title: Slack Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Slack Trigger node。按照技术文档将 Slack Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Slack Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger
layout:
  description:
    visible: false
---

# Slack Trigger node <a href="#slack-trigger-node" id="slack-trigger-node"></a>

使用 Slack Trigger node 响应 [Slack](https://slack.com/) 中的事件，并将 Slack 与其他应用程序集成。n8n 内置支持多种 Slack 事件，包括新消息、reaction 和新 channel。

在本页中，你可以找到 Slack Trigger node 可响应的事件列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/slack.md)找到此 node 的身份验证信息。
{% endhint %}
{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Slack integrations](https://n8n.io/integrations/slack-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **任意事件**：Slack 中发生任何事件时，此 node 都会触发。
* **App Home 已打开**：当用户打开你的 Slack app 的 [App Home](https://api.slack.com/surfaces/app-home) 标签页时，此 node 会触发。
* **Bot / App 被提及**：当你的 bot 或 app 在其所在 channel 中被[提及](https://slack.com/help/articles/205240127-Use-mentions-in-Slack)时，此 node 会触发。
* **文件设为公开**：当文件被[设为公开](https://slack.com/help/articles/4412651915539-Manage-public-file-sharing)时，此 node 会触发。
* **文件已分享**：当文件在 app 所在 channel 中被[分享](https://slack.com/help/articles/201330736-Add-files-to-Slack)时，此 node 会触发。
* **新消息发布到 Channel**：当新消息发布到 app 所在 channel 时，此 node 会触发。
* **新公共 Channel 已创建**：当新的[公共 channel](https://slack.com/help/articles/360017938993-What-is-a-channel)创建时，此 node 会触发。
* **新用户**：当新用户被添加到 Slack 时，此 node 会触发。
* **已添加 Reaction**：当 [reaction](https://slack.com/help/articles/202931348-Use-emoji-and-reactions) 被添加到 app 所在消息时，此 node 会触发。

## 参数 <a href="#parameters" id="parameters"></a>

设置要触发的事件后，使用其余参数进一步定义 node 的行为：

* **Watch Whole Workspace**：node 是否应在 workspace 的所有 channel 中监听所选 **Events**（开启）或不监听（关闭，默认）。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>注意</strong></p><p>这会针对你的 bot 或 app 所在任何 channel 中的每个事件各使用一次执行。请谨慎使用！</p></div>

* **Channel to Watch**：选择你的 node 应监听所选 **Events** 的 channel。只有未开启 **Watch Whole Workspace** 时才会显示此参数。你可以选择 channel：
    * **From list**：node 使用你的 credential 查询 workspace 中的 channel 列表，以便你选择所需 channel。
    * **By ID**：输入要监听的 channel ID。Slack 会在 channel 详情底部显示 channel ID，并提供一键复制按钮。
    * **By URL**：输入要监听的 channel URL，格式为 `https://app.slack.com/client/<channel-address>`。
* **Download Files**：是否下载文件并在 node 输出中使用（开启），或不下载（关闭，默认）。将此参数与 **File Made Public** 和 **File Shared** 事件一起使用。

## 选项 <a href="#options" id="options"></a>

你可以在 **Add Option** 时进一步细化 node 的行为：

* **Resolve IDs**：是否将 ID 解析为对应名称并返回（开启），或不解析（关闭，默认）。
* **Usernames or IDs to ignore**：选择用户名，或输入逗号分隔的编码用户 ID 字符串，以忽略来自这些用户的事件。可以从列表中选择，也可以使用 [expression](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/expressions-versus-data-nodes) 指定 ID。
* **Emoji Names to Filter**：输入逗号分隔（**不是** 冒号分隔）的 emoji 名称列表（例如 `thumbsup, eyes, white_check_mark`），将 **Reaction Added** 事件限制为仅这些特定 reaction。留空则任何 reaction 都会触发。

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Slack 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.slack.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/slack-trigger/)。

有关其 API 的详细信息，请参阅 [Slack 的文档](https://api.slack.com/apis/connections/events-api)。

## 必需 scopes <a href="#required-scopes" id="required-scopes"></a>

要使用此 node，你需要在 Slack 中创建一个应用程序并启用 event subscriptions。有关更多信息，请参阅 [Slack credentials | Slack Trigger configuration](../credentials/slack.md#slack-trigger-configuration)。

你必须为 Slack app 添加适当的 scopes，此 trigger node 才能工作。

此 node 至少需要 [conversations.list](https://api.slack.com/methods/conversations.list) 和 [users.list](https://api.slack.com/methods/users.list) 方法的 scopes。有关更完整的 scopes 列表，请查看 [Scopes | Slack credentials](../credentials/slack.md#scopes) 列表。

## 验证 webhook <a href="#verify-the-webhook" id="verify-the-webhook"></a>

从版本 `1.106.0` 起，你可以在配置 [Slack credentials](../credentials/slack.md#slack-trigger-configuration) 时设置 [Slack Signing Secret](https://api.slack.com/authentication/verifying-requests-from-slack#signing_secrets_admin_page)。设置后，Slack trigger node 会自动验证请求是否来自 Slack 且包含可信签名。n8n 建议设置此项，以确保你只处理 Slack 发送的请求。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Slack Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### Workflow 只在测试或生产环境中工作 <a href="#workflow-only-works-in-testing-or-production" id="workflow-only-works-in-testing-or-production"></a>

Slack 只允许你为每个 app 注册一个 webhook。这意味着，如果不重新配置已注册的 webhook URL，就无法从测试 URL 切换到生产 URL（反之亦然）。

如果你尝试测试一个也在生产环境中处于激活状态的 workflow，可能会遇到此问题。Slack 只会向两个 webhook URL 中的一个发送事件，因此另一个永远不会收到事件通知。

要绕过此问题，你可以在测试时停用 workflow：

{% hint style="warning" %}
**暂停生产流量**

这会临时停用你的生产 workflow 以便测试。停用期间，你的 workflow 将不再接收生产流量。
{% endhint %}

1. 前往你的 workflow 页面。
2. 切换顶部面板中的 **Active** 开关，临时停用 workflow。
3. 在 [Slack Trigger configuration](../credentials/slack.md#slack-trigger-configuration) 中编辑 **Request URL**，使用测试 webhook URL，而不是生产 webhook URL。
4. 使用测试 webhook URL 测试你的 workflow。
5. 测试完成后，在 [Slack Trigger configuration](../credentials/slack.md#slack-trigger-configuration) 中编辑 **Request URL**，使用生产 webhook URL，而不是测试 webhook URL。
6. 切换 **Inactive** 开关以重新启用 workflow。生产 webhook URL 应恢复工作。

### Token 已过期 <a href="#token-expired" id="token-expired"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/aLQxqepKmNn7Oz3PDTB7/" %}

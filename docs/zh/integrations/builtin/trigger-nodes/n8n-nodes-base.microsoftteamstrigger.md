---
title: Microsoft Teams Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Microsoft Teams Trigger node。按照技术文档将
  Microsoft Teams Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Microsoft Teams Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftteamstrigger
layout:
  description:
    visible: false
---

# Microsoft Teams Trigger node <a href="#microsoft-teams-trigger-node" id="microsoft-teams-trigger-node"></a>

使用 Microsoft Teams Trigger node 响应 [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) 中的事件，并将 Microsoft Teams 与其他应用程序集成。

在本页中，你可以找到 Microsoft Teams Trigger node 可响应的事件列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/microsoft.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**Government Cloud Support**

如果你使用的是政府云租户（US Government、US Government DOD 或 China），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **新频道**
* **新频道消息**
* **新聊天**
* **新聊天消息**
* **新团队成员**

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft Teams 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.microsoftteams.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/microsoft-teams-trigger/)。

有关其 API 的详细信息，请参阅 [Microsoft Teams 的文档](https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)。

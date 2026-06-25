---
title: Microsoft Outlook Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Microsoft Outlook Trigger node。按照技术文档将 Microsoft Outlook Trigger node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft Outlook Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftoutlooktrigger
layout:
  description:
    visible: false
---

# Microsoft Outlook Trigger node <a href="#microsoft-outlook-trigger-node" id="microsoft-outlook-trigger-node"></a>

使用 Microsoft Outlook Trigger node 响应 [Microsoft Outlook](https://www.microsoft.com/en-us/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook) 中的事件，并将 Microsoft Outlook 与其他应用集成。

在本页中，你可以找到 Microsoft Outlook Trigger node 可以响应的事件列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

此 node 支持两种身份验证选项：

- **Microsoft Outlook OAuth2 API**：Microsoft Outlook 专用 OAuth2 credential（默认）。
- **Microsoft OAuth2 API**：可在其他 Microsoft node 中复用的通用 Microsoft Graph credential。选择此选项时，请确保 credential 已授予此 node 所需的 scope（例如 `Mail.ReadWrite`）。

你可以在[这里](../credentials/microsoft.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用政府云租户（US Government、US Government DOD 或中国），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Microsoft Outlook integrations](https://n8n.io/integrations/microsoft-outlook-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 已收到消息

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft Outlook 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.microsoftoutlook.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/microsoft-outlook-trigger/)。

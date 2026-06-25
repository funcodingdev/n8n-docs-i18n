---
title: Microsoft Outlook node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft Outlook node。按照技术文档将 Microsoft Outlook node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Microsoft Outlook node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftoutlook
layout:
  description:
    visible: false
---

# Microsoft Outlook node <a href="#microsoft-outlook-node" id="microsoft-outlook-node"></a>

使用 Microsoft Outlook node 自动化 Microsoft Outlook 中的工作，并将 Microsoft Outlook 与其他应用集成。n8n 内置支持大量 Microsoft Outlook 功能，包括创建、更新、删除和获取 folder、message 与 draft。

在本页中，你可以找到 Microsoft Outlook node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

此 node 支持两种身份验证选项：

- **Microsoft Outlook OAuth2 API**：Microsoft Outlook 专用 OAuth2 credential（默认）。
- **Microsoft OAuth2 API**：可在其他 Microsoft node 中复用的通用 Microsoft Graph credential。选择此选项时，请确保 credential 已被授予此 node 所需的 scope（例如 `Mail.ReadWrite`、`Mail.Send`、`Calendars.ReadWrite` 和 `Contacts.ReadWrite`）。

有关设置身份验证的指导，请参阅 [Microsoft credentials](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用 government cloud tenant（US Government、US Government DOD 或 China），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

## 操作 <a href="#operations" id="operations"></a>

* Calendar
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新
* Contact
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新
* Draft
    * 创建
    * 删除
    * 获取
    * 发送
    * 更新
* Event
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新
* Folder
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新
* Folder Message
    * 获取多个
* Message
    * 删除
    * 获取
    * 获取多个
    * 移动
    * 回复
    * 发送
    * 发送并等待响应
    * 更新
* Message Attachment
    * 添加
    * 下载
    * 获取
    * 获取多个

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/c0Jp2CWNEFSR2IfIVdlL/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft Outlook node 文档集成模板](https://n8n.io/integrations/microsoft-outlook)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Outlook API 文档](https://learn.microsoft.com/en-us/outlook/rest/get-started)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

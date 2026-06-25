---
title: Microsoft Teams node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft Teams node。按照技术文档将 Microsoft Teams node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft Teams node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftteams
layout:
  description:
    visible: false
---

# Microsoft Teams node <a href="#microsoft-teams-node" id="microsoft-teams-node"></a>

使用 Microsoft Teams node 自动化 Microsoft Teams 中的工作，并将 Microsoft Teams 与其他应用集成。n8n 内置支持大量 Microsoft Teams 功能，包括创建和删除 channel、message 与 task。

在本页中，你可以找到 Microsoft Teams node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Microsoft credentials](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用 government cloud tenant（US Government、US Government DOD 或 China），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sYWM3IB0LEL4RkPx8ndF/" %}

## 操作 <a href="#operations" id="operations"></a>

* Channel
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新
* Channel Message
    * 创建
    * 获取多个
* Chat Message
    * 创建
    * 获取
    * 获取多个
    * 发送并等待响应
* Task
    * 创建
    * 删除
    * 获取
    * 获取多个
    * 更新

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/c0Jp2CWNEFSR2IfIVdlL/" %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft Teams node 文档集成模板](https://n8n.io/integrations/microsoft-teams)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Microsoft Teams API 文档](https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

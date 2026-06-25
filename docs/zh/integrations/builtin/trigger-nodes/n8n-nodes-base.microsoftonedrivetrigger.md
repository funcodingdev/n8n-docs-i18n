---
title: Microsoft OneDrive Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Microsoft OneDrive Trigger node。按照技术文档将 Microsoft OneDrive Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Microsoft OneDrive Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.microsoftonedrivetrigger
layout:
  description:
    visible: false
---

# Microsoft OneDrive Trigger node <a href="#microsoft-onedrive-trigger-node" id="microsoft-onedrive-trigger-node"></a>

使用 Microsoft OneDrive Trigger node 响应 [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage) 中的事件，并将 Microsoft OneDrive 与其他应用集成。n8n 内置支持 OneDrive 中的文件和文件夹事件。

在本页中，你可以找到 Microsoft OneDrive Trigger node 可以响应的事件列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/microsoft.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用政府云租户（US Government、US Government DOD 或中国），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Microsoft OneDrive integrations](https://n8n.io/integrations/microsoft-onedrive-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 文件已创建
* 文件已更新
* 文件夹已创建
* 文件夹已更新

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Microsoft OneDrive 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.microsoftonedrive.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/microsoft-onedrive-trigger/)。

有关此服务的更多信息，请参阅 [Microsoft 的 OneDrive API 文档](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/)。

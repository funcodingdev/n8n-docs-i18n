---
title: TheHive node documentation
description: >-
  了解如何在 n8n 中使用 TheHive node。按照技术文档将 TheHive node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: TheHive node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.thehive.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.thehive'
layout:
  description:
    visible: false
---

# TheHive node <a href="#thehive-node" id="thehive-node"></a>

使用 TheHive node 自动化 TheHive 中的工作，并将 TheHive 与其他应用集成。n8n 内置支持大量 TheHive 功能，包括创建 alert，统计 task log、case 和 observable。

在本页中，你可以找到 TheHive node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**TheHive 和 TheHive 5**

n8n 为 TheHive 提供两个 node。如果你想使用 TheHive 版本 3 或 4 API，请使用此 node（TheHive）。如果想使用版本 5，请使用 [TheHive 5](n8n-nodes-base.thehive5.md)。
{% endhint %}
{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [TheHive credentials](../credentials/thehive.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

可用操作取决于你的 API version。要查看操作列表，请创建 credential，并选择 API version。然后返回 node，选择要使用的 resource，n8n 会显示该 API version 可用的操作。

* Alert
* Case
* Log
* Observable
* Task

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 TheHive node 文档集成模板](https://n8n.io/integrations/thehive)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 TheHive 提供 trigger node。你可以在[这里](../trigger-nodes/n8n-nodes-base.thehivetrigger.md)找到 trigger node 文档。

有关此服务的更多信息，请参阅 TheHive 文档：

* [Version 3](https://docs.thehive-project.org/thehive/legacy/thehive3/api/)
* [Version 4](https://docs.thehive-project.org/cortex/api/api-guide/)

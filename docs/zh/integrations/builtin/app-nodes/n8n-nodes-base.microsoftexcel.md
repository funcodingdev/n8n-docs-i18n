---
title: Microsoft Excel 365 node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft Excel node。按照技术文档将 Microsoft Excel node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Microsoft Excel 365 node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftexcel
layout:
  description:
    visible: false
---

# Microsoft Excel 365 node <a href="#microsoft-excel-365-node" id="microsoft-excel-365-node"></a>

使用 Microsoft Excel node 自动化 Microsoft Excel 中的工作，并将 Microsoft Excel 与其他应用集成。n8n 内置支持大量 Microsoft Excel 功能，包括添加和检索 table data、workbook 列表，以及获取 worksheet。

在本页中，你可以找到 Microsoft Excel node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

此 node 支持两种身份验证选项：

- **Microsoft Excel OAuth2 API**：Microsoft Excel 专用 OAuth2 credential（默认）。
- **Microsoft OAuth2 API**：可在其他 Microsoft node 中复用的通用 Microsoft Graph credential。选择此选项时，请确保 credential 已被授予此 node 所需的 scope（例如 `Files.ReadWrite`，如果你的管理员同意的是该权限，则为 `Files.ReadWrite.All`）。

有关设置身份验证的指导，请参阅 [Microsoft credentials](../credentials/microsoft.md)。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用 government cloud tenant（US Government、US Government DOD 或 China），请确保在 Microsoft credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Table
    * 将 row 添加到 table 末尾
    * 检索 table column 列表
    * 检索 table row 列表
    * 查找特定 column value，然后返回匹配的 row
* Workbook
    * 向 workbook 添加新 worksheet。
    * 获取所有 workbook 的数据
* Worksheet
    * 获取所有 worksheet
    * 获取 worksheet 内容

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft Excel 365 node 文档集成模板](https://n8n.io/integrations/microsoft-excel)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

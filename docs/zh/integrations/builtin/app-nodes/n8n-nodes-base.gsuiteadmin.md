---
title: Google Workspace Admin node documentation
description: >-
  了解如何在 n8n 中使用 Google Workspace Admin node。按照技术文档将 Google Workspace Admin
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Google Workspace Admin node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin'
layout:
  description:
    visible: false
---

# Google Workspace Admin node <a href="#google-workspace-admin-node" id="google-workspace-admin-node"></a>

使用 Google Workspace Admin node 自动化 Google Workspace Admin 中的工作，并将 Google Workspace Admin 与其他应用集成。n8n 内置支持大量 Google Workspace Admin 功能，包括创建、更新、删除和获取 user、group 与 ChromeOS device。

在本页中，你可以找到 Google Workspace Admin node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Google credentials](../credentials/google/README.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* ChromeOS Device
    * 获取 ChromeOS device
    * 获取多个 ChromeOS device
    * 更新 ChromeOS device
    * 更改 ChromeOS device 的状态
* Group
    * 创建 group
    * 删除 group
    * 获取 group
    * 获取多个 group
    * 更新 group
* User
    * 将现有 user 添加到 group
    * 创建 user
    * 删除 user
    * 获取 user
    * 获取多个 user
    * 从 group 中移除 user
    * 更新 user

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Google Workspace Admin node 文档集成模板](https://n8n.io/integrations/google-workspace-admin)或[搜索所有模板](https://n8n.io/workflows/)

## 如何控制获取 user 的哪些 custom field <a href="#how-to-control-which-custom-fields-to-fetch-for-a-user" id="how-to-control-which-custom-fields-to-fetch-for-a-user"></a>

获取 user 信息时，有三种不同方式可以控制要检索哪些 custom field。使用 **Custom Fields** 参数选择以下选项之一：

- **Don't Include**：不包含任何 custom field。
- **Custom**：包含 **Custom Schema Names or IDs** 中 schema 的 custom field。
- **Include All**：包含与该 user 关联的所有字段。

要包含 custom field，请按以下步骤操作：

1. 从 **Custom Fields** 下拉列表中选择 **Custom**。
2. 在 **Custom Schema Names or IDs** 下拉列表中选择要包含的 schema 名称。

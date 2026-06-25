---
title: Microsoft Entra ID node documentation
description: >-
  了解如何在 n8n 中使用 Microsoft Entra ID node。按照技术文档将 Microsoft Entra ID node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Microsoft Entra ID node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.microsoftentra
layout:
  description:
    visible: false
---

# Microsoft Entra ID node <a href="#microsoft-entra-id-node" id="microsoft-entra-id-node"></a>

使用 Microsoft Entra ID node 自动化 Microsoft Entra ID 中的工作，并将 Microsoft Entra ID 与其他应用集成。n8n 内置支持大量 Microsoft Entra ID 功能，包括创建、获取、更新和删除 user 与 group，以及将 user 添加到 group 和从 group 中移除。

在本页中，你可以找到 Microsoft Entra ID node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/microsoftentra.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**政府云支持**

如果你使用 government cloud tenant（US Government、US Government DOD 或 China），请确保在 Microsoft Entra ID credentials 配置中选择合适的 **Microsoft Graph API Base URL**。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Group**
    * **Create**：创建新 group
    * **Delete**：删除现有 group
    * **Get**：检索特定 group 的数据
    * **Get Many**：检索 group 列表
    * **Update**：更新 group
* **User**
    * **Create**：创建新 user
    * **Delete**：删除现有 user
    * **Get**：检索特定 user 的数据
    * **Get Many**：检索 user 列表
    * **Update**：更新 user
    * **Add to Group**：将 user 添加到 group
    * **Remove from Group**：从 group 中移除 user

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Microsoft Entra ID node 文档集成模板](https://n8n.io/integrations/microsoft-entra-id-azure-active-directory)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Microsoft Entra ID 文档](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview?view=graph-rest-1.0)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Microsoft Entra ID node 的一些常见错误和问题，以及解决或排查它们的步骤。

### 更新 Allow External Senders 和 Auto Subscribe New Members 选项失败 <a href="#updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails" id="updating-the-allow-external-senders-and-auto-subscribe-new-members-options-fails"></a>

创建新 group 后，不能直接更新 **Allow External Senders** 和 **Auto Subscribe New Members** 选项。你必须在创建 group 后等待一段时间，才能更改这些选项的值。

设计先创建 group、再更新这些选项的 workflow，并且其中使用多个 Microsoft Entra ID node 时，请在两个操作之间添加 [Wait](../core-nodes/n8n-nodes-base.wait.md) node。将 Wait node 配置为至少暂停两秒，可为 group 完成初始化留出时间。等待结束后，update 操作就可以无错误地完成。

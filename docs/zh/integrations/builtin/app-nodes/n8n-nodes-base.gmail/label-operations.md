---
title: Gmail node Label Operations documentation
description: >-
  了解如何在 n8n 中使用 Gmail node 的 Label Operations。按照技术文档，
  将 Label Operations 集成到你的 workflows 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Gmail node Label Operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations
layout:
  description:
    visible: false
---

# Gmail node Label Operations <a href="#gmail-node-label-operations" id="gmail-node-label-operations"></a>

使用 Label operations 在 Gmail 中创建、删除、获取单个 label 或列出 labels。有关 Gmail node 本身的更多信息，请参考 [Gmail node](README.md)。

## Create a label <a href="#create-a-label" id="create-a-label"></a>

使用此 operation 创建新的 label。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Label**。
* **Operation**：选择 **Create**。
* **Name**：输入 label 的 display name。

### Create label options <a href="#create-label-options" id="create-label-options"></a>

使用这些 options 进一步调整 node 行为：

* **Label List Visibility**：设置 Gmail web interface 中 label list 里此 label 的 visibility。可选择：
    * **Hide**：不在 label list 中显示此 label。
    * **Show**（默认）：在 label list 中显示此 label。
    * **Show if Unread**：如果存在带有此 label 的 unread messages，则显示此 label。
* **Message List Visibility**：设置 Gmail web interface 的 message list 中，带有此 label 的 messages 的 visibility。选择是 **Show** 还是 **Hide** 带有此 label 的 messages。

更多信息请参考 [Gmail API Method: users.labels.create](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/create) 文档。

## Delete a label <a href="#delete-a-label" id="delete-a-label"></a>

使用此 operation 删除现有 label。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Label**。
* **Operation**：选择 **Delete**。
* **Label ID**：输入要删除的 label ID。

更多信息请参考 [Gmail API Method: users.labels.delete](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/delete) 文档。

## Get a label <a href="#get-a-label" id="get-a-label"></a>

使用此 operation 获取现有 label。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Label**。
* **Operation**：选择 **Get**。
* **Label ID**：输入要获取的 label ID。

更多信息请参考 [Gmail API Method: users.labels.get](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/get) 文档。


## Get Many labels <a href="#get-many-labels" id="get-many-labels"></a>


使用此 operation 获取两个或更多 labels。

输入以下参数：

* 选择 **Credential to connect with**，或新建一个 credential。
* **Resource**：选择 **Label**。
* **Operation**：选择 **Get Many**。
* **Return All**：选择 node 是返回全部 labels（打开），还是最多返回设定 limit 数量（关闭）。
* **Limit**：输入要返回的最大 labels 数量。仅在关闭 **Return All** 时使用。

更多信息请参考 [Gmail API Method: users.labels.list](https://developers.google.com/gmail/api/reference/rest/v1/users.labels/list) 文档。

## 常见问题 <a href="#common-issues" id="common-issues"></a>

有关常见 errors 或 issues 及建议解决步骤，请参考 [常见问题](common-issues.md)。

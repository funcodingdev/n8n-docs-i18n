---
title: Credential sharing
contentType: howto
nodeTitle: Share credentials securely
originalFilePath: credentials/credential-sharing.md
originalUrl: https://docs.n8n.io/credentials/credential-sharing
url: https://docs.n8n.io/administer/manage-credentials/share-credentials-securely
description: 在 organization 内分享 credentials。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# 安全分享 credentials

{% hint style="info" %}
**功能可用性**

所有 Cloud plans，以及 Business 和 Enterprise self-hosted plans 均可使用。
{% endhint %}

你可以直接与其他 users 分享 credential，让他们在自己的 workflows 中使用。也可以在 project[^1] 中分享 credential，让该 project 的所有 members 使用。任何使用 shared credential 的 users 都无法查看或编辑 credential details。

Users 可以分享他们创建并拥有的 credentials。只有 project admins 可以分享在 project 中创建并由 project 拥有的 credentials。Instance owners 和 instance admins 可以查看并分享 instance 上的所有 credentials。

有关 owners 和 admins 的更多信息，请参考 [Account types](../manage-users-and-access/understand-account-types.md)。

在 [projects](../manage-users-and-access/set-permissions-and-roles-rbac/) 中，user 的 role 控制他们如何与自己所属 projects 关联的 workflows 和 credentials 交互。

## 分享 credential <a href="#share-a-credential" id="share-a-credential"></a>

分享 credential：

1. 从左侧 menu 中选择 **Overview** 或一个 project。
2. 选择 **Credentials** 查看你的 credentials 列表。
3. 选择要分享的 credential。
4. 选择 **Sharing**。
5. 在 **Share with projects or users** dropdown 中，浏览或搜索你想与之分享 credentials 的 user 或 project。
6. 选择一个 user 或 project。
7. 选择 **Save** 应用更改。

## 移除 credential access <a href="#remove-access-to-a-credential" id="remove-access-to-a-credential"></a>

取消分享 credential：

1. 从左侧 menu 中选择 **Overview** 或一个 project。
2. 选择 **Credentials** 查看你的 credentials 列表。
3. 选择要取消分享的 credential。
4. 选择 **Sharing**。
5. 在你想从 shared users 和 projects 列表中移除的 user 或 project 上，选择 **trash icon**<img src="../.gitbook/assets/delete-node (1).png" alt="Trash icon" data-size="line">。
6. 选择 **Save** 应用更改。

[^1]: n8n projects 允许你将 workflows、variables 和 credentials 分离到不同 groups 中，以便更轻松地管理。Projects 通过 sharing 和 compartmentalizing related resources，让 teams 更容易协作。

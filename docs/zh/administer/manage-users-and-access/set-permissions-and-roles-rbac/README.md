---
contentType: overview
title: Role-based access control (RBAC)
description: 在 n8n 中设置和使用 role-based access control (RBAC)。
nodeTitle: Set permissions and roles (RBAC)
originalFilePath: user-management/rbac/index.md
originalUrl: 'https://docs.n8n.io/user-management/rbac'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac
layout:
  description:
    visible: false
---

# Role-based access control (RBAC) <a href="#role-based-access-control-rbac" id="role-based-access-control-rbac"></a>

{% hint style="info" %}
**功能可用性**

RBAC 可用于除 Community edition 之外的所有 plans。不同 plans 拥有不同数量的 projects 和 roles。Plan details 请参考 n8n 的 [pricing page](https://n8n.io/pricing/)。
{% endhint %}

{% hint style="info" %}
**Role types 和 account types**

Role types 和 [account types](../understand-account-types.md) 是不同概念。每个 account 都有一个 type。该 account 可以在不同 [projects](organize-work-in-projects.md) 中拥有不同 role types。
{% endhint %}

RBAC 是一种基于 user roles 和 projects 管理 workflows 与 credentials[^1] access 的方式。你将 workflows 分组到 projects 中，user access 取决于 user 的 project role。本 section 提供在 n8n 中使用 RBAC 的指南。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。

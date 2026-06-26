---
description: n8n account types
contentType: reference
nodeTitle: Understand account types
originalFilePath: user-management/account-types.md
originalUrl: 'https://docs.n8n.io/user-management/account-types'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/understand-account-types
layout:
  description:
    visible: false
---

# Account types <a href="#account-types" id="account-types"></a>

共有三种 account types：owner、admin 和 member。Account type 会影响 user permissions 和 access。

{% hint style="info" %}
**功能可用性**

要使用 admin accounts，需要 pro 或 enterprise plan。
{% endhint %}

{% hint style="info" %}
**Account types 和 role types**

Account types 和 role types 是不同概念。Role types 是 [RBAC](set-permissions-and-roles-rbac/README.md) 的一部分。

每个 account 都有一个 type。该 account 可以在不同 [projects](set-permissions-and-roles-rbac/organize-work-in-projects.md) 中拥有不同 [role types](set-permissions-and-roles-rbac/see-available-roles.md)。
{% endhint %}

{% hint style="info" %}
**为 owner 创建 member-level account**

n8n 建议 owners 为自己创建一个 member-level account。Owners 可以查看并编辑所有 workflows、credentials 和 projects。但是，没有办法查看某个特定 workflow 是谁创建的，因此如果你以 owner 身份构建和编辑 workflows，就有覆盖他人 work 的风险。
{% endhint %}

| Permission | Owner | Admin | Member |
| ---------- |------ | ----- | ------ |
| 管理自己的 email 和 password | ✅ | ✅ | ✅ |
| 管理自己的 workflows | ✅ | ✅ | ✅ |
| View、create 和 use tags | ✅ | ✅ | ✅ |
| Delete tags | ✅ | ✅ | ❌ |
| View 和 share all workflows | ✅ | ✅ | ❌ |
| View、edit 和 share all credentials | ✅ | ✅ | ❌ |
| 设置并使用 [Source control](../use-source-control-and-environments/README.md) | ✅ | ✅ | ❌ |
| 创建 [projects](set-permissions-and-roles-rbac/organize-work-in-projects.md) | ✅ | ✅ | ❌ |
| View all projects | ✅ | ✅ | ❌ |
| Add and remove users | ✅ | ✅ | ❌ |
| Access the Cloud dashboard | ✅ | ❌ | ❌ |

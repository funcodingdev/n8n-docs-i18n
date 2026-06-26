---
title: RBAC role types
description: 了解 n8n 中可用的 RBAC roles 及其 access。
contentType: reference
nodeTitle: See available roles
originalFilePath: user-management/rbac/role-types.md
originalUrl: 'https://docs.n8n.io/user-management/rbac/role-types'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles
layout:
  description:
    visible: false
---

# RBAC role types <a href="#rbac-role-types" id="rbac-role-types"></a>

{% hint style="info" %}
**功能可用性**

* Project Editor role 可用于 Pro Cloud 和 Self-hosted Enterprise plans。
* Project Viewer role 仅可用于 Self-hosted Enterprise 和 Cloud Enterprise plans。
{% endhint %}

在 projects 中，有三种 user roles：Admin、Editor 和 Viewer。这些 roles 控制 user 在 project 中可以做什么。一个 user 可以在不同 projects 中拥有不同 roles。

## Project Admin <a href="#project-admin" id="project-admin"></a>

Project Admin role 拥有最高 permissions。Project admins 可以：

* 管理 project settings：更改 name、删除 project。
* 管理 project members：invite members 和 remove members，更改 members 的 roles。
* View、create、update 和 delete project 内的任何 workflows、credentials 或 executions。

## Project Editor <a href="#project-editor" id="project-editor"></a>

Project Editor 可以 view、create、update 和 delete project 内的任何 workflows、credentials 或 executions。

## Project Viewer <a href="#project-viewer" id="project-viewer"></a>

Project Viewer 实际上是一个 `read-only` role，可以 access project 内的所有 workflows、credentials 和 executions。

Viewers 无法 manually execute project 中存在的任何 workflows。

{% hint style="info" %}
**Role types 和 account types**

Role types 和 [account types](../understand-account-types.md) 是不同概念。每个 account 都有一个 type。该 account 可以在不同 [projects](organize-work-in-projects.md) 中拥有不同 role types。
{% endhint %}

| Permission | Admin | Editor | Viewer |
| ---------- |------ | ------ | ------ |
| View project 中的 workflows | ✅ | ✅ | ✅ |
| View project 中的 credentials | ✅ | ✅ | ✅ |
| View executions | ✅ | ✅ | ✅ |
| Edit credentials 和 workflows | ✅ | ✅ | ❌ |
| Add workflows 和 credentials | ✅ | ✅ | ❌ |
| Execute workflows | ✅ | ✅ | ❌ |
| Manage members | ✅ | ❌ | ❌ |
| Modify project | ✅ | ❌ | ❌ |
| 在 credentials 中使用 external secrets | ✅* | ✅* | ❌ |
| Manage project secret vaults | ✅* | ❌ | ❌ |

\* 需要 instance owner 或 admin 启用 **Enable external secrets for project roles**。请参考 [Access for project roles](../../manage-credentials/use-external-secret-stores.md#access-for-project-roles)。此功能从 n8n version `2.13.0` 起可用。

[Variables](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/define-custom-variables) 和 [tags](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/manage-workflows/tag-workflows) 不受 RBAC 影响：它们在整个 n8n instance 中是 global。

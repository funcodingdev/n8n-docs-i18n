---
title: RBAC projects
contentType: howto
nodeTitle: Organize work in projects
originalFilePath: user-management/rbac/projects.md
originalUrl: https://docs.n8n.io/user-management/rbac/projects
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects
description: >-
  了解 n8n 如何使用 projects 实现 RBAC。学习如何创建和管理 projects。
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

# 在 projects 中组织 work

{% hint style="info" %}
**功能可用性**

RBAC 可用于除 Community edition 之外的所有 plans。不同 plans 拥有不同数量的 projects 和 roles。Plan details 请参考 n8n 的 [pricing page](https://n8n.io/pricing/)。
{% endhint %}

n8n 使用 projects 对 workflows 和 credentials[^1] 分组，并在每个 project 中为 users 分配 [roles](see-available-roles.md)。这意味着单个 user 可以在不同 projects 中拥有不同 roles，从而获得不同 access levels。

### 创建 project <a href="#create-a-project" id="create-a-project"></a>

Instance owners 和 instance admins 可以创建 projects。

创建 project：

1. 选择 <img src="../../.gitbook/assets/plus.png" alt="Plus icon" data-size="line"> **Add project**。
2. 填写 project settings。
3. 选择 **Save**。

### 在 project 中添加和移除 users <a href="#add-and-remove-users-in-a-project" id="add-and-remove-users-in-a-project"></a>

Project admins 可以添加和移除 users。

向 project 添加 user：

1. 选择 project。
2. 选择 **Project settings**。
3. 在 **Project members** 下，browse users 或按 username 或 email address 搜索。
4. 选择要添加的 user。
5. 检查 [role type](see-available-roles.md)，并在需要时更改。
6. 选择 **Save**。

从 project 移除 user：

1. 选择 project。
2. 选择 **Project settings**。
3. 在要移除 user 的 **three-dot menu** 中，选择 **Remove user**。
4. 选择 **Save**。

### 删除 project <a href="#delete-a-project" id="delete-a-project"></a>

删除 project：

1. 选择 project。
2. 选择 **Project settings**。
3. 选择 **Delete project**。
4. 选择如何处理 workflows 和 credentials。你可以选择：
   * **Transfer its workflows and credentials to another project**：n8n 会提示你选择一个 project，将 data 移到那里。
   * **Delete its workflows and credentials**：n8n 会提示你确认要删除 project 中的所有 data。

### 在 projects 或 users 之间移动 workflows 和 credentials <a href="#move-workflows-and-credentials-between-projects-or-users" id="move-workflows-and-credentials-between-projects-or-users"></a>

Workflow 和 credential owners 可以将 workflows 或 credentials（更改 ownership）移动到他们有 access 的其他 users 或 projects。

{% hint style="warning" %}
**Moving 会撤销 sharing**

Moving workflows 或 credentials 会移除所有 existing sharing。请注意，这可能影响当前 sharing 这些 resources 的其他 workflows。
{% endhint %}

1.  选择 **Workflow menu** <img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="Workflow menu icon" data-size="line"> 或 **Credential menu** <img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="Workflow menu icon" data-size="line"> > **Move**。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>Moving workflows with credentials</strong></p><p>移动包含 credentials 的 workflow 时，如果你有权 share credentials，可以选择同时 share credentials。这能确保 workflow 继续 access 执行所需的 credentials。n8n 会标注任何无法移动的 credentials（你没有 permission share 的 credentials）。</p></div>
2. 选择要 move to 的 project 或 user。
3. 选择 **Next**。
4. 确认你理解 move 的影响：如果 target project 中没有所需 credentials，workflows 可能停止工作，并且 n8n 会移除当前所有 individual sharing。
5. 选择 **Confirm move to new project**。

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。

---
title: Custom project roles
description: 在 n8n 中创建和管理具有 granular permissions 的 custom project roles。
contentType: howto
nodeTitle: Create custom roles
originalFilePath: user-management/rbac/custom-roles.md
originalUrl: 'https://docs.n8n.io/user-management/rbac/custom-roles'
url: >-
  https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac/create-custom-roles
layout:
  description:
    visible: false
---

# Custom project roles <a href="#custom-project-roles" id="custom-project-roles"></a>

{% hint style="info" %}
**功能可用性**

Custom roles 可用于 Self-hosted Enterprise 和 Cloud Enterprise plans。Plan details 请参考 n8n 的 [pricing page](https://n8n.io/pricing/)。

**可用版本：** n8n version 1.122.0（released November 24, 2025）

Secret vault scopes 从 n8n version `2.13.0` 起可用。
{% endhint %}

{% hint style="info" %}
**Instance roles vs project roles**

n8n 有两类 roles：
* **Instance roles**（[account types](../understand-account-types.md)）：跨整个 n8n instance 和所有 projects 的 Owner、Admin 和 Member roles
* **Project roles**：在特定 project 内应用的 roles（Admin、Editor、Viewer 和 custom roles）

Custom roles 是 project-level roles。它们定义 individual projects 内的 permissions，而不是整个 instance 范围的 permissions。
{% endhint %}

Custom project roles 允许你创建带有特定 permissions 的 roles，以适配 team needs。不同于 built-in project roles（Admin、Editor、Viewer），custom roles 让你可以定义对 workflows、credentials 和其他 project resources 的 granular access。

## 创建 custom role <a href="#create-a-custom-role" id="create-a-custom-role"></a>

Instance owners 和 instance admins 可以创建 custom roles。

创建 custom role：

1. 前往 **Settings** > **Project roles**。
2. 选择 **Create role**。
3. 输入 role name 和可选 description。
4. 为此 role 选择 permissions（scopes）：
	* **Workflow permissions**：View、execute、edit、create、publish、transfer、delete，或 manage workflows 的 data redaction
	* **Credential permissions**：View、edit、create、share、unshare、transfer 或 delete credentials
	* **Project permissions**：View、edit 或 delete projects
	* **Folder permissions**：View、edit、create、transfer 或 delete folders
	* **Execution permission**：Reveal redacted execution data
	* **Secret vault permissions**：View、create、edit、delete 或 sync project 的 secret vaults
	* **Secrets permission**：在 credentials 中使用 secrets
	* **Data table permissions**：View tables、view rows、edit tables、edit rows、create 或 delete tables
	* **Project variable permissions**：View、edit、create 或 delete project variables
	* **Source control**：Push to source control
5. 选择 **Create role**。

## 将 custom role 分配给 users <a href="#assign-a-custom-role-to-users" id="assign-a-custom-role-to-users"></a>

Project admins 可以将 custom roles 分配给 project members。Custom roles 只在被分配的特定 project 内生效。一个 user 可以在不同 projects 中拥有不同 roles。

分配 custom role：

1. 选择 project。
2. 选择 **Project settings**。
3. 在 **Project members** 下，browse 或 search users。
4. 选择 user，并从 dropdown 中选择 custom role。
5. 选择 **Save**。

{% hint style="info" %}
**Project-level permissions**

Custom role permissions 只在分配该 role 的 project 内生效。要在多个 projects 中授予相同 permissions，请在每个 project 中分别分配 custom role。
{% endhint %}

## 编辑 custom role <a href="#edit-a-custom-role" id="edit-a-custom-role"></a>

修改现有 custom role：

1. 前往 **Settings** > **Project roles**。
2. 找到要编辑的 custom role。
3. 选择 **three-dot menu** > **Edit**。
4. 更新 role name、description 或 permissions。
5. 选择 **Save changes**。

{% hint style="warning" %}
**Editing 会影响所有已分配 users**

对 custom role 的更改会立即影响在任何 project 中分配到该 role 的所有 users。如果该 role 跨多个 projects 使用，permission changes 会在该 role 被分配的所有地方生效。
{% endhint %}

## Duplicate custom role <a href="#duplicate-a-custom-role" id="duplicate-a-custom-role"></a>

基于现有 role 创建 new role：

1. 前往 **Settings** > **Project roles**。
2. 找到要 duplicate 的 role。
3. 选择 **three-dot menu** > **Duplicate**。
4. 按需修改 role name 和 permissions。
5. 选择 **Create role**。

## 删除 custom role <a href="#delete-a-custom-role" id="delete-a-custom-role"></a>

删除 custom role：

1. 前往 **Settings** > **Project roles**。
2. 找到要删除的 role。
3. 选择 **three-dot menu** > **Delete**。
4. 确认删除。

{% hint style="info" %}
**删除前重新分配 users**

如果 users 已分配到此 role，你必须先将他们重新分配到其他 role，然后才能删除它。
{% endhint %}

## Permission scopes reference <a href="#permission-scopes-reference" id="permission-scopes-reference"></a>

Custom roles 使用 permission scopes 定义 users 在 project 中可以做什么。下面每个 scope 都匹配 **Project roles** editor 中的 checkbox。Section headings 与 editor 中的 section names 一致；scope codes 是你会在 API responses 和 audit logs 中看到的内容。

{% hint style="info" %}
**Automatically granted scopes**

n8n 会将某些 scopes 配对，因此它们不会作为单独 checkbox 显示：

* 授予 `<resource>:read` 也会授予该 resource 匹配的 list scope（例如 `workflow:read` 会授予 `workflow:list`）。
* 授予 `workflow:publish` 也会授予 `workflow:unpublish`。
{% endhint %}

### Workflow scopes <a href="#workflow-scopes" id="workflow-scopes"></a>
* `workflow:create` - 创建 new workflows
* `workflow:read` - View workflow details
* `workflow:update` - Edit workflows
* `workflow:execute` - Execute workflows
* `workflow:publish` - Publish workflows（也授予 `workflow:unpublish`）
* `workflow:delete` - Delete workflows
* `workflow:move` - 在 projects 之间 transfer workflows
* `workflow:enableRedaction` - 为 workflow 开启 data redaction（参考 [Execution data redaction](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data)）
* `workflow:disableRedaction` - 为 workflow 关闭 data redaction（参考 [Execution data redaction](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data)）

### Credential scopes <a href="#credential-scopes" id="credential-scopes"></a>
* `credential:create` - 创建 new credentials
* `credential:read` - View credential details
* `credential:update` - Edit credentials
* `credential:delete` - Delete credentials
* `credential:move` - 在 projects 之间 transfer credentials
* `credential:share` - 与其他 users share credentials
* `credential:unshare` - Remove credential sharing

### Project scopes <a href="#project-scopes" id="project-scopes"></a>
* `project:read` - View project details
* `project:update` - Edit project settings
* `project:delete` - Delete projects

### Folder scopes <a href="#folder-scopes" id="folder-scopes"></a>
* `folder:create` - 创建 new folders
* `folder:read` - View folder contents
* `folder:update` - Rename folders
* `folder:delete` - Delete folders
* `folder:move` - Transfer folders

### Execution scopes <a href="#execution-scopes" id="execution-scopes"></a>
* `execution:reveal` - Reveal redacted execution data（参考 [Execution data redaction](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/redact-execution-data)）

### Secret vault scopes <a href="#secret-vault-scopes" id="secret-vault-scopes"></a>
Scope codes 使用 `externalSecretsProvider` prefix。Role editor 将此 section 列为 **Secrets vaults**。

* `externalSecretsProvider:create` - 在 project 中创建 new secret vaults
* `externalSecretsProvider:read` - View project 中的 secret vaults
* `externalSecretsProvider:update` - Edit secret vault configuration
* `externalSecretsProvider:delete` - 从 project 删除 secret vaults
* `externalSecretsProvider:sync` - Reload vault 的 secrets

### Secrets scope <a href="#secrets-scope" id="secrets-scope"></a>
Scope code 使用 `externalSecret` prefix。Role editor 将此 section 列为 **Secrets**。

* `externalSecret:list` - 在 credentials 中使用 secrets

### Data table scopes <a href="#data-table-scopes" id="data-table-scopes"></a>
* `dataTable:create` - 创建 new data tables
* `dataTable:read` - View data table schema
* `dataTable:update` - Edit data table schema
* `dataTable:delete` - Delete data tables
* `dataTable:readRow` - Read rows from data tables
* `dataTable:writeRow` - Insert 或 update data tables 中的 rows

### Project variable scopes <a href="#project-variable-scopes" id="project-variable-scopes"></a>
* `projectVariable:create` - 创建 new variables
* `projectVariable:read` - View variable values
* `projectVariable:update` - Edit variable values
* `projectVariable:delete` - Delete variables

### Source control scopes <a href="#source-control-scopes" id="source-control-scopes"></a>
* `sourceControl:push` - Push changes to source control

## Common custom role examples <a href="#common-custom-role-examples" id="common-custom-role-examples"></a>

这些是可为常见 use cases 创建的 example custom project roles。请记住，这些 roles 只在 individual projects 内生效，而不是跨整个 n8n instance 生效。

### Workflow developer <a href="#workflow-developer" id="workflow-developer"></a>
适合只处理 workflows 的 users：
* `workflow:create`、`workflow:read`、`workflow:update`、`workflow:execute`、`workflow:delete`
* `credential:read`（view credentials，但不 edit）
* `project:read`

### Credential manager <a href="#credential-manager" id="credential-manager"></a>
适合管理 credentials 的 users：
* `credential:create`、`credential:read`、`credential:update`、`credential:delete`、`credential:share`
* `workflow:read`（view workflows 以了解 credential usage）
* `project:read`

### Secrets user <a href="#secrets-user" id="secrets-user"></a>
适合在 credentials 中使用 external secrets、但不管理 vaults 的 users：
* `externalSecret:list`（在 credential expressions 中使用 secrets）
* `credential:create`、`credential:read`、`credential:update`（使用 secrets 管理 credentials）
* `workflow:read`
* `project:read`

### Workflow publisher <a href="#workflow-publisher" id="workflow-publisher"></a>
适合可以 publish workflows、但没有完整 edit access 的 users：
* `workflow:read`、`workflow:publish`
* `credential:read`
* `project:read`

{% hint style="info" %}
**Combining scopes**

你可以组合任意 scopes，创建匹配具体 needs 的 roles。请考虑 least privilege principle：只授予 users 完成 tasks 所需的 permissions。
{% endhint %}

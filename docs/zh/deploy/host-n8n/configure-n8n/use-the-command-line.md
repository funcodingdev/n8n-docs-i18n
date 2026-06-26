---
contentType: reference
nodeTitle: Use the command line
originalFilePath: hosting/cli-commands.md
originalUrl: https://docs.n8n.io/hosting/cli-commands
url: https://docs.n8n.io/deploy/host-n8n/configure-n8n/use-the-command-line
description: Server CLI 中可用的命令，Server CLI 是 n8n 内置的 command-line interface。
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

# 使用命令行

**Server CLI** 是一个内置 command-line interface，运行在与 n8n 安装相同的机器上。它为管理任务提供直接 database access，并且即使 n8n 未运行，也可以执行大多数命令。

{% hint style="info" %}
**n8n CLI**

想从远程机器以编程方式与 n8n 交互，或与 AI agents 集成？请查看 [n8n CLI](https://app.gitbook.com/o/gkeAaBEvbwHB2NmepVHG/s/r7wKI4I1BgdBCuq5Cvcx/)。
{% endhint %}

## 何时使用 Server CLI 与 n8n CLI <a href="#when-to-use-server-cli-vs-n8n-cli" id="when-to-use-server-cli-vs-n8n-cli"></a>

| Feature | Server CLI | n8n CLI |
| ------------------------ | ------------------------------------------------------------- | -------------------------------------------------------- |
| **运行位置** | 与 n8n 相同的机器 | 任何可访问网络的机器 |
| **Authentication** | Direct database access | API key |
| **是否要求 n8n 运行** | 否（大多数命令） | 是 |
| **最适合** | Instance operators、backups、migrations | Programmers、AI agents、remote management |
| **Security model** | 绕过 access controls | 遵守 user permissions 和 API key scope |
| **Use case examples** | Backup/restore、license management、emergency password resets | Workflow automation、通过代码管理 credentials |

## 运行 CLI commands <a href="#running-cli-commands" id="running-cli-commands"></a>

你可以在自托管 n8n 中使用 CLI commands。根据你选择的 n8n 安装方式，运行命令的方式有所不同：

* npm：`n8n` 命令可直接使用。下面示例使用这种方式。
*   Docker：`n8n` 命令可在 Docker container 内使用：

    ```sh
    docker exec -u node -it <n8n-container-name> <n8n-cli-command>
    ```

## 启动 workflow <a href="#start-a-workflow" id="start-a-workflow"></a>

你可以直接使用 CLI 启动 workflows。

按 ID 执行已保存的 workflow：

```bash
n8n execute --id <ID>
```

## Publish 或 unpublish workflow <a href="#publish-or-unpublish-a-workflow" id="publish-or-unpublish-a-workflow"></a>

你可以使用 CLI publish 或 unpublish workflow。在 n8n 2.0 中，[此前的 active/inactive toggle](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/v20-breaking-changes) 被 publish/unpublish model 取代。使用 `publish:workflow` 和 `unpublish:workflow` 从 CLI 更改 workflow 的 published state。

{% hint style="info" %}
**需要重启**

这些命令会操作 n8n database。如果你在 n8n 运行时执行它们，更改要到重启 n8n 后才会生效。
{% endhint %}

### Publish workflow <a href="#publish-a-workflow" id="publish-a-workflow"></a>

使用 `publish:workflow` 按 ID publish workflow。你也可以传入 `versionId` 来 publish 特定 historical version。

命令 flags：

| Flag | Description |
| ----------- | --------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --id | 要 publish 的 workflow ID。必填。 |
| --versionId | 要 publish 的可选 version ID。省略时，会 publish 当前 draft。 |

{% hint style="info" %}
**没有 `--all` flag**

与已弃用的 `update:workflow` 命令不同，`publish:workflow` 不支持 `--all`。这是有意设计：它可以防止在生产环境中意外批量 publish workflows。请按 ID 逐个 publish workflows。
{% endhint %}

按 ID publish workflow 的当前 draft：

```bash
n8n publish:workflow --id=<ID>
```

Publish workflow 的特定 historical version：

```bash
n8n publish:workflow --id=<ID> --versionId=<VERSION_ID>
```

### 取消 publish workflow <a href="#unpublish-a-workflow" id="unpublish-a-workflow"></a>

使用 `unpublish:workflow` 按 ID unpublish workflow，或一次性 unpublish 所有 workflows。

命令 flags：

| Flag | Description |
| ------ | ---------------------------------------------------------------- |
| --help | 帮助提示。 |
| --id | 要 unpublish 的 workflow ID。不能与 `--all` 一起使用。 |
| --all | 取消 publish 所有 workflows。不能与 `--id` 一起使用。 |

按 ID unpublish workflow：

```bash
n8n unpublish:workflow --id=<ID>
```

取消 publish 所有 workflows：

```bash
n8n unpublish:workflow --all
```

### update:workflow（已弃用） <a href="#updateworkflow-deprecated" id="updateworkflow-deprecated"></a>

{% hint style="warning" %}
**在 n8n 2.0 中弃用**

`update:workflow` 命令已弃用，并将被移除。请改用 [`publish:workflow`](use-the-command-line.md#publish-a-workflow) 和 [`unpublish:workflow`](use-the-command-line.md#unpublish-a-workflow)。详情请参阅 [n8n v2.0 breaking changes](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/v20-breaking-changes)。
{% endhint %}

按 ID 将 workflow 的 active status 设置为 false：

```bash
n8n update:workflow --id=<ID> --active=false
```

按 ID 将 workflow 的 active status 设置为 true：

```bash
n8n update:workflow --id=<ID> --active=true
```

将所有 workflows 的 active status 设置为 false：

```bash
n8n update:workflow --all --active=false
```

将所有 workflows 的 active status 设置为 true：

```bash
n8n update:workflow --all --active=true
```

## 导出 entities <a href="#export-entities" id="export-entities"></a>

你可以使用 CLI 从 n8n export database entities。此工具允许你从一种 database type（例如 SQLite）export 所有 entity types，并将它们 import 到另一种 database type（例如 Postgres）。

命令 flags：

| Flag | Description |
| ----------------------------------- | ---------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --outputDir | Output directory path |
| --includeExecutionHistoryDataTables | 包含 execution history data tables。默认排除它们，因为它们可能非常大 |

```bash
n8n export:entities --outputDir=./outputs --includeExecutionHistoryDataTables=true
```

## Export workflows 和 credentials <a href="#export-workflows-and-credentials" id="export-workflows-and-credentials"></a>

你可以使用 CLI 从 n8n export workflows 和 credentials。

命令 flags：

| Flag | Description |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --all | Export 所有 workflows/credentials。 |
| --backup | 为 backups 设置 --all --pretty --separate。你也可以选择设置 --output。 |
| --id | 要 export 的 workflow ID。 |
| --output, -o | 使用 separate files 时，输出 file name 或 directory。 |
| --pretty | 将输出格式化为更易阅读的形式。 |
| --separate | 每个 workflow export 一个文件（便于 versioning）。必须使用 --output 设置 directory。 |
| --decrypted | 以 plain text format export credentials。（仅 credentials。） |
| --version | 要 export 的特定 historical version 的 version ID。（仅 workflows，不能与 `--all` 或 `--published` 一起使用。） |
| --published | Export workflow 的 published/active version，而不是当前 draft。与 `--all` 组合使用时，会跳过 unpublished workflows。（仅 workflows，不能与 `--version` 一起使用。） |

### Workflows <a href="#workflows" id="workflows"></a>

将所有 workflows export 到 standard output（terminal）：

```bash
n8n export:workflow --all
```

按 ID export workflow，并指定 output file name：

```bash
n8n export:workflow --id=<ID> --output=file.json
```

将所有 workflows export 到特定 directory 中的单个文件：

```bash
n8n export:workflow --all --output=backups/latest/file.json
```

使用 `--backup` flag 将所有 workflows export 到特定 directory（详情见上文）：

```bash
n8n export:workflow --backup --output=backups/latest/
```

#### Export 特定 workflow version <a href="#export-a-specific-workflow-version" id="export-a-specific-workflow-version"></a>

你可以传入 `versionId` 和 `--version`，export workflow 的特定 historical version：

```bash
n8n export:workflow --id=<ID> --version=<VERSION_ID> --output=workflow-v1.json
```

#### Export workflow 的 published version <a href="#export-the-published-version-of-a-workflow" id="export-the-published-version-of-a-workflow"></a>

使用 `--published` export workflow 当前 published/active version，而不是当前 draft：

```bash
n8n export:workflow --id=<ID> --published --output=published.json
```

你可以将 `--published` 与 `--all` 组合，export 每个 workflow 的 published version。没有 published version 的 workflows 会被跳过：

```bash
n8n export:workflow --all --published --output=workflows.json
```

{% hint style="info" %}
**Version metadata**

Export workflow 时，n8n 会包含 `versionMetadata` property，其中包含该 version 的 workflow historical name 和 description。Import 命令会在 import 时将这些数据保留在 workflow history table 中。当前 workflow 的 name 和 description 不会被覆盖。
{% endhint %}

### Credentials <a href="#credentials" id="credentials"></a>

将所有 credentials export 到 standard output（terminal）：

```bash
n8n export:credentials --all
```

按 ID export credentials，并指定 output file name：

```bash
n8n export:credentials --id=<ID> --output=file.json
```

将所有 credentials export 到特定 directory 中的单个文件：

```bash
n8n export:credentials --all --output=backups/latest/file.json
```

使用 `--backup` flag 将所有 credentials export 到特定 directory（详情见上文）：

```bash
n8n export:credentials --backup --output=backups/latest/
```

以 plain text format export 所有 credentials。你可以用它从一个 installation 迁移到另一个 configuration file 中有不同 secret key 的 installation。

{% hint style="warning" %}
**敏感信息**

所有敏感信息都会在文件中可见。
{% endhint %}

```bash
n8n export:credentials --all --decrypted --output=backups/decrypted.json
```

## 导入 entities <a href="#import-entities" id="import-entities"></a>

你可以使用此命令从之前的 `export:entities` command import entities，它允许将 entities import 到与 export 时不同的 database type。当前支持的 database types 包括：SQLite、Postgres。

Import 前预期 database 为空；可以使用 `--truncateTables` 参数强制清空。

命令 flags：

| Flag | Description |
| ---------------- | -------------------------------------------------- |
| --help | 帮助提示。 |
| --inputDir | 保存 import output files 的 input directory |
| --truncateTables | Import 前 truncate tables |

```bash
n8n import:entities --inputDir ./outputs --truncateTables true
```

## Import workflows 和 credentials <a href="#import-workflows-and-credentials" id="import-workflows-and-credentials"></a>

你可以使用 CLI 将 workflows 和 credentials import 到 n8n。

{% hint style="warning" %}
**更新 IDs**

Export workflows 和 credentials 时，n8n 也会 export 它们的 IDs。如果现有 database 中有相同 IDs 的 workflows 和 credentials，它们会被覆盖。为避免这种情况，请在 import 前删除或更改 IDs。
{% endhint %}

可用 flags：

| Flag | Description |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| --help | 帮助提示。 |
| --input | 如果使用 --separate，则为 input file name 或 directory。 |
| --projectId | 将 workflow 或 credential import 到指定 project。不能与 `--userId` 一起使用。 |
| --separate | 从 --input 提供的 directory import `*.json` files。 |
| --userId | 将 workflow 或 credential import 到指定 user。不能与 `--projectId` 一起使用。 |
| --skipMigrationChecks | 跳过 migration validation checks。 |
| --activeState | 控制 imported workflows 的 active state。接受 `false`（默认，停用所有 imported workflows）或 `fromJson`（使用每个 workflow JSON 中的 `active` 字段；仅 multi-main mode）。 |

{% hint style="info" %}
**迁移到 SQLite**

n8n 将 workflow 和 credential names 限制为 128 个字符，但 SQLite 不强制 size limits。

这可能在 import 过程中导致 **Data too long for column name** 等错误。

在这种情况下，你可以在 n8n interface 中编辑 names 并重新 export，或在 import 前直接编辑 JSON file。
{% endhint %}

### Workflows <a href="#workflows" id="workflows"></a>

{% hint style="warning" %}
**已知问题：cron triggers 在 import 后继续运行**

Import 之前 active workflow 的行为会因运行模式而异。这是一个已知 bug。

在 multi-main 和 queue-mode instances 上，之前 active workflow 的 cron triggers 会在 import 时停用。

在非 multi-main instances 上，之前 active workflows 的 cron triggers 会继续运行，直到你重启 n8n instance。
{% endhint %}

从特定文件 import workflows：

```bash
n8n import:workflow --input=file.json
```

从指定 directory import 所有 JSON workflow files：

```bash
n8n import:workflow --separate --input=backups/latest/
```

{% hint style="info" %}
**Import 时的 version metadata**

如果 imported file 包含 `versionMetadata` property（由面向特定 version 或 published version 的 exports 添加），n8n 会在 workflow history table 中保留该 historical name 和 description。当前 workflow entity 的 name 和 description 会保持原样。
{% endhint %}

默认情况下，`import:workflow` 会停用每个 imported workflow。要改为保留每个 JSON file 中的 `active` 字段，请传入 `--activeState=fromJson`（仅支持 multi-main 和 queue mode）：

```bash
n8n import:workflow --separate --input=backups/latest/ --activeState=fromJson
```

### Credentials <a href="#credentials" id="credentials"></a>

从特定文件 import credentials：

```bash
n8n import:credentials --input=file.json
```

从指定 directory import 所有 JSON credentials files：

```bash
n8n import:credentials --separate --input=backups/latest/
```

## License <a href="#license" id="license"></a>

### Clear <a href="#clear" id="clear"></a>

从 n8n database 清除现有 license，并将 n8n 重置为默认 features：

```sh
n8n license:clear
```

如果你的 license 包含 [floating entitlements](#user-content-fn-1)[^1]，运行此命令还会尝试将它们释放回 pool，让其他 instances 可以使用。

### Info <a href="#info" id="info"></a>

显示现有 license 信息：

```sh
n8n license:info
```

## User management <a href="#user-management" id="user-management"></a>

你可以使用 n8n CLI reset user management。这会将 user management 恢复到 setup 前状态，并移除所有 user accounts。

如果你忘记 password，且没有设置 SMTP 通过 email reset password，请使用此命令。

```sh
n8n user-management:reset
```

### 为 user 禁用 MFA <a href="#disable-mfa-for-a-user" id="disable-mfa-for-a-user"></a>

如果 user 丢失 recovery codes，你可以使用此命令为该 user 禁用 MFA。然后该 user 可以重新登录并再次设置 MFA。

```sh
n8n mfa:disable --email=johndoe@example.com
```

### 禁用 LDAP <a href="#disable-ldap" id="disable-ldap"></a>

你可以使用下面的命令 reset LDAP settings。

```sh
n8n ldap:reset
```

## Uninstall community nodes 和 credentials <a href="#uninstall-community-nodes-and-credentials" id="uninstall-community-nodes-and-credentials"></a>

你可以使用 n8n CLI 管理 [community nodes](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/community-nodes/installation-and-management)。目前，你只能 uninstall community nodes 和 credentials；如果 community node 导致不稳定，这会很有用。

命令 flags：

| Flag | Description |
| ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| --help | 显示 CLI help。 |
| --credential | Credential type。访问 node 的 `<NODE>.credential.ts` 文件，并获取 `name` 的值。 |
| --package | Community node 的 package name。 |
| --uninstall | Uninstall node。 |
| --userId | 拥有 credential 的 user ID。自托管时查询 database；cloud 上使用 API key 查询 API。 |

### Nodes <a href="#nodes" id="nodes"></a>

按 package name uninstall community node：

```sh
n8n community-node --uninstall --package <COMMUNITY_NODE_NAME>
```

例如，要 uninstall [Evolution API community node](https://www.npmjs.com/package/n8n-nodes-evolution-api)，请输入：

```sh
n8n community-node --uninstall --package n8n-nodes-evolution-api
```

### Credentials <a href="#credentials" id="credentials"></a>

Uninstall community node credential：

```sh
n8n community-node --uninstall --credential <CREDENTIAL_TYPE> --userId <ID>
```

例如，要 uninstall [Evolution API community node credential](https://www.npmjs.com/package/n8n-nodes-evolution-api)，请访问 [repository](https://github.com/oriondesign2015/n8n-nodes-evolution-api)，并导航到 [`credentials.ts` file](https://github.com/oriondesign2015/n8n-nodes-evolution-api/blob/main/credentials/EvolutionApi.credentials.ts) 查找 `name`：

```sh
n8n community-node --uninstall --credential evolutionApi --userId 1234
```

## 安全审计 <a href="#security-audit" id="security-audit"></a>

你可以在 n8n instance 上运行 [security audit](security/run-security-audits.md)，以检测常见安全问题。

```sh
n8n audit
```

[^1]: 在 n8n 中，entitlements 会授予 n8n instances 在特定时间段内访问 plan-restricted features 的权限。

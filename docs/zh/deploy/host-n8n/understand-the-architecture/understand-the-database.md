---
description: 了解 n8n database structure
contentType: explanation
nodeTitle: Understand the database
originalFilePath: hosting/architecture/database-structure.md
originalUrl: 'https://docs.n8n.io/hosting/architecture/database-structure'
url: >-
  https://docs.n8n.io/deploy/host-n8n/understand-the-architecture/understand-the-database
layout:
  description:
    visible: false
---

# Database structure <a href="#database-structure" id="database-structure"></a>

本页面说明 n8n database 中每张 table 的用途。

## Database 和 query technology <a href="#database-and-query-technology" id="database-and-query-technology"></a>

默认情况下，n8n 使用 SQLite 作为 database。如果你使用其他 database，structure 会类似，但 data types 可能因 database 而异。

n8n 使用 [TypeORM](https://github.com/typeorm/typeorm) 进行 queries 和 migrations。

要检查 n8n database，可以使用 [DBeaver](https://dbeaver.io)。它是一个 open-source universal database tool。

## Tables <a href="#tables" id="tables"></a>

这些是 n8n 在 setup 期间创建的 tables。

### auth_identity <a href="#authidentity" id="authidentity"></a>

使用 [SAML](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/verify-user-identity/use-saml) 时，存储 external authentication providers 的 details。

### auth_provider_sync_history <a href="#authprovidersynchistory" id="authprovidersynchistory"></a>

存储 SAML connection 的 history。

### credentials_entity <a href="#credentialsentity" id="credentialsentity"></a>

存储用于向 integrations 进行 authentication 的 credentials[^1]。

### event_destinations <a href="#eventdestinations" id="eventdestinations"></a>

包含 [Log streaming](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/observe-and-log/stream-logs-to-external-systems) 的 destination configurations。

### execution_data <a href="#executiondata" id="executiondata"></a>

包含运行时的 workflow，以及 execution data。

### execution_entity <a href="#executionentity" id="executionentity"></a>

存储所有已保存的 workflow executions。Workflow settings 会影响 n8n 保存哪些 executions。

### execution_metadata <a href="#executionmetadata" id="executionmetadata"></a>

存储 [Custom executions data](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/understand-workflows/understand-executions/customize-executions-data)。

### installed_nodes <a href="#installednodes" id="installednodes"></a>

列出安装在你的 n8n instance 中的 [community nodes](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/community-nodes/installation-and-management)。

### installed_packages <a href="#installedpackages" id="installedpackages"></a>

列出安装在你的 n8n instance 中的 npm community nodes packages 的 details。[installed_nodes](#installed_nodes) 会列出每个 individual node。`installed_packages` 会列出 npm packages，而一个 package 可能包含多个 nodes。

### migrations <a href="#migrations" id="migrations"></a>

所有 database migrations 的 log。更多信息请阅读 TypeORM 文档中的 [Migrations](https://typeorm.io/docs/advanced-topics/migrations/)。

### project <a href="#project" id="project"></a>

列出 instance 中的 [projects](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects)。

### project_relation <a href="#projectrelation" id="projectrelation"></a>

描述 user 与 [project](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/set-permissions-and-roles-rbac/organize-work-in-projects) 之间的关系，包括 user 的 [role type](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles)。

### role <a href="#role" id="role"></a>

当前未使用。预留给未来 custom roles 相关工作使用。

### settings <a href="#settings" id="settings"></a>

记录 custom instance settings。这些 settings 不能通过 environment variables 控制。它们包括：

* 是否已设置 instance owner
* 用户是否选择跳过 owner 和 user management setup
* 是否启用某些 authentication 类型，包括 SAML 和 LDAP
* License key

### shared_credentials <a href="#sharedcredentials" id="sharedcredentials"></a>

将 credentials 映射到 users。

### shared_workflow <a href="#sharedworkflow" id="sharedworkflow"></a>

将 workflows 映射到 users。

### tag_entity <a href="#tagentity" id="tagentity"></a>

n8n instance 中创建的所有 workflow tags。此 table 会列出 tags。[workflows_tags](#workflows_tags) 记录哪些 workflows 拥有哪些 tags。

### user <a href="#user" id="user"></a>

包含 user data。

### variables <a href="#variables" id="variables"></a>

存储 [variables](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/code-in-n8n/define-custom-variables)。

### webhook_entity <a href="#webhookentity" id="webhookentity"></a>

记录你的 n8n instance workflows 中的 active webhooks。这不只是 Webhook node 中使用的 webhooks，也包括任何 trigger node 使用的所有 active webhooks。

### workflow_entity <a href="#workflowentity" id="workflowentity"></a>

你的 n8n instance 中已保存的 workflows。

### workflow_history <a href="#workflowhistory" id="workflowhistory"></a>

存储 workflows 的 previous versions。

### workflow_statistics <a href="#workflowstatistics" id="workflowstatistics"></a>

统计 workflow IDs 及其 status。

### workflows_tags <a href="#workflowstags" id="workflowstags"></a>

将 tags 映射到 workflows。[tag_entity](#tag_entity) 包含 tag details。

## Entity Relationship Diagram (ERD) <a href="#entity-relationship-diagram-erd" id="entity-relationship-diagram-erd"></a>

!["n8n ERD"](../../.gitbook/assets/n8n-database-diagram.png)

[^1]: 在 n8n 中，credentials 存储用于连接特定 apps 和 services 的 authentication information。使用你的 authentication information（username 和 password、API key、OAuth secrets 等）创建 credentials 后，你可以使用关联的 app node 与 service 交互。

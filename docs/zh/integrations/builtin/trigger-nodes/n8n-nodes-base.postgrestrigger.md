---
title: Postgres Trigger node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Postgres Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger
description: >-
  了解如何在 n8n 中使用 Postgres Trigger node。按照技术文档将 Postgres
  Trigger node 集成到你的 workflow 中。
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

# Postgres Trigger

使用 Postgres Trigger node 响应 [Postgres](https://www.postgresql.org/) 中的事件，并将 Postgres 与其他应用程序集成。n8n 内置支持响应 insert、update 和 delete 事件。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/postgres.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Postgres Trigger integrations](https://n8n.io/integrations/postgres-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

你可以配置 node 监听事件的方式。

* 选择 **Listen and Create Trigger Rule**，然后选择要监听的事件：
  * Insert
  * Update
  * Delete
* 选择 **Listen to Channel**，然后输入 node 应监控的频道名称。

{% hint style="info" %}
**Postgres 事件监听器和必需的数据库权限**

* 为了监听 trigger 事件，n8n 会在目标表上自动创建一个 Postgres trigger。该 trigger 会在你激活 workflow 时添加，并在你停用 workflow 时移除。
* 如果你的 workflow 处于未激活状态，当你测试 workflow 时也会添加该 trigger，并在测试事件监听停止后移除。
* Postgres trigger 会调用一个自动创建的 procedure，通知 n8n 该事件。
* 你的 Postgres credential 中的用户必须拥有创建和执行 trigger 及 procedure 的权限。在 PostgreSQL 中，这需要 superuser 访问权限、表所有权或 TRIGGER 权限，以及 procedure 所在 schema 上的 CREATE 权限。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Postgres 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.postgres/)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/postgres-trigger/)。

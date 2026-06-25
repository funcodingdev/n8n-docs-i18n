---
title: Asana node documentation
description: >-
  了解如何在 n8n 中使用 Asana node。按照技术文档将 Asana node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Asana node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.asana.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.asana'
layout:
  description:
    visible: false
---

# Asana node <a href="#asana-node" id="asana-node"></a>

使用 Asana node 自动化 Asana 中的工作，并将 Asana 与其他应用集成。n8n 内置支持大量 Asana 功能，包括创建、更新、删除和获取 user、task、project 与 subtask。

在本页中，你可以找到 Asana node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Asana credentials](../credentials/asana.md)。
{% endhint %}

{% hint style="info" %}
**更新到 1.22.2 或更高版本**

由于 Asana API 变更，此 node 中的一些操作自 2023 年 1 月 17 日起停止工作。请升级到 n8n 1.22.2 或更高版本。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Project
    * Create a new project
    * Delete a project
    * Get a project
    * Get all projects
    * Update a project
* Subtask
    * Create a subtask
    * Get all subtasks
* Task
    * Create a task
    * Delete a task
    * Get a task
    * Get all tasks
    * Move a task
    * Search for tasks
    * Update a task
* Task Comment
    * Add a comment to a task
    * Remove a comment from a task
* Task Tag
    * Add a tag to a task
    * Remove a tag from a task
* Task Project
    * Add a task to a project
    * Remove a task from a project
* User
    * Get a user
    * Get all users

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Asana node 文档集成模板](https://n8n.io/integrations/asana)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

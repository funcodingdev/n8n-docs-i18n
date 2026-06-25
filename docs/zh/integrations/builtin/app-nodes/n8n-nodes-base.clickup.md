---
title: ClickUp node documentation
description: >-
  了解如何在 n8n 中使用 ClickUp node。按照技术文档将 ClickUp node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: ClickUp node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.clickup.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.clickup'
layout:
  description:
    visible: false
---

# ClickUp node <a href="#clickup-node" id="clickup-node"></a>

使用 ClickUp node 自动化 ClickUp 中的工作，并将 ClickUp 与其他应用集成。n8n 内置支持大量 ClickUp 功能，包括创建、获取、删除和更新 folder、checklist、tag、comment 与 goal。

在本页中，你可以找到 ClickUp node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [ClickUp credentials](../credentials/clickup.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Checklist
    * 创建 checklist
    * 删除 checklist
    * 更新 checklist
* Checklist Item
    * 创建 checklist item
    * 删除 checklist item
    * 更新 checklist item
* Comment
    * 创建 comment
    * 删除 comment
    * 获取所有 comment
    * 更新 comment
* Folder
    * 创建 folder
    * 删除 folder
    * 获取 folder
    * 获取所有 folder
    * 更新 folder
* Goal
    * 创建 goal
    * 删除 goal
    * 获取 goal
    * 获取所有 goal
    * 更新 goal
* Goal Key Result
    * 创建 key result
    * 删除 key result
    * 更新 key result
* List
    * 创建 list
    * 检索 list 的 custom field
    * 删除 list
    * 获取 list
    * 获取所有 list
    * 获取 list member
    * 更新 list
* Space Tag
    * 创建 space tag
    * 删除 space tag
    * 获取所有 space tag
    * 更新 space tag
* Task
    * 创建 task
    * 删除 task
    * 获取 task
    * 获取所有 task
    * 获取 task member
    * 设置 custom field
    * 更新 task
* Task List
    * 将 task 添加到 list
    * 从 list 中移除 task
* Task Tag
    * 将 tag 添加到 task
    * 从 task 中移除 tag
* Task Dependency
    * 创建 task dependency
    * 删除 task dependency
* Time Entry
    * 创建 time entry
    * 删除 time entry
    * 获取 time entry
    * 获取所有 time entry
    * 启动 time entry
    * 停止当前运行的 timer
    * 更新 time entry
* Time Entry Tag
    * 将 tag 添加到 time entry
    * 获取所有 time entry tag
    * 从 time entry 中移除 tag

## 操作详情 <a href="#operation-details" id="operation-details"></a>

### Get a task <a href="#get-a-task" id="get-a-task"></a>

使用 **Get a task** 操作时，可以选择启用以下选项：

- **Include Subtasks**：启用后，还会获取并包含指定 task 的 subtask。
- **Include Markdown Description**：启用后，在响应中包含 `markdown_description` 字段，用于保留 task description 中的链接和格式。如果 task description 包含链接或富格式，此选项很有用。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 ClickUp node 文档集成模板](https://n8n.io/integrations/clickup)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

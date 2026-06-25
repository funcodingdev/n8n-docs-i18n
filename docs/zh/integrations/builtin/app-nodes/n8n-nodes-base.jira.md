---
title: Jira Software node documentation
description: >-
  了解如何在 n8n 中使用 Jira Software node。按照技术文档将 Jira Software node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Jira Software node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.jira.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jira'
layout:
  description:
    visible: false
---

# Jira Software node <a href="#jira-software-node" id="jira-software-node"></a>

使用 Jira Software node 自动化 Jira 中的工作，并将 Jira 与其他应用集成。n8n 内置支持大量 Jira 功能，包括创建、更新、删除和获取 issue 与 user。

在本页中，你可以找到 Jira Software node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Jira credentials](../credentials/jira.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Issue
    * 获取 issue changelog
    * 创建新 issue
    * 删除 issue
    * 获取 issue
    * 获取所有 issue
    * 为 issue 创建 email notification，并将其添加到 mail queue
    * 根据 issue 的状态，返回所有 transition，或返回 user 可对 issue 执行的 transition
    * 更新 issue
* Issue Attachment
    * 向 issue 添加 attachment
    * 获取 attachment
    * 获取所有 attachment
    * 移除 attachment
* Issue Comment
    * 向 issue 添加 comment
    * 获取 comment
    * 获取所有 comment
    * 移除 comment
    * 更新 comment
* User
    * 创建新 user。
    * 删除 user。
    * 检索 user。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Jira Software node 文档集成模板](https://n8n.io/integrations/jira-software)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

要了解 Jira Query Language (JQL) 的更多信息，请参阅[官方 JQL 文档](https://www.atlassian.com/software/jira/guides/expand-jira/jql)。

## 获取特定 project 的 issue <a href="#fetch-issues-for-a-specific-project" id="fetch-issues-for-a-specific-project"></a>

**Get All** 操作会返回 Jira 中的所有 issue。要获取特定 project 的 issue，你需要使用 Jira Query Language (JQL)。

例如，如果你想接收名为 `n8n` 的 project 的所有 issue，可以这样做：

- 从 **Operation** 下拉列表中选择 **Get All**。
- 将 **Return All** 开关设为 true。
- 选择 **Add Option**，然后选择 **JQL**。
- 在 **JQL** 字段中输入 `project=n8n`。

此 query 会获取名为 `n8n` 的 project 中的所有 issue。将 `n8n` 替换为你的 project 名称，即可获取你的 project 的所有 issue。

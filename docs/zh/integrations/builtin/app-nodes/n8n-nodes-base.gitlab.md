---
title: GitLab node documentation
description: >-
  了解如何在 n8n 中使用 GitLab node。按照技术文档将 GitLab node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: GitLab node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.gitlab.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.gitlab'
layout:
  description:
    visible: false
---

# GitLab node <a href="#gitlab-node" id="gitlab-node"></a>

使用 GitLab node 自动化 GitLab 中的工作，并将 GitLab 与其他应用集成。n8n 内置支持大量 GitLab 功能，包括创建、更新、删除和编辑 issue、repository、release 与 user。

在本页中，你可以找到 GitLab node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [GitLab credentials](../credentials/gitlab.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* File
    * Create
    * Delete
    * Edit
    * Get
    * List
* Issue
    * 创建新 issue
    * 在 issue 上创建新 comment
    * 编辑 issue
    * 获取单个 issue 的数据
    * 锁定 issue
* Release
    * 创建新 release
    * 删除新 release
    * 获取新 release
    * 获取所有 release
    * 更新新 release
* Repository
    * 获取单个 repository 的数据
    * 返回 repository 的 issue
* User
    * 返回 user 的 repository

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 GitLab node 文档集成模板](https://n8n.io/integrations/gitlab)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [GitLab 文档](https://docs.gitlab.com/ee/api/rest/)。

n8n 为 GitLab 提供 trigger node。你可以在[这里](../trigger-nodes/n8n-nodes-base.gitlabtrigger.md)找到 trigger node 文档。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

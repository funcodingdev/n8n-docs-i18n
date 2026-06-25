---
title: GitLab Trigger node 文档
description: >-
  了解如何在 n8n 中使用 GitLab Trigger node。按照技术文档将 GitLab Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: GitLab Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.gitlabtrigger
layout:
  description:
    visible: false
---

# GitLab Trigger node <a href="#gitlab-trigger-node" id="gitlab-trigger-node"></a>

[GitLab](https://gitlab.com/) 是基于 Web 的 DevOps 生命周期工具，提供 Git 仓库管理器，并包含 wiki、issue 跟踪和持续集成/持续安装 pipeline 功能。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/gitlab.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [GitLab Trigger integrations](https://n8n.io/integrations/gitlab-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 评论
* 机密 issue
* 机密评论
* 部署
* Issue
* Job
* Merge request
* Pipeline
* Push
* Release
* Tag
* Wiki 页面

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 GitLab 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.gitlab.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/gitlab-trigger/)。

有关其 API 的详细信息，请参阅 [GitLab 的文档](https://docs.gitlab.com/api/rest/)。

---
title: Jenkins node documentation
description: >-
  了解如何在 n8n 中使用 Jenkins node。按照技术文档将 Jenkins node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Jenkins node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.jenkins.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.jenkins'
layout:
  description:
    visible: false
---

# Jenkins node <a href="#jenkins-node" id="jenkins-node"></a>

使用 Jenkins node 自动化 Jenkins 中的工作，并将 Jenkins 与其他应用集成。n8n 内置支持大量 Jenkins 功能，包括列出 build、管理 instance，以及创建和复制 job。

在本页中，你可以找到 Jenkins node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Jenkins credentials](../credentials/jenkins.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Build
    * 列出 Build
* Instance
    * 取消 quiet down 状态
    * 将 Jenkins 置于 quiet mode；无法启动 build，Jenkins 已准备好关闭
    * 在可行环境中立即重启 Jenkins
    * 在可行环境中等待没有 job 运行后重启 Jenkins
    * 等待没有 job 运行后关闭
    * 立即关闭 Jenkins
* Job
    * 复制特定 job
    * 创建新 job
    * 触发特定 job
    * 触发特定 job

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Jenkins node 文档集成模板](https://n8n.io/integrations/jenkins)或[搜索所有模板](https://n8n.io/workflows/)

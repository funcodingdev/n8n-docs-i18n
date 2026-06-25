---
title: n8n 集成文档和指南
contentType: overview
hide:
  - feedback
  - kapaButton
nodeTitle: 集成
originalFilePath: integrations/index.md
originalUrl: https://docs.n8n.io/integrations
url: https://docs.n8n.io/integrations/
description: >-
  访问 n8n 集成文档和指南。查找全面资源，帮助你掌握如何使用不同类型的 node 集成 app，并改进自动化 workflow。
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
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Node

n8n 将集成称为 node。

Node 是 n8n 中 workflow 的构建块。它们可以是检索数据的入口、处理数据的函数，或者发送数据的出口。数据处理包括过滤、重组和更改数据。你的 API、服务或 app 可以有一个或多个 node。你可以连接多个 node，从而创建复杂的 workflow。

## 内置 node <a href="#built-in-nodes" id="built-in-nodes"></a>

n8n 包含一组内置集成。有关所有 n8n 内置 node 的文档，请参阅[内置 node](builtin/node-types.md)。

## 社区 node <a href="#community-nodes" id="community-nodes"></a>

除了使用内置 node，你还可以安装社区构建的 node。更多信息请参阅[社区 node](community-nodes/installation-and-management/)。

## 仅 credential 的 node 和自定义 operation <a href="#credential-only-nodes-and-custom-operations" id="credential-only-nodes-and-custom-operations"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/k23mQunNshTkLRuOqark/" %}

更多信息请参阅[自定义 operation](builtin/custom-api-actions-for-existing-nodes.md)。

## 通用集成 <a href="#generic-integrations" id="generic-integrations"></a>

如果需要连接到 n8n 没有对应 node 或仅 credential node 的服务，你仍然可以使用 [HTTP Request](builtin/core-nodes/n8n-nodes-base.httprequest/) node。有关如何设置身份验证并创建 API 调用的详细信息，请参阅该 node 页面。

## 下一步 <a href="#where-to-go-next" id="where-to-go-next"></a>

* 如果想创建自己的 node，请前往[创建 node](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/create-nodes/overview) 部分。
* 查看[社区 node](community-nodes/using-community-nodes.md)，了解如何安装和管理社区构建的 node。
* 如果想进一步了解 n8n 中不同 node、它们的功能和示例用法，请查看 n8n 的 node 库：[Core node](builtin/core-nodes/)、[Action](builtin/app-nodes/) 和 [Trigger](builtin/trigger-nodes/)。
* 如果想了解如何为不同 node 添加 credential，请前往 [Credential](builtin/credentials/) 部分。

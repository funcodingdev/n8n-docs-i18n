---
title: PostBin node documentation
description: >-
  了解如何在 n8n 中使用 PostBin node。按照技术文档将 PostBin node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: PostBin node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.postbin.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.postbin'
layout:
  description:
    visible: false
---

# PostBin node <a href="#postbin-node" id="postbin-node"></a>

PostBin 是一项帮助你测试 API client 和 webhook 的服务。使用 PostBin node 自动化 PostBin 中的工作，并将 PostBin 与其他应用集成。n8n 内置支持大量 PostBin 功能，包括创建和删除 bin，以及获取和发送 request。

在本页中，你可以找到 PostBin node 支持的操作列表，以及更多资源链接。

## 操作 <a href="#operations" id="operations"></a>

* Bin
    * 创建
    * 获取
    * 删除
* Request
    * 获取
    * 移除第一个
    * 发送

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 PostBin node 文档集成模板](https://n8n.io/integrations/postbin)或[搜索所有模板](https://n8n.io/workflows/)

## 发送 request <a href="#send-requests" id="send-requests"></a>

要向 PostBin bin 发送 request：

1. 前往 [PostBin](https://www.toptal.com/developers/postbin/)，并按照步骤生成新的 bin。PostBin 会给你一个唯一 URL，其中包含 bin ID。
2. 在 PostBin node 中，选择 **Request** resource。
3. 选择要执行的 **Operation** 类型。
4. 在 **Bin ID** 中输入你的 bin ID。

## 创建和管理 bin <a href="#create-and-manage-bins" id="create-and-manage-bins"></a>

你可以使用 PostBin node 创建和管理 PostBin bin。

1. 在 **Resource** 中，选择 **Bin**。
2. 选择 **Operation**。你可以创建、删除或获取 bin。

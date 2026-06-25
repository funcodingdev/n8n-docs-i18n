---
title: Twist node documentation
description: >-
  了解如何在 n8n 中使用 Twist node。按照技术文档将 Twist node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Twist node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.twist.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.twist'
layout:
  description:
    visible: false
---

# Twist node <a href="#twist-node" id="twist-node"></a>

使用 Twist node 自动化 Twist 中的工作，并将 Twist 与其他应用集成。n8n 内置支持大量 Twist 功能，包括在 channel 中创建 conversation，以及在线程上创建和删除 comment。

在本页中，你可以找到 Twist node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Twist credentials](../credentials/twist.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Channel
    * 归档 channel
    * 发起基于 public 或 private channel 的 conversation
    * 删除 channel
    * 获取 channel 相关信息
    * 获取所有 channel
    * 取消归档 channel
    * 更新 channel
* Comment
    * 向 thread 创建新 comment
    * 删除 comment
    * 获取 comment 相关信息
    * 获取所有 comment
    * 更新 comment
* Message Conversation
    * 在 conversation 中创建 message
    * 删除 conversation 中的 message
    * 获取 conversation 中的 message
    * 获取 conversation 中的所有 message
    * 更新 conversation 中的 message
* Thread
    * 在 channel 中创建新 thread
    * 删除 thread
    * 获取 thread 相关信息
    * 获取所有 thread
    * 更新 thread

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Twist node 文档集成模板](https://n8n.io/integrations/twist)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 获取 User ID <a href="#get-the-user-id" id="get-the-user-id"></a>

要获取某个 user 的 User ID：

1. 打开 **Team** 标签页。
2. 选择某个 user 的 avatar。
3. 复制 Twist URL 中 `/u/` 后面的字符串。这个字符串就是 User ID。例如，如果 URL 是 `https://twist.com/a/4qw45/people/u/475370`，则 User ID 是 `475370`。

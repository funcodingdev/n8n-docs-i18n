---
title: Mattermost node documentation
description: >-
  了解如何在 n8n 中使用 Mattermost node。按照技术文档将 Mattermost node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Mattermost node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.mattermost.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.mattermost'
layout:
  description:
    visible: false
---

# Mattermost node <a href="#mattermost-node" id="mattermost-node"></a>

使用 Mattermost node 自动化 Mattermost 中的工作，并将 Mattermost 与其他应用集成。n8n 内置支持大量 Mattermost 功能，包括创建、删除和获取 channel 与 user，以及发布 message 和添加 reaction。

在本页中，你可以找到 Mattermost node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Mattermost credentials](../credentials/mattermost.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Channel
    * 将 user 添加到 channel
    * 创建新 channel
    * Soft delete channel
    * 获取 channel 的 member 分页
    * 恢复 soft deleted channel
    * 搜索 channel
    * 获取 channel 统计信息
* Message
    * 通过在数据库中将 post 标记为已删除来 soft delete post
    * 向 channel 发布 message
    * 向 channel 发布 ephemeral message
* Reaction
    * 向 post 添加 reaction。
    * 从 post 移除 reaction
    * 获取一个或多个 post 的所有 reaction
* User
    * 创建新 user
    * 通过归档 user object 停用 user 并撤销其所有 session。
    * 检索所有 user
    * 按 email 获取 user
    * 按 ID 获取 user
    * 邀请 user 加入 team

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Mattermost node 文档集成模板](https://n8n.io/integrations/mattermost)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Mattermost 文档](https://api.mattermost.com/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## Channel ID 字段错误 <a href="#channel-id-field-error" id="channel-id-field-error"></a>

如果你不是 System Administrator，可能会在 **Channel ID** 字段旁看到错误：**there was a problem loading the parameter options from server: "Mattermost error response: You do not have the appropriate permissions.**

请让你的 system administrator 授予你 `post:channel` 权限。

## 查找 channel ID <a href="#find-the-channel-id" id="find-the-channel-id"></a>

要在 Mattermost 中查找 channel ID：

1. 从左侧边栏选择 channel。
2. 选择顶部的 channel 名称。
3. 选择 **View Info**。

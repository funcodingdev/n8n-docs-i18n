---
title: Wekan node 文档
description: >-
  了解如何在 n8n 中使用 Wekan node。按照技术文档将 Wekan node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Wekan node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.wekan.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.wekan'
layout:
  description:
    visible: false
---

# Wekan node <a href="#wekan-node" id="wekan-node"></a>

使用 Wekan node 自动化 Wekan 中的工作，并将 Wekan 与其他应用集成。n8n 内置支持大量 Wekan 功能，包括创建、更新、删除和获取 board 与 card。

在本页中，你可以找到 Wekan node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Wekan credentials](../credentials/wekan.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* 看板
    * 创建新看板
    * 删除看板
    * 获取看板数据
    * 获取所有用户看板
* 卡片
    * 创建新卡片
    * 删除卡片
    * 获取卡片
    * 获取所有卡片
    * 更新卡片
* 卡片评论
    * 在卡片上创建评论
    * 从卡片删除评论
    * 获取卡片评论
    * 获取所有卡片评论
* 清单
    * 创建新清单
    * 删除清单
    * 获取清单数据
    * 返回卡片的所有清单
* 清单项
    * 删除清单项
    * 获取清单项
    * 更新清单项
* 列表
    * 创建新列表
    * 删除列表
    * 获取列表数据
    * 获取所有看板列表

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Wekan node 文档集成模板](https://n8n.io/integrations/wekan)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 加载 node 的所有参数 <a href="#load-all-the-parameters-for-the-node" id="load-all-the-parameters-for-the-node"></a>

要加载所有参数，例如 Author ID，你需要向用户授予管理员权限。请参阅 [Wekan 文档](https://github.com/wekan/wekan/wiki/Features#members-click-member-initials-or-avatar--permissions-adminnormalcomment-only)了解如何更改权限。

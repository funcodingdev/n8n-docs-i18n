---
title: Redis node documentation
description: >-
  了解如何在 n8n 中使用 Redis node。按照技术文档将 Redis node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Redis node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.redis.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.redis'
layout:
  description:
    visible: false
---

# Redis node <a href="#redis-node" id="redis-node"></a>

使用 Redis node 自动化 Redis 中的工作，并将 Redis 与其他应用集成。n8n 内置支持大量 Redis 功能，包括删除 key、获取 key value、设置 key value，以及向 Redis channel 发布消息。

在本页中，你可以找到 Redis node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Redis credentials](../credentials/redis.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* 从 Redis 删除 key。
* 从 Redis 获取 key 的 value。
* 返回 Redis instance 的通用信息。
* 以原子方式将 key 增加 1。如果 key 不存在，则创建它。
* 返回所有匹配 pattern 的 key。
* 设置 Redis 中 key 的 value。
* 向 Redis channel 发布消息。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Redis node 文档集成模板](https://n8n.io/integrations/redis)或[搜索所有模板](https://n8n.io/workflows/)

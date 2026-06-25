---
title: Onfleet node documentation
description: >-
  了解如何在 n8n 中使用 Onfleet node。按照技术文档将 Onfleet node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Onfleet node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.onfleet.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.onfleet'
layout:
  description:
    visible: false
---

# Onfleet node <a href="#onfleet-node" id="onfleet-node"></a>

使用 Onfleet node 自动化 Onfleet 中的工作，并将 Onfleet 与其他应用集成。n8n 内置支持大量 Onfleet 功能，包括在 Onfleet 中创建和删除 task，以及检索 organization 详细信息。

在本页中，你可以找到 Onfleet node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Onfleet credentials](../credentials/onfleet.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Admin
    * 创建新 Onfleet admin
    * 删除 Onfleet admin
    * 获取所有 Onfleet admin
    * 更新 Onfleet admin
* Container
    * 在索引处添加 task（或追加）
    * 获取 container 信息
    * 完整替换 container 中的 task
* Destination
    * 创建新 destination
    * 获取特定 destination
* Hub
    * 创建新 Onfleet hub
    * 获取所有 Onfleet hub
    * 更新 Onfleet hub
* Organization
    * 检索你自己的 organization 详细信息
    * 检索与你已连接的 organization 的详细信息
* Recipient
    * 创建新 Onfleet recipient
    * 获取特定 Onfleet recipient
    * 更新 Onfleet recipient
* Task
    * 创建新 Onfleet task
    * 克隆 Onfleet task
    * 强制完成已开始的 Onfleet task
    * 删除 Onfleet task
    * 获取所有 Onfleet task
    * 获取特定 Onfleet task
    * 更新 Onfleet task
* Team
    * 将分配给 team 的 task 自动派发给值班 driver
    * 创建新 Onfleet team
    * 删除 Onfleet team
    * 获取特定 Onfleet team
    * 获取所有 Onfleet team
    * 获取 team 即将执行 task 的预计时间，并返回选定 driver
    * 更新 Onfleet team
* Worker
    * 创建新 Onfleet worker
    * 删除 Onfleet worker
    * 获取特定 Onfleet worker
    * 获取所有 Onfleet worker
    * 获取特定 Onfleet worker schedule
    * 更新 Onfleet worker

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Onfleet node 文档集成模板](https://n8n.io/integrations/onfleet)或[搜索所有模板](https://n8n.io/workflows/)

---
title: Home Assistant node documentation
description: >-
  了解如何在 n8n 中使用 Home Assistant node。按照技术文档将 Home Assistant node 集成到你的
  workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Home Assistant node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.homeassistant.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.homeassistant
layout:
  description:
    visible: false
---

# Home Assistant node <a href="#home-assistant-node" id="home-assistant-node"></a>

使用 Home Assistant node 自动化 Home Assistant 中的工作，并将 Home Assistant 与其他应用集成。n8n 内置支持大量 Home Assistant 功能，包括获取、创建和检查 camera proxy、configuration、log、service 与 template。

在本页中，你可以找到 Home Assistant node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Home Assistant credentials](../credentials/homeassistant.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Camera Proxy
    * 获取 camera screenshot
* Config
    * 获取 configuration
    * 检查 configuration
* Event
    * 创建 event
    * 获取所有 event
* Log
    * 获取特定 entity 的 log
    * 获取所有 log
* Service
    * 在特定 domain 中调用 service
    * 获取所有 service
* State
    * 创建新 record；如果已存在，则更新当前 record（upsert）
    * 获取特定 entity 的 state
    * 获取所有 state
* Template
    * 创建 template

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Home Assistant node 文档集成模板](https://n8n.io/integrations/home-assistant)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [Home Assistant 文档](https://developers.home-assistant.io/docs/api/rest/)。

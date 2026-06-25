---
title: Calendly Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Calendly Trigger node。按照技术文档将 Calendly Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Calendly Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.calendlytrigger
layout:
  description:
    visible: false
---

# Calendly Trigger node <a href="#calendly-trigger-node" id="calendly-trigger-node"></a>

[Calendly](https://calendly.com/) 是一款自动化排程软件，旨在帮助查找会议时间。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/calendly.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Calendly Trigger integrations](https://n8n.io/integrations/calendly-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 事件已创建
* 事件已取消

## 常见问题 <a href="#common-issues" id="common-issues"></a>

以下是 Calendly Trigger node 的一些常见错误和问题，以及解决或排查步骤。

### Node 只会被 Calendly 管理的预约触发 <a href="#node-only-triggers-for-calendly-managed-bookings" id="node-only-triggers-for-calendly-managed-bookings"></a>

Calendly webhook 只会针对由 Calendly 管理的预约和取消触发。直接在已连接日历（例如 Google Calendar）中创建或编辑事件，不会触发 Calendly Trigger node。

### Webhook 回调 URL 必须是公开 HTTPS <a href="#webhook-callback-url-must-be-public-https" id="webhook-callback-url-must-be-public-https"></a>

Calendly Trigger node 使用 Calendly webhook，而 Calendly 要求 webhook callback URL 必须是公开 HTTPS URL。进行本地测试时，请使用 [ngrok](https://ngrok.com/) 或 [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/) 等隧道，并配置 n8n 对 webhook 使用该公开 HTTPS URL。设置详情请参阅 [Configuration > Webhook URL](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy)。

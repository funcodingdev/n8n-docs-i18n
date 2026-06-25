---
title: Twilio Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Twilio Trigger node。按照技术文档将 Twilio Trigger
  node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Twilio Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.twiliotrigger
layout:
  description:
    visible: false
---

# Twilio Trigger node <a href="#twilio-trigger-node" id="twilio-trigger-node"></a>

使用 Twilio Trigger node 响应 [Twilio](https://www.twilio.com) 中的事件，并将 Twilio 与其他应用程序集成。n8n 内置支持多种 Twilio 事件，包括新的 SMS 和 call。

在本页中，你可以找到 Twilio Trigger node 可响应的事件列表，以及更多相关资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/twilio.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Twilio integrations](https://n8n.io/integrations/twilio-trigger/) 页面。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* 新 SMS
* 新 Call

{% hint style="info" %}
**New Call Delay**

Twilio 最多可能需要三十分钟才能为已完成的 call 生成摘要。
{% endhint %}

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Twilio 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.twilio.md)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/twilio/)。

有关其 API 的详细信息，请参阅 [Twilio 的文档](https://www.twilio.com/docs)。

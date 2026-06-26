---
title: WhatsApp Business Cloud node common issues
description: >-
  n8n 中 WhatsApp Business Cloud node 的常见问题文档。包含问题详情和建议解决方案。
contentType:
  - integration
  - reference
priority: high
nodeTitle: WhatsApp Business Cloud node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues
layout:
  description:
    visible: false
---

# WhatsApp Business Cloud node common issues <a href="#whatsapp-business-cloud-node-common-issues" id="whatsapp-business-cloud-node-common-issues"></a>

这里列出 [WhatsApp Business Cloud node](README.md) 的一些常见错误和问题，以及解决或排查步骤。

## Bad request - 请检查参数 <a href="#bad-request-please-check-your-parameters" id="bad-request-please-check-your-parameters"></a>

当 WhatsApp Business Cloud 因参数问题拒绝你的请求时，会发生此错误。使用 **Send Template** operation 时，如果发送的数据与模板格式不匹配，经常会看到此错误。

要解决此问题，请检查[消息模板](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343)中的参数。注意每个参数的数据类型，以及它们在模板中定义的顺序。

检查 n8n 映射到模板参数的数据。如果你使用表达式设置参数值，请检查输入数据，确保每个 item 都解析为有效值。你可能需要使用 [Edit Fields (Set) node](../../core-nodes/n8n-nodes-base.set.md)，或设置 fallback 值，以确保发送的值格式正确。

## 处理非文本媒体 <a href="#working-with-non-text-media" id="working-with-non-text-media"></a>

WhatsApp Business Cloud node 可以处理非文本消息，以及图片、音频、文档等媒体。

如果你的 operation 包含 **Input Data Field Name** 或 **Property Name** 参数，请将其设置为字段名本身，而不是使用表达式引用数据。

例如，如果你要发送 "Image" **MessageType** 的消息，并且 **Take Image From** 设置为 "n8n"，请将 **Input Data Field Name** 设置为类似 `data` 的字段名，而不是类似 `{{ $json.input.data }}` 的表达式。

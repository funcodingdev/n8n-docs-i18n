---
title: LinkedIn node documentation
description: >-
  了解如何在 n8n 中使用 LinkedIn node。按照技术文档将 LinkedIn node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: LinkedIn node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.linkedin.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkedin'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.linkedin'
layout:
  description:
    visible: false
---

# LinkedIn node <a href="#linkedin-node" id="linkedin-node"></a>

使用 LinkedIn node 自动化 LinkedIn 中的工作，并将 LinkedIn 与其他应用集成。n8n 支持创建 post。

在本页中，你可以找到 LinkedIn node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [LinkedIn credentials](../credentials/linkedin.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Post
    * Create

## 参数 <a href="#parameters" id="parameters"></a>

* **Post As**：选择以 **Person** 还是 **Organization** 身份发布。
* **Person Name or ID** 和 **Organization URN**：输入 person 或 organization 的标识符。<br>

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>以 organization 身份发布</strong></p><p>如果以 Organization 身份发布，请在 URN 字段中输入 organization 编号。例如，输入 <code>03262013</code>，而不是 <code>urn:li:company:03262013</code>。</p></div>

* **Text**：post 内容。
* **Media Category**：在 post 中包含图片或 article URL 时使用。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 LinkedIn node 文档集成模板](https://n8n.io/integrations/linkedin)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此服务的更多信息，请参阅 [LinkedIn API 文档](https://learn.microsoft.com/en-us/linkedin/)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

---
title: Airtop node documentation
description: >-
  了解如何在 n8n 中使用 Airtop node。按照技术文档将 Airtop node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Airtop node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.airtop.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.airtop'
layout:
  description:
    visible: false
---

# Airtop node <a href="#airtop-node" id="airtop-node"></a>

使用 Airtop node 自动化 Airtop 中的工作，并将 Airtop 与其他应用集成。n8n 内置支持大量 Airtop 功能，让你可以控制基于云的 web browser，用于查询、抓取和与网页交互等任务。

在本页中，你可以找到 Airtop node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Airtop credentials](../credentials/airtop.md)。
{% endhint %}


## 操作 <a href="#operations" id="operations"></a>

* Session
    * Create session
    * Save profile on termination
    * Terminate session
* Window
    * Create a new browser window
    * Load URL
    * Take screenshot
    * Close window
* Extraction
    * Query page
    * Query page with pagination
    * Smart scrape page
* Interaction
    * Click an element
    * Hover on an element
    * Type


## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Airtop node 文档集成模板](https://n8n.io/integrations/airtop)或[搜索所有模板](https://n8n.io/workflows/)


## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关该服务的更多信息，请参阅 [Airtop 文档](https://docs.airtop.ai/api-reference/airtop-api)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

如需帮助或创建 feature request，请联系 [Airtop Support](https://docs.airtop.ai/guides/misc/support)。

## Node 参考 <a href="#node-reference" id="node-reference"></a>

### 创建 session 和 window <a href="#create-a-session-and-window" id="create-a-session-and-window"></a>

创建 Airtop browser session 以获取 **Session ID**，然后使用它创建新的 browser window。之后，你可以使用任何 extraction 或 interaction 操作。

### 提取内容 <a href="#extract-content" id="extract-content"></a>

使用这些操作从 web browser 提取内容：

- **Query page**：从当前 window 提取信息。
- **Query page with pagination**：从带有 pagination 或 infinite scrolling 的页面提取信息。
- **Smart scrape page**：将 window 内容作为 markdown 获取。

在 query 操作中使用 **JSON Output Schema** 参数可以获取 JSON 响应。

### 与页面交互 <a href="#interacting-with-pages" id="interacting-with-pages"></a>

通过描述要交互的元素，在元素上点击、hover 或输入。

### 终止 session <a href="#terminate-a-session" id="terminate-a-session"></a>

结束 session 以节省资源。Session 会根据 **Create Session** 操作中设置的 **Idle Timeout** 自动终止，也可以使用 **Terminate Session** 操作手动终止。

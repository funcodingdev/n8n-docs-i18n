---
title: Airtable Trigger node 文档
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Airtable Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger
description: >-
  了解如何在 n8n 中使用 Airtable Trigger node。按照技术文档将 Airtable Trigger node 集成到你的 workflow 中。
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Airtable Trigger

[Airtable](https://airtable.com/) 是电子表格和数据库的混合体，具备数据库特性，但应用于电子表格。Airtable 表中的字段类似电子表格中的单元格，但拥有 `checkbox`、`phone number` 和 `drop-down list` 等类型，并且可以引用图片等文件附件。

在本页中，你可以找到 Airtable Trigger node 可以响应的事件列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/airtable.md)找到此 node 的身份验证信息。
{% endhint %}

## 事件 <a href="#events" id="events"></a>

* **新的 Airtable 事件**

## 相关资源 <a href="#related-resources" id="related-resources"></a>

n8n 为 Airtable 提供了一个 app node。你可以在[这里](../app-nodes/n8n-nodes-base.airtable/)找到 node 文档。

在 n8n 网站上查看[示例 workflow 和相关内容](https://n8n.io/integrations/airtable-trigger/)。

有关其 API 的详细信息，请参阅 [Airtable 的文档](https://airtable.com/developers/web/api/introduction)。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用这些参数配置你的 node。

### 轮询时间 <a href="#poll-times" id="poll-times"></a>

n8n 的 Airtable node 使用轮询来检查已配置 Airtable 资源的更新。**Poll Times** 参数用于配置查询频率：

* 每分钟
* 每小时
* 每天
* 每周
* 每月
* Every X：每隔给定分钟数或小时数检查更新。
* Custom：通过提供 [cron 表达式](https://en.wikipedia.org/wiki/Cron)自定义轮询间隔。

使用 **Add Poll Time** 按钮添加更多轮询间隔。

### Base <a href="#base" id="base"></a>

你想检查更新的 [Airtable base](https://support.airtable.com/docs/airtable-bases-overview)。你可以提供 base 的 URL 或 [base ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls)。

### Table <a href="#table" id="table"></a>

你想检查更新的 Airtable base 内的 [Airtable table](https://support.airtable.com/docs/tables-overview)。你可以提供 table 的 URL 或 [table ID](https://support.airtable.com/docs/finding-airtable-ids#finding-base-table-and-view-ids-from-urls)。

### Trigger Field <a href="#trigger-field" id="trigger-field"></a>

表中的创建字段或最后修改字段。Airtable Trigger node 使用它确定自上次检查以来发生了哪些更新。

### Download Attachments <a href="#download-attachments" id="download-attachments"></a>

是否从表中下载附件。启用后，**Download Fields** 参数定义附件字段。

### Download Fields <a href="#download-fields" id="download-fields"></a>

启用 **Download Attachments** 开关后，此字段定义要下载哪些表字段。字段名区分大小写。使用逗号分隔多个字段名。

### 其他字段 <a href="#additional-fields" id="additional-fields"></a>

使用 **Add Field** 按钮添加以下参数：

* **Fields**：要包含在输出中的字段逗号分隔列表。如果这里不指定任何内容，输出将只包含 **Trigger Field**。
* **Formula**：用于进一步过滤结果的 [Airtable formula](https://support.airtable.com/docs/formula-field-reference)。你可以用它为触发 workflow 的事件添加进一步约束。请注意，手动执行不会考虑 formula 值，只会在生产轮询时考虑。
* **View ID**：表视图的名称或 ID。定义后，只返回给定视图中可用的 record。

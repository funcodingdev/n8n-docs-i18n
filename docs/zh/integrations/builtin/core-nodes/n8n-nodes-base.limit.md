---
title: Limit
description: >-
  n8n 中 Limit node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Limit
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.limit.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.limit'
layout:
  description:
    visible: false
---

# Limit <a href="#limit" id="limit"></a>

使用 Limit node 可以移除超过已定义最大数量的 item。你可以选择 n8n 从输入数据的开头还是末尾保留 item。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

使用以下参数配置此 node。

### Max Items <a href="#max-items" id="max-items"></a>

输入 n8n 应保留的最大 item 数。如果输入数据包含的 item 多于此值，n8n 会移除多余 item。

### Keep <a href="#keep" id="keep"></a>

如果该 node 必须移除 item，请选择从哪里保留输入 item：

* **First Items**：从输入数据开头保留 **Max Items** 数量的 item。
* **Last Items**：从输入数据末尾保留 **Max Items** 数量的 item。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Limit 集成模板](https://n8n.io/integrations/limit)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/0nvcx1EqJQgGVzUXOOMN/" %}

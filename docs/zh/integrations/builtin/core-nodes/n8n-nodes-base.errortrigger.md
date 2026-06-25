---
title: Error Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Error Trigger node。按照技术文档将
  Error Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Error Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger
layout:
  description:
    visible: false
---

# Error Trigger node <a href="#error-trigger-node" id="error-trigger-node"></a>

你可以使用 Error Trigger node 创建 error workflow。当另一个已关联的 workflow 失败时，此 node 会获取失败 workflow 和错误的详细信息，并运行 error workflow。

## 用法 <a href="#usage" id="usage"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/odStQfuU7M0KPowwye9k/" %}


请注意以下事项：

* 如果某个 workflow 使用 Error Trigger node，你不必发布该 workflow。
* 如果某个 workflow 包含 Error Trigger node，默认情况下，该 workflow 会使用自身作为 error workflow。
* 手动运行 workflow 时，不能测试 error workflow。Error Trigger 只会在自动 workflow 出错时运行。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Error Trigger node 集成模板](https://n8n.io/integrations/error-trigger)或[搜索所有模板](https://n8n.io/workflows/)

## 相关资源 <a href="#related-resources" id="related-resources"></a>

你可以使用 [Stop And Error](n8n-nodes-base.stopanderror.md) node 向 Error Trigger 发送自定义消息。

阅读更多关于 n8n workflow 中 [Error workflows](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/flow-logic/handle-errors-gracefully) 的内容。

## Error data <a href="#error-data" id="error-data"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/rAiMowL1bA7C4GcH8FyS/" %}

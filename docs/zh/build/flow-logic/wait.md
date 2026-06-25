---
title: 等待
description: 如何让工作流执行等待。
contentType: howto
nodeTitle: Wait
originalFilePath: flow-logic/waiting.md
originalUrl: 'https://docs.n8n.io/flow-logic/waiting'
url: 'https://docs.n8n.io/build/flow-logic/wait'
layout:
  description:
    visible: false
---

# 等待 <a href="#waiting" id="waiting"></a>

等待允许你在工作流执行中途暂停，然后使用相同数据从暂停位置继续执行。如果你需要限制对某个服务的调用频率，或等待外部事件完成，这会很有用。你可以等待指定时长，也可以等到 webhook 触发。

让工作流等待需要使用 [Wait](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.wait) 节点。用法详情请参阅该节点文档。

n8n 提供了一个工作流模板，展示[限流并等待外部事件](https://n8n.io/workflows/1749-rate-limiting-and-waiting-for-external-events/)的基础示例。

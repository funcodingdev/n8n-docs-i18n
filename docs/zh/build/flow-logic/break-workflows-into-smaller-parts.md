---
contentType: howto
description: >-
  从其他工作流调用工作流，并将大型工作流拆分成更小的组件。
nodeTitle: Break workflows into smaller parts
originalFilePath: flow-logic/subworkflows.md
originalUrl: 'https://docs.n8n.io/flow-logic/subworkflows'
url: 'https://docs.n8n.io/build/flow-logic/break-workflows-into-smaller-parts'
layout:
  description:
    visible: false
---

# 子工作流 <a href="#sub-workflows" id="sub-workflows"></a>

你可以从一个工作流调用另一个工作流。这样可以构建模块化、类似微服务的工作流。如果工作流变得很大并遇到[内存问题](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/fix-memory-issues)，这种方式也会有帮助。创建子工作流需要使用 [Execute Workflow](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflow) 和 [Execute Sub-workflow Trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger) 节点。

Sub-workflow executions 不计入你的方案的月度执行次数或活跃工作流限制。

## 设置并使用子工作流 <a href="#set-up-and-use-a-sub-workflow" id="set-up-and-use-a-sub-workflow"></a>

本节会介绍如何同时设置父工作流和子工作流。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/wlwT5JcWyWTecnDN6aul/" %}

## 数据如何在工作流之间传递 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/edKlUxnfiRMq38CujuFv/" %}

## 子工作流转换 <a href="#sub-workflow-conversion" id="sub-workflow-conversion"></a>

如何将现有工作流拆分成子工作流，请参阅[子工作流转换](convert-to-sub-workflows.md)。

---
title: SecurityScorecard node documentation
description: >-
  了解如何在 n8n 中使用 SecurityScorecard node。按照技术文档将 SecurityScorecard node
  集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: SecurityScorecard node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.securityscorecard
layout:
  description:
    visible: false
---

# SecurityScorecard node <a href="#securityscorecard-node" id="securityscorecard-node"></a>

使用 SecurityScorecard node 自动化 SecurityScorecard 中的工作，并将 SecurityScorecard 与其他应用集成。n8n 内置支持大量 SecurityScorecard 功能，包括创建、更新、删除和获取 portfolio，以及获取 company 数据。

在本页中，你可以找到 SecurityScorecard node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [SecurityScorecard credentials](../credentials/securityscorecard.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* Company
    * 获取 company factor score 和 issue count
    * 获取 company 的历史 factor score
    * 获取 company 的历史 score
    * 获取 company 信息及其 scorecard 摘要
    * 获取 company 的 score improvement plan
* Industry
    * 获取 Factor Scores
    * 获取 Historical Factor Scores
    * 获取 Score
* Invite
    * 为 company/user 创建 invite
* Portfolio
    * 创建 portfolio
    * 删除 portfolio
    * 获取所有 portfolio
    * 更新 portfolio
* Portfolio Company
    * 将 company 添加到 portfolio
    * 获取 portfolio 中的所有 company
    * 从 portfolio 中移除 company
* Report
    * 下载已生成的 report
    * 生成 report
    * 获取最近生成的 report 列表

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 SecurityScorecard node 文档集成模板](https://n8n.io/integrations/securityscorecard)或[搜索所有模板](https://n8n.io/workflows/)

---
title: Rundeck node documentation
description: >-
  了解如何在 n8n 中使用 Rundeck node。按照技术文档将 Rundeck node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Rundeck node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.rundeck.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck'
url: 'https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.rundeck'
layout:
  description:
    visible: false
---

# Rundeck node <a href="#rundeck-node" id="rundeck-node"></a>

使用 Rundeck node 自动化 Rundeck 中的工作，并将 Rundeck 与其他应用集成。n8n 内置支持执行 job 和获取 metadata。

在本页中，你可以找到 Rundeck node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [Rundeck credentials](../credentials/rundeck.md)。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

- **Job**
    - 执行 job
    - 获取 job 的 metadata

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Rundeck node 文档集成模板](https://n8n.io/integrations/rundeck)或[搜索所有模板](https://n8n.io/workflows/)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/96ifDzfcUuwOyYrubZUt/" %}

## 查找 job ID <a href="#find-the-job-id" id="find-the-job-id"></a>

1. 访问你的 Rundeck dashboard。
2. 打开包含你想在 n8n 中使用的 job 的 project。
3. 在 sidebar 中选择 **JOBS**。
4. 在 **All Jobs** 下，选择你想在 n8n 中使用的 job 名称。
5. 在左上角 job 名称下方，复制以较小字体显示在 job 名称下的字符串。这就是你的 job ID。
6. 将此 job ID 粘贴到 n8n 的 **Job Id** 字段中。

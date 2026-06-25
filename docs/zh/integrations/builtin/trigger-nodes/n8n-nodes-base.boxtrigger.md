---
title: Box Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Box Trigger node。按照技术文档将 Box Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
nodeTitle: Box Trigger node documentation
originalFilePath: integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger
url: >-
  https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.boxtrigger
layout:
  description:
    visible: false
---

# Box Trigger node <a href="#box-trigger-node" id="box-trigger-node"></a>

[Box](https://www.box.com/) 是一家云计算公司，提供文件共享、协作以及其他用于处理上传到其服务器中文件的工具。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/box.md)找到此 node 的身份验证信息。
{% endhint %}

{% hint style="info" %}
**示例和模板**

有关帮助你入门的使用示例和模板，请参阅 n8n 的 [Box Trigger integrations](https://n8n.io/integrations/box-trigger/) 页面。
{% endhint %}

## 查找你的 Box Target ID <a href="#find-your-box-target-id" id="find-your-box-target-id"></a>

要在 Box 中获取 Target ID：

1. 打开你想监控的文件/文件夹。
2. 复制 URL 中 `folder/` 后面的字符串。这就是 target ID。例如，如果 URL 是 `https://app.box.com/folder/12345`，那么 `12345` 就是 target ID。
3. 将它粘贴到 n8n 的 **Target ID** 字段中。

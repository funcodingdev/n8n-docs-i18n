---
title: Google Sheets node common issues
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Google Sheets node common issues
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues
description: >-
  n8n 中 Google Sheets node 的常见问题和解决方案文档。包含问题详情和建议解决方式。
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

# Common issues

这里列出 [Google Sheets node](./) 的一些常见错误和问题，以及解决或排查步骤。

## Append an array <a href="#append-an-array" id="append-an-array"></a>

要将数据数组插入 Google Sheets，必须先将数组转换为有效的 JSON（key, value）格式。

为此，可以考虑使用：

1. [Split Out](../../core-nodes/n8n-nodes-base.splitout.md) node。
2. [AI Transform](../../core-nodes/n8n-nodes-base.aitransform.md) node。例如，尝试输入类似以下内容：

    ```
    Convert 'languages' array to JSON (key, value) pairs.
    ```
3. [Code node](../../core-nodes/n8n-nodes-base.code/)。

## Column names were updated after the node's setup <a href="#column-names-were-updated-after-the-nodes-setup" id="column-names-were-updated-after-the-nodes-setup"></a>

如果 Google Sheet 的列名在你设置 node 后发生变化，你会收到此错误。

要刷新列名，请重新选择 **Mapping Column Mode**。这应会提示 node 再次获取列名。

列名刷新后，更新 node 参数。

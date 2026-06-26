---
title: Telegram node File operations documentation
description: >-
  n8n 中 Telegram node 的 File 操作文档。包含配置所有 File 操作的详情。
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Telegram node File operations documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations
url: >-
  https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations
layout:
  description:
    visible: false
---

# Telegram node File operations <a href="#telegram-node-file-operations" id="telegram-node-file-operations"></a>

使用此操作从 Telegram 获取文件。有关 Telegram node 本身的更多信息，请参阅 [Telegram](README.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## Get File <a href="#get-file" id="get-file"></a>

使用此操作通过 Bot API [getFile](https://core.telegram.org/bots/api#getfile) method 从 Telegram 获取文件。

输入以下参数：

* **Credential to connect with**：创建或选择一个已有的 [Telegram credential](../../credentials/telegram.md)。
* **Resource**：选择 **File**。
* **Operation**：选择 **Get**。
* **File ID**：输入要获取的文件 ID。
* **Download**：选择是否希望 node 下载文件（开启）或不下载文件（关闭）。

有关更多信息，请参阅 Telegram Bot API [getFile](https://core.telegram.org/bots/api#getfile) 文档。

---
title: Scaling binary data in n8n
description: 如何处理大型文件而不降低 n8n 性能。
contentType: howto
nodeTitle: Handle binary data
originalFilePath: hosting/scaling/binary-data.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/binary-data'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/handle-binary-data'
layout:
  description:
    visible: false
---

# Binary data <a href="#binary-data" id="binary-data"></a>

Binary data 是任何文件类型的数据，例如 workflow 执行期间生成或处理的 image files 或 documents。

## 启用 filesystem mode <a href="#enable-filesystem-mode" id="enable-filesystem-mode"></a>

处理 binary data 时，n8n 默认将数据保存在内存中。处理大型文件时，这可能导致 crashes。

为避免这种情况，请将 `N8N_DEFAULT_BINARY_DATA_MODE` [环境变量](../basic-configuration/use-environment-variables/binary-data.md)改为 `filesystem`。这会让 n8n 将数据保存到磁盘，而不是使用内存。

如果你使用 queue mode，请将其切换为 `database`。n8n 不支持在 queue mode 中使用 `filesystem` mode。

## Binary data pruning <a href="#binary-data-pruning" id="binary-data-pruning"></a>

n8n 会将 binary data pruning 作为 execution data pruning 的一部分执行。详情请参考 [Execution data | Enable executions pruning](manage-execution-data.md#enable-executions-pruning)。

如果配置了多个 binary data modes，binary data pruning 会作用于当前启用的 binary data mode。例如，如果你的实例曾在 S3 中存储数据，之后切换到 filesystem mode，n8n 只会清理 filesystem 中的 binary data。详情请参考 [External storage](use-external-storage.md#usage)。

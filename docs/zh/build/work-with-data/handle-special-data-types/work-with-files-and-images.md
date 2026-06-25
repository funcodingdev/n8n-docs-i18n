---
title: Binary data
description: 了解并在 n8n 中使用 binary data。
contentType: overview
tags:
  - binary data
hide:
  - tags
nodeTitle: Work with files and images
originalFilePath: data/specific-data-types/binary-data.md
originalUrl: 'https://docs.n8n.io/data/specific-data-types/binary-data'
url: >-
  https://docs.n8n.io/build/work-with-data/handle-special-data-types/work-with-files-and-images
layout:
  description:
    visible: false
---

# Binary data <a href="#binary-data" id="binary-data"></a>

Binary data 是任何文件类型的数据，例如图片文件或文档。

本页汇总 n8n 中与 binary data 相关的资源。

## 在工作流中处理 binary data <a href="#working-with-binary-data-in-your-workflows" id="working-with-binary-data-in-your-workflows"></a>

你可以在 n8n 工作流中处理 binary data。n8n 提供了帮助你处理 binary data 的 node。你也可以使用代码。

### Nodes <a href="#nodes" id="nodes"></a>

有三个专门用于处理 binary data 文件的关键 node：

- [Convert to File](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.converttofile)：获取输入数据并将其作为文件输出。
- [Extract From File](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.extractfromfile)：从 binary format 获取数据并将其转换为 JSON。
- [Read/Write Files from Disk](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.readwritefile)：从 n8n 运行所在机器读取文件，或向其写入文件。

还有用于处理 XML 和 HTML 数据的独立 node：

* [HTML](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.html)
* [XML](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.xml)

以及执行常见任务的 node：

* [Compression](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.compression)
* [Edit Image](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.editimage)
* [FTP](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.ftp)

你可以使用 [Local File trigger](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.localfiletrigger)，基于本地文件变化触发工作流。

如需拆分或连接 binary data item，请使用 [data transformation nodes](../expressions-versus-data-nodes.md#other-data-transformation-nodes)。

### Code <a href="#code" id="code"></a>

你可以使用 [Code node](../../code-in-n8n/using-the-code-node.md) 在工作流中操作 binary data。例如，[获取 binary data buffer](../../code-in-n8n/cookbook/code-node/get-the-binary-data-buffer.md)：获取工作流中可用的 binary data。


## 自托管时配置 binary data mode <a href="#configure-binary-data-mode-when-self-hosting" id="configure-binary-data-mode-when-self-hosting"></a>

你可以使用 [Binary data environment variables](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data) 配置自托管 n8n 实例如何处理 binary data。这包括设置存储路径、选择 binary data 存储方式等任务。

你的配置会影响 n8n 的扩展能力：[Scaling | Binary data filesystem mode](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/scaling/handle-binary-data)。

读取和写入 binary 文件可能带来安全影响。如果要禁用 binary data 的读取和写入，请使用 `NODES_EXCLUDE` 环境变量。更多信息请参阅 [Environment variables | Nodes](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/nodes)。

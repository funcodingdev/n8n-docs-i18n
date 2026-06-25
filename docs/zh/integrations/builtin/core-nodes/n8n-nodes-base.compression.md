---
title: Compression
description: >-
  n8n 中 Compression node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: n8n-nodes-base.compression
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.compression.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression'
layout:
  description:
    visible: false
---

# Compression <a href="#compression" id="compression"></a>

使用 Compression node 可以压缩和解压文件。支持 Zip 和 Gzip 格式。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

Node 参数取决于你选择的 **Operation**。可选择：

* **Compress**：从输入数据创建压缩文件。
* **Decompress**：解压已有的压缩文件。

请参阅下面各节，了解每个 **Operation** 特有的参数。

### Compress <a href="#compress" id="compress"></a>

- **Input Binary Field(s)**：输入包含要压缩的二进制文件的输入数据字段名称。要压缩多个文件，请使用逗号分隔的列表。
- **Output Format**：选择将压缩输出格式化为 **Zip** 还是 **Gzip**。
- **File Name**：输入该 node 创建的 zip 文件名称。
- **Put Output File in Field**：输入输出数据中用于包含该文件的字段名称。

### Decompress <a href="#decompress" id="decompress"></a>

- **Put Output File in Field**：输入包含要解压的二进制文件的输入数据字段名称。要解压多个文件，请使用逗号分隔的列表。
- **Output Prefix**：输入要添加到输出文件名的前缀。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 n8n-nodes-base.compression 集成模板](https://n8n.io/integrations/compression)或[搜索所有模板](https://n8n.io/workflows/)

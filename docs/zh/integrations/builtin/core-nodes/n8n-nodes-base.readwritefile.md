---
title: Read/Write Files from Disk
contentType:
  - integration
  - reference
priority: critical
nodeTitle: Read/Write Files from Disk
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile
description: >-
  n8n 中 Read/Write Files from Disk node 的文档。n8n 是一个 workflow
  自动化平台。包含使用指导以及示例链接。
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

# Read/Write Files from Disk

使用 Read/Write Files from Disk node 可以在运行 n8n 的机器上读取文件或写入文件。

此 node 可以访问的路径取决于你的 n8n 部署。详情请参阅[文件位置](n8n-nodes-base.readwritefile.md#file-locations)。

## 操作 <a href="#operations" id="operations"></a>

* [**Read File(s) From Disk**](n8n-nodes-base.readwritefile.md#read-files-from-disk)：使用此操作从运行 n8n 的计算机检索一个或多个文件。
* [**Write File to Disk**](n8n-nodes-base.readwritefile.md#write-file-to-disk)：使用此操作在运行 n8n 的计算机上创建二进制文件。

有关为每个操作配置该 node 的更多信息，请参阅下面各节。

## Read File(s) From Disk <a href="#read-files-from-disk" id="read-files-from-disk"></a>

使用这些参数配置该操作：

* **File(s) Selector**：输入要读取文件的路径。
  * 要输入多个文件，请输入文件路径 pattern。你可以使用这些字符定义 path pattern：
    * `*`：匹配任意字符零次或多次，不包括路径分隔符。
    * `**`：匹配任意字符零次或多次，包括路径分隔符。
    * `?`：匹配任意单个字符，但不包括路径分隔符。
    * `[]`：匹配括号内的任意字符。例如，`[abc]` 会匹配字符 `a`、`b` 或 `c`，不匹配其他字符。

有关这些字符及其预期行为的更多信息，请参阅 [Picomatch 的 Basic globbing](https://github.com/micromatch/picomatch#basic-globbing) 文档。

### Read File(s) From Disk 选项 <a href="#read-files-from-disk-options" id="read-files-from-disk-options"></a>

你还可以使用这些 **Options** 配置此操作：

* **File Extension**：输入 node 输出中文件的扩展名。
* **File Name**：输入 node 输出中文件的名称。
* **MIME Type**：输入 node 输出中文件的 MIME type。文件扩展名及其 MIME type 列表请参阅 [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)。
* **Put Output File in Field**：输入输出数据中用于包含该文件的字段名称。

## Write File to Disk <a href="#write-file-to-disk" id="write-file-to-disk"></a>

使用这些参数配置该操作：

* **File Path and Name**：输入文件目标位置、文件名和文件扩展名。
* **Input Binary Field**：输入 node 输入数据中将包含二进制文件的字段名称。

### Write File to Disk 选项 <a href="#write-file-to-disk-options" id="write-file-to-disk-options"></a>

你还可以使用这些 **Options** 配置此操作：

此操作包含一个选项，即是否将数据 **Append** 到现有文件而不是创建新文件（开启），或创建新文件而不是追加到现有文件（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Read/Write Files from Disk 集成模板](https://n8n.io/integrations/readwrite-files-from-disk)或[搜索所有模板](https://n8n.io/workflows/)

## 文件位置 <a href="#file-locations" id="file-locations"></a>

此 node 可读取和写入的路径取决于你的 n8n 部署。

### n8n Cloud <a href="#n8n-cloud" id="n8n-cloud"></a>

在 n8n Cloud 上，该 node 只能访问 `/home/node/` 下的路径。此目录之外的路径（例如 `/tmp/` 或 `/data/`）会因访问错误而失败。

{% hint style="info" %}
**Cloud 上的字段 placeholder**

该 node 的 **File(s) Selector** 和 **File Path and Name** 字段中的默认 placeholder（例如 `/home/user/Pictures/**/*.png` 和 `/data/example.jpg`）只是示例。在 Cloud 上，请将它们替换为 `/home/node/` 下的路径。
{% endhint %}

{% hint style="warning" %}
**Cloud filesystem 是临时的**

此 node 在 Cloud 上写入的文件不保证在 workflow execution、worker restart 或 instance redeploy 之间持久存在。不要使用此 node 存储需要保留的文件。

n8n 将 `/home/node/.n8n/` 目录保留给内部状态。不要在那里写入你自己的文件。

如需在 Cloud 上进行持久文件处理，请使用 cloud storage node，例如 [AWS S3](../app-nodes/n8n-nodes-base.awss3.md)、[Google Drive](../app-nodes/n8n-nodes-base.googledrive/) 或 [FTP](n8n-nodes-base.ftp.md)。
{% endhint %}

### Self-hosted n8n <a href="#self-hosted-n8n" id="self-hosted-n8n"></a>

在 self-hosted n8n 上，默认情况下，该 node 可以访问 n8n process 可到达的任何路径。要限制访问，请将 [`N8N_RESTRICT_FILE_ACCESS_TO`](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/basic-configuration/use-environment-variables/security) 环境变量设置为一个或多个允许的目录（用分号分隔）。

{% hint style="info" %}
**n8n 2.0 中的默认值变化**

从 n8n 2.0 开始，`N8N_RESTRICT_FILE_ACCESS_TO` 默认值为 `~/.n8n-files`。要允许在其他位置执行文件操作，请显式设置该变量。详情请参阅 [n8n 2.0 breaking changes](https://app.gitbook.com/s/hhM8Cox90Piiv0u0EgHM/v20-breaking-changes#set-default-value-for-n8n_restrict_file_access_to)。
{% endhint %}

如果在 Docker 中运行 n8n，路径指的是 n8n container 的 filesystem，而不是 Docker host。要让此 node 可访问 host 目录，请将这些目录作为 volume 挂载到 container 中。

n8n 建议使用绝对文件路径以防止错误。

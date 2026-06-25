---
title: FTP
contentType:
  - integration
  - reference
priority: medium
nodeTitle: FTP
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ftp.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ftp
description: >-
  n8n 中 FTP node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
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

# FTP

FTP node 适用于访问 FTP 或 SFTP 服务器并向其上传文件。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/ftp.md)找到该 node 的身份验证信息。
{% endhint %}

要连接到 SFTP 服务器，请使用 SFTP credential。更多信息请参阅 [FTP credentials](../credentials/ftp.md)。

## 操作 <a href="#operations" id="operations"></a>

* [**Delete**](n8n-nodes-base.ftp.md#delete) 文件或文件夹
* [**Download**](n8n-nodes-base.ftp.md#download) 文件
* [**List**](n8n-nodes-base.ftp.md#list) 文件夹内容
* [**Rename**](n8n-nodes-base.ftp.md#rename) 或移动文件或文件夹
* [**Upload**](n8n-nodes-base.ftp.md#upload) 文件

{% hint style="info" %}
**上传文件**

要附加用于上传的文件，你需要使用额外的 node，例如 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) node 或 [HTTP Request](n8n-nodes-base.httprequest/) node，将文件作为 data property 传递。
{% endhint %}

## Delete <a href="#delete" id="delete"></a>

此操作包含一个参数：**Path**。输入你想连接到的远程路径。

### Delete 选项 <a href="#delete-options" id="delete-options"></a>

Delete 操作会添加一个新选项：**Folder**。如果开启此选项，该 node 可以删除文件夹和文件。此配置还会显示另一个选项：

* **Recursive**：如果开启此选项并删除文件夹或目录，该 node 会删除目标目录中的所有文件和目录。

## Download <a href="#download" id="download"></a>

使用这些参数配置该操作：

* **Path**：输入你想连接到的远程路径。
* **Put Output File in Field**：输入用于放置文件的输出二进制字段名称。

{% hint style="info" %}
**Concurrent Reads with SFTP**

使用 SFTP 时，你可以启用 concurrent reads。这可以提升下载速度，但并非所有 SFTP 服务器都支持。
{% endhint %}

## List <a href="#list" id="list"></a>

使用这些参数配置该操作：

* **Path**：输入你想连接到的远程路径。
* **Recursive**：选择是否返回一个对象，该对象表示在 FTP/SFTP 服务器中递归找到的所有目录/对象（开启）或不递归返回（关闭）。

## Rename <a href="#rename" id="rename"></a>

使用这些参数配置该操作：

* **Old Path**：在此字段中输入要重命名文件的现有路径。
* **New Path**：在此字段中输入重命名后文件的新路径。

### Rename 选项 <a href="#rename-options" id="rename-options"></a>

此操作会添加一个新选项：**Create Directories**。如果开启此选项，该 node 会在重命名现有文件或文件夹时递归创建目标目录。

## Upload <a href="#upload" id="upload"></a>

使用这些参数配置该操作：

* **Path**：输入你想连接到的远程路径。
* **Binary File**：选择你要上传二进制文件（开启），还是输入要上传的文本内容（关闭）。其他参数取决于你在此字段中的选择。
  * **Input Binary Field**：开启 **Binary File** 时显示。输入包含要上传文件的输入二进制字段名称。
  * **File Content**：关闭 **Binary File** 时显示。输入要上传文件的文本内容。

{% hint style="info" %}
**上传文件**

要附加用于上传的文件，你需要使用额外的 node，例如 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) node 或 [HTTP Request](n8n-nodes-base.httprequest/) node，将文件作为 data property 传递。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 FTP 集成模板](https://n8n.io/integrations/ftp)或[搜索所有模板](https://n8n.io/workflows/)

---
title: SSH
contentType:
  - integration
  - reference
priority: medium
nodeTitle: SSH
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.ssh.md
originalUrl: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh
url: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ssh
description: >-
  n8n 中 SSH node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
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

# SSH

SSH node 可用于通过 Secure Shell Protocol 执行命令。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/ssh.md)找到此 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* [**Execute** 命令](n8n-nodes-base.ssh.md#execute-command)
* [**Download** 文件](n8n-nodes-base.ssh.md#download-file)
* [**Upload** 文件](n8n-nodes-base.ssh.md#upload-file)

{% hint style="info" %}
**上传文件**

要附加文件用于上传，你需要使用额外的 node，例如 [Read/Write Files from Disk](n8n-nodes-base.readwritefile.md) node 或 [HTTP Request](n8n-nodes-base.httprequest/) node，将文件作为数据属性传递。
{% endhint %}

### Execute Command <a href="#execute-command" id="execute-command"></a>

使用这些参数配置此操作：

* **Credential to connect with**：选择现有 [SSH credential](../credentials/ssh.md) 或新建一个 credential 进行连接。
* **Command**：输入要在远程设备上执行的命令。
* **Working Directory**：输入 n8n 应在其中执行命令的目录。

### Download File <a href="#download-file" id="download-file"></a>

* **Credential to connect with**：选择现有 [SSH credential](../credentials/ssh.md) 或新建一个 credential 进行连接。
* **Path**：输入要下载文件的路径。此路径必须包含文件名。下载的文件会使用此文件名。要使用不同名称，请使用 **File Name** 选项。更多信息请参阅 [Download File 选项](n8n-nodes-base.ssh.md#download-file-options)。
* **File Property**：输入保存要下载的二进制数据的对象属性名称。

#### Download File 选项 <a href="#download-file-options" id="download-file-options"></a>

你可以使用 **File Name** 选项进一步配置此操作。使用此选项可将二进制数据文件名覆盖为你选择的名称。

### Upload File <a href="#upload-file" id="upload-file"></a>

* **Credential to connect with**：选择现有 [SSH credential](../credentials/ssh.md) 或新建一个 credential 进行连接。
* **Input Binary Field**：输入包含要上传文件的输入二进制字段名称。
* **Target Directory**：要上传文件的目标目录。文件名取自二进制数据文件名。要输入不同名称，请使用 **File Name** 选项。更多信息请参阅 [Upload File 选项](n8n-nodes-base.ssh.md#upload-file-options)。

#### Upload File 选项 <a href="#upload-file-options" id="upload-file-options"></a>

你可以使用 **File Name** 选项进一步配置此操作。使用此选项可将二进制数据文件名覆盖为你选择的名称。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 SSH 集成模板](https://n8n.io/integrations/ssh)或[搜索所有模板](https://n8n.io/workflows/)

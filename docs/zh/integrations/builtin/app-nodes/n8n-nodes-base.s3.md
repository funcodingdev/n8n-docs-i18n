---
title: S3 node documentation
contentType:
  - integration
  - reference
priority: medium
nodeTitle: S3 node documentation
originalFilePath: integrations/builtin/app-nodes/n8n-nodes-base.s3.md
originalUrl: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3
url: https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.s3
description: >-
  了解如何在 n8n 中使用 S3 node。按照技术文档将 S3 node 集成到你的 workflow 中。
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

# S3

使用 S3 node 自动化非 AWS S3 存储中的工作，并将 S3 与其他应用集成。n8n 内置支持大量 S3 功能，包括创建、删除和获取 bucket、file 与 folder。对于 AWS S3，请使用 [AWS S3](n8n-nodes-base.awss3.md)。

将 S3 node 用于非 AWS S3 方案，例如：

* [MinIO](https://min.io/)
* [Wasabi](https://wasabi.com/)
* [Digital Ocean spaces](https://www.digitalocean.com/products/spaces)

在本页中，你可以找到 S3 node 支持的操作列表，以及更多资源链接。

{% hint style="info" %}
**Credentials**

有关设置身份验证的指导，请参阅 [S3 credentials](../credentials/s3.md)。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/6vuTxJwns2nA8U7V56ij/" %}

## 操作 <a href="#operations" id="operations"></a>

* Bucket
  * 创建 bucket
  * 删除 bucket
  * 获取所有 bucket
  * 在 bucket 中搜索
*   File<br>

    * 复制 file
    * 删除 file
    * 下载 file
    * 获取所有 file
    * 上传 file

    <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p><strong>附加要上传的 file</strong></p><p>要附加要上传的 file，请使用另一个 node 将 file 作为 data property 传入。像 <a href="../core-nodes/n8n-nodes-base.readwritefile.md">Read/Write Files from Disk</a> node 或 <a href="../core-nodes/n8n-nodes-base.httprequest/">HTTP Request</a> 这样的 node 很适合。</p></div>
* Folder
  * 创建 folder
  * 删除 folder
  * 获取所有 folder

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 S3 node 文档集成模板](https://n8n.io/integrations/s3)或[搜索所有模板](https://n8n.io/workflows/)

## Node 参考 <a href="#node-reference" id="node-reference"></a>

### 在 Wasabi 中设置 file permission <a href="#setting-file-permissions-in-wasabi" id="setting-file-permissions-in-wasabi"></a>

向 [Wasabi](https://wasabi.com/) 上传 file 时，必须使用 **ACL** 下拉菜单设置 file permission，而不是使用 toggle。

![使用 S3 node 与 Wasabi 时的 file permission](../../.gitbook/assets/acl_dropdown.png)

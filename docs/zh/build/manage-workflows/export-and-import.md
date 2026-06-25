---
title: 导出和导入工作流
contentType: howto
nodeTitle: Export and import
originalFilePath: workflows/export-import.md
originalUrl: https://docs.n8n.io/workflows/export-import
url: https://docs.n8n.io/build/manage-workflows/export-and-import
description: 在 n8n 中导出和导入工作流的不同方式。
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

# 导出和导入

n8n 以 JSON 格式保存工作流。你可以将工作流导出为 JSON 文件，也可以将 JSON 文件导入到 n8n 库中。导出和导入工作流有多种方式。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/OlpV1rtc5ZIqBmvX4lBQ/" %}

## 复制粘贴 <a href="#copy-paste" id="copy-paste"></a>

你可以选择要复制到剪贴板的节点（`Ctrl + c` 或 `cmd + c`），然后将其粘贴（`Ctrl + v` 或 `cmd + v`）到 Editor UI 中，从而复制粘贴整个工作流或其中一部分。

要选择所有节点或一组节点，请点击并拖动：![选择一组节点](../../../build/.gitbook/assets/selectingnodes.gif)

## 从 Editor UI 菜单导入导出 <a href="#from-the-editor-ui-menu" id="from-the-editor-ui-menu"></a>

在顶部导航栏中，选择右上角的三个点 <img src="../../../build/.gitbook/assets/three-dots-horizontal (1).png" alt="Workflow menu icon" data-size="line">，可以看到以下选项：

* **Download**：将当前工作流作为 JSON 文件下载到你的电脑。
* **Import from URL**：从 URL 导入 workflow JSON，例如 [GitHub 上的这个 workflow JSON 文件](https://raw.githubusercontent.com/n8n-io/self-hosted-ai-starter-kit/refs/heads/main/n8n/demo-data/workflows/srOnR8PAY3u4RSwb.json)。
* **Import from File**：从你的电脑导入 JSON 文件形式的工作流。

## 从命令行导入导出 <a href="#from-the-command-line" id="from-the-command-line"></a>

* 导出：查看用于导出工作流或凭据的[完整命令列表](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/use-the-command-line#export-workflows-and-credentials)。
* 导入：查看用于导入工作流或凭据的[完整命令列表](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/use-the-command-line#import-workflows-and-credentials)。

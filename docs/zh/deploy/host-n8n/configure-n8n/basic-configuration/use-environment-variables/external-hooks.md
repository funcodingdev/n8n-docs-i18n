---
title: External hooks environment variables
description: >-
  用于将 external hooks 集成到 self-hosted n8n 实例中的环境变量。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: External hooks
originalFilePath: hosting/configuration/environment-variables/external-hooks.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/external-hooks'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/external-hooks
layout:
  description:
    visible: false
---

# External hooks 环境变量 <a href="#external-hooks-environment-variables" id="external-hooks-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

你可以定义 external hooks，让 n8n 在特定操作运行时执行它们。完整参考请见 [External hooks](../../external-hooks.md)，其中包括可用 hooks 和文件格式。

| Variable | Type  | Default | Description |
| :------- | :---- | :------ | :---------- |
| `EXTERNAL_HOOK_FILES` | String | - | 包含 backend external hooks 的文件。提供多个文件时，用 `EXTERNAL_HOOK_FILES_SEPARATOR` 中定义的字符分隔。 |
| `EXTERNAL_HOOK_FILES_SEPARATOR` | String | `:` | `EXTERNAL_HOOK_FILES` 的分隔符。在 Windows 上使用 `;`，以避免与 `C:\` 这类 drive-letter paths 冲突。 |
| `EXTERNAL_FRONTEND_HOOKS_URLS` | String | - | 包含 frontend external hooks 的文件 URL。提供多个 URL 时使用冒号分隔列表（"`:`"）。 |

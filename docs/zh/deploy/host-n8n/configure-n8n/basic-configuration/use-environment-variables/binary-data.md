---
title: Binary data environment variables
description: >-
  使用环境变量自定义 self-hosted n8n 实例的 binary data 存储模式和路径。
contentType: reference
tags:
  - environment variables
hide:
  - toc
  - tags
nodeTitle: Binary data
originalFilePath: hosting/configuration/environment-variables/binary-data.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/environment-variables/binary-data'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/binary-data
layout:
  description:
    visible: false
---

# Binary data 环境变量 <a href="#binary-data-environment-variables" id="binary-data-environment-variables"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/ASsLuMLGKMy2O0q7awMF/" %}

默认情况下，n8n 使用内存存储 binary data。Enterprise 用户可以选择改用外部服务。有关为 binary data 使用外部存储的更多信息，请参考 [External storage](../../scaling/use-external-storage.md)。

| Variable | Type  | Default  | Description |
| :------- | :---- | :------- | :---------- |
| `N8N_AVAILABLE_BINARY_DATA_MODES` | String | `filesystem` | 可用 binary data 模式的逗号分隔列表。 |
| `N8N_BINARY_DATA_STORAGE_PATH` | String | `N8N_USER_FOLDER/binaryData` | n8n 存储 binary data 的路径。 |
| `N8N_DEFAULT_BINARY_DATA_MODE` | String | `default` | 默认 binary data 模式。`default` 将 binary data 保存在内存中。设为 `filesystem` 可使用文件系统，设为 `s3` 可使用 AWS S3，设为 `database` 可使用 DB。请注意，binary data pruning 只作用于当前启用的 binary data 模式。例如，如果你的实例曾在 S3 中存储数据，之后切换到 filesystem 模式，n8n 只会清理文件系统中的 binary data。未来此行为可能会改变。 |

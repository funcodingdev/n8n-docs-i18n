---
title: Specify user folder path
description: 指定存储 user-specific data 的 folder 位置。
contentType: howto
nodeTitle: Specify user folder path
originalFilePath: hosting/configuration/configuration-examples/user-folder.md
originalUrl: 'https://docs.n8n.io/hosting/configuration/configuration-examples/user-folder'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-user-folder-path
layout:
  description:
    visible: false
---

# 指定 user folder path <a href="#specify-user-folder-path" id="specify-user-folder-path"></a>

n8n 会将 encryption key、SQLite database file 以及 tunnel ID（如果使用）等 user-specific data 保存在启动 n8n 的 user 的 `.n8n` subfolder 中。可以使用环境变量覆盖 user-folder。

```bash
export N8N_USER_FOLDER=/home/jim/n8n
```
有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/deployment.md)。

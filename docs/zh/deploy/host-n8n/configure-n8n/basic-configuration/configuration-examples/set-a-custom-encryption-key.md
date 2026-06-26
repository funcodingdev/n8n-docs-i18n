---
title: Set a custom encryption key
description: 为 n8n 设置自定义 encryption key，以安全加密 credentials。
contentType: howto
nodeTitle: Set a custom encryption key
originalFilePath: hosting/configuration/configuration-examples/encryption-key.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/encryption-key
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/set-a-custom-encryption-key
layout:
  description:
    visible: false
---

# 设置自定义 encryption key <a href="#set-a-custom-encryption-key" id="set-a-custom-encryption-key"></a>

n8n 会在首次启动时自动创建随机 encryption key，并将其保存到 `~/.n8n` folder。n8n 在 credentials 保存到 database 前使用该 key 对其加密。如果 key 尚未在 settings file 中，你可以使用环境变量设置它，让 n8n 使用你的自定义 key，而不是生成新 key。

在 [queue mode](../../scaling/enable-queue-mode.md) 中，你必须为所有 workers 指定 encryption key 环境变量。

```bash
export N8N_ENCRYPTION_KEY=<SOME RANDOM STRING>
```
有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/deployment.md)。

---
title: Specify location for your custom nodes
description: 为 custom nodes 添加 folders 并指定 paths。
contentType: howto
nodeTitle: Specify custom nodes location
originalFilePath: hosting/configuration/configuration-examples/custom-nodes-location.md
originalUrl: >-
  https://docs.n8n.io/hosting/configuration/configuration-examples/custom-nodes-location
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/specify-custom-nodes-location
layout:
  description:
    visible: false
---

# 指定 custom nodes 的位置 <a href="#specify-location-for-your-custom-nodes" id="specify-location-for-your-custom-nodes"></a>

每个 user 都可以添加 custom nodes，n8n 会在启动时加载它们。默认位置是启动 n8n 的 user 的 `.n8n/custom` subfolder。

你可以用环境变量定义更多 folders：

```bash
export N8N_CUSTOM_EXTENSIONS="/home/jim/n8n/custom-nodes;/data/n8n/nodes"
```
有关此变量的更多信息，请参阅 [Environment variables reference](../use-environment-variables/nodes.md)。

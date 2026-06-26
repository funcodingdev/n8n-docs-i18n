---
title: 阻止访问 nodes
description: 防止 n8n 用户访问特定 nodes。
contentType: howto
nodeTitle: Block specific nodes
originalFilePath: hosting/securing/blocking-nodes.md
originalUrl: 'https://docs.n8n.io/hosting/securing/blocking-nodes'
url: >-
  https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/block-specific-nodes
layout:
  description:
    visible: false
---

# 阻止访问 nodes <a href="#block-access-to-nodes" id="block-access-to-nodes"></a>

出于安全原因，你可能想阻止用户访问或使用特定 n8n nodes。如果你的用户可能不可信，这会很有用。

使用 `NODES_EXCLUDE` 环境变量，防止用户访问特定 nodes。

## 排除 nodes <a href="#exclude-nodes" id="exclude-nodes"></a>

更新你的 `NODES_EXCLUDE` 环境变量，使其包含一个字符串数组，列出你想阻止用户使用的所有 nodes。

例如，以这种方式设置变量：

```
NODES_EXCLUDE: "[\"n8n-nodes-base.executeCommand\", \"n8n-nodes-base.readWriteFile\"]"
```

会阻止 [Execute Command](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executecommand) 和 [Read/Write Files from Disk](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.readwritefile) nodes。

你的 n8n 用户将无法搜索或使用这些 nodes。

## 建议阻止的 nodes <a href="#suggested-nodes-to-block" id="suggested-nodes-to-block"></a>

可能带来安全风险的 nodes 会因你的使用场景和用户画像而异。以下是一些可以先考虑的 nodes：

* [Execute Command](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.executecommand)
* [Read/Write Files from Disk](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.readwritefile)

## 启用默认被阻止的 nodes <a href="#enable-nodes-that-are-blocked-by-default" id="enable-nodes-that-are-blocked-by-default"></a>

某些 nodes（例如 Execute Command）默认会被阻止。要启用它们，请将其从 exclude list 中移除：

```
NODES_EXCLUDE: "[]"
```

## 相关资源 <a href="#related-resources" id="related-resources"></a>

有关此环境变量的更多信息，请参考 [Nodes environment variables](../basic-configuration/use-environment-variables/nodes.md)。

有关设置环境变量的更多信息，请参考 [Configuration](../basic-configuration.md)。

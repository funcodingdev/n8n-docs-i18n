---
contentType: overview
title: Cluster nodes
description: '了解 n8n 中的 cluster node，并浏览 cluster node 库。'
nodeTitle: Cluster nodes
originalFilePath: integrations/builtin/cluster-nodes/index.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/cluster-nodes'
url: 'https://docs.n8n.io/integrations/builtin/cluster-nodes'
layout:
  description:
    visible: false
---

# Cluster nodes <a href="#cluster-nodes" id="cluster-nodes"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/nQYOCBZiuZBtHlBAOFq9/" %}

## Root nodes <a href="#root-nodes" id="root-nodes"></a>

每个 cluster 都从一个 [root node](#user-content-fn-1)[^1] 开始。

## Sub-nodes <a href="#sub-nodes" id="sub-nodes"></a>

每个 root node 可以连接一个或多个 sub-node[^2]。

[^1]: 每个 n8n cluster node 都包含一个 root node，用于定义该 cluster 的主要功能。一个或多个 sub-node 会连接到 root node，以扩展其功能。
[^2]: n8n cluster node 由一个或多个连接到 root node 的 sub-node 组成。sub-node 会扩展 root node 的功能，提供对特定服务或资源的访问，或提供特定类型的专用处理，例如 calculator 功能。

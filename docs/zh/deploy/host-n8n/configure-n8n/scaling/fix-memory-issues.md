---
contentType: explanation
nodeTitle: Fix memory issues
originalFilePath: hosting/scaling/memory-errors.md
originalUrl: 'https://docs.n8n.io/hosting/scaling/memory-errors'
url: 'https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/fix-memory-issues'
layout:
  description:
    visible: false
---

# Memory-related errors <a href="#memory-related-errors" id="memory-related-errors"></a>

n8n 不限制每个 node 可获取和处理的数据量。虽然这给你带来自由度，但当 workflow executions 需要的内存超过可用内存时，也可能导致错误。本页说明如何识别和避免这些错误。

{% hint style="info" %}
**仅适用于 self-hosted n8n**

本页描述 [self-hosting n8n](../../README.md) 时的 memory-related errors。请访问 [Cloud data management](../../../use-n8n-cloud/configure-cloud/manage-your-data.md)，了解 [n8n Cloud](/manage-cloud/overview.md) 的 memory limits。
{% endhint %}

## 识别 out of memory 情况 <a href="#identifying-out-of-memory-situations" id="identifying-out-of-memory-situations"></a>

n8n 会在某些 out of memory 情况中提供警告性 error messages。例如类似 **Execution stopped at this node (n8n may have run out of memory while executing it)** 的消息。

包含 **Problem running workflow**、**Connection Lost** 或 **503 Service Temporarily Unavailable** 的 error messages 表明某个 n8n instance 已不可用。

self-hosting n8n 时，你还可能在 server logs 中看到类似 **Allocation failed - JavaScript heap out of memory** 的 error messages。

在 n8n Cloud 上，或使用 n8n Docker image 时，n8n 遇到这类问题会自动重启。但如果使用 npm 运行 n8n，你可能需要手动重启。

## 常见原因 <a href="#typical-causes" id="typical-causes"></a>

当 workflow execution 需要的内存超过 n8n instance 可用内存时，就会发生这类问题。会增加 workflow execution 内存使用量的因素包括：

- [JSON data](https://app.gitbook.com/s/rPN1zU5jaYNvwH7RzxqA/work-with-data/understand-n8ns-data-structure) 的数量。
- binary data 的大小。
- workflow 中的 nodes 数量。
- 某些 nodes 很占内存：[Code](https://app.gitbook.com/s/BKcbOzIWja8NfqKDcqHc/builtin/core-nodes/n8n-nodes-base.code) node 和较旧的 Function node 会显著增加内存消耗。
- 手动或自动 workflow executions：manual executions 会增加内存消耗，因为 n8n 会为 frontend 复制一份数据。
- 同时运行的额外 workflows。

## 避免 out of memory 情况 <a href="#avoiding-out-of-memory-situations" id="avoiding-out-of-memory-situations"></a>

遇到 out of memory 情况时，有两种选择：增加 n8n 可用内存，或减少内存消耗。

### 增加可用内存 <a href="#increase-available-memory" id="increase-available-memory"></a>

self-hosting n8n 时，增加 n8n 可用内存意味着为 n8n 实例配置更多内存。这可能会让你的 hosting provider 产生额外费用。

在 n8n cloud 上，你需要升级到更大的 plan。

### 减少内存消耗 <a href="#reduce-memory-consumption" id="reduce-memory-consumption"></a>

这种方式更复杂，意味着要重建导致问题的 workflows。本节提供一些减少内存消耗的指南。并非所有建议都适用于所有 workflows。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/EzVIOV8i2lmQ5HW3xFoo/" %}

### 增加 old memory <a href="#increase-old-memory" id="increase-old-memory"></a>

这适用于 self-hosting n8n。遇到 **JavaScript heap out of memory** 错误时，通常可以为 V8 JavaScript engine 的 old memory 区域分配额外内存。为此，请通过 CLI 或 `NODE_OPTIONS` [环境变量](https://nodejs.org/api/cli.html#node_optionsoptions)设置合适的 [V8 option](https://nodejs.org/api/cli.html#--max-old-space-sizesize-in-megabytes) `--max-old-space-size=SIZE`。

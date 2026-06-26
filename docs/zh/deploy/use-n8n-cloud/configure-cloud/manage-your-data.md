---
contentType: howto
nodeTitle: Manage your data
originalFilePath: manage-cloud/cloud-data-management.md
originalUrl: https://docs.n8n.io/manage-cloud/cloud-data-management
url: https://docs.n8n.io/deploy/use-n8n-cloud/configure-cloud/manage-your-data
description: 如何在 Cloud 上管理你的数据。
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

# 管理你的数据

在 Cloud 上管理数据时，需要关注两个问题：

* Memory usage：处理大量数据的复杂 workflows 可能超过 n8n 的内存限制。如果发生这种情况，实例可能 crash 并变得无法访问。
* Data storage：根据你的 execution 设置和数量，n8n database 可能不断变大并耗尽存储空间。

为避免这些问题，n8n 建议你在构建 workflows 时考虑内存效率，并且不要保存不必要的数据。

## 每个 Cloud plan 的内存限制 <a href="#memory-limits-on-each-cloud-plan" id="memory-limits-on-each-cloud-plan"></a>

当前 plans：

* Trial：320MiB RAM，10 millicore CPU burstable
* Starter：320MiB RAM，10 millicore CPU burstable
* Pro-1（10k executions）：640MiB RAM，20 millicore CPU burstable
* Pro-2（50k executions）：1280MiB RAM，80 millicore CPU burstable
* Enterprise：4096MiB RAM，80 millicore CPU burstable

旧版 plans：

* Start：320MiB RAM，10 millicore CPU burstable
* Power：1280MiB RAM，80 millicore CPU burstable

n8n 为每个实例提供最高 100GB 的 data storage。

## 如何减少 workflow 中的内存消耗 <a href="#how-to-reduce-memory-consumption-in-your-workflow" id="how-to-reduce-memory-consumption-in-your-workflow"></a>

你构建 workflows 的方式会影响它们执行时消耗的数据量。虽然这些指南并不适用于所有情况，但它们提供了一组最佳实践基线，可帮助避免超过实例内存。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/EzVIOV8i2lmQ5HW3xFoo/" %}

请注意，n8n 本身运行也会消耗内存。平均而言，仅软件本身就会使用约 180MiB RAM。

与 UI 的交互也会消耗内存。当 workflow UI 正在执行重型 executions 时继续操作它，也可能让内存容量超过限制。

## 如何在 Cloud 上管理 execution data <a href="#how-to-manage-execution-data-on-cloud" id="how-to-manage-execution-data-on-cloud"></a>

Execution data 包括 node data、parameters、variables、execution context 和 binary data references。它是基于文本的。

Binary data 是 n8n 无法表示为纯文本的非文本数据。这包括图像、文档、音频文件和视频等文件与媒体。它比文本数据大得多。

如果某个 workflow 消耗大量数据且已经过了测试阶段，停止保存 successful executions 是一个不错的选择。

你可以通过两种方式控制 n8n 在 database 中存储多少 execution data：

在管理后台中：

1. 从 workspace 或 editor 导航到 **Admin Panel**。
2. 选择 **Manage**。
3. 在 **Executions to Save** 中取消选择你不想记录的 executions。

在 workflow 设置中：

1. 选择 **Options** <img src="../../.gitbook/assets/three-dot-options-menu (1).png" alt="Options menu" data-size="line"> 菜单。
2. 选择 **Settings**。n8n 会打开 **Workflow settings** modal。
3. 将 **Save successful production executions** 更改为 **Do not save**。

## Cloud data pruning 和 out of memory incident prevention <a href="#cloud-data-pruning-and-out-of-memory-incident-prevention" id="cloud-data-pruning-and-out-of-memory-incident-prevention"></a>

### 自动 data pruning <a href="#automatic-data-pruning" id="automatic-data-pruning"></a>

n8n 会在经过一定时间后，或达到最大存储限制时自动 prune execution logs，以先发生者为准。Pruning 始终从最旧到最新执行，限制取决于你的 Cloud plan：

* Start 和 Starter plans：最多保存 2500 次 executions，并保留 7 天 execution log；
* Pro plans：最多保存 25000 次 executions，并保留 30 天 execution log；
* Enterprise plan：最多保存 50000 次 executions，execution log retention time 不受限制。

### 手动 data pruning <a href="#manual-data-pruning" id="manual-data-pruning"></a>

尽管有自动 pruning 机制，较重的 executions 和 use cases 仍可能超过 database 容量。在这种情况下，n8n 会手动 prune 数据以保护实例稳定性。

1. 当实例达到 85% disk capacity 时，alert system 会警告 n8n。
2. n8n 会 prune execution data。n8n 通过运行实例 backup（workflows、users、credentials 和 execution data）并在不包含 execution data 的情况下恢复它来完成此操作。

由于此流程包含人工步骤，alert system 并不完美。如果 warnings 在非工作时间触发，或者数据消耗速度较高，可能还没来得及 prune 数据，剩余磁盘空间就已经被填满。

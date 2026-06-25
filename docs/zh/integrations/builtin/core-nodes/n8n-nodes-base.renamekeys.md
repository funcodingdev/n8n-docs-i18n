---
title: Rename Keys
description: >-
  n8n 中 Rename Keys node 的文档。n8n 是一款 workflow 自动化平台。包含用法指导和示例链接。
contentType:
  - integration
  - reference
priority: medium
nodeTitle: Rename Keys
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys'
layout:
  description:
    visible: false
---

# Rename Keys <a href="#rename-keys" id="rename-keys"></a>

使用 Rename Keys node 重命名 n8n 中键值对的 key。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

你可以使用 Rename Keys node 重命名一个或多个 key。选择 **Add new key** 按钮来重命名 key。

对于每个 key，输入：

- **Current Key Name**：要重命名的 key 当前名称。
- **New Key Name**：要分配给该 key 的新名称。

## Node 选项 <a href="#node-options" id="node-options"></a>

选择是否使用 **Regex** 正则表达式来识别要重命名的 key。要使用此选项，还必须输入：

* 要使用的 **Regular Expression**。
* **Replace With**：输入要分配给匹配 **Regular Expression** 的 key 的新名称。
* 你还可以选择这些 Regex 专用选项：
    * **Case Insensitive**：设置正则表达式是否应匹配大小写（关闭），或忽略大小写（开启）。
    * **Max Depth**：输入替换 key 的最大深度，使用 `-1` 表示无限制，使用 `0` 表示仅顶层。

{% hint style="warning" %}
**Regex 影响**

使用正则表达式可能会影响任何匹配该表达式的 key，包括你已经重命名过的 key。
{% endhint %}

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>

[浏览 Rename Keys 集成模板](https://n8n.io/integrations/rename-keys)或[搜索所有模板](https://n8n.io/workflows/)

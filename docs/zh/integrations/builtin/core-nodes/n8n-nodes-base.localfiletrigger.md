---
title: Local File Trigger node 文档
description: >-
  了解如何在 n8n 中使用 Local File Trigger node。按照技术文档将
  Local File Trigger node 集成到你的 workflow 中。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Local File Trigger node 文档
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.localfiletrigger
layout:
  description:
    visible: false
---

# Local File Trigger node <a href="#local-file-trigger-node" id="local-file-trigger-node"></a>

当检测到文件系统发生变化时，Local File Trigger node 会启动 workflow。这些变化包括文件或文件夹被添加、修改或删除。

{% hint style="warning" %}
**安全注意事项**

在存在不可信用户的环境中，Local File Trigger node 可能带来显著安全风险。因此，从 2.0 版本开始，该 node 默认处于[禁用](https://app.gitbook.com/s/jm0ZYRpZIPWge2ZSiDYO/host-n8n/configure-n8n/security/block-specific-nodes#exclude-nodes)状态。
{% endhint %}

{% hint style="info" %}
**仅限 self-hosted n8n**

此 node 在 n8n Cloud 上不可用。
{% endhint %}

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

你可以使用 **Trigger On** 参数选择要监听的事件。

## 对特定文件的更改 <a href="#changes-to-a-specific-file" id="changes-to-a-specific-file"></a>

当指定文件发生变化时，该 node 会触发。

在 **File to Watch** 中输入要监听文件的路径。

## 涉及特定文件夹的更改 <a href="#changes-involving-a-specific-folder" id="changes-involving-a-specific-folder"></a>

当所选文件夹中发生更改时，该 node 会触发。

配置这些参数：

- **Folder to Watch**：输入要监听的文件夹路径。
- **Watch for**：选择要监听的更改类型。


## Node 选项 <a href="#node-options" id="node-options"></a>

使用 node 的 **Options** 来包含或排除文件和文件夹。

- **Include Linked Files/Folders**：同时监听 linked file 或 folder 的更改。
- **Ignore**：要忽略的文件或路径。n8n 会测试整个路径，而不仅是文件名。支持 [Anymatch](https://github.com/micromatch/anymatch) 语法。
- **Max Folder Depth**：监听文件夹结构变化的深度。

### Ignore 示例 <a href="#examples-for-ignore" id="examples-for-ignore"></a>

忽略单个文件：

```sh
**/<fileName>.<suffix>
# For example, **/myfile.txt <a href="#for-example-myfiletxt" id="for-example-myfiletxt"></a>
```

忽略正在监听目录中的一个子目录：

```sh
**/<directoryName>/**
# For example, **/myDirectory/** <a href="#for-example-mydirectory" id="for-example-mydirectory"></a>
```

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Local File Trigger node 集成模板](https://n8n.io/integrations/local-file-trigger)或[搜索所有模板](https://n8n.io/workflows/)

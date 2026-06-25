---
title: Execute Sub-workflow
description: >-
  n8n 中 Execute Sub-workflow node 的文档。n8n 是一个 workflow
  自动化平台。包含使用指导以及示例链接。
contentType:
  - integration
  - reference
priority: high
nodeTitle: Execute Sub-workflow
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md
originalUrl: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow
url: >-
  https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow
layout:
  description:
    visible: false
---

# Execute Sub-workflow <a href="#execute-sub-workflow" id="execute-sub-workflow"></a>

使用 Execute Sub-workflow node 可以在运行 n8n 的宿主机器上运行另一个 workflow。

## Node 参数 <a href="#node-parameters" id="node-parameters"></a>

### Source <a href="#source" id="source"></a>

选择该 node 应从哪里获取 sub-workflow 信息：

- **Database**：选择此选项，可通过 ID 从数据库加载 workflow。你还必须输入以下任一项：
	- **From list**：从你的账户可用 workflow 列表中选择 workflow。
	- **Workflow ID**：输入 workflow 的 ID。Workflow URL 在 `/workflow/` 后包含该 ID。例如，如果某个 workflow 的 URL 是 `https://my-n8n-acct.app.n8n.cloud/workflow/abCDE1f6gHiJKL7`，则 **Workflow ID** 为 `abCDE1f6gHiJKL7`。
- **Local File**：选择此选项，可从本地保存的 JSON 文件加载 workflow。你还必须输入：
	- **Workflow Path**：输入希望该 node 执行的本地 JSON workflow 文件路径。
- **Parameter**：选择此选项，可从参数加载 workflow。你还必须输入：
	- **Workflow JSON**：输入希望该 node 执行的 JSON 代码。
- **URL**：选择此选项，可从 URL 加载 workflow。你还必须输入：
	- **Workflow URL**：输入要从中加载 workflow 的 URL。

### Workflow Inputs <a href="#workflow-inputs" id="workflow-inputs"></a>

如果使用 **database** 和 **From list** 选项选择 sub-workflow，则 sub-workflow 的输入 item 会自动显示，供你填写或映射值。

你可以选择移除请求的输入 item，在这种情况下，sub-workflow 会收到 `null` 作为该 item 的值。你也可以启用 **Attempt to convert types**，尝试自动将数据转换为 sub-workflow item 请求的类型。

如果 sub-workflow 的 Workflow Input Trigger node 使用 "Accept all data" 输入数据模式，则不会显示输入 item。

### Mode <a href="#mode" id="mode"></a>

使用此参数控制该 node 的执行模式。可选：

- **Run once with all items**：将所有输入 item 传入该 node 的单次执行。
- **Run once for each item**：对每个输入 item 依次执行一次该 node。

## Node 选项 <a href="#node-options" id="node-options"></a>

此 node 包含一个选项：**Wait for Sub-Workflow Completion**。它让你控制主 workflow 是否应等待 sub-workflow 完成后再进入下一步（开启），或主 workflow 是否应不等待而继续执行（关闭）。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Execute Sub-workflow 集成模板](https://n8n.io/integrations/execute-workflow)或[搜索所有模板](https://n8n.io/workflows/)

## 设置并使用 sub-workflow <a href="#set-up-and-use-a-sub-workflow" id="set-up-and-use-a-sub-workflow"></a>

本节会演示如何设置 parent workflow 和 sub-workflow。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/wlwT5JcWyWTecnDN6aul/" %}


## 数据如何在 workflow 之间传递 <a href="#how-data-passes-between-workflows" id="how-data-passes-between-workflows"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/edKlUxnfiRMq38CujuFv/" %}

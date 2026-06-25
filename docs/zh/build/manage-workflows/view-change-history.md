---
title: 工作流历史
contentType: howto
nodeTitle: View change history
originalFilePath: workflows/history.md
originalUrl: https://docs.n8n.io/workflows/history
url: https://docs.n8n.io/build/manage-workflows/view-change-history
description: 查看并恢复工作流的旧版本。
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

# 查看变更历史

{% hint style="info" %}
**功能可用性**

* 完整 workflow history 适用于 Enterprise Cloud 和 Enterprise Self-hosted。
* 最近五天的版本适用于 Cloud Pro 用户。
* 最近 24 小时的版本适用于所有用户。
{% endhint %}

使用 workflow history 查看并恢复工作流的旧版本。

## 理解工作流历史 <a href="#understand-workflow-history" id="understand-workflow-history"></a>

以下情况下，n8n 会创建新版本：

* 保存工作流。
* 恢复旧版本。n8n 会在恢复前保存最新版本。
* 使用 [Source control](https://app.gitbook.com/s/wMJrGrimpx3PxCJpUswm/use-source-control-and-environments) 从 Git 仓库拉取。注意，n8n 会将版本保存到实例数据库，而不是 Git。

更改工作流设置不会创建新版本。

{% hint style="info" %}
**工作流历史和执行历史**

不要将 workflow history 与 [Workflow-level executions list](../understand-workflows/understand-executions/view-executions-for-a-single-workflow.md) 混淆。

Executions 是工作流运行记录。通过 executions list，你可以查看当前工作流版本的历史运行。你可以将历史执行复制到编辑器中，在当前工作流里[调试并重新运行过去的执行](../understand-workflows/understand-executions/debug-executions.md)。

Workflow history 是工作流的旧版本：例如包含不同节点，或设置了不同参数的版本。
{% endhint %}

## 查看工作流历史 <a href="#view-workflow-history" id="view-workflow-history"></a>

要查看工作流历史：

1. 打开工作流。
2. 选择 **Workflow history** <img src="../../../build/.gitbook/assets/workflow-history.png" alt="Workflow history icon" data-size="line">。n8n 会打开一个菜单，显示已保存的工作流版本，并在画布中预览选中的版本。

## 恢复或复制旧版本 <a href="#restore-or-copy-previous-versions" id="restore-or-copy-previous-versions"></a>

你可以恢复某个旧版本，或复制它：

1. 在要恢复或复制的版本上，选择 **Options** <img src="../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options icon" data-size="line">。
2. 选择要执行的操作：
   * **Restore version**：用选中版本替换当前工作流。
   * **Clone to new workflow**：基于选中版本创建新工作流。
   * **Open version in new tab**：打开第二个标签页显示选中版本。可用于比较版本。
   * **Download**：将该版本下载为 JSON。
   * **Name version**：为该版本设置名称和描述。命名版本不会被自动清理。更多详情请参阅[命名版本](../understand-workflows/save-and-publish-workflows.md#naming-versions)。适用于 Pro 和 Enterprise 方案。

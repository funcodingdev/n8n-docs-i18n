---
contentType: howto
nodeTitle: Create and run workflows
originalFilePath: workflows/create.md
originalUrl: https://docs.n8n.io/workflows/create
url: https://docs.n8n.io/build/understand-workflows/create-and-run-workflows
description: 创建、运行和发布工作流。
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

# 创建和运行工作流

工作流[^1]是一组相互连接的 node，用于自动化一个流程。你可以在[工作流画布](#user-content-fn-2)[^2]上构建工作流。

## 创建工作流 <a href="#create-a-workflow" id="create-a-workflow"></a>

1. 选择侧边菜单左上角的 <img src="../../../build/.gitbook/assets/universal-resource-button (1).png" alt="universal create resource icon" data-size="line"> **按钮**。选择 workflow。
2. 如果你的 n8n 实例支持 project，还需要选择是在你的 **personal space** 中创建工作流，还是在你有权访问的特定 **project** 中创建。如果你使用的是社区版，则始终会在 personal space 中创建工作流。
3. 添加 trigger node 开始构建：选择 **Add first step...**

或者：

1. 在 **Overview** 页面或某个特定 **project** 中，选择右上角的 <img src="../../../build/.gitbook/assets/universal-resource-button (1).png" alt="universal create resource icon" data-size="line"> **create** 按钮。选择 workflow。
2. 如果你是在 **Overview** 页面执行此操作，工作流会创建在你的 personal space 中。如果你是在某个 project 中执行此操作，工作流会创建在该 project 中。
3. 添加 trigger node 开始构建：选择 **Add first step...**

如果这是你第一次构建工作流，可以使用[快速入门指南](../../../try-it-out/index.md)快速试用 n8n 功能。

## 手动运行工作流 <a href="#run-workflows-manually" id="run-workflows-manually"></a>

在构建和测试工作流时，或者当工作流没有 trigger node 时，你可能需要手动运行工作流。

如需手动运行，选择 **Execute Workflow**。

## 自动运行工作流 <a href="#run-workflows-automatically" id="run-workflows-automatically"></a>

所有新工作流默认都是未发布状态。参阅[发布和保存工作流](save-and-publish-workflows.md)。

以 trigger node 或 Webhook node 开始的工作流需要发布后才能自动运行。当工作流处于 inactive 状态时，必须手动运行。

如需发布工作流，打开工作流并点击 **Publish**。取消发布的选项位于工作流设置菜单中。

已发布的工作流会在触发条件满足时运行。

[^1]: n8n workflow 是一组用于自动化流程的 node。工作流会在触发条件发生时开始执行，并按顺序执行以完成复杂任务。
[^2]: 画布是 n8n 编辑器 UI 中用于构建工作流的主要界面。你可以在画布上添加并连接 node 来组成工作流。

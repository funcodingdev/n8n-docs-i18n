---
contentType: howto
nodeTitle: Save and publish workflows
originalFilePath: workflows/publish.md
originalUrl: https://docs.n8n.io/workflows/publish
url: https://docs.n8n.io/build/understand-workflows/save-and-publish-workflows
description: 保存、发布、取消发布工作流，并命名工作流版本。
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

# 保存和发布工作流

n8n 会在你编辑时自动保存工作流。当你准备将工作流投入生产时，发布该工作流。这种方式可以在支持安全迭代和审查的同时，避免意外修改生产版本。

## 保存机制 <a href="#how-saving-works" id="how-saving-works"></a>

编辑时更改会自动保存，通常在 1 到 5 秒内完成。不需要手动保存按钮。发布之前，所有编辑都会保留在草稿中。

## 发布机制 <a href="#how-publishing-works" id="how-publishing-works"></a>

发布会让工作流上线，并将其锁定到一个特定版本。生产执行会使用这个已发布版本，而不是你的最新编辑。发布后，工作流会启用以下能力：

* Webhook 和 form trigger 会使用生产 URL
* Schedule 会在你定义的时间运行
* 已连接 app 中的事件会触发此工作流

**初始状态** 打开没有可发布更改的工作流时，Publish 按钮处于禁用状态。

![](../../../build/.gitbook/assets/publish-initial.png)

**准备发布** 当工作流尚未发布但已有更改时，按钮会变为可用。

![](../../../build/.gitbook/assets/publish-ready.png)

**已发布，且为最新** 工作流当前已发布，并且自上次发布以来没有新的更改。

![](../../../build/.gitbook/assets/published.png)

**已发布，但有更改** 工作流已发布，但你在上次发布后做了尚未上线的更改。

![](../../../build/.gitbook/assets/published-changes.png)

**已发布，但更改无效** 工作流已发布，但当前状态无法重新发布（没有需要发布的 trigger）。

![](../../../build/.gitbook/assets/published-invalid.png)

**已发布，但存在错误** 工作流已发布，但最近的更改中存在错误，需要修复后才能再次发布。

![](../../../build/.gitbook/assets/published-error.png)

## 协作机制 <a href="#how-collaboration-works" id="how-collaboration-works"></a>

同一时间只有一个人可以编辑工作流。如果其他人正在编辑：

* 你会以只读模式查看工作流
* 当对方停止编辑或变为非活跃状态时，编辑锁会释放
* 随后你可以基于最新更改接管编辑

## 检查发布状态 <a href="#checking-publishing-status" id="checking-publishing-status"></a>

在 **Workflows** 页面，如果工作流已发布，其卡片上会显示指示标记。

![](../../../build/.gitbook/assets/published-indicator-wf-list.png)

## 发布工作流 <a href="#publishing-a-workflow" id="publishing-a-workflow"></a>

只要存在未发布更改，画布顶部的 **Publish** 按钮就会启用。

每次你修改工作流时，n8n 都会自动将这些更改保存为工作流的新版本。只有在更改后发布工作流，这些已保存版本才会在生产环境生效。

1. 点击 **Publish** 按钮（或使用快捷键 `Shift` + `p`）打开发布弹窗。
2. 版本名称默认为 UUID。你可以按需自定义名称，并添加版本描述。
3.  点击 **Publish** 让更改在生产环境生效。生产执行始终指向当前已发布版本。

    如果你只更新工作流设置，n8n 会重新发布该版本，无需你执行任何操作。

![](../../../build/.gitbook/assets/publish-modal.png)

## 命名版本 <a href="#naming-versions" id="naming-versions"></a>

{% hint style="info" %}
**功能可用性**

命名版本适用于 Pro 和 Enterprise Cloud 计划，以及 Enterprise 自托管计划。
{% endhint %}

命名版本允许你为任意工作流版本提供有意义的名称和描述。这有助于识别工作流开发过程中的重要里程碑。命名版本也会受到保护，不会被自动[版本历史清理](../manage-workflows/view-change-history.md)删除，因此会无限期保留。

从画布顶部命名版本：

1. 选择 **Publish** 按钮旁边的下拉箭头（或使用快捷键 `Cmd/Ctrl` + `s`）。
2. 选择 **Name version**。
3. 输入名称和可选描述。
4. 选择 **Save**。

![](../../../build/.gitbook/assets/publish-dropdown.png)

从版本历史页面命名版本：

1. 选择顶部的历史图标，打开版本历史。
2. 在要命名的版本上，选择 **Options** <img src="../../../build/.gitbook/assets/three-dot-options-menu (1).png" alt="Options icon" data-size="line">。
3. 选择 **Name version**。
4. 输入名称和可选描述。
5. 选择 **Save**。

## 管理版本历史 <a href="#managing-version-history" id="managing-version-history"></a>

点击顶部的历史图标即可查看和管理版本历史。在版本历史视图中，你可以执行以下操作：

* 取消发布工作流，将其从生产环境移除
* 恢复先前版本。恢复后，你可以在不影响生产执行的情况下处理该版本
* 发布工作流的另一个版本
* 命名版本，防止该版本被清理

## 如何取消发布工作流 <a href="#how-to-unpublish-a-workflow" id="how-to-unpublish-a-workflow"></a>

你可以从以下位置取消发布工作流：

* 画布顶部 **Publish** 按钮旁边的下拉箭头（或使用快捷键 `Cmd/Ctrl` + `u`）。
* 工作流列表
* 版本历史页面（针对已发布版本的取消发布操作）

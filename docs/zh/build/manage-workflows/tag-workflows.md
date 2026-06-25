---
title: 工作流标签
description: '使用标签标记工作流，让浏览工作流更容易。'
contentType: howto
nodeTitle: Tag workflows
originalFilePath: workflows/tags.md
originalUrl: 'https://docs.n8n.io/workflows/tags'
url: 'https://docs.n8n.io/build/manage-workflows/tag-workflows'
layout:
  description:
    visible: false
---

# 标签 <a href="#tags" id="tags"></a>

Workflow tags 允许你标记工作流。之后你可以按标签筛选工作流。

Tags 是全局的。这意味着创建 tag 后，n8n 实例上的所有用户都可以使用它。

## 给工作流添加标签 <a href="#add-a-tag-to-a-workflow" id="add-a-tag-to-a-workflow"></a>

要给工作流添加标签：

1. 在工作流中选择 **+ Add tag**。
2. 选择已有标签，或输入新的标签名称。
3. 选择标签并离开标签弹窗后，n8n 会在工作流名称旁显示该标签。

你可以添加多个标签。

## 按标签筛选 <a href="#filter-by-tag" id="filter-by-tag"></a>

浏览实例上的工作流时，可以按标签筛选。

1. 在 **Workflows** 页面选择 **Filters**。
2. 选择 **Tags**。
3. 选择一个或多个要筛选的标签。n8n 会列出带有这些标签的工作流。

## 管理标签 <a href="#manage-tags" id="manage-tags"></a>

你可以编辑已有标签。实例所有者可以删除标签。

1. 选择 **Manage tags**。它可以从 **Workflows** 页面的 **Filters** > **Tags** 打开，也可以在工作流中的 **+ Add tag** 弹窗中打开。
2. 将鼠标悬停在要修改的标签上。
3. 选择 **Edit** <img src="../../../build/.gitbook/assets/edit.png" alt="Add node icon" data-size="line"> 重命名，或选择 **Delete** <img src="../../../build/.gitbook/assets/delete.png" alt="Add node icon" data-size="line"> 删除。

{% hint style="warning" %}
**全局标签**

Tags 是全局的。如果你编辑或删除某个 tag，会影响 n8n 实例上的所有用户。
{% endhint %}

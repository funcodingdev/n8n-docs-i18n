---
title: Git
description: >-
  n8n 中 Git node 的文档。n8n 是一个 workflow 自动化平台。
  包含使用指导以及示例链接。
contentType:
  - integration
  - reference
nodeTitle: Git
originalFilePath: integrations/builtin/core-nodes/n8n-nodes-base.git.md
originalUrl: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git'
url: 'https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.git'
layout:
  description:
    visible: false
---

# Git <a href="#git" id="git"></a>

[Git](https://git-scm.com/) 是一个免费开源的分布式版本控制系统，旨在快速高效地处理从小型到大型的各种项目。

{% hint style="info" %}
**Credentials**

你可以在[这里](../credentials/git.md)找到该 node 的身份验证信息。
{% endhint %}

## 操作 <a href="#operations" id="operations"></a>

* **Add** 文件或文件夹到 commit。执行 [git add](https://git-scm.com/docs/git-add)。
* **Add Config**：添加配置属性。执行 [git config](https://git-scm.com/docs/git-config) set 或 add。
* **Clone** repository：执行 [git clone](https://git-scm.com/docs/git-clone)。
* **Commit** 文件或文件夹到 git。执行 [git commit](https://git-scm.com/docs/git-commit)。
* **Fetch** 远程 repository。执行 [git fetch](https://git-scm.com/docs/git-fetch)。
* **List Config**：返回当前配置。执行 [git config](https://git-scm.com/docs/git-config) query。
* **Log**：返回 git commit 历史。执行 [git log](https://git-scm.com/docs/git-log)。
* 从远程 repository **Pull**：执行 [git pull](https://git-scm.com/docs/git-pull)。
* **Push** 到远程 repository：执行 [git push](https://git-scm.com/docs/git-push)。
* **Push Tags** 到远程 repository：执行 [git push --tags](https://git-scm.com/docs/git-push#Documentation/git-push.txt---tags)。
* 返回当前 repository 的 **Status**：执行 [git status](https://git-scm.com/docs/git-status)。
* **Switch Branch:** 执行 [git switch](https://git-scm.com/docs/git-switch)。
* 创建新的 **Tag**：执行 [git tag](https://git-scm.com/docs/git-tag)。
* **User Setup**：设置用户。

有关每个操作的参数和选项的更多详情，请参阅下面各节。

## Add <a href="#add" id="add"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Paths to Add**：在此字段中输入逗号分隔的文件或文件夹路径列表。你可以使用绝对路径，也可以使用相对于 **Repository Path** 的相对路径。



## Add Config <a href="#add-config" id="add-config"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Key**：输入要设置的 key 名称。
* **Value**：输入要设置的 key 值。

### Add Config 选项 <a href="#add-config-options" id="add-config-options"></a>

Add config 操作会添加 **Mode** 选项。选择在本地 config 中 **Set** 还是 **Append** 该设置。


## Clone <a href="#clone" id="clone"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Authentication**：选择 **Authenticate** 以传入 credentials。选择 **None** 则不使用身份验证。
    * **Credential for Git**：如果选择 **Authenticate**，必须选择或创建该 node 要使用的 credentials。更多信息请参阅 [Git credential](../credentials/git.md)。
* **New Repository Path**：输入希望放置 cloned repository 的本地路径。
* **Source Repository**：输入要 clone 的 repository URL 或路径。

## Commit <a href="#commit" id="commit"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Message**：在此字段中输入要使用的 commit message。

### Commit 选项 <a href="#commit-options" id="commit-options"></a>

Commit 操作会添加 **Paths to Add** 选项。要 commit 所有 "added" 文件和文件夹，请将此字段留空。要 commit 特定的 "added" 文件和文件夹，请在此字段中输入逗号分隔的文件或文件夹路径列表。

你可以使用绝对路径，也可以使用相对于 **Repository Path** 的相对路径。

## Fetch <a href="#fetch" id="fetch"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。



## List Config <a href="#list-config" id="list-config"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。


## Log <a href="#log" id="log"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Return All**：开启后，该 node 会返回所有结果。关闭后，该 node 会返回最多 **Limit** 指定数量的结果。
* **Limit**：仅在关闭 **Return All** 时可用。输入要返回的最大结果数。

### Log 选项 <a href="#log-options" id="log-options"></a>

Log 操作会添加 **File** 选项。在此字段中输入文件或文件夹路径，以获取其历史记录。

你可以使用绝对路径，也可以使用相对于 **Repository Path** 的相对路径。

## Pull <a href="#pull" id="pull"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。

## Push <a href="#push" id="push"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Authentication**：选择 **Authenticate** 以传入 credentials，或选择 **None** 不使用身份验证。
    * 如果选择 **Authenticate**，必须选择或创建该 node 要使用的 **Credential for Git**。更多信息请参阅 [Git credential](../credentials/git.md)。

### Push 选项 <a href="#push-options" id="push-options"></a>

Push 操作会添加 **Target Repository** 选项。在此字段中输入要 push 到的 repository URL 或路径。

## Push Tags <a href="#push-tags" id="push-tags"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。

## Status <a href="#status" id="status"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。

## Switch Branch <a href="#switch-branch" id="switch-branch"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Branch Name**：输入要切换到的 branch 名称。

## Tag <a href="#tag" id="tag"></a>

使用这些参数配置该操作：

* **Repository Path**：输入 git repository 的本地路径。
* **Name**：在此字段中输入要创建的 tag 名称。

## User Setup <a href="#user-setup" id="user-setup"></a>

此操作只会提示你在 **Repository Path** 参数中输入 git repository 的本地路径。

## 模板和示例 <a href="#templates-and-examples" id="templates-and-examples"></a>


[浏览 Git 集成模板](https://n8n.io/integrations/git)或[搜索所有模板](https://n8n.io/workflows/)

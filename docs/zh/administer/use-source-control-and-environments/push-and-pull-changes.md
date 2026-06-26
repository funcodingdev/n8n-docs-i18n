---
title: Push and pull
description: 将 work 发送到 Git，并从 Git fetch work 到你的 instance。
contentType: howto
nodeTitle: Push and pull changes
originalFilePath: source-control-environments/using/push-pull.md
originalUrl: 'https://docs.n8n.io/source-control-environments/using/push-pull'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/push-and-pull-changes
layout:
  description:
    visible: false
---

# Push and pull <a href="#push-and-pull" id="push-and-pull"></a>

如果你的 n8n instance 连接到 Git repository，就需要让 work 与 Git 保持 sync。

本文档假设你熟悉一些 Git concepts 和 terminology。关于 n8n 如何与 Git 协作的介绍，请参考 [Git and n8n](use-git-in-n8n.md)。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sVOSvjfqJPLqOGb1x77B/" %}

## Fetch 其他人的 work <a href="#fetch-other-peoples-work" id="fetch-other-peoples-work"></a>

{% hint style="info" %}
**n8n roles 控制哪些 users 可以 pull (fetch) changes**

你必须是 instance owner 或 instance admin，才能从 git pull changes。
{% endhint %}

要从 Git pull work，请在 main menu 中选择 **Pull** <img src="../.gitbook/assets/pull-icon.png" alt="Pull icon" data-size="line">。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/z7oYIete6nifvfi0QZKs/" %}

n8n 可能会显示关于 overriding local changes 的 warning。选择 **Pull and override**，用 Git 中的 content 覆盖 local work。

当 changes 包含 new variable 或 credential stubs 时，n8n 会通知你需要在使用这些 items 前填充 values。

{% hint style="info" %}
**如何处理 deleted resources**

当 workflows、credentials、variables、tags 和 data tables 从 repository 中删除时，你的 local versions 不会自动删除。相反，当你 pull repository changes 时，n8n 会通知你任何 outdated resources，并询问是否要删除它们。
{% endhint %}

### Pull 时 workflow 和 credential owner 可能改变 <a href="#workflow-and-credential-owner-may-change-on-pull" id="workflow-and-credential-owner-may-change-on-pull"></a>

当你从 Git pull 到 n8n instance 时，n8n 会尝试将 workflows 和 credentials 分配给 matching user 或 project。

如果 original owner 是 user：

如果两个 instances 上都有同一个 owner（email 匹配），owner 保持不变。如果 original owner 不在 new instance 上，n8n 会将执行 pull 的 user 设置为 workflow owner。

如果 original owner 是 [project](../manage-users-and-access/set-permissions-and-roles-rbac/README.md)：

n8n 会尝试将 original project name 匹配到 new instance 上的 project name。如果没有 matching project，n8n 会用该 name 创建 new project，将 current user 分配为 project owner，并将 workflows 和 credentials import 到该 project。

### Pull 时 auto publish workflows <a href="#auto-publish-workflows-on-pull" id="auto-publish-workflows-on-pull"></a>

Pull 时，你可以使用 pull modal 中的 **Auto publish** dropdown 选择自动 publish workflows。它有三种 modes：

* **Off**（default）：不尝试 publish 任何 workflows。Workflows 保持当前 local publish state。
* **If workflow already published**：只尝试 publish 已在此 instance 上 published 的 workflows。New workflows 不会 publish。
* **On**：尝试 publish 所有 pulled workflows，包括 new workflows。

无论 auto publish setting 如何，n8n 永远不会 auto publish archived workflows。

启用 auto publish 后 pull，n8n 会显示 results modal，展示哪些 workflows 成功 published，哪些 failed。如果 workflow 有 validation errors 或 missing credentials，publishing 可能 fail。

Auto publish 也可以通过 [API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api/api-reference) 使用 pull endpoint 上的 `autoPublish` parameter 实现，其值为 `none`、`published` 或 `all`。

### Pulling 可能导致短暂 service interruption <a href="#pulling-may-cause-brief-service-interruption" id="pulling-may-cause-brief-service-interruption"></a>

如果你 pull changes 到 published workflow，n8n 会在 pulling 期间 unpublish workflow，然后再 republish。这可能导致 workflow 几秒 downtime。

## 将你的 work 发送到 Git <a href="#send-your-work-to-git" id="send-your-work-to-git"></a>

{% hint style="info" %}
**n8n roles 控制哪些 users 可以 push changes**

你必须是 instance owner、instance admin 或 project admin，才能 push changes to git。
{% endhint %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/jlwygEO1bOtH6HDbN3We/" %}

## 会 commit 哪些内容 <a href="#what-gets-committed" id="what-gets-committed"></a>

n8n 会将以下内容 commit 到 Git：

* Workflows，包括其 tags 和 workflow owner 的 email address。你可以选择要 push 的 workflows。
* Credential stubs - ID、name 和 type。其他 fields 只有在它们是 [expressions](https://docs.n8n.io/data/expressions/) 时才会包含。你可以选择要 push 的 credentials。
* Variable stubs（ID 和 name）
* Data table schemas（table name 和 column definitions，不包括 row data）。你可以选择要 push 的 data tables。
* Projects
* Folders

## Merge behaviors 和 conflicts <a href="#merge-behaviors-and-conflicts" id="merge-behaviors-and-conflicts"></a>

n8n 的 source control implementation 带有明确取向。它会自动解决 credentials 和 variables 的 merge conflicts。n8n 无法 detect workflows 上的 conflicts。

### Workflows <a href="#workflows" id="workflows"></a>

Push 或 pull 时，你必须明确告诉 n8n 如何处理 workflows。Git repository 是 source of truth。

Pull 时，你可能会收到 warning，提示 workflow 的 local copy 与 Git 不同；如果接受，local copy 会被覆盖。Pull 时请小心，不要丢失 relevant changes。

Push 时，local workflow 会覆盖 Git 中的内容，因此请确保你拥有最新 version，否则可能覆盖 recent changes。

为防止上述问题，应在完成 workflow 工作后立即 push changes。然后再 pull 就是安全的。

为避免 data loss：

* 设计 source control setup，让 workflows 单向流动。例如，在 development instance 上编辑，push 到 Git，然后 pull 到 production。不要在 production instance 上编辑并 push。
* 不要 push all workflows。选择你需要的 workflows。
* 谨慎手动编辑 Git repository 中的 files。

### Credentials、variables 和 workflow tags <a href="#credentials-variables-and-workflow-tags" id="credentials-variables-and-workflow-tags"></a>

Credentials 和 variables 不会有 merge issues，因为 n8n 会选择要保留的 version。

Pull 时：

* 如果 tag、variable 或 credential 不存在，n8n 会创建它。
* 如果 tag、variable 或 credential 已存在，n8n 不会 update 它，除非：
	* 你使用 API 或 externally 设置 variable value。New value 会覆盖 existing value。
	* Credential name 已更改。n8n 使用 Git 中的 version。
	* Tag name 已更改。n8n 会 update tag name。Renaming tags 时请小心，因为 tag names 是 unique 的，这可能在 pull process 中涉及 uniqueness 时导致 database issues。

Push 时：

* n8n 会覆盖 entire variables 和 tags files。
* 如果 credential 已存在，n8n 会用 changes 覆盖它，但 pull 时不会将这些 changes 应用到 existing credentials。

### Data tables <a href="#data-tables" id="data-tables"></a>

n8n 会跨 environments sync data table schemas（table structure 和 column definitions）。Row data 不会 sync。

Push 时：

* 你可以选择包含哪些 data tables。
* n8n 会 export table name、column names、column types 和 column order。

Pull 时：

* n8n 会创建本地不存在的 new data tables。
* 对于 existing data tables，n8n 会 update schema，使其匹配 Git 中的 version。这包括添加 new columns 和移除 remote version 中不再存在的 columns。

{% hint style="warning" %}
**Column removal 会导致 data loss**

如果 pulled data table 相比 local version 移除了 columns，n8n 会删除这些 columns 及其 data。此操作无法撤销。当这将发生时，n8n 会在 pull modal 中显示 warning。
{% endhint %}

{% hint style="info" %}
**使用 external secrets vault 管理 credentials**

如果你需要在不同 n8n environments 上使用不同 credentials，请使用 [external secrets](../manage-credentials/use-external-secret-stores.md)。
{% endhint %}

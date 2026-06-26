---
title: Tutorial - Create environments with source control
description: 如何使用 n8n 的 source control feature 创建 environments。
contentType: tutorial
nodeTitle: 'Tutorial: Create environments with source control'
originalFilePath: source-control-environments/create-environments.md
originalUrl: 'https://docs.n8n.io/source-control-environments/create-environments'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/tutorial-create-environments-with-source-control
layout:
  description:
    visible: false
---

# Tutorial: Create environments with source control <a href="#tutorial-create-environments-with-source-control" id="tutorial-create-environments-with-source-control"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/2T2SmMUgiLyck7FDDwRD/" %}

本 tutorial 会演示端到端设置 environments 的 process。你会创建两个 environments：development 和 production。它使用 GitHub 作为 Git provider。其他 providers 的 process 类似。

n8n 将 environments feature 构建在 Git 这一 version control software 之上。你将 n8n instance 链接到 Git branch，并使用 push-pull pattern 在 environments 之间移动 work。你应该对 environments 和 Git 有一定了解。如果需要更多相关信息，请参考：

* [Environments in n8n](work-with-environments.md)：environments 的目的，以及它们在 n8n 中如何工作。
* [Git and n8n](use-git-in-n8n.md)：n8n 中的 Git concepts 和 source control。

## 选择 source control pattern <a href="#choose-your-source-control-pattern" id="choose-your-source-control-pattern"></a>

在设置 source control 和 environments 前，你需要规划 environments，以及它们与 Git branches 的关系。n8n 支持不同 [Branch patterns](choose-branching-patterns.md)。对于 environments，你需要在两种 patterns 之间选择：multi-instance, multi-branch，或 multi-instance, single-branch。本 tutorial 覆盖这两种 patterns。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sVOSvjfqJPLqOGb1x77B/" %}

### Multiple instances, multiple branches <a href="#multiple-instances-multiple-branches" id="multiple-instances-multiple-branches"></a>

![Diagram](../.gitbook/assets/vc-multi-multi.png)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/O5AqRfApNuiINXZOe5j1/" %}

### Multiple instances, one branch <a href="#multiple-instances-one-branch" id="multiple-instances-one-branch"></a>

![Diagram](../.gitbook/assets/vc-multi-one.png)

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Vo4DpZeEyTa0iuufMDB8/" %}

## 设置 repository <a href="#set-up-your-repository" id="set-up-your-repository"></a>

选择 pattern 后，需要设置 GitHub repository。

{% tabs %}
{% tab title="Multi-branch" %}
1. [Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。
    * 确保 repository 是 private，除非你希望 workflows、tags、variable 和 credential stubs 暴露到 internet。
    * 使用 README 创建 new repository，这样你可以立即创建 branches。
1. 创建一个名为 `production` 的 branch 和另一个名为 `development` 的 branch。请参考 [Creating and deleting branches within your repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) 获取 guidance。
{% endtab %}

{% tab title="Single-branch" %}
[Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)。

  * 确保 repository 是 private，除非你希望 workflows、tags、variable 和 credential stubs 暴露到 internet。<br>
  * 使用 README 创建 new repository。这会创建 `main` branch，你会连接到它。
{% endtab %}
{% endtabs %}

## 将 n8n instances 连接到 repository <a href="#connect-your-n8n-instances-to-your-repository" id="connect-your-n8n-instances-to-your-repository"></a>

创建两个 n8n instances，一个用于 development，一个用于 production。

### 在 n8n 中配置 Git <a href="#configure-git-in-n8n" id="configure-git-in-n8n"></a>

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/UqTgO2VbAzax4T8z4Fyh/" %}

### 设置 deploy key <a href="#set-up-a-deploy-key" id="set-up-a-deploy-key"></a>

使用 n8n 中的 SSH key 为 repository 创建 deploy key，以设置 SSH access。该 key 必须具有 write access。Guidance 请参考 [GitHub | Managing deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)。

### 连接 n8n 并配置 instance <a href="#connect-n8n-and-configure-your-instance" id="connect-n8n-and-configure-your-instance"></a>

{% tabs %}
{% tab title="Multi-branch" %}
1. 在 n8n 的 **Settings** > **Environments** 中，选择 **Connect**。n8n 会连接到你的 Git repository。
1. 在 **Instance settings** 下，选择当前 n8n instance 要使用的 branch。将 production branch 连接到 production instance，将 development branch 连接到 development instance。
1. 仅 production instance：选择 **Protected instance**，防止 users 在此 instance 中编辑 workflows。
1. 选择 **Save settings**。
{% endtab %}

{% tab title="Single-branch" %}
1. 在 n8n 的 **Settings** > **Environments** 中，选择 **Connect**。
  1. 在 **Instance settings** 下，选择 main branch。
1. 仅 production instance：选择 **Protected instance**，防止 users 在此 instance 中编辑 workflows。
1. 选择 **Save settings**。
{% endtab %}
{% endtabs %}

## 从 development push work <a href="#push-work-from-development" id="push-work-from-development"></a>

在 development instance 中，创建一些 workflows、tags、variables 和 credentials。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/jlwygEO1bOtH6HDbN3We/" %}

## 将 work pull 到 production <a href="#pull-work-to-production" id="pull-work-to-production"></a>

你的 work 现在已经在 GitHub 中。如果你使用 multi-branch setup，它在 development branch 上。如果选择 single-branch setup，它在 main 上。

{% tabs %}
{% tab title="Multi-branch" %}
1. 在 GitHub 中，创建 pull request，将 development merge 到 production。
1. Merge pull request。
1. 在 production instance 中，在 main menu 中选择 **Pull** <img src="../.gitbook/assets/pull-icon.png" alt="Pull icon" data-size="line">。
{% endtab %}

{% tab title="Single-branch" %}
在 production instance 中，在 main menu 中选择 **Pull** <img src="../.gitbook/assets/pull-icon.png" alt="Pull icon" data-size="line">。
{% endtab %}
{% endtabs %}

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/z7oYIete6nifvfi0QZKs/" %}

### Optional：使用 GitHub Action 自动化 pulls <a href="#optional-use-a-github-action-to-automate-pulls" id="optional-use-a-github-action-to-automate-pulls"></a>

如果你想避免登录 production instance 来 pull，可以使用 [GitHub Action](https://docs.github.com/en/actions/creating-actions/about-custom-actions) 和 [n8n API](https://app.gitbook.com/s/r7wKI4I1BgdBCuq5Cvcx/n8n-api)，在每次将 new work push 到 production 或 main branch 时自动 pull。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/niFQjDjbGJDJTKB57Z1s/" %}

## 下一步 <a href="#next-steps" id="next-steps"></a>

了解更多：

* [Environments in n8n](work-with-environments.md) 和 [Git and n8n](use-git-in-n8n.md)
* [Source control patterns](choose-branching-patterns.md)

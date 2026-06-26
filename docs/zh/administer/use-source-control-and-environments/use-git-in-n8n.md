---
title: Git and n8n
description: n8n 中的 Git concepts 和 limitations。
contentType: explanation
nodeTitle: Use Git in n8n
originalFilePath: source-control-environments/understand/git.md
originalUrl: 'https://docs.n8n.io/source-control-environments/understand/git'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/use-git-in-n8n
layout:
  description:
    visible: false
---

# Git and n8n <a href="#git-and-n8n" id="git-and-n8n"></a>

n8n 使用 Git 提供 source control。要使用此 feature，了解一些 basic Git concepts 会有帮助。n8n 不实现所有 Git functionality：你不应将 n8n 的 source control 视为完整 version control。

{% hint style="info" %}
**刚接触 Git 和 source control？**

如果你刚接触 Git，不必担心。你不需要学习 Git 才能使用 n8n。本文档会解释你需要的 concepts。但设置 source control 时需要一些 Git knowledge，因为这涉及在 Git provider 中操作。
{% endhint %}
{% hint style="info" %}
**熟悉 Git 和 source control？**

如果你熟悉 Git，请不要依赖完全一致的 behaviors。特别要注意，n8n 中的 source control 不支持 pull request-style review 和 merge process，除非你在 n8n 外部的 Git provider 中完成。
{% endhint %}

本页面介绍 n8n 中使用的 Git concepts 和 terminology。它不会覆盖设置和管理 repository 所需的一切。执行 [Setup](set-up-source-control.md) 的人应熟悉 Git 和自己的 Git hosting provider。

{% hint style="info" %}
**这是简要介绍**

Git 是一个复杂主题。本 section 简要介绍在 n8n 中使用 environments 时所需的 key terms。如果你想深入学习 Git，请参考 [GitHub | Git and GitHub learning resources](https://docs.github.com/en/get-started/quickstart/git-and-github-learning-resources)。
{% endhint %}

## Git overview <a href="#git-overview" id="git-overview"></a>

[Git](https://git-scm.com/) 是用于管理、track 和协作处理多个 documents versions 的工具。它是 [GitHub](https://github.com/) 和 [GitLab](https://about.gitlab.com/) 等广泛使用 platforms 的基础。

## Branches：project 的多个 copies <a href="#branches-multiple-copies-of-a-project" id="branches-multiple-copies-of-a-project"></a>

Git 使用 branches 在彼此旁边维护 document 的多个 copies。每个 branch 都有自己的 version。常见 pattern 是拥有 main branch，然后每个想 contribute to project 的人都在自己的 branch（copy）上工作。完成 work 后，他们的 branch 会 merge 回 main branch。

![Diagram](../.gitbook/assets/simple-git-branch.png)

## Local 和 remote：在你的机器和 Git provider 之间移动 work <a href="#local-and-remote-moving-work-between-your-machine-and-a-git-provider" id="local-and-remote-moving-work-between-your-machine-and-a-git-provider"></a>

使用 Git 时的常见 pattern 是在自己的 computer 上安装 Git，并使用 GitHub 等 Git provider 在 cloud 中处理 Git。实际上，你在 GitHub 上有一个 Git repository（project），并在 local machine 上处理它的 copies。

n8n 使用此 pattern 进行 source control：你会在 n8n instance 上处理 workflows，但会将它们发送到 Git provider 进行存储。

## Push、pull 和 commit <a href="#push-pull-and-commit" id="push-pull-and-commit"></a>

n8n 使用三个 key Git processes：

* **Push**：将 work 从 instance 发送到 Git。这会将 workflows 和 tags 的 copy，以及 credential 和 variable stubs 保存到 Git。你可以选择要保存的 workflows。
* **Pull**：从 Git 获取 workflows、tags 和 variables，并将其加载到 n8n。你需要填充 refreshed items 中包含的任何 credentials 或 variable stubs。<br>

    <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Pulling 会覆盖你的 work</strong></p><p>如果你在 n8n 中更改了 workflow，必须先将 changes push 到 Git，再执行 pull。Pull 时，如果更改未存储在 Git 中，会覆盖你已做的任何 changes。</p></div>

* **Commit**：n8n 中的 commit 是一次将 work push 到 Git 的行为。在 n8n 中，commit 和 push 同时发生。

有关 n8n 如何与 Git 交互的详细信息，请参考 [Push and pull](push-and-pull-changes.md)。

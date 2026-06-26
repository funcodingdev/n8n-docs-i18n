---
title: Copy work between environments
description: 如何将 changes 从一个 environment 带到另一个 environment。
contentType: howto
nodeTitle: Move work between environments
originalFilePath: source-control-environments/using/copy-work.md
originalUrl: 'https://docs.n8n.io/source-control-environments/using/copy-work'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/move-work-between-environments
layout:
  description:
    visible: false
---

# 在 environments 之间复制 work <a href="#copy-work-between-environments" id="copy-work-between-environments"></a>

将 work 从一个 n8n instance 发送到另一个 instance 的步骤，会根据你使用 single Git branch 还是 multiple branches 而不同。

## Single branch <a href="#single-branch" id="single-branch"></a>

如果你只有一个 Git branch，复制 work 的步骤为：

1. 从一个 instance 将 work push 到 Git branch。
1. 登录另一个 instance，从 Git pull work。你可以[自动化 pulls](#automatically-send-changes-to-n8n)。

## Multiple branches <a href="#multiple-branches" id="multiple-branches"></a>

如果你有多个 Git branches，需要在 Git provider 中 merge branches，才能在 environments 之间复制 work。你无法直接在 n8n 中的 environments 之间复制 work。

常见 pattern：

1. 在 development instance 中执行 work。
1. 将 work push 到 Git 中的 development branch。
1. 将 development branch merge 到 production branch。有关如何执行此操作，请参考你的 Git provider 文档：<br>
	* [GitHub: Creating a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
	* [GitLab: Creating merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
	* [Git: Basic branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)
1. 在 production n8n instance 中，pull changes。你可以[自动化 pulls](#automatically-send-changes-to-n8n)。

## 自动发送 changes 到 n8n <a href="#automatically-send-changes-to-n8n" id="automatically-send-changes-to-n8n"></a>

你可以使用 `/source-control/pull` API endpoint 自动化复制 work process 的部分环节。Merge changes 后调用 API：

```curl
curl --request POST \
	--location '<YOUR-INSTANCE-URL>/api/v1/source-control/pull' \
	--header 'Content-Type: application/json' \
	--header 'X-N8N-API-KEY: <YOUR-API-KEY>' \
	--data '{"force": true}'
```

这意味着你可以使用 GitHub Action 或 GitLab CI/CD，在 merge 时自动 pull changes 到 production instance。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/niFQjDjbGJDJTKB57Z1s/" %}

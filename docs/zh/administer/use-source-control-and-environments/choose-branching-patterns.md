---
title: Branch patterns
description: >-
  了解 source control 中 n8n instances 与 Git branches 之间可能存在的不同关系。
contentType: explanation
nodeTitle: Choose branching patterns
originalFilePath: source-control-environments/understand/patterns.md
originalUrl: 'https://docs.n8n.io/source-control-environments/understand/patterns'
url: >-
  https://docs.n8n.io/administer/use-source-control-and-environments/choose-branching-patterns
layout:
  description:
    visible: false
---

# Branch patterns <a href="#branch-patterns" id="branch-patterns"></a>

n8n instances 和 Git branches 之间的关系很灵活。你可以根据 needs 创建不同 setups。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/sVOSvjfqJPLqOGb1x77B/" %}

## 多个 instances，多个 branches <a href="#multiple-instances-multiple-branches" id="multiple-instances-multiple-branches"></a>

此 pattern 包含多个 n8n instances，每个 instance 都链接到自己的 branch。

你可以将此 pattern 用于 environments。例如，创建两个 n8n instances：development 和 production。将它们分别链接到自己的 branches。从 development instance push work 到其 branch，然后通过 pull request 将 work 移动到 production branch，再 pull 到 production instance。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/O5AqRfApNuiINXZOe5j1/" %}

![Diagram](../.gitbook/assets/vc-multi-multi.png)

## 多个 instances，一个 branch <a href="#multiple-instances-one-branch" id="multiple-instances-one-branch"></a>

如果你希望 everywhere 使用相同 workflows、tags 和 variables，但在不同 n8n instances 中使用它们，可以使用此 pattern。

你可以将此 pattern 用于 environments。例如，创建两个 n8n instances：development 和 production。将它们都链接到同一个 branch。从 development push work，并将其 pull 到 production。

测试 n8n new version 时，此 pattern 也很有用：你可以创建一个使用 new version 的 new n8n instance，将其连接到 Git branch 并测试，而 production instance 保持在 older version，直到你确信可以安全 upgrade。

{% include "https://app.gitbook.com/s/GixZThfitWP21x2gQFpD/~/reusable/Vo4DpZeEyTa0iuufMDB8/" %}

![Diagram](../.gitbook/assets/vc-multi-one.png)

## 一个 instance，多个 branches <a href="#one-instance-multiple-branches" id="one-instance-multiple-branches"></a>

Instance owner 可以更改连接到 instance 的 Git branch。在这种情况下，完整 setup 很可能是 [多个 instances，多个 branches](#multiple-instances-multiple-branches) pattern，只是其中一个 instance 在 branches 之间切换。

这对 review work 很有用。例如，不同 users 可以在自己的 instance 上工作并 push 到自己的 branch。Reviewer 可以在 review instance 中工作，并在 branches 之间切换，以 load 不同 users 的 work。

{% hint style="info" %}
**No cleanup**

n8n 在更改 branches 时不会清理 instance 中的 existing contents。在此 pattern 中切换 branches 会导致每个 branch 的所有 workflows 都出现在你的 instance 中。
{% endhint %}
![Diagram](../.gitbook/assets/vc-one-multi.png)

## 一个 instance，一个 branch <a href="#one-instance-one-branch" id="one-instance-one-branch"></a>

这是最简单的 pattern。

![Diagram](../.gitbook/assets/vc-one-one.png)
